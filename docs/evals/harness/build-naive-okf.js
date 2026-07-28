#!/usr/bin/env node
/**
 * Method F builder: a NAIVE flat-OKF bundle from the corpus's converted
 * sources, with no ingestion protocol and no audit.
 *
 * This is the "fork something off the shelf" baseline for the comparative
 * eval (see ../methodology.md, the OKF arms): what an operator gets by
 * wiki-fying their source texts straight into the OKF container. It is
 * deliberately a floor, and deterministic so anyone can regenerate it —
 * split each converted source on H1/H2 headings, one concept file per
 * section, `type: note` frontmatter, an index.md per source and at the
 * root. What it deliberately lacks is the point of the comparison:
 *
 *   - no source-only audit (no Pass I; nothing checked any section)
 *   - no task axis (one flat projection, not reference × task)
 *   - no evidence markers, no verbatim/paraphrase discipline
 *   - no cross-links (a deterministic chunker invents no concept graph)
 *   - no scope/licence labelling, no provenance frontmatter
 *
 * The bundle it produces PASSES `okf validate` — conformance is a
 * container property, not a grounding property, which is the argument.
 *
 * A stronger variant (F+: one-shot LLM wiki-fication, still un-audited)
 * is the fair upgrade if this floor reads as a strawman; it costs tokens
 * and is not deterministic, so it is not built here.
 *
 * Usage: node docs/evals/harness/build-naive-okf.js [corpus-dir] [out-dir]
 * Defaults: corpus.commons/demo -> _evals/okf-naive (gitignored)
 */

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.resolve(__dirname, "..", "..", "..");
const corpusDir = path.resolve(REPO_ROOT, process.argv[2] || "corpus.commons/demo");
const outDir = path.resolve(REPO_ROOT, process.argv[3] || "_evals/okf-naive");

const convertedDir = path.join(corpusDir, "sources", "converted");
if (!fs.existsSync(convertedDir)) {
  console.error(`No converted sources at ${convertedDir}`);
  process.exit(1);
}

const sources = fs
  .readdirSync(convertedDir)
  .filter(
    (f) =>
      f.endsWith(".md") &&
      !f.startsWith(".") &&
      !f.startsWith("_") &&
      /^[a-z0-9]/.test(f) &&
      !f.endsWith("-images-alt.md") &&
      f !== "README.md"
  )
  .sort();

fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir, { recursive: true });

function slugify(s, cap = 60) {
  return (
    s
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, cap)
      .replace(/-+$/, "") || "section"
  );
}

function yamlStr(s) {
  return `"${String(s).replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
}

let totalConcepts = 0;
const perSource = [];
for (const file of sources) {
  const slug = file.replace(/\.md$/, "");
  const text = fs.readFileSync(path.join(convertedDir, file), "utf8");
  const lines = text.split("\n");

  // Split on H1/H2 headings. Content before the first heading becomes a
  // front-matter section when non-trivial.
  const sections = [];
  let current = { heading: slug, body: [] };
  for (const line of lines) {
    const m = line.match(/^#{1,2}\s+(.+)$/);
    if (m) {
      if (current.body.join("\n").trim().length > 200 || sections.length > 0) {
        sections.push(current);
      }
      current = { heading: m[1].trim(), body: [line] };
    } else {
      current.body.push(line);
    }
  }
  sections.push(current);
  const kept = sections.filter((s) => s.body.join("\n").trim().length > 0);

  const srcDir = path.join(outDir, slug);
  fs.mkdirSync(srcDir, { recursive: true });
  const entries = [];
  kept.forEach((s, i) => {
    const name = `${String(i + 1).padStart(3, "0")}-${slugify(s.heading)}.md`;
    const fm = [
      "---",
      "type: note",
      `title: ${yamlStr(s.heading)}`,
      `source: ${slug}`,
      "---",
      "",
    ].join("\n");
    fs.writeFileSync(path.join(srcDir, name), fm + s.body.join("\n").trimEnd() + "\n");
    entries.push({ name, heading: s.heading });
  });
  totalConcepts += entries.length;
  perSource.push({ slug, count: entries.length });

  fs.writeFileSync(
    path.join(srcDir, "index.md"),
    [
      `# ${slug}`,
      "",
      ...entries.map((e) => `- [${e.heading.replace(/[\[\]]/g, "")}](${e.name})`),
      "",
    ].join("\n")
  );
}

fs.writeFileSync(
  path.join(outDir, "index.md"),
  [
    "---",
    'okf_version: "0.2"',
    "---",
    "",
    "# Naive knowledge bundle (Method F baseline)",
    "",
    "Converted source texts split by heading into concept files, no ingestion protocol, no audit. Built by docs/evals/harness/build-naive-okf.js as the comparative-eval floor.",
    "",
    "## Sources",
    "",
    ...perSource.map((s) => `- [${s.slug}](/${s.slug}/index.md) — ${s.count} concept files`),
    "",
  ].join("\n")
);

const sizeMb = (function du(dir) {
  let bytes = 0;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    bytes += e.isDirectory() ? du(p) : fs.statSync(p).size;
  }
  return bytes;
})(outDir) / (1024 * 1024);

console.log(
  `Naive OKF bundle: ${totalConcepts} concept files from ${sources.length} sources (${sizeMb.toFixed(1)} MB) -> ${path.relative(REPO_ROOT, outDir)}`
);
