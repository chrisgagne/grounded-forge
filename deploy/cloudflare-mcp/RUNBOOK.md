# Connector incident runbook

For AAR Maker (`aar.groundedforge.com`) and Factory Review (`review.groundedforge.com`). One person runs both and owns every step here: Chris Gagné. This page lists the moves in order. It's for the moment something goes wrong, so it skips the why.

What the connectors hold about people: each user's GitHub login and numeric id, OAuth client records, tokens (hashed) in each Worker's `OAUTH_KV` namespace, and Workers Logs lines (login, tool, library file) kept up to seven days. They hold no conversation text: the library is static, and the user's own AI client does the generating.

## Levers

| Lever | How | Effect |
|---|---|---|
| Shut one person out | Add the GitHub login to `BLOCKED_USERS` in the deployed config, and deploy | Refused at sign-in, and on every call with their live tokens, at once |
| Take a connector offline | Cloudflare dashboard → Workers → the Worker → Settings → Domains & Routes → remove the custom domain. The spend cap does the same for both automatically | Nothing reaches the Worker; code, KV and secrets are untouched |
| End every session | Rotate `COOKIE_SECRET` and the GitHub OAuth app's client secret (`npx wrangler secret put …`), then delete every key in the Worker's `OAUTH_KV` | Every client and token is gone; everyone signs in again |
| Fix what the library says | Correct the corpus distillation, `npm run build`, then redeploy the connector (its deploy runs the self-test first) | Users get the corrected text on their next call |
| Read what happened | Cloudflare dashboard → Workers → the Worker → Logs (seven days only) | Who called which tool and file, when |

## A security breach

Leaked secrets, someone else in the Cloudflare or GitHub account, or abuse through the endpoints.

1. **Contain:**
   - If the account or a secret is compromised, take the affected connector offline.
   - Rotate the Cloudflare and GitHub credentials that could be involved.
   - End every session (lever 3).
   - If the abuse comes from one person, block that login instead.
2. **Preserve:** export the relevant Workers Logs before the seven-day window closes, and note the times.
3. **Assess:** whose data was reachable. At most that's GitHub logins and ids, and client records. Tokens are stored hashed.
4. **Tell people:**
   - Post a notice on the connector's landing page.
   - Open an issue on the repository.
   - If the breach is likely to cause anyone serious harm, notify the Privacy Commissioner (NotifyUs) and the people affected, as soon as practicable (NZ Privacy Act 2020, Part 6).
5. **Restore:** bring the domain back, check `/privacy` and a tool call, and record what happened and what changed.

## Wrong or harmful guidance

A user reports, or a review finds, that the library led their assistant to bad advice: a misattributed claim, an invented quote, a distillation that's wrong, or content that shouldn't ship.

1. **Triage within a working day:**
   - Find the distillation and passage. The user's report, or the log line's file name, points to it.
   - Check it against the converted source.
2. **If the library is wrong:** fix the distillation (lever 4). Then check whether the same claim sits in other task projections of that source.
3. **If the library is right and the user's assistant invented it:** reply with the passage that holds, and note the pattern. Client-side invention is a known limit.
4. **If the content shouldn't ship at all:** take the connector offline while it's removed from the build.
5. **Reply** to the person who reported it with what was found and what changed. **Record** it in the repository's issue tracker.

## A user says the guidance cost them money

Treat it as wrong guidance (above), plus three more steps:
- Keep the report and the relevant log lines.
- Answer in writing.
- Talk to the insurer before admitting fault. The disclaimer and licence terms (`DISCLAIMER.md`, `LICENSE-CONTENT`) set out what was offered.
