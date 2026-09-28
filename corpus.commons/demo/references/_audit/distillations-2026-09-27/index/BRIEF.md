# Distillation-index audit brief

The runtime router of each compiled app is generated from a task's `{TASK-UPPERCASE}-DISTILLATION-INDEX.md`. Each row points a practitioner's need or trigger at one distillation, with a short description of what that distillation offers. Nobody has audited these rows against the distillations they point to. You do that for one task axis and a set of sources named in your prompt. Work from ``. Edit no file other than your outputs.

## Read
1. The index file: `corpus.commons/demo/distillations/{task}/{TASK-UPPERCASE}-DISTILLATION-INDEX.md`, in full, so you know its phases, tables and column formats.
2. For each source in your prompt, the distillation `corpus.commons/demo/distillations/{task}/{slug}-{task}.md`, in full.

Use `/usr/bin/grep -n -F` for searches; the default grep is ugrep and errors on complex patterns.

## Check
Every line of the index that names one of your distillations (`{slug}-{task}.md`): table rows, catalogue entries and summary lines. For each, ask:
- Does the distillation carry what the row says it does? The framework, concept, author, chapter, count or claim named in the row must appear in the distillation. A row that promises content the distillation lacks sends the runtime to the wrong file.
- Is the row's description faithful to the distillation? Watch for credits to authors the distillation does not credit (for example a theorist the source never names), hardened hedges ("must" for "should", "always" for "often"), wrong counts, wrong chapters, and quotation marks around words that are not in the distillation.
- Trigger wording copied from the task spec (the first column of a listener-table row) is fine as a trigger; the rest of the row must still match the distillation.

The distillations were repaired on 2026-09-27 and are the reference here: fix the row, not the distillation.

## Output
Write `{scratchpad}/repair/index-audit/{task}-{batch}.json`, where `{batch}` is in your prompt:
```json
{"task": "...", "sources": ["..."], "rows_checked": 0, "rows_ok": 0,
 "edits": [{"file": "<index path from repo root>", "old": "<the whole line, exactly as it is>", "new": "<corrected whole line, or empty to delete the row>", "why": "<one line: what the row claimed and what the distillation carries (with its line number)>"}],
 "notes": "..."}
```
Keep each row's column count and its trigger wording. Prefer correcting a row to deleting it; delete only when the distillation carries nothing that serves the row's need. Copy each `old` line byte for byte from the file.
