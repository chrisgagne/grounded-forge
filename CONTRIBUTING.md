# Contributing

Three ways to contribute, in increasing order of investment:

1. **Issues.** File against any problem you can reproduce: a build failure, a broken cross-link, a distillation that disagrees with its source, an audit fixture the model handles wrong. Issues that name a specific file and line are the most useful kind.
2. **Code or content fixes.** PRs welcome against the substrate (skills, build system, docs) and against the demo corpus in `corpus.commons/demo/`. The demo is a worked example for forks; improvements to it improve the worked example. Match the existing style in the file you're editing.
3. **A corpus.** This is the largest contribution and the one with the most discipline attached. See below.

## Contributing a corpus

The repo ships one corpus in [`corpus.commons/demo/`](corpus.commons/demo/): a 26-source set anchored on the OpenStax twelve-book catalogue with supplementary methodology sources, projected onto five task axes. The `corpus.commons/` tier is plural by design: it can grow to hold many corpora, each contributed by an operator who has produced one.

A corpus contribution is a folder under `corpus.commons/{your-handle}-{corpus-name}/` containing the full self-contained corpus: sources (source-cards, converted markdown), references (light + deep), distillations (per task axis), lenses (optional), and a corpus-level README explaining what the corpus is for, who curated it, and what task domains it serves.

### Admission rule

**Everything in `corpus.commons/` must be redistributable under an open or open-nc licence.** Concretely:

- Every deep reference's `**Scope:**` line must be `open` or `open-nc`.
- Every `.source.md` sidecar's `scope:` frontmatter must match.
- The licence is named explicitly (the URL to the licence text is fine).
- If a source's licence is ambiguous, *don't include it*. The build's scope filter is one defence; the contributor's licence vetting is the load-bearing one.

If your corpus contains anything `copyrighted`, `confidential`, or `personal`, keep it in your own `corpus.local/`; that tier is gitignored exactly so you can hold mixed-scope material without it leaking into a public PR.

### Layout

Same as `corpus.commons/demo/`. Run [`creating-corpus`](.claude/skills/creating-corpus/SKILL.md) or `python scripts/create-corpus.py` to scaffold; the resulting tree is what the build expects.

```
corpus.commons/{your-handle}-{corpus-name}/
  sources/
    ingest/        # empty (operator's staging area; .gitkeep tracks the dir)
    original/      # one .source.md sidecar per source; binaries optional
    converted/     # one .md per source, the "tape" Pass C read
  references/      # light + deep references
  distillations/   # one subdirectory per task axis
    {task}/        # {TASK}-DISTILLATION-INDEX.md + per-source projections
  lenses/          # optional: lens specs + LENS-INDEX.md
  apps/            # build output per profile (regenerable, tracked so reviewers can browse)
  distros/         # tarballs from `npm run package` (gitignored; the README inside is tracked)
  README.md        # what this corpus is for; owner; scope; licence summary
```

### The discipline the protocol assumes

Every deep reference in `corpus.commons/` has passed the 9-pass ingestion protocol described in [`docs/architecture/ingestion-protocol.md`](docs/architecture/ingestion-protocol.md), including Pass I (the source-only audit). Contributions that bypass the protocol are not eligible: Pass I is the load-bearing audit gate and `corpus.commons/` is the tier that promises it.

If your corpus uses a non-standard ingestion approach (different conversion tooling, additional passes, custom evidence-classification markers), document it in the corpus-level `README.md` so future readers understand what discipline backs the content.

### Namespacing

The slug under `corpus.commons/` should namespace under your handle or organisation: `corpus.commons/chrisgagne-management-sciences/` or `corpus.commons/anthropic-cookbook/`. Attribution is in the path. PRs vouch for the licence claim under the contributor's name.

### Process

1. Open an issue first if the corpus is large (>10 sources) or contentious; easier to align before authoring than at PR-review time.
2. Submit the PR with the full corpus directory plus a corpus-level README naming what the corpus is for, scope range, licence summary, source list with URLs, and any non-default ingestion choices.
3. Reviewers will spot-check Pass I audits, scope claims, and a handful of citations. The goal is corpus integrity, not exhaustive re-audit.
4. On merge, the corpus is tracked in `corpus.commons/`. The build admits it once you point a profile at it via `builds.yaml`.

## Pre-push audit

The repo ships a pre-push audit at [`scripts/git-hooks/pre-push`](scripts/git-hooks/pre-push). It runs seven checks before any push to a remote: private-tier leakage, `.gitignore` correctness, credentials and absolute paths, internal markdown-link integrity, required supporting files, `LICENSE` shape (GitHub licensee compatibility), and conventional cruft. The rule is simple: audit before push, every time.

### Enable on your clone

```bash
git config core.hooksPath scripts/git-hooks
```

One-time, per clone. After that, `git push` runs the audit and stops the push if any check fails.

The hook honours `git push --no-verify` as the explicit override. Use it sparingly. Say why in the push commit message or the PR.

### What the audit covers and what it does not

- **Covers:** substrate files outside `corpus.commons/*/sources/`, `corpus.commons/*/apps/`, and `corpus.commons/*/build-profiles/`. Those three sit outside the audit's lane on purpose. Source content carries citation paths that are not repo-internal. Built-app output uses bare-path resolution from a different root. Build-profile templates resolve at deploy time.
- **Does not cover:** the *quality* of what you push. The audit is repo hygiene, not content review. Content review lives in the 9-pass ingestion protocol and the `audit-attribution` skill.

### Claude Code integration

If you use Claude Code in this repo, the audit also fires through [`.claude/settings.json`](.claude/settings.json) when Claude Code runs a `git push` Bash command. That layer is operator-level: it fires inside *your* Claude Code sessions. The git-side hook fires on terminal pushes by you or by any forker who turned on `core.hooksPath`.

### When the audit fails

Read the failure message. It names the check and the specific files. Three patterns and how to handle each:

- **Private-tier leakage:** a tracked file under `corpus.local/`, `projects.local/`, `_planning/`, or `_evals/`. Move the file out of the private tier, or add the path to `.gitignore` and `git rm --cached` the file. Do not `--no-verify` past this.
- **Credentials, tokens, operator home paths:** quote the line, redact, recommit. Do not `--no-verify` past this either.
- **Broken markdown links:** fix the link target or drop the reference. `--no-verify` is fine only when the broken link points at a known deferred file that lands in a later commit.

The script is shell. It reads as documentation. If a check fires for the wrong reason in your work, the script is where to refine it.

## A note on tone

The repo prefers direct, precise prose. Match it. Throat-clearing ("In this section we will discuss…") and puffery ("This revolutionary framework…") both go; say what something does and why, and if it doesn't do something important, say why. UK English spelling in docs (per the conventional house style); the codebase doesn't have many spelling-relevant identifiers.
