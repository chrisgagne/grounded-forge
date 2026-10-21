# Build this change

You are the build leg. Implement the change in this worktree so the locked acceptance tests pass, without breaking anything else.

## The story

# Let people delete a note

People can create and read notes but can't get rid of one. They want to delete a note they no longer need.

## What we want

- A signed-in person can delete one of their own notes.
- Once deleted, the note is gone: it no longer shows in their list, can't be read by id, and its tags go with it.
- Deleting a note that doesn't exist, or that belongs to someone else, looks the same to the caller as a missing note.
- Nobody can delete a note without being signed in.


## Acceptance criteria

## AC-1: A signed-in person who sends `DELETE /notes/:id` for one of their own notes gets a success response with no body.
check: test/notes.test.js :: deletes one of the caller's own notes
assumption: Success is `204 No Content` with an empty body. The story doesn't say what a successful delete returns.

## AC-2: Once a note is deleted, `GET /notes/:id` for that note answers 404, the same as for a note that never existed.
check: test/notes.test.js :: a deleted note can no longer be read by id

## AC-3: Once a note is deleted, it no longer appears in the owner's `GET /notes` list, and their other notes are still listed newest first.
check: test/notes.test.js :: a deleted note no longer appears in the list

## AC-4: Once a note is deleted, its tags go with it: listing by one of its tags no longer returns it, and the database has no tag rows left for that note's id.
check: test/notes.test.js :: deleting a note removes its tags

## AC-5: Deleting a note id that does not exist answers 404 with the same body as reading a missing note.
check: test/notes.test.js :: deleting a missing note answers 404

## AC-6: A note id that is not a whole number, such as `/notes/not-a-number`, answers 404 on delete, just like a read.
check: test/notes.test.js :: deleting a non-numeric note id answers 404
assumption: A malformed id is treated as a missing note (404), not bad input (400), to match how `GET /notes/:id` already behaves.

## AC-7: When one person tries to delete another person's note, the answer is 404 with the same body as a missing note, and the note is unchanged: its owner can still read it with the same title, body and tags.
check: test/notes.test.js :: deleting someone else's note answers 404 and leaves it intact

## AC-8: A `DELETE /notes/:id` request with no session cookie, or with an invalid one, answers 401 and the note stays readable by its owner.
check: test/notes.test.js :: deleting a note requires a signed-in session

## AC-9: Deleting one note leaves the owner's other notes unchanged: same ids, titles, bodies and tags.
check: test/notes.test.js :: deleting a note leaves the caller's other notes untouched

## AC-10: Deleting the same note a second time answers 404.
check: test/notes.test.js :: deleting an already-deleted note answers 404
assumption: Deleting is not idempotent-success. A repeat delete is answered like any other missing note.

## AC-11: Once a note is deleted, a later `POST /notes/summary` request does not include its title or body in what is sent to the model.
check: test/summary.test.js :: a deleted note is not included in later summaries


## Locked tests

These files are locked. A guard blocks any edit to them, and the gate re-hashes them after you finish: a changed locked test fails the change. If a locked test looks wrong, say so in your final message and leave it as it is.

- scripts/perf.js
- test/auth.test.js
- test/config.test.js
- test/helpers/app.js
- test/helpers/fakes.js
- test/llm-client.test.js
- test/mailer.test.js
- test/migrations.test.js
- test/notes.test.js
- test/passwords.test.js
- test/summarise.test.js
- test/summary.test.js
- test/tools.test.js
- test/users.test.js

## Commands the gate will run from the worktree root

- install: `npm ci`
- test: `npm test`
- typecheck: `npm run typecheck`
- perf: `npm run perf`

## Open items from review or from the accountable person

- F1 (medium, confirmed) src/notes/repo.js:78: Because note ids can be reused after a hard delete, a repeated DELETE of a stale id can erase a newer note instead of answering 404. Review's reason: migrations/0003_create_notes.up.sql:2 is `id INTEGER PRIMARY KEY` with no AUTOINCREMENT, so SQLite reuses the max id after it is deleted. deleteNote (repo.js:78) only matches on id and user_id, so the same user's repeated DELETE removes their new note, which breaks AC-10's 404 in that case. I lowered it from critical to medium: the user_id filter means only the caller's own notes are at risk, never another user's.
- returned by Chris: fix F1

## Rules

- Change the implementation, not the tests. You may add tests of your own in new files; they won't be locked.
- Keep to what the story asks. Add a dependency only if the story needs it, and say why in your final message.
- Run the test command (and typecheck and lint, if listed) before you finish, and fix what fails.
- If the change includes a database migration, a delete or a bulk update, write `rollback.md` at the worktree root: how to undo the change, and a line `rehearse: <command>` naming a command that runs the rollback against a test database and exits 0 when it works.
- Your shell runs in a sandbox: it can write only inside this worktree, has no network beyond localhost unless the factory's config allows a domain, and can't read credentials or the git metadata's config. Pushing and rewriting history are blocked.
- Leave your work uncommitted; the factory commits it. The sandbox doesn't let the leg write git metadata.

Your final message says what you changed and why, what you ran and what it showed, and anything you're unsure of. It is filed as the builder's assertion, not as evidence: the gate runs everything again.
