# Pass I Audit Log — lfuo-learning-review-guide-2024

**Audit target:** `corpus.commons/demo/references/lfuo-learning-review-guide-2024-deep.md`
**Source:** US Forest Service, Risk Management Council & Office of Safety & Occupational Health (2024). *Learning From Unintended Outcomes and Learning Review Implementation Guide*. Revised April 2024. 98 pages. Public domain (17 USC §105).
**Source converted markdown:** `corpus.commons/demo/sources/converted/lfuo-learning-review-guide-2024.md` (5,170 lines covering all 98 pages of the PDF; body content from line ~415 through Recommended Reading at line 5170; TOC pages at lines 94–401 and inline page-number markers throughout).
**Auditor:** claude-opus-4-7[1m], xhigh effort, 9-pass protocol.
**Date:** 2026-05-13.

## Calibration

Read prior to cold-read:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical correction case).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control).

## Audit summary

| Bucket | Count |
|---|---|
| Total non-trivial claims audited | ~140 |
| Source-anchored, no fix needed | 138 |
| Claims stripped | 0 |
| Citations corrected in-place | 1 |
| Cross-corpus drift detected | 0 |
| Training-data leakage detected | 0 |
| Post-source vocabulary detected | 0 |
| Task-application guidance smuggled into deep | 0 |
| Verbatim accuracy slips | 0 |

The deep reference is ~370 lines for a 98-page operational guide. Every [V] marker corresponds to a verbatim quotation verified character-by-character against the converted markdown. One citation correction was applied; no claims were stripped.

## Citation corrections

### Correction 1 — line 17 (Author's-thesis third load-bearing claim, "Recommendations vs Lessons Learned")

The thesis paragraph attributed the "Recommendations vs Lessons Learned" section to `(Part 6, "Recommendations vs Lessons Learned")`. The source TOC (line 181) places this section on page 32, which falls inside Part 5 ("Initiating the FLA: Before the FLA Team Arrives and the early days", pages 23–34); Part 6 ("Engaging the process") begins on page 35. The remainder of the deep ref correctly cites this section as Part 5 in five places (the section heading in Part IV of the deep ref, plus four prose paragraphs and two "Positions framed against" entries). Fixed the line-17 citation from Part 6 to Part 5 for consistency.

## Verbatim-quotation spot-checks against the converted markdown

| Claim | Verified against source line(s) |
|---|---|
| "not only ineffective for improving safety related to a specific accident, but also damaging to the overall learning culture" | 482–484 |
| "valued learning opportunity and as a means to reducing uncertainty of future outcomes" | 472–474 |
| "It is impossible to predict all the potential situations that will arise in complex systems, and people are relied upon to make sense of these emerging conditions, learn in the moment, and innovate and adapt solutions to fit the situation" | (Part 1 opening prose, around line 422–426) |
| "make mistakes, but most of the time (almost continuously) they are actually creating safety" | 432–433 |
| "human performance variability is not only normal, it's the rule" | 573 |
| "In the criminal justice arena accountability means punishments and correction. In our Just Culture, accountability means creating the space for each person involved to provide an honest account..." | 531–533 |
| "An account is something you tell and learn from. Accountability is taking that story..." (Glossary, "Accountability") | 4772 |
| Accountabilism glossary definition | (Glossary entry following Accountability) |
| "Information is the lifeblood of safety. We must cherish it and protect it" | 1031–1032 |
| "Blaming employees can be a form of the Fundamental Attribution Error" | 1058–1060 |
| "FLAs must avoid causal statements" | 1659 |
| "Cause isn't something investigators 'find' or 'discover'; cause is always something we create by recreating the event..." | 3783–3785 |
| "In many circumstances, recommendations actually interfere with learning. Often recommendations, when implemented, add complexity to the workplace, which has the paradoxical effect of increasing risk" | 1671–1673 |
| Networked causality glossary definition | 4919–4924 |
| "Practitioners at the 'sharp end' (those workers who directly confront the risks of the workplace) are inheritors of policies, training programs, tools, culture, incentives, etc., that are the responsibility of those managers and administrators at the 'blunt-end'" | 3802–3805 |
| Dekker & Pruchnicki 2013 opening epigram ("Actions that are interpreted as 'bad decisions'...") | 2296–2299 |
| "Consensus is not the goal. Tension between individual team member's perspectives is valuable" | 2307–2308 |
| "Most often, the Lessons Learned Analysis will reveal that multiple improbable events were necessary for the accident to occur" | 2333–2335 |
| "You may find some of these 'hows' do not apply and some will be redundant. Use those that are helpful and don't waste time trying to cook-book the process" | 2377–2378 |
| "Storytelling is widely recognized by educators as the most effective tool for experiential teaching and leading cultural change within an organization" | 2477–2479 |
| "storytelling moves Lessons Learned into the vicarious experience of Lessons Lived" | 2456 |
| Dekker, Cilliers, Hofmeyr 2011 "respect otherness" quote | 2537–2541 |
| "Remember this is their story, not yours" | 2697 |
| "FLA teams must guard against making counterfactual arguments such as: 'If this person had done X...'" | 2859–2869 |
| "Illuminating the gap between work as imagined by administrators and work as actually accomplished will illuminate substantial and critical organizational vulnerabilities" | 2887–2891 |
| Reckless-and-willful-disregard threshold ("intentional, unjustifiable, and occurred with the foreknowledge that the conduct was likely to result in serious harm, death, or injury") | 3853 (Appendix C) |
| "FLAs are for the vast majority of events in which good people, doing what they thought made sense at the time, ended up in an unexpected situation" | (Appendix C, immediately after the threshold) |
| Analysis-vs-synthesis frame ("The machine metaphor is not as widely applicable as our culture seems to give it credit for"; "Life is an emergent property that cannot be fully examined through analysis"; "Synthesis is the process of trying to understand how emergent properties come to be") | ~3170–3192 (Part 10, "What is a Learning Review?") |
| Dekker 2014 *Field Guide* quote ("in complex situations, people must act based on uncertain, incomplete, and sometimes even contradictory information") | 3248 |
| LR analysis-applicable-to-mechanical-ergonomic-structural ("'analysis' is applicable only to objective information") | (Part 10, "How the learning review process examines...") |
| Organizational Learning Product / Field Learning Product framing | (Part 11, "Learning Review Products" through "Field Learning Product") |
| Slovic risk-as-construct quote ("Risk does not exist 'out there'...") via Kahneman footnote 12 | 4393–4397 |
| "the best definition of 'safety' is: the reasonableness of risk. It is a feeling..." | 4400–4402 (Handout A); 2055–2056 (Part 6, Ten Principles agreement #10) |
| "Risk Management is wholly concerned with managing risks, not outcomes. Risk management is counterintuitive" | (Handout A bullets) |
| Recognition Primed Decision Making definition ("a model people can use experience to generate a plausible option as the first one they consider") | 4949–4950 |
| ETTO definition ("If demands to productivity or performance are high, thoroughness is reduced...") | 4845–4846 |
| HRO five hallmarks (preoccupation with failure, reluctance to oversimplify, sensitivity to operations, commitment to resilience, deference to expertise) | 4881–4883 |
| Five HRO-style example questions in Handout D | (Handout D body around lines 4570–4630) |
| Paul Chamberlin "improve performance by capitalizing on the shared experiences of participants" | 2783–2786 |
| Thirtymile-Cramer-Esperanza arc ("Our employees were criminally prosecuted in the aftermath of the Thirtymile and Cramer fires...") | 3707–3717 |
| I-90 Tarkio Fire Entrapment first learning-focused investigation (2005) | 641 |
| Mann Gulch / Maclean's *Young Men and Fire* as canonical organisational-learning narrative | 593–594 |
| Pole Creek Bucket Extraction perspective-faithful storytelling case | 2553–2557 |
| Appendix E "CRITICAL" peer-participation guidance ("Don't try to save money or minimize the footprint of the team by cutting these positions") | 4084–4090 |
| Deflection-question worked examples (interviewer redirects to morning routine) | 1956–1992 |
| Ten Principles and Agreements for the group dialogue | 2025–2065 |
| "Listen for the silent voice" facilitator move | 2222–2231 |
| "Exploit points of departure" facilitator move | 2163–2174 |
| "Location, location, location" / "stage for the FLA performance" | 2119–2120 |
| "When 'we just need more training' comes up… Try to dig deeper" | 2211 |
| "Sharp end" / "blunt end" framing | 3802–3805 |
| Restorative justice paragraph ("After a serious accident, employees are often emotionally harmed, and relationships can be strained or broken... the FLA process seeks to restore victims to wholeness") | 545–551 (Part 1, "Just Culture") |
| Dekker & Breakey 2016 citation (Glossary "Restorative justice" footnote 14) | 4960–4963 |
| Hollnagel 2008 *Resilience Engineering Perspectives* citation (Appendix B footnote 11) | (Appendix B body) |
| Lisa Cron *Wired for Story* citation (Handout E footnote 13) | (Handout E body) |
| FLA team self-AAR after process closure ("It is helpful for FLA teams to reconvene... and to conduct an After-Action Review of their FLA experience") | 3000–3003 |

All quotations verified character-for-character against the converted markdown. The "Five Hows" graphic list and the Handout C "FLA Watch Outs" four-biases graphic did not extract as text from the PDF (they are visual elements in the source); the deep reference flags both gaps in the "Citation and source-integrity notes" section and references the surrounding prose, which is verifiable.

## Cross-claim verifications for the Part / Appendix / Handout citation taxonomy

| Section | Citation style used | Source page | Source Part |
|---|---|---|---|
| "Systems Thinking" | (Part 1, ...) | p. 9 | Part 1 |
| "Just Culture" | (Part 1, ...) | p. 9–11 | Part 1 |
| "Learning" / "What is organizational learning?" / "How we got here" | (Part 1, ...) | p. 11–13 | Part 1 |
| "The tools" (AAR/RLS/FLA/Learning Review) | (Part 2, ...) | p. 14–16 | Part 2 |
| "Starting the process" / "Questions to consider..." / "Learning beyond accidents" / "Administrative assurance of no punitive actions" | (Part 3, ...) | p. 17–20 | Part 3 |
| "Priority Delegating Official Actions" / "Forming the FLA team" / "Potential FLA team members and roles" / "A Common Operating Picture" / "Cooperation with Other Investigations" / "Recommendations vs Lessons Learned" | (Part 5, ...) | p. 23–34 | Part 5 |
| "Setting the stage" / "Site visits, Interviews..." / "Interviews" / "Principles and Agreements..." / "Suggestions to FLA Facilitator..." / "Sand Tables, Google Earth, and ArcMap" | (Part 6, ...) | p. 35–43 | Part 6 |
| "The Lessons Learned Analysis" / "The Five Hows..." / "A Process for conducting a Lessons Learned Analysis" | (Part 7, ...) | p. 44–47 | Part 7 |
| "Why FLA Storytelling?" / "Different Perspectives" / "Storytelling Basics" / "Validating Stories through the Readback process" | (Part 8, ...) | p. 51–55 | Part 8 |
| "Avoid Counterfactual Arguments" / "Display Misalignments..." / "Serious Crimes or Reckless and Willful Disregard..." / "FLA Learning Products" | (Part 9, ...) | p. 56–60 | Part 9 |
| "What is a Learning Review?" / "An overview of the process" / "How the learning review process examines mechanical, ergonomic and structural failures" / "The learning review process" / "Preparing to Hold the First Focus Group" | (Part 10, ...) | p. 61–66 | Part 10 |
| "Learning Review Board" / "Learning Review Products" / "Organizational Learning Product" / "Field Learning Product" / "Recommendations" | (Part 11, ...) | p. 67–71 | Part 11 |
| "A Deeper Dive Into Just Culture" | (Appendix A, ...) | p. 72–73 | Appendix A |
| "A Deeper Dive into Causal Factors" | (Appendix B, ...) | p. 74 | Appendix B |
| "Is an FLA the Right Tool?" | (Appendix C, ...) | p. 75 | Appendix C |
| "Restorative Justice Checklist" | (Appendix F, ...) | p. 80–81 | Appendix F |
| "Lessons and Advice for fla teams" | (Appendix E, ...) | p. 78–79 | Appendix E |
| "Understanding the Work Under a Just Culture" | (Handout A, ...) | p. 86–87 | Handout A |
| "FLA 'Watch outs'" | (Handout C, ...) | p. 90–91 | Handout C |
| "Two Different Styles for Dialogue Focused Questions" | (Handout D, ...) | p. 92 | Handout D |
| "Tips for Facilitated Learning Analysis Storytelling" | (Handout E, ...) | p. 93–94 | Handout E |
| Glossary entries ("Accountability"; "Accountabilism"; "Networked causality"; "Recognition primed decision making"; "Efficiency-Thoroughness Trade-Off"; "GAP"; "High Reliability Organization"; "Restorative justice"; "Retributive justice"; "Sensemaking"; "Storytelling"; "Systems Thinking") | (Glossary, ...) | p. 95–98 | Glossary |
| Hollnagel ETTO footnote 2 | (Part 3, footnote 2) | p. 20 | Part 3 |
| Hollnagel ETTO footnote 4 | (Part 5, "Recommendations vs Lessons Learned", footnote 4) | p. 32 | Part 5 |
| Dekker & Pruchnicki 2013 footnote 5 | (Part 7, footnote 5) | p. 44 | Part 7 |
| Dekker, Cilliers, Hofmeyr 2011 footnote 6 | (Part 8, footnote 6) | p. 52 | Part 8 |
| Dekker 2014 *Field Guide* footnote 8 | (Part 10, footnote 8) | p. 64 | Part 10 |
| Hollnagel 2008 *Resilience Engineering Perspectives* footnote 11 | (Appendix B, footnote 11) | p. 74 | Appendix B |
| Slovic via Kahneman footnote 12 | (Handout A, footnote 12) | p. 86 | Handout A |
| Lisa Cron *Wired for Story* footnote 13 | (Handout E, footnote 13) | p. 93 | Handout E |
| Dekker & Breakey 2016 footnote 14 | (Glossary, "Restorative justice", footnote 14) | p. 98 | Glossary |
| Roese & Vohs 2012 hindsight bias paper | (Recommended Reading, "Accident, Safety and Human Performance") | p. 100 | Recommended Reading |

All citations align with source structure. Note: the source's table of contents lists "Recommendations vs lessons learned" under Part 5 (page 32, between "Cooperation with Other Investigations" and "Human Performance Expertise"), and this attribution is now consistent throughout the deep reference after Correction 1.

## Cross-checks for the failure-mode catalogue

- **Training-data leakage.** No claims about Forest Service authors' biographies or careers were added. Sidney Dekker, Erik Hollnagel, Karl Weick, Kathleen Sutcliffe, Gary Klein, Daniel Kahneman, James Reason, Lisa Cron, Jonathan Gottschall, Norman Maclean, Paul Chamberlain are named only when the source names them, in the contexts where the source uses them. No external-knowledge biographical claims about any of these authors were imported. **Pass.**
- **Post-source vocabulary.** No introduction of concepts from outside the 2024 guide. The deep ref does not import Dekker's later vocabulary (e.g., "Safety Differently", "Safety-II") that does not appear in this source; it does not import Hollnagel's "resilience engineering" beyond what the source's footnote 11 itself names; it does not import Klein's "naturalistic decision-making" framework beyond what the Glossary's RPD entry says. The lineage note (Paul Chamberlain's original FLA → APA/FLA → FLA → combined FLA-LR (2020) → LFUO 2024) is sourced directly to the Preface (lines ~22–30). **Pass.**
- **Cross-corpus drift.** The deep ref's "Connections the author makes" section records only authors the source itself names — verified against the source's footnotes (Hollnagel ETTO at 1652, Hollnagel Resilience at 3829, Dekker & Pruchnicki at 2296, Dekker Cilliers Hofmeyr at 2537, Dekker Field Guide at 3248, Slovic via Kahneman at 4393, Cron *Wired for Story* at 4717, Dekker & Breakey at 4960), the Glossary's attributed entries (Isaacs at "Dialogue", Weick & Sutcliffe at HRO, Klein at RPD, Sinek at Appendix A footnote 10), and the Recommended Reading list (Dekker, Marx, Sharpe, Conklin, Reason, Kahneman, Roese & Vohs, Tavris & Aronson, Woods & Cook, Adams, Taleb, Gottschall, Isaacs, Garvin, Senge, Schein, Hollnagel, Jolly et al., Loudermilk et al., Scott & Burgan). No author was added to the connections section that the source does not cite. **Pass.**
- **Task-application guidance smuggled into the deep.** No diagnostic questions, no practitioner checklists, no phase-by-phase prescriptions in the deep tier. All such material is in the distillations (`lfuo-learning-review-guide-2024-decision-making.md`, `lfuo-learning-review-guide-2024-stakeholder-engagement.md`). The "Questions to Ask" sections in the distillations are clearly tagged as projections, not as source content. **Pass.**
- **Verbatim accuracy slips.** Blockquotes spot-checked character-by-character against the converted markdown for: the Ten Principles and Agreements (lines 2025–2065); the Dekker & Pruchnicki epigram (2296–2299); the Dekker, Cilliers, Hofmeyr diversity-of-narrative passage (2537–2541); the Slovic risk-as-construct passage (4393–4397); the Recognition Primed Decision Making definition (4949–4950); the ETTO definition (4845–4846); the Networked Causality definition (4919–4924); the Accountability and Accountabilism Glossary entries; the cook-book Five Hows instruction (2377–2378); the "their story, not yours" readback instruction (2697). All preserve the source's italicisation, capitalisation, smart-quote choices ('curly'), and exact wording. No "tidying" of smart-quotes-to-straight or capitalisation was introduced. **Pass.**
- **Silent partial coverage.** The deep reference flags two specific gaps in its "Citation and source-integrity notes" section: (1) the Five Hows list in Part 7 appears in the source as a graphic and did not extract as text; (2) the Handout C "FLA Watch Outs" four-biases-plus-a-way-of-thinking list appears in the source as a graphic and did not extract as text. Both gaps are named explicitly with the reader directed to the original PDF at `corpus.commons/demo/sources/original/lfuo-learning-review-guide-2024.pdf` for the visual lists. Image classification was deferred (text-only ingest) — flagged in the source.md sidecar and in the deep reference's coverage line. **Pass.**

## Gate decision

The deep reference passes Pass I and is cleared to ship. Light reference (`lfuo-learning-review-guide-2024.md`) and distillations (`lfuo-learning-review-guide-2024-decision-making.md`, `lfuo-learning-review-guide-2024-stakeholder-engagement.md`) derive from the audited deep and inherit the discipline by construction. Public-domain scope (17 USC §105) places no copyright propagation obligation on derivative artefacts.

## Open follow-ups

- **Image classification.** The Five Hows graphic (Part 7) and the Handout C "FLA Watch Outs" graphic both warrant visual classification when `ingesting-images` is next run against this corpus; both are SUBSTANTIVE candidates (framework graphics, not decorative).
- **Lineage note.** The Chamberlin/Chamberlain spelling discrepancy in the source (Preface uses "Chamberlain", Part 9 page 56 uses "Chamberlin") is preserved in the deep reference's "Connections" section with a note. The light reference and distillations use "Chamberlain" (the Preface spelling) per the source's primary usage.

## Scoped re-audit 2026-10-16: restored text

**Auditor:** claude-opus-5-5, fresh subagent, fix-in-place mode. A blind cross-family leg (codex) runs in parallel on a frozen copy; this leg did not read it. The driver stamps once every leg is done; this leg leaves the stamp and every "Pass I has not run." line alone.

**Scope.** Only the text restored by the 2026-10-16 re-conversion (PyMuPDF text blocks, `sort=False`) and the deep-reference text written for it: the 114 lines added or changed in the deep reference since `origin/main` (`git diff origin/main`), holding 206 `[V]` and 86 `[AP]`/`[AR]`/`[AE]`/`[BT]` markers plus their unmarked framing sentences. Everything else is unchanged since the 2026-05-13 audit above and was not re-audited.

**Coverage.**
- Deep reference: read in full, 504 of 504 lines.
- Tape: every dispatched range read in full (8–78, 353–407, 421–511, 539–614, 633–699, 776–856, 886–945, 973–1009, 1042–1085, 1093–1249, 1314–1376, 1467–1498, 1507–1590, 1671–1703, 1733–1785, 1802–1826, 1854–1909, 1937–1977, 1991–2020, 2039–2075, 2106–2174, 2200–2235, 2265–2300, 2330–2363, 2415–2446, 2474–2628, 2636–2673, 2705–2740, 2771–2796, 2909–2937, 2943–3005, 3074–3117, 3167–3203, 3273–3358, 3401–3425, 3432–3456, 3593–3617, 3903–3927, 4025–4146, 4195–4400, 4401–4873, 4874–5038, 5066–5106, 5185–5227). Out-of-range checks were greps (lines 1386, 1639, 3249, 5138, 5297–5305).
- OCR: `ocr-pdf-p77.txt`, `p78`, `p87`, `p88` read in full.
- Renders (7 of 10 allowed, all succeeded): PDF pp. 22, 46, 58, 59, 87, 88, 91. Page numbers were confirmed with `pdftotext -f N -l N` before rendering.

**Calibration.** Read fixtures 01, 07 and 12 before the cold read.

### Counts

| | |
|---|---|
| Claims audited (in-scope marked claims plus framing sentences) | ~300 |
| Source-anchored as written | all but the 10 below |
| Stripped | 0 |
| Corrected (claim reworded to what the passage says) | 8 |
| Marker-corrected | 1 |
| Quotation-corrected | 1 (Salt Fire caption, quoted in full in place of a fragment credited to the wrong speaker) |

### Changes made (current line numbers)

1. **L9 (Coverage), L432 (Part XVII), L500 (integrity notes): caption misattribution.** The render of PDF p. 91 shows that the excerpt "The wind is gusting and they feel a wave of heat on their backs as they pass campsite 5…" sits in a box captioned "2011 Pagami Creek Fire Entrapments Faciliated Learning Analysis". The image-held quote ("I knew right then…", credited to "Ashley") sits above the "2018 Horse Park Fire Entrapment" caption. The converted text puts the Horse Park caption directly before the Pagami Creek excerpt, and the deep reference had the two swapped in all three places. Corrected: the excerpt is now credited to Pagami Creek, the image-held quote to Horse Park, and L432 says where the pairing was read.
2. **L21 (thesis).** "The guide frames all four claims with two epigraphs" put the reference's own four-claim thesis structure on the source. Changed to "The guide opens with two epigraphs before its Preface".
3. **L25 (front matter).** "carries a participant's words, 'Get in This Truck!'": in the source, a voice the speaker heard said those words. Replaced with the full caption quote, "I got behind the safety shelter; then in a little bit, I heard a voice say, Get in This Truck!" [V] (tape 55–59), and "from" became "credited to".
4. **L83 (Part III).** "The facing page carries…": the source does not establish a facing-page layout. Changed to "The next page carries…" (tape 1132–1153).
5. **L111 (Part IV). Marker correction.** The December 2014 analysis sentence was marked `[V] [AR]`. It is a verbatim report of a finding, not the author's argument, so `[AR]` was removed and `[V]` kept.
6. **L121 (Part IV, data sidebar).** "a form, developed with Joint Fire Science Program Project 18-S-01-1 and the Wildland Fire Histomap project": the source says research needs were "established" in conjunction with those projects. It does not say the form was developed with them (tape 1574–1587). Reworded, and the "Learning Through Work" link named.
7. **L144 (Part IV).** "A boxed section closes Part 5" contradicted the unchanged L142, "Part 5 closes on human performance expertise". Changed to "A boxed section follows it". Gregg Creek still comes after the box in the source.
8. **L376 (Part XIII, Appendix D).** The eight-step oral briefing was described as "each with a worked example". Step 8 has a note on timing, not an "Ex." (tape 4132–4134). Changed to "the first seven with a worked example and the last with a note on timing".

### Checked and confirmed (no change)

- **Part 4 graphic (L87–95).** Render of p. 22: circles 1–7 match the deep reference's order (AAR RLS FLA LR; Initiate; Interact; Bringing it all together; Readbacks; Brief Delegating Official; Learning Review Process).
- **Five Hows (L208).** Render of p. 46: five boxes in a ring around the stem. The converted order runs clockwise from the top, so "the order given here is the converted text's, not a sequence the source sets" is accurate.
- **LR outline (L276).** Render of p. 59: boxes joined by arrows, in the deep reference's order.
- **Handout C (L301–307).** Renders of pp. 87–88 confirm the five headings (Confirmation Bias, Fundamental Attribution Error, Outcome Bias, Hindsight Bias, Counterfactual Thinking). The three `[AP]` boxes match the OCR. The FAE and counterfactual `[V]` quotes match the tape.
- **Appendix F (L389–399).** Every `[AP]` statement was checked against `ocr-pdf-p77.txt` and `p78`: the five question sets, the parties and needs, restorative vs retributive, the five reasons to avoid a retributive culture, forgiveness, the goals, "If you fire someone, what have you fixed?", and the Dekker credit with "Public Domain".
- **Integrity note (3).** Render of p. 58: the "Dynamics of Influence & Change" graphic's text box says "Our goal is to understand the internal and external pressures that influenced decisions and actions", as described.
- **Appendices G/H, Handouts A/B/D/E, Glossary pull quote, Connections and Positions additions.** Traced line by line; no defect.

### Verbatim report

- **Before and after the fixes:** 64 apostrophe, 16 initial, 2 near, 3 page, 2 interrupted, 3 missing. The new Salt Fire quotation passes.
- **Known noise, as the dispatch notes:**
  - L39, L109 and L255 report `missing`: the quotation runs past a box at the foot of a page.
  - L51, L61 and L196 report `page`: a page number falls inside the quotation.
  - L79 reports `near`: "101- 37".
  - L280 reports `interrupted`: "ergonomic7".
  - L453 reports `interrupted`: footnote 14 falls inside the quotation.
- **Out of scope, noted only:** L338 (`near`, the May text) ends its quotation with "variability)". The source carries footnote marker 11 after "variability". It was not re-checked here.

### Derived tier: claims to re-derive

None of the changed claims is carried by the light reference or the distillations. A grep of all five LFUO distillations, the light reference and the three named index files found no mention of Horse Park, Pagami Creek, the Salt Fire caption, the data sidebar or Histomap, the "facing page", the epigraphs "framing" the thesis, or the Appendix D "each with a worked example". The December 2014 analysis appears in the AAR distillation (concept 18), the software-business distillation (concept 15) and the light reference, all without the `[AR]` marker, so the marker correction does not reach them. Re-stamp the derived tier against the new deep hash once the driver stamps.

### Open, for the parent

- **Possible derived-tier over-reach (not edited; derived tier is read-only here).** The retro distillation's new question row says Handout D's six questions are "phrased as how and what rather than why (Handout B)". Handout D's question 4 asks "Why did you do it? … Why didn't you do it?" The source does not reconcile Handout B's "Never ask WHY" with Handout D's questions, so the merge is the distillation's own. It should be labelled as an application, or the "why" questions reworded with that label.
- **Cross-family leg.** This leg is same-family. The gate decision waits on the codex leg's sort.

### Apply leg: sort's remaining edits and the derived tier

**Auditor:** claude-opus-5-5, apply leg. Read `sort.md` and `blind-findings.md` in full; checked each remaining edit against the tape and, for Appendix F, a render of PDF pp. 77–78 (2 renders, both succeeded).

**Sort result.** 20 confirmed defects: 6 fixed by this leg's fix-in-place pass, 1 fix incomplete (L142), 12 missed by it (1 in the deep reference, 11 in the derived tier or source card), plus the retro adaptation it left open. 0 over-flagged by either auditor; 1 disputed (L83 "facing page"; the "next page" wording stands). Gate: pass once the two remaining deep edits are applied.

**Deep reference.**
1. **L391 (Appendix F), applied with changed wording.** "It asks five sets of questions, each marked no or yes" described the checklist as binary. The render of p. 77 shows each line as a bar running from NO to YES; p. 78's "Guidance for Use of Restorative Just Culture Checklist" says "On the checklist, mark where you think you are … Together, the marks reveal what you still need to do" (OCR p. 78). Now: five headings, each line running from NO to YES, users marking where they think they are so the marks show what is still to do [AP], citing both sections and PDF pp. 77–78. The sort's wording ("response lines anchored NO and YES") was tightened to the guidance's own sense.
2. **L142 (Part IV), applied as written.** "Part 5 closes on human performance expertise" became "Part 5's final titled subsection concerns human performance expertise". The transition box and the Gregg Creek sidebar follow it before Part 6 (tape 1853–1901).

**Verbatim report after the fixes:** unchanged at 64 apostrophe, 16 initial, 2 near, 3 page, 2 interrupted, 3 missing; every flag is the known noise listed above.

**Derived tier.** The fix-in-place pass found none of its changed claims in the derived tier. The sort's confirmed derived defects and two kindred narrowings were corrected:
- Light reference: "conditions … are the basis" → "often form the basis" (tape 826–827), and the paragraph moved out of the middle of the four-tool list; "reports avoid names" → "typically avoid" (tape 3181); "don't edit sentences as a group" → be wary of sentence-level group editing, save polish for the final draft (tape 4987–4990); the facilitator-moves sentence and signature position 13 now carry all three readings of early agreement (tape 2342–2351); "Two epigraphs frame the guide" → "The guide opens with two epigraphs", matching deep L21.
- AAR distillation: the dialogue-questions row now ends at "What might we do differently?" (tape 4858–4861); the fusion question and the "whole group agrees early" diagnosis carry all three readings.
- Retro distillation: the data-gathering row ends at "What might we do differently?" and labels the how-and-what recasting of Handout D's why questions as the distillation's application after Handout B; the fusion question and diagnosis carry all three readings.
- Software-business distillation: the note-taking advice in the signed-statements row is credited to Handout B.
- Stakeholder distillation: "Handout C's full watch-out list is a graphic in the PDF" was stale; it now names the five watch-outs and the permission to call out biases.
- Indexes: AAR-DISTILLATION-INDEX.md's Handout D row and RETRO-DISTILLATION-INDEX.md's Handout D and fusion rows corrected to match.

check-verbatim on each edited derived file: apostrophe, initial and one out-of-scope `page` flag only.

**Open.** The source card (`sources/original/lfuo-learning-review-guide-2024.source.md`) still says "no OCR required" (L24), "stays PARTIAL until" (L28), and calls the guide "the current canonical iteration" and "the current production guide" (L20); the sort confirms all three. Not edited here: the source card is outside this leg's scope.


### Gate settlement (2026-10-16, orchestrator)

The apply leg passed the gate with two open items, both settled against the source before `--accept-gate`:

1. **Source card.** Three stale or unsupported claims corrected: "current canonical iteration" and "current production guide" now read "the latest iteration the source describes" and "the later revision", since the source gives only the April 2024 revision and its lineage. "No OCR required" now records the image-held text (three Handout C boxes, Appendix F). The PARTIAL sentence now records the 2026-10-16 coverage.
2. **Appendix F "Others" line.** A render of PDF p. 77 shows an "Others — please specify" line under each of the first three headings. Added to Part XIV's first bullet.

The sort's one disputed item (the "facing page" wording for PDF pp. 20–21) had already been changed by the apply leg to "The next page"; it needed no further edit.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `fa3bb6b432f33a9cf1963d4dfc284490a78383d389c966318fa90527d93b99c9`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `393394a19e4bb4fca8a2e437ac8604150e248a88ff836e90888ddb7617b91ddf`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_lfuo-learning-review-guide-2024_crossfamily_blind.md`, `_ingest_pass_I_lfuo-learning-review-guide-2024_crossfamily_sort.md`, `_ingest_pass_I_lfuo-learning-review-guide-2024_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 20 defects (6 fixed, 1 fix incomplete, 12 missed by the fix-in-place audit: 1 in the deep reference and 11 in the derived tier or source card, plus 1 retro adaptation it left open), found 0 over-flagged by the blind auditor and 0 by the fixer, left 1 disputed (L83 "facing page"), and gave a PASS verdict once two remaining deep edits are applied.

**Remaining edits applied (2026-10-16):** Of the two remaining edits, one was applied as written (L142, Part 5's final titled subsection) and one with changed wording (L391, Appendix F: each line runs from NO to YES and users mark where they think they are, per the p. 78 guidance and the p. 77 render), and none was declined.

**Gate:** accepted by operator. Deep reference sha256 `4c4f07ef96c5467dc3962f51d6099d7f03f3131e5a5888285b194c4a36e094eb`, stamp included.

## Derived-tier fidelity check (2026-10-16)

Fidelity check of the derived tier for the restored text (2026-10-16). Checked about 184 claims against the audited deep reference: about 95 light-reference additions, about 38 in the aar distillation, 23 in retro, 15 in software-business, 5 in stakeholder-engagement and 8 index rows. The decision-making distillation had nothing in scope. Fixed 11. Five restored dropped hedges or a quoted qualifier: "most" FLAs focus on the scene (light reference and software-business concept 15), "very often" for false memories, "generally" for one lead interviewer, and the deep reference's "RMO" in place of an expansion it does not carry. Four removed a quotation the deep reference lacks, Handout C's "permission to call out any biases they see", from aar concept 19, the aar Phase 2 row, retro concept 13 and the stakeholder Phase 3 row. One moved a claim to its own anchor (aar concept 7, Lessons Learned Analysis), and one corrected the light reference's Dekker citation to the 2008 *Just Culture: Who Gets to Draw the Line?* quoted in the restored Part 1 box. Index rows needed no change. check-verbatim on each edited file shows only apostrophe, initial and one known `page` flag. No errors were found in the deep reference; its omission of the Handout C instruction, which predates the restored text, is recorded in `fidelity-deep-defects.json`.

### Post-stamp addition (2026-10-16, orchestrator)

The fidelity check recorded one omission in the deep reference (in `fidelity-deep-defects.json`): Part X did not carry Handout C's opening instruction. The passage predates the restored text, but the derived tier had quoted it. Added to Part X as [V] (tape L4733–4735, "FLA 'Watch outs'"), checked with check-verbatim, and the derived tier restamped against the new hash. The derived tier still carries no quotation of the sentence; the fidelity check's removals stand.
