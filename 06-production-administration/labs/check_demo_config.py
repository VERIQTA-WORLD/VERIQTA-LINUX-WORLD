#!/usr/bin/env python3
"""Validate the intentionally small JSON schema used by the configuration lab."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        config = json.loads(args.file.read_text())
    except (OSError, ValueError) as error:
        parser.error(f'cannot read valid JSON: {error}')
    if not isinstance(config, dict) or set(config) != {'port', 'message'}:
        parser.error('expected exactly port and message properties')
    if type(config['port']) is not int or not 1 <= config['port'] <= 65535:
        parser.error('port must be an integer from 1 through 65535')
    if not isinstance(config['message'], str) or not config['message'].strip():
        parser.error('message must be a nonempty string')
    print('Demo configuration accepted')


if __name__ == '__main__':
    main()
