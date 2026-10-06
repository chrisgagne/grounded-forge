**Blind audit result: fail pending the corrections below.** The central thesis is source-grounded, but the reference contains factual errors, lost qualifications, citation errors and coverage gaps.

## 1. What I read

**In full:** `blind-brief.md`; all three calibration fixtures, before the cold read; `pass-i-spec.md`; `frozen-deep.md`, all 355 lines; `source-card.md`; and `tape.md`, end to end, including front matter, all eleven chapters, sidebars, findings, recommendations, endnotes, Appendices A–C and the final pages. I also read the repository operating contract and its nine prescribed architecture documents.

**In part:** the original PDF, visually inspecting printed pp. 171, 202 and 203; and supporting ingestion-protocol material for evidence-marker definitions. PDF metadata and the complete file checksum were checked. :codex-file-citation{path="_planning/pass-i/demo/caib-report-vol1/source.pdf" purpose="source"}

The frozen reference matches its supplied SHA-256. The PDF matches the source card’s SHA-256. A source-specific run of `check-verbatim.py` returned **no findings**. I accepted the brief’s completed independent second-OCR verification and did not repeat its quotation-page renders.

I did not read the parallel auditor’s findings or logs. No files were edited.

All source pages below are **printed page numbers**; all reference lines refer to `frozen-deep.md`.

## 2. Findings

1. **L9 — Structure: incorrect front-matter boundaries and title.**  
   **Evidence:** the Synopsis continues onto p. 13. The introductory sections occupy pp. 14–17.  
   **Exact fix:** replace `Report Synopsis (pp. 11–12)` with `Report Synopsis (pp. 11–13)`; replace `"A Brief Introduction to the Space Shuttle" and NASA organisation sidebars (pp. 13–17)` with `"An Introduction to the Space Shuttle" (pp. 14–15) and "An Introduction to NASA" (pp. 16–17)`.

2. **L9 — Structure: unsupported statement about chapter endings.**  
   **Evidence:** Chapters 1, 2, 5 and 8 contain neither numbered findings nor recommendations; Chapter 9 contains recommendations but no findings; Chapter 11 is a recommendations compilation without endnotes. Findings elsewhere occur within chapters.  
   **Exact fix:** replace the final sentence with:  
   `Findings and recommendations appear within the relevant chapters. Chapters 1, 2, 5 and 8 contain neither numbered findings nor recommendations; Chapter 9 contains recommendations but no findings. Chapter 11 compiles the recommendations and has no separate findings or endnotes.`

3. **L11, L343; source card — Provenance/count: incorrect word count.**  
   **Evidence:** both `wc -w` and whitespace splitting return **167,496**, not 166,877. The newline count is 25,038.  
   **Exact fix:** replace every `166,877 words` with `167,496 whitespace-delimited words`; where both counts are given, use `25,038 newline-delimited lines and 167,496 whitespace-delimited words`.

4. **L15, L299 — Lost spatial qualification.**  
   **Evidence:** Executive Summary p. 9 and §3.1 p. 49 locate the strike **in the vicinity of** the lower half of RCC panel 8.  
   **Exact fix:** replace `struck the lower half of Reinforced Carbon-Carbon (RCC) panel 8` with `struck the wing in the vicinity of the lower half of Reinforced Carbon-Carbon (RCC) panel 8`. In L299 use `struck in the vicinity of the lower half of RCC panel 8, left wing`.

5. **L33, L315 — Quantity: lost lower bound on documents reviewed.**  
   **Evidence:** Executive Summary p. 9 states **more than 30,000 documents**.  
   **Exact fix:** replace `some 30,000 documents reviewed` with `more than 30,000 documents reviewed`; replace `about 30,000 documents` in L315 with `more than 30,000 documents`.

6. **L33 — Citation locator.**  
   **Evidence:** the separation of return-to-flight and continuing-to-fly recommendations is on p. 9. Page 10 is a photograph.  
   **Exact fix:** change the final citation from `(Executive Summary, p. 10)` to `(Executive Summary, p. 9)`.

7. **L35 — Citation locators.**  
   **Evidence:** the statements about difficult, internally resisted changes and improvements that atrophy appear on Synopsis p. 13. The checks-and-balances and learning-organisation statements appear on p. 12.  
   **Exact fix:** cite the combined preview sentence `(Synopsis, pp. 12–13)`; change the final sentence’s citation to `(Synopsis, p. 13)`.

8. **L9; insert after L39 — Coverage: introductory sections are listed but not substantively represented.**  
   **Evidence:** pp. 14–17 explain the Shuttle’s principal components and NASA’s matrix of Centers, programmes and contractors.  
   **Exact fix:** insert:  
   `The introductory sections distinguish the Orbiter, main engines, External Tank and Solid Rocket Boosters, and describe the tiles, blankets and RCC components of the Thermal Protection System [AP] (Introduction to the Space Shuttle, pp. 14–15). NASA is described as a heavily matrixed organisation: Centers provide facilities and support, while programmes employ civil servants and contractors. The Shuttle Program Office at Johnson manages the programme; Kennedy supplies launch, landing and processing facilities; and Marshall manages the main-engine, External Tank and reusable solid-rocket-motor contracts [AP] (Introduction to NASA, pp. 16–17).`

9. **L45 — Over-broad temporal scope.**  
   **Evidence:** p. 21 limits the organisational-capability judgement to capabilities **as they existed at the time of the Columbia accident**.  
   **Exact fix:** replace `whose safe operation exceeded NASA's organisational capabilities` with `whose safe operation exceeded NASA's organisational capabilities as they existed at the time of the Columbia accident`.

10. **L49 — Quantity: missing inflation adjustment and time unit.**  
    **Evidence:** p. 24 gives **10 working days**, versus an observed average of 67 days, and says the sevenfold cost comparison is inflation-adjusted. Chapter 1 endnote 16, p. 26, explains the conversion.  
    **Exact fix:** replace the economics sentence with:  
    `The promised economics never arrived: turnaround averaged 67 days against 10 working days projected, and missions cost more than $140 million, about seven times the earlier projection after adjustment for inflation [AE] (Ch 1, p. 24; endnote 16, p. 26).`

11. **L65 — Quantity: reversed participation bound.**  
    **Evidence:** p. 47 states **more than 25,000 people**, not “up to 25,000”.  
    **Exact fix:** replace `with up to 25,000 people` with `with more than 25,000 people`.

12. **L69 — Source-external addition: “kitchen-table”.**  
    **Evidence:** Osheroff’s sidebar, p. 54, describes an experiment initially performed on the Stanford Physics Department loading dock. It supplies no kitchen-table setting or label.  
    **Exact fix:** replace `his own kitchen-table experiment` with `his own experiment`.

13. **L77 — Factual/sequence: departure during manoeuvres asserted as established.**  
    **Evidence:** p. 63 says an attitude manoeuvre **possibly** imparted the departure velocity. The Board could not positively identify the object (§3.5 findings, p. 64).  
    **Exact fix:** replace the sentence with:  
    `An object was tracked in orbit with Columbia from 17 January until its decay; an attitude manoeuvre may have imparted its initial departure velocity. Exclusionary testing left an RCC panel fragment of approximately 140 square inches or greater as the matching candidate, although the Board could not positively identify the object [AE] (Ch 3, pp. 62–64).`

14. **L79 — Lost qualification: modelled breach size presented as reconstructed size.**  
    **Evidence:** p. 66 uses a ten-inch hole as an analytical example and expressly says the exact breach size will never be known and could have been smaller or larger.  
    **Exact fix:** replace `the Board reconstructs a breach of about ten inches in the lower RCC near panel 8` with:  
    `the Board analyses heating consistent with a breach near RCC panel 8, using an assumed ten-inch hole in one calculation; the exact breach size is unknown and may have been smaller or larger`.

15. **L83 — Citation locator.**  
    **Evidence:** both spare-panel and physics-based-model recommendations appear on p. 83. Page 84 contains endnotes.  
    **Exact fix:** change the final citation from `(Ch 3, p. 84)` to `(Ch 3, p. 83)`.

16. **L87 — Factual: wrong spilled substance.**  
    **Evidence:** “Hypergolic Fuel Spill”, p. 90, describes a **hydrazine** spill.  
    **Exact fix:** replace `a 1999 hydraulic spill` with `a 1999 hydrazine spill`.

17. **L87 — Lost qualification: crushed foam categorically ruled out.**  
    **Evidence:** F4.2-6, p. 90, says crushed foam **does not appear** to have contributed.  
    **Exact fix:** remove crushed foam from the categorical “ruled out” list and add:  
    `Crushed foam beneath the left bipod strut does not appear to have contributed to the loss of the ramp [AP] (Ch 4, p. 90).`

18. **L87 — Factual: permitted procedures converted into completed incidents; wrong page.**  
    **Evidence:** F4.2-13 and R4.2-3, p. 94, concern two closeout **processes able to be performed** by one person. The recommendation also covers intertank hand-spraying.  
    **Exact fix:** replace the closeout sentence with:  
    `Two final-closeout processes at Michoud could be performed by a single person, prompting a recommendation that at least two employees attend all final closeouts and intertank-area hand-spraying procedures [AP] (Ch 4, p. 94).`

19. **L87, L311 — Quantity/scope: planned and as-flown risk are not distinguished.**  
    **Evidence:** p. 94 gives an estimated risk of **1 in 370** and an actual as-flown value of **1 in 356**.  
    **Exact fix:** use:  
    `The micrometeoroid and orbital-debris critical-penetration risk was estimated at 1 in 370 before STS-107; its as-flown value was 1 in 356. The cumulative programme risk was calculated as 1 in 3 [AE] (Ch 4, p. 94).`  
    In L311 replace the value with `1 in 370 estimated; 1 in 356 as flown; about 1 in 3 cumulatively`.

20. **L99 — Quantity: lost lower bound.**  
    **Evidence:** p. 103 says government discretionary spending grew in purchasing power by **more than 25 percent**.  
    **Exact fix:** replace `discretionary spending rose 25 percent` with `government discretionary spending rose more than 25 percent in purchasing power`.

21. **L99, L309 — Metric: presidential requests labelled as budget amounts.**  
    **Evidence:** p. 104 distinguishes presidential requests, congressional appropriations and NASA operating plans. The cited $4.128 billion and $2.977 billion are requests.  
    **Exact fix:** in L99 use `the presidential budget request for the Shuttle fell from $4.128 billion in FY1993 to $2.977 billion in FY1998`. Rename L309’s metric `Shuttle presidential budget requests / purchasing power`; begin its value `$4.128bn requested for FY1993; $2.977bn requested for FY1998`.

22. **L101 — Factual attribution: O’Connor’s role at resignation.**  
    **Evidence:** p. 107 identifies Bryan O’Connor as head of the Shuttle Program at NASA Headquarters. His return as Associate Administrator for Safety and Mission Assurance was in 2002.  
    **Exact fix:** replace `NASA's top safety official objected that it was a safety issue and resigned` with `Bryan O'Connor, head of the Shuttle Program at NASA Headquarters, objected that the transfer was a safety issue and resigned`.

23. **Between L105 and L107 — Coverage: §5.6 omitted.**  
    **Evidence:** “A Change in NASA Leadership”, pp. 115–116, describes O’Keefe’s appointment and programme changes.  
    **Exact fix:** insert:  
    `**A change in leadership (Sec 5.6).** Sean O'Keefe replaced Goldin after November 2001. In 2002 he transferred Shuttle and Station programme management from Johnson to NASA Headquarters, considered contract expansion and competitive sourcing, and initiated workforce planning and comparisons with other high-risk enterprises. The November 2002 Integrated Space Transportation Plan redirected funding towards the Shuttle and Station, introduced the Orbital Space Plane as a complement, and envisaged Shuttle operation through at least 2010, with possible extension to 2020 or beyond [AE] (Ch 5, pp. 115–116).`

24. **L119 — Over-broad scope: absence of observation converted into absence of loss.**  
    **Evidence:** p. 123 says no right-bipod loss was observed on the **66 flights with suitable imagery**.  
    **Exact fix:** replace `while the right never did` with `while no right-bipod foam loss was observed on the 66 flights with suitable imagery`.

25. **L121 — Metric/scope: tile-damage superlative lacks its area basis.**  
    **Evidence:** p. 124 describes a **9-by-4.5-by-0.5-inch divot**, calling it the largest area of tile damage.  
    **Exact fix:** replace `which caused the largest tile damage in the programme's history` with `which left a 9-by-4.5-by-0.5-inch divot described as the largest area of tile damage in Shuttle history`.

26. **L121 — Lost uncertainty and incorrect locator: sample bias.**  
    **Evidence:** the sidebar on p. 124 says the apparent concentration on Columbia is **probably** a sample bias.  
    **Exact fix:** replace the final sentence with:  
    `A sidebar explains that five of the seven known events occurred on Columbia probably because of sampling bias: its umbilical-well cameras had imaged the bipod on 26 of 28 missions [AE] (Ch 6, p. 124).`

27. **L127 — Quantity/metric: dings counted as distinct tiles.**  
    **Evidence:** p. 127 reports **707 dings**, including 298 greater than an inch in one dimension; it does not report 707 distinct damaged tiles.  
    **Exact fix:** replace `damaged 707 tiles` with `left 707 damage dings, 298 greater than an inch in one dimension`.

28. **L127 — Metric: loss-of-Orbiter risk described as tile-loss risk.**  
    **Evidence:** pp. 129–130 describe the probability of **losing an Orbiter due to failure of Thermal Protection System tiles**. They also qualify the estimate by limited data and simplified assumptions.  
    **Exact fix:** replace the final sentence with:  
    `A 1990 probabilistic study estimated about a 1-in-1,000 probability per mission of losing an Orbiter because of Thermal Protection System tile failure, with debris-related problems accounting for approximately 40 percent of that probability. The Board notes that actual risk could differ because of limited data and simplified assumptions, and that NASA had not fully exploited the study's insights [BT] (Ch 6, pp. 129–130).`

29. **L127 — Citation locators for non-bipod events.**  
    **Evidence:** the quoted judgement about increasingly casual disposition of STS-56/58 and the STS-87 count of 308 hits appear on p. 129.  
    **Exact fix:** change the citation following that quoted judgement to `(Ch 6, p. 129)` and the citation following the STS-87 sentence to `(Ch 6, p. 129)`.

30. **After L127 — Coverage: “Impact Resistant Tile” subsection omitted.**  
    **Evidence:** p. 130 records existing impact-resistant tiles and their limitations.  
    **Exact fix:** insert:  
    `**Impact-resistant tile.** TUFI-coated AETB tile offered approximately 6–20 times the debris-impact resistance of current acreage tile, and at least 772 advanced tiles had been installed on Orbiter base heat shields and upper body flaps. Its higher thermal conductivity prevented its use as a replacement for larger areas of tile coverage [AE]. The Board also judged that next-generation tile certification would not adequately address debris threats unless impact requirements reflected specific probable damage sources [AP] (Ch 6, p. 130).`

31. **L137 — Structure: ordinary conclusion labelled a sidebar.**  
    **Evidence:** the risk-accumulation paragraphs are part of §6.2’s conclusion on p. 139, not a sidebar.  
    **Exact fix:** replace `The chapter's sidebar on risk states the mechanism` with `The section's conclusion states the mechanism`.

32. **L145 — Factual attribution: classification assigned to the wrong people.**  
    **Evidence:** p. 143 and F6.3-5, p. 171, attribute the out-of-family classification to United Space Alliance; the co-chair arrangement followed it.  
    **Exact fix:** replace the final sentence with:  
    `United Space Alliance categorised the strike as out of family, triggering the contractual co-chair arrangement [AE] (Ch 6, pp. 143, 171).`

33. **L145 — Lost qualification: photo group’s belief.**  
    **Evidence:** p. 142 says the group believed the Orbiter **may have been damaged**.  
    **Exact fix:** replace `the photo group believed there was damage` with `the photo group believed the Orbiter may have been damaged`.

34. **L147, L301 — Quantity: missing volume basis of the calibration ratio.**  
    **Evidence:** p. 143 explicitly makes the 640-fold and 400-fold comparisons **in volume**.  
    **Exact fix:** in L147 use `the debris was estimated at up to 640 times larger in volume than the calibration projectiles (the Board's best estimate is 400 times)`. Rename L301’s metric `Debris volume relative to Crater calibration`.

35. **L149 — Factual sequence/attribution: same-day e-mails and shared judgement.**  
    **Evidence:** pp. 147–148 reproduce Ham’s criticism dated 21 January and Dittemore’s response dated 22 January. His response says the matter is worth revisiting; it does not itself call the rationale poor.  
    **Exact fix:** replace `in e-mails the same day she and the programme manager called the STS-113 rationale poor` with `in an e-mail on 21 January she called the STS-113 rationale poor; the programme manager's response on 22 January said it was worth examining again`.

36. **L149 — Factual: wrong missed question to the crew.**  
    **Evidence:** p. 148 says ground personnel already had 35 seconds of downlinked footage. They failed to ask Brown for **additional footage**.  
    **Exact fix:** replace the final sentence with:  
    `Nobody asked David Brown whether he had additional External Tank separation footage beyond the 35 seconds already downlinked (Missed Opportunity 2) [AE] (Ch 6, p. 148).`

37. **L151 — Factual: second imagery request conflated with another route.**  
    **Evidence:** pp. 150–151 and the summary on p. 166 give the route: Bob White → Lambert Austin → Department of Defense Manned Space Flight Support Office. It did not pass through a Kennedy manager.  
    **Exact fix:** replace the second-request sentence with:  
    `The second imagery request began when United Space Alliance manager Bob White telephoned Lambert Austin at Johnson; Austin then contacted the Department of Defense Manned Space Flight Support Office [AE] (Ch 6, pp. 150–151).`

38. **L157 — Factual: interview responses placed inside the team meeting.**  
    **Evidence:** p. 157 says team members shrugged when **asked by the Board** what “mandatory need” meant.  
    **Exact fix:** replace the opening sentence with:  
    `The Debris Assessment Team put a rationale for mandatory viewing on its agenda; when later questioned by the Board, most members could not explain what "mandatory need" meant [AE] (Ch 6, pp. 156–157).`

39. **L157 — Factual: alternate trajectories wrongly described as unconsidered.**  
    **Evidence:** p. 160 says engineers found no alternate re-entry trajectory that would substantially reduce heating in the impact area.  
    **Exact fix:** replace `no alternate trajectory was considered` with `engineers reported that no alternate re-entry trajectory would substantially reduce heating in the general area of the foam strike`.

40. **L159 — Lost distribution qualification: favourable and adverse results treated alike.**  
    **Evidence:** p. 164 distinguishes wide circulation of favourable simulations from restricted circulation of the most unfavourable scenario.  
    **Exact fix:** replace `circulated their results widely` with `circulated favourable results to a wider Johnson audience, while sharing the most unfavourable scenario only with their management and selected Johnson engineers`.

41. **L176, L312 — Lost condition: consumables extension.**  
    **Evidence:** p. 173 makes Flight Day 30 depend on modified crew activity and sleep time to reduce carbon-dioxide production.  
    **Exact fix:** replace the consumables sentence with:  
    `With modified crew activity and sleep time, carbon-dioxide scrubbing could have supported a stay until the morning of Flight Day 30 (15 February) [AE] (Ch 6, p. 173).`  
    In L312 use `Hypothetical Atlantis launch on 10 February; modified crew activity and sleep time could extend consumables to the morning of Flight Day 30 (15 February)`.

42. **L199 — Over-broad scope and changed metric: Aerospace verification and failure figures.**  
    **Evidence:** p. 184 describes support for Air Force launch verification without asserting “every” launch. It labels 2.9 percent a **probability of failure**, rather than establishing an observed failure rate.  
    **Exact fix:** replace the Aerospace sentences with:  
    `The Aerospace Corporation provides independent launch verification for the U.S. Air Force and is not subject to schedule or cost pressures. The Board credits its involvement with reducing engineering errors and reports a 2.9 percent probability of failure for expendable launch vehicles, compared with 14.6 percent in the commercial sector [AE] (Ch 7, p. 184).`

43. **L276 — Quantity/scope: corrosion-inspection denominator and certainty.**  
    **Evidence:** p. 221 excludes the **tile-covered outer mould line** from the 90/10-percent division and says corrosion in the remaining portion **may remain undetected**.  
    **Exact fix:** replace the final sentence with:  
    `Approximately 90 percent of Orbiter structure, excluding the tile-covered outer mould line, can be inspected for corrosion; corrosion in the remaining 10 percent may remain undetected for the vehicle's life [AE] (Ch 10, p. 221).`

44. **L286 — Factual chronology: charter rewriting dated too early.**  
    **Evidence:** p. 232 says rewriting was **proposed during the first week**; the revised charter was signed and ratified on 18 February.  
    **Exact fix:** replace `the Board renamed itself and rewrote its charter in its first week to secure its independence` with `the Board renamed itself at the outset and proposed rewriting its charter during its first week to secure its independence; the revised charter was signed and ratified on 18 February 2003`.

45. **L288 — Over-broad disclosure claim.**  
    **Evidence:** p. 233 specifies exemption under the **Freedom of Information Act**, while providing for limited Congressional access under a special written agreement.  
    **Exact fix:** replace `were exempt from disclosure` with `were exempt from disclosure under the Freedom of Information Act; limited Congressional access was governed by a special written agreement preserving confidentiality`.

46. **L290 — Lost exception: Inspector General access.**  
    **Evidence:** p. 233 permits requested attendance **except at proceedings involving privileged witness statements**.  
    **Exact fix:** replace `the NASA Inspector General could attend its proceedings` with `the NASA Inspector General could attend proceedings on request, except those involving privileged witness statements`.

47. **L353 — Source-external factual addition: non-existence of STS-173.**  
    **Evidence:** the p. 127 caption supplies `STS-173`; it does not supply the assertion that this mission “did not exist”. The report also explains that mission designations and flight sequence differ, p. 27.  
    **Exact fix:** **strip** `, a mission that did not exist`. Retain the caption’s wording as a recorded source feature.

## 3. Count and required assessments

**531 audit units checked:** 508 evidence-marked claim spans, nine “positions framed against” entries, and fourteen substantive header/source-integrity blocks. Compound units were checked clause by clause; this is a span-based count, not a claim that the reference contains only 531 atomic propositions.

**47 numbered defects**, counted once under their primary class:

| Primary class | Count |
|---|---:|
| Quantity, metric, scope or lost qualification | 23 |
| Factual sequence or attribution | 11 |
| Citation locator | 4 |
| Structure | 3 |
| Coverage | 3 |
| Source-external addition | 2 |
| Provenance/count | 1 |
| **Total** | **47** |

No additional verbatim mismatches, unsupported cross-author connections, post-source vocabulary or task-application guidance were found. No separate evidence-marker correction is required after the substantive corrections above.

**Key-statistics table:** all eighteen rows have source anchors, but the table does not fully preserve the source’s meanings and qualifications. Rows **299, 301, 309, 311, 312 and 315** require the corrections above. The other twelve rows are source-supported.

**Source limitations:** there is no standalone author-limitations list to approve. The rescue-provenance note at L355 correctly identifies a post-accident NASA assessment. Several important qualifications need restoration, particularly breach-size uncertainty, observation limits and the consumables assumptions.

The source also expressly states limits that the reference does not collect: no detailed organisational prescription, p. 9; potentially unknowable precise foam-loss mechanisms, p. 53; fault-tree elements that may never be closed, p. 86; unevaluated transportation-plan and Orbital Space Plane requirements, p. 210; and public-risk-study uncertainty requiring later reassessment, p. 224. These are author-stated bounds, not grounds for adding an auditor’s methodological verdict.

## 4. Over-flag guard

- **Core thesis and organisational explanation:** clean. Equal causal weight, history as cause, normalisation, inverted burden of proof, hierarchy, weak signals and structural remedies are explicit Board claims.
- **Strong evaluative wording:** “seriously flawed”, “remarkably accurate”, “bureaucracy and process trumped thoroughness and reason”, and the “single most compelling reason” are source wording. They are not ingester-added judgements.
- **Nine opposed positions:** clean. The Board explicitly criticises each position; these are not invented oppositions derived from bounded positive claims.
- **Chapter coverage:** all eleven chapters and Appendices A–C have body anchors. The chapter-level TOC gate passes. Findings 8, 23 and 30 concern narrower omissions.
- **Section 6.3 finding numbers:** clean. The p. 171 render confirms F6.3-9 through F6.3-17 and supports the reference’s account of conversion loss.
- **Chapter 8 column joins:** clean. Renders of pp. 202–203 confirm the contractor-dependence sentence and the slippery-slope passage. The paraphrases preserve their meaning.
- **Seven bipod events and roughly ten percent:** clean. The reference distinguishes seven of 113 missions from the subset with suitable imagery.
- **Workforce figures at L101:** clean against p. 107’s narrative, even though the nearby workforce table has a different year alignment. This is not an ingester-created discrepancy.
- **84,900-pound recovery figure:** supported by Chapter 10 endnote 2, p. 224. Page 47 says “more than 84,900 pounds”; the report itself supplies both forms.
- **Recorded source inconsistencies:** the January 23 liftoff date, January 19/20 decay dates, STS-62 dates, Fishback/Fischbeck spellings, “principle metrics”, “independant”, and STS-33/51-L caption are present in the source. They should not be silently corrected as conversion errors.
- **Third-party material and markers:** the substantive `[V]` passages are Board prose. Borrowed frameworks and named connections are source-cited. Case-summary `[AE]` markers do not themselves claim experimental demonstration.
- **PDF absence and second-OCR statements:** treated as historical statements about the producing run. The audit package’s present PDF and the operator’s later OCR check do not establish that those historical statements were false.
- **Provenance:** title, date, ISBN, Board authorship, imprint and PDF checksum are supported. The quoted copyright designation is confirmed by the [NASA NTRS record](https://ntrs.nasa.gov/citations/20030093634).