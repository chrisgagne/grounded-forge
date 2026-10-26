---
name: removing-resources
description: Removes one ingested source from a corpus as if it had never been ingested. Retires the original to sources/removed/, deletes the source's references, distillations, converted text, audit files and working files, takes it off the concept index and the distillation indexes, retires its slug-table ID, then rewrites every other distillation, task spec, lens and build profile that still draws on it, has a fresh reviewer audit those rewrites, and rebuilds. The inverse of ingesting-resources. Use when a source is superseded (a replaced policy, a new edition ingested separately) or no longer worth keeping.
argument-hint: "{slug} [--corpus {name}] [--reason \"...\"]"
---

# Removing Resources

The inverse of [`ingesting-resources`](../ingesting-resources/SKILL.md). When it finishes, the corpus reads as if the source had never been ingested: no file, index row, concept credit or cross-reference names it, and nothing it alone supplied survives in another source's distillation. The original binary and its sidecar are kept at `sources/removed/{slug}/`, stamped with the date and reason, so the corpus remembers what left and why.

Two halves:

- **Mechanical**: [`scripts/remove-source.py`](../../../scripts/remove-source.py) moves, deletes, edits the indexes, takes the source off the concept rows and rebuilds the derived indexes. Dry run by default.
- **Editorial**: this skill works through what the script can't decide, which is every other file that still draws on the source. That is the larger half. A source woven into a corpus is cited by name in other distillations' cross-references, joint index rows, task specs and agent prompts; in the demo corpus one source was named in about 30 other files.

## When to use

- A source is superseded: a policy replaced, a guide withdrawn, a new edition ingested as its own source.
- A source is no longer worth keeping: off-topic, low quality, or a duplicate of a better one.

## When not to use

- Re-ingesting a revised source under the same slug. Run `ingesting-resources`; it overwrites in place.
- Dropping one distillation (one source, one task axis). Delete the file and its index rows by hand, then build.
- A licence takedown that must also leave git history. This skill removes the source from the current tree; purging history and redeploying connectors are separate operator decisions.

## The rule for other files

**Remove what the source supplied, not just its name.** If a sentence keeps the idea and drops the citation, the claim stays in the corpus with no source behind it, which is worse than leaving the citation. For each passage that names the removed source:

- An entry about the removed source alone (a cross-reference row, a routing bullet such as *"route to `{slug}`"*, a signal-table row whose answer is that source) is deleted whole.
- A joint entry (*"Scrum Guide + Field Guide"*, a row naming two sources) is rewritten to keep only what the remaining sources supply. Never delete a joint entry whole: the remaining source's part stays, reworded if it read as half of a pair.
- **Support is settled by the remaining source's deep reference, never by its distillation alone.** Distillations synthesise across sources, so another source's distillation can already carry the removed source's content without naming it (a number, a rule, a named practice). Checking against that distillation would certify the very content being removed. A claim kept for a remaining source needs a line in its deep reference.
- When a need was routed to the removed source and a remaining source covers it, route it to the remaining practice that matches the need's scope, not the nearest name (a routine retrospective need goes to a retrospective practice, not to an incident postmortem).
- Prose that synthesises across sources is rewritten without the removed source's contribution. If the passage only made sense with it, delete the passage.
- After deleting a row, line or clause, read its neighbours: *"the default"*, *"as above"*, *"both"*, a count or a numbered list can now point at something gone.
- A section or table left empty is deleted, heading included, unless the template requires the section; then it says so plainly (*"No cross-references in this corpus."*).

Write each file as if the source had never existed: no "formerly", "removed" or "see also (retired)" notes.

**Scope is what the removal touches.** A misattribution or stale count that was already there, in a line the removal didn't need to change, is listed in the summary as pre-existing and left alone; fixing it here buries the removal in unrelated edits. A gap the removal opens is reported as a gap: never write new projection content (a row, a claim, a re-route a remaining source's distillation doesn't already carry) to fill it.

## Procedure

### 1. Confirm the target

Resolve the slug and corpus (bare name, e.g. `demo`). Ask the operator for the reason in one line; it is stamped on the retired sidecar.

Check the working tree is clean (`git status`), so the removal is one reviewable diff.

Read the source's light and deep references in full now, while they exist; `--apply` deletes them. Write down two lists:

- **Names**: the short names other files use for it (*"the Field Guide"*, *"Approach Perfect"*, an acronym).
- **Terms**: what only this source supplied, so it can be found where its name is gone: coined terms, named practices and rules, numbers and limits in the wording other files use (*"one or two"*), formulas, and the authors it cites (*"Prime Directive"*, *"Kerth"*, *"capacity-adjusted velocity"*). Another file can carry these without naming the source; a name search alone misses them.

Search each entry once before using it. One that also names something else (*"Field Guide"* also hits Dekker's field guide; the author's name hits the author's own lens and the licence notices) still goes in, but expect its hits to need sorting by hand.

### 2. Dry run

```bash
python3 scripts/remove-source.py --corpus {name} {slug} --reason "{reason}" --also "{name or term}" [--also ...]
```

Pass every name and term with `--also`. Matching ignores case and needs a word boundary before each entry, so a stem (*"co-facilitat"*) still matches its endings; an entry of five characters or fewer, or one in capitals (*"FLO"*, *"UDL"*), needs a boundary on both sides, and capitals also match case, so *"FLO"* finds *"FLO)"* and *"FLO,"* but not *"flow"*.

Read the output with the operator: the files that move and go, the index rows that go, the concept rows (and how many the source alone credits, which go too), and the list of other files that still name it. If a delete looks wrong, stop and find out why before applying. A file another source owns should never be on the delete list.

Then take the verbatim baseline, before anything is deleted, over every distillation in the corpus (you'll find files to edit later that aren't on the list yet): `python3 scripts/check-verbatim.py {corpus}/distillations/*/*.md > _planning/removals/{corpus}/{slug}.verbatim-before.txt`. Taken after `--apply`, the removed source's quotes already read as missing and the baseline can't tell old findings from new ones.

### 3. Apply

Rerun with `--apply`. It rebuilds each axis's `task-index.json` from the edited index views (the build ships them as committed, so they must be rebuilt here); if a view had drifted from its JSON before the removal, the rebuild brings that drift into this diff too, so say so in the summary. On the corpus's ingest machine, with Pass H staging in `_planning/`, the script edits the staging and reassembles `reference-index.json` and the concept index, then runs `check_topics`. On a fresh clone (`_planning/` is gitignored, so there is no staging) it edits the shipped indexes by ID instead, through the same writer, so both routes give the same concept index. Either way it ends with the slug-table check; every check must report ok.

Every untracked file the run changes or deletes is saved first, under `_planning/removals/{corpus}/{slug}/backup/`. To undo a run: `python3 scripts/remove-source.py --corpus {name} {slug} --restore`, then `git restore --staged --worktree -- .` for the tracked half. It writes its report to `_planning/removals/{corpus}/{slug}.json`: `index_rows_deleted` (rows and bullets that pointed only at the source), `index_rows_to_rewrite` (joint rows in the distillation indexes, and sections the removal left empty), `concept_rows_gone`, and `still_named_in` (every other file naming the source, with line numbers).

### 4. Rewrite what still draws on it

Work through `index_rows_deleted` first: each deleted row named a need (a situation, a phase, a quick-start case). Re-route it with a new row when a remaining source's deep reference covers that need at the same scope; otherwise it is a coverage gap for the summary. Then `index_rows_to_rewrite`, then `still_named_in`, applying **The rule for other files**. The list covers the names and terms you passed; search again for any you think of along the way. A term stays only where a remaining source's deep reference supplies it. Found only in a remaining source's distillation, it is the removed source's content carried there, and it goes. Found only in a remaining source's converted text, it has no reference behind it and goes too, though re-projecting that source could bring it back; say so in the summary. By kind:

- **Other distillations**: cross-reference sections, routing bullets, joint claims, and unnamed carried content found by the terms. When a sentence routes a need to the removed source and a remaining source plainly covers that need, route it there, after checking that source's deep reference supplies it. Afterwards run `check-verbatim.py` on the edited files and compare with the baseline: files often carry older findings, and only a new one is yours. A `[V]` quote that is now found nowhere is the removed source's words carried into another file; remove it.
- **Distillation indexes** (`{TASK}-DISTILLATION-INDEX.md`): the reference and situation cells of joint rows still name the source; rewrite them. A phase left with no rows goes, or takes a row from a remaining source that covers it.
- **Keep the three routing layers in step.** A need routed in a task spec (`tasks/*.md`) is routed again in its axis's operator index (`*-DISTILLATION-INDEX.md`), and the index view is what becomes the runtime `task-index.json`. When you re-route a need in one, find and change the matching rows in the other; rebuilding the JSON copies whatever the view says, omissions included.
- **Task specs** (`tasks/*.md`): a signal-table row whose answer was this source is re-routed when a remaining source's deep reference covers the need at the same scope, and goes otherwise; joint rows are rewritten; the source list loses its entry, and gains any remaining source you newly route to that it doesn't list. Check phase headings, success criteria and eval falsifiers too: a phase named after the source's practice is renamed for what remains, and a falsifier that needs the source is restated with the sources that remain. A design target the task took from the source (a number, a limit, a named step) goes with it, even where it reads as the task's own choice; name it in the summary so the operator can decide whether the axis wants it back from another source. If the removal leaves a phase with no source, say so in the summary as a coverage gap rather than inventing one.
- **Other sources' references** never change: a deep or light reference describes its own source, and a term the removed source shares with it (*"observer"*, *"Kerth"*) is that source's own. The sweep leaves `references/` out for this reason.
- **Other sources' sidecars** (`sources/original/*.source.md`): the provenance prose sometimes names sibling sources; drop the removed one. Never edit a source's converted or original text.
- **Build profiles, agents and lenses** (`build-profiles/*.md`, `.claude/agents/*.md` and their `.codex/agents/*.toml` twins, `lenses/*.md`): drop the source from lists and examples.
- **Repo files** (`README.md`, `builds.yaml`, `LICENSE-CONTENT`, `docs/` outside `docs/evals/`, skills under `.claude/skills/`, test fixtures under `tests/` that use the slug): drop the source from lists, licence tables and examples; if it is a worked example, swap in another source rather than leaving a dead one. Fix a count of sources or distillations only where it was right before the removal; a count that was already stale goes in the summary instead. An image whose drawing shows the source (a matrix picture listing its rows) needs redrawing; tell the operator, and leave its alt text matching the image until then.
- **Deploy configs** (`deploy/`): a hand-written connector (its instructions, tool descriptions, landing page, example slugs and selftest fixtures) is edited like any other file, then listed in the summary for redeploy. A generated `deploy/*/src/bundle.json` is never hand-edited; it is re-bundled.
- **The same role in many files**: when a hub source is removed, one phrasing (*"TC 25-20 and LFUO carry the protocol"*) recurs in many distillations. Check the role once against the remaining source's deep reference and apply the narrowed wording everywhere; a role the remaining source doesn't fill comes out rather than passing to it.

Leave history as it is: other sources' audit records under `references/_audit/`, eval rounds under `docs/evals/`, and dated snapshots in `_planning/`.

When done, rerun the search for the slug and every name and term; the only hits left should be history, `sources/removed/`, terms a remaining source supplies, and names that mean something else.

### 5. Audit the rewrites

The agent that wrote the rewrites can't audit them: it reads its own reasoning back as evidence. In both test runs that built this skill, the rewriting agent followed the rule and still credited a remaining source with more than its deep reference says, and a cold reviewer caught it each time. So a fresh reviewer, from another model family where one is available, checks every edit before the build:

```bash
python3 scripts/remove-source.py --corpus {name} {slug} --audit            # Codex, read-only
python3 scripts/remove-source.py --corpus {name} {slug} --audit --family claude   # no Codex: a fresh claude -p
```

The script packs the diff of every edited file, the removed source's light and deep references (kept at apply time) and this skill, hands the reviewer [`audit.md`](audit.md), and writes `_planning/removals/{corpus}/{slug}/audit/review-{n}.md`. It exits 0 on `Verdict: clean` and 2 otherwise.

Work through each high and medium finding. Check it against the deep reference it cites before acting; a reviewer can be wrong, and a finding you can't verify is reported, not applied. Apply the fix, or the smaller one the deep reference supports. Leave alone what the review lists as supported. Where two rounds disagree, the deep reference decides; note which line settled it.

Then run `--audit` again: each round audits the whole diff fresh, and every fix must pass through a round, so never end on unaudited fixes. Stop at a clean verdict. If the third round still finds something, fix it and run a fourth, and report whatever the fourth finds as open, with your reason, instead of fixing again. An attempt that fails without a review (a usage limit, a crash) is not a round; rerun it, or switch to `--family claude` and say in the summary that the remaining rounds were same-family.

### 6. Rebuild and verify

```bash
python3 -m scripts.build_indexes.build_task_index --corpus {name}   # the rewrites edited the index views after the script built their JSON
npm run build
npm run setup-chroma -- --corpus corpus.commons/{name} --rebuild   # if {corpus}/chroma/ exists
```

The build must pass. A failure on referential integrity means a file still links to one of the removed source's files, usually a doc that used it as a worked example; that is rewrite work left undone (*Rewrite what still draws on it*), not a build problem. Then confirm the source is gone from what ships: `grep -rlF {slug} {corpus}/apps {corpus}/okf` returns nothing beyond the copies of an image's alt text waiting on a redraw.

### 7. Summary

One screen for the operator:

- Source removed (citation), reason, ID retired.
- Files retired to `sources/removed/{slug}/`; count of files deleted.
- Concept rows: credits removed, and each row that went with it by name (`concept_rows_gone` in the report). For each row that lost the credit but survives (`concept_rows_kept`, with its aliases), check its name and aliases against your terms list: an alias only the removed source used comes out of `_planning/staging/{corpus}/concepts/decisions.json`, and a row still named with the removed source's coinage is flagged for re-filing. Reassemble afterwards (`python3 -m scripts.build_indexes.build_concept_index --corpus {name} --assemble`) and list every hand edit to staging here, since the audit diff doesn't show staging. A row can go although a remaining source covers the idea, because that source was never credited on it; the operator can credit it again with a re-filing pass (`refile_sources`).
- Index rows deleted and rewritten, per task axis.
- Other files rewritten, each with one line on what changed.
- Checks: index rebuilds, `check_topics`, slug table, `check-verbatim`, audit rounds and their verdicts, build, Chroma.
- Audit findings left open, each with the reason.
- Changes the rebuilds pulled in that aren't the removal: line counts in `reference-index.json` that had drifted from the references, a task index whose view had drifted from its JSON, a task index that changed `schema_version` because the axis dropped below the shard threshold. Name them so the reader of the diff doesn't take them for mistakes.
- **Left for the operator:** connector redeploys (any `deploy/*/src/bundle.json` that named the source), images that show it, and the commit. Read the diff before committing; it is the review of every editorial call this skill made.

## Related skills

- [`ingesting-resources`](../ingesting-resources/SKILL.md): the inverse.
- [`creating-distillations`](../creating-distillations/SKILL.md): its cross-reference section is what the rewrite step edits most.
- [`matching-references`](../matching-references/SKILL.md): find a remaining source that covers a phase the removed one left empty.
