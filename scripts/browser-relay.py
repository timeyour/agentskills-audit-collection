#!/usr/bin/env python3
"""
Local relay for the browser extension: CORS-friendly evidence upload.

Writes PNG + metadata under validation/artifacts/<runId>/screenshots/.

Usage:
  python3 scripts/browser-relay.py
  python3 scripts/browser-relay.py --port 8766
"""

from __future__ import annotations

import argparse
import base64
import json
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "validation" / "artifacts"
RUN_ID_RE = re.compile(r"^[a-zA-Z0-9._-]+$")


def repo_relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


class RelayHandler(BaseHTTPRequestHandler):
    server_version = "AgentSkillsBrowserRelay/0.1"

    def log_message(self, fmt: str, *args) -> None:
        print(f"[relay] {self.address_string()} - {fmt % args}")

    def _cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in ("/", "/health"):
            self._json(200, {"ok": True, "service": "browser-relay", "artifactsRoot": str(ARTIFACTS)})
            return
        self._json(404, {"ok": False, "error": "not found"})

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path != "/api/evidence":
            self._json(404, {"ok": False, "error": "not found"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self._json(400, {"ok": False, "error": "invalid JSON"})
            return

        run_id = str(data.get("runId") or "").strip()
        if not RUN_ID_RE.match(run_id):
            self._json(400, {"ok": False, "error": "invalid runId"})
            return

        png_data_url = data.get("pngDataUrl") or ""
        if not png_data_url.startswith("data:image/png;base64,"):
            self._json(400, {"ok": False, "error": "pngDataUrl required (data:image/png;base64,...)"})
            return

        b64 = png_data_url.split(",", 1)[1]
        try:
            png_bytes = base64.b64decode(b64, validate=True)
        except Exception:
            self._json(400, {"ok": False, "error": "invalid base64"})
            return

        run_dir = ARTIFACTS / run_id
        shots = run_dir / "screenshots"
        shots.mkdir(parents=True, exist_ok=True)

        stamp = utc_stamp()
        png_path = shots / f"ext-{stamp}.png"
        meta_path = shots / f"ext-{stamp}.meta.json"
        png_path.write_bytes(png_bytes)

        meta = {
            "source": "browser-extension",
            "runId": run_id,
            "url": data.get("url"),
            "note": data.get("note"),
            "stageId": data.get("stageId"),
            "stepId": data.get("stepId"),
            "capturedAt": data.get("capturedAt") or datetime.now(timezone.utc).isoformat(),
            "pngFile": png_path.name,
        }
        meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        events = run_dir / "run-events.ndjson"
        if events.parent.exists():
            event = {
                "ts": meta["capturedAt"],
                "type": "evidence_captured",
                "source": "browser-extension",
                "path": repo_relative(png_path),
                "url": meta.get("url"),
                "stageId": meta.get("stageId"),
                "stepId": meta.get("stepId"),
            }
            with events.open("a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")

        self._json(
            200,
            {"ok": True, "path": repo_relative(png_path), "metaPath": repo_relative(meta_path)},
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="AgentSkills browser extension relay")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--bind", default="127.0.0.1")
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.bind, args.port), RelayHandler)
    print(f"Browser relay listening on http://{args.bind}:{args.port}")
    print(f"Artifacts root: {ARTIFACTS}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
