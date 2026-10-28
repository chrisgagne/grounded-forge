// A packed library on Cloudflare Workers (AAR Maker, or another connector in connectors/): the
// OAuth server (workers-oauth-provider, tokens in KV) in front of the MCP endpoint, with GitHub as
// the sign-in. Each person signs in as themselves, so the logs name who used it and BLOCKED_USERS
// can shut one person out without touching anyone else. GitHub is asked for no scopes: the Worker
// reads only the public login and id, and keeps no GitHub token.
import { OAuthProvider } from "@cloudflare/workers-oauth-provider";
import mcp from "./mcp.js";
import { connector } from "./corpus.js";

const NAME = connector.title;

// claude.ai's callbacks are fixed; ChatGPT's carry a per-connector callback id; Claude Code's
// is a localhost port it picks at login. Cursor registers three and signs in with whichever its
// version uses: localhost (desktop, current), cursor.com (cloud agents) or its private-use
// cursor:// scheme (older desktop builds).
const REDIRECT_URIS = [
  "https://claude.ai/api/mcp/auth_callback",
  "https://claude.com/api/mcp/auth_callback",
  "https://chatgpt.com/connector_platform_oauth_redirect",
  "https://www.cursor.com/agents/mcp/oauth/callback",
  "cursor://anysphere.cursor-mcp/oauth/callback",
];
const REDIRECT_PATTERNS = [
  /^https:\/\/chatgpt\.com\/connector\/oauth\/[A-Za-z0-9_-]+$/,
  /^http:\/\/(localhost|127\.0\.0\.1):[0-9]{2,5}\/callback$/,
];
const redirectAllowed = (uri) => REDIRECT_URIS.includes(uri) || REDIRECT_PATTERNS.some((re) => re.test(uri));

const REMEMBER_DAYS = 30;

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

const PRIVACY = `${connector.pages.privacy}\n<p><a href="/privacy">Privacy policy</a></p>`;

// A connector's contact is a URL (an issue tracker) or an email address.
const CONTACT = connector.contact.startsWith("https://")
  ? `open an issue at <a href="${esc(connector.contact)}">${esc(connector.contact.replace(/^https:\/\//, ""))}</a>`
  : `email <a href="mailto:${esc(connector.contact)}">${esc(connector.contact)}</a>`;

// The full policy behind /privacy. Every connector runs on this code, so the data handling is the
// same for all of them; only the name, the contact and what users bring (pages.privacy) differ.
const policy = (origin) => `<h1>${esc(NAME)}: privacy policy</h1>
<p>${esc(NAME)} is a read-only library served as an MCP connector at <code>${esc(origin)}/mcp</code>, run by Chris Gagné. This page says what it collects, where that goes and how long it's kept.</p>
<h2>What it collects</h2>
<ul>
<li><strong>Your GitHub username and numeric id</strong>, when you sign in. GitHub is asked for no permissions, so ${esc(NAME)} sees no email address, no repositories and nothing private, and it keeps no GitHub token.</li>
<li><strong>Sign-in records:</strong> the AI client you connected (Claude, ChatGPT, Cursor or another) and the tokens it holds, stored hashed. A cookie on this site remembers your consent for ${REMEMBER_DAYS} days.</li>
<li><strong>A log line when you sign in, connect and call a tool:</strong> your GitHub username, the AI client (at sign-in), and for a tool call the tool and the library file or section it read, or how many matches a search found. Nothing else about a request is logged.</li>
</ul>
<h2>What it doesn't collect</h2>
<p>Your conversation stays with your AI client, under that client's own terms. A tool call carries only short arguments, such as a file name or a few search words. The server uses them to answer and logs none of them, so what you type never reaches the logs.</p>
<h2>Who else handles it</h2>
<p>Cloudflare hosts the server, its logs and the sign-in records. GitHub handles sign-in. Nothing is sold or shared with anyone else, and there are no analytics, ads or tracking cookies.</p>
<h2>How long it's kept</h2>
<p>Logs: up to seven days, Cloudflare's retention. Access tokens expire after 30 days and refresh tokens after a year. The consent cookie lasts ${REMEMBER_DAYS} days.</p>
<h2>Your choices</h2>
<p>Remove the connector in your AI client to stop using it, and revoke ${esc(NAME)} under GitHub → Settings → Applications → Authorized OAuth Apps. To have your sign-in records deleted now, or with any question, ${CONTACT}.</p>
<p class="mute"><small><a href="/">${esc(NAME)}</a></small></p>`;

// Cursor's one-click install link: the server's config, base64-encoded, in a cursor:// deep link.
const cursorInstall = (origin) => `cursor://anysphere.cursor-deeplink/mcp/install?name=${connector.id}&config=${
  encodeURIComponent(btoa(JSON.stringify({ url: `${origin}/mcp` })))}`;

const page = (title, body, status = 200, headers = new Headers()) => {
  headers.set("Content-Type", "text/html; charset=utf-8");
  headers.set("Cache-Control", "no-store");
  headers.set("X-Robots-Tag", "noindex, nofollow");
  return new Response(`<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/icon-512.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><title>${esc(title)}</title>
<style>
:root{color-scheme:light dark;--bg:#fbfaf7;--fg:#1d1d1b;--mute:#5f5e5a;--line:#dcd9d0;--accent:#1f5f8b}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#ecebe6;--mute:#a3a29c;--line:#383733;--accent:#79b4dd}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,sans-serif}
main{max-width:34rem;margin:0 auto;padding:3rem 1rem}
h1{font-size:1.4rem;margin:0 0 1rem}h2{font-size:1.1rem;margin:1.75rem 0 .5rem}p,li{color:var(--fg)}small,.mute{color:var(--mute)}
a{color:var(--accent)}
code{font-size:.9em;background:var(--line);padding:.1em .35em;border-radius:4px;word-break:break-all}
.row{display:flex;gap:.75rem;margin-top:1.5rem;flex-wrap:wrap}
button{font:inherit;padding:.6rem 1.1rem;border-radius:6px;border:1px solid var(--line);background:transparent;color:var(--fg);cursor:pointer}
button.go{background:var(--accent);border-color:var(--accent);color:#fff}
</style></head><body><main>${body}</main></body></html>`, { status, headers });
};

const githubAuthorizeUrl = (env, origin, state) => {
  const u = new URL("https://github.com/login/oauth/authorize");
  u.searchParams.set("client_id", env.GITHUB_CLIENT_ID);
  u.searchParams.set("redirect_uri", `${origin}/callback`);
  u.searchParams.set("state", state);
  u.searchParams.set("allow_signup", "true");
  return u.toString();
};

const toGitHub = async (env, origin, authReq, headers) => {
  const up = await env.OAUTH_PROVIDER.beginUpstream(authReq, { headers });
  up.headers.set("Location", githubAuthorizeUrl(env, origin, up.state));
  return new Response(null, { status: 302, headers: up.headers });
};

const blocked = (env, login) => (env.BLOCKED_USERS ?? "").toLowerCase().split(/[\s,]+/).filter(Boolean)
  .includes(login.toLowerCase());

const handler = {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = url.origin;

    if (url.pathname === "/" && request.method === "GET") {
      return page(NAME, connector.pages.landing.replaceAll("{{origin}}", esc(origin))
        .replaceAll("{{cursor}}", esc(cursorInstall(origin))).replace("{{privacy}}", PRIVACY));
    }

    if (url.pathname === "/privacy" && request.method === "GET") {
      return page(`${NAME}: privacy policy`, policy(origin));
    }

    if (url.pathname === "/authorize" && request.method === "GET") {
      let authReq;
      try {
        authReq = await env.OAUTH_PROVIDER.parseAuthRequest(request);
      } catch (e) {
        return page("Can't connect", `<h1>Can't connect</h1><p>${esc(e.message)}</p>`, 400);
      }
      if (!redirectAllowed(authReq.redirectUri)) {
        console.log(JSON.stringify({ action: "authorize", outcome: "bad-redirect", redirect: authReq.redirectUri }));
        return page("Can't connect", `<h1>Can't connect</h1><p>${esc(NAME)} accepts connections from Claude, Claude Code, ChatGPT and Cursor. This client's return address isn't one of theirs.</p>`, 400);
      }
      if (await env.OAUTH_PROVIDER.isConsentRemembered(request, authReq, { secret: env.COOKIE_SECRET })) {
        return toGitHub(env, origin, authReq, new Headers());
      }
      const who = await env.OAUTH_PROVIDER.describeConsent(authReq);
      const consent = await env.OAUTH_PROVIDER.beginConsent(authReq);
      const app = who.clientName || who.redirectHost;
      return page(`Connect ${NAME}`, `<h1>Connect ${esc(NAME)}</h1>
<p><strong>${esc(app)}</strong> (returning to <code>${esc(who.redirectHost)}</code>) wants to use ${esc(NAME)} for you. Next you'll sign in with GitHub.</p>
${PRIVACY}
<form method="post" action="/authorize"><input type="hidden" name="handle" value="${esc(consent.handle)}">
<div class="row"><button class="go" name="decision" value="approve">Continue with GitHub</button>
<button name="decision" value="deny">Cancel</button></div></form>`, 200, consent.headers);
    }

    if (url.pathname === "/authorize" && request.method === "POST") {
      const form = await request.clone().formData();
      const handle = String(form.get("handle") ?? "");
      try {
        if (form.get("decision") !== "approve") {
          const denied = await env.OAUTH_PROVIDER.denyConsent(request, handle);
          return new Response(null, { status: 302, headers: denied.headers });
        }
        const ok = await env.OAUTH_PROVIDER.approveConsent(request, handle, {
          remember: { secret: env.COOKIE_SECRET, maxAgeSeconds: REMEMBER_DAYS * 86400 },
        });
        return toGitHub(env, origin, ok.request, ok.headers);
      } catch (e) {
        return page("Can't connect", `<h1>That sign-in expired</h1><p>Start again from your AI client. (${esc(e.message)})</p>`, 400);
      }
    }

    if (url.pathname === "/callback" && request.method === "GET") {
      let resumed;
      try {
        resumed = await env.OAUTH_PROVIDER.finishUpstream(request);
      } catch (e) {
        return page("Can't connect", `<h1>That sign-in expired</h1><p>Start again from your AI client. (${esc(e.message)})</p>`, 400);
      }
      const code = url.searchParams.get("code");
      if (!code) {
        return page("Sign-in cancelled", `<h1>Sign-in cancelled</h1><p>GitHub didn't complete the sign-in. Start again from your AI client.</p>`, 400, resumed.headers);
      }
      const tokenRes = await fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: { Accept: "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
          redirect_uri: `${origin}/callback`,
        }),
      });
      const tok = await tokenRes.json().catch(() => ({}));
      if (!tok.access_token) {
        console.log(JSON.stringify({ action: "callback", outcome: "github-token-failed", error: tok.error ?? tokenRes.status }));
        return page("Can't connect", `<h1>GitHub sign-in failed</h1><p>Start again from your AI client.</p>`, 502, resumed.headers);
      }
      const userRes = await fetch("https://api.github.com/user", {
        headers: { Authorization: `Bearer ${tok.access_token}`, Accept: "application/vnd.github+json", "User-Agent": `${connector.id}-worker` },
      });
      const user = await userRes.json().catch(() => ({}));
      if (!user.login) {
        console.log(JSON.stringify({ action: "callback", outcome: "github-user-failed", status: userRes.status }));
        return page("Can't connect", `<h1>GitHub sign-in failed</h1><p>Start again from your AI client.</p>`, 502, resumed.headers);
      }
      if (blocked(env, user.login)) {
        console.log(JSON.stringify({ login: user.login, action: "callback", outcome: "blocked" }));
        return page("Access closed", `<h1>Access closed</h1><p>This GitHub account can't use ${esc(NAME)}.</p>`, 403, resumed.headers);
      }
      const { redirectTo } = await env.OAUTH_PROVIDER.completeAuthorization({
        request: resumed.request,
        userId: String(user.id),
        metadata: { login: user.login },
        scope: resumed.request.scope,
        props: { login: user.login, id: user.id },
      });
      console.log(JSON.stringify({ login: user.login, action: "callback", outcome: "ok", client: resumed.request.clientId }));
      resumed.headers.set("Location", redirectTo);
      return new Response(null, { status: 302, headers: resumed.headers });
    }

    return new Response("Not found", { status: 404 });
  },
};

// A blocked person's live tokens stop working at once, not when they expire.
const api = {
  async fetch(request, env, ctx) {
    if (ctx.props?.login && blocked(env, ctx.props.login)) {
      return new Response(JSON.stringify({ error: "access closed" }), { status: 403, headers: { "Content-Type": "application/json" } });
    }
    return mcp.fetch(request, env, ctx);
  },
};

// The provider needs the resource's absolute URL at construction, and that comes from env
// (PUBLIC_URL), so it's built on the first request.
let provider;

export default {
  fetch(request, env, ctx) {
    provider ??= new OAuthProvider({
      apiRoute: "/mcp",
      apiHandler: api,
      defaultHandler: handler,
      authorizeEndpoint: "/authorize",
      tokenEndpoint: "/token",
      clientRegistrationEndpoint: "/register",
      scopesSupported: ["corpus.read"],
      // Each refresh is two KV writes, so a month keeps them rare. A long token costs little:
      // it reads a shared library, and BLOCKED_USERS is checked on every call.
      accessTokenTTL: 30 * 86400,
      refreshTokenTTL: 365 * 86400,
      clientIdMetadataDocumentEnabled: true,
      // Lets older Cursor builds sign in with cursor://; redirectAllowed still admits only the
      // exact URIs above.
      allowPrivateUseRedirectUris: true,
      resourceMetadata: { resource: `${env.PUBLIC_URL}/mcp`, scopes_supported: ["corpus.read"], resource_name: NAME },
    });
    return provider.fetch(request, env, ctx);
  },
};
