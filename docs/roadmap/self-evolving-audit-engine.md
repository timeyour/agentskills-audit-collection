# Self-Evolving Audit Engine Roadmap

This document turns the user-provided WaytoAGI, Feishu, and packaged research notes into a cautious roadmap for self-improving audit workflows.

It is a roadmap, not an implemented capability claim.

## Goal

Move from one-off audit reports to a repeatable loop:

```text
plan -> generate/check -> audit -> fix -> retest -> lesson -> guardrail
```

The repository should remain instruction-first until there is a concrete need for a runtime engine.

## Generator + Critic Loop

Use two separate roles:

| Role | Responsibility |
| --- | --- |
| Generator | Builds or fixes the product, page, workflow, or code. |
| Critic/Auditor | Attacks the result using evidence rules, failure modes, visual metrics, and permission boundaries. |

Minimum loop:

```text
Generator output
  ->
Auditor checks failure modes and evidence
  ->
S0-S4 findings
  ->
Generator fixes
  ->
Auditor retests
  ->
Lessons candidate
```

Rules:
- The auditor must not accept the generator's claims as evidence.
- The generator must fix from findings, not from vague criticism.
- The loop stops only when blockers are closed or explicitly accepted as known risk.

## Queen + Specialist Model

For larger workflows, use a coordinator:

| Role | Responsibility |
| --- | --- |
| Queen Agent | Defines scope, permission level, pass order, and acceptance gate. |
| Specialist Agent | Performs focused work such as implementation, visual repair, or test creation. |
| Independent Auditor | Reviews the result with failure-mode and evidence checklists. |

Gate rule:
- `S0` blocks release.
- `S1` requires explicit risk acceptance or fix before release.
- `S2` can ship only with a regression plan.
- `S3-S4` become backlog or polish.

## Lessons Ledger

Every audit can produce lessons, but not every lesson should become a global rule.

Use this decision table:

| Lesson Type | Store In | Example |
| --- | --- | --- |
| One-off target detail | Validation report only | This specific demo site uses a mocked login. |
| Repeated project pattern | Project docs or `validation/` | This repo often forgets invalid-form states. |
| Cross-project guardrail | `CLAUDE.md` or skill reference | Do not claim workflow success without live/browser or execution evidence. |
| Physical test lesson | `physical-flow-test` lessons ledger | HAR files must be redacted before sharing. |

Lesson format:

```text
Trigger:
Observed failure:
Evidence:
Better rule:
Where to store:
Retest:
```

## HOT/WARM/COLD Memory Pattern

The user-provided research described a memory tiering pattern. Use it as an inspiration, not as a repository guarantee.

| Tier | Meaning | Use In This Repo |
| --- | --- | --- |
| HOT | Rules that should be loaded every time. | `CLAUDE.md` and core skill references. |
| WARM | Useful but situational patterns. | `validation/`, `docs/research/`, case-specific templates. |
| COLD | Historical notes and candidates. | Research archive or candidate lists. |

Promotion criteria:
- Appears in at least three audits.
- Has clear evidence and a fix.
- Improves future audit behavior without adding noise.

Demotion criteria:
- Only applies to one tool, one site, or one temporary event.
- Lacks verification.
- Creates conflicting guidance.

## When To Update CLAUDE.md

Update `CLAUDE.md` only when a lesson is:

- repeated across multiple targets;
- evidence-backed;
- safe as a general instruction;
- short enough to improve behavior rather than dilute it.

Do not update `CLAUDE.md` for:

- unverified claims;
- candidate websites;
- one-off product quirks;
- external tool popularity numbers;
- speculative platform ideas.

## v2 Runtime Ideas

These are future directions, not current repository claims:

| Idea | Purpose | Status |
| --- | --- | --- |
| Core runner | Deterministic Playwright, screenshot, and report orchestration. | Roadmap |
| Visual metrics engine | Measure spacing, contrast, screenshot diffs, and layout drift. | Roadmap |
| MCP server | Expose audit actions as tools for agent clients. | Roadmap |
| A2A agent card | Let other agents discover the audit system. | Roadmap |
| Web dashboard | Show evidence, screenshots, S0-S4 findings, and fix prompts. | Roadmap |

Keep the current skills usable without these runtime layers.

## Near-Term Implementation Order

1. Harden repository self-validation.
2. Add research-backed failure modes and aesthetic metrics.
3. Add lessons ingestion rules.
4. Add deterministic visual regression examples only after a real target needs them.
5. Consider runtime engine only after instruction-only workflows show repeated manual overhead.
