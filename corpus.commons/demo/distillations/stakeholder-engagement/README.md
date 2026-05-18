# corpus.commons/demo/distillations/stakeholder-engagement/

Stakeholder-engagement distillations. One distillation per source, projecting the source onto stakeholder-engagement work. The *stakeholder-engagement* column of the matrix.

## What goes here

One distillation per source in the corpus, named `{source-slug}-stakeholder-engagement.md`. Each file follows the canonical distillation structure:

- `## Stakeholder-Engagement Relevance`, why this source matters for stakeholder work.
- `## Key Concepts for Stakeholder Engagement`, paraphrased from the source with parenthetical citations.
- `## Questions to Ask During Stakeholder Engagement`, phase-organised diagnostic tables. The canonical phase list lives in [`corpus.commons/demo/distillations/stakeholder-engagement/STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md`](STAKEHOLDER-ENGAGEMENT-DISTILLATION-INDEX.md); distillations use those phase names.
- `## What to Look For`, pattern / signal / diagnosis / follow-up entries.
- `## When to Use This Reference`.
- `## Example`, fictional, original. No verbatim source blockquotes.
- `## Anti-patterns This Reference Helps Avoid`.
- `## Integration with Other References`.

## What does not go here

- Verbatim source blockquotes. Distillations paraphrase concepts and cite parenthetically. Verbatim quotes live in the deep reference, where the evidence-class marker travels with them and Pass D exactness verification has run. Link to the deep ref rather than duplicating the quote.
- Material not traceable to the deep reference. Distillations derive from the verified deep, not from the source directly. If you need a claim that the deep doesn't carry, re-ingest the source so the deep gets it; don't smuggle the claim into the distillation.
- Author biographical material the source does not provide.
- Decision-making-specific guidance. That projection lives in `corpus.commons/demo/distillations/decision-making/`.

## How files are produced

Distillations are produced by the substrate `creating-distillations` skill — one source × one task axis per invocation, gated by a per-distillation applicability check. The input is the verified deep reference; the source is not re-read. When a new task axis is being assembled, the substrate `creating-applications` skill orchestrates the per-distillation invocations across the corpus.

The demo corpus ships 24 stakeholder-engagement distillations projecting the OpenStax corpus and supplementary sources onto this task axis. Pass G.0 (applicability gate) was honoured per source.
