# Business Decomposition

Use this reference to split a business goal into executable layers.

## Decomposition Ladder

1. Business outcome
   - What real-world result should change?
   - Who benefits?
   - What metric, artifact, or decision proves success?

2. Business stages
   - Major phases in the customer/operator journey.
   - Example: discover -> qualify -> prepare -> execute -> verify -> follow up.

3. Substeps
   - Smaller actions inside each stage.
   - Example: collect URL -> identify CTAs -> click CTA -> record result -> classify issue.

4. Execution units
   - A unit is ready when it has:
     - one input;
     - one output;
     - one execution mode;
     - one checkpoint;
     - one owner;
     - one retry rule.

5. Acceptance units
   - What must be true before moving to the next stage?

## Split Until Clear

Keep splitting when:

- the step has multiple owners;
- the step has multiple tools;
- the output is vague;
- failure would be hard to locate;
- a human decision is hidden inside the step;
- retry behavior differs by failure type;
- a later step depends on unverified data.

Stop splitting when:

- input and output are explicit;
- evidence can prove pass/fail;
- the tool choice is obvious;
- retry/fallback is clear;
- the unit can be delegated or executed independently.

## Echo And Delta

Use the FDE-inspired split:

- `Echo`: demand discovery, context capture, translation, narrative, stakeholder alignment.
- `Delta`: build, integrate, deploy, test, automate, monitor.

Long-cycle and long-chain products usually need both.

## Stage Tree Fields

| Field | Meaning |
| --- | --- |
| Level | 0 for business goal, 1 for stage, 2 for substep, 3+ for execution unit. |
| Stage | Business phase. |
| Step | Concrete action. |
| Input | What the unit needs. |
| Output | What the unit produces. |
| Owner | Agent, human, system, or external party. |
| Dependency | Tool, data, permission, credential, API, or prior output. |
