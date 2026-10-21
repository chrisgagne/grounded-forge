# Pass I quotations audit: openstax-business-ethics (2026-10-15)

**Mode:** quotations. Deep reference read in full (669 of 669 lines). Source: `corpus.commons/demo/sources/converted/openstax-business-ethics.md` (20,239 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run, plus a scan of the deep ref for `[V]` segments with no quotation marks (the checker counts those with a figure in them as "figure claims" and does not check them).

## Counts

- Actionable checker lines worked: 14 (5 near, 3 interrupted, 2 missing, 4 no-quote; the stakeholder-engagement 158 no-quote is reported twice).
- Quotation-corrected, deep ref: 7 lines (136, 312, 320, 340, 406, 412, 528).
- `[V]` on paraphrase, fixed by quoting the source's words with `[V]` kept: 9 lines (19, 138, 232, 234, 276, 280, 328, 330; 234 twice). Line 19 also gains an `[AP]` for its unquoted remainder.
- Marker-corrected, deep ref: 51 Key-statistics rows (552–606): 30 `[V]` → `[AP]`, 21 `[V] [BT]` → `[BT]`.
- Derived-tier edits: 5 (stakeholder-engagement 158 and 209; software-business 86, 98, 216).
- Stripped: 0.
- Left as is (conversion noise): 4 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 19 | no-quote (triage): ethical minimum/maximum glossed in the deep ref's own words under `[V]`, plus "introduced as a tool for managers and stakeholders to evaluate corporate conduct", which no passage says | Now quotes the body text: ethical minimum "the least a company might do that complies with the law", ethical maximum "the strongest possible action to behave ethically in a given situation" [V]; the remainder reads "are introduced through the Samsung washer recall" [AP], which is what the section does. The "tool for managers and stakeholders" framing is dropped | src 3866–3870 (Ch 3.1) |
| 136 | near: "people, planet, profit" in lower case | Now "People, Planet, Profit", as the source's section heading sets it (the only place the three words appear together) | src 4630 (Ch 3.4) |
| 138 | no-quote (triage): Coca-Cola water figures paraphrased under `[V]`; "local population" is not the source's word | Now quotes: in Chiapas, Mexico, "the Coca-Cola bottling plant consumes more than one billion liters of water daily, but only about half the population has running water" [V] | src 4737–4738 (Ch 3.4) |
| 232 | figure paraphrase under `[V]`: "the inflation-adjusted minimum wage declined 23%" | Now the real minimum wage "actually declined by 23 percent" [V]. The quote starts after "inflationadjusted", which the conversion glues | src 9133 (Ch 6.2) |
| 234 | figure paraphrase under `[V] [BT]`: "a 35% wage gap" | Now "a wage gap of about 35 percent each year" [V] [BT] | src 9178 (Ch 6.2) |
| 234 | figure paraphrase under `[V]`: "pay equity is projected for 2059-2119" | Now women "are not projected to reach pay equity until at least 2059, with projections based on recent trends predicting dates as late as 2119" [V] | src 9192–9193 (Ch 6.2) |
| 276 | figure paraphrase under `[V] [BT]`: millennials' 91% | Now 91 percent "say they do not expect to stay with their current job longer than three years" [V] [BT] | src 10461–10463 (Ch 7.1) |
| 280 | figure paraphrase under `[V]`: non-compete coverage ("one in six workers earning under $40,000") | Quoted whole: "About 20 percent of the U.S. private-sector workforce, and about one in six people in jobs earning less than $40,000 a year, are now covered by non-compete agreements" [V] | src 10662–10663 (Ch 7.1) |
| 312 | missing (triage): "concerted activity" is not in the source | Now the post was not part of a "concerted or group action" among Duane's fellow employees, so not protected under the NLRA, and Etchingham called it more like "a tantrum" and "childish ridicule" than speech protected under Section 7 [V] [BT]. The source ties Section 7 to the tantrum sentence, not to "concerted" | src 11612–11616 (Ch 7.5) |
| 320 | near: Krawcheck quote nested a spurious opening mark before "before long", and the `...` hid the switch from narration to her own words | Split into two quotes: "speaking out did come at a cost. … at that time" and Krawcheck writes that "before long I was 'reorganized out' of that role" [V] | src 11884–11896 (Ch 7.5) |
| 328 | figure paraphrase under `[V] [BT]` (McKinsey 15%, 35%, 50%); "50% higher" drops the source's "more than" | Quoted: "15 percent more likely to post financial returns above their industry median in the United States"; "35 percent more likely to show returns exceeding their respective industry median" [V] [BT]; "had returns on equity more than 50 percent higher than those companies that ranked in the lowest 25 percent" [V] [BT] | src 12600–12603, 12622–12624 (Ch 8.1) |
| 330 | figure paraphrase under `[V] [BT]`: "68% of management roles held by White people" | Now "of the company’s management and leadership roles, 68 percent are held by White people" [V] [BT] | src 12551–12552 (Ch 8.1) |
| 340 | near: "occupying" inside the Welsh quote; the source's quote mark follows it | Now occupying "a place parallel … qualifying for the exception" | src 12922–12923 (Ch 8.2) |
| 406 | missing: Commonwealth Fund quote; the words are right but the page header `**260 9 • Professions under the Microscope**` falls between "high" and "income", and the deep ref's `...` covers the rest of the sentence and the source's own ". . ." | Split into two quotes joined by "and". Each now matches; the first is `interrupted` by the header (see Left as is) | src 14954–14960 (Ch 9.4) |
| 412 | near: Hiltzik quote dropped the source's quote marks round ‘voluntary’ | Now "'voluntary' wellness programs …" | src 15154–15155 (Ch 9.4) |
| 528 | near (blockquote): Mill blockquote opened with "the", which sits outside the source's quote mark | Blockquote now opens at "only purpose", as line 87 already does | src 2581–2583 (Ch 2.4) |
| 552–606 | Key-statistics table: `[V]` on 51 unquoted figure cells | `[V]` → `[AP]` (30 rows); `[V] [BT]` → `[BT]` (21 rows). Values not re-traced; spot checks against the source held (WEF $2 trillion 8038, Hurricane Harvey fifty-two inches 14734 and 40 percent 14740, VW nearly $30 billion 8123, Microsoft $97 million 16738, $390 gift threshold 11377, CLC $2 trillion/decade 6141, 39–73 million jobs 16791, 55 million / 35 percent contractors 16650–16651) | — |

## Changes, derived tier

- `distillations/stakeholder-engagement/…-stakeholder-engagement.md:158` (triage): the Worked Example's framework-citation list put `[V]` on citations, not quotations. Now ethical minimum/maximum and moral minimum `[AP]` (the source's own terms), triple bottom line `[BT]` (Elkington, as the deep ref's Connections list has it).
- `…-stakeholder-engagement.md:209`: the evidence-marker note said ethical minimum/maximum, moral minimum and the triple bottom line "are `[V]`". Now says they carry `[V]` definitions in the deep ref and that the Worked Example cites them as `[AP]` and `[BT]`, so the note stays true after the 158 change.
- `distillations/software-business/…-software-business.md:86`: carried the deep ref's wrong quote "concerted activity" under NLRA Section 7 (unmarked). Now not part of a "concerted or group action" among fellow employees, so not protected under the NLRA.
- `…-software-business.md:98`: the Hiltzik quote dropped the quote marks round 'voluntary', as deep 412 did. Fixed the same way.
- `…-software-business.md:216`: the evidence-marker note said the SOX and FCPA dates are `[V]` in the deep ref. They are Key-statistics rows, now `[AP]`; the note now says `[AP]`. Its other claims still hold: the False Claims Act award figures (deep 316), the McKinsey 15%/35% figures (deep 328, now quoted) and the CEO-pay ratio data (deep 260) keep `[V]` in the prose.
- Propagation grep of the light ref and all five distillations for "Chiapas", "concerted", "ethical minimum/maximum", "tool for", "planet", "2059", "wage gap", "nine in ten", "one in six", "50 percent", "68", "reorganized", "place parallel", "voluntary", "only purpose", "high income", "declined": no other copy of a wrong quotation or `[V]` marker. The light ref (39) and software-business (40, 72) give "declined 23%" and "35% wage gap" as unmarked paraphrase; retro 14 and aar 16 gloss ethical minimum/maximum without the dropped "tool" framing (aar 16's two `[V]` quotes match the Key Terms). Decision-making 28 quotes Mill from "only purpose", which matches. aar 105's note ("The ethical minimum/maximum distinction is `[V]` in the deep ref") stays true.

## Left as is (conversion noise)

- **Deep 406** (interrupted): first half of the Commonwealth Fund quote runs across the page header `**260 9 • Professions under the Microscope**` between "high" and "income" (src 14954–14959).
- **Deep 474** (interrupted): "employees are more likely to be unethical when they are dissatisfied with / their jobs" runs across the running header `**Access for free at openstax.org**` and `**11.2 • Committing to an Ethical View 305**` (src 17751–17757).
- **aar 24** and **retro 20** (interrupted): the same Ch 11.2 quote and the same header (src 17751–17757).

## Triage cross-check

Every triage row was fixed:

- **Deep 19** (no-quote, paraphrase under `[V]`): the definitions are now quoted from Ch 3.1; the unsupported "tool for managers and stakeholders" framing is replaced with `[AP]` "introduced through the Samsung washer recall".
- **Deep 138** (no-quote, paraphrase under `[V]`): the Coca-Cola figures are now the source's sentence, quoted; "local population" corrected to "population".
- **Deep 312** (missing, "concerted activity"): the source says "concerted or group action" (src 11613); quote corrected, and the Section 7 link moved to the sentence the source attaches it to. Same wording fixed in software-business 86.
- **Stakeholder-engagement 158** (no-quote, framework-citation list): marker fix, `[V]` → `[AP]` / `[BT]`; note at 209 adjusted to match.

## Checker counts

- Before: 16 apostrophe, 6 initial, 5 near, 3 interrupted, 2 missing, 4 no-quote (14 failing); 59 figure claims not checked.
- After: 18 apostrophe, 6 initial, 4 interrupted (4 failing, all conversion noise listed above); 1 figure claim not checked. Apostrophe rose by two because the new quotes at 328 and 330 are checked and match at that level; interrupted rose by one because deep 406 moved from `missing` to `interrupted`; the figure-claim count fell because the Key-statistics rows no longer carry `[V]` and the prose figure claims are now quoted.

## Open

- Stamp left as is (quotations mode). No commit made, no build run. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and five distillations need re-stamping by the parent.
- Claim change the derived tier could carry: deep 19 drops "introduced as a tool for managers and stakeholders to evaluate corporate conduct". No derived file carries that phrase.
- Outside a quotations pass: the integrity note at deep 665 says every verbatim quotation "was verified character-by-character against the source markdown in Pass D", which this run shows was not so. A full Pass I should reword it. The Key-statistics values were spot-checked, not traced row by row.
