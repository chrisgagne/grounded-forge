# Scoping a source

A 20-minute walk through the two skills that bracket ingestion: `finding-resources` (the *before*) and `ingesting-images` (the *after*, for the visual axis). Together they're how you scope an ingestion well rather than paying the 9-pass cost on a source that wasn't a fit, and how you complete the image axis when text-only ingestion left it partial.

Recommended after [ingesting one source](ingesting-one-source.md). That tutorial walked the full 9-pass protocol; this one teaches the discipline that makes ingestion cheaper and the follow-up that makes a source fully usable.

## What you'll have done

By the end:

1. Run `finding-resources` against a topic in your corpus's gap area and read the triage report.
2. Picked one *proceed* candidate from the report, and one *sample first* candidate, and known why each landed in its bucket.
3. (Optionally) run `ingesting-images` against a source you ingested in the previous tutorial, or against one of the demo corpus's existing sources, and seen substantive diagrams entered into the corpus's image index.

## What you need

- The repo cloned, Claude Code logged in. ([The demo app](the-demo-app.md) walks the setup.)
- The Agile Manifesto source from [ingesting one source](ingesting-one-source.md), or any other source you've ingested. (Step 3 needs a source to classify images for. If you skipped the previous tutorial, the optional path uses the demo corpus's existing sources.)
- ~$0–1 in Opus 4.7 tokens for `finding-resources`. `ingesting-images` runs Sonnet sub-agents for the classification waves; ~$0.50–2 for a small source.

## Step 1: Find a gap to fill

`finding-resources` works best when you give it a specific gap to scout against, not a free-form *"find me some books on management"*. Gaps come from one of three places:

- **A thin distillation** in an existing task index. The decision-making axis's *evaluating-trade-offs* phase has fewer references than the others, or the stakeholder axis has nothing on cross-cultural conflict.
- **A new task axis you're scoping.** You're about to walk [adding a task axis](adding-a-task-axis.md) and want candidate sources before scaffolding the axis.
- **A named topic you noticed in `matching-references`**. You ran a topic query in the previous tutorial and the corpus returned nothing.

For this tutorial we'll use a concrete gap in the demo corpus: **rigorous treatment of group decision-making research** beyond the OpenStax management chapters. The corpus has organisational-behaviour and decision-framework references, but no behavioural-science source specifically on small-group decision dynamics.

Open Claude Code in the source repo:

```bash
cd /path/to/grounded-forge
claude .
```

Invoke the skill:

```
/finding-resources rigorous treatment of small-group decision-making research, behavioural science axis
```

By default the skill applies a `cc-only` licence filter: only Creative Commons, public-domain, and permissive open-source candidates. (This is the strictest filter and the safest default. Pass `unfiltered` if you want to handle licensing manually.)

The skill walks four steps:

1. **Candidate generation**: web search across known-good repositories (OpenStax, Stanford Encyclopedia, BCcampus, OECD, etc.) plus broader search.
2. **Viability checks**: each candidate runs through the gates from [`docs/architecture/source-integrity.md`](../architecture/source-integrity.md). Self-contained, expository prose, full text available, deterministic conversion path, distinguishable authorship.
3. **Licence and scope check**: explicit licence string for every candidate, regardless of filter mode.
4. **Gap-fit triage**: each candidate gets one of three verdicts, with the reason recorded.

## Step 2: Read the triage report

The skill writes a report to a path it tells you (typically `_planning/finding-resources-{topic-slug}-{date}.md`). The report has three sections.

**Proceed** entries are ready to feed straight into `ingesting-resources`. They look like:

```
### proceed-1: Janis, "Groupthink", chapter excerpts (HathiTrust)

- URL: https://hathitrust.org/...
- Format: PDF (deterministic via markitdown)
- Licence: Public domain (US Government work, 1972 source)
- Scope: open
- Coverage: Direct treatment of cohesion-induced decision pathology;
  the canonical reference for group decision-making failure modes.
- Gap fit: Fills the "small-group decision dynamics" gap; complements
  existing OpenStax management chapters with behavioural-science depth.
- Estimated size: ~80 pages of selected chapters; ~20 min ingestion.
```

**Sample first** entries are viable on most checks but uncertain on one. The skill names which check:

```
### sample-first-1: OECD Working Paper No. 87, "Group decision-making
in complex policy environments"

- URL: https://oecd.org/...
- Format: PDF
- Licence: OECD terms of use (permissive but verify per-document)
- Scope: open-nc (likely; verify before ingestion)
- Coverage: Strong on policy-context group decisions; uncertain whether
  it cites primary behavioural research or operates at policy-summary
  level.
- Probe: Read sections 2–3 and the bibliography before committing.
- Gap fit: Fills part of the gap; depth of primary research grounding
  is the open question.
```

**Skip** entries explain why:

```
### skip-1: Various blog posts on Groupthink (Wikipedia, Medium, etc.)

- Reason: Tertiary sources, not expository documents with citation
  discipline. Routes back to the primary sources already named under
  proceed-1.
```

The skill is *not* doing the ingestion; it's doing the triage that makes ingestion cheap. Each `proceed` entry is shaped as ready input for `/ingesting-resources`.

## Step 3: (Optional) Run image classification

Most sources have images: diagrams, charts, photos, decorative figures. The 9-pass text protocol skips them by default; the image axis is a separate skill so it can be run in parallel with text ingestion or completed later when context budgets allow.

If you ingested the Agile Manifesto in the previous tutorial, it has effectively no images (it's three pages of text). Pick a source with visual content instead. The demo corpus's OpenStax sources are dense with diagrams and useful as a worked example:

```
/ingesting-images openstax-organizational-behavior
```

The skill walks 13 steps but the user-visible ones are:

1. **Extract images** if the `{slug}-images/` directory is empty. Runs `python3 scripts/extract-images.py` against the original PDF.
2. **Wave the file list** into batches of 64 (for sources over ~100 images). Each wave is one Sonnet dispatch + one splice + one commit.
3. **Per-wave classification**: a read-only Sonnet sub-agent inspects each image visually (not by filename, not by file size: visually) and classifies it as **SUBSTANTIVE** (diagrams, charts, data tables, frameworks, screenshots that carry information) or **DECORATIVE** (photos, covers, logos, decorative figures).
4. **Splice substantive entries** into the corpus's `sources/converted/IMAGE-INDEX.yaml`. Decoratives are deleted file-by-file.
5. **Per-wave commit**, so partial progress is recoverable if a later wave fails.
6. **Final wave**: switch the IMAGE-INDEX header from `PARTIAL` to `FINAL`, with a reconciliation line confirming `indexed + deleted = original-extraction-count`.

For a small source (~30 images), one wave is enough; the run finishes in a few minutes. For a textbook with 800+ images, it's a long-running multi-wave job; the per-wave commits are the recovery surface if your session is interrupted.

The output is an updated `IMAGE-INDEX.yaml` with entries like:

```yaml
- file: openstax-organizational-behavior-images/figure-14-3-conflict-types.png
  description: A 2×2 matrix mapping conflict types by intensity (low/high)
    and substance (task/relationship). Each quadrant labelled with a
    typical organisational example.
  classified: SUBSTANTIVE
  page_hint: ch.14, p.342
```

These entries are what makes images queryable in the same way text is: a downstream skill can ask *"which images in the corpus address conflict-type taxonomies?"* and get a structured answer.

**Hard rule from the skill**: every entry shipped in IMAGE-INDEX.yaml has been *visually inspected*. The skill blocks heuristic shortcuts (filename matching, file size, extension) because the same format carries diagrams in one source and photographs in another. Visual inspection is non-negotiable. See `.claude/skills/ingesting-images/SKILL.md` for the full discipline.

## What just happened

You used the two skills that bracket ingestion:

- **`finding-resources`** is *pre-ingestion triage*: it pays the cost of search and viability checks so you don't pay the cost of a failed 9-pass run. The output is a structured report; the `proceed` entries are formatted as ready input for `ingesting-resources`.
- **`ingesting-images`** is *post-ingestion image classification*: text and image axes run independently, so a source can be text-ingested first (the higher-value axis for most queries) and image-ingested later when context is available.

Together they make ingestion *cheap to scope*. The 9-pass cost goes where it earns: on sources you've triaged and decided to commit to, and on the visual axis when it materially helps retrieval.

## What's next

- **[Adding a task axis](adding-a-task-axis.md)**: a new *column* in the matrix. `creating-tasks` scopes the axis, `creating-applications` assembles the application, `creating-distillations` projects every applicable source onto it. ~60–90 minutes.
- **[Adding a lens](adding-a-lens.md)**: per-distillation modifiers that shape what's salient through a perspective, role, or methodology stance. ~45 minutes.
- **[Scaffolding a corpus](scaffolding-a-corpus.md)**: the full forker arc, when you're ready to move out of the demo. ~2–3 hours.
- Read [`docs/architecture/source-integrity.md`](../architecture/source-integrity.md) for the discipline `finding-resources` enforces and *why* the viability gates are non-negotiable.
