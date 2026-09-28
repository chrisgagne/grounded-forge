# Demo distillation repair — per-source brief

You are repairing ONE source's deep reference and distillations in the demo corpus, using an audit that a fresh Opus model ran against them. Work from ``. Your source slug and its distillations are in your prompt. An independent auditor will check every line you change against the converted source, so each edit must hold up on its own.

Paths (from the repo root):
- Deep ref: `corpus.commons/demo/references/{slug}-deep.md`; light ref: `corpus.commons/demo/references/{slug}.md`
- Converted source: `corpus.commons/demo/sources/converted/{slug}.md`
- Distillations: `corpus.commons/demo/distillations/{task}/{slug}-{task}.md`
- Audit findings, one JSON per distillation: `corpus.commons/demo/references/_audit/distillations-2026-09-27/{slug}-{task}.json`
- Deep-ref fix list: `corpus.commons/demo/references/_audit/distillations-2026-09-27/DEEP-REF-FIXES.md` (take your source's sections and every CROSS-FILE line that names your source or its distillations)
- Your outputs: `{scratchpad}/repair/out/`

Use `/usr/bin/grep -n -F` (or `-i -F`) for searches; the default grep is ugrep and errors on complex patterns.

## Read first
1. `.claude/skills/creating-distillations/projection-protocol.md`: what a distillation may contain. Applied guidance (questions to ask, what to look for, worked examples) is the distillation's job; claims about what the author says must trace to the deep reference.
2. The deep reference, in full. Then each audit JSON for your source, and your DEEP-REF-FIXES.md lines.

Full coverage is a gate. Read the deep ref and each distillation end to end. When you verify a finding at source, read the cited passage plus enough surrounding text to be sure of its meaning. When a fix asks you to extend coverage of a section, read that whole section of the source before you write. If you cannot read something in full, say so in your report and leave that item undone.

## Phase 1: deep reference (and light reference)
Apply, after checking each against the converted source:
- every deep-ref error in DEEP-REF-FIXES.md for your source;
- every finding whose fix begins `cycle-to-deep` (or that says the source supports a claim the deep ref lacks). Add the passage to the deep ref.

Write additions in the deep ref's own style: put them in the section that covers that part of the source (in the source's order), use the same locator format, e.g. `(Ch 6.4, "Section title")`, and mark evidence the same way. `[V]` means the source's words exactly; copy the quotation character for character from the converted source. `[BT]` means the source relaying someone else. `[AP]` means paraphrase.

Correct errors in place and write the corrected text as if it had always been there: no "corrected", "previously" or dated notes.

If a deep-ref correction changes something the light ref also states, correct the light ref the same way (grep it). Leave frontmatter as it is unless a fix requires a change there. Leave every provenance stamp line alone; the orchestrator re-stamps.

## Phase 2: distillations
For each distillation, work through its findings in order. For each finding:
1. **Re-verify.** Check the claim against the deep ref (after your Phase 1 edits) and, where it matters, the converted source. Auditors are sometimes wrong: a finding can say "no hits" for text that is there, or name the wrong chapter.
2. **Decide.** `applied` (the audit's fix, as written), `revised` (your own fix, because the audit's is wrong or clumsy), or `rejected` (the claim was right; no edit).
3. **Edit.**
   - CONTRADICTED: correct it to what the source says.
   - UNSUPPORTED: if the source supports it, add it to the deep ref (Phase 1) and keep it. If it is outside knowledge (a framework, study, statistic, law or author the source does not carry), remove it; where the point still helps the reader as the distillation's own applied guidance, keep it without attributing it to the author or the source.
   - MINOR-DRIFT: fix the wording, citation, chapter, count or marker.
   - Many findings say "recurs at lines …". Fix every recurrence, and grep all your distillations for the same error; the audit often logged only the first.
   - Write every fix as if the corrected text had always been there. Keep sentences flowing and tables intact; if you remove a claim, repair the sentence or list around it.
   - Every `[V]` you keep or write must match the converted source word for word (grep for it). Mark a verbatim quotation `[V]` when the words are the author's own, and `[BT]` when the source quotes someone else. A section title inside a citation is a pointer and carries no marker.
   - Change only what the findings, their recurrences, and your Phase 1 corrections require. Leave the rest of the text alone.
   - Leave each distillation's provenance stamp line alone.
4. Cross-source claims: when a distillation's claim about ANOTHER corpus source is wrong, fix the claim in your distillation by checking that source's deep ref (`corpus.commons/demo/references/{other}-deep.md`). Edit no other source's files.

Your source's own figures come first. If the audit says the source itself is wrong (a SOURCE ERROR line), keep the source's figure as the source gives it, and put it under `for_chris` in your log.

## Phase 3: index rows
The runtime routing indexes are generated from `corpus.commons/demo/distillations/{task}/{TASK-UPPERCASE}-DISTILLATION-INDEX.md`. These files are shared with other agents, so **edit none of them**. Instead, for each of your distillations, find every line in that task's index that names your distillation file (`/usr/bin/grep -n -F "{slug}-{task}.md"`), and check the row's text against your repaired distillation. Where a row carries an error you fixed, or a claim your distillation no longer makes, propose a replacement line.

Write the proposals to `out/{slug}-index-edits.json` as a list:
```json
[{"file": "corpus.commons/demo/distillations/aar/AAR-DISTILLATION-INDEX.md", "old": "<the whole line, exactly as it is>", "new": "<the whole replacement line, or empty to delete the row>", "why": "<one line>"}]
```
Keep each row's column count and its trigger/when wording; change only what the fix requires. Write `[]` when no row needs a change.

## Logs: write as you go
- After Phase 1, write `out/{slug}-deep.json`: `{"slug": "...", "changes": [{"where": "deep|light", "line": N, "kind": "fix|cycle-to-deep|coverage", "what": "<one line>", "source_lines": "<converted-source line range>"}], "not_done": [], "for_chris": []}`.
- After each distillation, before starting the next, write `out/{slug}-{task}.json`: `{"distillation": "<path>", "findings": {"D001": {"action": "applied|revised|rejected", "note": "<one line; required for revised and rejected>"}}, "extra_fixes": ["<recurrences or related fixes beyond the listed findings, one line each>"], "for_chris": []}`. Cover every finding ID in the audit JSON.

## Report back
Per distillation: findings applied / revised / rejected, plus extra fixes. Deep ref: fixes and additions made, and anything not done. Then list anything that needs Chris's decision, one line each.
