# Building your library

A walkthrough for forking this repo and standing up a reference × task matrix in your own domain. The repo is domain-neutral; the example task axes (decision-making, stakeholder-engagement) and the OpenStax demo corpus are illustrative. Replace them.

## A concrete starting point

The simplest fork looks like this:

```bash
git clone <this-repo> my-library
cd my-library
# Pick your task axes. Pick two or three to start.
# Pick your sources. Three to ten is plenty for a first cut.
# Run the ingestion protocol, populate the indexes, ship.
```

You are aiming for a `corpus.commons/{your-corpus}/apps/{your-profile}/` directory that compiles your sources, your task projections, and your CLAUDE.md template into a self-contained assistant distribution.

**Prerequisites:** Node.js ≥ 18 for the build, Python 3.9+ for the ingestion scripts, an `ANTHROPIC_API_KEY` for the LLM-mediated passes, and Claude Code (or another Claude API surface) to run the skills.

## Step 1: Pick your task axes

A task axis is a recurring kind of work an assistant in your domain needs to support. Examples:

- *Coaching*: framing, exploration, intervention, integration.
- *Risk assessment*: scoping, identification, evaluation, treatment, monitoring.
- *Hiring*: profiling, sourcing, screening, interviewing, reference-checking, deciding.
- *Onboarding*: pre-arrival, week-one, first-month, ramp.

Two task axes to start. Partition each task into 5–8 named *phases* or *situations*, which become the sections of your distillation index.

## Step 2: Pick your sources

A source is one author-topic unit. Typically a book, sometimes a paper, sometimes a methodology document. Three to ten sources is a sensible first cut.

Use the [`finding-resources`](../../.claude/skills/finding-resources/SKILL.md) skill if you need candidates and triage. It runs each candidate through a viability check (licence, deterministic-conversion-possible, full source readable, expository prose) and buckets the output into *proceed*, *sample first*, *skip*. Skip the skill when you already have the source in hand.

Criteria:

- *Stable enough to be worth pre-projecting.* Sources superseded every quarter cost more than they save.
- *Substantive enough to merit a deep ref.* A blog post doesn't need this architecture.
- *Source licence.* Record the actual licence in each deep-ref's `**Licence:**` line. See [`../architecture/copyright.md`](../architecture/copyright.md) for the operator's stance; verify with qualified counsel.
- *Distribution scope.* Record one of `open`, `open-nc`, `copyrighted`, `confidential`, or `personal` in each deep-ref's `**Scope:**` line. See [`../reference/scope-taxonomy.md`](../reference/scope-taxonomy.md) for the levels and what filters at build time.

## Step 3: Run the ingestion protocol

Invoke the `ingesting-resources` skill at [`.claude/skills/ingesting-resources/SKILL.md`](../../.claude/skills/ingesting-resources/SKILL.md). Per source, the protocol produces:

1. A deep reference (`{author}-{topic}-deep.md`).
2. A light reference (`{author}-{topic}.md`) derived from the verified deep.
3. One distillation per task axis (`corpus.commons/{corpus}/distillations/{task}/{author}-{topic}-{task}.md`).

Pass I (source-only audit) is the gate: a deep reference does not ship until Pass I passes. For the protocol's rationale, see [`../architecture/ingestion-protocol.md`](../architecture/ingestion-protocol.md).

## Step 4: Indexes update themselves

The ingestion skill's Pass H drives the mechanical-index pipeline once per source: allocate slug-ID, run the deterministic preprocessor, dispatch the Sonnet refs and cross-link passes, regenerate the runtime JSON indexes. Operators do not hand-edit any JSON index; updates flow through frontmatter, the slug table, and the per-task operator-inspection markdown views (which Pass G authors).

The runtime indexes that get regenerated each Pass H:

- `corpus.commons/{corpus}/references/slug-table.json`: append-only IDs.
- `corpus.commons/{corpus}/reference-index.json`: the file catalogue.
- `corpus.commons/{corpus}/concept-index.json`: the concept axis with section pointers.
- `corpus.commons/{corpus}/distillations/{task}/task-index.json`: the per-axis situation router.

The operator-inspection markdown views (`references/REFERENCE-INDEX.md`, per-task `{TASK}-DISTILLATION-INDEX.md`) sit alongside the JSON as readable surfaces for browsing the corpus. The architectural argument for the split is at [`../architecture/two-layer-indexes.md`](../architecture/two-layer-indexes.md).

## Step 5: Configure builds.yaml

Each profile in [`builds.yaml`](../../builds.yaml) is a slice of the matrix. For a fork that ships two task axes:

```yaml
builds:
  my-task-1:
    description: "..."
    output_dir: corpus.commons/my-corpus/apps/my-task-1
    max_scope: open-nc
    references:
      include_patterns: ["*.md"]
    distillations:
      include: [my-task-1]
    lenses:
      include: true
    skills:
      include: [matching-references, answer-from-library]
    claude_md:
      template: my-task-1

  my-task-2:
    # same shape, second task axis
```

The full schema is at [`../reference/build-profile-schema.md`](../reference/build-profile-schema.md).

For each profile, write a CLAUDE.md template at `corpus.commons/{your-corpus}/build-profiles/{profile}.md` (or `corpus.local/{your-corpus}/build-profiles/{profile}.md` for private corpora). The template ships into `apps/{profile}/CLAUDE.md` and briefs the assistant on the task domain, the distillation index, the retrieval order, and the source-integrity rule. ~400 words.

## Step 6: Build, verify, ship

```bash
npm install
npm run build
diff -rq corpus.commons/my-corpus/apps/my-task-1/ corpus.commons/my-corpus/apps/my-task-2/
```

The `diff -rq` verify-step assumes you configured two profiles in Step 5; if you're shipping a single-axis fork, skip the diff and inspect `corpus.commons/my-corpus/apps/{your-profile}/` directly. With two profiles, the diff should show different distillation directories and different CLAUDE.md templates; same references. If the two apps ship identical content, the `distillations.include` lists in `builds.yaml` need fixing.

To package an app as a tarball for distribution:

```bash
npm run package my-task-1
```

Produces `corpus.commons/my-corpus/distros/my-task-1-v{version}-{scope}.tar.gz` with a `LICENCE-MANIFEST.md` at the root.

## Step 7: Add task axes or sources later

The architecture is additive:

- **New source**: run the 9-pass protocol once via the `ingesting-resources` skill. The new row populates across all existing columns.
- **New task axis**: run `creating-applications`. It scopes the axis (via `creating-tasks`), scaffolds the distillation directory and index, creates the build profile, and orchestrates per-distillation projection.

For why the architecture is shaped this way, see [`../architecture/projection-time.md`](../architecture/projection-time.md) and [`../architecture/matrix-pattern.md`](../architecture/matrix-pattern.md).
