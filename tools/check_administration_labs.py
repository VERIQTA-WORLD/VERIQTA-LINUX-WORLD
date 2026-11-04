#!/usr/bin/env python3
"""Execute eight portable administration exercises using temporary files only.

Does not install policy, change packages, run systemd, rotate host logs or retire
infrastructure. The isolated visudo check is excluded from this portable run.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / '06-production-administration'
CASES = {
    'linux-server-readiness-checklist.md': ('ready_lab', 3, ['Decision: BLOCKED', 'Console test: pending']),
    'user-access-and-sudo-management.md': ('access_lab', 3, ['draft not installed', 'Unverified: actual command path']),
    'patching-and-maintenance.md': ('patch_lab', 3, ['Transaction accepted: no', 'Reboot performed: no']),
    'backup-and-restore-operations.md': ('backup_lab', 4, ['initial byte comparison: 0', 'damaged byte comparison: 1', 'recovered byte comparison: 0', 'record two']),
    'monitoring-and-alerting.md': ('monitor_lab', 2, ['sample 4: ALERT', 'sample 6: RECOVERED']),
    'capacity-and-performance-reviews.md': ('capacity_lab', 2, ['days to reserve: 5.0', 'days to full: 15.0', 'ACTION NEEDED']),
    'configuration-changes-and-rollback.md': ('config_lab', 5, ['invalid candidate status: 2', 'active still matches previous: 0', 'rollback byte comparison: 0', '"message":"after"', '"message":"before"']),
    'linux-server-decommissioning.md': ('retire_lab', 3, ['BLOCKED: restore_verified', 'READY FOR REVIEW: lab-vm-001']),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run_exercises():
    for name, (variable, count, expected) in CASES.items():
        text = (GUIDES / name).read_text().split('## Follow-along lab', 1)[1]
        blocks = re.findall(r'^```bash\n(.*?)^```', text, re.M | re.S)
        if name == 'user-access-and-sudo-management.md':
            require(sum(block.strip().startswith('visudo ') for block in blocks) == 1,
                    'Review changed optional visudo block selection')
            blocks = [block for block in blocks if not block.strip().startswith('visudo ')]
        require(len(blocks) == count, f'{name}: review changed lab block selection')
        code = "rm() { printf 'y\\n%.0s' {1..30} | command rm \"$@\"; }\n" + '\n'.join(blocks)
        code = code.replace(f'{variable}=$(mktemp -d)',
                            f'{variable}=$(mktemp -d)\nprintf "LAB_PATH:%s\\n" "${variable}"', 1)
        with tempfile.TemporaryDirectory(prefix='lw-admin-check-') as directory:
            script = Path(directory) / 'exercise.sh'
            script.write_text(code)
            result = subprocess.run(['bash', str(script)], cwd=ROOT, text=True,
                                    input='', capture_output=True, timeout=20)
        require(result.returncode == 0, f'{name}: script failed\n{result.stdout}\n{result.stderr}')
        require(all(item in result.stdout for item in expected),
                f'{name}: expected observation missing\n{result.stdout}\n{result.stderr}')
        paths = re.findall(r'^LAB_PATH:(.+)$', result.stdout, re.M)
        require(len(paths) == 1 and not Path(paths[0]).exists(), f'{name}: cleanup incomplete')
        print(f'PASS {name}: expected observations and temporary-directory cleanup')


def check_validator():
    helper = GUIDES / 'labs/check_demo_config.py'
    cases = [
        ({'port': 8000, 'message': 'ready'}, 0),
        ({'port': True, 'message': 'ready'}, 2),
        ({'port': 0, 'message': 'ready'}, 2),
        ({'port': 65536, 'message': 'ready'}, 2),
        ({'port': '8000', 'message': 'ready'}, 2),
        ({'port': 8000, 'message': ''}, 2),
        ({'port': 8000, 'message': 'ready', 'extra': True}, 2),
        ({'message': 'ready'}, 2),
        ([], 2),
    ]
    with tempfile.TemporaryDirectory(prefix='lw-schema-check-') as directory:
        candidate = Path(directory) / 'candidate.json'
        for value, status in cases:
            candidate.write_text(json.dumps(value))
            result = subprocess.run([sys.executable, str(helper), str(candidate)],
                                    capture_output=True, text=True, timeout=5)
            require(result.returncode == status, f'Unexpected schema result for {value}')
        candidate.write_text('{broken JSON')
        result = subprocess.run([sys.executable, str(helper), str(candidate)],
                                capture_output=True, text=True, timeout=5)
        require(result.returncode == 2, 'Malformed JSON was not rejected')
    print('PASS validator: valid input plus nine invalid syntax/schema cases')


if __name__ == '__main__':
    run_exercises()
    check_validator()
    print('Portable exercises only; systemd, logrotate, visudo and package-manager behavior require separate Linux review.')
