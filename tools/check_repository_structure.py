#!/usr/bin/env python3
"""Check canonical navigation and, optionally, preservation against a migration baseline."""
import argparse
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    '00-start-here', '01-Beginner-to-Advanced', '02-Labs', '03-Projects',
    '04-command-reference', '05-troubleshooting-and-recovery', '06-system-administration',
    '07-linux-distributions', '08-resources-and-reference', '09-desktop-and-workstation-linux',
    '10-automation-and-reproducibility', '11-containers-and-isolation',
    '12-security-and-software-trust', '13-performance-and-observability',
    '14-image-based-and-declarative-linux', '15-linux-internals-and-development',
]
PROTECTED = EXPECTED[1:4]
APPROVED_LINKS = {'02-Labs/README.md', '03-Projects/README.md', '03-Projects/01. Junior/README.md'}
OLD = ['00-Start-Here', '04-commands-and-cheat-sheets', '06-production-administration', '09-cheat-sheets']


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def exact_exists(path):
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return False
    current = ROOT
    for part in parts:
        if not current.is_dir() or part not in {p.name for p in current.iterdir()}:
            return False
        current = current / part
    return True


def tree(baseline, paths):
    data = subprocess.run(['git', 'ls-tree', '-rz', baseline, '--', *paths], cwd=ROOT,
                          check=True, capture_output=True).stdout
    result = {}
    for entry in data.split(b'\0'):
        if not entry:
            continue
        metadata, name = entry.split(b'\t', 1)
        mode, kind, sha = metadata.decode().split()
        require(kind == 'blob', 'Unexpected non-file entry in preservation scope')
        result[name.decode()] = (mode, sha)
    return result


def blob_hash(path):
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def check_preservation(baseline):
    entries = tree(baseline, PROTECTED)
    require(bool(entries), 'Baseline contains no protected collection files')
    current_names = {p.relative_to(ROOT).as_posix() for name in PROTECTED for p in (ROOT / name).rglob('*')
                     if p.is_file() and p.name != '.DS_Store'}
    require(current_names == set(entries), 'Files were added or removed inside folders 1–3')
    for name, (mode, sha) in entries.items():
        path = ROOT / name
        require(mode in {'100644', '100755'}, f'Review unexpected file mode: {name}')
        if name in APPROVED_LINKS:
            original = subprocess.run(['git', 'show', f'{baseline}:{name}'], cwd=ROOT,
                                      check=True, capture_output=True).stdout
            require(original.count(b'00-Start-Here') == 1, f'Baseline link count changed: {name}')
            require(path.read_bytes() == original.replace(b'00-Start-Here', b'00-start-here'),
                    f'Change beyond the one approved link: {name}')
        else:
            require(blob_hash(path) == sha, f'Protected content changed: {name}')
        require(bool(path.stat().st_mode & 0o111) == (mode == '100755'), f'Executable mode changed: {name}')
    sheets = tree(baseline, ['09-cheat-sheets'])
    require(len(sheets) == 70, 'Expected 70 sheets in the migration baseline')
    for name, (_mode, sha) in sheets.items():
        destination = ROOT / name.replace('09-cheat-sheets/', '04-command-reference/cheat-sheets/', 1)
        require(destination.is_file() and blob_hash(destination) == sha, f'Moved sheet contents differ: {name}')
    print(f'PASS preservation: {len(entries)} files in folders 1–3, only three approved link edits; 70 moved sheets byte-identical')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', help='Explicit pre-migration commit for preservation checks')
    args = parser.parse_args()
    names = {p.name for p in ROOT.iterdir() if p.is_dir()}
    require(set(EXPECTED) <= names, 'Missing canonical collection directory')
    require(not set(OLD) & names, 'Old top-level collection directory remains')
    numbered = {name for name in names if re.match(r'^\d\d-', name)}
    require(numbered == set(EXPECTED), 'Unexpected or duplicate numbered collection')
    for folder in EXPECTED[10:]:
        require('**Status: planned.**' in (ROOT / folder / 'README.md').read_text(), f'Missing planned label: {folder}')
    sheets = sorted((ROOT / '04-command-reference/cheat-sheets').glob('*.md'))
    require(len(sheets) == 70, 'Expected one collection of 70 cheat sheets')
    index = (ROOT / '04-command-reference/cheat-sheet-index.md').read_text()
    require(all(f'cheat-sheets/{path.name}' in index for path in sheets), 'Missing sheet-index entry')
    navigation = [ROOT / 'README.md', ROOT / 'docs/repository-structure.md', ROOT / '08-resources-and-reference/README.md']
    navigation += list((ROOT / '00-start-here').glob('*.md'))
    navigation += [ROOT / path / 'README.md' for path in EXPECTED[9:]]
    navigation += [ROOT / name for name in APPROVED_LINKS]
    count = 0
    for path in navigation:
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            # Only the approved Start Here targets are in scope inside folders 1–3.
            # Their other existing links are deliberately not repaired by this migration.
            if path.relative_to(ROOT).as_posix() in APPROVED_LINKS and '00-start-here' not in unquote(parsed.path).split('/'):
                continue
            destination = Path(os.path.normpath(path.parent / unquote(parsed.path))) if parsed.path else path
            require(exact_exists(destination), f'Missing/case-mismatched navigation target in {path.name}: {target}')
            count += 1
    if args.baseline:
        check_preservation(args.baseline)
    print(f'PASS structure: 16 canonical collections, six scope roadmaps, 70 indexed sheets and {count} navigation links')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
