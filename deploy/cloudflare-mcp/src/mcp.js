// MCP endpoint (Streamable HTTP, JSON responses, stateless) for a packed library. The OAuth
// provider has already checked the access token before this runs; ctx.props carries the GitHub
// login it was issued to. The connector's name and tool descriptions come from its profile
// (connectors/{name}.mjs), packed into the bundle.
import * as corpus from "./corpus.js";

const PROTOCOL_VERSIONS = ["2025-11-25", "2025-06-18", "2025-03-26"];
const ORIGIN_OK = /^https:\/\/([a-z0-9-]+\.)*(claude\.ai|claude\.com|anthropic\.com|chatgpt\.com|openai\.com)$/i;

const C = corpus.connector;
const T = C.tools;
const INSTRUCTIONS = C.instructions;

const RO = { readOnlyHint: true, destructiveHint: false, openWorldHint: false };

// A connector's front door (its profile's `start`): a tool named for what people ask for, so a
// client that loads tools only on demand finds it. It returns the guide.
const START = C.start ? [{
  name: C.start.name,
  title: C.start.title,
  description: C.start.description,
  inputSchema: { type: "object", properties: {} },
  annotations: RO,
}] : [];

const TOOLS = [
  ...START,
  {
    name: "get_workflow",
    title: T.get_workflow.title,
    description: T.get_workflow.description
      .replace("{{workflows}}", corpus.workflowNames().filter((n) => n !== "guide").join(", ")),
    inputSchema: { type: "object", required: ["name"], properties: {
      name: { type: "string", description: "Workflow name, or \"guide\"." },
      file: { type: "string", description: "A supporting file in that workflow, as named in its SKILL.md. Default SKILL.md." },
      part: { type: "integer", minimum: 1, description: "Part number for long files. Default 1." },
    } },
    annotations: RO,
  },
  {
    name: "route",
    title: T.route.title,
    description: T.route.description,
    inputSchema: { type: "object", properties: {
      section: { type: "string", description: T.route.section },
    } },
    annotations: RO,
  },
  {
    name: "read_distillation",
    title: "Read a distillation",
    description: T.read_distillation.description,
    inputSchema: { type: "object", required: ["source"], properties: {
      source: { type: "string", description: T.read_distillation.source },
      section: { type: "string", description: "Optional: text from a heading, e.g. \"Phase 3\"." },
    } },
    annotations: RO,
  },
  {
    name: "list_topics",
    title: "List the library's topics",
    description: "The topics block of the concept index: every subject and cross-school debate the "
      + "library covers, one compact row each (id, name, synonyms, boundary note, kind, broader topic, "
      + "concept and source counts, debate sides).",
    inputSchema: { type: "object", properties: {} },
    annotations: RO,
  },
  {
    name: "find_concepts",
    title: "Find concepts",
    description: "The concept rows of the concept index → the sources credited with each, with "
      + "context. With a topic, returns every concept filed under it (a debate's rows carry the "
      + "side, e.g. t031.1). With a query, every word must match a concept's name or synonyms. "
      + "Give either or both.",
    inputSchema: { type: "object", properties: {
      topic: { type: "string", description: "A topic id from list_topics (e.g. \"t031\") or a topic name." },
      query: { type: "string", description: T.find_concepts.query },
      limit: { type: "integer", minimum: 1, maximum: 50, description: "For a query, default 15. A topic alone returns all its concepts." },
    } },
    annotations: RO,
  },
  {
    name: "list_sources",
    title: "List sources",
    description: "The catalogue of sources with a distillation: id, slug, title and attribution "
      + "line. Filter by author, title or slug words; with no query, lists them all.",
    inputSchema: { type: "object", properties: {
      query: { type: "string", description: T.list_sources.query },
    } },
    annotations: RO,
  },
  {
    name: "get_lenses",
    title: "Get the lens index",
    description: T.get_lenses?.description ?? "",
    inputSchema: { type: "object", properties: {} },
    annotations: RO,
  },
].filter((t) => t.name !== "get_lenses" || corpus.hasLenses())
  .map((t) => ({ ...t, annotations: { ...t.annotations, title: t.title } }));

// A connector's starter prompts (its profile's `prompts`): what a person picks from the client's
// menu to begin, so the start doesn't wait on Claude deciding to load the connector.
// {{argument}} becomes what the person typed, or that argument's fallback; {{start}} the
// front door's name.
const PROMPTS = C.prompts ?? [];
const promptText = (p, args) => p.text
  .replace(/\{\{start\}\}/g, C.start?.name ?? "get_workflow")
  .replace(/\{\{(\w+)\}\}/g, (_, k) => String(args[k] ?? "").trim()
    || (p.arguments ?? []).find((a) => a.name === k)?.fallback || "");

class UnknownTool extends Error {}

const json = (status, body, headers = {}) => new Response(JSON.stringify(body), {
  status,
  headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", ...headers },
});

// A JSON header block, then (for file reads) the markdown itself, unescaped.
const toolText = (data, body = null, isError = false) => {
  const content = [{ type: "text", text: JSON.stringify(data, null, 4) }];
  if (body !== null) content.push({ type: "text", text: body });
  return { content, isError };
};

// Returns [result, log note]. Log notes name library files and sections, never free-text queries.
const callTool = (name, args) => {
  const str = (k) => String(args[k] ?? "").trim();
  if (C.start && name === C.start.name) {
    const [head, body] = corpus.workflow("guide", "", 1);
    return [toolText(head, body), `${head.workflow}/${head.file}#${head.part}`];
  }
  switch (name) {
    case "get_workflow": {
      const [head, body] = corpus.workflow(str("name"), str("file"), parseInt(args.part ?? 1, 10));
      return [toolText(head, body), `${head.workflow}/${head.file}#${head.part}`];
    }
    case "route": {
      const out = corpus.route(str("section"));
      return [toolText(out), out.section ?? "(list)"];
    }
    case "read_distillation": {
      const [head, body] = corpus.readDistillation(str("source"), str("section"));
      return [toolText(head, body), head.slug + (head.section ? ` §${head.section}` : "")];
    }
    case "list_topics": {
      const out = corpus.listTopics();
      return [toolText(out), `count=${out.count}`];
    }
    case "find_concepts": {
      const limit = Math.min(Math.max(parseInt(args.limit ?? 15, 10) || 1, 1), 50);
      const out = corpus.findConcepts(str("query"), str("topic"), limit);
      return [toolText(out), (out.topic ? out.topic.split(" ")[0] + " " : "") + `matches=${out.matches}`];
    }
    case "list_sources": {
      const out = corpus.listSources(str("query"));
      return [toolText(out), `count=${out.count}`];
    }
    case "get_lenses":
      if (!corpus.hasLenses()) break;
      return [toolText(corpus.loadJson("lens-index.json")), "lens-index"];
  }
  throw new UnknownTool(`unknown tool: ${name}`);
};

const log = (login, action, outcome) => console.log(JSON.stringify({ login, action, outcome }));

export default {
  async fetch(request, env, ctx) {
    const login = ctx.props?.login ?? "?";

    // DNS-rebinding guard: browsers send Origin; server-to-server calls usually don't.
    const origin = request.headers.get("Origin") ?? "";
    if (origin !== "" && !ORIGIN_OK.test(origin)) {
      log(login, "mcp", "bad-origin");
      return json(403, { error: "forbidden origin" });
    }
    if (request.method !== "POST") {
      // No server-initiated stream: GET/DELETE aren't supported.
      return new Response(null, { status: 405, headers: { Allow: "POST" } });
    }
    if (env.LIMITER) {
      const { success } = await env.LIMITER.limit({ key: login });
      if (!success) {
        log(login, "mcp", "rate-limited");
        return json(429, { error: "rate limited: try again in a minute" }, { "Retry-After": "60" });
      }
    }

    let msg;
    try {
      msg = await request.json();
    } catch {
      msg = null;
    }
    if (!msg || typeof msg !== "object" || Array.isArray(msg) || msg.jsonrpc !== "2.0" || !("method" in msg)) {
      return json(400, { jsonrpc: "2.0", id: null, error: { code: -32600, message: "Invalid Request" } });
    }
    // Notifications (no id) get 202 and no body.
    if (!("id" in msg)) return new Response(null, { status: 202 });

    const id = msg.id;
    const method = String(msg.method);
    const params = msg.params && typeof msg.params === "object" ? msg.params : {};
    const result = (r) => json(200, { jsonrpc: "2.0", id, result: r });
    const error = (code, message) => json(200, { jsonrpc: "2.0", id, error: { code, message } });

    switch (method) {
      case "initialize": {
        const requested = String(params.protocolVersion ?? "");
        log(login, "mcp:initialize", "ok");
        return result({
          protocolVersion: PROTOCOL_VERSIONS.includes(requested) ? requested : PROTOCOL_VERSIONS[0],
          capabilities: { tools: { listChanged: false }, ...(PROMPTS.length ? { prompts: { listChanged: false } } : {}) },
          serverInfo: {
            name: C.id, title: C.title, version: C.version,
            icons: [{ src: `${env.PUBLIC_URL}/icon-512.png`, mimeType: "image/png", sizes: ["512x512"] }],
          },
          instructions: INSTRUCTIONS,
        });
      }
      case "ping":
        return result({});
      case "tools/list":
        return result({ tools: TOOLS });
      case "prompts/list":
        return result({ prompts: PROMPTS.map(({ name, title, description, arguments: a = [] }) => ({
          name, title, description, arguments: a.map(({ name, description }) => ({ name, description, required: false })),
        })) });
      case "prompts/get": {
        const p = PROMPTS.find((x) => x.name === String(params.name ?? ""));
        if (!p) return error(-32602, `unknown prompt: ${params.name}`);
        const args = params.arguments && typeof params.arguments === "object" ? params.arguments : {};
        log(login, `prompt:${p.name}`, "ok");
        return result({ description: p.description, messages: [{ role: "user", content: { type: "text", text: promptText(p, args) } }] });
      }
      case "tools/call": {
        const name = String(params.name ?? "");
        const args = params.arguments && typeof params.arguments === "object" ? params.arguments : {};
        try {
          const [out, note] = callTool(name, args);
          log(login, `tool:${name}`, `ok ${note}`);
          return result(out);
        } catch (e) {
          if (e instanceof UnknownTool) return error(-32602, e.message);
          log(login, `tool:${name}`, e instanceof corpus.ToolInputError ? "input-error" : "error");
          return result(toolText({ error: e.message }, null, true));
        }
      }
      default:
        return error(-32601, `Method not found: ${method}`);
    }
  },
};
