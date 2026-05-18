# Ingesting one source

A 60-minute walk through ingesting one source and building an app from it. You'll have the matrix expanding under your own hands by the end.

Recommended after [querying the library](querying-the-library.md). That tutorial taught you to read against the corpus; this one teaches you to extend it. The demo corpus is reasonable as a stable base, so a fresh corpus isn't required for your first ingestion.

## What you'll have done

By the end:

1. Picked one small public-licensed source.
2. Run the 9-pass ingestion protocol against it via the `ingesting-resources` skill, producing a deep reference, a light reference, and one distillation.
3. Built an app that includes the new source alongside the existing demo references.
4. Asked the new app a question that exercises *your* source and seen it cited.
5. Packaged the rebuilt app as a tarball you could hand to a colleague.

That's the matrix architecture working with material you brought.

## What you need

- The repo cloned. ([The demo app](the-demo-app.md) walks the clone step.)
- Node 18+ and Python 3.9+.
- A scratch directory (we'll use `~/gaf-tutorial/`).
- A working `markitdown` install for PDF/EPUB conversion: `pip install markitdown`.
- **Claude Code logged in.** Run `claude` once and complete `/login` if you haven't. The ingestion skill in Step 3 runs in an interactive Claude Code session; ~$1–5 in Opus 4.7 tokens for a small source.
- **Recommended pre-flight:** run `/matching-references {your topic}` from the [querying tutorial](querying-the-library.md) to check the corpus doesn't already cover your source's territory. Ingesting a duplicate wastes the 9-pass cost.

## Step 1: Pick a source

For this tutorial we'll use the **Agile Manifesto plus the 12 principles**: three pages of foundational text under a permissive licence. It's small enough to ingest in one session and conceptually rich enough to project usefully onto decision-making.

If you'd rather use your own source, pick one with these properties:

- **Short enough.** Under 30 pages. Bigger sources take 20–40 minutes of ingestion wall-clock; for a tutorial we want under 10.
- **Public-licensed.** CC0, CC BY, CC BY-SA, MIT, or public domain. Avoid all-rights-reserved material for this tutorial.
- **Expository prose.** Not slides, not a code dump, not a spreadsheet. The protocol works best on argumentative text.
- **Not already in the demo corpus.** You want to see the matrix *expand*, not duplicate.

Download the source as a PDF or copy the text into a markdown file.

## Step 2: Drop it into the corpus's ingest folder

The `ingest/` folder is where the protocol's runbook expects new material:

```bash
cp ~/Downloads/agile-manifesto.pdf corpus.commons/demo/sources/ingest/
```

Or if you have it as text:

```bash
cp ~/agile-manifesto.md corpus.commons/demo/sources/ingest/
```

You can verify it's staged:

```bash
ls corpus.commons/demo/sources/ingest/
```

## Step 3: Run the ingestion skill

Open Claude Code in the source repo:

```bash
cd /path/to/grounded-forge
claude .
```

In the session, invoke the skill:

```
/ingesting-resources agile-manifesto
```

(Or use whatever filename you dropped into `ingest/`; the skill resolves it.)

The skill walks Passes A through I:

- **Pass A**: frontmatter sidecar at `sources/original/agile-manifesto.source.md` (licence, scope, URL), converted markdown at `sources/converted/agile-manifesto.md`.
- **Passes B–E**: deep reference at `references/agile-manifesto-deep.md` with verbatim citations, evidence-classification markers ([V], [AP], [AR], [AE], [BT]).
- **Pass F**: light reference at `references/agile-manifesto.md`.
- **Pass G**: one distillation per applicable task axis. For decision-making, that lands at `distillations/decision-making/agile-manifesto-decision-making.md`.
- **Pass H**: mechanical-index pipeline. Allocate slug-ID, run the preprocessor, dispatch the Sonnet refs + cross-link passes, regenerate the runtime JSON indexes (`reference-index.json`, `concept-index.json`, per-axis `task-index.json`) and the operator-inspection markdown views (`REFERENCE-INDEX.md`, `DECISION-MAKING-DISTILLATION-INDEX.md`).
- **Pass I**: source-only audit. The deep ref doesn't ship until this passes.

Wall-clock for a 3-page source: ~5 minutes. For a 30-page source: ~20 minutes. The skill prints a per-pass summary so you can see the protocol working.

If Pass I fails, the skill flags exactly which claim didn't trace and pauses for you to inspect. The audit is not advisory; a failed Pass I means the deep reference doesn't ship.

## Step 4: Build the decision app

The new source is now part of the corpus. Build the decision app to include it:

```bash
npm run build:decision
```

The build output should show the reference count up by 2 (the light + deep variants of the new source) and the distillation count up by 1 (assuming Pass G said yes for `decision-making`). The exact numbers vary with corpus state; what matters is the delta. If you ran the demo first and added one source on top, expect the run to read something like:

```
References: 54 files copied   # was 52
Distillations: 27 files copied # was 26
```

(Pass G is per-distillation applicability-gated. If your new source is decision-relevant but not stakeholder-relevant, only the decision distillation gets produced, and the stakeholder build will report the same count it had before.)

## Step 5: Try it in the app

Copy the freshly-built decision app out:

```bash
rm -rf ~/gaf-tutorial/decision-app
cp -r corpus.commons/demo/apps/decision ~/gaf-tutorial/decision-app
cd ~/gaf-tutorial/decision-app
claude .
```

Ask a question that exercises your source. For the Agile Manifesto:

> Our team is debating whether to adopt fixed-scope sprints or rolling-priority kanban. How should we think about this?

What you should see: the assistant routes through `distillations/decision-making/task-index.json`, identifies the agile-manifesto distillation as one of the relevant distillations, reads it, and cites back to the deep reference. *Your* source is now part of the matrix the assistant routes through.

![A practitioner at a wooden desk in afternoon daylight, leaning slightly toward a laptop showing a long prose response, a handwritten notebook open beside the keyboard, coffee mug in hand. A quiet half-smile of recognition: the moment a thoughtful answer reflects their own thinking back to them.](../assets/success.png)

*The quiet moment when your own source comes back to you, projected onto the task you care about, in language you'd recognise as accurate.*

## Step 6: Package it

You've extended the corpus. Package the app so you can hand it to a colleague:

```bash
# back in the repo root
npm run package decision
```

The new tarball at `corpus.commons/demo/distros/decision-v0.2.1-open-nc.tar.gz` now includes the Agile Manifesto reference and distillation. The `LICENCE-MANIFEST.md` inside the tarball lists every source (including yours) with its scope and licence.

## What just happened

You extended the matrix by one source. The work was:

- **One ingestion run** (~5–20 minutes wall-clock, ~$1–5 in Opus 4.7 tokens for small sources).
- **One build** (mechanical, ~10 seconds).
- **One re-package** (mechanical, ~5 seconds).

The architecture is *additive*: a new source adds one row that populates across every applicable task column. The references the demo already shipped are unchanged. The distillation index gets a new routing entry where your source applies. The build picks all of this up automatically.

For a much bigger pull (a fork's worth of corpus, multiple task axes, custom build profiles), see the how-to: [`../how-to/build-your-library.md`](../how-to/build-your-library.md).

## What's next

- **[Scoping a source](scoping-a-source.md)**: the *before* of ingestion. `finding-resources` triages candidate sources before you pay the 9-pass cost; `ingesting-images` completes the visual axis on a source you ingested text-only. ~20 minutes.
- **[Adding a task axis](adding-a-task-axis.md)**: a new *column* in the matrix instead of a new row. Scope a task axis, scaffold an application, project every applicable source onto it. ~60–90 minutes.
- **[Adding a lens](adding-a-lens.md)**: design a per-distillation modifier that shapes what's salient through a perspective, role, or methodology stance. ~45 minutes.
- **[Scaffolding a corpus](scaffolding-a-corpus.md)**: the full forker arc. Move out of the demo and into a corpus of your own. ~2–3 hours.
- Read [`../architecture/projection-time.md`](../architecture/projection-time.md) for the cost-curve argument once you've felt the protocol's per-source cost first-hand.
