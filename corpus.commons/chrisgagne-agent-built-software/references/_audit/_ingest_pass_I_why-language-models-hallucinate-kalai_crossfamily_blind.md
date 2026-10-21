## 1. Reading and audit scope

Read in full:

- `blind-brief.md`, all three calibration fixtures, and `pass-i-spec.md`.
- `frozen-deep.md`, lines 1–363.
- `tape.md`, lines 1–1161, including all six appendices, eight footnotes, and 94 bibliography entries.
- `source-card.md`, lines 1–59, and `frozen-deep.sha256`.
- Repository operating instructions and the prescribed architecture documents.

The frozen reference’s SHA-256 matches `frozen-deep.sha256`.

No original PDF, TeX/BBL files, or image assets are present in this folder. I therefore checked textual figure claims against the captions, but could not independently verify the images, PDF checksum, page count, conversion-tool versions, acquisition history, or the ingester’s claimed visual inspection. These remain **unverified provenance claims**, not demonstrated falsehoods.

I ran `check-verbatim.py` against the supplied tape. Its output was reviewed manually: several reported “no-quote” cases are displayed equations or blockquotes followed by standalone markers.

**Decision: fail pending correction.** No files were changed. This response is the complete report; the filesystem is read-only.

## 2. Numbered findings

### 1. Missing substantive coverage of §2, “Related work”

**Deep lines:** 9, 11; body as a whole.  
**Class:** Coverage omission; TOC-versus-body-anchor mismatch.  
**Evidence:** Tape 83–95.

The structure lists §2, but the body never cites or summarises it. Good–Turing discussion elsewhere does not cover the section’s other substantive content.

**Exact fix:** Insert the following section, with subsequent reference-section numbering adjusted:

> ### Related work (§2)
>
> The authors describe their reduction from binary classification to density estimation as novel to their knowledge, while identifying reductions between learning problems as an established technique [AP] (§2, “Related work”).
>
> The reviewed literature identifies factors including overconfidence, decoding randomness, snowballing, long-tailed samples, misleading alignment training, spurious correlations, exposure bias, the reversal curse, and context hijacking [AP] (§2, “Related work”).
>
> The closest theoretical predecessor connects Good–Turing missing-mass estimates to hallucinations, but does not include prompts, uncertainty expressions, connections to supervised learning, or post-training modifications. The section also describes a validity-oracle learning algorithm that is statistically efficient but not computationally efficient, and theoretical work on trade-offs between avoiding invalid outputs and generating diverse valid content [AP] (§2, “Related work”).
>
> Reported mitigation methods include RLHF, RLAIF, and DPO. Other cited studies examine hallucination rates initially decreasing and later increasing during fine-tuning on novel information, predictive signals of factual accuracy and uncertainty in queries and internal activations, and inconsistencies across semantically related queries [AP] (§2, “Related work”).
>
> The authors distinguish the development of hallucination evaluations from barriers to their adoption, citing the 2025 AI Index report’s observation that these benchmarks have struggled to gain traction. They also discuss nuanced linguistic expressions of uncertainty and the relevance of pragmatics [AP] (§2, “Related work”).

Restore coverage rather than weakening the completeness declaration.

### 2. Reversed direction of the formal reduction

**Deep line:** 17.  
**Class:** Technical misstatement.  
**Evidence:** Tape 85, 103, 147, 454.

“Reducing valid generation to an IIV binary-classification problem” reverses the stated reduction. The authors reduce classification to density estimation by constructing a classifier from a generative model.

**Exact fix:** Replace the affected sentence with:

> The authors formalise this by constructing an **Is-It-Valid (IIV)** binary classifier from a base language model and lower-bounding the model’s generation error in terms of that classifier’s error [AP] (§1.1, “Errors caused by pretraining”; §3.1, “The reduction without prompts”).

### 3. Unsupported interpretation of the title

**Deep line:** 19, first sentence.  
**Class:** Source-external analytical framing; invented opposition.  
**Evidence:** Tape 233, 343, 426 support multiple factors and bounded assumptions, but do not discuss how the title should be interpreted.

**Exact fix:** **Strip**:

> The title should not be read as asserting one universal mechanism.

Retain the remainder of the paragraph.

### 4. Dissertation example overstates fabricated institutions

**Deep line:** 38, second sentence.  
**Class:** Factual overstatement.  
**Evidence:** Tape 44–48; bibliography entry at 1025.

The reference says all three models “invented” institutions. GPT-4o supplied CMU, which agrees with the dissertation bibliography entry. The source expressly establishes that none supplied the correct **title or year**.

**Exact fix:**

> Three models supplied different titles, institutions, and years for Kalai’s doctoral dissertation; none supplied the correct title or year [AP] (§1, Table 1).

### 5. `[V]` extends to paraphrased calibration-definition prose

**Deep line:** 90.  
**Class:** Evidence-marker mismatch.  
**Evidence:** Tape 151–157.

The displayed inequality matches the source mathematically, but “where … for the above-threshold set” is paraphrased prose.

**Exact fix:** Change line 90’s `[V]` to `[AP]`. Retain the displayed inequality.

### 6. `[V]` marks paraphrased prompted-setting prose

**Deep line:** 105.  
**Class:** Evidence-marker mismatch.  
**Evidence:** Tape 215, 219–225.

The classifier description and explanation of \(\delta\) are paraphrases, not verbatim source wording.

**Exact fix:** Change line 105’s `[V]` to `[AP]`. Retain the displayed bound.

### 7. One `[V]` marker covers a quotation and subsequent paraphrases

**Deep line:** 119.  
**Class:** Evidence-marker mismatch.  
**Evidence:** Tape 198–200.

The opening quoted sentence matches the source heading after removing emphasis markup. The remaining sentences are paraphrases.

**Exact fix:** Place `[V]` immediately after the opening quotation, with its existing source anchor. End the remaining paraphrased material with `[AP]` and the same anchor.

### 8. Theorem 2 upper-bound summary uses `[V]` and adds an unstated interpretation

**Deep line:** 147.  
**Classes:** Evidence-marker mismatch; source-external analytical framing.  
**Evidence:** Tape 271–274, 719–765.

The sentence is not verbatim. “Showing that the dependence is not merely an artefact of the lower-bound technique” is an interpretation the authors do not state.

**Exact fix:**

> Theorem 2 also states that an efficient algorithm produces a calibrated model with \(\delta=0\) and, with probability at least 99%,  
> \[
> \operatorname{err}\le\operatorname{sr}
> -\frac{\operatorname{sr}}{\max_c|\mathcal E_c|+1}
> +\frac{13}{\sqrt N}.
> \]
> [AP] (§3.3.1, Theorem 2).

### 9. Missing-mass description obscures the joint probability

**Deep line:** 135, second sentence.  
**Class:** Changed probability interpretation.  
**Evidence:** Tape 558–570, particularly 567.

“Probability that a future answered prompt was not answered” can read as conditional on the future sample being answered. The defined missing mass is the **joint** probability of an unanswered-in-training prompt and a non-IDK future response.

**Exact fix:**

> The singleton rate \(\operatorname{sr}=|\mathcal S|/N\) estimates missing mass: the probability that a fresh training-distribution sample has a non-IDK response and its prompt had no non-IDK response in the training sample [AP] (§3.3.1, Definition 2; Appendix B, Lemma 1).

### 10. Formal-setting assumptions are omitted

**Deep lines:** 96–107, 199–208; limitations summary.  
**Class:** Dropped setting qualifiers.  
**Evidence:** Tape 215, 888, 1153.

The reference omits the finite-string-space assumption and the authors’ qualification that training dialogues drawn from the same prompt distribution are unrealistic. Finiteness is explicitly used in Observation 1’s proof.

**Exact fix:** Add after line 96:

> The analysis assumes a finite set of plausible strings for simplicity. In the prompted setting, training examples are valid dialogues drawn from the same prompt distribution used in the analysis; the authors call this assumption unrealistic and suggest that its failure may produce higher error rates [AP] (§3.2, “The reduction with prompts”; footnote 4).

### 11. Search limitation drops “may”

**Deep line:** 267, last sentence.  
**Class:** Dropped qualifier; over-broad finding.  
**Evidence:** Tape 438.

The source says search **may not help** with letter-counting or other intrinsic hallucinations. “Does not directly solve” states a stronger conclusion.

**Exact fix:**

> Search may not help with miscalculations such as letter miscounting or other intrinsic hallucinations [AP] (§5, “Search (and reasoning) are not panaceas”).

### 12. Lemma 2 summary drops a factor of two

**Deep line:** 295, first sentence.  
**Class:** Changed mathematical quantity.  
**Evidence:** Tape 622–625.

Lemma 2 lower-bounds **twice** IIV error by singleton rate minus a finite-sample term. The reference describes a lower bound on IIV error itself.

**Exact fix:**

> Lemma 2 states that, for any \(N\ge1\), \(\gamma\in(0,1]\), and algorithm outputting \(\hat p\), with probability at least \(1-\gamma\),
> \[
> 2\operatorname{err}_{\mathrm{iiv}}
> \ge\operatorname{sr}
> -\frac{6\ln(3N/\gamma)}{\sqrt N}.
> \]
> [AP] (Appendix B, Lemma 2).

Retain the following sentence about independence.

### 13. Source-integrity notes omit visible conversion losses

**Deep lines:** 7, 11, 357, 363.  
**Source-card lines:** 36–46.  
**Class:** Missing source-integrity caveat.  
**Evidence:** Tape 85–95, 169, 279, 853, 1079, 1131, among other locations.

Numerous in-text citation identities are blank. Bibliography titles also contain visible losses, including “-4 Technical Report” and an empty title at line 1131. Retaining 94 bibliography entries does not establish citation-level completeness.

**Exact fix:** Add to the deep reference’s source-integrity notes and the source card’s conversion description:

> **Conversion caveat:** The tape contains six appendices, eight footnotes, and 94 bibliography entries, but many in-text citation identities are missing and some bibliography titles are incomplete. Resolving those identities and verifying citation-level fidelity requires the original TeX/BBL or PDF.

Do not infer missing attribution solely from the bibliography.

## 3. Counts and required checks

**Claims checked:** 118 claim-bearing audit units in the deep reference, counting each substantive paragraph, list item, displayed result, blockquote, metadata assertion, or evidence-map row once. Compound statements and all table cells were traced within those units; this is not an inflated atomic-sentence count. The complete source card was checked separately.

**13 findings**, grouped by primary class:

| Primary class | Count |
|---|---:|
| Coverage omission | 1 |
| Technical reduction-direction error | 1 |
| Source-external analytical framing | 1 |
| Factual overstatement | 1 |
| Evidence-marker mismatch | 4 |
| Probability interpretation / dropped setting qualifiers | 3 |
| Changed mathematical quantity | 1 |
| Missing conversion-integrity caveat | 1 |

Finding 8 also contains source-external framing.

**Key statistics:** There is no key-statistics table. The eight-row evidence map is substantively supported. Displayed main-theorem bounds, the 50/50 mixture, trigram error of at least one half, benchmark counts, and HLE accuracy below 30% match the tape. The numerical defect is the omitted factor of two in the Lemma 2 prose summary.

**Authors’ limitations:** All six named §5 discussion topics are represented. The list substantially matches the authors’ limitations, subject to the strengthened search statement in finding 11. The additional formal assumptions in finding 10 should also be recorded.

**Quotation check:** All five blockquotes match the tape’s textual content. The italic emphasis in the base-model heading is preserved. No blockquote wording repair is required.

## 4. Over-flag guard

- **Penalty 2 at \(t=0.75\), line 240:** The tape itself gives this value at line 416, although \(t/(1-t)=3\). This is a source inconsistency, not an introduced numerical mismatch. Do not silently correct it while presenting the result as faithful paraphrase.
- **Displayed equations marked `[V]`, lines 161 and 206:** Their mathematical content matches the source. The reference expressly permits `[V]` for reproduced displayed results. The checker’s “no-quote” reports do not establish defects here.
- **Standalone `[V]` markers after blockquotes:** The adjacent blockquotes supply the verbatim text. These are checker extraction limitations, not marker violations.
- **“Socio-technical”:** Explicitly supplied and explained by the authors at tape 16 and 355.
- **GIGO’s unformalised treatment:** Tape 349 explicitly says its statistical similarity is self-evident and explains why no formal treatment is supplied.
- **Poor modelling as a larger contributor to letter-counting errors:** Tape 347 states this interpretation; it is not auditor-invented causation.
- **Retrieval is not described as ineffective, line 269:** Tape 438 explicitly acknowledges reduced hallucinations before describing remaining failures. This boundary summary is supported.
- **Calibration distinctions and cautious theorem summaries:** Tape 169–200 and the formal statements support the distinction between threshold-specific calibration, stronger calibration notions, and post-training behaviour.
- **Model and causal boundary notes, lines 361–362:** These accurately delimit what the formal results and benchmark review establish. They do not introduce an unsupported methodological verdict.
- **PDF/image inspection and acquisition assertions:** Unverifiable from the supplied folder, but absence of the originals does not prove that the ingester failed to inspect them.
- **No uncited cross-author connection, task-application checklist, or post-source terminology:** None identified.