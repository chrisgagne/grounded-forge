# Notes app: theory

What this program is for, how its parts fit, and the rules that keep it safe to change. If a change breaks one of the rules below, the change updates this file in the same commit and says why.

## Purpose

A personal notes service. People sign up, keep notes with tags, and ask an LLM to summarise their notes, optionally emailing the summary to themselves. The notes and the profile (name, email, date of birth) are personal data; most of the design is about keeping each person's data to that person.

## Parts

- `src/router.js`, `src/http.js`: a small router and JSON helpers. Route handlers run in order; a handler that ends the response stops the chain, which is how `requireSession` guards routes.
- `src/auth/`: passwords (scrypt), server-side sessions, the `requireSession` guard, and the signup, login and logout routes.
- `src/users/`: the profile: repository, validation and the `/me` routes.
- `src/notes/`: notes and tags: repository and the `/notes` routes.
- `src/llm/`: the summary assistant: the provider client, the tool dispatcher, the summary loop and the `/notes/summary` route.
- `src/mail/`: the mail provider client.
- `src/db/` and `migrations/`: the SQLite connection (`node:sqlite`) and the up/down migration runner.
- `scripts/perf.js`: the latency budget for the notes list.

## Invariants

**T1. Data is scoped to the session's user.** Every read or write of a profile or a note is scoped to `req.user.id` in the SQL itself. No route takes a user id from the request. A note that belongs to someone else is answered exactly like a missing note (404).

**T2. Sessions are server-side and expire on a fixed clock.** The cookie holds a random 256-bit token; the database holds only its SHA-256. A session ends 7 days after login (`SESSION_TTL_DAYS`), whether or not it is used; an expired session is deleted when it is next presented. Logout deletes the session row. The cookie is `HttpOnly; Secure; SameSite=Lax`.

**T3. Passwords are only ever stored as scrypt hashes, and login does not reveal who has an account.** Each hash has its own salt. The hash never leaves `src/users/repo.js` (`toProfile` omits it). Login answers a wrong password and an unknown email identically, and does the same scrypt work for both.

**T4. Profile fields stay inside the app.** Name, email and date of birth leave the app only in responses to their owner and as the recipient address of the owner's own summary email. They are never sent to the LLM provider. Dates of birth are optional, ISO `YYYY-MM-DD`, real and in the past.

**T5. Note text is data, never instructions.** The model sees note titles, bodies, tags and dates, escaped, inside a `<notes>` element in the user turn. The system prompt is a constant: no user-supplied text is ever placed in it.

**T6. The model can only reach allowlisted tools, and no tool takes a recipient from the model.** The dispatcher offers the model only the tools allowlisted for the request and refuses anything else. `send_email` is offered only when the user asked for email, and its recipient is bound by the server to the signed-in user's own address; it is not a tool input. So no note text can choose who receives mail.

**T7. The app tells the user what actually happened.** `email.status` in the summary response is `sent` only after the mail provider accepted the message (2xx); a failed send is reported as `failed`. Errors from the LLM or mail provider are logged and answered with a clear failure, never with success.

**T8. Logs never carry personal content.** Log lines carry ids, counts, routes, statuses and error messages. They never carry note text, prompts, summaries, passwords, session tokens or profile fields.

**T9. SQL text is constant.** Every query uses bound parameters; no SQL is built from request data.

**T10. Every schema change can be undone.** A migration is a numbered `NNNN_name.up.sql` with a matching `.down.sql`, and runs in a transaction. `npm run migrate -- down` reverts the latest. A migration that drops or rewrites personal-data columns ships with a down path and a tested restore.

**T11. Credentials come from the environment.** `LLM_API_KEY` and `MAIL_API_KEY` are read from the environment; no credential is ever committed. Without them the app runs but cannot reach the providers.

**T12. The notes list costs what one page costs.** `GET /notes` is one query whose work is bounded by the page size, not by how many notes the user has. `npm run perf` holds the median under 50 ms for a user with 50,000 notes.

**T13. Few dependencies, pinned.** There are no runtime dependencies. Development dependencies are pinned to exact versions in `package-lock.json`.

## API

| Route | Session | Purpose |
|---|---|---|
| `POST /signup` | no | Create an account (`email`, `password` of 10 to 200 characters, `name`, optional `dateOfBirth`). |
| `POST /login` | no | Start a session; sets the `sid` cookie. |
| `POST /logout` | yes | End the session. |
| `GET /me`, `PATCH /me` | yes | Read or change your own name and date of birth. Email and password are not changed here. |
| `GET /notes` | yes | Your notes, newest first; `limit` (at most 100), `offset`, `tag`. |
| `POST /notes` | yes | Create a note (`title`, `body`, up to 10 `tags`). |
| `GET /notes/:id` | yes | One of your notes. |
| `POST /notes/summary` | yes | Summarise your 50 newest notes (optionally one `tag`); `email: true` also emails you the summary. |
