# Pass H Verification Log — OpenStax, Principles of Economics 3e

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Phase 2 parallel-batch wrap-up.** This book was partially ingested in the original parallel batch — the deep ref and Pass A ledger landed but Passes F, G, H, I and the staging files did not. This wrap-up agent completed those passes against the existing deep ref and Pass A ledger. The deep ref was not re-derived.

## Files produced (this wrap-up)

| Artefact | Path | Status |
|---|---|---|
| Light reference | `corpus.commons/demo/references/openstax-economics-3e.md` | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-economics-3e-decision-making.md` | Complete (G.0 clear-yes) |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-economics-3e-stakeholder-engagement.md` | Complete (G.0 clear-yes, narrower scope) |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-economics-3e_verification.md` | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-economics-3e_source_audit.md` | Complete |
| SEARCH-INDEX staging | `_ingest_search_index_economics-3e.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | Complete |
| DECISION-MAKING-INDEX staging | `_ingest_dm_economics-3e.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | Complete |
| STAKEHOLDER-ENGAGEMENT-INDEX staging | `_ingest_se_economics-3e.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | Complete |
| IMAGE-INDEX staging | `_ingest_image_index_economics-3e.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | Complete |

Pre-existing artefacts (not re-done):

| Artefact | Path | Status |
|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-economics-3e-deep.md` | 581 lines (left unchanged; no Pass I issues found requiring strip) |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-economics-3e_ledger.md` | 117 lines (left unchanged) |

## Pass-by-pass results (this wrap-up only)

### Pass F: Light-reference derivation

Three-pass derivation from the existing verified deep ref: condense (parts → flat depth-2 headings, with substantial chapter consolidation given the book's 34 chapters); tier-separate (no application guidance); trace verify (~120 substantive claims traced to deep ref locations). Light ref totals 211 lines covering the book's full breadth across micro and macro.

Synthesis decisions:
- Chapters were grouped into thematic clusters (Foundations; Demand & Supply; Elasticity & Consumer Choice; Production & Market Structures; Antitrust, Externalities, Public Goods; Labour, Inequality, Information; Public Economy; Macro Measurement & Growth; Unemployment & Inflation; AD-AS; Money, Banking & Monetary Policy; Exchange Rates, Fiscal Policy & Borrowing; Trade & Globalisation) to keep the light ref scannable rather than mirroring all 34 chapters as separate sections.
- Behavioural economics (Ch 6.3) is preserved as its own substantive content because it represents the book's clearest contrarian framing of strict rationality.
- Twelve signature contrarian positions (deep ref has eight in its "explicitly framed against" list; light ref expands slightly by surfacing methodological positions implicit in the deep ref) — all traced back to the deep ref's body.

### Pass G: Application file projection

**Sub-pass G.0 — Applicability decisions:**

- **Decision-making**: **CLEAR YES.** The book defines its subject as "the study of how humans make decisions in the face of scarcity" (Ch 1.1). Foundational decision-theoretic concepts (opportunity cost, marginal analysis, sunk costs, budget constraint, PPF, comparative advantage) are introduced in the first two chapters and applied throughout. Profit-maximisation rules (Chs 8-10), expected value and risk (Ch 16), behavioural anomalies (Ch 6.3), and time-discounting (App C) extend the scope. The book is essentially a decision-making toolkit at multiple scales (consumer, firm, government).
- **Stakeholder-engagement**: **CLEAR YES, narrower scope.** Most of the book operates at the system / market level, but several chapters address structural stakeholder relationships substantively: externalities and public goods (Chs 12-13); labour markets, monopsony, unions, discrimination, immigration (Ch 14); poverty and inequality (Ch 15); information and insurance (Ch 16); public economy (Ch 18); antitrust (Ch 11); and trade / globalisation (Chs 33-34). The book's distinctive contribution to stakeholder engagement is **structural** — explaining why certain stakeholder relationships have the bargaining shape they do, and what institutional response matches what structural problem. The application file is framed accordingly: it is not a guide to interpersonal engagement but to recognising the systemic forces that shape any specific engagement. This is a real contribution rather than an artificial fit.

**Sub-pass G.1 — Project:** verified-deep-ref concepts projected onto each task's working vocabulary. For decision-making, the projection translated economic vocabulary (opportunity cost, marginal analysis, comparative advantage, elasticity, equilibrium, expected value, present-discounted value) into decision-process vocabulary. For stakeholder-engagement, the projection translated structural concepts (externality, free-rider, monopsony, bilateral monopoly, asymmetric information, public-choice realism, regulatory capture) into engagement-design vocabulary.

**Sub-pass G.2 — Phase-organise:** decision-making file organised into the standard six phases (framing, bounding, exploring, deciding, ratifying, reviewing); stakeholder-engagement file organised into the standard seven phases (mapping, framing, convening, surfacing conflict, reaching agreement, ratifying, post-engagement).

**Sub-pass G.3 — Cross-check:** each phase's diagnostic content traces back to the deep ref. Verbatim-blockquote regex `^>\s*"` returns no matches in either application file (verified after writing).

### Pass H: Cross-reference (this pass)

Per the Phase 2 parallel-batch protocol, this wrap-up agent does NOT touch canonical indexes (race risk has passed but the consolidation pattern is preserved for parent-agent cleanliness). Staging files for each canonical index were produced:

- `_ingest_search_index_economics-3e.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — light-ref row, deep-ref row, and ~50 concept-A-Z entries pointing into the deep ref.
- `_ingest_dm_economics-3e.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — Quick-start rows and phase-by-phase rows for the decision-making index.
- `_ingest_se_economics-3e.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — Quick-start rows and phase-by-phase rows for the stakeholder-engagement index.
- `_ingest_image_index_economics-3e.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — image classification methodology and curated entries.

### Pass I: Source-only audit

Documented in `corpus.commons/demo/references/_ingest_pass_I_openstax-economics-3e_source_audit.md`. Summary: ~340 distinct claims audited against the source markdown, 340/340 source-anchored, 0 stripped. All evidence-class markers ([V], [AP], [AR], [AE], [BT]) verified against their attached claims. No training-data leakage, post-source vocabulary, or cross-corpus drift found.

## Image classification — CRITICAL CORRECTION

The pilot heuristic "PNG = substantive, JPEG = decorative" is **completely inverted** for this book. Visual inspection by sampling at multiple page positions and file-size brackets confirmed:

- **Total images:** 348 (3 PNG, 345 JPEG).
- **PNGs (3):** all front-matter decorative — Rice University logo (p0005-1.png, 46KB), paper-texture frame (p0006-1.png, 1.8MB), abstract dark frame (p0006-6.png, 33KB). Zero substantive PNGs.
- **JPEGs (345):** the vast majority are conceptual diagrams (supply-demand curves, IS-LM diagrams, AS-AD models, cost curves, PPF diagrams, circular flow diagrams, flowcharts). A subset are chapter-opener photographs and stock images.
- **File-size signal:** JPEGs <100KB are almost always diagrams. JPEGs 100-200KB are mostly diagrams (sampled p0083-1, p0222-1, p0530-2, p0899-1 — all diagrams). JPEGs 200-400KB are mixed (sampled p0666-1 and p0683-1 are photos; p0726-1 and p0871-1 are diagrams). JPEGs >400KB are almost always photos (sampled p0151-1, p0177-1, p0573-1, p0783-1 — all photos).
- **Estimated substantive count:** ~290 (the JPEGs <200KB plus the diagrams in the 200-400KB range).
- **Estimated decorative count:** ~58 (the 3 PNGs plus the photos >200KB and the chapter-opener photographs).

The image-index staging file (`_ingest_image_index_economics-3e.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation)) uses the size-based heuristic plus visual sampling to produce a curated set of substantive entries. Time and budget constraints precluded individual classification of all 345 JPEGs; the staging file documents this methodology transparently and labels the entries as "approximate" classifications. A v0.1.5+ refinement could classify each image individually.

**Methodology refinement for future ingestion:** the PNG-vs-JPEG heuristic is unreliable across OpenStax books. Some books (Org Behavior, Marketing) store diagrams as PNG; others (Economics 3e) store diagrams as JPEG. Visual inspection plus size-based heuristic per book is the only reliable method. The pilot finding has been overstated as a corpus-wide rule.

## Pass G.0 decisions summary

| Axis | Decision | Reasoning |
|---|---|---|
| Decision-making | **clear-yes** | The book defines its subject as decision-making under scarcity; foundational decision-theoretic concepts run throughout. Strong, well-scoped projection. |
| Stakeholder-engagement | **clear-yes (narrower)** | While the book is system-level, several chapters provide structural framing (externality, free-rider, monopsony, asymmetric information, regulatory capture, public-choice realism, trade-distribution) that is genuinely valuable for engagement work. The application file is framed as "structural framing of engagements" rather than "interpersonal engagement guide" to honour the book's actual contribution. |

## Known limitations and follow-ups

- **Image-index staging.** Curated rather than per-image-classified; methodology documented in the staging file. v0.1.5+ refinement would classify each of the 345 JPEGs and ~3 PNGs individually.
- **Citation density across 34 chapters.** The deep ref covers 34 chapters in 581 lines, which compresses heavily compared to single-domain books. Some claims (especially in the macro chapters) are condensed; v0.1.5+ could expand selected sections.
- **Behavioural economics in Ch 6.3.** Treated compactly in the deep ref; the application files draw on it more substantially. Future updates could expand the deep ref's behavioural-economics section.
- **Public-choice content (Ch 18).** Treated as a single Part in the deep ref but is rich enough to warrant deeper treatment in a future revision.
- **Application-guidance separation.** The deep ref does not contain application guidance. The application files contain no verbatim source quotes (verified). Tier separation is clean.
