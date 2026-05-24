# Case: Committed Citizens

## Meta

| Field | Value |
| --- | --- |
| Type | Consulting website |
| Source | v0 / Vercel Community |
| Full report | `validation/vibe-sites-live-position-retest.md` |
| Benchmark tags | `cms-gap`, `deployment`, `content-ops` |

## Why Worth Testing

Turns vague “needs a CMS” into a **concrete deployment-readiness issue** with editorial workflow impact.

## Observable Workflow

Marketing pages → `/insights` articles → contact/lead paths → team publishing expectation.

## Typical Findings

- `/insights` hard-coded articles (`deployment` S1–S2)
- No preview/publish pipeline for non-developers
- Env vars for CMS provider missing

## Evidence Level

| Finding | Level |
| --- | --- |
| Hard-coded articles in source | `SOURCE` |
| No admin route | `LIVE` or `INFERRED` with file cite |
| CMS connected | `PHYSICAL` only after staging proof |

## Issue Card Pattern

```text
Title: Insights section not editable without code deploy
Severity: S1
Area: deployment
Evidence: SOURCE — articles hard-coded in repo
Impact: Team cannot publish; stale content risk
Fix: Add headless CMS schema, roles, migration, preview URL, env vars
Regression: Non-dev publishes draft → preview → live without redeploy
```

## Copyable Fix Pattern

```text
Add a CMS plan for /insights: content schema, author/editor roles,
migrate existing hard-coded articles, preview flow, deployment env vars, rollback plan.
```

## Reuse

Default benchmark for **deploy-check** and public report “Fix Priority” sections.
