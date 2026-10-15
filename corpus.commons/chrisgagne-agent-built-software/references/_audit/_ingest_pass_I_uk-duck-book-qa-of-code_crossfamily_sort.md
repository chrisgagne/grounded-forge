## 1. What I read

Read in full:

- `sort-brief.md`, the three calibration fixtures and `pass-i-spec.md`, before reviewing the findings.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, all 508 lines.
- Repository `CLAUDE.md` and its required architecture documents.

Compared `frozen-deep.md` with `post-audit-deep.md`. Exactly seven lines changed: 279, 286, 317, 363, 401, 477 and 497. I independently checked every raised finding against the relevant tape passages, including linked URLs, figure directives and captions. This was a sort of the two audits, not another full-tape audit.

The post-audit hash matches `post-audit-deep.sha256`:

`0008d32fc61c12c7c44aaee76a86d6259825452357c33cf8aaaccac5e8a2cc61`

The tape independently measures 6,656 lines, 49,425 whitespace-delimited words and 19 file markers. Its hash matches the reference:

`7126cd8914ce6f28cee79a546a25fe5043e19743fa3e5f2f660d2192de9b0708`

All 19 tape files are represented in the deep reference. No `source.*`, acquisition manifest, original TOC or image files were supplied in this folder.

No files were edited.

## 2. Sorted ledger

“Fixer” includes findings recorded under **Open items** and **Checked and left as is**, not just its seven edits. Counts use independently correctable claim locations: repeated defects in different claims count separately; closely related clauses within one paragraph count together. Thus blind finding 1 becomes three records, finding 2 becomes four, and finding 8 becomes two.

### Confirmed and fixed

| ID | Post-audit line | Tape line(s) | Raised by | Decision |
|---|---:|---:|---|---|
| C1 | 317 | 4799–4803 | Fixer, change 3 | “Most informative” dropped **Perhaps**. “Were perhaps the most informative part” correctly restores the hedge. |
| C2 | 363 | 5727–5730 | Both: fixer change 4; blind finding 6 | An unfinished task was presented as evidence of insufficient breakdown. The source asks readers to **consider whether** it was sufficiently broken down. The fix correctly restores that invitation. |
| C3 | 401 | 6576–6583 | Fixer, change 5 | “Leaving the user a reverse-centaur” made a possible outcome categorical. “May turn into” correctly preserves the source’s possibility. |
| C4 | 477 | 1805, 1817; whole-tape search | Fixer, change 6 | The source names the principles using their full phrases; neither abbreviation appears in the tape. Replacing **YAGNI, DRY** with those phrases satisfies the source-vocabulary requirement without changing the concepts. |
| C5 | 497 | 6583 | Fixer, change 7 | “Turns the user” repeated the categorical reverse-centaur claim. “Can turn” correctly restores possibility. This is a separate claim occurrence from C3. |

### Confirmed, fix wrong or incomplete

None of the applied fixes is wrong. These confirmed defects were identified by the fixer but left unresolved.

| ID | Post-audit line | Tape line(s) | Raised by | Decision |
|---|---:|---:|---|---|
| C6 | 5 | 1–6, 51–63; no commit metadata supplied | Both: fixer open item; blind finding 1 | The acquisition commit and date are asserted without the evidence needed to verify them. This is an unsupported provenance claim, not a demonstrated false commit. No fix was applied. |
| C7 | 501 | Whole-tape search; independently measured tape properties | Both: fixer open item; blind finding 1 | Commit/date, original TOC order, removed front matter/imports, byte-for-byte preservation and agreement with a manifest remain unverified. The measurable tape properties are correct. No fix was applied. |
| C8 | 507 | 2352–2359, 3292–3300, 4352–4359, 6219–6226, 6334–6341, 6587–6594 | Both: fixer open item; blind finding 2 | The tape establishes remote URLs and image references. It does not establish copying status or the contents of a missing manifest. The fixer specifically raised the unsupported manifest assertion here and left it unchanged. |
| C9 | 106 | 741–747 | Fixer, calibration note | The fixer explicitly recognised the lost hedge but accepted it. “This is … frustrating” strengthens “can be frustrating”, especially where manual steps are difficult to replicate quickly. Restore possibility. |
| C10 | 488 | 741–747 | Fixer, calibration note | The same strengthening recurs in a separate framed-against claim. Restore “can be frustrating” here too. |

### Missed by the fix-in-place audit

| ID | Post-audit line | Tape line(s) | Raised by | Decision |
|---|---:|---:|---|---|
| C11 | 7 | All 19 file markers; original `_toc.yml` absent | Blind, finding 1 | The supplied sequence is observable; its agreement with the repository’s original TOC is not. The fixer’s open item did not specifically identify this structure-line assertion. |
| C12 | 32 | 2352–2359 | Blind, finding 2 | The Wikimedia directive is remote, but “not copied” is unsupported acquisition metadata. |
| C13 | 34 | 3292–3300 | Blind, finding 2 | The xkcd directive is remote, but “not copied” is unsupported acquisition metadata. |
| C14 | 35 | 4352–4359 | Blind, finding 2 | The xkcd directive is remote, but “not copied” is unsupported acquisition metadata. |
| C15 | 60 | 68–79 | Blind, finding 3 | The accessibility summary omits **most** for keyboard, speech-recognition and screen-reader access, and omits the exclusion of referenced third-party content. These qualify the represented commitments. |
| C16 | 269 | 3791–3794 | Blind, finding 4 | “A data breach is unauthorised access” substitutes actual access for the source’s condition that unauthorised individuals **may access** accidentally included sensitive information. |
| C17 | 287 | 4378–4387, especially 4381 | Blind, finding 5 | “DBMSs manage access and concurrency” loses **usually** from the source’s capability statement. |
| C18 | 395 | 6320–6324 | Blind, finding 7 | One terminal `[BT]` covers borrowed findings, the chapter’s organisational inference, and its uncited environmental and ethical commentary. Those evidence classes need separating. |

### Over-flagged

| ID | Post-audit line | Tape line(s) | Raised by | Decision |
|---|---:|---:|---|---|
| O1 | 286 | 4372–4373 | Fixer, change 2 | **Over-flagged by the fixer.** “Horror stories” is present in the cited URL’s path. Calling the linked material the group’s “horror stories” introduces no unsupported substantive claim. The fixer itself accepts a comparable URL-derived description of the Aqua book at line 473. The replacement is also source-supported and can remain. |

### Disputed

| ID | Post-audit line | Tape line(s) | Raised by | Both readings and disposition |
|---|---:|---:|---|---|
| D1 | 279 | 4148–4149, 4189–4190 | Fixer, change 1; blind expressly disagrees | **Narrow reading:** only YAML and TOML are expressly associated with “compact and human-readable”; assigning that description to all four named formats exceeds the passage. **Broad reading:** “formats like YAML and TOML” describes a general category introduced immediately beforehand, so the original is reasonable compression. The wording does not settle that scope conclusively. Retain the fixer’s narrower wording, which is directly supported. |
| D2 | 175 | 1265–1268 | Blind, finding 8 | **Omission reading:** an explicit packaging/distribution boundary belongs beside the packaging summary and helps prevent overestimating the section’s coverage. **Summary reading:** line 175 reports recommendations, without claiming to explain packaging procedures; complete reading coverage does not require reproducing every scope statement. The omission is real, but a mandatory Pass I defect is not established. |
| D3 | 379 | 6269, 6271 | Blind, finding 8 | **Omission reading:** the transformer and post-training summary should preserve the authors’ explicit limits on further discussion. **Summary reading:** the paragraph accurately summarises the discussion actually supplied and does not promise comprehensive treatment. The missing boundaries are useful additions, but their omission alone does not demonstrate a false claim or missing-chapter failure. |

D2 and D3 are excluded from the required edits and capture counts. Line 502 says every tape line was read; it does not say every source statement was reproduced.

### Defects introduced by fixer edits

**None confirmed.** All seven replacement passages trace to the tape. The disputed configuration narrowing and the unnecessary spreadsheet rewording remain faithful to it.

The fixer’s derived-tier observations concern files outside this bundle. I have not independently verified those observations and do not count them as deep-reference defects. Line 508’s pending status is an administrative item deliberately reserved for the driver, rather than a source-grounding finding.

## 3. Remaining edits

These are exact changes to the current `post-audit-deep.md`. Line numbers refer to the unchanged, hash-verified file.

1. **Line 5 — strip unsupported acquisition metadata.**

   Current:

   > at commit fa39f2089905fe07c08ae4d66671736a1becd3c5 (2026-06-09)

   **Strip**, including its preceding space. Keep the repository URL and following full stop.

2. **Line 7 — replace the complete structure introduction.**

   Current:

   > **Structure:** A root page and 18 chapters, in the order of the repository's `book/_toc.yml`, concatenated into one tape with a `<!-- file: book/{name}.md -->` marker before each file:

   Replacement:

   > **Structure:** A root page and 18 chapters, in the order presented in the supplied tape, with a `<!-- file: book/{name}.md -->` marker before each file:

3. **Line 32 — remove the copying assertion.**

   Current:

   > remote Wikimedia image (not copied),

   Replacement:

   > remote Wikimedia image,

4. **Line 34 — remove the copying assertion while retaining the alt-text description.**

   Current:

   > remote xkcd "Documents" comic (not copied; alt describes poor file naming);

   Replacement:

   > remote xkcd "Documents" comic (alt describes poor file naming);

5. **Line 35 — remove the copying assertion.**

   Current:

   > remote xkcd ".NORM Normal File Format" comic (not copied).

   Replacement:

   > remote xkcd ".NORM Normal File Format" comic.

6. **Line 60 — replace the accessibility-list clause.**

   Current:

   > lists what users should be able to do (change colours and fonts, zoom up to 300%, navigate by keyboard and speech recognition, use screen readers),

   Replacement:

   > excludes referenced third-party content and says users should be able to change colours, contrast levels and fonts, zoom up to 300% without text spilling off-screen, navigate most of the website using a keyboard or speech-recognition software, and listen to most of the website using a screen reader,

   Retain the management, keyboard-navigation, response-time and enforcement clauses and their citations.

7. **Line 106 — restore the frustration hedge.**

   Current:

   > this is time-consuming, frustrating and error-prone [AP]

   Replacement:

   > this is time-consuming and error-prone, and can be frustrating, especially where manual steps are difficult to replicate quickly [AP]

8. **Line 269 — restore potential access as the breach condition.**

   Current:

   > A data breach is unauthorised access through accidental inclusion in a remote repository;

   Replacement:

   > The book calls it a data breach if unauthorised individuals may access sensitive information accidentally included in a remote repository;

   Retain the response steps and existing citations.

9. **Line 287 — restore the DBMS qualifier.**

   Current:

   > DBMSs manage access and concurrency;

   Replacement:

   > DBMSs usually support authorisation of database access and concurrent access by multiple users;

10. **Line 395 — replace the final compound sentence and separate its markers.**

    Current:

    > A study by Anthropic "suggests" that LLM adoption, "especially if it is done quickly and aggressively" [V], can harm learning on the job, with possible implications for internal career progression and technical debt; negative impacts on psychological wellbeing (increased boredom, decreased motivation) have been measured; LLM code can contain critical security vulnerabilities, important for web-based platforms; and the chapter notes environmental costs (electricity and fresh water, especially in training) and ethical concerns (copyrighted training data, reproduced bias, offensive and harmful content) [BT] (book/generative_ai.md, "Vibe check failed - The risks of vibe coding").

    Replacement:

    > A study by Anthropic suggests that LLM adoption, especially when rapid and aggressive, can negatively affect learning on the job [BT]. The chapter identifies potential organisational implications for internal career progression and technical debt [AR]. It also cites measured negative impacts on psychological wellbeing, including increased boredom and decreased motivation, and material on critical security vulnerabilities in LLM-generated code, particularly relevant to web-based platforms and applications [BT]. The chapter additionally raises environmental concerns about electricity and fresh-water consumption, especially during training, and ethical concerns about copyrighted training material, reproduced bias, and offensive or harmful content [AP] (book/generative_ai.md, "Vibe check failed - The risks of vibe coding").

11. **Line 488 — restore the repeated frustration hedge.**

    Current:

    > Framed as time-consuming, frustrating and error-prone because inputs and outputs connect only through manual intervention [AP]

    Replacement:

    > Framed as time-consuming and error-prone because inputs and outputs connect only through manual intervention; these processes can be frustrating, especially where manual steps are difficult to replicate quickly [AP]

12. **Line 501 — replace the conversion-path note.**

    Current:

    > - **Conversion path.** The tape is a concatenation of the repository's Markdown at commit fa39f2089905fe07c08ae4d66671736a1becd3c5 (2026-06-09), in `book/_toc.yml` order, with front matter and MDX imports dropped and text otherwise byte for byte (per the acquisition manifest). Tape: `corpus.commons/chrisgagne-agent-built-software/sources/converted/uk-duck-book-qa-of-code.md`, 6,656 lines, 49,425 words, 19 files, sha256 `7126cd8914ce6f28cee79a546a25fe5043e19743fa3e5f2f660d2192de9b0708` (matches the manifest). MyST directives (figures, admonitions, tabs, epigraphs, list-tables, a `{todo}`) are kept as written and were read as part of the text. Code examples appear in Python and R tabs; this reference cites the prose and treats code as worked examples.

    Replacement:

    > - **Conversion evidence.** The supplied `tape.md` contains 6,656 lines, 49,425 whitespace-delimited words and 19 file markers; its sha256 is `7126cd8914ce6f28cee79a546a25fe5043e19743fa3e5f2f660d2192de9b0708`. MyST directives and Python and R code examples are present. The acquisition manifest and original repository files were not supplied, so the acquisition commit, date, original TOC order, removal of front matter and imports, and byte-for-byte conversion fidelity remain unverified. This reference cites the prose and treats code as worked examples.

13. **Line 507 — replace the figures note.**

    Current:

    > - **Figures.** Captions and alt text are cited above; the image files themselves are for the orchestrator to inspect. Three figures are remote and were not copied (the Wikimedia DAG image and two xkcd comics). The `gradient_descent.png` figure, nested inside the generative AI primer dropdown, is referenced in the tape but is absent from the manifest's image list. The two prompts in the centaur example exist only as images (`reverse-centaur-prompting.png`, `centaur-prompting.png`); the tape carries their alt text and captions, not their wording.

    Replacement:

    > - **Figures.** Figure captions and alt text are represented in the tape. Three figure directives use remote URLs: the Wikimedia DAG image and two xkcd comics. The tape also references `gradient_descent.png`, nested inside the generative AI primer dropdown. Image files and the acquisition manifest were not supplied, so copying status, manifest completeness and image contents remain unverified. The two centaur-example prompts are referenced as images (`reverse-centaur-prompting.png`, `centaur-prompting.png`); the tape carries their alt text and captions, not their wording.

## 4. Counts

These count claim-location records in the ledger, rather than the auditors’ differently grouped numbered findings.

| Classification | Count |
|---|---:|
| Confirmed defects, total | 18 |
| Confirmed and fixed | 5 |
| Confirmed, fix incomplete or not applied | 5 |
| Missed by the fixer and still defective | 8 |
| Over-flagged by fixer | 1 |
| Over-flagged by blind | 0 |
| Disputed | 3 |
| New defects introduced by fixer edits | 0 |

The fixer raised C1–C10, including its acknowledged but unchanged hedge losses and open provenance items. The blind auditor raised C2, C6–C8 and C11–C18. Their shared confirmed claims are C2, C6, C7 and C8.

Capture: fixer=10 blind=12 both=4

## 5. Gate verdict after remaining edits

**Pass**, once all 13 remaining edits are correctly applied.

They resolve every confirmed outstanding defect in this sort. The narrower configuration wording can remain; the disputed omissions do not establish missing-chapter coverage or false substantive claims.

This is a pass against the supplied tape. Acquisition provenance and image contents remain explicitly unverified. The driver should complete its audit-status update and stamping after applying and checking the edits.