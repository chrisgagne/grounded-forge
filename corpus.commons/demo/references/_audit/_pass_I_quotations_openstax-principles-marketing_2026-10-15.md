# Pass I quotations audit: openstax-principles-marketing (2026-10-15)

**Mode:** quotations. Deep reference read in full (580 of 580 lines). Source: `corpus.commons/demo/sources/converted/openstax-principles-marketing.md` (41,595 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the three distillations (decision-making, software-business, stakeholder-engagement), plus the human triage of that run. Every quoted span in the deep ref, the light ref and the distillations was also matched against the source (whitespace and quote-glyph normalised), which surfaced five misquotations the checker does not see because they sit under `[BT]`, `[AP]` or no marker.

## Counts

- Actionable checker lines worked: 6 (1 missing, 5 no-quote).
- Further quotations found wrong outside the checker's scope: 5 in the deep ref, 4 in the derived tier.
- Quotation-corrected: 9 lines in the deep ref (19, 190, 200, 236, 315, 351, 542, 561, 562).
- Marker-corrected: 3 lines in the deep ref (19: paraphrase split off under its own `[AP]`; 160: paraphrased dimensions replaced by quotations under `[V]`, the masculinity clause now `[AP]`; 477: paraphrased CBD claim replaced by quotations).
- Stripped: 0 claims. One phrase removed in a rewritten line (160, "and later additions", which Ch 5.3 does not say).
- Derived-tier edits: 4 (light ref 87, 120; decision-making 173; software-business 25).
- Left as is (conversion noise): none.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 19 | missing: "is bombarded with marketing messages throughout the day"; the source's subject is plural ("consumers are bombarded"). The `[V]` also covered the 5,000-ads figure and "a single channel rarely cuts through", both paraphrase | Quote now "consumers are bombarded with marketing messages throughout the day" [V], cited to Ch 13.1 "The Importance of the Promotion Mix", where it sits. The 5,000-ads figure keeps its own Ch 13.1 "What Is the Promotion Mix?" citation; the single-channel clause is marked `[AP]` (source: "one communication method alone is not likely to cut through the clutter and noise") | src 25521–25522, 25612–25618 (Ch 13.1) |
| 160 | no-quote: the four Hofstede dimensions paraphrased under one `[V]` | Quoted in the source's words: "identified five dimensions that could be used to distinguish one culture from another"; "Four of these dimensions directly affect marketing in different cultures"; the PDI ("moderately low PDI score of 40 on a scale of 1 to 100, compared to a world average of 55"), individualism (91; Ecuador and Guatemala single digits) and UAI (46; Italy 75, Poland 93) sentences, each `[V]`. Masculinity/femininity (Japan high; the United States and Canada low) stays paraphrase, now `[AP]`. Dropped "and later additions": Ch 5.3 names five original dimensions and nothing later (the six-dimension version is Ch 8.3, already noted at line 578) | src 10308–10311, 10316–10340 (Ch 5.3) |
| 190 | no-quote: TCPA hours paraphrased ("8 a.m. … 9 p.m. recipient time") | Now "approved by Congress in 1991, no calls can be made prior to 8:00 a.m. or after 9:00 p.m. in the recipient’s time zone" [V] | src 12574–12575 (Ch 6.3) |
| 200 | no-quote (triage): direct-to-consumer drug ads paraphrased under `[V]`; "the only two countries" is not the source's wording | Now "the United States and New Zealand are the only countries where this type of marketing is allowed" [V], introduced as advertising prescription medications to the general public | src 13700–13704 (Ch 7.1) |
| 236 | no-quote: sociodemographic figures; "≈ 34 million below the poverty line" where the source says "over 34 million individuals" "living in poverty" | Poverty clause now "over 34 million people living in poverty in 2019"; disabilities clause quoted: "This group represents an estimated 61 million Americans. About one in four adults lives with some type of disability" [V]. The other figures (5.6 per cent, 14.4 million; the 2020 Census generation counts) checked against the source and unchanged | src 16046–16085 (Ch 8.2) |
| 315 | Maxwell House quote dropped "and" (unmarked quote, not checked by the checker) | Now "bold, vigorous, and deep tasting" | src 20557 (Ch 10.2) |
| 351 | GoToMeeting quote "$49 all-you-can-meet" is not the source's wording | Now $49 "all you can meet flat-rate pricing" | src 24200 (Ch 12.3, Table 12.1) |
| 477 | no-quote (triage): CBD claim paraphrased under `[V]` ("Manhattan world's largest CBD, highest retail rent globally"); the markup figures had no citation | Now "Manhattan is the world’s largest central business district"; "It has the highest retail rent in the world" [V] (Ch 18.3, "Central Business District"). The markup figures (grocery ~15 per cent, clothing 100–300 per cent; keystone doubles wholesale) checked and now cited (Ch 18.3, "Retail Pricing") | src 36160–36163, 36250–36257 (Ch 18.3) |
| 536 | Key-statistics row for the TCPA, aligned with the corrected line 190 (unquoted figure cell; checker counts it as a figure claim) | "no calls before 8:00 a.m. or after 9:00 p.m. in the recipient's time zone" | src 12575 (Ch 6.3) |
| 542 | Levitt quote in Connections (`[BT]`) reworded: "people don't want a quarter-inch drill, they want a quarter-inch hole" | Now "People don’t want to buy a quarter-inch drill; they want a quarter-inch hole", as line 156 already has it | src 10059–10060 (Ch 5.2) |
| 561 | "build it and they will come" is not the source's wording, and the line sits in Ch 1.4, not Ch 1.1 | Now the production concept's "If you build it, they will come", cited Ch 1.4; the framing against product-driven strategy keeps its Ch 1.1 citation | src 1992–1993 (Ch 1.4) |
| 562 | "shortsighted perspective that limits business growth" is not the source's wording | Now generalising buyers anywhere in the world "is a shortsighted perspective, because it limits business growth and commercial possibilities" | src 15772–15773 (Ch 8.2) |

## Changes, derived tier

- **Light ref 87:** "planet, people, profits" dropped the source's "and"; now "planet, people, and profits" (src 37669, Ch 19.1).
- **Light ref 120:** "Build it and they will come" → "If you build it, they will come" (src 1992–1993).
- **Decision-making distillation 173:** same misquotation, same fix.
- **Software-business distillation 25:** GoToMeeting's "$49 all-you-can-meet" → $49 "all you can meet flat-rate pricing" (src 24200). Line 44's unquoted "all-you-can-meet model" is paraphrase and stays.
- Propagation grep of the light ref and all three distillations for every other corrected wording ("bombarded", "New Zealand", "Manhattan", "CBD", "PDI", "individualism", "Telephone Consumer", "8 a.m.", "poverty", "61 million", "vigorous", "quarter-inch", "shortsighted", "one size", "later additions", "retail rent", "only two countries"): no other copied quotation or marker found. Light ref 95 (Hofstede individualism 91, PDI 40), light ref 108 ("quarter-inch hole"), light ref 125 ("shortsighted") and decision-making 24 (the full Levitt quote) match the source.
- Quoted phrases in the distillations that are task-side scare quotes or anti-pattern labels (decision-making 131, 180; software-business 105, 121, 141, 145–161; stakeholder-engagement 174) are not attributed to the source and were left as they are.
- No distillation note describes the deep ref's markers on the changed lines.

## Left as is (conversion noise)

- None. No `interrupted`, `page` or `glyph` lines in either run. The `apostrophe` (6) and `initial` (2) lines need no fix.

## Triage cross-check

- **Deep 19** (missing, are→is): real defect. Fixed: the quote now takes the source's own subject, "consumers are bombarded …", and the paraphrase the `[V]` had covered is split off under `[AP]`.
- **Deep 200** (no-quote, paraphrase under `[V]`): real defect. Fixed: the source sentence quoted word for word; "only two countries" (not in the source) is gone.
- **Deep 477** (no-quote, paraphrase under `[V]`): real defect. Fixed: both CBD claims quoted from the source, with a section citation the line had lacked.

## Checker counts

- Before: 6 apostrophe, 2 initial, 1 missing, 5 no-quote (6 failing); 72 figure claims not checked.
- After: 6 apostrophe, 2 initial (0 failing); 72 figure claims not checked.

## Open

- Stamp left as is (quotations mode). The deep ref carries no `Pass I applied` stamp; the light ref's `derived-from-deep` hash is now stale and needs re-stamping by the parent. No commit made, no build run.
- Figure claims under `[V]` (72, e.g. lines 58, 112, 118, 130, 140 and the key-statistics table) are the protocol's convention and were not traced one by one; those checked while working (lines 160, 236, 477) match the source.
- Outside a quotations pass but noticed: several section names in citations do not appear verbatim anywhere in the converted source (e.g. 29 "How Marketing Benefits the Organization, Its Interested Parties, and Society", 94 "Consumer Markets Defined", 140 "Bribes and Grease Payments", 212 "Ways an Organization Can Enter", 443 "Marketing Channels Defined"); a full Pass I should check citation anchors. Light ref 35 lists Hofstede's six dimensions under international segmentation, where Ch 5.3 gives four (the six are Ch 8.3).
