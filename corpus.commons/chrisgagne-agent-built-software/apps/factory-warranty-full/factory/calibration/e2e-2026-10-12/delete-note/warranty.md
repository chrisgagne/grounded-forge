# Warranty pack: 20261012-162527-let-people-delete-a-note

**Change:** Let people delete a note  
**Repo:** `<scratch>/e2e/notes-app` · **branch** `factory/20261012-162527-let-people-delete-a-note` · **baseline** `56105efa0b80` → **head** `12adfe2758b0373e2cbbaad8edeea771a2b32855` (tree `2aebf24fe54b9f1fb2e4586265e60b693e0913f5`)  
**Builder:** claude  
**Assembled from ledger events** e001–e058 (`ledger.json`).

**Status:** READY TO SIGN

## Story

> # Let people delete a note
>
> People can create and read notes but can't get rid of one. They want to delete a note they no longer need.
>
> ## What we want
>
> - A signed-in person can delete one of their own notes.
> - Once deleted, the note is gone: it no longer shows in their list, can't be read by id, and its tags go with it.
> - Deleting a note that doesn't exist, or that belongs to someone else, looks the same to the caller as a missing note.
> - Nobody can delete a note without being signed in.

## Risk classes

- **auth**: keyword in story/acceptance: session. Required gates: none beyond the standard gates. Review focus: OWASP ASVS 5.0 V6 Authentication, V7 Session Management and V8 Authorization (V9 Self-contained Tokens and V10 OAuth and OIDC where tokens or OAuth are involved).
- **irreversible**: keyword in story/acceptance: delete, deletes, deleting. Required gates: none beyond the standard gates. Review focus: What can't be undone; is there a backup and a rehearsed restore?

Triage: pass (e030), phase diff.

## Demonstrated

Commands the driver ran, with exit codes and output hashes.

- [e016] tests:install `npm ci` exit 0, output sha256 `c674bbc82c220d3b`, log `tests/install.log`
- [e017] tests:baseline-tests `npm test` exit 0, output sha256 `17a2693d33efa3ea`, log `tests/baseline-tests.log`
- [e019] tests:new-tests `npm test` exit 1 (expected: red before the build), output sha256 `7213526d8d656799`, log `tests/new-tests.log`
- [e033] gate:install `npm ci` exit 0, output sha256 `eb75e4b59cacdf4e`, log `gate/install.log`
- [e034] gate:typecheck `npm run typecheck` exit 0, output sha256 `9b19c927d3113c8a`, log `gate/typecheck.log`
- [e037] gate:tests `npm test` exit 0, output sha256 `c5688bbe252919d6`, log `gate/tests.log`
- [e038] gate:perf `npm run perf` exit 0, output sha256 `e94e7fb378ba234c`, log `gate/perf.log`
- [e039] gate:secrets `gitleaks git --no-banner --redact --ignore-gitleaks-allow --log-opts=56105efa0b80cfa74712467886257ef8c5995bb0..HEAD --report-format json --report-path <scratch>/e2e/notes-app/.factory/changes/20261012-162527-let-people-delete-a-note/gate/gitleaks.json .` exit 0, output sha256 `1b819ec67936a373`, log `gate/secrets.log`
- [e041] gate:sast `semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-nosem --json --quiet --error --severity ERROR --severity WARNING -- ./docs/THEORY.md ./rollback.md ./scripts/rehearse-rollback.js ./src/notes/repo.js ./src/notes/routes.js ./test/notes.test.js ./test/summary.test.js` exit 0, output sha256 `d171af1ce2eaacac`, log `gate/sast.log`
- [e032] locked-test hash check: **pass**, 14 files

## Asserted, not evidence

The builder's own words. Nothing here was checked by running anything.

**Builder summary** (`builder-summary.md`):

> Signed-in people can now delete their own notes with `DELETE /notes/:id`. The full test suite passes (66 of 66, including all 11 acceptance criteria), and typecheck and perf pass too. The work is uncommitted, as the brief asks.
>
> ## What I changed
> - **`src/notes/repo.js`**: added `deleteNote(db, userId, noteId)`. In one transaction it deletes the note's tag rows, then the note row, both limited to the signed-in user's id in the SQL itself. It returns whether a note was actually deleted. I delete the tags explicitly rather than relying on the database's cascade, so they go even on a connection where foreign keys are switched off.
> - **`src/notes/routes.js`**: added `DELETE /notes/:id` behind the existing sign-in check, so no session or a bad one gets 401. A successful delete returns 204 with no body, using the existing `sendNoContent` helper. An id that isn't a whole number, a missing note, someone else's note and an already-deleted note all get the same 404 `{ error: 'Note not found' }` as reading a missing note.
> - **`docs/THEORY.md`**: added the new route to the API table. No rule in that file changes, since the new route follows the existing ones.
> - **`rollback.md`** and **`scripts/rehearse-rollback.js`**: the brief requires these because the change includes a delete. There's no migration, so undoing the change is just reverting the code. Reverting won't bring back notes that were already deleted, because the rows are really gone; they can only be recovered from a database backup. `rollback.md` gives the SQL to restore one note and its tags from a backup. The rehearsal script runs that against a throwaway database (back up, delete a note, restore it, check it matches) and exits 0. The line is `rehearse: node --disable-warning=ExperimentalWarning scripts/rehearse-rollback.js`.
>
> No new dependencies.
>
> ## What I ran
> - `npm test`: 66 passed, 0 failed.
> - `npm run typecheck`: no errors.
> - `npm run perf`: all three scenarios well under the 50 ms budget (1.02, 1.1 and 2.29 ms medians).
> - The rehearsal script: printed `rollback rehearsal ok` and exited 0.
> - I didn't run `npm ci` because `node_modules` was already installed.
>
> ## What I'm unsure of
> - **Rollback scope:** the rollback restores notes from a backup, which assumes production backs up its database. Nothing in the repo says it does.
> - **Typecheck coverage:** I didn't check whether `tsconfig.json` covers `scripts/`, so the new rehearsal script may not be typechecked.
> - **Locked tests:** none of them looked wrong to me.

**Tests-leg summary** (`tests-summary.md`):

> I wrote 11 acceptance tests. All of them fail right now for the expected reason: there's no `DELETE /notes/:id` route yet, so the router answers `405 Method not allowed`. The 55 existing tests still pass and typecheck is clean. I added the new tests to the end of two files without changing any existing lines, and left them uncommitted.
>
> | AC | File | Test name | What it asserts |
> |---|---|---|---|
> | AC-1 | test/notes.test.js | deletes one of the caller's own notes | Deleting your own note answers 204 with an empty body. |
> | AC-2 | test/notes.test.js | a deleted note can no longer be read by id | After a delete, `GET /notes/:id` answers 404 with the same body as an id that never existed. |
> | AC-3 | test/notes.test.js | a deleted note no longer appears in the list | With three notes and the middle one deleted, `GET /notes` lists `['third', 'first']`. |
> | AC-4 | test/notes.test.js | deleting a note removes its tags | Listing by `?tag=work` no longer returns the deleted note, `?tag=team` (only on that note) returns nothing, and the database has no tag rows for its id. |
> | AC-5 | test/notes.test.js | deleting a missing note answers 404 | Deleting a note id that doesn't exist answers 404 with the same body as reading it. |
> | AC-6 | test/notes.test.js | deleting a non-numeric note id answers 404 | `DELETE /notes/not-a-number` answers 404 with the same body as `GET /notes/not-a-number`, and the caller's note is still listed. |
> | AC-7 | test/notes.test.js | deleting someone else's note answers 404 and leaves it intact | Bob deleting Alice's note gets 404 with the missing-note body, and Alice still reads the same title, body and tags. |
> | AC-8 | test/notes.test.js | deleting a note requires a signed-in session | A delete with no cookie, or with a forged `sid` cookie, answers 401, and the owner can still read the note. |
> | AC-9 | test/notes.test.js | deleting a note leaves the caller's other notes untouched | The other notes keep the same id, title, body and tags, both in the list (newest first) and when read by id. |
> | AC-10 | test/notes.test.js | deleting an already-deleted note answers 404 | A second delete of the same note answers 404 with the missing-note body. |
> | AC-11 | test/summary.test.js | a deleted note is not included in later summaries | After a delete, the request sent to the model by `POST /notes/summary` still includes the kept note but not the deleted note's title or body. |
>
> To avoid hard-coding the 404 message, the tests check that a delete's 404 body is the same as what `GET` returns for a missing note.

## Gates

| Check | Status | Event | Detail |
|---|---|---|---|
| locked-tests | pass | e032 |  |
| install | pass | e033 | exit 0 |
| typecheck | pass | e034 | exit 0 |
| lint | skipped | e035 | commands.lint is not configured |
| build | skipped | e036 | commands.build is not configured |
| tests | pass | e037 | exit 0 |
| perf | pass | e038 | exit 0 |
| secrets | pass | e039 | exit 0 |
| deps | skipped | e040 | the change touches no lockfile |
| sast | pass | e041 | exit 0 |
| rollback | skipped | e042 | no class in risk.json requires a rollback (no migration or irreversible path or pattern) |
| surface | pass | e043 | the change edits no test-runner or scanner config |
| ratchet:semgrep_findings | pass | e044 |  |
| required | pass | e045 |  |
| unchanged | pass | e046 |  |
| theory-doc | info | e047 |  |

**Stage outcomes:**

- spec: ready (pass)
- tests: ready (pass)
- build: ready (pass)
- triage: ready (pass)
- gate: ready (pass)
- review: ready (pass)

## Ratchet

- [e044] semgrep_findings: 0 at baseline → 0 after the change (**pass**); `semgrep scan --config p/default --config '<factory>/factory/rules/semgrep' --metrics=off --disable-nosem --json --quiet -- .`, output sha256 baseline `78b623d55f43cf79`, after `2d65b4e87c442e15`

## Theory doc

- [e047] `docs/THEORY.md`: changed by this change

## Review

- [e051] reviewer-claude (claude-opus-5-5): pass, $0.43, 63.4 s
- [e053] reviewer-codex (gpt-6.1-sol): pass, 29070 tokens, 41.0 s
- [e055] sort (claude-opus-5-5): pass, $0.25, 274.8 s
- [e050] grounding: seeds (28 axis rows)

| ID | Severity | Verdict | Where | Claim | Sort reason | Resolution |
|---|---|---|---|---|---|---|
| F1 | medium | confirmed | src/notes/repo.js:78 | Because note ids can be reused after a hard delete, a repeated DELETE of a stale id can erase a newer note instead of answering 404. | migrations/0003_create_notes.up.sql:2 is `id INTEGER PRIMARY KEY` with no AUTOINCREMENT, so SQLite reuses the max id after it is deleted. deleteNote (repo.js:78) only matches on id and user_id, so the | - |
| F2 | medium | confirmed | rollback.md:16 | The restore in rollback.md fails once the deleted note's id has been reused by a newer note, and the rehearsal never tries that case. | The id has no AUTOINCREMENT (0003_create_notes.up.sql:2), so it can be handed to a newer note, possibly another user's. The restore `INSERT INTO notes SELECT * ... WHERE id = :note_id` would then hit  | - |
| F3 | medium | disputed | rollback.md:11 | The only recovery path for deleted notes needs a pre-delete backup, and nothing in the repo takes one. | A repo-wide grep for backup/VACUUM finds only rollback.md and the rehearsal script, which backs up its own throwaway database. So the repo does not back up data/notes.db. Production backups could stil | - |
| F4 | low | confirmed | src/notes/routes.js:69 | Deletes are not logged, so operators can't find the note_id and user_id the restore SQL needs. | The new router.delete handler calls deleteNote and then sendNoContent with no log line. src/ has no request logging (the only console calls are in migrate-cli.js). THEORY.md T8 allows logging ids, so  | - |

## Irreversible operations and rollback

- Classes: irreversible.
- [e042] rollback: skipped; no class in risk.json requires a rollback (no migration or irreversible path or pattern)

## Residual risks

- [e035] gate:lint skipped: commands.lint is not configured
- [e036] gate:build skipped: commands.build is not configured
- F3 disputed (medium): The only recovery path for deleted notes needs a pre-delete backup, and nothing in the repo takes one.

## Sign-off

Accountable person: ______________________

Decision: [ ] sign   [ ] return

Reason (for a return): ______________________

Record the decision with `factory sign --change 20261012-162527-let-people-delete-a-note --by NAME` or `factory return --change 20261012-162527-let-people-delete-a-note --reason "..."`. The ledger records it with this pack's sha256. The harness never signs.
