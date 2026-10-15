import assert from 'node:assert/strict';
import { test } from 'node:test';
import { loadConfig } from '../src/config.js';

test('reads settings from the environment', () => {
  const config = loadConfig({
    PORT: '8080',
    DATABASE_PATH: '/var/lib/notes/notes.db',
    LLM_API_KEY: 'from-env',
    LLM_MODEL: 'some-model',
    SESSION_TTL_DAYS: '3',
  });
  assert.equal(config.port, 8080);
  assert.equal(config.databasePath, '/var/lib/notes/notes.db');
  assert.equal(config.llm.apiKey, 'from-env');
  assert.equal(config.llm.model, 'some-model');
  assert.equal(config.sessionTtlMs, 3 * 24 * 60 * 60 * 1000);
});

test('has no credentials unless the environment provides them', () => {
  const config = loadConfig({});
  assert.equal(config.llm.apiKey, '');
  assert.equal(config.mail.apiKey, '');
});
