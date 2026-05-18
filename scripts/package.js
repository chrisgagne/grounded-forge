#!/usr/bin/env node

/**
 * Package a compiled app as a versioned, scope-labelled tarball.
 *
 * Usage:
 *   node scripts/package.js <app-name>
 *   node scripts/package.js decision
 *   node scripts/package.js --all
 *
 * Reads the app at corpus.commons/{corpus}/apps/{app-name}/, computes the
 * most-restrictive scope across its references, writes a manifest of
 * every reference's licence + scope into the bundle, and produces
 *   corpus.commons/{corpus}/distros/{app-name}-v{version}-{scope}.tar.gz
 *
 * Hard refusals (build/operator bug, never an intentional ship):
 *   - secrets present (.env, credentials.json, *.pem)
 *   - operator-only artefacts present (_audit/, _planning/, _ingest_*)
 *   - reference with no parseable Scope: line
 *
 * Labels (constraint travels with artefact, recipient sees in filename):
 *   - bundle's most-restrictive scope → filename suffix
 *   - per-reference licence + scope → LICENCE-MANIFEST.md in tarball root
 */

const fs = require("fs");
const path = require("path");
const tar = require("tar");
const yaml = require("js-yaml");

const REPO_ROOT = path.resolve(__dirname, "..");
const CONFIG_FILE = "builds.yaml";

const SCOPE_RANK = {
  open: 0,
  "open-nc": 1,
  copyrighted: 2,
  confidential: 3,
  personal: 4,
};

const SECRET_PATTERNS = [/^\.env/, /credentials\.json$/, /\.pem$/, /\.key$/];
const OPERATOR_ARTEFACTS = [/^_audit\//, /^_planning\//, /\/_audit\//, /\/_planning\//, /_ingest_/];

function readVersion() {
  const pkg = JSON.parse(
    fs.readFileSync(path.join(REPO_ROOT, "package.json"), "utf8")
  );
  return pkg.version;
}

function loadBuildsConfig() {
  const text = fs.readFileSync(path.join(REPO_ROOT, CONFIG_FILE), "utf8");
  return yaml.load(text);
}

function resolveAppDir(appName, config) {
  const profile = config.builds?.[appName];
  if (!profile) {
    throw new Error(
      `Unknown app: '${appName}'. Run 'npm run list' to see available profiles.`
    );
  }
  const appDir = path.resolve(REPO_ROOT, profile.output_dir);
  if (!fs.existsSync(appDir)) {
    throw new Error(
      `App not built: ${appDir}\nRun 'npm run build:${appName}' first.`
    );
  }
  return { appDir, profile };
}

function walk(dir, base = dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const rel = path.relative(base, full);
    if (entry.isDirectory()) {
      out.push(...walk(full, base));
    } else {
      out.push(rel);
    }
  }
  return out;
}

function refuseOnSecrets(files) {
  const hits = files.filter((f) =>
    SECRET_PATTERNS.some((p) => p.test(path.basename(f)))
  );
  if (hits.length) {
    throw new Error(
      `Refusing to package: secrets detected in app bundle.\n  ${hits.join("\n  ")}`
    );
  }
}

function refuseOnOperatorArtefacts(files) {
  const hits = files.filter((f) => OPERATOR_ARTEFACTS.some((p) => p.test(f)));
  if (hits.length) {
    throw new Error(
      `Refusing to package: operator-only artefacts in app bundle.\n  ${hits.join("\n  ")}`
    );
  }
}

function parseScope(filePath) {
  const text = fs.readFileSync(filePath, "utf8");
  const m = text.match(/^\*\*Scope:\*\*\s*(\S+)/m);
  return m ? m[1] : null;
}

function parseLicence(filePath) {
  const text = fs.readFileSync(filePath, "utf8");
  // Accept "Licence:", "License:", or "licensed:" (case-insensitive). The
  // licence string is usually wrapped in bold immediately after; fall back
  // to plain inline if no bold form is present.
  const bold = text.match(/licen[cs]e[d]?:\s*\*\*([^*]+)\*\*/i);
  if (bold) return bold[1].trim();
  const inline = text.match(/licen[cs]e[d]?:\s*([^.\n]+)/i);
  return inline ? inline[1].trim() : "unknown";
}

function inspectReferences(appDir) {
  const refsDir = path.join(appDir, "references");
  if (!fs.existsSync(refsDir)) {
    return { scopes: [], rows: [] };
  }
  const deepRefs = fs
    .readdirSync(refsDir)
    .filter((f) => f.endsWith("-deep.md"))
    .map((f) => path.join(refsDir, f));

  const rows = [];
  const missing = [];
  for (const ref of deepRefs) {
    const slug = path.basename(ref, ".md");
    const scope = parseScope(ref);
    const licence = parseLicence(ref);
    if (!scope) {
      missing.push(slug);
      continue;
    }
    rows.push({ slug, scope, licence });
  }

  if (missing.length) {
    throw new Error(
      `Refusing to package: ${missing.length} reference(s) missing **Scope:** line.\n  ${missing.join("\n  ")}`
    );
  }
  return { rows };
}

function mostRestrictiveScope(rows) {
  if (rows.length === 0) return "open";
  let maxScope = "open";
  let maxRank = -1;
  for (const r of rows) {
    const rank = SCOPE_RANK[r.scope];
    if (rank === undefined) {
      throw new Error(
        `Refusing to package: reference '${r.slug}' has unknown scope '${r.scope}'. Valid: ${Object.keys(SCOPE_RANK).join(", ")}`
      );
    }
    if (rank > maxRank) {
      maxRank = rank;
      maxScope = r.scope;
    }
  }
  return maxScope;
}

function writeManifest(appDir, appName, version, scope, rows) {
  const manifestPath = path.join(appDir, "LICENCE-MANIFEST.md");
  const lines = [
    `# Licence manifest`,
    ``,
    `**App:** ${appName}`,
    `**Version:** ${version}`,
    `**Most-restrictive scope:** ${scope}`,
    `**References:** ${rows.length}`,
    ``,
    `## Scope levels`,
    ``,
    `| Scope | Meaning |`,
    `|---|---|`,
    `| open | Public, redistributable, no commercial restriction. |`,
    `| open-nc | Public, redistributable, non-commercial use only. |`,
    `| copyrighted | Single-organisation redistribution; further redistribution requires the right-holder's permission. |`,
    `| confidential | Single-organisation use; not for redistribution. |`,
    `| personal | Single-recipient use; not for sharing. |`,
    ``,
    `The tarball's filename carries the most-restrictive scope across all bundled references. The recipient inherits that constraint.`,
    ``,
    `## References`,
    ``,
    `| Slug | Scope | Licence |`,
    `|---|---|---|`,
    ...rows
      .sort((a, b) => a.slug.localeCompare(b.slug))
      .map((r) => `| ${r.slug} | ${r.scope} | ${r.licence} |`),
    ``,
  ];
  fs.writeFileSync(manifestPath, lines.join("\n"));
  return manifestPath;
}

async function packageApp(appName) {
  const version = readVersion();
  const config = loadBuildsConfig();
  const { appDir } = resolveAppDir(appName, config);

  console.log(`\nPackaging: ${appName}`);
  console.log(`  App dir: ${path.relative(REPO_ROOT, appDir)}`);
  console.log(`  Version: ${version}`);

  // Distros dir is a sibling of apps/
  const distrosDir = path.resolve(appDir, "..", "..", "distros");
  fs.mkdirSync(distrosDir, { recursive: true });

  // Walk the app, run hard-fail gates.
  const files = walk(appDir);
  refuseOnSecrets(files);
  refuseOnOperatorArtefacts(files);

  // Inspect references, compute most-restrictive scope.
  const { rows } = inspectReferences(appDir);
  const scope = mostRestrictiveScope(rows);
  console.log(`  References: ${rows.length}`);
  console.log(`  Most-restrictive scope: ${scope}`);

  // Write the manifest into the app dir so it lands inside the tarball.
  const manifestPath = writeManifest(appDir, appName, version, scope, rows);
  console.log(`  Manifest: ${path.relative(REPO_ROOT, manifestPath)}`);

  // Tar it. cwd is the apps/ dir; the only entry is the app's folder name,
  // which becomes the top-level directory inside the tarball.
  const tarballName = `${appName}-v${version}-${scope}.tar.gz`;
  const tarballPath = path.join(distrosDir, tarballName);
  await tar.create(
    {
      file: tarballPath,
      gzip: true,
      cwd: path.dirname(appDir),
    },
    [path.basename(appDir)]
  );

  // Remove the manifest from the source tree (it lives inside the tarball only).
  fs.unlinkSync(manifestPath);

  const sizeKb = Math.round(fs.statSync(tarballPath).size / 1024);
  console.log(`\n  Wrote: ${path.relative(REPO_ROOT, tarballPath)} (${sizeKb} KB)`);
  console.log(`\n  Recipient install:`);
  console.log(`    tar -xzf ${tarballName}`);
  console.log(`    cd ${appName}`);
  console.log(`    claude .`);

  if (scope !== "open") {
    console.log(`\n  ⚠  Scope is '${scope}'. Distribute only to recipients authorised at this level.`);
  }
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0 || args.includes("--help") || args.includes("-h")) {
    console.log(`
Usage:
  node scripts/package.js <app-name>    Package one app
  node scripts/package.js --all         Package every built app

Produces corpus.commons/{corpus}/distros/{app}-v{version}-{scope}.tar.gz.
`);
    return;
  }
  const config = loadBuildsConfig();
  const targets = args.includes("--all") ? Object.keys(config.builds || {}) : args;

  console.log(`Packaging ${targets.length} app(s)...`);
  for (const t of targets) {
    try {
      await packageApp(t);
    } catch (e) {
      console.error(`\nFAILED: ${t}\n  ${e.message}`);
      process.exitCode = 1;
    }
  }
}

main();
