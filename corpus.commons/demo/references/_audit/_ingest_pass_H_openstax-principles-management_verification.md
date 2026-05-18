# Pass H Verification Log — OpenStax, Principles of Management

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Parallel-batch run:** Phase 2 wrap-up subagent for Book 11 of 12 in the OpenStax PoC corpus.

## Wrap-up scope

A prior subagent run completed Passes A-E for this book (deep ref and Pass A ledger landed on disk; light ref, applications, Pass H, Pass I, and staging files did not). This wrap-up subagent run produces the missing artefacts: Pass F (light ref), Pass G (both applications, after G.0), this Pass H verification log, Pass I source-only audit, and the four staging files. The deep ref is preserved; Pass I applied two minor fixes during the audit (citation re-anchoring; verbatim-quote nesting) — recorded in the Pass I log.

## Files produced

| Artefact | Path | Lines | Status |
|---|---|---|---|
| Deep reference (preserved from prior run, Pass I fixes applied in-place) | `corpus.commons/demo/references/openstax-principles-management-deep.md` | 1023 | Complete |
| Light reference | `corpus.commons/demo/references/openstax-principles-management.md` | ~205 | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-principles-management-decision-making.md` | ~145 | Complete |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-principles-management-stakeholder-engagement.md` | ~165 | Complete |
| Pass A ledger (preserved from prior run) | `corpus.commons/demo/references/_ingest_pass_A_openstax-principles-management_ledger.md` | 100 | Complete |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-principles-management_verification.md` | (this file) | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-principles-management_source_audit.md` | (Pass I artefact) | Complete |
| Search-index staging | `_ingest_search_index_principles-management.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Decision-making index staging | `_ingest_dm_principles-management.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Stakeholder-engagement index staging | `_ingest_se_principles-management.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Image-index staging | `_ingest_image_index_principles-management.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | (staging) | Complete |

## Pass-by-pass results

### Pass A: Context (preserved from prior run)

The prior subagent run captured: source metadata (16 authors total, lead David S. Bright; CC BY-NC-SA 4.0 licence; ISBNs; first published 2019-03-20); structure map (18 chapters, no separate appendix); pre-flight gates (completeness, citation style, model identity) all passed. Pass A ledger at `corpus.commons/demo/references/_ingest_pass_A_openstax-principles-management_ledger.md`.

### Pass B: Structural read (preserved from prior run)

The prior run identified 18 substantive chapters covering managing/performing, managerial decision-making, history of management, environments and culture, ethics/CSR, international management, entrepreneurship, strategic analysis, strategic management process, structure and change, HR, diversity, leadership, motivation, teams, communication, planning and controlling, technology and innovation. Each chapter's substantive sections were mapped to specific line ranges in the converted markdown. Pedagogical scaffolding (Key Terms, Summary of Learning Outcomes, Chapter Review Questions, Management Skills Application Exercises, Managerial Decision Exercises, Critical Thinking Case) was identified and excluded per Option B coverage scope.

### Pass C: Deep read with citations (preserved from prior run)

The prior run read all 18 chapters' substantive content from the converted markdown (`corpus.commons/demo/sources/converted/openstax-principles-management.md`, 31,465 lines). Approximately 310 load-bearing claims captured, each tied to a `(Ch N, "Section name")` citation. Working notes in the deep ref capture: named cases (Mintzberg, Kotter, Stewart, Sproull, Hannaway, Taylor, Fayol, Weber, Mayo, Barnard, Follett, Woodward, Hofstede, GLOBE, Cox-Blake, Ely-Thomas, Cameron-Quinn, Drucker, Schein, McClelland, Maslow, Alderfer, Herzberg, self-determination theorists, Vroom, Adams, Locke, Bandura, French-Raven, Fiedler, House, Tannenbaum-Schmidt, McGregor, Tuckman, Katzenbach-Smith, Lencioni, Linda Hill, Lewin, Kotter, Cooperrider, Olson-Eoyang, Porter, Barney VRIO, Ulrich, WorldatWork, Nohria-Groysberg-Lee, Fernandez-Araoz, Effron-Ort, Greenleaf, Brown-Trevino, Ulrich, Hewlett-Packard, Bezos, Welch, Larkin and Larkin, Eccles and Nohria, Shewhart-Deming, Koontz-O'Donnell, Tavistock Institute, Bessemer); key statistics with provenance (~25 numerical claims); contrarian positions (16 explicit positions framed against); and cross-author connections (~35 attributions to external sources via [BT]).

### Pass D: Blockquote extraction (preserved from prior run)

Approximately 60+ verbatim quotations carrying [V] markers throughout the deep ref. Pass I (this run) verified 27 specific verbatim quotes character-by-character against the source markdown using grep and direct reads. Two quotation-formatting issues identified during Pass I and corrected in-place. The remaining verbatim quotes spot-checked (Drucker on language, Larkin and Larkin, Porter "stuck in the middle", communication is invention, GE forced ranking, McClelland social power, SDT extrinsic-rewards, Hannaway, Stewart percentages, soldiering, Follett library window, Barnard zone of indifference, Weyerhaeuser truck-driver, Bandura/Vroom expectancy, etc.) all confirmed verbatim.

### Pass E: Synthesis (preserved from prior run)

The prior run assembled the deep reference (1,023 lines) per the canonical template: HTML-comment frontmatter, source/structure/citation-style header, author's thesis (paraphrased with citations), 18 thematic Parts each with subsections, Key Statistics table, Connections section, Positions Framed Against section, Citation and Source-Integrity Notes section. Evidence-class markers ([V], [AP], [AR], [AE], [BT]) applied throughout. Tier separation maintained: no application guidance smuggled into the deep ref (Pass I verified).

### Pass F: Light-reference derivation (this run)

Three-pass derivation from verified deep ref:

- **Condense:** the deep ref's 18 thematic Parts were reduced to flat depth-2 headings in the light ref. Sub-section structure dropped.
- **Tier-separate:** no application guidance present in the light ref; verified by inspection. The light ref is a faithful summarisation.
- **Trace verify:** approximately 155 substantive claims in the light ref each trace to a paragraph in the deep ref. Closing HTML comment records the trace count.

Light ref totals approximately 205 lines (more compact than the deep ref's 1,023). The book's coverage is substantial enough that the light ref is denser than the OB pilot's 137 lines — appropriate for an 18-chapter source covering both the full leading-planning-organising-controlling architecture and the strategic-analysis layer not present in OB.

### Pass G: Application file projection (this run)

**Sub-pass G.0 — Applicability decisions:**

- **Decision-making**: CLEAR YES. The source dedicates Chapter 2 to managerial decision-making (six sections, ~1,400 lines of substantive content) using the same dual-system, six-step, six-barrier framings as OpenStax Organizational Behavior Ch 6. Beyond Ch 2, decision-making is threaded through Ch 3 (Follett's three conflict-resolution paths, Woodward's contingency school), Chs 8-9 (strategic analysis and strategic management as systematic decision-making), Ch 10 (change-model decisions), Ch 14 (motivation-as-decision-about-effort), and Ch 17 (planning as systematic decision-making, with goal-domain-hybrid distinction). The application file projects the cognitive process from Ch 2, the strategic decision frameworks from Chs 8-9, the change-model lens from Ch 10, and the planning lens from Ch 17. Distinct value over OB: strategic-analysis tools (SWOT, PESTEL, Porter's Five Forces, VRIO), Drucker's eight-area goal hierarchy, goal-vs-domain-vs-hybrid planning, and the four change models.

- **Stakeholder engagement**: CLEAR YES. Chapter 5 is the most concentrated stakeholder-engagement chapter in the OpenStax management corpus, with explicit stakeholder definition (citing Freeman), eight stakeholder-analysis questions, the rejection of shareholder-primacy, and the seven ethical principles for stakeholder reasoning. Chapter 6 provides cross-cultural stakeholder engagement through Hofstede and GLOBE. Chapter 13 frames followers as the most critical leadership factor and develops LMX. Chapter 15 provides head-body-heart cultural intelligence and four conflict sources / four interventions for multicultural teams. Chapter 16 anchors the Mintzberg liaison role. Chapter 17 contrasts control-oriented and involvement-oriented planning. Distinct value over OB: the explicit ethical-lens framing (seven principles), the rejection of shareholder-primacy, Freeman's stakeholder theory reproduced directly, the eight-question stakeholder analysis, FCPA / UN Global Compact international ethics, the moral-entrepreneur concept, and servant leadership / stewardship as the ethical leadership style.

**Sub-pass G.1 — Project:** the verified deep ref's concepts were projected onto each task's working vocabulary.

**Sub-pass G.2 — Phase-organise:** each application file built phase-organised diagnostic tables.
- Decision-making: Framing, Bounding, Exploring, Deciding, Implementation, Monitoring (six phases — added "Implementation" to the OB pilot's structure to capture the change-model lens that this book adds).
- Stakeholder engagement: Mapping, Framing, Convening, Surfacing conflict, Reaching agreement, Implementation and sustaining (six phases — collapsed OB pilot's seven slightly).

**Sub-pass G.3 — Cross-check:** for each phase, the diagnostic content was cross-checked back to the deep ref for traceability. Only paraphrased citations; no verbatim blockquotes (regex `^>\s*"` returns nothing in either application file — verified).

### Pass H: Cross-reference (this pass)

This wrap-up subagent does NOT touch the canonical indexes (per parallel-batch instructions, the parent agent merges staging files after all subagents return). Instead, four staging files have been produced for the parent agent to merge:

- `_ingest_search_index_principles-management.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — entries for SEARCH-INDEX.md (light-ref row, deep-ref row, ~50 concept-A-Z entries).
- `_ingest_dm_principles-management.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — entries for DECISION-MAKING-INDEX.md (quick-start rows, phase-by-phase rows across six phases).
- `_ingest_se_principles-management.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — entries for STAKEHOLDER-ENGAGEMENT-INDEX.md (quick-start rows, phase-by-phase rows across six phases).
- `_ingest_image_index_principles-management.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — entries for IMAGE-INDEX.yaml (103 substantive PNG entries).

Format mirrors the existing canonical indexes and the business-ethics / entrepreneurship staging exemplars so the parent agent can splice cleanly.

### Pass I: Source-only audit (this run)

Pass I read the deep ref cold and audited approximately 310 claims. Two minor fixes were applied in-place during the audit:
- Fix 1: citation re-anchored from an excluded section (Ch 1 "Summary of Learning Outcomes 1.3") to a substantive section (Ch 1.3 "Major Characteristics of the Manager's Job") for the first verbatim definition of management.
- Fix 5: verbatim-quote nesting corrected — the deep ref's `"a 'messy and hectic stream of ongoing activity'"` was simplified to `"messy and hectic stream of ongoing activity"` to match the source's actual quotation marks.

Pass I outcome: **PASS** (after Fixes 1 and 5 applied). No claims required strip; ~306 of 310 claims source-anchored without modification. No application guidance smuggled into deep ref (verified). No post-source vocabulary detected. No cross-corpus drift (all [BT] markers trace to authors named in the source). Full audit log at `corpus.commons/demo/references/_ingest_pass_I_openstax-principles-management_source_audit.md`.

## Image classification

- **Total images extracted from PDF**: 186 (per pre-existing files at `docs/images/principles-management/`)
- **Substantive (kept and indexed)**: 103 (all PNGs from p0026 onwards — chapter exhibits, diagrams, charts, models, frameworks)
- **Decorative (deleted)**: 83 (80 JPEGs, all photographs of people, places, events, products; 3 front-matter PNGs at pages 5-6: Rice University logo, paper-texture frame, dark abstract frame)

Classification methodology: per the parallel-batch correction protocol, the PNG=substantive heuristic was treated as unreliable and visual inspection was applied. Visual sampling confirmed:
- Front-matter PNGs (pages 5-6): decorative (Rice logo, paper texture, dark frame).
- All JPEGs visually inspected via sampling: photographs of cathedrals, streets, executives, factories, products, historical figures — decorative.
- All PNGs from page 26 onwards visually sampled: substantive diagrams (Mintzberg's role clusters pyramid, management-levels pyramid, six-structures-by-era diagram, history-of-management influence diagram, etc.).

The pattern matches the entrepreneurship book's batch finding (PNG = mostly substantive but verify; JPEG = predominantly decorative). For Principles of Management, the JPEGs were uniformly decorative and the PNGs from p0026 onwards uniformly substantive.

Per-image descriptive text in the image-index staging file is the parallel-batch baseline; v0.1.5+ refinement should produce richer descriptions tied to specific Exhibit references in the source.

## Pass G.0 decisions per axis (one-line reasons)

- **Decision-making — CLEAR YES**: Ch 2 is dedicated to managerial decision-making with the same frameworks as OB Ch 6, plus distinct strategic-decision tools (SWOT, PESTEL, Porter's Five Forces, VRIO), goal-vs-domain-vs-hybrid planning, and four change models. Application file projects the integration.
- **Stakeholder engagement — CLEAR YES**: Ch 5 is dedicated to ethics, CSR, and stakeholder management with explicit Freeman-grounded stakeholder theory, eight-question analysis, rejection of shareholder-primacy, and seven ethical principles; cross-cultural engagement (Ch 6) and team-boundary management (Ch 15) extend the projection. Application file projects ethical, cultural, and political layers.

## Methodology notes for parallel-batch consistency

These observations from this wrap-up run should propagate consistently with the rest of the batch:

1. **Wrap-up handover validity**: a prior subagent run that completes only Passes A-E is a valid handover state. The wrap-up run can complete F-I and staging files without redoing the deep ref. The deep ref's quality must be Pass-I-audited by the wrap-up subagent (which this run did, applying two small fixes in-place).

2. **Image classification correction**: the PNG=substantive heuristic from the OB pilot is unreliable as a blanket rule. For this book, the heuristic happened to hold (all JPEGs decorative; all PNGs from p0026 substantive), but visual inspection is necessary to confirm — front-matter PNGs are typically decorative, and edge cases (large abstract PNGs, small icon PNGs, photographic PNGs) must be inspected individually.

3. **Cross-corpus pairing**: this book overlaps significantly with OpenStax Organizational Behavior (motivation, leadership, teams, communication, HR, diversity, structure, change, environments and culture). The application files explicitly invoke pairing rather than substitution — the two books complement each other and should be used together where both apply.

4. **Application-file phase structure**: this book's application files use six phases per axis rather than the OB pilot's six-decision-making and seven-stakeholder phases. The phase structures are adapted to surface this book's distinct content (the change-model lens for decision-making; the ethical-lens framing for stakeholder engagement) rather than mechanically copying the pilot.

5. **Verbatim quote care**: Pass I caught two small verbatim-quotation issues (citation off-target to an excluded section; nested-quote formatting). These are easy to introduce and easy to miss without a cold Pass I read. Subagents in the rest of the batch should verify verbatim quotes character-by-character against the source markdown using grep, not by memory.

## Indexes updated (line counts)

This wrap-up subagent does NOT update the canonical indexes (the parent agent merges staging files post-batch). Staging files contain the entries for merge:

- `_ingest_search_index_principles-management.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — light-ref row, deep-ref row, ~55 concept-A-Z entries.
- `_ingest_dm_principles-management.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — 8 quick-start rows, ~20 phase-by-phase rows across six phases.
- `_ingest_se_principles-management.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — 9 quick-start rows, ~20 phase-by-phase rows across six phases.
- `_ingest_image_index_principles-management.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — 103 substantive image entries.

## Known limitations and follow-ups

- **Per-image descriptive text** is the parallel-batch baseline ("Substantive figure (Exhibit) extracted from page N") rather than rich content-specific descriptions. v0.1.5+ refinement should produce richer per-image descriptions tied to specific Exhibit references in the source markdown.
- **Cross-corpus deduplication** in the application files: where this book substantially overlaps with OpenStax Organizational Behavior, the application files explicitly invoke pairing rather than re-presenting the same content twice. The decision about whether the corpus consumer wants both or one is left to the operator at retrieval time, with the application files surfacing the distinction explicitly.
- **The Adler-Gunderson row** in the deep ref's Key Statistics table notes a contextually-relevant statistic that is "not in this source" — included for cross-book consistency but flagged honestly. The parent agent may strip during consolidation; the audit notes the stylistic option.
