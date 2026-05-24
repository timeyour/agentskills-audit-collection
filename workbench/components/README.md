# Workbench Components (contracts)

Implement when adding a frontend (Next.js, Vite, etc.). All components are **presentational**; data from `AuditReport` type generated from schema.

## AuditHeader

| Prop | Type | Required |
| --- | --- | --- |
| `target` | object | yes |
| `scope` | object | yes |
| `finalVerdict` | object | yes |
| `evidenceGrade` | string | yes |

Renders: URL, audit mode, overall risk badge, evidence grade, pass indicator, summary paragraph.

## FeatureInventoryTable

| Prop | Type |
| --- | --- |
| `items` | `featureInventory[]` |
| `onSelectFeature` | `(id: string) => void` optional |

Renders sortable table; status uses flow status colors (not severity).

## FlowExecutionTimeline

| Prop | Type |
| --- | --- |
| `entries` | `flowExecutionLog[]` |
| `activeIndex` | number optional |

Renders vertical timeline; each entry shows steps[], expected, actual, EvidenceLevel chip, StatusBadge.

## IssueCard

| Prop | Type |
| --- | --- |
| `issue` | `issueCard` |

Subcomponents: SeverityBadge, evidence block, reproduction (mono), fix, CopyPromptBox (single issue).

## SeverityBadge

| Prop | Type |
| --- | --- |
| `severity` | S0–S4 |
| `size` | sm \| md optional |

Maps to DESIGN.md `severity-s0` … `severity-s4`.

## EvidenceTable

| Prop | Type |
| --- | --- |
| `items` | evidence summary items |
| `artifactLinks` | string[] optional |

Columns: type, status, notes, links.

## CopyPromptBox

| Prop | Type |
| --- | --- |
| `prompt` | string |
| `label` | string optional |

Read-only textarea + copy button; scoped `.asw-copy-box`.

## RegressionChecklist

| Prop | Type |
| --- | --- |
| `checks` | `regressionChecks[]` |
| `onToggle` | optional for interactive retest |

Checkbox + issueId + check text; status pending/passed/failed.

## StatusBadge (shared)

| Prop | Type |
| --- | --- |
| `status` | FlowStatus or PASS/WARN/FAIL for scorecard |

Separate from SeverityBadge — do not reuse colors.

## File stubs (M2)

When scaffolding:

```text
workbench/app/
  components/
    AuditHeader.tsx
    FeatureInventoryTable.tsx
    FlowExecutionTimeline.tsx
    IssueCard.tsx
    SeverityBadge.tsx
    EvidenceTable.tsx
    CopyPromptBox.tsx
    RegressionChecklist.tsx
  styles/
    tokens.css      # from DESIGN.md
    workbench.css   # .asw-workbench scoped only
```
