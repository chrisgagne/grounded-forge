#!/usr/bin/env node
// Packs a compiled AAR app into src/bundle.json, the one module the Worker reads the library from:
// the distillations, a catalogue of them, the task, concept and lens indexes, the workflows, and
// the guide with the app's DISCLAIMER.md and LICENSE-CONTENT. Lens specs, docs and the full slug
// table stay behind. JSON files are stored parsed, markdown as text.
//
//   node bundle.mjs                                  the public aar-mode app, its CLAUDE.md as the guide
//   node bundle.mjs --app DIR                        another compiled AAR app
//   node bundle.mjs --guide FILE                     serve FILE as the guide instead of the app's CLAUDE.md
//   node bundle.mjs --workflow DIR [--workflow DIR]  also serve a workflow folder (SKILL.md and its .md files)
//   node bundle.mjs --drop NAME                      leave one of the app's workflows out
//
// The workflows are the app's skills (.claude/skills/{name}/) and its runtime agents
// (.claude/agents/{name}.md, each served as that workflow's SKILL.md).
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const TASK = "aar"; // src/corpus.js reads {slug}-aar.md filenames
const NOT_SERVED = [/^port-notes\.md$/, /^review-.*\.md$/]; // authoring notes kept beside a workflow

const opts = { app: path.resolve(here, "../../corpus.commons/demo/apps/aar-mode"), guide: null, workflow: [], drop: [] };
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i += 2) {
  const key = argv[i].replace(/^--/, "");
  if (!(key in opts) || argv[i + 1] === undefined) throw new Error(`usage: see the header of bundle.mjs (bad argument '${argv[i]}')`);
  const val = path.resolve(argv[i + 1]);
  if (Array.isArray(opts[key])) opts[key].push(key === "drop" ? argv[i + 1] : val);
  else opts[key] = val;
}

const read = (p) => fs.readFileSync(p, "utf8");
const isFile = (p) => fs.existsSync(p) && fs.statSync(p).isFile();
const files = {};

// The distillation's title, and the first line under it (its Source line), cut to 300 characters.
const titleAndSource = (text) => {
  const lines = text.split("\n");
  const at = lines.findIndex((l) => l.startsWith("# "));
  if (at === -1) return ["", ""];
  const next = lines.slice(at + 1).find((l) => l.trim() && !l.startsWith("#") && l.trim() !== "---") ?? "";
  return [lines[at].slice(2).trim(), [...next.trim()].slice(0, 300).join("")];
};

const app = opts.app;
const distDir = path.join(app, "distillations", TASK);
const slugs = JSON.parse(read(path.join(app, "slug-table.json"))).slugs;
const suffix = `-${TASK}.md`;
const shipped = new Map(fs.readdirSync(distDir).filter((f) => f.endsWith(suffix)).map((f) => [f.slice(0, -suffix.length), f]));
const missing = [...shipped.keys()].filter((s) => !Object.values(slugs).includes(s)).sort();
if (missing.length) throw new Error(`distillations with no slug-table id: ${missing.join(", ")}`);

const sources = {};
for (const [id, slug] of Object.entries(slugs).sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))) {
  if (!shipped.has(slug)) continue;
  const text = read(path.join(distDir, shipped.get(slug)));
  const [title, source] = titleAndSource(text);
  const headings = text.split("\n").filter((l) => /^#{2,3} /.test(l)).map((l) => l.replace(/^#+/, "").trim());
  sources[id] = { slug, title, source, headings, chars: [...text].length };
  files[`distillations/${slug}.md`] = text;
}
const today = new Date();
const packed = [today.getFullYear(), today.getMonth() + 1, today.getDate()].map((n) => String(n).padStart(2, "0")).join("-");
files["catalog.json"] = { corpus: path.basename(path.resolve(app, "../..")), task: TASK, packed, sources };

const concepts = JSON.parse(read(path.join(app, "concept-index.json")));
if (concepts.schema_version !== 3) {
  throw new Error(`concept-index.json is schema ${concepts.schema_version}; src/corpus.js reads schema 3 (a topics block, then concept rows). Rebuild the app on a topic-filed index.`);
}
files["concept-index.json"] = concepts;
files["lens-index.json"] = JSON.parse(read(path.join(app, "lens-index.json")));
files["task-index.json"] = JSON.parse(read(path.join(distDir, "task-index.json")));

// A workflow folder's served files: its top-level markdown, less authoring notes.
const addWorkflow = (name, dir) => {
  if (!isFile(path.join(dir, "SKILL.md"))) throw new Error(`workflow ${name} has no SKILL.md in ${dir}`);
  if (Object.keys(files).some((k) => k.startsWith(`workflows/${name}/`))) throw new Error(`workflow ${name} is named twice`);
  for (const f of fs.readdirSync(dir)) {
    if (f.startsWith(".") || !f.endsWith(".md") || NOT_SERVED.some((re) => re.test(f)) || !isFile(path.join(dir, f))) continue;
    files[`workflows/${name}/${f}`] = read(path.join(dir, f));
  }
};
const skills = path.join(app, ".claude", "skills");
for (const name of fs.existsSync(skills) ? fs.readdirSync(skills).sort() : []) {
  if (!name.startsWith(".") && !opts.drop.includes(name)) addWorkflow(name, path.join(skills, name));
}
const agents = path.join(app, ".claude", "agents");
for (const f of fs.existsSync(agents) ? fs.readdirSync(agents).sort() : []) {
  const name = f.replace(/\.md$/, "");
  if (!f.endsWith(".md") || opts.drop.includes(name)) continue;
  if (Object.keys(files).some((k) => k.startsWith(`workflows/${name}/`))) throw new Error(`workflow ${name} is named twice`);
  files[`workflows/${name}/SKILL.md`] = read(path.join(agents, f));
}
for (const dir of opts.workflow) addWorkflow(path.basename(dir), dir);

files["workflows/guide/SKILL.md"] = read(opts.guide ?? path.join(app, "CLAUDE.md"));
files["workflows/guide/DISCLAIMER.md"] = read(path.join(app, "DISCLAIMER.md"));
files["workflows/guide/LICENSE-CONTENT.md"] = read(path.join(app, "LICENSE-CONTENT"));

const out = path.join(here, "src/bundle.json");
const sorted = Object.fromEntries(Object.keys(files).sort().map((k) => [k, files[k]]));
fs.writeFileSync(out, JSON.stringify({ built: today.toISOString(), files: sorted }));
const workflows = new Set(Object.keys(files).filter((k) => k.startsWith("workflows/")).map((k) => k.split("/")[1]));
const kb = Math.round(fs.statSync(out).size / 1024);
console.log(`bundle.json: ${Object.keys(sources).length} distillations, ${workflows.size} workflows (${[...workflows].sort().join(", ")}), ${kb} KB, from ${path.relative(process.cwd(), app) || "."}`);
