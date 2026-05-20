# Querying the library

A 30-to-45-minute walk through the three skills you use to query an existing corpus without ingesting anything: `answer-from-corpus`, `matching-references`, and `audit-attribution`. Includes a *reading the trace* section that teaches you to audit any answer in five seconds. No build, no ingestion, no cost beyond Opus tokens for the queries themselves.

Recommended after [the demo app](the-demo-app.md). The demo gave you the *feel* of the matrix. This tutorial gives you the *protocols* the matrix runs on, so you can drive the retrieval deliberately instead of trusting the assistant's defaults.

## What you'll have done

By the end:

1. Asked the same question two ways: once with the default assistant behaviour, once via the `answer-from-corpus` skill invoked explicitly. Watched the trace get more disciplined.
2. Used `matching-references` to enumerate what's already in the corpus on a topic, before considering ingestion.
3. Run `audit-attribution` against a short draft to see which references in the corpus overlap with its claims.

You'll come out with a working mental model of *consumption* of the library, separate from *production*. The later tutorials extend the library; this one teaches you to read it.

## What you need

- The repo cloned and one demo app handy. ([The demo app](the-demo-app.md) walks the steps.)
- Claude Code logged in. The three skills run interactively; expect ~$0.10-1 in Opus tokens for the queries in this tutorial.
- A short prose draft, around 300-800 words, on a topic the demo corpus has coverage on. (Decision-making, stakeholder dynamics, motivation, organisational behaviour: anywhere the corpus is dense.) The draft is for Step 4. If you don't have one, the step suggests material you can paste.

## Step 1: Open the decision app

```bash
cd corpus.commons/demo/apps/decision
claude .
```

You're back in the session you used in *the demo app* tutorial. The corpus and skills are bundled.

## Step 2: Ask a question two ways

First, the default behaviour. Ask:

> Our finance team is recommending we sell the product line at a loss to clear inventory. What should I be thinking about before agreeing?

The assistant routes through the matrix and answers. You should see file paths cited and evidence-classification markers (`[V]`, `[AP]`, `[AR]`) on the deeper claims. If the answer reads like generic LLM prose with no file paths, the assistant has skipped the protocol.

Now ask the same question, but invoke the skill explicitly:

```
/answer-from-corpus Our finance team is recommending we sell the product line at a loss to clear inventory. What should I be thinking about before agreeing?
```

Watch what changes. The skill prints its work as it goes:

- **Step 0:** classifies the query shape. *Diagnostic* (a situation in a known task domain) vs *named lookup* vs *synthesis*. For this question, *diagnostic*.
- **Step 0.5:** lens-applicability check. Reads `lens-index.json` and decides whether any lens materially reshapes the answer. For most queries in the demo corpus: *no lens*.
- **Sub-claim decomposition.** Writes out the 3-6 sub-claims the answer needs to make, before reading any references.
- **Routing.** Reads `distillations/decision-making/task-index.json`, identifies the relevant phase (likely *evaluating-trade-offs* or similar), pulls the distillations that route to it, then reads the deep references for the authors whose argument is doing real work.

The default behaviour does this implicitly; the explicit invocation makes it inspectable. That's the value. When an answer feels thin or off, asking the same question via `/answer-from-corpus` forces the protocol and surfaces where retrieval went sideways.

## Step 2.5: Read the trace

Every `/answer-from-corpus` invocation ends with a one-line trace footer that names how the answer was retrieved. The trace is mandatory; without it, you can't tell whether the protocol ran or the model fell back to priors. Once you know how to read it, you can audit any answer in five seconds.

A typical trace for the question above looks like:

```
---
*Trace [Diagnostic, lens: none, corpus: demo, no-deep]:
decision-making/task-index → sub-claims: framing the loss
(openstax-OB), accounting treatment (openstax-accounting),
stakeholder dynamics (tomlinson-stakeholder-engagement), defensibility
(openstax-OB Ch 6) → Pass 3 deferred (distillation carries projected
citations; deliverable is artefact-shaped)*
```

The bracket carries six fields, in order, each load-bearing:

| Field | What it tells you |
|---|---|
| **Protocol** | `Named` / `Diagnostic` / `Synthesis`. Which retrieval shape the skill classified your question as. If you asked a named-lookup question and got `Synthesis`, the classifier missed; ask again more specifically. |
| **Regime** *(optional)* | `Citation-grade` / `Depth-over-breadth` / `Orientation`. Appears only when a non-default regime fired. Citation-grade means the deep references were re-validated for verbatim citation; Orientation means depth was deferred for a survey question. |
| **Lens** | `lens: <slug>` or `lens: none`. Which lens (if any) shaped salience. For most queries against the demo corpus, `lens: none`. |
| **Corpus** | `corpus: <slug>`. Which corpus was resolved-against. `corpus: demo` is the default in this tutorial. |
| **Deep-flag** | `deep` / `no-deep` / `partial`. Whether Pass 3 (deep-reference reading) fired. `no-deep` doesn't mean low-quality; it means the distillations carried the projected citations and re-reading the deeps would only thicken existing coverage. `partial` means deep reads were bounded by source-availability and the trace body names the gap. |

After the bracket, the trace narrates the actual route taken: which index was read first, which sub-claims the answer needed to make, which source addressed each sub-claim. The arrow chain (`task-index → sub-claims: … → Pass 3 …`) is the retrieval audit. You should be able to point at any non-trivial claim in the answer and find the source named in the trace.

**What to check on every answer:**

1. **Does the protocol match the question shape?** Named-lookup questions should classify as `Named`; in-task diagnostics should classify as `Diagnostic`; corpus-survey questions should classify as `Synthesis`. A mismatch means routing went sideways; ask again with sharper signal.
2. **Is `lens: none` correct?** For most demo queries, yes. If the trace says `lens: cto` and you weren't asking for a CTO-perspective answer, the lens-applicability check over-detected.
3. **Are the sub-claims complete?** The trace lists 3-10 sub-claims for Diagnostic and Synthesis protocols. If a sub-claim you'd expect is missing (you asked about decision-making *and* stakeholder dynamics; the trace shows only decision-making sources), the decomposition step missed a dimension.
4. **Are the cited sources the right ones?** The trace names sources by slug. If you can read `tomlinson-stakeholder-engagement` in the trace, the answer is grounded in Tomlinson's treatment; if you can't, no claim in the answer about stakeholder dynamics traces to him.
5. **Does the deep-flag match what the answer claims?** An answer that cites *verbatim* passages but has `no-deep` in the trace is internally inconsistent: the verbatim claim depends on a deep read that didn't happen. Either Pass 3 fires (`deep`) and the verbatim is defensible, or the verbatim shouldn't be there.

The trace is not decoration. It's the audit surface the architecture is shaped around: when an answer fails (wrong source, missing sub-claim, fabricated citation), the trace tells you exactly where in the protocol it failed. *Read the trace before reading the answer* once you have the muscle: the trace tells you whether to trust the prose above it.

### When the trace is missing

If an answer comes back with no trace footer, the assistant skipped the protocol. Possible causes:

- The skill wasn't invoked explicitly and the bundled CLAUDE.md isn't being honoured. Re-invoke with `/answer-from-corpus` to force.
- The deliverable is non-prose-shaped (a thread, a list of pull-quotes) and the trace is in the chat scaffolding *above* the deliverable, not below. Look up, not down.
- The user requested `essay only` or `no trace`. Rare; assume protocol ran but trace was suppressed by request.

The skill's discipline is that the trace is mandatory unless explicitly suppressed. A silently-missing trace is a signal, not an oversight.

## Step 3: Enumerate the corpus on a topic

You may not know what the corpus already covers on a topic. Asking the assistant *"what's in the library on X?"* sometimes works, but the discipline lives in `matching-references`:

```
/matching-references stakeholder conflict
```

The skill returns a structured list: each reference with its slug, paths to the light and deep references, and a one-line justification for why it matched. Output looks roughly like:

```
1. tomlinson-stakeholder-engagement
   light: references/tomlinson-stakeholder-engagement.md
   deep:  references/tomlinson-stakeholder-engagement-deep.md
   why:   Direct treatment of stakeholder identification and conflict cycles.

2. openstax-organizational-behavior
   light: references/openstax-organizational-behavior.md
   deep:  references/openstax-organizational-behavior-deep.md
   why:   Chapter 14 covers conflict management at team and inter-group level.

3. dekker-just-culture
   light: references/dekker-just-culture.md
   deep:  references/dekker-just-culture-deep.md
   why:   Conflict between accountability frames in post-incident review.

[…]
```

Try variations to feel the skill's reach:

```
/matching-references decision biases
/matching-references how teams handle disagreement
/matching-references Maslow's hierarchy of needs
```

Three different *shapes* of query: a topic, a situation, and a named concept. The skill routes them through different indexes:

- Topic and situation queries hit the **concept axis** (`concept-index.json`) and the **task-axis indexes** (`distillations/{task}/task-index.json`).
- Named-concept queries hit `concept-index.json` directly via alias lookup.
- Named-author or named-title queries hit the **corpus catalogue** (`reference-index.json`).

When `matching-references` returns nothing, that's a real signal: the corpus genuinely doesn't cover the topic. That's when you'd reach for the *scoping a source* tutorial: bringing new material in.

## Step 4: Audit a draft for under-attribution

The third query skill is `audit-attribution`. It's heavier than the other two: an essay-length check against the corpus, asking *which references in the library overlap closely enough with this draft's argument that they should be named in the attribution*.

The skill is calibrated for **synthesis writing**: blog posts, board papers, book chapters where the author is integrating multiple traditions and the build/contribute boundary may have blurred. Citation count is not the metric; the metric is whether a reader who knows the source bodies can tell what's being built on versus contributed.

Save a short draft to a file. If you don't have one, paste this example into `~/draft.md`:

```markdown
# On stakeholder ambiguity

Every project I've worked on has had stakeholders who weren't on the
named list. The customer-success lead who pulls the deal sideways at
quarter-end. The legal counsel who flags a contract clause three weeks
into integration. The director two levels up whose silence on the
weekly is itself a signal.

What I've come to think of as *stakeholder ambiguity* isn't a planning
failure. It's a feature of how organisations actually work: the formal
authority diagram and the actual influence graph are different graphs,
and the second is what determines whether a project lands.

The practitioner move is to ask, before each phase gate: who's not on
the named list whose position changed in the last two weeks? That
question routes more decisions than I'd care to admit.
```

Then invoke:

```
/audit-attribution ~/draft.md
```

The skill walks five steps: reads the draft, identifies its distinctive contributions, scans the corpus for closest neighbours, classifies the overlap (*safe synthesis* / *adjacent territory* / *under-attribution risk* / *demoted distinctive*), and recommends specific provenance fixes.

For a draft this short, the audit will likely surface `tomlinson-stakeholder-engagement` and (depending on phrasing) one or two organisational-behaviour sources. It might flag *"stakeholder ambiguity"* as a coinage that needs an explicit *"my term for"* marker, or recommend a footnote naming Tomlinson's identification protocol as the closest cited neighbour.

The skill is not a fact-check. It's a *build/contribute boundary check*: surfacing what a reader familiar with the corpus would notice you didn't name. The fix is rarely *"add citations"*: it's usually *"add one provenance sentence naming the closest neighbour and the distinction you're drawing."*

## What just happened

You used the three read-only skills in the substrate:

- **`answer-from-corpus`**: the runtime query protocol. Shape-classification (named lookup / diagnostic / synthesis), lens-applicability, sub-claim decomposition, routed reads. The same protocol the bundled CLAUDE.md instructs the assistant to run; invoking it explicitly makes the trace inspectable.
- **`matching-references`**: the topic-to-resource router. Tells you what's already in the corpus on a topic, before you reach for ingestion. The setup gate for `ingesting-resources` calls this skill explicitly to catch duplicates.
- **`audit-attribution`**: the under-attribution check for synthesis writing. Surfaces closest-neighbour references the draft may need to name.

These three are *consumption-side* skills. They don't change the corpus; they read against it. Every tutorial after this one is *production-side*: adding sources, adding task axes, adding lenses. The discipline of querying first is what makes the production discipline matter: if you don't know what's already in the library, you'll re-ingest material that's already there or under-attribute work you're building on.

## What's next

- **[Ingesting one source](ingesting-one-source.md)**: the 9-pass ingestion protocol against one source you bring yourself. The first production tutorial. ~60 minutes.
- **[`docs/architecture/two-layer-indexes.md`](../architecture/two-layer-indexes.md)**: why the corpus catalogue and the task-axis indexes do different jobs. Useful background once you've felt both via `matching-references`.
- **[`docs/architecture/llm-epistemology.md`](../architecture/llm-epistemology.md)**: the *why* behind the protocol's discipline. The matrix exists because LLMs are weak at exactly the moves the explicit `/answer-from-corpus` invocation forces.
