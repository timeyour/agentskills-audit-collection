"""Smoke test for scripts/browser-relay.py evidence upload."""

from __future__ import annotations

import base64
import importlib.util
import json
import tempfile
import threading
import unittest
import urllib.request
from http.server import HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_relay_module():
    path = ROOT / "scripts" / "browser-relay.py"
    spec = importlib.util.spec_from_file_location("browser_relay", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def _tiny_png_data_url() -> str:
    raw = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    )
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii")


class TestBrowserRelay(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.browser_relay = _load_relay_module()
        self.browser_relay.ARTIFACTS = Path(self.tmp.name) / "artifacts"
        self.server = HTTPServer(("127.0.0.1", 0), self.browser_relay.RelayHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_address[1]}"

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)
        self.tmp.cleanup()

    def test_evidence_upload(self) -> None:
        run_id = "test-run-001"
        body = json.dumps(
            {
                "runId": run_id,
                "note": "test",
                "url": "https://example.com",
                "pngDataUrl": _tiny_png_data_url(),
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/api/evidence",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        self.assertTrue(data["ok"])
        pngs = list((self.browser_relay.ARTIFACTS / run_id / "screenshots").glob("ext-*.png"))
        self.assertEqual(len(pngs), 1)
        metas = list((self.browser_relay.ARTIFACTS / run_id / "screenshots").glob("ext-*.meta.json"))
        self.assertEqual(len(metas), 1)

    def test_narrate_passthrough(self) -> None:
        body = json.dumps(
            {
                "text": "Checking primary CTA",
                "task": "translate",
                "targetLocale": "zh",
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/api/narrate",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        self.assertTrue(data["ok"])
        self.assertEqual(data["mode"], "passthrough")
        self.assertEqual(data["text"], "Checking primary CTA")


if __name__ == "__main__":
    unittest.main()
