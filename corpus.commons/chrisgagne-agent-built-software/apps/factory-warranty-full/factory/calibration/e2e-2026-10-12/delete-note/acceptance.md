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
