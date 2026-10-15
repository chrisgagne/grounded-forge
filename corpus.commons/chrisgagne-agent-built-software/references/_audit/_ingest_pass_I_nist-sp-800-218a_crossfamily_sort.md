## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md`, and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, lines 1–332.
- `tape.md`, lines 1–1172, including all Table 1 columns, references and glossary.
- `source-card.md`, repository operating instructions and the required architecture documents.

Compared the frozen and post-audit references: only lines 97 and 318 changed. Verified that the post-audit checksum matches `post-audit-deep.sha256`.

Checked `source.pdf` metadata and checksum. Its complete deterministic `pdftotext -layout` extraction equals `tape.md` byte for byte. I did not visually inspect rendered PDF pages.

Ran `check-verbatim.py` against `post-audit-deep.md` with `tape.md` explicitly supplied: **no findings**. No files were edited.

## 2. Sorted ledger

| Finding | Raised by | Post-audit line | Source evidence | Classification and decision |
|---|---|---:|---|---|
| AI RMF entries described as “function names and numbers” | Fixer | 97 | Tape 480–491, p. 7; identifier examples at 518–529, p. 8, and 606–615, p. 10 | **Confirmed and fixed.** The Profile supplies names and numbered identifiers but does not call Govern, Map, Measure and Manage “functions”. That technical classification imports knowledge of the cited framework. The replacement, “a name and number”, describes the displayed entries without adding that classification. |
| PDF creation date changed from `2024-07-26` to `2024-07-25, UTC−04:00` | Fixer | 318 | Original PDF metadata; no tape passage. Raw creation timestamp: `D:20240725200545-04'00'` | **Disputed.** The fixer’s reading treats “PDF metadata … created” as reporting the date in the metadata’s recorded offset; under that reading, 25 July is appropriate. The alternative reading reports the same instant converted to UTC or the operator’s timezone: it is 26 July in both UTC and New Zealand time. I reproduced both conversions. The original unqualified date is ambiguous, rather than demonstrably false. The replacement resolves the ambiguity correctly and should remain. |
| “Pass I: see the stamp on line 2 and the audit log” points to a blank line | Both: blind finding 1; fixer’s “Left open” | 330; target line 2 | No tape passage applies: this is an internal audit-status claim. Line 2 remains blank in the supplied post-audit artefact. | **Confirmed, fix incomplete.** The blind auditor requests a strip. The fixer independently recognises the missing stamp but leaves the sentence for the driver. A future stamp may repair the reference, but the current artefact still contains the dangling claim. Strip the sentence. |

**Missed by the fix-in-place audit:** none. The remaining line-330 defect was explicitly recognised by the fixer, so it is an unresolved finding shared by both auditors, rather than a blind-only miss.

**Over-flagged:** none. The creation-date finding is classified as disputed because its status depends on the intended timezone convention.

**Fix-introduced defects:** none. Both changed passages remain source-faithful: line 97 now describes the displayed identifiers, and line 318 accurately reports the PDF’s recorded date and offset.

The fixer’s caution about `[BT]` on lines 306–308 does not establish another defect. SBOM/SLSA, FISMA/OMB A-130 and OLIR are explicitly named in the source: tape 744–749, p. 13; 69–75, PDF p. 3; and 178–183, p. ii. The connection statements report those supplied relationships without importing external claims.

## 3. Remaining edits

1. **Post-audit line 330 — strip.**

   Current text:

   `**Pass I.** Pass I: see the stamp on line 2 and the audit log.`

   Replacement: **strip**.

   Verification: post-audit line 2 is blank; no completed Pass I stamp appears there. This correction rests on the artefact itself, since NIST’s source cannot substantiate its derivative reference’s audit status.

No further source-verified edits are required.

## 4. Counts

Counts use distinct defects, merging both auditors’ reports of the same claim.

| Classification | Count |
|---|---:|
| Confirmed defects, total | 2 |
| Confirmed and fixed | 1 |
| Confirmed, fix wrong or incomplete | 1 |
| Missed by the fix-in-place audit | 0 |
| Over-flagged — fixer | 0 |
| Over-flagged — blind | 0 |
| Disputed | 1 |
| Defects introduced by fixer edits | 0 |

The disputed creation-date finding is excluded from capture. Line 330 is included because it is a confirmed defect within the deep reference, and both auditors raised it.

Capture: fixer=2 blind=1 both=1

## 5. Gate verdict after remaining edits

**Pass**, once line 330 is stripped.

The supplied source supports the reference’s substantive content and section coverage. Neither fixer edit introduces a new defect, and the verbatim check reports no findings. This verdict permits the subsequent Pass I stamping and derived-tier provenance steps; it does not attest that those steps have already occurred.