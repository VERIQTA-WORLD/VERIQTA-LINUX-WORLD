#!/usr/bin/env python3
"""Bounded loopback-only static server for the documented recovery exercises."""
import argparse
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import signal
import threading


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--ready-file', type=Path, required=True)
    parser.add_argument('--seconds', type=int, default=180)
    args = parser.parse_args()
    if not args.directory.is_dir() or not 1 <= args.seconds <= 300:
        parser.error('directory must exist and seconds must be between 1 and 300')
    stopping = threading.Event()

    def stop(_signum, _frame):
        stopping.set()

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    handler = partial(SimpleHTTPRequestHandler, directory=str(args.directory.resolve()))
    with ThreadingHTTPServer(('127.0.0.1', 0), handler) as server:
        thread = threading.Thread(target=server.serve_forever, kwargs={'poll_interval': 0.1}, daemon=True)
        thread.start()
        try:
            args.ready_file.write_text(str(server.server_port) + '\n')
            stopping.wait(args.seconds)
        finally:
            server.shutdown()
            thread.join(timeout=2)


if __name__ == '__main__':
    main()
