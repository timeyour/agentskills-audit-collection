# Process Agent Pattern

Use this reference when converting a human-heavy business process into a runnable process agent.

This pattern is useful for workflows such as product launch, sales enablement, onboarding, customer support, operations, compliance, and other multi-role business processes.

## Core Idea

Do not build an agent by asking "what should the AI say?"

Build a process agent by asking:

```text
What business process currently depends on people passing context by hand, and how can it be decomposed, templated, checkpointed, and iterated?
```

## Four-Stage Lifecycle

| Stage | Goal | Output |
| --- | --- | --- |
| 1. Define the problem | Identify the real business bottleneck and customer/operator roles. | Problem statement, users, pain point, success metric. |
| 2. Define business flow and data templates | Convert messy manual work into a stable flow and reusable input/output templates. | Flow map, node map, data template, handoff rules. |
| 3. Build the process agent | Combine business know-how, data construction, and tools into a runnable process. | Process agent, tool map, checkpoint map, operating guide. |
| 4. Iterate and optimize | Collect signals, diagnose root causes, test improvements, and verify whether repeated problems decrease. | Signal ledger, root-cause log, retry plan, improvement evidence. |

## Stage 1: Define The Problem

Ask:

- Who is the customer or internal user?
- Is this a single person's problem or a multi-role collaboration problem?
- What information gap, coordination gap, or execution gap causes delay or error?
- What process currently depends on repeated meetings, manual explanation, or hidden know-how?
- What would prove the process agent reduced friction?

Good problem statements name:

- role;
- scenario;
- bottleneck;
- current workaround;
- desired outcome;
- measurable signal.

## Stage 2: Business Flow And Data Templates

Map the process as nodes.

For each node, define:

- actor;
- input;
- output;
- decision;
- data template;
- handoff target;
- evidence;
- checkpoint.

Look for first-order value:

- reduce information gap;
- reduce manual repetition;
- convert tacit know-how into stable templates;
- make the next step possible without asking another person;
- shorten cycle time from weeks/days to hours/minutes.

## Stage 3: Build The Process Agent

A process agent needs three parts:

1. Business know-how
   - domain rules;
   - historical cases;
   - tacit judgment;
   - exception handling;
   - output quality expectations.

2. Data construction
   - stable data templates;
   - required fields;
   - missing-data handling;
   - retrieval or source-of-truth mapping;
   - evidence lineage.

3. Tools
   - AgentSkills;
   - Dify workflows;
   - APIs;
   - deterministic code;
   - RPA where no API exists;
   - human decision gates.

Do not let one agent own the entire process if the process has distinct failure modes. Split into sub-agents or units when business nodes, data templates, checkpoints, or tool modes differ.

## Stage 4: Iteration Agent

Add an iteration loop:

```text
collect signals -> diagnose root cause -> simulate or test change -> verify reduction -> update process
```

Signal collection:

- user/operator questions;
- repeated confusion;
- wrong outputs;
- blocked handoffs;
- missing fields;
- sales/support objections;
- time spent at each node;
- repeated manual corrections.

Root-cause diagnosis:

- Is this a missing data template?
- Is this unclear business know-how?
- Is this a tool failure?
- Is this a handoff failure?
- Is this a prompt/skill failure?
- Is this a human approval bottleneck?

Simulation or test:

- Test the changed step against real examples.
- Use another agent or reviewer to ask whether the fix addresses the root cause or only the symptom.
- Reject shallow fixes that only patch wording.

Verification:

- Did the same type of question decrease?
- Did cycle time improve?
- Did handoff failure decrease?
- Did manual correction decrease?
- Did the downstream user trust the output more?

## Capability Requirements

A real process-agent builder needs:

1. Business architecture capability
   - define process stages;
   - identify roles;
   - abstract tacit know-how;
   - design handoffs.

2. Technical implementation capability
   - map tools;
   - build workflows;
   - connect data and APIs;
   - implement checkpoints.

3. Effect validation capability
   - define success signals;
   - verify outcomes;
   - detect shallow fixes;
   - prove repeated issues declined.

The harness should lower the talent-density requirement by making these capabilities explicit and reusable.

## Output Add-On

When using this pattern, add these tables to the harness:

```markdown
## Process Agent Lifecycle

| Stage | Business Question | Output | Checkpoint | Owner |
| --- | --- | --- | --- | --- |

## Signal And Iteration Loop

| Signal | Root Cause | Change Tried | Verification | Result |
| --- | --- | --- | --- | --- |
```

## Anti-Patterns

- Automating the current messy process without defining the real problem.
- Building an agent before the data template exists.
- Treating every node as a prompt.
- Letting one agent own multiple unrelated failure modes.
- Optimizing symptoms instead of root causes.
- No signal ledger after deployment.
- No proof that repeated questions or handoff failures decreased.
