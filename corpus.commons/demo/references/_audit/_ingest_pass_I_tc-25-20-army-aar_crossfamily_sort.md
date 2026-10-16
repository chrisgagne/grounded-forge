## 1. What I read

Read in full: `sort-brief.md`, `pass-i-spec.md`, all three calibration fixtures, both audit reports, `post-audit-deep.md` (296 lines), `tape.md` (1,413 lines), and `source-card.md`. I compared the frozen and post-audit references and read both auditors’ briefs to establish their original scope.

I independently checked the relevant AAR and retro distillation passages, light-reference passages, and Markdown index rows. For the original, I checked PDF metadata, deterministically extracted PDF pages 6–8 and 16–17, and visually inspected page 16, containing Figure 3-2: (`_planning/pass-i/demo/tc-25-20-army-aar/source.pdf`)

Both reference manifests match their files. The post-audit SHA-256 is:

`6429e0b66aea6979b7a8daf394000902ddfd92752ec82a3eb1b391c054df319b`

The verbatim checker reports one `near` match at line 178, attributable to conversion spacing and intervening page furniture.

This report sorts the scoped re-audit findings and checks the actual edits. It does not replace the historical audit of unchanged material. No files were modified.

## 2. Sorted ledger

Duplicate findings are consolidated. “Deep” means `post-audit-deep.md`; derived filenames below are relative to `corpus.commons/demo/distillations/`.

| ID | Finding and auditor | Classification | Deep line; source evidence | Determination |
|---|---|---|---|---|
| 1 | Figure 4-1 falsely described as captured verbatim — blind finding 1; fixer change 3 | **Confirmed and fixed** | Deep **290**, referring to **149**; tape **765–798** | Line 149 abbreviates the outline, omits parenthetical wording and joins items with arrows. Line 290 now accurately describes it as an outline of the headings. |
| 2 | Figure 4-1 outline incorrectly marked `[V]` — fixer’s first “Left open” item | **Confirmed and fixed** | Deep **149**; tape **767–796** | The outline is a paraphrase. The actual snapshot carries `[AP]`, although the fixer log still describes this correction as open. No further edit is needed. |
| 3 | Figure 3-2 absent from the image-content caveat — fixer’s second “Left open” item | **Confirmed and fixed** | Deep **290**; tape **642–643**, **667**, **720–724**; PDF pages **16–17** | The snapshot now identifies both image-only figures. The page-16 render confirms that Figure 3-2 contains handwritten comment cards. This corrects the completeness of the integrity note; it does not establish that the handwritten contents were ingested. |
| 4 | Exhaustive planning checklist omits two document types — blind finding 2; fixer calls the question consistent | **Missed by the fix-in-place audit** | Deep **72** is correct; `aar/tc-25-20-army-aar-aar.md:56`; tape **295–302**, especially **296–297** | The question promises “each Figure 1-4 planning action” but mentions only reviewing the training and evaluation plan. The source also requires reviewing ARTEP mission training plans and soldier training publications. The derived defect remains. |
| 5 | Figure 4-1 restricted to formal AARs — blind finding 3; also recognised in fixer’s derived-tier notes | **Missed by the fix-in-place audit**, under the brief’s definition of an unresolved blind finding | Deep **46**, **149** are unrestricted; `aar/tc-25-20-army-aar-aar.md:44`; tape **151–156**, **232–235**, **765–798** | The source calls this a recommended sequence for conducting “an AAR”. Informal AARs use the standard format. Tape **829–831** restricts the OPFOR commander’s contribution to formal AARs, not the entire outline. The fixer detected this defect but left it unresolved in the derived tier. |
| 6 | “Three items carry a gloss” allegedly asserts an inaccurate total — fixer change 2 and proposed propagation | **Over-flagged — fixer** | Deep **46**; tape **185–194**, particularly **187**, **190–191** | The sentence identifies three particular explanatory glosses; it does not say that only three items contain parentheses. All three glosses are present. Additional parentheticals do not falsify that bounded statement. The replacement “The parentheticals include” is accurate and can remain, but the edit was not required. The same applies to the corresponding “glosses three” wording in AAR concept 17, retro concept 13 and both index rows. |
| 7 | “The same emphasis opens the circular” — fixer change 1 | **Disputed** | Deep **17**; tape **89–93**, **166–178**, **800–809** | **Fixer’s reading:** the phrase locates Figure 1-1 at the circular’s opening and attributes an explicit climate framing to that figure. **Alternative reading:** “opens” describes the introductory material broadly, and participation/open-ended questions repeat the climate emphasis. The Preface explicitly discusses climate, and Chapter 4 explicitly connects these practices to atmosphere. The original is imprecise rather than demonstrably source-external. The replacement accurately states the correspondence and needs no revision. |

**Confirmed, fix wrong or incomplete:** none in the changed deep-reference passages. The two unresolved substantive defects are in the AAR distillation.

### Other determinations and new-defect check

- **Restored figures:** deep lines **44–58**, **70–78** and table rows **265–266** agree with tape **166–329**. The eight-point and ten-item counts are correct.
- **“tutors training plans”:** retain. Tape **325–326** and PDF page **8** carry that wording.
- **Planning/Preparation order:** deep line **78** correctly describes the correspondence with the Chapter 2 and Chapter 3 section sequence.
- **Grouped conducting sequence:** deep lines **46** and **149** accurately summarise the relationship between Figures 1-2 and 4-1; they need not reproduce identical formatting.
- **C2:** deep line **178** matches tape **895**. Its checker warning concerns “Figure 4-2” spacing and the inserted header/folio at tape **877–887**, not altered author wording.
- **Derived mappings:** the Sprint Goal/plan question and assessment-recipient question are permissible task guidance, supported by tape **187**, **190–191** and **327**. They are not deep-tier source claims.

**No verified new defect was introduced by the edits.** The revised thesis correspondence, parenthetical wording, `[AP]` marker and Figure 4-1 description are accurate.

The new sentence at deep line **290** reporting an all-page Tesseract check is a historical process assertion. I did not reproduce that OCR run or inspect its receipt. Its presence is not independently verified here; that alone does not establish falsity or justify a source-only strip. The same distinction applies to earlier conversion and reading-history assertions.

## 3. Remaining edits

**Changes still needed in `post-audit-deep.md`: none verified.** The two corrections described as open in the fixer log are already present in the supplied snapshot.

The following **derived-tier changes remain necessary**. They are listed separately because editing the deep reference cannot repair them.

1. **`aar/tc-25-20-army-aar-aar.md:56` — replace the question.**

   **Current:**

   > Has each Figure 1-4 planning action been done: OCs selected and trained, the training and evaluation plan reviewed, AAR timing set, attendance decided, sites and training aids chosen, the AAR plan reviewed (Source: *TC 25-20*, Ch 1, Figure 1-4)?

   **Replacement:**

   > Has each Figure 1-4 planning action been done: qualified OCs selected and trained; the training and evaluation plan, ARTEP mission training plans and soldier training publications reviewed; AAR timing identified; attendance determined; potential sites selected; training aids chosen; and the AAR plan reviewed (Source: *TC 25-20*, Ch 1, Figure 1-4)?

   **Verified against:** tape **295–302**.

2. **`aar/tc-25-20-army-aar-aar.md:44` — replace the final sentence.**

   **Current:**

   > The format is the skeleton a facilitator can run in order; Figure 4-1 expands it for the formal AAR.

   **Replacement:**

   > The format is the skeleton a facilitator can run in order; Figure 4-1 gives a recommended sequence for conducting an AAR as a grouped outline with additional discussion subtopics.

   **Verified against:** tape **151–156**, **232–235**, **765–798**.

No change to the derived “glosses three” passages is required.

## 4. Counts

Counts are deduplicated by issue; repeated derived occurrences are not counted separately.

| Classification | Count |
|---|---:|
| Confirmed defects, total | **5** |
| — Confirmed and fixed | **3** |
| — Confirmed, fix wrong or incomplete | **0** |
| — Missed/unresolved blind findings | **2** |
| Over-flagged — blind auditor | **0** |
| Over-flagged — fixer | **1** |
| Disputed | **1** |
| Verified new defects introduced | **0** |

Of the two unresolved blind findings, the fixer **missed the checklist omission** and **recognised but deferred the formal-AAR restriction**.

## 5. Gate verdict

**FAIL for completion of the scoped ingestion gate.** The two verified AAR-distillation defects remain, and the derived tier still requires re-derivation/review and provenance stamping against the final audited deep reference.

**The scoped deep-reference content passes this sort:** no further verified edit to `post-audit-deep.md` is required. Once the two derived corrections and required provenance work are completed, this sort identifies no remaining blocker within the scoped re-audit.