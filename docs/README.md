# grounded-forge docs

Four kinds of documentation, sorted by what you're trying to do:

| If you're… | Start here |
|---|---|
| **Learning** the matrix architecture by doing | [`tutorial/`](tutorial/) |
| **Building** your own corpus or app | [`how-to/`](how-to/) |
| **Looking up** a field, taxonomy, or term | [`reference/`](reference/) |
| **Understanding** why the architecture is shaped this way | [`architecture/`](architecture/) |

## Tutorial: learn by doing

The seven tutorials are sequential and incremental. Each introduces one or two substrate skills, in the order an operator naturally encounters them. The first two are no-cost; the rest each add one skill or sub-skill at a time. Read at least up to the one that matches your immediate work; the later tutorials wait when you need them.

1. [The demo app](tutorial/the-demo-app.md): open a pre-built demo app, ask it questions, feel the matrix route end-to-end. No setup, no cost. ~25 minutes.
2. [Querying the library](tutorial/querying-the-library.md): the three read-only skills — `answer-from-library`, `matching-references`, `audit-attribution` — plus a *reading the trace* section that teaches the five-second answer audit. ~30–45 minutes.
3. [Ingesting one source](tutorial/ingesting-one-source.md): the 9-pass ingestion protocol via `ingesting-resources`, against one source you bring. The matrix expands by one row. ~60 minutes.
4. [Scoping a source](tutorial/scoping-a-source.md): the *before* of ingestion (`finding-resources`) and the *after* of the image axis (`ingesting-images`). ~20 minutes.
5. [Adding a task axis](tutorial/adding-a-task-axis.md): a new *column* in the matrix. `creating-tasks` scopes the axis, `creating-applications` orchestrates assembly, `creating-distillations` projects every applicable source. The matrix's defining two-dimensional move. ~60–90 minutes.
6. [Adding a lens](tutorial/adding-a-lens.md): the per-distillation modifier. `creating-lenses` scopes the lens; Pass G applies it where the gate fires. ~45 minutes.
7. [Scaffolding a corpus](tutorial/scaffolding-a-corpus.md): the full forker arc, with `creating-corpus`. Spin up `corpus.local/{your-corpus}/` from nothing. ~2–3 hours.

## How-to: guided procedures for specific goals

- [Build your library](how-to/build-your-library.md): fork the repo, pick task axes, ingest sources, configure builds, ship.
- [Extend or clear the demo](how-to/extend-or-clear-the-demo.md): finish the image classification on the demo corpus, or strip it and start fresh.

## Reference: lookup material

- [Vocabulary](reference/vocabulary.md): the load-bearing nouns and verbs (source, reference, distillation, application, lens, …).
- [Distribution scope](reference/scope-taxonomy.md): the five-level taxonomy that governs which references ship in which app.
- [Build profile schema](reference/build-profile-schema.md): every field of a `builds.yaml` profile, what it does, what it defaults to.
- [Known limitations](reference/known-limitations.md): what ships partial in this release, how to complete or clear it.
- [Pass I audit results](audit-results/): per-source audit logs and cross-corpus summary.

## Architecture: why the matrix works this way

- [Overview](architecture/overview.md): one-page summary; read first.
- [LLM epistemology](architecture/llm-epistemology.md): the problem the architecture is solving against.
- [Projection time](architecture/projection-time.md): the cost-curve argument vs. standard RAG.
- [Matrix pattern](architecture/matrix-pattern.md): worked example of the reference × task projection.
- [Two-layer indexes](architecture/two-layer-indexes.md): why corpus catalogue and distillation index do different jobs.
- [Source integrity](architecture/source-integrity.md): the rule and what enforces it.
- [Ingestion protocol](architecture/ingestion-protocol.md): rationale for the nine-pass shape.
- [Capability binding](architecture/capability-binding.md): how profiles declare abstract capabilities and the runtime resolves them.
- [Known architectural limits](architecture/known-architectural-limits.md): three limits intrinsic to the design.
- [Copyright](architecture/copyright.md): the operator's stance and the system's neutrality.
- [Decisions and non-decisions](architecture/decisions-and-non-decisions.md): what was decided, what was considered and turned down, what's deferred.

## Top-level

- [`../README.md`](../README.md): repo overview and quick-start
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md): contributing a corpus to the commons tier
- [`../CLAUDE.md`](../CLAUDE.md): the assistant's system context when working *on* this repo
