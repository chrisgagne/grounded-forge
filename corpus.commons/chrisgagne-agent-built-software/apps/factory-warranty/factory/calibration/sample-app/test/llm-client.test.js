import assert from 'node:assert/strict';
import { test } from 'node:test';
import { createLlmClient } from '../src/llm/client.js';
import { fakeFetch, jsonResponse } from './helpers/fakes.js';

const reply = { content: [{ type: 'text', text: 'hi' }], stop_reason: 'end_turn' };

test('calls the Messages API with the configured key and model', async () => {
  const { fetch, requests } = fakeFetch(() => jsonResponse(200, reply));
  const llm = createLlmClient({ baseUrl: 'https://llm.test', apiKey: 'test-key', model: 'test-model', fetch });
  const tools = [{ name: 'send_email', description: 'd', input_schema: { type: 'object' } }];
  const result = await llm.complete({ system: 'sys', messages: [{ role: 'user', content: 'hello' }], tools });
  assert.equal(requests[0].url, 'https://llm.test/v1/messages');
  assert.equal(requests[0].init.headers['x-api-key'], 'test-key');
  assert.equal(requests[0].body.model, 'test-model');
  assert.equal(requests[0].body.system, 'sys');
  assert.deepEqual(requests[0].body.tools, tools);
  assert.deepEqual(result, { content: reply.content, stopReason: 'end_turn' });
});

test('leaves tools out of the request when none are offered', async () => {
  const { fetch, requests } = fakeFetch(() => jsonResponse(200, reply));
  const llm = createLlmClient({ baseUrl: 'https://llm.test', apiKey: 'test-key', model: 'm', fetch });
  await llm.complete({ system: 'sys', messages: [], tools: [] });
  assert.equal('tools' in requests[0].body, false);
});

test('throws when the provider answers with an error', async () => {
  const { fetch } = fakeFetch(() => jsonResponse(529, { error: { type: 'overloaded_error' } }));
  const llm = createLlmClient({ baseUrl: 'https://llm.test', apiKey: 'test-key', model: 'm', fetch });
  await assert.rejects(llm.complete({ system: 's', messages: [] }), /status 529/);
});

test('refuses to call the provider without an API key', async () => {
  const { fetch, requests } = fakeFetch(() => jsonResponse(200, reply));
  const llm = createLlmClient({ baseUrl: 'https://llm.test', apiKey: '', model: 'm', fetch });
  await assert.rejects(llm.complete({ system: 's', messages: [] }), /LLM_API_KEY/);
  assert.equal(requests.length, 0);
});
