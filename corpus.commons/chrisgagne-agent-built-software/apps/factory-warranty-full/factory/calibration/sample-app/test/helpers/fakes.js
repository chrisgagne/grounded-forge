/** A model reply containing only text. */
export function text(value) {
  return { content: [{ type: 'text', text: value }], stopReason: 'end_turn' };
}

/** A model reply asking to call one tool. */
export function toolUse(name, input, id = `toolu_${name}`) {
  return { content: [{ type: 'tool_use', id, name, input }], stopReason: 'tool_use' };
}

/**
 * An LLM client that returns scripted replies in order and records every request it receives.
 * A scripted Error is thrown instead of returned.
 */
export function scriptedLlm(...replies) {
  const calls = [];
  return {
    calls,
    async complete(request) {
      calls.push(structuredClone(request));
      const next = replies.shift();
      if (next === undefined) throw new Error('scriptedLlm has no reply left');
      if (next instanceof Error) throw next;
      return next;
    },
  };
}

/** A mailer that records messages instead of sending them. */
export function fakeMailer() {
  const sent = [];
  return {
    sent,
    async send(message) {
      sent.push(message);
      return { id: `msg_${sent.length}` };
    },
  };
}

/** A fetch stand-in that records requests and answers with `respond(url, init)`. */
export function fakeFetch(respond) {
  const requests = [];
  /** @type {typeof fetch} */
  const fetchImpl = async (url, init) => {
    requests.push({ url: String(url), init, body: init?.body ? JSON.parse(String(init.body)) : undefined });
    return respond(String(url), init);
  };
  return { fetch: fetchImpl, requests };
}

/** @param {number} status @param {unknown} body */
export function jsonResponse(status, body) {
  return new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
}
