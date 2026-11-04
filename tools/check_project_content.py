#!/usr/bin/env python3
"""Check project navigation, lifecycle sections and shell syntax without running labs."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import re
import subprocess
import sys

from check_command_content import exact_exists

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '03-Projects'
LEVELS = ('01. Junior', '02. Mid-Level', '03. Senior')


def headings(text):
    """Read actual headings, excluding configuration/scripts inside fenced blocks."""
    result = []
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        elif not fenced:
            match = re.match(r'^#{1,6}\s+(.+)$', line)
            if match:
                result.append(match.group(1))
    return result


def anchors(text):
    used = {}
    result = set()
    for heading in headings(text):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = used.get(slug, 0)
        result.add(f'{slug}-{count}' if count else slug)
        used[slug] = count + 1
    return result


def check():
    errors = []
    guides = []
    for level in LEVELS:
        files = sorted(p for p in (BASE / level).glob('*.md') if p.name != 'README.md')
        if len(files) != 10 or [p.name[:2] for p in files] != [f'{n:02d}' for n in range(1, 11)]:
            errors.append(f'{level}: expected ten numbered project guides')
        guides.extend(files)
    files = [BASE / 'README.md', BASE / 'project-workflow.md']
    files += [BASE / level / 'README.md' for level in LEVELS] + guides
    link_count = block_count = 0
    anchor_cache = {}
    for path in files:
        label = str(path.relative_to(ROOT))
        if not path.is_file():
            errors.append(f'{label}: missing page')
            continue
        text = path.read_text()
        if not text.strip():
            errors.append(f'{label}: empty page')
        if len(re.findall(r'^```[^\n]*$', text, re.M)) % 2:
            errors.append(f'{label}: unbalanced fences')
        if path in guides:
            hs = headings(text)
            for name in ('05. Prerequisites', '10. Environment Setup', '12. Step-by-Step Implementation',
                         '16. Testing', '17. Failure Simulation'):
                if name not in hs:
                    errors.append(f'{label}: missing {name}')
            # Check full numbered sections, including subheadings, not just their opening sentence.
            sections = re.split(r'^# (\d{2}\. [^\n]+)\n', text, flags=re.M)
            pairs = list(zip(sections[1::2], sections[2::2]))
            for kind in ('Prerequisites', 'Environment Setup', 'Step-by-Step Implementation',
                         'Testing', 'Failure Simulation', 'Cleanup', 'Cleanup Verification'):
                matches = [body for title, body in pairs if title.split('. ', 1)[1] == kind]
                if not matches or len(matches[0].strip()) < 100:
                    errors.append(f'{label}: missing/substantially empty {kind} section')
            if not any(h.startswith('18.') for h in hs):
                errors.append(f'{label}: missing diagnostic/recovery section')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            link_count += 1
            destination = Path(os.path.normpath(path.parent / unquote(parsed.path))) if parsed.path else path
            if not exact_exists(destination):
                errors.append(f'{label}: missing/case-mismatched destination {target}')
            elif parsed.fragment and destination.suffix == '.md':
                if destination not in anchor_cache:
                    anchor_cache[destination] = anchors(destination.read_text())
                if unquote(parsed.fragment) not in anchor_cache[destination]:
                    errors.append(f'{label}: missing anchor {target}')
        for code in re.findall(r'^```(?:bash|sh)\n(.*?)^```', text, re.M | re.S):
            block_count += 1
            result = subprocess.run(['bash', '-n'], input=code, text=True, capture_output=True)
            if result.returncode:
                errors.append(f'{label}: shell syntax: {result.stderr.strip()}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(guides)} projects, {len(files)} pages, {link_count} local links/anchors, {block_count} shell blocks.')
    print('Navigation, section coverage and syntax only; no project deployment or Linux runtime behavior is verified.')
    return 0


if __name__ == '__main__':
    sys.exit(check())
