# Pass I source-only audit: nhs-just-culture-guide-deep.md

**Date:** 2026-05-13
**Auditor model:** claude-opus-4-7[1m]
**Deep ref under audit:** `corpus.commons/demo/references/nhs-just-culture-guide-deep.md`
**Source read at Pass C:** `corpus.commons/demo/sources/converted/nhs-just-culture-guide.md` (single-page A3 landscape poster; full content read, no section omitted).

## Calibration

Before the cold read, three audit-fixture exemplars were re-read to calibrate against known-bad and known-clean patterns:

- `tests/audit-fixtures/01-training-leakage.md` — biographical claim the source does not make.
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` — `[V]` marker on a paraphrased sentence.
- `tests/audit-fixtures/12-clean-negative-control.md` — clean negative control.

## Audit pass

Each claim in the deep reference was traced to a specific passage in the converted source (the preamble's four caveats; the three preamble paragraphs framing purpose and use; each of the five tests with their sub-questions; each of the seven recommendation end-states; the source's footer attribution). Verbatim quotations were spot-checked character-by-character against the converted markdown.

### Claims audited

The deep reference contains roughly 45 distinct claims across the thesis (5 paragraphs), Part I (caveats and framing), Part II (the five sequential tests), Part III (the seven recommendation end-states), the Key Statistics table (6 rows), the Connections list (2 entries), the Positions-framed-against section (1 entry, characterised as implicit not explicit), and the Citation and source-integrity notes. Each was checked against the converted markdown.

### Findings and fixes (applied to the deep ref before this log was written)

1. **Verbatim slip in the thesis: "support" vs "supports".** The thesis paragraph originally quoted the source as `designed to "support a conversation between managers about..."`, using the infinitive "support". The source reads "This guide supports a conversation..." with the third-person-singular "supports". The deep ref had mid-quote-shifted the tense to fit the surrounding "designed to" construction. **Action:** rewrote the sentence to introduce the quote with a direct attribution, preserving the source's exact wording ("This guide supports a conversation between managers about whether a staff member involved in a patient safety incident requires specific individual support or intervention to work safely"). The [V] marker now matches the verbatim text.

2. **Verbatim slip in caveat 2 ("Re-entrant"): dropped "the guide".** The deep ref originally rendered caveat 2 as a [V] quote: "The guide can be used at any point of an investigation, but may need to be revisited as more information becomes available." The source reads "A just culture guide can be used at any point of an investigation, but the guide may need to be revisited as more information becomes available" — the deep ref had dropped the second instance of "the guide". **Action:** re-rendered the [V] quote as "can be used at any point of an investigation, but the guide may need to be revisited as more information becomes available" — beginning the quote mid-sentence and preserving the source's word order. Added an [AP] marker on the trailing paraphrase about re-entrancy implications, separating the verbatim from the paraphrase.

3. **Verbatim slips on Q3 foresight sub-questions: slash spacing.** The deep ref originally rendered 3a as "Are there agreed protocols / accepted practice in place that apply to the action / omission in question?" and 3b as "Were the protocols / accepted practice workable and in routine use?" — adding spaces around the slashes. The source uses tight slashes (`protocols/accepted`, `action/omission`). The audit fixture `06-verbatim-capitalisation-tidy.md` (also `05-verbatim-smart-quote-tidy.md`) covers this exact class of typography-tidying slip. **Action:** restored the source's tight slashes in both 3a and 3b.

### Coverage notes

- **Complete coverage.** The source is a single A3 landscape poster; all textual content (four caveats, three preamble paragraphs, five tests with all sub-questions, seven recommendation end-states, footer attribution) has been preserved in the converted markdown and represented in the deep reference. No claim in the deep reference depends on content outside the converted file.

- **Editorial repair in the converted markdown.** The raw `pymupdf4llm` extraction renders the sentence "Action singling out an individual is rarely appropriate most patient safety issues have deeper causes and require wider action" without a punctuation mark between "appropriate" and "most". The mid-sentence omission is almost certainly a layout artefact (the poster's visual rendering carries a punctuation mark — most likely an em-dash — that the line-break conversion drops). The converted markdown at `sources/converted/nhs-just-culture-guide.md` restores an em-dash to make the sentence grammatical, and the deep ref quotes it with the em-dash. This is recorded here as an editorial repair, not a verbatim transcription; downstream consumers should treat the em-dash in the deep ref's quote as a punctuation reconstruction. The semantic content of the sentence is unaffected.

- **No image axis.** The poster contains visual flow elements (the decision-tree arrows and box layout) but no embedded substantive diagrams that warrant the image-index treatment beyond what is captured in the converted markdown's logical structure. The image axis is text-only for this run; no follow-up `ingesting-images` invocation is needed.

- **OGL v3.0 attribution requirement.** The Open Government Licence v3.0 imposes an attribution-only requirement on derivative artefacts. The deep ref, light ref, and both distillations all carry the OGL v3.0 / NHS Improvement attribution in their Source line. Build profiles that include these artefacts inherit the attribution requirement only; no copyleft propagation applies.

### Evidence-class marker audit

Spot-checked sample of evidence-class markers in body prose:

- `[V]` markers: 26 instances. After the three verbatim-slip fixes (items 1, 2, 3 above), all `[V]` quotes match the converted source character-for-character, with the one acknowledged editorial repair (em-dash in the "rarely appropriate" sentence) flagged above. The blockquoted recommendation end-states (A through G) were re-checked sentence-by-sentence and match exactly.
- `[AP]` markers: 4 instances, all paraphrasing the source's framing without claiming verbatim status.
- `[AR]` markers: 13 instances, all reporting the source's argument structure (the structural prior of default-to-system; the sequential gating of tests; the parallel-investigation obligation preserved on every branch; the comparison of "is unlikely to be appropriate" vs "may not be appropriate"). All trace to passages in the preamble or to structural patterns visible in the test/recommendation layout.
- `[BT]` markers: 2 instances, both on the source's footer attribution to Professor James Reason and the NPSA Incident Decision Tree. No further characterisation of either lineage was attached to the deep reference — the source names them but does not develop them.
- `[AE]` markers: none. The source contains no worked examples; it is a procedural decision aid.

### Cross-corpus drift check

The deep reference does not connect the NHS guide to any other source in the corpus. The source itself cites only Reason and the NPSA Incident Decision Tree (both registered as `[BT]`). The Connections section in the deep ref correctly reports this minimal citation lineage without manufacturing connections to other authors. The distillations (decision-making and stakeholder-engagement) make integration suggestions in their "Integration with Other References" sections; those are distillation-tier synthesis, not deep-ref-tier claims, and are appropriate at that tier.

### Task-application-smuggling check

The deep reference contains no task-application guidance: no diagnostic questions for managers, no anti-patterns, no worked-example projections. The procedural shape of the source (sequential five-test tree with seven recommendation end-states) is described as the source's argument structure, not as an operator runbook. Diagnostic questions and anti-patterns live in the distillations at `nhs-just-culture-guide-decision-making.md` and `nhs-just-culture-guide-stakeholder-engagement.md`, which is the correct tier separation.

### Post-source-vocabulary check

The deep reference uses the source's own vocabulary (just culture; deliberate harm; foresight test; substitution test; mitigating circumstances; not appropriate to single out; wider investigation). It does not import concepts from later just-culture literature (e.g., Dekker's *Just Culture* book; Reason's *Managing the Risks of Organizational Accidents*; safety-II vocabulary; restorative just culture) that the source itself does not name. The Connections section correctly lists only Reason and the NPSA Incident Decision Tree (the two lineages the source's footer names), without speculating on which of Reason's specific works the guide draws from.

### Verbatim accuracy re-check on the seven recommendation end-states

Each of the seven recommendation end-states is rendered as a `[V]` blockquote in the deep reference. Each was re-checked character-by-character against the converted source:

- **Recommendation A** (deliberate harm): exact match.
- **Recommendation B** (substance abuse): exact match.
- **Recommendation C** (health issue): exact match.
- **Recommendation D** (foresight-branch — not appropriate to single out): exact match.
- **Recommendation E** (substitution-branch — not appropriate to single out): exact match; textually identical to Recommendation D in the source, which the deep ref calls out explicitly.
- **Recommendation F** (mitigation applies): exact match.
- **Recommendation G** (residual — management action plus wider investigation): exact match.

### Verbatim accuracy re-check on the eleven sub-questions

- **1a** (deliberate harm): exact match.
- **2a/2b/2c** (substance abuse; physical ill health; mental ill health): all three exact matches.
- **3a/3b/3c** (agreed protocols; workable and in routine use; knowingly departed) — *post-fix* exact matches; pre-fix slash-spacing slip corrected.
- **4a/4b/4c** (peer behaviour; training missed; supervision absent): all three exact matches.
- **5a** (mitigating circumstances): exact match.

## Result

**Pass.** The deep reference ships. Three verbatim-slip fixes were applied in-place before this log was written. One editorial repair (an em-dash inserted into a sentence the raw conversion dropped punctuation from) is documented above and flagged in the deep ref's "Citation and source-integrity notes" by reference; the semantic content is unaffected. The light reference and the two distillations derive from this audited deep reference; the source-only discipline propagates by construction.

The deep reference's coverage of the source is complete: every textual element of the single-page poster (four caveats; three preamble paragraphs; five tests with eleven sub-questions; seven recommendation end-states; footer attribution) is represented. No silent partial coverage; no training-data leakage; no post-source vocabulary; no cross-corpus drift; no task-application guidance smuggled into the deep tier.

**Files produced this run:**

- `corpus.commons/demo/sources/original/nhs-just-culture-guide.source.md` — frontmatter sidecar.
- `corpus.commons/demo/sources/original/nhs-just-culture-guide.pdf` — original PDF (1.5MB, OGL v3.0, redistributable; force-added to git on this run).
- `corpus.commons/demo/sources/converted/nhs-just-culture-guide.md` — converted markdown (decision-tree-as-logical-structure).
- `corpus.commons/demo/references/nhs-just-culture-guide-deep.md` — audited deep reference.
- `corpus.commons/demo/references/nhs-just-culture-guide.md` — light reference (derived from audited deep).
- `corpus.commons/demo/distillations/decision-making/nhs-just-culture-guide-decision-making.md` — decision-making distillation (Pass G applicability: clear yes — this is a decision aid).
- `corpus.commons/demo/distillations/stakeholder-engagement/nhs-just-culture-guide-stakeholder-engagement.md` — stakeholder-engagement distillation (Pass G applicability: yes — the source positions itself as a communication tool for managers, staff, patients, and families).
- `corpus.commons/demo/references/REFERENCE-INDEX.md` — updated (Light + Deep reference rows; concept-index entries for Decision-making, Foresight test, Incident Decision Tree, Just culture, Mitigating circumstances test, Patient safety incident response, Reason James, Substitution test).
- `corpus.commons/demo/distillations/decision-making/DECISION-MAKING-DISTILLATION-INDEX.md` — updated (quick-start rows; phase-by-phase rows across all six phases; new "Just-culture and patient-safety incident response" reference category).
- `corpus.commons/demo/distillations/stakeholder-engagement/STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md` — updated (quick-start rows; phase-by-phase rows across mapping, framing, convening, agreement, ratifying, and post-engagement phases; new "Just-culture and patient-safety stakeholder engagement" reference category).
- `corpus.commons/demo/references/_audit/_ingest_pass_I_nhs-just-culture-guide_source_audit.md` — this log.

**Input source removed from `sources/ingest/`:** confirmed (moved to `sources/original/`).
