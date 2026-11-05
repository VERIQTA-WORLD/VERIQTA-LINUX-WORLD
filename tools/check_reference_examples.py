#!/usr/bin/env python3
"""Execute marked folder-8 examples and cleanup as an ordinary account.

No privileged changes or external network requests. Optional Linux observations
inspect only local command resolution, mounts, routing and journal metadata.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / '08-resources-and-reference'
EXPECTED = {
    'linux-glossary.md': 4,
    'linux-official-documentation.md': 1,
    'linux-filesystem-reference.md': 2,
    'linux-configuration-file-reference.md': 2,
    'linux-log-location-reference.md': 2,
    'linux-networking-reference.md': 2,
    'linux-books-and-learning-resources.md': 1,
    'linux-interview-preparation.md': 2,
}


def marked(text, name):
    blocks = re.findall(r'<!-- reference:' + name + r' -->\s*```bash\n(.*?)^```',
                        text, flags=re.M | re.S)
    if len(blocks) != 1:
        raise ValueError(f'expected one {name} block, found {len(blocks)}')
    return blocks[0]


def invoke(command, env):
    try:
        result = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as error:
        return {'command': command, 'status': 127 if isinstance(error, OSError) else 124,
                'stdout': '', 'stderr': str(error)}
    return {'command': command, 'status': result.returncode,
            'stdout': result.stdout, 'stderr': result.stderr}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--linux-observations', action='store_true')
    parser.add_argument('--report', type=Path, help='New private JSON evidence file; never overwritten')
    args = parser.parse_args()
    if os.geteuid() == 0:
        parser.error('use an ordinary account, not root')
    if args.linux_observations and platform.system() != 'Linux':
        parser.error('--linux-observations requires Linux')
    if args.report and args.report.exists():
        parser.error('report already exists')
    env = dict(os.environ, LC_ALL='C')
    if platform.system() == 'Darwin':
        # Bypass Apple's /usr/bin developer-tool shim, which writes xcrun_db
        # into TMPDIR; use the interpreter already executing this checker.
        env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env.get('PATH', '')
    record = {'platform': platform.platform(), 'pages': {}, 'observations': []}
    failures = []
    for name, minimum in EXPECTED.items():
        text = (PAGES / name).read_text()
        exercise, cleanup = marked(text, 'exercise'), marked(text, 'cleanup')
        with tempfile.TemporaryDirectory(prefix='linux-world-reference-') as parent:
            private_env = dict(env, TMPDIR=parent)
            # Each rm call gets its own confirmation input: BSD rm may read ahead.
            # The wrapper supplies answers only inside this isolated execution.
            wrapper = "rm() { (set +o pipefail; printf 'y\\n%.0s' {1..32} | command rm \"$@\"); }\n"
            script = wrapper + exercise + '\n' + cleanup
            result = invoke(['bash', '-e', '-o', 'pipefail', '-c', script], private_env)
            remaining = [str(p.relative_to(parent)) for p in Path(parent).rglob('*')]
            result['remaining_fixture_paths'] = remaining
            result['source_sha256'] = hashlib.sha256(text.encode()).hexdigest()
            passes = len(re.findall(r'^PASS:', result['stdout'], flags=re.M))
            ok = result['status'] == 0 and passes >= minimum and not remaining
            record['pages'][name] = result
            print(('PASS' if ok else 'FAIL') + ': ' + name + ' exercise, assertions and cleanup')
            if not ok:
                failures.append(name)
                print(result['stderr'])
    if args.linux_observations:
        commands = [
            ['bash', '-c', 'type -a printf; help printf >/dev/null'],
            ['findmnt', '--target', '/'],
            ['stat', '--', '/'],
            ['ls', '-ld', '--', '/bin'],
            ['ip', '-brief', 'address'],
            ['ip', 'route', 'get', '127.0.0.1'],
            ['getent', 'ahosts', 'localhost'],
            ['ss', '-lnt'],
            ['journalctl', '--list-boots', '--no-pager'],
            ['journalctl', '--disk-usage'],
        ]
        for command in commands:
            if not shutil.which(command[0]):
                failures.append('missing tool: ' + command[0])
                continue
            observation = invoke(command, env)
            record['observations'].append(observation)
            if observation['status']:
                failures.append('observation failed: ' + ' '.join(command))
        record['os_release'] = Path('/etc/os-release').read_text()
        record['versions'] = [invoke(command, env) for command in
                              [['bash', '--version'], ['python3', '--version'],
                               ['systemctl', '--version'], ['findmnt', '--version']]]
        print(f"Recorded {len(record['observations'])} read-only Linux observations; inspect access/visibility notices in the report.")
    record['failures'] = failures
    if args.report:
        fd = os.open(args.report, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as handle:
            json.dump(record, handle, indent=2)
            handle.write('\n')
    if failures:
        print('FAIL: ' + '; '.join(failures))
        return 1
    print('PASS: all eight published examples and their cleanup completed.')
    print('This does not execute every table fragment or validate external sites.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
