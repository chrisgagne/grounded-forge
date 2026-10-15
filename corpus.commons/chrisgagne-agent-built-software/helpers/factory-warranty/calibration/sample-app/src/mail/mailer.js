/**
 * @typedef {{ send: (message: { to: string, subject: string, text: string }) => Promise<{ id: string | null }> }} Mailer
 */

/**
 * Sends mail through the provider's HTTP API.
 * @returns {Mailer}
 */
export function createMailer({ apiUrl, apiKey, from, timeoutMs = 5000, fetch = globalThis.fetch }) {
  return {
    async send({ to, subject, text }) {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'content-type': 'application/json', authorization: `Bearer ${apiKey}` },
        body: JSON.stringify({ from, to, subject, text }),
        signal: AbortSignal.timeout(timeoutMs),
      });
      if (!response.ok) throw new Error(`Mail API responded with status ${response.status}`);
      const data = /** @type {any} */ (await response.json().catch(() => ({})));
      return { id: typeof data.id === 'string' ? data.id : null };
    },
  };
}
