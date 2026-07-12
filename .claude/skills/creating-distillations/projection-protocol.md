# The projection protocol

Rationale and detail for `creating-distillations`. The runbook is at [`SKILL.md`](SKILL.md); this document carries the *why* behind each step. Read both.

Covers Pass G of the 9-pass ingestion protocol, also reachable directly via `creating-distillations`. Orchestration is in [`creating-applications/SKILL.md`](../creating-applications/SKILL.md); upstream task scoping in [`creating-tasks/SKILL.md`](../creating-tasks/SKILL.md).

## A concrete example first

The OpenStax *Organizational Behavior* deep reference projects onto two task axes in the demo corpus. Open alongside the deep ref:

- Deep reference at [`corpus.commons/demo/references/openstax-organizational-behavior-deep.md`](../../../corpus.commons/demo/references/openstax-organizational-behavior-deep.md). Task-neutral; the source's argument with verbatim citations.
- Decision-making projection at [`corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md`](../../../corpus.commons/demo/distillations/decision-making/openstax-organizational-behavior-decision-making.md). Ch 6.4's process-vs-relationship-conflict distinction lands as a "what to look for" diagnostic pattern.
- Stakeholder-engagement projection at [`corpus.commons/demo/distillations/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md`](../../../corpus.commons/demo/distillations/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md). The same Ch 6.4 distinction lands as a phase-organised diagnostic question in the conflict-surfacing phase.

Same source, same concept, two projections shaped by the task. The discipline of *applicability before projection* is what stops it producing thin or strained projections for pairs that do not fit.

## Why projection at ingestion, not at query

The work of mapping source-vocabulary to task-vocabulary is paid once at ingestion and reused at every query, instead of being re-derived per query against context-window pressure. If the projection is generic, the runtime claim collapses: a generic projection is no better than letting the model reshape from the deep ref at query time. The discipline of this protocol is what makes the projection worth pre-paying. (Full argument in [`docs/architecture/projection-time.md`](../../../docs/architecture/projection-time.md).)

## Pass G.0: source-applicability gate

Before any projection, decide whether the source genuinely applies to the named task. This is a real decision, not pro-forma. Three outcomes:

- **Clear yes.** Proceed to projection.
- **Clear no.** Stop. Tell the operator the source doesn't apply, with the reason. No file is generated. Honour the skip: empty distillations in the matrix are honest, and a thin or forced projection degrades the distillation's usefulness more than absence does.
- **Ambiguous.** Present the case to the operator with a recommendation, and ask. The operator's call decides whether to proceed.

The applicability question is not "could the source say something about the task?": almost any general-knowledge source can be made to say something about almost any task. The question is: *does the source surface diagnostic questions a practitioner of this task actually asks, in a way that the deep ref's content can land on?* If a projection has to reach for tangential examples and force the source's vocabulary into the task's frame, the answer is no.

Three diagnostic questions for the operator (or for Claude when self-evaluating):

1. Does the source surface diagnostic questions a practitioner of this task would actually ask?
2. Are there phases of the task where the source's concepts naturally land?
3. Is the source's contrarian position relevant to the task, or orthogonal to it?

If two or three of those land *no* or *forced*, the source does not apply.

## Projection template

The distillation structure is uniform across the corpus. Every projection produces these sections, in this order:

- `## {Task} Relevance`: one or two paragraphs naming what the source brings to the task. Specific. Not "this source is about decision-making"; rather "this source's Ch 6 dual-system framing applies to decisions made under emotional pressure, where the operator needs to slow the reactive system".
- `## Key Concepts for {Task}`: a numbered list of 8-12 source concepts, each with a citation `(Source: Author, Title, Ch N, "Section name")`. These are the concepts the rest of the distillation uses; this section is the projection's working vocabulary.
- `## Questions to Ask During {Task}`: phase-organised tables. One table per phase. Three columns: Need, Question, (optional) Source-tag. The questions are the load-bearing artefact for runtime use; if a practitioner can read this section and immediately have better questions to ask in the room, the projection has worked.
- `## What to Look For`: patterns to notice in the work. Each pattern has Signal / Diagnosis / Follow-up sub-fields. This is the diagnostic catalogue the practitioner consults when something feels wrong but they can't name what.
- `## When to Use This Reference`: situational gates. When does the practitioner reach for this source rather than another in the corpus that also applies?
- `## Worked Example`: source-grounded. A short worked example showing the reference applied to a realistic scenario. The scenario itself is operator-authored, but each substantive claim about how the source's framing applies must cite the source by chapter and section. **When the source's own words carry a claim the example turns on, include the verbatim passage as a blockquote with its evidence marker — copy it from the deep ref's audited `[V]` block; do not re-extract from the source.** The discipline: the example is yours, the framework citations within it trace through pass-D-audited verbatim passages.
- `## Anti-patterns This Reference Helps Avoid`: failure modes the source's framing helps the practitioner notice and avoid.
- `## Integration with Other References`: a table linking this source to other applicable references in the corpus, naming the relationship (combine with X for Y; this source extends X's framing on Z).
- `## Citation and Source-Integrity Notes`: explicit audit-trail tail. Three sub-elements: (1) **Borrowed-through gaps**, authors the source cites by name but who are not held directly in this corpus (e.g. *Goldratt cited via Open Kanban; Theory of Constraints not held as a primary reference*). Names them so a reader knows the chain. (2) **Named limits of the source**, what the source explicitly does not cover, scope boundaries the author flags, terminology the author defines narrowly. (3) **Evidence-marker continuity**, confirms the distillation's citations preserve the deep ref's `[V]` / `[AP]` / `[AR]` / `[AE]` / `[BT]` markers where they matter; flags any place the distillation paraphrases what the deep ref carries as verbatim, with reasoning.

The structure is uniform so that downstream consumers (the runtime assistant, sibling distillations cross-referencing this one, future operators reading the file) know where to look. Don't deviate from the section headings; don't add new sections; don't reorder.

When the task spec carries field 2a (a runtime listener grain), two additional sections appear at the end of the distillation: see "Trigger-grain projection" below. These are appended after the standard nine, not interleaved into them.

## Trigger-grain projection (when the task spec carries field 2a)

The standard template answers *what does this source bring to this task?*: the macro-projection. It is not enough to fire the source at runtime when a specific moment calls for a specific framework.

Field 2a carries a seed table of trigger→response pairs, per phase. The trigger is what the practitioner *observes in the room*; the response is the framework + teach-in-the-moment script. Pass G's job, when 2a is present, is to map *this source's content* onto *these triggers*.

Two new sections in the distillation:

- `## Runtime triggers this source addresses`: table with three columns: *Trigger* (lifted verbatim from field 2a so listener-table rows match across distillations); *Content from this source that addresses it* (specific concept, chapter, citation); *Teach-in-the-moment script* (1-3 sentences the practitioner can say or do, grounded in the source's framing).
- `## Trigger extensions surfaced by this source`: optional. Triggers the source clearly addresses that the seed table didn't anticipate. The operator folds these back into the task spec to grow the seed table; logging extensions here rather than silently extending the index keeps the task spec canonical.

Without trigger-grain projection, Pass G produces shelf material: distillations that *could* fire if the practitioner remembered to read them in the moment but won't, because no listener is watching for the trigger. With it, the distillations *are* the runtime listener.

**When the task spec does NOT carry field 2a.** Lens-neutral 2D axes produce the standard nine-section distillation; the two trigger-grain sections do not appear. Back-filling triggers onto an older axis is an operator move (re-run `creating-tasks`, add field 2a, then re-run `creating-distillations`), not an automatic Pass G inference.

**Trigger-mismatch flag.** If Pass G fires *clear yes* on source-applicability but the source addresses *zero* triggers in the seed table, flag this in the distillation's header. The distillation exists, the macro-router will fire it, the micro-router will not. Sometimes correct (the source's contribution is situation-type level, not in-moment); sometimes a signal the seed table is incomplete and the source's extensions should grow it.

## Citation discipline

Distillations carry the source's claims in two registers: **paraphrased** prose with parenthetical attribution, and (where the source's licence allows redistribution) **verbatim** blockquotes with evidence markers (`[V]` / `[AP]` / `[AR]` / `[AE]` / `[BT]`) for the load-bearing passages the projection turns on.

The verbatim register is not re-extracted from the source — it is **copied from the deep reference's already-audited Pass D blockquotes**. Pass D ran the exactness verification against the source text once, at deep-ref construction. Pass G copies those audited passages into the distillation; the marker travels with the quote. Re-extracting from the source at Pass G reopens the failure modes Pass D closed (silent drift, evidence-marker confusion). The flow is one-way: source → Pass D → deep ref → Pass G copy → distillation. Apps ship distillations only; the deep ref remains in the corpus as the audit-of-record but does not travel with the compiled application.

### Scope gates the verbatim register

The deep ref's `Scope:` frontmatter decides whether Pass G writes verbatim quotes into the distillation:

- **`Scope: open` or `Scope: open-nc`**: write 2-5 verbatim blockquotes per distillation with `[V]` (or other) markers, copied from the deep ref's Pass-D-audited passages. The source's licence permits redistribution; the app ships the quotes.
- **`Scope: copyrighted`, `Scope: confidential`, or `Scope: personal`**: **no verbatim quotes in the distillation.** Paraphrased prose with parenthetical attribution only. Mark the load-bearing claims with `[AP]` (author paraphrase) so the citation register stays visible without redistributing the protected text. The deep ref still carries the audited `[V]` passages at corpus level for audit; the app does not.

The rule tracks the distribution contract, not the audit chain. Pass D's exactness audit runs against every source regardless of scope; what changes at Pass G is *what travels with the compiled application*. The build refuses to ship a distillation that carries `[V]` blockquotes from a copyrighted+ source — this is enforcement, not just style.

**When to fire the verbatim register (open sources only).** A load-bearing claim is one where the source's exact phrasing matters: a definition the author coined, a principle stated as such, a statistic, a named pattern, an inflection sentence. Roughly two to five verbatim blockquotes per distillation; more becomes a deep ref masquerading as a distillation. When in doubt, paraphrase with attribution and let the deep ref carry the verbatim.

Cite paraphrased concepts inline with parenthetical attribution: `(Source: Author, Title, Ch N, "Section name")`. The distillation's claims must trace to the deep reference, which traces to the source. Smuggling new claims into the distillation (concepts that aren't in the deep) re-opens the failure modes the source-only audit was designed to close.

## Concept anchors

Each numbered entry in `## Key Concepts for {Task}` carries an **anchor**: a short slug placed at the start of the line as a comment-style marker, e.g. `<!-- concept: phronesis -->`. The build's concept-index rebuilder reads these anchors and produces per-source `{section, dist_line}` pointers that route the runtime from a concept name directly into the distillation. Without anchors, the concept-index falls back to naming the source only (no in-source landing point).

Anchor slugs match the concept-index's top-level keys where the concept already exists (run `grep -l "^  \"{slug}\":" corpus.commons/{corpus}/concept-index.json` to find the canonical slug). When a concept new to the corpus appears in this distillation, coin a kebab-case slug and let the index-builder add it on the next rebuild.

The discipline is light: anchor the concepts most likely to be the entry point for a runtime concept lookup. Anchors on the worked-example concepts in particular pay off — those are the ones a practitioner will look up by name.

## Lens-as-optional-framing

Lenses are windows with characteristic salience, weighting, and vocabulary. Two lenses can reach for the same (source, task) distillation but find different things salient.

Lens specs live at `corpus.commons/{corpus}/lenses/{lens-slug}.md`, produced by `creating-lenses`. If a lens is named but has no spec, run `creating-lenses` first.

The matrix is 2D by default. Lens pre-projection is *opt-in per distillation*. For each named lens, evaluate the (source, task, lens) triple and choose one of four outcomes:

- **Clear no.** Lens does not materially reweight what's salient for this distillation. No additional artefact. Logged as lens-skip.
- **Clear yes, partial reshape.** Lens reweights a subset of the diagnostic questions (perhaps 2-4 of 12-15 across phases). Add a `## Through the {lens-name} lens` section inside the existing distillation: reweighted questions, the lens's native vocabulary, salience-and-recedes notes specific to this distillation.
- **Clear yes, deep reshape.** Lens materially reweights most of the distillation. Project a separate per-lens distillation at `{slug}-{task}-{lens-name}.md` with the full template structure written through the lens. It does *not* duplicate the lens-neutral file with light edits; if it would, the right outcome was *partial reshape*.
- **Ambiguous.** Surface to the operator with a recommendation.

Default is *do nothing*. Empty (source, task, lens) distillations are honest: they say *this lens does not change what matters for this distillation*.

### Retrieval-time fallback

When a query specifies a lens and no pre-projected distillation or section exists, the retrieval layer reads the lens-neutral distillation and applies the lens at query time. The lens file (salience, recedes, native vocabulary, characteristic weightings) is small; this is cheap. The fallback is what makes the *clear no* outcome safe: even with no pre-projection, the lens still shapes the answer.

## Cycling: projection sometimes sharpens the deep

Projection is not unidirectional. When a projection reveals a gap in the deep reference (a glossed-over concept, a wrong evidence marker, a missing connection), update the deep reference and re-project. Do not paper over the gap in the distillation.

## Failure modes

- **Skipping the source-applicability gate.** Generating a distillation for a (source, task) pair where the source doesn't actually fit produces a file that strains to find diagnostic questions, reaches for cross-references, and reads as filler. The signal: the projection's "Key Concepts" list is light, the phase-organised tables have questions that could come from any source, the worked example feels generic. Better to return a clear *no, this source does not apply* and record the skip in the run summary.
- **Skipping the lens-applicability gate.** Pre-projecting against every named lens by default inflates the corpus with thin lens-shaped variations of the same content. The default for lenses is *do nothing*; pre-project only where Claude judges the lens materially reweights the distillation.
- **Re-extracting verbatim from the source at Pass G.** The verbatim register in distillations is a *copy* of already-audited Pass D blockquotes, not a fresh extraction. Pass D ran the exactness audit against the source once at deep-ref construction; Pass G copies those passages with their evidence markers intact. Re-extracting from the source reopens the failure modes Pass D closed.
- **Verbatim from a copyrighted, confidential, or personal source.** Pass G's verbatim register is open-licence-only. When the deep ref's `Scope:` is `copyrighted`, `confidential`, or `personal`, the distillation carries paraphrased prose with `[AP]` markers and parenthetical citation — never `[V]` blockquotes. The deep ref still carries the audited verbatim at corpus level; the app does not. The build refuses to ship distillations that violate this gate, so the failure surfaces at compile time rather than at distribution.
- **Smuggling new claims.** If a concept is not in the deep reference, it does not belong in the distillation. Re-ingest if the concept warrants inclusion; do not assert it in the projection without auditable backing.
- **Generic projection.** The distillation should reshape the source for the task. If a reader could swap the task name throughout and the file would still make sense, the projection has not done its work. The signal: the diagnostic questions don't use the task's working vocabulary, the worked example doesn't engage the task's typical conditions, the anti-patterns are generic critical-thinking failures rather than task-specific traps.
- **Anti-patterns without signal/diagnosis/follow-up.** A bullet list of "things to avoid" without the diagnostic shape (signal → diagnosis → follow-up) is a hand-wave. The What-to-Look-For and Anti-patterns sections are runtime tools; they need to be useful when the practitioner is in the middle of the work.
- **Integration table as stub.** "Combine with [other source] for [topic]" without naming the relationship is filler. The integration section should make the cross-corpus structure visible: this source extends X's framing on Y; this source contradicts Z's claim on W; this source plus X together cover what neither covers alone.
- **Mismatched task vocabulary.** The distillation's working vocabulary should be the task's own: *decisions* for decision-making, *stakeholders* for stakeholder-engagement, *risk events* for risk-assessment if that's the new axis. Source-author vocabulary is preserved in the deep reference; task-applied vocabulary lives in the distillations.
- **Re-reading the source during projection.** Distillation projection is from the verified deep, not from the source. Re-reading the source reintroduces the failure modes the deep ref has already audited out (training-prior leakage, drift away from cited material, evidence-marker confusion).

## Architectural note

Distillations are the distillations; this protocol is what produces a distillation. The matrix stays 2D by default; 3D extension happens distillation by distillation via the lens-applicability gate above. The default for any (source, task, lens) triple is *no additional artefact*. See [`docs/architecture/matrix-pattern.md`](../../../docs/architecture/matrix-pattern.md).
