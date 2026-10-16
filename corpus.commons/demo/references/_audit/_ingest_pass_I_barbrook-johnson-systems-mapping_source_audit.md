# Pass I Audit Log — barbrook-johnson-systems-mapping

**Audit target:** `corpus.commons/demo/references/barbrook-johnson-systems-mapping-deep.md`
**Source:** Barbrook-Johnson, P., & Penn, A. S. (2022). *Systems Mapping: How to build and use causal models of systems*. Palgrave Macmillan / Springer Nature, Cham. ISBN 978-3-031-01833-6. DOI 10.1007/978-3-031-01919-7. 197 pages. CC BY 4.0 (Open Access).
**Source converted markdown:** `corpus.commons/demo/sources/converted/barbrook-johnson-systems-mapping.md` (9,124 lines covering all 197 pages of the PDF; body chapters from Ch 1 *Introduction* through Ch 12 *Conclusion* with Index at lines 8770–9123).
**Auditor:** claude-opus-4-7[1m], xhigh effort, 9-pass protocol.
**Date:** 2026-05-13.

## Calibration

Read prior to cold-read:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case — biographical claim source does not make).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical correction case — [V] on paraphrased sentence).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control).

## Audit summary

| Bucket | Count |
|---|---|
| Total non-trivial claims audited | ~180 |
| Source-anchored, no fix needed | 178 |
| Claims stripped | 0 |
| Citations corrected in-place | 1 |
| Verbatim quotes corrected in-place | 1 |
| Cross-corpus drift detected | 0 |
| Training-data leakage detected | 0 |
| Post-source vocabulary detected | 0 |
| Task-application guidance smuggled into deep | 0 |
| Marker corrections (V→AP) | 0 |
| Marker corrections (AP→V) | 0 |

The deep reference is ~470 lines for a 197-page methods monograph covering seven distinct mapping methods. Every [V] marker corresponds to a verbatim quotation that was verified character-by-character against the converted markdown. Two corrections applied in-place during the audit pass.

## Calibration alignment

- *Training-leakage fixture (01).* The deep reference does not contain any biographical or career claims about Barbrook-Johnson or Penn beyond what the source itself states (the "About the Authors" section, page 408–484 in the converted markdown). Their CECAN affiliation, prior work in environmental policy, and the disclosure that PSM is "their" method are all source-stated.
- *Marker-mismatch fixture (07).* Every [V] marker in the deep reference was checked for the presence of quotation-marked verbatim text. One marker initially carried a quote that had been silently re-cased and re-punctuated; the verbatim text was restored (see "Corrections" below).
- *Clean negative control (12).* The deep reference's prose, evidence markers, and citation discipline closely match the shape of the clean fixture. No over-flagging applied.

## Corrections applied during audit

**Correction 1 — verbatim quote restored to exact form.**

*Location:* Section "Five general-purpose uses of systems mapping (Ch 1)", item 1 ("Helping us think").

*Before:* "The most fundamental value — \"you basically cannot avoid having it do this to you\" [V] (Ch 1, \"How Can Systems Mapping Be Useful?\")."

*After:* "The most fundamental value — \"You basically cannot avoid having it do this to you!\" [V] (Ch 1, \"How Can Systems Mapping Be Useful?\")."

*Why:* The source text at converted-markdown line 1212 reads "You basically cannot avoid having it do this to you!" (capital Y, ending with exclamation). The deep ref had silently down-cased the Y and replaced the exclamation with a closing period — Pass D verbatim-accuracy slip caught at Pass I. Restored to exact form.

**Correction 2 — Fig 1.2 layout description softened.**

*Location:* "Part I: Framing — what systems mapping is and how it fits together (Ch 1)" — Fig 1.2 description.

*Before:* "**Fig 1.2** — *emphasis on participation* × *intuitive-easy-to-start ↔ formal-harder-to-start*. PSM, Rich Pictures, and FCM emphasise participation; BBN and System Dynamics are more formal; CLD sits in the middle."

*After:* "**Fig 1.2** — *emphasis on participation* × *intuitive-easy-to-start ↔ formal-harder-to-start*. Positions the methods on those two spectra (the converted-markdown figure layout was fragmented by OCR; the prose-captured placements include PSM and FCM as participation-emphasising, BBN as neutral on participation, and System Dynamics as on the formal end of the second axis)."

*Why:* The pymupdf4llm conversion of Fig 1.2 produced fragmented table-cell text (converted-markdown lines 940–977) without preserving the full graphical placement of all seven methods. The original placement of Rich Pictures and CLD on the participation axis is not visible in the converted markdown. The earlier description over-extended the source. Softened to make the conversion limitation explicit and to stop short of claims not supported by the surviving prose.

## Verbatim quote spot-checks (sampling)

The following [V] quotes were verified character-by-character against the converted markdown:

| Quote (first words) | Converted-markdown line | Verified |
|---|---|---|
| "All except one of the methods in this book always have..." | 810–814 | ✓ |
| "make the landscape of methods clearer, to help people find..." | 648–650 | ✓ |
| "interconnected set of elements that is coherently..." | 755 | ✓ (Meadows 2008 quote, [BT]) |
| "covered well elsewhere and they are entire ways of..." | 1034 | ✓ |
| "horrendograms" (term in scare quotes) | 1238, 3799 | ✓ |
| "shark-infested waters" | 620 | ✓ (not used in deep ref body but verified for thesis paraphrase) |
| "we can work with them to steer and nurture the change we want" | 8736–8737 | ✓ |
| "We must accept that we cannot force or control..." | 8734–8736 | ✓ |
| "Where a method fits with both the project and the system..." | 8152–8153 | ✓ |
| "core system engine" (term) | 2793 (def) and many sites | ✓ |
| "FLAs must avoid causal statements" — *not used* (this is LFUO not BJ&P) | — | not a quote from this source; no risk of cross-corpus drift |
| "It is well worth spending an extra ten minutes..." | 3714–3716 | ✓ |
| "Cognitive scientists have shown that..." — *not used* (this is LFUO not BJ&P) | — | not a quote from this source |
| "the maps are intended to be 'owned' by the stakeholders..." | 3417–3419 | ✓ |
| "transcription can easily take five or six times..." | 7705–7706 | ✓ |
| "Allocate half of your resources to design and communication" | 3054 (heading); 3060–3063 (body) | ✓ |
| "give away power" — facilitation principle | 7637–7641 | ✓ |
| "you basically cannot avoid having it do this to you!" — *corrected to "You basically..."* | 1208–1212 | ✓ after correction |

## Cross-corpus drift check

The deep reference makes citations only to authors that the source itself cites. Key checks:

- *Box & Draper (1987)* — source cites at line 774 ("Box and Draper, 1987"); deep ref's [BT] citation is correct.
- *Meadows (2008)* — source cites at line 754–755; deep ref's [BT] citation is correct.
- *Williams & Hummelbrunner (2011)* — source cites at line 745–747; deep ref's [BT] citation is correct.
- *Star & Griesemer (1989)* — source cites at line 6834–6835; deep ref's [BT] citation is correct.
- *Dekker* — source does *not* cite Dekker; deep ref's concept-index pointer correctly notes "No primary citation in this source. Cross-reference: Dekker is a foundational source for LFUO 2024's just-culture framing" — this is a corpus-internal cross-reference, not a claim about this source's content.
- *Kim (2000)* — source cites at line 2932; deep ref's [BT] citation of the eight system archetypes is correct.
- *Checkland* — source cites Checkland at multiple lines (1845, 1960–1968); deep ref's account of SSM origins traces to these.
- *Forrester (1968)* — source cites at line 6636; deep ref's [BT] citation is correct.
- *Sterman (2018)* — source cites at line 6651; deep ref's [BT] citation is correct.
- *Helfgott et al. (2015)* — source cites at line 4210–4212 and 5075–5079; deep ref's [BT] citation is correct.
- *Pearl (1988); Neapolitan (1989)* — source cites at line 5720–5725; deep ref's [BT] citation is correct.
- *Limits to Growth (Meadows et al. 1972)* — source cites at line 3241–3244; deep ref's [BT] citation is correct.
- *Kosko (1986); Axelrod (1976)* — source cites at lines 5098–5100 and 4968–4969; deep ref's [BT] citation is correct.
- *Bell & Morse (2013a, 2013b); Bell, Berg & Morse (2016a, 2016b)* — source cites at lines 1940–1954; deep ref's [BT] citations are correct.

No cross-author claims were introduced that the source does not make.

## Training-data leakage check

The deep reference makes no biographical claim about the authors that the source itself does not make. The "About the Authors" pages (converted markdown lines 408–484) describe Barbrook-Johnson's role at the Environmental Change Institute and Smith School at Oxford, his prior CECAN/Surrey work, and his use of "agent-based modelling, network analysis, and systems mapping". The deep reference's mention of the authors' PSM-development history is sourced to Ch 5's history section (lines 3812–3836). No claim is made about subsequent work, awards, or roles not in the source.

## Post-source vocabulary check

The deep reference uses the source's own vocabulary throughout. Key terms checked:
- *appropriateness* — source's term (Ch 11)
- *horrendogram* — source's term (Chs 1, 4, 5)
- *core system engine* — source's term (Ch 4)
- *boundary objects* — source's term, citing Star & Griesemer (Ch 9)
- *interested amateurs* — source's term, citing Dennett and Johnson (Ch 9)
- *causal flow* — source's term (Ch 5)
- *ladder of using methods* — source's term (Ch 12)
- *participatory steering of complex adaptive systems* — source's term (Ch 12)
- *quantitative storytelling* — source's term (Ch 6)
- *give away power* — paraphrase of source's "giving away power" (Ch 5, Ch 10)

No vocabulary from later author work or adjacent literatures has been smuggled in.

## Task-application-in-deep check

The deep reference contains no diagnostic questions, anti-pattern lists, or task-projected guidance. All such content lives in the distillation files (decision-making and stakeholder-engagement). The deep reference is faithful summary of the source's own structural argument, with citations.

## Evidence-class marker consistency check

| Marker | Used | Internally consistent |
|---|---|---|
| [V] (verbatim) | All instances carry quotation marks containing verbatim text from the source | ✓ |
| [AP] (author paraphrase) | All instances are paraphrases of source content | ✓ |
| [AR] (author argument) | Used for thesis-paragraph claims that report the authors' argument structure | ✓ |
| [AE] (author example) | Used for the worked examples (UK obesity CLD, Maldives SD, Brazilian Amazon FCM, NHS Rich Picture, etc.) | ✓ |
| [BT] (borrowed-through) | Used for citations of other authors the source cites (Meadows, Williams, Box & Draper, Star & Griesemer, Kim, Helfgott, Pearl, Neapolitan, Forrester, Sterman, Bell & Morse, Kosko, Axelrod) | ✓ |

## Coverage check

The deep reference covers:
- All twelve chapters (Ch 1 Introduction through Ch 12 Conclusion) — covered.
- All seven method chapters (Chs 2–8) — each given its own deep-ref section with the six standardised sub-elements.
- All three cross-cutting chapters (Chs 9–11) — covered.
- The Conclusion's five take-home messages — covered.
- All figures referenced by caption (Figs 1.1–1.3, 2.1–2.2, 3.1–3.2, 4.1–4.2, 5.1–5.2, 6.1–6.3, 7.1–7.3, 8.1–8.2, 9.1, 11.1–11.2) — referenced.
- All tables (Tables 1.1–1.2, 5.1–5.2, 6.1, 7.1–7.3, 11.1–11.3) — referenced.

The Index (converted markdown lines 8770–9123) was cross-checked for concept names; no concept of decision-making or stakeholder-engagement relevance was found to be unaddressed in the deep ref.

## Audit verdict

**PASS.** The deep reference ships. Two in-place corrections applied during the audit; no claims stripped. The marker discipline, citation accuracy, and source-only coverage all hold. Light reference and the two distillations derive from this audited deep reference and inherit the discipline by construction.

## Scoped re-audit 2026-10-16: restored tables and figure labels

**Auditor:** fresh same-family subagent (claude-opus-5-5), fix-in-place. A blind cross-family leg (codex) runs separately on a frozen copy; until it reports, this leg is audited-but-unverified.

**Scope.** Only the material restored by the 2026-10-16 re-conversion (PyMuPDF text blocks) and the deep-reference text written for it (`git diff origin/main` on the deep reference): the Coverage line; the Fig 1.3 bullet; Table 1.2 and the "Methods deliberately excluded" paragraph; the Fig 3.2 sentences; Table 5.1; the Fig 6.1 and 6.3 sentences; Tables 11.1–11.3 and the sentences around them; the three new key-statistics rows; the "Conversion path" note. The rest of the deep reference is unchanged since the earlier audit and was not re-audited, except the "Figures" integrity note, which the restored material made untrue (see below).

**Reads.**
- Tape ranges read in full (2,321 of 9,853 lines): 1050–1110, 1160–1560, 2395–2550, 3660–3870, 4590–4840 (plus 4840–4905 to reach the Fig 6.3 caption), 8150–9300. Spot greps outside them: Fig 8.1/8.2 captions (6160–6173, 6350–6366) to confirm they carry no text labels.
- Deep-reference text in scope read in full via the diff (all added and changed lines).
- Page renders (5 of 10 allowed, all succeeded): PDF pp. 26 (Fig 1.3), 52 (Fig 3.2), 98 (Fig 6.1), 100 (Fig 6.3), 186 (Table 11.3). Tables 11.1 and 11.2 were checked from the tape's reading order, which runs row by row with every cell present, so no render was needed. The source is born-digital, so the scanned-source OCR check does not apply.
- `check-verbatim.py`: 53 apostrophe, 26 initial, 3 near, 1 interrupted. The three `near` lines (337, 348, 350: "templates/ inspiration", "feedbacks/ dynamical", "system/ situation") are a slash at a line end in the tape; the quotations are verbatim, checker limitation. The `interrupted` line (296, Ch 9) is out of scope and is a running header, conversion noise. No glyph, missing or wrong-source finding.

**Counts.** Claims audited: 104. Source-anchored as written: 100. Stripped: 1. Corrected (reworded): 3. Marker-corrected: 0. Quotation-corrected: 0.

**What was checked and holds.**
- Fig 1.3: five region labels verbatim (tape 1064–1077); every placement matches the p. 26 render, including FCM at the meeting of Network analysis, Plots and numbers and Assess contribution, BBN inside both Assess and Plots and numbers, SD in Simulate inside Plots and numbers, and all seven inside Diagrams. [AP] is right for the placements.
- Table 1.2: fifteen methods; all fifteen "Why not in this book?" cells verbatim; the Cynefin, CHAT, giga-mapping, outcome-mapping and stakeholder-mapping quotations verbatim; the further-reading names match their cells (Foot (2014) is in the CHAT row). Key-stats row "most 'Not causal' or not focused on causal understanding": 12 of 15 reasons cite a lack of causal focus; holds.
- Fig 3.2: column labels verbatim; on the p. 52 render the textbook and teacher-training boxes sit under OUTPUTS, "Teachers have skills…" under OUTCOMES, and "Improved learning outcomes and staying on rates / For boys and girls" is the IMPACT box. The "quick communication tool" quotation is verbatim (tape 2544–2545).
- Table 5.1: caption and all fourteen rows verbatim and in row order (tape 3696–3845); the key-stats split of 3 stakeholder-suggested and 4 system-suggested starting points holds.
- Fig 6.1: twelve labels verbatim (the source prints “Policies” in double quotes; quote style only); the p. 98 render shows weights from −0.5 to +1 next to the arrows, and the text says the values are "annotated next to the arrows" (tape 4625–4626). Fig 6.3: four titles verbatim; the p. 100 render shows the same six-factor legend for all four plots and an x-axis to 20.
- Table 11.1: caption and every cell of all seven rows verbatim and in column order (tape 8198–8865); the ease-of-use key-stats row holds; the "adding new columns" quotation is verbatim (tape 8894–8897).
- Table 11.2: every cell matches the tape's row order (8979–9073); the six column headings and the "simplification" quotation are verbatim.
- Table 11.3: every cell matches the p. 186 render column by column, including the RP row (CLD, FCM, PSM, ToC "Embed map in diagram"; SD "Sketch plots of SD outputs"; BBN empty); the reading note and the "best demonstrations" quotation are verbatim.
- Coverage line: Figs 3.1, 5.2, 8.1, 8.2, 11.1 and 11.2 show a caption with no text labels in the tape; the claim holds.

**Changes to the deep reference.**
1. Line 9 (Coverage), stripped "(about 1,300 words)". No passage or check supports the figure, and the tape ranges holding the restored table and figure text run to roughly 2,000 words, so it's probably low.
2. Line 75 ("Methods deliberately excluded"), reworded the lead-in "The descriptions place several of these near the book's methods:" to "From the description and further-reading cells:". This was source-external framing: the Cynefin, CHAT, giga-mapping and stakeholder-mapping cells quoted after it don't relate those methods to the book's methods, and the stakeholder quotation comes from the further-reading cell, not a description.
3. Line 330 (Table 11.1 lead-in), changed the garbled "the bullet glyph-free cells are joined across line breaks" to "cells are joined across line breaks". This is editorial and leaves the claim unchanged.
4. Line 457 ("Figures" integrity note), replaced "All figures are referenced by caption only … the source of all figure-related claims". The restored labels of Figs 1.3, 3.2, 6.1 and 6.3 made it untrue. It now says which figures are quoted from their labels and checked against renders, and that the rest stay caption-only.

**Left open.**
- Coverage line: "A tesseract OCR of all 197 pages … found no other restored-text gap" is a process claim this leg didn't re-run. It's left as written.
- Fig 1.2 bullet (out of scope, unchanged) still says the figure layout "was fragmented by OCR". The new conversion may now hold Fig 1.2's labels; this leg didn't check, because they're outside the restored set it was given.
- The [BT] marker on the Table 1.2 further-reading list is defensible (cross-author pointers) and was not changed.

**Derived tier (not edited; parent re-derives).** None of the four deep edits changes a claim the derived tier carries; edit 2 removes framing that no derived artefact repeats. The derived additions were traced against the tape and renders:
- Light reference, Tables 11.1–11.3 paragraph: "embed any map in a Rich Picture" overstates Table 11.3. The RP row embeds CLD, FCM, PSM and ToC maps; for SD it's "Sketch plots of SD outputs", and the BBN cell is empty. Suggested wording: "embed a CLD, FCM, PSM or ToC map in a Rich Picture".
- Light reference, excluded-methods list: "causal/cognitive mapping, which they would most likely have added next" goes slightly beyond the source's "the methods we most likely would have included had we expanded our focus". Suggested wording: "which they would most likely have included had they widened their focus".
- Light reference, Fig 1.3 sentence, Table 5.1 sentence and Table 11.2 sentence: hold.
- aar concept 9 and the "principled place to start" row: all five Table 5.1 quotations verbatim and correctly attributed; they hold.
- retro submap row and "Two candidate experiments" row: quotations verbatim; "for an experiment the team controls" maps to the "Intervention or controllable factors" row; they hold.
- software-business concept 19 (Table 11.3 examples) and the two Phase 1 rows (Table 11.1 "When most appropriate" quotations, Table 11.2 forecasting "None"): verbatim and correctly placed; they hold.
- Source card coverage sentence: consistent with the audited Coverage line; it holds.

**Verdict.** The scoped material passes after the four in-place edits. Not stamped: the driver stamps once the cross-family leg is in.

### Apply leg 2026-10-16: the sort's remaining edits and the derived tier

**Reads.** `sort.md` and `blind-findings.md` in full; the scoped deep-reference text; every prescribed tape range in full (1050–1110, 1160–1560, 2395–2550, 3660–3870, 4590–4905, 8150–9300) plus tape 940–1050 for Figs 1.1–1.2; renders of PDF pp. 24 (Fig 1.1) and 25 (Fig 1.2), both succeeded. The light reference and all five distillations read in full.

**Deep-reference edits.**
1. Fig 1.2 bullet (line 48), applied with changed wording. The figure's labels are in the tape (1001–1045), so "fragmented by OCR" and "prose-captured placements" were untrue. The placements now follow the p. 25 render: Rich Pictures, PSM and FCM toward participation; ToC and CLD just above the centre; BBN and SD toward neutral; RP and ToC intuitive; CLD and PSM just past the centre; FCM further; BBN and SD furthest toward formal. [AP], with the render cited. The sort's wording left out ToC's and CLD's participation positions and grouped FCM with the formal end only implicitly.
2. "Figures" integrity note (line 457), applied with changed wording. The blanket "all other figures are referenced by caption only" is gone; it now says Figs 1.1 and 1.2 carry their labels in the converted text and their Part I placements were checked against renders of pp. 24–25. The Fig 1.1 bullet (line 47) holds against the p. 24 render.

`check-verbatim.py` after the edits: 53 apostrophe, 26 initial, 3 near (the slash line ends), 1 interrupted (line 296, running header); no real mismatch.

**Disputed finding settled.** Light reference "would most likely have added next": the source says "These are the methods we most likely would have included had we expanded our focus" (tape 1236–1240). "Next" adds a sequence the source doesn't state; rewritten to the source's counterfactual.

**Derived-tier corrections.**
- Light reference: excluded-methods clause (above); Fig 1.2 sentence brought into line with the corrected deep bullet; "embed any map in a Rich Picture" narrowed to Table 11.3's RP row (CLD, FCM, PSM, ToC maps embedded; SD outputs sketched; tape 9216–9234).
- Retro: Named limits said Table 1.2 was "not recoverable from the converted text"; it now says the table lists fifteen excluded methods, most for not being focused on causal understanding (deep key-stats row; tape 1199–1538).
- Software-business: Phase 1 forecasting row no longer says the book holds that no method forecasts a many-factor market or org-design question; it now says Table 11.2 names no method as most appropriate for forecasting there, and carries the authors' simplification caveat [V] (tape 9050–9056, 9078–9081).
- AAR, decision-making, stakeholder-engagement, the distillation indexes and the source card: no claim the audited deep no longer supports.

**Verdict.** Every confirmed defect is fixed in the deep reference or the derived tier; check-verbatim is clean on all edited files.


### Gate settlement (2026-10-16, orchestrator)

The apply leg passed the gate with one open item: the Coverage line's OCR claim was unverified by any leg. The orchestrator ran the OCR on 2026-10-16 with tesseract 5 at 300 dpi on all 197 pages and checked each OCR line of 25 or more normalised characters as a substring of the converted text (bullet glyphs stripped; a line also counts as matched when half or both thirds of it match, to absorb single-character OCR slips). 194 lines stayed unmatched. Inspection shows two kinds: upside-down OCR of the rotated landscape tables (PDF pp. 28–30, 81–82, 176–186), whose text the converted text holds the right way up, and text inside figures drawn as images (Fig 3.1 p. 51, Fig 5.2 p. 80, Table 5.2's cells p. 90, Fig 6.x p. 98–100, the Maldives model p. 129, Fig 9.x p. 144, Figs 11.1–11.2 pp. 182 and 185). The Coverage line now states this method and result instead of the bare claim.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `02e2ed281db13e0a6af3f44590428d617b821fca16dc657c6fb757e087a6cc60`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `38951fcac8e2aa000cbcd7b7ba5951db85264d7203cbd176ffd91295ab258923`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_barbrook-johnson-systems-mapping_crossfamily_blind.md`, `_ingest_pass_I_barbrook-johnson-systems-mapping_crossfamily_sort.md`, `_ingest_pass_I_barbrook-johnson-systems-mapping_crossfamily_prompts.md`.

**Sort result:** The sort found 6 confirmed findings (3 correctly fixed, 2 fixed incompletely or outstanding in the derived tier, 1 missed by the fixer), 1 defect introduced by a historical fix, 0 over-flagged by the blind auditor, 1 over-flagged by the fixer, 1 disputed and 1 editorial correction, with the scoped deep-reference gate PASS once its two edits are applied and the full shipment gate FAIL until the two derived-tier defects are corrected.

**Remaining edits applied (2026-10-16):** Both remaining edits were applied with changed wording and none declined: the Fig 1.2 bullet was tightened to the p. 25 render (adding ToC's and CLD's near-centre positions and FCM's place short of BBN and SD), and the Figures note now names the pp. 24–25 renders for Figs 1.1–1.2 instead of the sort's one-line sentence.

**Gate:** accepted by operator. Deep reference sha256 `3c1cd8cd9dca1acea0be19fd50d163308c7ebd1b4e9d3acb6266f1070ec600e3`, stamp included.

## Scoped re-audit 2026-10-16: restored tables and figure labels

**Derived-tier fidelity leg.** A fresh claude-opus-5-5 agent checked the derived tier against the audited deep reference. Its scope was the derived text written for the restored Tables 1.2, 5.1 and 11.1–11.3 and Figs 1.3, 3.2, 6.1 and 6.3. It read the deep reference, the light reference, all five distillations and the source card in full, the prescribed tape ranges in full (1050–1110, 1160–1560, 2395–2550, 3660–3870, 4590–4840, 8150–9300), and this source's 70 rows in the five distillation indexes. Full report: `_planning/pass-i/demo/barbrook-johnson-systems-mapping/fidelity-report.md`.

**Result.** 143 claims traced: light reference 36, aar 10, retro 10, software-business 12, decision-making 3, stakeholder-engagement 1, source card 1, index rows 70 (structure and trace). One fix in place: in the light reference's Table 11.1 summary, "BBN for low-risk quantification of contributions to outcomes" now reads "BBN for low-risk quantification or quantitative analysis of contributions to outcomes", restoring the cell's two separate conditions (tape 8502–8514). No distillation or index row changed. `check-verbatim.py` on the derived files reports only quote-style and initial-capital normalisation.

**Deep-reference defect recorded, not fixed** (`fidelity-deep-defects.json`): line 120 places Fig 3.2's labels in their columns with [V] markers only. The placements come from the p. 52 render, so they should carry [AP] with the render named, as Fig 1.3's do.

## Derived-tier fidelity check (2026-10-16)

The scoped derived-tier fidelity check traced 143 claims to the audited deep reference for *Systems Mapping* (Barbrook-Johnson & Penn, 2022): 36 in the light reference, 10 in aar, 10 in retro, 12 in software-business, 3 in decision-making, 1 in stakeholder-engagement, 1 on the source card, and 70 index rows checked for structure and traced to their distillations. All prescribed tape ranges were read in full and every derived file was read in full. One claim was fixed in place: in the light reference's Table 11.1 summary, a merged BBN condition was split back into the table's two separate conditions. No distillation or index row needed a change; every quotation added for Tables 1.2, 5.1 and 11.1–11.3 is verbatim and correctly anchored, and `check-verbatim.py` reports nothing beyond quote-style and initial-capital normalisation on the derived files. One deep-reference defect was recorded and not fixed: the Fig 3.2 column placements carry [V] only, where Fig 1.3's render-read placements carry [AP].

### Post-stamp marker fix (2026-10-16, orchestrator)

The fidelity check recorded one deep-reference defect: Fig 3.2's column placements carried only [V], though the tape gives the labels without column markup. A sentence now marks the placements [AP], read from a render of PDF p. 52, matching Fig 1.3. The label quotations stay [V]. Derived tier restamped against the new hash.
