# Pass I, apply leg: close the audit of `${slug}`

Work from the repo root. Corpus `${corpus}`. The packet folder is `${packet}`.

Two audits have run on the deep reference `${deep}`: a fix-in-place audit (log at `${log}`) and a blind audit (`blind-findings.md` in the packet). A sort leg (`sort.md` in the packet) then checked both against the source and listed **Remaining edits**.
${notes}
## Step 1: verify and apply the remaining edits

Read `sort.md` in full, then the current deep reference. For each remaining edit, open the tape (`${tape}`) and, where the edit concerns a chart, figure or image-only text, the original (${original_line}; render a page with `pdftoppm -r 110 -f N -l N -png` into `$$TMPDIR`, at most ${render_cap} renders, and stop at the first failed render). Apply an edit only if the source supports it; you may tighten the wording to match the source more closely. Never apply one blind. Record each edit as applied, applied with changed wording (say how), or declined (say why, with the source line). Settle each disputed finding against the source the same way. Then run `python3 scripts/check-verbatim.py ${deep}` and fix any real mismatch.

Don't stamp the deep reference or touch any "Pass I has not run." line; the driver does that.

## Step 2: bring the derived tier into line

The light reference (`${light}`) and the distillations (`${corpus}/distillations/*/${slug}-*.md`), where they exist, were derived from the pre-audit deep reference. Read the fix-in-place log's list of changed claims, your own applied edits, and each derived file in full. Wherever a derived file carries a claim the audited deep reference no longer supports (or supports only in a narrower form), rewrite it to the deep's current claim, anchor and marker. Remove any header text saying the file is provisional, pre-audit, or needs re-deriving. Distillations of copyrighted, confidential or personal sources carry no `[V]` token. Also correct this source's rows in the `{TASK}-DISTILLATION-INDEX.md` files where they carry a changed claim. Run check-verbatim on each derived file you edit.

## Rules

Don't run Pass H scripts, edit JSON indexes, stamp anything, stage or commit, or edit files of any other slug.

## Report

Write `${packet}/apply-report.json`, then give a short final message. The JSON has exactly these keys:

- `same_family`: claims audited and corrected by the fix-in-place audit, from its log (e.g. "357 claims audited, 10 corrected").
- `sort_result`: one sentence with the sort's counts as it states them (confirmed, missed, over-flagged by each auditor, disputed, gate verdict).
- `applied_note`: one sentence: how many remaining edits were applied as written, applied with changed wording, and declined, naming any declined or changed one briefly.
- `gate`: `"pass"` when every confirmed defect is now fixed in the deep reference and check-verbatim is clean; otherwise `"fail"`.
- `open`: a list of strings, one per question the operator must settle (a finding you couldn't settle against the source, a coverage gap, a needed re-read). Empty when there is none.
- `derived_changes`: a list of strings, "file:line before → after".
