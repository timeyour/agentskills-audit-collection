# Checkpoint And Retry Policy

Use this reference to make AI-assisted workflows safe to run repeatedly.

## Checkpoint Types

| Type | Use When | Evidence |
| --- | --- | --- |
| `AUTO-STRUCTURE` | Output format, schema, required fields, or file presence can be checked automatically. | Schema validation, table row count, file path, parser result. |
| `AUTO-BEHAVIOR` | A command, test, browser flow, API call, or link check can verify behavior. | Test output, HTTP status, screenshot, console/network log. |
| `AUTO-QUALITY` | A score/rubric can detect obvious quality issues. | Rubric score, issue count, lint/a11y/perf output. |
| `HUMAN-JUDGMENT` | Taste, brand, strategy, stakeholder alignment, or ambiguous tradeoff matters. | Decision note and rationale. |
| `HUMAN-RISK` | Private data, credential, payment, legal, irreversible, or destructive action appears. | Explicit approval record. |

## Retry Rules

| Failure Type | Retry? | Strategy |
| --- | --- | --- |
| Missing required field | Yes | Retry with schema reminder and missing-field list. |
| Broken format | Yes | Retry with exact expected format and example. |
| Tool/network transient failure | Yes | Retry with backoff or alternate tool. |
| Ambiguous requirement | No blind retry | Ask human or run `/skill-study`/`/harness` to clarify. |
| Low-quality reasoning | Yes | Retry with critique, evidence gap, and narrower task. |
| Repeated same failure | Stop | Change mode, escalate, or split step smaller. |
| Permission/payment/private action | No | Human checkpoint required. |
| Destructive action | No | Human checkpoint and rollback plan required. |

## Retry Limits

Default:

- Low-risk formatting/content: 2 retries.
- Tool/network transient: 2 retries plus fallback.
- Browser/RPA: 1 retry, then human or alternate integration.
- Production side effect: 0 blind retries.

## Escalation Triggers

Escalate when:

- the same checkpoint fails twice;
- evidence is insufficient but the next step depends on it;
- a human approval is required;
- the agent would need credentials or private data;
- a workflow touches money, deletion, publication, outreach, or legal/privacy decisions;
- the correct execution mode is unclear.

## Checkpoint Row

| Field | Meaning |
| --- | --- |
| Step | Unit being checked. |
| Checkpoint | What must be true. |
| Automatic/Human | Who or what checks it. |
| Pass condition | Exact condition to continue. |
| Fail condition | Exact condition to retry, split, or escalate. |
| Evidence | Artifact or locator proving the result. |
| Owner | Agent, human, external system, or tool. |
