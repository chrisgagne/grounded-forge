# Pass H Verification Log — OpenStax, Entrepreneurship

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Run:** Phase 2 batch ingestion (one of 11 books).

## Files produced

| Artefact | Path | Status |
|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-entrepreneurship-deep.md` | Complete |
| Light reference | `corpus.commons/demo/references/openstax-entrepreneurship.md` | Complete |
| Decision-making application | `prompts/applications/decision-making/openstax-entrepreneurship-decision-making.md` | Complete |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-entrepreneurship-stakeholder-engagement.md` | Complete |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-entrepreneurship_ledger.md` | Complete |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-entrepreneurship_verification.md` | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-entrepreneurship_source_audit.md` | Complete |
| Search-index staging | `_ingest_search_index_entrepreneurship.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | Complete |
| Decision-making index staging | `_ingest_dm_entrepreneurship.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | Complete |
| Stakeholder-engagement index staging | `_ingest_se_entrepreneurship.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | Complete |
| Image-index staging | `_ingest_image_index_entrepreneurship.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | Complete |

## Pass-by-pass results

### Pass A: Context

Captured: source metadata (21 contributing authors total — 2 senior + 19 contributors; senior authors Michael Laverty and Chris Littel; CC BY-NC-SA 4.0 licence; ISBNs; original publication year 2020); structure map (15 chapters, no formal Appendix beyond a "Suggested Resources" reading list); pre-flight gates passed. Citation style chosen: `(Ch N, "Section name")` because pymupdf4llm does not preserve PDF page anchors.

### Pass B: Structural read

Identified: 15 substantive chapters covering the entrepreneurial perspective and mindset, journey and pathways, ethics and CSR, creativity and innovation, opportunity identification, problem solving (lean and design thinking), pitching and storytelling, marketing and sales, finance and accounting, lean startup launch, business model and plan, networks and team building, legal/tax/risk structures, resource planning, and next steps. Section counts and source line ranges recorded in the Pass A ledger.

Per-chapter pedagogical scaffolding (Key Terms, Summary, Review Questions, Discussion Questions, Case Questions, Suggested Resources) identified and flagged for exclusion per Option B coverage scope. Appendix A (Suggested Resources reading list) and Index excluded as standard back-matter.

### Pass C: Deep read with citations

Read all 15 chapters' substantive content in full from the converted markdown (`corpus.commons/demo/sources/converted/openstax-entrepreneurship.md`). Extracted approximately 200+ load-bearing claims, each tied to a `(Ch N, "Section name")` citation. Working notes captured: named cases (Phil Libin/Evernote, Chloe Huang algae pavilion, Warby Parker, Burt's Bees/Roxanne Quimby, Spanx/Sara Blakely, Bee Love/Brenda Palms Barber, Vital Vio, Stacy's Pita Chips, FedEx/Fred Smith, Chris Johnson/Rapid Brands, Drybar/Alli Webb, Birchbox, iBackPack failure, Dropbox/Drew Houston, IMVU/Eric Ries, Zappos/Nick Swinmurn, Quirky, Vita Coco, Stitch Fix, Twitter from Odeo, La Vida Lola fictional case, New Story 3D-printed homes, Johnny Cupcakes, Hometown Pizzeria fictional case, Lovepop, YouTube/Google harvest, Foursquare, MooseJaw, Drycabin, Lay's Do Us a Flavor, Niantic Ingress/Pokémon GO, Method cleaning products, TOMS Shoes/Mycoskie, Project Shakti/Unilever, Sweet Beginnings/Bee Love, BitGiving, Embrace Innovations, GE FastWorks, Toyota lean, Sherron Watkins/Enron, J&J Tylenol, GM ignition switch, Equifax breach, Eli Lilly Zyprexa, Martin Shkreli/Turing, Madoff, Volkswagen, Gordon Moore/Fairchild/Intel, Madam C. J. Walker, Charles Drew, Sybilla Masters, Mary Dixon Kies, Thomas Jennings, Andrew Carnegie, Eli Whitney, Elias Howe, Samuel Morse, Polaroid OneStep+, Nintendo from Hanafuda cards, Nikola Tesla); key statistics with provenance; contrarian positions; cross-author connections (Schumpeter, Smith, Drucker, Christensen, Ries, Blank, Andreessen, Osterwalder/Pigneur, Maurya, Kelley/Brown/IDEO, Chesbrough, Kawasaki, de Bono, Rogers, Granovetter, Kirton, Brabham, Markides, Pfeffer/Salancik, Kahn-style biases via Cossette, Wallas, Klein, Sandberg, McClelland-style F&F vs VC funding distribution).

Coverage scope: substantive content of all 15 chapters. Excluded: Key Terms, Summary, Review Questions, Discussion Questions, Case Questions, Suggested Resources (all explicitly excluded per Option B); Appendix A reading list; Index.

### Pass D: Blockquote extraction

Verbatim quotations extracted from the source and verified character-by-character. Approximately 35 verbatim quotes embedded in the deep ref carrying [V] markers. Selected quotes:

- "an entrepreneur is someone who identifies and acts on an idea or problem that no one else has identified or acted on" (Ch 1.1)
- "in the for-profit world, an entrepreneur is someone who creates and runs a new business where one did not exist before" (Brown, cited Ch 1.1)
- Schumpeter's creative destruction definition (Ch 2.2)
- Whyte on bureaucratic social ethic (Ch 2.2)
- Mozart on incubation (Ch 4.3, citing Zaslaw)
- Christensen's disruptive technology definition (Ch 1.3)
- Andreessen's "great markets pull product out of the startup" (Ch 7.3)
- Schumpeter on entrepreneurial value creation (Ch 5.1)
- Chesbrough on open innovation (Ch 4.1)
- Brabham on crowdsourcing (Ch 6.2)
- Tim Brown on design thinking (Ch 6.3)
- ASQ on Six Sigma (Ch 6.4)
- Cossette via the chapter on cognitive biases of entrepreneurs (Ch 15.2)
- Bailey and Rehman on reflection from HBR (Ch 15.5)
- Multiple verbatim definitions from key-terms-style framing within chapter text (creativity, innovation, invention, pivot, MVP, lean startup, hubris, escalation of commitment, etc.)

Each verbatim quote carries the [V] evidence-class marker and a section-anchored citation.

### Pass E: Synthesis

Assembled the deep reference per the canonical template: HTML-comment frontmatter, source/structure/citation-style header, author's thesis (paraphrased), 15 thematic Parts each with subsections, Key Statistics table (~37 metrics with provenance), Connections section (~25 cited authors with [BT] markers), Positions Framed Against section (~6 contrarian positions), Citation and Source-Integrity Notes section. Evidence-class markers ([V], [AP], [AR], [AE], [BT]) applied throughout. Tier separation maintained: no application guidance smuggled into the deep ref.

Notable synthesis decisions:

- Chapters with high named-case density (Ch 7 pitching, Ch 8 marketing, Ch 9 finance) were summarised at the framework level rather than enumerating every example, to keep the deep ref usefully navigable rather than duplicating the source text.
- Chapter 13 (legal/tax/risk) was treated more compactly than the conceptual chapters because much of its content is procedural rather than framework-level; the deep ref captures the entity-selection decision tree but does not enumerate every state-by-state variation.
- Where the source describes a tool (e.g., the Business Model Canvas) that has its own canonical reference outside this text (Osterwalder and Pigneur), the deep ref cites the originator with [BT] and treats the OpenStax presentation as a teaching summary.

### Pass F: Light-reference derivation

Three-pass derivation from verified deep ref: condense (parts → flat depth-2 headings); tier-separate (no application guidance); trace verify (~140 substantive claims traced to deep ref locations). Light ref totals approximately 200 lines. No application guidance present (verified by section review).

### Pass G: Application-file projection

#### Pass G.0: Applicability assessment

- **Decision-making:** Clear-yes. The entire book is structured around decisions an entrepreneur must make (vision, structure, funding, pivot, hire). Many sections directly address decision-making frameworks (build-measure-learn loop, go-or-no-go, Delphi method, Nominal Group technique, six entrepreneurial problem-solving skills, two problem-solving models, ten pivot strategies, fail-safe points). The text catalogues cognitive biases (Ch 15.2) that interfere with entrepreneurial decisions and offers structured group-decision techniques (Ch 15.3).
- **Stakeholder-engagement:** Clear-yes. The text explicitly distinguishes shareholders from stakeholders (Ch 3.1), reproduces the Business Roundtable's 2019 stakeholder commitment, treats customer empathy mapping as a core design tool (Ch 11.2), covers audience-tailored pitching to multiple stakeholder categories (Ch 7.3), introduces social entrepreneurship and B-corp certification (Ch 3.2), and develops post-harvest mentor/consultant/champion roles (Ch 15.4). Founders' agreements (Ch 15.1) are treated as the foundational stakeholder-engagement document.

Both projections were produced.

#### Pass G.1-G.3: Project, phase-organise, cross-check

Decision-making application file: 23 key concepts identified and traced; six-phase question structure (opportunity recognition, validation and lean iteration, structure and funding, operational and go-to-market, pivot/scale/exit, structured group decisions); ten what-to-look-for patterns; one worked example (veterinary CRM founder pre-pivot); six anti-patterns; integration table mapping to four external frameworks.

Stakeholder-engagement application file: 20 key concepts identified and traced; seven-phase question structure (stakeholder identification, customer engagement, founders/employees/culture, investors/capital partners, suppliers/partners/network, community/regulators/public, post-harvest roles); ten what-to-look-for patterns; one worked example (community food cooperative pre-launch); eight anti-patterns; integration table mapping to six external frameworks.

Both application files contain zero verbatim blockquotes (verified manually): the regex `^>\s*"` matches nothing in either file.

### Pass H: Cross-reference (this file)

Staging files produced for parent-agent merge:

- `_ingest_search_index_entrepreneurship.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — light-ref row, deep-ref row, concept-A-Z entries.
- `_ingest_dm_entrepreneurship.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — decision-making index entries.
- `_ingest_se_entrepreneurship.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — stakeholder-engagement index entries.
- `_ingest_image_index_entrepreneurship.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — image index YAML for merge into `docs/images/IMAGE-INDEX.yaml`.

### Pass I: Source-only audit

See `_ingest_pass_I_openstax-entrepreneurship_source_audit.md` for the full audit log. Summary: ~210 claims audited, ~208 source-anchored without modification, 1 marker correction, 1 strip; 35+ verbatim blockquotes verified character-by-character against source; zero application guidance in the deep ref; zero post-source vocabulary.

## Image classification

The image directory `docs/images/entrepreneurship/` contains 222 images. Classification was done via filename heuristic per the parallel-batch instructions (PNG = usually substantive diagram; JPEG = usually decorative photograph), then sampled spot-check for confirmation against figure captions in the source markdown.

- **Substantive (PNG-dominant, framework diagrams and process flows):** approximately 145 images. These include the Business Model Canvas (Figure 2.22), Lean Strategy Canvas (Figure 2.23), Design Thinking Process (Figure 2.24), Four Lenses Strategic Framework (Figure 2.25), the build-measure-learn loop (Figure 10.3), the lean plan cycle (Figure 10.14), the venture life cycle (Figure 2.20, Figure 14.15, Figure 10.15), the diffusion curve (Figure 4.9), Drucker's seven sources of innovation (Figure-style Table 4.3), the Six Thinking Hats (Figure 4.4), the empathy map (Figure 11.9), the SMART goals diagram (Figure 1.9, Figure 7.4), the SWOT analysis (Figure 5.9), the PEST analysis (Figure 5.10, Figure 14.10-14.11), the three-circles tool (Figure 5.11), the marketing-mix 7Ps (Figure 8.3), the six-step sales process (Figure 8.15), the accounting equation (Figure 9.6), the financial statements diagrams (Figures 9.7-9.16), the cognitive biases diagram (Figure 15.5), and many process-flow diagrams.
- **Decorative (JPEG-dominant, founder portraits and product photos):** approximately 77 images. These include the Phil Libin/Evernote portrait (Figure 1.1), Warby Parker founders (Figure 1.2), Burt's Bees product (Figure 1.3), various entrepreneur portraits (Madison, Madam C. J. Walker, Steve Jobs etc.), product shots (Bee Love products, Birchbox, Drybar locations, Polaroid cameras, Lovepop kirigami cards, the HP garage), location photos, and decorative scenery.

The detailed image-by-image classification is in the staging file `_ingest_image_index_entrepreneurship.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation).

## Known issues and notes

- **Multi-author voice:** with 21 contributing authors, some chapters have markedly different writing styles; the deep ref attributes claims to chapter and section as the source presents them, treating the text as a single integrated work.
- **Repeated content:** the source has substantial repetition across chapters (e.g., SMART goals introduced in Ch 1.2 and re-introduced in Ch 7.1; Christensen disruptive innovation in Ch 1.3, Ch 4.2, and Ch 11.1; lean startup in Ch 4.2 and Ch 10). The deep ref consolidates these into the chapter where the concept first or most fully appears, with cross-references where re-treatment matters.
- **Fictional cases:** the text uses fictional cases (Hometown Pizzeria, La Vida Lola, Helios Panels, Christina's Confections, Soraya's tutoring) alongside real cases. The deep ref preserves the fiction-vs.-real distinction in passing where the source itself is explicit.
- **Time-bound statistics:** several statistics are dated (2018-2019). The deep ref reports them with their year-of-publication context per the source.

## Token usage estimate

Per-pass effort estimate (heuristic, not measured):

- Pass A: light (metadata extraction)
- Pass B: medium (structure mapping over 15-chapter, 36,500-line source)
- Pass C: heavy (full read of all 15 chapters; primary effort sink)
- Pass D: medium (blockquote extraction and verification)
- Pass E: heavy (synthesis into deep ref)
- Pass F: medium (light-ref derivation)
- Pass G: medium-heavy (two application files with phase-organised tables and worked examples)
- Pass H: light (this file plus staging files)
- Pass I: medium (source-only audit, see separate file)

Source size pushed Pass C/E into the heavy band; the deep ref length reflects that the source covers a wide breadth of frameworks rather than going deep on a few.
