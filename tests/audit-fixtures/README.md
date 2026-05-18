# Pass I audit fixtures

Hand-crafted snippets used to calibrate and regression-test the Pass I source-only audit (the gate at the end of the [9-pass ingestion protocol](../../.claude/skills/ingesting-resources/9-pass-protocol.md)). Each fixture is a short deep-reference excerpt with one violation embedded (or, in the negative-control case, no violation). The expected auditor finding is recorded in the file's frontmatter.

These fixtures are test data, not corpus material. The build does not ship them — `build.js` only walks `corpus.commons/{corpus}/`, `docs/`, `.claude/skills/`, `build-profiles/`, and a small handful of other shipped-content roots.

## Why this directory exists

Anthropic's [harness-design article](https://www.anthropic.com/engineering/harness-design-long-running-apps) flagged a recurring pattern: agents that evaluate their own work tend to praise it, and tuning a separate evaluator with explicit calibration is far more tractable than making a generator self-critical. Pass I is this repo's separate evaluator. The fixtures give it a known-bad set to anchor against, and a regression set to re-run when adopting a new model.

The article also noted that "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing." The 9 passes were designed for one model class; the fixtures are how this repo verifies Pass I still earns its keep on the next.

## Layout

Each fixture is a markdown file with YAML frontmatter and a body. Filenames encode the failure mode (`01-training-leakage.md`, `12-clean-negative-control.md` and so on); ordering is presentational, not semantic.

```
tests/audit-fixtures/
├── README.md                          (this file)
├── 01-training-leakage.md
├── 02-post-source-vocabulary.md
├── 03-cross-corpus-drift.md
├── 04-distillation-guidance-in-deep.md
├── 05-verbatim-smart-quote-tidy.md
├── 06-verbatim-capitalisation-tidy.md
├── 07-marker-mismatch-V-without-verbatim.md
├── 08-marker-mismatch-BT-without-source-citing.md
├── 09-verbatim-quote-in-distillation.md
├── 10-uncited-author-cross-reference.md
├── 11-silent-partial-coverage.md
└── 12-clean-negative-control.md
```

## Fixture frontmatter contract

```yaml
---
id: NN-short-slug
failure_mode: <canonical name from the failure-mode reference>
severity: <strip | correct | none>
expected_finding: <one sentence the auditor should produce>
seed_source: <slug of the deep ref whose style this mimics, or "synthetic">
tier: <deep | distillation>
---
```

`severity` of `strip` means the violating sentence must be removed; `correct` means it must be amended in place (typically a marker change or a verbatim repair); `none` is the negative control.

## Two uses

**Calibration (in-prompt few-shot).** A small subset of these fixtures is referenced from the Pass I procedure in [`.claude/skills/ingesting-resources/9-pass-protocol.md`](../../.claude/skills/ingesting-resources/9-pass-protocol.md) as exemplars. The auditor reads them before reading the deep reference under audit, anchoring its sense of what counts as a violation. Today the prompt cites three: training leakage (`01`), marker mismatch (`07`), and the negative control (`12`). Adding more anchors at the cost of prompt length is a tuning decision the operator can make per run.

**Regression test (operator-invoked).** When a new model is adopted, run `tests/run-audit-fixtures.sh` from the repo root. The script prints each fixture's frontmatter and body, then asks the operator to record whether Pass I (running under the new model) flagged the violation correctly. The output is a checklist; the operator decides whether the auditor still earns its keep before rolling the model into the protocol.

This is intentionally not an automated LLM-in-the-loop runner. The audit is a judgement call; mechanising the verdict would be the same self-evaluation trap the article warns against. The runner's job is to present the fixture and capture the operator's verdict, nothing more.

## When to run

- Adopting a new model in [the protocol](../../.claude/skills/ingesting-resources/9-pass-protocol.md) (e.g. moving from Opus 4.7 to a successor).
- After non-trivial edits to the Pass I procedure or its calibration exemplars.
- After observing a Pass I miss in a real ingestion (add a new fixture matching the miss; re-run).

You do not need to run the fixtures on every ingestion. Pass I already runs once per source as part of the protocol; the fixtures verify Pass I itself, not individual sources.

## Adding a fixture

1. Pick a failure mode (one of those listed in the [failure-mode reference](../../.claude/skills/ingesting-resources/9-pass-protocol.md#failure-mode-reference)) or a new one observed in the wild.
2. Take a 5-15 line excerpt from a real deep reference whose style you want the fixture to mimic. Edit a single sentence to inject the violation. Record the original `seed_source` slug in frontmatter so future readers can compare.
3. Write a frontmatter `expected_finding` that reads as the auditor's own report — not a description of the violation, but the sentence Pass I should produce on encountering it.
4. Add the fixture to the regression runner's list. Adding to the calibration exemplars is a separate, intentional decision; do not auto-add.

A fixture that the auditor catches trivially in every model generation is not load-bearing. Keep the set small and skewed toward the violations that have actually slipped past audit in past ingestions.
