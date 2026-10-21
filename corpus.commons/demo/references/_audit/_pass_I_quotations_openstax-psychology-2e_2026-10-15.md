# Pass I quotations audit: openstax-psychology-2e (2026-10-15)

**Mode:** quotations. Deep reference read in full (514 of 514 lines). Source: `corpus.commons/demo/sources/converted/openstax-psychology-2e.md` (47,143 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the four distillations (aar, decision-making, retro, stakeholder-engagement), plus the human triage row. A second scan matched every quoted span in those six files (whatever its marker) against the normalised source, to catch wrong quotations the checker does not see because they sit outside `[V]` segments.

## Counts

- Actionable checker lines worked: 3 (1 missing, 1 interrupted, 1 no-quote).
- Further quotations checked from the full-file scan: 4 deep-ref lines with a quoted span absent from the source or verbatim under a non-`[V]` marker (103, 248, 252, 285).
- Quotation-corrected: 3 lines in the deep ref (75, 248, 285).
- Marker-corrected: 2 lines in the deep ref (103, 252: verbatim quotes under `[AP]` now `[V]`, paraphrase keeps `[AP]`). Line 285's `[AP]` became `[V]` with its rewrite.
- Stripped: 0.
- Derived-tier edits: 0.
- Left as is (conversion noise): 2 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 75 | no-quote (triage row): Table 3.1 summarised under `[V]`, and three cells were wrong. The deep ref gave dopamine "(mood, sleep, learning, reward, addiction)", GABA "(quieting/inhibition)" and norepinephrine "(arousal)"; the table's "Involved in" column reads "Mood, sleep, learning", "Brain function, sleep" and "Heart, intestines, alertness" | Each neurotransmitter's "Involved in" cell now quoted exactly, under the table's title, "Major Neurotransmitters and How They Affect Behavior"; GABA given its full name as the table does. `[V]` kept; citation now names the "Neurotransmitters and Drugs" subsection | src 5092–5115 (Ch 3.2) |
| 103 | `[AP]` over two verbatim quotes, one capitalised against the source ("The whole is…") | Gestalt-principles list keeps `[AP]`; the thesis now quoted as the source has it, "the idea that the whole is different from the sum of its parts" `[V]`; "educated guesses that we make while interpreting sensory information" now `[V]`; the paraphrase that follows keeps `[AP]` | src 9749–9751, 9842–9843 (Ch 5.6) |
| 248 | unmarked quote "we are afraid because we tremble" not in the source | Replaced with the source's own statement: the theory "asserts that emotions arise from physiological arousal" `[V]` | src 19670 (Ch 10.4) |
| 252 | Barrett quote verbatim but marked `[AP]` | Paraphrase ("concept-based predictions that construct experience") keeps `[AP]`; the quote is now `[V]` | src 19823–19825 (Ch 10.4) |
| 285 | `[AP]` over a quotation that is not in the source: "much more common in individualistic cultures (e.g., United States, Canada, United Kingdom) than collectivistic cultures (e.g., Japan, China, Korea, India, Latin American countries, African countries)". The source names no such list; it says individualistic cultures "tend to be found in western countries such as the United States, Canada, and the United Kingdom" and collectivistic ones "in east Asian countries and in Latin American and African countries" | Rewritten in the source's words, quoted: individualistic-culture people "have the greatest tendency to commit the fundamental attribution error"; collectivistic-culture people "are less likely to commit the fundamental attribution error"; the two country descriptions as the source gives them; "focus on the group more than on the individual" kept. Marker now `[V]` | src 22811–22831 (Ch 12.1) |

## Changes, derived tier

- None. Propagation grep of the light ref and all four distillations for each corrected wording ("tremble", "Japan, China", "much more common in individualistic", "dopamine", "GABA", "norepinephrine", "acetylcholine", "Two identical", "sum of its parts", "educated guesses", "collectivistic", "individualistic"): no copied quotation or marker found. The light ref (23) lists the neurotransmitters by name only, with no per-transmitter function. Decision-making distillation 37, light ref 55 and stakeholder-engagement 169 paraphrase the cultural FAE finding ("more pronounced in individualistic than collectivistic cultures"; "less common in collectivistic cultures"), which the corrected line still supports.
- The distillations' evidence-marker-continuity notes (aar 136, retro 156, decision-making 204, stakeholder-engagement 199) describe the Ch 7.3 bias table and the Ch 12.1 FAE definition (deep 484) as `[V]`; both are unchanged, so the notes stay true.
- No change alters a claim the light ref or a distillation carries. The deep ref's content changed (the Table 3.1 cells at 75 are now correct), so the derived-provenance stamps need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 49** (missing): "a well-developed set of ideas that propose an explanation for observed phenomena". The body text reads "A **theory** is a welldeveloped set of ideas that propose an explanation for observed phenomena" (src 2678): the converter dropped the hyphen in "well-developed". The Key Terms gloss prints "well-developed" (src 3973). The quote is the source's words; the checker was misled by the glued compound.
- **Deep 363** (interrupted): the EEOC harassment quote runs across the running header `**474 13 • Industrial-Organizational Psychology**` (src 26883–26889). The quote is otherwise word for word.

The remaining checker lines (13 apostrophe, 13 initial, 4 ligature) need no fix. The distillation lines among them (aar 18, 20; decision-making 18, 19, 21, 25, 53; retro 18, 20) are capital, apostrophe or `confrms` ligature differences only; the aar/retro line 20 ellipsis correctly marks the dropped "—or attributions—".

## Triage cross-check

- **Deep 75** (no-quote, neurotransmitter table summarised under `[V]`): fixed. The summary also misreported three cells (dopamine, GABA, norepinephrine); each cell is now quoted exactly from Table 3.1 and the `[V]` holds.

## Checker counts

- Before: 13 apostrophe, 13 initial, 4 ligature, 1 interrupted, 1 missing, 1 no-quote (3 failing); 7 figure claims not checked.
- After: 13 apostrophe, 13 initial, 4 ligature, 1 interrupted, 1 missing (2 failing, both conversion noise listed above); 7 figure claims not checked. The new `[V]` quotations at 75, 103, 248, 252 and 285 all match exactly.
- The seven key-statistics figure claims were spot-checked against the source: 6% of bachelor's degrees (src 932), 7 plus or minus 2 / 4 plus or minus 1 (src 14449–14453), 50% and 70% forgetting (src 15253), 50% greater survival (src 29054), 68% and 2.2% IQ (src 13398, 13411), about 1% schizophrenia (src 32037), around forty percent obese and nearly three-quarters overweight (src 18972). All present.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Outside a quotations pass but noticed: several verbatim quotes sit with no marker beside them (deep 29 "use the scientific method to acquire knowledge"; 37 the two I-O quotes; 49 "capable of being shown to be incorrect"; 327 "the mother of modern management"). They match the source; a full Pass I could add `[V]`.
