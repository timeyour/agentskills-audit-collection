# Audit Report Format

Use this format for full audit outputs.

## Audit Summary

- Target:
- Target type:
- Audit level:
- Date:
- Verdict:
- Functional score:
- Visual score:
- Deployment readiness:
- Scope:
- Biggest blocker:
- Fix first:

## Severity Scale

| Level | Meaning |
| --- | --- |
| `S0` | Blocks launch or delivery; core workflow unavailable, data/security risk, or production dependency missing. |
| `S1` | Seriously hurts conversion, trust, correctness, privacy, or operational reliability. |
| `S2` | Noticeable UX, workflow, visual, accessibility, or deployment issue; temporary launch possible with known risk. |
| `S3` | Refinement (打磨/润色): copy, layout, or minor interaction. See `docs/severity-standard.md`. |
| `S4` | Future enhancement or benchmark idea. |

## Evidence Split

| Claim | Source Locator | Live Evidence | Confidence | Next Check |
| --- | --- | --- | --- | --- |

## Feature Inventory

| Feature | Start URL | Live Position | Locator | Dependency | Safe To Execute | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Flow Execution Log

| Feature | Steps Run | Expected | Actual | Evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Visual Quality

| Area | Position | Expected | Observed | Severity | Issue ID |
| --- | --- | --- | --- | --- | --- |

## Deployment Readiness

| Requirement | Status | Evidence | Missing/Risk | Fix |
| --- | --- | --- | --- | --- |

## Issue Cards

### <Issue ID> - <S0-S4> - <Title>

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

## Regression Check

- What to retest:
- Required evidence:
- Pass/fail condition:

## Copyable Fix Pack

1. 
2. 
3. 

## Experience Ledger

- Repeated failure patterns:
- Good fix prompts:
- Bad fix prompts:
- Benchmark examples:
- Guardrail updates:

## Final Verdict

- Verdict:
- Ready for next pass:
- Remaining blockers:
