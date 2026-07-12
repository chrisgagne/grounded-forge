# The demo app

A walk through the matrix architecture using the apps that ship pre-built in the repo. No `npm install`, no build, no ingestion. Just open Claude Code and ask. Budget 20-30 minutes wall-clock including two Claude Code sessions; about 10 of those minutes is reading.

By the end you will have:

1. Opened the decision app in Claude Code.
2. Asked it a question and seen the matrix route through index → distillation → deep reference.
3. Opened the stakeholder app and asked the *same* question, and watched the answer change.

That last step is the architecture in one move. Once you've felt it, the rest of the docs make sense.

## What you need

- Claude Code installed.

That's it. The apps ship pre-built and tracked in the repo, so cloning is enough to use them.

## Step 1: Clone the repo (if you haven't)

```bash
git clone https://github.com/chrisgagne/grounded-forge.git
cd grounded-forge
```

The five demo apps are already built at `corpus.commons/demo/apps/`:

```
corpus.commons/demo/apps/
├── decision/
├── stakeholder/
├── software-business/
├── aar-mode/
└── retro-mode/
```

Each is a self-contained Claude Code project: a `CLAUDE.md`, a `references/` folder with all 26 light + deep references, a task-specific `distillations/` folder, a `lenses/` folder, and bundled skills under `.claude/skills/`. The two ceremony apps (`aar-mode`, `retro-mode`) also ship a corpus-bound runtime agent under `.claude/agents/`.

## Step 2: Open the decision app in Claude Code

```bash
cd corpus.commons/demo/apps/decision
claude .
```

You're now in a Claude Code session whose context is *the app*, not the source repo. The session sees the references, the distillations, the lenses, the skills, and the CLAUDE.md that tells it how to behave.

## Step 3: Ask it a decision question

In the session:

> I'm choosing between two technical co-founders for my software startup. One has deeper engineering skill; the other has stronger commercial instincts. How should I think through this decision?

What you should see (it may take a moment):

1. The assistant reads `distillations/decision-making/task-index.json` (the situation router) along with the corpus-level `reference-index.json` and `concept-index.json`.
2. It identifies which distillations apply (likely a combination of decision-frameworks sources, organisational-behaviour sources on team composition, possibly the facilitation guide if it routes that way).
3. It reads the relevant distillation file(s), the pre-projected guidance for decision-making work.
4. When it cites, it cites from the *deep* reference (`{slug}-deep.md`), carrying evidence-classification markers like `[V]` (verbatim), `[AP]` (author paraphrase), `[AR]` (author argument).

If the answer is grounded (claims trace to files, citations are inline, the assistant says "I don't have coverage on X" when the corpus doesn't reach), the chain is working.

If the answer reads like generic LLM output with no file paths, the assistant has bypassed the protocol. Ask it to re-do the question using the `answer-from-corpus` skill: *"Please use the answer-from-corpus skill for this question."* That invokes the protocol explicitly.

## Step 4: Ask the same question of the stakeholder app

Exit the session (`Ctrl-D`) and open the stakeholder app:

```bash
cd ../stakeholder
claude .
```

Ask the **same** question:

> I'm choosing between two technical co-founders for my software startup. One has deeper engineering skill; the other has stronger commercial instincts. How should I think through this decision?

Watch what changes.

The decision app frames the question as *how do I make a defensible decision*, with cognitive biases, decision frameworks, and evaluation criteria.

The stakeholder app frames the same question as *how does the co-founder relationship play out with everyone else*: the engagement dynamics with investors, the team you're hiring, customers, the board you'll eventually have.

Same corpus, same question, different task projection. That difference is what the matrix produces. The references are identical; the distillations differ; the CLAUDE.md differs. Each app has been pre-shaped for its task domain.

![A wide-eyed baby tasting ice cream for the first time, eyes huge with surprise, mid-bite. A parent's smile in the corner of the frame.](../assets/happy-baby.png)

*That feeling? That's the architecture, working. Now you have a reference point for the rest of the docs.*

## Step 5: Ask something the corpus handles well

The demo corpus is a 28-source library covering organisational behaviour, management, motivation, decision frameworks, stakeholder conflict, ethics, marketing, finance, accounting, business law, psychology, economics, systems-thinking foundations, strategic org design (Org Topologies), military doctrine on command under uncertainty (MCDP 1 Warfighting), and a small software-business slice.

Try one of these in the decision app:

> Our team is split on whether to ship the breaking change now or wait for the next quarter. How should we work through this?

> I'm hiring a senior engineer. What should I be paying attention to that I might be missing?

> My finance team is recommending an investment I don't fully understand. How do I think about it?

Watch what gets cited. The matrix's job is to surface the *right* reference at the right point in the question, with the *right* projection for the task you're doing.

## Step 6: Ask something the corpus doesn't handle

Try:

> What's the right Kubernetes architecture for a 50-engineer team?

The honest answer is *the corpus doesn't cover this*. A well-behaved app says so, rather than fabricating an answer. If your run of this question produces a confident architectural recommendation, the protocol isn't being honoured. See [`../architecture/source-integrity.md`](../architecture/source-integrity.md) for why the discipline matters.

The demo corpus does well with cross-functional decisions, stakeholder dynamics, organisational behaviour patterns, and general business reasoning. It does poorly with specialised technical domains, regulated work (medicine, law), fast-moving fields (current events, recent product releases), and anything where you'd need a non-public source.

That gap is what the next tutorial begins to close.

## What just happened

You exercised the matrix architecture end-to-end without writing or building anything:

- **Pre-built:** the five demo apps ship in the repo; no build step needed to use them.
- **Routing:** each app's CLAUDE.md instructs the assistant to read the runtime JSON indexes first (the corpus-level `reference-index.json` and `concept-index.json`, plus the per-task `task-index.json`).
- **Projection:** the same reference reads differently in the decision app and the stakeholder app, because each shipped a different pre-projection.
- **Citation:** answers trace to deep references with evidence-classification markers, not to training priors.

The architecture's claim is that this is *cheaper, more honest, and more scalable* than asking the model to re-derive task-specific guidance from raw sources on every query. For the argument, read [`../architecture/projection-time.md`](../architecture/projection-time.md).

## What's next

- **Strongly recommended: [Querying the library](querying-the-library.md)**: the three read-only skills (`answer-from-corpus`, `matching-references`, `audit-attribution`). Still no cost; still no build. Teaches you to drive the matrix deliberately rather than trusting defaults. ~30 minutes.
- **[Ingesting one source](ingesting-one-source.md)**: the 9-pass ingestion protocol against one source you bring. The matrix expands by one row. ~60 minutes.
- **[Scoping a source](scoping-a-source.md)** / **[Adding a task axis](adding-a-task-axis.md)** / **[Adding a lens](adding-a-lens.md)**: the incremental skill walkthroughs. Each takes 20-90 minutes.
- **[Scaffolding a corpus](scaffolding-a-corpus.md)**: the full forker arc, when you're ready to leave the demo.
- **[Architecture overview](../architecture/overview.md)**: the one-page explanation of *what* the matrix is and *why* it works.
