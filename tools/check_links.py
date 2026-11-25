"""Check local Markdown file/image links; does not crawl external URLs or anchors."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1]
errors = []
count = 0
for source in root.rglob('*.md'):
    if '.git' in source.parts:
        continue
    content = re.sub(r'```.*?```', '', source.read_text(encoding='utf-8'), flags=re.S)
    for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', content):
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        count += 1
        path = (source.parent/unquote(parsed.path)).resolve()
        if not path.is_relative_to(root) or not path.exists():
            errors.append(f'{source.relative_to(root)} -> {target}')
print(f'{count} local links checked; {len(errors)} broken')
for error in errors:
    print(error)
raise SystemExit(bool(errors))
