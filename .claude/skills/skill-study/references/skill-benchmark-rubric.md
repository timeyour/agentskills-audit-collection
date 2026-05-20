# External Skill Benchmark Rubric

Use this rubric to study other AgentSkills, open-source skill repos, workflow prompts, tool recipes, and AI builder examples.

## Score Dimensions

Score each external skill or pattern from 0-3.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Trigger clarity | Vague topic | Some cue words | Clear use cases | Clear, testable trigger conditions |
| Task boundary | Undefined | Broad topic | Bounded workflow | Explicit scope and stop conditions |
| Evidence discipline | None | Source only | Source + expected output | Source/live/tool evidence split |
| Workflow shape | Tips | Loose steps | Repeatable sequence | Repeatable sequence with failure handling |
| Validation | None | Manual check | Acceptance checklist | Edge cases, retest, and pass/fail verdict |
| Output usefulness | Paragraph | Checklist | Structured artifact | Copyable fixes, issue cards, benchmark updates |
| Portability | Tool-locked | Framework-specific | Adaptable | Stateless and project-agnostic |
| Anti-pattern coverage | None | Generic warnings | Known failure modes | Actionable failure probes |

## Adoption Labels

- `ADOPT`: score is strong and pattern directly improves an existing AgentSkill.
- `ADAPT`: useful but needs conversion to this repo's audit workflow.
- `REFERENCE`: keep as benchmark inspiration only.
- `REJECT`: too broad, too basic, too brittle, or unsupported.

## Extraction Questions

Ask these questions for every external skill:

1. What concrete user request should trigger it?
2. What does it make the agent do that a generic prompt would miss?
3. What artifact does it produce?
4. What evidence does it require before claiming success?
5. What edge cases or adversarial failures does it catch?
6. What should be copied into our skills, and what should stay out?

## Conversion Rules

- Convert topics into workflows.
- Convert claims into evidence requirements.
- Convert examples into benchmark cases.
- Convert repeated failures into guardrails.
- Convert broad soft skills into review behavior.
- Convert tool-specific recipes into optional execution notes unless the tool is required.

## Reject Rules

Reject or downgrade patterns that:

- only say "be better" without actions;
- require hidden session state;
- depend on proprietary UI steps without fallback;
- duplicate an existing skill without adding coverage;
- create basic curriculum instead of improving audit behavior;
- cannot produce an observable output.
