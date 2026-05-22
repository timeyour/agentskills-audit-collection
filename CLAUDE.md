# AgentSkills Audit Collection

This file is the source of truth for this repository. The skills in `.claude/skills/` must treat these rules as binding unless a later ADR changes them.

## Workflow

- Use `/audit` when the user wants a full website/product/open-source app audit covering source evidence, live flows, visual quality, deployment readiness, five-pass acceptance, and learning.
- Use `/skill-study` when the user wants the agent to learn from external skills, open-source repos, global skill reports, course/job skill lists, competitor tools, or workflow examples.
- Use `/harness` when the user wants to operationalize a business workflow, split work into multiple layers, choose prompt/skill/Dify/RPA/code/human execution, define checkpoints, or add retry/escalation strategy.
- Use `/flow-test` when the user specifically wants every function, CTA, form, route, auth path, or dashboard workflow tested.
- Use `/physical-flow-test` when `/flow-test` or `/audit` finds a critical path requiring real browser proof, when the user asks whether a live workflow actually works, or when source evidence and live evidence disagree.
- Use `/visual-qa` when the user wants page style, layout, craft, aesthetic quality, or AI slop diagnosed.
- Use `/deploy-check` when the user asks what is missing for production deployment.
- Use `/accept-five` when one pass is not enough and findings need to become reusable experience.
- Use `/agent-diagnose` when auditing AI agent behavior, prompt safety, strategy drift, permission escalation, or evidence failures.

## Rules

- AgentSkills are stateless. A skill must be usable without relying on hidden session history.
- AgentSkills must stay instruction-only unless a future ADR explicitly allows scripts.
- Generated physical browser test scripts belong in target project artifacts, not inside `.claude/skills/`.
- `CLAUDE.md` is the rule source for project-specific governance.
- `DESIGN.md` is the visual source of truth for generated audit workbench UI, examples, screenshots, and report surfaces.
- Keep `DESIGN.md` compatible with Google DESIGN.md shape: YAML design tokens first, human guidance second.
- Reference files belong in each skill's `references/` directory and should only be loaded when needed.
- Keep skill bodies concise; put templates and long checklists in references.
- External skill learning must produce concrete workflow triggers, audit checks, benchmark labels, guardrails, or rejection reasons.
- Do not convert broad market skills into basic courses inside this repository.
- Maintain an adversarial stance against source claims, broken workflows, visual slop, deployment theater, and rubber-stamp reviews.
- Do not skip verification just because implementation looks simple.
- Multi-step audits must use progressive reporting so the user can see stage progress, evidence collected, blockers, and next actions before the final report.
- Prefer observable acceptance criteria over intent descriptions.
- New guardrails must be specific, triggerable, and reviewable.
- Validation examples may exist, but they must stay outside `.claude/skills/` and must not be required for skill use.
- Every skill should preserve the shared report shape when applicable: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.
- Use `S0-S4` severity for delivery impact: `S0` blocks launch, `S1` serious conversion/trust/security/reliability risk, `S2` noticeable issue with temporary launch possible, `S3` polish, `S4` future enhancement.
- If a finding cannot be reproduced, located, fixed, or retested, mark the evidence gap explicitly.
- A skill that only produces a polished command name or vague opinion has failed.
- For complex workflows, use a harness before execution: stage tree, execution matrix, checkpoints, retry/escalation, and human-intervention map.
- Do not choose RPA, Dify, prompt, or skills before mapping the business steps and failure points.
- For process-agent work, require the lifecycle: define problem, define business flow and data templates, build the process agent, iterate from signal/root-cause/verification.
- Do not automate a messy human process before turning tacit know-how into explicit data templates, handoff rules, checkpoints, and success signals.

## ADR Log

## ADR: Progressive Reporting For Transparent Audits

- Date: 2026-05-22
- Status: Accepted
- Context: Long audits can become black boxes when the agent stays silent until the final report. Users need to see what was checked, what evidence exists, which blockers appeared, and what will happen next.
- Decision: Add `audit/references/progressive-reporting.md` and require `/audit` and `/flow-test` to emit concise progress updates during multi-step runs. Progress updates are evidence checkpoints, not final verdicts, and they must preserve safety boundaries around private, payment, destructive, and production-mutation actions.
- Consequences: Audit runs become more observable and easier to trust. Final reports still use the shared Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons shape.

## ADR: Physical Browser Verification For Critical Flows

- Date: 2026-05-21
- Status: Accepted
- Context: Static flow audits can miss runtime failures caused by JavaScript execution, auth boundaries, third-party scripts, network behavior, timing, and browser-only UI states.
- Decision: Add `/physical-flow-test` as the bridge from cognitive audit to executable browser verification. It generates Python Playwright test packages for real execution, collects trace, screenshot, HAR, video, console, and result artifacts, and feeds those artifacts back into severity, reproduction, regression, and lessons.
- Consequences: Critical workflow claims require physical evidence before being marked working. The skills remain instruction-only; generated tests and artifacts live in the target project or audit workspace.

## ADR: Process Agents Need Flow Templates And Signal Loops

- Date: 2026-05-20
- Status: Accepted
- Context: A process agent can look impressive while merely wrapping a messy human workflow in AI. The user's supplied process-agent material emphasizes defining the problem, business flow, data templates, full process-agent construction, and iterative optimization from signals.
- Decision: `/harness` includes a process-agent pattern. Process-agent planning must define the problem, map business flow and data templates, combine business know-how/data/tools, and maintain a signal/root-cause/verification loop after deployment.
- Consequences: The system avoids one-prompt automation theater and can prove whether repeated questions, handoff failures, cycle time, or manual corrections actually decreased.

## ADR: Harness Before Complex Execution

- Date: 2026-05-19
- Status: Accepted
- Context: AI-assisted workflows can fail when a large business process is collapsed into one prompt or one skill. Some steps belong in prompts, some in AgentSkills, some in Dify, some in deterministic code, some in RPA, and some require human judgment or approval.
- Decision: Add `/harness` as the engineering delivery planning layer. It decomposes business goals into multi-level steps, routes each unit to an execution mode, and defines checkpoints, retries, fallbacks, and human escalation before implementation or audit.
- Consequences: Complex workflows become more reliable, inspectable, and recoverable. The system can distinguish automation opportunities from places where human intervention is mandatory.

## ADR: Unified Evidence Output And S0-S4 Severity

- Date: 2026-05-19
- Status: Accepted
- Context: The collection should not become a set of attractive command names. Each skill needs to produce evidence that a user can understand, reproduce, fix, retest, and learn from.
- Decision: All skills use a shared output shape when applicable: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons. Delivery impact is classified with `S0-S4`.
- Consequences: Reports are more comparable across audit, flow testing, visual QA, deployment checks, five-pass acceptance, agent diagnosis, and external skill study.

## ADR: External Skill Learning Is Pattern Extraction

- Date: 2026-05-19
- Status: Accepted
- Context: The collection needs to learn from open-source skills, AI workflow examples, and market skill trend reports without becoming a generic education list.
- Decision: `/skill-study` converts external sources into workflow triggers, evidence requirements, validation checks, benchmark labels, and guardrails. Broad skills such as AI literacy, data analysis, communication, and process optimization are translated into audit behavior rather than basic curriculum.
- Consequences: The repository can keep learning from the ecosystem while preserving the task-oriented AgentSkills shape.

## ADR: Instruction-Only Skills

- Date: 2026-05-18
- Status: Accepted
- Context: The collection is meant to improve AI-assisted engineering discipline without adding runtime dependencies or brittle local scripts.
- Decision: Skills in this repository use Markdown instructions and reference files only. No `scripts/` directories are included.
- Consequences: The workflow stays portable across Claude Code projects, but deterministic automation must be handled by the host project rather than bundled here.

## ADR: CLAUDE.md as Governance Source

- Date: 2026-05-18
- Status: Accepted
- Context: `/audit` and the task skills need a stable place to load, evaluate, and update project rules.
- Decision: `CLAUDE.md` is the canonical rule source. Skills may reference local conventions, but explicit governance rules belong here.
- Consequences: Projects adopting these skills should keep `CLAUDE.md` current and use ADR-style entries for durable process changes.

## ADR: Validation Artifacts Stay Outside Skills

- Date: 2026-05-18
- Status: Accepted
- Context: The practical validation run needed a TODO CLI example, tests, and workflow reports. Those artifacts are useful proof, but they should not make the skills stateful or add runtime requirements to `.claude/skills/`.
- Decision: Validation examples may live in `examples/`, `tests/`, and `validation/`. They must not be placed inside `.claude/skills/`, and the skills must remain usable without them.
- Consequences: The repository can include proof of the workflow while preserving portable, instruction-only skills.
