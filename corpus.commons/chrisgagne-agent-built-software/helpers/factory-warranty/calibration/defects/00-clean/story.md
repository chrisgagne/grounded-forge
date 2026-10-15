# Edit a note after saving it

People make typos and change their minds about tags. Today the only fix is to copy the note into a new one, which loses its date and clutters the list.

As someone who keeps notes, I want to change a note's title, text or tags after I've saved it.

## Acceptance

- `PATCH /notes/:id` with any of `title`, `body` and `tags` updates that note and returns it.
- Fields I don't send stay as they were. Sending `tags` replaces the note's tags.
- The note keeps its created date; its updated date moves to now.
- The same rules apply as when creating a note (a title of 1 to 200 characters, at most 10 lowercase tags, and so on).
- I can only edit my own notes.
