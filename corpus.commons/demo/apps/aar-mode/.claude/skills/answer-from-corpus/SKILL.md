---
name: answer-from-corpus
description: Source-grounded answer to a question via shape-aware retrieval against the dist-only corpus: classifies the query as a named lookup, a diagnostic, or a synthesis, then runs the right protocol (direct route via slug, task-index → distillations, or three-pass index → distillations). Stops on sub-claim coverage, not on counts.
argument-hint: "<question or topic>"
---

# Answer from corpus

Source-grounded answer protocol for any substantive question the corpus may cover. Distillations are the source-grounded product: each carries paraphrased prose with parenthetical attribution and verbatim blockquotes copied from already-audited Pass D passages, with evidence markers (`[V]` / `[AP]` / `[AR]` / `[AE]` / `[BT]`) preserved. The reference tier (light + deep) stays at corpus level as the audit-of-record but does not travel with the compiled app; this skill reads distillations only.

Invoke this skill to *operationalise* the bundled CLAUDE.md's grounding directive: CLAUDE.md sets the principle (search before reasoning from priors; cite or admit guessing), this protocol runs it as executable steps — shape-classification, traceability, citation density, corpus breadth.

## Procedure

**Path convention.** Every path in this skill is written from the app's perspective: `./distillations/{task}/`, `./concept-index.json`, `./lens-index.json`, `./slug-table.json`. The distillations directory and the runtime JSON indexes sit at the app root.

**`--corpus {slug}` flag.** When the operator passes `--corpus my-corpus` in the invocation (e.g., `/answer-from-corpus --corpus demo What is a definition of done?`), the skill targets that named corpus's bundled artefacts. Default: the only corpus the app ships.

### Step 0: Classify the query shape

Before any reads, classify the question:

- **Named lookup.** The user names a specific framework, author, work, or concept ("what does TC 25-20 say about the AAR cycle", "tell me about Dekker's Just Culture as treated in the corpus"). Signal: the answer reduces to *what does this one source say*. → **Protocol N.**
- **Diagnostic.** The user describes a situation that needs reference-mediated guidance ("how do I handle a stakeholder conflict", "I need to make a decision under uncertainty"). Signal: there's a task domain in play, and the corpus has distillations for it. → **Protocol D.**
- **Synthesis.** The user asks what the corpus says about a broad topic ("what is Agile", "what does the corpus say about employee motivation"). Signal: the answer benefits from breadth across multiple authors/traditions and the question is not a named lookup or in-task diagnostic. → **Protocol S.**

When ambiguous, default to the more expansive protocol (S over N, D over N). Never ask the user to disambiguate unless genuinely unclear.

### Step 0.5: Lens-applicability check

After classifying the query and before any reads, check whether a lens materially reweights what's salient for this query.

**Skip this step for Protocol N.** Named lookups answer *what does this one source say*; a lens would distort, not clarify.

**For Protocols D and S:**

1. **Read `./lens-index.json` unconditionally.** The lens index is a small curated runtime artefact (one entry per lens under `lenses.{slug}`). Each entry carries `kind`, `spec_path`, `purpose`, `reach_for_when`, and a structured `salience` block (`notices_first`, `recedes`, `native_vocabulary`). Read it the way the task-axis indexes are read: as a map, not a search target. Always read it for Protocols D and S.
2. **Detect the lens-shaped signal.** The deliverable is lens-shaped when it asks for role-specific guidance, a perspective-bound read, an artefact aimed at a named reader-type, a query asking for a named person's voice or framings, an AAR/retro write-up where reader-role is load-bearing, a coaching brief, or process documentation where role-and-circumstance is the unit of analysis. If the query is lens-neutral, no lens applies and the rest of the protocol runs unmodified.
3. **Name the lens(es) the index surfaces** and confirm with the operator before proceeding when more than one lens could apply. When exactly one lens fits unambiguously, name it in the trace and proceed.
4. **The index entry is usually sufficient**; the `salience` block carries enough of the lens's vocabulary to apply at retrieval time. **Read the full spec** at `lenses.{slug}.spec_path` only when the query needs the lens's grounding contract, fire-list, or trust-breaking-failure-mode reasoning.
5. **At retrieval, prefer a pre-projected (source, task, lens) distillation when one exists.** Otherwise apply the lens at query time via the index entry's `salience` block.

The trace footer names the lens used (or "no lens" when the deliverable was lens-neutral).

**Step 0.5 runs *before* sub-claim decomposition.** The lens shapes what the sub-claims should be: a CTO-lens memo and a builder-lens runbook decompose the same source question into different sub-claim lists.

### Sub-claim decomposition (Protocols D and S)

For Protocols D and S, *before* reading distillations, decompose the question into the 3-10 sub-claims the answer will need to make. Write the sub-claim list out explicitly. Examples:

- "What is Agile?" → origin/motivation; key principles; methodology family; common failure modes; critique/limits; evolution post-Agile.
- "How do I handle a stakeholder conflict?" → identify positions vs interests; surface the conflict safely; structure the conversation; close to commitment.

The sub-claim list is the coverage map for retrieval. Stop reading when every sub-claim has at least one strong source AND the next read would only thicken existing coverage.

Skip decomposition for Protocol N: a named lookup has one sub-claim by construction.

### Protocol N: Named lookup

1. **Resolve the source slug.** Read `./slug-table.json` (`{schema_version, corpus, generated, next_id, slugs}`; `id → slug` under `slugs`). When the user names an author or title, scan the slugs for a match. If the user names a concept and not a specific source, read `./concept-index.json` (entries under top-level `concepts` with `{name, aliases, sources}`) and route from concept → sources.
2. **Read the relevant distillation(s).** For the slug + the user's task domain (if applicable), open `./distillations/{task}/{slug}-{task}.md`. Distillations carry author attribution in the first paragraph, paraphrased claims with parenthetical citations, and verbatim blockquotes with evidence markers (`[V]` / `[AP]` / `[AR]` / `[AE]` / `[BT]`) for the load-bearing passages. The distillation is what you cite from.
3. **Stop.** No triage, no breadth sweep.

When the named source is referenced in the corpus but no distillation projects onto the user's task, surface that gap: *"The corpus has [source] but no distillation projects it onto [task]; here's what the closest task projection says."*

### Protocol D: Diagnostic

1. **Decompose the question** into 3-6 sub-claims (see above).
2. **Read the precondition gate.** Load three files: the task-axis index at `./distillations/{task}/task-index.json`, the slug-table at `./slug-table.json`, and the concept axis at `./concept-index.json`. Read each whole-file in one pass (paginate with successive `offset/limit` Read calls if any file exceeds the cap).

   The task-axis index partitions the task into named phases (each a `section`) and lists which sources apply (`rows` as `[need, slug-id, when]` triples). The slug-table resolves slug-IDs to distillation file paths: `./distillations/{task}/{slug}-{task}.md`. The concept-index does concept routing — task-index rows carry slug-IDs but not concept pointers, so the concept-index is what lets you land on a named concept inside the source the task-index named.

   **Stub-or-empty-task-index escape clause.** If `task-index.json` is a stub (`sections: []` or `generated_from: "stub-*"`), the task-axis projection has not been authored yet. In that case the corpus-level concept axis is doing all the routing work; proceed to step 3 using concept-index to identify candidate sources.

3. **Identify the relevant phase or situation** for the question.
4. **Read every distillation the index surfaces** for that phase/situation (typically 2-5). Distillations at `./distillations/{task}/{slug}-{task}.md` are pre-projected for exactly this shape; trust the projection. Each distillation already carries verbatim citations + evidence markers in-band for the load-bearing claims — that is the citation tier in dist-only retrieval.
5. **Tag each distillation against the sub-claim list.** Stop when every sub-claim has at least one strong source AND the next distillation would only restate.

### Protocol S: Synthesis

Three explicit passes:

**Pass 1: Routing.** Decompose the question into 5-10 sub-claims. Then route via the runtime JSON indexes:

- `./slug-table.json`: slug ↔ ID mapping; load once per session.
- `./concept-index.json`: concept axis with aliases and per-source pointers (entries under top-level `concepts`). Schema: every source entry carries `{id}` and most carry `{context}`. The in-source `(section, md_line)` pair that exists in the corpus-level index is stripped at build time for apps — distillations are full-read at Pass 2, so the pointer is unnecessary at app runtime.
- `./distillations/{task}/task-index.json` per task domain in play.

**Cap-aware surfaces.** Some runtime artefacts may exceed the Read tool's 25k single-call cap. For all JSON indexes, read the whole object: if a single Read returns the entire file, you're done; if it exceeds the cap, paginate with successive `offset/limit` Read calls until EOF. Never use `grep` or `python3 -c '... json.load ...'` against a JSON index to extract a single key in lieu of reading the file. Distillation files are small (typically 8-15KB each) and always fit in one Read.

**EOF-successive-reads pattern (apply whenever an artefact exceeds the cap):**

```
Read(file, offset=0,   limit=400)
Read(file, offset=400, limit=400)
Read(file, offset=800, limit=400)
... continue until a Read returns fewer lines than `limit` (that's the EOF signal).
```

Result: a candidate set of slug-IDs (author + title resolved from the first paragraph of each distillation; concept-axis sources from `concept-index.json`; task-bound rows from `task-index.json`). No file reads beyond the indexes in this pass.

**Pass 2: Distillation read.** Read the distillation for every candidate above the relevance floor, with diversity-aware deduplication (don't read three OpenStax distillations on related topics if one carries the load; spread across distinct authors and traditions). For each distillation, tag which sub-claim(s) it addresses.

Stopping rule is *triangulation*, not just coverage. Continue until every sub-claim has at least two sources you'd cite, AND you've identified at least one place where authors converge and one place where they disagree or emphasise differently.

**Pass 3: Citation density.** Distillations already carry verbatim blockquotes with evidence markers for the load-bearing passages — that *is* Pass 3 in dist-only retrieval. The verbatim register fired in the distillation at Pass G; what's in the distillation is already audit-of-record material (copied from Pass D's audited blockquotes in the deep ref). Pull the verbatim quotes from the distillation directly when the deliverable needs them; do not re-extract from anywhere else.

When a distillation lacks the in-band verbatim register (older distillations produced before the Pass G schema change), surface that in the trace: *"distillation carries paraphrased citations only; older Pass G schema."* Do not invent verbatim quotes.

Pick the regime by deliverable signal:

| Regime | Triggering signals | Pass 3 behaviour |
|---|---|---|
| **Citation-grade** | Regulated/scholarly/audit/disputed context; explicit "with citations"; defensibility-critical (legal review, manager pushback); user has named an author and expects rigour | Surface every in-band verbatim quote + evidence marker the distillation carries for the load-bearing claims. |
| **Depth-over-breadth** | Operator-bound action ("what should I do"); mechanism question ("how does X work"); disagreement adjudication; thesis-bearing prose under any length; anti-pattern detection | 2-4 load-bearing distillations read thoroughly; surface verbatim quotes where they sharpen the claim. |
| **Orientation** | Library-survey question ("what's in the corpus on X"); definition or one-liner; time-critical (live session); non-expert audience | Paraphrased citations sufficient; surface verbatim only when the user signals enumeration or rigour. |

**Default to Depth-over-breadth when in doubt.**

### Image-axis discovery (when `--with-images` is passed)

If the app's corpus ships `./sources/converted/IMAGE-INDEX.yaml` (apps do not ship sources by default; this fires only when the corpus operator opted to bundle the image library), grep by source_ref for each cited slug. If the index isn't shipped, name that in the trace footer (`image-axis: not bundled in app`).

### Token budget posture

Stay inside the context window with comfortable headroom for the answer-writing step (~200k tokens reserved). Distillations are small, so Pass 2 is cheap; a 50-distillation read still fits comfortably.

### Write the answer

Write in the form the user asked for (essay, list, table, etc.). **Match the citation style to the form.**

- **Prose deliverables** (essay, memo, briefing, one-pager): cite by author and work in the prose itself (e.g., "Larman argues…", "the OpenStax OB chapter on conflict frames it as…"). Surface evidence markers (`[V]` verbatim, `[AP]` author paraphrase, `[AR]` author argument, `[AE]` author example, `[BT]` borrowed-through) where they sharpen a claim. Do not put relative file paths inline.
- **Technical or operator-facing deliverables** (code, config, runbook, internal note where the operator wants to inspect the trace): cite by relative file path inline.
- When in doubt, default to the prose-cite style.

### No-coverage and partial coverage

**Full no-coverage.** If the corpus does not cover the question (the indexes have no relevant entries, the candidate distillations don't apply) say so plainly. Do not fall back to training to fabricate a confident answer. *"The corpus does not cover this; here's why, and here's what's adjacent that might help"* is a valid response. *Adjacent* covers two distinct moves: (a) **adjacent corpus material**: sources already in the corpus that touch the topic obliquely, with the obliqueness named; (b) **external-ingestion candidates**: named authors or works the operator could ingest to extend the corpus. The second is licensed only as ingestion candidates, not citable claims — phrase as *"Beck's Extreme Programming Explained would be a candidate ingestion"*, not as *"Beck argues that..."*.

**Partial coverage** is the more common case. Where the acknowledgement lands depends on deliverable shape:

- **Artefact-shaped deliverables** (process documents, RACI matrices, templates, runbooks, AAR/retro write-ups, briefs, memos written *as the thing itself*): the corpus-gap note goes in the trace footer, not the deliverable.
- **Thesis-bearing prose with stated rigour** (essay with citations, briefing where defensibility is load-bearing, scholarly or audit context): surface the boundary in the prose itself, one sentence, in the lede or a closing turn.

**Lens-as-sole-grounded-source pattern.** Real-person and role-bound lens specs sometimes cite primary sources that are not in the corpus. When the matrix axes carry no relevant material for the query *but* the lens spec carries the framings the query asks for, the lens spec serves as the citable reference for this run. Trace footer shape: `*Trace [Synthesis, lens: chris-gagne-consultant-coach, partial-matrix-coverage]: lens-index → spec read in full via spec_path; matrix axes carry no relevant material → answer grounded in lens spec citations*`.

### Append a trace footer

After the answer, append a one-line footer naming the protocol used and (for Protocols D and S) the sub-claim → source mapping.

**Bracket-tag schema.** The leading bracket carries: protocol tag (Named / Diagnostic / Synthesis), regime tag if a non-default regime fired (Citation-grade / Depth-over-breadth / Orientation), lens tag (`lens: <slug>` or `lens: none`), `corpus: <slug>`, the image-flag (`with-images` when `--with-images` was passed), and any architectural-coverage qualifier (`partial-matrix-coverage`).

Examples in increasing complexity:

```
---
*Trace [Named, lens: none, corpus: demo]: slug-table → openstax-organizational-behavior → distillations/decision-making/openstax-organizational-behavior-decision-making.md*
```

```
---
*Trace [Diagnostic, lens: cto, corpus: demo]: stakeholder-engagement/task-index → sub-claims: identify positions/interests (openstax-OB), surface conflict safely (openstax-OB), structure conversation (liberating-structures), close to commitment (lfuo) → lens applied retrieval-time via cto.md salience-and-vocabulary*
```

```
---
*Trace [Synthesis, Depth-over-breadth, lens: none, corpus: demo]: Pass 1 (decision-making/task-index + stakeholder-engagement/task-index + concept-index) → sub-claims: framing (openstax-OB), method choice (barbrook-johnson), facilitation (liberating-structures), post-event (tc-25-20, lfuo) → Pass 2 (5 distillations read) → verbatim markers surfaced from in-band citations*
```

The trace is mandatory unless the user explicitly requests "no trace" or "essay only".

**Non-prose deliverable shapes** (a list of N pull-quotes, a thread, a single-line position, *"three sentences each, no synthesis"*) compress the trace to a one-line bracket-tag annotation in the chat scaffolding *above* the deliverable, not below it.

## Discipline

- **Refuse to include any non-trivial claim** that does not trace to a distillation you read. Author and work in prose is enough for the reader; the file path lives in your working memory and your willingness to defend the claim if challenged. If you find yourself reaching for a confident assertion you can't trace, either find the distillation that supports it or remove the assertion.
- **Honour the form the user asked for.** When the user names a length or form ("500-word essay", "one-pager", "brief", "memo"), treat it as a hard constraint.
- **Length-target tolerance: ±30%.** Inside the band: ship. Outside on the high side: cut. Outside on the low side: deepen with the next-most-relevant distillation or honestly cap the response.
- **Sub-claim coverage, not file count.** Stop when every sub-claim has at least one strong source AND additional reads would thicken rather than extend coverage.
- **Subagent dispatch is off by default; opt in with `--dispatch`.** In an interactive session against a single corpus, parallel subagents add round-trips without buying breadth.

## Inputs

- A question or topic in plain language. The skill detects shape and task domain from content.
- Optional flag: `--dispatch`. Parallel sub-claim retrieval to subagents. Default off.
- Optional flag: `--with-images`. Triggers image-axis discovery if the corpus ships the image index.

## Outputs

- An answer in the form the user asked for, with prose citations (or file-path citations if technical/operator-facing).
- A mandatory trace footer naming the protocol and sub-claim → source mapping.

## When to use

- Any substantive question the corpus might address.
- The default path for source-grounded answers from the corpus.

## When not to use

- The corpus does not cover the topic. Use `matching-references` first to check if you're not sure.

## Related skills

- `matching-references`: topic-to-source search across the corpus catalogue. Use it first if you're unsure whether the corpus covers the topic.
