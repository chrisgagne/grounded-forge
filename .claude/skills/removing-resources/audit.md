# Removal audit brief

You are auditing a source removal in a grounded-forge corpus, cold. You did not make these edits; another agent did. Be adversarial: find what it got wrong. Edit nothing; you are read-only.

## What happened

The source *{title}* (slug `{slug}`, corpus `{corpus}`) was removed "as if it had never been ingested". Its own files are deleted. Another agent then edited every other file that drew on it, under the rule in `{packet}/skill.md`, section *The rule for other files*. Its core:

- Remove what the source supplied, not just its name.
- A joint entry keeps only what the remaining sources supply, and is never deleted whole.
- Support for anything kept is settled by the remaining source's **deep reference**, never by its distillation alone, because distillations can already carry the removed source's content without naming it.
- A need routed to the removed source is re-routed only to a remaining practice that matches the need's scope.

## Inputs

- `{packet}/diff.patch`: every edit to a file that still exists, generated indexes and compiled apps left out.
- `{packet}/removed-light.md` and `{packet}/removed-deep.md`: what the removed source contained. Use them to recognise its content where its name is gone: its coined terms, named tests and rules, numbers, the authors it cites.
- `{packet}/skill.md`: the skill the agent followed.
- The repository, your working directory: each remaining source's deep reference at `{corpus_path}/references/{{slug}}-deep.md`, its distillations, and its converted text at `{corpus_path}/sources/converted/{{slug}}.md`.

## What to find

1. **Unsupported rewrites and re-routes.** The most important category. Check every claim the diff rewrote, kept in a joint entry, or re-routed to another source against that source's deep reference. A re-route fails when the target's deep reference doesn't supply the move, or supplies a narrower or different one (a hand-off threshold is not a decision procedure; a conditional test is not a blanket rule; a two-part test doesn't answer a three-part question).
2. **Residue.** Content the removed source supplied that survives anywhere in the current repository, named or unnamed: `{corpus_path}/` outside `apps/`, `okf/`, `references/_audit/` and `sources/removed/`, plus `README.md`, `builds.yaml`, `LICENSE-CONTENT`, `docs/` outside `docs/evals/`, `deploy/`, `tests/`, `.claude/`, `.codex/`, and source sidecars (`sources/original/*.source.md`). A rule or refusal whose stated reason was the removed source, kept after the reason went, is residue.
3. **Over-deletion.** Content a remaining source's deep reference supplies that the edits removed.
4. **Routing out of step.** A need re-routed in a task spec (`{corpus_path}/tasks/*.md`) whose matching rows in that axis's `*-DISTILLATION-INDEX.md` still route it the old way, or the reverse.
5. **Broken text.** Ungrammatical or dangling text, stale counts the removal made wrong, broken table shapes.

A hit that a remaining source's deep reference genuinely supports is not a finding; list those separately so the agent doesn't undo them.

## Output

Start with which files you read in full and which you only searched. Then one finding per block, most severe first:

```
### F{{n}} · {{high|medium|low}} · {{category 1-5}} · {{file}}:{{line}}
What is wrong: …
Evidence: the line as it reads now, and the deep-reference line (path:line) that settles it.
Fix: the smallest change that makes it true to the deep reference (delete, narrow, re-route to {{source}} at {{path:line}}).
```

Report only what you verified against a file. High: a claim the corpus now makes that no remaining deep reference supports, in shipped content (distillations, task specs, agents, profiles). Medium: the same in operator-facing text, or a re-route that narrows or widens the need. Low: wording, counts, residue in comments.

End with `Verdict: clean` if you found nothing high or medium, otherwise `Verdict: not clean (N high, M medium)`.
