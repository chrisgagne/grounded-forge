# Pass I sort report — CAIB Report, Volume I

**Current verdict: fail pending 31 numbered edit groups. Verdict after those edits: pass.** I confirmed 57 distinct defects across the two audits. The fixer introduced no new verified defect.

## 1. What I read

**In full:** `sort-brief.md`; the three calibration fixtures; `pass-i-spec.md`; `blind-findings.md`; `fixer-audit-log.md`; `post-audit-deep.md`, all 355 lines; `blind-brief.md`; `fixer-prompt.md`; `source-card.md`; the repository operating contract and its nine prescribed architecture documents.

**For comparison:** every changed line between `frozen-deep.md` and `post-audit-deep.md`, including the original wording.

**Source verification:** targeted passages in `tape.md` for every finding and substantive repair. This sort did **not** repeat either auditor’s end-to-end source read. I also visually inspected the original PDF’s printed pp. 104, 171, 202 and 203: the budget table, recovered findings numbers and disputed column joins. :codex-file-citation{path="_planning/pass-i/demo/caib-report-vol1/source.pdf" purpose="source"}

Mechanical checks:

- Frozen and post-audit deep references match their supplied SHA-256 files.
- The PDF matches the source card’s SHA-256.
- Both `wc` and whitespace splitting give **167,496 words**; the tape contains **25,038 newlines** and **250 form feeds**.
- `check-verbatim.py post-audit-deep.md --source tape.md --no-corpus-search` reports **no findings**.
- The statistics table contains **18 data rows**, not the fixer log’s reported 17.

All **L** locators below refer to `post-audit-deep.md`. All source pages are **printed pages**.

## 2. Sorted ledger

### Blind audit

**B1–B47** correspond to the blind audit’s numbered findings.

| ID | Classification | Post line(s) | Source evidence and adjudication |
|---|---|---:|---|
| B1 | Missed | 9 | Synopsis continues onto p. 13; the introductions begin on pp. 14 and 16. Their titles are “An Introduction to the Space Shuttle” and “An Introduction to NASA”. |
| B2 | Missed | 9 | The TOC and chapter lists contradict the assertion that every chapter closes with findings, recommendations and endnotes. Chapters 1, 2, 5 and 8 have neither numbered findings nor recommendations; Chapter 11 is the recommendations compilation, pp. 225–227. |
| B3 | Missed | 11, 343 | The tape itself measures 167,496 whitespace-delimited words. The retained 166,877 count is incorrect. The source card repeats it, but that file is outside the requested edits. |
| B4 | Missed | 15, 299 | pp. 9, 49; tape 518–524, 4237–4244: the strike was **in the vicinity of** the lower half of panel 8. Both occurrences omit that qualification. |
| B5 | Missed | 33, 315 | p. 9; tape 500–504: **more than 30,000** documents. Both occurrences lose the lower bound. |
| B6 | Missed | 33 | The return-to-flight/continuing-to-fly distinction is on p. 9, tape 555–566. Page 10 contains the photograph. |
| B7 | Missed | 35 | Checks and balances are on p. 12; difficult, resisted changes and atrophying improvements are on p. 13, tape 797–818. |
| B8 | Missed | 9; insertion after 39 | pp. 14–17 describe Shuttle components and NASA’s matrix. Neither introductory section receives substantive treatment. The chapter-level gate nevertheless passes; this is a narrower coverage omission under the audit brief’s section-coverage requirement. |
| B9 | Missed | 45 | p. 21; tape 1438–1441 expressly bounds the organisational-capability judgement to the time of the accident. |
| B10 | Missed | 49 | p. 24; tape 1705–1718: **10 working days** and an inflation-adjusted cost comparison. Endnote 16, p. 26, tape 1921–1924 explains the conversion. |
| B11 | Confirmed and fixed | 65 | p. 47; tape 4126–4128: **more than 25,000** people. Correctly repaired. |
| B12 | Confirmed and fixed | 69 | p. 54; tape 4740–4750 places the experiment on Stanford’s loading dock. “Kitchen-table” was unsupported and is removed. |
| B13 | Confirmed and fixed | 77 | p. 63; tape 5720–5727 says the manoeuvre **possibly** imparted departure velocity. The repair restores that uncertainty. “Matched” describes the exclusionary testing, not positive identification; F3.5-2, p. 64, does not contradict the repaired sentence. |
| B14 | Confirmed and fixed | 79 | p. 66; tape 6165–6181 uses a ten-inch hole as an analytical example and says the exact size will never be known. Correctly repaired. |
| B15 | Confirmed and fixed | 83 | R3.8-1 and R3.8-2 are on p. 83, tape 8346–8359. Correctly recited. |
| B16 | Confirmed and fixed | 87 | p. 90; tape 9033–9043 identifies hydrazine. Correctly repaired. |
| B17 | Missed | 87 | F4.2-6, p. 90, tape 9025–9026 says crushed foam **does not appear** to have contributed. It remains categorically “ruled out”. |
| B18 | Confirmed, fix incomplete | 87 | F4.2-13 and R4.2-3, p. 94, tape 9401–9402, 9452–9455. The repair correctly changes completed incidents into permitted processes, but retains p. 93 and omits intertank hand-spraying from the recommendation. |
| B19 | Over-flagged — blind auditor | 87, 311 | p. 94, tape 9433–9445 gives both the 1-in-370 estimate and 1-in-356 as-flown value. L87 explicitly reports an **estimate**; L311 summarises the same approximate figure. Neither says it is the as-flown value. Adding the latter would improve detail, but its omission does not falsify the reported estimate. |
| B20 | Missed | 99 | p. 103, tape 10156–10163: government discretionary spending grew **more than 25 percent in purchasing power**. |
| B21 | Missed | 99, 309 | p. 104, tape 10421–10427 and Figure 5.3-4: the figures are presidential **requests**, distinct from appropriations and operating plans. Confirmed visually. |
| B22 | Confirmed and fixed | 101 | p. 107, tape 11138–11149: O’Connor was head of the Shuttle Program at Headquarters when he resigned. Correctly repaired; naming him is optional. |
| B23 | Missed | insertion after 105 | §5.6, pp. 115–116, tape 12210–12327 covers the leadership and strategy changes. That section remains omitted. |
| B24 | Missed | 119 | p. 123, tape 13248–13255: no right-bipod loss was **observed on 66 imaged flights**, rather than never occurring. |
| B25 | Missed | 121 | p. 124, tape 13338–13343 calls the divot the largest **area** of tile damage. The unqualified superlative loses that metric. |
| B26 | Confirmed, fix incomplete | 121 | p. 124, tape 13295–13315. “Probably” is restored, but the sidebar remains incorrectly cited to p. 123. |
| B27 | Confirmed and fixed | 127 | p. 127, tape 13708–13716 reports 707 **dings**, not distinct tiles. Correctly repaired. The accompanying counterfactual burn-through wording also matches tape 13666–13674. |
| B28 | Missed | 127 | pp. 129–130, tape 14017–14054: the study estimates **Orbiter loss due to tile failure**, not tile-loss probability, and states its data and assumption limits. |
| B29 | Missed | 127 | The STS-56/58 judgement and STS-87 count occur on p. 129, tape 13956–13971. Their retained p. 128 citations are wrong. |
| B30 | Missed | insertion after 127 | “Impact Resistant Tile”, p. 130, tape 14056–14072 remains omitted. It explains existing mitigations and their limits. |
| B31 | Missed | 137 | p. 139, tape 15157–15206: risk accumulation is part of §6.2’s conclusion, not a sidebar. |
| B32 | Confirmed and fixed | 145 | pp. 143, 171; tape 15422–15426, 17119–17122 assigns classification to United Space Alliance. Removing the incorrect co-chair attribution fixes the defect. |
| B33 | Missed | 145 | p. 142, tape 15374–15378: the photo group believed the Orbiter **may have been** damaged. |
| B34 | Missed | 147, 301 | p. 143, tape 15450–15454 explicitly compares **volume**. Both occurrences remain unspecific. |
| B35 | Confirmed and fixed | 149 | pp. 147–148, tape 15724–15763: Ham’s criticism was on 21 January; Dittemore replied on 22 January. The repair retains only Ham’s correctly dated judgement. It need not reproduce his reply. |
| B36 | Missed | 149 | p. 148, tape 15791–15803: the missed question concerned **additional** footage beyond the 35 seconds already downlinked. |
| B37 | Confirmed and fixed | 151 | pp. 150–151, tape 15913–15924: White → Austin → DoD support office. Correctly repaired. |
| B38 | Confirmed and fixed | 157 | p. 157, tape 16300–16309: the shrugs were answers to the Board, not behaviour inside the meeting. Correctly repaired. |
| B39 | Confirmed and fixed | 157 | p. 160, tape 16471–16480: engineers considered trajectories and found none substantially reducing heating. Correctly repaired. |
| B40 | Confirmed and fixed | 159 | p. 164, tape 16713–16721 distinguishes distributions of favourable and unfavourable results. The repaired comparative wording preserves that distinction. |
| B41 | Missed | 176, 312 | p. 173, tape 17251–17260: reaching the morning of Flight Day 30 depends on modified crew activity and sleep. Both occurrences omit the condition. |
| B42 | Missed | 199 | p. 184, tape 18334–18375 supports Air Force launch verification without “every”, and labels 2.9 percent a **probability of failure**. |
| B43 | Missed | 276 | p. 221, tape 22216–22220 excludes the tile-covered outer mould line from the denominator and says corrosion in the remainder **may remain undetected**. |
| B44 | Confirmed and fixed | 286 | p. 232, tape 22939–22945, 22986–22993: first-week proposal, signed on 18 February. Correctly repaired. |
| B45 | Missed | 288 | p. 233, tape 23048–23063 specifies FOIA exemption and limited Congressional access. |
| B46 | Missed | 290 | p. 233, tape 23119–23122 allows requested Inspector General attendance **except** privileged-statement proceedings. |
| B47 | Missed | 353 | p. 127, tape 13781–13783 supplies “STS-173”; it supplies no assertion that this mission did not exist. Strip the external assertion. |

### Fix-in-place audit

**F1–F21** correspond to “Claims corrected to the source”. **S1–S2** are the two framing findings; **C1–C6** are the citation corrections, in log order.

| ID | Classification | Post line(s) | Source evidence and adjudication |
|---|---|---:|---|
| F1 | Confirmed and fixed | 39 | p. 97, tape 9692–9708 names Weinberg and the NRC route, but does not identify him as a nuclear physicist. Correctly removes source-external biography. |
| F2 | Disputed | 55 | p. 27, tape 1959–1961 says more than 70 scientists were involved. **Defect reading:** the original implies individually attributable experiments. **Clean reading:** “more than 70 scientists’ experiments” is a loose collective description, not a count of experiments. The replacement is faithful and clearer; no remaining edit is needed. |
| F3 — participation | Confirmed and fixed | 65 | Same defect as B11. |
| F3 — geography | Over-flagged — fixer | 65 | p. 44, tape 3811–3815 gives more than 2,000 square miles in Texas alone; p. 47 also describes western Louisiana. The original combined Texas/Louisiana area exceeding 2,000 square miles is not contradicted. The new wording is more specific and valid. |
| F4 — kitchen-table | Confirmed and fixed | 69 | Same defect as B12. |
| F4 — pressure result | Over-flagged — fixer | 69 | p. 54, tape 4751–4795 describes and explains pressure-induced cracking. The original “showed how hydrostatic pressure cracks the foam” did not assert foam ejection. The expanded replacement is source-supported, but this particular allegation of overstatement does not hold. |
| F5 | Confirmed and fixed | 77 | Same defect as B13. |
| F6 | Confirmed and fixed | 79 | Same defect as B14. |
| F7 | Confirmed and fixed | 87 | p. 87, tape 8727–8757 attributes oversight and requirement confusion to the weld-inspection lapse. The repair correctly attaches that explanation to the lapse. |
| F8 | Confirmed and fixed | 87 | Same defect as B16. |
| F9 | Confirmed, fix incomplete | 87 | Same defect and remaining problems as B18. |
| F10 | Confirmed and fixed | 87 | Synopsis p. 12, tape 730–734 supplies the 3,000-element count; Chapter 4 p. 86 supplies the smaller listed tree and closure account. The added attribution fixes the locator. |
| F11 | Confirmed and fixed | 101 | Same defect as B22. |
| F12 | Confirmed, fix incomplete | 121 | Same defect and remaining locator problem as B26. |
| F13 | Confirmed and fixed | 127 | Same defect as B27, with a faithful counterfactual and camera description, p. 127. |
| F14 | Confirmed and fixed | 145 | Same defect as B32; the p. 143 citation is also correct. |
| F15 | Confirmed and fixed | 149 | Same defect as B35. |
| F16 | Confirmed and fixed | 151 | Same defect as B37. |
| F17 | Confirmed and fixed | 157 | Same defect as B38. |
| F18 | Confirmed and fixed | 157 | Same defect as B39. |
| F19 | Confirmed and fixed | 159 | p. 160, tape 16500–16507 says the briefing focused **primarily** on tiles. “All” was too strong; correctly repaired. |
| F20 | Confirmed and fixed | 159 | Same distribution defect as B40. The additional correction to Langley/Johnson engineers and Ames as the simulator site is supported by p. 164, tape 16696–16712. |
| F21 | Confirmed and fixed | 286 | Same defect as B44. |
| S1 | Disputed | 182 | p. 177, tape 17598–17620 calls this a central piece of the expanded cause model and labels the organisational cause statement. **Defect reading:** “because it is the report’s organising claim” supplies the ingester’s editorial rationale. **Clean reading:** it accurately describes the source’s organising role without grading evidence. The neutral repair is acceptable. |
| S2 | Confirmed and fixed | 223 | p. 196, tape 19672–19693 supplies the sequence, but no judgement of its precision. “Precisely” was source-external evaluation; “step by step” describes the actual exposition. |
| C1 | Confirmed and fixed | 69 | The testing assertions occur on p. 52, tape 4518–4556. Expanding p. 53 to pp. 52–53 repairs their locator. |
| C2 | Confirmed and fixed | 83 | Same defect as B15. |
| C3 | Confirmed and fixed | 117 | The 0.006-foot-pound requirement is on p. 122, tape 12999–13006. |
| C4 | Confirmed and fixed | 135 | “Every bit of padding” is on p. 138, tape 15042–15050. |
| C5 | Confirmed and fixed | 145 | Same locator repair accompanying F14/B32. |
| C6 | Confirmed and fixed | 276 | Maintenance-documentation content is on p. 220; modification growth is on p. 221. The expanded citation covers both. |
| Header — PDF index rationale | Over-flagged — fixer | 10 | The original expressly defined its “PDF page index” as the form-feed count. That zero-based index equals the printed page; it was not an incorrect numerical mapping. The replacement usefully distinguishes index from one-based PDF page numbering. |
| Integrity — column boundary | Confirmed and fixed | 347 | Printed p. 203 visually shows the complete slippery-slope sentence within the right column. The original column-boundary explanation was wrong; the replacement correctly describes tape interleaving. |

The remaining logged changes are **verified updates or additions, not allegations of defects in the frozen reference**:

| Logged change | Post line(s) | Assessment |
|---|---:|---|
| Record completed second OCR | 8, 349 | Supported by the operator notes in both dispatch briefs. An earlier run’s inability to perform OCR is not disproved by its later completion. |
| Clarify local PDF location | 343 | The local ingest PDF exists. Its present availability does not establish that the producer’s historical availability statement was false. |
| Restore findings identifiers | 172, 347 | Printed p. 171 confirms every added identifier. The frozen reference already acknowledged conversion loss; adding identifiers improves it without repairing a false paraphrase. |
| Confirm p. 202 contractor join | 347 | The original page confirms the join from the left-column foot to the right-column head. No substantive defect existed in that paraphrase. |
| Narrow sidebar citation to p. 54 | 69 | Correct, but the original pp. 54–55 range already included the passage. |

**Introduced-defect check:** I checked all 28 changed lines. The added source details, identifiers, dates, qualifications and layout explanations are supported. **No new defect was verified.**

## 3. Remaining edits

These are **31 numbered edit groups**, corresponding to the 29 missed findings and two incomplete repairs. Where a group contains several replacements, apply all of them. Locators refer to the current file.

1. **L9 — introductory structure.**

   Current:
   `Report Synopsis (pp. 11–12); "A Brief Introduction to the Space Shuttle" and NASA organisation sidebars (pp. 13–17).`

   Replacement:
   `Report Synopsis (pp. 11–13); "An Introduction to the Space Shuttle" (pp. 14–15) and "An Introduction to NASA" (pp. 16–17).`

2. **L9 — chapter endings.**

   Current:
   `Each chapter closes with findings, recommendations and endnotes; Chapter 2 and Chapter 8 carry no findings.`

   Replacement:
   `Findings and recommendations appear within the relevant chapters. Chapters 1, 2, 5 and 8 contain neither numbered findings nor recommendations; Chapter 9 contains recommendations but no findings. Chapter 11 compiles the recommendations and has no separate findings or endnotes.`

3. **L11 and L343 — conversion count.**

   At both locations, replace:
   `25,038 lines and 166,877 words`

   With:
   `25,038 newline-delimited lines and 167,496 whitespace-delimited words`

4. **L15 and L299 — strike location.**

   L15, current:
   `struck the lower half of Reinforced Carbon-Carbon (RCC) panel 8`

   Replacement:
   `struck the wing in the vicinity of the lower half of Reinforced Carbon-Carbon (RCC) panel 8`

   L299, current:
   `struck lower half of RCC panel 8, left wing`

   Replacement:
   `struck in the vicinity of the lower half of RCC panel 8, left wing`

5. **L33 and L315 — documents reviewed.**

   Replace `some 30,000 documents reviewed` at L33 with `more than 30,000 documents reviewed`.

   Replace `about 30,000 documents` at L315 with `more than 30,000 documents`.

6. **L33 — recommendation distinction citation.**

   In the final sentence, replace `(Executive Summary, p. 10)` with `(Executive Summary, p. 9)`.

7. **L35 — Synopsis citations.**

   For the sentence ending `difficult and internally resisted`, replace `(Synopsis, p. 12)` with `(Synopsis, pp. 12–13)`.

   For the final sentence ending `improvements that fade over time`, replace `(Synopsis, p. 12)` with `(Synopsis, p. 13)`.

8. **After L39 — introductory coverage.**

   Current: no substantive treatment of the two introductory sections.

   Insert:
   > The introductory sections distinguish the Orbiter, main engines, External Tank and Solid Rocket Boosters, and describe the tiles, blankets and RCC components of the Thermal Protection System [AP] (Introduction to the Space Shuttle, pp. 14–15). NASA is described as a heavily matrixed organisation: Centers provide facilities and support, while programmes employ civil servants and contractors. The Shuttle Program Office at Johnson manages the programme; Kennedy supplies launch, landing and processing facilities; and Marshall manages the main-engine, External Tank and reusable solid-rocket-motor contracts [AP] (Introduction to NASA, pp. 16–17).

9. **L45 — temporal qualification.**

   Current:
   `whose safe operation exceeded NASA's organisational capabilities`

   Replacement:
   `whose safe operation exceeded NASA's organisational capabilities as they existed at the time of the Columbia accident`

10. **L49 — turnaround and cost comparison.**

    Current:
    `The promised economics never arrived: turnaround took 67 days against 10 projected, and missions cost more than $140 million, about seven times the projection.`

    Replacement:
    `The promised economics never arrived: turnaround averaged 67 days against 10 working days projected, and missions cost more than $140 million, about seven times the earlier projection after adjustment for inflation [AE] (Ch 1, p. 24; endnote 16, p. 26).`

11. **L87 — crushed-foam qualification.**

    **Strip** `a crushed piece of foam under the left bipod strut after the tank was de-mated in a manifest reshuffle, ` from the categorical ruled-out list.

    After that sentence, insert:
    `Crushed foam beneath the left bipod strut does not appear to have contributed to the loss of the ramp [AP] (Ch 4, p. 90).`

12. **L87 — closeout repair completion.**

    Current:
    `Two Michoud closeout processes can be performed by a single person, prompting a recommendation that at least two employees attend every final closeout [AP] (Ch 4, p. 93).`

    Replacement:
    `Two final-closeout processes at Michoud could be performed by a single person, prompting a recommendation that at least two employees attend all final closeouts and intertank-area hand-spraying procedures [AP] (Ch 4, p. 94).`

13. **L99 — discretionary spending.**

    Current:
    `discretionary spending rose 25 percent`

    Replacement:
    `government discretionary spending rose more than 25 percent in purchasing power`

14. **L99 and L309 — budget metric.**

    L99, current:
    `its budget fell from $4.128 billion in FY1993 to $2.977 billion in FY1998`

    Replacement:
    `the presidential budget request for the Shuttle fell from $4.128 billion in FY1993 to $2.977 billion in FY1998`

    L309, current metric:
    `Shuttle budget`

    Replacement:
    `Shuttle presidential budget requests / purchasing power`

    L309, current value:
    `$4.128bn (FY1993) to $2.977bn (FY1998); about 40% loss of purchasing power over the decade`

    Replacement:
    `$4.128bn requested for FY1993; $2.977bn requested for FY1998; about 40% loss of purchasing power over the decade`

15. **After L105 — §5.6 coverage.**

    Current: no substantive treatment of §5.6.

    Insert:
    > **A change in leadership (Sec 5.6).** Sean O'Keefe replaced Goldin after November 2001. In 2002 he transferred Shuttle and Station programme management from Johnson to NASA Headquarters, considered contract expansion and competitive sourcing, and initiated workforce planning and comparisons with other high-risk enterprises. The November 2002 Integrated Space Transportation Plan redirected funding towards the Shuttle and Station, introduced the Orbital Space Plane as a complement, and envisaged Shuttle operation through at least 2010, with possible extension to 2020 or beyond [AE] (Ch 5, pp. 115–116).

16. **L119 — observation limit.**

    Current:
    `while the right never did`

    Replacement:
    `while no right-bipod foam loss was observed on the 66 flights with suitable imagery`

17. **L121 — tile-damage metric.**

    Current:
    `which caused the largest tile damage in the programme's history`

    Replacement:
    `which left a 9-by-4.5-by-0.5-inch divot described as the largest area of tile damage in Shuttle history`

18. **L121 — sample-bias locator.**

    In the final sidebar sentence, replace `(Ch 6, p. 123)` with `(Ch 6, p. 124)`. Retain the restored `probably`.

19. **L127 — probabilistic study metric and limits.**

    Current:
    `A 1990 probabilistic study that put tile-loss risk at about 1 in 1,000 a mission, with debris as 40 percent of it, had not been fully used [BT] (Ch 6, pp. 129–130).`

    Replacement:
    `A 1990 probabilistic study estimated about a 1-in-1,000 probability per mission of losing an Orbiter because of Thermal Protection System tile failure, with debris-related problems accounting for approximately 40 percent of that probability. The Board notes that actual risk could differ because of limited data and simplified assumptions, and that NASA had not fully exploited the study's insights [BT] (Ch 6, pp. 129–130).`

20. **L127 — non-bipod event citations.**

    Replace `(Ch 6, p. 128)` following `the increasingly casual ways in which debris impacts were dispositioned` with `(Ch 6, p. 129)`.

    Replace `(Ch 6, p. 128)` following the STS-87 sentence with `(Ch 6, p. 129)`.

    Retain p. 128 for the fourteen-event table itself.

21. **After L127 — impact-resistant tile coverage.**

    Current: no substantive treatment of this subsection.

    Insert:
    > **Impact-resistant tile.** TUFI-coated AETB tile offered approximately 6–20 times the debris-impact resistance of current acreage tile, and at least 772 advanced tiles had been installed on Orbiter base heat shields and upper body flaps. Its higher thermal conductivity prevented its use as a replacement for larger areas of tile coverage [AE]. The Board judged that certification of next-generation tiles would not adequately address debris threats because their impact requirements did not appear to reflect specific probable damage sources [AP] (Ch 6, p. 130).

22. **L137 — conclusion identification.**

    Current:
    `The chapter's sidebar on risk states the mechanism`

    Replacement:
    `The section's conclusion states the mechanism`

23. **L145 — photo group’s uncertainty.**

    Current:
    `the photo group believed there was damage`

    Replacement:
    `the photo group believed the Orbiter may have been damaged`

24. **L147 and L301 — calibration comparison.**

    L147, current:
    `the debris was estimated at up to 640 times larger (the Board's best estimate is 400 times)`

    Replacement:
    `the debris was estimated at up to 640 times larger in volume than the calibration projectiles (the Board's best estimate is 400 times)`

    L301, current metric:
    `Debris size relative to Crater calibration`

    Replacement:
    `Debris volume relative to Crater calibration`

25. **L149 — missed crew question.**

    Current:
    `Nobody asked the crew whether they had filmed the tank at separation (Missed Opportunity 2) [AE] (Ch 6, p. 148).`

    Replacement:
    `Nobody asked David Brown whether he had additional External Tank separation footage beyond the 35 seconds already downlinked (Missed Opportunity 2) [AE] (Ch 6, p. 148).`

26. **L176 and L312 — consumables condition.**

    L176, current:
    `Carbon-dioxide scrubbing limited the stay to Flight Day 30 (15 February).`

    Replacement:
    `With modified crew activity and sleep time, carbon-dioxide scrubbing could have supported a stay until the morning of Flight Day 30 (15 February) [AE] (Ch 6, p. 173).`

    L312, current value:
    `Atlantis launch possible 10 February; consumables to Flight Day 30 (15 February)`

    Replacement:
    `Hypothetical Atlantis launch on 10 February; modified crew activity and sleep time could extend consumables to the morning of Flight Day 30 (15 February)`

27. **L199 — Aerospace scope and metric.**

    Current:
    `The Aerospace Corporation independently verifies every Air Force launch and is subject to no schedule or cost pressure; its involvement is credited with a 2.9 percent failure rate against 14.6 percent commercially [AE] (Ch 7, p. 184).`

    Replacement:
    `The Aerospace Corporation provides independent launch verification for the U.S. Air Force and is not subject to schedule or cost pressures. The Board credits its involvement with reducing engineering errors and reports a 2.9 percent probability of failure for expendable launch vehicles, compared with 14.6 percent in the commercial sector [AE] (Ch 7, p. 184).`

28. **L276 — corrosion denominator and certainty.**

    Current:
    `About 10 percent of the Orbiter's structure cannot be inspected for corrosion [AE] (Ch 10, p. 221).`

    Replacement:
    `Approximately 90 percent of Orbiter structure, excluding the tile-covered outer mould line, can be inspected for corrosion; corrosion in the remaining 10 percent may remain undetected for the vehicle's life [AE] (Ch 10, p. 221).`

29. **L288 — disclosure scope.**

    Current:
    `were exempt from disclosure [AE] (App A, p. 233).`

    Replacement:
    `were exempt from disclosure under the Freedom of Information Act; limited Congressional access was governed by a special written agreement preserving confidentiality [AE] (App A, p. 233).`

30. **L290 — Inspector General exception.**

    Current:
    `the NASA Inspector General could attend its proceedings`

    Replacement:
    `the NASA Inspector General could attend proceedings on request, except those involving privileged witness statements`

31. **L353 — source-external mission assertion.**

    **Strip:** `, a mission that did not exist`

    Retain the source caption’s `through STS-173` wording and its page citation.

## 4. Counts

Counts below distinguish **finding occurrences** from **distinct defects**. Overlapping audit findings and repeated citation repairs are counted once in the combined ledger. Verified housekeeping updates and identifier additions are excluded from defect counts.

| Classification | Blind occurrences | Fixer occurrences | Combined, distinct |
|---|---:|---:|---:|
| Confirmed and fixed | 15 | 26 | 26 |
| Confirmed, fix wrong or incomplete | 2 | 2 | 2 |
| Missed by fix-in-place audit | 29 | — | 29 |
| Over-flagged | 1 | 3 | 4 |
| Disputed | 0 | 2 | 2 |
| **Total adjudicated** | **47** | **33** | **63** |

- **Confirmed distinct defects:** 57, including the 29 misses.
- **Remaining distinct defects:** 31.
- **Over-flags:** blind auditor 1; fixer 3.
- **Disputed:** 2.
- **Verified defects introduced by the fixer:** 0.

The fixer’s 33 occurrences comprise its 21 numbered claim findings, two separately adjudicated subsidiary allegations, two framing findings, six citation findings, the PDF-index allegation and the column-boundary correction.

## 5. Gate verdict after remaining edits

**Pass once all 31 edit groups are applied.**

All eleven chapters and Appendices A–C have body coverage. The additions repair the narrower omissions identified by the blind audit. The confirmed factual, quantitative, qualification and citation defects then have source-supported repairs. The two disputed passages already have acceptable replacements; the over-flagged passages require no further changes. The current quotation check passes, and no fixer-introduced defect remains.

This is the **sort-leg verdict**. No source file or reference was edited or stamped. Derived-tier re-derivation and hash stamping remain subsequent protocol operations.