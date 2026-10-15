## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md`, all three calibration fixtures, both audit reports, `post-audit-deep.md` (543 lines), and `tape.md` (1,436 lines).
- `source-card.md`, the acquisition manifest, both checksum files, the repository’s `CLAUDE.md` and its required architecture documents.

Also checked:

- Every difference between `frozen-deep.md` and `post-audit-deep.md`.
- The complete original HTML programmatically. Pandoc reconversion reproduced the tape **byte for byte**.
- All three local SVG originals’ text and structure. Extracted and visually inspected the risk matrix’s embedded PNG.
- SHA-256 values for both deep references, the tape and HTML. All current values match their supplied records.
- The post-audit reference with `check-verbatim.py --source tape.md`: **no findings**.

No files were changed. This message is the report. All deep-reference line numbers below refer to `post-audit-deep.md`.

## 2. Sorted ledger

Findings are counted separately where they concern different claims or different checksum values. Consequently, the fixer’s combined checksum finding contributes two defects.

### Confirmed and fixed

| ID | Deep line | Raised by | Source evidence | Decision |
|---|---:|---|---|---|
| C1 | 5 | Both: fixer §1; blind §1 | Acquisition manifest line 6; source-card publication statement. No tape passage supplies the November date. | The unsupported `2025-11-24` update date was correctly stripped. The revised attribution to the operator’s source record is supported by the source card. |
| C2 | 33 | Fixer §2 | Tape 118–127 | The source defines the terms and says their usage is consistent with the Functional Standards. Replacing “in the defined senses of” with the explicit relationship stated in the tape removes an unsupported attribution. |
| C3 | 39 | Fixer §3 | Tape 5 | The working group’s origin is the book’s own historical account, not information borrowed from Macpherson’s review. `[BT]` → `[AP]` is correct. |
| C4 | 211 | Fixer §4 | Tape 446–456; original `Table_3.2_risk_matrix_v2.svg` | The cells are vector rectangles, not embedded raster images. The replacement correctly describes unlabelled cells in shades of red. |
| C5 | 453 | Fixer §5 | Tape 1322; modal conventions at 118–127 | “Should” imposed the book’s defined recommendation category on wording that says “it is important”. The replacement preserves the source’s force. |
| C6 | 505 | Both: fixer §6; blind §5 | Tape 118–127 | “The source of” asserted derivation. The replacement correctly reports consistency. |
| C7 | 534 | Both: fixer §7; blind §2 | Complete tape bytes; acquisition manifest line 24 | The corrected tape hash is `c8ff4140884f8d7cdb3d4e130f2e11197235dfde8dcce3c314e85ae9fc1ada1d`. |
| C8 | 534 | Both: fixer §7; blind §3 | Complete HTML bytes; acquisition manifest line 8; source-card checksum | The corrected HTML hash is `7182986afa6388ec31d3195ba07d01c214e16674f81c29a760c3b94f882009e0`. |
| C9 | 538 | Fixer §8 | Tape 446–456; original risk-matrix SVG | The repeated claim that the cells are raster images was correctly replaced. However, the replacement introduces a separate defect, N1 below. |

### Confirmed, fix wrong or incomplete

| ID | Deep line | Raised by | Source evidence | Decision |
|---|---:|---|---|---|
| C10 | 542 | Fixer, “Open” | Source-card processing statement; acquisition manifest `post_processing`; tape 1302 and 1396 | The records confirm two operator-approved safelinks rewrites, but do **not** identify their sections. The fixer explicitly raised this verification gap and left it unresolved. The current URLs cannot establish which links previously contained wrappers. Strip the location parenthetical while retaining the documented processing history. |

C10 concerns unsupported specificity in the deep reference, not a defect in the source card. It is counted as a fixer capture because the fixer explicitly identified the unresolved claim.

### Missed by the fix-in-place audit

| ID | Deep line | Raised by | Source evidence | Decision |
|---|---:|---|---|---|
| C11 | 459 | Blind §4 | Tape 1334–1336 | The director-agreement recommendation applies to **thresholds**. The reference incorrectly extends it to definitions. Both definitions and thresholds should align with the risk framework. Still unfixed. |
| C12 | 507 | Blind §6 | NAO: tape 352, 616. Toolkit: 153, 356, 864, 970, 1117, 1296 | The grouped description attributes repeated, stage-specific uncertainty guidance to both works. That coverage belongs to the Toolkit; the NAO guide has two differently situated references. Still unfixed. |

### Over-flagged

**None by either auditor.**

The blind auditor’s guards against flagging mixed paraphrase and exact quotations, source-native errors, three distinct image assets, and source-stated oppositions are supported. Those guards are not additional defect findings.

### Disputed

**None requiring a judgement-based disposition.** The confirmed items above turn on traceable wording, file contents or provenance records.

### New defect introduced by the fixer

| ID | Deep line | Introduced by | Source evidence | Decision |
|---|---:|---|---|---|
| N1 | 538 | Fixer §8 | Original risk-matrix SVG, embedded PNG `img0`, and its placement immediately before the vector “Risk” text | The raster is **not blank**. It contains a white “Risk” graphic with varying transparency. Its 323 × 172 pixels include alpha values from 0 to 102. Describing it as “a blank white image” mistakes its appearance against white for absence of content. Correcting the vector-cell description did not justify that new assertion. |

No other introduced defect was found in the fixer’s edits.

## 3. Remaining edits

1. **Line 459 — restrict director agreement to thresholds.**

   Current:

   > definitions and thresholds should align with the organisation's risk framework and be agreed by the director of analysis or equivalent

   Replacement:

   > definitions and thresholds should align with the organisation's risk framework; thresholds should be agreed by the director of analysis or equivalent

   Verified against tape 1336.

2. **Line 507 — separate the two uncertainty references.**

   Current:

   > - Uncertainty Toolkit for Analysts in Government and the NAO good practice guide on managing uncertainty: recommended throughout for assessing, quantifying and communicating uncertainty; approving [BT] (Ch 1, "1.3.4 Uncertainty"; Ch 2, "Uncertainty"; Ch 4, "4.5 Uncertainty in analysis"; Chs 6 to 9, uncertainty sections).

   Replacement:

   > - Uncertainty Toolkit for Analysts in Government: cited across the principles, definitions and life-cycle chapters for assessing, quantifying and communicating uncertainty [BT] (Ch 1, "1.3.4 Uncertainty"; Ch 2, "Uncertainty"; Chs 6 to 9, uncertainty sections). The NAO good practice guide on managing uncertainty is linked in the uncertainty definition and presented as guidance for decision makers and senior leaders [BT] (Ch 2, "Uncertainty"; Ch 4, "4.5 Uncertainty in analysis").

   Verified against tape 153, 352–356, 616, 864, 970, 1117 and 1292–1298.

3. **Line 538 — remove the introduced blank-raster claim.**

   Current:

   > its cells are unlabelled shapes filled in shades of red, and its one embedded raster is a blank white image.

   Replacement:

   > its cells are unlabelled shapes filled in shades of red, and its one embedded raster is a white graphic with varying transparency behind the “Risk” text.

   Verified against the original SVG structure and extracted PNG.

4. **Line 542 — strip the unsupported locations of the historical rewrites.**

   Current text to **strip**, including its preceding space:

   >  (Ch 9, "9.5 Black-box models and the delivery, communication and sign-off stage"; Ch 10, "10.1.2 Guidance and advice for performing assurance")

   The resulting sentence retains the documented fact that two external links contained safelinks wrappers. The source card and acquisition manifest support that processing history, the operator’s approval date and the statement that nothing else changed; they do not support the section mapping.

## 4. Counts

| Disposition | Count |
|---|---:|
| Confirmed original defects, total | **12** |
| Confirmed and fixed | 9 |
| Confirmed, fix incomplete | 1 |
| Missed by the fixer; still defective | 2 |
| Over-flagged by fixer | 0 |
| Over-flagged by blind auditor | 0 |
| Disputed | 0 |
| New defects introduced by fixer, excluded from capture | **1** |
| Remaining edits | **4** |

Capture counts include C10, the fixer’s explicitly raised but unresolved provenance issue. They count the two hashes separately and the repeated raster-cell assertions separately because each is a distinct claim in the deep reference.

Capture: fixer=10 blind=6 both=4

## 5. Gate verdict once remaining edits are applied

**Pass**, once all four remaining edits are applied.

The reference covers the acknowledgements, all ten chapters and closing material. The quotation check is clean, and the sorted findings would then leave no confirmed source-fidelity defect outstanding.

This is a conditional content verdict. Line 543’s pending status and the formal Pass I stamp remain for the driver to update after the corrections and audit record are in place.