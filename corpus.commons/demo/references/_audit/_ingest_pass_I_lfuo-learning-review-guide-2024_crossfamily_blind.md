## Scoped re-audit 2026-10-16: restored text

**Disposition: corrections required.** I found 13 defects: two in the deep reference, eight in the derived tier, and three in the source card. No files were changed. The filesystem is read-only, so this report was not appended to the existing audit log.

### 1. What I read

Read in full:

- `blind-brief.md`, all three calibration fixtures, and `pass-i-spec.md`, before reading the reference.
- `frozen-deep.md`, cold. Its SHA-256 matches `frozen-deep.sha256`: `fa3bb6b432f33a9cf1963d4dfc284490a78383d389c966318fa90527d93b99c9`.
- Every tape range specified in the brief. Those ranges contain **3,031 distinct newline-numbered lines**, accounting for their overlap.
- All four supplied OCR files and `source-card.md`.
- The scoped derived additions and replacements, identified against `origin/main`.

Inspected the original PDF’s cover and Preface, process graphics, restorative checklist, bias boxes, and “Dynamics of Influence & Change” graphic: PDF pp. 1, 3, 22, 46, 58–59, 77–78 and 87–88.

(`_planning/pass-i/demo/lfuo-learning-review-guide-2024/source.pdf`)

Ran the quotation checker against `tape.md`. Also checked PDF metadata, page count and checksum; the source-card checksum matches the original PDF.

An initial form-feed line-counting error exposed 107 additional adjacent tape lines: 347–352, 413–420, 529–538, 622–632, 762–775, 870–885, 956–972, 1024–1041 and 1086–1092. I corrected the numbering and reread all requested ranges. I did not perform a full read of the remaining tape.

I did **not** read the fixer’s findings or the previous audit log. Unchanged material remains outside this audit’s disposition.

### 2. Findings

Deep-reference line numbers below refer to `frozen-deep.md`. Derived filenames are abbreviated by task.

1. **Deep reference, line 391 — incorrect response-format description.**

   “Each marked no or yes” describes the restorative checklist as binary. PDF p. 77 supplies response **lines** anchored NO and YES; p. 78 explicitly illustrates marking different positions on those lines.

   **Exact fix:** replace the second sentence with:

   > It organises questions under five headings, with response lines anchored NO and YES on which users mark their position [AP] (Appendix F, “Restorative Just Culture Checklist”, PDF pp. 77–78).

2. **Deep reference, line 376 — unsupported source description.**

   “Each with a worked example” overstates Appendix D. The first seven briefing items include examples; item eight gives timing guidance without a worked example of next steps or a timeline. Evidence: tape 4094–4134, particularly 4132–4134.

   **Exact fix:** strip `, each with a worked example`.

3. **Light reference, line 29 — dropped qualifier.**

   “Conditions of influence are the basis of the FLA’s analysis” removes the source’s **often**. The deep reference preserves it correctly. Evidence: tape 826–827: “These conditions often form the basis of the analysis part of the FLA process.”

   **Exact fix:** replace the opening sentence with:

   > **Conditions of influence** often form the basis of the FLA’s analysis.

4. **Light reference, line 98 — dropped qualifier.**

   “Reports avoid names” makes categorical what the source describes as typical practice. Evidence: tape 3181–3182: reports “typically avoid using people’s names”.

   **Exact fix:** replace `**Privacy:** reports avoid names` with:

   > **Privacy:** reports typically avoid names

5. **Light reference, line 134 — caution strengthened into prohibition.**

   “Don’t edit sentences as a group” exceeds Handout E. The source says to be **wary** of sentence-level group editing and to save polishing for the final draft. Evidence: tape 4987–4990.

   **Exact fix:** replace:

   > Have one person write the story; don’t edit sentences as a group.

   with:

   > Have one person write the story; be wary of editing sentences as a group, and save sentence polishing for the final draft.

6. **Light reference, line 176 — dropped alternatives.**

   “Agreement means the points of departure haven’t surfaced” retains only one of the source’s three explanations. The dialogue may also have been unnecessary, or participants may not want to discuss their differences. Evidence: tape 2342–2351; deep reference line 194.

   **Exact fix:** replace the item with:

   > 13. **Fear the fusion, not the confusion.** Agreement may mean the facilitated dialogue was unnecessary, points of departure have not surfaced, or participants do not want to discuss them.

7. **AAR distillation, line 124 — dropped alternative in diagnosis.**

   The “whole group agrees early” row diagnoses unrevealed or unspoken differences, omitting the source’s explanation that the facilitated analysis may have been unnecessary. Agreement alone does not establish either retained diagnosis. Evidence: tape 2345–2351.

   **Exact fix:** replace the diagnosis cell with:

   > The facilitated analysis may have been unnecessary, points of departure may not have surfaced, or people may not want to discuss them (Part 6, box)

8. **Retro distillation, line 97 — dropped alternatives in diagnosis.**

   “Fusion: points of departure haven’t surfaced” converts one possible explanation into the diagnosis. Evidence: tape 2345–2351.

   **Exact fix:** replace the diagnosis cell with:

   > The facilitated analysis may have been unnecessary, points of departure may not have surfaced, or people may not want to discuss them (Part 6, box)

9. **RETRO-DISTILLATION-INDEX.md, line 142 — dropped alternatives.**

   “Agreement means the points of departure haven’t surfaced” repeats the categorical reduction. Evidence: tape 2345–2351.

   **Exact fix:** replace the final cell with:

   > “FEAR THE FUSION. NOT THE CONFUSION”: agreement may mean the dialogue was unnecessary, points of departure have not surfaced, or people do not want to discuss them; watch for outcome and hindsight bias.

10. **Retro distillation, line 59 — incorrect list endpoint.**

    The row says Handout D’s questions end with “What can we learn as an organization?” The sixth question continues: **“What might we do differently?”** Evidence: tape 4858–4861.

    **Exact fix:** replace the answer cell with:

    > Handout D’s six AAR-type questions, starting with “What was planned?” [V] and ending with “What might we do differently?” [V]. This distillation adapts them into how-and-what prompts using Handout B’s interview guidance.

    The last sentence also makes clear that rephrasing the dialogue questions is this distillation’s application: Handout D itself retains several “why” questions.

11. **Source card, line 24 — stale extraction claim.**

    “No OCR required” is incompatible with the card’s later recognition of image-only Appendix F and with the image-held bias boxes. The PDF is born-digital, but its complete substantive content is not available through text extraction alone. Evidence: tape 4217–4219; supplied OCR files; PDF pp. 77–78 and 87–88.

    **Exact fix:** replace the opening sentence with:

    > The PDF is born-digital, but Appendix F and three Handout C boxes require OCR or direct inspection of the page images.

12. **Source card, line 28 — stale coverage status.**

    The card says the reference “stays PARTIAL until Passes C–E cover” the restored material. That describes the state before the scoped additions, whereas frozen-deep line 9 records their completion and Parts XIII–XVII carry the newly covered material.

    **Exact fix:** replace the paragraph with:

    > **Deep reference coverage.** The earlier conversion omitted framed sidebars, pull quotes, worksheets and interview guides. The frozen deep reference records the restored material as covered on 2026-10-16 and includes OCR-based coverage of Appendix F and the image-held Handout C boxes. Those additions are undergoing this scoped Pass I re-audit.

13. **Source card, line 20 — unsupported temporal provenance.**

    “Current canonical iteration” and “the current production guide actively used by USFS and partner agencies” are not established by the supplied source. The cover establishes the April 2024 revision; the Preface establishes its lineage and changes. Neither establishes current adoption or production status at ingestion or audit time.

    **Exact fix:** replace `The 2024 guide is the current canonical iteration of a process that began` with:

    > The guide’s Preface traces a process that began

    Strip the final sentence beginning `The 2024 version was selected for ingestion over the 2020 predecessor`.

### 3. Count and required checks

For reproducibility, I counted a **claim-bearing audit unit** as one changed nonblank prose line, list item, table row or source-card metadata entry. Multiple assertions within a unit were checked together; this is not an inflated estimate of atomic propositions.

| Tier | Units checked |
|---|---:|
| Deep reference | 107 |
| Light reference and scoped distillation/index changes | 74 |
| Source card | 18 |
| **Total** | **199** |

The changed deep-reference lines contain **206 `[V]` markers**, including quotations retained within rewritten paragraphs.

| Defect class | Count |
|---|---:|
| Incorrect response-format description | 1 |
| Unsupported source description | 1 |
| Dropped qualifier or alternative | 7 |
| Incorrect list endpoint | 1 |
| Stale conversion or coverage statement | 2 |
| Unsupported temporal provenance | 1 |
| **Total** | **13** |

Within scope, I found no additional quotation mismatch requiring correction, unsupported author/work cross-reference, post-source vocabulary, or task-application guidance introduced into the deep tier.

**Key statistics:** the deep reference has no key-statistics table. The scoped numerical descriptions—including seven process steps, five Hows, six AAR question groups, eight briefing steps, citation years and example dates—match the source. Finding 2 concerns the claim about examples accompanying those eight steps.

**Author-stated limitations:** there is no separate limitations list in the deep reference. The scoped discussion preserves the source’s relevant boundaries: external authorities remain outside the administrative assurance; briefing material and delegation templates are non-exhaustive or optional; the Five Hows are selectively applicable; and escalation may require substantially more time and money. The dropped qualifications in the light tier are reported above. I did not treat conversion limitations as limitations asserted by the source’s authors.

Historical ingest activity and comparisons against the earlier conversion cannot all be independently reconstructed from this packet; this audit does not newly certify those workflow measurements.

### 4. Over-flag guard

- **Restorative-justice sentence across a page box:** clean. Tape 475 resumes at 503–505. The checker’s `missing` result reflects extraction order.
- **“Forming the FLA team” quotation:** clean. Tape 1318–1320 resumes at 1368–1369 after the box.
- **“Serious Crimes” quotation:** clean. Tape 3083–3084 resumes at 3111.
- **`101-37`:** clean. Tape 1071–1072 splits the identifier across lines. No quantity was changed.
- **“Institutioned”, “happed”, “it about” and “administer pause”:** clean reproductions of the printed wording.
- **Three OCR-based bias descriptions:** clean `[AP]` claims. Confirmation, outcome and hindsight bias match the supplied OCR and page images; the hindsight paragraph retains both alternative-outcome exercises.
- **Appendix F’s substantive paraphrases:** clean apart from the response-format description in finding 1. Its parties, needs, obligations, forgiveness process and four goals are source-held.
- **Process-graphic order:** clean. The Part 4 numbering and Learning Review arrows support the reference’s sequences. The Five Hows are correctly described as a ring rather than a prescribed sequence.
- **Reason’s *The Human Condition* attribution:** clean as a report of what this guide prints at tape 3105–3107. Substituting a different title from background knowledge would breach this audit’s source-only rule.
- **“Never ask WHY” versus Handout D’s why questions:** both occur in the source. Their different settings—interviews and facilitated dialogue—do not warrant correcting the deep reference.
- **Applied software and retrospective examples:** permitted in the derived tier. The explicitly labelled mappings are not defects merely because the guide’s examples concern wildland fire.
- **Prompting inquiry when a group agrees early:** permissible task application. Findings 6–9 concern categorical diagnoses that discard source alternatives, rather than the act of inviting further inquiry.
- **Omitted links, report-cover images and illustrative captions:** no missing substantive section established within scope. Summarisation does not require reproducing every link or illustration.