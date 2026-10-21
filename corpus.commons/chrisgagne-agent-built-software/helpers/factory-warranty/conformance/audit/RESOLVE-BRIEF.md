# Resolving the blind audit of a matrix part

A blind auditor of another model family (Sol, gpt-6.1-sol) checked a conformance-matrix part and listed disagreements and missing rows. You resolve each one **by the source text and the code**, never by which party you trust more and never by your own view of what is good enough.

Read: `conformance/BRIEF.md` (the matrix rules and status definitions), the matrix file, the audit file, and, for each disagreement, the source lines and repo files both sides cite (read enough around them to be sure). Grep the repo to check any test, check or fixture either side names.

For each disagreement decide one of: **audit right** (edit the matrix row to match), **matrix right** (leave it), or **neither** (edit to what the source and code support). For each missing row: add it if the source supports it in the matrix's scope, or record why not. Then update the matrix header's counts per status so they match the table.

Write `conformance/audit/resolution-<part>.md`: one line per item, `| Row ID | Field | Decision | Basis (source line or file:line) |`, then the new counts. Edit only the matrix file and your resolution file. Your final message: the counts of each decision, the status changes, and the new counts per status.
