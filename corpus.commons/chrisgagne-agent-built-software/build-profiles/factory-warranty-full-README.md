# Factory Warranty (full)

A software factory for AI-built changes, and the open library its reviewers read: all 18 sources (NIST, CISA, OWASP,
Microsoft, OpenSSF, UK government assurance guidance, METR's productivity trial, SWE-bench, Google's DORA report and
others), projected onto eight stages of a change's life, from specifying it to releasing it.

It asks whether whoever signs off an AI-built change can rely on evidence instead of reading every line. The
[corpus README](../../README.md) has the whole story: what the factory does, every pre-registered test of it, the
results (including where its review doesn't beat the labs' own tools) and its limits.

## Use it

- **Ask the library.** Open this folder in Claude Code (`claude .`) and ask what evidence a change needs before you
  sign it off. The skills in `.claude/skills/` are `review-change` (review one change and write a plain-words
  sign-off sheet), `answer-from-corpus` and `matching-references`.
- **Review a change without installing anything.** Add `https://review.groundedforge.com/mcp` to Claude or ChatGPT as
  a custom connector and sign in with GitHub ([how](https://review.groundedforge.com/)). That's the review stage only.
- **Run the factory.** It needs macOS, Python 3.12+, [uv](https://docs.astral.sh/uv/), Claude Code, the Codex CLI,
  `gitleaks`, `osv-scanner` and `semgrep`:

  ```bash
  uv tool install --editable ./factory
  factory run STORY.md --repo PATH
  ```

  [`factory/README.md`](factory/README.md) covers the config and [`factory/DESIGN.md`](factory/DESIGN.md) what it
  guarantees and what it can't.

## Before you rely on it

- On a public benchmark, its review brief found no more than a plain "review this as a careful senior engineer" prompt
  on either Claude or OpenAI's model. What it adds is the gate around the review: tests locked before the build,
  sandboxed checks, a sheet a non-coder can sign from, and a tamper-evident log.
- Its rules (what blocks, the false-stop bar) are marked PROPOSED in [`factory/factory/policy.yaml`](factory/factory/policy.yaml).
- It runs on macOS only, and a signature is a record, not cryptography.

## What's here

| Path | What it is |
|---|---|
| `CLAUDE.md` | The guide an assistant reads first: the eight stages, demonstrated against asserted, the retrieval order |
| `distillations/warranting-agent-built-software/` | One write-up per source, and the stage router (`task-index.json`) |
| `concept-index.json`, `slug-table.json` | The concept index and the source IDs |
| `.claude/skills/` | `review-change`, `answer-from-corpus`, `matching-references` |
| `factory/` | The factory itself (MIT) |

## Licence

The code is MIT ([`LICENSE`](LICENSE)). Each write-up keeps its source's licence ([`LICENSE-CONTENT`](LICENSE-CONTENT)),
and several are share-alike, so keep their attribution when you quote. The DORA report is CC BY-NC-SA, which makes this
build non-commercial as a whole; `factory-warranty` is the same app without it, for any use.
[`DISCLAIMER.md`](DISCLAIMER.md) sets out the terms.
