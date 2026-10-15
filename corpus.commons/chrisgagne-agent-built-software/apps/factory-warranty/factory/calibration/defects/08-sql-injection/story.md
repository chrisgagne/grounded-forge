# Search my notes

People with hundreds of notes can't find anything; the list only filters by tag.

## What we want

- `GET /notes/search?q=…` returns my notes whose title or text contains what I typed, ignoring upper and lower case.
- Newest first, at most 50 results, each shaped like a note in the list.
- An empty search is an error.
