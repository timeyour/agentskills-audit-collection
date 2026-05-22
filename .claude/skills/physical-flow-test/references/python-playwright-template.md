# Python Playwright Template

Use this reference when generating runnable physical flow tests. Keep generated code in the target project's `artifacts/physical-tests/{timestamp}-{flow-name}/` directory, not inside this skill.

## Install And Run

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -q tests/
```

`requirements.txt` should normally contain:

```text
playwright
pytest
python-dotenv
```

## Required Python Pattern

Use Python Playwright sync API primitives, not Node Playwright Test options.

```python
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Error, expect, sync_playwright


load_dotenv()

BASE_URL = os.environ.get("TARGET_URL", "http://localhost:5000")
HEADLESS = os.environ.get("HEADLESS", "true").lower() != "false"
ARTIFACT_ROOT = Path(os.environ.get("ARTIFACT_ROOT", "artifacts"))


def make_paths(flow_name: str) -> dict[str, Path]:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    root = ARTIFACT_ROOT / f"{run_id}-{flow_name}"
    paths = {
        "root": root,
        "traces": root / "traces",
        "screenshots": root / "screenshots",
        "har": root / "har",
        "videos": root / "videos",
        "logs": root / "logs",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def write_console_log(path: Path, events: list[dict]) -> None:
    lines = [
        f"[{event['type']}] {event['text']}"
        for event in events
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_login_flow():
    paths = make_paths("login-flow")
    console_events = []
    result = {
        "flow": "login-flow",
        "target_url": BASE_URL,
        "status": "running",
        "artifacts": {},
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(
            record_video_dir=str(paths["videos"]),
            record_har_path=str(paths["har"] / "network.har"),
        )
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True,
        )
        page = context.new_page()
        page.on(
            "console",
            lambda msg: console_events.append({"type": msg.type, "text": msg.text}),
        )
        page.on(
            "pageerror",
            lambda exc: console_events.append({"type": "pageerror", "text": str(exc)}),
        )

        try:
            page.goto(BASE_URL, wait_until="domcontentloaded")
            expect(page.get_by_role("link", name="Get Started")).to_be_visible()
            page.get_by_role("link", name="Get Started").click()

            expect(page.get_by_label("Username")).to_be_visible()
            page.get_by_label("Username").fill(os.environ["TEST_USERNAME"])
            page.get_by_label("Password").fill(os.environ["TEST_PASSWORD"])
            page.get_by_role("button", name="Sign in").click()

            expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
            expect(page.get_by_text("Signed in as test_user")).to_be_visible()

            result["status"] = "passed"
        except (AssertionError, Error) as exc:
            result["status"] = "failed"
            result["error"] = str(exc)
            failure_path = paths["screenshots"] / "failure.png"
            page.screenshot(path=str(failure_path), full_page=True)
            result["artifacts"]["failure_screenshot"] = str(failure_path)
            raise
        finally:
            trace_path = paths["traces"] / "trace.zip"
            console_path = paths["logs"] / "console.log"
            result_path = paths["root"] / "result.json"

            context.tracing.stop(path=str(trace_path))
            write_console_log(console_path, console_events)

            context.close()
            browser.close()

            result["artifacts"].update({
                "trace": str(trace_path),
                "har": str(paths["har"] / "network.har"),
                "console": str(console_path),
                "videos": str(paths["videos"]),
            })
            write_json(result_path, result)
```

## Generation Notes

- Start tracing with `context.tracing.start(...)` and stop with `context.tracing.stop(path=...)`.
- Record HAR with `browser.new_context(record_har_path=...)`.
- Record video with `browser.new_context(record_video_dir=...)`.
- Screenshot on failure inside `except`.
- Close the context before expecting HAR/video files to be finalized.
- Prefer `expect(...)` assertions over manual sleeps.
- Use `page.wait_for_url`, `expect(locator).to_be_visible`, or response predicates instead of fixed timeouts.
