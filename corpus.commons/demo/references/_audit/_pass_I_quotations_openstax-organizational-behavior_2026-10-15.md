# Pass I quotations audit: openstax-organizational-behavior (2026-10-15)

**Mode:** quotations. Deep reference read in full (750 of 750 lines). Source: `corpus.commons/demo/sources/converted/openstax-organizational-behavior.md` (32,852 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of an earlier run.

## Counts

- Actionable checker lines worked: 8 (2 interrupted, 1 missing, 5 no-quote).
- Quotation-corrected (paraphrase under `[V]` replaced with the source's words, marker kept `[V]`): 3 in the deep ref (lines 25, 137, 183).
- Marker-corrected: 3 in the deep ref (`[V]` → `[AP]` on line 470; `[AP]` added to the paraphrased halves of lines 25 and 183).
- Restructured so the marker closes the quoting sentence: 1 (line 364), with a citation correction.
- Derived tier: 0 changes.
- Stripped: 0.
- Left as is (conversion noise): 3 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 25 | no-quote: four functions of work and alienation paraphrased under `[V]` | The four-functions sentence now carries `[AP]`. Alienation is quoted exactly: "individuals often experience sensations of powerlessness, meaninglessness, and normlessness—a condition called alienation" [V] | src 833–871 (Ch 1.1, "Functions of Work"); quote at 868–870 |
| 137 | no-quote: three kinds of diversity paraphrased under `[V]` | Each definition quoted exactly ("represents an individual’s visible characteristics, including, but not limited to, age, body size, visible disabilities, race, or sex"; "includes traits that are nonobservable such as attitudes, values, and beliefs"; "includes traits that are deep-level but may be concealed or revealed at the discretion of individuals who possess them"); `[V]` kept | src 6104–6111 (Ch 5.1) |
| 183 | no-quote: programmed and non-programmed decisions paraphrased under `[V]` | Programmed definition quoted ("are those that are repeated over time and for which an existing set of rules can be developed to guide the process" [V]); heuristics clause marked `[AP]`; nonprogrammed definition quoted ("are novel, unstructured decisions that are generally based on criteria that are not well-defined"); the reflective-system claim now quotes the source ("will generally need to be processed via the reflective system in our brains in order for us to reach a good decision" [V]). The old example "scheduling" now reads "setting a weekly work schedule", as the source's example is | src 8193–8194, 8196–8203, 8228–8233, 8269–8271 (Ch 6.3) |
| 364 | no-quote: the Hopper quote sat mid-sentence ("— … — is reproduced [V]"), so the `[V]` closed a sentence with no quote. The quote itself was exact | Rewritten so `[V]` closes the quoting sentence: The text reproduces Grace Hopper's distinction: "You don’t manage people, you manage things. You lead people." [V]. Citation corrected from "Paths to Leadership" to "Leader Emergence": the quote sits under the 12.3 heading (src 17823), before the "Paths to Leadership" subhead (src 17871) | src 17856–17857 |
| 470 | no-quote: distributive/integrative bargaining paraphrased under `[V]` | `[V]` → `[AP]`; citation adds Table 14.2. The paraphrase checks: "win-lose", "Resources are fixed and limited", "short-term relationship"; "win-win", "variable resources to be divided, efforts to maximize joint outcomes", "long-term relationship" | src 21579–21593, 21606–21611, 21629–21649 |

The second `[V]` on line 470 (skilled vs average negotiator figures) is a figure claim the checker does not test. Checked by hand against Table 14.4: 5.1/2.6 options, 39%/11% on areas of agreement, 21%/10% asking questions, 1%/6% attacking opponent (src 21756–21757, 21784, 21786). All match.

## Changes, derived tier

None. Propagation grep of the light ref and all five distillations for each corrected passage (powerlessness, alienation, surface-level, deep-level, hidden diversity, invisible social, programmed / non-programmed, distributive, integrative, Grace Hopper, manage things, described their opponents):

- No derived artefact carries any of these passages under `[V]`. The light ref (lines 29, 33, 65) and the decision-making distillation (line 18) restate the diversity, decision-type and bargaining paraphrases as unmarked paraphrase with chapter attribution, which is correct as written.
- The distillations' `initial` findings (aar 12; decision-making 16, 28; software-business 32, 103, 234) are capitalisation at sentence start and need no fix.
- No change alters a claim the light ref or a distillation carries; the line 183 example change ("weekly work schedule" for "scheduling") is a wording refinement, not a claim change. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 59** (interrupted): the Rokeach value definition runs across the running header `**44   2 • Individual and Cultural Differences**` (src 2460–2465). The words are contiguous on the page.
- **Deep 93** (interrupted): the organisational-commitment definition runs across `**Access for free at openstax.org**` and `**3.5 • Work-Related Attitudes   75**` (src 4106–4115). The words are contiguous on the page.
- **Deep 458** (missing): the executive-study quote starts "typically described" on src 21250, then the running header `**402   14 • Conflict and Negotiations**` (src 21253), then "themselves as using collaboration … almost exclusively" (src 21256–21257). The quote matches the page exactly. The checker reports `missing` rather than `interrupted` because the first run before the header is two words, under its three-word minimum for an anchoring run.

## Triage cross-check

Every triage row was fixed:

- **Deep 25** (four functions / alienation): the paraphrase half is now `[AP]`; the alienation sentence is quoted word for word under `[V]`.
- **Deep 137** (three kinds of diversity): replaced with the source's three definitions, quoted exactly; `[V]` kept.
- **Deep 183** (non-programmed decisions): replaced with the source's definitions and its reflective-system sentence, quoted exactly; the heuristics clause, which is paraphrase, is `[AP]`.
- **Deep 470** (bargaining strategies): `[V]` → `[AP]`. The paraphrase is faithful to the text and Table 14.2.

The fifth no-quote line (deep 364) was a placement defect, not a wording one: the quote was exact but the marker closed the wrong sentence. Fixed by restructuring, as above.

## Checker counts

- Before: 6 apostrophe, 10 initial, 2 interrupted, 1 missing, 5 no-quote (8 failing).
- After: 6 apostrophe, 10 initial, 2 interrupted, 1 missing (3 failing, all conversion noise listed above).

## Open

- Stamp left as is (quotations mode). No commit made; no build run.
- `docs/architecture/matrix-pattern.md` reproduces none of the corrected quotes (its only match, a Thomas-mode row mentioning "integrative", is unquoted paraphrase). No doc change needed.
- Outside this pass's scope, noted for a full Pass I: line 458 closes with the gloss "a self-serving asymmetry [V]"; the source's own words are "the executives had flattering portraits of their own willingness to satisfy both sides" (src 21258–21259). The gloss is the ref's, under a `[V]` that the quote earns. Line 404 says Ch 12.7–12.8 were "present but not fully covered in the read", which is a reader-side partial-coverage admission without an operator-approved `coverage:` declaration.
