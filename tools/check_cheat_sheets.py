#!/usr/bin/env python3
"""Check the command-only collection without executing any listed command."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
folder = root / '09-cheat-sheets'
files = sorted(folder.glob('*.md'))
errors = []
lines = 0
if not files:
    errors.append('No cheat sheets found')
for path in files:
    text = path.read_text()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md', path.name):
        errors.append(f'{path.name}: filename must describe the task using lowercase words')
    match = re.fullmatch(r'```bash\n(.+\n)```\n', text, re.S)
    if not match:
        errors.append(f'{path.name}: expected one Bash block and no prose')
        continue
    body = match[1]
    for number, line in enumerate(body.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            errors.append(f'{path.name}:{number}: blank line or comment')
        if line.rstrip() != line:
            errors.append(f'{path.name}:{number}: trailing whitespace')
        result = subprocess.run(['bash', '-n'], input=line+'\n', text=True, capture_output=True)
        if result.returncode:
            errors.append(f'{path.name}:{number}: incomplete Bash command: {result.stderr.strip()}')
    result = subprocess.run(['bash', '-n'], input=body, text=True, capture_output=True)
    if result.returncode:
        errors.append(f'{path.name}: Bash syntax: {result.stderr.strip()}')
    lines += len(body.splitlines())
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} command-only sheets; {lines} command lines; each line and block passes Bash syntax checks.')
print('No examples executed. Optional tools, permissions and version-specific options require the matching Linux environment.')
