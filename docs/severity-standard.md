# Severity Standard (S0–S4)

**Canonical definition for the entire repository.** Skills, templates, schema, and UI must reference this file — do not redefine severity elsewhere.

> **Terminology:** English **refinement** (or “polish” in the sense of *打磨 / 润色*) — **not** the country/language “Polish / 波兰语”.

## Levels

| Level | EN name | 中文 | Meaning | Typical examples |
| --- | --- | --- | --- | --- |
| **S0** | Blocker | 阻断 | Blocks launch or delivery | Core workflow down; data leak; missing prod dependency; auth bypass |
| **S1** | Critical | 严重 | Seriously hurts conversion, trust, correctness, privacy, or ops | Broken primary CTA; misleading pricing; PII exposure; no error handling on payment |
| **S2** | Major | 重要 | Noticeable issue; launch possible only with known risk | Mobile overlap hides CTA; form succeeds with no feedback; env vars documented but not wired |
| **S3** | Minor | 次要 | Refinement: copy, layout, minor interaction — not blocking launch | Spacing inconsistency; weak microcopy; non-blocking contrast |
| **S4** | Future | 增强 | Enhancement or benchmark idea for later | Nice-to-have feature; competitive reference pattern |

### One-line (中文)

| 等级 | 意义 |
| --- | --- |
| **S0** | 阻断上线或交付 |
| **S1** | 严重损害转化、信任、正确性、隐私或运营 |
| **S2** | 明显问题；在已知风险下仍可启动 |
| **S3** | 细节打磨 / 文案 / 布局 / 轻微交互（**不是**语言「波兰语」） |
| **S4** | 未来增强或参考想法 |

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
5. **Never use “Polish” alone in user-facing Chinese** — write 打磨 / 润色 / 细节优化 instead.

## Gap Markers (not severities)

| Marker | Use when |
| --- | --- |
| `UNKNOWN` | Could not observe; must not guess |
| `NOT_APPLICABLE` | Check does not apply to this product type |
| `SKIPPED-SAFE` | Deliberately not executed (auth, payment, destructive submit) |

## Schema Field

Issue cards use `"severity": "S0" | "S1" | "S2" | "S3" | "S4"`.

See [audit-report.schema.json](../schemas/audit-report.schema.json).
