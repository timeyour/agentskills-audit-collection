---
name: physical-flow-test
description: Generate executable real-browser flow tests using Python Playwright from business flows. Use when cognitive audit, flow-test, audit, or accept-five needs physical browser proof for CTA, form, auth, upload, checkout, dashboard, production, staging, or local workflows.
---

# Physical Flow Test

Use this skill to turn business flows into real executable browser tests.

```text
business flow -> harness decomposition -> Python Playwright package -> real execution -> artifacts -> regression check -> lessons
```

This skill must not guess whether a workflow works. It produces tests that a user, CI job, or real browser environment must execute.

## When To Use

Use `/physical-flow-test` when the user needs to:

1. Verify critical user paths with real browser clicks.
2. Upgrade `/flow-test` from static inspection to physical execution.
3. Generate repeatable regression tests for important workflows.
4. Validate staging, production, or local environments with real network behavior.
5. Collect physical evidence for `/audit` or `/accept-five`.
6. Check CTA, forms, login, signup, dashboard actions, uploads, exports, checkout, or booking flows.
7. Convert business-level acceptance criteria into runnable browser tests.

Prefer `/harness` first. If `/harness` is unavailable, perform a minimal harness decomposition inside this skill before generating code.

## Core Rules

1. Never claim a workflow works without real execution evidence.
2. Decompose the business goal into minimal executable units before writing tests.
3. Generate Python tests using `pytest` and `playwright.sync_api`.
4. Use `python -m pytest -q tests/`, not the Node/TypeScript Playwright runner, unless the user explicitly asks for TypeScript.
5. Every generated test must include trace capture, screenshot on failure, HAR/network capture, video when supported, console log capture, clear assertions, and safe failure handling.
6. Output generated packages under `./artifacts/physical-tests/{timestamp}-{flow-name}/`.
7. Use the audit permission model before generating tests for production, authenticated, payment, deletion, upload, admin, or private-data flows.
8. Mark payment, deletion, irreversible submission, production email/SMS sending, and real purchase flows as `SKIPPED-SAFE` unless explicitly allowed.
9. Never hardcode secrets, passwords, tokens, or cookies. Use environment variables and `.env.example` placeholders.
10. Require artifact redaction before sharing HAR, trace, screenshots, video, or console logs.
11. Use `S0-S4` severity and preserve the shared output shape.

## Workflow

1. Intake and scope: identify flow name, URL or local command, environment, browser target, auth needs, test account, high-risk actions, expected results, and required artifacts.
2. Surface and permission check: use any available web surface map, apply the permission model, and mark unsafe units `SKIPPED-SAFE`.
3. Harness decomposition: map business goal -> user intent -> page/route -> action -> locator -> expected result -> checkpoint -> failure signal.
4. Generate test package: create `README.md`, `requirements.txt`, `.env.example`, `run-tests.sh`, `tests/test_{flow_name}.py`, and artifact directories.
5. Execution instruction: provide exact commands for installing Python dependencies, installing Chromium, and running pytest.
6. Artifact review: inspect returned trace, screenshots, HAR, console logs, video, and result JSON against expected behavior.
7. Regression and lessons: convert findings into regression checks, locator rules, auth/session rules, network dependency rules, timeout rules, and safe-skip rules.

## References

- `references/python-playwright-template.md`
- `references/artifact-schema.md`
- `references/safe-execution-policy.md`
- `references/locator-policy.md`
- `references/regression-lessons-ledger.md`
- `../audit/references/permission-model.md`
- `../audit/references/web-surface-discovery.md` when a surface map is needed before test generation

## Output Format

```text
Physical Flow Test Summary
Target Flow:
Environment:
Harness Used:
Execution Mode:
Risk Level:

Scope
Evidence
Findings
Severity
Reproduction
Fix Suggestion
Regression Check
Lessons
```

## Anti-Patterns

- Claiming a workflow works without physical execution.
- Mentally simulating browser clicks.
- Generating tests without requiring execution.
- Testing only happy paths.
- Missing trace, HAR, video, console log, or failure screenshot capture.
- Hardcoding credentials.
- Sharing raw HAR files without redaction.
- Running destructive production actions by default.
- Using brittle selectors when accessible locators exist.
- Treating docs, marketing copy, source code, or screenshots as proof of working behavior.
