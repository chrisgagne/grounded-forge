#!/usr/bin/env node

/**
 * grounded-forge corpus MCP server
 *
 * Exposes the runtime retrieval surface — concept axis, task-axis situation
 * router, distillations, lenses — as MCP tools, so any MCP client reaches the
 * corpus without the answer-from-corpus skill in context.
 *
 * The tool surface mirrors the retrieval order in CLAUDE.md: classify, check
 * lens applicability, index, then distillation.
 *
 * Runs against either root, because both carry the same four artefacts:
 *   corpus.commons/{corpus}/            (operator tier)
 *   corpus.commons/{corpus}/apps/{app}/ (shipped tier, pointers stripped)
 *
 *   node scripts/mcp/corpus-server.mjs --root corpus.commons/demo
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "node:fs";
import path from "node:path";

// ---------------------------------------------------------------- corpus root

const argRoot = (() => {
  const i = process.argv.indexOf("--root");
  return i !== -1 ? process.argv[i + 1] : undefined;
})();

const ROOT = path.resolve(
  argRoot || process.env.GROUNDED_FORGE_ROOT || "corpus.commons/demo",
);

const readJson = (rel) => {
  const file = path.join(ROOT, rel);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, "utf8"));
};

const conceptIndex = readJson("concept-index.json");
// schema_version 2 stores concepts as compact rows
// [slug, name, aliases, source_ids, contexts?]; normalise to the dict
// shape ({slug: {name, aliases, sources: [{id, context?}]}}) the lookup
// code reads, so both index generations serve identically.
if (conceptIndex && Array.isArray(conceptIndex.concepts)) {
  const byRow = {};
  for (const [slug, name, aliases, ids, contexts] of conceptIndex.concepts) {
    byRow[slug] = {
      name,
      aliases,
      sources: ids.map((id) =>
        contexts?.[id] ? { id, context: contexts[id] } : { id },
      ),
    };
  }
  conceptIndex.concepts = byRow;
}
const slugTable = readJson("references/slug-table.json") ?? readJson("slug-table.json");
const lensIndex = readJson("lens-index.json") ?? readJson("lenses/lens-index.json");

if (!conceptIndex || !slugTable) {
  console.error(
    `[grounded-forge] no corpus at ${ROOT} — expected concept-index.json and slug-table.json`,
  );
  process.exit(1);
}

const slugForId = (id) => slugTable.slugs[id] ?? null;
const idForSlug = (slug) =>
  Object.entries(slugTable.slugs).find(([, s]) => s === slug)?.[0] ?? null;

const taskDomains = () => {
  const dir = path.join(ROOT, "distillations");
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => e.name)
    .sort();
};

// ------------------------------------------------------------------- helpers

const ok = (text) => ({ content: [{ type: "text", text }] });

// A miss returns isError with the near-neighbours rather than throwing, so the
// caller can correct itself instead of losing the turn.
const miss = (text) => ({ content: [{ type: "text", text }], isError: true });

// Concept keys are hyphenated slugs; callers type prose. Normalise both ways
// before comparing, or every multi-word lookup silently falls through to the
// substring tier.
const asSlug = (s) => s.toLowerCase().trim().replace(/\s+/g, "-");

// ---------------------------------------------------------------------- tools

const TOOLS = [
  {
    name: "list_task_domains",
    description:
      "List the task axes this corpus has been projected onto, with the number " +
      "of distillations in each. Call this first when you do not already know " +
      "which task domain the user's situation belongs to.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
      additionalProperties: false,
    },
  },
  {
    name: "route_situation",
    description:
      "Route a described situation to the distillations that address it, using " +
      "the task-axis situation router. Call this when the user describes a " +
      "problem or a phase of work ('we keep relitigating decisions', 'planning a " +
      "reorg') rather than naming a source or a concept. Returns matching " +
      "need/source/when rows grouped by phase; follow up with get_distillation.",
    inputSchema: {
      type: "object",
      properties: {
        task: {
          type: "string",
          description: "Task domain, e.g. 'decision-making'. See list_task_domains.",
        },
        query: {
          type: "string",
          description:
            "Free text describing the situation. Omit to return the full router " +
            "for this task domain.",
        },
      },
      required: ["task"],
      additionalProperties: false,
    },
  },
  {
    name: "lookup_concept",
    description:
      "Find which sources cover a named concept, via the concept axis. Call this " +
      "when the user names a specific idea, framework, or term ('escalation of " +
      "commitment', 'Cynefin', 'psychological safety'). Matches exact keys, " +
      "aliases, then substrings. Returns source slugs to pass to get_distillation.",
    inputSchema: {
      type: "object",
      properties: {
        concept: {
          type: "string",
          description: "Concept name, alias, or fragment.",
        },
      },
      required: ["concept"],
      additionalProperties: false,
    },
  },
  {
    name: "get_distillation",
    description:
      "Read a distillation: one source projected onto one task domain. This is " +
      "the payload — it carries paraphrased claims with parenthetical " +
      "attribution, verbatim blockquotes, and evidence markers ([V], [AP], [AR], " +
      "[AE], [BT]) in band. Read the whole file unless you already know which " +
      "section you need; the full read is what grounds a claim.",
    inputSchema: {
      type: "object",
      properties: {
        slug: {
          type: "string",
          description: "Source slug, e.g. 'openstax-organizational-behavior'.",
        },
        task: {
          type: "string",
          description: "Task domain, e.g. 'decision-making'.",
        },
        section: {
          type: "string",
          description:
            "Optional '## ' heading to return alone. Omit for the full " +
            "distillation, which is the default and usually correct.",
        },
      },
      required: ["slug", "task"],
      additionalProperties: false,
    },
  },
  {
    name: "list_lenses",
    description:
      "List the lenses available in this corpus, with what each one is for and " +
      "when to reach for it. Call this before decomposing a diagnostic or " +
      "synthesis question — a lens changes what counts as salient, so it has to " +
      "be chosen before the sub-claims are formed, not after.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
      additionalProperties: false,
    },
  },
  {
    name: "get_lens",
    description:
      "Read a full lens spec. Call this once list_lenses shows a lens that " +
      "materially reweights the current question.",
    inputSchema: {
      type: "object",
      properties: {
        lens: { type: "string", description: "Lens name, e.g. 'cto'." },
      },
      required: ["lens"],
      additionalProperties: false,
    },
  },
];

// ------------------------------------------------------------------- handlers

const handlers = {
  list_task_domains() {
    const rows = taskDomains().map((task) => {
      const dir = path.join(ROOT, "distillations", task);
      const count = fs
        .readdirSync(dir)
        .filter((f) => f.endsWith(`-${task}.md`)).length;
      return `- ${task} (${count} distillations)`;
    });
    if (!rows.length) return miss(`No distillations directory under ${ROOT}.`);
    return ok(`Task domains in ${slugTable.corpus}:\n${rows.join("\n")}`);
  },

  route_situation({ task, query }) {
    const index = readJson(path.join("distillations", task, "task-index.json"));
    if (!index) {
      return miss(
        `No task index for '${task}'. Available: ${taskDomains().join(", ") || "none"}.`,
      );
    }

    const terms = (query || "").toLowerCase().split(/\s+/).filter((t) => t.length > 3);
    const out = [];

    for (const section of index.sections) {
      const rows = section.rows.filter((row) => {
        if (!terms.length) return true;
        const hay = row.join(" ").toLowerCase();
        return terms.some((t) => hay.includes(t));
      });
      if (!rows.length) continue;
      out.push(`\n## ${section.section}`);
      for (const [need, id, when] of rows) {
        out.push(`- **${need}** — ${slugForId(id) ?? id}\n  ${when}`);
      }
    }

    if (!out.length) {
      return miss(
        `No rows in '${task}' matched "${query}". Call route_situation without a ` +
          `query to see the full router, or try lookup_concept instead.`,
      );
    }
    return ok(`# ${task} router${query ? ` — matches for "${query}"` : ""}${out.join("\n")}`);
  },

  lookup_concept({ concept }) {
    const raw = concept.toLowerCase().trim();
    const slug = asSlug(concept);
    const concepts = conceptIndex.concepts;
    const keys = Object.keys(concepts);
    const aliasesOf = (k) => (concepts[k].aliases || []).map((a) => a.toLowerCase());

    let matched = keys.filter((k) => k === slug);
    if (!matched.length) {
      matched = keys.filter((k) =>
        aliasesOf(k).some((a) => a === raw || asSlug(a) === slug),
      );
    }
    if (!matched.length) {
      matched = keys.filter(
        (k) =>
          k.includes(slug) ||
          concepts[k].name.toLowerCase().includes(raw) ||
          aliasesOf(k).some((a) => a.includes(raw) || asSlug(a).includes(slug)),
      );
    }

    if (!matched.length) {
      // Suggest on word overlap, not whole-string overlap — a miss is only
      // recoverable if the caller gets somewhere to go next.
      const words = slug.split("-").filter((w) => w.length > 3);
      const suggestions = keys
        .filter((k) => words.some((w) => k.includes(w)))
        .slice(0, 8);
      return miss(
        `No concept matching "${concept}" in ${keys.length} indexed concepts.` +
          (suggestions.length
            ? ` Closest: ${suggestions.join(", ")}.`
            : ` Try route_situation for a situation-shaped query instead.`),
      );
    }

    const out = matched.slice(0, 10).map((key) => {
      const c = concepts[key];
      const sources = c.sources
        .map((s) => `  - ${slugForId(s.id) ?? s.id}${s.context ? ` — ${s.context}` : ""}`)
        .join("\n");
      return `## ${c.name}${c.aliases?.length ? ` (aliases: ${c.aliases.join(", ")})` : ""}\n${sources}`;
    });

    return ok(out.join("\n\n"));
  },

  get_distillation({ slug, task, section }) {
    const file = path.join(ROOT, "distillations", task, `${slug}-${task}.md`);
    if (!fs.existsSync(file)) {
      const known = idForSlug(slug)
        ? `Slug '${slug}' exists but has no ${task} distillation.`
        : `Unknown slug '${slug}'.`;
      return miss(`${known} Use lookup_concept or route_situation to find one.`);
    }

    const text = fs.readFileSync(file, "utf8");
    if (!section) return ok(text);

    const blocks = text.split(/^## /m);
    const hit = blocks.find((b) =>
      b.toLowerCase().startsWith(section.toLowerCase().replace(/^##\s*/, "")),
    );
    if (!hit) {
      const headings = blocks.slice(1).map((b) => b.split("\n")[0]);
      return miss(`No section "${section}". Sections: ${headings.join(" | ")}`);
    }
    return ok(`## ${hit}`);
  },

  list_lenses() {
    if (!lensIndex) return miss(`No lens index under ${ROOT}.`);
    const out = Object.entries(lensIndex.lenses).map(
      ([name, l]) =>
        `## ${name} (${l.kind})\n${l.purpose}\n**Reach for when:** ${l.reach_for_when}`,
    );
    return ok(out.join("\n\n"));
  },

  get_lens({ lens }) {
    const entry = lensIndex?.lenses?.[lens];
    const rel = entry?.spec_path ?? path.join("lenses", `${lens}.md`);
    const file = path.join(ROOT, rel);
    if (!fs.existsSync(file)) {
      const known = Object.keys(lensIndex?.lenses ?? {}).join(", ");
      return miss(`No lens '${lens}'.${known ? ` Available: ${known}.` : ""}`);
    }
    return ok(fs.readFileSync(file, "utf8"));
  },
};

// ------------------------------------------------------------------ transport

const server = new Server(
  { name: "grounded-forge-corpus", version: "0.4.0" },
  { capabilities: { tools: {} } },
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const handler = handlers[request.params.name];
  if (!handler) return miss(`Unknown tool: ${request.params.name}`);
  try {
    return handler(request.params.arguments ?? {});
  } catch (err) {
    return miss(`${request.params.name} failed: ${err.message}`);
  }
});

await server.connect(new StdioServerTransport());
console.error(`[grounded-forge] corpus MCP server ready — root: ${ROOT}`);
