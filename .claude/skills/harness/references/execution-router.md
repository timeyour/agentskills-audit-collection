# Execution Router

Use this reference to choose the right execution mode for each step.

## Modes

| Mode | Use When | Avoid When | Evidence |
| --- | --- | --- | --- |
| `PROMPT` | One-off reasoning, summary, drafting, classification, ideation. | Repeatability, strict validation, external side effects, or hidden state matter. | Prompt, input, output, reviewer check. |
| `SKILL` | A repeatable agent workflow with known structure and output format. | The step is too project-specific or needs deterministic code. | Skill name, output artifact, issue/check table. |
| `DIFY` | Multi-step LLM workflow, API chain, knowledge base, form-to-output business automation. | UI-only tasks, brittle browser interactions, or high-judgment approvals. | Workflow ID/name, input/output schema, run log. |
| `RPA` | UI-only repetitive operation where no API or direct integration exists. | API, code, or stable export/import path exists. | Screen path, selectors/images, run log, fallback. |
| `CODE` | Deterministic transform, parser, data validation, tests, scraping, integration, batch job. | Human judgment or ambiguous business context dominates. | Command, test output, artifact diff/log. |
| `HUMAN` | Approval, brand judgment, legal/privacy, payment, credential entry, relationship handling, irreversible action. | It can be objectively automated with low risk. | Decision record, owner, timestamp, rationale. |
| `EXTERNAL` | SaaS/API/platform action outside the agent's direct control. | The agent cannot verify result or side effect. | API response, console screenshot, webhook/log. |

## Routing Heuristics

- Prefer `SKILL` for repeatable reasoning workflows.
- Prefer `CODE` for deterministic, testable transforms.
- Prefer `DIFY` for reusable business automation with structured inputs and outputs.
- Prefer `RPA` only when UI is the only available integration.
- Require `HUMAN` when judgment, permission, money, private data, or irreversible change is involved.
- Use `PROMPT` only for low-risk, low-repeatability units.

## Route Output

Each routed unit should answer:

1. Why this mode?
2. What input schema does it need?
3. What output schema must it produce?
4. What evidence proves it worked?
5. What failure should trigger retry?
6. What failure should trigger human escalation?
