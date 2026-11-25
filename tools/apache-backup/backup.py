"""Create a private Apache lab backup. Does not restore or reload services."""

import argparse
import hashlib
import json
import os
import tarfile
from datetime import datetime, timezone
from pathlib import Path


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def create_backup(config, web, output):
    sources = []
    for label, supplied in [('config', Path(config)), ('web', Path(web))]:
        if supplied.is_symlink() or not supplied.is_dir():
            raise ValueError(f'La fuente debe ser un directorio real: {supplied}')
        sources.append((label, supplied.resolve()))
    output = Path(output).absolute()
    if not output.parent.is_dir():
        raise ValueError('El directorio de destino debe existir')
    resolved_output = output.resolve()
    for _, source in sources:
        if resolved_output.is_relative_to(source):
            raise ValueError('El archivo de backup no puede estar dentro de una fuente')
    if sources[0][1].is_relative_to(sources[1][1]) or sources[1][1].is_relative_to(sources[0][1]):
        raise ValueError('Las fuentes deben ser directorios separados, sin anidación')

    entries = []
    # Walk without following directory symlinks; preserve safe internal links.
    for label, source in sources:
        paths = [source]
        for directory, dirs, files in os.walk(source, followlinks=False):
            paths.extend(Path(directory)/name for name in sorted(dirs + files))
        for path in paths:
            relative = Path(label) / path.relative_to(source)
            item = {'path': relative.as_posix()}
            if path.is_symlink():
                target = os.readlink(path)
                if os.path.isabs(target) or not path.resolve().is_relative_to(source) or not path.exists():
                    raise ValueError(f'Enlace externo, absoluto o roto no admitido: {path}')
                item.update(type='symlink', target=target)
            elif path.is_file():
                item.update(type='file', sha256=digest(path), bytes=path.stat().st_size)
            elif path.is_dir():
                item.update(type='directory')
            else:
                raise ValueError(f'Archivo especial no admitido: {path}')
            entries.append((path, item))

    # O_EXCL prevents overwriting existing files, including symlinks.
    descriptor = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            with tarfile.open(fileobj=stream, mode='w:gz', dereference=False) as archive:
                for path, item in entries:
                    archive.add(path, arcname=item['path'], recursive=False)
                payload = json.dumps({
                    'created_utc': datetime.now(timezone.utc).isoformat(),
                    'scope': 'Apache config and DocumentRoot; not a full server backup',
                    'entries': [item for _, item in entries],
                }, indent=2).encode('utf-8')
                import io
                info = tarfile.TarInfo('manifest.json')
                info.size = len(payload)
                info.mode = 0o600
                archive.addfile(info, io.BytesIO(payload))
    except BaseException:
        output.unlink(missing_ok=True)  # Only this newly created incomplete archive.
        raise
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path('/etc/apache2'))
    parser.add_argument('--web', type=Path, default=Path('/var/www/sacznweb'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        output = create_backup(args.config, args.web, args.output)
        print(f'Backup creado: {output}\nSHA-256: {digest(output)}')
    except (OSError, ValueError, tarfile.TarError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
