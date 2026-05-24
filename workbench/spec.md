# Workbench Application Spec (M2 target)

## Input

- Primary: JSON file conforming to [schemas/audit-report.schema.json](../schemas/audit-report.schema.json)
- Default fixture: [validation/golden/audit-report.example.json](../validation/golden/audit-report.example.json)

## Routes (minimal)

| Route | Purpose |
| --- | --- |
| `/` | Load report JSON (file picker or query `?report=`) |
| `/export` | Generate markdown from public template (M4) |

## Page Regions

### 1. AuditHeader

- `target.url`, `target.productType`, `target.auditMode`
- `finalVerdict.overallRisk` → SeverityBadge
- `evidence.overallGrade`
- `scope.auditPass` / 5 if present
- `finalVerdict.summary`

### 2. Left — FeatureInventoryTable

Columns: name, startUrl, livePosition, safeToExecute, status (badge).

Sort: failed/skipped first.

### 3. Center — FlowExecutionTimeline

Vertical timeline from `flowExecutionLog[]`:

- step list
- expected vs actual
- status color by FlowStatus
- highlight row matching “current” agent step (optional live mode M3)

### 4. Right — Issues + Fixes

- Stack of IssueCard
- CopyPromptBox bound to `copyableFixPack`
- RegressionChecklist from `regressionChecks[]`

### 5. Footer — EvidenceTable

Rows from `evidence.items[]` plus artifact links aggregated from issue cards.

## Styling

Import tokens from DESIGN.md YAML (generate CSS variables at build time or hand-map once).

Namespace: `.asw-workbench` on root container.

```css
/* Example — all rules must live under .asw-workbench */
.asw-workbench .asw-btn-primary { ... }
```

## Validation

- [ ] Golden JSON renders without console errors
- [ ] S0–S4 badges use token colors only
- [ ] No global `button` / `h1` overrides
- [ ] Every issue card shows reproduction + regression
- [ ] Missing optional fields show UNKNOWN, not blank

## Out of Scope for M2 Skeleton

- WebSocket live agent feed
- Playwright embedded runner
- Auth to target sites

See [docs/v0.1-scope.md](../docs/v0.1-scope.md).
