# Demo Website Audit Report

Target URL: `http://localhost:5000`
Date: 2026-05-22
Audit Mode: mixed source and local demo smoke
Overall Risk: S2

This sample report shows how AgentSkills findings should be packaged for a website owner. It is not a production audit. It uses the tiny demo app in `examples/physical-flow-demo/` as a report-format example.

## Executive Summary

- The demo site has a clear homepage CTA, fake login flow, dashboard, task form, and failure states.
- The main flows are suitable for demonstrating public audit reports.
- The app still needs stronger production framing before it could represent a real client-ready site.
- The highest-value next step is adding physical browser artifacts: screenshots, trace, console log, and result JSON.

## Scorecard

| Area | Status | Notes |
| --- | --- | --- |
| Offer clarity | PASS | Demo purpose is visible. |
| Primary CTA | PASS | Homepage CTA points to login. |
| Core workflow | PASS | Login and dashboard route exist. |
| Failure state | PASS | Login and task creation include failure states. |
| Mobile layout | WARN | Needs screenshot-backed verification. |
| Visual trust | WARN | Demo styling is adequate but not product-grade. |
| Performance | UNKNOWN | No browser performance pass attached. |
| Accessibility | UNKNOWN | No accessibility pass attached. |
| Deployment readiness | WARN | Demo app is local-only. |
| Evidence quality | WARN | Source and smoke evidence exist; physical artifacts are still missing. |

## Top Findings

### [S2] Physical browser artifacts are missing

| Field | Detail |
| --- | --- |
| Scope | Demo report evidence |
| Evidence | Source files and smoke checks exist, but no trace, HAR, video, or screenshots are attached. |
| Impact | A reviewer can understand the flow, but cannot independently inspect browser runtime behavior. |
| Fix Suggestion | Run `/physical-flow-test` against the demo app and attach redacted trace, screenshots, console log, and result JSON. |
| Regression Check | Re-open the HTML report and confirm artifact links are present and match the tested flow. |

### [S2] Report is local-only

| Field | Detail |
| --- | --- |
| Scope | Public delivery |
| Evidence | Target URL is `localhost`, and the static report is stored locally. |
| Impact | The report is not yet shareable with an external website owner. |
| Fix Suggestion | Publish reports through GitHub Pages or a lightweight hosted site. |
| Regression Check | Open the hosted report URL in a private browser session and verify it loads without local files. |

### [S3] Visual style is serviceable but generic

| Field | Detail |
| --- | --- |
| Scope | Demo app presentation |
| Evidence | The app uses simple Bootstrap-style layout and generic demo copy. |
| Impact | It proves workflow structure, but not premium report or audit workbench design. |
| Fix Suggestion | Apply `DESIGN.md` rules to the report surface and demo pages. |
| Regression Check | Compare before/after screenshots and confirm typography, spacing, and severity cards are consistent. |

## Evidence

| Evidence Type | Status | Notes |
| --- | --- | --- |
| SOURCE | available | Demo app files exist under `examples/physical-flow-demo/`. |
| LIVE | partial | Local smoke checks passed. |
| PHYSICAL | missing | No redacted Playwright trace, HAR, video, or screenshots attached. |
| INFERRED | limited | Visual quality comments are based on source/report shape, not full screenshot QA. |
| UNKNOWN | present | Mobile, accessibility, and performance need dedicated passes. |

## Copyable Fix Prompt

```text
Turn this local demo audit into a shareable public website audit report.

Requirements:
- Publish the report as a static HTML page.
- Add links to redacted screenshots, trace, console log, and result JSON.
- Preserve the S0-S4 severity model.
- Keep the report readable for a non-technical website owner.
- Include a regression check for every finding.
```

## Regression Check

```text
1. Open the hosted report URL.
2. Confirm the target URL, date, risk level, and findings are visible.
3. Open each evidence link.
4. Confirm every S1/S2 issue has a fix suggestion and retest step.
5. Re-run the audited flow after fixes and update the status.
```

## Lessons

- The public-facing product is the report, not the skill file.
- A useful report must be shareable without explaining Claude Code.
- Physical artifacts turn a report from opinion into evidence.
