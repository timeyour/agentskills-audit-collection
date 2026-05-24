"""Tests for M3 audit_capture (HTTP fallback, no Playwright required)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "scripts"))

from audit_capture import http_probe, parse_surface, main  # noqa: E402
from export_public_report import render_report  # noqa: E402


class TestAuditCapture(unittest.TestCase):
    def test_parse_surface_counts(self) -> None:
        html = """
        <html><head><title>Demo</title></head>
        <body><a href="/x">x</a><button>Go</button><form><input></form></body></html>
        """
        surface = parse_surface(html, "https://example.com")
        self.assertEqual(surface["page_title"], "Demo")
        self.assertEqual(surface["buttons_count"], 1)
        self.assertEqual(surface["forms_count"], 1)

    def test_capture_writes_result_without_playwright(self) -> None:
        fake_html = "<html><head><title>OK</title></head><body></body></html>"
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "test-run"
            run_dir.mkdir()
            with mock.patch(
                "audit_capture.http_probe",
                return_value={
                    "status": "passed",
                    "http_status": 200,
                    "final_url": "https://example.com",
                    "html": fake_html,
                },
            ):
                code = main(["https://example.com", "--run-dir", str(run_dir), "--no-playwright"])
            self.assertEqual(code, 0)
            result = json.loads((run_dir / "result.json").read_text())
            self.assertEqual(result["capture_tool"], "urllib")
            self.assertTrue((run_dir / "logs" / "console.log").is_file())


class TestExportPublicReport(unittest.TestCase):
    def test_render_contains_scoped_class(self) -> None:
        golden = ROOT / "validation" / "golden" / "audit-report.example.json"
        data = json.loads(golden.read_text(encoding="utf-8"))
        html = render_report(data)
        self.assertIn("asw-public", html)
        self.assertIn("Executive summary", html)
        self.assertIn("ISSUE-001", html)
        self.assertIn("检测过程摘要", html)
        self.assertIn("优秀网站对照", html)
        self.assertIn("四维验收概览", html)


if __name__ == "__main__":
    unittest.main()
