import assert from 'node:assert/strict';
import { once } from 'node:events';
import { createServer } from 'node:http';
import { createApp } from '../../src/app.js';
import { openDatabase } from '../../src/db/index.js';
import { migrateUp } from '../../src/db/migrate.js';
import { createLogger } from '../../src/log.js';
import { fakeMailer, scriptedLlm } from './fakes.js';

export const DAY = 24 * 60 * 60 * 1000;

export const alice = {
  email: 'alice@example.com',
  password: 'correct horse battery',
  name: 'Alice Moreau',
  dateOfBirth: '1990-04-12',
};

export const bob = {
  email: 'bob@example.com',
  password: 'plaid-giraffe-77',
  name: 'Bob Tanaka',
  dateOfBirth: '1985-11-30',
};

/**
 * Starts the app on an ephemeral port with an in-memory database and fake LLM and mailer.
 * @param {{ llm?: any, mailer?: any, now?: () => number }} [options]
 */
export async function startTestApp({ llm = scriptedLlm(), mailer = fakeMailer(), now = Date.now } = {}) {
  const db = openDatabase(':memory:');
  migrateUp(db);
  const server = createServer(createApp({ db, llm, mailer, now, log: createLogger({ level: 'silent' }) }));
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  const { port } = /** @type {import('node:net').AddressInfo} */ (server.address());
  const baseUrl = `http://127.0.0.1:${port}`;

  /**
   * @param {string} method
   * @param {string} path
   * @param {{ body?: unknown, cookie?: string, headers?: Record<string, string> }} [options]
   */
  async function request(method, path, { body, cookie, headers = {} } = {}) {
    const response = await fetch(baseUrl + path, {
      method,
      headers: {
        ...(body === undefined ? {} : { 'content-type': 'application/json' }),
        ...(cookie ? { cookie } : {}),
        ...headers,
      },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const raw = await response.text();
    return { status: response.status, headers: response.headers, body: raw ? JSON.parse(raw) : null };
  }

  return {
    db,
    llm,
    mailer,
    request,
    async close() {
      server.closeAllConnections();
      await new Promise((resolve) => server.close(resolve));
      db.close();
    },
  };
}

/** @typedef {Awaited<ReturnType<typeof startTestApp>>} TestApp */

/** @param {TestApp} app @param {typeof alice} user */
export async function signUp(app, user) {
  const res = await app.request('POST', '/signup', { body: user });
  assert.equal(res.status, 201, `signup failed: ${JSON.stringify(res.body)}`);
  return res.body.user;
}

/** @param {{ headers: Headers }} res */
export function sessionCookie(res) {
  const header = res.headers.get('set-cookie');
  assert.ok(header, 'expected a set-cookie header');
  return header.split(';')[0];
}

/** @param {TestApp} app @param {{ email: string, password: string }} user */
export async function logIn(app, { email, password }) {
  const res = await app.request('POST', '/login', { body: { email, password } });
  assert.equal(res.status, 200, `login failed: ${JSON.stringify(res.body)}`);
  return sessionCookie(res);
}

/** @param {TestApp} app @param {typeof alice} user */
export async function signUpAndLogIn(app, user) {
  await signUp(app, user);
  return logIn(app, user);
}

/**
 * @param {TestApp} app
 * @param {string} cookie
 * @param {{ title: string, body?: string, tags?: string[] }} note
 */
export async function addNote(app, cookie, note) {
  const res = await app.request('POST', '/notes', { cookie, body: note });
  assert.equal(res.status, 201, `create note failed: ${JSON.stringify(res.body)}`);
  return res.body.note;
}
