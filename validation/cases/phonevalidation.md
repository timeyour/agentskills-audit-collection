# Case: PhoneValidation.app

## Meta

| Field | Value |
| --- | --- |
| Type | Commercial micro-tool |
| Source | Made with Lovable |
| Full report | `validation/top-20-vibe-coded-sites-audit.md` |
| Benchmark tags | `monetization`, `credits`, `upload`, `micro-saas` |

## Why Worth Testing

Proves audit value on **small tools with pricing, credits, CSV upload, and data/privacy dependencies** — easier to bound than vague platforms.

## Observable Workflow

Free credits → phone number test → CSV upload promise → pricing → credit accounting → history/export expectations.

## Typical Findings

- Pricing/credits UI vs actual billing backend (`deployment`)
- Upload path may be UI-only (`workflow` S1–S2)
- Privacy policy and data retention (`trust` / `data`)

## Evidence Level

| Check | Level |
| --- | --- |
| Marketing + pricing pages | `SOURCE` / `LIVE` |
| Real charge / credit deduct | `PHYSICAL` or `SKIPPED-SAFE` |
| CSV processing | `PHYSICAL` with redacted sample file |

## Issue Card Pattern

```text
Title: CSV upload advertised but no upload handler
Severity: S1
Area: workflow
Evidence: LIVE — upload control present; submit returns no network activity
Fix: Implement upload endpoint + progress + error states
Regression: Upload 3-row fixture CSV; expect job id in history
```

## Copyable Fix Pattern

```text
Close the commercial loop: credits decrement on success, pricing matches backend,
CSV upload works with validation errors, export/history persists after refresh.
Add privacy copy for phone number retention.
```

## Reuse

Default benchmark for **deployment readiness** + **monetization surface** audits.
