# AAR Maker on Cloudflare: a compiled app as a remote MCP connector

A working example of serving a compiled grounded-forge app as a remote MCP connector, so a practitioner's own Claude or ChatGPT (on their own plan) can use the library without installing anything. This Cloudflare Worker serves the open-corpus [`aar-mode`](../../corpus.commons/demo/apps/aar-mode/) app as **AAR Maker** at `https://aar.groundedforge.com/mcp`.

For a local connector over stdio, use [`scripts/mcp/corpus-server.mjs`](../../scripts/mcp/corpus-server.mjs) instead; it reads an app folder directly and needs no sign-in.

## What the Worker does

- **Serves the library as seven read-only tools** over MCP's Streamable HTTP transport (JSON responses, stateless, POST only): `get_workflow` (the workflows and the guide), `route` (the AAR task index), `read_distillation`, `list_topics`, `find_concepts`, `list_sources` and `get_lenses`. The library is packed into the Worker at deploy time; nothing is fetched at runtime.
- **Has a front door** when the connector's profile sets `start`: one more tool, named and described in the words people ask with (AAR Maker's is `start_after_action_review_or_postmortem`), that returns the guide. claude.ai loads a connector's tools only when Claude decides it needs them, and the other tool names don't say what the connector is for.
- **Offers starter prompts** when the profile sets `prompts`: MCP prompts a person picks from the client's menu (AAR Maker's: run an after-action review, write a postmortem, debrief without blame), each one a first message that calls the front door.
- **Each person signs in with GitHub.** The Worker is its own OAuth server ([`@cloudflare/workers-oauth-provider`](https://github.com/cloudflare/workers-oauth-provider), tokens hashed in the `OAUTH_KV` namespace), with GitHub as the sign-in. GitHub is asked for no scopes: the Worker reads only the public login and id, and keeps no GitHub token. Clients register themselves; only Claude's, Claude Code's and ChatGPT's return addresses are accepted.
- **Logs who called which tool, never what they typed.** Each call writes one line to Workers Logs: the GitHub login, the tool, and the library file or section it read (or a match count). Query text, incident details and anything else the user types are never logged. The consent page says so before anyone signs in.
- **Shuts one person out without touching anyone else.** Add a GitHub login to `BLOCKED_USERS` in `wrangler.jsonc` and deploy: sign-in and every call with their live tokens refuse them at once.
- **Rate-limits per login:** 120 MCP calls a minute (the `LIMITER` binding).

## Files

| File | What it is |
|------|-----------|
| `src/index.js` | The OAuth server, GitHub sign-in, the landing and consent pages. |
| `src/mcp.js` | The MCP endpoint: tools, server instructions, the per-call log line. |
| `src/corpus.js` | Reads the packed library: distillations, indexes, workflows. |
| `bundle.mjs` | Packs a compiled app and a connector's words into `src/bundle.json` (a build artefact, gitignored). |
| `aar-maker/` | The live AAR Maker's guide and its three facilitation workflows (`aar-new`, `aar-deep`, `aar-actions`). |
| `connectors/` | One file per connector: its name, tool descriptions, pages, the app it packs and its self-test values. `aar-maker.mjs` is the default. |
| `selftest.mjs` | Calls every tool in-process against the built bundle (`npm test`). |
| `wrangler.jsonc` | Worker config: domain, bindings, vars. |
| `public/` | Icons (Factory Review's; `wrangler.review.jsonc`). |
| `public-aar-maker/` | AAR Maker's icons (`wrangler.jsonc`). |

By default `bundle.mjs` packs [`corpus.commons/demo/apps/aar-mode`](../../corpus.commons/demo/apps/aar-mode/): its 22 distillations, task, concept and lens indexes, its skills and its `aar-facilitator` runtime agent (each served as a workflow), and the app's `CLAUDE.md` as the guide (`get_workflow("guide")`) with its `DISCLAIMER.md` and `LICENSE-CONTENT` beside it. The app's files were written for a folder install, so the server instructions map the files they name to tools. Lens specs, docs and the full slug table stay behind. Flags change what it packs:

```bash
node bundle.mjs --app DIR          # another compiled AAR app
node bundle.mjs --guide FILE       # serve FILE as the guide
node bundle.mjs --workflow DIR     # also serve a workflow folder (its SKILL.md and other .md files); repeatable
node bundle.mjs --drop NAME        # leave one of the app's workflows out; repeatable
```

The live AAR Maker deploys from this folder with its own guide and three facilitation workflows, published in [`aar-maker/`](aar-maker/) and packed with:

```bash
node bundle.mjs --guide aar-maker/guide.md \
  --workflow aar-maker/workflows/aar-new --workflow aar-maker/workflows/aar-deep --workflow aar-maker/workflows/aar-actions \
  --drop aar-facilitator
```

A plain `node bundle.mjs` serves the app's `aar-facilitator` workflow and its `CLAUDE.md` as the guide instead.

`src/corpus.js` reads distillations named `{slug}-{task}.md`, for the connector's task, and a schema 3 concept index (a topics block, then concept rows). The words the connector shows (its name, the tool descriptions, the landing and consent pages) come from its file in `connectors/`.

## Another connector: Factory Review

The same Worker serves the [factory-warranty](../../corpus.commons/chrisgagne-agent-built-software/) app as **Factory Review** at `https://review.groundedforge.com/mcp`: the factory's review stage (the `review-change` workflow and its sign-off sheet) and its 17-source library. `connectors/factory-review.mjs` holds its words and `wrangler.review.jsonc` its config, with its own OAuth namespace and GitHub OAuth app.

```bash
npm run test:review     # pack factory-review and run the self-test against it
npm run deploy:review   # pack it and deploy with wrangler.review.local.jsonc (your ids filled in)
```

A new connector is a file in `connectors/` (copy one), a wrangler config for its domain, and `node bundle.mjs --connector NAME`.

## Deploy your own

You need a Cloudflare account with a domain on it, Node 22, and a GitHub account.

1. **Install.** From this folder: `npm install`.
2. **Pick the domain** the connector lives on, say `aar.example.org`. Set it in `wrangler.jsonc` (`routes` and `PUBLIC_URL`), and rename the Worker (`name`) if you like.
3. **Make a GitHub OAuth app** (GitHub → Settings → Developer settings → OAuth Apps → New OAuth App). Homepage URL `https://aar.example.org`; authorization callback URL `https://aar.example.org/callback`. Put its client ID in `wrangler.jsonc` as `GITHUB_CLIENT_ID`, and generate a client secret for the next step.
4. **Set the two secrets.** They live in Cloudflare, never in a file here:

   ```bash
   npx wrangler secret put GITHUB_CLIENT_SECRET   # the OAuth app's client secret
   npx wrangler secret put COOKIE_SECRET          # any long random string, e.g. from `openssl rand -hex 32`
   ```

   `COOKIE_SECRET` signs the cookie that remembers a person's consent for 30 days.
5. **Create the KV namespace** that holds OAuth clients, grants and tokens:

   ```bash
   npx wrangler kv namespace create OAUTH_KV
   ```

   Put the id it prints in `wrangler.jsonc`, in place of `REPLACE_WITH_OAUTH_KV_ID`.
6. **Test and deploy:**

   ```bash
   node bundle.mjs   # pack the app into src/bundle.json
   npm test          # call every tool in-process against it
   npm run deploy    # pack again, then wrangler deploy
   ```

   The first deploy attaches the custom domain. Open `https://aar.example.org/` to check the landing page.

To keep your ids out of a public fork, copy `wrangler.jsonc` to `wrangler.local.jsonc` (gitignored), fill that in, and deploy with `node bundle.mjs && npx wrangler deploy -c wrangler.local.jsonc`.

**Who used it:** Cloudflare dashboard → Workers → your Worker → Logs. Logs are kept for your account's Workers Logs retention period.

## Connect

- **Claude:** Settings → Connectors → Add custom connector → the connector URL (`https://aar.groundedforge.com/mcp`, or your own).
- **ChatGPT** (Plus, Pro, Business, Enterprise, Edu; web only): Settings → Security and login → turn on Developer mode; then Plugins → + → Create app → Create MCP App → the connector URL, authentication OAuth.

Either opens the consent page; sign in with GitHub. Then start a chat and ask for an AAR.

In Claude, open the connector and set its read-only tools to *Always allow*, or Claude asks before every library read. In Claude Code: `claude mcp add --transport http aar-maker https://aar.groundedforge.com/mcp`, then `/mcp` to sign in.

[chrisgagne/aar-maker](https://github.com/chrisgagne/aar-maker) is AAR Maker as a Claude plugin, in its own repository because the directory's validator downloads the whole repository: the same server plus a skill that tells Claude to call the front door when someone asks for an after-action review, postmortem or debrief. A skill's description is in Claude's context from the start, where a connector's tools may load only on demand.

## Licence

The Worker code is MIT, like the rest of the substrate, and so are the guide and workflows in `aar-maker/`, which are skill specifications. The library it serves carries its sources' licences: each distillation's Source line names its source's licence, and non-commercial terms apply to open-nc material. See [`LICENSE-CONTENT`](../../LICENSE-CONTENT) and the app's [`DISCLAIMER.md`](../../corpus.commons/demo/apps/aar-mode/DISCLAIMER.md).
