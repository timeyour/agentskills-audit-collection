# Skill Routing Map

AgentSkills uses **one orchestrator** and **focused sub-modules**. Do not add parallel “full audit” skills; extend references or sub-flows instead.

## Entry Points

| Skill | Role | When to call |
| --- | --- | --- |
| `/audit` | **Primary orchestrator** | Default for URL/project delivery acceptance |
| `/harness` | Pre-audit decomposition | Complex business workflows before build or audit |
| `/skill-study` | External learning | Ingest repos, trend reports, competitor workflows |

## Sub-Flows (callable standalone or from `/audit`)

| Skill | Module | Output focus |
| --- | --- | --- |
| `/flow-test` | Live functional testing | Feature inventory, flow execution log, expected vs actual |
| `/physical-flow-test` | Browser proof | Playwright package + trace/HAR/screenshot artifacts |
| `/visual-qa` | Craft & slop | Visual findings, aesthetic issues, responsive/trust |
| `/ai-product-audit` | Product pattern fit | Scenario clarity, conversion readiness |
| `/deploy-check` | Production readiness | Env, auth, DB, CMS, analytics, monitoring gaps |
| `/accept-five` | Five-pass acceptance | Pass ledger, lessons, guardrail updates |
| `/agent-diagnose` | Adversarial reliability | Agent/workflow failure modes |

## Recommended Flow

```text
[optional] /skill-study  →  [optional] /harness
         ↓
      /audit  ─────────────────────────────────────┐
         │                                          │
         ├── /flow-test                             │
         ├── /physical-flow-test (critical paths)   │
         ├── /visual-qa                             │
         ├── /ai-product-audit (when product-fit)   │
         ├── /deploy-check                          │
         └── /accept-five (important audits)        │
         ↓                                          │
   audit-report (schema)  ←────────────────────────┘
         ↓
   public report template  OR  workbench UI (future)
```

## Routing Rules

1. **Never skip scope.** State what was inspected and what was `SKIPPED-SAFE`.
2. **Sub-skills must emit schema-shaped fragments** that `/audit` merges; standalone runs should still produce full report sections with explicit gaps.
3. **Severity always uses `docs/severity-standard.md`** — no local redefinitions.
4. **Evidence always uses `docs/evidence-levels.md`** — separate source, live, physical, inferred, unknown.
5. **Instruction-only:** skills live in `.claude/skills/`; scripts run in host project or `validation/`, not inside skill folders.

## Anti-Patterns

| Do not | Do instead |
| --- | --- |
| Add `/full-audit-v2` | Extend `/audit` references |
| Duplicate S0–S4 tables in each SKILL.md | Link to `docs/severity-standard.md` |
| Claim PASS without physical evidence when runtime proof is required | Mark `UNKNOWN` or run `/physical-flow-test` |
| Hide missing fields | `UNKNOWN` / `NOT_APPLICABLE` / `SKIPPED-SAFE` |

## File Locations

```text
.claude/skills/audit/SKILL.md              → orchestrator
.claude/skills/flow-test/                  → functional module
.claude/skills/physical-flow-test/         → browser artifacts
.claude/skills/visual-qa/                  → visual module
.claude/skills/deploy-check/              → deployment module
.claude/skills/accept-five/                → five-pass module
schemas/audit-report.schema.json           → unified output contract
validation/templates/                      → human-readable report shells
```
