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
