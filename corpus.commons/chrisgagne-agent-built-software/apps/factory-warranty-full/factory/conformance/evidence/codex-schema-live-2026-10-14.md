# Live check of the Codex reviewer's output schema (2026-10-14)

One `legs.run_codex` call, model gpt-6.1-sol, with `--output-schema` set to CODEX_FINDINGS_SCHEMA (factory `fbe025a`), on a one-file folder (`a.js`: `add` returns `a - b`). Codex accepted the schema, exited 0, used 16,037 tokens, and its final message parsed and passed `validate_findings`.

Final message, verbatim:

```json
{"findings":[{"severity":"medium","file":"a.js","line":1,"claim":"The add function subtracts instead of adding its arguments.","evidence":"The implementation returns `a - b`. Calling `add(2, 3)` returns -1 instead of the expected 5. Change the expression to `a + b`.","axis_row":null}]}
```
