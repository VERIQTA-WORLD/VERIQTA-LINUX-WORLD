#!/usr/bin/env python3
"""Read four simple os-release identity fields without executing shell content.

A bounded teaching reader, not a complete parser for arbitrary os-release fields
or an authorization to select system-changing commands automatically.
"""
import argparse
import json
from pathlib import Path
import re

FIELDS = {'ID', 'ID_LIKE', 'VERSION_ID', 'VARIANT_ID'}
HINTS = {
    'debian': 'Debian-related', 'ubuntu': 'Debian-related',
    'fedora': 'Fedora/RPM-related', 'rhel': 'Enterprise RPM-related',
    'rocky': 'Enterprise RPM-related', 'almalinux': 'Enterprise RPM-related',
    'centos': 'CentOS/RPM-related', 'opensuse': 'SUSE/RPM-related',
    'opensuse-leap': 'SUSE/RPM-related', 'opensuse-tumbleweed': 'SUSE/RPM-related',
    'sles': 'SUSE/RPM-related', 'arch': 'Arch-related',
    'alpine': 'Alpine-related', 'nixos': 'NixOS',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', type=Path, required=True)
    args = parser.parse_args()
    try:
        with args.file.open('rb') as stream:
            data = stream.read(16385)
        if len(data) > 16384:
            parser.error('identity input exceeds the 16 KiB teaching limit')
        text = data.decode('utf-8')
        fields = {}
        for number, line in enumerate(text.splitlines(), 1):
            key, separator, raw = line.partition('=')
            if not separator or key not in FIELDS:
                continue
            if key in fields:
                parser.error(f'duplicate identity field {key} at line {number}')
            value = raw.strip()
            quoted = value.startswith(('"', "'"))
            if quoted:
                if len(value) < 2 or value[-1] != value[0]:
                    parser.error(f'unbalanced quotes in {key}')
                value = value[1:-1]
            allowed = r'[a-z0-9._ -]*' if key == 'ID_LIKE' else r'[A-Za-z0-9._+-]*'
            if not re.fullmatch(allowed, value) or (' ' in value and not quoted):
                parser.error(f'{key} is outside the supported simple identity syntax')
            fields[key] = value
        if not fields.get('ID'):
            parser.error('a nonempty ID field is required')
        candidates = [fields['ID']] + fields.get('ID_LIKE', '').split()
        hint = next((HINTS[value] for value in candidates if value in HINTS), 'Unknown; research this product')
        print(json.dumps({'identity': fields, 'family_hint': hint,
                          'tool_and_policy_state': 'not observed'}, indent=2, sort_keys=True))
    except (OSError, UnicodeError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
