// The per-IP limiter in front of the OAuth paths (src/oauth-limit.js). Run by `npm test`.
import assert from "node:assert/strict";
import { oauthLimit, OAUTH_PATHS } from "./src/oauth-limit.js";

// A limiter that allows `max` calls per key, like the Workers rate-limit binding.
const fakeLimiter = (max) => {
  const seen = new Map();
  return { async limit({ key }) { seen.set(key, (seen.get(key) ?? 0) + 1); return { success: seen.get(key) <= max }; }, seen };
};
const req = (path, ip = "203.0.113.9", method = "POST") =>
  new Request(`https://aar.example.org${path}`, { method, headers: { "CF-Connecting-IP": ip } });

const quiet = console.log; console.log = () => {};
try {
  // Each OAuth path is limited; the third call from one IP over a limit of 2 gets a 429.
  for (const path of OAUTH_PATHS) {
    const env = { LIMITER: fakeLimiter(2) };
    assert.equal(await oauthLimit(req(path), env), null);
    assert.equal(await oauthLimit(req(path), env), null);
    const r = await oauthLimit(req(path), env);
    assert.equal(r.status, 429, path);
    assert.equal(r.headers.get("Retry-After"), "60");
  }
  // Another IP has its own allowance, and the key is the IP, prefixed so it can't collide with a login.
  const env = { LIMITER: fakeLimiter(1) };
  await oauthLimit(req("/register", "198.51.100.1"), env);
  assert.equal(await oauthLimit(req("/register", "198.51.100.2"), env), null);
  assert.deepEqual([...env.LIMITER.seen.keys()], ["ip:198.51.100.1", "ip:198.51.100.2"]);
  // /mcp, the landing page and metadata aren't touched by this limiter.
  for (const path of ["/mcp", "/", "/privacy", "/.well-known/oauth-authorization-server"]) {
    const e = { LIMITER: fakeLimiter(0) };
    assert.equal(await oauthLimit(req(path, "203.0.113.9", "GET"), e), null, path);
    assert.equal(e.LIMITER.seen.size, 0, path);
  }
  // No binding (local runs) means no limiting.
  assert.equal(await oauthLimit(req("/token"), {}), null);
} finally {
  console.log = quiet;
}
console.log("oauth-limit: all passed");
