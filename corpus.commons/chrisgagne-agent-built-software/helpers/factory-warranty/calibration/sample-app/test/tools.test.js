import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ToolError, createToolDispatcher, sendEmailTool } from '../src/llm/tools.js';
import { fakeMailer } from './helpers/fakes.js';

function recordingTool(name, run = async (input) => input.value) {
  const calls = [];
  return {
    calls,
    tool: {
      name,
      description: `${name} tool`,
      inputSchema: { type: /** @type {const} */ ('object'), properties: { value: { type: 'string' } }, required: ['value'] },
      run: async (input) => {
        calls.push(input);
        return run(input);
      },
    },
  };
}

test('offers the model only allowlisted tools', () => {
  const a = recordingTool('alpha');
  const b = recordingTool('beta');
  const dispatcher = createToolDispatcher([a.tool, b.tool], { allow: ['beta'] });
  assert.deepEqual(
    dispatcher.definitions().map((definition) => definition.name),
    ['beta'],
  );
  assert.ok(dispatcher.definitions()[0].input_schema);
});

test('refuses to run a tool that is not allowlisted', async () => {
  const a = recordingTool('alpha');
  const dispatcher = createToolDispatcher([a.tool], { allow: [] });
  const outcome = await dispatcher.dispatch({ name: 'alpha', input: { value: 'x' } });
  assert.equal(outcome.ok, false);
  assert.equal(a.calls.length, 0);
});

test('refuses a call with missing required input', async () => {
  const a = recordingTool('alpha');
  const dispatcher = createToolDispatcher([a.tool], { allow: ['alpha'] });
  const outcome = await dispatcher.dispatch({ name: 'alpha', input: {} });
  assert.equal(outcome.ok, false);
  assert.equal(a.calls.length, 0);
});

test('a tool that throws comes back as a failure without internal details', async () => {
  const broken = recordingTool('alpha', async () => {
    throw new Error('connect ECONNREFUSED 10.0.0.5:5432');
  });
  const refusing = recordingTool('beta', async () => {
    throw new ToolError('That is not allowed');
  });
  const dispatcher = createToolDispatcher([broken.tool, refusing.tool], { allow: ['alpha', 'beta'] });
  const crashed = await dispatcher.dispatch({ name: 'alpha', input: { value: 'x' } });
  assert.equal(crashed.ok, false);
  assert.doesNotMatch(String(crashed.error), /ECONNREFUSED/);
  const refused = await dispatcher.dispatch({ name: 'beta', input: { value: 'x' } });
  assert.equal(refused.error, 'That is not allowed');
});

test('send_email sends to the recipient the server bound', async () => {
  const mailer = fakeMailer();
  const dispatcher = createToolDispatcher([sendEmailTool({ mailer, recipient: 'alice@example.com' })], {
    allow: ['send_email'],
  });
  const outcome = await dispatcher.dispatch({ name: 'send_email', input: { subject: 'Notes', body: 'Summary' } });
  assert.equal(outcome.ok, true);
  assert.deepEqual(mailer.sent, [{ to: 'alice@example.com', subject: 'Notes', text: 'Summary' }]);
});
