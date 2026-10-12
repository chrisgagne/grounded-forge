// AAR Maker on Cloudflare Workers: the OAuth server (workers-oauth-provider, tokens in KV) in
// front of the MCP endpoint, with GitHub as the sign-in. Each person signs in as themselves, so
// the logs name who used it and BLOCKED_USERS can shut one person out without touching anyone else.
// GitHub is asked for no scopes: the Worker reads only the public login and id, and keeps no
// GitHub token.
import { OAuthProvider } from "@cloudflare/workers-oauth-provider";
import mcp from "./mcp.js";

// claude.ai's callbacks are fixed; ChatGPT's carry a per-connector callback id; Claude Code's
// is a localhost port it picks at login.
const REDIRECT_URIS = [
  "https://claude.ai/api/mcp/auth_callback",
  "https://claude.com/api/mcp/auth_callback",
  "https://chatgpt.com/connector_platform_oauth_redirect",
];
const REDIRECT_PATTERNS = [
  /^https:\/\/chatgpt\.com\/connector\/oauth\/[A-Za-z0-9_-]+$/,
  /^http:\/\/(localhost|127\.0\.0\.1):[0-9]{2,5}\/callback$/,
];
const redirectAllowed = (uri) => REDIRECT_URIS.includes(uri) || REDIRECT_PATTERNS.some((re) => re.test(uri));

const REMEMBER_DAYS = 30;

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

const PRIVACY = `<p>Signing in shares your public GitHub username with AAR Maker, nothing else: no email, no repositories.</p>
<p>What's logged: your GitHub username, which tool was called and which library file it read. Never what you type, and never your incident details. Logs are kept by Cloudflare for a few days.</p>`;

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
h1{font-size:1.4rem;margin:0 0 1rem}p,li{color:var(--fg)}small,.mute{color:var(--mute)}
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
      return page("AAR Maker", `<h1>AAR Maker</h1>
<p>A source-grounded after-action review coach, served as an MCP connector. It runs a review blameless by default and draws on openly licensed sources: US Army TC 25-20, the US Forest Service learning review guide, NHS Just Culture, the DOE human performance handbooks, the Columbia accident report and others.</p>
<p>Connector URL: <code>${esc(origin)}/mcp</code></p>
<p><strong>Claude</strong> (web, desktop or mobile): Settings → Connectors → Add custom connector, paste the URL, then sign in with GitHub. Open the connector and set Read-only tools to <em>Always allow</em>, or Claude will ask before every library read.</p>
<p><strong>Claude Code:</strong> <code>claude mcp add --transport http aar-maker ${esc(origin)}/mcp</code>, then <code>/mcp</code> to sign in.</p>
<p><strong>ChatGPT:</strong> Settings → Plugins, add a server (Streamable HTTP, the URL above, no token), then sign in with GitHub. Start your first message with “Use AAR Maker to…”: ChatGPT won't use it unless asked.</p>
<p><strong>First run:</strong> “Help me run an after-action review of [the incident or project].” Bring the timeline and who was involved.</p>
${PRIVACY}
<p class="mute"><small>Built by Chris Gagné. The library's licence terms are served with it: ask the assistant for AAR Maker's licence.</small></p>`);
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
        return page("Can't connect", `<h1>Can't connect</h1><p>AAR Maker accepts connections from Claude, Claude Code and ChatGPT. This client's return address isn't one of theirs.</p>`, 400);
      }
      if (await env.OAUTH_PROVIDER.isConsentRemembered(request, authReq, { secret: env.COOKIE_SECRET })) {
        return toGitHub(env, origin, authReq, new Headers());
      }
      const who = await env.OAUTH_PROVIDER.describeConsent(authReq);
      const consent = await env.OAUTH_PROVIDER.beginConsent(authReq);
      const app = who.clientName || who.redirectHost;
      return page("Connect AAR Maker", `<h1>Connect AAR Maker</h1>
<p><strong>${esc(app)}</strong> (returning to <code>${esc(who.redirectHost)}</code>) wants to use AAR Maker for you. Next you'll sign in with GitHub.</p>
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
        headers: { Authorization: `Bearer ${tok.access_token}`, Accept: "application/vnd.github+json", "User-Agent": "aar-maker-worker" },
      });
      const user = await userRes.json().catch(() => ({}));
      if (!user.login) {
        console.log(JSON.stringify({ action: "callback", outcome: "github-user-failed", status: userRes.status }));
        return page("Can't connect", `<h1>GitHub sign-in failed</h1><p>Start again from your AI client.</p>`, 502, resumed.headers);
      }
      if (blocked(env, user.login)) {
        console.log(JSON.stringify({ login: user.login, action: "callback", outcome: "blocked" }));
        return page("Access closed", `<h1>Access closed</h1><p>This GitHub account can't use AAR Maker.</p>`, 403, resumed.headers);
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
      accessTokenTTL: 3600,
      refreshTokenTTL: 365 * 86400,
      clientIdMetadataDocumentEnabled: true,
      resourceMetadata: { resource: `${env.PUBLIC_URL}/mcp`, scopes_supported: ["corpus.read"], resource_name: "AAR Maker" },
    });
    return provider.fetch(request, env, ctx);
  },
};
