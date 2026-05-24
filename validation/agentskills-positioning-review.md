# AgentSkills Positioning Review

Date: 2026-05-19

## Verdict

The user's latest positioning is accepted.

AgentSkills should be described as an AI product delivery acceptance system, not a coding skill pack.

## Adopted Definition

AgentSkills turns vibe-coded websites and products from "looks done" into deliverables that are:

- tested step by step;
- evidence-backed;
- reproducible;
- risk-aware;
- fixable with copyable prompts;
- retestable;
- reusable as future guardrails and benchmarks.

## Adopted Architecture

```text
skill-study
    ↓
audit
    ↓
flow-test / visual-qa / deploy-check
    ↓
accept-five
    ↓
agent-diagnose
    ↓
rules memory / benchmark library
```

## Adopted Output Shape

Every skill should preserve this structure when applicable:

1. Scope
2. Evidence
3. Findings
4. Severity
5. Reproduction
6. Fix Suggestion
7. Regression Check
8. Lessons

## Adopted Severity Scale

| Level | Meaning |
| --- | --- |
| `S0` | Blocks launch or delivery; core workflow unavailable, data/security risk, or production dependency missing. |
| `S1` | Seriously hurts conversion, trust, correctness, privacy, or operational reliability. |
| `S2` | Noticeable UX, workflow, visual, accessibility, or deployment issue; temporary launch possible with known risk. |
| `S3` | Refinement (打磨/润色): copy, layout, or minor interaction. |
| `S4` | Future enhancement or benchmark idea. |

## Main Guardrail

Do not let AgentSkills become a collection of nice command names.

Each skill must produce evidence that someone else can understand, reproduce, fix, retest, and learn from.

## Implemented Updates

- Updated `README.md` with positioning, architecture, output shape, and `S0-S4` scale.
- Updated `REQUIREMENTS.md` with unified output and severity requirements.
- Updated `CLAUDE.md` with governance rules and an ADR.
- Updated `PRODUCT.md` and `DESIGN.md`.
- Updated skill outputs and audit references to use `S0-S4`.

## Next Real Validation

The next useful proof is not another concept expansion. It should be one complete audit report for a real target:

```text
Project: <target site>
Verdict: do not launch / can gray release / can deliver
Core issues:
S0 blockers:
Reproduction steps:
Fix prompts:
Regression checks:
Lessons:
```
