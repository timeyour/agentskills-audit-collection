# Artifact Schema

Use this schema for generated test packages and returned execution evidence.

## Generated Package Layout

```text
artifacts/physical-tests/{timestamp}-{flow-name}/
  README.md
  requirements.txt
  .env.example
  run-tests.sh
  tests/
    test_{flow_name}.py
  artifacts/
    {run-id}-{flow-name}/
      traces/
        trace.zip
      screenshots/
        failure.png
        checkpoint-{step}.png
      har/
        network.har
        network.redacted.har
      videos/
        *.webm
      logs/
        console.log
      result.json
```

## Naming Rules

- `timestamp`: UTC, `YYYYMMDDTHHMMSSZ`.
- `flow-name`: lowercase kebab case, for example `login-flow`.
- `run-id`: unique UTC run timestamp.
- Screenshots: `checkpoint-{step}.png` or `failure.png`.
- HAR files: raw `network.har`, redacted `network.redacted.har`.
- Result file: always `result.json`.

## Result JSON

```json
{
  "flow": "login-flow",
  "target_url": "https://staging.example.com",
  "environment": "staging",
  "status": "passed",
  "started_at": "2026-05-21T12:00:00Z",
  "finished_at": "2026-05-21T12:00:09Z",
  "steps": [
    {
      "name": "open homepage",
      "status": "passed",
      "expected": "Get Started CTA is visible",
      "actual": "CTA was visible"
    }
  ],
  "artifacts": {
    "trace": "artifacts/20260521T120000Z-login-flow/traces/trace.zip",
    "har": "artifacts/20260521T120000Z-login-flow/har/network.redacted.har",
    "console": "artifacts/20260521T120000Z-login-flow/logs/console.log",
    "videos": "artifacts/20260521T120000Z-login-flow/videos/"
  }
}
```

## Evidence Levels

- `PHYSICAL-PASS`: real browser run passed with returned artifacts.
- `PHYSICAL-FAIL`: real browser run failed with returned artifacts.
- `GENERATED-NOT-RUN`: test package generated but not executed.
- `STATIC-ONLY`: finding comes from source or HTML inspection only.
- `UNKNOWN`: evidence is missing or cannot be reproduced.

Do not report a flow as working unless evidence level is `PHYSICAL-PASS`.
