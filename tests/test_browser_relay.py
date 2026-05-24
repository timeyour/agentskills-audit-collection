"""Smoke test for scripts/browser-relay.py evidence upload."""

from __future__ import annotations

import base64
import importlib.util
import json
import threading
import urllib.request
from http.server import HTTPServer
from pathlib import Path

import pytest

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


@pytest.fixture
def relay_server(tmp_path, monkeypatch):
    browser_relay = _load_relay_module()
    monkeypatch.setattr(browser_relay, "ARTIFACTS", tmp_path / "artifacts")
    server = HTTPServer(("127.0.0.1", 0), browser_relay.RelayHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}", browser_relay
    server.shutdown()


def test_evidence_upload(relay_server):
    base_url, browser_relay = relay_server
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
        f"{base_url}/api/evidence",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode())
    assert data["ok"] is True
    pngs = list((browser_relay.ARTIFACTS / run_id / "screenshots").glob("ext-*.png"))
    assert len(pngs) == 1
    metas = list((browser_relay.ARTIFACTS / run_id / "screenshots").glob("ext-*.meta.json"))
    assert len(metas) == 1


def test_narrate_passthrough(relay_server):
    base_url, _browser_relay = relay_server
    body = json.dumps(
        {
            "text": "Checking primary CTA",
            "task": "translate",
            "targetLocale": "zh",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}/api/narrate",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode())
    assert data["ok"] is True
    assert data["mode"] == "passthrough"
    assert data["text"] == "Checking primary CTA"
