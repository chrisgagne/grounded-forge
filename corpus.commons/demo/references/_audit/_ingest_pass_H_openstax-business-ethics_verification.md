# Pass H verification — OpenStax, Business Ethics

**Model identity:** claude-opus-4-7[1m] (Opus 4.7, 1M context). Confirmed at Step 0 of the parallel-batch instructions.

## Pass-by-pass results

| Pass | Output | Status |
|---|---|---|
| A: Context | `_ingest_pass_A_openstax-business-ethics_ledger.md` | Complete |
| B: Structural read | Internal map; 11 substantive chapters + 3 substantive appendices identified | Complete |
| C: Deep read with citations | Source markdown read in full (lines 1-20239); citation style `(Ch N, "Section name")` and `(App {A|B|C}, "Section name")` applied to all non-trivial claims | Complete |
| D: Blockquote extraction | 12 verbatim blockquotes selected and verified character-by-character against the source markdown | Complete |
| E: Synthesis | `corpus.commons/demo/references/openstax-business-ethics-deep.md` (659 lines) | Complete |
| F: Light-ref derivation | `corpus.commons/demo/references/openstax-business-ethics.md` (165 lines); ~180 substantive claims traced to deep ref | Complete |
| G.0: Applicability | Decision-making: clear-yes; Stakeholder-engagement: clear-yes (see below) | Complete |
| G.1-G.3: Projection | `prompts/applications/decision-making/openstax-business-ethics-decision-making.md` (170 lines); `prompts/applications/stakeholder-engagement/openstax-business-ethics-stakeholder-engagement.md` (180 lines); zero verbatim blockquotes verified by `grep -n '^>\s*"'` returning no matches | Complete |
| H: Cross-reference | This file plus staging files for SEARCH-INDEX, DM-INDEX, SE-INDEX, IMAGE-INDEX | Complete |
| I: Source-only audit | `_ingest_pass_I_openstax-business-ethics_source_audit.md` | Complete |

## Pass G.0 applicability decisions

### Decision-making axis: clear-yes

The book is a sustained treatment of ethical decision-making. Reasons:

- **Three normative ethical theories** explicitly framed as decision lenses (Ch 1.1, "Ends, Means, and Character in Business").
- **Single ethical standard** is itself a decision rule (Ch 1.3).
- **Moral minimum, ethical minimum, ethical maximum** — practical decision typology (Ch 3.1, Ch 4.1).
- **Categorical imperative** as decision criterion (Ch 2.5).
- **Veil-of-ignorance test** as procedural decision tool (Ch 2.6).
- **Phronesis** as the practical-wisdom virtue underlying ethical decision-making (Ch 1.1).
- **Worked decision contexts** in nearly every chapter: insider trading, bribery, whistleblowing, hiring and firing, accommodation, harassment response, layoff communication, sustainability investments, animal-testing decisions, advertising-targeting decisions, telecommuting policy, contractor classification.
- **Lead author's "succinct theory"** (Appendix C) is itself a credo about how to make ethical business decisions.

### Stakeholder-engagement axis: clear-yes

Chapter 3 ("Defining and Prioritising Stakeholders") is dedicated to the central engagement question; Chapter 4 ("Three Special Stakeholders: Society, the Environment, and Government") extends it. Reasons:

- **Stakeholder definition** is foundational to the book's argument structure (Ch 1.1, Ch 3.1).
- **Donaldson and Preston three-approach taxonomy** (descriptive, instrumental, normative) directly applies to engagement-method selection (Ch 3.2).
- **Grunig and Hunt linkage model** (enabling, normative, functional, diffused) categorises stakeholders for engagement (Ch 3.2).
- **Four publics** (nonpublic, latent, aware, active) — a communication-strategy taxonomy (Ch 3.2).
- **Stakeholder prioritisation tools** — power × interest, exigency, MITRE five-step (Ch 3.3).
- **Triple bottom line** (Elkington) reframes stakeholder externalities (Ch 3.4).
- **Social contract** with society as stakeholder (Ch 1.2, Ch 4.1).
- **Earth jurisprudence** treats environment as stakeholder with legal standing (Ch 4.2).
- **Cross-cultural engagement** (Ch 5.3 on localisation, contact / noncontact cultures, time conventions).
- **Employee engagement** (Ch 6, Ch 8) — workplace, wages, accommodation, diversity, inclusion.
- **Whistleblowing as stakeholder voice** (Ch 7.5).
- **Tone at the top** as engagement-leadership lever (Ch 11.3).

## Image classification

**Total images extracted:** 103 files (95 JPEG, 8 PNG).

**Substantive count:** 0 (zero) — the textbook uses textual / typographic figures (e.g., Figure 1.5 "stakeholder priority spreadsheet" is a textual three-column layout; Figure 3.4 "organisational linkage" is a labelled-text diagram in OpenStax style; Figure 3.6 "triple bottom line" is a text-labelled Venn-style figure). These conceptual diagrams render in the source PDF as composited illustrations whose extraction by `extract-images.py` yields the underlying photo plates rather than the conceptual diagrams themselves. Visual sampling of the 8 PNGs (p0005-1 Rice University logo; p0006-1 paper texture; p0006-6 dark frame; p0024-1 Buffett-Obama photo; p0113-1 solar-panel house photo; p0115-1 Keystone XL protest photo; p0119-1 Deepwater Horizon fire photo; p0024-1 photo) confirmed all are decorative photographs or front-matter design elements rather than framework diagrams. Visual sampling of representative JPEGs confirmed they are photographs (executives, historical figures, scenes).

**Decorative count:** 103 (all extracted images).

**Methodology note:** The pilot's heuristic (PNG = usually substantive diagram, JPEG = usually decorative photo) does not transfer well to *Business Ethics*. This book's pedagogy relies on case discussion and prose framing rather than on conceptual diagrams. Where the source PDF carries figures with conceptual content (stakeholder priority spreadsheet, linkage model, triple bottom line, Aristotelian virtue chart, codetermination tables), these figures are typographic compositions in the OpenStax layout — `extract-images.py` does not extract them as standalone images. Operators wishing to source visual representations of these frameworks for compiled distributions will need to author or licence them separately.

**Action:** the substantive image list in `_ingest_image_index_business-ethics.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) is empty. Per the parallel-batch instructions, the file is emitted with a header comment documenting the zero count so the parent agent can splice it cleanly into `docs/images/IMAGE-INDEX.yaml` (with a note about the textual-figures finding). All 103 image files in `docs/images/business-ethics/` may be deleted by the parent agent during consolidation, since none are indexed.

## Claim count

**Approximate substantive claim count in the deep ref:** ~340 distinct claims (counting prose claims with inline citations and table rows; not counting individual statistics in the key-statistics table separately from the claim-bearing paragraph that introduces them).

**Approximate claim count in the light ref:** ~180 substantive claims, all traced to the deep ref.

**Verbatim blockquote count:** 12 (Author's thesis section opening; Mill's harm principle; Kant's categorical imperative; Donaldson and Preston on intrinsic value; Howard Ross on diversity-and-inclusion; Aristotle on happiness; Aristotle on magnanimity; Ch 1.3 ethical-theorist convergence; Ch 1.2 stockholders / stakeholders / errors; App C on deontology preference; Ch 1.1 business-ethics definition; restated definitions). Each was character-verified against the source markdown in Pass D.

## Stage / staging files produced

| File | Purpose |
|---|---|
| `corpus.commons/demo/references/_ingest_pass_A_openstax-business-ethics_ledger.md` | Pass A ledger |
| `corpus.commons/demo/references/_ingest_pass_H_openstax-business-ethics_verification.md` | This Pass H verification log |
| `corpus.commons/demo/references/_ingest_pass_I_openstax-business-ethics_source_audit.md` | Pass I source-only audit |
| `_ingest_search_index_business-ethics.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | Staging entries for SEARCH-INDEX.md (light-ref row, deep-ref row, concept-A-Z entries) |
| `_ingest_dm_business-ethics.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | Staging entries for DECISION-MAKING-INDEX.md |
| `_ingest_se_business-ethics.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | Staging entries for STAKEHOLDER-ENGAGEMENT-INDEX.md |
| `_ingest_image_index_business-ethics.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | Staging entries for IMAGE-INDEX.yaml (empty list with header note) |

## Pipeline issues encountered

1. **Markdown artefacts.** The pymupdf4llm 0.2.9 conversion produces section headings with markdown emphasis markers (e.g., `### **2.1 The Concept of Ethical Business in Ancient Athens**`). Citations in the deep ref strip these markers (e.g., `(Ch 2.1, "The Concept of Ethical Business in Ancient Athens")`). The conversion also occasionally splits headings across two lines (e.g., the App B title splits "Profiles in Business Ethics: Contemporary Thought" + " B " + " Leaders" — a layout artefact from the PDF's two-column format). Citations use the joined readable title.

2. **Footnote references.** Footnotes in the source appear as inline `[1]`, `[2]`, etc. (not always sequential at chapter boundaries). The deep ref does not preserve footnote numbers; instead, where a third-party attribution carries the [BT] marker, the source text's attribution is summarised in the prose.

3. **Roman-numeral footnotes in appendices.** Appendix A and B use Roman-numeral footnotes (i, ii, iii ...) in addition to chapter footnotes. These were tracked when reading but are not separately cited.

4. **Substantive images sparse.** As noted in the image-classification section, this book's pedagogy uses textual / typographic figures rather than extractable concept diagrams. The 0-image substantive count is unusual relative to the pilot but reflects the source.

5. **Evidence-marker calls.** Some claims required judgment between [AP] (paraphrasing the author) and [BT] (the author attributes to a third party). Convention applied: if the author cites a named scholar / theorist (Donaldson, Preston, Grunig, Hunt, Elkington, Hardin, Pigou, Galbraith, Weber, Drucker, Reich, Bainbridge, Stout, Rest, Ross, Cullinan, Berry, Stone, Latham, Lindahl, Neumark, Wascher, etc.), the marker is [BT]. If the author makes a structural argument or normative position not derived from a named authority, the marker is [AP] or [AR]. Where a verbatim quote is reproduced, [V] travels with it.

6. **No partial-coverage degradation.** Per the source-integrity rule, the entire substantive content of all eleven chapters and three appendices was read. Excluded sections (Key Terms, Summary, Assessment Questions, Endnotes, Answer Key, Index) are pedagogical scaffolding declared in the deep-ref frontmatter.

## Token and effort estimate

- Pass A (ledger): light. ~10 minutes operator equivalent.
- Pass B (structural read): medium. Chapter / section identification and high-level mapping.
- Pass C (deep read): heavy. The source is 20,239 lines; full substantive coverage required reading all eleven chapters and three appendices.
- Pass D (blockquote verification): medium.
- Pass E (synthesis): heavy. The deep ref runs 659 lines.
- Pass F (light derivation): medium. 165 lines.
- Pass G (applicability + projection): heavy. Two application files at 170 and 180 lines each.
- Pass H (cross-reference + staging): medium. Four staging files plus this verification log.
- Pass I (source-only audit): medium-heavy. See the audit log for details.

Overall effort: heavy. Token usage will be reported by the harness.
