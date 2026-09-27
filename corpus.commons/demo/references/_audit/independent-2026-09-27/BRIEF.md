# Independent Pass I audit — brief (findings only)

You are auditing one deep reference against the source it claims to describe. You did not write the deep reference and have no stake in it. Your job is the trace test: for every claim, find the passage in the source that supports it.

## Files in your packet

- `deep.md` — the deep reference under audit (a frozen copy; its sha256 is in `packet.json`).
- `source.md` — the converted source text. This is the only evidence. Your own knowledge of the author, the book, or the field is not evidence.
- `pass-i-spec.md` — the Pass I procedure and failure-mode reference. Read it first.
- `fixture-01-training-leakage.md`, `fixture-07-marker-mismatch.md`, `fixture-12-clean-negative-control.md` — calibration exemplars. Read all three before the deep reference. Fixture 12 is clean and must not be flagged: over-flagging costs as much as missing.
- `packet.json` — slug, file names, line counts, and any packet-specific note.

## Coverage rule (gate)

Read `deep.md` in full and `source.md` in full. Proceed to write findings only once both are read end to end. If anything stops a full read (context, errors, file damage), say so in `read_coverage` with exact line ranges, and mark the audit PARTIAL. A partial audit reported as complete is the one unacceptable outcome.

## What to audit

Every subject-matter claim: prose, table cells, list items, the thesis paragraph, evidence-class markers (`[V]` verbatim, `[AP]` author paraphrase, `[AR]` author argument, `[AE]` author example, `[BT]` borrowed-through), blockquotes, citations (chapter/page/section pointers), counts and enumerations, named people and works, and "Connections" claims about what the source cites.

Out of scope: the metadata header, licence and provenance notes, conversion notes, and structural tallies of the deep reference itself. Existing `<!-- AUDIT ... -->` comments are prior auditors' notes; judge the claims, not the comments.

Grade each claim:

- **FAITHFUL** — a passage supports it, with the right marker and citation.
- **MINOR-DRIFT** — supported in substance but with a dropped qualifier, a wrong or loose citation pointer, a marker that overstates (`[V]` on a paraphrase), or a verbatim quote with small wording slips.
- **UNSUPPORTED** — no passage says it. This includes source-external framing: evaluative labels, evidence-quality rankings, causal explanations, and "the author frames against X" oppositions the source does not make.
- **CONTRADICTED** — the source says otherwise (wrong count, wrong attribution, reversed meaning).

Prime yourself for the producer's known failure modes: attributions to people or works the source never names (training-data leakage); enumeration miscounts; dropped bounding qualifiers; dated-fact drift; `[V]` quotes that are not character-exact; claims placed in the wrong chapter; post-source vocabulary; task guidance (diagnostic questions, how-to advice) smuggled into the deep tier. The test is never "is this true?" but "which passage says it?" If you agree with a claim because you already know it, go and find it in the source.

## Searching the source

Search before you grade. Conversions render punctuation inconsistently: an em dash may appear as `—`, `--` or `---`; quotes may be curly or straight; line breaks may split a phrase; footnote markers may interrupt words. When a quoted phrase does not match, search a distinctive 3–5 word fragment with punctuation stripped before concluding it is absent. Record the searches you ran for every non-FAITHFUL finding.

Chapter and section structure: list the source's chapters/major sections, then check that the deep reference covers each. A readable chapter absent from the deep reference, without an operator-approved `coverage: partial` declaration, is a finding (`failure_mode: silent-partial-coverage`).

## Output

Return a single JSON object and nothing else, in this schema:

```json
{
  "source": "<slug>",
  "auditor": "<model name and mode>",
  "date": "2026-09-26",
  "deep_sha256": "<from packet.json>",
  "read_coverage": {"deep": "lines 1-N of N", "source": "lines 1-M of M", "complete": true},
  "claims_audited": 0,
  "tally": {"faithful": 0, "minor_drift": 0, "unsupported": 0, "contradicted": 0},
  "toc_check": {"source_sections": ["..."], "missing_from_deep": ["..."]},
  "findings": [
    {
      "id": "F001",
      "deep_line": 0,
      "claim": "<the claim, quoted or tightly paraphrased from deep.md>",
      "grade": "MINOR-DRIFT | UNSUPPORTED | CONTRADICTED",
      "failure_mode": "<short name, e.g. training-leakage, miscount, dropped-qualifier, marker-overstates, verbatim-slip, wrong-citation, source-external-framing, cross-corpus-drift, task-guidance-in-deep, silent-partial-coverage>",
      "source_check": "<what the source actually says, with source.md line numbers>",
      "searches": ["<pattern>", "..."],
      "fix": "<strip | correct: exact replacement text | mark-unverifiable>"
    }
  ],
  "notes": "<anything a repairer needs: conversion damage, sections you could not verify and why>"
}
```

List every non-FAITHFUL claim in `findings`. Count FAITHFUL claims only in the tally. Do not edit any file.
