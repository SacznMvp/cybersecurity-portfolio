import hashlib
import json
import os
import tarfile
import tempfile
import unittest
from pathlib import Path

from backup import create_backup


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config, self.web = self.root/'config', self.root/'web'
        self.config.mkdir()
        self.web.mkdir()
        (self.config/'site.conf').write_bytes(b'ServerName lab.test\n')
        (self.web/'index.html').write_bytes(b'<h1>Lab</h1>\n')
        self.output = self.root/'backup.tar.gz'

    def test_archive_manifest_and_file_contents(self):
        create_backup(self.config, self.web, self.output)
        with tarfile.open(self.output) as archive:
            manifest = json.load(archive.extractfile('manifest.json'))
            for item in manifest['entries']:
                if item['type'] == 'file':
                    content = archive.extractfile(item['path']).read()
                    self.assertEqual(hashlib.sha256(content).hexdigest(), item['sha256'])
            self.assertEqual(archive.extractfile('web/index.html').read(), b'<h1>Lab</h1>\n')

    def test_no_overwrite(self):
        self.output.write_text('original')
        with self.assertRaises(FileExistsError):
            create_backup(self.config, self.web, self.output)
        self.assertEqual(self.output.read_text(), 'original')

    def test_restore_generated_archive_to_empty_staging(self):
        if not hasattr(tarfile, 'data_filter'):
            self.skipTest('Requires a Python release with tarfile data filter')
        create_backup(self.config, self.web, self.output)
        staging = self.root/'staging'
        staging.mkdir()
        with tarfile.open(self.output) as archive:
            archive.extractall(staging, filter='data')
        self.assertEqual((staging/'config/site.conf').read_bytes(), (self.config/'site.conf').read_bytes())
        self.assertEqual((staging/'web/index.html').read_bytes(), (self.web/'index.html').read_bytes())

    def test_output_cannot_be_inside_source(self):
        with self.assertRaises(ValueError):
            create_backup(self.config, self.web, self.web/'backup.tar.gz')

    def test_missing_and_nested_sources(self):
        with self.assertRaises(ValueError):
            create_backup(self.root/'missing', self.web, self.output)
        with self.assertRaises(ValueError):
            create_backup(self.root, self.web, self.output)

    def make_link(self, path, target):
        try:
            path.symlink_to(target)
        except OSError as error:
            self.skipTest(f'Symlinks not permitted on this host: {error}')

    def test_internal_symlink_preserved(self):
        self.make_link(self.config/'enabled.conf', 'site.conf')
        create_backup(self.config, self.web, self.output)
        with tarfile.open(self.output) as archive:
            entry = archive.getmember('config/enabled.conf')
            self.assertTrue(entry.issym())
            self.assertEqual(entry.linkname, 'site.conf')

    def test_external_symlink_rejected(self):
        self.make_link(self.config/'external', '../web/index.html')
        with self.assertRaises(ValueError):
            create_backup(self.config, self.web, self.output)
        self.assertFalse(self.output.exists())


if __name__ == '__main__':
    unittest.main()
