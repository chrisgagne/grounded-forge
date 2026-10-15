# Pass I source-only audit: OpenStax, Organizational Behavior

**Auditor:** fresh claude-opus-5-5 subagent (fix-in-place leg)
**Audit date:** 2026-10-15
**Subject:** `corpus.commons/demo/references/openstax-organizational-behavior-deep.md` (778 lines; all 778 read, in four consecutive chunks)
**Source:** `corpus.commons/demo/sources/converted/openstax-organizational-behavior.md` (32,934 lines, including the four Ch 12 spans restored from the original PDF with pdftotext on 2026-10-15)
**Line numbers** below are as read, before the Pass I stamp was inserted at line 2; add 1 for the stamped file.
**Second leg:** not yet run. Treat this reference as audited but unverified until a cross-family blind audit and sort is done.

## Procedure

Read the Pass I section and failure-mode reference of `.claude/skills/ingesting-resources/9-pass-protocol.md`, the three calibration fixtures (01, 07, 12), and the 2026-10-15 quotations log. Ran `scripts/check-verbatim.py` before the read; its report was the quotation work list. Read the deep reference in full, then traced every prose claim, list, table cell, marker and cross-reference by grepping the source for its distinctive words and reading the passage around the hit. Ch 12.7, 12.8 and 12.9 (deep-ref lines 402–430) were traced sentence by sentence against source lines 18710–19189, including the restored spans and Table 12.1. Re-ran the checker at the end.

## Counts

| Dimension | Count |
|---|---|
| Claims audited (sentences, list items, table rows, markers, connection and position bullets) | about 470 |
| Source-anchored without change | about 427 |
| Claims corrected (wording changed to match the source) | 27 |
| Claims stripped (in whole or in part) | 5 |
| Evidence markers corrected | 10 |
| Quotations corrected | 1 |
| Total edits | 43 |

Checker before: 6 apostrophe, 4 initial, 2 interrupted, 1 missing. Checker after: 7 apostrophe, 5 initial, 2 interrupted, 0 missing. The extra apostrophe and initial lines come from quotations newly marked `[V]` (lines 241, 450) and need no fix. The two `interrupted` lines (59, 93) are page headers inside the quotation: conversion noise, not a defect.

TOC-vs-anchors: all 19 chapters and Appendix A are anchored in the body. Pass.

## Ch 12.7–12.9 (new sections): trace result

The new sections are well grounded. Every quotation matches; the restored "You Are Now the Leader" and "Uber’s Need for an Ethical Leader" features are summarised accurately; endnotes 91 (Gardner et al.), 101 and 102 (Pillai, Schriesheim and Williams) support the `[BT]` attributions at lines 410 and 422.

**Table 12.1 (line 406).** The converted table loses its header row (it reads "Supportive or Neutralizer | Leader Behavior Influenced Substitute Instrumental Leadership Leadership | Col3"). Reading the rows by empty and filled cells, every placement in line 406 matches: experience/ability/training, structured task, feedback by task, formalisation (substitute) and inflexibility (neutraliser) fall in the second (instrumental) column only; intrinsically satisfying task in the first only; "professional" orientation and cohesive work group substitute in both; indifference to rewards, low position power and a leader located apart neutralise both. The printed header wording ("Substitute Leadership", "Instrumental Leadership") rests on the dispatch's page-render check; the original PDF is not in this worktree or the main checkout, so it was not re-checked here.

Three wording fixes in these sections (lines 412, 418, 430; see below). Ch 12.6 note: the deep ref covers Fiedler but not House and Evans's path-goal theory or the cross-cultural context, both of which Ch 12.6 treats at length (source lines 18570–18705). Left open; see "Open items".

## Changes, by line

### Stripped

| Line | Claim removed | Reason |
|---|---|---|
| 15 | "managers who treat employees as interchangeable units misread their organisations" | No passage says this; replaced with "each carries implications for how employees are managed". |
| 372 | "*charismatic* power is its near-synonym" (referent power) | Not in the French-Raven list; the source links charisma to legitimate power. |
| 718 | "across 60+ countries" (TEA row) | The source gives no country count; now "across GEM economies". |
| 728 | Ch 17 in "French and Raven ... cited in three chapters (12, 13, 17)" | French and Raven appear only in Ch 12.3 and Ch 13.1. |
| 749 | Ch 17.1 and "approvingly across multiple chapters" (Drucker) | Drucker is quoted in Ch 11.4 and Ch 15.5 only. |

### Markers corrected

| Line | Change | Reason |
|---|---|---|
| 85 | [AP] → [V] | Quoted text is verbatim (Ch 3.4). |
| 167 | [V, list verbatim from source] → [AP] | The 15 characteristics are summarised, not quoted. |
| 225 | [AP] → [V] | McClelland quotation is verbatim. |
| 241 | [AP] → [V] | Self-efficacy quotation is verbatim. |
| 274 | [V, paraphrased list] → [AP] | Lawler's conditions are paraphrased. |
| 280 | [V, list] → [AP] | The incentive test is paraphrased; also "diagnostic" → the source's "simple test". |
| 286 | [AP] → [V] | Group definition is verbatim. |
| 450 | [AP] → [V] | Simon gloss is verbatim. |
| 594 | [V, list with percentages] → [AP] | List is reworded; the numbers stand. |
| 596 | [V, list] → [AP] | List is reworded. |

### Quotation corrected

| Line | Change | Reason |
|---|---|---|
| 484 | Quotation now starts at "as using collaboration"; "a self-serving asymmetry" replaced with the source's own words, "had flattering portraits of their own willingness to satisfy both sides in a dispute" [V]; section anchor added. | Checker reported `missing`: the quotation crossed a page header between "described" and "themselves". "Self-serving asymmetry" was the deep ref's label, not the source's. Closes the open item from the quotations log. |

### Claims corrected

| Line | Was | Now | Reason |
|---|---|---|---|
| 17 | "cultures that fit the environment outperform those that do not"; mechanistic/organic "the central design choice" | structure should fit environmental complexity and change; culture helps the organisation adapt to and integrate with its environment; the distinction "recurs in both chapters" | No passage says fitting cultures outperform; "central" is an evaluative label. |
| 35 | 21st-century manager "is predicted to need" | "Citing Fast Company's prediction" | The source attributes the five skills to Fast Company. |
| 85 | SIP "a sophisticated variant"; "Research supports both" | "a more complicated variant"; both views "have merit" | Source wording. |
| 91 | MSQ "the dominant instrument" | "one of the most popular instruments" | Source: "One of the most popular". |
| 155 | heterogeneous groups outperform "by week 17" | intervals 1–2 vs 3–4 (13 and 17 weeks), with no significant overall difference later | Matches the Watson passage; the old wording implied an overall reversal. |
| 161 | integration-and-learning "the strongest fit with firm success" | "strongly links the group's diversity to the firm's success" | The source describes what the perspective links, not a ranking. |
| 179 | EI "supports the toggle between systems" | the text describes EI as "a toggling between emotions and logic" | The source's toggle is emotions/logic, not reflective/reactive systems. |
| 232 | "The signature SDT claim" | "SDT researchers have consistently found" | Evaluative label; source wording. |
| 240 | goal hazards included "goal conflict" | Locke's cautions as listed: neglect of other areas, unintended consequences, impossible goals, quantified measures, individual goals in teams | "Goal conflict" is not among them; two cautions were missing. |
| 292 | Ch 9.1: "groups can regress to earlier stages when membership changes or scope changes" | Ch 9.1 stresses Tuckman does not claim all groups follow the sequence | The regression point is in Ch 10.2, not Ch 9.1; moved there (line 324). |
| 296 | role conflict etc. "discussed at length in Ch 18" | "named and deferred to later study; they return as stressors in Ch 18.2" | The source says only "reserved for later study". |
| 324 | (added) | stages are not linear; a new member or a confusing new task can cause a slide back (Ch 10.2) | Relocated from line 292 with the source's two triggers. |
| 336 | managerial intervention "(last resort)", exit "(very last resort)" | "(to be used sparingly)", "(last resort)" | Source wording. |
| 412 | "argues from press sources [BT, Hakim; Yakowicz; Kauflin]" that a manager title is an opportunity to lead | the opportunity claim attributed to Keating via Hakim [BT, Hakim] | Only the Hakim-sourced passage makes that claim. |
| 418 | "Transactional leaders, often those who subscribe to ..." | "Leaders who subscribe to ... are often described as transactional" | The source runs the inference the other way. |
| 430 | resistance "because existing paradigms frame perception" | "uncertainty breeds resistance, and existing paradigms frame perception and are not easily thrown away" | The source ties resistance to uncertainty. |
| 568 | Lewin "Best for stable contexts" | "Most understandable when the organisation is assumed to be generally stable, a context the text calls increasingly rare" | "Best for" overstates the source. |
| 588 | merit rating "expanded by GE under Jack Welch in the 1980s into forced-ranking" | from 1981 Welch championed forced ranking at GE, "another military creation" | Forced ranking is not presented as an expansion of merit rating. |
| 594 | "The 2011 SHRM study found" | "A 2011 SHRM article by Stephen Miller reports" | Source wording. |
| 660 | managerial ability and technical knowledge "are equally necessary" | entrepreneurs "also need" both | "Equally" is not in the source. |
| 732 | "Hersey-Blanchard situational theory" as a Ch 12.6 connection | Fiedler and House-Evans path-goal are the two theories explored; Hersey and Blanchard's "life cycle theory" is only listed | The source names it once, under a different label. |
| 733 | Lewin and Kotter "change management classics" | "one of the first and one of the most widely used" | Evaluative label; source wording. |
| 755 | equality vs equity argument credited to equity theory (Ch 7.4) | expectancy theory, weak E2s (Ch 7.3) | The passage is in the expectancy-theory section. |
| 757 | position "Stereotyping as factual baseline" | "Stereotyping in employment decisions", with the source's definition and quotation | Invented opposition: no passage frames against stereotypes as a baseline. |
| 760 | position "Treating culture as soft / non-strategic" | "Strategy as more influential than culture", with the text's gloss of Drucker | Invented opposition; the source's contrast is culture vs strategy. |
| 764 | 32,852 lines | 32,934 lines, including the restored Ch 12 spans | Current file. |
| 770 | "skips ... footnote 46 in Ch 15.5" | footnote 46 is fused to the next word ("46Culture"); footnote 15 in Ch 4.3 has no marker | Marker 46 is present at source line 23453. The source card carries the same "skips" wording; not edited (out of scope). |
| 776 | distillations "(decision-making, stakeholder-engagement)" | all five: aar, decision-making, retro, software-business, stakeholder-engagement | Current distillation set. |

## Checked and left as is

- Line 143: Cox and Blake "six potential competitive advantages" lists five. The source says "Six opportunities" and lists five; the deep ref reproduces the source.
- Line 324: "Katzenbach-Smith" performance curve; the source misspells "Katzenberg" here.
- Line 280: "Rucker" for the source's "Ruker Plan"; spelling only.
- Integrity notes on the conversion path (markitdown failure, Option B, OpenStax API field) are process provenance, not source claims.

## Open items

1. **Ch 12.6 path-goal theory and cross-cultural context not covered.** Both are substantial in the source (lines 18570–18705). The chapter is anchored, so the TOC gate passes; adding them is a synthesis decision for the parent.
2. **Smaller sections without body coverage:** Ch 13.4 ("Limiting the Influence of Political Behavior"), Ch 18.4 ("Coping with Work related Stress"), Ch 19.4 ("New Venture Financing"). Chapter anchors exist; noted for completeness.
3. **Source card wording** on footnote 46 ("skips") should match the corrected deep-ref note; the source card is outside this audit's edit scope.
4. **Second leg** (cross-family blind audit and sort) not run.
5. **Derived tier** needs re-derivation; see the parent's report for the edits that change claims the light reference or distillations carry.
