#!/usr/bin/env python3
"""Check two-column cheat sheets and command syntax without executing examples."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
folder = root / '09-cheat-sheets'
files = sorted(folder.glob('*.md'))
errors = []
commands = 0
if not files:
    errors.append('No cheat sheets found')
for path in files:
    lines = path.read_text().splitlines()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md', path.name):
        errors.append(f'{path.name}: filename must describe the task using lowercase words')
    if lines[:2] != ['| Command | What you can do with it |', '| --- | --- |']:
        errors.append(f'{path.name}: expected the two-column table header')
        continue
    if len(lines) < 3:
        errors.append(f'{path.name}: no command rows')
    for number, line in enumerate(lines[2:], 3):
        if line.rstrip() != line:
            errors.append(f'{path.name}:{number}: trailing whitespace')
        # GFM requires pipes to be escaped even inside table code spans.
        if len(re.findall(r'(?<!\\)\|', line)) != 3:
            errors.append(f'{path.name}:{number}: expected exactly two table columns')
            continue
        match = re.fullmatch(r'\| `(.+)` \| (.+) \|', line)
        if not match:
            errors.append(f'{path.name}:{number}: expected inline command and description')
            continue
        command, description = match.groups()
        command = command.replace(r'\|', '|')
        if '`' in command or not description.strip() or description.lstrip().startswith('#'):
            errors.append(f'{path.name}:{number}: invalid command or description')
        result = subprocess.run(['bash', '-n'], input=command+'\n', text=True, capture_output=True)
        if result.returncode:
            errors.append(f'{path.name}:{number}: Bash syntax: {result.stderr.strip()}')
        commands += 1
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} two-column sheets; {commands} commands with descriptions; Bash syntax and table separators checked.')
print('No examples executed. Optional tools, permissions and version-specific options require the matching Linux environment.')
