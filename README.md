# grounded-forge

![A workshop scene under daylight: a craftsperson in a leather apron hands a small leather-bound notebook to a practitioner with a messenger bag, anvil in the foreground, a wall of lit card-catalog drawers behind them. In the background, a second figure flails amid airborne loose papers.](docs/assets/forge-hero.png)

*A workshop for grounded assistants: facilitators, coaches, analysts, advisors. Forge a distribution here; run it wherever your sources need to stay.*

**Project once, retrieve distillations.** A retrieval architecture for source-grounded assistants that do repeated work in known task domains.

*Selection beats reshape.* The library reads each source once under a structured 9-pass ingestion protocol, and pre-projects it onto every task domain the assistant supports. Runtime is lookup, not re-derivation: the assistant routes to an already-projected distillation in a reference × task matrix, then cites back to the source. The synthesis work is paid for once at ingestion, under audit; queries select an already-projected cell rather than re-derive it from raw chunks. (Citation discipline at runtime is bundled into each app's CLAUDE.md template. The deployed agent inherits the behaviour; the build does not enforce it as an architectural invariant.)

![A hand-drawn notebook page titled "The matrix", showing a grid with three task-axis columns — decision-making, stakeholder-engagement, software-business — and eight reference rows (barbrook-johnson-systems-mapping, openstax-organizational-behavior, approach-perfect-field-guide-scrum-events, nhs-just-culture-guide, jones-evidence-based-sweng, openstax-psychology-2e, flo-facilitation-guide, tc-25-20-army-aar), with ellipses for further rows. Filled dots fill most cells; hollow dots mark Pass G skips on the software-business column for the last three rows. Below the grid: "X references × Y task axes = Z relevant distillations; each ● is a distillation: one source × one task; ○ = Pass G gate said no for that (source, task) distillation."](docs/assets/the-matrix.png)

*The reference × task matrix. The diagram samples three task axes and eight references; the actual demo corpus ships 26 references across five task axes (decision-making, stakeholder-engagement, software-business, aar, retro).*

A ○ says the source's contribution is already carried elsewhere in the matrix. TC 25-20 covers the facilitation craft of AAR; its decision-making and stakeholder-engagement projections deliver that craft. The software-business-specific incident weight — system-vs-individual blame, regulator-facing learning loops, the PR-and-customer dimensions of a technical event — comes from NHS Just Culture, LFUO, and Business Ethics. Runtime routes through whichever projection carries the question.

Each distillation is a markdown file at `corpus.commons/{corpus}/distillations/{task}/{slug}-{task}.md`, one source projected onto one task domain. The demo corpus ships 26 references projected onto five task axes: `decision-making` with 26 distillations, `stakeholder-engagement` with 26, `software-business` with 23 (three Pass G skips routed cross-axis), plus the two ceremony axes `aar` and `retro` (each with 18 cells; Pass G skips routed cross-axis to `decision-making` and `software-business`). 111 distillations total. Fork it and ingest your own corpus; the included content can be stripped in one command.

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

1. **[The demo app](docs/tutorial/the-demo-app.md):** open a built app in Claude Code, ask it questions, see the matrix route. Zero setup. ~25 minutes.
2. **[Querying the library](docs/tutorial/querying-the-library.md):** the three read-only skills — `answer-from-library`, `matching-references`, `audit-attribution` — plus *reading the trace* (the five-second answer audit). ~30–45 minutes.
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

Same references in both apps. Different distillation directories (each carrying its own per-axis `task-index.json` runtime router plus the `.md` operator-inspection view), different CLAUDE.md. Each app is one column of the matrix, sliced and shipped independently. The corpus-level runtime indexes (`slug-table.json`, `reference-index.json`, `concept-index.json`) ship identically across apps.

To run an app: copy the app folder out of the source tree and open it in Claude Code (`cp -r corpus.commons/demo/apps/decision ~/decision-app && cd ~/decision-app && claude .`). The bundled CLAUDE.md instructs the assistant to read the runtime JSON indexes first, route to the relevant distillation, and cite back to the deep reference. Semantic-search dispatch via the persisted Chroma collection sits beneath the curated indexes as a safety net (see *Semantic search on clone* below).

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

A PreToolUse hook at [`.claude/hooks/validate-deep-ref.py`](.claude/hooks/validate-deep-ref.py) fires before any Write or Edit against `corpus.commons/demo/references/*-deep.md` and blocks the call if structural contracts are violated (frontmatter present, blockquote citations within five lines, evidence markers well-formed, no `TODO` / `[citation pending]` artefacts). The Pass I source-only audit is the model-level guard; the hook is the deterministic guard. A heuristic on-demand audit at `scripts/audit-deep-ref.py` runs claim-line coverage analysis with intentional false positives; operator reads, operator decides.

```bash
npm run audit-deep-refs                                    # audit every deep ref
python3 scripts/audit-deep-ref.py corpus.commons/demo/references/X.md  # one file
```

### Installing as a Claude Code plugin

The repo doubles as a Claude Code plugin (`.claude-plugin/plugin.json`). The skills under `.claude/skills/`, the hook at `.claude/settings.json`, and the bundled CLAUDE.md auto-discover when installed. Clone-and-run produces the same configuration as a plugin install; the manifest is the published surface, not a separate build artefact.

## Forking for your own domain

The repo ships a demo corpus at [`corpus.commons/demo/`](corpus.commons/demo/) and a private workspace at `corpus.local/` (gitignored, created on demand). The split is structural: `corpus.commons/` is tracked, redistributable, open-licensed; `corpus.local/` is yours and never enters the repo.

A corpus is self-contained: sources, references, distillations, lenses, compiled apps, and packaged tarballs all sit inside one folder. Tomorrow's contributor PR adds a folder under `corpus.commons/`; tomorrow's operator drops a folder into `corpus.local/`. The layout is identical either way.

The full forker arc is **[Scaffolding a corpus](docs/tutorial/scaffolding-a-corpus.md)** (tutorial) and **[`docs/how-to/build-your-library.md`](docs/how-to/build-your-library.md)** (how-to reference for the same procedure).

**Sharing a corpus.** When your `corpus.local/your-corpus/` is ready to ship publicly, move the folder to `corpus.commons/your-handle-your-corpus/` and open a PR. The layout doesn't change; the licence rule does. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Everything in `corpus.commons/` must be redistributable under open or open-nc.

## Integration, runtime coupling, and exit

The corpus is portable. References, distillations, lenses, and indexes are plain markdown under `corpus.commons/{corpus}/` or `corpus.local/{corpus}/`. The build system is Node.js producing more markdown. The packaging script produces tarballs. The 9-pass ingestion protocol is described in prose; the source-only audit discipline is a methodology, not a vendor lock-in. A fork that reuses the corpus material with a different orchestration framework would inherit the artefacts without modification.

The runtime is coupled to Claude Code. Opening an app folder with `claude .`, invoking skills via `/answer-from-library` and friends, the PreToolUse hook validating deep references at write time, the in-session retrieval flow: all assume Claude Code as the substrate. The skills under `.claude/skills/`, the hook under `.claude/hooks/`, and the `.claude-plugin/plugin.json` manifest are Claude Code's surfaces. A fork that wants the same experience under a different agent framework (LangGraph, CrewAI, plain SDK calls) would need to re-implement the runtime layer. The corpus would survive the move; the orchestration would not.

Model coupling is lighter than it looks. The 9-pass ingestion protocol was developed and run primarily against Claude Opus 4.7, and the deep references carry `Generated by:` metadata naming the model used. In the few side-by-side comparisons made — without much regard for token cost — the Opus output read as more reliable than Sonnet. That preference is not a measurement, and other models (Claude Sonnet, GPT-4-class, open-weight models with sufficient context and citation discipline) could plausibly do the same work. Forkers running their own ingestion under a different model are invited to test and report findings; the protocol as documented does not bind to one model. Re-ingesting an existing source under a different model produces a separate artefact, distinguishable by the `Generated by:` metadata, so corpora can carry parallel ingestions for comparison.

An exit looks like this: the corpus is files. The MIT licence covers the substrate (build system, scripts, architecture docs, skills, build profiles, index frames); CC BY 4.0 covers the long-form prose and original content (references, distillations, lenses, source sidecars authored by the maintainer); source licences govern the deep references derived from each source (per-source scope and licence are stamped in the file's frontmatter). An operator who decides to stop using this architecture takes their corpus and goes. The artefacts produced under it are readable by any tool that reads markdown. Nothing in the design or the protocol creates a lock-in to this repo's maintainer or to Anthropic.

## Audit receipts and evals

Two eval surfaces ship: a source-only audit at ingestion, and a comparative method evaluation against the runtime.

The source-only audit is Pass I of the 9-pass protocol. Aggregate Pass I outcomes across ~3,080 audited claims in the demo corpus: ~99.4% required no correction at first audit (7 marker corrections, 7 strips, 4 other fixes applied before ship). The audit is run by the same model family that produced the deep references, so the figure measures internal consistency of the source-only protocol, not independent verification. Per-source audit summaries are at [`docs/audit-results/`](docs/audit-results/) (full logs at [`corpus.commons/demo/references/_audit/`](corpus.commons/demo/references/_audit/)). The protocol is at [`docs/architecture/source-integrity.md`](docs/architecture/source-integrity.md); Pass I is calibrated against the hand-crafted fixture corpus at [`tests/audit-fixtures/`](tests/audit-fixtures/), twelve short snippets covering the seven named failure modes plus a clean negative control.

The comparative method evaluation uses a blind LLM-judge protocol at [`docs/evals/harness/`](docs/evals/harness/), ranking four method-answers to the same prompt under a 5-criterion rubric. The four methods (each collected manually by the operator in its natural product surface; only the judge step is automated):

- **A:** naive Claude with web search available; the model never chose to invoke it across the eval rounds. A forced-web-search variant of A would likely land between this A and B; not yet measured.
- **B:** Claude with research forced. Available in the Claude.ai web app only. Claude Code can be told to web-search (the model has a `WebSearch` tool), but the result of that more closely resembles A than B; B's deep-research subagent flow is not reducible to a tool call. A user could run B manually in Claude.ai and paste the result into Claude Code as context, but that workaround does not transfer to automated tooling: anywhere the matrix is invoked programmatically (the demo app, `/answer-from-library`, a subagent in a pipeline) cannot consume B's output. B is a comparison the maintainer and architect-buyer can run; not a comparison a forker can wire into their dev loop.
- **C:** Claude with the corpus's converted markdown sources in context.
- **D:** matrix via skill, `claude .` opened in the built app folder.

Methodology, rubric, and known limitations at [`docs/evals/methodology.md`](docs/evals/methodology.md). Findings from the internal eval rounds, summarised qualitatively because the corpora used extend beyond the demo corpus:

1. *On canonical material with good filename hygiene, Method C wins; the matrix is overhead.* A paired filename-obscuration probe on canonical material—readable author-and-topic slugs of the form `{author}-{topic}-{year}.md` versus hashed names—showed Method C with original filenames beat C with obscured filenames by 0.6 rubric points and *doubled* the named-scholar count (26 vs 13). The same probe on non-canonical material showed the two C variants tracking within 0.2 rubric points; the filename effect disappeared. The mechanism: filename signal works as a *key* that invokes Claude's training prior; when the prior is dense (canonical authors), filenames let Claude route in one read and spend the remaining context on content. When the prior is absent (non-public material), filename signal has nothing to invoke. Pre-migration (markdown indexes), C-original-names beat the matrix on canonical material at 40% of the token cost; the matrix paid ~3× the tokens routing through indexes Claude already knew. **Post-migration (JSON indexes, May 2026), the per-query token ratio dropped from ~131k to 28–47k tokens on the demo corpus depending on which task axis is loaded, roughly 34–36% of the pre-migration cost, which closes the 3× gap to near parity with C-original-names on first query and inverts it on second-and-subsequent queries thanks to session amortisation.** The single-query token comparison from the pre-migration eval overstated the steady-state gap because it ignored both session amortisation and the markdown-vs-JSON cost asymmetry that the migration has since removed. See [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md) for the post-migration numbers.

2. *The matrix is necessary, not redundant, when Claude's training prior cannot route the corpus.* The flip side of finding 1. On thin-filename corpora, on non-public corpora, and where curator-vs-canonical disagreement is load-bearing, training prior routing fails and the matrix's curation does the work.

3. *The lens architecture earns measurable rubric points on top of the matrix's curation.* On non-public material, Method D-with-lenses beat Method D-lensless by 0.6 rubric points on the same prompt, the same magnitude as the filename-routing effect on canonical material, in the direction the lens architecture predicts. The lens improved brief adherence rather than citation density (named-scholar counts near-identical at 8 vs 9). The lens spec is doing work on how the artefact is structured, which is what it's designed for.

4. *The matrix's distinctive value-add is structurally invisible to single-LLM-as-judge rubrics.* Two compounding limits:
   - *Corpus limit.* On canonical material, A is degenerate (the model didn't search) and B underperforms (Research scored 8.60 vs C-original-names's 9.80), so the eval becomes a contest between C variants and D. Fair enough on its own terms, except finding 1 shows C's win is filename-key-into-training-prior, not better content access.
   - *Judge limit.* On non-canonical material, A is still degenerate, but **B wins** the rubric (9.60) on the strength of reaching the canonical-derivative cluster (names the judge recognised from prior), while C and D cited operator-curated material the judge had to take on faith. The judge's `evidence_grounding` and `defensibility` criteria collapse to *"is this in my training prior?"* On canonical material that maps to truth and the rubric works. On non-canonical material it maps to *recognise-the-derivative-cluster*, which is the inverse of what the matrix is for. And the comparison a forker could actually run inside Claude Code—a forced-web-search variant of A—is not in the current eval results.

   **There is no comparison this rubric supports that fairly measures D's distinctive value-add, because the rubric's verification surface is the judge's training prior, and the matrix is precisely the architecture defending against that prior dominating the answer.**

Finding 4 is consistent with a hypothesis already in the library: Chris's LLM-epistemology corollary to Larman's Law 4 (*"displaced managers become coaches become consultants become prolific content producers, dominating the written record at roughly an order of magnitude over original thought leaders; LLMs trained on text inherit this ratio; frequency ≠ truth, language is not intelligence"*). The matrix is the library's defensive structure against this dynamic. The eval works at the artefact level (the lens earns measurable points; the matrix's filename-immunity holds on non-canonical material) but cannot fully measure what the matrix is for, because the judge operates from the consultant-frequency mean.

What this release defends: the matrix is necessary (not redundant) when Claude's training prior cannot route the corpus, and the lens earns measurable rubric points on top of that curation. The matrix's distinctive value-add — per-claim auditability on operator-curated non-canonical material — is real but structurally invisible to single-LLM-as-judge rubrics. On canonical material with good filename hygiene, naive corpus-access often suffices and the matrix is overhead. The release ships these as bounded claims, not blanket ones.

Candidates for the next eval-rubric rework: a calibrated heuristic critic that reads against operator-marked ground truth rather than against judge-prior; an operator-as-judge framing for specific traditions; an audit-trace fidelity score; the missing forced-web-search variant of A. The matrix's case lands when the verification surface stops being the judge's training prior.

Forks evaluate the architecture against their own corpora using the judge protocol at [`docs/evals/harness/`](docs/evals/harness/). The architectural ground is in [`docs/architecture/`](docs/architecture/).

## Prior art

The architecture composes ideas already published. The synthesis—matrix pre-projection at ingestion under a source-only protocol—is novel; each component has an antecedent worth naming.

Jerry Liu's "Files Are All You Need" (LlamaIndex, January 2026) frames file-system retrieval as an alternative to vector-store retrieval; the matrix lives entirely on the file system. Anthropic Skills (Zhang and Murag, "Don't Build Agents, Build Skills Instead", AI Engineer talk, 2026) packages procedural knowledge as file-dispatched artefacts; the matrix uses the same dispatch pattern but the dispatch target is *primarily* a pre-projected source distillation rather than a workflow step. (Skills can carry both prose and procedure; the distinction is what the dispatched artefact is *primarily for*.)

Karpathy's "LLM Wiki" ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), 4 April 2026) proposes that an LLM incrementally maintains a markdown wiki, with entity pages, concept pages, and indexes, as new sources arrive, moving bookkeeping cost from the human to the LLM. Obsidian as the IDE; the human browses, the LLM writes. The same load-bearing observation (*ingestion-time projection compounds; query-time re-derivation does not*) drives both designs.

The matrix architecture was running in production in prior work by the operator, ingested under the same 9-pass protocol, by **15 February 2026**, six weeks before the LLM Wiki gist was published. The convergence is independent. The mention here is to credit the public articulation and to mark three architectural differences the eval rounds made visible.

The artefact the LLM produces is built for the LLM, not the human. The wiki pattern's premise is that an LLM-maintained wiki is *also* a navigable knowledge product for a human reader. That introduces a human-readable intermediary between the source corpus and the runtime question, useful for browsing, but it adds a layer that doesn't pay back at query time and bends the artefact toward what's pleasant to browse rather than what's efficient to retrieve from. The matrix's deep references, light references, distillations, and curated routing indexes are designed for an *assistant* to consume during a query: deep refs carry verbatim quotes with evidence markers (`[V]/[AP]/[AR]/[AE]/[BT]`), light refs are reading-budget-shaped, distillations are pre-projected onto task domains, indexes are curator-built routers. The human reads the *answer*, not the artefact. The runtime path is source → matrix distillation → assistant → answer, where the wiki path would be source → wiki → human → assistant → answer. Cutting the human-readable intermediary is the load-bearing simplification.

The matrix adds the task axis. A wiki is built around one knowledge domain (the user's interest). The matrix has one reference axis and N task projections: same sources, different task readings, pre-computed at ingestion. A coaching wiki and a decision-making wiki built Karpathy-style would be two separate wikis sharing source content but duplicating bookkeeping. The matrix has one source corpus serving N downstream applications without duplication.

The matrix compiles distributable applications that narrow the corpus. `npm run build` produces shipped, scoped apps: a *decision* app carries all references + the decision-making task projection; a *stakeholder* app carries all references + the stakeholder-engagement task projection. Each app has its own bundled CLAUDE.md, its own bundled skills, and its own narrowed surface, sized for the task domain the operator is working in. The full corpus stays upstream. A wiki is a personal artefact; a matrix slice is a shippable application. The build system at [`builds.yaml`](builds.yaml) and [`build.js`](build.js) is what makes this concrete: same matrix, multiple compiled assistants, scope-filtered at ship time. This is the production-side difference: a wiki accumulates; a matrix accumulates *and ships*.

The discipline is the last difference. The wiki pattern names the bookkeeping problem; it does not name the source-fidelity problem. The 9-pass protocol's Pass I (source-only audit) is the architectural response to the LLM-epistemology problem in [`docs/architecture/llm-epistemology.md`](docs/architecture/llm-epistemology.md): without source-only discipline, an LLM-maintained wiki drifts toward the consultant-frequency mean its training data already carries. The audit is what stops the wiki pattern from being a clever instantiation of the very problem it is meant to solve.

RAG+ ([Wang et al., "RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning", EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1630/)) adds an application step to standard RAG, retrieving usage examples alongside source chunks at query time. The matrix moves the same application step from retrieval time to ingestion time: the projection from source to task is generated once under the 9-pass protocol, audited against the source, and read directly at runtime. The cost-curve framing is in [`docs/architecture/projection-time.md`](docs/architecture/projection-time.md).

Three near-neighbours in the literature deserve naming and differentiation from this work.

*Cyc-style microtheory* (Lenat & Marcus, [*Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc*](https://arxiv.org/abs/2308.04445), arXiv:2308.04445, 2023). Cyc's microtheories partition *contexts of assertion* within a shared logical knowledge base; the same proposition can hold in one microtheory and not in another, with explicit lifting rules to move assertions between them. Lenat & Marcus argue that an LLM augmented with Cyc-style symbolic reasoning could constrain the LLM's generation against logical contradictions in its training data. The matrix is a different bet: task-axis projections are natural-language distillations derived from prose sources, where Cyc's microtheories are contextually partitioned logical assertions. What the matrix shares with Cyc is the *temporal* gesture — work moved to ingestion time so it does not have to be re-done at query time — where the matrix's task axes partition task-shaped projections of a shared prose corpus and Cyc's microtheories partition contexts of assertion within a shared logical knowledge base. The substrate differs and the partition discipline differs; the load-bearing convergence is on ingestion-time precomputation.

*Clancey's NEOMYCIN-style strategic-vs-domain knowledge separation* (Clancey, *From GUIDON to NEOMYCIN and HERACLES in Twenty Short Lessons*, AI Magazine 7(3), 1986). NEOMYCIN's architectural insight was to lift diagnostic strategy out of the rule base into a separate knowledge layer (the HERACLES shell), so the same strategic knowledge could drive different domain knowledge bases. The matrix's two axes are *source* and *task*, where NEOMYCIN's split is *strategic* and *domain*. NEOMYCIN's generality never delivered the predicted reuse outside teaching-explanation contexts; the matrix avoids the same trap by binding projection to specific source-task pairs rather than carving along an abstract strategic-versus-domain split.

*Stochastic-parrots concerns* (Bender, Gebru, McMillan-Major, & Shmitchell, [*On the Dangers of Stochastic Parrots*](https://dl.acm.org/doi/10.1145/3442188.3445922), FAccT 2021). The Bender et al. critique is that LLMs reproduce the statistical patterns of their training data without understanding meaning. The 9-pass source-only audit is the most direct response this architecture has to that critique: every claim in a deep reference traces to a passage in a source the operator selected, so the operator's source-selection becomes the unit of accountability rather than the training-data prior. The audit cannot verify the source's relation to the world; that remains the operator's job. The matrix is a partial answer to Bender, not a remediation.

## Decisions and non-decisions

A short list of options considered and turned down. Full reasoning per item in [`docs/architecture/decisions-and-non-decisions.md`](docs/architecture/decisions-and-non-decisions.md).

- **Standard RAG** (retrieve-and-reshape at query time). Right tool when the question space is unbounded or the corpus changes faster than ingestion. Wrong tool for repeated work in known task domains, which is what this repo targets.
- **Cross-encoder reranker shipped by default.** Real quality bump on synthesis queries, real install-size cost (sentence-transformers + PyTorch). Flag exists (`--rerank`); evaluation against this corpus has not been run. Honest framing: thought about, not yet measured.
- **Claude Code agent teams** (experimental multi-session orchestration). Plausible for parallel ingestion across many books. Rejected: experimental status, tmux/iTerm2 dependency, and the wrong wow factor for the audience. Retrieval quality is the headline, not parallel orchestration. Within-session subagents already handle parallel ingestion at this corpus scale.
- **Audio hooks on session-end.** Cute, orthogonal to the architectural argument. Out.
- **Demo transcripts shipped in-repo.** Operator-led capture against the live corpus has more credibility than scripted output. The `setup-chroma.py --check` path provides the smaller version (query → top hits, end-to-end, no Claude Code invocation needed).

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

`npm run package` extends the same mechanism into shipped tarballs: each tarball's filename carries the most-restrictive scope across its bundled references (`decision-v0.2.1-open-nc.tar.gz`), and the tarball ships with a `LICENCE-MANIFEST.md` listing every reference's individual scope and licence. The full reference is at [`docs/reference/scope-taxonomy.md`](docs/reference/scope-taxonomy.md).

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
│       └── distros/            # Packaged tarballs from `npm run package`
├── corpus.local/               # gitignored: your private corpora
├── .claude/skills/             # Substrate authoring + runtime skills (corpus-agnostic)
├── scripts/                    # Build helpers (package.js, create-corpus.py, setup-chroma.py, …)
└── tests/audit-fixtures/       # Pass I calibration + regression fixtures
```

This release ships a 26-source demo corpus, five fully-populated task axes (111 distillations + a small number of explicit Pass G skips routed cross-axis), the lens library, the semantic-search backend, and the packaging tool. The matrix stays 2D by default; lenses are operator-opt-in per distillation. The next eval-rubric rework targets the gap named in *Audit receipts and evals* above: the single-LLM-as-judge rubric is structurally blind to the matrix's distinctive value-add (per-claim auditability on operator-curated non-canonical material), and a different verification surface is needed to measure it.
