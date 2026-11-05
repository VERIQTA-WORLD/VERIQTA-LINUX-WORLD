#!/usr/bin/env python3
"""Run the ten published workstation CLI fixtures, not graphical/hardware tasks."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / '09-desktop-and-workstation-linux'
EXPECTED = {
    'installation-and-recovery.md': 2,
    'desktop-and-accessibility.md': 1,
    'applications-and-software-trust.md': 1,
    'displays-and-graphics.md': 1,
    'audio-video-and-screen-sharing.md': 1,
    'power-battery-and-suspend.md': 1,
    'peripherals-printing-and-removable-media.md': 1,
    'personal-backups-and-migration.md': 3,
    'developer-workstation.md': 3,
    'desktop-troubleshooting-and-recovery.md': 2,
}


def extract(text, name):
    blocks = re.findall(r'<!-- workstation:' + name + r' -->\s*```bash\n(.*?)^```',
                        text, flags=re.M | re.S)
    if len(blocks) != 1:
        raise ValueError(f'expected exactly one {name} block')
    return blocks[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='New private JSON file outside the repository')
    args = parser.parse_args()
    if platform.system() != 'Linux' or os.geteuid() == 0:
        parser.error('run on Linux as an ordinary account, not root')
    if args.report:
        report_path = args.report.resolve()
        if report_path == ROOT or ROOT in report_path.parents:
            parser.error('retain machine-specific reports outside the repository')
        if report_path.exists():
            parser.error('report already exists')
    evidence = {'platform': platform.platform(),
                'os_release': Path('/etc/os-release').read_text(), 'examples': {}}
    failures = []
    for name, markers in EXPECTED.items():
        source = (COLLECTION / name).read_text()
        with tempfile.TemporaryDirectory(prefix='linux-world-workstation-') as parent:
            script = "rm() { (set +o pipefail; printf 'y\\n%.0s' {1..32} | command rm \"$@\"); }\n"
            script += extract(source, 'exercise') + '\n' + extract(source, 'cleanup')
            try:
                result = subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', script],
                                        cwd=ROOT, env=dict(os.environ, TMPDIR=parent, LC_ALL='C'),
                                        text=True, capture_output=True, timeout=90)
                remaining = [str(p.relative_to(parent)) for p in Path(parent).rglob('*')]
                passed = result.returncode == 0 and not remaining
                passed = passed and len(re.findall(r'^PASS:', result.stdout, flags=re.M)) >= markers
                evidence['examples'][name] = {'status': result.returncode, 'stdout': result.stdout,
                    'stderr': result.stderr, 'remaining_fixture_paths': remaining,
                    'source_sha256': hashlib.sha256(source.encode()).hexdigest()}
            except (OSError, subprocess.TimeoutExpired) as error:
                passed = False
                evidence['examples'][name] = {'error': str(error)}
            print(('PASS' if passed else 'FAIL') + ': ' + name)
            if not passed:
                failures.append(name)
                print(evidence['examples'][name])
    evidence['failures'] = failures
    if args.report:
        fd = os.open(report_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as handle:
            json.dump(evidence, handle, indent=2)
            handle.write('\n')
    print('CLI fixtures only: no graphical interaction, physical-device use, installation or suspend is validated.')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
