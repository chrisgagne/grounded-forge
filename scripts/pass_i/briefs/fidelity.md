# Pass I, fidelity check of the derived tier: `${slug}`

Work from the repo root. Corpus `${corpus}`, scope `${scope}`. You did not write any of these files.
${notes}
**Authority:** the audited deep reference `${deep}` (stamped on line 2), and behind it the tape `${tape}`. Read the deep reference in full first. Open the tape wherever a derived claim's wording or anchor needs checking against the source. Render no pages.

**Under check:** the light reference `${light}`, every distillation `${corpus}/distillations/*/${slug}-*.md`, and this source's rows in each `{TASK}-DISTILLATION-INDEX.md` (grep for the slug). Read each in full.

For every sentence and table row:
- **Light reference:** the deep reference says it, with the same anchor.
- **Distillations:** each source-grounded claim traces to the deep reference with the right anchor and marker; no claim the deep lacks; no hedge dropped, no scope widened, no quantity changed; nothing attributed to the wrong person; application and the distillation's own scripts are labelled as such, never presented as the author's claim; no evaluative labels or corpus-scope superlatives in the distillation's own voice. Copyrighted, confidential and personal sources: no `[V]` token and no verbatim run from the source beyond short names and labels.
- **Rows about other corpus sources** (integration tables, cross-references) are outside Pass I: check only that each named slug or file exists and the row claims nothing about *this* source the deep reference lacks.
- **Index rows:** trace to the distillation; column counts match the table header; no `---` inside a table.

Fix drift in place, as narrowly as possible. Run `python3 scripts/check-verbatim.py` on each file you edit. Don't stamp, run Pass H scripts, edit JSON, edit the deep reference, or stage or commit. If you find a defect in the deep reference itself, report it; don't fix it.

**Report:** write `${packet}/fidelity-report.md` with what you read, each fix (file, before → after, reason), counts of claims checked and fixed per file, and any deep-reference defect found. End it with a section `## Summary for the audit log`: one paragraph giving the counts and the kinds of fix, describing only the files and the source.
