// Read-only access to the packed app bundle (src/bundle.json, written by bundle.mjs):
// distillations, the task and concept indexes, the lens index and the workflows.
import bundle from "./bundle.json";

const PART_BYTES = 60000; // workflow files longer than this are served in parts

export class ToolInputError extends Error {}

const files = bundle.files;
export const connector = bundle.connector;
const TASK = connector.task;
const escapeRe = (t) => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const TASK_SUFFIX = new RegExp(`(-${escapeRe(TASK)})?\\.md$`);
const TASK_FILE = new RegExp(`([a-z0-9][a-z0-9-]*)-${escapeRe(TASK)}\\.md`, "g");
const bytes = (s) => new TextEncoder().encode(s).length;

export const loadJson = (rel) => {
  if (!(rel in files)) throw new Error(`${rel} unavailable`);
  return files[rel];
};

const sources = () => loadJson("catalog.json").sources;

const sourceBrief = (id) => {
  const s = sources()[id];
  return { id, slug: s.slug, title: s.title };
};

const slugToId = (slug) => {
  for (const [id, s] of Object.entries(sources())) if (s.slug === slug) return id;
  return null;
};

// Accepts a 3-character id, a slug, or a path/filename like distillations/{task}/{slug}-{task}.md.
const resolveSource = (raw) => {
  let ref = raw.toLowerCase().trim().replace(/^.*\//, "").replace(TASK_SUFFIX, "");
  if (ref in sources()) return ref;
  const id = slugToId(ref);
  if (id !== null) return id;
  const near = [];
  for (const s of Object.values(sources())) {
    if (ref !== "" && (s.slug.includes(ref) || s.title.toLowerCase().includes(ref))) near.push(s.slug);
  }
  throw new ToolInputError(`no distillation for '${ref}'` +
    (near.length ? `; did you mean: ${near.slice(0, 8).join(", ")}` : "; call list_sources to see them all"));
};

const headingLevel = (line) => {
  const m = /^(#{1,6}) /.exec(line);
  return m ? m[1].length : 0;
};

export const readDistillation = (ref, section) => {
  const id = resolveSource(ref);
  const s = sources()[id];
  const text = files[`distillations/${s.slug}.md`] ?? "";
  const head = { id, slug: s.slug, title: s.title };
  if (section.trim() === "") return [head, text];
  const want = section.trim().toLowerCase();
  const lines = text.split("\n");
  const start = lines.findIndex((l) => headingLevel(l) >= 2 && l.toLowerCase().includes(want));
  if (start === -1) {
    throw new ToolInputError(`no heading matching '${section}' in ${s.slug}; headings: ${s.headings.join(" | ")}`);
  }
  const level = headingLevel(lines[start]);
  const out = [];
  for (let i = start; i < lines.length; i++) {
    const l = headingLevel(lines[i]);
    if (i > start && l > 0 && l <= level) break;
    out.push(lines[i]);
  }
  return [{ ...head, section: lines[start].replace(/^#+/, "").trim() }, out.join("\n")];
};

// Every source a JSON fragment points at: 3-character ids, {slug}-{task}.md filenames and
// backticked slugs.
const sourcesIn = (node, found) => {
  if (Array.isArray(node) || (node && typeof node === "object")) {
    for (const v of Object.values(node)) sourcesIn(v, found);
    return;
  }
  if (typeof node !== "string") return;
  if (node in sources()) found.add(node);
  for (const m of [...node.matchAll(TASK_FILE), ...node.matchAll(/`([a-z0-9][a-z0-9-]*)`/g)]) {
    const id = slugToId(m[1]);
    if (id !== null) found.add(id);
  }
};

export const route = (section) => {
  const sections = loadJson("task-index.json").sections;
  if (section.trim() === "") {
    return {
      task: TASK,
      sections: sections.map((s) => ({ section: s.section, rows: (s.rows ?? []).length })),
      next: 'Call route with a section name (or a unique part of one, e.g. "Phase 4") for its rows.',
    };
  }
  const want = section.trim().toLowerCase();
  let hits = sections.filter((s) => s.section.toLowerCase() === want);
  if (hits.length === 0) hits = sections.filter((s) => s.section.toLowerCase().includes(want));
  if (hits.length !== 1) {
    throw new ToolInputError((hits.length === 0 ? `no section matches '${section}'` : `'${section}' matches several sections`) +
      "; sections: " + (hits.length ? hits : sections).map((s) => s.section).join(" | "));
  }
  const found = new Set();
  sourcesIn(hits[0], found);
  return { ...hits[0], sources: [...found].sort().map(sourceBrief) };
};

// The concept index is schema 3: a topics block, then concept rows
// [name, kind, synonyms, source_ids, topic_ids, contexts?]. Rows on a debate's side carry the
// debate's ID with a suffix (t031.1), so a topic's rows are those tagged with its ID or with
// its ID and a suffix.
const conceptIndex = () => {
  const index = loadJson("concept-index.json");
  if (index.schema_version !== 3) throw new Error("concept-index.json is not schema 3");
  return index;
};

export const listTopics = () => {
  const index = conceptIndex();
  return { topic_format: index.topic_format, count: index.topics.length, topics: index.topics };
};

// Accepts a topic ID (t031) or a topic's name, whole or a unique part of it.
const resolveTopic = (ref) => {
  const want = ref.trim().toLowerCase();
  const near = [];
  for (const t of conceptIndex().topics) {
    if (t[0] === want || t[1].toLowerCase() === want) return t;
    if (t[1].toLowerCase().includes(want)) near.push(t);
  }
  if (near.length === 1) return near[0];
  throw new ToolInputError(`no single topic matching '${ref}'` +
    (near.length ? "; did you mean: " + near.slice(0, 8).map((t) => `${t[0]} ${t[1]}`).join(" | ")
      : "; call list_topics to see them all"));
};

export const findConcepts = (query, topic, limit) => {
  const tokens = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const within = topic.trim() === "" ? null : resolveTopic(topic);
  if (tokens.length === 0 && within === null) throw new ToolInputError("query or topic required");
  const index = conceptIndex();
  const phrase = tokens.join(" ");
  const scored = [];
  for (const row of index.concepts) {
    const [name, , synonyms, , topicIds] = row;
    if (within !== null && !topicIds.some((id) => id === within[0] || id.startsWith(within[0] + "."))) continue;
    const names = [name, ...synonyms].map((n) => n.toLowerCase());
    const hay = names.join(" ");
    if (!tokens.every((t) => hay.includes(t))) continue;
    const score = tokens.length === 0 ? 0 : names.includes(phrase) ? 0 : name.toLowerCase().startsWith(phrase) ? 1 : 2;
    scored.push([score, bytes(name), row]);
  }
  scored.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const topicNames = Object.fromEntries(index.topics.map((t) => [t[0], t[1]]));
  // A topic's rows come back whole: the topic is the unit a question routes through.
  const shown = within !== null && tokens.length === 0 ? scored : scored.slice(0, limit);
  const concepts = shown.map(([, , row]) => {
    const [name, kind, synonyms, ids, topicIds] = row;
    const contexts = row[5] ?? {};
    const srcs = ids.filter((id) => id in sources())
      .map((id) => ({ ...sourceBrief(id), ...(id in contexts ? { context: contexts[id] } : {}) }));
    const topics = topicIds.map((id) => ({ id, name: topicNames[id.split(".")[0]] ?? "" }));
    return { concept: name, kind, synonyms, topics, sources: srcs };
  });
  const head = {};
  if (query) head.query = query;
  if (within) head.topic = `${within[0]} ${within[1]}`;
  return { ...head, matches: scored.length, shown: concepts.length, concepts };
};

export const listSources = (query) => {
  const tokens = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const out = [];
  for (const [id, s] of Object.entries(sources())) {
    const hay = `${s.slug} ${s.title} ${s.source}`.toLowerCase();
    if (!tokens.every((t) => hay.includes(t))) continue;
    out.push({ id, slug: s.slug, title: s.title, source: s.source });
  }
  return { count: out.length, sources: out };
};

export const hasLenses = () => "lens-index.json" in files;

export const workflowNames = () => [...new Set(Object.keys(files)
  .map((k) => /^workflows\/([^/]+)\/SKILL\.md$/.exec(k)?.[1])
  .filter(Boolean))].sort();

// Split on blank lines so no part ends mid-paragraph.
const splitParts = (text) => {
  if (bytes(text) <= PART_BYTES) return [text];
  const parts = [];
  let cur = "";
  for (const para of text.split("\n\n")) {
    if (cur !== "" && bytes(cur) + bytes(para) + 2 > PART_BYTES) {
      parts.push(cur);
      cur = "";
    }
    cur += (cur === "" ? "" : "\n\n") + para;
  }
  parts.push(cur);
  return parts;
};

export const workflow = (name, file, part) => {
  const names = workflowNames();
  if (!names.includes(name)) throw new ToolInputError(`unknown workflow '${name}'; workflows: ${names.join(", ")}`);
  const prefix = `workflows/${name}/`;
  const inDir = Object.keys(files).filter((k) => k.startsWith(prefix) && !k.slice(prefix.length).includes("/"))
    .map((k) => k.slice(prefix.length)).filter((f) => f.endsWith(".md")).sort();
  const want = file === "" ? "SKILL.md" : file.replace(/^.*\//, "");
  if (!inDir.includes(want)) throw new ToolInputError(`workflow '${name}' has no file '${want}'; files: ${inDir.join(", ")}`);
  const parts = splitParts(files[prefix + want]);
  if (!(part >= 1 && part <= parts.length)) throw new ToolInputError(`part must be 1-${parts.length}`);
  const head = { workflow: name, file: want, part, parts: parts.length, other_files: inDir.filter((f) => f !== want) };
  if (part < parts.length) head.next = `Read part ${part + 1} before acting on this file.`;
  return [head, parts[part - 1]];
};
