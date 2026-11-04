#!/usr/bin/env python3
"""Check JUN-071–083 and optionally execute their bounded published exercises.

Never executes unmarked host observations, systemd commands, mounts, sudo or remote SSH.
The default run includes loopback listeners; use --static-only or --skip-loopback as needed.
"""
import argparse
import ast
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit

from check_command_content import exact_exists

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '02-Labs/Junior/05-Logs-Monitoring-and-Troubleshooting'
REQUIRED_TAGS = {'setup', 'fixtures', 'implementation', 'tests', 'run-tests', 'final-checks'}


def heading_anchors(text):
    fenced = False
    used = {}
    result = set()
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        elif not fenced and re.match(r'^#{1,6}\s+', line):
            title = re.sub(r'^#{1,6}\s+', '', line)
            slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
            count = used.get(slug, 0)
            result.add(slug + ('-' + str(count) if count else ''))
            used[slug] = count + 1
    return result


def static_check(files):
    links = blocks = embedded = 0
    cache = {}
    for path in files:
        text = path.read_text()
        label = str(path.relative_to(ROOT))
        if not text.strip():
            raise AssertionError(label + ': empty page')
        if len(re.findall(r'^```[^\n]*$', text, re.M)) % 2:
            raise AssertionError(label + ': unbalanced fences')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            destination = Path(os.path.normpath(path.parent / unquote(parsed.path))) if parsed.path else path
            if not exact_exists(destination):
                raise AssertionError(label + ': missing/case-mismatched link ' + target)
            if parsed.fragment and destination.suffix == '.md':
                if destination not in cache:
                    cache[destination] = heading_anchors(destination.read_text())
                if unquote(parsed.fragment) not in cache[destination]:
                    raise AssertionError(label + ': missing anchor ' + target)
        for code in re.findall(r'^```bash\n(.*?)^```', text, re.M | re.S):
            blocks += 1
            result = subprocess.run(['bash', '-n'], input=code, text=True, capture_output=True)
            if result.returncode:
                raise AssertionError(label + ': Bash syntax: ' + result.stderr)
            for source in re.findall(r"<<'PY'\n(.*?)^PY$", code, re.M | re.S):
                ast.parse(source, filename=label)
                embedded += 1
    return links, blocks, embedded


def execute(path, skip_loopback):
    tagged = re.findall(r'<!-- lab:([\w-]+) -->\n```bash\n(.*?)\n```', path.read_text(), re.S)
    names = [tag for tag, _ in tagged]
    if not REQUIRED_TAGS <= set(names) or len(names) != len(set(names)):
        raise AssertionError(path.name + ': missing or duplicate execution tags')
    chosen = []
    for tag, code in tagged:
        if tag in REQUIRED_TAGS or tag.startswith('exercise-'):
            if skip_loopback and tag == 'exercise-083-run':
                print('SKIP JUN-083 live loopback exercise; fixture tests still run')
                continue
            chosen.append(code)
    # The marked snippets are reviewed repository code, not a general sandbox.
    # Only HOME is replaced, keeping all workspaces under this private temp root.
    with tempfile.TemporaryDirectory(prefix='linux-world-jun-') as folder:
        env = os.environ.copy()
        env['HOME'] = folder
        script = 'set -eu\n' + '\n'.join(chosen)
        result = subprocess.run(['bash'], input=script, text=True, capture_output=True,
                                env=env, cwd=folder, timeout=55)
        if result.returncode:
            raise AssertionError(path.name + ': execution failed\n' + result.stdout + result.stderr)
        counts = re.findall(r'PASS: (\d+) assertions', result.stdout)
        if len(counts) != 2 or counts[0] != counts[1]:
            raise AssertionError(path.name + ': regression/final-check results missing or inconsistent')
        # Let TemporaryDirectory remove only this run's exact private tree.
        workspace = list((Path(folder) / 'veriqta-linux-labs').glob('JUN-*'))
        if len(workspace) != 1:
            raise AssertionError(path.name + ': unexpected workspace inventory')
        print('PASS ' + path.name + ': published setup, exercise, implementation and ' + counts[0]
              + ' regression assertions; final rerun and private cleanup')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--static-only', action='store_true')
    parser.add_argument('--skip-loopback', action='store_true')
    parser.add_argument('--lab', type=int, choices=range(71, 84))
    parser.add_argument('--preserved-baseline', help='optional git ref for byte-preservation of JUN-069/070')
    args = parser.parse_args()
    guides = sorted(p for p in BASE.glob('*.md') if re.match(r'\d{2}\. JUN-0(?:7[1-9]|8[0-3]) ', p.name))
    if [int(p.name[:2]) for p in guides] != list(range(71, 84)):
        raise AssertionError('expected exactly JUN-071 through JUN-083')
    selected = [p for p in guides if not args.lab or int(p.name[:2]) == args.lab]
    for path in selected:
        tags = re.findall(r'<!-- lab:([\w-]+) -->', path.read_text())
        if not REQUIRED_TAGS <= set(tags):
            raise AssertionError(path.name + ': missing runnable project sections')
        for section in ('Welcome', 'prerequisites', 'Safety', 'regression', 'controlled failures',
                        'Knowledge assessment', 'cleanup', 'Completion checklist'):
            if section.lower() not in path.read_text().lower():
                raise AssertionError(path.name + ': missing ' + section)
    navigation = [BASE / 'README.md', ROOT / '02-Labs/Junior/README.md', ROOT / '02-Labs/README.md']
    navigation += [ROOT / '02-Labs' / name for name in
                   ('LAB-ENVIRONMENT.md', 'LAB-SAFETY.md', 'LAB-STANDARD.md', 'PROGRESS-TRACKER.md')]
    links, blocks, embedded = static_check(selected + navigation)
    junior = ROOT / '02-Labs/Junior/README.md'
    ids = [int(x) for x in re.findall(r'^\| JUN-(\d{3}) \|', junior.read_text(), re.M)]
    if ids != list(range(1, 84)):
        raise AssertionError('Junior index must link each of 83 labs once, in order')
    if args.preserved_baseline:
        for number in (69, 70):
            path = next(p for p in BASE.glob(str(number) + '.*.md'))
            relative = str(path.relative_to(ROOT))
            original = subprocess.check_output(['git', 'show', args.preserved_baseline + ':' + relative], cwd=ROOT)
            if hashlib.sha256(original).digest() != hashlib.sha256(path.read_bytes()).digest():
                raise AssertionError(path.name + ': differs from preserved baseline')
        print('PASS: JUN-069 and JUN-070 byte-identical to ' + args.preserved_baseline)
    print(f'PASS static: {len(selected)} new labs, {links} local links/anchors, {blocks} Bash blocks, {embedded} Python heredocs')
    if not args.static_only:
        for path in selected:
            execute(path, args.skip_loopback)
    print('No Linux host, manager, mount, policy, external DNS or remote SSH behavior is certified by these checks.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (AssertionError, OSError, SyntaxError, subprocess.SubprocessError) as error:
        print('FAIL: ' + str(error), file=sys.stderr)
        sys.exit(1)
