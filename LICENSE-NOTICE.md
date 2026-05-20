# Licence notice

The repo ships under a two-tier licence. Code is MIT. Content carries the share-alike obligation it inherits from upstream sources.

## Substrate tier — MIT ([`LICENSE`](LICENSE))

The MIT licence covers the *substrate* tier:

- All code (scripts, build system).
- Architecture documentation under `docs/architecture/`.
- The vocabulary reference at `docs/reference/vocabulary.md`.
- Build profile templates under `corpus.commons/{corpus}/build-profiles/` and `corpus.local/{corpus}/build-profiles/`.
- Skill specifications (every `SKILL.md` under `.claude/skills/` and under any corpus's `.claude/skills/`).
- Index frames: per-task `INDEX.md` operator views and the runtime JSON indexes (`slug-table.json`, `concept-index.json`, `reference-index.json`, `task-index.json`), each living inside the corpus root it describes.

## Content tier — see [`LICENSE-CONTENT`](LICENSE-CONTENT)

The *content* tier — references, distillations, lenses, source sidecars, and long-form prose (`README.md`, `CONTRIBUTING.md`, `DISCLAIMER.md`, `LICENSE-CONTENT`) — sits under [`LICENSE-CONTENT`](LICENSE-CONTENT).

Third-party-derived material stays under its upstream licence as recorded in `LICENSE-CONTENT` Section 2.

## Why two files

GitHub's licence-detection tool reads `LICENSE` and expects canonical licence text with no preamble. Keeping `LICENSE` as pure MIT text lets the About panel show the licence cleanly; this `LICENSE-NOTICE.md` carries the dual-tier explanation that used to sit at the top of `LICENSE`.
