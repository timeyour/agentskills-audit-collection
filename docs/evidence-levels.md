# Evidence Levels

Evidence discipline is what separates delivery acceptance from vibe checks. Every finding must declare **how** it was observed.

## Primary Evidence Types

| Level | Code | Meaning | Trust for “works in production” |
| --- | --- | --- | --- |
| Source | `SOURCE` | Repo, static export, docs, screenshots supplied by builder | Low alone |
| Live | `LIVE` | Agent visited URL; DOM/navigation observed without full browser artifacts | Medium |
| Physical | `PHYSICAL` | Real browser run with trace, screenshot, HAR, console, or result JSON | High |
| Inferred | `INFERRED` | Pattern-based judgment from source + partial live (e.g. “likely needs CMS”) | Medium-low; must cite reasoning |
| Unknown | `UNKNOWN` | Not observed; cannot claim | None |

## Physical Sub-Statuses (from physical-flow-test)

| Status | Meaning |
| --- | --- |
| `PHYSICAL-PASS` | Browser run passed; artifacts returned |
| `PHYSICAL-FAIL` | Browser run failed; artifacts returned |
| `GENERATED-NOT-RUN` | Test package generated, not executed |
| `STATIC-ONLY` | Source/HTML inspection only |

**Rule:** Do not report a flow as working unless evidence is `PHYSICAL-PASS` or unambiguous `LIVE` with steps and actual result recorded.

## Audit Mode (report metadata)

| Mode | Description |
| --- | --- |
| `source` | Source-level only |
| `live` | Live navigation without full artifact suite |
| `physical-browser` | Playwright or equivalent with artifacts |
| `mixed` | Combination (common for v0.1) |

## Per-Finding Requirements

Each issue card and flow log row should include:

- `evidenceLevel`: primary type
- `evidenceSummary`: one-line observation
- `artifacts`: paths or URLs when `PHYSICAL` (optional array)
- `reproduction`: steps, URL, selector/label, input (required for S0–S2)

## Scorecard / Verdict Interaction

| Evidence quality | Typical verdict cap |
| --- | --- |
| Mostly `SOURCE` + `INFERRED` | Cannot claim “delivery ready” |
| `LIVE` without failure-path tests | “Pass with notes” at best |
| `PHYSICAL` on critical paths | Eligible for “ready” if no S0/S1 open |

## Gap Markers

Same as severity doc: `UNKNOWN`, `NOT_APPLICABLE`, `SKIPPED-SAFE` — use instead of omitting fields.

## Schema

See `evidence` and `issueCards[].evidence` in [audit-report.schema.json](../schemas/audit-report.schema.json).

## Artifact Storage

Runtime files belong under `validation/artifacts/` (or project-local `artifacts/` during runs). See [validation/artifacts/README.md](../validation/artifacts/README.md).
