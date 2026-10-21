## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md`, and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, lines 1–363.
- `frozen-deep.md`, lines 1–363, and the complete diff between the two references.
- `tape.md`, lines 1–1161, including all appendices, bibliography entries and footnotes.
- `source-card.md`.
- The repository’s `CLAUDE.md` and its nine prescribed architecture documents.

The post-audit reference matches its supplied SHA-256:

`b2fda0e111db2a1f5d665738b8abf824b0923f12a5677a44a7cd1e3b79f16ac9`

I ran `check-verbatim.py` on `post-audit-deep.md` with `tape.md` explicitly supplied as the source. It reported no findings. That checks quotation wording; it does not establish that a marker correctly classifies surrounding prose.

No original PDF, TeX/BBL files or figure assets are present. Image inspection and acquisition-history claims therefore remain independently unverified. Their absence does not demonstrate that the original ingester’s inspection claims were false.

No files were changed. This response is the complete report.

## 2. Sorted ledger

All deep-reference locations below refer to **post-audit** line numbers. Removed wording was checked in `frozen-deep.md`. Compound findings are split where they concern independently assessable defects.

### Confirmed and fixed

| ID | Finding | Raised by | Post-audit line | Tape evidence | Assessment |
|---|---|---|---:|---|---|
| C1 | §2 lacked body coverage despite appearing in the structure declaration | Both | 326–335 | 83–95 | The added section restores substantive related-work coverage and the missing section anchor. |
| C2 | Unsupported instruction about how to interpret the title | Both | 19 | 343 | Correctly replaced with the authors’ explicit multiple-factor statement. |
| C3 | Dissertation example said all three models invented institutions | Both | 38 | 44–48; 1025 | Correctly narrowed to incorrect titles and years. CMU was consistent with the bibliography. |
| C4 | `[V]` covered paraphrased calibration-definition prose | Both | 90 | 151–157 | Correctly changed to `[AP]`; the bound remains mathematically faithful. |
| C5 | `[V]` covered paraphrased prompted-setting prose | Both | 105 | 213–225 | Correctly changed to `[AP]`. |
| C6 | One `[V]` covered a heading quotation and subsequent paraphrases | Both | 119 | 198–200 | Correctly separated into a quoted heading and marked explanatory prose. |
| C7 | Theorem 2 upper-bound summary was incorrectly marked `[V]` | Both | 147 | 271–274 | Correctly replaced with an explicit, paraphrased statement of the upper bound. |
| C8 | Upper-bound summary added the ingester’s “not merely an artefact” interpretation | Both | 147 | 265–274; 719–765 | The bounds support a mathematical comparison, but the source does not state this interpretive verdict. Correctly removed under the source-only standard. |
| C9 | “Verified” added an unsupported qualification to the fixed-question system | Fixer | 119 | 200 | The source specifies a question-answer database, calculator and IDK fallback; it does not describe a verification process. The replacement is faithful. |
| C10 | Search limitation strengthened “may not help” into “does not directly solve” | Both | 265 | 438 | Correctly restored the source’s hedge. |

### Confirmed, fix wrong or incomplete

**None among the defects the fixer expressly raised in the deep reference.**

The conversion-integrity finding below remains incomplete despite the fixer adding a narrower note about missing author names. The fixer did not expressly identify the deep reference’s broader completeness-caveat defect.

### Missed by the fix-in-place audit

| ID | Finding | Raised by | Post-audit line | Tape evidence | Assessment |
|---|---|---|---:|---|---|
| M1 | Direction of the formal reduction is reversed | Blind, finding 2 | 17 | 56; 67; 85; 147 | The authors reduce classification to density estimation by constructing a classifier from a generative model. “Reducing valid generation to … binary-classification” reverses that direction. |
| M2 | Finite-string-space assumption omitted | Blind, finding 10 | 96; 199–208 | 888; 1153 | Finiteness is stated explicitly and used in Observation 1’s proof. It should accompany the formal-setting summary. |
| M3 | Same-prompt-distribution assumption and its acknowledged unrealism omitted | Blind, finding 10 | 96–107 | 213–215 | The reference records the prompt distribution but omits the authors’ express qualification about training dialogues drawn from that distribution. |
| M4 | Lemma 2 summary drops the factor of two | Blind, finding 12 | 293 | 622–625 | The lemma lower-bounds **twice** IIV error by singleton rate minus the correction term. The unchanged summary states a stronger bound. |
| M5 | Source-integrity notes omit the full extent of visible conversion losses | Blind, finding 13 | 7; 11; 328; 357 | 85–95; 963; 1079; 1131 | Line 328 acknowledges missing in-text names. It does not disclose damaged bibliography titles or qualify citation-level completeness. Counting 94 entries does not establish intact attribution. |

Blind finding 13 also concerns `source-card.md`. That external-file component is excluded from the deep-reference capture count and from the remaining edits below.

### Over-flagged

These are **fixer** findings. The replacements are generally source-faithful, so their unnecessary removal or rewording does not require restoration.

| ID | Finding rejected | Post-audit line | Tape evidence | Why it does not establish a defect |
|---|---|---:|---|---|
| O1 | “Deliberately limited calibration claim” | 115 | 169; 196; 869 | The authors explicitly distinguish this weak, single-threshold condition from stronger calibration notions. |
| O2 | The result does not establish calibration of every post-trained confidence statement | 115 | 196; 200 | This accurately limits a threshold-specific base-model result. |
| O3 | “Emphatic qualifier” | 119 | 198 | The source itself italicises “only for base models”. Calling that emphasis emphatic is supported. |
| O4 | Theorem 2 does not equate every deployed model’s measured hallucination rate with singleton rate | 149 | 241; 265–274 | This is an accurate scope boundary for a specified random model and high-probability bounds. |
| O5 | Observation 1 is a decision-theoretic property rather than an empirical training-run result | 208 | 361–368; 888–893 | The observation optimises expected score over beliefs about graders. The description accurately identifies what the result establishes. |
| O6 | Retrieval is not ineffective, but does not remove every failure mode | 267 | 438 | The source expressly acknowledges reduced hallucinations while retaining the guessing incentive. “Does not remove every” means that some failures remain; it does not assert that every failure remains. |
| O7 | “Another architecture” extends the analysis improperly | 52 | 32; 107 | The analysis is explicitly general, does not rely on Transformer properties, and applies to general density estimation. |
| O8 | Scoring abstentions “as wrong” | 56 | 75; 359; 361 | In the binary scheme, abstentions and incorrect answers receive the same zero score. The original wording is a supported description of grading. |
| O9 | Original paraphrase of the calibration/error implication | 119 | 161; 196; 200 | Its qualification involving difficult IIV distinctions and cross-entropy fitting traces to the source. The separate `[V]` and “verified” defects remain confirmed. |
| O10 | Distribution shift was not asserted to be the only explanation | 177 | 343; 347 | The source explicitly presents combined factors and suggests poor models may contribute more to letter-counting errors. |
| O11 | WildBench’s “partly helpful answer containing factual errors” | 220 | 925–929 | This reasonably paraphrases a “fair” response contrasted with a poor response that does not meaningfully help. The replacement is more precise, but the original does not establish a factual defect. |
| O12 | Faithfully reproduced Theorem 3 equation could not carry `[V]` because its LaTeX was re-typeset | 161 | 307–310 | The original marker definition expressly allowed reproduced displayed results. Equivalent mathematical typesetting alone does not establish paraphrased prose or changed mathematical content. |
| O13 | Faithfully reproduced Observation 1 equation could not carry `[V]` because its LaTeX was re-typeset | 206 | 365–368 | The same reasoning applies. The change to `[AP]` is acceptable, but was not a necessary defect repair. |

The five quotation-formatting changes and the accompanying marker-definition update are administrative changes, not additional confirmed defects or over-flags. The fixer acknowledged that the original blockquote wording already matched the source.

### Disputed

| ID | Finding | Raised by | Post-audit line | Tape evidence | Both readings |
|---|---|---|---:|---|---|
| D1 | “Useful assistant” in the post-training description | Fixer | 56 | 73; 355 | Strict reading: “assistant” imports a product role the source does not specify. Ordinary paraphrase reading: it describes the stated transition towards useful responses without confident falsehoods. The replacement resolves the concern without requiring a confirmed-defect count. |
| D2 | Figure 2’s post-RL model was “not similarly calibrated” | Fixer | 121 | 200; 204–208 | Text-only reading: the caption establishes only pretrained calibration, so narrowing is prudent. Image reading: the unavailable right panel might substantiate the original comparison. The source packet cannot settle that reading. |
| D3 | “Develops two factors formally and names three additional ones” | Fixer | 127 | 233; 345–349; 851–880 | Global reading: it misleadingly suggests only two factors receive formal treatment, overlooking Appendix D. Local reading: it accurately describes the organisation of §§3.3–3.4 and does not explicitly exclude later formal treatment. The replacement removes the ambiguity. |
| D4 | Missing-mass prose changes a joint probability into a conditional probability | Blind, finding 9 | 135 | 558–570, especially 567 | Conditional reading: “a future answered prompt” conditions on answering and changes the denominator. Event-description reading: “answered” is part of the event whose probability is being described. The formal source is unambiguously joint; the prose is ambiguous rather than demonstrably a different probability. |

### Defect introduced by the fixer

| ID | New defect | Post-audit line | Tape evidence | Assessment |
|---|---|---:|---|---|
| N1 | `[V]` again covers both an exact quotation and paraphrased prose | 335 | 93 | “Relatively little work has examined barriers to adopting hallucination benchmarks” paraphrases the source. The quoted AI Index wording matches, but the terminal `[V]` leaves the preceding paraphrase incorrectly classified. Split the markers. |

The other fixes introduce no confirmed new source-grounding defect. In particular, the new formulas retain their mathematical quantities, and the quotation-formatting changes retain their wording.

### Findings outside the supplied deep reference

The fixer’s derived-tier section concerns an absent light-reference file. Its quoted candidates can be compared with the tape, but the actual file and its context cannot be independently checked here:

- The deployed-rate and decision-theoretic boundary statements are supported by the theorem and observation settings.
- The “partly erroneous helpful answer” wording has the same support discussed in O11.
- “Verified” lacks the source support identified in C9; “giving up breadth” describes the database system’s restricted answering scope but adds interpretation.
- The retrieval-incentive statement traces to tape 438; intrinsic-error wording must retain the source’s hedge.
- The classical-computation wording traces to tape 345.
- “Not universal folklore” has no supporting passage identified in the tape.
- Adding related-work material to the light reference was labelled optional, not a confirmed defect.

These are excluded from the deep-reference counts. The audit log’s “same-family” label is also inconsistent with its own stated Claude auditor and GPT generator; that is an audit-log issue, not a deep-reference defect.

## 3. Remaining edits

Only the following verified changes are required in `post-audit-deep.md`.

1. **Line 17 — correct the reduction direction.**

   Current:

   > The authors formalise this by reducing valid generation to an **Is-It-Valid (IIV)** binary-classification problem and lower-bounding a base model's generation error in terms of the induced IIV classifier's error.

   Replacement:

   > The authors formalise this by constructing an **Is-It-Valid (IIV)** binary classifier from a base language model and lower-bounding that model's generation error in terms of the induced classifier's error.

   Verified against tape 56, 85 and 147.

2. **After line 96 — insert the omitted setting assumptions.**

   Current text: none; insertion after the prompted-setting paragraph.

   Replacement/addition:

   > The analysis assumes a finite set of plausible strings for simplicity. In the prompted setting, training examples are valid dialogues drawn from the same prompt distribution used in the analysis; the authors call this assumption unrealistic and suggest that its failure may produce higher error rates [AP] (§3.2, “The reduction with prompts”; footnote 4).

   Verified against tape 215 and 1153; finiteness is used at tape 888.

3. **Line 293 — restore Lemma 2’s factor of two.**

   Current:

   > Lemma 2 lower-bounds IIV error by the singleton rate, up to a finite-sample term.

   Replacement:

   > Lemma 2 states that, for any \(N\ge1\), \(\gamma\in(0,1]\), and algorithm outputting \(\hat p\), with probability at least \(1-\gamma\), \(2\operatorname{err}_{\mathrm{iiv}}\ge\operatorname{sr}-6\ln(3N/\gamma)/\sqrt N\).

   Retain the following independence sentence and its `[AP]` attribution.

   Verified against tape 622–625 and 689.

4. **After line 357 — insert the complete conversion caveat.**

   Current text: no comprehensive conversion caveat; line 328 mentions missing in-text author names only.

   Replacement/addition:

   > - **Conversion caveat:** The supplied tape contains six appendices, eight footnotes, and 94 bibliography entries, but many in-text citation identities are missing and some bibliography titles are incomplete. Section coverage and bibliography-entry counts do not establish citation-level completeness. Resolving those identities and verifying citation-level fidelity requires the original TeX/BBL or PDF.

   Verified against tape 85–95, 963, 1079 and 1131.

5. **Line 335 — separate paraphrase from quotation.**

   Current:

   > - Relatively little work has examined barriers to adopting hallucination benchmarks; the 2025 AI Index report notes they “have struggled to gain traction within the AI community.” [V] (§2).

   Replacement:

   > - The authors report that relatively little work has examined barriers to adopting hallucination benchmarks [AP] (§2). They cite the 2025 AI Index report’s observation that these benchmarks “have struggled to gain traction within the AI community.” [V] (§2).

   Verified against tape 93.

## 4. Counts

Counts use independently assessable **deep-reference defects**, not edit operations. Blind finding 8 contains two defects; blind finding 10 contains two omitted assumptions.

| Disposition | Count |
|---|---:|
| Confirmed original deep-reference defects | 15 |
| Confirmed and fixed | 10 |
| Confirmed fixer-raised defects with wrong/incomplete fixes | 0 |
| Missed by the fixer and still requiring correction | 5 |
| Over-flagged by fixer | 13 |
| Over-flagged by blind auditor | 0 |
| Disputed | 4 |
| New defects introduced by fixer | 1 |

The disputed findings comprise three fixer findings and one blind finding. External-file findings and the newly introduced defect are excluded from capture.

Capture: fixer=10 blind=14 both=9

## 5. Gate verdict once remaining edits are applied

**Pass for source fidelity against the supplied converted tape.**

The five edits correct the remaining confirmed claims, assumptions, conversion disclosure and newly introduced marker mismatch. All listed body sections and appendices then have substantive anchor coverage.

This verdict does **not** independently certify original-image inspection or citation-level conversion fidelity. Those limits must remain visible in the audit record. Before shipping derived artefacts, the light reference and any distillations must be checked or re-derived from the corrected deep reference and stamped under the prescribed provenance procedure.