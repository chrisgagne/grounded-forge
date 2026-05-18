---
name: ingesting-resources
description: Runs the 9-pass ingestion protocol against a single source dropped in {corpus-root}/sources/ingest/, producing a .source.md sidecar, the converted markdown, a deep reference, a light reference, one distillation per applicable task axis, and index and image updates. On success, the input source is removed from sources/ingest/.
argument-hint: "[source path inside {corpus-root}/sources/ingest/, or 'paste'] [--corpus {root}] [--full | --text-only]"
---

# Ingesting Resources

Promotes a source from `{corpus-root}/sources/ingest/` (staging) to `{corpus-root}/sources/original/` (audited) by running the 9-pass protocol against it.

Each successful invocation produces, all inside the active corpus:

- One sidecar at `sources/original/{slug}.source.md` with frontmatter (title, author, URL, scope, licence, ingested, original_format, checksum_sha256).
- Converted markdown at `sources/converted/{slug}.md` (the "tape" Pass C read).
- One deep reference at `references/{slug}-deep.md`.
- One light reference at `references/{slug}.md`.
- One distillation per *applicable* task axis at `distillations/{task}/{slug}-{task}.md`. The protocol forms an opinion about applicability and asks the operator to confirm borderline cases.
- Updates to the runtime JSON indexes (`references/slug-table.json`, `reference-index.json`, `concept-index.json`, per-task `distillations/{task}/task-index.json`) and the operator-inspection `.md` views alongside.
- Substantive images extracted and indexed in `{corpus-root}/sources/converted/IMAGE-INDEX.yaml`.
- An ingestion summary.
- **The input source removed from `sources/ingest/`.** Directory state is the workflow indicator: anything in `ingest/` is unaudited; anything in `original/` has been through the protocol.

`{corpus-root}` is operator-supplied (e.g., `corpus.commons/demo/`). Default: active corpus from working-directory inference, or `builds.yaml`'s `defaults.source_dir`.

Per-pass procedures, templates, and failure modes are in [`9-pass-protocol.md`](9-pass-protocol.md).

## When to use

- Adding a new source to the corpus.
- Re-ingesting after a substantive revision (new edition, corrected text, previous Pass I failure).
- Re-ingesting when a model advance makes the deep ref materially better.

## When not to use

- Editing an existing reference's prose. Substantive edits rerun Pass C onwards; cosmetic edits rerun Pass I at minimum.
- Adding a new task axis without a new source. Run `creating-tasks` → `creating-applications` instead.
- Searching the corpus for an existing source. Run `matching-references` instead.

---

## Setup gates

Confirm before any pass runs.

### Accept input

**File path mode.** A path to a PDF, EPUB, or pre-extracted markdown file in `{corpus-root}/sources/ingest/`.

```
/ingesting-resources corpus.local/my-corpus/sources/ingest/some-book.pdf
/ingesting-resources corpus.commons/demo/sources/ingest/new-source.epub
```

**Paste mode.** Literal text pasted with explicit source metadata. The pasted text is written to `{corpus-root}/sources/ingest/{slug}.md` first, then promoted by the protocol.

```
/ingesting-resources paste --corpus corpus.local/my-corpus
```

The operator provides: pasted source text, plus author, title, edition, year, ISBN or DOI.

**Flags.**

- `--corpus {path}`: set the active corpus root. Default: infer from input path, or `builds.yaml`'s `defaults.source_dir`. All output artefacts land inside this corpus root.
- `--full` / `--text-only`: pre-commit the image-scope decision (pre-flight check 4). When absent, prompt the operator.

```
/ingesting-resources corpus.local/my-corpus/sources/ingest/some-book.pdf --text-only
/ingesting-resources paste --corpus corpus.local/my-corpus --full
```

Required metadata (either mode):

- Author (primary; secondary authors as a list).
- Title and subtitle.
- Edition / year of publication.
- ISBN or DOI where available.
- Source format and condition (PDF / EPUB / extracted markdown; conversion notes if any).
- Source licence (exact string: `CC BY 4.0`, `CC BY-NC-SA 4.0`, `All rights reserved`, etc., or `unverified`).
- Distribution scope: `open`, `open-nc`, `copyrighted`, `confidential`, or `personal`. Usually correlates with licence (CC BY → `open`, CC BY-NC-SA → `open-nc`, all-rights-reserved or unverified → `copyrighted`) but can diverge. The build excludes references whose scope exceeds a profile's `max_scope`; `personal` ships in no profile. Both fields land on the deep ref at Pass A: licence in `**Source:**`, scope on `**Scope:**`.

**Source preparation.** Pre-extract to markdown for better citation-anchor preservation. Default converter: [markitdown](https://github.com/microsoft/markitdown) (`pip install 'markitdown[all]'`). PDF fallback when markitdown fails: [`pymupdf4llm`](https://pypi.org/project/pymupdf4llm/). Converted markdown lands in `{corpus-root}/sources/converted/`.

### Pre-invocation: check for duplicate

Before invoking, run `matching-references` for the source's central topic. If a reference for this source already exists in the corpus, do not re-ingest unless one of the "When to use" conditions applies (substantive revision, model advance, prior Pass I failure).

### Source-integrity pre-flight (mandatory)

The first three checks below stop the run if they fail; the fourth is an operator decision recorded in the deep ref.

**1. Confirm completeness.** Verify the source is whole without committing to a full read yet. Check: the table of contents matches actual section headers, chapter-boundary markers are present, no obvious gaps or truncation appear (a final chapter cut mid-paragraph is a clear signal). If anything is missing or partial, **stop**. Either get the full source or label the coverage limitation in the deep reference's frontmatter explicitly (`partial coverage: chapters 1-4 only`).

**2. Detect citation style.** Grep for page anchors (`{page` markers in pandoc output, or numeric page boundaries in the converted markdown):

- Page anchors preserved: cite as `(Ch N, p. M)`.
- Page anchors lost in conversion: cite as `(Ch N, "Section name")`.

Per-source decision. Record it in the deep reference's source/structure block.

**3. Confirm model identity.** Opus 4.7 or higher. Record the operator's session model in the deep ref's frontmatter (Pass A). If the protocol fans out to subagents, each subagent declares its model identity in its first response; on any mismatch, stop and report.

**4. Image scope decision.** Declare up front whether this run includes image classification:

- **Full.** Every extracted image is visually inspected and either added to `IMAGE-INDEX.yaml` (substantive) or deleted (decorative).
- **Text-only.** Skip image classification this run. Record in the deep reference's coverage line. Complete later via `ingesting-images`.

No default. If neither `--full` nor `--text-only` was passed, prompt the operator. **Never start full and truncate mid-classification on context budget**: that produces silent partial coverage and violates source-integrity. If full looks too large for one session, declare text-only and run `ingesting-images` later.

### Effort and quality policy

| Tier | Effort | Protocol |
|---|---|---|
| Deep reference | xhigh | Full 9-pass (A through I) |
| Light reference | high | Pass F: 3-pass derivation from verified deep |
| Distillation | high | Pass G: applicability gate plus 3-pass projection, per applicable task axis |

Every downstream artefact (light, distillation, indexes) derives from the deep. Pass I is the gate; nothing ships before Pass I passes on the deep.

---

## The 9 passes

Run in order. Full procedure, templates, contracts, and pass-specific failure modes are in [`9-pass-protocol.md`](9-pass-protocol.md).

- **Pass A, Context.** Metadata, structure, citation-style block, frontmatter.
- **Pass B, Structural read.** Read once at speed; build an internal map.
- **Pass C, Deep read with citations.** Read the source in full; attach citations to every non-trivial claim.
- **Pass D, Blockquote extraction.** Select short verbatim passages; verify character-by-character.
- **Pass E, Synthesis.** Assemble the deep reference; apply `[V]` `[AP]` `[AR]` `[AE]` `[BT]` markers.
- **Pass F, Light-reference derivation.** Three sub-passes from the verified deep; source not re-read.
- **Pass G, Distillation projection.** Applicability gate (G.0); project per applicable axis (G.1–G.3).
- **Pass H, Cross-reference.** Drive the mechanical-index pipeline: allocate slug-ID, run preprocessor, dispatch Sonnet refs + cross-link passes, regenerate JSON indexes. Cross-check sibling distillations.
- **Pass I, Source-only audit.** Read the deep cold; trace every claim. Deep ships only when Pass I passes.

---

## Parallel-batch operations

When ingesting many sources in one work-session, dispatch multiple subagents in parallel: one source per subagent.

**Per-source staging files.** Each source agent writes its per-source artefacts to namespaced staging paths the build scripts read at corpus level. The canonical JSON indexes are derived; nobody edits them by hand. Staging layout (paths relative to repo root):

- `_planning/extracted/{corpus}/{slug}.json`: deterministic preprocessor output (one per source).
- `_planning/staging/{corpus}/refs/{slug}.json`: Sonnet refs-pass output (one per source).
- `_planning/staging/{corpus}/concepts/candidates.json`, `decisions.json`: corpus-wide concept aggregation (single file, written once after every per-source step completes).
- `docs/images/_ingest_image_index_{slug}.yaml`: image-index staging (one per source).

The build scripts (`scripts/build_indexes/`) consume the staging artefacts and write the canonical JSON indexes in `corpus.commons/{corpus}/`. Two reasons for the staging layer:

- **No race on the JSON indexes.** Per-source extractions and Sonnet refs passes run in parallel; the build scripts merge at corpus level after every agent completes.
- **Intermediate work survives partial failure.** If a source agent's session times out or rate-limits before its final report, staging artefacts remain on disk; the operator resumes without re-running the preprocessor.

**Concurrency ceiling.** Around 4-5 simultaneous Opus 4.7 ingestion subagents. Beyond that, Anthropic-side rate limits drop requests. Wrap-up subagents (Pass H + I on already-text-complete sources) tolerate slightly more.

---

## Post-pass operations

After Pass I passes on the deep and Passes F, G, H have produced the derived artefacts, four operations finalise the ingestion.

### Promote source from ingest/ to original/

Directory state is the workflow indicator: anything in `sources/ingest/` is unaudited; anything in `sources/original/` has been through the protocol.

1. **Author the `.source.md` sidecar** at `{corpus-root}/sources/original/{slug}.source.md` with frontmatter populated from Pass A metadata:

   ```markdown
   ---
   title: {from Pass A}
   author: {from Pass A — primary author, et al. for multi-author works}
   publisher: {from Pass A, if known}
   publish_year: {YYYY}
   isbn: {if known}
   url: {canonical URL or DOI}
   scope: {open | open-nc | copyrighted | confidential | personal}
   licence: {exact licence string from Pass A}
   ingested: {YYYY-MM-DD of this run}
   original_format: {pdf | epub | docx | md | ...}
   converted_via: {markitdown <version> | pymupdf4llm <version> | manual | ...}
   checksum_sha256: {sha256 of the input file, if binary}
   ---

   # Source: {Title} ({Author})

   {2–4 line body: provenance prose, where the source was acquired,
   any conversion caveats, links to converted markdown and deep ref.}
   ```

2. **Write the converted markdown** to `{corpus-root}/sources/converted/{slug}.md` (if not already present from a manual pre-conversion). This is the "tape" Pass C read; Pass C's deep reference traces against this file.

3. **Do NOT automatically copy the binary** from `ingest/` to `original/`. Whether to ship the original is a redistribution decision depending on licence and operator intent. The build's `.gitignore` ignores `corpus.commons/*/sources/original/*.{pdf,epub,mobi,azw3}`; operators with rights to redistribute can `git add -f` after this step.

4. **Remove the input file** from `{corpus-root}/sources/ingest/`. The sidecar and converted markdown carry the audited record forward.

**Failure recovery.** If any pass fails, **leave the input file in `ingest/`** and remove any partial output artefacts from `original/`, `converted/`, `references/`, `distillations/`. The `ingest/` directory state is the recovery signal: anything still there is unfinished business.

### Image extraction

Runs only if pre-flight scope is *full*. Skip if *text-only*; [`ingesting-images`](../ingesting-images/SKILL.md) handles it later.

**Ordering:** image extraction must run before the input file is removed from `ingest/`.

1. Run `python3 scripts/extract-images.py {corpus-root}/sources/ingest/{source}.pdf` before removing the input.
2. The extractor writes images to `{corpus-root}/sources/converted/{source-slug}-images/` and an extraction manifest to `{corpus-root}/sources/converted/extraction-manifest.json`.
3. Classify each extracted image by visual inspection (Read tool on the image file):
   - **SUBSTANTIVE**: diagram, chart, table, model, framework, process flow, decision tree, formula illustration, or other figure carrying conceptual content. Add an entry to `{corpus-root}/sources/converted/IMAGE-INDEX.yaml` with description, tags, suggested-use, and framework cross-references.
   - **DECORATIVE**: photographs, cover art, ornamental rules, blank frames, publisher logos, paper textures, icons. Delete from `{corpus-root}/sources/converted/{source-slug}-images/`.
4. Image *files* are gitignored. The *index* travels with the repo. If an image is not in `IMAGE-INDEX.yaml`, it is not part of the library.

**Per-image visual inspection is mandatory.** Never bulk-classify by filename, file extension, file size, or any metadata-only signal: the same format carries diagrams in one source and photographs in another.

### Build verification

```bash
npm run build
```

Both profiles should produce non-empty `{corpus-root}/apps/{profile}/` and pass referential integrity. The build's *sources pair-check* validates that every `sources/converted/{slug}.md` has a `sources/original/{slug}.source.md` sibling; a fresh ingestion should land both atomically.

### Ingestion summary

Output a one-screen summary covering:

- Source ingested (citation).
- Pass-by-pass results (durations, claim counts, audit fail count before fixes).
- Files produced: `.source.md` sidecar path, converted markdown path, deep ref path, light ref path, distillation file paths.
- Applicability decisions per task axis: applied, skipped (with reason), operator-confirmed on borderline calls.
- Indexes updated.
- Images extracted, classified SUBSTANTIVE, classified DECORATIVE.
- **Promotion confirmed**: input file removed from `sources/ingest/` (or, on partial failure, input remains in `ingest/` for re-run; name this explicitly).
- Open follow-ups (e.g., partial-coverage note in frontmatter flagged for re-ingestion when missing chapters arrive).

---

## Related skills

- `creating-corpus`: scaffold a new corpus before ingesting into it.
- `finding-resources`: triage candidates against the protocol's preconditions before dropping into `sources/ingest/`.
- `matching-references`: search the corpus for an existing source before ingesting a duplicate.
- `creating-distillations`: per-distillation projection; invoked by this skill's Pass G.
- `creating-applications`: assemble a new application (build profile + distillation index + orchestrated per-distillation distillation).
- `creating-tasks`: scope a new task axis. Upstream of `creating-applications`.
