# Examples

The examples in this directory are validation fixtures, not the product itself.

`examples/todo_cli/` exists to prove that the AgentSkills workflow can turn a small requirement into:

- a spec;
- tests;
- implementation;
- review findings;
- regression checks;
- learning notes.

Run the validation tests from the repository root:

```bash
python3 -m unittest discover -s tests
```

The skills do not depend on this example. It is included so the repository has executable proof, not only Markdown instructions.
