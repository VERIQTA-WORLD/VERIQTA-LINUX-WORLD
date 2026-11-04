#!/usr/bin/env python3
"""One bounded worker for observing CPU and resident memory, not a stress test."""
import argparse
import os
from pathlib import Path
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=int, default=20)
    parser.add_argument('--mib', type=int, default=16)
    parser.add_argument('--ready-file', type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.seconds <= 60 or not 1 <= args.mib <= 64:
        parser.error('seconds must be 1..60 and mib must be 1..64')
    data = bytearray(args.mib * 1024 * 1024)
    for offset in range(0, len(data), 4096):
        data[offset] = 1
    args.ready_file.write_text(str(os.getpid()) + '\n')
    deadline = time.monotonic() + args.seconds
    value = 1
    while time.monotonic() < deadline:
        value = (value * 1664525 + 1013904223) & 0xFFFFFFFF
    print(f'Completed bounded work; retained {len(data)} bytes; result {value}')


if __name__ == '__main__':
    main()
