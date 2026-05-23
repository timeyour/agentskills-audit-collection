# Requirements

## Core Purpose

This project exists to make AI-assisted website and product audits concrete, repeatable, and evidence-based.

The target problem is not "how to write more code with AI." The target problem is how to make an AI agent test real product workflows, diagnose visual quality, expose deployment gaps, and turn findings into copyable fixes.

## User Need

The user needs a reusable Claude Code AgentSkills workflow that can force an AI agent to:

1. Open a site, app, repo, or AI-built project and identify every important feature.
2. Execute workflows as far as safely possible.
3. Judge page quality, craft, and AI slop with evidence.
4. Identify deployment dependencies and missing production pieces.
5. Repeat acceptance through five passes.
6. Accumulate experience into better prompts, guardrails, and benchmarks.
7. Learn from external skills, repositories, market trend reports, and competitor workflows while preserving evidence discipline.
8. Decompose complex business workflows into executable layers with checkpoints, retries, and human intervention before implementation or audit.

In short:

```text
Turn vibe coding from "looks done" into "tested, located, scored, and fixable."
```

Sharper positioning:

```text
AgentSkills is an acceptance and audit system for AI-generated websites and products. It turns "looks done" into "tested step by step, reproducible, risk-aware, fixable, retestable, and reusable."
```

## Expanded Product Need: Website Audit Workbench

The more concrete product need is an at-a-glance website audit workflow.

The user does not only want a list of vibe-coded websites. The user wants to inspect those sites and immediately understand:

- where the webpage quality is good or broken;
- where layout, typography, spacing, responsiveness, and content hierarchy fail;
- which buttons, forms, CTAs, navigation items, and workflows are connected or broken;
- what the user problem and proposed solution are for each issue;
- what can be copied directly into an AI builder, issue tracker, or implementation prompt;
- what is missing for deployment, such as domain, environment variables, backend, database, auth, analytics, storage, email, CMS, SEO, or monitoring.

The desired output should be scannable like an audit board, not buried in paragraphs.

This product should also act as an aesthetic and craft diagnostic layer. It should help the user understand whether a site feels designed, not merely generated.

Each inspected site or page should produce:

- a quality score;
- live detection positions for issues and interactions;
- a visual/layout issue list;
- an interaction/workflow map;
- a feature-by-feature execution log;
- a deployment readiness checklist;
- issue cards with severity, evidence, root cause, fix recommendation, and one-click-copy text;
- a final "what to fix first" priority list.

## Aesthetic Intelligence Requirement

The workbench should help quantify aesthetic and product quality without pretending that taste is only a numeric score.

It should inspect:

- whether the page has a clear design intent;
- whether the first viewport communicates the offer and next action;
- whether visual hierarchy, spacing, typography, color, imagery, and component systems feel coherent;
- whether the page shows "AI slop" signals such as generic gradients, template-card repetition, irrelevant imagery, vague copy, mismatched components, or fake trust cues;
- whether the page uses patterns that match its product category;
- whether the experience creates a believable scenario and converts inspiration into action.

For lifestyle, commerce, creator, and service sites, the audit should also ask:

- What scene or future state is the user being invited into?
- Can the user imagine themselves taking the next action?
- Does the page connect aspiration to a concrete workflow, such as booking, saving, buying, sharing, uploading, or contacting?

The score should be supported by specific issue cards and evidence, not taste claims alone.

## Functional Flow Testing Requirement

The audit workflow must not stop at static inspection. For each page or app, the agent should identify every important feature and walk through the user flow as far as safely possible.

Features to test include:

- navigation and routing;
- CTA buttons;
- contact, booking, signup, login, checkout, RSVP, upload, search, filter, copy, export, and share flows;
- form validation, success states, error states, loading states, and empty states;
- auth-gated and admin-gated workflows;
- persistence after refresh or navigation;
- email/SMS/payment/storage/database/CMS dependencies when visible;
- mobile and desktop variants.

Each tested feature should produce:

- starting URL;
- exact live position;
- steps performed;
- expected result;
- actual result;
- screenshots or locator evidence when available;
- risk level;
- recommended fix;
- copyable fix prompt.

## Five-Pass Acceptance Requirement

Important audits should be accepted through five repeated passes, not a single inspection.

Each pass has a different purpose:

1. Baseline pass: confirm the page loads, identify the product type, inventory features, and map the happy path.
2. Functional pass: execute every safe workflow and record expected vs actual behavior.
3. Edge and failure pass: test invalid input, empty states, loading states, mobile viewports, auth boundaries, and refresh/back behavior.
4. Visual and deployment pass: inspect craft quality, responsive polish, accessibility, SEO, backend dependencies, env vars, CMS/admin, analytics, and monitoring gaps.
5. Retest and learning pass: verify fixes or unresolved blockers, detect repeated issue patterns, and update guardrails, templates, or copy prompts.

After five passes, the audit should produce an experience ledger:

- recurring issue patterns;
- false positives;
- prompt patterns that produced good fixes;
- prompt patterns that failed;
- new checklist items;
- guardrail updates for `CLAUDE.md` or skill references;
- examples worth keeping as benchmarks.

The fifth pass is not just another test. It exists to convert findings into reusable experience.

## External Skill Learning Requirement

The collection should be able to study other people's skills and global skill trends without becoming a basic curriculum.

When ingesting sources such as open-source skill repos, AI workflow examples, course/job skill trend reports, or competitor tools, the agent must:

- record source locator, claim, date if visible, and confidence;
- separate market demand from executable skill design;
- extract workflow triggers, task boundaries, validation steps, output artifacts, and anti-patterns;
- translate broad trends into audit capabilities instead of course topics;
- classify each pattern as `ADOPT`, `ADAPT`, `REFERENCE`, or `REJECT`;
- update skill references, benchmark labels, or guardrails only when the change is specific and testable.

Examples:

- `AI literacy` becomes a check for whether an AI product claim is visible, useful, and connected to a real workflow.
- `workflow automation` becomes a check for repeated steps, broken handoffs, missing integrations, and copyable automation opportunities.
- `communication` becomes a requirement that findings are located, severity-ranked, and directly actionable.
- `adaptability` becomes a retest and learning loop after new evidence appears.

## Harness Engineering Requirement

Complex AI-assisted delivery should use a harness before execution.

The harness turns a business objective into:

- business stages;
- substeps;
- execution units;
- execution-mode routing;
- automatic checkpoints;
- human checkpoints;
- retry limits;
- fallback modes;
- escalation paths;
- acceptance handoff.

For process-agent work, the harness should also support a four-stage lifecycle:

1. define the problem;
2. define business flow and data templates;
3. build the process agent from business know-how, data construction, and tools;
4. iterate through signal collection, root-cause diagnosis, simulated/tested change, and verification.

Execution modes include:

- `PROMPT`: one-off reasoning, drafting, classification, or low-risk transformation.
- `SKILL`: repeatable AgentSkills workflow with known output format.
- `DIFY`: structured LLM workflow, API chain, knowledge base, or business automation.
- `RPA`: UI-only repetitive process when no API or stable integration exists.
- `CODE`: deterministic transform, parser, validation, integration, or test.
- `HUMAN`: judgment, approval, credential, payment, legal/privacy, brand, or irreversible decision.
- `EXTERNAL`: SaaS/API/platform step outside direct agent control.

The agent should split steps until each execution unit has:

- one input;
- one output;
- one owner;
- one execution mode;
- one checkpoint;
- one retry/fallback rule;
- one acceptance condition.

This requirement is inspired by FDE-style engineering practice: enter the real workflow, translate messy demand into executable requirements, build the smallest useful solution, test with users/operators, and turn repeated learning into a reusable system.

## Visual Quality Requirement

The audit must inspect visual and style quality, not only functional correctness.

It should flag:

- weak first viewport;
- unclear hierarchy;
- inconsistent spacing, alignment, typography, color, radius, icons, or shadows;
- template-clone feeling;
- mismatched visual style across sections;
- low-quality or irrelevant imagery;
- mobile overlap, cropping, hidden CTAs, or unreadable text;
- weak trust signals or conversion flow;
- accessibility and contrast issues.

The visual review should say what is wrong, where it is, why it matters, and how to fix it.

## Open-Source Execution Layer

The skills remain instruction-only, but the workflow may use open-source tools in the host project or validation environment when available.

Recommended tool categories:

- Browser flow testing: Playwright or equivalent.
- Accessibility checks: axe-core or equivalent.
- Performance/SEO checks: Lighthouse or equivalent.
- Link checking: a crawler/link checker.
- HTML/CSS validation: markup/style linters where useful.
- Screenshot comparison: image diff tooling where regression testing matters.
- Console/network inspection: browser automation logs.

Open-source tools should produce evidence. They do not replace human/agent judgment on product value, visual quality, workflow usefulness, or deployment readiness.

## Website Audit Issue Card Requirements

Each issue card should include:

- Severity: `S0`, `S1`, `S2`, `S3`, or `S4`.
- Area: layout, copy, interaction, workflow, data, deployment, SEO, performance, accessibility, or trust.
- Live position: URL, page area, element label, source line/selector/screenshot coordinate, and workflow step.
- Evidence: what was observed.
- Problem: why it matters.
- Likely cause: what may be missing or misconfigured.
- Fix: concrete action.
- Copy prompt: a ready-to-copy instruction for an AI builder or developer.
- Validation: how to confirm the fix.

Severity meanings:

| Level | Meaning |
| --- | --- |
| `S0` | Blocks launch or delivery; core workflow unavailable, data/security risk, or production dependency missing. |
| `S1` | Seriously hurts conversion, trust, correctness, privacy, or operational reliability. |
| `S2` | Noticeable UX, workflow, visual, accessibility, or deployment issue; temporary launch possible with known risk. |
| `S3` | Polish, copy, layout, or minor interaction improvement. |
| `S4` | Future enhancement or benchmark idea. |

## Unified Output Requirement

Every skill should preserve a shared evidence-first report shape when applicable:

1. Scope: what was inspected and what was intentionally skipped.
2. Evidence: source, live, tool, screenshot, locator, or inference level.
3. Findings: issue list or pattern list.
4. Severity: `S0-S4` delivery impact.
5. Reproduction: exact steps, URL, page area, selector/text, input, or command.
6. Fix Suggestion: concrete fix, owner/dependency if known, and copyable prompt.
7. Regression Check: how to verify the fix and avoid reintroducing the issue.
8. Lessons: benchmark labels, guardrails, prompt improvements, or rejection reasons.

If a skill cannot fill a field, it should mark it `UNKNOWN`, `NOT APPLICABLE`, or `SKIPPED-SAFE`; it should not silently omit the field.

## Why Batch Validation Exists

The website case validation is not the final product. It is a proof method.

The goal of validating real vibe-coded websites is to check whether the skills can handle messy, real-world judgment tasks:

- separate evidence from hype;
- reject weak or dead examples;
- distinguish demos from production cases;
- rank examples by practical reuse value;
- preserve caveats instead of overclaiming.
- expose layout, workflow, deployment, and quality problems in a reusable audit format.

This tests whether the workflow is useful beyond a toy TODO CLI.

## Primary Requirements

- Provide task-oriented Claude Code AgentSkills:
  - `/skill-study` for learning from external skills, repositories, market skill reports, and competitor workflows.
  - `/harness` for decomposing business objectives into execution units with checkpoints, retries, human intervention, and tool routing.
  - `/audit` for the full website/product audit workflow.
  - `/flow-test` for feature-by-feature live workflow testing.
  - `/physical-flow-test` for generating executable Python Playwright tests and collecting trace, screenshot, HAR, video, console, and result artifacts for critical workflows.
  - `/visual-qa` for visual quality, style, and AI slop review.
  - `/ai-product-audit` for product-pattern fit, scenario clarity, and conversion readiness.
  - `/deploy-check` for production readiness and dependency gaps.
  - `/accept-five` for five-pass acceptance and experience accumulation.
  - `/agent-diagnose` for adversarial agent/workflow reliability checks.
- Keep each skill stateless and independently callable.
- Keep skills instruction-only; do not bundle scripts inside `.claude/skills/`.
- Treat `CLAUDE.md` as the project governance source.
- Include references for templates and checklists.
- Validate the workflow with both:
  - a small implementation task;
  - a real-world batch judgment task.
- Support website audit outputs that make page quality, connected workflows, issue fixes, and deployment gaps visible at a glance.
- Support feature-by-feature flow testing, including expected vs actual behavior and visual quality findings.
- Support five-pass acceptance testing so repeated findings become durable project experience.
- Support external skill-study passes so trend reports and open-source examples become concrete audit checks rather than vague learning lists.
- Support a unified output format and `S0-S4` severity scale across all skills.
- Support harness planning so complex workflows are decomposed and routed before implementation, audit, or automation.

## Success Criteria

The project is successful if a user can install or copy the skills into a Claude Code project and reliably use them to:

- audit a website and produce clear issue cards with copyable fixes and deployment readiness notes.
- execute a site's core workflows and show exactly where each flow works, fails, or needs deployment work.
- repeat acceptance up to five passes and accumulate lessons into rules, templates, and fix prompts.
- ingest an external skill source or trend report and return adoption decisions, rejected patterns, and exact guardrail/checklist updates.
- produce evidence that another person can understand, reproduce, fix, retest, and learn from.
- turn a messy business objective into a stage tree, execution matrix, checkpoint table, retry/escalation plan, and acceptance handoff.

## Non-Goals

- This is not a website showcase repo.
- This is not a generic prompt collection.
- This is not a basic skills curriculum.
- This is not a replacement for project-specific engineering judgment.
- This is not a script automation toolkit.
- This does not claim that all vibe-coded examples are production-quality.
- This is not a collection of pretty command names without verifiable outputs.
- This is not a one-prompt automation fantasy; complex business work requires decomposition, checkpoints, and human boundaries.

## Target Audience

- Solo builders using AI to ship code.
- Developers who want AI assistance without architecture decay.
- Teams experimenting with Claude Code Skills.
- Builders learning how to turn vibe coding into client-ready or production-ready work.
