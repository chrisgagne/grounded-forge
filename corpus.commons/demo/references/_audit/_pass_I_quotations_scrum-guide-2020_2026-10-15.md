# Pass I quotations audit: scrum-guide-2020 (2026-10-15)

**Mode:** quotations. Deep reference read in full (269 of 269 lines). Source: `corpus.commons/demo/sources/converted/scrum-guide-2020.md` (681 lines; read in full). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 16 (10 near, 1 page, 2 interrupted, 3 no-quote).
- Quotation-corrected: 7 lines in the deep ref (70, 74, 92, 93, 94, 109, 171): bulleted source lists quoted inline as one span.
- Unquoted source words under `[V]` given quotation marks: 13 lines in the deep ref (17, 231–237, 241, 243, 244, 245; 237, 241 and 245 were the checker's no-quote lines, the rest the same defect found alongside).
- Marker-corrected: 0 (every `[V]` could carry the source's own words, so each was quoted rather than reclassified).
- Stripped: 0.
- Derived-tier edits: 3 lines (software-business 46, 80; stakeholder-engagement 16).
- Left as is (conversion noise): 3 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 17 | Value names unquoted under `[V]` | Now "people becoming more proficient in living five values": "Commitment, Focus, Openness, Respect, and Courage" [V] | src 215–218 |
| 70 | near: the four-bullet Developers list quoted inline as one span | Lead-in "are always accountable for" and each bullet quoted separately, exact | src 269–279 |
| 74 | near: Product Owner backlog-management list, same | Lead-in and each of the four bullets quoted separately | src 291–300 |
| 92 | near: Scrum Master serving the Scrum Team, same | Each bullet quoted separately | src 325–338 |
| 93 | near: Scrum Master serving the Product Owner, same | Each bullet quoted separately | src 340–352 |
| 94 | near: Scrum Master serving the organization, same | Each bullet quoted separately | src 354–365 |
| 109 | near: during-the-Sprint conditions, same | "During the Sprint" and each bullet quoted separately | src 388–396 |
| 171 | near: artifact commitments, same | Lead-in, each of the three bullets and the closing sentence quoted separately | src 527–537 |
| 231 | `[V]` on unquoted table cell (count of accountabilities) | Cell now quotes "three specific accountabilities within the Scrum Team: the Developers, the Product Owner, and the Scrum Master" | src 259–261 |
| 232 | `[V]` on unquoted table cell (count of events) | Cell now quotes "its five events" | src 196–197 |
| 233 | `[V]` on unquoted table cell (count of artifacts) | Cell now quotes "its three formal artifacts"; citation adds (Scrum Theory, "Transparency"), where the number is stated; the Scrum Artifacts section does not number them | src 180–181 |
| 234 | `[V]` on unquoted table cell (count of values) | Cell now quotes "five values: Commitment, Focus, Openness, Respect, and Courage" | src 215–218 |
| 235 | `[V]` on unquoted table cell (pillars) | Cell now quotes "the empirical Scrum pillars of transparency, inspection, and adaptation". The source never says "three pillars"; it names them | src 172–173 |
| 236 | `[V]` on unquoted table cell (Planning topics) | Cell now quotes the three topic headings, "Why is this Sprint valuable?"; "What can be Done this Sprint?"; "How will the chosen work get done?" | src 426–446 |
| 237 | no-quote (triage): "Product Owner only" under `[V]` | Cell now adds "Only the Product Owner has the authority to cancel the Sprint" | src 413–414 |
| 241 | no-quote: Creative Commons URL in backticks under `[V]` | Now quotes the licence statement, "for license under the Attribution Share-Alike license of Creative Commons", with the URL as the source prints it (`https://creativecommons.org/licenses/by-sa/4.0/`) | src 38–41, 672–674 |
| 243 | Collaborator names in italics, source words unquoted under `[V]` | Whole sentence quoted: "single out those who were instrumental at the start: Jeff Sutherland worked with … and all of them worked together" | src 648–650 |
| 244 | OOPSLA fact in italics under `[V]` | Now Ken Schwaber and Jeff Sutherland "first co-presented Scrum at the OOPSLA Conference in 1995" [V] | src 656 |
| 245 | no-quote (triage): organisations listed in italics under `[V]` | Now quotes "To honor the first places where it was tried and proven, we recognize Individual Inc., Newspage, Fidelity Investments, and IDX (now GE Medical)" | src 665–666 |

## Changes, derived tier

- **Software-business 46** (near): the four organisation-service bullets quoted as one span; now each quoted separately, and the lead-in "is responsible for" now reads "serves the organisation by", following the source's "serves the organization in several ways" (src 354).
- **Software-business 80** (near): lead-in and the first two bullets now quoted separately.
- **Stakeholder-engagement 16** (near): lead-in and all four bullets now quoted separately.
- Propagation grep of the light ref and all five distillations for each corrected wording ("accountable for:", "During the Sprint", "it is the Product Goal", "Coaching the team members", "Helping find techniques", "Leading, training", "Product Owner only", "OOPSLA", "McKenna", "Individual Inc", "creativecommons", "Courage"): no other copied quotation or marker. The light ref carries no evidence markers; its table (lines 55–67) and Key Connections list (73–75) are unmarked paraphrase and stay as they are. Decision-making 38 and 68 already quote the source exactly.
- The distillation notes that describe the deep ref (aar 117, stakeholder-engagement 181: the Creative Commons licence is the only explicit external pointer; no `[BT]` items) stay true.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 111** (page): the page number `7` sits inside "more learning / 7 / cycles" (src 400–403).
- **Deep 163** (interrupted): the converter glued "one-month" into `onemonth` (src 518).
- **Retro 38** (interrupted): the same quotation and the same glued `onemonth` (src 518).

The `initial` (32) and `apostrophe` (8) lines need no fix. Deep 19's inner 'developers' is the source's “developers” in single quotes nested inside a double-quoted span; the checker files it under initial.

## Triage cross-check

Both triage rows were fixed:

- **Deep 237** (no-quote, "Product Owner only" table cell under `[V]`): the cell now carries the source's sentence, "Only the Product Owner has the authority to cancel the Sprint". The same defect on the six count rows above it (231–236) was fixed too.
- **Deep 245** (no-quote, paraphrase under `[V]`): the source's own recognition sentence is now quoted (src 665–666). Lines 243 and 244, the same pattern in the same list, were fixed too.

## Checker counts

- Before: 7 apostrophe, 32 initial, 10 near, 1 page, 2 interrupted, 3 no-quote; 7 figure claims not checked (16 failing).
- After: 8 apostrophe, 32 initial, 1 page, 2 interrupted; 0 figure claims not checked (3 failing, all conversion noise listed above). Apostrophe rose by one because deep 92's "Scrum Team's progress", formerly inside a near span, is now its own quotation and matches at that level.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
