# Repair diff audit brief

Another model has just repaired ONE demo source's deep reference and distillations after an audit. You check the repair. You did not write it. Work from ``. Your source slug is in your prompt.

Get the changes with:
```
git diff HEAD -- corpus.commons/demo/references/{slug}-deep.md corpus.commons/demo/references/{slug}.md corpus.commons/demo/distillations/*/{slug}-*.md
```
Ignore changes to `<!-- derived-from-deep: ... -->` stamp lines. Also check the index rows changed for your source: in `git diff HEAD -- 'corpus.commons/demo/distillations/*/*-INDEX.md'`, the added lines that name one of your source's distillation files (`{slug}-`). Each must match the distillation it points to.

## Check every added or changed line
- **Deep ref and light ref:** each added or corrected statement must match the converted source (`corpus.commons/demo/sources/converted/{slug}.md`). Read the cited passage with enough context to be sure. Check the locator (chapter, section, page) and the evidence marker.
- **Distillations:** each added or corrected claim about what the source says must trace to the deep ref as it now stands. Applied guidance (questions, patterns, worked-example steps) is allowed if it attributes nothing to the author that the deep ref does not carry. Claims about other corpus sources must match that source's deep ref (`corpus.commons/demo/references/{other}-deep.md`).
- **`[V]`:** the quoted words appear word for word in the converted source (`/usr/bin/grep -n -F`; the default grep is ugrep and errors on complex patterns). `[BT]` where the source relays someone else.
- **Edit quality:** broken sentences, orphaned list items, table rows with the wrong column count, leftover traces of the edit ("corrected", "previously", "note:"), and the same error still present elsewhere in the changed files.
- **Removals:** flag a removed claim only if the deep ref fully supported it and nothing in the audit record justified removing it (`corpus.commons/demo/references/_audit/distillations-2026-09-27/{slug}-{task}.json`).

- **Flagged quotations:** if `{scratchpad}/repair/vflags/{slug}.json` exists, it lists `[V]` quotations in your source's distillations that a mechanical checker could not find in the converted source, even ignoring punctuation (`kind: MISS`), or found only in another source (`kind: CROSS:{slug}`). Check every one, including those marked `pre_existing`: read the source passage and grade it. A difference only in line-break hyphenation, OCR garbling, page headers or footnote numbers inside the passage is FAITHFUL; any changed, added or dropped word is MINOR-DRIFT with an exact `correct:` fix. A CROSS quotation is FAITHFUL when the distillation attributes it to that other source.

Read each changed file in full once, so you judge each change in context. Full coverage is a gate; if you cannot read something, say so.

Grades: FAITHFUL, MINOR-DRIFT, UNSUPPORTED, CONTRADICTED, EDIT-DEFECT.

## Output
Write `{scratchpad}/repair/diffaudit/{slug}.json`:
```json
{"slug": "...", "changed_lines_checked": 0, "tally": {"faithful": 0, "minor_drift": 0, "unsupported": 0, "contradicted": 0, "edit_defect": 0},
 "findings": [{"file": "...", "line": 0, "text": "...", "grade": "...", "problem": "...", "evidence": "<source or deep-ref lines>", "fix": "correct: <exact replacement> | strip | re-mark: <marker>"}],
 "notes": "..."}
```
List every non-FAITHFUL line. Edit no file other than your output. Write the JSON early and rewrite it after each file you finish checking, so your progress survives an interrupted run; keep each tool call small (a few hundred lines per read, one grep at a time).
