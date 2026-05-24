# Workbench UI Specification (v0.1)

The Audit Workbench is a **pre-launch diagnostic console**, not a marketing site. Visual source of truth: [DESIGN.md](../DESIGN.md).

## Engineering Rules (non-negotiable)

```text
1. All Audit Workbench UI styles MUST be scoped (CSS modules, shadow DOM, or prefixed class namespace e.g. .asw-*).
2. NEVER globally override button, h1, p, table, or form elements.
3. All sizes, colors, radii, and spacing MUST come from DESIGN.md tokens.
4. Components MUST accept severity, status, and evidenceLevel via props — no hardcoded palette in leaf components.
5. Prefer data-driven render from schemas/audit-report.schema.json.
```

## Layout (three-column + footer)

```text
┌─────────────────────────────────────────────────────────────────┐
│ AuditHeader — URL, overall risk, pass #, evidence grade, score   │
├──────────────┬────────────────────────────┬─────────────────────┤
│ Feature      │ FlowExecutionTimeline      │ IssueCard stack     │
│ Inventory    │ (current step, status)     │ + CopyPromptBox     │
│ Table        │                            │ + RegressionChecklist│
├──────────────┴────────────────────────────┴─────────────────────┤
│ EvidenceTable — artifacts, levels, links                         │
└─────────────────────────────────────────────────────────────────┘
```

## Components

| Component | Priority | Data source | Notes |
| --- | --- | --- | --- |
| `AuditHeader` | P0 | `target`, `scope`, `finalVerdict` | Summary, risk badge, audit mode |
| `FeatureInventoryTable` | P0 | `featureInventory[]` | Safe-to-execute, status, locator |
| `FlowExecutionTimeline` | P0 | `flowExecutionLog[]` | Vertical timeline; highlight current |
| `IssueCard` | P0 | `issueCards[]` | evidence, impact, fix, regression |
| `SeverityBadge` | P0 | `severity` prop | Maps to DESIGN severity tokens |
| `EvidenceTable` | P0 | `evidence[]` | SOURCE / LIVE / PHYSICAL / … |
| `CopyPromptBox` | P1 | `copyableFixPack` | One-click copy |
| `RegressionChecklist` | P1 | `regressionChecks[]` | Checkbox list for retest |

Component contracts: [workbench/components/README.md](../workbench/components/README.md).

## Props Conventions

```typescript
// Illustrative — implement in chosen framework later
type Severity = 'S0' | 'S1' | 'S2' | 'S3' | 'S4';
type EvidenceLevel = 'SOURCE' | 'LIVE' | 'PHYSICAL' | 'INFERRED' | 'UNKNOWN';
type FlowStatus = 'PASS' | 'PARTIAL' | 'FAIL' | 'UNKNOWN' | 'SKIPPED-SAFE';
```

## Live mode (v0.1.5)

Real-time audit uses **`schemas/audit-run.schema.json`** (in-progress) separate from final **`audit-report.schema.json`**.

| UI region | Live data |
| --- | --- |
| Left rail | `stages[]` with pending / in_progress / completed |
| Center | `activeAnnotation` + current stage `steps[]` |
| Right | `findingsPreview[]` + `run-events.ndjson` tail |
| Header | `progress.label`, `target.url`, poll `updatedAt` |

Implementation: [workbench/live/index.html](../workbench/live/index.html) — poll `run-state.json` every 1s.

See [live-audit-workflow.md](live-audit-workflow.md).

## v0.1 Delivery

- **No framework installed** for final report view (M2).
- **Live HTML viewer** ships at `workbench/live/`.
- Golden render target: load `validation/golden/audit-report.example.json` in a future `workbench/app`.
- Static alternative: `reports/demo-site-audit.html` demonstrates public report styling.

## Public vs Internal

| Surface | Audience | Hides |
| --- | --- | --- |
| Workbench | Auditor / builder | — |
| Public report | Client / stakeholder | Agent mechanics, raw skill names |

Template: `validation/templates/public-website-audit-report-template.md`.
