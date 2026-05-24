#!/usr/bin/env python3
"""
Serve AgentSkills workbench from repo root.

Accepts both URL styles (fixes 404 when workspace parent is cursorskils):
  /workbench/live/?barrierlens=1
  /agentskills-audit-collection/workbench/live/?barrierlens=1
"""

from __future__ import annotations

import argparse
import os
import re
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
STRIP_PREFIX = "/agentskills-audit-collection"


class WorkbenchHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        print(f"[workbench] {self.address_string()} - {fmt % args}")

    def _normalize_path(self) -> str:
        parsed = urlparse(self.path)
        path = parsed.path or "/"
        if path.startswith(STRIP_PREFIX + "/") or path == STRIP_PREFIX:
            path = path[len(STRIP_PREFIX) :] or "/"
        if path == "/live" or path == "/workbench":
            path = "/workbench/live/"
        return path + (("?" + parsed.query) if parsed.query else "")

    def do_GET(self) -> None:
        self.path = self._normalize_path()
        return super().do_GET()

    def do_HEAD(self) -> None:
        self.path = self._normalize_path()
        return super().do_HEAD()

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="AgentSkills workbench static server")
    parser.add_argument("--port", type=int, default=int(os.environ.get("ASW_LIVE_PORT", "8765")))
    parser.add_argument("--bind", default="127.0.0.1")
    args = parser.parse_args()

    os.chdir(ROOT)
    server = ThreadingHTTPServer((args.bind, args.port), WorkbenchHandler)
    base = f"http://{args.bind}:{args.port}"
    print(f"Serving ROOT: {ROOT}")
    print(f"Port: {args.port}")
    print(f"Live (BarrierLens): {base}/workbench/live/?barrierlens=1")
    print(f"Live (paste URL):   {base}/workbench/live/?url=https://barrierlens.vercel.app/")
    print(f"Also works:         {base}/agentskills-audit-collection/workbench/live/?barrierlens=1")
    print(f"Report:             {base}/reports/barrierlens-audit.html")
    print(f"Launcher:           {base}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
