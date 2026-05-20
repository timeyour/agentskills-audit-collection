# /review Validation Output: TODO CLI

## Issues Found

- `MEDIUM` Invalid TODO item shape was not rejected clearly.
  - Evidence: initial `load_todos` only checked that parsed JSON was a list. A file like `[{"id": "one"}]` would load and later fail through `KeyError` or type-sensitive behavior.
  - Resolution: Added `test_invalid_item_shape_raises_clear_error` before implementation, then added item-shape validation in `load_todos`.
  - Status: Fixed.

- `LOW` Local atomic commit could not be completed in this sandbox.
  - Evidence: `git init -b main` returned `Operation not permitted`.
  - Impact: Does not affect TODO CLI behavior, but prevents fully validating the commit step locally.
  - Status: Documented in `validation/tdd.md`.

## Verdict

PASS WITH NOTES

The implementation satisfies the agreed behavior after the review-driven fix. The remaining note is environmental, not behavioral.

## Spec Coverage

- `add` stores a pending item and prints its id: covered by unit and CLI tests.
- `list` shows pending/done state and titles: covered by formatting and CLI tests.
- `done` marks an existing item complete: covered by unit and CLI tests.
- Empty titles are rejected: covered by unit test.
- Missing id exits non-zero: covered by CLI test.
- Missing JSON file behaves as empty list: covered by unit test.
- Corrupt or invalid JSON file reports a clear error: covered by syntax and item-shape tests.

## Behavior Checks

- Happy path: add/list/done round trip passed.
- Edge cases: empty title, missing file, invalid item shape passed.
- Error paths: corrupt JSON and missing id passed.
- State transitions: pending to done covered.
- Boundary conditions: next id increments from existing data.

## Regression Checks

Command:

```bash
python3 -m unittest discover -s tests
```

Result:

```text
Ran 10 tests
OK
```

Manual smoke:

```text
Added #1: manual smoke
[ ] #1 manual smoke
Done #1: manual smoke
[x] #1 manual smoke
```

## Drift Detection

- No files were added inside `.claude/skills/*/scripts`.
- Validation code is isolated under `examples/`, `tests/`, and `validation/`.
- No unexpected feature expansion beyond add/list/done.

## Security Scan

- No hardcoded secrets found.
- No `shell=True`, `eval`, or unsafe command construction in implementation.
- CLI only reads/writes the file path explicitly passed via `--file`.

## Residual Risk

- The sample TODO CLI is intentionally minimal and not packaged for installation.
- Local git commit validation remains blocked until a repository can be initialized or a GitHub target is provided.
