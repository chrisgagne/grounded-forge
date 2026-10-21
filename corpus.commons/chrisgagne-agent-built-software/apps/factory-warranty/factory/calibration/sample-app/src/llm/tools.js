export class ToolError extends Error {}

/**
 * @typedef {{
 *   name: string,
 *   description: string,
 *   inputSchema: { type: 'object', properties: Record<string, object>, required?: string[] },
 *   run: (input: Record<string, string>) => Promise<unknown>,
 * }} Tool
 * @typedef {{ ok: boolean, result?: unknown, error?: string, cause?: Error }} ToolOutcome
 */

/**
 * Offers the model only the allowlisted tools, and refuses calls to anything else.
 * @param {Tool[]} tools
 * @param {{ allow: string[] }} options
 */
export function createToolDispatcher(tools, { allow }) {
  const available = tools.filter((tool) => allow.includes(tool.name));
  return {
    definitions() {
      return available.map((tool) => ({ name: tool.name, description: tool.description, input_schema: tool.inputSchema }));
    },

    /**
     * @param {{ name: string, input?: any }} call
     * @returns {Promise<ToolOutcome>}
     */
    async dispatch(call) {
      const tool = available.find((candidate) => candidate.name === call.name);
      if (!tool) return { ok: false, error: `Tool ${call.name} is not available` };
      const input = call.input ?? {};
      const missing = (tool.inputSchema.required ?? []).filter((key) => typeof input[key] !== 'string' || !input[key]);
      if (missing.length) return { ok: false, error: `Missing required input: ${missing.join(', ')}` };
      try {
        return { ok: true, result: await tool.run(input) };
      } catch (err) {
        return { ok: false, error: err instanceof ToolError ? err.message : 'Tool failed', cause: err };
      }
    },
  };
}

/**
 * Emails the signed-in user. The server binds the recipient; the model only writes the subject and body.
 * @param {{ mailer: import('../mail/mailer.js').Mailer, recipient: string }} deps
 * @returns {Tool}
 */
export function sendEmailTool({ mailer, recipient }) {
  return {
    name: 'send_email',
    description: "Email the summary to the signed-in user's own address.",
    inputSchema: {
      type: 'object',
      properties: {
        subject: { type: 'string', description: 'Subject line, at most 200 characters' },
        body: { type: 'string', description: 'Plain-text body' },
      },
      required: ['subject', 'body'],
    },
    async run({ subject, body }) {
      if (subject.length > 200) throw new ToolError('Subject must be at most 200 characters');
      const { id } = await mailer.send({ to: recipient, subject, text: body });
      return { status: 'sent', id };
    },
  };
}
