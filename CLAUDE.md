# grounded-forge, system instructions

You are working *on* the grounded-forge repo. The distributions this repo compiles ship their own CLAUDE.md, sourced from per-corpus build profiles under `corpus.commons/{corpus}/build-profiles/` or `corpus.local/{corpus}/build-profiles/`.

## What this repo is

A working example of the reference × task matrix architecture: a retrieval pattern that pre-projects sources to task domains at ingestion time so runtime is lookup, not reshape. Task-axis projection moves from generation time to ingestion time, produced by an LLM operating under a structured protocol that enforces source-only citation discipline.

Lenses are per-distillation modifiers applied where they materially reweight what's salient, not a third axis. Specs live at `corpus.commons/{corpus}/lenses/` and are designed via the `creating-lenses` skill at [`.claude/skills/creating-lenses/SKILL.md`](.claude/skills/creating-lenses/SKILL.md); per-distillation applicability is decided at Pass G of `creating-distillations`. Each lens carries a `visibility:` frontmatter field (`open`, `open-nc`, `copyrighted`, `confidential`, or `personal`) parallel to references' `Scope:`; the build's `max_visibility:` ceiling per profile filters which lenses ship.

For the architectural argument, read in this order:

1. [`docs/reference/vocabulary.md`](docs/reference/vocabulary.md): the noun/verb grammar. Read first; the rest assumes it.
2. [`docs/architecture/overview.md`](docs/architecture/overview.md)
3. [`docs/architecture/llm-epistemology.md`](docs/architecture/llm-epistemology.md): *why* the matrix exists. The Larman's-Law-4 / LLM-epistemology problem the architecture is solving against.
4. [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md)
5. [`docs/architecture/two-layer-indexes.md`](docs/architecture/two-layer-indexes.md)
6. [`docs/architecture/matrix-pattern.md`](docs/architecture/matrix-pattern.md)
7. [`docs/architecture/source-integrity.md`](docs/architecture/source-integrity.md)
8. [`docs/architecture/known-architectural-limits.md`](docs/architecture/known-architectural-limits.md): three limits intrinsic to the design.
9. [`docs/architecture/capability-binding.md`](docs/architecture/capability-binding.md)

Further reading: [`docs/architecture/gridmaker.md`](docs/architecture/gridmaker.md) is an aside on the older vocabulary the architecture's lens-design discipline draws on (Bruteau's *psychic grid*) and the rule that follows from it (*lenses are windows, not selves*) — the rule shapes how lens specs are authored in [`.claude/skills/creating-lenses/SKILL.md`](.claude/skills/creating-lenses/SKILL.md) and [`.claude/skills/gridmaker-interview/SKILL.md`](.claude/skills/gridmaker-interview/SKILL.md).

## Build system

Each build profile is an application: a distributable bundle composed of references and the per-task distillations the application needs. Profiles are listed in [`builds.yaml`](builds.yaml).

Profiles ship distinct content: distinct distillation directory (which carries its own distillation index), distinct CLAUDE.md template. Same references across profiles.

```bash
npm install
npm run build              # all profiles
npm run build:{profile}    # one profile
npm run clean              # remove apps/
npm run list               # list profiles
```

The build is in [`build.js`](build.js); profiles configured in [`builds.yaml`](builds.yaml); profile CLAUDE.md templates live at `{source_dir}/build-profiles/{profile}.md` (corpus-bound).

v0.2.1 ships five public profiles (open-nc ceiling) under `corpus.commons/demo/`:

- `decision`, `stakeholder`, `software-business`: three task-axis projections of the same reference corpus.
- `aar-mode`: open-corpus After-Action Review assistant.
- `retro-mode`: open-corpus retrospective-facilitation assistant.

Private profiles, if any, live in per-corpus `builds.yaml` files under `corpus.local/{corpus}/` and are auto-discovered by `build.js` when present. The two corpus.commons ceremony profiles share the reference axis with the corpus.commons decision-making and stakeholder-engagement axes; together they make the matrix architecture operationally visible: one corpus, multiple task projections.

Validation runs referential integrity (path references in shipped files resolve) and structure (required files and directories present). Two parallel filters: a *distribution scope* filter excludes references whose `**Scope:**` exceeds the profile's `max_scope:` ceiling; a *lens visibility* filter excludes lenses whose `visibility:` exceeds the profile's `max_visibility:` ceiling. Both ceilings live in [`builds.yaml`](builds.yaml). `personal` ships in no profile under either taxonomy. Scope is the mechanical complement to [`docs/architecture/copyright.md`](docs/architecture/copyright.md); the taxonomy is in [`README.md`](README.md#distribution-scope).

## Corpus layout

Substrate (build system, docs, profile templates, and *substrate* skills) is separate from data (corpora + outputs + *corpus-bound* skills). Corpora live under two tiers:

```
corpus.commons/                                 # tracked — open or open-nc; ships
  demo/                                         # the seed corpus
    sources/
      ingest/                                   # staging; operator drops material here
      original/{slug}.source.md                 # required — frontmatter sidecar
      original/{slug}.{pdf,epub,...}            # optional — present only when redistributed
      converted/{slug}.md                       # required — what Pass C reads
    references/                                 # Light + deep references
      slug-table.json                           # slug ↔ short-ID (Phase 2)
    reference-index.json                        # file catalogue (runtime)
    concept-index.json                          # concept axis with section pointers (runtime)
    distillations/{task}/                       # Task projections, the task axis
      task-index.json                           # situation router (runtime)
      DECISION-MAKING-DISTILLATION-INDEX.md     # operator-inspection view
      {source-slug}-{task}.md                   # One projection per source per task
    lenses/                                     # Lens specs + LENS-INDEX.md
    .claude/skills/                             # Corpus-bound skills (see below)
    apps/{profile}/                             # Compiled outputs (tracked)
    distros/                                    # Packaged release artefacts
corpus.local/                                   # gitignored — operator's private corpora
projects.local/                                 # gitignored — operator's outputs
```

A corpus is self-contained: source-cards, converted markdown, references, distillations, lenses, corpus-bound skills, builds, and packaged releases all sit inside one folder. Move the folder between tiers to change privacy. The build is corpus-rooted (`source_dir` in `builds.yaml` points at one corpus).

## Skills layout: substrate vs corpus-bound

Two locations, one rule: **substrate skills are corpus-agnostic; corpus-bound skills cite a specific corpus's references or task axes.**

- `.claude/skills/` (repo root): substrate skills, ship with the forge: `creating-*`, `ingesting-*`, `finding-resources`, `matching-references`, `answer-from-library`, `audit-attribution`. Discovered automatically by Claude Code from any working directory in the repo.
- `{corpus-root}/.claude/skills/`: corpus-bound skills, travel with the corpus. Discovered automatically by Claude Code when you work *inside* that corpus directory, or from anywhere when invoked with `--add-dir {corpus-root}/`.

When authoring corpus-bound skills, either work from inside the corpus or launch Claude Code with `--add-dir {corpus-root}/` so the corpus skills load alongside substrate. The build resolver checks the corpus first, then substrate; collisions warn and prefer the corpus version. Compiled apps flatten everything into the app's `.claude/skills/`, so runtime sees one directory.

Per-app skill membership is enumerated in each profile's `skills:` list in [`builds.yaml`](builds.yaml).

**Cross-skill references identify by heading text, not by step number.** Inside a single SKILL.md, *"see Step 5 below"* renumbers atomically when you reshuffle. Across skills, *"see the per-distillation orchestration step in `creating-applications`"* is rename-stable; *"see `creating-applications` Step 5"* is not. Keep ordinals in headings (they aid reading flow); never use them as the identity key for an external reference. Pass labels (`Pass A`–`Pass I`) in the 9-pass ingestion protocol are stable named anchors, not sequential steps, and are exempt.

The demo corpus's `openstax-organizational-behavior` slug is the canonical worked example used in `docs/architecture/matrix-pattern.md`.

## Retrieval pattern

When working in this repo or in any compiled distribution, the retrieval order matches the procedure documented in [`.claude/skills/answer-from-library/SKILL.md`](.claude/skills/answer-from-library/SKILL.md):

1. **Classify the query shape.** Named lookup (one source, Protocol N), diagnostic (situation in a known task domain, Protocol D), or synthesis (breadth across the corpus, Protocol S). Shape determines which indexes to read and in what order.
2. **Lens-applicability check.** For Protocols D and S, read `lens-index.json` unconditionally and detect whether a lens materially reweights what's salient. Skipped for Protocol N. The lens shapes how sub-claims decompose, so this runs *before* decomposition.
3. **Index, then distillation, then reference.** Read the runtime JSON indexes: `reference-index.json` (file catalogue), `concept-index.json` (concept axis with per-source section pointers), and `distillations/{task}/task-index.json` for the user's task domain. The slug-IDs in those indexes resolve through `references/slug-table.json` to file paths. The distillation is the pre-projected matrix cell: read it first for diagnostic questions; applicability has already been considered at ingestion. The deeper tiers are for citation and verification.
4. **Light ref for orientation, deep ref for citation.** The light reference is for fast orientation. The deep reference carries verbatim citations and evidence-classification markers; cite from the deep.
5. **`concept-index.json` for named concepts.** Look up the concept (or an alias) directly; each entry lists which sources cover it plus a section / md_line pointer where available. Grep across `corpus.commons/{corpus}/references/` only when a concept isn't in the index: a real gap, not a routing-effort default.

The runtime JSON indexes are derived artefacts; never hand-edit them. The per-task `{TASK}-DISTILLATION-INDEX.md` and `lenses/LENS-INDEX.md` operator-view markdowns are the authoring loop for their respective build scripts in `scripts/build_indexes/`: Pass G authors the operator view, the build regenerates the JSON from it plus the deep-ref frontmatter and the per-source extracted artefacts. `reference-index.json` and `concept-index.json` have no markdown operator view; they are built from the staging artefacts and deep-ref frontmatter directly, and the runtime reads the JSON. See [`docs/architecture/two-layer-indexes.md`](docs/architecture/two-layer-indexes.md).

## Distillation indexes

Each task domain has a `task-index.json` at `corpus.commons/demo/distillations/{task}/task-index.json`: the runtime situation router. It partitions the task into named phases (`section` field) and lists which references apply to each phase as `[need, slug-id, when]` rows. The corresponding `.md` view (`{TASK-UPPERCASE}-DISTILLATION-INDEX.md`) is the operator-inspection layer authored by Pass G. Read the JSON first when the user names their current phase or situation.

## Source integrity rule

**Never silently degrade source coverage to work around operational constraints.** If a task requires reading a full source and the system cannot handle it (timeouts, API errors, context limits), the correct response is: retry, or tell the operator and let them decide. Never skip sections of a source text and present the output as complete. Never instruct sub-agents to read partial files as a "pragmatic tradeoff." If a deep reference says "from the source text", it must mean the full source text was read. Partial coverage must be explicitly labelled as partial.

**Use deterministic converters, not the model.** When a source is a PDF or EPUB, convert it to text with a deterministic tool (markitdown, pandoc, pdftotext, calibre's ebook-convert) before ingestion. Do not ask the model to read the binary directly. Model-mediated extraction silently drops content (sidebars, footnotes, tables, figure captions) and the loss is invisible to downstream consumers. The 9-pass audit cannot recover what never reached the model's context.

Full statement and rationale: [`docs/architecture/source-integrity.md`](docs/architecture/source-integrity.md).

## 9-pass ingestion protocol

Every reference in this library is produced by the 9-pass ingestion protocol documented in [`docs/architecture/ingestion-protocol.md`](docs/architecture/ingestion-protocol.md). Passes A–E build the deep reference (context, structural read, deep read with citations, blockquote extraction, synthesis); Pass F derives the light reference; Pass G projects per task axis; Pass H cross-references; Pass I runs the source-only audit.

Invoked via the `ingesting-resources` skill at [`.claude/skills/ingesting-resources/SKILL.md`](.claude/skills/ingesting-resources/SKILL.md).

Pass I (source-only audit) is calibrated against a fixture corpus at [`tests/audit-fixtures/`](tests/audit-fixtures/). Three exemplars are read at the start of every audit; the full twelve-fixture set is a regression check when adopting a new model. See [`tests/audit-fixtures/README.md`](tests/audit-fixtures/README.md).

## Creating new applications

When a user asks to create an application—*"please create an AAR facilitator app"*, *"build me a coaching tool from this corpus"*, *"I want a distribution for incident review"*, or similar—invoke the [`creating-applications`](.claude/skills/creating-applications/SKILL.md) skill. **This is the single entry point.** The skill scopes the task axis if a spec doesn't already exist (calling `creating-tasks` inline), then scaffolds the distillation directory, distillation index, build profile, CLAUDE.md template, and any practitioner-role agents, then orchestrates per-distillation distillation by calling `creating-distillations` for each applicable source.

Route all *"create an app"* asks to `creating-applications`.

## Principles

Ground every source-grounded claim in a passage in a reference file. If the reference does not support the claim, say so; quote or cite only from the reference, and treat training-data knowledge of the author as out of scope. When citing, surface the evidence-classification marker (`[V]`, `[AP]`, `[AR]`, `[AE]`, `[BT]`) where it matters to the conclusion. What an author *demonstrated* is not what they *asserted*.

Keep the tiers separate. References describe the source; distillations apply the source to a task; library-level synthesis (cross-reference integration) lives in distillations, not in deep references. Build profiles are slices of the matrix: a new task domain is a new column, not a new repo.
