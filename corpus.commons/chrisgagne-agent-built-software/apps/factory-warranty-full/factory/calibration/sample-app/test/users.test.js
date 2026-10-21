import assert from 'node:assert/strict';
import { test } from 'node:test';
import { alice, bob, signUpAndLogIn, startTestApp } from './helpers/app.js';

test('GET /me returns the signed-in user\'s profile', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('GET', '/me', { cookie });
  assert.equal(res.status, 200);
  assert.equal(res.body.user.email, alice.email);
  assert.equal(res.body.user.name, alice.name);
  assert.equal(res.body.user.dateOfBirth, alice.dateOfBirth);
});

test('each user sees only their own profile', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const aliceCookie = await signUpAndLogIn(app, alice);
  const bobCookie = await signUpAndLogIn(app, bob);
  assert.equal((await app.request('GET', '/me', { cookie: aliceCookie })).body.user.email, alice.email);
  assert.equal((await app.request('GET', '/me', { cookie: bobCookie })).body.user.email, bob.email);
});

test('PATCH /me updates the name and date of birth', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('PATCH', '/me', { cookie, body: { name: 'Alice M. Moreau', dateOfBirth: '1990-04-13' } });
  assert.equal(res.status, 200);
  assert.equal(res.body.user.name, 'Alice M. Moreau');
  assert.equal(res.body.user.dateOfBirth, '1990-04-13');
  const again = await app.request('GET', '/me', { cookie });
  assert.equal(again.body.user.dateOfBirth, '1990-04-13');
});

test('PATCH /me can clear the date of birth', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('PATCH', '/me', { cookie, body: { dateOfBirth: null } });
  assert.equal(res.status, 200);
  assert.equal(res.body.user.dateOfBirth, null);
});

test('PATCH /me rejects dates of birth that are not real past dates', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  for (const dateOfBirth of ['2023-02-30', '12/04/1990', 'next tuesday', '2999-01-01']) {
    const res = await app.request('PATCH', '/me', { cookie, body: { dateOfBirth } });
    assert.equal(res.status, 400, `expected ${dateOfBirth} to be rejected`);
  }
});

test('PATCH /me does not change the email address', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('PATCH', '/me', { cookie, body: { email: 'mallory@example.com' } });
  assert.equal(res.status, 400);
  assert.equal((await app.request('GET', '/me', { cookie })).body.user.email, alice.email);
});
