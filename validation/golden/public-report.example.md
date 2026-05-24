# Public Website Audit Report (Example)

> Customer-facing surface. Hides agent/skill mechanics. Derived from [audit-report.example.json](audit-report.example.json).

## Report Metadata

| Field | Value |
| --- | --- |
| Title | Demo App Delivery Readiness |
| Target URL | `http://localhost:5000` (replace with staging for real delivery) |
| Date | 2026-05-22 |
| Audit Mode | mixed |
| Overall Risk | **S2** |
| Evidence quality | MEDIUM |

## Executive Summary

- The demo proves core login and dashboard flows exist for training and report format validation.
- **Cannot be treated as production-ready** — hosting is local-only and browser artifacts are missing.
- Fix physical evidence first, then publish a shareable report URL.
- Mobile, accessibility, and performance were **not tested** (`UNKNOWN`).

## Scorecard

| Area | Status | Notes |
| --- | --- | --- |
| Offer clarity | PASS | Demo purpose visible |
| Primary CTA | PASS | Routes to login |
| Core workflow | PASS | Login + dashboard exist |
| Mobile layout | UNKNOWN | No screenshot pass |
| Visual trust | WARN | Generic demo styling |
| Performance | UNKNOWN | Not measured |
| Accessibility | UNKNOWN | Not measured |
| Deployment readiness | FAIL | Local-only |
| Evidence quality | WARN | No trace/screenshots |

## Top Findings

### [S2] Physical browser artifacts are missing

| Field | Detail |
| --- | --- |
| Evidence | Smoke and source only — no trace, HAR, or screenshots |
| Impact | Third parties cannot verify runtime behavior |
| Fix | Run browser tests; attach redacted artifacts |
| Regression | Open report and confirm artifact links work |

### [S2] Report is not publicly hosted

| Field | Detail |
| --- | --- |
| Evidence | localhost target; report in repo only |
| Impact | Cannot send to client as acceptance deliverable |
| Fix | Publish static HTML (e.g. GitHub Pages) |
| Regression | Open URL in private browser |

## Fix Priority

1. Add physical browser evidence (ISSUE-001)
2. Publish shareable report URL (ISSUE-002)
3. Visual polish (S3)

## Copyable Fix Prompt

```text
Turn this local demo audit into a shareable public website audit report.

Requirements:
- Publish the report as a static HTML page
- Run Playwright on login and dashboard flows
- Attach redacted trace, screenshots, console log, result.json
- Apply DESIGN.md severity and evidence styling
- Mark UNKNOWN where mobile, a11y, or performance were not tested
```

## Regression Check

- [ ] Artifacts present and linked
- [ ] Hosted report loads without local files
- [ ] Critical flows marked PASS only with PHYSICAL evidence

## Lessons

Demo audits must attach browser proof before claiming delivery readiness.

---

Template source: [validation/templates/public-website-audit-report-template.md](../templates/public-website-audit-report-template.md)
