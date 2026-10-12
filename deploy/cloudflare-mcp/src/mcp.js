// MCP endpoint (Streamable HTTP, JSON responses, stateless) for the AAR Maker library. The OAuth
// provider has already checked the access token before this runs; ctx.props carries the GitHub
// login it was issued to.
import * as corpus from "./corpus.js";

const PROTOCOL_VERSIONS = ["2025-11-25", "2025-06-18", "2025-03-26"];
const ORIGIN_OK = /^https:\/\/([a-z0-9-]+\.)*(claude\.ai|claude\.com|anthropic\.com|chatgpt\.com|openai\.com)$/i;

const INSTRUCTIONS = "AAR Maker: a source-grounded After-Action Review assistant built on an open library: "
  + "distillations of openly licensed sources (US Army TC 25-20, the US Forest Service learning "
  + "review guide, the NHS Just Culture guide, the DOE human performance handbooks, the Columbia "
  + "accident report and others) projected onto AAR work. Before facilitating an AAR or "
  + "answering from the library, call get_workflow with name \"guide\" once per conversation: it "
  + "sets the discipline (blameless by default, local rationality, contributory factors not the "
  + "cause) and the retrieval order. The guide and workflows were written for a folder install; "
  + "where they name a file, use the matching tool: task-index.json or AAR-DISTILLATION-INDEX.md → "
  + "route, {slug}-aar.md → read_distillation, concept-index.json → list_topics and find_concepts, "
  + "slug-table.json → list_sources, lens-index.json → get_lenses, a skill or agent file → "
  + "get_workflow. Cite only "
  + "what a tool returned; if the library does not cover something, say so. The library is built "
  + "from open and open-nc sources: [V] passages are verbatim under each source's licence, each "
  + "distillation's Source line names that licence, and non-commercial terms apply to open-nc "
  + "material (the guide's LICENSE-CONTENT.md and DISCLAIMER.md set out the terms).";

const RO = { readOnlyHint: true, destructiveHint: false, openWorldHint: false };

const TOOLS = [
  {
    name: "get_workflow",
    title: "Get a workflow or the guide",
    description: "Use this first for any after-action review, post-incident review, postmortem, "
      + "retrospective or lessons-learned conversation, before asking the user anything. "
      + "AAR Maker's facilitation and retrieval workflows. Call get_workflow(\"guide\") once at "
      + "the start of any conversation that uses this library: it sets the AAR discipline, the "
      + "retrieval order, the licensing terms, and how file paths in the workflows map to these "
      + `tools. Workflows: ${corpus.workflowNames().filter((n) => n !== "guide").join(", ")}. `
      + "With no file, returns the workflow's SKILL.md and lists its other "
      + "files. Long files come in parts: read every part. Follow the workflow.",
    inputSchema: { type: "object", required: ["name"], properties: {
      name: { type: "string", description: "Workflow name, or \"guide\"." },
      file: { type: "string", description: "A supporting file in that workflow, as named in its SKILL.md. Default SKILL.md." },
      part: { type: "integer", minimum: 1, description: "Part number for long files. Default 1." },
    } },
    annotations: RO,
  },
  {
    name: "route",
    title: "Route an AAR situation",
    description: "Use when running an after-action review, post-incident review, postmortem or "
      + "retrospective, to choose which sources fit each phase. "
      + "The AAR task index: the situation router. With no section, lists its sections "
      + "(Phases 0-5: scoping, timeline and local rationality, contributory factors, just-culture "
      + "sorting, action design, learning-loop closure). With a section, returns its rows (need → "
      + "source id, and when it applies) and the sources those rows point to. Read before choosing "
      + "distillations.",
    inputSchema: { type: "object", properties: {
      section: { type: "string", description: "Section name or a unique part of one, e.g. \"Phase 4\" or \"Anti-Patterns\"." },
    } },
    annotations: RO,
  },
  {
    name: "read_distillation",
    title: "Read a distillation",
    description: "One distillation: a single openly licensed source (TC 25-20, the Forest Service learning "
      + "review guide, NHS Just Culture, the DOE human performance handbooks, the Columbia accident "
      + "report, ...) projected onto AAR work, with evidence markers [V] [AP] [AR] [AE] [BT]. Its "
      + "Source line names the source's licence. Returns the whole distillation, or one section of "
      + "it when `section` is given.",
    inputSchema: { type: "object", required: ["source"], properties: {
      source: { type: "string", description: "A 3-character id from route/find_concepts, or a slug (e.g. tc-25-20-army-aar)." },
      section: { type: "string", description: "Optional: text from a heading, e.g. \"Phase 3\"." },
    } },
    annotations: RO,
  },
  {
    name: "list_topics",
    title: "List the library's topics",
    description: "The topics block of the concept index: every subject and cross-school debate the "
      + "library covers, one compact row each (id, name, synonyms, boundary note, kind, broader topic, "
      + "concept and source counts, debate sides). Read it once per conversation, then pick the topics "
      + "each part of the question needs and fetch their concepts with find_concepts.",
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
      query: { type: "string", description: "Concept name or synonym, e.g. \"just culture\"." },
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
      query: { type: "string", description: "Optional words to match, e.g. \"army\"." },
    } },
    annotations: RO,
  },
  {
    name: "get_lenses",
    title: "Get the lens index",
    description: "Lenses that reweight what's salient for a named reader (builder, a PM bounded by a BA role, "
      + "agentic builder, a named consultant-coach): purpose, when to reach for each, and its "
      + "salience block. Apply a lens from its salience block; the full specs aren't served.",
    inputSchema: { type: "object", properties: {} },
    annotations: RO,
  },
];

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
          capabilities: { tools: { listChanged: false } },
          serverInfo: {
            name: "aar-maker", title: "AAR Maker", version: "0.2.0",
            icons: [{ src: `${env.PUBLIC_URL}/icon-512.png`, mimeType: "image/png", sizes: ["512x512"] }],
          },
          instructions: INSTRUCTIONS,
        });
      }
      case "ping":
        return result({});
      case "tools/list":
        return result({ tools: TOOLS });
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
