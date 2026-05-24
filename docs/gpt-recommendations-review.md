# GPT Recommendations vs Repository State

Review date: 2026-05-24. Compares the external GPT integration plan with this checkout.

## Verdict

**GPT’s diagnosis is largely correct.** The upstream repo already encodes most of the v0.1 integration line (schema, docs, validation layers, golden examples). The main gap was **executable Workbench UI** (M2): contracts existed; a data-driven report viewer was missing until `workbench/report/`.

## P0 — Unified acceptance standard

| GPT ask | Status | Location |
| --- | --- | --- |
| `audit-report.schema.json` | Done | `schemas/audit-report.schema.json` |
| S0–S4 single standard | Done | `docs/severity-standard.md` |
| Skill routing (`/audit` entry) | Done | `docs/skill-routing-map.md` |
| Evidence levels | Done | `docs/evidence-levels.md` |
| v0.1 scope freeze | Done | `docs/v0.1-scope.md` |

**GPT was right:** without one schema and one severity table, skills would keep diverging. `REQUIREMENTS.md` and the schema already align on required fields and gap markers (`UNKNOWN`, `NOT_APPLICABLE`, `SKIPPED-SAFE`).

## P1 — PRODUCT MVP & DESIGN → UI

| GPT ask | Status | Notes |
| --- | --- | --- |
| MVP feature set in PRODUCT | Documented | `PRODUCT.md` unchanged in meaning |
| Scoped UI rules | Done | `docs/workbench-ui-spec.md` |
| Component contracts | Done | `workbench/components/README.md` |
| Real UI components | **Partial → M2** | `workbench/report/index.html` renders golden JSON; no React app yet |
| `demo-site-audit.html` | Exists | Uses **different** palette (pre-DESIGN); public-report style, not internal workbench |

**GPT was right** about scoped CSS. **Correction:** `reports/demo-site-audit.html` is not the workbench — use `workbench/report/` for schema-driven internal view.

## P1 — validation/ reorganization

| GPT ask | Status |
| --- | --- |
| `templates/` | Done — 4 canonical templates |
| `cases/` | Done — 4 golden case briefs |
| `artifacts/` | Done — README + placeholder |
| `golden/` | Done — `audit-report.example.json`, `public-report.example.md` |
| Root template duplicates | Kept with “canonical copy” pointers (backward links) |

**GPT was right** that validation was a “material pile”; structure is now three-layer + historical `*.md` batch reports preserved.

## P2 — CASE_STUDIES

| GPT ask | Status |
| --- | --- |
| Structured case format | Partial — `CASE_STUDIES.md` uses bullet sections; `validation/cases/*.md` has fuller briefs |

Optional follow-up: trim `CASE_STUDIES.md` to index-only linking to `validation/cases/`.

## Milestones

| Milestone | GPT | This repo |
| --- | --- | --- |
| M0 docs + schema | Required | Done |
| M1 validation layout | Required | Done |
| M2 workbench UI | Required | `workbench/report/` (static); framework app still optional |
| M1.5 live viewer | Not in original GPT list | Done — `workbench/live/` + `audit-run.schema.json` |
| M3 semi-auto checks | Done | `scripts/audit_capture.py`, `docs/m3-capture-workflow.md` |
| M4 public HTML export | Done | `scripts/export_public_report.py` regenerates `reports/demo-site-audit.html` |
| M5 README as product entry | Done | 30s pitch + `docs/screenshots/*.svg` wireframes |

## Audience choice (developer vs customer)

GPT recommended **customer acceptance reports first**. `docs/v0.1-scope.md` records the same bet. Internal workbench + public report template serve both; prioritize exporting `validation/golden/public-report.example.md` for stakeholders.

## What to do next (actionable)

1. Run report viewer locally and validate a real `/audit` JSON output against the schema.
2. Add `scripts/validate_audit_report.py` (optional) or CI step using `jsonschema`.
3. Regenerate `reports/demo-site-audit.html` from golden JSON or align tokens with DESIGN.md.
4. M3: wire URL load, console, screenshot paths into `validation/artifacts/<runId>/`.
5. M5: README screenshot + one-liner above the fold.

## Skills integrity

GPT correctly said: **do not put scripts inside `.claude/skills/`**. Scripts remain in `scripts/` and `validation/`; skills stay instruction-only.
