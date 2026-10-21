/**
 * @typedef {{ type: 'text', text: string } | { type: 'tool_use', id: string, name: string, input: any }} ContentBlock
 * @typedef {{ role: 'user' | 'assistant', content: string | any[] }} Message
 * @typedef {{ name: string, description: string, input_schema: object }} ToolDefinition
 * @typedef {{ complete: (request: { system: string, messages: Message[], tools?: ToolDefinition[] }) => Promise<{ content: ContentBlock[], stopReason: string }> }} LlmClient
 */

/**
 * Client for the provider's Messages API.
 * @returns {LlmClient}
 */
export function createLlmClient({ baseUrl, apiKey, model, maxTokens = 1024, timeoutMs = 30_000, fetch = globalThis.fetch }) {
  return {
    async complete({ system, messages, tools = [] }) {
      if (!apiKey) throw new Error('LLM_API_KEY is not set');
      const response = await fetch(new URL('/v1/messages', baseUrl), {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-api-key': apiKey,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify({ model, max_tokens: maxTokens, system, messages, ...(tools.length ? { tools } : {}) }),
        signal: AbortSignal.timeout(timeoutMs),
      });
      if (!response.ok) throw new Error(`LLM request failed with status ${response.status}`);
      const data = /** @type {any} */ (await response.json());
      return { content: data.content ?? [], stopReason: data.stop_reason };
    },
  };
}
