import assert from 'node:assert/strict';
import { test } from 'node:test';
import { addNote, alice, bob, signUpAndLogIn, startTestApp } from './helpers/app.js';
import { fakeMailer, scriptedLlm, text, toolUse } from './helpers/fakes.js';

test('summarises the caller\'s notes and nobody else\'s', async (t) => {
  const llm = scriptedLlm(text('You are planning Q3 and buying milk.'));
  const app = await startTestApp({ llm });
  t.after(app.close);
  const aliceCookie = await signUpAndLogIn(app, alice);
  const bobCookie = await signUpAndLogIn(app, bob);
  await addNote(app, aliceCookie, { title: 'Q3 planning', body: 'Draft the roadmap.' });
  await addNote(app, aliceCookie, { title: 'Shopping', body: 'Milk.' });
  await addNote(app, bobCookie, { title: 'Bob secret', body: 'Not for Alice.' });

  const res = await app.request('POST', '/notes/summary', { cookie: aliceCookie, body: {} });
  assert.equal(res.status, 200);
  assert.equal(res.body.summary, 'You are planning Q3 and buying milk.');
  assert.equal(res.body.email, null);
  const sent = JSON.stringify(llm.calls[0]);
  assert.match(sent, /Q3 planning/);
  assert.match(sent, /Milk\./);
  assert.doesNotMatch(sent, /Bob secret/);
});

test('emails the summary to the signed-in user when asked', async (t) => {
  const llm = scriptedLlm(toolUse('send_email', { subject: 'Your notes', body: 'Summary body' }), text('Sent you the summary.'));
  const mailer = fakeMailer();
  const app = await startTestApp({ llm, mailer });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  await addNote(app, cookie, { title: 'Q3 planning', body: 'Draft the roadmap.' });

  const res = await app.request('POST', '/notes/summary', { cookie, body: { email: true } });
  assert.equal(res.status, 200);
  assert.deepEqual(res.body.email, { to: alice.email, status: 'sent' });
  assert.equal(mailer.sent.length, 1);
  assert.equal(mailer.sent[0].to, alice.email);
  assert.equal(mailer.sent[0].text, 'Summary body');
});

test('only summarises notes with the requested tag', async (t) => {
  const llm = scriptedLlm(text('Work things.'));
  const app = await startTestApp({ llm });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  await addNote(app, cookie, { title: 'Standup', tags: ['work'] });
  await addNote(app, cookie, { title: 'Dentist', tags: ['home'] });
  const res = await app.request('POST', '/notes/summary', { cookie, body: { tag: 'work' } });
  assert.equal(res.status, 200);
  const sent = JSON.stringify(llm.calls[0]);
  assert.match(sent, /Standup/);
  assert.doesNotMatch(sent, /Dentist/);
});

test('does not call the model when there is nothing to summarise', async (t) => {
  const llm = scriptedLlm();
  const app = await startTestApp({ llm });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  const res = await app.request('POST', '/notes/summary', { cookie, body: {} });
  assert.equal(res.status, 200);
  assert.equal(llm.calls.length, 0);
});

test('answers 502 when the model is unavailable', async (t) => {
  const llm = scriptedLlm(new Error('LLM request failed with status 529'));
  const app = await startTestApp({ llm });
  t.after(app.close);
  const cookie = await signUpAndLogIn(app, alice);
  await addNote(app, cookie, { title: 'Q3 planning' });
  const res = await app.request('POST', '/notes/summary', { cookie, body: {} });
  assert.equal(res.status, 502);
  assert.doesNotMatch(JSON.stringify(res.body), /529/);
});
