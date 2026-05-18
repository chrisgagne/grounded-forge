# Pass H Verification Log — OpenStax, Psychology 2e

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Run type:** Phase 2 wrap-up (deep ref and Pass A pre-existed; this run completed F, G, H, I + staging files).

## Files produced

| Artefact | Path | Lines | Status |
|---|---|---|---|
| Deep reference (pre-existing; Pass I edits applied) | `corpus.commons/demo/references/openstax-psychology-2e-deep.md` | 505 | Complete (post-Pass-I) |
| Light reference | `corpus.commons/demo/references/openstax-psychology-2e.md` | ~130 | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-psychology-2e-decision-making.md` | ~190 | Complete |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-psychology-2e-stakeholder-engagement.md` | ~225 | Complete |
| Pass A ledger (pre-existing) | `corpus.commons/demo/references/_ingest_pass_A_openstax-psychology-2e_ledger.md` | 91 | Complete |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-psychology-2e_verification.md` | (this file) | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-psychology-2e_source_audit.md` | (Pass I artefact) | Complete |
| Search-index staging | `_ingest_search_index_psychology-2e.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | ~250 | Complete |
| DM-index staging | `_ingest_dm_psychology-2e.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | ~85 | Complete |
| SE-index staging | `_ingest_se_psychology-2e.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | ~95 | Complete |
| Image-index staging | `_ingest_image_index_psychology-2e.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | ~120 | PARTIAL — see image-classification section |

## Pass-by-pass results (passes F, G, H, I)

### Pass F: Light-reference derivation

Three-pass derivation from the verified deep ref:

1. **Condense.** Reduced the deep ref's 16 Parts into flat depth-2 headings: discipline; research methods; biopsychology; consciousness/sensation/perception; learning; cognition/intelligence/judgement; memory; lifespan development; motivation/emotion; personality; social psychology; I-O psychology; stress/health. Therapy (Part XIV) and disorders (Part XV) are presented in the deep ref but not given their own light-ref headings; their content is summarised within the broader thesis paragraph.
2. **Tier-separate.** Stripped any application guidance that bled in. The light ref is faithful summarisation, no diagnostic questions, no anti-patterns, no worked examples.
3. **Trace verify.** ~150 substantive claims traced to deep ref locations. No application guidance present (verified).

Light ref totals ~130 lines. The closing comment records "Verified: ~150 substantive claims traced to deep ref. No application guidance (tier-separated)."

### Pass G: Application-file projection

#### Sub-pass G.0 — Applicability decisions

- **Decision-making**: **CLEAR YES.** The source has a sustained chapter on cognition (Ch 7) including the canonical bias inventory (anchoring, confirmation, hindsight, representativeness, availability) plus mental set and functional fixedness. Chapter 8 (Memory) provides the reconstructive-memory framing relevant to evidence evaluation. Chapter 12 (Social Psychology) provides attribution biases (FAE, actor-observer, self-serving), conformity (Asch), obedience (Milgram), and groupthink. Chapter 10 provides arousal and emotion. Chapter 6 provides reinforcement and decision-habit formation. Strong, well-scoped projection supported.

- **Stakeholder engagement**: **CLEAR YES.** Chapter 12 is the densest engagement-relevant content: roles/norms/scripts; Yale persuasion model and ELM; foot-in-the-door; Asch and Milgram; groupthink and group polarisation; prejudice/stereotype/discrimination including dual attitudes (explicit/implicit); bystander effect; relationship formation. Chapter 6 provides behaviour-change mechanics. Chapter 13 provides procedural justice (Greenberg) and leadership styles. Chapter 14 provides social-support research relevant to sustaining stakeholders. Strong projection supported.

#### G.0 scope constraint applied

Per the spawn-prompt directive, application files draw ONLY on cognitive, social, organisational, and motivational psychology content (Chs 6, 7, 8, 9, 10, 11, 12, 13, 14). Therapy and clinical content from Chapters 15 and 16 is **excluded** from application projection. This is recorded in the deep ref's Application-projection note (Citation and source-integrity notes, last bullet). Both application files name this constraint explicitly in their relevance section.

#### Sub-pass G.1 — Project

Verified deep ref's concepts projected onto each task's working vocabulary. For decision-making: heuristics, bias inventory, attribution errors, group dynamics, arousal-performance curve, reinforcement and habit formation. For stakeholder engagement: roles/norms/scripts, persuasion routes, conformity and obedience, groupthink, in-group/out-group dynamics, contact theory, behaviour-change mechanics, social support.

#### Sub-pass G.2 — Phase-organise

Each application file built phase-organised diagnostic tables:

- **Decision-making phases:** Framing, Bounding, Exploring, Deciding, Implementing, Reviewing.
- **Stakeholder-engagement phases:** Mapping, Framing, Convening, Surfacing conflict, Reaching agreement, Sustaining.

Phase choice mirrors the OB pilot exemplar to maintain consistent phase vocabulary across the corpus.

#### Sub-pass G.3 — Cross-check

Each phase's diagnostic content was cross-checked back to the deep ref for traceability. Only paraphrased citations; no verbatim blockquotes.

**Verification: regex `^>\s*"` matches nothing in either application file.** Confirmed via grep:
- `prompts/applications/decision-making/openstax-psychology-2e-decision-making.md`: 0 matches.
- `prompts/applications/stakeholder-engagement/openstax-psychology-2e-stakeholder-engagement.md`: 0 matches.

### Pass H: Cross-reference (this pass)

Per the parallel-batch protocol, canonical indexes (`SEARCH-INDEX.md`, `DECISION-MAKING-INDEX.md`, `STAKEHOLDER-ENGAGEMENT-INDEX.md`, `IMAGE-INDEX.yaml`) are NOT updated by the wrap-up agent — staging files emitted instead for the parent agent to merge. Staging files produced:

- `_ingest_search_index_psychology-2e.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation): light-ref table row, deep-ref table row, and ~80 concept-A-Z entries spanning A–Y (no W, X, Z entries — unusual but reflective of vocabulary distribution in the source).
- `_ingest_dm_psychology-2e.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation): 7 quick-start entries + 17 phase entries (across 6 phases). Pass G.0 clear-yes.
- `_ingest_se_psychology-2e.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation): 10 quick-start entries + 18 phase entries (across 6 phases). Pass G.0 clear-yes.
- `_ingest_image_index_psychology-2e.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation): PARTIAL — see Image classification section below.

### Pass I: Source-only audit

See companion file `corpus.commons/demo/references/_ingest_pass_I_openstax-psychology-2e_source_audit.md` for the full audit log. Summary:

- Claims audited (approximate body sentences with citations or evidence markers): ~190
- Claims source-anchored without modification: 188
- Claims requiring marker correction: 1 (object permanence row in Key statistics: changed from [V] to [AP] because the row label "develops between 5 and 8 months" is a paraphrase even though words overlap with source line 16540).
- Claims requiring strip / fix (no source support / corruption): 1 (Buss row in Key statistics: the metric label was corrupted to "Number of monkeys' first words across 37 cultures" — clearly an artefact, not in the source. Fixed to "Buss (1989) cross-cultural mate-preference study" with consistent value column).
- Verbatim blockquotes verified: the deep ref does not use `> "..."` blockquote format (verbatim quotes are inline within prose, marked [V]). Spot-checked verbatim claims via grep against source (Asch 76%, Milgram 65%, Pavlov "lock-and-key relationship", Maslow criticism, Holt-Lunstad survival likelihood, Chandola job-strain 68%, Buss 37 cultures): all verbatim claims confirmed.
- Application guidance found in deep ref: 0
- Post-source vocabulary detected: 0

**Pass I outcome: PASS (after 2 fixes).**

## Image classification

**Status: PARTIAL — exhaustive visual inspection of 353 images was not completed within the wrap-up agent's time budget.** Per the grounded-forge Source Integrity rule, this partial coverage is labelled explicitly rather than presented as comprehensive.

### Counts

- **Total images extracted from PDF:** 353 (349 JPEG, 4 PNG)
- **Visually inspected:** ~25 (sample across pages 5, 6, 19, 34, 47, 67, 87, 91, 96, 99, 103, 107, 157, 167, 182, 193, 213, 291, 325, plus the 4 PNGs)
- **Confirmed substantive (entered in staging YAML):** 6 (1 PNG + 5 JPEGs as named entries)
- **Confirmed decorative (sampled):** 3 PNGs + ~12 JPEGs sampled
- **Unclassified:** ~324 JPEGs (not visually inspected — substantive count almost certainly higher than the 5 confirmed JPEGs)

### Heuristic finding (corrects pilot heuristic)

The pilot heuristic from OpenStax *Organizational Behavior* (PNG = usually substantive; JPEG = usually decorative) **inverts in this corpus**:

- **Of 4 PNGs**: 3 decorative (Rice University logo, paper-texture frame, dark-frame asset; all in front-matter pages 5–6) and 1 substantive (Punnett square at p0087-1.png).
- **JPEGs are mixed**: sample inspection suggests roughly 30–40% are substantive diagrams (neuron anatomy, brain regions, eye anatomy, somatosensory homunculus, conceptual frames like the Big Five OCEAN model and Gestalt continuation). The remainder are decorative photographs (people in everyday settings, historical figures, contextual scenes).

This inversion makes the pilot heuristic unreliable for *Psychology 2e* and means honest classification requires per-image visual inspection at scale.

### Confirmed substantive entries (in staging YAML)

| File | Page | Subject | Style |
|---|---|---|---|
| p0087-1.png | 87 | Punnett square (genetics) | diagram |
| p0091-1.jpeg | 91 | Neuron anatomy | diagram |
| p0096-1.jpeg | 96 | CNS / PNS body diagram | diagram |
| p0099-1.jpeg | 99 | Brain sulci / gyri | diagram |
| p0103-1.jpeg | 103 | Somatosensory cortex homunculus | diagram |
| p0167-1.jpeg | 167 | Eye and retina anatomy | diagram |

### Sampled-substantive but not entered (insufficient detail captured to write index entry)

The following pages contained substantive content visible in the brief sample but were not given full YAML entries:

- p0034-1.jpeg (Big Five OCEAN trait diagram, Ch 11)
- p0083-1.jpeg (PET / CT / MRI brain-imaging methods, Ch 3)
- p0107-1.jpeg (CT / MRI scans illustrating tumour, Ch 3)
- p0182-2.jpeg (Gestalt continuation, dotted-line X figure, Ch 5)

These should be added by the parent agent or a follow-up classification pass.

### Likely substantive but not inspected

Based on the deep ref's content, substantive diagrams are likely on pages covering:
- Ch 3 brain anatomy (frontal lobe, hippocampus, amygdala) — pages ~100–125
- Ch 4 sleep stages EEG — pages ~140–160
- Ch 5 Gestalt principles, depth cues, illusions — pages ~180–220
- Ch 6 conditioning chambers, reinforcement schedule curves — pages ~220–260
- Ch 7 problem-solving figures, IQ bell curve — pages ~260–300
- Ch 8 Atkinson-Shiffrin three-stage memory model, brain-region figures — pages ~300–330
- Ch 9 Erikson's eight stages, Piaget conservation tasks — pages ~340–380
- Ch 10 Maslow hierarchy, emotion-theory comparison figure — pages ~390–420
- Ch 11 Big Five OCEAN (already noted: p0034 is a likely instance) — pages ~430–470
- Ch 12 attribution diagrams, Asch line study, Milgram apparatus — pages ~470–520
- Ch 13 leadership-style frames, organisational-culture layers — pages ~530–575
- Ch 14 GAS curve, social-support figures, Yerkes-Dodson — pages ~575–620

### Recommendation for parent agent

DO NOT mass-delete the unclassified JPEGs in `docs/images/psychology-2e/`. The runbook's "if not in IMAGE-INDEX.yaml, not in the library" rule means deletion now would discard substantive diagrams that are merely unclassified, not confirmed-decorative. Either:

(a) Schedule a follow-up image-classification pass before any deletion, or
(b) Accept that the image-index for *Psychology 2e* will be expanded over time as substantive images are identified, with no immediate deletion of unclassified files.

## Methodology refinements for future wrap-up agents

1. **Image classification heuristics are corpus-specific.** The pilot's PNG-substantive / JPEG-decorative heuristic does not transfer cleanly. Each corpus needs its own quick visual sample before bulk classification rules are applied. Plan for visual inspection of a 20–30 image sample at the start, then scale heuristics from that sample.

2. **Image volume affects feasibility.** With 353 images, individual visual inspection is a multi-hour task. Future ingestion runs should budget image classification as a distinct work block from the deep-ref reading and application-file authoring, not assume it is incidental.

3. **Source-Integrity rule applies to image classification too.** Silent under-classification (treating an unclassified JPEG as decorative-by-default) is the equivalent of silently dropping source coverage. The honest move is to label partial classification explicitly and flag for follow-up.

4. **Pre-existing artefacts on disk inform later passes.** This wrap-up agent inherited a deep ref and Pass A ledger that pre-existed. The deep ref had two minor errors (one corrupted Key-statistics row label, one [V] marker that should have been [AP]). Both were caught by Pass I's audit-cold pass. This is the protocol working as designed; the discipline of running Pass I separately from synthesis catches what the synthesising agent missed.

## Known limitations and follow-ups

- **Image classification is partial.** ~324 JPEGs not visually inspected. A follow-up classification pass is needed before any decorative-image deletion is performed.
- **Concept-A-Z entries.** Staging file's concept index is comprehensive for Chs 1–14 but deliberately omits clinical-disorder and therapy-modality entries (Chs 15–16) per the Application-projection constraint. If future task axes added to the corpus do warrant clinical content (e.g., a "wellbeing-coaching" axis specifically scoped to clinical content), those entries would need to be added via a separate ingestion pass.
- **Cross-corpus integration.** Several concepts overlap with OpenStax *Organizational Behavior* (attribution theory, conformity, groupthink, McGregor X/Y, Mintzberg roles, Hawthorne effect, organisational culture, procedural justice). Parent agent merging into SEARCH-INDEX should add cross-reference pointers rather than letting one source supersede the other.
