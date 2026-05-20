---
name: finding-resources
description: Discovers and triages candidate sources before ingestion. Produces a triage report with licence, distribution scope, format, viability verdict, and gap-fit notes: three buckets (proceed, sample first, skip). Each `proceed` entry is shaped as ready input for `ingesting-resources`.
argument-hint: "[topic or gap query] [licence-filter: cc-only|permissive|unfiltered]"
---

# Finding Resources

Discovery and triage of candidate sources before paying the 9-pass ingestion cost. Each invocation produces a triage report at an operator-chosen path with three buckets:

- **proceed**: viable; ready to feed into `ingesting-resources`
- **sample first**: uncertain on one of the viability checks; one more probe needed
- **skip**: not viable, with the specific reason recorded

Viability rules in [`docs/architecture/source-integrity.md`](../../../docs/architecture/source-integrity.md). Licence/scope distinction in the *Distribution scope* section of [`README.md`](../../../README.md) and [`docs/architecture/copyright.md`](../../../docs/architecture/copyright.md).

## When to use

- Filling a thin distillation in an existing distillation index (e.g. the decision-making axis has no source on project management).
- Adding a new task axis (`creating-tasks` → `creating-applications` workflow): need candidate sources whose framing maps onto the new axis.
- Forking the repo for a new corpus: step 2 of the README's forking flow ("Pick your sources") routes here.
- Auditing a candidate source someone has already named, when you want a structured viability check before committing to ingestion.

## When not to use

- The source is already known and the operator wants to ingest it. Run `ingesting-resources` directly.
- The question is "is X already in our corpus?" Run `matching-references`.
- The question is "which existing reference applies to this situation?" Run `answer-from-corpus`.

---

## Setup

### Inputs

The skill takes two flexible arguments.

**Topic or gap query.** Free-form ("project management for stakeholder engagement"; "rigorous group-decision-making research") or structured by axis + thin distillation ("decision-making axis, the conflict-resolution phase has no behavioural-science source"). The skill reads `{corpus-root}/reference-index.json` (file catalogue), `{corpus-root}/concept-index.json` (concept axis), and the relevant `{corpus-root}/distillations/{task}/task-index.json` to identify gaps and avoid recommending duplicates. The default `{corpus-root}` is `corpus.commons/demo/` in this repo.

**Licence filter mode** (default `cc-only`):

- `cc-only`: only candidates with explicit Creative Commons, public-domain, or permissive open-source licences. Highest signal-to-noise for forks targeting public distribution.
- `permissive`: adds clearly-published-for-public-consumption material (government works, institutional reports, open journals).
- `unfiltered`: no licence filter at search time. Operator handles licensing manually per candidate.

Recording the licence on every candidate is *not* optional: every triage entry carries the exact licence string regardless of filter mode.

### What counts as a "source"

A source is any **expository document with clear authorship, full text available, and a deterministic conversion path**. Books are the most common shape but not the only one. All of the following are candidates if they pass the viability checks below:

- **Books and book chapters**: textbooks, monographs, edited volumes
- **Methodology and research papers**: original journal articles, working papers, technical reports, systematic reviews
- **Standards and frameworks**: ISO/IEEE/NIST documents, regulatory frameworks, professional body standards
- **Institutional and policy documents**: government reports, central-bank research, IGO publications
- **Long-form essays and chapter-length pieces** with clear authorship and citation discipline
- **Lectures and structured talks with full transcripts**: TED, conference keynotes, lecture series. The *transcript* is the ingestable artefact; slide decks alone are not (see the OCW lesson below).
- **Documentaries and interview series with full transcripts**: same constraint: text, not video
- **Curated synthesis sites with stable expository pages**: Stanford Encyclopedia of Philosophy, Cochrane Reviews, systematic-review repositories, well-edited reference works

What does *not* count: blog posts (too thin to merit a deep ref), social-media threads, Q&A site answers, slide decks alone, video without transcripts, executive summaries that point at unavailable longer documents.

### Known-good repositories to bias toward

The skill's web search starts here before broader queries. Edit this list to bias toward your domain:

- **Open content & textbooks**: OpenStax, BCcampus Open Textbooks, LibreTexts, Saylor Academy, MIT OpenCourseWare (transcripts and full lecture notes only), Stanford Encyclopedia of Philosophy
- **Open primary research**: PLOS journals, eLife, BMJ Open, Nature Communications (CC BY portion), arXiv (per-paper licences), bioRxiv, SSRN (per-paper licences)
- **Institutional / policy**: OECD iLibrary, World Bank Open Knowledge Repository, IMF eLibrary, UN documents, Federal Reserve research papers, GAO and CBO reports
- **Standards bodies**: NIST publications, ISO public-domain summaries, IEEE open-access portion, professional body open standards
- **Public domain / classics**: Project Gutenberg, Internet Archive (per-item rights), HathiTrust public-domain works

**A note on slide-deck sources.** MIT OCW management courses, corporate "thought leadership" white papers, and conference talk notes are usually *teaching kits* (slides + readings + cases), not expository documents. Pass the *Self-contained* and *Expository prose* viability checks before recommending these. Hit rate is low; audit overhead is real.

---

## Procedure

### Step 1: Candidate generation

Run the topic/gap query against the known-good repositories above first, then broader web search if needed. Aim for 5-15 candidates before triage; the triage funnel will narrow this to the proceed bucket.

For each candidate, capture: title, author(s), publisher / platform, year, source URL, format (PDF / EPUB / HTML / markdown), apparent licence statement.

### Step 2: Pre-flight viability triage

For each candidate, run the five checks below *in order*. Stop at the first failing check; record the specific reason.

**1. Licence recorded.** Find an explicit licence statement on the source page or document. Capture the exact string with version and modifiers (e.g. "CC BY-NC-SA 4.0", not "Creative Commons"). If absent or unclear, do not skip: this is a flag, not a kill. Record `Licence: unverified` and continue to the next check; the candidate may surface as `sample first` after triage with `Scope: copyrighted` as the conservative default.

**2. Format → conversion path.** Confirm a deterministic conversion path exists per [`source-integrity.md`](../../../docs/architecture/source-integrity.md) ("Use deterministic converters, not the model"). PDF, EPUB, HTML, and pre-extracted markdown all pass: `markitdown` or `pymupdf4llm` will handle them. Fail conditions: behind-paywall (cannot retrieve), JavaScript-rendered-only (no static HTML), image-PDF without OCR layer, video/audio-only.

**3. Self-contained?** Is the *intellectual content* in this document, or is the document a syllabus / teaching kit / link compendium pointing to external readings? Read the table of contents and one section. If the section reads as commentary on or pointers to external works, the source is scaffolding, not substance: ingesting it produces a thin deep reference. *This is the OCW lesson: a course's lecture notes are usually slide decks pointing at copyrighted textbooks, not standalone treatises.*

**4. Expository prose vs slide deck?** Sample one substantive section (5-10 pages or 1500+ words). Decks (titles + bullets + diagrams, designed to be spoken to) fail. Hybrid handouts (some prose, some bullets) pass with a note. The test: would a competent reader unfamiliar with the source understand the substantive claim by reading this passage *alone*? If no, fail.

**5. Full source readable?** Page count and chunkability under the protocol's full-source rule. Massive multi-volume works (>500 pages) and works that depend on missing predecessor volumes flag as `sample first`. The 9-pass protocol does not silently truncate; the operator either ingests the whole source or labels coverage explicitly per `docs/architecture/source-integrity.md`.

### Step 3: Gap-fit scoring

For each surviving candidate (proceed or sample first), check fit against the existing corpus:

- Read `{corpus-root}/reference-index.json` (file catalogue) and the relevant per-task `{corpus-root}/distillations/{task}/task-index.json` for whichever axes the corpus configures. In the demo, that's [`corpus.commons/demo/reference-index.json`](../../../corpus.commons/demo/reference-index.json) plus the five per-axis task indexes under `corpus.commons/demo/distillations/`. The `.md` operator-inspection views remain alongside if a human-readable read is preferred.
- For each candidate: which task-axis distillations does the source plausibly fill? Where does it overlap with existing corpus, and is the overlap *complementary* (different angle on the same topic, keep) or *duplicative* (same angle, same depth, skip unless replacing)?
- Note the overlap explicitly in the triage entry.

### Step 4: Output the triage report

Write to an operator-chosen path (default `_planning/finding-resources-{date}.md` if the operator has not specified). Three sections—**proceed**, **sample first**, **skip**—each entry shaped as ingestion-ready input.

---

## Output schema

Every entry, regardless of bucket, carries:

```markdown
### {Author}, *{Title}* ({year})

**Source:** {full citation}
**Licence:** **{exact licence string}** | {url}
**Scope:** {open|open-nc|copyrighted|confidential|personal — see below}
**Format:** {pdf|epub|html|markdown}
**Conversion:** {markitdown|pymupdf4llm|other}
**Verdict:** {proceed|sample first|skip} — {one-line reason}
**Likely applicable axes:** [{decision-making, stakeholder-engagement, ...}]
**Corpus fit:** {complementary to {existing slug} on {angle} | duplicative of {existing slug} | gap-fill in {axis}/{phase}}
```

### Scope assignment

The skill suggests `Scope:` based on the licence:

| Licence | Suggested scope |
|---|---|
| CC0, public-domain, CC BY, CC BY-SA, MIT, Apache, BSD | `open` |
| CC BY-NC, CC BY-NC-SA, CC BY-NC-ND | `open-nc` |
| All-rights-reserved published material | `copyrighted` |
| Unverified / no licence statement | `copyrighted` (conservative default) |

The operator overrides at ingestion if the *use intent* differs from the licence-implied scope (e.g. a CC-BY paper used for a confidential client engagement, where the artefact's distribution scope should match the engagement, not the upstream licence). Scope governs distribution; licence governs attribution and derivative-rights. They ride together.

`confidential` and `personal` are not assignable from public discovery: those scopes are operator-tagged at ingestion when the source is org-internal or personal material.

---

## What this skill does NOT do

- **Ingest.** That's `ingesting-resources`. The triage report is its input.
- **Match against existing corpus for query-time retrieval.** That's `matching-references` (named lookup) or `answer-from-corpus` (situation routing).
- **Render redistribution judgements.** Per [`copyright.md`](../../../docs/architecture/copyright.md), the build is neutral infrastructure. The skill records licence and suggests scope; the operator decides what to ingest and where to ship it. The build's `max_scope` ceiling enforces distribution at profile time, not at discovery time.

---

## What this skill cannot reliably do

- **Authoritativeness judgement.** Cannot reliably tell a primary source from a secondary citation, a methodologically rigorous paper from a popularised summary, or a predatory journal from a reputable one. The operator owns this call.
- **Currency.** A 2015 paper since retracted or contradicted by replication failures will still surface. The skill does not check citation graphs.
- **Field-specific quality signals.** Applies a generic prior (peer-reviewed, institutional publisher, established repository); operators in specialised fields should override.
- **Deep-vetting for high-stakes additions.** For regulated domains or public-facing assistants, run high-stakes candidates through Claude Research or a domain expert before ingestion.
- **Originality vs synthesis.** Cannot tell whether a candidate is the original source of a framework or a summary of someone else's work. Flag in *Corpus fit* when it matters.

---

## Related skills

- `ingesting-resources`, runs the 9-pass protocol on a `proceed` entry from this skill's report.
- `matching-references`, checks the corpus for an existing source before adding a near-duplicate.
- `creating-distillations`, projects one existing reference onto one existing task axis (no new source needed).
- `creating-applications`, assembles a new application (build profile + distillation index + N orchestrated distillations) when adding a task axis.
- `creating-tasks`, scopes a new task axis with Jobs-to-be-Done discipline before assembly.
