# Friendlier dates on notes

The notes page shows raw timestamps like `2026-03-02T09:14:07.000Z`. People want "3 days ago".

## What we want

- Each note in the `GET /notes`, `GET /notes/:id` and `POST /notes` responses gets `createdAgo`, such as "a few seconds ago", "3 days ago" or "a month ago".
- `createdAt` stays as it is for clients that use it.
