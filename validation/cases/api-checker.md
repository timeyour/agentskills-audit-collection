# Case: API Checker

## Meta

| Field | Value |
| --- | --- |
| Type | Interactive developer tool |
| Source | v0 / Vercel Community |
| Full report | `validation/top-20-vibe-coded-sites-audit.md` |
| Benchmark tags | `workflow-mapping`, `position-aware`, `developer-tool` |

## Why Worth Testing

Best proof that AI-built products can expose **exact, testable workflow positions** — not just polished landing pages.

## Observable Workflow

Request configuration → endpoint input → HTTP method → auth helpers → query params → test action → response panel → history → code generator.

## Typical Findings

- Strong visible flow map for `/flow-test`
- Gaps appear when auth, rate limits, or backend proxies are not documented
- Visual QA: density and hierarchy on tool panels

## Evidence Level

| Pass | Typical level |
| --- | --- |
| Source | `SOURCE` |
| Live click-through | `LIVE` |
| Automated API call test | `PHYSICAL` when Playwright + network HAR attached |

## Issue Card Pattern

```text
Title: Primary test action unreachable from default view
Severity: S1
Area: workflow
Evidence: LIVE — CTA visible but request panel does not open
Fix: Wire test button to active request builder state
Regression: Run flow-test step 3; expect response panel within 2s
```

## Copyable Fix Pattern

```text
Map every visible control on the API tester to a named workflow step.
Add loading, error, and empty states for the response panel.
Document auth header injection and export the flow as a checklist for regression.
```

## Reuse

Use as default benchmark when validating **feature inventory** and **flow execution log** fields in `audit-report.schema.json`.
