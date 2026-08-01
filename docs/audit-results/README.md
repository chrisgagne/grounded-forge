# Pass I audit logs

Pass I of the 9-pass ingestion protocol is the source-only audit: every claim, table cell, evidence-class marker, and cross-reference in a deep reference is read cold against the converted source, and anything that cannot be traced to a passage is stripped or flagged. The deep reference does not ship until Pass I passes.

**Pass I must run in a fresh context — and preferably a different model — from the one that produced the deep reference.** An in-context self-audit is blind to the training-priors the producing session just wrote in: it reads them as source-grounded and passes them, certifying its own fabrications as "verified at source." Independence is what makes the read actually cold, and it is the only thing that catches a confident hallucination the producer believes. See [`source-integrity.md`](../architecture/source-integrity.md).

## Status of the demo corpus

The demo corpus was audited **in-context** — each deep reference audited within the session that produced it — which predates the independence requirement above, and that audit cannot be relied on as verification. An in-context source-only audit passes the producer's own confident errors: attributions to people the source never names, and enumerated counts the source contradicts, both stamped "confirmed at source." The demo corpus is therefore **pending a fresh, independent re-audit**, and its deep references should be treated as producer-drafted until then.

The per-source in-context audit logs remain in the source repo under [`corpus.commons/demo/references/_audit/`](../../corpus.commons/demo/references/_audit/) as the record of what the in-context audit reported — not an independent-verification guarantee. They are excluded from the compiled distribution.

## What a single audit pass buys

A single source-only audit reduces injected error but does not eliminate it, and the residual is hard to quantify with one auditor. What is defensible: an independent pass lets substantially more claims be extracted from the source without adding grep-verifiable fabrication (a named source, person, or work absent from the text) that the producer would otherwise ship uncaught. Residual error falls with repeated, independent checks — at ingestion or at run time — and with more capable producing models. It is not that one pass is sufficient; it is that an independent pass helps enough to make dense, source-cited extraction worth more than sparse, un-audited extraction.

## What Pass I does and does not catch

Pass I verifies fidelity to source. It does not and cannot verify quality of source. A source-only protocol against a derivative or fashionable source produces a faithful projection of derivative or fashionable content. **Source selection is the operator's job and the rule the protocol does not enforce.** See [`source-integrity.md`](../architecture/source-integrity.md) for the integrity rule and what it covers.

For the empirical question of whether pre-projection improves end-user answer quality compared with generic retrieval, see the [comparative eval methodology](../evals/methodology.md) and harness shipped alongside.

## Reading the per-source logs

Each `_ingest_pass_I_{slug}_source_audit.md` file documents the audit procedure for that source (how the cold read and verification were performed), the fixes applied during that audit with locations, spot-checks, and notes for future re-ingestion. The log is the historical integrity record for the in-context audit; a fresh, independent re-audit is what will supersede it.
