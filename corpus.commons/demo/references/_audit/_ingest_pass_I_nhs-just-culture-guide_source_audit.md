# Pass I source-only audit: nhs-just-culture-guide-deep.md

**Date:** 2026-10-15
**Mode:** audit (full Pass I, fix in place)
**Auditor:** fresh claude-opus-5-5 subagent (same family as the generator). No cross-family leg was run in this dispatch, so treat the reference as audited but unverified until a second-family blind audit and sort is done.
**Deep ref under audit:** `corpus.commons/demo/references/nhs-just-culture-guide-deep.md` (184 lines before the audit, all read)
**Source:** `corpus.commons/demo/sources/converted/nhs-just-culture-guide.md` (109 lines, all read). This is the Poppler `pdftotext -raw` per-region conversion; the source card is `corpus.commons/demo/sources/original/nhs-just-culture-guide.source.md`.
**Calibration read first:** the Pass I section and failure-mode reference of `9-pass-protocol.md`; fixtures 01, 07 and 12.

## Counts

| | |
|---|---|
| Claims audited | about 125 (header and notes 20, thesis 16, Part I 14, Part II 30, Part III 30, statistics 6 rows, connections and positions 9) |
| Source-anchored as written | about 102 |
| Corrected in place (claim reworded to what the source says) | 15 |
| Stripped | 5 clauses or sentences (some inside corrected lines) |
| Marker-corrected | 4 (statistics rows `[V]` to `[AP]`) |
| Quotation-corrected | 0 |

## Verbatim check

`python3 scripts/check-verbatim.py` before and after: one `initial` line (line 15, `action` against the source's `Action`), which needs no fix. No `glyph`, `near`, `page`, `interrupted`, `wrong-source`, `missing` or `no-quote` lines. Two new `[V]` quotations were added during the audit (lines 19 and 38, "can be used by all parties to explain how they will respond to incidents"); both pass.

## Routing check against the new converted text

Every routing claim was checked against the row grouping in the converted text (header bar, question column, answer label, recommendation, END HERE per row):

- Q1 row: 1a, `Yes`, recommendation (A), END HERE; next header "No go to next question - Q2. health test". Supports 1a Yes to A, No to Q2.
- Q2 first row: 2a, `Yes`, recommendation (B). Supports 2a Yes to B.
- Headerless row 535-590: 2b and 2c, one `Yes`, recommendation (C). Supports Yes to 2b or 2c to C.
- Header "if No to all go to next question - Q3. foresight test". Supports No to all of 2a to 2c going to Q3.
- Q3 row: 3b, 3c, 3a (converter order; the numbers carry the order), `If No to any`, recommendation (D); next header "if Yes to all go to next question - Q4". Supports both Q3 routings.
- Q4 row: 4a to 4c, `If Yes to any`, recommendation (E); next header "if No to all go to next question - Q5". Supports both Q4 routings.
- Q5 row: 5a, `Yes`, recommendation (F); header bar "if No", recommendation (G). Supports both Q5 routings.

The header's A to G mapping (line 8) matches these rows. D and E are word-for-word identical in the converted text (lines 74-77 and 88-91). The police-referral claim (A only) holds: G names regulatory bodies, suspension and disciplinary processes, not police. No routing claim depends on headings, letters or routing bullets from the old ingester-written file.

## Changes (line numbers are pre-edit)

1. **L15, correct.** "The decision tree is calibrated to this prior" asserted design intent the source does not state. Now: "Two of the tree's end-states restate it", which is what D and E do in nearly the preamble's words.
2. **L19, correct.** "positioned for use by *all parties* — managers, staff, patients, families — as a communication tool" turned the source's audience (staff, patients and families, who are helped to understand) into its list of users, and "all parties" is never spelt out. Now quotes the source: "can be used by all parties to explain how they will respond to incidents" [V].
3. **L25, correct.** "The poster opens with four caveats": in the converted text the "Please note" block comes after the three preamble paragraphs (lines 29-41). Now "The preamble closes with four caveats".
4. **L28, strip and relabel.** The `[AP]` sentence "the inputs to the tests are facts surfaced by the investigation, and as those facts change, the path through the tree may change" is the ingester's mechanism, not the author's point; stripped. The label "Re-entrant", which is not the source's term, becomes "Usable at any point, open to revisiting".
5. **L38, correct.** "both an internal decision aid and an external communication tool": the internal/external split is not in the source, and the communication tool also serves staff. Now names the paragraph 3 use in the source's words, quoted [V].
6. **L42, correct.** "the source's argument that culpability is the exception, not the default" uses vocabulary the source does not have ("culpability"). Also, "built to surface ... before management action is directed at the individual" was wrong for Recommendation A, which comes at Q1. Now states the order of the questions relative to G and quotes paragraph 2's "before formal management action is directed at an individual staff member" [V].
7. **L70, strip.** "the load-bearing test for whether the system held up its side of the contract": the contract metaphor is not in the source.
8. **L70, correct.** "the only path that proceeds further toward potential individual accountability": "accountability" is not the source's word. Now "the only path that proceeds to Q4".
9. **L80, correct.** "structurally disadvantaged by training gaps (4b)" and "ordinary supervision was absent (4c)" went past the questions' wording. Now close paraphrases of 4b and 4c.
10. **L80, strip.** "The test's name — substitution — captures the operational question: would substituting another comparable individual into the same situation have produced a different outcome?" The source never explains the test's name, and 4a asks about behaviour, not outcome. This is the generator's outside knowledge of the substitution test.
11. **L88, correct.** "no peer-behaviour, training-gap, or supervision-failure exoneration": E says singling out is "unlikely to be appropriate" and wider actions may include the individual, which is not exoneration. Now "No to the peer-behaviour, missed-training and supervision questions"; the Q3 gloss now includes "in routine use".
12. **L92, correct and strip.** "health-affecting-work pathways requiring occupational-health or substance-abuse-at-work response": "requiring" overstates C's "likely to include", and occupational health belongs to C only. The "every recommendation pairs ... a directive about wider investigation" claim now says which wording each uses (A to C "wider investigation is still needed"; D to G "the patient safety incident investigation should indicate the wider actions"). The gloss "patient-safety outcomes are not exhausted by the individual response" is stripped.
13. **L124, correct.** "The phrasing ... is deliberate" asserts authorial intent, and "the locus of corrective work at the system level" is not the source's framing. Rewritten in terms of the wider actions the investigation indicates.
14. **L140, correct.** "the case has cleared the prior filters, so the question is open" gave a reason for F's wording that the source does not give. The causal "so" is removed.
15. **L148, correct.** "peers would not have behaved the same" overstated a No to 4a, which means *no indications* that peers would behave the same way; "no indication that senior team members failed" put 4a's "indications" onto 4c. Both fixed. "a graduated set of management responses ... before reaching for regulatory bodies" read a sequence into a list; now quotes G's list and its "may require ..." clause.
16. **L156-159, marker.** Four statistics rows marked `[V]` were counts, not verbatim text. Reclassified to `[AP]`, each noted as counted.
17. **L161, correct.** "B and C route to occupational-health pathways": only C mentions occupational health. Now B goes to substance-abuse-at-work guidance and C to health guidance likely to include occupational health referral.
18. **L166, correct.** "The source attributes its structure to the NPSA's Incident Decision Tree": the footer says "Based on the work of", not "structure". Reworded.
19. **L172, correct.** "a *default to individual blame*": "blame" is not the source's word. Now uses the source's own phrase, "the tendency to treat wider patient safety issues as individual issues".
20. **L176, strip.** "1.5MB" is in neither the source card nor the converted text, and the PDF is not in the repo.

## Checked and left as is

- Header (L5) metadata: 2018, OGL v3.0, the mirror URL, and the retired publisher page after the 2022 NHS Improvement / NHS England merger come from the source card, not the poster text. They are bibliographic provenance, not claims about the source's content. The OGL characterisation (L184) restates the source card's licence note.
- Preamble paragraph numbers: the converted text has no blank lines. The three paragraphs come from the short closing lines (lines 10, 17, 28) and the sentence breaks. These are citation devices, and the source card also says "three preamble paragraphs".
- Citation subsection labels such as `(Q1, "Deliberate harm test")` capitalise the poster's lower-case header bar text ("Q1. deliberate harm test"). They are location labels, not quotations, so they are left as is.
- L50, "the only test in the tree that addresses *intent*": 1a is the only question about intention. 3c asks about *knowing* departure, which is a state of mind but not intent to harm. Left.
- L13 italic *circumstances in which an error was made* is the source's phrase, used as emphasis inside a paraphrase. Left.
- No cross-reference beyond Reason and the NPSA Incident Decision Tree, both named in the footer. Image-only content (logos, strapline) is not relied on anywhere.
- Coverage: every line of the converted source maps to a part of the deep reference. The TOC-vs-anchors check passes: title, preamble paragraphs 1 to 3, all four "Please note" bullets, Q1 to Q5 with all 11 sub-questions, all seven recommendations, and the footer.

## Derived-tier edits to carry forward (light ref and distillations not edited here)

The light reference `corpus.commons/demo/references/nhs-just-culture-guide.md` carries these superseded claims:

- L13 and L54: "re-entrant"; L13 and L60: guide "for managers, staff, patients, and families" / "for use by all parties — managers, staff, patients, families" (changes 2, 4, 5).
- L13: "patient-safety outcomes are not exhausted by the individual response" (change 12).
- L22: Q4 glossed as "peers would have done the same; training was missed; senior supervision absent" (changes 9, 15). It is also less exact than the source: 4a asks about *indications*.
- L25: "health-affecting-work pathways" (changes 12, 17).
- L35: "Graduated response ... before reaching regulatory bodies" (change 15).
- L43: "whether the system held up its side of the contract" and "advances toward potential individual accountability" (changes 7, 8).
- L45: the substitution test asks "whether substituting another comparable individual ... would have produced a different outcome" (change 10).
- L65: the NPSA Incident Decision Tree as the "structural predecessor" (change 18).
- L69: "Default to system, not to individual" and L70: "The system question is never extinguished by any finding about the individual"; both sit on the claims changed in 1 and 12.

Light ref L20 also says Q2 "Yes to any → exit", which flattens the two Q2 exits (B for 2a, C for 2b or 2c). It is not a deep-ref change, but it should be fixed when the light ref is re-derived. Re-derive the light ref and all five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), then re-stamp with `scripts/check_derived_provenance.py --corpus demo --stamp --slug nhs-just-culture-guide`.

## Open

- Cross-family second leg not run.
- Derived tier not re-derived or re-stamped (out of scope for this dispatch).
