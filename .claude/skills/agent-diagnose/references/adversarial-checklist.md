# Adversarial Review Checklist

Use this checklist to force behavioral skepticism. Not every item applies to every change.

## Spec and Scope

1. Does every acceptance criterion have implementation coverage?
2. Does every acceptance criterion have verification coverage?
3. Did the implementation change behavior outside the stated scope?
4. Are assumptions documented and still valid?
5. Is any out-of-scope work hidden in the diff?
6. Are public APIs, CLI flags, schemas, or UI contracts changed intentionally?

## Happy Path

7. Does the primary path work from start to finish?
8. Are outputs observable and aligned with the spec?
9. Does the implementation preserve expected defaults?
10. Are user-facing messages accurate and actionable?

## Edge Cases

11. Empty input.
12. Null or missing fields.
13. Very large input.
14. Duplicate input.
15. Invalid format.
16. Boundary values.
17. Timezone, locale, or encoding differences.
18. Existing data from older versions.

## Error Paths

19. External service failure.
20. Network or filesystem failure.
21. Permission denied.
22. Partial failure and retry behavior.
23. Cleanup after failure.
24. User-facing error clarity.

## State and Data

25. State transitions are valid and reversible where needed.
26. Persistence is correct.
27. Concurrent operations do not corrupt state.
28. Idempotency is preserved where expected.
29. Migrations or compatibility paths are covered.

## Security and Safety

30. No secrets or credentials are hardcoded.
31. Inputs are validated before trust boundaries.
32. Logs do not expose sensitive data.
33. Authn/authz assumptions are explicit.
34. Injection, path traversal, and unsafe shell execution risks are addressed.

## Drift

35. No unrelated formatting churn.
36. No dead code or abandoned alternatives.
37. No new TODO/FIXME without owner or reason.
38. No premature abstraction.
39. No duplicated logic that should share an existing local pattern.
40. No tests weakened, skipped, or deleted without justification.
