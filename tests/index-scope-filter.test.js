#!/usr/bin/env node
/**
 * A source the scope gate holds back must not reach an app through the axis's
 * index: its rows go, other rows lose its cited parts, and a disagreement keeps
 * it as a plain citation, not a pointer to the held-back file.
 *
 * Usage: node tests/index-scope-filter.test.js (from the repo root)
 */
const { filterIndexForShipped } = require("../build.js");

function assert(cond, msg) {
  if (!cond) throw new Error(`assertion failed: ${msg}`);
}

const task = "some-task";
const heldBack = new Map([["held-src", "*Held Report* (2025), https://example.org/held.pdf"]]);
const known = new Set(["held-src", "kept-a", "kept-b"]);
const index = [
  "# Index",
  "- **Evidence:** `kept-a`, `held-src`, `kept-b`",
  "## Named disagreements",
  "| D1 | Who is right? | `held-src` vs `kept-a` | They differ. |",
  "## Phase 1",
  "| Purpose | Framework | Distillation File |",
  "|---|---|---|",
  "| Only held | Its idea | `held-src-some-task.md` |",
  "| Shared | Both ideas | `kept-a-some-task.md`, `held-src-some-task.md` |",
  "| Kept only | An idea | `kept-b-some-task.md` |",
  "#### Runtime listeners: Phase 1",
  "| Trigger | Response |",
  "|---|---|",
  "| Mixed | Do X (`kept-a`) • Do Y (`held-src`) |",
  "| Held only | Do Y (`held-src`) |",
  "| Two in one | Do Z (`kept-b`, `held-src`) |",
  "## Files",
  "- `held-src-some-task.md`: what it says",
  "- `kept-a-some-task.md`: what it says",
].join("\n");

const { text, dropped } = filterIndexForShipped(index, heldBack, known, task);
const lines = text.split("\n");
assert(!/`held-src/.test(text), "no pointer to the held-back source survives");
assert(lines.includes("- **Evidence:** `kept-a`, `kept-b`"), "a list loses only the held-back name");
assert(lines.includes("| D1 | Who is right? | *Held Report* (2025), https://example.org/held.pdf vs `kept-a` | They differ. |"),
  "a disagreement keeps the held-back source as a plain citation");
assert(!lines.some((l) => l.startsWith("| Only held")), "a row citing only the held-back source goes");
assert(lines.includes("| Shared | Both ideas | `kept-a-some-task.md` |"), "a shared row keeps its other file");
assert(lines.includes("| Kept only | An idea | `kept-b-some-task.md` |"), "an unrelated row is untouched");
assert(lines.includes("| Mixed | Do X (`kept-a`) |"), "a listener row loses only the held-back part");
assert(!lines.some((l) => l.startsWith("| Held only")), "a listener row with nothing left goes");
assert(lines.includes("| Two in one | Do Z (`kept-b`) |"), "a part citing two sources keeps the shipped one");
assert(!lines.some((l) => l.startsWith("- `held-src")), "a list line about the held-back file goes");
assert(lines.includes("- `kept-a-some-task.md`: what it says"), "other list lines stay");
assert(dropped === 3, `three lines dropped (got ${dropped})`);

const untouched = filterIndexForShipped(index, new Map(), known, task);
assert(untouched.text === index && untouched.dropped === 0, "nothing held back changes nothing");
console.log("index-scope-filter: all assertions passed");
