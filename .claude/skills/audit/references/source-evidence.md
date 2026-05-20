# Source Evidence

Use this reference during the source pass of an audit.

## Evidence Types

- `source claim`: gallery card, docs, README, community post, landing copy, product page.
- `live evidence`: actual loaded page, clicked workflow, screenshot, browser locator, network/console result.
- `execution evidence`: CLI output, test result, Playwright trace, Lighthouse/axe result, source diff.
- `inferred evidence`: reasonable guess from source material; always mark low confidence.

## Required Fields

| Field | Meaning |
| --- | --- |
| Source URL | Where the claim came from. |
| Claim | What is being claimed. |
| Locator | Text, line, selector, screenshot area, route, or section. |
| Confidence | high / medium / low. |
| Needs live proof? | yes / no. |
| Next check | What would prove or disprove it. |

## Confidence Rules

- `high`: explicit source claim plus live evidence or execution evidence.
- `medium`: explicit source claim, but live behavior not tested.
- `low`: gallery card, visual inference, sparse crawl, or unclear attribution.

## Guardrails

- Never merge source evidence and live evidence into one column.
- Mark auth-gated flows separately from public flows.
- Mark screenshots and browser traces as stronger than text crawls for visual claims.
- Mark tool/CLI/extension claims as source-pass until executed.
