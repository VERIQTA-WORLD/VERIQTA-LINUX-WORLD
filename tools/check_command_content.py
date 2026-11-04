#!/usr/bin/env python3
"""Check authored guides, structural navigation and Bash syntax without executing examples."""
from pathlib import Path
import os
import ast
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / '04-command-reference'
RECOVERY = ROOT / '05-troubleshooting-and-recovery'
ADMINISTRATION = ROOT / '06-system-administration'
DISTRIBUTIONS = ROOT / '07-linux-distributions'
DISTRIBUTION_REQUIRED = (
    '## Scope and environment',
    '## What changes in practice',
    '## Follow-along lab',
    '## Verification and limits',
    '## Cleanup',
    '## References',
)
ADMIN_REQUIRED = (
    '## Environment and permissions',
    '## Before you begin',
    '## Operating procedure',
    '## Follow-along lab',
    '## Verification and rollback',
    '## Cleanup',
    '## References',
)
RECOVERY_REQUIRED = (
    '## Environment and permissions',
    '## Evidence and interpretation',
    '## Follow-along lab',
    '## Recovery and verification',
    '## Cleanup',
    '## References',
)
REQUIRED = (
    '## Environment and permissions',
    '## Quick reference',
    '## Follow along',
    '## Expected results and verification',
    '## Common mistakes and next checks',
    '## Authoritative references',
)


def exact_exists(path):
    """Check spelling component by component even on case-insensitive macOS."""
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return False
    current = ROOT
    for part in relative.parts:
        if not current.is_dir() or part not in {p.name for p in current.iterdir()}:
            return False
        current = current / part
    return True


def check():
    errors = []
    navigation = sorted((ROOT / '00-start-here').glob('*.md')) + [ROOT / '08-resources-and-reference/README.md', ROOT / 'docs/repository-structure.md', ROOT / 'docs/structure-migration-validation.md']
    navigation += [p / 'README.md' for p in ROOT.iterdir() if p.is_dir() and p.name[:2] in {'09', '10', '11', '12', '13', '14', '15'}]
    files = navigation + sorted(COLLECTION.rglob('*.md')) + sorted(RECOVERY.glob('*.md')) + sorted(ADMINISTRATION.glob('*.md')) + sorted(DISTRIBUTIONS.glob('*.md')) + [ROOT / 'README.md', ROOT / 'docs/folders-04-08-assessment.md', ROOT / 'CONTRIBUTING.md', ROOT / 'NOTICE.md', ROOT / 'LICENSE.md']
    references = [p for p in COLLECTION.glob('*/*.md') if p.name != 'README.md' and p.parent.name != 'cheat-sheets']
    recovery_guides = [p for p in RECOVERY.glob('*.md') if p.name not in {'README.md', 'VALIDATION.md'}]
    contracts = {p: REQUIRED for p in references}
    contracts.update({p: RECOVERY_REQUIRED for p in recovery_guides})
    admin_guides = [p for p in ADMINISTRATION.glob('*.md') if p.name not in {'README.md', 'VALIDATION.md'}]
    contracts.update({p: ADMIN_REQUIRED for p in admin_guides})
    distribution_guides = [p for p in DISTRIBUTIONS.glob('*.md') if p.name not in {'README.md', 'VALIDATION.md'}]
    contracts.update({p: DISTRIBUTION_REQUIRED for p in distribution_guides})
    blocks = 0
    links = 0
    for path in files:
        text = path.read_text()
        label = str(path.relative_to(ROOT))
        if not text.strip():
            errors.append(f'{label}: empty page')
        if path in contracts:
            for heading in contracts[path]:
                if heading not in text:
                    errors.append(f'{label}: missing {heading}')
            if not re.search(r'\[[^\]]+\]\(https://', text):
                errors.append(f'{label}: no upstream reference')
        fences = re.findall(r'^```[^\n]*$', text, flags=re.M)
        if len(fences) % 2:
            errors.append(f'{label}: unbalanced code fences')
        for code in re.findall(r'^```bash\n(.*?)^```', text, flags=re.M | re.S):
            blocks += 1
            for embedded in re.findall(r"<<'PY'\n(.*?)^PY$", code, flags=re.M | re.S):
                try:
                    ast.parse(embedded)
                except SyntaxError as error:
                    errors.append(f'{label}: embedded Python syntax: {error}')
            result = subprocess.run(['bash', '-n'], input=code, text=True, capture_output=True)
            if result.returncode:
                errors.append(f'{label}: Bash syntax: {result.stderr.strip()}')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            relative = unquote(parsed.path)
            destination = Path(os.path.normpath(path.parent / relative)) if relative else path
            links += 1
            if not exact_exists(destination):
                errors.append(f'{label}: missing or case-mismatched link {target}')
            elif parsed.fragment and destination.is_file() and destination.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', destination.read_text(), flags=re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(parsed.fragment) not in slugs:
                    errors.append(f'{label}: missing heading anchor {target}')
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith('|'):
                # Pipes inside inline code must be escaped to survive GitHub tables.
                for inline in re.findall(r'`([^`]+)`', line):
                    if re.search(r'(?<!\\)\|', inline):
                        errors.append(f'{label}:{line_number}: unescaped pipe in table code')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(files)} pages, {len(contracts)} content contracts, {blocks} Bash blocks, {links} local links.')
    print('Syntax and structure only: no Linux command execution or external URL availability is claimed.')
    return 0


if __name__ == '__main__':
    sys.exit(check())
