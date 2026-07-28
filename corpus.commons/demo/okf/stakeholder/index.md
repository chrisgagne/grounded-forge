---
okf_version: "0.2"
---

# demo — stakeholder knowledge bundle

An Open Knowledge Format (OKF v0.2) bundle emitted by grounded-forge/0.4.0. Each task axis is a directory of concept files; each concept file is one source projected onto that task under a 9-pass, source-only ingestion protocol, with evidence markers and attribution preserved in-band.

## Task axes

- [stakeholder-engagement](stakeholder-engagement/index.md) — 27 concept files

## Lenses

- [lenses](lenses/index.md) — 6 per-distillation modifiers

## Evidence markers

Claims in concept files carry in-band evidence classification from ingestion:

- `[V]` verbatim — exact source text, audited against the source.
- `[AP]` attributed paraphrase.
- `[AR]` attributed argument (the author's reasoning, restated).
- `[AE]` attributed example.
- `[BT]` borrowed-through — a discipline carried via an openly licensed source rather than its canonical (non-open) author.

## Provenance and trust

Concept files declare `generated.by: grounded-forge/0.4.0`; `generated.at` is the source distillation's last change date. They deliberately do not declare `verified:` — the ingestion audit (Pass I) is a same-model-family, source-only consistency check whose receipts live at corpus level in the producing repository, not the independent confirmation OKF's `verified:` field asserts. Treat every concept file as machine-generated under an audited protocol; the audit trail is one repository upstream.

## Licence

Most-restrictive scope across sources: **open-nc**. Per-source scope and licence: [LICENCE-MANIFEST.md](LICENCE-MANIFEST.md).
