import assert from 'node:assert/strict';
import { test } from 'node:test';
import { addNote, alice, bob, signUpAndLogIn, startTestApp } from './helpers/app.js';

test('creates a note with de-duplicated tags', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('POST', '/notes', {
    cookie,
    body: { title: '  Quarterly plan ', body: 'Ship the export feature.', tags: ['work', 'planning', 'work'] },
  });
  assert.equal(res.status, 201);
  assert.equal(res.body.note.title, 'Quarterly plan');
  assert.deepEqual(res.body.note.tags, ['planning', 'work']);
});

test('rejects notes without a title or with malformed tags', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  assert.equal((await app.request('POST', '/notes', { cookie, body: { body: 'no title' } })).status, 400);
  assert.equal((await app.request('POST', '/notes', { cookie, body: { title: 'x', tags: ['Not A Tag'] } })).status, 400);
  assert.equal((await app.request('POST', '/notes', { cookie, body: { title: 'x', tags: 'work' } })).status, 400);
});

test('lists only the caller\'s notes, newest first', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const aliceCookie = await signUpAndLogIn(app, alice);
  const bobCookie = await signUpAndLogIn(app, bob);
  await addNote(app, aliceCookie, { title: 'first' });
  await addNote(app, bobCookie, { title: 'bob only' });
  await addNote(app, aliceCookie, { title: 'second' });
  const res = await app.request('GET', '/notes', { cookie: aliceCookie });
  assert.equal(res.status, 200);
  assert.deepEqual(
    res.body.notes.map((note) => note.title),
    ['second', 'first'],
  );
});

test('filters the list by tag', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  await addNote(app, cookie, { title: 'standup', tags: ['work'] });
  await addNote(app, cookie, { title: 'groceries', tags: ['home'] });
  await addNote(app, cookie, { title: 'retro', tags: ['work', 'team'] });
  const res = await app.request('GET', '/notes?tag=work', { cookie });
  assert.deepEqual(
    res.body.notes.map((note) => note.title),
    ['retro', 'standup'],
  );
});

test('paginates with limit and offset and caps the page size', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  for (let i = 1; i <= 5; i += 1) await addNote(app, cookie, { title: `note ${i}` });
  const page = await app.request('GET', '/notes?limit=2&offset=1', { cookie });
  assert.deepEqual(
    page.body.notes.map((note) => note.title),
    ['note 4', 'note 3'],
  );
  const capped = await app.request('GET', '/notes?limit=1000', { cookie });
  assert.equal(capped.body.limit, 100);
});

test('rejects invalid paging parameters', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  for (const query of ['limit=0', 'limit=abc', 'offset=-1', 'offset=1.5']) {
    assert.equal((await app.request('GET', `/notes?${query}`, { cookie })).status, 400, query);
  }
});

test('reads a single note, but not someone else\'s', async (t) => {
  const app = await startTestApp();
  t.after(app.close);
  const aliceCookie = await signUpAndLogIn(app, alice);
  const bobCookie = await signUpAndLogIn(app, bob);
  const note = await addNote(app, aliceCookie, { title: 'private', body: 'my diary' });
  const own = await app.request('GET', `/notes/${note.id}`, { cookie: aliceCookie });
  assert.equal(own.status, 200);
  assert.equal(own.body.note.body, 'my diary');
  assert.equal((await app.request('GET', `/notes/${note.id}`, { cookie: bobCookie })).status, 404);
  assert.equal((await app.request('GET', '/notes/not-a-number', { cookie: aliceCookie })).status, 404);
});
