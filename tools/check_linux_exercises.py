#!/usr/bin/env python3
"""Reproduce folders 4–7 exercises in an explicitly disposable, booted Linux VM.

Requires an ordinary sudo-authorized account, working systemd user manager and
preinstalled utilities. Creates bounded tmpfs mounts and runtime user units.
Never provisions packages, reboots, changes host resolver/firewall policy or
accepts a package transaction. Raw output is private evidence, not public data.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CORE = [
    ('05-troubleshooting-and-recovery/service-will-not-start.md',
     ['start status: 1', 'ExecMainStatus=1', 'ExecMainStatus=0'], {0, 1}, 45),
    ('05-troubleshooting-and-recovery/disk-space-or-inodes-are-exhausted.md',
     ['Observed ENOSPC while writing payload', 'Observed ENOSPC after', 'write recovered'], {0, 1}, 40),
    ('05-troubleshooting-and-recovery/filesystem-is-read-only.md',
     ['write status: 1', 'write restored'], {0, 1}, 30),
    ('05-troubleshooting-and-recovery/server-will-not-boot.md',
     ['verification status: 1', 'verification status: 0'], {0, 1}, 30),
    ('05-troubleshooting-and-recovery/cpu-or-memory-usage-is-high.md',
     ['worker status: 0', 'VmRSS', 'Completed bounded work; retained 16777216 bytes'], {0, 1}, 45),
    ('05-troubleshooting-and-recovery/dns-resolution-is-failing.md',
     ['lookup status: 2', 'lookup status: 0', '127.0.0.1'], {0, 1, 2}, 45),
    ('06-system-administration/service-management-and-restart-safety.md',
     ['CanReload=no', 'Restart=no', 'active', 'unit listing status: 1'], {0, 1}, 30),
    ('06-system-administration/log-management-and-rotation.md',
     ['preview left original intact: 0', 'new log starts empty: 0', 'event three'], {0}, 30),
    ('06-system-administration/user-access-and-sudo-management.md',
     ['parsed OK', 'draft not installed'], {0}, 30),
]
PORTABLE_REFERENCES = {
    'navigation-commands.md', 'file-management-commands.md', 'file-search-commands.md',
    'grep-reference.md', 'sed-reference.md', 'awk-reference.md', 'pipes-and-redirection.md',
    'tar-reference.md', 'rsync-reference.md',
}


class Review:
    def __init__(self):
        self.records = []

    def command(self, label, command, allowed=(0,), timeout=60):
        environment = os.environ.copy()
        environment['LC_ALL'] = 'C'
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                timeout=timeout, env=environment)
        self.records.append({'check': label, 'status': result.returncode,
                             'stdout': result.stdout, 'stderr': result.stderr})
        if result.returncode not in allowed:
            raise AssertionError(label + ': status ' + str(result.returncode) + '\n' + result.stderr)
        return result

    def published(self, relative, start_heading, expected, allowed, timeout=45, replacement=None):
        text = (ROOT / relative).read_text()
        start = text.index(start_heading)
        end_heading = '## Expected results' if relative.startswith('04-') else '## References'
        end = text.index(end_heading, start)
        code = '\n'.join(re.findall(r'^```bash\n(.*?)^```', text[start:end], re.M | re.S))
        if replacement is not None:
            code = replacement
        if not code:
            raise AssertionError(relative + ': no exercise found')
        variables = re.findall(r'^(\w+)=\$\(mktemp -d\)', code, re.M)
        for variable in ('lab_unit_file', 'safe_file'):
            collision_check = 'test ! -e "$' + variable + '" && test ! -L "$' + variable + '"'
            code = code.replace(collision_check, collision_check + ' || exit 90')
        # Enforce the written stop condition before mounted-filesystem writers run.
        for variable, limit in (('space_lab', 8), ('readonly_lab', 4)):
            needle = 'findmnt --mountpoint "$' + variable + '/fs"'
            if needle in code:
                guard = ('\ntest "$(findmnt -n -o FSTYPE --mountpoint "$' + variable
                         + '/fs")" = tmpfs || exit 90\n')
                guard += ('python3 - "$' + variable + '/fs" <<\'PY\'\nimport os, sys\ns=os.statvfs(sys.argv[1])\n'
                          + 'assert 0 < s.f_blocks*s.f_frsize <= ' + str(limit * 1024 * 1024) + '\n'
                          + ('assert 0 < s.f_files <= 128\n' if variable == 'space_lab' else '')
                          + 'PY\ntest "$?" -eq 0 || exit 90\n')
                code = code.replace(needle, needle + guard, 1)
        # A failed comparison must not be hidden by later successful cleanup.
        code = re.sub(r'^(cmp .+)$', r'\1 || exit 91', code, flags=re.M)
        with tempfile.TemporaryDirectory(prefix='linux-world-runner-') as folder:
            trace = Path(folder) / 'statuses'
            script = Path(folder) / 'exercise.sh'
            prelude = "set -u\nrm() { printf 'y\\n%.0s' {1..100} | command rm \"$@\"; }\n"
            # DEBUG preserves $? used by published status-capture commands.
            prelude += 'exec 3>' + str(trace) + '\n'
            prelude += 'trap \'printf "LW_STATUS:%s NEXT:%q\\n" "$?" "$BASH_COMMAND" >&3\' DEBUG\n'
            post = '\n:\n'
            for variable in variables:
                post += 'test ! -e "$' + variable + '" || exit 92\n'
            post += 'printf "LINUX_WORLD_CLEANUP_OK\\n"\n'
            script.write_text(prelude + code + post)
            result = self.command(relative, ['bash', str(script)], allowed=(0,), timeout=timeout)
            trace_text = trace.read_text()
            self.records[-1]['command_status_trace'] = trace_text
            statuses = [int(x) for x in re.findall(r'^LW_STATUS:(\d+) NEXT:', trace_text, re.M)]
            if not statuses or any(status not in allowed for status in statuses):
                raise AssertionError(relative + ': unexpected intermediate statuses ' + str(sorted(set(statuses)))
                                     + '\n' + trace_text)
            if not all(token in result.stdout for token in expected):
                raise AssertionError(relative + ': expected evidence absent\n' + result.stdout[-3000:])
            if 'LINUX_WORLD_CLEANUP_OK' not in result.stdout:
                raise AssertionError(relative + ': cleanup not reached')
            if 'service-management-and-restart-safety' in relative:
                pids = re.search(r'before=(\d+) after=(\d+)', result.stdout)
                if not pids or not all(int(x) > 0 for x in pids.groups()) or pids[1] == pids[2]:
                    raise AssertionError('restart did not show distinct live process IDs')
            if 'filesystem-is-read-only' in relative and 'Read-only file system' not in result.stderr:
                raise AssertionError('expected EROFS observation missing')
            self.records[-1]['intermediate_statuses'] = sorted(set(statuses))
            print('PASS ' + relative, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--confirm-disposable-vm', action='store_true', required=True)
    parser.add_argument('--report', type=Path, required=True, help='new private JSON evidence file')
    args = parser.parse_args()
    if platform.system() != 'Linux' or os.geteuid() == 0:
        parser.error('run as an ordinary account inside a disposable Linux VM')
    if args.report.exists():
        parser.error('report already exists; choose a new private path')
    review = Review()
    virt = review.command('VM boundary', ['systemd-detect-virt', '--vm']).stdout.strip()
    if not virt or virt == 'none':
        raise AssertionError('a virtual-machine boundary is required')
    review.command('sudo prerequisite', ['sudo', '-n', 'true'])
    review.command('user manager prerequisite', ['systemctl', '--user', 'show-environment'])
    os_release = Path('/etc/os-release').read_text()
    identity = re.search(r'^ID="?([a-z0-9_-]+)"?$', os_release, re.M)
    if not identity or identity[1] not in ('ubuntu', 'debian', 'fedora'):
        parser.error('this runner targets Ubuntu, Debian and conventional Fedora VMs only')
    family = 'rpm' if identity[1] == 'fedora' else 'deb'
    metadata = {'review_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'os_release': os_release, 'kernel': platform.release(), 'architecture': platform.machine(),
                'virtualization': virt}
    sources = []
    for collection in ('04-command-reference', '05-troubleshooting-and-recovery',
                       '06-system-administration', '07-linux-distributions', 'tools'):
        sources.extend(path for path in (ROOT / collection).rglob('*')
                       if path.is_file() and not path.name.startswith('._')
                       and path.suffix in ('.md', '.py'))
    metadata['source_sha256'] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                 for path in sorted(sources)}
    for label, command in {
        'bash': ['bash', '--version'], 'python': ['python3', '--version'],
        'systemd': ['systemctl', '--version'], 'util_linux': ['findmnt', '--version'],
        'logrotate': ['logrotate', '--version'], 'ssh': ['ssh', '-V'],
    }.items():
        result = review.command(label, command)
        metadata[label] = (result.stdout or result.stderr).splitlines()[0]
    try:
        for name in ('check_portable_examples.py', 'check_recovery_labs.py',
                     'check_administration_labs.py', 'check_distribution_labs.py'):
            review.command(name, [sys.executable, str(ROOT / 'tools' / name)], timeout=70)
            print('PASS ' + name, flush=True)
        for relative, expected, allowed, timeout in CORE:
            review.published(relative, '## Follow-along lab', expected, allowed, timeout)
        for path in sorted((ROOT / '04-command-reference').glob('*/*.md')):
            if (path.name.startswith('._') or path.name == 'README.md'
                    or path.parent.name == 'cheat-sheets' or path.name in PORTABLE_REFERENCES):
                continue
            if path.name == 'apt-reference.md' and family != 'deb': continue
            if path.name == 'dnf-reference.md' and family != 'rpm': continue
            replacement = None
            allowed = {0}
            expected = []
            if path.name == 'firewall-reference.md':
                replacement = 'sudo ufw status verbose' if family == 'deb' else 'sudo firewall-cmd --state\nsudo firewall-cmd --get-active-zones'
                allowed = {0, 252}
            if path.name == 'process-management-commands.md':
                allowed = {0, 1, 143}
                expected = ['child exit: 143']
            if path.name == 'dnf-reference.md': allowed = {0, 1}
            if path.name == 'recovery-command-reference.md': expected = ['note: OK']
            if path.name == 'permissions-and-ownership.md': expected = ['600 ', '\n700\n']
            review.published(str(path.relative_to(ROOT)), '## Follow along', expected, allowed,
                             timeout=90 if family == 'rpm' else 45, replacement=replacement)
        review.command('actual os-release reader', [sys.executable, str(ROOT / '07-linux-distributions/labs/read_identity.py'), '--file', '/etc/os-release'])
        commands = {
            'boot/root observation': 'cat /proc/cmdline; findmnt --target /; lsblk -f; systemctl --failed --no-pager',
            'process/cgroup/pressure observation': 'cat /proc/self/cgroup; cat /proc/pressure/cpu /proc/pressure/memory /proc/pressure/io',
            'resolver ownership': 'readlink -f /etc/resolv.conf; cat /etc/nsswitch.conf; resolvectl status',
            'security modules': 'sudo cat /sys/kernel/security/lsm',
        }
        if family == 'rpm':
            commands.update({'Fedora network ownership': 'nmcli device status; nmcli connection show --active',
                             'SELinux state': 'getenforce; sestatus',
                             'DNF proposal': 'dnf --assumeno upgrade bash'})
        else:
            commands.update({'Debian-family network ownership': 'networkctl list --no-pager; systemctl is-active systemd-networkd.service',
                             'AppArmor state': 'sudo aa-status',
                             'APT proposal': 'apt-get -s install --only-upgrade bash'})
            if identity[1] == 'ubuntu':
                commands['Netplan configuration inspection'] = 'sudo netplan get'
        for label, script in commands.items():
            # Observation absence is retained as data; the report records its actual status.
            review.command(label, ['bash', '-c', script], allowed=(0, 1, 2, 3, 4, 127), timeout=90)
            print('RECORDED ' + label, flush=True)
        success = True
    except Exception:
        success = False
        raise
    finally:
        descriptor = os.open(args.report, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, 'w') as output:
            json.dump({'environment': metadata, 'success': success, 'checks': review.records}, output, indent=2)
            output.write('\n')
        print('Private evidence: ' + str(args.report), flush=True)
    print('PASS named-VM exercise reproduction; no real workload or production certification is claimed')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, OSError, subprocess.SubprocessError) as error:
        print('FAIL: ' + str(error), file=sys.stderr)
        sys.exit(1)
