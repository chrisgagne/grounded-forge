# MCDP-1 distillation regeneration brief

You are regenerating ONE distillation of `mcdp1-warfighting` (U.S. Marine Corps, *MCDP 1: Warfighting*, 1997) for one task axis in the demo corpus. The task is in your prompt. Work from ``. The existing distillation predates the template and an audit found it the least faithful in the corpus, so you are replacing it, not patching it. An independent auditor will check every claim you write against the deep reference and the source.

## Read, in this order
1. `.claude/skills/creating-distillations/SKILL.md` and `.claude/skills/creating-distillations/projection-protocol.md`. Follow them: Pass G.0 applicability gate, the nine-section template in order, concept anchors, citation discipline, and (if the task spec has a seed trigger→response table) the two trigger-grain sections.
2. The task spec: `corpus.commons/demo/tasks/{task}.md`, including its seed trigger→response table.
3. The deep reference, in full: `corpus.commons/demo/references/mcdp1-warfighting-deep.md`. It is the only content input. Its Pass-D `[V]` passages are what you quote.
4. For structure only, one well-audited distillation on the same axis: `corpus.commons/demo/distillations/{task}/nhs-just-culture-guide-{task}.md`. Match its shape and header; take none of its content.
5. The audit of the distillation you are replacing: `corpus.commons/demo/references/_audit/distillations-2026-09-27/mcdp1-warfighting-{task}.json`. Every finding is a mistake the new file must not repeat. Read the old file (`corpus.commons/demo/distillations/{task}/mcdp1-warfighting-{task}.md`) only to see which phases it tried to serve.
6. The task's index, `corpus.commons/demo/distillations/{task}/{TASK-UPPERCASE}-DISTILLATION-INDEX.md`: its phases and the rows other sources contribute. Do not edit it.

Full coverage is a gate: read the deep ref, the task spec and the audit JSON end to end. If you cannot, stop and say so.

## Rules that the old file broke
- Every claim about what MCDP 1 says traces to a passage of the deep ref. The source is a Marine Corps doctrine pamphlet: it does not mention software, DORA, XP, Blue Ocean, Coram, Marquet, Goldratt, agile, lean or any business framework. Applied guidance for the task (questions, patterns, the worked example) is yours to write, and must not put words in the doctrine's mouth.
- Claims about other corpus sources (Integration section) must match those sources' deep refs (`corpus.commons/demo/references/{slug}-deep.md`). Open each one you cite. The demo corpus slugs are the files in `corpus.commons/demo/references/` ending `-deep.md`.
- `[V]` = the source's words, word for word in the converted source `corpus.commons/demo/sources/converted/mcdp1-warfighting.md`. The deep ref restored some OCR-garbled spellings ("he" for the scan's "be", "commitment" for "commitruent", "Force" for "Eorce") and straightened quote marks. Grep each quotation (`/usr/bin/grep -n -F`, trying a distinctive fragment if the whole line misses) and prefer passages that match as they stand. Where the passage you need carries an OCR garble, quote it with the deep ref's restoration and list it in your report with its source line. Two to five verbatim blockquotes, per the protocol. Scope is `open`, so `[V]` is permitted.
- `[BT]`, never `[V]`, for words the source quotes from someone else: the epigraphs, Clausewitz, Sun Tzu, Patton, Napoleon, Gelernter, the Joint Pub definitions. The deep ref now marks these `[BT]`; keep its marker.
- The deep ref was cleaned of non-source content on 2026-09-27 (no Auftragstaktik, Schwerpunkt, Boyd lineage, Klein, Goldratt or after-action-review parallels). None of it comes back, including in the Integration section: MCDP 1's word for its review practice is *critique*.
- Numbers, counts and enumerations match the deep ref exactly.
- Worked example: the scenario is yours; any outcome it reports is the scenario's, never the doctrine's demonstrated effect.

## Pass G.0
Run the applicability gate honestly. If the answer for your task is *clear no*, do not write the file: report the reasoning and stop. If it is ambiguous, say so in your report with a recommendation, and proceed with the file.

## Output
1. Overwrite `corpus.commons/demo/distillations/{task}/mcdp1-warfighting-{task}.md`. First line, a generation comment in the same format as the NHS file's (model: claude-opus-5-5; date 2026-09-27; Task: {task}). Omit the `derived-from-deep` stamp line; the orchestrator re-stamps.
2. Index proposals at `{scratchpad}/repair/out/mcdp1-warfighting-{task}-index-edits.json`, a list of:
   - `{"file": "<index path from repo root>", "old": "<whole existing line naming this distillation>", "new": "<replacement line, or empty to delete>", "why": "..."}` for each existing line that names `mcdp1-warfighting-{task}.md`;
   - `{"file": "...", "after": "<whole existing line to insert below, e.g. the last row of the right phase table>", "new": "<new row>", "why": "..."}` for each new listener-table or phase row, following the column format of the rows around it and lifting trigger wording verbatim from the task spec's seed table.
3. Report: the applicability verdict, section-by-section line counts, the `[V]` quotations used (each with its converted-source line), how you avoided each class of the old audit's findings, and the index proposals in one line each.
