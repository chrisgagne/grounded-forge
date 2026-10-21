# Let people delete a note

People can create and read notes but can't get rid of one. They want to delete a note they no longer need.

## What we want

- A signed-in person can delete one of their own notes.
- Once deleted, the note is gone: it no longer shows in their list, can't be read by id, and its tags go with it.
- Deleting a note that doesn't exist, or that belongs to someone else, looks the same to the caller as a missing note.
- Nobody can delete a note without being signed in.
