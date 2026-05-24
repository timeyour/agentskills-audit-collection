#!/usr/bin/env python3
"""
M3 semi-automated capture: URL load, surface hints, console log, screenshot.

Writes to validation/artifacts/<runId>/ (or an existing run dir from audit-run-init.sh).

Playwright (optional): pip install playwright && playwright install chromium
Without Playwright: HTTP HEAD/GET + HTML parse only (screenshot marked SKIPPED-SAFE).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS_ROOT = ROOT / "validation" / "artifacts"


class SurfaceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.links: list[str] = []
        self.buttons = 0
        self.forms = 0
        self.inputs = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if t == "title":
            self._in_title = True
        elif t == "a":
            href = dict(attrs).get("href")
            if href and href.startswith(("http", "/")):
                self.links.append(href)
        elif t == "button":
            self.buttons += 1
        elif t == "form":
            self.forms += 1
        elif t == "input":
            self.inputs += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rel_to_root(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)


def new_run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + f"-{Path.cwd().name}"


def ensure_run_dir(run_dir: Path | None, url: str) -> Path:
    if run_dir:
        run_dir = run_dir.resolve()
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir
    run_id = new_run_id()
    path = ARTIFACTS_ROOT / run_id
    path.mkdir(parents=True, exist_ok=True)
    return path


def http_probe(url: str, timeout: int) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AgentSkills-AuditCapture/0.1 (+https://github.com/timeyour/agentskills-audit-collection)"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(512_000)
            charset = resp.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "status": "passed",
                "http_status": resp.status,
                "final_url": resp.geturl(),
                "content_type": resp.headers.get("Content-Type", ""),
                "html": text,
            }
    except urllib.error.HTTPError as e:
        return {
            "status": "partial",
            "http_status": e.code,
            "final_url": url,
            "error": str(e),
            "html": "",
        }
    except Exception as e:
        return {"status": "failed", "http_status": None, "final_url": url, "error": str(e), "html": ""}


def parse_surface(html: str, base_url: str) -> dict:
    parser = SurfaceParser()
    if html:
        try:
            parser.feed(html)
        except Exception:
            pass
    unique_links = sorted(set(parser.links))[:50]
    return {
        "page_title": parser.title.strip() or "UNKNOWN",
        "links_sample": unique_links,
        "links_count": len(unique_links),
        "buttons_count": parser.buttons,
        "forms_count": parser.forms,
        "inputs_count": parser.inputs,
    }


def capture_playwright(url: str, run_dir: Path, timeout_ms: int) -> dict:
    from playwright.sync_api import sync_playwright

    logs_dir = run_dir / "logs"
    shots_dir = run_dir / "screenshots"
    logs_dir.mkdir(exist_ok=True)
    shots_dir.mkdir(exist_ok=True)
    console_lines: list[str] = []
    shot_path = shots_dir / "homepage.png"
    result: dict = {"tool": "playwright", "screenshot": None, "console_log": None}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        def on_console(msg):
            console_lines.append(f"[{msg.type}] {msg.text}")

        page.on("console", on_console)
        response = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
        page.wait_for_timeout(500)
        page.screenshot(path=str(shot_path), full_page=False)

        links = page.eval_on_selector_all(
            "a[href]",
            "els => els.slice(0, 50).map(a => a.getAttribute('href'))",
        )
        buttons = page.locator("button").count()
        forms = page.locator("form").count()
        final_url = page.url
        page_title = page.title()
        http_status = response.status if response else None

        browser.close()

    log_path = logs_dir / "console.log"
    log_path.write_text("\n".join(console_lines) or "(no console messages)\n", encoding="utf-8")
    result["screenshot"] = rel_to_root(shot_path)
    result["console_log"] = rel_to_root(log_path)
    result["http_status"] = http_status
    result["final_url"] = final_url
    result["surface"] = {
        "page_title": page_title or "UNKNOWN",
        "links_sample": links or [],
        "links_count": len(links or []),
        "buttons_count": buttons,
        "forms_count": forms,
    }
    result["status"] = "passed" if response and response.ok else "partial"
    return result


def patch_run_state(run_dir: Path, annotation: str) -> None:
    state_path = run_dir / "run-state.json"
    if not state_path.is_file():
        return
    data = json.loads(state_path.read_text(encoding="utf-8"))
    data["activeAnnotation"] = annotation
    data["updatedAt"] = utc_now()
    for stage in data.get("stages", []):
        if stage.get("id") == "live-functional":
            stage["status"] = "in_progress"
            for step in stage.get("steps", []):
                if step.get("id") == "homepage-load":
                    step["status"] = "completed"
    state_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_event(run_dir: Path, event: dict) -> None:
    events = run_dir / "run-events.ndjson"
    with events.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capture URL evidence into validation/artifacts/<runId>/")
    parser.add_argument("url", help="Target URL (https://...)")
    parser.add_argument("--run-dir", type=Path, help="Existing run directory from audit-run-init.sh")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds")
    parser.add_argument("--no-playwright", action="store_true", help="Force urllib-only capture")
    args = parser.parse_args(argv)

    url = args.url.strip()
    if not re.match(r"^https?://", url, re.I):
        print("error: URL must start with http:// or https://", file=sys.stderr)
        return 2

    started = utc_now()
    run_dir = ensure_run_dir(args.run_dir, url)
    for sub in ("screenshots", "logs", "traces", "har"):
        (run_dir / sub).mkdir(exist_ok=True)

    patch_run_state(run_dir, f"M3 capture: loading {url}")
    append_event(
        run_dir,
        {"ts": started, "type": "capture_started", "url": url, "runDir": rel_to_root(run_dir)},
    )

    steps: list[dict] = []
    capture_tool = "urllib"
    playwright_result: dict | None = None

    if not args.no_playwright:
        try:
            playwright_result = capture_playwright(url, run_dir, args.timeout * 1000)
            capture_tool = "playwright"
            steps.append(
                {
                    "name": "playwright_goto",
                    "status": playwright_result.get("status", "UNKNOWN"),
                    "http_status": playwright_result.get("http_status"),
                    "actual": playwright_result.get("final_url"),
                }
            )
            steps.append(
                {
                    "name": "screenshot",
                    "status": "passed",
                    "path": playwright_result.get("screenshot"),
                }
            )
            steps.append(
                {
                    "name": "console_log",
                    "status": "passed",
                    "path": playwright_result.get("console_log"),
                }
            )
            surface = playwright_result.get("surface", {})
        except ImportError:
            steps.append(
                {
                    "name": "playwright",
                    "status": "SKIPPED-SAFE",
                    "notes": "Install: pip install playwright && playwright install chromium",
                }
            )
            surface = {}
        except Exception as e:
            steps.append({"name": "playwright", "status": "failed", "error": str(e)})
            surface = {}
    else:
        steps.append({"name": "playwright", "status": "SKIPPED-SAFE", "notes": "--no-playwright"})

    if capture_tool != "playwright" or not playwright_result:
        probe = http_probe(url, args.timeout)
        steps.append(
            {
                "name": "url_load",
                "status": probe.get("status", "UNKNOWN"),
                "http_status": probe.get("http_status"),
                "actual": probe.get("final_url"),
                "error": probe.get("error"),
            }
        )
        surface = parse_surface(probe.get("html", ""), url)
        if capture_tool != "playwright":
            steps.append(
                {
                    "name": "screenshot",
                    "status": "SKIPPED-SAFE",
                    "notes": "Requires Playwright",
                }
            )
            log_path = run_dir / "logs" / "console.log"
            log_path.write_text(
                "# Console capture unavailable without Playwright\n"
                f"# HTTP probe: {probe.get('http_status')} {probe.get('final_url', url)}\n",
                encoding="utf-8",
            )
            steps.append({"name": "console_log", "status": "partial", "path": rel_to_root(log_path)})

    finished = utc_now()
    overall = "passed"
    if any(s.get("status") == "failed" for s in steps):
        overall = "failed"
    elif any(s.get("status") in ("partial", "SKIPPED-SAFE", "UNKNOWN") for s in steps):
        overall = "partial"

    result = {
        "schemaVersion": "0.1.0",
        "runId": run_dir.name,
        "target_url": url,
        "capture_tool": capture_tool,
        "status": overall,
        "started_at": started,
        "finished_at": finished,
        "steps": steps,
        "surface": surface,
        "artifacts": {
            "screenshot": next((s.get("path") for s in steps if s.get("name") == "screenshot" and s.get("path")), None),
            "console_log": next((s.get("path") for s in steps if s.get("name") == "console_log" and s.get("path")), None),
            "result_json": rel_to_root(run_dir / "result.json"),
        },
    }

    result_path = run_dir / "result.json"
    result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    append_event(
        run_dir,
        {"ts": finished, "type": "capture_completed", "status": overall, "resultPath": rel_to_root(result_path)},
    )
    patch_run_state(run_dir, f"M3 capture done ({overall}): {run_dir.name}")

    print(f"RUN_DIR={rel_to_root(run_dir)}")
    print(f"RESULT={rel_to_root(result_path)}")
    print(f"STATUS={overall}")
    print(f"TOOL={capture_tool}")
    if result["artifacts"].get("screenshot"):
        print(f"SCREENSHOT={result['artifacts']['screenshot']}")
    return 0 if overall != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
