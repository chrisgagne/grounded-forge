# AGENTS.md — grounded-forge application

This is a compiled application: a corpus subset projected onto a task axis.
Claude Code reads `CLAUDE.md`; this file points any AGENTS.md-aware runtime
(Codex and others) at the same operating contract.

## Read first

1. **`CLAUDE.md`** in this directory — the operating contract for this app:
   what it is, what it ships, and how to retrieve. Read it in full before
   answering from the corpus.
2. **Skills** ship in two parallel layouts holding identical content:
   `.agents/skills/{skill}/SKILL.md` and `.claude/skills/{skill}/SKILL.md`.
   Invoke a skill natively where your runtime supports it; otherwise read its
   `SKILL.md` and follow it as a written procedure. The retrieval procedure is
   `answer-from-corpus`.

## Non-negotiable: Source Integrity

Ground every source-grounded claim in a passage carried by a distillation.
Distillations carry paraphrased prose with parenthetical attribution and
verbatim blockquotes with evidence markers (`[V]` / `[AP]` / `[AR]` / `[AE]`
/ `[BT]`) preserved in-band. If the distillation does not support a claim, say
so — do not supply it from training-data knowledge of the author. Cite the
distillation before stating the claim.

## What this app ships (dist-only)

- `distillations/{task}/` — the source-grounded product. Cite from these.
- Runtime JSON indexes at the app root (`concept-index.json`,
  `slug-table.json`, `lens-index.json`) and `distillations/{task}/task-index.json`.
  Read the indexes to route; never cite an index entry as if it were primary
  evidence.
- `lenses/` — per-distillation modifiers. Apply when a lens materially
  reweights what is salient.

The reference tier (light + deep) does not travel with this app; it lives at
corpus level as the audit-of-record. The verbatim passages and evidence
markers already in the distillations are what Pass D audited against the
source text — they are your citable provenance.
