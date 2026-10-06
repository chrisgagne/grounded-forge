**1. What I read**

Read in full: `sort-brief.md`; the three calibration fixtures; `pass-i-spec.md`; both audit reports; and `post-audit-deep.md`, lines 1–307. Also read `source-card.md`, both checksum files, the repository instructions and the required architecture documents.

Compared every changed passage between `frozen-deep.md` and `post-audit-deep.md`. Independently checked the findings against the relevant tape passages, with full-file searches for the disputed terminology and cross-volume references. This was a sort leg, not another end-to-end tape audit.

Visually inspected original PDF page 20, printed p. 14, for FACTS formatting. Verified PDF metadata, file size, checksum and word counts. Both deep-reference checksums match. The original has 137 pages and 2,248,402 bytes.

The verbatim checker, run against `post-audit-deep.md` with `tape.md` explicitly supplied, returned no findings. There are **57 substantive `[V]` occurrences**, not 59; the fixer counted two additional mentions of the marker in explanatory text.

No files were modified. The complete report follows.

**2. Sorted ledger**

`B` identifies a numbered blind finding; `F` identifies a numbered fixer change. All deep-reference line numbers below refer to **post-audit-deep.md**.

| Finding | Classification | Post-audit line(s) | Tape evidence and adjudication |
|---|---|---:|---|
| **B1 / F1, F5, F8: unsupported Volume 1 attributions** | **Confirmed, fix incomplete** | 7, 14, 208, 279, 299, 305 | Tape 26–29 and 74–77 establishes the companion relationship; 3197–3199 refers to Volume 1, Chapter 4, for culpability methods. Tape 40–42 states the paradigm without attributing its formula to Volume 1; 2934–2962 presents Anatomy of an Event without that attribution. F1, F5 and F8 correctly remove the unsupported formula/model attributions at lines 14, 208 and 279. Specific outside-author credits, pages/endnote, converter comparison and formula comparison remain at lines 7, 299 and 305. Neither supplied Volume 2 nor its provenance card establishes those particulars. |
| **B2: document organisation marked `[AR]`** | **Missed by the fix-in-place audit** | 20 | Tape 170–185 describes the sections and their users. “The volume divides the work three ways” is descriptive author content, appropriately `[AP]`. The `[AR]` remains. |
| **B3 / F3: Sections 1–2 described as aiming at active errors at the point of work** | **Disputed** | 20, 255 | The blind reading treats this as an exclusive classification that excludes document defects and delayed consequences; tape 35–37 and 1374–1381 supports that objection. The alternative reading treats “aim at” as a summary of the principal emphasis, consistent with the Foreword’s active-error/latent-error framing at 23–25 and the Introduction’s division at 158–185. The current wording never expressly says “only,” so the blind finding is stronger than the sentence necessarily warrants. F3 adds relevant evidence but does not resolve the ambiguity. The replacement below follows the Introduction’s broader wording. |
| **B4: applicability lists called “the reliable statement”** | **Missed by the fix-in-place audit** | 36 | Tape 201–204 directs readers to each tool’s applicability section for further details. It does not supply the reference’s reliability judgement. |
| **B5 / F4: Project Planning qualifiers** | **Confirmed, fix incomplete** | 152 | Tape 1919–1923 says “not typically used” and includes programme work. F4 correctly restores those qualifications. Tape 1925–1926 says the work plan “may address” the elements “as applicable”; “The project work plan covers” still drops both qualifications. |
| **B6: lagging indicators categorically cannot predict** | **Missed by the fix-in-place audit** | 190 | Tape 2524–2525 says they “do not necessarily predict future accomplishments.” “Not predicting what comes next” remains categorically stronger. |
| **B7: indicator scale and conditional criteria** | **Missed by the fix-in-place audit** | 192, 266 | Tape 2584–2589 qualifies quantitative and disaggregate criteria; 2600–2605 gives 1–5 as an example and permits unequal importance among criteria. Line 192 still makes 1–5 the prescribed scale. Line 266 additionally omits the conditional criteria. |
| **B8 / F7: invented skill-based mapping** | **Confirmed and fixed** | 250–251 | Tape 343–357 and 688–691 explicitly connects situational-awareness tools and self-checking with skill-mode work. The other passages describe targets without assigning that mode: 936–1028, 1047–1062, 1100–1115 and 1673–1684. F7 correctly removes “slips and lapses” and separates the other tools. Full-file searches find neither term. |
| **B9: every defect said to remain hidden** | **Missed by the fix-in-place audit** | 255 | Tape 4415–4416 defines a defect as an embedded result of an earlier engineering error. Remaining undetected until later operational activities belongs to the latent-error definition at 4460–4463. The combined definition still transfers that qualification to defects. |
| **B10: FACTS numbering attributed to conversion loss** | **Missed by the fix-in-place audit** | 66, 301 | Tape 579–601 matches the original PDF, printed p. 14: only Foresee is numbered; Confirm and Test are unnumbered headings; Ask and Stop are bullets. Original-page inspection confirms that the numbering was not lost during conversion. Both incorrect explanations remain. |
| **B11 / F9: conversion word counts** | **Confirmed and fixed in the deep reference** | 10, 299 | Independent counting reproduces 37,576 whitespace-delimited tape words and 34,106 `pdftotext` words. F9 correctly replaces the unreproducible counts and identifies the method. The unchanged source-card counts remain a separate provenance issue outside the requested deep-reference edits. |
| **B12: quotation inside declared paraphrase-only material** | **Missed by the fix-in-place audit** | 7, 226, 303 | Tape 3284 exactly supports the quotation, printed p. 98. Its wording is correct, but line 7 explicitly puts that passage within the paraphrase-only exception. Line 226 violates that declaration; line 303’s assertion about quotation locations is consequently false. |
| **F2: requirements/enhancement wording** | **Confirmed and fixed** | 16 | Tape 72–73 says the tools “may” enhance approaches in the Good Practices guidance; 85–88 describes example practices that “can” enhance implementation of existing requirements. The replacement restores this qualified formulation and distinguishes guidance approaches from requirements. |
| **F6: whose confidence defines the just-culture balance** | **Confirmed and fixed** | 224 | Tape 3181–3185 expressly locates the confidence “among managers.” F6 restores that actor. Changing “no tolerance” to “zero tolerance” also follows the source without changing its meaning. |

**Over-flagged findings:** none conclusively established for either auditor.

The remaining cross-volume particulars in B1 are not declared false about Volume 1. They fail this source-only reference’s trace test. The fixer’s reported checks of another tape cannot establish them within the supplied Volume 2 evidence.

**New defects introduced by the fixer:** none confirmed. Every changed passage was compared with its pre-audit wording and checked against the relevant evidence. The new “about 275 words per page” is an acceptable approximation of **274.277** and does not require correction.

The fixer’s assertion that no quotation occurs in excepted material is incorrect: line 226 quotes p. 98. That is a missed existing defect, not a newly introduced one. The incorrect quotation count is likewise an audit-log error, not an additional deep-reference defect.

**3. Remaining edits**

Apply these to the current `post-audit-deep.md`. Line numbers identify the supplied version; they will shift after edits.

1. **Line 7 — replace item (3).**

   **Current:**
   > (3) **Material that Volume 1 credits to named outside authors**, followed here for consistency with the Vol. 1 deep reference (`doe-hpi-handbook-vol1-deep.md`): the just-culture prerequisites, the Foresight, Culpability and Substitution tests and the reporting-system barriers and solutions in "Reporting Errors and Near Misses" (pp. 96–98), and the Culpability Decision Tree (p. 99), which Vol. 1 adapts from Reason, Reason and Hobbs, and Johnston (Vol. 1, Ch 4, pp. 4-24 to 4-31); and the debrief questions and mindset-reconstruction steps of "Investigating Events Triggered by Human Error" (pp. 85–89), which parallel the goals–focus–knowledge problem-analysis questions Vol. 1 credits to Dekker's *Field Guide to Human Error Investigations* (Vol. 1, Ch 3, p. 3-22, endnote 23). Volume 2 itself names no outside author anywhere and carries no endnotes.

   **Replacement:**
   > (3) **Investigation, reporting and culpability material**: for this reference, "Investigating Events Triggered by Human Error" (pp. 85–89), the reporting and culpability material on pp. 96–98, and the Culpability Decision Tree (p. 99) are paraphrased. Volume 2 refers readers to Volume 1, Chapter 4, for further detail on the culpability methods (Sec 3, pp. 96–97).

   **Evidence:** tape 2934–2962 and 3197–3225. This preserves the operator’s conservative quotation policy while removing unsupported cross-source particulars.

2. **Line 299 — strip the Volume 1 converter comparison.**

   **Current span:** `, the same converter family as Volume 1 (` followed by `` `markitdown 0.1.5` `` and `)`.

   **Replacement:** strip that span.

   The sentence will end:
   > … converted with `markitdown 0.1.8` (deterministic; no model-mediated extraction).

   **Evidence:** the supplied source card records Volume 2’s converter; no supplied provenance establishes Volume 1’s converter version.

3. **Line 305 — strip the Volume 1 formula comparison.**

   **Current span:**
   > , where Volume 1 writes "Re + Mc → ØE"

   **Replacement:** strip.

   **Evidence:** tape 40–42 supports the preceding description of Volume 2’s formula.

4. **Line 20 — correct the opening marker.**

   **Current:**
   > The volume divides the work three ways [AR] (Introduction, p. 1).

   **Replacement:**
   > The volume divides the work three ways [AP] (Introduction, p. 1).

   **Evidence:** tape 170–185.

5. **Line 20 — resolve the disputed scope summary.**

   **Current:**
   > The first two sections aim at active errors at the point of work; the third at the latent conditions that provoke error and weaken defences (Foreword, p. i; Introduction, p. 1; Sec 3, p. 70).

   **Replacement:**
   > Sections 1 and 2 describe behaviours that help individuals and work teams anticipate, prevent or catch errors before they harm people, facilities or the environment; Section 3 provides methods for identifying latent organisational weaknesses that provoke error or weaken defences [AP] (Introduction, p. 1; Sec 3, p. 70).

   **Evidence:** tape 158–185 and 2283–2291. This is a source-verified resolution of B3, rather than a declaration that its exclusive reading is mandatory.

6. **Line 255 — replace the complete bullet, resolving B3 and correcting B9.**

   **Current:**
   > - **Active versus latent.** Sections 1 and 2 aim at active errors at the job site; Section 3's tools aim at latent organisational weaknesses that provoke error or degrade defences (Foreword, p. i; Introduction, p. 1; Sec 3, p. 70) [AP]. The Definitions distinguish an active error, which immediately changes plant state, from a latent error and a defect, which embed undesired conditions that stay hidden until revealed later (Definitions, pp. 128–130) [AP].

   **Replacement:**
   > - **Active versus latent.** Sections 1 and 2 describe behaviours that help individuals and work teams anticipate, prevent or catch errors before they harm people, facilities or the environment; Section 3's tools help identify latent organisational weaknesses that provoke error or degrade defences (Introduction, p. 1; Sec 3, p. 70) [AP]. The Definitions distinguish an active error, which changes equipment, system or plant state and triggers immediate undesired consequences, from a latent error, which unknowingly embeds an undesired condition or reduces equipment reliability and remains undetected until subsequent operational activities reveal it. A defect is an undesired result of an earlier engineering-process error embedded in the physical plant or design-bases documentation (Definitions, pp. 128–130) [AP].

   **Evidence:** tape 158–185, 2283–2291, 4376–4377, 4415–4416 and 4460–4463.

7. **Line 36 — remove the unsupported reliability judgement.**

   **Current:**
   > each tool's own "Use This Tool" list is the reliable statement of when to apply it.

   **Replacement:**
   > each tool's own "Use This Tool" list gives further details about its applicability.

   **Evidence:** tape 201–204.

8. **Line 152 — restore the work-plan qualifications.**

   **Current:**
   > The project work plan covers Initiate

   **Replacement:**
   > The project work plan may address the following elements, as applicable: Initiate

   **Evidence:** tape 1925–1926.

9. **Line 190 — restore the lagging-indicator qualification.**

   **Current:**
   > showing where one is but not predicting what comes next

   **Replacement:**
   > showing current position and accomplishments but not necessarily predicting future accomplishments

   **Evidence:** tape 2524–2525.

10. **Line 192 — identify 1–5 as an example.**

    **Current:**
    > using a simple matrix and a 1–5 scale

    **Replacement:**
    > using a matrix and a simple scoring scale, for example 1–5

    **Evidence:** tape 2600–2605.

11. **Line 266 — replace the complete statistics-table row.**

    **Current:**
    ```markdown
    | Criteria for judging a candidate indicator | seven (direct, objective, adequate, quantitative, disaggregate, practical, reliable), rated on a 1–5 scale | [AP] (Sec 3, pp. 78–79) |
    ```

    **Replacement:**
    ```markdown
    | Criteria for judging a candidate indicator | seven: direct, objective, adequate, quantitative where possible, disaggregate where appropriate, practical and reliable; an example scoring scale is 1–5, and the criteria need not be equally important | [AP] (Sec 3, pp. 78–79) |
    ```

    **Evidence:** tape 2576–2605.

12. **Line 66 — correct the FACTS explanation.**

    **Current:**
    > (The step numbering after step 1 is lost in conversion; see the integrity notes.)

    **Replacement:**
    > (The original PDF, like the converted text, numbers only Foresee as step 1; Confirm and Test are unnumbered headings, while Ask open-ended questions and Stop when unsure appear as bullets.)

    **Evidence:** tape 579–601; original PDF page 20, printed p. 14.

13. **Line 301 — correct the corresponding integrity note.**

    **Current:**
    > The FACTS steps (p. 14) lose their numbering after step 1: "Confirm" and "Test" appear as unnumbered paragraph heads and "Ask open-ended questions" and "Stop when unsure" as bullets.

    **Replacement:**
    > The FACTS formatting on p. 14 is preserved from the original: only Foresee is numbered, Confirm and Test are unnumbered headings, and Ask open-ended questions and Stop when unsure appear as bullets.

    **Evidence:** tape 579–601; original PDF page 20, printed p. 14.

14. **Line 226 — apply the declared paraphrase-only treatment.**

    **Current:**
    > "Launching a reporting system without first establishing a Just Culture" [V]

    **Replacement:**
    > introducing an error-reporting system before establishing a just culture

    Retain the sentence’s concluding `[AP]` marker.

    **Evidence:** tape 3284. This also resolves the contradiction with lines 7 and 303.

The source card’s stale word counts and cross-volume provenance require separate attention; they are not included in this list of edits to `post-audit-deep.md`.

**4. Counts**

Counts use **finding groups**, preserving the blind auditor’s twelve numbered groups and adding the fixer’s two independent findings, F2 and F6. Shared findings are counted once.

| Outcome | Count |
|---|---:|
| Confirmed and fixed | 4 |
| Confirmed, fix incomplete | 2 |
| Missed entirely by the fix-in-place audit | 7 |
| **Confirmed defects, total** | **13** |
| Over-flagged — blind auditor | 0 |
| Over-flagged — fixer | 0 |
| Disputed | 1 |
| New defects introduced by fixer | 0 |

The seven entirely missed groups are **B2, B4, B6, B7, B9, B10 and B12**. B1 and B5 also retain unfixed components, recorded under incomplete fixes.

Of the blind auditor’s twelve groups, eleven are confirmed and one is disputed. All nine fixer changes are accounted for: F1/F5/F8 map to B1; F3 to B3; F4 to B5; F7 to B8; F9 to B11; F2 and F6 stand independently.

**5. Gate verdict**

**Current verdict: fail.**

**Once the fourteen remaining edits are applied: pass for the deep reference’s declared text-only scope.** The edits remove the confirmed residual defects and resolve the disputed summary using directly supported wording. The TOC has body coverage, and the independent verbatim check is clean.

This verdict does not certify recovery of the omitted matrix assignments or diagram connections. The unchanged source card and derived artefacts also remain outside this sort’s certification; downstream re-derivation and stamping are still required by the Pass I procedure.