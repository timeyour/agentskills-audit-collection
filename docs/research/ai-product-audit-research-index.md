# AI Product Audit Research Index

This index summarizes user-provided WaytoAGI, Feishu, and packaged research notes about AI-generated product auditing, aesthetic QA, and self-evolving agent systems.

It is a source index, not a claims database. Unverified figures, candidate websites, and externally reported popularity metrics must not be promoted into case studies without follow-up verification.

## Source Status Labels

| Status | Meaning |
| --- | --- |
| `verified` | Confirmed inside this repository or through direct local evidence. |
| `user-provided` | Provided by the user in chat, Feishu output, or zip materials. Useful as research input, not independently verified here. |
| `needs-verification` | Plausible external claim that needs source checking before public use. |
| `candidate-only` | Possible sample, site, tool, or benchmark candidate. Not a case study. |

## Provided Materials

| Material | Status | Useful Extraction |
| --- | --- | --- |
| Feishu/WaytoAGI report on AI audit and self-evolution | `user-provided` | Failure modes, aesthetic metrics, Generator/Critic loop, lessons memory pattern. |
| Skills x GitHub x self-evolution x frontend design report | `user-provided` | Skill ecosystem framing, self-improving skill ideas, frontend QA themes. |
| `AI_Product_Audit_Research_Report.md` from zip | `user-provided` | Industry context, AI slop, A2A/MCP ecosystem framing. |
| `Audit_Collection_Evolution_Blueprint.md` from zip | `user-provided` | Skill-Core-Gateway roadmap idea. |
| `Master_Evolution_Plan_v2.0.md` from zip | `user-provided` | Visual metrics, failure pattern JSON, Queen/Specialist model. |
| `Project_Context_for_CodeX.md` from zip | `user-provided` | Concise product identity and AI acceptance positioning. |
| `Project_Master_Archive_Full_History.md` from zip | `user-provided` | Conversation history and candidate implementation prompts. |

## What Was Promoted Into Repository Rules

| Research Theme | Destination | Reason |
| --- | --- | --- |
| Field validation, concurrency, N+1, swallowed exceptions, memory pagination, hallucinated APIs, hardcoded secrets | `.claude/skills/audit/references/failure-modes.md` | Repeated AI delivery failures can become evidence-backed audit checks. |
| AI slop, spacing drift, hierarchy, visual weight, component consistency, Figma vs code comparison | `.claude/skills/visual-qa/references/aesthetic-metrics.md` | Useful for visual QA when framed as heuristics and evidence requirements. |
| Generator/Critic, Queen/Specialist, lessons ledger, HOT/WARM/COLD memory | `docs/roadmap/self-evolving-audit-engine.md` | Useful roadmap material, but not yet implemented runtime behavior. |

## What Was Not Promoted As Fact

| Item | Status | Reason |
| --- | --- | --- |
| 300 vibe-coded site examples | `candidate-only` | The list mixes real domains, templates, generated names, and patterns. |
| 1000 global websites | `candidate-only` | Useful as a sampling idea, but not an audited case library. |
| Tool star counts, download counts, and marketplace rankings | `needs-verification` | Popularity numbers change and need direct source checks. |
| OpenClaw, ClawHub, Capability Evolver ecosystem claims | `needs-verification` | Potentially relevant to positioning, but not required for current skill behavior. |
| MCP/A2A/web dashboard implementation claims | `needs-verification` | Roadmap only; this repository remains instruction-only today. |

## Candidate Pool Policy

Candidate sites and tools may be collected, but they must stay outside `CASE_STUDIES.md` until audited.

Required fields for a future candidate list:

```text
name:
url:
source:
status: candidate-only / verified / audited
category:
audit priority:
reason to inspect:
last checked:
notes:
```

Promotion rule:
- A candidate becomes a case study only after an audit report exists under `validation/` or `reports/`.

## Link and Citation Policy

When turning research into public docs:

- Prefer stable source titles and URLs.
- Mark user-provided claims as user-provided until independently checked.
- Do not quote long copyrighted source passages.
- Do not imply that this repository performed a full WaytoAGI or Feishu crawl unless the retrieval log is included.
- Keep README short; put detailed research in `docs/research/`.

## Next Research Questions

- Which failure modes appear most often in real vibe-coded websites already audited under `validation/`?
- Which aesthetic metrics are practical to measure with screenshots and CSS alone?
- Which lessons deserve promotion from validation reports into `CLAUDE.md`?
- What minimum runtime layer would reduce manual audit overhead without breaking the instruction-only skill model?
