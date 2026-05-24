# Live Functional Audit Template

Use this template when testing every feature of a website or web app.

## Audit Summary

- Site:
- Source:
- Platform:
- Audit date:
- Auditor:
- Audit level: source-level / visual-level / clicked-flow / authenticated-flow
- Overall verdict: PASS / PASS WITH NOTES / FAIL
- Functional score: 0-100
- Visual score: 0-100
- Deployment readiness: READY / PARTIAL / NOT READY / UNKNOWN
- Biggest blocker:
- Fix first:

## Feature Inventory

| Feature | Start URL | Live Position | Locator | Dependency | Safe To Execute | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Navigation |  |  |  |  |  |  |
| Primary CTA |  |  |  |  |  |  |
| Contact/lead form |  |  |  | email/backend |  |  |
| Signup/login |  |  |  | auth/database |  |  |
| Search/filter |  |  |  | data/API |  |  |
| Dashboard/admin |  |  |  | auth/database |  |  |
| Upload/download/export/copy |  |  |  | storage/API |  |  |
| Checkout/payment |  |  |  | payment provider |  |  |

## Flow Execution Log

| Feature | Steps Run | Expected | Actual | Evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1.  |  |  |  |  |  |

Status values:

- `PASS`
- `PARTIAL`
- `FAIL`
- `UNKNOWN`
- `SKIPPED-SAFE`

## Visual Quality Review

| Area | Position | Expected Quality | Observed Issue | Severity | Fix |
| --- | --- | --- | --- | --- | --- |
| First viewport |  | Clear offer and CTA |  |  |  |
| Navigation |  | Predictable and readable |  |  |  |
| Typography |  | Clear hierarchy |  |  |  |
| Spacing/alignment |  | Consistent layout |  |  |  |
| Mobile |  | No overlap/cropping |  |  |  |
| Imagery/assets |  | Relevant and loaded |  |  |  |
| Trust/conversion |  | Proof and clear next step |  |  |  |

## Deployment Readiness

| Requirement | Status | Evidence | Missing/Risk | Fix |
| --- | --- | --- | --- | --- |
| Domain + SSL |  |  |  |  |
| Env vars |  |  |  |  |
| Backend/API |  |  |  |  |
| Database |  |  |  |  |
| Auth/session |  |  |  |  |
| Email/SMS |  |  |  |  |
| Storage |  |  |  |  |
| Payment |  |  |  |  |
| CMS/admin |  |  |  |  |
| Analytics |  |  |  |  |
| Error monitoring |  |  |  |  |
| SEO/sitemap/robots |  |  |  |  |
| Privacy/terms/compliance |  |  |  |  |
| Backup/export/rollback |  |  |  |  |

## Issue Cards

### <Severity> - <Issue Title>

- Area:
- URL:
- Live position:
- Locator:
- Workflow step:
- Expected:
- Actual:
- Evidence:
- Problem:
- Likely cause:
- Fix:
- Copy prompt:
- Validation:

## Copyable Fix Pack

1. 
2. 
3. 

## Open-Source Tool Evidence

| Tool | Command/Method | Result | File/Link |
| --- | --- | --- | --- |
| Playwright |  |  |  |
| axe-core |  |  |  |
| Lighthouse |  |  |  |
| Link checker |  |  |  |
| HTML/CSS validator |  |  |  |
