import assert from 'node:assert/strict';
import { test } from 'node:test';
import { createMailer } from '../src/mail/mailer.js';
import { fakeFetch, jsonResponse } from './helpers/fakes.js';

test('posts the message to the mail API', async () => {
  const { fetch, requests } = fakeFetch(() => jsonResponse(202, { id: 'msg_42' }));
  const mailer = createMailer({ apiUrl: 'https://mail.test/send', apiKey: 'mail-key', from: 'Notes <n@example.com>', fetch });
  const result = await mailer.send({ to: 'alice@example.com', subject: 'Hi', text: 'Body' });
  assert.deepEqual(result, { id: 'msg_42' });
  assert.equal(requests[0].url, 'https://mail.test/send');
  assert.equal(requests[0].init.headers.authorization, 'Bearer mail-key');
  assert.deepEqual(requests[0].body, { from: 'Notes <n@example.com>', to: 'alice@example.com', subject: 'Hi', text: 'Body' });
});

test('throws when the mail API refuses the message', async () => {
  const { fetch } = fakeFetch(() => jsonResponse(503, { error: 'unavailable' }));
  const mailer = createMailer({ apiUrl: 'https://mail.test/send', apiKey: 'k', from: 'n@example.com', fetch });
  await assert.rejects(mailer.send({ to: 'alice@example.com', subject: 'Hi', text: 'Body' }), /status 503/);
});
