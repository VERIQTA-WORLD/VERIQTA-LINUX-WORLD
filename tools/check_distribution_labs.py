#!/usr/bin/env python3
"""Run portable distribution-study exercises; no Linux host probes or changes."""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / '07-linux-distributions'
CASES = {
    'understanding-linux-distribution-families.md': ('family_lab', 3, ['Debian-related', 'Alpine-related', 'Enterprise RPM-related', 'not observed']),
    'choosing-a-linux-distribution.md': ('choice_lab', 2, ['Candidate A: REJECTED: vendor_support', 'Candidate B: eligible for further comparison']),
    'ubuntu-administration-notes.md': ('ubuntu_lab', 2, ['"ID": "ubuntu"', '"VERSION_ID": "24.04"', 'Network owner and resolver: not observed']),
    'debian-administration-notes.md': ('debian_lab', 2, ['"ID": "debian"', '"ID": "ubuntu"', 'Different: product ID']),
    'rhel-and-compatible-distributions.md': ('enterprise_lab', 2, ['"ID": "rhel"', '"ID": "rocky"', 'application certification and coverage']),
    'fedora-administration-notes.md': ('fedora_lab', 2, ['"VARIANT_ID": "workstation"', '"VARIANT_ID": "silverblue"', 'No package transaction is authorized']),
    'package-manager-comparison.md': ('packages_lab', 2, ['Task: identify the installed package', 'Package transaction accepted: no']),
    'apparmor-and-selinux-overview.md': ('policy_lab', 2, ['ordinary allowed, policy denied: DENY', 'ordinary denied, policy allowed: DENY', 'both example checks allow: ALLOW']),
    'distribution-differences-quick-reference.md': ('compare_lab', 2, ['Debian-related', 'Fedora/RPM-related', 'Unknown: network/resolver owner']),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run_exercises():
    for name, (variable, count, expected) in CASES.items():
        text = (GUIDES / name).read_text().split('## Follow-along lab', 1)[1]
        # Host observations in Verification and limits are deliberately excluded.
        selected = text.split('## Verification and limits', 1)[0] + text.split('## Cleanup', 1)[1]
        blocks = re.findall(r'^```bash\n(.*?)^```', selected, re.M | re.S)
        require(len(blocks) == count, f'{name}: review changed block selection')
        code = "rm() { printf 'y\\n%.0s' {1..30} | command rm \"$@\"; }\n" + '\n'.join(blocks)
        code = code.replace(f'{variable}=$(mktemp -d)',
                            f'{variable}=$(mktemp -d)\nprintf "LAB_PATH:%s\\n" "${variable}"', 1)
        with tempfile.TemporaryDirectory(prefix='lw-distro-check-') as directory:
            script = Path(directory) / 'exercise.sh'
            script.write_text(code)
            result = subprocess.run(['bash', str(script)], cwd=ROOT, text=True,
                                    input='', capture_output=True, timeout=20)
        require(result.returncode == 0, f'{name}: failed\n{result.stdout}\n{result.stderr}')
        require(all(item in result.stdout for item in expected),
                f'{name}: missing expected observation\n{result.stdout}\n{result.stderr}')
        paths = re.findall(r'^LAB_PATH:(.+)$', result.stdout, re.M)
        require(len(paths) == 1 and not Path(paths[0]).exists(), f'{name}: cleanup incomplete')
        print(f'PASS {name}: expected observations and temporary-directory cleanup')


def check_reader():
    helper = GUIDES / 'labs/read_identity.py'
    valid = [
        ('ID=ubuntu\nVERSION_ID="24.04"\nID_LIKE=debian\n', 'Debian-related'),
        ('ID=debian\nVERSION_ID=13\n', 'Debian-related'),
        ('ID=fedora\nVARIANT_ID=silverblue\n', 'Fedora/RPM-related'),
        ('ID=rhel\n', 'Enterprise RPM-related'),
        ('ID=rocky\n', 'Enterprise RPM-related'),
        ('ID=almalinux\n', 'Enterprise RPM-related'),
        ('ID=alpine\n', 'Alpine-related'),
        ('ID=arch\n', 'Arch-related'),
        ('ID=nixos\n', 'NixOS'),
        ('ID=opensuse-tumbleweed\n', 'SUSE/RPM-related'),
        ("ID='exampleos'\nID_LIKE='rhel fedora'\n", 'Enterprise RPM-related'),
        ('ID=exampleos\nID_LIKE="fedora rhel"\n', 'Fedora/RPM-related'),
        ('ID=exampleos\n', 'Unknown; research this product'),
    ]
    invalid = [b'NAME=Example\n', b'ID=\n', b'ID="ubuntu\n', b'ID=ubuntu\nID=debian\n',
               b'ID_LIKE=rhel fedora\nID=exampleos\n', b'#' * 16385, b'\xff']
    with tempfile.TemporaryDirectory(prefix='lw-identity-check-') as directory:
        record = Path(directory) / 'os-release'
        marker = Path(directory) / 'must-not-exist'
        for text, hint in valid:
            record.write_text(text)
            result = subprocess.run([sys.executable, str(helper), '--file', str(record)],
                                    capture_output=True, text=True, timeout=5)
            require(result.returncode == 0, result.stderr)
            report = json.loads(result.stdout)
            require(report['family_hint'] == hint and report['tool_and_policy_state'] == 'not observed', 'Reader inferred unobserved state')
        # Input is data, never shell source. Both ignored and recognized fields must not execute.
        record.write_text(f'ID=ubuntu\nNAME="$(touch {marker})"\n')
        result = subprocess.run([sys.executable, str(helper), '--file', str(record)], capture_output=True, timeout=5)
        require(result.returncode == 0 and not marker.exists(), 'Ignored metadata executed shell content')
        invalid.append(f'ID="$(touch {marker})"\n'.encode())
        for data in invalid:
            record.write_bytes(data)
            result = subprocess.run([sys.executable, str(helper), '--file', str(record)], capture_output=True, timeout=5)
            require(result.returncode == 2 and not marker.exists(), 'Invalid metadata was accepted or executed')
    print(f'PASS identity reader: {len(valid)} classifications, unobserved-state preservation, {len(invalid)} invalid inputs and no shell execution')


if __name__ == '__main__':
    run_exercises()
    check_reader()
    print('Fixture and conceptual exercises only; no distribution installation, host query, package transaction or policy change performed.')
