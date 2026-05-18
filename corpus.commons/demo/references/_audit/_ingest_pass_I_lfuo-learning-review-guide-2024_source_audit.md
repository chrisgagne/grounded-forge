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
