# chrisgagne-agent-built-software

A corpus under the `corpus.commons/` tier.

## What this corpus is for

_One paragraph: the domain, the kind of question the corpus is built
to answer, who curated it, what task axes it serves._

## Task axes

- `distillations/warranting-agent-built-software/`

## Scope and licence

Everything in this corpus must be redistributable under an open or open-nc licence. See `../../CONTRIBUTING.md` for the admission rule.

## Layout

```
sources/ingest/        # drop material here, then run ingesting-resources
sources/original/      # one .source.md sidecar per ingested source
sources/converted/     # the markdown Pass C reads
references/            # light + deep references; REFERENCE-INDEX.md
distillations/{task}/   # per-task projections; per-task index
lenses/                # optional lens specs; LENS-INDEX.md
.claude/skills/        # corpus-bound skills (substrate skills stay at repo root)
apps/                  # build output per profile
distros/               # tarballs from `npm run package` (empty until shipped)
```
