// The OAuth paths run before anyone has signed in, so the per-login limiter on /mcp can't cover
// them. Client registration and token calls write to KV and cost money, so these paths are
// limited per client IP instead. The IP is used as the limiter key only and is never logged.
export const OAUTH_PATHS = new Set(["/register", "/authorize", "/token", "/callback"]);

// Returns a 429 Response when the caller is over the limit, else null.
export async function oauthLimit(request, env) {
  if (!env.LIMITER) return null;
  const path = new URL(request.url).pathname;
  if (!OAUTH_PATHS.has(path)) return null;
  const ip = request.headers.get("CF-Connecting-IP") ?? "unknown";
  const { success } = await env.LIMITER.limit({ key: `ip:${ip}` });
  if (success) return null;
  console.log(JSON.stringify({ action: "oauth", outcome: "rate-limited", path }));
  return new Response("Too many requests: try again in a minute.", {
    status: 429,
    headers: { "Retry-After": "60", "Cache-Control": "no-store" },
  });
}
