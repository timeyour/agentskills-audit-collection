# AgentSkills Audit Collection

A task-oriented Claude Code AgentSkills collection for auditing websites, web apps, open-source projects, and AI-built products.

AgentSkills is an acceptance and audit system for AI-generated websites and products. It turns vibe-coded results from "looks done" into engineering delivery assets that are tested step by step, reproducible, risk-aware, fixable, retestable, and reusable.

## Workflow

```text
skill-study -> harness -> audit -> flow-test / visual-qa / deploy-check -> accept-five -> agent-diagnose -> rules memory / benchmark library
```

## Skills

- `/skill-study`: learn from external skills, repositories, market skill reports, and competitor workflows.
- `/harness`: decompose business goals into execution units with prompt/skill/Dify/RPA/code/human routing, checkpoints, retries, and escalation.
- `/audit`: run the end-to-end website/product audit workflow.
- `/flow-test`: test every visible feature and user workflow.
- `/visual-qa`: audit visual craft, layout, responsive behavior, and AI slop.
- `/deploy-check`: inspect production readiness and missing runtime dependencies.
- `/accept-five`: run five-pass acceptance and accumulate lessons.
- `/agent-diagnose`: adversarially diagnose AI agent and workflow failure modes.

## Design Principles

- Instruction-only skills: no bundled scripts.
- `CLAUDE.md` is the governance source of truth.
- Every skill must produce evidence that another person can understand, reproduce, fix, and retest.
- Complex workflows must be decomposed into business stages and execution units before choosing prompt, skill, Dify, RPA, code, or human intervention.
