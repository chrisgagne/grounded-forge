# Adding a lens

A 45-minute walk through designing a lens and applying it to distillations in an existing application. You'll scope a lens (`creating-lenses`), drop the spec into the corpus, and watch a re-run of `creating-distillations` produce lens-shaped sections (or per-lens variants) where the gate fires applicable.

Recommended after [adding a task axis](adding-a-task-axis.md). By this point you've used the row direction (sources) and the column direction (task axes). A lens is neither: it's a *per-distillation modifier* that shapes what's salient through a perspective, role, or methodology stance. The matrix stays two-dimensional; the lens optionally reshapes one cell.

## What you'll have done

By the end:

1. Picked a candidate lens — we'll use **`engineering-manager-post-incident`** as the worked example, a personifiable-archetype lens.
2. Walked the `creating-lenses` dialogue and produced a spec at `corpus.commons/demo/lenses/engineering-manager-post-incident.md`.
3. Decided which distillations the lens applies to, and re-run `creating-distillations` for those (source, task) pairs with the lens in scope.
4. Asked the same diagnostic question with and without the lens active, and watched the answer's vocabulary, salience, and recommended actions change.

## What you need

- The repo cloned, Claude Code logged in.
- Either the `risk-assessment` app from [adding a task axis](adding-a-task-axis.md), or one of the existing apps from the demo: `decision`, `stakeholder`, `aar-mode`, `retro-mode`. The lens worked example below pairs naturally with `aar-mode` or `retro-mode` because *post-incident* is their territory; it works against `decision` too but the demonstration is less vivid.
- ~$1–3 in Opus 4.7 tokens. The lens dialogue is cheap (~$0.20); the re-projection of affected distillations is the bulk.

## What a lens *is* and *isn't*

The vocabulary discipline matters because lenses are easy to confuse with task axes.

A **task axis** is the *what work* dimension: what a practitioner is *doing*. Decision-making, stakeholder-engagement, risk-assessment. The axis is the column direction; references are pre-projected onto it at ingestion time.

A **lens** is the *who or what stance* dimension: through whose perspective is the work being done? Engineering-manager-post-incident, CTO-at-Series-B, Goldratt-on-constraints, queue-physics. A lens is *not* a third axis; it's a per-distillation modifier. The matrix stays 2D.

Three kinds of lens are first-class (per the `creating-lenses` skill):

- **Personifiable-archetype**: a role-in-circumstance that anyone could be standing in. *engineering-manager-post-incident*, *first-time-board-chair*, *PM-handling-feature-pivots*.
- **Named-real-person**: a specific person whose published material grounds the lens. The lens reads *as if Jane Doe were reading, given what her public material reveals about her stance*, not *as Jane Doe*.
- **Non-personifiable-frame**: a methodology or analytical stance. *queue-physics-lens*, *loss-aversion-lens*, *theory-of-constraints-lens*. No chair to sit in; just a way of seeing.

For this tutorial we'll use the first kind — it's the most common and the easiest to demonstrate.

## Step 1: Scope the lens

```bash
cd /path/to/grounded-forge
claude .
```

Invoke the skill:

```
/creating-lenses engineering-manager-post-incident
```

The dialogue has six phases:

- **Phase 0:** frame the work. The skill reads aloud what the spec will contain.
- **Phase 1:** kind of lens. Three diagnostic questions decide whether your lens is personifiable-archetype, named-real-person, or non-personifiable-frame. For our worked example: **personifiable-archetype** (we're naming a role-in-circumstance, not a specific person).
- **Phase 2:** job-and-circumstance. *What job is the lens-wearer doing? In what circumstance?* For `engineering-manager-post-incident`: *understanding what just happened and what to change without (a) blaming the engineer closest to the trigger, (b) reaching for the most visible procedural fix, or (c) shipping a retro that has no follow-through.*
- **Phase 3:** salience and vocabulary. What does the lens-wearer *notice first*? What *recedes*? What's their *native vocabulary*? For our example:
  - Notices first: timeline disagreements between teams, decisions made under partial information, hand-offs where context was lost.
  - Recedes: tooling specifics, individual code-quality calls, blame-as-explanation.
  - Native vocabulary: *contributing factors*, *latent conditions*, *just culture*, *blameless review*, *systemic vs proximate causes*.
- **Phase 4:** grounding contract. Where does the lens's intelligence come from? What does it refuse? The grounding contract is what stops a lens from becoming generic LLM-flavoured advice. For our example: *the lens reads through Dekker's just-culture framing and the AAR cycle; refuses individual-attribution explanations even when the operator asks for them.*
- **Phase 5:** fire-list. What older framing does this lens *displace*? The fire-list keeps the lens honest about what it's replacing. For our example: *replaces the implicit "find the engineer who broke it" framing that most informal post-incident conversations default to.*
- **Phase 6:** trust-breaking failure mode. The single most dangerous failure mode the lens has. For our example: *acting as if blameless review means no individual accountability; the lens distinguishes individual accountability from individual attribution, and a failure to hold that distinction breaks trust with the engineering team.*

The dialogue takes 10-20 minutes. The output lands at `corpus.commons/demo/lenses/engineering-manager-post-incident.md`. The spec also carries `visibility:` frontmatter (`open`, `open-nc`, `copyrighted`, `confidential`, `personal`) parallel to references' `Scope:`; that field controls which build profiles can ship the lens.

After the spec is written, the build's index generator picks the lens up at the next build: `lenses/LENS-INDEX.md` and `lens-index.json` get an entry, including the `salience` block (notices-first / recedes / native-vocabulary) that the runtime's lens-applicability check reads.

## Step 2: Decide which distillations the lens applies to

A lens is per-distillation, not per-task and not per-source. The same lens might fire applicable on the `learning-from-incidents × dekker-just-culture` distillation but skip on the `learning-from-incidents × openstax-accounting` distillation. Pass G of `creating-distillations` runs a four-outcome applicability gate per (source, task, lens) combination:

- **Clear yes (full reshape)**: the lens materially reweights salience for this distillation. The skill produces a separate per-lens distillation at `distillations/{task}/{slug}-{task}-{lens-name}.md`.
- **Partial reshape**: the lens shifts some emphasis but doesn't justify a separate file. A `## Through the {lens-name} lens` section is added inside the main distillation.
- **Clear no**: the lens is irrelevant to this distillation. Skip log entry, no change to the file.
- **Operator-confirmed no**: the gate is uncertain in the *no* direction; the operator confirms.

For the worked example, the lens is most likely to fire applicable on distillations in the `learning-from-incidents` task axis (the `aar-mode` app) and on a few distillations in `decision-making` where post-incident context shifts the salience.

## Step 3: Re-project affected distillations

You have two options.

**Option A: surgical.** Re-run `creating-distillations` for the (source, task) pairs you think the lens applies to, with the lens named:

```
/creating-distillations learning-from-incidents dekker-just-culture --lens engineering-manager-post-incident
```

The skill runs Pass G's applicability gate, decides full-reshape / partial-reshape / no, and produces the appropriate output.

**Option B: orchestrated.** Re-invoke `creating-applications` against the existing task axis with the lens in scope. The orchestrator iterates every applicable source for the task and runs the per-lens applicability gate against each:

```
/creating-applications learning-from-incidents --add-lens engineering-manager-post-incident
```

For a tutorial, Option A is cheaper and more visible. Pick two or three distillations you think the lens applies to and re-run them surgically.

## Step 4: Build and feel the difference

```bash
npm run build:aar-mode
cd corpus.commons/demo/apps/aar-mode
claude .
```

Ask a question that's *post-incident* shaped:

> The on-call engineer made a config change Friday night that took us down for two hours. The team is split between "wow that was reckless" and "the runbook didn't cover that case." How should I run the retro on Monday?

Without the lens active, the assistant routes through the AAR distillations and gives generally-good AAR guidance. With the lens active (the bundled CLAUDE.md instructs `/answer-from-library` to read `lens-index.json` and detect lens-shaped queries), the answer should:

- **Lead with what the engineering-manager-post-incident lens notices first**: the timeline of decisions under partial information, the hand-off where context was lost, the runbook gap as a *latent condition*, not the engineer's individual judgement call.
- **Use the lens's native vocabulary**: *contributing factors*, *latent conditions*, *blameless review* (with the *individual-accountability vs individual-attribution* distinction the trust-breaking-failure-mode section guards).
- **Refuse moves the lens explicitly fires**: any framing that resolves to *"the engineer was reckless"* should be reshaped or rejected.

To force the lens explicitly:

```
/answer-from-library --lens engineering-manager-post-incident The on-call engineer made a config change Friday night that took us down for two hours…
```

The `--lens` flag bypasses the lens-applicability check and applies the lens regardless. Useful when you want to *see* what the lens does to an answer; the default routing applies the lens only when the query is genuinely lens-shaped.

## What just happened

You added a per-distillation modifier without adding a new axis to the matrix. The chain was:

- **`creating-lenses`** scoped the lens under role-in-circumstance discipline, with grounding contract and trust-breaking-failure-mode guards.
- **`creating-distillations`** ran Pass G's per-distillation applicability gate against the lens and produced full-reshape, partial-reshape, or no-change outputs.
- **Runtime application** in the deployed app: `answer-from-library` reads `lens-index.json`, detects lens-shaped queries (or accepts an explicit `--lens` flag), and shapes salience through the lens at query time when no pre-projected (source, task, lens) distillation exists.

The corpus row count is unchanged. The corpus column count is unchanged. The lens index has one new entry; affected distillations carry a `## Through the {lens-name} lens` section or have a sibling per-lens variant; the runtime knows when to apply the lens.

This is the matrix's *third dimension that isn't* — per-distillation modifiers, applied where they earn their keep, not everywhere. Skill `creating-lenses` keeps lens design rigorous; Pass G's applicability gate keeps lens application selective.

## What's next

- **[Scaffolding a corpus](scaffolding-a-corpus.md)**: the full forker arc, now that you've used every substrate skill in the demo corpus. ~2–3 hours.
- Read [`docs/reference/vocabulary.md`](../reference/vocabulary.md) §lens for the lens vocabulary's place in the noun/verb grammar.
- Read [`.claude/skills/creating-distillations/projection-protocol.md`](../../.claude/skills/creating-distillations/projection-protocol.md) §Lens-as-optional-framing for the four-outcome applicability gate's full rules.
- If your corpus is gathering its own real-named-person lenses (a CTO whose published material is worth grounding against, a methodology author whose framings keep coming up): read the *named-real-person* branch of the `creating-lenses` skill. The grounding contract there is the load-bearing constraint; *ventriloquism* is the failure mode and the lens is what guards against it.
