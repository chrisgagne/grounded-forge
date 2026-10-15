# Pass I quotations audit: lfuo-learning-review-guide-2024 (2026-10-15)

**Mode:** quotations. Deep reference read in full (368 of 368 lines). Source: `corpus.commons/demo/sources/converted/lfuo-learning-review-guide-2024.md` (passages read around each hit). Scope open (public domain, 17 USC §105), so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 21 (2 glyph, 5 near, 10 page, 1 interrupted, 2 missing, 1 no-quote).
- Quotation-corrected: 6 in the deep ref (1 glyph, 1 word inserted, 4 closing punctuation), 1 in a distillation (glyph).
- Marker-corrected: 1 in the deep ref (HRO hallmarks paraphrase under `[V]`).
- Label corrected: 1 in the deep ref (invented "not adjudication" heading), with its copies in the light ref and one distillation.
- Stripped: 0.
- Left as is (conversion noise): 13 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 161 | Facilitator-move label "Encourage sensemaking, not adjudication" is not in the source; "adjudication" appears nowhere in it. The source contrasts the group dialogue with a group interview, not with adjudication. The label was copied into a distillation as a quotation | Label now "Encourage sensemaking."; the bullet adds the source's contrast: Facilitation "closely resembles a group interview. The goal of the interviews is to obtain information from participants" [V]; the existing "The goal of the group dialogue session…" quote keeps its `[V]` | src 2174–2181 |
| 170 | glyph: em dash in "involved in the accident — which they had" | Spaced hyphen, as the converted source prints it | src 2302–2307 |
| 211 | missing (triage): "FLA team members must not discuss anything…" | Now "team members must not discuss anything they learned during the FLA process with anyone" [V]; the source has no "FLA" before "team members" here. The 4-word match the checker found was the Part 5 "Trust" sentence (src 1594–1598), a different passage | src 2948–2949 |
| 211 | near: 'accident' closed before the source's period | Now "…an 'accident.'" (source: an “accident.”) | src 2918–2919 |
| 250 | near: same pattern | Now "…'work as performed.'" | src 3487–3488 |
| 261 | no-quote (triage): "The HRO questions cluster around the five HRO hallmarks: …" was a paraphrase under `[V]` (it also dropped the source's "and" before "deference") | Split into two quotes: Handout D, "The five hallmarks of High Reliability Organizations (HRO) can also be used to help structure or frame a facilitated dialogue" [V]; Glossary, "preoccupation with failure, reluctance to oversimplify, sensitivity to operations, commitment to resilience and deference to expertise" [V] [BT] (Weick and Sutcliffe attribution kept) | src 4585–4588; 4880–4883 |
| 285 | near: 'objective risk' closed before the period | Now "…'objective risk.'" | src 4391–4397 |
| 344 | near: Chamberlin quote closed before the period | Now "…experiences of participants.'" | src 2784–2786 |

## Changes, derived tier

- `distillations/decision-making/lfuo-learning-review-guide-2024-decision-making.md:12` (glyph): same em dash as deep 170; now the source's spaced hyphen (src 2305).
- `distillations/stakeholder-engagement/lfuo-learning-review-guide-2024-stakeholder-engagement.md:46` (missing, triage): "Encourage sensemaking, not adjudication" was quoted as a named facilitator move. Now: the group dialogue is not a group interview: its goal "is to encourage sensemaking through dialogue to achieve a better understanding of the multiple perspectives of the participants" [V] (src 2178–2181).
- `references/lfuo-learning-review-guide-2024.md:60`: unmarked paraphrase "encourage sensemaking, not adjudication" now "encourage sensemaking through dialogue (the group dialogue is not a group interview)". This changes a claim the light ref carries.
- Propagation grep of the light ref and all five distillations for "adjudicat", "must not discuss", "considered an", "work as performed", "objective risk", "capitalizing on the shared", "involved in the accident —", "hallmark", "preoccupation with failure", "Chamberl". Other "adjudicat" hits (decision-making 65; software-business 204; stakeholder-engagement 109, 192, 196, 208) apply the word to points of departure and conflicting accounts, which the source supports ("The idea is not to validate one story over the other", src 2169–2173); they are unmarked and stay. Light 102 and 127 already close their quotes after the period. Light 96 and decision-making 54 carry the five hallmarks as unmarked paraphrase, which Handout D and the Glossary support. No other copy of a corrected quotation or marker.
- The stakeholder-engagement evidence-continuity note (249) stays true: its Key Concept quotations remain `[V]` deep-ref passages.
- The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and the five distillations need re-stamping by the parent.

## Left as is (conversion noise)

Page numbers inside the quoted span (`page`):

- **Deep 19** and **stakeholder-engagement 62**: "most 51 effective" (page number 51, src 2483).
- **Deep 33**: "after an 10 incident" (page 10, src 551).
- **Deep 43**: "talk to the 72 accident investigation team" (page 72, src 3714).
- **Deep 53** and **software-business 180**: "without 14 recommendations" (page 14, src 737).
- **Deep 83**: "outcome 24 and/or" (page 24, src 1222).
- **Deep 162**: "quiet participants 42 and work them" (page 42, src 2228).
- **Deep 211**: "human safety 58 or committed" (page 58, src 2912).

Footnote markers inside the quoted span:

- **Deep 236** (page): "ergonomic [7], and structural" carries footnote marker 7 (the footnote defines ergonomics, src 3252); the quote omits the marker (src 3212–3215).
- **Deep 277** (near): "variability11 (both human" carries footnote marker 11 glued to the word (footnote 11 is the Hollnagel citation, src 3818); the quote omits it (src 3813–3815).

Interrupted:

- **Deep 324**: the Glossary "Storytelling" entry runs across footnotes 14–15 and page number 98 between "An FLA's story is a" and "factual description" (src 5002–5018). The words are contiguous on the page.

## Triage cross-check

- **Deep 211** (missing, "FLA" inserted): confirmed. The source reads "team members must not discuss anything they learned during the FLA process with anyone" (src 2948–2949). "FLA" removed.
- **Deep 261** (no-quote, paraphrase under `[V]`): confirmed. Replaced with two quotes of the source's words, Handout D and Glossary. See table.
- **Stakeholder-engagement 46** (missing, "Encourage sensemaking, not adjudication"): confirmed absent; "adjudication" does not occur in the source. The phrase originated as a deep-ref label (deep 161) and was also carried, unquoted, by the light ref (60). All three fixed; no other distillation carries it.

Every triage row was addressed.

## Checker counts

- Before: 51 apostrophe, 29 initial, 2 glyph, 5 near, 10 page, 1 interrupted, 2 missing, 1 no-quote (21 failing).
- After: 53 apostrophe, 29 initial, 1 near, 10 page, 1 interrupted (12 failing, all conversion noise listed above). Apostrophe rose by two: deep 170 (former glyph) and deep 285 (former near) now match at the apostrophe level. Deep 211, 250 and 344 (former near) and the new deep 161, deep 261 and stakeholder-engagement 46 quotes match exactly.

## Open

- Stamp left as is (quotations mode). No commit made; no build run.
- Not in quotations scope, noted for a full Pass I: deep 261 says Handout D's questions are "drawn from Weick and Sutcliffe's High Reliability Organisations work" [BT]; Handout D itself does not name them (the Glossary does). Retro 135 renders the Appendix B quote without its inner quote marks around "find" and "discover"; it sits in a continuity note, not under a marker, and the checker passes it.
- Derived-provenance stamps for the light ref and five distillations are stale against the edited deep ref; the parent re-stamps.
