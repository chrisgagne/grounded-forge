# grounded-forge

![A workshop scene under daylight: a craftsperson in a leather apron hands a small leather-bound notebook to a practitioner with a messenger bag, anvil in the foreground, a wall of lit card-catalog drawers behind them. In the background, a second figure flails amid airborne loose papers.](docs/assets/forge-hero.png)

*A workshop for grounded assistants: facilitators, coaches, analysts, advisors. Forge a distribution here; run it wherever your sources need to stay.*

**Project once, retrieve distillations.** A retrieval architecture for source-grounded assistants that do repeated work in known task domains.

*Selection beats reshape.* The library reads each source once under a structured 9-pass ingestion protocol, and pre-projects it onto every task domain the assistant supports. Runtime is lookup, not re-derivation: the assistant routes to an already-projected distillation in a reference × task matrix, then cites back to the source. The synthesis work is paid for once at ingestion, under audit; queries select an already-projected cell rather than re-derive it from raw chunks.

**Measured, receipts published.** Run head-to-head against Google's OKF reference producer over the same sources, the 9-pass tier extracted 1.7× the atomic claims at hard-error rates of 0.33% vs 0.38%, no detected difference ([the round](docs/evals/rounds/2026-08-08-producer-head-to-head/)). All 9,364 claims in the corpus's 27 deep references have been traced back to source by an independent cross-model auditor, and every verified finding repaired ([receipts](corpus.commons/demo/references/_audit/)). First-query routing costs 28–47k tokens, down from ~131k ([the numbers](docs/architecture/projection-time.md)).

![A hand-drawn notebook page titled "The matrix", showing a grid with three task-axis columns — decision-making, stakeholder-engagement, software-business — and eight reference rows (barbrook-johnson-systems-mapping, openstax-organizational-behavior, approach-perfect-field-guide-scrum-events, nhs-just-culture-guide, jones-evidence-based-sweng, openstax-psychology-2e, flo-facilitation-guide, tc-25-20-army-aar), with ellipses for further rows. Filled dots fill most cells; hollow dots mark Pass G skips on the software-business column for the last three rows. Below the grid: "X references × Y task axes = Z relevant distillations; each ● is a distillation: one source × one task; ○ = Pass G gate said no for that (source, task) distillation."](docs/assets/the-matrix.png)

*The reference × task matrix. The diagram samples three task axes and eight references; the actual demo corpus ships 27 references across five task axes (decision-making, stakeholder-engagement, software-business, aar, retro).*

A ○ says the source's contribution is already carried elsewhere in the matrix. TC 25-20 covers the facilitation craft of AAR; its decision-making and stakeholder-engagement projections deliver that craft. The software-business-specific incident weight — system-vs-individual blame, regulator-facing learning loops, the PR-and-customer dimensions of a technical event — comes from NHS Just Culture, LFUO, and Business Ethics. Runtime routes through whichever projection carries the question.

Each distillation is a markdown file at `corpus.commons/{corpus}/distillations/{task}/{slug}-{task}.md`, one source projected onto one task domain. The demo corpus ships 27 references projected onto five task axes: `decision-making` with 27 distillations, `stakeholder-engagement` with 27, `software-business` with 24 (three Pass G skips routed cross-axis), plus the two ceremony axes `aar` and `retro` (each with 19 cells; the eight Pass G skips per ceremony axis are routed cross-axis to `decision-making` and `software-business`). 116 distillations total. Fork it and ingest your own corpus; the included content can be stripped in one command.

![A hand-drawn notebook page titled "Gagné, after Larman: From Law 4 to LLM Authority". A cascade diagram walks from "original thought leader (slow, hard, rare)" through displaced manager → coach → consultant → LLM slop, producing prolific content (books, blogs, LinkedIn, talks) that becomes LLM training-data volume — orders of magnitude more than the primary source. Side annotation: "primary source / nuance / the point" fading to "outliers." Bottom statement: "DEFAULT LLM AUTHORITY = consultant-frequency mode. Web search gives access to more language, not to truth."](docs/assets/gagne-larman.png)

*The diagnosis. An LLM inherits its default authority from training: the consensus voice of the consultant-derivative layer that wrote the most. The primary source, slow and rare, sits in the outlier tail. Web search and "research-grade" routing amplify the same distribution.*

**Default LLM authority is consultant-frequency mode. Web search gives access to more language, not to truth.** The matrix refuses that default. Pick your sources. Project them onto your task. The assistant then reads through your windows, not the training distribution's. One rule follows: *lenses are windows, not selves* — the discipline lens specs are written under. An aside on the older vocabulary (Bruteau's *psychic grid*, 1979) and how it grounds the rule is at [The Gridmaker](docs/architecture/gridmaker.md). Read it after the engineering docs, or skip.

## Apps shipped

- **`decision`**: decision-making assistant; all references projected to the decision-making task axis.
- **`stakeholder`**: stakeholder-engagement assistant; same references, stakeholder-engagement projection.
- **`software-business`**: software-business assistant for the technical-commercial intersection.
- **`aar-mode`**: open-corpus After-Action Review assistant. Discipline borrowed-through LFUO 2024 + NHS Just Culture + SSDL + TC 25-20; ships an `aar-facilitator` runtime agent. 
- **`retro-mode`**: open-corpus retrospective-facilitation assistant. Discipline borrowed-through the Approach Perfect Field Guide + Open Practice Library + Liberating Structures + Open Kanban; ships a `retro-facilitator` runtime agent. 

The two ceremony profiles cross-link: `aar-mode` is the event-triggered cross-functional axis, `retro-mode` is the iterative team-internal axis. Same underlying corpus, different projection.

## What you can do from here

Before running anything, [`docs/examples/marines-vs-business-admin-conversation.md`](docs/examples/marines-vs-business-admin-conversation.md) shows what the output looks like: a captured `answer-from-corpus` session, verbatim — Marine warfighting doctrine × textbook business administration, with the full routing pass, retrieval trace, and evidence markers in-band. ~5 minutes to read.

1. **[The demo app](docs/tutorial/the-demo-app.md):** open a built app in Claude Code, ask it questions, see the matrix route. Zero setup. ~25 minutes.
2. **[Querying the library](docs/tutorial/querying-the-library.md):** the three read-only skills — `answer-from-corpus`, `matching-references`, `audit-attribution` — plus *reading the trace* (the five-second answer audit). ~30–45 minutes.
3. **[Ingesting one source](docs/tutorial/ingesting-one-source.md):** the 9-pass ingestion protocol against one source you bring. The matrix expands by one row. ~60 minutes.
4. **[Scoping a source](docs/tutorial/scoping-a-source.md):** `finding-resources` (pre-ingestion triage) + `ingesting-images` (the visual axis). ~20 minutes.
5. **[Adding a task axis](docs/tutorial/adding-a-task-axis.md):** a new *column* in the matrix. `creating-tasks` + `creating-applications` + `creating-distillations`. ~60–90 minutes.
6. **[Adding a lens](docs/tutorial/adding-a-lens.md):** the per-distillation modifier. `creating-lenses` + Pass G's per-distillation gate. ~45 minutes.
7. **[Scaffolding a corpus](docs/tutorial/scaffolding-a-corpus.md):** the full forker arc with `creating-corpus`. ~2–3 hours.

For how-to guides, lookup material, and the architectural argument, the docs index is at [`docs/README.md`](docs/README.md). See [`docs/architecture/overview.md`](docs/architecture/overview.md) for the one-page summary, and [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md) for the cost-curve framing against standard RAG.

## Who this is for

This is for people building source-grounded assistants in narrow task domains where the same sources get re-read for the same handful of tasks.

The open corpus provided shows the pattern for general business reference work; it is a proxy for a coaching, training, or advisory library, not for a regulated-domain knowledge base or a high-velocity source corpus. See [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md) for when the matrix is the wrong tool.

## How to use

**For the demo (zero-setup):** Node 18+ for the build and the packager, Python 3.9+ for `npm run remove-corpus` and the Chroma scripts. `pip install chromadb` is the only Python dependency in the default path.

**Going past the demo** — opening a built app, ingesting your own source, scaffolding a fresh corpus — needs more. Claude Code installed and signed in, `ANTHROPIC_API_KEY` exported (or a Claude subscription that covers Opus usage), `markitdown` for source conversion, and roughly $1–5 of Opus tokens per ingested source under the 9-pass protocol. The tutorials list these where they apply.

```bash
npm install
npm run build
diff -rq corpus.commons/demo/apps/decision/ corpus.commons/demo/apps/stakeholder/
```

The `diff` proves the matrix architecture in one command:

```
Files corpus.commons/demo/apps/decision/CLAUDE.md and corpus.commons/demo/apps/stakeholder/CLAUDE.md differ
Only in corpus.commons/demo/apps/decision/distillations: decision-making
Only in corpus.commons/demo/apps/stakeholder/distillations: stakeholder-engagement
```

Same reference corpus upstream of both. Different distillation directories (each carrying its own per-axis `task-index.json` runtime router plus the `.md` operator-inspection view), different CLAUDE.md. Each app is one column of the matrix, sliced and shipped independently. The shipped corpus-level indexes (`slug-table.json` and the distillation-only `concept-index.json`) are identical across apps; `reference-index.json` and the reference tier stay upstream.

To run an app: copy the app folder out of the source tree and open it in Claude Code (`cp -r corpus.commons/demo/apps/decision ~/decision-app && cd ~/decision-app && claude .`). The bundled CLAUDE.md instructs the assistant to read the runtime JSON indexes first, route to the relevant distillation, and attribute claims with the citations and evidence markers each distillation carries in-band. Semantic-search dispatch via the persisted Chroma collection sits beneath the curated indexes as a safety net (see *Semantic search on clone* below).

To hand an app to someone else: `npm run package decision` produces a scope-labelled tarball in `corpus.commons/demo/distros/`. The recipient untars and runs `claude .`.

For a worked example of the routing chain (index hit → distillation → deep-ref citation), see [`docs/architecture/matrix-pattern.md`](docs/architecture/matrix-pattern.md).

### Semantic search on clone

The semantic-search backend is a Chroma collection persisted at `{corpus_root}/chroma/`, one per corpus, regenerated on clone. Chroma is a derived index, model + library-version bound, so the recipe ships in the repo and the index is rebuilt locally.

```bash
pip install chromadb
python3 scripts/setup-chroma.py             # build the demo corpus's chroma index (~30s)
python3 scripts/setup-chroma.py --check     # run 3 canned queries, print top hits
```

`--check` proves the retrieval loop end-to-end without invoking Claude Code: natural-language queries route to pre-projected distillations of the corpus, ordered by cosine similarity. For a different corpus, pass `--corpus corpus.local/your-corpus`; the chroma directory resolves to that corpus's root. To rebuild the collection after editing references or distillations, `python3 scripts/setup-chroma.py --rebuild`. The default embedding function is chromadb's `DefaultEmbeddingFunction` (ONNX runtime, `all-MiniLM-L6-v2`, ~80MB downloaded once to a per-machine cache); no PyTorch dependency in the default path. An opt-in cross-encoder rerank (`--rerank`) is documented but not evaluated for this corpus; see [`docs/architecture/decisions-and-non-decisions.md`](docs/architecture/decisions-and-non-decisions.md).

### Source-integrity at write time

A PreToolUse hook at [`.claude/hooks/validate-deep-ref.py`](.claude/hooks/validate-deep-ref.py) fires before any Write or Edit against `corpus.commons/demo/references/*-deep.md` and blocks the call if structural contracts are violated (frontmatter present, blockquote citations within five lines, evidence markers well-formed, no `TODO` / `[citation pending]` artefacts). The hook is a thin adapter over the runtime-agnostic checks in [`scripts/validate/deep_ref_core.py`](scripts/validate/deep_ref_core.py), so every enforcement point — this hook, the build-time validation, and the git pre-push audit — gates on the identical contract from one source of truth. The Pass I source-only audit is the model-level guard; the hook is the deterministic guard. A heuristic on-demand audit at `scripts/audit-deep-ref.py` runs claim-line coverage analysis with intentional false positives; operator reads, operator decides.

```bash
npm run audit-deep-refs                                    # audit every deep ref
python3 scripts/audit-deep-ref.py corpus.commons/demo/references/X.md  # one file
```

### Installing as a Claude Code plugin

The repo doubles as a Claude Code plugin (`.claude-plugin/plugin.json`). The skills under `.claude/skills/`, the hook at `.claude/settings.json`, and the bundled CLAUDE.md auto-discover when installed. Clone-and-run produces the same configuration as a plugin install; the manifest is the published surface, not a separate build artefact.

### Agent-ready for any tool

Claude Code reads `CLAUDE.md`; other coding agents (Codex and the growing set of AGENTS.md-aware tools) read `AGENTS.md`. The repo ships one at its root — a thin adapter that points any file-access agent at the same guardrails: read `CLAUDE.md`, invoke the skills under `.claude/skills/*/SKILL.md` natively where the runtime supports it, fall back to reading them as written procedures where it does not, and honour the source-integrity floor and tier separation. The durable enforcement lives where every agent hits it regardless of vendor: the git pre-push audit and build-time validation, not any one runtime's pre-write hook. Any agent that lands here inherits the discipline from the first file it reads.

## Forking for your own domain

The repo ships a demo corpus at [`corpus.commons/demo/`](corpus.commons/demo/) and a private workspace at `corpus.local/` (gitignored, created on demand). The split is structural: `corpus.commons/` is tracked, redistributable, open-licensed; `corpus.local/` is yours and never enters the repo.

A corpus is self-contained: sources, references, distillations, lenses, compiled apps, and packaged tarballs all sit inside one folder. Tomorrow's contributor PR adds a folder under `corpus.commons/`; tomorrow's operator drops a folder into `corpus.local/`. The layout is identical either way.

The full forker arc is **[Scaffolding a corpus](docs/tutorial/scaffolding-a-corpus.md)** (tutorial) and **[`docs/how-to/build-your-library.md`](docs/how-to/build-your-library.md)** (how-to reference for the same procedure).

**Sharing a corpus.** When your `corpus.local/your-corpus/` is ready to ship publicly, move the folder to `corpus.commons/your-handle-your-corpus/` and open a PR. The layout doesn't change; the licence rule does. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Everything in `corpus.commons/` must be redistributable under open or open-nc.

## Integration, runtime coupling, and exit

The corpus is portable. References, distillations, lenses, and indexes are plain markdown under `corpus.commons/{corpus}/` or `corpus.local/{corpus}/`. The build system is Node.js producing more markdown. The packaging script produces tarballs. The 9-pass ingestion protocol is described in prose; the source-only audit discipline is a methodology, not a vendor lock-in. A fork that reuses the corpus material with a different orchestration framework would inherit the artefacts without modification.

The runtime targets agentic CLIs, at two levels of maturity. Claude Code is the extensively exercised substrate: opening an app folder with `claude .`, invoking skills via `/answer-from-corpus` and friends, the PreToolUse hook validating deep references at write time, the in-session retrieval flow. The skills under `.claude/skills/`, the hook under `.claude/hooks/`, and the `.claude-plugin/plugin.json` manifest are Claude Code's surfaces. Codex is newly ported and smoke-tested: `AGENTS.md` points it at the same contract, with skills read as written procedures rather than invoked natively, and enforcement carried by the runtime-neutral layers (the git pre-push audit and build-time validation). A fork that wants the same experience under a different agent framework (LangGraph, CrewAI, plain SDK calls) would need to re-implement the runtime layer. The corpus would survive the move; the orchestration would not.

Model coupling is lighter than it looks. The 9-pass ingestion protocol was developed and run primarily against Claude Opus 4.7, and the deep references carry `Generated by:` metadata naming the model used. In informal side-by-side reads (not a measured comparison), the Opus output was more reliable than Sonnet; other models (Claude Sonnet, GPT-4-class, open-weight models with sufficient context and citation discipline) could plausibly do the same work. Forkers running their own ingestion under a different model are invited to test and report findings; the protocol as documented does not bind to one model. Re-ingesting an existing source under a different model produces a separate artefact, distinguishable by the `Generated by:` metadata, so corpora can carry parallel ingestions for comparison.

An exit looks like this: the corpus is files. The MIT licence covers the substrate (build system, scripts, architecture docs, skills, build profiles, index frames); CC BY 4.0 covers the long-form prose and original content (references, distillations, lenses, source sidecars authored by the maintainer); source licences govern the deep references derived from each source (per-source scope and licence are stamped in the file's frontmatter). An operator who decides to stop using this architecture takes their corpus and goes. The artefacts produced under it are readable by any tool that reads markdown, and the build emits each profile's data layer as an Open Knowledge Format (OKF v0.2) bundle — a published interchange format any conformant tool can consume — so the exit has a standards-track door as well as a file tree (see [`docs/how-to/emit-okf.md`](docs/how-to/emit-okf.md)). Nothing in the design or the protocol creates a lock-in to this repo's maintainer or to Anthropic.

## Audit receipts and evals

Two results lead, both receipted in-repo.

**Head-to-head against Google's OKF reference producer**, over the same sources, cross-model, with matched judges and matched audit priming: on the fully matched arm the 9-pass tier extracted 909 atomic claims to the naive producer's 526 — 1.7× the coverage — at hard-error rates of 0.33% vs 0.38%, no detected difference. A broader, less-matched arm reached ~3× coverage but does not support an error-rate comparison, and the two arms are reported separately. More coverage at no measured cost in error rate, from the production passes alone: the matched references ran Passes A–E only, so the matched result did not depend on the audit pass Google's producer lacks. The full record, both arms' artefacts, and every audit receipt are published at [`docs/evals/rounds/2026-08-08-producer-head-to-head/`](docs/evals/rounds/2026-08-08-producer-head-to-head/); anyone can re-run the audits.

**The deep-reference tier is independently audited in full: a census, not a sample.** A fresh-context auditor from a different model family traced all 9,364 claims across all 27 deep references back to their converted sources at strict claim grain (2026-08-08). The pre-repair tier graded 97.45% clean, with a 2.6% hard-error rate dominated by attributions to people the sources never name and enumeration miscounts; all 446 findings were re-verified against source during repair (445 fixed, 1 rejected as source-supported), with 412 propagated fixes chasing the repairs into the light references and distillations and a finding-by-finding re-verification pass on the six worst sources. The receipts (per-source machine-readable findings, the corpus summary, and the repair record) are at [`corpus.commons/demo/references/_audit/`](corpus.commons/demo/references/_audit/). A single audit pass reduces but does not eliminate injected error; residual error falls with repeated, independent checks and with more capable producing models. Google's reference producer ships with no source-level audit.

**The audit tier catches its own blind spot.** The head-to-head round surfaced a failure mode of LLM self-audit: an in-context audit certified the producing model's own fabrications as "verified at source", and the identical procedure in a fresh context failed the same file; a fresh audit in the second model family likewise caught that family's own leakage. The causal variable is context freshness, not the model. So Pass I, the protocol's source-only audit — a cold read of each finished deep reference that traces every claim back to the converted source and refuses to ship anything that fails the trace test — **must run in a fresh context, and preferably a different model, from the one that produced the deep reference.** An in-context self-audit reads the training-priors the producing session just wrote in as source-grounded and passes them; independence is what makes the cold read cold, and it is the only thing that catches a confident hallucination the producer believes. Fresh-context Pass I is mandatory in the protocol, and the corpus-wide independent audit above ran under it. The protocol is at [`docs/architecture/source-integrity.md`](docs/architecture/source-integrity.md); Pass I is calibrated against the fixture corpus at [`tests/audit-fixtures/`](tests/audit-fixtures/), twelve short fixtures covering the protocol's named failure modes plus a clean negative control.

The comparative method evaluation is a separate surface: a blind LLM-judge protocol at [`docs/evals/harness/`](docs/evals/harness/) ranks four method-answers to the same prompt under a 5-criterion rubric — naive Claude, Claude with research forced, the converted sources in context, and the matrix — each collected in its natural product surface. Method definitions, reproducibility notes, and the rubric are at [`docs/evals/methodology.md`](docs/evals/methodology.md). Findings from the internal eval rounds, summarised qualitatively because the corpora used extend beyond the demo corpus:

1. *The matrix is necessary, not redundant, where Claude's training prior cannot route the corpus.* On thin-filename corpora, on non-public corpora, and where curator-vs-canonical disagreement is load-bearing, training-prior routing fails and the matrix's curation does the work.

2. *The lens architecture earns measurable rubric points on top of the matrix's curation.* On non-public material, Method D-with-lenses beat Method D-lensless by 0.6 rubric points on the same prompt, in the direction the lens architecture predicts. The lens improved brief adherence rather than citation density (named-scholar counts near-identical at 8 vs 9): the lens spec is doing work on how the artefact is structured, which is what it's designed for.

3. *Post-migration, the routing tax is small on the first query and gone by the second.* The May 2026 index migration (markdown to JSON) cut the matrix's per-query first-load from ~131k tokens to 28–47k on the demo corpus (corpus-level indexes alone at the low end, plus one task axis at the high end) — near the token cost of naive corpus access on the first query — and session amortisation inverts the comparison on second-and-subsequent queries. A paired filename-obscuration probe located the mechanism behind naive corpus access's strength: readable `{author}-{topic}-{year}.md` filenames work as keys into Claude's training prior. On canonical material, original filenames beat obscured ones by 0.6 rubric points and doubled the named-scholar count (26 vs 13); on non-canonical material the two variants tracked within 0.2 points and the effect disappeared. Post-migration numbers at [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md).

4. *Where the corpus is canonical and the filenames route it, these rounds showed no answer-quality gain for the matrix; naive corpus access suffices there.* The matrix's remaining case on that surface is audit traceability and session amortisation; its necessary case is the corpora the training prior cannot route.

One limit of that rubric is structural, and it is why the producer head-to-head above exists. A single LLM-as-judge cannot measure the matrix's distinctive value-add — per-claim auditability on operator-curated non-canonical material — because the judge's verification surface is its own training prior, the very distribution the matrix defends against. The judge operates from the consultant-frequency mean: the library's LLM-epistemology corollary to Larman's Law 4 ([`docs/architecture/llm-epistemology.md`](docs/architecture/llm-epistemology.md)) showing up inside the eval. The head-to-head sidesteps the judge's prior entirely by auditing producer output against source text, claim by claim. The full analysis, the per-round evidence, and the next-rubric candidates (a critic calibrated against operator-marked ground truth, an audit-trace fidelity score, the forced-web-search arm) are at [`docs/evals/methodology.md`](docs/evals/methodology.md).

What this release defends: the producer discipline is benchmarked (1.7× coverage at no measured cost in error rate on the fully matched arm against Google's reference producer); the deep-reference tier behind every app is independently audited claim-by-claim, receipts published; the matrix is necessary where the training prior cannot route the corpus; and the lens earns measurable rubric points on top of that curation. Where the corpus is canonical and filenames route it, naive corpus access suffices. These ship as bounded claims with their receipts, not blanket ones.

Forks evaluate the architecture against their own corpora using the judge protocol at [`docs/evals/harness/`](docs/evals/harness/). The architectural ground is in [`docs/architecture/`](docs/architecture/).

## Prior art

The matrix was in production by 15 February 2026—seven weeks before Karpathy's LLM Wiki gist, four months before Google's OKF—running in the operator's prior work under the same 9-pass protocol. Three independent arrivals at the same substrate: markdown knowledge files, deterministic routing, ingestion-time projection. The synthesis this repo adds—matrix pre-projection at ingestion under a source-only audit—is the producer discipline the later two leave open. Each component has an antecedent worth naming.

Jerry Liu's "Files Are All You Need" (LlamaIndex, January 2026) frames file-system retrieval as an alternative to vector-store retrieval; the matrix lives entirely on the file system. Anthropic Skills (Zhang and Murag, "Don't Build Agents, Build Skills Instead", AI Engineer talk, 2026) packages procedural knowledge as file-dispatched artefacts; the matrix uses the same dispatch pattern but the dispatch target is *primarily* a pre-projected source distillation rather than a workflow step. (Skills can carry both prose and procedure; the distinction is what the dispatched artefact is *primarily for*.)

Karpathy's "LLM Wiki" ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), 4 April 2026) proposes that an LLM incrementally maintains a markdown wiki, with entity pages, concept pages, and indexes, as new sources arrive, moving bookkeeping cost from the human to the LLM. Obsidian as the IDE; the human browses, the LLM writes. The same load-bearing observation (*ingestion-time projection compounds; query-time re-derivation does not*) drives both designs.

The convergence is independent (the matrix predates the gist, as above); the mention here credits the public articulation and marks three architectural differences the eval rounds made visible.

The artefact the LLM produces is built for the LLM, not the human. The wiki pattern's premise is that an LLM-maintained wiki is *also* a navigable knowledge product for a human reader. That introduces a human-readable intermediary between the source corpus and the runtime question, useful for browsing, but it adds a layer that doesn't pay back at query time and bends the artefact toward what's pleasant to browse rather than what's efficient to retrieve from. The matrix's deep references, light references, distillations, and curated routing indexes are designed for an *assistant* to consume during a query: deep refs carry verbatim quotes with evidence markers (`[V]/[AP]/[AR]/[AE]/[BT]`), light refs are reading-budget-shaped, distillations are pre-projected onto task domains, indexes are curator-built routers. The human reads the *answer*, not the artefact. The runtime path is source → matrix distillation → assistant → answer, where the wiki path would be source → wiki → human → assistant → answer. Cutting the human-readable intermediary is the load-bearing simplification.

The matrix adds the task axis. A wiki is built around one knowledge domain (the user's interest). The matrix has one reference axis and N task projections: same sources, different task readings, pre-computed at ingestion. A coaching wiki and a decision-making wiki built Karpathy-style would be two separate wikis sharing source content but duplicating bookkeeping. The matrix has one source corpus serving N downstream applications without duplication.

The matrix compiles distributable applications that narrow the corpus. `npm run build` produces shipped, scoped apps: a *decision* app carries the decision-making projection with its runtime routers; a *stakeholder* app carries the stakeholder-engagement projection; the reference tier stays upstream as the shared audit-of-record. Each app has its own bundled CLAUDE.md, its own bundled skills, and its own narrowed surface, sized for the task domain the operator is working in. The full corpus stays upstream. A wiki is a personal artefact; a matrix slice is a shippable application. The build system at [`builds.yaml`](builds.yaml) and [`build.js`](build.js) is what makes this concrete: same matrix, multiple compiled assistants, scope-filtered at ship time. This is the production-side difference: a wiki accumulates; a matrix accumulates *and ships*.

The discipline is the last difference. The wiki pattern names the bookkeeping problem; it does not name the source-fidelity problem. The 9-pass protocol's Pass I (source-only audit) is the architectural response to the LLM-epistemology problem in [`docs/architecture/llm-epistemology.md`](docs/architecture/llm-epistemology.md): without source-only discipline, an LLM-maintained wiki drifts toward the consultant-frequency mean its training data already carries. The audit is what stops the wiki pattern from being a clever instantiation of the very problem it is meant to solve.

Google's Open Knowledge Format ([OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog), Apache-2.0, published 12 June 2026; v0.2 at the time of writing) is the strongest convergence yet, and the first from a platform vendor rather than a practitioner: knowledge shipped as a bundle of markdown concept files with YAML frontmatter, standard-markdown cross-links, reserved `index.md` routers for progressive disclosure, and deterministic navigation preferred over embedding retrieval. That is the substrate this repo was already running on (in production by 15 February 2026, as above; the convergence is independent). The difference is where the spec stops. OKF specifies the *container* and is silent on the *producer*: nothing in it says how a concept file gets made, what its claims trace to, or how drift is caught — and Google's reference producer is an LLM enrichment agent over BigQuery metadata with no source-only audit. The container argument is settling; the producer discipline is the open problem, and it is the part this repo is about. It is also now the measured part: run over prose sources — outside its BigQuery home domain — the reference producer minted zero references until the round's operator adapted its reuse gate, and at full match the 9-pass tier extracted 1.7× the claims with no detected difference in error rate ([the round](docs/evals/rounds/2026-08-08-producer-head-to-head/)).

So the build treats OKF as an exit door, not a rival. From v0.4.0 any profile can *emit* its gated output as a conformant OKF v0.2 bundle — evidence markers, per-source licence manifest, and provenance frontmatter in-band, validated against the community `okf` CLI — and the shipped `matrix` bundle carries all five task projections of the same 27 sources in one tree, expressing the task axis (a dimension OKF's one-file-per-concept model lacks) as directory structure. Conformance is a container property; this repo ships an audited producer behind it. The full argument is in [`docs/architecture/okf-interop.md`](docs/architecture/okf-interop.md); the decision to emit from audited distillations rather than fork the un-audited producer is in [`docs/architecture/decisions-and-non-decisions.md`](docs/architecture/decisions-and-non-decisions.md).

RAG+ ([Wang et al., "RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning", EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1630/)) adds an application step to standard RAG, retrieving usage examples alongside source chunks at query time. The matrix moves the same application step from retrieval time to ingestion time: the projection from source to task is generated once under the 9-pass protocol, audited against the source, and read directly at runtime. The cost-curve framing is in [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md).

Three near-neighbours in the literature deserve naming and differentiation from this work.

*Cyc-style microtheory* (Lenat & Marcus, [*Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc*](https://arxiv.org/abs/2308.04445), arXiv:2308.04445, 2023). Cyc's microtheories partition *contexts of assertion* within a shared logical knowledge base; the same proposition can hold in one microtheory and not in another, with explicit lifting rules to move assertions between them. Lenat & Marcus argue that an LLM augmented with Cyc-style symbolic reasoning could constrain the LLM's generation against logical contradictions in its training data. The matrix is a different bet: task-axis projections are natural-language distillations derived from prose sources, where Cyc's microtheories are contextually partitioned logical assertions. What the matrix shares with Cyc is the *temporal* gesture — work moved to ingestion time so it does not have to be re-done at query time — where the matrix's task axes partition task-shaped projections of a shared prose corpus and Cyc's microtheories partition contexts of assertion within a shared logical knowledge base. The substrate differs and the partition discipline differs; the load-bearing convergence is on ingestion-time precomputation.

*Clancey's NEOMYCIN-style strategic-vs-domain knowledge separation* (Clancey, *From GUIDON to NEOMYCIN and HERACLES in Twenty Short Lessons*, AI Magazine 7(3), 1986). NEOMYCIN's architectural insight was to lift diagnostic strategy out of the rule base into a separate knowledge layer (the HERACLES shell), so the same strategic knowledge could drive different domain knowledge bases. The matrix's two axes are *source* and *task*, where NEOMYCIN's split is *strategic* and *domain*. NEOMYCIN's generality never delivered the predicted reuse outside teaching-explanation contexts; the matrix avoids the same trap by binding projection to specific source-task pairs rather than carving along an abstract strategic-versus-domain split.

*Stochastic-parrots concerns* (Bender, Gebru, McMillan-Major, & Shmitchell, [*On the Dangers of Stochastic Parrots*](https://dl.acm.org/doi/10.1145/3442188.3445922), FAccT 2021). The Bender et al. critique is that LLMs reproduce the statistical patterns of their training data without understanding meaning. The 9-pass source-only audit is the most direct response this architecture has to that critique: every claim in a deep reference traces to a passage in a source the operator selected, so the operator's source-selection becomes the unit of accountability rather than the training-data prior. The audit cannot verify the source's relation to the world; that remains the operator's job. The matrix is a partial answer to Bender, not a remediation.

## Decisions and non-decisions

A short list of options considered and turned down. Full reasoning per item in [`docs/architecture/decisions-and-non-decisions.md`](docs/architecture/decisions-and-non-decisions.md).

- **Standard RAG** (retrieve-and-reshape at query time). Right tool when the question space is unbounded or the corpus changes faster than ingestion. Wrong tool for repeated work in known task domains, which is what this repo targets.
- **Cross-encoder reranker shipped by default.** Real quality bump on synthesis queries, real install-size cost (sentence-transformers + PyTorch). Flag exists (`--rerank`); evaluation against this corpus has not been run. Thought about, not yet measured.
- **Claude Code agent teams** (experimental multi-session orchestration). Plausible for parallel ingestion across many books. Rejected: experimental status, tmux/iTerm2 dependency, and the wrong wow factor for the audience. Retrieval quality is the headline, not parallel orchestration. Within-session subagents already handle parallel ingestion at this corpus scale.
- **Audio hooks on session-end.** Cute, orthogonal to the architectural argument. Out.
- **Demo transcripts shipped in-repo.** Operator-led capture against the live corpus has more credibility than scripted output. The `setup-chroma.py --check` path provides the smaller version (query → top hits, end-to-end, no Claude Code invocation needed).
- **Forking Google's OKF Reference Agent as the producer.** Rejected: BigQuery-shaped input, no source-only audit — the drift class Pass I exists to catch. The build emits OKF v0.2 bundles from already-audited distillations instead; the format is the container, the 9-pass protocol is the producer.

## Licence split

The repo splits on substrate vs content:

- **Substrate** (code (build system, scripts), architecture documentation under `docs/architecture/`, the vocabulary reference, build profile templates under `corpus.commons/{corpus}/build-profiles/`, skill specifications (every `SKILL.md`), and index frames at per-task distillation INDEX `.md`, `LENS-INDEX.md`, and the runtime JSON indexes): **MIT**. See [`LICENSE`](LICENSE).
- **Content authored by the maintainer** (references, distillations, lenses, source sidecars, and long-form prose at `README.md`, `CONTRIBUTING.md`, `DISCLAIMER.md`, `LICENSE-CONTENT`): **CC BY 4.0**. See [`LICENSE-CONTENT`](LICENSE-CONTENT).
- **Third-party-derived references and distillations** (e.g. `corpus.commons/demo/references/openstax-*`, `corpus.commons/demo/distillations/{task}/openstax-*`): inherit each source's licence. The 12-book OpenStax corpus mostly carries **CC BY-NC-SA 4.0** (NonCommercial + ShareAlike); *Introduction to Business* is the one exception at CC BY 4.0. Each deep reference's frontmatter records the actual licence. See [`LICENSE-CONTENT`](LICENSE-CONTENT) Section 2 for the full source-by-source table.
- **Disclaimer and warranty.** Use of the Materials is also subject to [`DISCLAIMER.md`](DISCLAIMER.md) (no warranty, NZ Consumer Guarantees Act 1993 s 43 and Fair Trading Act 1986 s 5D contracting-out for in-trade supplies, AI-output disclaimer, limitation of liability, NZ governing law).

**Commercial use.** Audit every source in the corpus and confirm you have a licence to use it for the commercial purpose you intend, including any sources you add yourself. Per-source licences are recorded in [`LICENSE-CONTENT`](LICENSE-CONTENT) Section 2 and on each deep reference's frontmatter. The substrate (MIT) carries no source-licensing constraint, but commercial deployment also engages the supply terms in [`DISCLAIMER.md`](DISCLAIMER.md). Obtain your own legal advice before commercial deployment.

## Distribution scope

Licence governs *attribution and derivative-rights*; **scope** governs *distribution*. Each deep reference carries a `**Scope:**` line, and each build profile in [`builds.yaml`](builds.yaml) declares a `max_scope` ceiling. References whose scope exceeds the profile's ceiling are excluded at build time. Five levels, monotonic risk gradient:

| Rank | Scope | What goes here |
|---|---|---|
| 0 | `open` | Public-domain, CC0, CC BY, CC BY-SA, MIT, Apache, gov't works |
| 1 | `open-nc` | CC BY-NC, CC BY-NC-SA, open with non-commercial restriction |
| 2 | `copyrighted` | Published all-rights-reserved material the operator/org has legitimate access to |
| 3 | `confidential` | Bounded-access engagement material (client docs, past AARs, incident data) |
| 4 | `personal` | Operator's own private notes, journals, drafts; never ships in any profile |

The demo profiles default to `max_scope: open-nc`, matching the OpenStax + supplementary CC sources. The mechanism is *latent* in this configuration (nothing exceeds the ceiling), but it's there for forks that mix confidential client material with public CC sources. `personal` is excluded by construction: no `max_scope` value admits it.

`npm run package` extends the same mechanism into shipped tarballs: each tarball's filename carries the most-restrictive scope across its bundled references (`decision-v0.4.0-open-nc.tar.gz`), and the tarball ships with a `LICENCE-MANIFEST.md` listing every reference's individual scope and licence. Emitted OKF bundles carry the identical mechanism — the licence manifest travels *inside* each bundle, and `node scripts/package.js {profile} --okf` produces the same scope-labelled tarball form. The full reference is at [`docs/reference/scope-taxonomy.md`](docs/reference/scope-taxonomy.md).

## A note on copyright

The author is not a lawyer; neither is the AI that helped build this. Nothing in the repo is legal advice. The build system and the ingestion protocol are neutral infrastructure. Some use modes (internal knowledge bases, personal libraries, distributions of CC-BY material) are unlikely to raise the question; distributing artefacts derived from copyrighted sources without a licence may, and how depends on the operator's jurisdiction and circumstances. See [`docs/architecture/copyright.md`](docs/architecture/copyright.md) and the full warranty disclaimer at [`DISCLAIMER.md`](DISCLAIMER.md).

## Repo layout

```
grounded-forge/
├── build.js                    # Build script
├── builds.yaml                 # Profile definitions
├── package.json
├── docs/
│   ├── tutorial/               # Learn-by-doing walkthroughs (querying-the-library, ingesting-one-source, …)
│   ├── how-to/                 # Task-oriented guides (build-your-library, …)
│   ├── reference/              # Lookup material (vocabulary, known-limitations, …)
│   ├── architecture/           # Explanations of why the matrix works the way it does
│   └── evals/                  # Methodology + judge protocol for the comparative method eval
├── corpus.commons/
│   └── demo/                   # The OpenStax demo corpus
│       ├── references/         # Light + deep references (the reference axis)
│       ├── distillations/      # Task projections (the task axis)
│       ├── lenses/             # Per-distillation modifier specs
│       ├── sources/            # original/ + converted/ + ingest/
│       ├── tasks/              # Task-axis specs (operator-inspection)
│       ├── build-profiles/     # CLAUDE.md templates per shipped profile (corpus-bound)
│       ├── .claude/agents/     # Corpus-bound runtime agents
│       ├── apps/               # Compiled apps per build profile
│       ├── okf/                # Emitted OKF v0.2 interchange bundles (per app + full-matrix)
│       └── distros/            # Packaged tarballs from `npm run package`
├── corpus.local/               # gitignored: your private corpora
├── .claude/skills/             # Substrate authoring + runtime skills (corpus-agnostic)
├── scripts/                    # Build helpers (package.js, create-corpus.py, setup-chroma.py, …)
└── tests/audit-fixtures/       # Pass I calibration + regression fixtures
```

This release ships a 27-source demo corpus, five task axes (116 distillations, with 19 explicit Pass G skips routed cross-axis), the lens library, six validated OKF v0.2 interchange bundles (one per app profile plus the full-matrix `matrix` bundle), the semantic-search backend, and the packaging tool. The matrix stays 2D by default; lenses are operator-opt-in per distillation. The producer discipline behind it is benchmarked and the corpus it ships is audited, receipts in-repo: [the head-to-head round](docs/evals/rounds/2026-08-08-producer-head-to-head/) and [the audit record](corpus.commons/demo/references/_audit/).
