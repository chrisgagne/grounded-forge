import assert from 'node:assert/strict';
import { test } from 'node:test';
import { DAY, alice, bob, logIn, sessionCookie, signUp, signUpAndLogIn, startTestApp } from './helpers/app.js';

test('signup creates an account and returns the profile without the password hash', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const res = await app.request('POST', '/signup', { body: alice });
  assert.equal(res.status, 201);
  assert.equal(res.body.user.email, alice.email);
  assert.equal(res.body.user.name, alice.name);
  assert.equal('passwordHash' in res.body.user || 'password_hash' in res.body.user, false);
  const row = app.db.prepare('SELECT password_hash FROM users WHERE email = ?').get(alice.email);
  assert.notEqual(row.password_hash, alice.password);
});

test('signup rejects an email that is already registered, whatever its case', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  await signUp(app, alice);
  const res = await app.request('POST', '/signup', { body: { ...bob, email: 'ALICE@example.com' } });
  assert.equal(res.status, 409);
});

test('signup rejects short passwords and invalid emails', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const short = await app.request('POST', '/signup', { body: { ...alice, password: 'short' } });
  assert.equal(short.status, 400);
  const badEmail = await app.request('POST', '/signup', { body: { ...alice, email: 'alice.example.com' } });
  assert.equal(badEmail.status, 400);
});

test('login sets an HttpOnly session cookie', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  await signUp(app, alice);
  const res = await app.request('POST', '/login', { body: { email: alice.email, password: alice.password } });
  assert.equal(res.status, 200);
  const header = res.headers.get('set-cookie');
  assert.match(header, /^sid=[A-Za-z0-9_-]{43};/);
  assert.match(header, /HttpOnly/);
  assert.match(header, /SameSite=Lax/);
});

test('login gives the same answer for a wrong password and an unknown email', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  await signUp(app, alice);
  const wrongPassword = await app.request('POST', '/login', { body: { email: alice.email, password: 'not the password' } });
  const unknownEmail = await app.request('POST', '/login', { body: { email: 'nobody@example.com', password: 'not the password' } });
  assert.equal(wrongPassword.status, 401);
  assert.equal(unknownEmail.status, 401);
  assert.deepEqual(wrongPassword.body, unknownEmail.body);
});

test('routes that need a session answer 401 without a valid one', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  assert.equal((await app.request('GET', '/me')).status, 401);
  assert.equal((await app.request('GET', '/me', { cookie: 'sid=forged-token' })).status, 401);
  assert.equal((await app.request('GET', '/notes')).status, 401);
  assert.equal((await app.request('POST', '/notes/summary', { body: {} })).status, 401);
});

test('logout ends the session', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('POST', '/logout', { cookie });
  assert.equal(res.status, 204);
  assert.match(sessionCookie(res), /^sid=$/);
  assert.equal((await app.request('GET', '/me', { cookie })).status, 401);
});

test('a session is valid until it expires', async (t) => {
  let clock = Date.parse('2026-03-02T09:00:00Z');
  const app = await startTestApp({ now: () => clock });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  clock += 6 * DAY;
  assert.equal((await app.request('GET', '/me', { cookie })).status, 200);
});

test('rejects a session after it expires', async (t) => {
  let clock = Date.parse('2026-03-02T09:00:00Z');
  const app = await startTestApp({ now: () => clock });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  clock += 8 * DAY;
  const res = await app.request('GET', '/me', { cookie });
  assert.equal(res.status, 401);
});

test('each login gets its own session', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  await signUp(app, alice);
  const first = await logIn(app, alice);
  const second = await logIn(app, alice);
  assert.notEqual(first, second);
  await app.request('POST', '/logout', { cookie: first });
  assert.equal((await app.request('GET', '/me', { cookie: second })).status, 200);
});
