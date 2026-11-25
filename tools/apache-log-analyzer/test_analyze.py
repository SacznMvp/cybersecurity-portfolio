import csv
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from analyze import parse_line, summarize, write_csv

HERE = Path(__file__).parent


class AnalyzerTests(unittest.TestCase):
    def test_known_fixture_and_invalid_count(self):
        report = summarize((HERE/'sample.log').read_text().splitlines(), 3)
        self.assertEqual((report['valid_lines'], report['invalid_lines']), (6, 1))
        self.assertEqual(report['bytes_known'], 1088)
        self.assertEqual(report['requests_with_unknown_bytes'], 1)
        self.assertEqual(report['triage'][0]['client'], '192.0.2.20')
        self.assertEqual(report['triage'][0]['http_errors'], 3)
        self.assertIn('/search', report['top_paths'])
        self.assertNotIn('synthetic', json.dumps(report))

    def test_ipv6_and_escaped_user_agent(self):
        row = parse_line('2001:db8::1 - - [24/Nov/2026:10:00:00 +0000] "GET / HTTP/2.0" 200 12 "-" "A\\"B"')
        self.assertEqual(row['ip'], '2001:db8::1')

    def test_bad_fields_are_rejected(self):
        base = '192.0.2.1 - - [24/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 1'
        for bad in [base.replace('192.0.2.1', '999.0.0.1'), base.replace('24/Nov', '31/Nov'),
                    base.replace('200 1', '999 1'), base+' junk', base.replace('+0000', '+9999')]:
            self.assertIsNone(parse_line(bad))

    def test_missing_request_and_double_slash(self):
        base = '192.0.2.1 - - [24/Nov/2026:10:00:00 +0000] '
        self.assertEqual(parse_line(base+'"-" 408 -')['path'], '(sin solicitud)')
        self.assertEqual(parse_line(base+'"GET //admin?a=b HTTP/1.1" 404 0')['path'], '//admin')

    def test_csv_is_parseable(self):
        stream = io.StringIO()
        write_csv(summarize((HERE/'sample.log').read_text().splitlines(), 3), stream)
        records = list(csv.DictReader(io.StringIO(stream.getvalue())))
        self.assertEqual(records[0]['http_errors'], '3')

    def test_cli_outputs_and_prevents_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)/'report.json'
            command = [sys.executable, str(HERE/'analyze.py'), str(HERE/'sample.log'), '--threshold', '3', '--output', str(target)]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            original = target.read_bytes()
            self.assertEqual(json.loads(original)['valid_lines'], 6)
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            self.assertEqual(target.read_bytes(), original)

    def test_cli_rejects_empty_input_and_invalid_threshold(self):
        with tempfile.TemporaryDirectory() as temp:
            empty = Path(temp)/'empty.log'
            empty.write_text('garbage\n')
            for args in [[str(empty)], [str(HERE/'sample.log'), '--threshold', '0']]:
                self.assertNotEqual(subprocess.run([sys.executable, str(HERE/'analyze.py'), *args], capture_output=True).returncode, 0)


if __name__ == '__main__':
    unittest.main()
