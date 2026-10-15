import assert from 'node:assert/strict';
import { test } from 'node:test';
import { hashPassword, verifyPassword } from '../src/auth/passwords.js';

test('a hashed password verifies', async () => {
  const stored = await hashPassword('correct horse battery');
  assert.match(stored, /^scrypt\$/);
  assert.equal(await verifyPassword('correct horse battery', stored), true);
});

test('the wrong password does not verify', async () => {
  const stored = await hashPassword('correct horse battery');
  assert.equal(await verifyPassword('correct horse battery!', stored), false);
});

test('each hash has its own salt', async () => {
  const [first, second] = await Promise.all([hashPassword('same password'), hashPassword('same password')]);
  assert.notEqual(first, second);
});

test('a malformed stored hash never verifies', async () => {
  assert.equal(await verifyPassword('anything', 'plaintext-password'), false);
  assert.equal(await verifyPassword('anything', 'scrypt$16384$8$1$c2FsdA==$'), false);
});
