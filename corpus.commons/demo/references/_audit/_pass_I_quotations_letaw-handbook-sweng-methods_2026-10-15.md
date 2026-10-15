# Pass I (quotations mode): letaw-handbook-sweng-methods, 2026-10-15

**Mode:** quotations. Only `check-verbatim.py` findings, plus quotations found wrong while fixing them. The `Pass I applied` stamp is unchanged.
**Files:** `references/letaw-handbook-sweng-methods-deep.md` (392/392 lines read), the five distillations `distillations/*/letaw-handbook-sweng-methods-*.md`, the light ref `references/letaw-handbook-sweng-methods.md` (grepped for propagation).
**Source:** `sources/converted/letaw-handbook-sweng-methods.md`. Every fix below is checked against this file; line numbers are source lines.

## Counts

| | |
|---|---|
| Actionable findings in the work list | 23 (deep: 18 no-quote, 2 near, 2 missing; retro: 2 no-quote) |
| Triage rows | 17, all handled below |
| Quotation-corrected | 3 (deep 43, 75, 148) |
| Marker-corrected (`[V]` → `[AP]`, or `[V]` split into a quoted `[V]` sentence plus an `[AP]` paraphrase sentence) | 18 (deep 15, 29, 39, 51, 71, 75, 85, 138, 142, 193, 218, 219, 226, 248, 277; retro 20 twice, 34) |
| Stripped | 0 |
| Left as is | 2 (deep 19, 197) |

## Check-verbatim before and after

- Before (from the dispatch work list): 54 apostrophe, 26 initial, 2 near, 2 missing, 18 no-quote.
- After: 57 apostrophe, 27 initial, 2 missing, 0 near, 0 no-quote. The apostrophe/initial counts rose only because the split sentences now give the checker more quoted spans to compare; those classes need no fix.

## Deep reference changes

- **15** `[AP] [V]` → `[V]`. The marker after the Introduction cite had an empty segment. The sentence's quoted questions ("Is this algorithm correct?", "How does my team know…", "People keep misinterpreting…") are in the source at 330–335; "the field keeps changing" paraphrases 331–332.
- **29** Split. The Waterfall/"swim up a waterfall" sentence keeps `[V] [BT]` (source 584–587). The Royce-modifications sentence becomes `[AP] [BT]`, reworded to "goes back to the requirements stage as needed" to follow source 587–589.
- **39** Split. "a well-known framework for software project management" is `[V]` (676). The three-categories sentence becomes `[AP] [BT]` (685–686).
- **43** Quotation corrected. The deep had "fixed-length development periods of one month or less. . . A new Sprint…". Source 715–717 reads `fixed-length development periods of “one month or less . . . A new Sprint starts immediately after the conclusion of the previous Sprint.”` The source's own inner quotation mark opens at "one month", so the quote is now two exact spans: "fixed-length development periods" of "one month or less . . . A new Sprint starts…".
- **51** Split. The "'Agile' has associated values…" quote stays `[V]` (788–789). The Scrum-Guide-changes-frequently paraphrase becomes `[AP]` (789–792).
- **71** Split. "need buy-in from the whole team" stays `[V]`. The eight-questions summary becomes `[AP]`; the source has eight questions, 1032–1060.
- **75** (two findings) Split. The "a method for checking and building consensus…" definition stays `[V]` (1188). The one-person/fist-or-five-fingers sentence becomes `[AP]` (1188–1190). The encoding was the source's words without quotation marks (triage: "source words, unquoted"), so each level's text is now quoted exactly as source 1200–1210 has it, e.g. "Strong reject. Blocks consensus". I left out each item's final period so the checker's sentence scope reaches the `[V]`.
- **85** Trailing `[V] [AP]` → `[AP]`. The inline `[V]` on "the server setup task still has many unknowns" stays. The remaining list paraphrases 1394–1412.
- **138** Optional use-case parts: `[V]` → `[AP]`. The list paraphrases 2184–2201.
- **142** SRS definition sentence: `[V]` → `[AP]` (2207–2209). "The best way to learn about SRSs is to look at some" keeps its `[V]`.
- **148** Quotation corrected. The deep had "evaluate whether your plans are any good (e.g., … quality attributes)". Source 2356–2357 reads "decide (evaluate) whether your plans are any good (e.g., are clear, are logical, reflect your project’s desired quality attributes, and so on)", and the quote now gives those words.
- **193** Second sentence (two architectures, not every option): `[V]` → `[AP]` (2786–2788).
- **218** Split. Monolith "all at once" stays `[V]` (2966). The microservices paraphrase becomes `[AP]`, and I restored the source's "potentially" (2966–2967).
- **219** Split. "must have enough space, memory…" stays `[V]` (2973–2974). The microservices paraphrase becomes `[AP]`, reworded to "replicating the more-used services more times" (2980–2981). The deep's "only" was not in the source.
- **226** Split. The WinGui Gateway / Message Broker sentence keeps `[V] [AE]` (3068–3073). The JSON/Profile Service sentence becomes `[AP] [AE]`, with "relational store" reworded to the source's "relational database used within the monolith" (3077–3079).
- **248** Heuristic-expansion sentence: `[V] [BT]` → `[AP] [BT]`. "are anticipated" becomes "may expand in future", because the source says "will potentially expand" (3285–3287).
- **277** "The chapter summary lists all eight heuristics": `[V]` → `[AP]` (3529–3550).

## Distillation changes

- **retro 20** The eleven-code-smell list (smell names only, no quoted span): `[V]` → `[AP]`. On the same line, `"code is hard to maintain" [V]` lost its marker. The phrase occurs in source 3649, but the distillation uses it as a hypothetical retro theme next to an unmarked one, so the `[V]` implied a Letaw claim the line doesn't carry. The quotation marks stay.
- **retro 34** The Eisenhower quadrant summary: `[V]` → `[AP]` (Ch 2.5.3).

## Propagation (derived tier)

I grepped the light ref and all five distillations for the two corrected wordings ("one month or less. . .", "evaluate whether your plans") and for each re-marked claim. None of the wrong wordings appear anywhere. The light ref has no `[V]` markers, and its key-statistics row "Sprint length cap | one month or less" is unquoted and correct. **No derived-tier edits beyond the retro fixes above.** None of the deep edits changes a claim's substance. Two narrow wording corrections (218 adds "potentially"; 219 drops "only"; 248 softens "anticipated") might sit in a distillation paraphrase, but greps for "all at once", "replicat", "relational" and "Future expansion" found no derived-tier carrier.

## Left as is

- **Deep 19** `missing` (14 of 24 words). The quote is exact. The source splits "implica­** **tions" with a soft hyphen across bold markers (Ch 2, opening), which is conversion noise.
- **Deep 197** `missing` (13 of 15 words). The quote is exact. The source splits "indi­** **vidually" the same way (Ch 5.2), also conversion noise.
- `apostrophe` and `initial` lines need no fix under the protocol.

## Open

- The retro distillation's `derived-from-deep` stamp now points at a pre-edit deep hash, and the deep has changed too. The parent should re-stamp the derived tier (`check_derived_provenance.py --stamp --slug letaw-handbook-sweng-methods`) after review.
