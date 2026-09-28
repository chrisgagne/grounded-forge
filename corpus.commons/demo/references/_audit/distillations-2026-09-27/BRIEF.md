# Distillation audit — brief (findings only)

You are auditing one distillation from the demo corpus of a research library. A distillation projects one source onto one task (decision-making, stakeholder engagement, AAR, retrospectives, software business). Its claims must trace to the source's **deep reference**, which has itself been audited against the source. You did not write the distillation.

Repository: ``

## Read, in this order

1. `.claude/skills/creating-distillations/projection-protocol.md` — what a distillation may and may not contain.
2. The distillation, in full.
3. Its deep reference, in full: `corpus.commons/demo/references/{slug}-deep.md` (slug = the distillation filename minus `-{task}.md`).
4. As needed: `corpus.commons/demo/sources/converted/{slug}.md` to check a quotation, and other sources' deep references to check what the distillation says about them.

Full coverage is a gate: read the distillation and the deep reference end to end. If you cannot, say so in `read_coverage` and mark the audit partial.

## What to check

Every claim: prose, list items, table cells, questions' embedded premises, the worked example, and the integration section.

- **Trace.** Which passage of the deep reference supports it? A claim the deep reference does not contain is UNSUPPORTED, even if it is true.
- **Applied guidance** (questions to ask, what to look for, anti-patterns, worked-example steps) is allowed: it is the distillation's job. It fails only if it rests on a premise the source does not support, or attributes the guidance to the author when the source does not give it.
- **Worked example.** It may be hypothetical. It fails if it presents an outcome, figure or result as the source's finding or as the framework's demonstrated effect when the deep reference reports no such thing.
- **Attribution.** Right author, right chapter or section, right concept name. Watch for a definition attached to the wrong concept and for positions the author rejects presented as the author's.
- **Quotations and markers.** `[V]` = the author's words, word for word in the converted source. `[BT]` = the source relaying someone else. `[AP]` = paraphrase. Flag a marker that does not fit.
- **Integration with other references.** Each claim about another corpus source must match that source's deep reference. Open it and check.
- **Numbers and counts.** Check every figure, count and enumeration against the deep reference.

Grades: FAITHFUL, MINOR-DRIFT (supported but loosened, mis-cited, or marker wrong), UNSUPPORTED, CONTRADICTED.

## Output

Write a single JSON object to the output path you were given:

```json
{
  "distillation": "<path>",
  "auditor": "<model>",
  "read_coverage": {"distillation": "lines 1-N of N", "deep": "lines 1-M of M", "complete": true},
  "claims_audited": 0,
  "tally": {"faithful": 0, "minor_drift": 0, "unsupported": 0, "contradicted": 0},
  "findings": [
    {"id": "D001", "line": 0, "section": "...", "claim": "...", "grade": "...", "failure_mode": "...", "evidence": "<deep-ref or source line numbers and what they say>", "fix": "strip | correct: <exact replacement> | re-mark: <marker>"}
  ],
  "notes": "..."
}
```

List every non-FAITHFUL claim. Edit no file other than your output.
