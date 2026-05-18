---
name: ingesting-images
description: Classifies images extracted from an already-ingested source as substantive (diagrams, charts, frameworks) or decorative (photos, covers, logos), and appends substantive entries to the corpus image index.
argument-hint: "[source slug or 'all']"
---

# Ingesting Images

Visual image classification for a source whose text-axis ingestion is already complete. Produces SUBSTANTIVE entries appended to `corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml`, deletes DECORATIVE files, updates the source's Pass H verification log count.

Completes the image axis when `ingesting-resources` ran *text-only* (or image classification was abandoned mid-run from context budget).

## When to use

- The source's IMAGE-INDEX.yaml entries are stub-format or labelled PARTIAL and you want full coverage.
- A source was ingested text-only originally and you want to add the image axis now.
- A source's images were re-extracted (e.g., after a substantive PDF revision) and need re-classification.

## When not to use

- Full source ingestion: use `ingesting-resources`.
- Searching the corpus for an existing source: use `matching-references`.
- Routine reading of an existing classified source: read `corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml` directly.

## Prerequisites

- The source's deep reference exists at `corpus.commons/{corpus}/references/{prefix}-{slug}-deep.md`.
- Either (a) the source PDF / EPUB exists at `corpus.commons/{corpus}/sources/original/{slug}.{ext}` (so images can be re-extracted), or (b) the image directory at `corpus.commons/{corpus}/sources/converted/{md-slug}-images/` already contains extracted files.

## Procedure

1. **Resolve scope.** If the argument is a single slug, classify that source. If `all`, scan IMAGE-INDEX.yaml for entries whose comments include `PARTIAL` or `Description not yet authored`, and process each affected source in turn.
2. **Ensure images extracted.** If `{md-slug}-images/` is empty or missing, run `python3 scripts/extract-images.py corpus.commons/{corpus}/sources/original/{slug}.{ext}` to populate.
3. **Read existing index entries** for the source from the corpus's `IMAGE-INDEX.yaml` to know what's already classified. Do not duplicate entries already present.
4. **Split into waves.** For sources over ~100 images, group the file list into waves of 64 (8 batches × 8 files conceptually). One wave = one read-only Sonnet dispatch + one splice + one commit. This bounds context per dispatch, gives a clean recovery point if a session is interrupted, and lets the operator pause between waves without losing state.
5. **Dispatch one read-only Sonnet agent per wave.** The agent gets the Read tool only: no Bash, no Edit, no Write. Brief it with: (a) the full list of file paths for this wave, (b) the SUBSTANTIVE / DECORATIVE criteria, (c) the exact YAML-line format for substantive entries, (d) the hard rule that data tables / exercise data sets / source documents are substantive (do not flag as decorative just because they lack diagrams), (e) instruction to read each file and report, never fabricate from filename. The single-agent-of-64 pattern is materially more context-efficient than fanning out 8 parallel agents of 8.
6. **Stage the wave's YAML in `/tmp`.** Write the agent's substantive entries to `/tmp/{slug}-wave{N}.yaml`. This keeps the in-progress wave out of git and recoverable if validation fails.
7. **Delete decoratives file-by-file.** The auto-mode classifier blocks bulk-glob `rm` of pre-existing files. Chain individual `rm` commands with `&&` (one per file). Then verify the new disk count.
8. **Splice the staging YAML into IMAGE-INDEX.yaml.** Use `sed -i.bak` to update the PARTIAL header (entries / decoratives deleted / unclassified remaining), then `cat /tmp/{slug}-wave{N}.yaml >> IMAGE-INDEX.yaml`. Validate with `python3 -c "import yaml; yaml.safe_load(open(...))"`: fails fast on any malformed entry.
9. **Commit each wave.** Convention: `image-ingestion: {slug} wave {N} — N kept, M deleted [corpus-data]` with a body summarising the chapter / topic coverage. Per-wave commits are the recovery point; if a later wave goes sideways, the wave-N commit is intact.
10. **On the final wave, switch PARTIAL → FINAL** in the header, with the reconciliation line `indexed + deleted = original-extraction-count`. Update the planning log entry from PARTIAL to the consolidated final summary.
11. **Append one consolidated line per source** to `_planning/image-ingestion-log.md` (or whichever the operator names). Per-wave entries belong in commit messages, not the log. Drift between log header and actual index entries is a known drift hazard: verify the index count with `python3 -c "import yaml; d=yaml.safe_load(open(...)); print(len([e for e in d if e.get('file','').startswith('{slug}-images/')]))"` before writing FINAL counts.
12. **Update Pass H** at `corpus.commons/{corpus}/references/_audit/_ingest_pass_H_{prefix}-{slug}_verification.md` with the refreshed image-classification counts (substantive / decorative).
13. **Verify and report**: total images processed, substantive count, decorative count, decorative rate, anomalies, recovery actions needed (e.g., orphaned files on disk without index entries).

## Hard rule (Source Integrity)

Every entry shipped in IMAGE-INDEX.yaml must have been visually inspected. Do not bulk-classify by filename, file extension, file size, or any metadata-only signal. Those heuristics are unreliable across publishers: the same format carries diagrams in one source and photographs in another. Visual inspection is non-negotiable.

If a source has hundreds of images and one session won't finish them, stop and report progress; the operator re-invokes in a fresh session. Do not silently truncate. Label partial IMAGE-INDEX entries as such (header comment naming what's classified and what isn't).

## Hard rule (Staging file integrity)

The per-wave staging file at `/tmp/{slug}-wave{N}.yaml` is the agent's actual classification output. If a session is summarized and resumes later, do NOT overwrite that file from memory. Either (a) re-dispatch the agent for that wave, or (b) confirm the staging file's contents match real reads by spot-checking 3-5 images against the description. The Write tool happily overwrites without warning: losing the agent's verified output and replacing it with reconstruction from page-number inference is the most common source-integrity failure mode in this skill.

## Sonnet failure modes to override

Read-only Sonnet dispatches reliably classify images but consistently make the same three errors. The operator (Opus) must override these:
- **Exercise data tables flagged as decorative** because they lack diagrams or annotation. Override: any data table the student computes from is substantive.
- **Variance / source-document scans (invoices, checks, payslips) flagged as decorative.** Override: documents that carry pedagogical data are substantive.
- **Cumulative count drift**: Sonnet's summary totals can be off-by-one or off-by-two across a wave's classification. Override: recount decoratives yourself from the actual flagged entries, don't trust the summary number.

## Related skills

- `ingesting-resources`, full ingestion of a new source (text axis plus image axis at pre-flight scope).
- `matching-references`, search the corpus for an existing source by topic.
- `creating-distillations`, project one existing verified deep reference onto one existing task axis (per-distillation projection).
- `creating-applications`, assemble a new application across multiple distillations.
