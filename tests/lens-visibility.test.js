#!/usr/bin/env node
/**
 * Lens-visibility regression tests.
 *
 * Exercises the three behaviours introduced for v0.2.1:
 *   1. Spec-location gate: corpus.commons/ refuses any lens above 'open-nc'.
 *   2. App-shipping filter: lenses above the profile's max_visibility do not
 *      appear in the compiled app's lenses/ directory.
 *   3. LENS-INDEX regeneration: each app's LENS-INDEX.md table lists only
 *      the lenses that actually shipped, with a Visibility column.
 *
 * The tests do not depend on a test framework. Each case is a small function
 * that either succeeds silently or throws. The runner at the bottom collects
 * failures, prints a summary, and exits non-zero on any failure.
 *
 * Usage:
 *   node tests/lens-visibility.test.js
 *
 * Run from the repo root.
 */

const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");

const REPO_ROOT = path.resolve(__dirname, "..");
const BUILD_JS = path.join(REPO_ROOT, "build.js");

function assert(cond, msg) {
  if (!cond) throw new Error(`assertion failed: ${msg}`);
}

function runBuild(args, opts = {}) {
  try {
    const out = execFileSync("node", [BUILD_JS, ...args], {
      cwd: REPO_ROOT,
      encoding: "utf8",
      stdio: ["ignore", "pipe", "pipe"],
      ...opts,
    });
    return { code: 0, stdout: out, stderr: "" };
  } catch (e) {
    return {
      code: e.status ?? 1,
      stdout: e.stdout ? e.stdout.toString() : "",
      stderr: e.stderr ? e.stderr.toString() : e.message,
    };
  }
}

function readFrontmatterVisibility(lensPath) {
  const body = fs.readFileSync(lensPath, "utf8");
  if (!body.startsWith("---")) return null;
  const end = body.indexOf("\n---", 3);
  if (end === -1) return null;
  const fm = body.slice(3, end);
  const m = fm.match(/^visibility:\s*(\S+)\s*$/m);
  return m ? m[1] : null;
}

// Case 1: the spec-location gate fails the build when a confidential lens
// is placed under corpus.commons/. We create a temporary lens file in the
// demo corpus, run the build, expect a non-zero exit and the right message,
// then clean up. The cleanup runs in a finally block so a thrown assertion
// still removes the test file.
function testCommonsConfidentialFails() {
  const lensesDir = path.join(REPO_ROOT, "corpus.commons/demo/lenses");
  const tempLens = path.join(lensesDir, "_test-confidential-lens.md");
  const body =
    "---\n" +
    "name: Test Confidential Lens\n" +
    "kind: archetype\n" +
    "slug: _test-confidential-lens\n" +
    "visibility: confidential\n" +
    "---\n\n" +
    "# Test Confidential Lens\n\n" +
    "Synthetic fixture for the spec-location gate. Removed by the test runner.\n";
  fs.writeFileSync(tempLens, body);
  try {
    // Use a real profile name so main() reaches the gate; --list returns
    // before the gate (listing shouldn't fail on lens state), and --clean
    // is destructive. The gate throws before any per-profile work runs.
    const result = runBuild(["decision"]);
    assert(
      result.code !== 0,
      `expected non-zero exit when a confidential lens lives under corpus.commons/; got code ${result.code}`
    );
    const combined = result.stdout + result.stderr;
    assert(
      /visibility=confidential/.test(combined),
      `expected error message to name visibility=confidential; got: ${combined.slice(0, 400)}`
    );
    assert(
      /cannot live under corpus\.commons\//.test(combined),
      `expected error message to name the corpus.commons constraint; got: ${combined.slice(0, 400)}`
    );
  } finally {
    if (fs.existsSync(tempLens)) fs.unlinkSync(tempLens);
  }
}

// Case 2: a personal lens does not appear in any app whose profile has
// max_visibility: confidential. Walks every corpus.local/*/ corpus root,
// identifies personal-visibility lenses by frontmatter, and asserts none
// of them appear in any built app under that corpus root. Substrate-agnostic:
// no corpus name is hardcoded.
function testPersonalAbsentFromConfidentialApps() {
  const localTier = path.join(REPO_ROOT, "corpus.local");
  if (!fs.existsSync(localTier)) {
    console.log("  skip: corpus.local/ not present");
    return;
  }
  const corpusRoots = fs
    .readdirSync(localTier, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => path.join(localTier, e.name));
  if (corpusRoots.length === 0) {
    console.log("  skip: no corpora under corpus.local/");
    return;
  }

  let totalChecked = 0;
  let totalPersonal = 0;
  for (const corpusRoot of corpusRoots) {
    const lensesDir = path.join(corpusRoot, "lenses");
    if (!fs.existsSync(lensesDir)) continue;
    const personalLenses = fs
      .readdirSync(lensesDir)
      .filter(
        (f) => f.endsWith(".md") && f !== "LENS-INDEX.md" && f !== "README.md"
      )
      .filter((f) => readFrontmatterVisibility(path.join(lensesDir, f)) === "personal");
    if (personalLenses.length === 0) continue;
    totalPersonal += personalLenses.length;

    const appRoot = path.join(corpusRoot, "apps");
    if (!fs.existsSync(appRoot)) continue;
    const apps = fs
      .readdirSync(appRoot, { withFileTypes: true })
      .filter((e) => e.isDirectory())
      .map((e) => e.name);
    for (const app of apps) {
      const appLensDir = path.join(appRoot, app, "lenses");
      if (!fs.existsSync(appLensDir)) continue;
      for (const lens of personalLenses) {
        const shipped = path.join(appLensDir, lens);
        assert(
          !fs.existsSync(shipped),
          `personal-visibility lens leaked into ${app}: ${shipped}`
        );
      }
      totalChecked++;
    }
  }
  if (totalPersonal === 0) {
    console.log("  skip: no personal-visibility lenses found under corpus.local/");
    return;
  }
  console.log(`  checked ${totalChecked} corpus.local app(s) for ${totalPersonal} personal lens(es)`);
}

// Case 3: the open-nc Chris lens appears in every corpus.commons app.
// Skip when an app dir is missing (the operator hasn't built it yet); when
// every dir is missing, skip the case entirely so the runner doesn't fail
// against a clean checkout.
function testChrisLensInCommonsApps() {
  const expectedApps = ["decision", "stakeholder", "software-business", "aar-mode", "retro-mode"];
  const appRoot = path.join(REPO_ROOT, "corpus.commons/demo/apps");
  if (!fs.existsSync(appRoot)) {
    console.log("  skip: corpus.commons/demo/apps not built");
    return;
  }
  const builtApps = expectedApps.filter((a) =>
    fs.existsSync(path.join(appRoot, a))
  );
  if (builtApps.length === 0) {
    console.log("  skip: no corpus.commons apps built");
    return;
  }
  for (const app of builtApps) {
    const lensPath = path.join(appRoot, app, "lenses", "chris-gagne-consultant-coach.md");
    assert(
      fs.existsSync(lensPath),
      `chris-gagne-consultant-coach.md (open-nc) missing from app: ${app}`
    );
  }
  console.log(`  verified Chris lens present in ${builtApps.length} corpus.commons app(s)`);
}

// Case 4: each app's LENS-INDEX.md table contains a row for every shipped
// lens and no rows for unshipped ones. Reads the lenses/ directory and the
// LENS-INDEX.md table; checks the symmetric difference is empty. Also
// asserts the regenerated index carries a 'Visibility' column header.
function testLensIndexMatchesShipped() {
  const roots = [path.join(REPO_ROOT, "corpus.commons/demo/apps")];
  const localTier = path.join(REPO_ROOT, "corpus.local");
  if (fs.existsSync(localTier)) {
    for (const e of fs.readdirSync(localTier, { withFileTypes: true })) {
      if (!e.isDirectory()) continue;
      const apps = path.join(localTier, e.name, "apps");
      if (fs.existsSync(apps)) roots.push(apps);
    }
  }
  let appsChecked = 0;
  for (const appRoot of roots) {
    if (!fs.existsSync(appRoot)) continue;
    const apps = fs
      .readdirSync(appRoot, { withFileTypes: true })
      .filter((e) => e.isDirectory())
      .map((e) => e.name);
    for (const app of apps) {
      const appLensDir = path.join(appRoot, app, "lenses");
      const indexPath = path.join(appLensDir, "LENS-INDEX.md");
      if (!fs.existsSync(indexPath)) continue;
      const shippedLenses = new Set(
        fs
          .readdirSync(appLensDir)
          .filter(
            (f) =>
              f.endsWith(".md") && f !== "LENS-INDEX.md" && f !== "README.md"
          )
          .map((f) => f.replace(/\.md$/, ""))
      );
      const indexContent = fs.readFileSync(indexPath, "utf8");
      assert(
        /\|\s*Visibility\s*\|/.test(indexContent),
        `${app}/lenses/LENS-INDEX.md lacks the Visibility column`
      );
      // Pull every slug from a table row of the shape '[slug](slug.md)'.
      const indexed = new Set();
      const slugPattern = /\[([a-z0-9-]+)\]\([a-z0-9-]+\.md\)/g;
      let m;
      while ((m = slugPattern.exec(indexContent)) !== null) {
        indexed.add(m[1]);
      }
      for (const slug of shippedLenses) {
        assert(
          indexed.has(slug),
          `${app}/lenses/LENS-INDEX.md missing row for shipped lens: ${slug}`
        );
      }
      for (const slug of indexed) {
        assert(
          shippedLenses.has(slug),
          `${app}/lenses/LENS-INDEX.md carries row for unshipped lens: ${slug}`
        );
      }
      appsChecked++;
    }
  }
  if (appsChecked === 0) {
    console.log("  skip: no built apps to check");
    return;
  }
  console.log(`  verified LENS-INDEX matches shipped lenses across ${appsChecked} app(s)`);
}

const cases = [
  ["spec-location gate refuses confidential lens under corpus.commons/", testCommonsConfidentialFails],
  ["personal lens absent from corpus.local apps (max_visibility=confidential)", testPersonalAbsentFromConfidentialApps],
  ["open-nc Chris lens ships in every corpus.commons app", testChrisLensInCommonsApps],
  ["regenerated LENS-INDEX in each app matches shipped lens set", testLensIndexMatchesShipped],
];

let failures = 0;
for (const [name, fn] of cases) {
  console.log(`\n[case] ${name}`);
  try {
    fn();
    console.log("  pass");
  } catch (e) {
    failures++;
    console.log(`  FAIL: ${e.message}`);
  }
}

console.log("");
if (failures > 0) {
  console.log(`${failures} case(s) failed.`);
  process.exit(1);
} else {
  console.log(`All ${cases.length} cases passed.`);
}
