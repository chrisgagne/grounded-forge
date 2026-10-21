**Blind audit result: six defects. The frozen reference requires correction before passing Pass I.** No files were edited.

**1. Material read**

Read in full:

- `blind-brief.md`, all three calibration fixtures, and `pass-i-spec.md`.
- `frozen-deep.md`, lines 1–543.
- `tape.md`, lines 1–1436.
- `source-card.md`, `frozen-deep.sha256`, and the acquisition manifest.
- All text labels in the three locally available SVG originals.

Checked the original HTML programmatically in full and inspected relevant markup. Reconversion with `pandoc -f html -t gfm --wrap=none` reproduced `tape.md` **byte for byte**. The frozen reference’s SHA-256 matches `frozen-deep.sha256`.

Inspected SVG text and positioning attributes; did not visually inspect embedded raster content. No finding below depends on interpreting that content. Consulted the live GOV.UK page for publication metadata and licensing. Did not read linked secondary works or the parallel auditor’s findings.

**2. Findings**

1. **Deep line 5 — unsupported provenance: update date.**

   **Problem:** The reference attributes an update on **2025-11-24** to the acquisition record. That record contains `public_updated_at: 2025-07-30T00:00:00+01:00`; it contains no November update date. Neither the supplied HTML body nor the tape supplies that date. The live page gives publication as 30 July 2025. [GOV.UK publication record](https://www.gov.uk/guidance/the-aqua-book)

   **Exact fix:** Strip:

   > with the GOV.UK record updated 2025-11-24,

   Keep the supported publication date.

2. **Deep line 534 — incorrect provenance: tape checksum.**

   **Problem:** The stated tape hash, `f5734e…bfd4d3`, does not match either the supplied tape or the acquisition manifest.

   **Evidence:** SHA-256 calculated from the complete `tape.md`; acquisition manifest line 24. The tape has the stated 1,436 lines.

   **Exact fix:** Replace the tape checksum clause with:

   > sha256 `c8ff4140884f8d7cdb3d4e130f2e11197235dfde8dcce3c314e85ae9fc1ada1d` (matches the manifest’s `tape_sha256`).

3. **Deep line 534 — incorrect provenance: HTML checksum.**

   **Problem:** The stated HTML hash, `256b92…61ff`, does not match either the supplied original or the acquisition manifest.

   **Evidence:** SHA-256 calculated from the complete `source.html`; acquisition manifest line 8. The source-card checksum correctly matches this HTML.

   **Exact fix:** Replace the HTML checksum clause with:

   > has sha256 `7182986afa6388ec31d3195ba07d01c214e16674f81c29a760c3b94f882009e0` (matches `html_sha256`).

4. **Deep line 459 — broadened requirement: agreement of definitions.**

   **Problem:** “Definitions and thresholds should … be agreed by the director of analysis” extends the director-agreement recommendation to definitions. The source requires both definitions and thresholds to align with the risk framework, but specifies director agreement only for thresholds.

   **Evidence:** Tape lines 1334–1336.

   **Exact fix:** Replace:

   > definitions and thresholds should align with the organisation’s risk framework and be agreed by the director of analysis or equivalent

   with:

   > definitions and thresholds should align with the organisation’s risk framework; thresholds should be agreed by the director of analysis or equivalent

5. **Deep line 505 — unsupported attribution: origin of modal conventions.**

   **Problem:** Calling the UK Government Functional Standards “the source of” the conventions asserts derivation. The passage establishes consistency, not origin.

   **Evidence:** Tape lines 118–127 list the conventions and say the usage is consistent with the Functional Standards.

   **Exact fix:** Replace the entry with:

   > UK Government Functional Standards: the book says its modal-verb usage is consistent with these standards [BT] (Ch 1, “1.3 How to use this book”).

6. **Deep line 507 — overbroad description of cross-reference coverage.**

   **Problem:** Grouping the Uncertainty Toolkit and the NAO guide as “recommended throughout for assessing, quantifying and communicating uncertainty” attributes the Toolkit’s repeated, stage-specific treatment to both works. The NAO guide is mentioned in the uncertainty definition and in guidance for decision makers and senior leaders; the later stage-specific references concern the Toolkit.

   **Evidence:** NAO references: tape lines 352 and 616. Toolkit references: lines 153, 356, 864, 970, 1117 and 1296.

   **Exact fix:** Replace the entry with:

   > Uncertainty Toolkit for Analysts in Government: cited across the principles, definitions and life-cycle chapters for assessing, quantifying and communicating uncertainty [BT] (Ch 1, “1.3.4 Uncertainty”; Ch 2, “Uncertainty”; Chs 6 to 9, uncertainty sections). The NAO good practice guide on managing uncertainty is linked in the uncertainty definition and recommended for decision makers and senior leaders [BT] (Ch 2, “Uncertainty”; Ch 4, “4.5 Uncertainty in analysis”).

**3. Counts and required checks**

The audit checked **233 claim-bearing units**: paragraphs, list entries, blockquotes and table rows. Compound units were checked clause by clause; this is not an invented atomic-claim count. Five units contain the six defects above.

Also checked:

| Check | Count/result |
|---|---:|
| Evidence-marker occurrences | 362 |
| Quotation spans checked mechanically | 142 |
| Blockquotes checked against source text | 4 |
| Key-statistics rows | 14 |
| Provenance defects | 3 |
| Unsupported attribution | 1 |
| Broadened scope or requirement | 2 |
| Verbatim or evidence-marker defects | 0 |
| Missing source sections | 0 |
| Uncited authors or works introduced | 0 |
| Task-application or post-source vocabulary defects | 0 |

**Statistics:** All 14 rows match the tape. This includes the fourteen named group members, four roles, four stages, six RIGOUR elements, ten assurance factors, four illustrated interventions, four risk levels, six verification classes, nine maturity assessment areas, annual publication frequency, 2024–25 funding year and eleven handover-documentation bullets. No empirical sample sizes, effect estimates or significance levels are reported.

**Limitations:** There is no separate list of methodological limitations. The limitations and qualifications distributed through the reference match those the source states: no definitive single quality test, inherent uncertainty, residual risk, constraints on assurance, urgent-analysis exceptions, data limitations and restrictions on appropriate publication. I found no invented methodological verdict.

**Coverage:** All ten chapters, acknowledgements, closing material and substantive subsections receive coverage. No undeclared partial textual coverage was found.

**4. Over-flag guard**

- **Four blockquotes:** All match their source passages after removing quotation delimiters and presentation syntax. No smart-quote substitution or wording correction is needed.
- **Mixed prose around `[V]` markers:** Lines such as 41 and 144 contain exact quoted excerpts within paraphrased sentences. The markers have identifiable verbatim content; they are not the fixture’s quotation-free `[V]` failure.
- **SVG-specific claims:** Local originals exist and support the reported labels and positioning. The acquisition manifest’s “remote, not fetched” image statuses are stale; they do not establish that the reference invented the labels.
- **Three images versus four occurrences:** There are three distinct image assets; the lifecycle diagram appears twice. “Three images” is defensible as an asset count.
- **Source typos and awkward wording:** The recorded anomalies are present in the HTML as well as the tape. Explicitly disclosed paraphrasing of malformed wording does not constitute a fabricated quotation.
- **“Positions … frames against”:** The source explicitly rejects verification-only assurance, interpreting independence as excluding analyst assurance, disproportionate effort, isolated interventions and a linear lifecycle. These are supported oppositions. “Taken one at a time” is reasonably read as selecting interventions singly in this context, rather than imposing a temporal prohibition.
- **Named methods, AI vocabulary and software approaches:** These appear in the source. They are neither imported task guidance nor post-source terminology.
- **Borrowed-through references and approving labels:** The named works are cited by the source, and recommendations generally support the approving descriptions. Findings 5 and 6 concern the precise relationships asserted, not the existence of those citations.
- **Authorship and licence:** Collective authorship is supported; no role is invented for Alec Waterhouse. The licence is supported by the acquisition evidence and the [GOV.UK footer](https://www.gov.uk/guidance/the-aqua-book). The source-card’s HTML checksum is correct.