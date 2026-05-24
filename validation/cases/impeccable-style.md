# Case: impeccable.style

## Meta

| Field | Value |
| --- | --- |
| Type | AI design tooling site |
| Source | Public site + open-source repo |
| Full report | `validation/impeccable-style-five-pass-audit.md` |
| Benchmark tags | `five-pass`, `source-vs-runtime`, `tool-product` |

## Why Worth Testing

Validates **five-pass acceptance** and separation of **source evidence vs runtime proof** on a real design-tool product.

## Observable Workflow

Marketing → docs → install/CLI claims → extension/browser flows → screenshot-backed visual QA.

## Typical Findings

- Route/deep-link gaps (`workflow`)
- CLI boundaries documented but not executed (`UNKNOWN` until physical run)
- Docs accurate, runtime unproven (`INFERRED` vs `PHYSICAL-PASS`)

## Evidence Level

| Pass | Focus |
| --- | --- |
| 1 Baseline | `SOURCE` inventory |
| 2 Functional | `LIVE` / `PHYSICAL` |
| 3 Edge | `PHYSICAL` or `SKIPPED-SAFE` |
| 4 Visual/deploy | screenshots + deploy checklist |
| 5 Retest | lessons → guardrails |

## Issue Card Pattern

```text
Title: Install instructions not verified in audit environment
Severity: S2
Area: workflow
Evidence: UNKNOWN — CLI not executed
Fix: Run physical-flow-test install script; attach result.json
Regression: Fresh machine install completes with documented command only
```

## Copyable Fix Pattern

```text
Separate marketing claims from verified runtime:
run install, extension load, and one design-token export path;
attach trace/screenshots; update docs where actual differs from promised.
```

## Reuse

Default benchmark for **`/accept-five`** and five-pass template alignment.
