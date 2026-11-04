#!/usr/bin/env python3
"""Run bounded, unprivileged portable exercises; never mount or edit host policy.

Executes published method, offline SSH, reachability and verification snippets.
The two HTTP scenarios bind only to loopback. No Linux-only lab is executed.
"""
from pathlib import Path
import os
import re
import signal
import socket
import subprocess
import sys
import tempfile
import time
from urllib.request import ProxyHandler, build_opener

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / '05-troubleshooting-and-recovery'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run_guide(name, variable, expected, count, offline_ssh=False):
    text = (GUIDES / name).read_text().split('## Follow-along lab', 1)[1]
    if offline_ssh:
        # The optional authentication test needs an authorized SSH VM and is excluded.
        text = text.split('## Recovery and verification', 1)[0] + text.split('## Cleanup', 1)[1]
    blocks = re.findall(r'^```bash\n(.*?)^```', text, re.M | re.S)
    require(len(blocks) == count, f'{name}: review changed lab block selection')
    # Give each rm invocation its own confirmation stream, like separate terminal replies.
    # A single shared pipe can be read ahead by the first rm and starve later prompts.
    code = "rm() { printf 'y\\n%.0s' {1..30} | command rm \"$@\"; }\n" + '\n'.join(blocks)
    code = code.replace(f'{variable}=$(mktemp -d)', f'{variable}=$(mktemp -d)\nprintf "LAB_PATH:%s\\n" "${variable}"', 1)
    with tempfile.TemporaryDirectory(prefix='lw-check-') as script_dir:
        script = Path(script_dir) / 'exercise.sh'
        script.write_text(code)
        process = subprocess.Popen(['bash', str(script)], cwd=ROOT, text=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, start_new_session=True)
        try:
            stdout, stderr = process.communicate('y\n' * 30, timeout=45)
            require(process.returncode == 0, f'{name}: failed\n{stdout}\n{stderr}')
            require(all(item in stdout for item in expected), f'{name}: missing expected observations\n{stdout}\n{stderr}')
            require('FAILED' not in stdout, f'{name}: a repeated acceptance check failed')
            if name == 'server-is-unreachable.md':
                require(stdout.splitlines().count('ready') == 2, 'Expected a successful response both before failure and after recovery')
            paths = re.findall(r'^LAB_PATH:(.+)$', stdout, re.M)
            require(len(paths) == 1 and not Path(paths[0]).exists(), f'{name}: temporary-directory cleanup incomplete')
            print(f'PASS {name}: expected observations and cleanup')
        finally:
            # This group belongs only to this test script and its children.
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            if process.poll() is None:
                try:
                    process.communicate(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.communicate()


def check_helpers():
    helpers = GUIDES / 'labs'
    opener = build_opener(ProxyHandler({}))
    with tempfile.TemporaryDirectory(prefix='lw-helper-check-') as directory:
        root = Path(directory)
        site = root / 'site'
        site.mkdir()
        (site / 'health.txt').write_text('ready\n')
        ready = root / 'port'
        with (root / 'http.log').open('w') as log:
            server = subprocess.Popen([sys.executable, str(helpers / 'loopback_http.py'),
                                       '--directory', str(site), '--ready-file', str(ready),
                                       '--seconds', '2'], stdout=log, stderr=log)
            try:
                deadline = time.monotonic() + 5
                while not ready.exists() and server.poll() is None and time.monotonic() < deadline:
                    time.sleep(0.05)
                require(ready.exists(), 'HTTP helper did not become ready; inspect loopback permissions')
                port = int(ready.read_text())
                with opener.open(f'http://127.0.0.1:{port}/health.txt', timeout=2) as response:
                    require(response.status == 200 and response.read() == b'ready\n', 'HTTP helper response mismatch')
                # An unfinished request must not keep the bounded teaching server alive.
                with socket.create_connection(('127.0.0.1', port), timeout=2) as unfinished:
                    unfinished.sendall(b'GET /health.txt HTTP/1.1\r\nHost: 127.0.0.1\r\n')
                    require(server.wait(timeout=5) == 0, 'HTTP helper failed bounded exit with an unfinished request')
            finally:
                if server.poll() is None:
                    server.terminate()
                    server.wait(timeout=5)
        for helper, arguments in [('loopback_http.py', ['--directory', str(site), '--seconds', '301']),
                                  ('bounded_load.py', ['--mib', '65']),
                                  ('bounded_load.py', ['--seconds', '61'])]:
            result = subprocess.run([sys.executable, str(helpers / helper), '--ready-file', str(root / 'invalid'),
                                     *arguments], capture_output=True, text=True, timeout=5)
            require(result.returncode == 2 and not (root / 'invalid').exists(), f'{helper}: accepted an out-of-bounds request')
        worker = subprocess.run([sys.executable, str(helpers / 'bounded_load.py'), '--seconds', '1',
                                 '--mib', '1', '--ready-file', str(root / 'worker')],
                                capture_output=True, text=True, timeout=5)
        require(worker.returncode == 0 and 'retained 1048576 bytes' in worker.stdout, 'Bounded worker failed')
        require((root / 'worker').read_text().strip().isdigit(), 'Worker readiness PID missing')
    print('PASS helpers: loopback response, bounded exit, rejected resource limits and 1 MiB/1-second worker')


def main():
    # Fail before creating exercise data if the sandbox disallows loopback listeners.
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', 0))
    run_guide('linux-troubleshooting-method.md', 'case_dir',
              ['H1:', 'H2:', 'Conclusion:', 'Unresolved:'], 4)
    run_guide('ssh-login-is-failing.md', 'ssh_lab', ['port 65022', 'port 22', 'hostname 127.0.0.1'], 3, offline_ssh=True)
    run_guide('server-is-unreachable.md', 'reach_lab', ['ready', 'curl status: 7'], 6)
    run_guide('verify-recovery-after-a-fix.md', 'verify_lab',
              ['request status: 0', 'content comparison status: 1', 'content comparison status: 0', 'sample 5: accepted'], 5)
    check_helpers()
    print('Portable checks only. systemd, DNS/NSS, tmpfs, Linux /proc and boot validation remain separate.')


if __name__ == '__main__':
    main()
