# Adding a task axis

A 60-to-90-minute walk through adding a new *column* to the matrix. You'll scope a task axis (`creating-tasks`), scaffold an application around it (`creating-applications`), and watch the orchestrator project every applicable source onto the new axis (`creating-distillations`). The matrix you saw as one column in [the demo app](the-demo-app.md) becomes a two-column corpus under your hands.

Recommended after [ingesting one source](ingesting-one-source.md). That tutorial taught you to add a row to the matrix (one new source × all existing task columns). This one teaches you to add a column (one new task × all applicable existing references). The two together are the matrix's two-dimensional defining move.

## What you'll have done

By the end:

1. Picked a candidate task axis the demo corpus could plausibly support (we'll use `risk-assessment` as the worked example).
2. Walked the `creating-tasks` dialogue and produced a task spec at `corpus.commons/demo/tasks/risk-assessment.md`.
3. Invoked `creating-applications`, which orchestrates the rest: scaffolds the distillation directory, seeds the distillation index, adds a build profile, authors the CLAUDE.md template, and dispatches per-source distillations.
4. Built and ran the new app.

The references on the row axis are unchanged. The distillation column is new. The build profile is new. Same corpus, new projection.

## What you need

- The repo cloned, Claude Code logged in. ([The demo app](the-demo-app.md) walks the setup.)
- ~$2–8 in Opus 4.7 tokens. Most of the cost is in Step 3's per-distillation orchestration: Pass G's applicability gate runs against every reference in the demo corpus, and the ones that fire *yes* produce a full distillation file each.
- ~60–90 minutes wall-clock, depending on how many of the demo's 26 references fire applicable for your task.

## Step 0: Pick a task axis

The discipline `creating-tasks` enforces is **Jobs-to-be-Done framing**: a task is a job a practitioner does in a circumstance, named with a verb and a noun. Not a *domain*, not a *role*, not a *topic*. The slug test is the one-line check: *"What does a practitioner do when they're doing this work?"*

Pass the verb-and-noun test:

- `decision-making` (✓ verb + noun)
- `stakeholder-engagement` (✓ verb + noun)
- `risk-assessment` (✓ verb + noun)
- `learning-from-incidents` (✓ verb + noun)
- `facilitating-retrospectives` (✓ verb + noun)

Fails the test (these are domains or roles, not tasks):

- `strategy` (✗ noun alone)
- `software-business` (✗ domain, not a job; survives only as a coarse parent for several real tasks)
- `the-CFO-role` (✗ role, not a job; needs a job-shaped verb)

For this tutorial we'll use **`risk-assessment`**: a task the demo corpus can plausibly support (the existing references on organisational behaviour, finance, ethics, decision-frameworks, and stakeholder dynamics all have something to say about risk) without being so obviously covered that the new axis adds nothing.

If you'd rather use your own axis, pick one that:

- Passes the verb-and-noun test.
- The demo corpus's existing references can plausibly support. (Half-a-dozen sources should fire *yes* at Pass G. If your axis is too narrow for the corpus, the orchestrator will produce few distillations and the result will feel thin.)
- Doesn't already exist in `corpus.commons/demo/distillations/`.

## Step 1: Scope the task axis

Open Claude Code in the source repo:

```bash
cd /path/to/grounded-forge
claude .
```

You can invoke `creating-tasks` directly if you want to scope the axis without immediately assembling its application:

```
/creating-tasks risk-assessment
```

Or invoke `creating-applications` straight away; it runs `creating-tasks` inline if no spec exists:

```
/creating-applications risk-assessment
```

Either path produces the same dialogue. We'll walk it standalone for clarity; the orchestrator's path is the same conversation, just continuous into Step 2.

The dialogue has nine phases:

- **Phase 0:** frame the work. The skill reads aloud what the spec will contain and confirms you want to proceed.
- **Phase 1:** problem statement. *What specific work is this axis meant to support?* One paragraph, concrete. Not *"help with risk decisions"*; rather, *"a practitioner who has identified a candidate risk and needs to weigh likelihood, impact, mitigation cost, and second-order effects before committing to action or non-action"*.
- **Phase 2:** practitioner questions. 5-10 concrete questions a practitioner asks in the field. *"How do I distinguish low-probability/high-impact risk from background noise?"* *"What's the cost of mitigation that I should weigh against the cost of inaction?"* *"Who needs to be consulted before I commit to a mitigation that has its own risks?"*
- **Phase 2a:** runtime listener grain. Trigger unit (what the practitioner observes) → response unit (the framework or check they reach for). At least five rows per phase. This is required. Without it the application is a catalogue, not a coach.
- **Phase 3:** available sources. Which existing references in the corpus, by slug, are likely to apply. The skill helps by reading the corpus catalogue and surfacing candidates; you confirm or trim.
- **Phase 4:** intended lenses (if any).
- **Phase 4a:** intended runtime agents (if any).
- **Phase 5:** overlap with existing axes. Where `risk-assessment` overlaps with `decision-making` (it does, substantially) and what makes them distinct.
- **Phase 6:** success criteria. How would you know in 3-6 months whether the axis was worth the work?
- **Phase 7:** dry-run check. The skill projects your scoping back to you and asks you to confirm.
- **Phase 8:** GO / YELLOW / NO-GO verdict.

The dialogue takes 15-25 minutes. The output lands at `corpus.commons/demo/tasks/risk-assessment.md`. Look at it before continuing: this is the spec everything downstream reads.

## Step 2: Scaffold the application

If you invoked `creating-tasks` standalone, run:

```
/creating-applications risk-assessment
```

(If you invoked `creating-applications` in Step 1, the dialogue continues here without a re-invocation.)

The skill walks five steps:

- **Step 1: distillation directory.** Creates `corpus.commons/demo/distillations/risk-assessment/`.
- **Step 2: distillation index.** Authors `RISK-ASSESSMENT-DISTILLATION-INDEX.md` (the operator-inspection view) seeded from the task spec's practitioner questions (Phase 2) and runtime listener grain (Phase 2a). The runtime JSON (`task-index.json`) is regenerated from this markdown by the build scripts.
- **Step 3: build profile.** Adds an entry to `builds.yaml`:

  ```yaml
  builds:
    risk-assessment:
      description: "Source-grounded assistant for risk-assessment work…"
      output_dir: corpus.commons/demo/apps/risk-assessment
      max_scope: open-nc
      references:
        include_patterns: ["*.md"]
      distillations:
        include: [risk-assessment]
      […]
  ```

  Plus an `npm run build:risk-assessment` script in `package.json`.
- **Step 4: CLAUDE.md template.** Authors `corpus.commons/demo/build-profiles/risk-assessment.md`. The template tells the deployed app's runtime how to route queries: what indexes to read, what citation discipline to follow, what to refuse.
- **Step 4a: agent files** (if the task spec declared any agents).
- **Step 5: per-distillation orchestration.** Here's where the cost lives. The skill iterates the *available sources* list from Phase 3 of the task spec and dispatches one `creating-distillations` call per source. Often in parallel batches.

## Step 3: Watch the per-distillation orchestration

Step 5 is the matrix's defining move. Each source named in the task spec gets one Pass G applicability check. The four-outcome gate:

- **Clear yes**: the source has substantive content for this task. The skill produces a full distillation file at `distillations/risk-assessment/{slug}-risk-assessment.md`.
- **Operator-confirmed yes**: the source might apply but the gate is uncertain; the operator confirms before the distillation is written.
- **Clear no**: the source has nothing meaningful to say about this task. Skip log entry, no distillation produced.
- **Operator-confirmed no**: the gate is uncertain in the *no* direction; the operator confirms the skip.

For the demo corpus's 26 references and an axis like `risk-assessment`, expect roughly 8-15 *yes* outcomes. The remaining sources are genuinely off-axis: a marketing reference has little to say about risk-assessment in the operational sense, even though *risk* appears in its text.

Each *yes* distillation includes a **`## Runtime triggers this source addresses` section** that maps the source's content to specific triggers from the task spec's seed table (Phase 2a). This is what makes the new app coach-shaped rather than catalogue-shaped: at retrieval, the runtime can route from *"I just noticed the team is dismissing low-probability tail risks because they sound 'paranoid'"* (a trigger) to *the section of the distillation that addresses that exact dynamic*.

The orchestrator writes its work as it goes; you can watch the per-distillation files appear in `distillations/risk-assessment/` and the index get updated by the consolidator at the end of the batch.

## Step 4: Build and run

```bash
npm run build:risk-assessment
```

The build copies your references into `corpus.commons/demo/apps/risk-assessment/`, copies the new distillation directory, stamps the CLAUDE.md template, and validates referential integrity.

Try it:

```bash
cd corpus.commons/demo/apps/risk-assessment
claude .
```

Ask a risk-assessment-shaped question:

> Our infrastructure team wants to defer the database migration by two quarters because the on-call team is stretched. What should I be thinking about in deciding whether to push back?

The assistant should route through `distillations/risk-assessment/task-index.json`, identify the relevant phase (likely *weighing-mitigation-vs-deferral* or whatever phase structure your task spec produced), pull the distillations that route there, and cite back to the deep references.

Compare with the decision-making app:

```bash
cd ../decision
claude .
```

Same question, different projection. The decision app frames it as *how do I make a defensible call?* The risk-assessment app frames it as *what's the full risk surface of the deferral itself, including the second-order effects?* Same corpus, two columns, two answers.

That difference is the matrix's two-dimensional value, now under your own hands.

## What just happened

You added a column to the matrix. The chain was:

- **`creating-tasks`** scoped the axis under Jobs-to-be-Done discipline.
- **`creating-applications`** scaffolded the distillation directory, distillation index, build profile, CLAUDE.md template, and any agents.
- **`creating-distillations`** projected every applicable source onto the new axis, gated by Pass G's four-outcome applicability check.

The corpus didn't grow on the row axis: no new sources, no new references. The corpus grew on the column axis: one new task projection across the existing reference set. That's the matrix architecture's defining move; the demo's `decision`, `stakeholder`, and `software-business` apps are three pre-built columns; you've just added a fourth.

Cost discipline: the per-distillation orchestration is the expensive step ($2–8 of Opus tokens for the demo's 26 references). The scoping and scaffolding steps are cheap ($0.10–0.50 each). The cost concentrates where the value concentrates: in the actual projections.

## What's next

- **[Adding a lens](adding-a-lens.md)**: lens design and per-distillation lens application. A lens is a per-distillation modifier; it shapes salience through a perspective, role, or methodology stance. ~45 minutes.
- **[Scaffolding a corpus](scaffolding-a-corpus.md)**: the full forker arc. Move out of the demo and into a corpus of your own. The skills you've used here re-apply unchanged to a local corpus. ~2–3 hours.
- Read [`docs/architecture/matrix-pattern.md`](../architecture/matrix-pattern.md) for the worked example of reference × task projection. The matrix is now operationally visible to you; the architecture doc will land differently than it would have before this tutorial.
- Read [`docs/architecture/projection-time.md`](../architecture/projection-time.md) for the cost-curve argument: why pre-projecting at ingestion time is cheaper at scale than re-projecting at query time, even though you just felt the ingestion-time cost first-hand.
