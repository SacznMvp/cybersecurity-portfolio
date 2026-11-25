"""Offline triage of Apache Common/Combined access logs; standard library only."""

import argparse
import csv
import ipaddress
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

# Quoted fields may contain Apache-style escaped characters.
QUOTED = r'"(?:[^"\\]|\\.)*"'
LINE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<request>(?:[^"\\]|\\.)*)" '
    r'(?P<status>[1-5]\d{2}) (?P<bytes>\d+|-)'
    rf'(?: {QUOTED} {QUOTED})?$'
)
REQUEST = re.compile(r'^(?P<method>[A-Z]+) (?P<target>\S+) HTTP/\d+(?:\.\d+)?$')
TIME = re.compile(
    r'^(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) ([+-])(\d{2})(\d{2})$'
)
MONTHS = {m: i for i, m in enumerate(
    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'), 1)}


def valid_time(value):
    match = TIME.fullmatch(value)
    if not match:
        return False
    day, month, year, hour, minute, second, _, offset_hour, offset_minute = match.groups()
    try:
        datetime(int(year), MONTHS[month], int(day), int(hour), int(minute), int(second))
        return int(offset_hour) <= 23 and int(offset_minute) <= 59
    except (ValueError, KeyError):
        return False


def parse_line(line):
    match = LINE.fullmatch(line.rstrip('\r\n'))
    if not match or not valid_time(match['time']):
        return None
    try:
        ip = str(ipaddress.ip_address(match['ip']))
    except ValueError:
        return None
    request = REQUEST.fullmatch(match['request'])
    # Apache may use '-' when no valid request was received (e.g. HTTP 408).
    if match['request'] == '-':
        path = '(sin solicitud)'
    elif request:
        target = request['target']
        if target == '*':
            path = '*'
        elif target.startswith('/'):
            # Preserve //paths instead of treating them as network locations.
            path = target.split('?', 1)[0].split('#', 1)[0]
        elif target.startswith(('http://', 'https://')):
            try:
                path = urlsplit(target).path or '/'
            except ValueError:
                return None
        else:
            return None
    else:
        return None
    return {'ip': ip, 'path': path, 'status': int(match['status']),
            'bytes': None if match['bytes'] == '-' else int(match['bytes'])}


def summarize(lines, threshold=10):
    if threshold < 1:
        raise ValueError('threshold must be positive')
    statuses, paths, clients, errors = Counter(), Counter(), Counter(), Counter()
    total = valid = transferred = unknown_bytes = 0
    for line in lines:
        total += 1
        row = parse_line(line)
        if row is None:
            continue
        valid += 1
        statuses[str(row['status'])] += 1
        paths[row['path']] += 1
        clients[row['ip']] += 1
        if row['status'] >= 400:
            errors[row['ip']] += 1
        if row['bytes'] is None:
            unknown_bytes += 1
        else:
            transferred += row['bytes']
    ordered = lambda counter: dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))
    return {
        'schema_version': 1, 'total_lines': total, 'valid_lines': valid,
        'invalid_lines': total-valid, 'bytes_known': transferred,
        'requests_with_unknown_bytes': unknown_bytes,
        'status_counts': dict(sorted(statuses.items())),
        'top_paths': dict(list(ordered(paths).items())[:10]),
        'client_counts': ordered(clients),
        'triage': [{'client': ip, 'http_errors': count, 'requests': clients[ip],
                    'reason': 'Umbral de respuestas 4xx/5xx en el archivo completo'}
                   for ip, count in ordered(errors).items() if count >= threshold],
        'error_threshold': threshold,
        'limitations': [
            'Indicadores para revisión, no confirmación de ataques.',
            'Sin ventana temporal, correlación entre fuentes ni contenido de solicitudes POST.',
            'La IP puede corresponder a un proxy, NAT o monitorización legítima.',
            'Se omiten query strings; las rutas e IP aún pueden contener datos sensibles.',
        ],
    }


def write_csv(report, stream):
    writer = csv.writer(stream)
    writer.writerow(['client', 'http_errors', 'requests', 'reason'])
    for item in report['triage']:
        writer.writerow([item['client'], item['http_errors'], item['requests'], item['reason']])


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('debe ser mayor que cero')
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Archivo Common o Combined, UTF-8')
    parser.add_argument('--threshold', type=positive, default=10)
    parser.add_argument('--format', choices=['json', 'csv'], default='json')
    parser.add_argument('--output', type=Path, help='Archivo nuevo; no se sobrescribe')
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding='utf-8', errors='replace') as source:
            report = summarize(source, args.threshold)
        if not report['valid_lines']:
            parser.error('No se encontraron líneas válidas; comprueba el formato del log.')
        def emit(stream):
            if args.format == 'json':
                json.dump(report, stream, ensure_ascii=False, indent=2)
                stream.write('\n')
            else:
                write_csv(report, stream)
        if args.output:
            with args.output.open('x', encoding='utf-8', newline='') as stream:
                emit(stream)
        else:
            emit(sys.stdout)
        print(f"Válidas: {report['valid_lines']}; rechazadas: {report['invalid_lines']}", file=sys.stderr)
    except OSError as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
