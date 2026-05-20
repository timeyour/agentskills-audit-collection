# Product Definition

## Product Idea

An AI website and product audit workbench that tests real workflows, diagnoses visual quality, and turns findings into copyable fixes.

It is a delivery acceptance system for AI-generated products: harness planning, QA department, risk audit, acceptance workflow, and retrospective memory in one loop.

It is not a generic website gallery. It is a diagnostic system for builders who want to know:

- what works;
- what breaks;
- what looks weak;
- where the issue is;
- why the issue matters;
- what to copy into an AI builder or code agent to fix it.

## Product Thesis

AI builders can produce screens quickly, but they often ship work that is visually inconsistent, functionally incomplete, or deployment-fragile.

The opportunity is to build an audit layer that combines:

- functional QA;
- adversarial agent safety checks;
- aesthetic and craft diagnosis;
- real product-pattern references;
- deployment readiness;
- copyable repair prompts.

## User Promise

Paste a URL or project, and the workbench shows:

1. every important feature and workflow;
2. where each workflow works, fails, or is unknown;
3. where the page feels visually weak or AI-generated;
4. what deployment dependencies are missing;
5. which fixes matter first;
6. prompts that can be copied into Claude Code, Lovable, v0, Replit, Bolt, or another builder.

## Core Loop

```text
business objective or URL/project -> harness planning -> scope -> evidence -> feature inventory -> flow execution -> visual/aesthetic audit -> deployment audit -> issue cards -> regression checks -> copyable fix pack -> retest -> lessons
```

For important audits, run this as a five-pass loop:

```text
baseline -> functional -> edge/failure -> visual/deployment -> retest/experience
```

## Product Modes

- `Harness plan`: decompose a business objective into execution units with prompt/skill/Dify/RPA/code/human routing.
- `Source pass`: inspect gallery/project/source claims.
- `Visual pass`: inspect page screenshots and visual hierarchy.
- `Clicked-flow pass`: execute public workflows.
- `Authenticated pass`: execute gated workflows with supplied credentials or demo mode.
- `Retest pass`: verify that fixes worked.
- `Five-pass acceptance`: repeat the audit through five lenses and turn repeated findings into guardrails.

## Harness Layer

Before complex implementation or audit, the product should ask:

- What is the business stage tree?
- Which units are prompts?
- Which units deserve AgentSkills?
- Which units belong in Dify or another workflow engine?
- Which units require deterministic code?
- Which units are UI-only and may need RPA?
- Which units require human approval or judgment?
- What automatic checkpoint proves each unit worked?
- What retry/fallback happens when it fails?
- When must the process stop and escalate?

For process agents, it should also ask:

- What is the real business bottleneck?
- What business flow and data templates make the process runnable?
- What know-how, data, and tools are needed?
- What signals show the agent is failing in the field?
- Does the iteration fix the root cause or only the symptom?
- Did repeated questions, handoff failures, or manual corrections actually decrease?

## Viba-Inspired Insight

The product should not only ask "is this page pretty?"

It should ask:

- What scenario is this page preparing the user for?
- What self-image, business outcome, or action does it help the user move toward?
- Can the user see themselves in the next step?
- Is the page only inspiration, or does it convert inspiration into action?

For lifestyle, service, commerce, and creator products, this matters as much as button correctness.

## Experience Accumulation

The product should become smarter through repeated audits.

After each five-pass acceptance cycle, save:

- repeated failure patterns;
- high-quality reference patterns;
- weak prompts and improved prompts;
- deployment gaps that recur;
- visual craft issues that recur;
- benchmark examples to compare against future sites.

## Delivery Severity

Use `S0-S4` to keep product reports tied to delivery risk:

- `S0`: do not launch or deliver.
- `S1`: serious trust, conversion, correctness, privacy, or reliability risk.
- `S2`: launch is possible only with a known risk note.
- `S3`: polish issue.
- `S4`: future enhancement.

## Differentiation

- Against simple QA tools: adds visual taste, product context, and fix prompts.
- Against design inspiration sites: tests whether the thing actually works.
- Against Lighthouse-only audits: focuses on user workflows and business readiness.
- Against AI builders: catches what the builder missed.

## Non-Goals

- Not a design clone generator.
- Not a generic benchmark leaderboard.
- Not a replacement for human product judgment.
- Not limited to vibe-coded sites; those are the starting dataset.
