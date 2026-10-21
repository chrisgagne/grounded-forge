#!/usr/bin/env node
// Self-test of the Worker's MCP handler, run in-process past the OAuth layer against whatever
// src/bundle.json holds:
//
//   npm test     (bundles src/mcp.js with esbuild into .wrangler/test/, then runs this file)
import fs from "node:fs";
import mcp from "./.wrangler/test/mcp.mjs";

const PART_BYTES = 60000; // as in src/corpus.js
const { files, connector } = JSON.parse(fs.readFileSync(new URL("./src/bundle.json", import.meta.url), "utf8"));
const want = connector.selftest; // this connector's expected slugs, sections and words
const lenses = "lens-index.json" in files;

let failures = 0;
let nextId = 1;
const check = (label, ok, detail = "") => {
  if (!ok) failures++;
  console.log(`  ${ok ? "ok  " : "FAIL"} ${label}${detail !== "" ? `  (${detail})` : ""}`);
};

const post = async (body, headers = {}) => {
  const res = await mcp.fetch(new Request("https://test/mcp", {
    method: "POST", headers: { "Content-Type": "application/json", ...headers }, body: JSON.stringify(body),
  }), {}, { props: { login: "selftest" } });
  const text = await res.text();
  return [res.status, text ? JSON.parse(text) : null];
};

const call = async (name, args) => {
  const [, r] = await post({ jsonrpc: "2.0", id: nextId++, method: "tools/call", params: { name, arguments: args } });
  const content = r.result?.content ?? [];
  return { error: !!r.result?.isError || !!r.error, head: content[0] ? JSON.parse(content[0].text) : {}, body: content[1]?.text ?? "" };
};

console.log(`self-test: ${connector.id}`);
let [status, r] = await post({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-06-18" } });
check("initialize", r.result?.serverInfo?.name === connector.id, `status ${status}`);
check("instructions carry the licence terms", (r.result?.instructions ?? "").includes(want.licenceWord));

[, r] = await post({ jsonrpc: "2.0", id: 2, method: "tools/list" });
const names = (r.result?.tools ?? []).map((t) => t.name);
check("tools/list", JSON.stringify([...names].sort()) === JSON.stringify(
  ["find_concepts", ...(lenses ? ["get_lenses"] : []), "get_workflow", "list_sources", "list_topics", "read_distillation", "route"]),
  names.join(","));
check("no unfilled placeholder in a tool description", !JSON.stringify(r.result?.tools ?? []).includes("{{"));

let c = await call("get_workflow", { name: "guide" });
check("guide, with the disclaimer and licence beside it", !c.error && c.body.length > 1000
  && ["DISCLAIMER.md", "LICENSE-CONTENT.md"].every((f) => (c.head.other_files ?? []).includes(f)), `${c.body.length} chars`);

// The longest workflow file: in parts if it's over PART_BYTES, whole otherwise.
const [longest] = Object.keys(files).filter((k) => /^workflows\/[^/]+\/[^/]+\.md$/.test(k))
  .sort((a, b) => Buffer.byteLength(files[b]) - Buffer.byteLength(files[a]));
const [, wfName, wfFile] = longest.split("/");
c = await call("get_workflow", { name: wfName, file: wfFile });
const parts = c.head.parts ?? 0;
if (Buffer.byteLength(files[longest]) > PART_BYTES) {
  check("long workflow file comes in parts", !c.error && parts > 1 && "next" in c.head, `${longest}: ${parts} parts`);
  c = await call("get_workflow", { name: wfName, file: wfFile, part: parts });
  check("last part has no next", !c.error && !("next" in c.head));
} else {
  check("longest workflow file comes whole", !c.error && parts === 1 && !("next" in c.head), longest);
}

c = await call("get_workflow", { name: "guide", file: "../../../wrangler.jsonc" });
check("path traversal refused", c.error);

c = await call("route", {});
check("route lists sections", (c.head.sections ?? []).length > 5, `${(c.head.sections ?? []).length} sections`);

c = await call("route", { section: want.phase });
check(`route ${want.phase}`, !c.error && (c.head.rows ?? []).length > 0 && (c.head.sources ?? []).length > 0,
  `${(c.head.rows ?? []).length} rows, ${(c.head.sources ?? []).length} sources`);

c = await call("read_distillation", { source: want.slug });
check("read by slug", !c.error && c.body.includes(want.slugText), `${c.body.length} chars`);
const id = c.head.id ?? "";

c = await call("read_distillation", { source: id });
check("read by id", !c.error && c.head.slug === want.slug, id);

c = await call("read_distillation", { source: want.sectionPath, section: want.section });
check("read a section by path", !c.error && "section" in c.head, c.head.section ?? "");

c = await call("read_distillation", { source: "no-such-source" });
check("unknown source is a tool error", c.error);

c = await call("list_topics", {});
const topics = c.head.topics ?? [];
check("list_topics", !c.error && topics.length > 0, `${topics.length} topics`);

c = await call("find_concepts", { query: want.concept });
check("find_concepts", (c.head.matches ?? 0) > 0, `${c.head.matches ?? 0} matches`);

const first = topics[0] ?? ["", "", [], "", "", "", 0];
c = await call("find_concepts", { topic: first[0] });
check("find_concepts by topic returns the topic's rows", !c.error && c.head.shown === first[6],
  `${c.head.shown ?? 0} of ${first[6]} rows under ${first[0]}`);

c = await call("find_concepts", {});
check("find_concepts with neither query nor topic is a tool error", c.error);

c = await call("list_sources", { query: want.sourceQuery });
check("list_sources", (c.head.count ?? 0) > 0, `${c.head.count ?? 0} sources`);

c = await call("list_sources", {});
check("list_sources all", (c.head.count ?? 0) >= want.minSources, `${c.head.count ?? 0} sources`);

if (lenses) {
  c = await call("get_lenses", {});
  check("get_lenses", "lenses" in c.head, `${Object.keys(c.head.lenses ?? {}).length} lenses`);
}

[status] = await post({ jsonrpc: "2.0", id: 99, method: "ping" }, { Origin: "https://evil.example" });
check("foreign Origin refused", status === 403, `got ${status}`);

[status] = await post({ jsonrpc: "2.0", method: "notifications/initialized" });
check("notification gets 202", status === 202, `got ${status}`);

console.log(failures ? `${failures} FAILED` : "all passed");
process.exit(failures ? 1 : 0);
