#!/usr/bin/env python3
"""Source-removal tests: remove-source.py touches only the removed source's own files and rows.

These cases lock in:

- a file is the source's own when its name is or starts with the slug, or
  carries it as an underscore-bounded token, but never when it belongs to a
  longer slug in the corpus that starts with this one (``scrum-guide-2020`` vs
  ``scrum-guide-2020-annotated``);
- in a distillation index, a row or bullet pointing only at the source goes
  and is listed for re-routing, a row shared with other sources keeps their
  files and is listed for rewriting, and a table or list section left with
  nothing in it is listed too;
- the retired sidecar keeps its frontmatter and gains ``removed:`` and
  ``removed_reason:``;
- without Pass H staging, rewriting the shipped concept index through the
  assembler's writer reproduces it byte for byte when nothing is removed;
- a topic left with no rows goes, and a topic that named it as broader loses
  the link;
- sweep terms match on word boundaries: an acronym matches case and stands
  alone ("FLO" finds "(FLO)" but not "workflow"), a stem still finds its
  endings.

No test framework, matching tests/refile.test.py: each case succeeds silently
or raises; the runner collects failures, prints a summary, exits non-zero.

Usage:
    python3 tests/remove-source.test.py
"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

_spec = importlib.util.spec_from_file_location("remove_source", REPO_ROOT / "scripts" / "remove-source.py")
rs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rs)

SLUG = "scrum-guide-2020"
TASKS = ["aar", "retro"]


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def removal(root: Path) -> "rs.Removal":
    r = rs.Removal("no-such-corpus", SLUG, "superseded", True, [])
    r.root, r.dist, r.tasks = root, root / "distillations", TASKS
    r.rel = lambda p: str(p.relative_to(root))
    r.do = lambda message, fn=None: fn() if fn else None
    return r


def case_owns_whole_token_only():
    longer = [f"{SLUG}-annotated"]
    own = [f"{SLUG}.md", f"{SLUG}-deep.md", f"{SLUG}-aar.md", f"{SLUG}-retro--builder.md",
           f"{SLUG}-index-edits.json", f"_ingest_pass_I_{SLUG}_source_audit.md",
           f"_pass_I_quotations_{SLUG}_2026-10-15.md", f"_ingest_image_index_{SLUG}.yaml", f"{SLUG}.json"]
    other = [f"{SLUG}-annotated.md", f"{SLUG}-annotated-deep.md", f"{SLUG}-annotated-aar.md",
             f"_ingest_pass_I_{SLUG}-annotated_source_audit.md", "open-kanban-aar.md", "x-scrum-guide-2020.md"]
    for name in own:
        assert_(rs.owns(name, SLUG, longer), f"{name} should be the source's own")
    for name in other:
        assert_(not rs.owns(name, SLUG, longer), f"{name} is not the source's own")


def case_index_rows():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        index = root / "distillations" / "aar" / "AAR-DISTILLATION-INDEX.md"
        index.parent.mkdir(parents=True)
        index.write_text(
            "## Quick start\n\n| Situation | Reference | Distillation |\n|---|---|---|\n"
            f"| Joint | Field Manual + Scrum Guide | `field-manual-aar.md`, `{SLUG}-aar.md` |\n"
            f"| Alone | Scrum Guide | `{SLUG}-aar.md` |\n\n"
            "## Phase two\n\n| Need | Reference | Distillation | When |\n|---|---|---|---|\n"
            f"| Only this | Scrum Guide | `{SLUG}-aar.md` | always |\n\n"
            f"## Files\n\n- `{SLUG}-aar.md` — the Scrum Guide on AARs; pair with `field-manual-aar.md`.\n"
            f"- `field-manual-aar.md` — the field manual; pair with `{SLUG}-aar.md`.\n",
            encoding="utf-8")
        r = removal(root)
        r.edit_task_indexes()
        text = index.read_text(encoding="utf-8")
        assert_(f"{SLUG}-aar.md" not in text, f"source's file still named:\n{text}")
        assert_("| Joint | Field Manual + Scrum Guide | `field-manual-aar.md` |" in text, f"shared row mangled:\n{text}")
        assert_("| Alone |" not in text and "Only this" not in text, "sole rows kept")
        assert_("Scrum Guide on AARs" not in text, "a bullet about the source that mentions another stayed")
        assert_("- `field-manual-aar.md` — the field manual; pair with" in text, "other source's bullet lost")
        whys = [(x["text"], x["why"]) for x in r.rewrite]
        assert_(any("Joint" in t and "shared" in w for t, w in whys), f"shared row not listed: {whys}")
        assert_(any(t == "Phase two" and "no rows" in w for t, w in whys), f"empty table not listed: {whys}")
        assert_(not any(t == "Quick start" for t, _ in whys), f"non-empty table listed: {whys}")
        deleted = [x["text"] for x in r.deleted_rows]
        assert_(any("| Alone |" in d for d in deleted) and any("Only this" in d for d in deleted),
                f"deleted rows not listed for re-routing: {deleted}")


def case_emptied_list_section():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        index = root / "distillations" / "retro" / "RETRO-DISTILLATION-INDEX.md"
        index.parent.mkdir(parents=True)
        index.write_text(
            f"## By category\n\n### Learning from events\n\n- `{SLUG}-retro.md` — the Scrum Guide.\n\n"
            "### Facilitation\n\n- `field-manual-retro.md` — the field manual.\n", encoding="utf-8")
        r = removal(root)
        r.edit_task_indexes()
        whys = [(x["text"], x["why"]) for x in r.rewrite]
        assert_(("Learning from events", "this section has nothing left under it") in whys, f"emptied list section missed: {whys}")
        assert_(not any(t in ("Facilitation", "By category") for t, _ in whys), f"live section listed: {whys}")


def case_sweep_terms():
    flo, stem, short = rs.needle_pattern("FLO"), rs.needle_pattern("co-facilitat"), rs.needle_pattern("Annie")
    assert_(all(flo.search(x) for x in ("the FLO guide", "(FLO)", "FLO, LS")), "acronym missed a real mention")
    assert_(not any(flo.search(x) for x in ("workflow", "flow", "Flo Rida")), "acronym matched inside a word or in lower case")
    assert_(stem.search("co-facilitators debrief") and not stem.search("reco-facilitate"), "stem boundary wrong")
    assert_(short.search("anxious annie") and not short.search("Annies"), "short term boundary wrong")


def case_sidecar_stamp():
    with tempfile.TemporaryDirectory() as tmp:
        sidecar = Path(tmp) / f"{SLUG}.source.md"
        sidecar.write_text('---\ntitle: "The Scrum Guide"\nscope: open\n---\n\n# Source: The Scrum Guide\n', encoding="utf-8")
        removal(Path(tmp)).stamp(sidecar)
        text = sidecar.read_text(encoding="utf-8")
        head, _, body = text[4:].partition("\n---\n")
        assert_(head.splitlines()[-2:][0].startswith("removed: "), f"no removed date:\n{text}")
        assert_(head.splitlines()[-1] == 'removed_reason: "superseded"', f"no reason:\n{text}")
        assert_('title: "The Scrum Guide"' in head and body.strip() == "# Source: The Scrum Guide", f"frontmatter broken:\n{text}")


def case_shipped_index_round_trip():
    """Without staging, the concept index is rewritten from the shipped files by
    the assembler's own writer; unchanged input must give the same bytes."""
    import json
    root = REPO_ROOT / "corpus.commons" / "demo"
    runtime = json.loads((root / "concept-index.json").read_text(encoding="utf-8"))
    deep = json.loads((root / "concept-index-deep.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "concept-index.json"
        rs._write_schema3(out, runtime["corpus"], deep["concepts"], rs.topics_from_runtime(runtime, deep["concepts"]))
        assert_(out.read_bytes() == (root / "concept-index.json").read_bytes(), "runtime index changed on round trip")
        rs.write_deep(out, deep)
        assert_(out.read_bytes() == (root / "concept-index-deep.json").read_bytes(), "deep index changed on round trip")


def case_empty_topics_go():
    doc = {"topics": [
        {"key": "parent", "concepts": ["a"]},
        {"key": "emptied", "broader": "parent", "concepts": [], "examples": []},
        {"key": "child", "broader": "emptied", "concepts": [], "examples": ["b"]},
        {"key": "debate", "concepts": [], "positions": [{"label": "x", "concepts": ["c"]}]},
    ]}
    gone = rs.drop_empty_topics({**doc, "topics": [dict(t, name=t["key"]) for t in doc["topics"]]})
    assert_(gone == ["emptied"], f"wrong topics dropped: {gone}")
    kept = {"topics": [dict(t, name=t["key"]) for t in doc["topics"]]}
    rs.drop_empty_topics(kept)
    child = next(t for t in kept["topics"] if t["key"] == "child")
    assert_(child["broader"] == "", "child still points at a dropped topic")
    assert_([t["key"] for t in kept["topics"]] == ["parent", "child", "debate"], "a topic with members went")


def main() -> int:
    cases = [v for k, v in sorted(globals().items()) if k.startswith("case_")]
    failures = []
    for case in cases:
        try:
            case()
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{case.__name__}: {exc}")
    print(f"{len(cases) - len(failures)}/{len(cases)} remove-source cases pass")
    for f in failures:
        print(f"  FAIL {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
