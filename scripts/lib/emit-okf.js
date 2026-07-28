/**
 * OKF bundle emitter — serialise a compiled app into an Open Knowledge
 * Format (OKF v0.2) bundle.
 *
 * The emitter is a serialiser, not a producer. Its input is a BUILT app
 * directory, which means every distribution gate has already run upstream
 * in build.js: the max_scope ceiling, the max_visibility ceiling, and the
 * verbatim-restriction gate ([V] markers banned above open-nc scopes).
 * Nothing here re-reads a source, re-derives a claim, or re-implements a
 * gate — the bundle is a pure function of the gated app output.
 *
 * Mapping (grounded-forge → OKF v0.2):
 *   distillation {slug}-{task}.md   → concept file /{task}/{slug}.md
 *   task-index.json (per axis)      → reserved /{task}/index.md router
 *   lens spec                       → concept file /lenses/{slug}.md (type: lens)
 *   distillation-sources.json       → /LICENCE-MANIFEST.md + per-file scope
 *   concept-index.json co-occurrence→ "Related concepts" markdown links
 *   **Source:** line                → frontmatter sources: family + resource:
 *
 * Trust fields are deliberately conservative: concept files carry
 * generated: (actor `grounded-forge/{version}`, per the spec's
 * producer/version convention) and do NOT carry verified: — the Pass I
 * audit is same-model-family internal consistency whose receipts live at
 * corpus level, not the independent confirmation OKF's verified: asserts.
 *
 * Determinism: rebuilds from an unchanged corpus produce byte-identical
 * bundles (tracked bundles diff clean). The only date emitted is
 * generated.at, taken from the source distillation's last git commit —
 * stable until the distillation itself changes; omitted when the corpus
 * is not a git checkout.
 *
 * Cross-links are emitted as RELATIVE paths, not the spec-recommended
 * bundle-absolute form. Both are OKF-legal; the absolute form resolves
 * only inside an OKF-aware consumer, while relative links also navigate
 * on GitHub, in Obsidian, on disk, and under the repo's link audits.
 * Concept ids are unchanged (still the path minus .md).
 */

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const OKF_VERSION = "0.2";

// ---------------------------------------------------------------------------
// Emission
// ---------------------------------------------------------------------------

/**
 * @param {object} opts
 * @param {string} opts.appDir      Built app directory (gated input).
 * @param {string} opts.bundleDir   Bundle destination; recreated from scratch.
 * @param {string} opts.corpusDir   Corpus root, for git provenance dates.
 * @param {string} opts.profileName Build profile name (bundle identity).
 * @param {string} opts.version     grounded-forge version, for generated.by.
 * @param {string} [opts.corpusName] Corpus display name for the root index.
 * @returns {{conceptCount:number, taskAxes:string[], lensCount:number, warnings:string[]}}
 */
function emitOkfBundle(opts) {
  const { appDir, bundleDir, corpusDir, profileName, version } = opts;
  const warnings = [];

  const slugTable = readJson(path.join(appDir, "slug-table.json")) || { slugs: {} };
  const idToSlug = slugTable.slugs || {};
  const slugToId = new Map(
    Object.entries(idToSlug).map(([id, slug]) => [slug, id])
  );
  const conceptIndex = readJson(path.join(appDir, "concept-index.json")) || { concepts: {} };
  const provenance = readJson(path.join(appDir, "distillation-sources.json")) || { sources: [] };
  const scopeBySlug = new Map(
    (provenance.sources || []).map((s) => [s.slug, s])
  );

  // Co-occurrence graph from the concept index: two sources are related
  // when they cover a shared concept. id -> Map(relatedId -> Set(concept)).
  // Deterministic — no embedding similarity, no model call.
  const related = new Map();
  for (const [key, entry] of Object.entries(conceptIndex.concepts || {})) {
    const ids = (entry.sources || []).map((s) => s.id);
    for (const a of ids) {
      if (!related.has(a)) related.set(a, new Map());
      for (const b of ids) {
        if (a === b) continue;
        if (!related.get(a).has(b)) related.get(a).set(b, new Set());
        related.get(a).get(b).add(entry.name || key);
      }
    }
  }

  // -- catalogue the app's distillations (the gated matrix cells) ----------
  const distDir = path.join(appDir, "distillations");
  const taskAxes = fs.existsSync(distDir)
    ? fs
        .readdirSync(distDir, { withFileTypes: true })
        .filter((e) => e.isDirectory())
        .map((e) => e.name)
        .sort()
    : [];

  const cells = new Map(); // `${task}/${slug}` -> cell
  for (const task of taskAxes) {
    const dir = path.join(distDir, task);
    const suffix = `-${task}.md`;
    for (const file of fs.readdirSync(dir).sort()) {
      if (!file.endsWith(".md")) continue;
      if (file === "README.md" || /-DISTILLATION-INDEX\.md$/i.test(file)) continue;
      // Underscore-prefixed files are operator staging artefacts by repo
      // convention (e.g. _pass_G_skips.md); not cells, not warned about.
      if (file.startsWith("_")) continue;
      if (!file.endsWith(suffix)) {
        // Lens-variant or other non-canonical shape; the bundle carries one
        // concept file per (source, task) cell.
        warnings.push(`skipped non-cell file: ${task}/${file}`);
        continue;
      }
      const slug = file.slice(0, -suffix.length);
      const body = fs.readFileSync(path.join(dir, file), "utf8");
      const title = stripTaskSuffix((body.match(/^#\s+(.+)$/m) || [])[1] || slug);
      const sourceLine = (body.match(/^\*\*Source:\*\*\s*(.+)$/m) || [])[1] || "";
      let url = (sourceLine.match(/https?:\/\/\S+/) || [])[0] || "";
      url = url.replace(/[.,;)\]]+$/, "");
      cells.set(`${task}/${slug}`, {
        task,
        slug,
        id: slugToId.get(slug) || null,
        title,
        sourceLine,
        url,
        body,
      });
    }
  }

  // -- emit ---------------------------------------------------------------
  fs.rmSync(bundleDir, { recursive: true, force: true });
  fs.mkdirSync(bundleDir, { recursive: true });

  const sortedCells = [...cells.values()].sort((a, b) =>
    `${a.task}/${a.slug}`.localeCompare(`${b.task}/${b.slug}`)
  );

  for (const cell of sortedCells) {
    const dest = path.join(bundleDir, cell.task, `${cell.slug}.md`);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.writeFileSync(
      dest,
      conceptFileFor(cell, {
        cells,
        related,
        idToSlug,
        scopeBySlug,
        taskAxes,
        corpusDir,
        version,
        warnings,
      })
    );
  }

  // -- per-axis reserved index.md from the situation router ----------------
  for (const task of taskAxes) {
    const taskIndex = readJson(path.join(distDir, task, "task-index.json"));
    fs.writeFileSync(
      path.join(bundleDir, task, "index.md"),
      taskIndexMd(task, taskIndex, cells, idToSlug)
    );
  }

  // -- lenses --------------------------------------------------------------
  const lensCount = emitLenses(appDir, bundleDir, corpusDir, version, warnings);

  // -- licence manifest ----------------------------------------------------
  writeLicenceManifest(bundleDir, profileName, version, provenance);

  // -- reserved root index.md ---------------------------------------------
  fs.writeFileSync(
    path.join(bundleDir, "index.md"),
    rootIndexMd({
      corpusName: opts.corpusName || provenance.corpus || "corpus",
      profileName,
      version,
      taskAxes,
      cells,
      lensCount,
      mostRestrictiveScope: provenance.most_restrictive_scope || "open",
    })
  );

  return { conceptCount: cells.size, taskAxes, lensCount, warnings };
}

// One OKF concept file: spec-native frontmatter + the distillation body
// verbatim (in-bundle cross-links repathed) + appended Related-concepts
// links derived from the concept index.
function conceptFileFor(cell, ctx) {
  const { cells, related, idToSlug, scopeBySlug, taskAxes, corpusDir, version, warnings } = ctx;
  const { task, slug, id, title, sourceLine, url } = cell;

  const prov = scopeBySlug.get(slug);
  if (!prov) {
    warnings.push(`no provenance row for source ${slug} (${task}); scope omitted`);
  }
  const generatedAt = gitLastCommitIso(
    corpusDir,
    path.join("distillations", task, `${slug}-${task}.md`)
  );
  // Source URL: the .source.md sidecar in the corpus of record is the
  // authority; the distillation's own **Source:**-line URL is the fallback.
  const resource = sidecarUrl(corpusDir, slug) || url || null;

  const fm = ["---", "type: distillation", `title: ${yamlStr(title)}`];
  fm.push(
    `description: ${yamlStr(
      `${title}, projected onto the ${task} task axis; evidence markers and attribution travel in-band.`
    )}`
  );
  if (resource) fm.push(`resource: ${resource}`);
  fm.push(`tags: [distillation, ${task}]`);
  // Extension keys (spec §5: producers may add arbitrary keys).
  fm.push(`task: ${task}`);
  if (prov) fm.push(`scope: ${prov.scope}`);
  if (sourceLine) {
    fm.push("sources:");
    fm.push(`  - id: ${slug}`);
    fm.push(`    title: ${yamlStr(stripMd(sourceLine))}`);
    if (resource) fm.push(`    resource: ${resource}`);
  }
  fm.push("generated:");
  fm.push(`  by: grounded-forge/${version}`);
  if (generatedAt) fm.push(`  at: ${generatedAt}`);
  fm.push("---", "");

  // Body travels verbatim from the gated app. The one transform is path
  // repair: app-layout distillation cross-links (rooted, ../-relative, and
  // same-axis sibling forms) are repathed to their bundle-layout targets
  // when the target travels in this bundle. Links to artefacts that stay
  // at corpus level (references/, docs/) are left as-written; OKF
  // consumers must tolerate links whose targets are not in the bundle.
  const repath = (whole, linkTask, linkSlug) =>
    cells.has(`${linkTask}/${linkSlug}`)
      ? `](${relLink(task, linkTask, `${linkSlug}.md`)})`
      : whole;
  let body = cell.body
    .replace(/\]\(distillations\/([a-z0-9-]+)\/([a-z0-9-]+)-\1\.md\)/g, repath)
    .replace(/\]\(\.\.\/([a-z0-9-]+)\/([a-z0-9-]+)-\1\.md\)/g, repath)
    .replace(
      new RegExp(`\\]\\(([a-z0-9-]+)-${task}\\.md\\)`, "g"),
      (whole, linkSlug) => repath(whole, task, linkSlug)
    );

  let out = fm.join("\n") + body.trimEnd() + "\n";

  // Related concepts: deterministic links from the concept index.
  const sameSource = taskAxes
    .filter((t) => t !== task && cells.has(`${t}/${slug}`))
    .map((t) => `[${t}](${relLink(task, t, `${slug}.md`)})`);

  const rel = [];
  if (id && related.has(id)) {
    for (const [relId, concepts] of related.get(id)) {
      const relSlug = idToSlug[relId];
      if (relSlug && cells.has(`${task}/${relSlug}`)) {
        rel.push({
          slug: relSlug,
          title: cells.get(`${task}/${relSlug}`).title,
          shared: [...concepts].sort(),
        });
      }
    }
  }
  rel.sort(
    (a, b) => b.shared.length - a.shared.length || a.slug.localeCompare(b.slug)
  );

  if (sameSource.length || rel.length) {
    out += "\n## Related concepts\n";
    if (sameSource.length) {
      out += `\n**Same source, other task axes:** ${sameSource.join(" · ")}\n`;
    }
    if (rel.length) {
      out += "\n";
      for (const r of rel) {
        out += `- [${r.title}](${r.slug}.md) — shared: ${r.shared
          .slice(0, 4)
          .join(", ")}\n`;
      }
    }
  }
  return out;
}

// Reserved per-axis index.md: the situation router rendered as grouped
// link lists (progressive disclosure per spec §4). No frontmatter —
// reserved files carry none.
function taskIndexMd(task, taskIndex, cells, idToSlug) {
  const lines = [
    `# ${task} — situation router`,
    "",
    `One concept file per source, projected onto the \`${task}\` task axis. Each row maps a situation to the concept files that apply. Bundle root: [index.md](../index.md).`,
    "",
  ];
  for (const section of (taskIndex && taskIndex.sections) || []) {
    const rows = routerRows(section, cells, idToSlug, task);
    if (!rows.length) continue;
    lines.push(`## ${section.section}`, "");
    lines.push(...rows, "");
  }
  // Fallback (and completeness backstop): every cell in this axis, listed.
  const all = [...cells.values()]
    .filter((c) => c.task === task)
    .sort((a, b) => a.slug.localeCompare(b.slug));
  lines.push(`## All concept files (${all.length})`, "");
  for (const c of all) {
    lines.push(`- [${c.title}](${c.slug}.md)`);
  }
  lines.push("");
  return lines.join("\n");
}

// Task-index schemas differ across axes: situation-router axes use columns
// [situation, ids] with an id ARRAY; phase axes use [need, id, when] with a
// single id STRING. Resolve by column name, tolerate both.
function routerRows(section, cells, idToSlug, task) {
  const cols = section.columns || [];
  const idIdx = cols.findIndex((c) => c === "ids" || c === "id");
  const labelIdx = cols.findIndex((c) =>
    ["situation", "need", "question"].includes(c)
  );
  const out = [];
  for (const row of section.rows || []) {
    const rawIds = idIdx >= 0 ? row[idIdx] : row.find(Array.isArray);
    const ids = Array.isArray(rawIds) ? rawIds : rawIds ? [rawIds] : [];
    const label =
      labelIdx >= 0 ? row[labelIdx] : row.find((c) => typeof c === "string") || "";
    const links = ids
      .map((id) => {
        const slug = idToSlug[id];
        return slug && cells.has(`${task}/${slug}`)
          ? `[${slug}](${slug}.md)`
          : null;
      })
      .filter(Boolean);
    if (links.length) out.push(`- ${stripMd(label)} → ${links.join(", ")}`);
  }
  return out;
}

// Lens specs travel as concept files under /lenses/. Each already carries
// YAML frontmatter (name, kind, visibility); the emitter injects the OKF
// fields — `type: lens` plus title (from name:), description (the first
// sentence of the spec's **Purpose:** line), and generated — ahead of the
// existing keys. Unknown types are legal: consumers that don't know lenses
// skip them, consumers that do get the full spec.
function emitLenses(appDir, bundleDir, corpusDir, version, warnings) {
  const srcDir = path.join(appDir, "lenses");
  if (!fs.existsSync(srcDir)) return 0;
  const files = fs
    .readdirSync(srcDir)
    .filter(
      (f) =>
        f.endsWith(".md") &&
        f !== "LENS-INDEX.md" &&
        f !== "README.md" &&
        fs.statSync(path.join(srcDir, f)).isFile()
    )
    .sort();
  if (!files.length) return 0;

  const destDir = path.join(bundleDir, "lenses");
  fs.mkdirSync(destDir, { recursive: true });
  const emitted = [];
  for (const f of files) {
    const raw = fs.readFileSync(path.join(srcDir, f), "utf8");
    const slug = f.replace(/\.md$/, "");
    const generatedAt = gitLastCommitIso(corpusDir, path.join("lenses", f));
    let out;
    if (raw.startsWith("---\n")) {
      const fmEnd = raw.indexOf("\n---", 4);
      const fmBlock = raw.slice(4, fmEnd);
      const inject = [];
      if (!/^type:/m.test(fmBlock)) inject.push("type: lens");
      if (!/^title:/m.test(fmBlock)) {
        const name = (fmBlock.match(/^name:\s*(.+)\s*$/m) || [])[1];
        inject.push(`title: ${yamlStr(name || slug)}`);
      }
      if (!/^description:/m.test(fmBlock)) {
        const purpose = (raw.match(/^\*\*Purpose:\*\*\s*(.+)$/m) || [])[1];
        const firstSentence = purpose
          ? (stripMd(purpose).match(/^(.+?\.)(?:\s|$)/) || [null, stripMd(purpose)])[1]
          : null;
        if (firstSentence) inject.push(`description: ${yamlStr(firstSentence)}`);
      }
      if (!/^generated:/m.test(fmBlock)) {
        inject.push("generated:", `  by: grounded-forge/${version}`);
        if (generatedAt) inject.push(`  at: ${generatedAt}`);
      }
      out = inject.length
        ? "---\n" + inject.join("\n") + "\n" + fmBlock + raw.slice(fmEnd)
        : raw;
    } else {
      warnings.push(`lens ${f} has no frontmatter; type: lens block prepended`);
      out = `---\ntype: lens\ntitle: ${yamlStr(slug)}\n---\n\n` + raw;
    }
    fs.writeFileSync(path.join(destDir, f), out);
    emitted.push(slug);
  }

  const lines = [
    "# Lenses",
    "",
    "Per-distillation modifiers: each lens reweights what is salient in a distillation without becoming a third axis. Applicability is decided per distillation at ingestion (Pass G). Bundle root: [index.md](../index.md).",
    "",
    ...emitted.map((slug) => `- [${slug}](${slug}.md)`),
    "",
  ];
  fs.writeFileSync(path.join(destDir, "index.md"), lines.join("\n"));
  return emitted.length;
}

// The licence manifest travels inside the bundle (the app packager writes
// its manifest transiently at tar time; a bundle is browsed in place, so
// the constraint must sit in the tree). It is a concept document, so it
// carries a type.
function writeLicenceManifest(bundleDir, profileName, version, provenance) {
  const rows = (provenance.sources || [])
    .slice()
    .sort((a, b) => a.slug.localeCompare(b.slug));
  const scope = provenance.most_restrictive_scope || "open";
  const lines = [
    "---",
    "type: licence-manifest",
    'title: "Licence manifest"',
    `description: "Per-source scope and licence for every source behind this bundle; the bundle inherits the most-restrictive scope."`,
    "generated:",
    `  by: grounded-forge/${version}`,
    "---",
    "",
    "# Licence manifest",
    "",
    `**Bundle:** ${profileName} (OKF ${OKF_VERSION}, emitted by grounded-forge/${version})`,
    `**Most-restrictive scope:** ${scope}`,
    `**Sources:** ${rows.length}`,
    "",
    "## Scope levels",
    "",
    "| Scope | Meaning |",
    "|---|---|",
    "| open | Public, redistributable, no commercial restriction. |",
    "| open-nc | Public, redistributable, non-commercial use only. |",
    "| copyrighted | Single-organisation redistribution; further redistribution requires the right-holder's permission. |",
    "| confidential | Single-organisation use; not for redistribution. |",
    "| personal | Single-recipient use; not for sharing. |",
    "",
    "The bundle inherits the most-restrictive scope across all sources below. The recipient inherits that constraint.",
    "",
    "## Sources",
    "",
    "| Source | Scope | Licence |",
    "|---|---|---|",
    ...rows.map((r) => `| ${r.slug} | ${r.scope} | ${r.licence} |`),
    "",
  ];
  fs.writeFileSync(path.join(bundleDir, "LICENCE-MANIFEST.md"), lines.join("\n"));
}

// Reserved root index.md. The one index allowed frontmatter, and only the
// okf_version declaration (spec §4).
function rootIndexMd(opts) {
  const { corpusName, profileName, version, taskAxes, cells, lensCount, mostRestrictiveScope } = opts;
  const lines = [
    "---",
    `okf_version: "${OKF_VERSION}"`,
    "---",
    "",
    `# ${corpusName} — ${profileName} knowledge bundle`,
    "",
    `An Open Knowledge Format (OKF v${OKF_VERSION}) bundle emitted by grounded-forge/${version}. Each task axis is a directory of concept files; each concept file is one source projected onto that task under a 9-pass, source-only ingestion protocol, with evidence markers and attribution preserved in-band.`,
    "",
    "## Task axes",
    "",
  ];
  for (const task of taskAxes) {
    const n = [...cells.values()].filter((c) => c.task === task).length;
    lines.push(`- [${task}](${task}/index.md) — ${n} concept files`);
  }
  if (lensCount > 0) {
    lines.push("", `## Lenses`, "", `- [lenses](lenses/index.md) — ${lensCount} per-distillation modifiers`);
  }
  lines.push(
    "",
    "## Evidence markers",
    "",
    "Claims in concept files carry in-band evidence classification from ingestion:",
    "",
    "- `[V]` verbatim — exact source text, audited against the source.",
    "- `[AP]` attributed paraphrase.",
    "- `[AR]` attributed argument (the author's reasoning, restated).",
    "- `[AE]` attributed example.",
    "- `[BT]` borrowed-through — a discipline carried via an openly licensed source rather than its canonical (non-open) author.",
    "",
    "## Provenance and trust",
    "",
    `Concept files declare \`generated.by: grounded-forge/${version}\`; \`generated.at\` is the source distillation's last change date. They deliberately do not declare \`verified:\` — the ingestion audit (Pass I) is a same-model-family, source-only consistency check whose receipts live at corpus level in the producing repository, not the independent confirmation OKF's \`verified:\` field asserts. Treat every concept file as machine-generated under an audited protocol; the audit trail is one repository upstream.`,
    "",
    "## Licence",
    "",
    `Most-restrictive scope across sources: **${mostRestrictiveScope}**. Per-source scope and licence: [LICENCE-MANIFEST.md](LICENCE-MANIFEST.md).`,
    ""
  );
  return lines.join("\n");
}

// ---------------------------------------------------------------------------
// Bundle validation — the build-time conformance gate. The Rust `okf`
// CLI is the external check; this keeps the build self-sufficient (Node
// only) while enforcing the same producer-side rules.
// ---------------------------------------------------------------------------

function validateOkfBundle(bundleDir) {
  const errors = [];
  let conceptCount = 0;
  let linksChecked = 0;

  const mdFiles = [];
  (function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name.endsWith(".md")) mdFiles.push(full);
    }
  })(bundleDir);

  for (const file of mdFiles) {
    const rel = path.relative(bundleDir, file);
    const content = fs.readFileSync(file, "utf8");
    const base = path.basename(file);
    const hasFrontmatter = content.startsWith("---\n");

    if (base === "index.md" || base === "log.md") {
      // Reserved files carry no frontmatter — except the bundle-root
      // index.md, which may declare okf_version and nothing else.
      if (hasFrontmatter) {
        const fmEnd = content.indexOf("\n---", 4);
        const fm = content.slice(4, fmEnd);
        const isRoot = rel === "index.md";
        const keys = fm
          .split("\n")
          .filter((l) => /^\S/.test(l))
          .map((l) => l.split(":")[0]);
        if (!isRoot || keys.some((k) => k !== "okf_version")) {
          errors.push(`${rel}: reserved file carries disallowed frontmatter`);
        }
      }
    } else {
      conceptCount++;
      if (!hasFrontmatter) {
        errors.push(`${rel}: concept file missing frontmatter`);
        continue;
      }
      const fmEnd = content.indexOf("\n---", 4);
      const fm = fmEnd === -1 ? "" : content.slice(4, fmEnd);
      if (!/^type:\s*\S/m.test(fm)) {
        errors.push(`${rel}: concept file missing required 'type:' field`);
      }
    }

    // Internal links must resolve inside the bundle — the emitter wrote
    // them, so a miss is an emitter bug, not tolerated breakage. The one
    // tolerated case, matching the spec's, is a body link whose first
    // path segment names a directory this bundle does not carry (a
    // cross-axis link in a single-axis bundle, or a corpus-level path
    // like references/): the target legitimately lives outside the
    // bundle and consumers must tolerate it. When the segment IS a
    // directory of this bundle, the file must exist.
    const linkRe = /\]\(([^)\s#]+\.md)\)/g;
    let m;
    while ((m = linkRe.exec(content)) !== null) {
      const link = m[1];
      if (/^[a-z][a-z0-9+.-]*:/i.test(link)) continue;
      const target = link.startsWith("/")
        ? path.join(bundleDir, link)
        : path.resolve(path.dirname(file), link);
      const bundleRel = path.relative(path.resolve(bundleDir), target);
      if (bundleRel.startsWith("..")) {
        linksChecked++;
        errors.push(`${rel}: link escapes the bundle: ${link}`);
        continue;
      }
      const firstSeg = bundleRel.split(path.sep)[0];
      const segIsBundleDir =
        bundleRel.includes(path.sep) &&
        fs.existsSync(path.join(bundleDir, firstSeg)) &&
        fs.statSync(path.join(bundleDir, firstSeg)).isDirectory();
      if (bundleRel.includes(path.sep) && !segIsBundleDir) continue;
      linksChecked++;
      if (!fs.existsSync(target)) {
        errors.push(`${rel}: dangling bundle link ${link}`);
      }
    }
  }

  return { errors, conceptCount, linksChecked, fileCount: mdFiles.length };
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function readJson(p) {
  try {
    return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function yamlStr(s) {
  return `"${String(s).replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
}

// Relative link between bundle locations one directory deep. Directory ""
// is the bundle root.
function relLink(fromDir, toDir, file) {
  if (fromDir === toDir) return file;
  const up = fromDir ? "../" : "";
  return toDir ? `${up}${toDir}/${file}` : `${up}${file}`;
}

function stripMd(s) {
  return String(s).replace(/\*+/g, "").trim();
}

// Strip the ", {Task} Distillation" / " — {Task} Distillation" suffix from
// a distillation H1. Comma and em/en dash are the observed separators; a
// title that is nothing but the suffix falls back to the full H1.
function stripTaskSuffix(title) {
  const stripped = title.replace(/\s*[,—–]\s*[^,—–]*Distillation\s*$/i, "").trim();
  return stripped || title.trim();
}

// Source URL from the corpus of record: the .source.md sidecar's url:
// frontmatter field. Null when the sidecar is absent or carries no
// http(s) URL — nothing is invented for URL-less sources.
const sidecarUrlCache = new Map();
function sidecarUrl(corpusDir, slug) {
  const key = `${corpusDir} ${slug}`;
  if (sidecarUrlCache.has(key)) return sidecarUrlCache.get(key);
  let url = null;
  try {
    const raw = fs.readFileSync(
      path.join(corpusDir, "sources", "original", `${slug}.source.md`),
      "utf8"
    );
    if (raw.startsWith("---")) {
      const end = raw.indexOf("\n---", 3);
      const m = raw.slice(3, end).match(/^url:\s*(.+?)\s*$/m);
      const candidate = m ? m[1].replace(/^["']|["']$/g, "") : null;
      if (candidate && /^https?:\/\//.test(candidate)) url = candidate;
    }
  } catch {
    url = null;
  }
  sidecarUrlCache.set(key, url);
  return url;
}

// Last-commit date (ISO 8601) of a corpus file — the provenance anchor for
// generated.at. Stable across rebuilds until the distillation changes;
// null (field omitted) when the corpus is not a git checkout.
const gitDateCache = new Map();
function gitLastCommitIso(corpusDir, relPath) {
  const key = path.join(corpusDir, relPath);
  if (gitDateCache.has(key)) return gitDateCache.get(key);
  let out = null;
  try {
    out =
      execFileSync("git", ["log", "-1", "--format=%cI", "--", relPath], {
        cwd: corpusDir,
        stdio: ["ignore", "pipe", "ignore"],
      })
        .toString()
        .trim() || null;
  } catch {
    out = null;
  }
  gitDateCache.set(key, out);
  return out;
}

module.exports = { emitOkfBundle, validateOkfBundle, OKF_VERSION };
