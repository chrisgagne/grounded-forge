Tags typed with capitals or stray spaces now save in their lowercase, trimmed form, so "Work " saves as "work". The typecheck passes and all 68 tests pass, including every acceptance test from AC-1 to AC-14.

## What I changed
The only change is to `validateNoteInput` in `src/notes/routes.js`. It now checks tags in two steps:

1. **Check what was sent, as today.** `tags` must be a list of no more than 10 strings, all of the same type. The 10-tag limit counts the tags as sent, before any merging of duplicates (AC-10, AC-11).
2. **Clean up, then check again.** Each tag is trimmed and lowercased, and the result is checked against the existing pattern `/^[a-z0-9][a-z0-9-]{0,31}$/`. That pattern already refuses blank tags, tags starting with a hyphen, internal spaces, characters that aren't allowed, and tags over 32 characters (AC-7, AC-8, AC-9). Duplicates are then removed from the cleaned-up tags, so "Work", " work" and "work" are saved once (AC-6, AC-12).

Both steps refuse with the same 400 message as before (AC-13). Since only cleaned-up tags reach the database, reading a note back and filtering by `tag=work` both show the cleaned-up form (AC-4, AC-5). The list filter itself is unchanged, so `tag=Work` won't match notes saved as "work" (AC-14).

I added no dependencies and no migration, so no `rollback.md` is needed. The work is left uncommitted.

## What I ran
- `check typecheck`: the scans passed and `tsc --noEmit` reported no errors.
- `check test`: the scans passed, and 68 tests ran with 68 passing and 0 failing.

## What I'm unsure of
- **Semgrep couldn't reach its server.** Both runs logged blocked connections to `semgrep.dev:443`, but the check still said "scans passed". Semgrep may have run with only the rules it had locally. The gate might behave differently if it has network access.
- **The check said "2 changed file(s)" but I edited only one**, `src/notes/routes.js`. The second may be something the factory created; I didn't track it down.
- **I didn't run `npm run perf` or `npm ci`.** The check tool only lets me run `typecheck` and `test`.

None of the locked tests looked wrong.