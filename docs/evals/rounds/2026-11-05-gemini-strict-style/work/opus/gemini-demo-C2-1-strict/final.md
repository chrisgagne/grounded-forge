I read all four files in full, in order: `scoring-brief.md`, `cases.json`, `keys.json` and `packet.md`, which includes the whole legend of 45 chunks and the quotation-locations list. I graded each claim against the chunk its marker cites, so I didn't need the converted sources. The score file is at `./gemini-demo-C2-1-strict.score.json`, and its 55 graded citations match the 55 markers in the chat answer.

- **Citations graded:** 55
- **Supports / partial / none:** 15 / 39 / 1
- **wrong_book:** 0 yes, 55 no
- **Quotes exact / with a quotation:** 0 / 0. The one MISSING entry in the list is a misread by the quote checker: the flagged text is paraphrase around a one-word quoted term, so I graded no quotation.
- **Ideas present / credited:** 10 / 9, out of 13
- **sources_cited:** 10
- **Note:** Most markers are stacked on compound claims where each chunk carries only one part, hence the many partials. One control-cycle claim cites a chunk that says five stages, and one appraisal claim cites a control-process chunk with nothing on appraisal (the single none). One Columbia report chunk ends before the clause it is cited for, and one Army claim merges gate-task prerequisites with retraining.
