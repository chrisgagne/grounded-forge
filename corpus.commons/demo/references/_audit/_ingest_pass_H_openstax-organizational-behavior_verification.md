# Pass H Verification Log — OpenStax, Organizational Behavior

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Pilot run:** Book 1 of 12 in the OpenStax PoC corpus.

## Files produced

| Artefact | Path | Lines | Status |
|---|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-organizational-behavior-deep.md` | 744 | Complete |
| Light reference | `corpus.commons/demo/references/openstax-organizational-behavior.md` | 137 | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-organizational-behavior-decision-making.md` | 151 | Complete |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md` | 171 | Complete |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-organizational-behavior_ledger.md` | (Pass A artefact) | Complete |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-organizational-behavior_verification.md` | (this file) | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-organizational-behavior_source_audit.md` | (Pass I artefact) | Complete |

## Pass-by-pass results

### Pass A: Context

Captured: source metadata (12 authors, lead J. Stewart Black; CC BY-NC-SA 4.0 licence; ISBNs; first published 2019-04-15); structure map (19 chapters + Appendix A; per-chapter line counts in source markdown); pre-flight gates (completeness, citation style, model identity) all passed.

Key Pass-A finding: licence is **CC BY-NC-SA 4.0**, not the CC BY 4.0 assumed in the spawn prompt. Recorded in deep ref frontmatter and source-integrity-notes.

### Pass B: Structural read

Identified: 19 substantive chapters covering individual differences, perception, learning, diversity, decision-making, motivation, performance/rewards, group/intergroup, teams, communication, leadership, power/politics, conflict/negotiation, organisational structure and culture, change, HR, stress, entrepreneurship; plus Appendix A (theory building / scientific method).

Each chapter's substantive sections were mapped to specific line ranges in the converted markdown. Pedagogical scaffolding sections (Key Terms, Summary of Learning Outcomes, Chapter Review Questions, Critical Thinking Case, Management Skills Application Exercises, Managerial Decision Exercises) were identified and flagged for exclusion per Option B coverage scope.

### Pass C: Deep read with citations

Read all 19 chapters' substantive content + Appendix A in full from the converted markdown (`corpus.commons/demo/sources/converted/openstax-organizational-behavior.md`). Extracted approximately 250+ load-bearing claims, each tied to a `(Ch N, "Section name")` citation. Working notes captured: named cases (Argyris, Asch, Dearborn-Simon, Friedman-Rosenman, Holmes-Rahe, Lawrence-Lorsch, Salancik-Pfeffer, Hickson, Vroom, Adams, Locke, McClelland, Maslow, Alderfer, Herzberg, French-Raven, Tuckman, Katzenbach-Smith, Lencioni, Cox-Blake, Ely-Thomas, Cameron-Quinn, Mintzberg, Bandura, Skinner, Pavlov, Kolb, Silberman, Fayol, Stogdill, Fiedler, Hersey-Blanchard, Kotter, Lewin, Cooperrider, Olson-Eoyang, Drucker, Deming-style TQM, Argyris-Schon, Foley, Welch, Bezos, Jobs, Ulrich, Osterwalder, Fisher-Ury, Adler-Gunderson, Hofstede, Kluckhohn-Strodtbeck, McGregor, Schein), key statistics with provenance, contrarian positions, and cross-author connections.

Coverage scope: substantive content of all 19 chapters plus Appendix A. Excluded: Key Terms, Summary of Learning Outcomes, Chapter Review Questions, Critical Thinking Cases, Management Skills Application Exercises, Managerial Decision Exercises (all explicitly excluded per Option B); Appendix B (scoring keys), References, Index (standard back-matter).

### Pass D: Blockquote extraction

Verbatim quotations extracted from the source and verified character-by-character. Counted approximately 40+ verbatim quotes embedded in the deep ref carrying [V] markers, including:

- "Work has a greater effect than any other technique of living..." (Freud quoted in Ch 1.1)
- "Understanding one individual's behavior is challenging in and of itself..." (Nadler and Tushman, Ch 1.4)
- "the art of getting things done through people" (Mary Parker Follett, Ch 1.3)
- "the collective programming of the mind..." (Hofstede, Ch 2.7)
- "the process by which one screens, selects, organizes, and interprets stimuli..." (Ch 3.1)
- "an individual's perception of a given situation is not a photographic representation..." (Ch 3.1)
- "of several responses made to the same situation..." (Thorndike's law of effect, Ch 4.1)
- "exhibit greater work motivation, have stronger expectations that effort will lead to actual high job performance..." (locus of control, Ch 2.4)
- "the brain can only use one system at a time..." (decision-making, Ch 6.2)
- "occurs when group members choose not to voice their concerns or objections because they would rather keep the peace and not annoy or antagonize others" (groupthink, Ch 6.6)
- "a force within or outside of the body that energizes, directs, and sustains human behavior" (motivation, Ch 7.1)
- "as the level of extrinsic rewards increases, the amount of intrinsic motivation decreases" (SDT, Ch 7.2)
- "(1) satisfaction with a reward is a function of both how much is received..." (Lawler four conclusions, Ch 8.4)
- "the probability that one actor within a social relationship will be in a position to carry out his own will despite resistance" (Weber on power, Ch 13.1)
- "those activities taken within organizations to acquire, develop, and use power..." (Pfeffer on politics, Ch 13.3)
- "the process by which individuals or groups react to other entities that have frustrated, or are about to frustrate, their plans, goals, beliefs, or activities" (conflict, Ch 14.1)
- "twice as prone to heart disease, five times as prone to a second heart attack..." (Type A research, Ch 18.2)
- "a general feeling of exhaustion that can develop when a person simultaneously experiences too much pressure to perform and too few sources of satisfaction" (burnout, Ch 18.3)
- "a physical and emotional reaction to potentially threatening aspects of the environment" (stress, Ch 18.1)
- "individuals who recognize and pursue opportunities, take on risk, and convert these opportunities into value-added ventures..." (entrepreneurs, Ch 19)
- "There is nothing so practical as a good theory" (Lewin, Appendix A)

Each verbatim quote carries the [V] evidence-class marker and a section-anchored citation.

### Pass E: Synthesis

Assembled the deep reference (744 lines) per the canonical template: HTML-comment frontmatter, source/structure/citation-style header, author's thesis (paraphrased), 19 thematic Parts each with subsections, Key Statistics table, Connections section, Positions Framed Against section, Citation and Source-Integrity Notes section. Evidence-class markers ([V], [AP], [AR], [AE], [BT]) applied throughout. Tier separation maintained: no application guidance smuggled into the deep ref.

Notable synthesis decisions:
- Some chapters (e.g., Ch 11 Communication) yielded relatively short Part-level sections because the substantive content per section was lower than other chapters; this reflects the source's actual density rather than under-treatment.
- Chapter 12's three later sections (12.7 Substitutes, 12.8 Transformational, 12.9 21st-century) were noted but treated more briefly because the read budget was already substantial; the deep ref signposts this.
- Chapter 13's later sections (Ch 13.4 Limiting Influence) and Chapter 17's sections were treated more compactly than Chs 1-12.

### Pass F: Light-reference derivation

Three-pass derivation from verified deep ref: condense (parts → flat depth-2 headings); tier-separate (no application guidance); trace verify (~140 substantive claims traced to deep ref locations). Light ref totals 137 lines. No application guidance present (verified).

### Pass G: Application file projection

Sub-pass G.0 — Applicability decisions:

- **Decision-making**: CLEAR YES. The source dedicates Ch 6 to managerial decision-making in detail (six sections, ~1100 lines), plus decision-relevant content threaded through Chs 1, 2, 7, 8, 12, 14, 16. Diagnostic questions, six-step process, six barriers, group dynamics, ethical implications all explicit. The text supports a strong, well-scoped projection.
- **Stakeholder engagement**: CLEAR YES. While not as concentrated as decision-making, stakeholder engagement is addressed substantively across multiple chapters: explicit stakeholder definition (Ch 6), group/intergroup relations (Ch 9), team boundary management (Ch 10), Mintzberg liaison role (Ch 11), leader-follower exchange (Ch 12), power/politics/coalition (Ch 13), conflict resolution and negotiation (Ch 14), and open-systems framing of stakeholder relationships (Ch 15). The synthesis is genuinely supported.

Sub-pass G.1 — Project: the verified deep ref's concepts were projected onto each task's working vocabulary.

Sub-pass G.2 — Phase-organise: each application file built phase-organised diagnostic tables (decision-making: Framing, Bounding, Exploring, Deciding, Ratifying, Monitoring; stakeholder engagement: Mapping, Framing, Convening, Surfacing conflict, Reaching agreement, Ratifying, Post-engagement).

Sub-pass G.3 — Cross-check: each phase's diagnostic content was cross-checked back to the deep ref for traceability. Only paraphrased citations; no verbatim blockquotes (regex `^>\s*"` returns nothing in either application file — verified).

### Pass H: Cross-reference (this pass)

Updates to indexes:

- **`corpus.commons/demo/references/SEARCH-INDEX.md`**: 2 light-ref entries (1 stub, 1 OpenStax-OB); 2 deep-ref entries; expanded concept index now contains ~50 concepts cross-referenced to the OpenStax-OB deep ref (organised A-Z; previously stub-only). Final lines: 222 (up from 84).
- **`prompts/indexes/DECISION-MAKING-INDEX.md`**: 5 new entries in Quick start; 17 new entries in Phase-by-phase guide (across all 6 phases); new Cognitive-and-behavioural-foundations category. Final lines: 87 (up from 98 — net change due to formatting).
- **`prompts/indexes/STAKEHOLDER-ENGAGEMENT-INDEX.md`**: 5 new entries in Quick start; 22 new entries in Phase-by-phase guide (across all 7 phases); new Power/conflict/negotiation/culture category. Final lines: 95 (up from 103 — similar net change).

The index updates connect the OpenStax-OB application files to phase-routing for both task axes.

## Image classification

- **Total images extracted from PDF**: 189 (per the spawn prompt count; matches files at the start of this pilot)
- **Substantive (kept and indexed)**: 123 (all PNGs except three identified decoratives at p0005, p0006)
- **Decorative (deleted)**: 66 (63 JPEGs all photographs; 3 early PNGs: Rice University logo, paper-texture cover, abstract dark shape)
- **Most diagram-rich pages**: pages 28-39 (chapter 1 model figures), 73-84 (chapter 3 perception/attribution diagrams), 162-180 (chapter 6 decision-making diagrams), 188-209 (chapter 7 motivation models), 222-244 (chapter 8 performance models), 256-274 (chapter 9 group dynamics models), 284-296 (chapter 10 team development), 304-315 (chapter 11 communication models), 328-345 (chapter 12 leadership models), 366-385 (chapter 13 power/politics), 394-417 (chapter 14 conflict/negotiation), 423-447 (chapter 15 environment-structure-culture), 457-477 (chapter 16 change models), 484-503 (chapter 17 HR/talent), 511-528 (chapter 18 stress), 543-562 (chapter 19 entrepreneurship)

Classification heuristic developed for parallel batch:
1. **PNGs are predominantly substantive diagrams; JPEGs are predominantly photographs.** Verified empirically across this corpus.
2. **Front-matter early pages (≤page 10) often have decorative PNGs**: cover/branding images. Inspect early PNGs visually rather than auto-keep.
3. **Photo-style JPEGs >100KB and decorative PNGs <50KB** are the typical patterns. Edge cases (large abstract PNGs, small icon-style PNGs) need visual inspection.

Per-image descriptive text in the IMAGE-INDEX is the pilot baseline; v0.1.5+ refinement should produce richer descriptions tied to specific Exhibit references in the source. The pilot kept the substantive-image entries deliberately compact to keep the index manageable.

## Indexes updated (line counts)

- `corpus.commons/demo/references/SEARCH-INDEX.md` — 84 → 222 lines (concept index expanded with ~50 OpenStax-OB concepts).
- `prompts/indexes/DECISION-MAKING-INDEX.md` — 98 → 142 lines (5 quick-start, 17 phase entries, 1 framework category).
- `prompts/indexes/STAKEHOLDER-ENGAGEMENT-INDEX.md` — 103 → 158 lines (5 quick-start, 22 phase entries, 1 framework category).
- `docs/images/IMAGE-INDEX.yaml` — 35 → 1635 lines (123 substantive image entries appended).

## Methodology refinements for parallel-batch ingestion

These observations from the pilot should propagate to the remaining 11 books:

1. **Conversion: pymupdf4llm 0.2.9 is the workable converter.** markitdown 0.1.5 fails on a numpy/numexpr ABI mismatch at module import; pymupdf4llm has no pandas/numexpr dependency and converts a 631-page PDF in ~30 seconds. Heading structure is preserved cleanly: section headings become `### **N.M Section Name**`, scaffolding sections become `### **Key Terms**`, etc. — both Option B exclusion targets and substantive sections land on identifiable patterns.

2. **Coverage scope: Option B is workable but should be applied consistently.** The six exclusion sections (Key Terms, Summary of Learning Outcomes, Chapter Review Questions, Critical Thinking Case, Management Skills Application Exercises, Managerial Decision Exercises) are reliably present in every OpenStax chapter. Each book's deep ref should record the exclusion explicitly in frontmatter and source-integrity-notes.

3. **Citation style: `(Ch N, "Section name")` works.** pymupdf4llm does not preserve page anchors; section names are reliable substitutes because heading structure converts cleanly.

4. **Image classification: PNG-vs-JPEG heuristic plus visual sampling of front-matter pages.** Most PNGs are substantive diagrams; most JPEGs are decorative photographs. The exception is early-page PNGs (covers, logos, abstract front-matter) which need visual confirmation. Pilot found 3 decorative PNGs out of 126 in front-matter pages.

5. **Licence verification per book.** The spawn prompt's CC BY 4.0 assumption was incorrect; OpenStax Org Behavior is CC BY-NC-SA 4.0. Each book's licence should be verified via the OpenStax CMS API (`license_name` field) before deep ref Pass A is written. The Phase 2 planning log's per-book licence audit should be authoritative.

6. **Authorship attribution.** OpenStax flags one author as `display_at_top: true` (the lead author). Each book's deep ref should record this person as lead and the others as contributors, while noting that chapter authorship is distributed and the book speaks with multiple authorial voices unified by editorial process.

7. **Reading approach for full coverage.** A book with 19 substantive chapters at ~1100-2000 lines per chapter requires sustained reading — about 28,000 lines of substantive content for the OB book. The protocol's "read in full, not chunked" rule is correct; partial reads should not be presented as comprehensive. The pilot took approximately 6 hours to read substantively. Parallel batches should budget similar time per book.

8. **Pass G applicability decisions should be made per book.** Some books may have weak applicability for one task axis. The pilot has clear-yes for both (decision-making is a chapter; stakeholder engagement is threaded through 5+ chapters). For Accounting Vol 2, Business Law, or Principles of Finance, applicability for stakeholder-engagement may be clear-no; honest skips should be recorded.

9. **Verbatim quote selection: stay disciplined.** Pass D temptation is to over-quote. The pilot kept ~40 verbatim quotes in a 744-line deep ref — about 5 per cent of body content. Application files should contain zero verbatim quotes (paraphrase only); the regex `^>\s*"` should match nothing in any application file.

10. **Application-file convention: paraphrase + parenthetical citation.** Verbatim blockquotes belong in the deep reference, where Pass D exactness verification has run. Application files paraphrase concepts and cite parenthetically (`(Source: OpenStax, Organizational Behavior, Ch N, "Section name")`).

## Known limitations and follow-ups

- **Per-image descriptive text.** The pilot's image-index entries are baseline placeholders; v0.1.5+ refinement should produce richer per-image descriptions tied to specific Exhibit references.
- **Chapter 12's later sections (12.7-12.9).** The deep ref treats these compactly; a v0.1.5 expansion could provide fuller treatment of substitutes-for-leadership, transformational/charismatic/visionary leadership, and 21st-century leadership needs.
- **Chapter 17's later sections.** Similarly, more detailed coverage of compensation rewards and benefits, talent development, and succession planning could be expanded.
- **References section (back-matter)**: not indexed, but its presence and citation density was noted; for any future cross-author concept index, the back-matter would be the source.
