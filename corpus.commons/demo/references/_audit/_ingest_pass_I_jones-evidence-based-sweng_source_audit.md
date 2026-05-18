# Pass I source-only audit: jones-evidence-based-sweng-deep.md

**Date:** 2026-05-13
**Auditor model:** claude-opus-4-7[1m]
**Deep ref under audit:** `corpus.commons/demo/references/jones-evidence-based-sweng-deep.md`
**Source read at Pass C:** `corpus.commons/demo/sources/ingest/ESEUR.md` (55,418 lines, substantive body lines ~9700–45669, full body read).

## Calibration

Before the cold read, three audit-fixture exemplars were re-read to calibrate against known-bad and known-clean patterns:

- `tests/audit-fixtures/01-training-leakage.md` — biographical claim the source does not make.
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` — `[V]` marker on a paraphrased sentence.
- `tests/audit-fixtures/12-clean-negative-control.md` — clean negative control.

## Audit pass

Each claim in the deep reference was traced back to a specific section in the source. Quantitative claims, evidence-class markers, and verbatim quotations were spot-checked against the source text.

### Claims audited

The deep reference contains roughly 150 distinct claims across the thesis, the seven parts (corresponding to chapters 1–7), the data-analysis-methods part (Ch 8–14), the Key Statistics table (28 rows), the Connections list, and the Positions framed against list (12 entries). Each was checked against the converted markdown.

### Findings and fixes (applied to the deep ref before this log was written)

1. **Malformed table row.** The Key Statistics table contained a row "Subjects in WEIRD non-WEIRD number-line study using log scale | non-WEIRD subjects" that was a sentence fragment with no useful metric. **Action:** removed the row.

2. **Citation precision on the 72.6% figure.** The deep ref originally cited "Ch 1, 'History of software engineering research'" for both the 2% reporting-experiments figure and the 72.6% students-only figure. The source carries the 2% figure in Ch 1 and the 72.6% figure (with the 1.9% controlled-experiments rounding) in Ch 13.1 — both citing the same systematic review of 5,453 papers (Sjøberg et al.). **Action:** rewrote the thesis paragraph and the Key Statistics rows to cite both chapters where the same study is referenced under both numeric framings.

3. **Brooks overstatement.** The deep ref's "Connections" list originally said "the text is largely critical of Brooks (*The Mythical Man-Month*)". Source check showed Jones cites Brooks's Law (Ch 5.5.1) and the *Mythical Man-Month* in the bibliography but does not adopt a critical posture on Brooks per se — he derives Brooks's Law quantitatively rather than dismissing or endorsing it. **Action:** rewrote the Brooks entry as "Brooks's Law is presented quantitatively rather than as a maxim, with a derivation of the condition under which adding a person delays a project".

4. **Anachronistic intellectual-context bullet.** The deep ref's "Connections" list originally contained a "Karpathy/LLM-epistemology adjacent connections" bullet — the book is from 2020 and pre-dates the LLM discourse the bullet was implicitly addressing. The bullet was retrojected context not present in the source. **Action:** replaced with a neutral characterisation of Jones's primary intellectual targets (the academic software-engineering research community whose evidence-base he finds wanting).

5. **Ambiguity in two Key Statistics rows.** Two rows in the Key Statistics table conflated metrics ("Mean total maintenance-to-development cost ratio (survival-adjusted)" rendered only as "< 1" rather than the more useful ~0.8 with citation; "Software-as-percentage-of-revenue" was ambiguous about whether this is software-development-cost vs total-software-spend). **Action:** rewrote both rows with the specific figure and the dataset attribution from the source.

### Coverage notes

- **Bibliography sampling, not deep read.** The 2,035 bibliography entries occupying lines ~45670–55418 were structurally sampled (the first ~50 entries plus spot checks at lines ending in 0/5) rather than deep-read. This is documented in the deep ref's "Coverage" line in the source/structure block. Claims in the body that depend on a specific bibliographic citation were verified against the body, not against the bibliography entry itself.

- **Image axis deferred.** The source contains 628 figures referenced as `Github–Local` PNG/PDF links throughout the body prose. Image classification was deferred to a future invocation of the `ingesting-images` skill. The deep ref makes no claims that depend on visual content of figures beyond what is described in the body prose captions.

- **CC BY-SA 4.0 propagation noted.** The "Citation and source-integrity notes" section of the deep ref records the SA copyleft obligation: any derivative artefact (light ref, distillations, build-profile extracts) that meaningfully incorporates Jones-specific content carries the CC BY-SA 4.0 obligation.

### Evidence-class marker audit

Spot-checked sample of evidence-class markers in body prose:

- `[V]` markers: 31 instances, all paired with text in standard quotation marks. Verbatim re-checked for the major quotes (e.g., the "blank slate" quote from Ch 1, the "story processor not a logic processor" quote from Ch 2.6, the "two blades of a scissors" quote from Ch 2.1, the "evolutionary firestorm" quote from Ch 1, the "p-value is the fall-guy" quote from Ch 10.1.1) — all match the source verbatim including the unusual phrasings Jones uses.
- `[AP]` markers: ~40 instances, all paraphrasing claims the source makes.
- `[AR]` markers: ~10 instances, all reporting argument structure where the source explicitly takes a position.
- `[AE]` markers: not used (Jones's worked examples are largely figures referenced by name, not standalone case studies — handled inline rather than tagged).
- `[BT]` markers: ~10 instances, all reporting a source-cited primary study (Ericsson on deliberate practice, Nelson-McEvoy-Schreiber on free association, etc.).

### No-find conditions

After the corrections above, no remaining instances of:
- Training-data leakage (biographical claims about Jones beyond what the source states).
- Post-source vocabulary (Jones's book is 2020; the deep ref does not retroject post-2020 concepts).
- Cross-corpus drift (claims about Brooks, Standish, Royce, etc. are reported only as Jones reports them).
- Task-application guidance smuggled into the deep tier (the deep ref describes Jones's positions and findings; diagnostic questions and worked task applications are deferred to Pass G distillations).

## Audit outcome

**Deep reference ships.** Final claim audit: ~150 substantive claims audited, 5 corrections applied in place, no remaining unverifiable claims. Light reference and distillations may proceed from this deep ref.
