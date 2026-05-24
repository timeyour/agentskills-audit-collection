# Severity Standard (S0–S4)

**Canonical definition for the entire repository.** Skills, templates, schema, and UI must reference this file — do not redefine severity elsewhere.

## Levels

| Level | Name | Meaning | Typical examples |
| --- | --- | --- | --- |
| **S0** | Blocker | Blocks launch or delivery | Core workflow down; data leak; missing prod dependency; auth bypass |
| **S1** | Critical | Seriously hurts conversion, trust, correctness, privacy, or ops | Broken primary CTA; misleading pricing; PII exposure; no error handling on payment |
| **S2** | Major | Noticeable UX, workflow, visual, a11y, or deployment issue; launch possible with known risk | Mobile overlap hides CTA; form succeeds with no feedback; missing env documented but not wired |
| **S3** | Minor | Polish, copy, layout, minor interaction | Spacing inconsistency; weak microcopy; non-blocking a11y contrast |
| **S4** | Future | Enhancement or benchmark idea | Nice-to-have feature; competitive reference pattern |

## Area Tags (for issue cards)

Use one primary area per finding:

`layout` · `copy` · `interaction` · `workflow` · `data` · `deployment` · `seo` · `performance` · `accessibility` · `trust`

## UI Mapping (from DESIGN.md)

| Level | Token | Hex |
| --- | --- | --- |
| S0 | `severity-s0` | `#7A1E1E` |
| S1 | `severity-s1` | `#B42318` |
| S2 | `severity-s2` | `#92400E` |
| S3 | `severity-s3` | `#3B5B73` |
| S4 | `severity-s4` | `#475467` |

## Rules

1. **One severity per issue card** — if multiple apply, use the highest impact level and note secondary impact in `impact`.
2. **Overall risk** for a report = highest open severity among unresolved blockers (not an average).
3. **Do not inflate** — aesthetic-only issues are rarely above S2 unless they break trust or conversion on the primary path.
4. **Do not deflate** — missing production dependencies for a claimed-live product are at least S0–S1 depending on workflow criticality.

## Gap Markers (not severities)

| Marker | Use when |
| --- | --- |
| `UNKNOWN` | Could not observe; must not guess |
| `NOT_APPLICABLE` | Check does not apply to this product type |
| `SKIPPED-SAFE` | Deliberately not executed (auth, payment, destructive submit) |

## Schema Field

Issue cards use `"severity": "S0" | "S1" | "S2" | "S3" | "S4"`.

See [audit-report.schema.json](../schemas/audit-report.schema.json).
