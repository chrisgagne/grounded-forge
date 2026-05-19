---
name: answer-from-library
description: Source-grounded answer to a question via shape-aware retrieval: classifies the query as a named lookup, a diagnostic, or a synthesis, then runs the right protocol (direct route, task-index → distillations → deeps, or three-pass index/Chroma → lights → deeps). Stops on sub-claim coverage, not on counts.
argument-hint: "<question or topic>"
---

# Answer from library

Source-grounded answer protocol for any substantive question the library may cover. The *library* is the assembled body of references and distillations the skill is searching; the *matrix* is the architectural pattern (reference × task projection) that pre-shapes how the library is organised. Invoke this skill to *operationalise* the bundled CLAUDE.md's grounding directive: CLAUDE.md sets the principle (search before reasoning from priors; cite or admit guessing), this protocol runs it as executable steps: shape-classification, traceability, citation density, library breadth.

## Procedure

**Path convention.** Every path in this skill is written from the **source-repo perspective**: `corpus.commons/demo/{file}`. When `/answer-from-library` runs inside a **deployed application** (any subdir of `corpus.commons/demo/apps/`, e.g., `apps/decision/`, `apps/stakeholder/`, `apps/software-business/`), the `corpus.commons/demo/` prefix is stripped one-to-one: `corpus.commons/demo/reference-index.json` resolves as `./reference-index.json`, `corpus.commons/demo/distillations/{task}/task-index.json` as `./distillations/{task}/task-index.json`, `corpus.commons/demo/references/{slug}.md` as `./references/{slug}.md`, and so on. The rest of every path is unchanged. The deployed-app `CLAUDE.md` documents the bare-path layout from the app's own perspective; this skill's `corpus.commons/demo/` literals are the source-repo equivalents. Translate at read time; do not paginate or grep for files the literal path-string fails to find.

**`--corpus {slug}` flag.** When the operator passes `--corpus my-corpus` in the invocation (e.g., `/answer-from-library --corpus demo What is a definition of done?`), the skill targets `corpus.commons/{slug}/` or `corpus.local/{slug}/` instead of the default. Use the flag in two cases: (a) the source repo carries more than one commons or local corpus and the active one is ambiguous; (b) the operator wants to route a query against a specific named corpus regardless of CWD. Default resolution: if the CWD is inside a deployed app, use the bundled corpus (bare paths); if the CWD is inside the source repo and exactly one commons corpus exists, use it; if more than one corpus exists and no flag is passed, refuse with a one-line list of available corpora and ask. The trace footer names the corpus resolved-against: `corpus: demo` or `corpus: my-corpus`.

### Step 0: Classify the query shape

Before any reads, classify the question:

- **Named lookup.** The user names a specific framework, author, work, or concept ("walk me through the OpenStax Principles of Management chapter structure", "what does TC 25-20 say about the AAR cycle", "tell me about Dekker's Just Culture as treated in the corpus"). Signal: the answer reduces to *what does this one source say*. → **Protocol N.**
- **Diagnostic.** The user describes a situation that needs reference-mediated guidance ("how do I handle a stakeholder conflict", "I need to make a decision under uncertainty"). Signal: there's a task domain in play, and the corpus has distillations for it. → **Protocol D.**
- **Synthesis.** The user asks what the corpus says about a broad topic ("what is Agile", "what does the library say about employee motivation"). Signal: the answer benefits from breadth across multiple authors/traditions and the question is not a named lookup or in-task diagnostic. → **Protocol S.**

When ambiguous, default to the more expansive protocol (S over N, D over N). Never ask the user to disambiguate unless genuinely unclear.

### Step 0.5: Lens-applicability check

After classifying the query and before any reads, check whether a lens materially reweights what's salient for this query.

**Skip this step for Protocol N.** Named lookups answer *what does this one source say*; a lens would distort, not clarify.

**For Protocols D and S:**

1. **Read [`corpus.commons/demo/lens-index.json`](../../../corpus.commons/demo/lens-index.json) unconditionally.** The lens index is a small curated runtime artefact (one entry per lens under `lenses.{slug}`). Each entry carries `kind`, `spec_path`, `purpose`, `reach_for_when`, and a structured `salience` block (`notices_first`, `recedes`, `native_vocabulary` as a list of phrases) that primes the lens's vocabulary at a glance. Read it the way the task-axis indexes are read: as a map, not a search target. Always read it for Protocols D and S; do not short-circuit on a query that *seems* lens-neutral, because the detection in step 2 is what reads the entries against the query, and that detection needs the index loaded. The companion operator-inspection view at `corpus.commons/demo/lenses/LENS-INDEX.md` carries the same data in prose form; the JSON is the runtime source of truth.
2. **Detect the lens-shaped signal.** The deliverable is lens-shaped when it asks for role-specific guidance, a perspective-bound read, an artefact aimed at a named reader-type (CTO, PM, executive, builder), a query asking for a named living person's voice or for their published framings to be applied to the artefact (real-person lens), an AAR/retro write-up where reader-role is load-bearing, a coaching brief, or process/RACI documentation where role-and-circumstance is the unit of analysis. If the query is lens-neutral (a generic synthesis question with no reader-bound output), no lens applies and the rest of the protocol runs unmodified.
3. **Name the lens(es) the index surfaces** and confirm with the operator before proceeding when more than one lens could apply or when the choice changes the deliverable's shape materially. When exactly one lens fits unambiguously, name it in the trace and proceed without asking.
4. **For most lens-shaped queries, the index entry is sufficient**: the `salience` block carries enough of the lens's vocabulary (notices-first / recedes / native-vocabulary) to apply at retrieval time. **Read the full spec** at the path under `lenses.{slug}.spec_path` (e.g., `corpus.commons/demo/lenses/cto.md`) only when the query needs the lens's grounding contract, fire-list, or trust-breaking-failure-mode reasoning, i.e. when *why* this lens reads what it does is material, not just *what* it reads. Citation-grade synthesis, real-person voice fidelity, and high-stakes artefact shaping are the typical cases.
5. **At retrieval, prefer a pre-projected (source, task, lens) distillation when one exists.** If the distillation is lens-neutral in this build, apply the lens at query time via the index entry's `salience` block (and the full spec's *Salience and vocabulary* section if Step 4 says read the full spec): the retrieval-time fallback documented in [`projection-protocol.md`](../creating-distillations/projection-protocol.md) §Retrieval-time fallback.

Lens application shapes salience and voice; the matrix-axis reads (task index → distillations → deeps) run unchanged. The trace footer names the lens used (or "no lens" when the deliverable was lens-neutral).

**Step 0.5 runs *before* sub-claim decomposition.** The lens shapes what the sub-claims should be: a CTO-lens memo and a builder-lens runbook decompose the same source question into different sub-claim lists. Decompose after the lens is named, not before.

### Sub-claim decomposition (Protocols D and S)

For Protocols D and S, *before* reading reference files, decompose the question into the 3-10 sub-claims the answer will need to make. Write the sub-claim list out explicitly. Examples:

- "What is Agile?" → origin/motivation; key principles; methodology family; common failure modes; critique/limits; evolution post-Agile.
- "How do I handle a stakeholder conflict?" → identify positions vs interests; surface the conflict safely; structure the conversation; close to commitment.

The sub-claim list is the coverage map for retrieval. Stop reading when every sub-claim has at least one strong source AND the next read would only thicken existing coverage.

Skip decomposition for Protocol N: a named lookup has one sub-claim by construction.

### Protocol N: Named lookup

1. **Route directly.** Read the corpus catalogue at `corpus.commons/demo/reference-index.json`: top-level shape is `{schema_version, corpus, generated_from, refs}`; the per-entry catalogue lives under the `refs` field, keyed by 3-character slug-ID (e.g., `refs["00h"]`) with each entry carrying `{slug, author, year, title, primary_topic, concept_tags, lines_light, lines_deep, scope}`. To resolve a named source: scan `refs` entries for an author/title/concept_tags match, take the entry's `slug` field, then read `corpus.commons/demo/references/{slug}.md` and `{slug}-deep.md`. The ID is the join key for concept-index and task-index cross-references; the slug is the file-path key. For task-bound named references also read the relevant task-axis index at `corpus.commons/demo/distillations/{task}/task-index.json`.
2. **Read the light first.** `corpus.commons/demo/references/{slug}.md` for orientation.
3. **Read the deep.** `corpus.commons/demo/references/{slug}-deep.md` if the question needs citations or substantive treatment. For "what is X" questions and for full-coverage signals ("walk me through", "every section", "full map") read the deep regardless of regime. For "remind me of X" questions, the light alone may suffice. **Pick the regime** (Citation-grade / Depth-over-breadth / Orientation: table under Protocol S Pass 3) the same way Protocol S does; for a Named lookup with explicit "with citations" or scholarly context, or with a defensibility-critical / under-legal-review framing, fire Citation-grade and surface evidence-classification markers. **Long-deep pagination:** if `reference-index.json`'s `refs[id].lines_deep` for the slug exceeds ~400, apply the EOF-successive-reads pattern under Pass 1's cap-aware surfaces and label each read in the trace.
4. **Read the distillation** if the question is task-bound: `corpus.commons/demo/distillations/{task}/{slug}-{task}.md`.
5. **Stop.** No triage, no breadth sweep.

### Protocol D: Diagnostic

1. **Decompose the question** into 3-6 sub-claims (see above).
2. **Read the task-axis index** at `corpus.commons/demo/distillations/{task}/task-index.json`. The JSON partitions the task into named phases or situations (each a `section`) and lists which references apply to each (`rows` as `[need, slug-id, when]` triples). Resolve each slug-ID via `corpus.commons/demo/references/slug-table.json` (top-level shape `{schema_version, corpus, generated, next_id, slugs}`; the `id → slug` mapping lives under `slugs.{id}`) or via `reference-index.json["refs"][id].slug`; either gets you the file-path key for `references/{slug}.md`, `{slug}-deep.md`, and `distillations/{task}/{slug}-{task}.md`. **Note: the larger task-axis indexes exceed the Read tool's 25k cap**: see Pass 1's cap-aware surfaces and the EOF-successive-reads pattern; for Protocol D prefer the python3 query against `sections[].rows` since you know the phase from step 3.

Unlike Protocol S Pass 1, Protocol D does not require the corpus-level indexes (`reference-index.json`, `concept-index.json`) by default: the task-axis index plus the slug-table resolve the candidate sources. Read the corpus-level indexes only if the task-axis index doesn't surface a match or the question crosses the task axis.
3. **Identify the relevant phase or situation** for the question.
4. **Lean-mode check (when `--lean` is passed).** If the index surfaces ≤ 2 sources for the identified situation, skip Step 5 (distillations read) and proceed directly to Step 7 (deep refs against the named sources). The index has already done the routing the distillations would do; on canonical material with good filename hygiene, reading the distillations is content-routing overhead. The default (without `--lean`) is to read the distillations regardless. The flag is the operator's opt-in to the cost-collapse hypothesis: that the curated index is sufficient to route directly to deep refs when it points at one or two sources for a situation. Hypothesis under test: collapsing this step on canonical material brings D's tokens within ~1.5× of Method C without rubric-quality loss; on non-canonical material the distillations layer is doing real work and lean-mode should hurt. Run the eval suite to test.
5. **Read every distillation the index surfaces** for that phase/situation (typically 2-5 in this corpus). Distillations at `corpus.commons/demo/distillations/{task}/{slug}-{task}.md` are pre-projected for exactly this shape; trust the projection.
6. **Tag each distillation against the sub-claim list.** Stop when every sub-claim has at least one strong source AND the next distillation would only restate.
7. **Read the deep ref** for any author whose argument is doing real work in the answer: `corpus.commons/demo/references/{slug}-deep.md`. The threshold is "would I cite this author?": yes → read the deep. **Pick the regime** (Citation-grade / Depth-over-breadth / Orientation: table under Protocol S Pass 3) and apply its Pass-3 behaviour; for diagnostic queries the Depth-over-breadth regime is the default, and the distillation-carries-projected-citations calibration applies. The Citation-grade regime fires under D step 7 when the query carries defensibility-critical signals (legal review, audit context, "with citations", manager-pushback): when it fires, apply the Pass-3 read-scope rule under Protocol S Pass 3 (full deep vs targeted re-validation per defensibility unit). **Long-deep pagination:** if `reference-index.json`'s `refs[id].lines_deep` for the slug exceeds ~400, apply the EOF-successive-reads pattern under Pass 1's cap-aware surfaces and label each read in the trace.

### Protocol S: Synthesis

Three explicit passes:

**Pass 1: Routing.** Decompose the question into 5-10 sub-claims. Then route:

- **Precondition gate: read three corpus-level JSON indexes plus the task-axis index(es) for the domain(s) in play.**

  Corpus-level (always loaded):
  - `corpus.commons/demo/references/slug-table.json`: slug ↔ ID mapping; load once per session. The `id → slug` map lives under the top-level `slugs` key (full shape: `{schema_version, corpus, generated, next_id, slugs}`).
  - `corpus.commons/demo/reference-index.json`: file catalogue (one entry per reference: author, year, title, primary_topic, concept_tags, scope, line counts). The catalogue's per-ID entries live under the top-level `refs` key (full shape: `{schema_version, corpus, generated_from, refs}`); query as `ri["refs"][id]`.
  - `corpus.commons/demo/concept-index.json`: concept axis with aliases and per-source pointers (entries under top-level `concepts`). Schema: every source entry carries `{id}` and most carry `{context}`; the `{section, md_line}` pair is **best-effort**, present when the build's mechanical match resolved (~57% of source mentions on the demo corpus, ~65% of concepts have at least one pointer), absent when it didn't. When the pointer is absent, fall through to `grep -n` against the deep ref to find the passage.

  Task-axis (load when the question fits a domain):
  - `corpus.commons/demo/distillations/{task}/task-index.json`: situation router. For grounded-forge's shipped axes (`decision-making`, `stakeholder-engagement`, `software-business`), read the index for each domain that applies; for synthesis questions that span both decision-making and stakeholder-engagement, read both.

  **Cap-aware surfaces.** Several runtime artefacts in the demo corpus either exceed or sit close to the Read tool's 25k single-call cap; each has a specific access pattern:

  - **`concept-index.json` (~22k tokens)**: query a specific concept with `python3 -c "import json; ci = json.load(open('corpus.commons/demo/concept-index.json')); c = ci.get('concepts', ci); print(json.dumps(c.get('{slug}'), indent=2))"`. Concept slugs are kebab-case canonical names (e.g., `after-action-review`, `just-culture`, `dual-process-theory`). **Aliases live inside the canonical entry's `aliases` array, not as top-level keys**: to resolve an alias (e.g., `aar` → `after-action-review`), reverse-lookup with `python3 -c "import json; ci = json.load(open('corpus.commons/demo/concept-index.json'))['concepts']; alias = 'aar'; print(next((k for k, v in ci.items() if alias in v.get('aliases', [])), None))"` then probe the canonical key. Try both singular and plural forms; aliases are typically stored singular. Bash querying preserves the index's structure cheaper than paginating and is the right move for any concept-anchored query. Read the whole file only when you need to *browse* the concept axis (rare).
  - **Task-axis indexes (`distillations/{task}/task-index.json`)**: token sizes are corpus-dependent and grow as distillations are added. On the current demo corpus `decision-making` and `stakeholder-engagement` both exceed the 25k cap; `software-business` is smaller but check before reading. Check size with `wc -c` against the cap, then either paginate (`offset=0, limit=400`; then `offset=400` to EOF: see EOF rule below) or query directly with `python3` against `sections[].rows` when you know the phase. For Protocol D specifically prefer the python3 query route, since you usually know the phase from Step 3.
  - **`lens-index.json`**: small on the current demo corpus (~3k tokens, one Read call). Cap-awareness named here for forward-compatibility: if a future corpus pushes it over, query with `python3 -c "..."` against `lenses.{slug}` the same way `concept-index.json` is queried.
  - **OpenStax deep refs ≥700 lines**: nine of the 25 demo deep refs (e.g., `openstax-organizational-behavior-deep.md` at 745 lines, `openstax-principles-management-deep.md` at 1,024 lines) exceed the cap. When Pass 3 requires the whole deep, take **successive 400-line reads until EOF**. The exact line count is in `reference-index.json`'s `refs[id].lines_deep` field; consult it before reading to know how many passes are needed. Label every read in the trace. The Source Integrity rule is firm: full coverage or labelled partial; never silent truncation.

  **EOF-successive-reads pattern (apply whenever a runtime artefact exceeds the cap):**

  ```
  Read(file, offset=0,   limit=400)
  Read(file, offset=400, limit=400)
  Read(file, offset=800, limit=400)
  ... continue until a Read returns fewer lines than `limit` (that's the EOF signal).
  ```

  The three example offsets (0, 400, 800) are a worked example for a ~1024-line file, **not a template**: a 1,500-line file needs four reads, a 600-line file needs two. Always stop on the "fewer than `limit` lines returned" signal, not on the example offsets. Read truncates silently at EOF (returns the lines available, not an error). For a future corpus where any index or deep ref exceeds the cap, the same pattern applies.

- **Query Chroma via `matching-references`** as an expansion pass, *after* the index reads, when (a) the index entries left one or more sub-claims uncovered, (b) the query uses terminology the curator may not have anticipated, or (c) you suspect a semantic neighbour the curator's literal-keyword cues won't surface. Use `n_results: 50`. Returns metadata (filenames + similarity scores), not document bodies. Pass 2's light-read triage filters Chroma candidates the same way it filters index-surfaced ones.

- **Grep `corpus.commons/demo/references/*.md`** when Chroma is unavailable and index reading hasn't surfaced coverage for a sub-claim.

Result: a candidate set of slug-IDs (author + title resolved from `reference-index.json`; concept-axis sources from `concept-index.json`; task-bound rows from `task-index.json`). No file reads beyond the indexes in this pass.

**Pass 2: Triage on lights.** Read the light refs for every candidate above the relevance floor, with diversity-aware deduplication (don't read three OpenStax books on related topics if one carries the load; spread across distinct authors and traditions). For each light read, tag which sub-claim(s) it addresses.

Stopping rule is *triangulation*, not just coverage. Continue until every sub-claim has at least two sources you'd cite, AND you've identified at least one place where authors converge and one place where they disagree or emphasise differently. For grounded-forge's small corpus this typically means reading 5-10 of the 14 lights for a broad query; 3-5 for a narrow one.

**Pass 3: Citation density on deeps.** Pass 3 fires by default for every regime except Orientation. Deeps add specific named statistics, exact quotes, and modal observations that lights summarise away.

Pick the regime by deliverable signal:

| Regime | Triggering signals | Pass 3 behaviour |
|---|---|---|
| **Citation-grade** | Regulated/scholarly/audit/disputed context; explicit "with citations"; defensibility-critical (legal review, manager pushback); user has named an author and expects rigour | **Mandatory + broad.** Every cited author. Surface evidence-classification markers (`[V]` `[AP]` `[AR]` `[AE]` `[BT]`) and page references. |
| **Depth-over-breadth** | Operator-bound action ("what should I do"); mechanism question ("how does X work"); disagreement adjudication; thesis-bearing prose under any length; anti-pattern detection | **Mandatory + narrow.** 2-4 load-bearing deeps read thoroughly; skip deeps for authors whose role is brief mention. |
| **Orientation** | Library-survey question ("what's in the corpus on X"); definition or one-liner; time-critical (live session); non-expert audience. Full structural enumeration of a single named source ("walk me through every section of book X") *also* fires here, but read the deep regardless of the optional-Pass-3 default, because the user has signalled they want enumeration, not a survey | **Optional by default, mandatory when the user signals enumeration.** Defer with explicit reasoning in the trace footer when deferring; fire when the user names full coverage. |

**Default to Depth-over-breadth when in doubt.** Synthesis questions, thesis-bearing prose under any length, and operator-bound action all fall here, and Pass 3 fires.

**Pass 3 read scope under Citation-grade.** *Full deep* when the defensibility unit is the integrated argument across multiple sections (the author's chain of reasoning, the structure of a chapter's case). *Targeted re-validation* (grep returning the passage plus ~5 lines before and after as context) when the defensibility unit is a specific named passage with a clear in-source location (a verbatim quote, a single-row stat, a named-and-attributed mechanic). In both cases the trace footer names the read scope per author: `openstax-OB (full, 0-745)`, `liberating-structures (partial, grep on "buy-in" / "central tendency", ±5 lines context)`. The Source Integrity rule still applies: full coverage or labelled partial, never silent truncation. When deciding, ask: is what I'm citing *this exact sentence*, or *this author's argument*? The first authorises targeted; the second requires full.

**`--no-deep` flag.** When the operator passes `--no-deep` in the invocation (e.g., `/answer-from-library --no-deep Write a 500-word essay on X`), Pass 3 is deferred regardless of regime. The trace footer annotates the operator's choice (`[no-deep]` when the flag was passed, `Pass 3 deferred (reason)` when Orientation regime is selected).

For each author selected, read their deep at `corpus.commons/demo/references/{slug}-deep.md`. Edge cases:

- **Deep doesn't exist.** Some sources are light-only. Either go to the source material itself or honestly say "no deep available, light-only treatment."
- **Distillation already does Pass 3's job** (Protocol D context). For diagnostic queries where Pass G has produced a strong distillation with projected citations in-band, the distillation *is* the projected deep. Reading the deep on top is often redundant: common enough on the current demo corpus that deferring Pass 3 here is the *normal* path for Protocol D, not the exception.

  **Calibration: where the verbatim markers came from is load-bearing.** When Pass 3 is deferred, the `[V]` / `[AP]` / `[AR]` / `[AE]` / `[BT]` markers in the answer come from *distillation prose*, not from re-validated deep-ref passages. That's correct for how-to / artefact-shaped deliverables where the projection is the unit of value. It's wrong for the Citation-grade regime (regulated / scholarly / audit / disputed context, explicit "with citations", defensibility-critical) where the verbatim claim itself is what's being defended: in that regime, fire Pass 3 against the deep even when the distillation looks sufficient, and surface the deep-ref line range alongside the marker. The trace footer should name the choice: *Pass 3 deferred (distillation carries projected citations)* vs *Pass 3 fired (verbatim markers re-validated against deep)*.

### Image-axis discovery (when `--with-images` is passed)

Fires after Pass 3 in Protocols D and S, and after the deep read (step 3) in Protocol N. The image axis is the corpus's classified-image library: `corpus.commons/demo/sources/converted/IMAGE-INDEX.yaml` (one entry per kept image, with `file`, `source_ref`, `description`, `style`, `tags`, optional `suggested_use`). It is not loaded into a runtime JSON index; access is grep-by-source_ref.

**Procedure:**

1. **Build the set of cited slugs.** For Protocol N, one slug (the named source). For Protocol D, the slugs of each distillation read in step 5 and each deep read in step 7. For Protocol S, the slugs of each deep read in Pass 3.
2. **Grep the YAML by source_ref for each slug.** The IMAGE-INDEX entry shape places `source_ref` one or two lines after `- file:`; `grep -B 2 -A 6 "source_ref: {slug}$"` returns the file path plus the surrounding description/page/tags/style fields per match. The `$` anchor avoids substring matches (e.g., `10xorg` shouldn't match `10xorg-export`). Use the source-repo path `corpus.commons/demo/sources/converted/IMAGE-INDEX.yaml`; when running in a deployed app, the bare-path equivalent is `sources/converted/IMAGE-INDEX.yaml`.
3. **Aggregate candidates per slug.** Build a list: per cited source, `(file_path, style, description, suggested_use)`. Drop entries whose `style` is incompatible with the deliverable (e.g., photographs for a hand-drawn carousel; long-form chart series for a single-slide use).
4. **Surface in the trace footer, not in the deliverable body.** Image candidates ride the trace, not the prose. The operator opens the candidate files manually and decides whether to use them; this skill discovers and lists, it does not decide. See the trace-footer extension below.

**No-coverage is honest.** If `IMAGE-INDEX.yaml` does not exist for this corpus or has no entries for any cited slug, name that in the trace footer (`image-axis: no entries for cited slugs`). Do not fabricate candidates.

**Cap-awareness.** `IMAGE-INDEX.yaml` files can be large (the aarbuddy library is 2 MB; the demo library is comparable). The grep-by-source_ref pattern keeps the surfaced context small. Do not full-read the YAML.

### Token budget posture

Stay inside the context window with comfortable headroom for the answer-writing step (~200k tokens reserved). Beyond that, breadth is the goal: a 100k-token Pass 2 on a synthesis query that produces a deeply-evidenced answer is well-spent.

### Write the answer

Write in the form the user asked for (essay, list, table, etc.). **Match the citation style to the form.**

- **Prose deliverables** (essay, memo, briefing, one-pager): cite by author and work in the prose itself (e.g., "Larman argues…", "the OpenStax OB chapter on conflict frames it as…"). Do not put relative file paths inline; they break essay flow and signal "abandoned essay form" to readers. If the user asks for traceability or a source list, append it once at the end, not throughout.
- **Technical or operator-facing deliverables** (code, config, runbook, internal note where the operator wants to inspect the trace): cite by relative file path inline.
- When in doubt, default to the prose-cite style for anything written in sentences and paragraphs.

Surface evidence-classification markers (`[V]` verbatim, `[AP]` author paraphrase, `[AR]` author argument, `[AE]` author example, `[BT]` borrowed-through) where they bear on the conclusion, but only when they sharpen a claim, not as decoration on every sentence.

### No-coverage and partial coverage

**Full no-coverage.** If the library does not cover the question (the index has no relevant entries, the candidate distillations don't apply, the deep references don't carry the load) say so plainly. Do not fall back to training to fabricate a confident answer. *"The library does not cover this; here's why, and here's what's adjacent that might help"* is a valid response. *Adjacent* covers two distinct moves: (a) **adjacent corpus material**: sources already in the corpus that touch the topic obliquely, with the obliqueness named; (b) **external-ingestion candidates**: named authors or works the operator could ingest to extend the corpus. The second is licensed when the corpus is clearly thin on a topic the operator has named, but it must be framed as *ingestion candidates, not citable claims*. Phrase as *"Beck's Extreme Programming Explained would be a candidate ingestion if the operator wants this topic covered grounded"*, not as *"Beck argues that..."*. The discipline: training-derived knowledge of an author may name them as an ingestion target, but must not be used to ground a substantive claim.

**Partial coverage** is the more common case. Where the acknowledgement lands depends on deliverable shape:

- **Artefact-shaped deliverables** (process documents, RACI matrices, templates, runbooks, AAR/retro write-ups, briefs, memos written *as the thing itself*): the corpus-gap note goes in the trace footer, not the deliverable. Keep the prose clean; let the trace carry the gap.

- **Thesis-bearing prose with stated rigour** (essay with citations, briefing where defensibility is load-bearing, scholarly or audit context): surface the boundary in the prose itself, one sentence, in the lede or a closing turn. Examples:

  - *"The library does not contain a primary reference for the 2001 Manifesto; this essay characterises Agile through the authors who critique, evolve, and reframe it."*
  - *"Beck's *Extreme Programming Explained* is not in the corpus; XP claims here are made via secondary treatment, not Beck directly."*

- **Default when in doubt:** trace footer only. Surface in prose only when the deliverable explicitly invites a methodological note.

**Lens-as-sole-grounded-source pattern.** Real-person and role-bound lens specs sometimes cite primary sources (Heifetz, Weinberg, Block, Scott, etc.) that are not in `references/`. When the matrix axes carry no relevant material for the query *but* the lens spec carries the framings the query asks for, the lens spec serves as the citable reference for this run. Pass 2 and Pass 3 against the matrix axes are correctly deferred (no relevant material to read). Trace footer shape: `*Trace [Synthesis, lens: chris-gagne-consultant-coach, no-deep, partial-matrix-coverage]: lens-index → spec read in full via spec_path; matrix axes carry no relevant material for the named framings → answer grounded in lens spec citations of [authors not in references/]*`. If the deliverable is thesis-bearing prose with stated rigour, also surface the boundary in the lede: *"The framings in this read are drawn from the chris-gagne lens spec, which cites Heifetz, Weinberg, and Larman; those primary sources are not in the corpus and the claims here are made via the lens's secondary treatment, not the authors directly."* The partial-coverage marker in the bracket-tag is mandatory.

**No-coverage and partial-coverage guidance applies cross-protocol**, to Protocol N (named source missing or thinly covered), Protocol D (task-index doesn't surface candidates for the situation), and Protocol S (sub-claims uncovered after Pass 1-2-3). The structural placement of this section is incidental; the rules govern any protocol's output when the corpus runs thin on what the query needs.

### Append a trace footer

After the answer, append a one-line footer naming the protocol used and (for Protocols D and S) the sub-claim → source mapping.

**Bracket-tag schema.** The leading bracket carries (in order): protocol tag (Named / Diagnostic / Synthesis), regime tag if a non-default regime fired (Citation-grade / Depth-over-breadth / Orientation), lens tag (`lens: <slug>` or `lens: none`), `corpus: <slug>` (which corpus was resolved-against; `corpus: demo` by default, the `--corpus` flag's value otherwise), the deep-flag (`deep` / `no-deep` / `partial`), the image-flag (`with-images` when `--with-images` was passed; omit otherwise), and any architectural-coverage qualifier (`partial-matrix-coverage` when the matrix axes carry no relevant material). Examples in increasing complexity:

```
---
*Trace [Named, lens: none, corpus: demo, deep]: reference-index → openstax-organizational-behavior (light + deep)*
```

```
---
*Trace [Named, Citation-grade, lens: none, corpus: demo, deep]: reference-index → nhs-just-culture-guide (light + deep, full 184 lines) + lfuo-learning-review-guide-2024 (deep, full 323 lines); evidence markers [V] [AR] [BT] surfaced; partial-coverage boundary surfaced in lede (no Dekker primary in corpus)*
```

```
---
*Trace [Diagnostic, lens: cto, corpus: demo, no-deep]: stakeholder-engagement/task-index → sub-claims: identify positions/interests (openstax-OB-stakeholder-engagement), surface conflict safely (openstax-OB-stakeholder-engagement), structure conversation (liberating-structures-stakeholder-engagement), close to commitment (lfuo-stakeholder-engagement) → Pass 3 deferred (distillation carries projected citations; deliverable is artefact-shaped) | lens applied retrieval-time via cto.md salience-and-vocabulary*
```

```
---
*Trace [Diagnostic, Citation-grade, lens: none, corpus: demo, deep]: decision-making/task-index → Phases 3+4 → sub-claims: groupthink diagnosis (openstax-OB), pre-commitment moves (open-practice-library, liberating-structures), session mechanics (open-practice-library, letaw fist-of-five), defensibility (openstax-OB Ch 6.4 + 6.6) → Pass 3 fired per author: openstax-OB (full, 0-745), liberating-structures (partial, grep on "buy-in" / "central tendency", ±5 lines context), open-practice-library (partial, grep on "Disagree-and-Commit" / "HiPPO", ±5 lines context)*
```

```
---
*Trace [Synthesis, lens: none, corpus: demo, deep]: Pass 1 (decision-making/task-index + stakeholder-engagement/task-index + concept-index, Chroma N/A) → sub-claims: framing (openstax-OB), method choice (barbrook-johnson), facilitation (liberating-structures), post-event (tc-25-20, lfuo) → Pass 3 (3 deeps: openstax-OB, barbrook-johnson, lfuo)*
```

```
---
*Trace [Synthesis, lens: chris-gagne-consultant-coach, corpus: demo, no-deep, partial-matrix-coverage]: Step 0.5 lens-index → chris-gagne-consultant-coach (real-person, spec read in full via spec_path); matrix axes carry no relevant material for Heifetz / Weinberg / Larman framings → answer grounded in lens spec citations*
```

When `--with-images` was passed, append an image-axis line per cited slug, listing candidate file paths with style + suggested_use:

```
---
*Trace [Synthesis, Depth-over-breadth, lens: none, corpus: aarbuddy, deep, with-images]: Pass 1 (concept-index → reinertsen + goldratt + dekker) → Pass 2 (5 lights) → Pass 3 (3 deeps: donald-g-reinertsen-..., goldratt-the-choice, drift-into-failure-...) → image-axis (--with-images): donald-g-reinertsen-...-images/p0142-1.jpeg [diagram, "cost-of-delay curves for product development"] + donald-g-reinertsen-...-images/p0167-2.jpeg [chart, "queue size vs cycle time"] | goldratt-the-choice-images/p0089-1.png [diagram, "five focusing steps"] | drift-into-failure-...-images/p0211-1.jpeg [diagram, "Dekker's drift trajectory"]*
```

The trace is mandatory unless the user explicitly requests "no trace" or "essay only".

**Non-prose deliverable shapes** (a list of N pull-quotes, a thread, a single-line position, *"give me the line and the path"*, *"three sentences each, no synthesis"*) treat the form-match rule as load-bearing on placement: compress the trace to a one-line bracket-tag annotation in the chat scaffolding *above* the deliverable, not below it; the deliverable itself stays clean of scaffolding. The trace is still mandatory, just relocated. Append the full sub-claim → source mapping as a follow-up message only if the operator asks for it. The Source Integrity discipline holds in either placement.

**Deep-flag semantics:**
- `deep`: Pass 3 fired and the deep was read (full or with documented partial per author).
- `no-deep`: Pass 3 deferred. Name the reason in the trace body (e.g., `Pass 3 deferred (Orientation regime, library-survey question)` or `Pass 3 deferred (distillation carries projected citations)` for Protocol D's distillation-as-projected-deep case).
- `partial`: Pass 3 fired but coverage is bounded by source-availability (e.g., no Dekker primary in corpus for a Dekker-named query; lens-as-sole-source). Combine with `partial-matrix-coverage` when the matrix axes carry no relevant material.

**Image-flag semantics:**
- `with-images`: `--with-images` was passed; image-axis discovery fired against `sources/converted/IMAGE-INDEX.yaml` for every cited slug. The trace body lists candidates per slug as `{slug}-images/{file} [style, suggested_use]`.
- Omit the flag (no `with-images` in the bracket-tag) when image discovery did not run. This is the default; do not insert a `no-images` placeholder.

When `--no-deep` was passed, the bracket-tag uses `no-deep` and the trace body names the flag as the cause (e.g., `Pass 3 deferred (--no-deep flag passed)`). When Pass 3 fires by default, list the deeps read with their per-author read scope (full vs partial-grep, with line ranges) under the Citation-grade rule.

## Discipline

- **Refuse to include any non-trivial claim** that does not trace to a file you read. Author and work in prose is enough for the reader; the file path lives in your working memory and your willingness to defend the claim if challenged. If you find yourself reaching for a confident assertion you can't trace, either find the file that supports it or remove the assertion.
- **Honour the form the user asked for.** When the user names a length or form ("500-word essay", "one-pager", "brief", "memo"), treat it as a hard constraint. Do not append a "Sources" section, "For further reading", meta-commentary about the matrix, or scaffolding sections (Executive Summary, Key Takeaways, etc.) unless the user asked for them.
- **Length-target tolerance: ±30%.** When the user names a word count or implies one ("500 words", "around 1500 words", "~3500 words"), treat the band as N × 0.7 to N × 1.3. Inside the band: ship. Outside on the high side: cut, even if it means a tighter argument. Outside on the low side: deepen with the next-most-relevant source or honestly cap the response. Rule of thumb: a well-cited 500-word essay runs ~7-8 paragraphs of moderate density. The trace footer can be excluded from the word count.
- **Sub-claim coverage, not file count.** Stop when every sub-claim has at least one strong source AND additional reads would thicken rather than extend coverage.
- **Subagent dispatch is off by default; opt in with `--dispatch`.** In an interactive Claude Code session against a single corpus, parallel subagents add round-trips without buying breadth the main thread couldn't get from the same indexes. Subagents also write tokens that don't show up in the user's `/context` view, so an interactive operator watching their budget underestimates session cost. Default behaviour is to run every read in-session. Opt in with `--dispatch` when the skill is composed inside a larger agent flow (a parent orchestrator owns cost-tracking) or when the operator deliberately wants fan-out across sub-claims and accepts the `/context` blind-spot.

## Inputs

- A question or topic in plain language. The skill detects shape and task domain from content.
- Optional flag: `--no-deep`. When present, Pass 3 is deferred regardless of regime.
- Optional flag: `--dispatch`. When present, parallel sub-claim retrieval (Pass 2's light reads, Pass 3's deep reads) is dispatched to subagents. Default off: every read runs in the user's session so `/context` visibility and wall-clock latency stay predictable. Use `--dispatch` when composing inside a larger agent flow or when the operator accepts the `/context` blind-spot in exchange for fan-out.
- Optional flag: `--lean`. Protocol-D-only. When present, skip the distillations read (Step 5) when the index surfaces ≤ 2 sources for the situation; route the curated index directly to the deep refs. Tests the cost-collapse hypothesis: on canonical material the distillations layer is content-routing overhead Claude's training prior would have done from filenames alone. Default off pending eval (re-run the eval suite with the flag and report).
- Optional flag: `--with-images`. Triggers image-axis discovery after Pass 3 (or after the deep read in Protocol N): for each source whose deep was read, grep `IMAGE-INDEX.yaml` for entries matching that source's slug and surface candidate diagrams, charts, and illustrations in the trace footer. Default off; image discovery is a non-trivial token cost (per-source grep + candidate listing) and most prose deliverables don't need it. Pass when the deliverable is visual: carousel, deck, slides, blog with images, illustrated essay.

## Outputs

- An answer in the form the user asked for, with prose citations (or file-path citations if technical/operator-facing).
- A mandatory trace footer naming the protocol and sub-claim → source mapping.

## When to use

- Any substantive question the corpus might address.
- The default path for source-grounded answers from the library.

## When not to use

- The user has already named a specific reference and just wants a quote. Read the reference directly.
- The corpus does not cover the topic. Use `matching-references` first to check if you're not sure.

## Related skills

- `matching-references`: topic-to-resource search across the corpus catalogue. Use it first if you're unsure whether the corpus covers the topic, or as Pass 1 of Protocol S when Chroma is configured.
