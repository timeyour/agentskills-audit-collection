# Five-Pass Acceptance Template

Use this template for repeated website/app/product audits.

## Audit Target

- Name:
- URL:
- Source:
- Product category:
- Primary scenario:
- Date:
- Audit level:
- Credentials/demo access:

## Pass 1: Baseline

| Check | Result | Evidence | Unknowns |
| --- | --- | --- | --- |
| URL loads |  |  |  |
| Product category identified |  |  |  |
| Main user scenario clear |  |  |  |
| Main routes/pages listed |  |  |  |
| Feature inventory complete |  |  |  |
| Happy path mapped |  |  |  |

## Pass 2: Functional

| Feature | Start URL | Live Position | Steps | Expected | Actual | Status | Issue ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 1.  |  |  |  |  |

## Pass 3: Edge And Failure

| Edge Case | Feature | Steps | Expected | Actual | Status | Issue ID |
| --- | --- | --- | --- | --- | --- | --- |
| Empty input |  |  |  |  |  |  |
| Invalid input |  |  |  |  |  |  |
| Duplicate action |  |  |  |  |  |  |
| Back/refresh |  |  |  |  |  |  |
| Mobile viewport |  |  |  |  |  |  |
| Auth boundary |  |  |  |  |  |  |

## Pass 4: Visual And Deployment

### Visual Quality

| Area | Position | Expected | Actual | Severity | Issue ID |
| --- | --- | --- | --- | --- | --- |
| First viewport |  |  |  |  |  |
| Hierarchy |  |  |  |  |  |
| Spacing/alignment |  |  |  |  |  |
| Typography/color |  |  |  |  |  |
| Component consistency |  |  |  |  |  |
| Mobile fit |  |  |  |  |  |
| AI slop signal |  |  |  |  |  |

### Deployment Readiness

| Requirement | Status | Evidence | Missing/Risk | Issue ID |
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
| Privacy/terms |  |  |  |  |
| Backup/export/rollback |  |  |  |  |

## Pass 5: Retest And Learn

| Prior Issue | Retest Step | Previous Status | Current Status | Regression? | Lesson |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Issue Cards

### <Issue ID> - <Severity> - <Title>

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
- Retest pass:

## Experience Ledger

### Repeated Failure Patterns

| Pattern | Seen In | Why It Matters | New Guardrail |
| --- | --- | --- | --- |
|  |  |  |  |

### Good Fix Prompts

| Prompt | Worked Because | Reuse When |
| --- | --- | --- |
|  |  |  |

### Bad Fix Prompts

| Prompt | Failed Because | Replace With |
| --- | --- | --- |
|  |  |  |

### Benchmark Examples

| Example | Good Pattern | Use As Comparison For |
| --- | --- | --- |
|  |  |  |

### Guardrail Updates

| Target File | Proposed Change | Reason |
| --- | --- | --- |
| CLAUDE.md |  |  |
| review/references/*.md |  |  |

## Final Verdict

- Verdict:
- Functional score:
- Visual score:
- Deployment readiness:
- Critical blockers:
- Fix first:
- Ready for next pass:
