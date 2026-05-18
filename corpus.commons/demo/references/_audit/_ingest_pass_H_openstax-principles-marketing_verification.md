# Pass H Verification Log — OpenStax, Principles of Marketing

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Phase 2 parallel batch wrap-up.** This book hit rate limits during the parallel batch run; the 9-pass deep ref, light ref, both application files, and Pass A ledger were produced in the original run and exist on disk. This wrap-up subagent produces the missing artefacts: Pass H (this file), Pass I, four staging files for the consolidating parent agent.

## Files produced (canonical)

| Artefact | Path | Lines | Status |
|---|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-principles-marketing-deep.md` | 575 (post-Pass-I strip) | Complete |
| Light reference | `corpus.commons/demo/references/openstax-principles-marketing.md` | 127 | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-principles-marketing-decision-making.md` | 179 | Complete |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-principles-marketing-stakeholder-engagement.md` | 192 | Complete |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-principles-marketing_ledger.md` | (Pass A artefact) | Complete |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-principles-marketing_verification.md` | (this file) | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-principles-marketing_source_audit.md` | (Pass I artefact) | Complete |

## Files produced (staging — parent merges)

| Artefact | Path |
|---|---|
| SEARCH-INDEX staging | `_ingest_search_index_principles-marketing.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) |
| DECISION-MAKING-INDEX staging | `_ingest_dm_principles-marketing.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) |
| STAKEHOLDER-ENGAGEMENT-INDEX staging | `_ingest_se_principles-marketing.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) |
| IMAGE-INDEX staging | `_ingest_image_index_principles-marketing.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) |

## Pass-by-pass results (recovered from existing artefacts)

### Pass A: Context

Captured: source metadata (lead author Maria Gomez Albrecht, UT Dallas; nine contributing authors; first publication 2023; ©2026 Rice University; CC BY-NC-SA 4.0; ISBNs 978-1-711471-51-8 / 978-1-711471-52-5 / 978-1-951693-88-6); structure map (19 chapters across three units, plus Preface, Answer Key, Index); pre-flight gates (completeness, citation style, model identity) all passed.

Source: `corpus.commons/demo/sources/converted/openstax-principles-marketing.md` (41,595 lines / ~2 MB; 707-page PDF converted via pymupdf4llm 0.2.9).

### Pass B: Structural read

Identified: 19 substantive chapters in three units. Unit 1 (Setting the Stage): Marketing and Customer Value, Strategic Planning. Unit 2 (Understanding the Marketplace): Consumer Markets, Business Markets, STP, Marketing Research, Global Marketing, Diversity Marketing. Unit 3 (Product/Promotion/Price/Place): Products, NPD, Services, Pricing, IMC, Advertising/PR, Personal Selling/Sales Promotion, Direct/Online/Social/Mobile, Distribution, Retailing/Wholesaling, Sustainable Marketing.

Per-chapter scaffolding sections identified for Option B exclusion: Chapter Outline; Chapter Summary; Key Terms; Applied Marketing Knowledge: Discussion Questions; Critical Thinking Exercises; Building Your Personal Brand; What Do Marketers Do?; Marketing Plan Exercise; Closing Company Case; References (per-chapter footnote bibliography).

### Pass C: Deep read with citations

Read all 19 chapters' substantive content in full from converted markdown. Extracted approximately 230+ load-bearing claims, each tied to a `(Ch N, "Section name")` citation. Working notes captured: named cases (Coca-Cola, Apple/iPad/iPhone, Tesla, McDonald's, Netflix, Amazon, Patagonia, Bombas, Walmart, Disney, Tylenol J&J, Nike, Best Buy, Dollar Shave Club, Dove, Kylie Jenner, Hsieh/Zappos, IKEA, Ford, Nooyi/PepsiCo, Chouinard/Patagonia, Henderson, Kotler, Levitt, Ries-Trout, Hofstede, Maslow, Hall, Lovelock, Zeithaml/Parasuraman/Berry, Keller, Rogers); key statistics with provenance; contrarian positions; cross-author connections.

Coverage scope: substantive content of all 19 chapters plus In-the-Spotlight openers and numbered sections with Learning Outcomes. Excluded: scaffolding sections per chapter (10 named exclusion sections per chapter); Preface, Answer Key, Index back-matter.

### Pass D: Blockquote extraction

Verbatim quotations extracted from the source and verified character-by-character. Approximately 35 verbatim quotes embedded in the deep ref carrying `[V]` markers, including:

- "every process involved in moving a product or service from the organization to the consumer" (AMA-derived working definition, Ch 1.1)
- "the ratio between the perceived benefits and costs incurred by the customer in acquiring your products or services" (customer value, Ch 1.1)
- "a promise of value that communicates the benefits of your company's products or services" (value proposition, Ch 1.1)
- "the means through which companies track, manage, and analyze customer interactions" (CRM, Ch 1.6)
- "approximately 84 percent of customers indicate that loyalty programs are an incentive to remain with a brand, and 66 percent report that their spending behavior is actually altered by the ability to earn rewards" (Ch 1.6)
- "you can't be all things to all people" (Ch 5.1)
- "not to create something new and different, but to manipulate what's already up there in the mind" (Ries-Trout, Ch 5.6)
- "People don't want to buy a quarter-inch drill; they want a quarter-inch hole" (Levitt, Ch 5.2)
- "the function that links the consumer, customer, and public to the marketer through information" (Ch 6.1, AMA on marketing research)
- "an organization should meet the needs of its present consumers without compromising the ability of future generations to fulfill their own needs" (Kotler, Ch 19.1)
- "When you're only No. 2, you try harder. Or else." (Avis, Ch 5.6)
- "an intangible asset with tangible value" (brand, Ch 9.5)
- "a system of people, organizations, and activities that work together to make goods and services available to consumers to purchase" (marketing channel, Ch 17.1)
- "Sustainability to us is remaining a profitable business while doing the right thing" (Costco, Ch 19.2)
- "paid communication messages that identify a brand or organization and is intended to reach a large number of recipients" (advertising, Ch 14.1)

Each verbatim quote carries the `[V]` evidence-class marker and a section-anchored citation.

### Pass E: Synthesis

Assembled the deep reference (576 lines pre-strip; 575 post-Pass-I) per the canonical template: HTML-comment frontmatter, source/structure/citation-style header, author's thesis (paraphrased; five load-bearing claims), 14 thematic Parts each with subsections (Marketing fundamentals; Strategic planning; Consumer behaviour; B2B; STP; Research; Global; Diversity; Products and services; NPD; Pricing; IMC; Distribution and retailing; Sustainable marketing), Key Statistics table, Connections section, Positions Framed Against section, Citation and Source-Integrity Notes section. Evidence-class markers (`[V]`, `[AP]`, `[AR]`, `[AE]`, `[BT]`) applied throughout. Tier separation maintained: no application guidance smuggled into the deep ref.

### Pass F: Light-reference derivation

Three-pass derivation from verified deep ref: condense (parts → flat depth-2 headings); tier-separate (no application guidance); trace verify (~120 substantive claims traced to deep ref locations). Light ref totals 127 lines. No application guidance present (verified).

### Pass G: Application file projection

Sub-pass G.0 — Applicability decisions:

- **Decision-making**: CLEAR YES. The book is dense with explicit decision points across the marketing mix (4Ps decisions; pricing objective choice; promotion-mix selection; channel intensity), strategic-planning decisions (vision, mission, gap analysis, SMART goals, BCG, SWOT, four growth strategies), customer-journey decisions (segmentation/targeting/positioning), new-product decisions (nine-stage NPD), and distribution decisions. Every chapter is built around decisions a marketer or general manager makes; the projection is well-scoped.
- **Stakeholder engagement**: CLEAR YES. The book treats marketing engagement explicitly as multi-stakeholder. Ch 1.1 names "interested parties" as stakeholders (internal: employees, owners, managers, investors; external: customers, creditors, suppliers, distributors, society). Ch 11.2 service-profit chain links employee engagement to customer value. Ch 11.2 Service Marketing Triangle names three engagement legs. Ch 11.3 Gap Model names five engagement breakdowns. Ch 14.4 PR explicitly multi-public. Ch 8 multicultural / sociodemographic engagement. Ch 19.2 explicit stakeholder-vs-shareholder framing. Strong projection support.

Sub-pass G.1 — Project: the verified deep ref's concepts were projected onto each task's working vocabulary.

Sub-pass G.2 — Phase-organise: each application file built phase-organised diagnostic tables (decision-making: Frame the situation, Choose the customer focus, Decide on the marketing mix, NPD/innovation, Distribution and operations, Pick metrics and monitor, Sustainability/ethics review; stakeholder engagement: Map the stakeholders, Choose engagement intent, Choose channels and message, Engage employees, Engage customers across the journey, Engage suppliers/intermediaries, Engage public/regulators/community/planet, Resolve engagement breakdowns).

Sub-pass G.3 — Cross-check: each phase's diagnostic content was cross-checked back to the deep ref for traceability. Only paraphrased citations; no verbatim blockquotes (regex `^>\s*"` returns nothing in either application file — verified).

### Pass H: Cross-reference (this pass — deferred to staging)

Per parallel-batch protocol, this subagent does NOT touch canonical indexes (race risk). Instead, the cross-reference work produces four staging files for the consolidating parent agent to splice into the canonical indexes:

- **SEARCH-INDEX staging** (`_ingest_search_index_principles-marketing.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation)): light-ref table row, deep-ref table row, ~70 concept-A-Z entries pointing at deep-ref Parts and sections.
- **DECISION-MAKING-INDEX staging** (`_ingest_dm_principles-marketing.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation)): Quick-start rows for marketing-decision archetypes; phase-by-phase additions for Frame / Choose customer focus / Marketing-mix / NPD / Distribution / Metrics / Sustainability-and-ethics phases.
- **STAKEHOLDER-ENGAGEMENT-INDEX staging** (`_ingest_se_principles-marketing.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation)): Quick-start rows for engagement archetypes; phase-by-phase additions for Mapping / Engagement intent / Channels-and-message / Employee / Customer-journey / Supplier-and-intermediary / Public-regulators-community-planet / Resolve-breakdowns phases.
- **IMAGE-INDEX staging** (`_ingest_image_index_principles-marketing.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation)): substantive PNG entries; decoratives flagged for deletion.

## Image classification

- **Total images extracted from PDF**: 234 (121 PNG, 113 JPEG)
- **Substantive (kept and indexed)**: 117 (PNG concept diagrams of frameworks, models, charts, decision trees, segmentation visualisations)
- **Decorative (deleted from disk)**: 117 (113 JPEGs — all photographs of products, people, places; 4 PNGs: Rice University logo at p0005-1, paper-texture frame at p0006-1, abstract dark frame at p0006-6, and a six-pane food-photograph collage at p0324-1)

Methodology: per the post-pilot correction (the pilot's "PNG = substantive, JPEG = decorative" heuristic is unreliable — Entrepreneurship had only 3 of 21 PNGs substantive, Business Ethics had zero of 8), each of the 121 PNGs was opened and visually inspected before classification. For *Principles of Marketing* the heuristic happened to hold strongly — only 4 PNGs were decorative (the three front-matter design elements plus one mid-book photograph collage at Ch 8.3). The remaining 117 PNGs are concept diagrams from the OpenStax in-house figure system (4Ps Mix, Marketing Process, BCG, SWOT, STP, NPD nine-stage, 5A journey, RATER, Gap Model, etc.), all of which are substantive frameworks referenced by the deep ref.

Per-image descriptive text in the staging YAML names the figure number, title, and content of each diagram, with tags and a one-line suggested-use cue mapping the image to a decision-making or stakeholder-engagement phase. The staging YAML lists all 117 substantive images.

## Pass G.0 record

- Decision-making axis: **clear-yes** — Marketing decisions are the book's organising principle.
- Stakeholder-engagement axis: **clear-yes** — Multi-stakeholder framing throughout, explicit in Ch 1.1, Ch 11, Ch 19.

## Methodology refinements observed

1. **Heuristic robustness — overridden by visual inspection.** The pilot heuristic ("PNG = usually substantive, JPEG = usually decorative") was tested against visual inspection of every PNG. For this book it largely held (117 of 121 PNGs were substantive concept diagrams), but four PNGs were decorative — three front-matter assets at pages 5–6 and one photograph collage at page 324. The corrected methodology is: visually inspect each image before classifying. Per the post-pilot Entrepreneurship and Business Ethics audits, the heuristic is unreliable across the corpus and must not be used as a shortcut.
2. **Coverage scope.** Option B exclusions named consistently in this book (10 scaffolding section types per chapter), reliably identified via `### **...**` heading pattern.
3. **Citation style.** `(Ch N, "Section name")` works; pymupdf4llm preserves section heading structure cleanly.
4. **License verified.** Front matter confirms CC BY-NC-SA 4.0 (matches all OpenStax non-Business-Law / non-Anatomy books in the corpus).
5. **Connections-section discipline.** Pass I caught one cross-author claim (Mary Parker Follett) that the source does not cite; stripped. The deep ref's Connections section must be checked claim-by-claim against the source — author-name grep is the right tool.

## Known limitations

- **Per-image descriptive text.** Staging YAML uses pilot-baseline placeholders; v0.1.5+ refinement should produce richer per-image descriptions tied to specific Exhibit references (e.g., "Exhibit 1.5 The 4Ps of Marketing").
- **Closing-chapter (Ch 19) treatment.** Per the source's own note, Ch 19 is "supplemental" with fewer features than other chapters; deep-ref treatment is correspondingly compact (Part XIV).
- **Ch 8 multicultural-population statistics.** Statistics are 2020 Census-era; will need refresh when 2030 Census data are available.
