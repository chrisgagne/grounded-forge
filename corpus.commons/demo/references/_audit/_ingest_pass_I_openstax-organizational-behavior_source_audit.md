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

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** fresh claude-opus-5-5 subagent (fix-in-place leg). Same-family audit only: no cross-family leg was run, so these paragraphs are audited but unverified.
**Audit date:** 2026-10-17
**Subject:** `corpus.commons/demo/references/openstax-organizational-behavior-deep.md` (907 lines). Line numbers below are current; no edit added or removed a line.
**Source:** `corpus.commons/demo/sources/converted/openstax-organizational-behavior.md` (32,177 lines; PyMuPDF text blocks, re-converted 2026-10-16), with `corpus.commons/demo/sources/original/openstax-organizational-behavior.pdf` in the main checkout for label checks.

### Scope

Only the deep-reference text written on 2026-10-17 for the spans the re-conversion restored: lines 10, 24, 34, 36, 52, 58, 64, 70, 82, 94, 116, 135, 150, 152, 162, 170, 172, 202, 206, 212, 239, 249, 259, 275, 288, 292, 298, 302, 314, 315, 321, 339, 365, 375, 387, 391, 393, 401, 403, 407, 413, 415, 433, 437, 443, 513, 523, 525, 539, 541, 545, 547, 553, 555, 559, 565, 585, 587, 597, 605, 649, 680, 684, 695, 697, 705, 719, 723, 754, 756, 764, 785, 807, 815, 899 (the changed ranges in `git diff origin/main`). Where a 2026-10-17 edit extended a pre-existing paragraph (lines 288, 315, 391, 401, 523, 545, 585, 754, 899), only the added clauses were in scope. Everything else was audited on 2026-10-15 and was not re-read.

### What was read

- The Pass I section and failure-mode reference of `.claude/skills/ingesting-resources/9-pass-protocol.md`; fixtures 01, 07 and 12.
- Every scoped deep-reference line, in full.
- The whole restored-span extract (`ob-extract.md`, 2,947 lines, every `===== L{a}-{b}` block) and, for each new paragraph, the whole box or passage in the tape from title to sources, including the parts the old conversion already held: all 56 feature boxes (title through sources and questions), the chapter-intro or body text a paragraph draws on (Ch 2.1 Mahon sentence, Ch 2.4 lead-in to "Personality Clash", Ch 2.5 basic-conflict text before Kayak, Ch 3.2 Table 3.3 lead-in and follow-up, Ch 6.4 lead-in to Nadella, Ch 13 and Ch 19 intros), and the body and table spans listed on the Coverage line (Tables 2.1, 2.2, 8.2, 13.1, 13.3, 14.3, 17.1; Kolb and Silberman; expectancy model and footnote 2; Gabarro; Ch 10.6 interventions, cultural intelligence and Lee and Liao practices through "cognitive complexity"; Ch 11.2 types of communication; Ch 13.1 ignoring; Ch 13.3 Hickson; Ch 14.3 prevention; Ch 18.3 social support). Front matter "Contributing Authors" was read for the Hartmann claim.
- Labels: every box title was located in a pdftotext dump of the original PDF and the ALL-CAPS label on the same page read; each box page carries exactly one feature label. Two pages were rendered (PDF pp. 112 and 416) while finding the page offset; the label checks themselves rest on the text dump. No tape damage was found that needed a render.

### Verbatim check

Before: 7 apostrophe, 5 initial, 2 interrupted (all in pre-existing text). After: the same. All 75 `[V]` quotations in the scoped lines match the tape.

### Counts

| Dimension | Count |
|---|---|
| Scoped paragraphs (non-empty lines) | 75 |
| Sentence-level claims audited | about 280 |
| Quotations (`[V]`) checked | 75 |
| Evidence markers checked | 203 (137 `[BT…]`, 66 `[AE]`/`[AP]`/`[AR]`) |
| Section citations checked | 98 |
| Feature-type labels checked against the PDF | 56 |
| Source-anchored without change | about 268 claims |
| Claims corrected (wording) | 10 |
| Claims stripped | 0 |
| Evidence markers corrected | 2 |
| Quotations corrected | 1 |
| Total edits | 13 (12 table rows below; line 375's second row carries a wording and a marker fix), in 10 paragraphs |

Placement: every feature paragraph sits in the Part for its chapter and the subsection for its section, and every `(Ch N.N, "Title")` names the section or box where the text sits. Labels: all 56 feature-type names match the PDF.

Coverage line (line 10): the 235 runs / about 21,700 words match the diff's kept-run count. Every restored box (all 19 chapter openers and 37 section features) and every body or table span it lists has a paragraph; no restored span of 40 or more words outside Concept Check items, running headers and figure credits is missing. Table 6.2 is in the old conversion, as line 899 says.

### Changes, by line

| Line | Was | Now | Reason |
|---|---|---|---|
| 82 | Jerry "agrees ways to measure" Chaz's effort | Jerry "talks with him about ways to measure" | Source: "They talk about ways to measure". |
| 152 | "when they did not realise it was happening" | "even if they did not realise it was happening" | Source wording ("even if"). |
| 172 | "Symphony orchestras have auditioned musicians behind screens since the 1970s" | many orchestras have used blind auditions since the 1970s, in some cases behind screens | The source dates the practice, then says screens are used "In some instances". |
| 239 | the feature "illustrates why empathy helps leaders with relationship conflict" | the text introduces it, after arguing that relationship conflict shows why emotional intelligence and empathy benefit leaders, as showing how one CEO encourages empathetic collaboration [AR] | Framing the box does not make; now the text's own lead-in (source line 8269). |
| 259 | "He moves her to an information systems team" | "He recommends she move" | Source: "Kyle recommends that Bridget move". |
| 275 | Bombas sock donation [BT, Bombas] | [BT, Mulvey] | The in-text citation for the donation is (Mulvey 2017); Bombas is cited for the four-million-pairs figure. Marker correction. |
| 275 | quotation ended "…motivates employees" [V] | quotation runs on to "…to police the company itself to be a better global citizen" [V] | The cut changed the claim from motivating employees in general to motivating them to police the company. Quotation correction. |
| 314 | reviews "central to a growth strategy" | reviews "of the highest importance to Tesla's success" | Source wording; "growth strategy" was the deep ref's frame. |
| 375 | Hartmann "of one of the book's contributing authors" | adds "(as the front matter lists her)" | The fact comes from the front matter's Contributing Authors list, not the box. |
| 375 | "earlier HR and quality roles"; [AP] | "HR and quality roles"; [AE] | The box gives no order for those roles; marker aligned with the unsourced profile at line 684 and the other author-written profiles. Marker correction. |
| 565 | many blame Welch's approach for GE's later fiscal problems | many blame Welch's approach and GE's conglomerate approach, while others fault his successor Jeff Immelt | The source sentence gives both views. |
| 684 | career "runs from a Big 6 firm through HR and quality roles … to global HR leader" | began at a Big 6 firm; before Trellis, global HR leader; has also held HR and quality roles at … | The box does not order the Wachovia, Genworth, Sun and Andersen roles. |

### Checked and left as is

- Line 64: "to show the role of personality in the demise of one of America's largest and oldest architectural firms" comes from the Ch 2.4 lead-in just before the box, not the box; the paragraph's sentence is still accurate.
- Line 70: "Against the bleak picture of the incongruity thesis" glosses the box's "the above scenario paints a bleak portrait", which follows the Ch 2.5 basic-conflict text.
- Line 152 and 587: "Shaping a Salesperson’s Behavior" calls itself an "ethical challenge" and the Lakers box title begins "Sustainability and Responsible Management:", but the only label on each page (PDF pp. 113, 417) is MANAGERIAL LEADERSHIP; the deep ref's feature types stand.
- Line 815: "illustrates government making federal-lab technology available for commercialisation" rests on the box's own discussion question 2.
- Line 116: [BT, ATD] attributes the 218 per cent figure to the organisation the box names, not a listed source; acceptable.
- Line 401: Lee and Liao's third and fourth practices ("boost your cultural metacognition", "cognitive complexity") sit after the "Understanding Our Global Colleagues" box (source lines 15746–15753); grounded.
- Line 899: the Ch 4.3 → Ch 4.2 correction is right (Kolb and Silberman sit in Ch 4.2).

### Derived tier

None of the edited claims appears in `references/openstax-organizational-behavior.md` or the five distillations (checked by grep for Bombas, Hartmann, orchestra, Tesla, Nadella, Welch-and-Immelt, Lyle, Bridget, Chaz; the Welch hits there concern forced ranking). No re-derivation is needed for these edits. The light reference and distillations do not yet carry the 2026-10-17 feature-box material at all; adding it is a Pass F/G decision for the parent.

### Open

1. **Second leg.** No cross-family blind audit and sort of the 2026-10-17 paragraphs has been run.
2. **Stamp.** Not changed; the parent decides whether the existing Pass I stamp now covers the restored text.
3. **PARTIAL label.** Line 10 no longer carries a PARTIAL label; this audit found the coverage claim accurate for the restored spans.

### Derived tier and stamp (2026-10-17, orchestrator)

The PARTIAL notes are gone from the light reference, the five distillations and the source card, replaced by a coverage statement that names the single-family audit. As Pass G would, the stakeholder-engagement distillation's Phase 1 (Mapping) table gains one row from the "Who Am I Managing?" feature (Ch 10.3): its internal-stakeholder checklist and the Hill quotation, both as audited above. The other restored features are illustrative cases that add no concept to the aar, decision-making, retro or software-business projections, so those carry no new content. A second Pass I stamp on line 3 of the deep reference records this scoped audit; the 2026-10-15 stamp and its "audited, unverified" second-leg status stand. Derived tier restamped against the new deep-reference hash.
