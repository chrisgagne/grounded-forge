# Pass I quotations audit: openstax-principles-management (2026-10-15)

**Mode:** quotations. Deep reference read in full (1025 of 1025 lines). Source: `corpus.commons/demo/sources/converted/openstax-principles-management.md` (31,465 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of an earlier run.

## Counts

- Actionable checker lines worked: 25 (1 glyph, 7 near, 1 page, 2 interrupted, 5 missing, 9 no-quote).
- Quotation-corrected: 11 in the deep ref, 1 in a distillation (propagation).
- Marker-corrected: 5 in the deep ref, 1 in a distillation.
- Quotation marks added (marker kept `[V]`): 2.
- Stripped: 0.
- Left as is (conversion noise): 5 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 97 | missing: `"front-page-of-a-newspaper"` is not the source's wording | Rewrote: think about how you would feel "if that decision ended up on the front page of a major newspaper. If you would feel guilty or ashamed, don't do it!" [V] | src 2198–2201 (Ch 2.5) |
| 206 | near: source reads `set the “tone at the top,”` (comma inside the inner quote) | Quote now ends `'tone at the top,'"` | src 5099–5100 |
| 253 | glyph: `20-30%` | `20–30%` (en dash, as source) | src 6473–6474 |
| 261 | missing: source opens `“[m]ore than nine-in-10…` | Moved "more than" outside the quote; quote starts at "nine-in-10 Millennials" | src 6591–6592 |
| 311 | no-quote: religion percentages written as "per cent" under `[V]` | `[V]` → `[AP]` (figures check against source: 31%, 24.1%, 15.1%, 6.9%, 0.2%) | src 8389–8392 |
| 528 | near: SHRM bullet list quoted inline with semicolons | Each of the four bullets quoted separately, exact | src 16078–16084 |
| 530 | no-quote: WorldatWork six elements, list paraphrased | `[V]` → `[BT]` (the text cites World at Work) | src 16142–16175 |
| 553 | no-quote: three kinds of diversity, paraphrase | `[V]` → `[AP]` | src 17104–17113 |
| 561 | no-quote: model minority myth, paraphrase | `[V]` → `[AP]` | src 17399–17404, 18492–18494 |
| 654 | near: source reads `what “can be.”` | Quote now ends `'can be.'"` | src 20277 |
| 668 | missing: quote began "but, on the other hand"; source has "On the other hand" opening a new sentence | Rewrote: research results do not support Maslow's hierarchical notion; "On the other hand, there is some evidence that people satisfy the lower-order needs before they attempt to satisfy higher-order needs" [V] | src 21541–21551 |
| 686 | missing: "the components of expectancy theory predict…" reworded | Now "the individual components predict performance just as well, without being multiplied" [V], with "Recent research demonstrates that" outside the quote | src 22721–22723 (Ch 14.4) |
| 766 | no-quote: CQ head/body/heart, paraphrase | `[V]` → `[BT]`, credited to the authors of the HBR article "Cultural Intelligence", as the source does | src 24038–24055 |
| 825 | no-quote: goal planning, paraphrase under `[V]` | Quoted the source exactly: "people set specific goals and then create action statements" [V] (the old wording dropped "then") | src 25879–25880 |
| 857 | missing: "do their best" | Now (as opposed to simply "doing their best"). The triage row says the source reads "do your best"; that phrase is the text's general goal-specificity example (src 26512–26513). The Weyerhaeuser passage itself reads "doing their best" (src 26515–26516), which is what this line quotes | src 26512–26519 |
| 871 | near: the source sets “newness” in its own quote marks | Quote now opens `"'newness' in the development…` | src 27968–27970 |
| 899 | near: ellipsis joined "the success" in lower case; source has a sentence break and "The success" | Now "the mirror image of leadership. … The success of organizations…" | src 28530–28534 |
| 901 | no-quote: three questions given unquoted under `[V]` | Each question quoted exactly; `[V]` kept | src 28584–28586 |

## Changes, derived tier

- `distillations/software-business/openstax-principles-management-software-business.md:32`: the same 'tone at the top' quote as deep 206 (propagation); now ends `'tone at the top,'"`.
- `distillations/stakeholder-engagement/openstax-principles-management-stakeholder-engagement.md:158`: the worked-example provenance sentence listed marker classes as bare `[BT]`/`[V]` tokens over a framework list (two no-quote findings). The classes are now written out in words. The only `[V]` left sits on the one real quotation ("If you would feel guilty or ashamed, don't do it!", Ch 2.5). Head-body-heart is now described as borrowed through the HBR article, matching the deep ref's new `[BT]`.
- Propagation grep of the light ref and all five distillations for each corrected wording ("front-page", "do their best", "20-30", "nine-in-10", "Recognize and reward", "without being multiplied", "success of organizations", "newness", "tone at the top", "can be", "on the other hand", "goal planning", "head, body", "Where are we now", WorldatWork, model minority, hidden diversity): no other wrong quotation found. The newspaper-test rows in decision-making (86), stakeholder (69) and software-business (114) are unquoted paraphrase, and they already say "front page of a major newspaper". The light ref's mentions are all paraphrase.
- No change alters a claim the light ref carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 31** (interrupted): the Eccles–Nohria quote runs across the running header `**Access for free at openstax.org** **1.2 • The Roles Managers Play 9**` (src 745–751). The words are contiguous on the page.
- **Deep 59** (page): the footnote marker `[1]` sits between "future." and "Bad publicity" (src 1473). It is a reference mark, not the author's words.
- **Deep 340** (near): the checker matched the Key Terms gloss (src 11153, no comma, capital P). The deep ref cites Ch 7.1 body text, which reads "people with vision, / drive, and creativity, who are willing…" (src 9912–9918) across the running header `**188 7 • Entrepreneurship**`. The quote matches the body text exactly.
- **Deep 668a** (interrupted): the converted text reads "selffulfillment" (src 21486), where the converter dropped a line-end hyphen. The quote keeps "self-fulfillment" rather than copying the garble.
- **Deep 668b** (interrupted): the corrected "On the other hand…" quote runs across the running header `**Access for free at openstax.org** **14.2 • Content Theories of Motivation 413**` (src 21541–21551).

## Triage cross-check

Every triage row was fixed: 97, 530, 553, 561, 686, 766, 825, 857, 901. On 857, the triage's reading ("source says do your best") is half right, as the table above explains: the line is now corrected to the Weyerhaeuser passage's own words, "doing their best".

## Checker counts

- Before: 30 apostrophe, 1 glyph, 5 initial, 7 near, 1 page, 2 interrupted, 5 missing, 9 no-quote (25 failing).
- After: 33 apostrophe, 7 initial, 1 near, 1 page, 3 interrupted (5 failing, all conversion noise listed above). Apostrophe and initial counts rose because the corrected quotes now match at those non-failing levels.

## Open

- Stamp left as is (quotations mode). No commit made.
- Deep ref line 932 (Key statistics) carries a row marked `[not in this source]` for Adler–Gunderson negotiator figures. This is outside the scope of a quotations pass. A full Pass I should strip it.

## Follow-up, 2026-10-15: the open item

- **Key statistics, Adler–Gunderson row stripped.** The row ("Skilled vs avg negotiators options per issue … n/a … [not in this source]") had no value and no source passage: `sources/converted/openstax-principles-management.md` names neither Adler nor Gunderson (its only negotiator passages, l.885 and l.24824, describe the manager's decisional role). The light reference and the distillations never carried the row. Provenance re-stamped.
