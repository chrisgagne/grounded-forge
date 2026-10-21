import os
from pathlib import Path

import pytest

from factory import axis
from factory.stages import parse_json
from factory.stages.review import bar, blocking, parse_strict, validate_findings, validate_sort
from factory.stages.spec import check_file, parse_acceptance

# The axis spec: $FACTORY_AXIS_SPEC, or the open corpus's spec when the factory sits at its home in grounded-forge,
# corpus.commons/chrisgagne-agent-built-software/helpers/factory-warranty/.
AXIS = Path(os.environ.get("FACTORY_AXIS_SPEC") or
            Path(__file__).resolve().parents[1] / "../../tasks/warranting-agent-built-software.md")


def test_acceptance_with_ids_and_checks_passes():
    text = ("## AC-1: A note can be created\ncheck: test/notes.test.js :: creates a note\n\n"
            "## AC-2: Missing notes give 404\n- check: `test/notes.test.js` :: returns 404\n")
    criteria, problems = parse_acceptance(text)
    assert problems == [] and [c["id"] for c in criteria] == ["AC-1", "AC-2"]
    assert check_file(criteria[1]["check"]) == "test/notes.test.js"


def test_acceptance_problems_block():
    _, problems = parse_acceptance("## AC-1: works well\n\n## AC-1: handles errors\ncheck: test/x.test.js :: y\n")
    assert any("no `check:`" in p for p in problems) and any("twice" in p for p in problems)
    assert parse_acceptance("1. it works\n2. it is fast\n")[1]


def test_findings_validation_and_axis_rows():
    raw = [{"severity": "HIGH", "file": "src/a.js", "line": "12", "claim": "c", "evidence": "e", "axis_row": "P3.1"},
           {"severity": "low", "claim": "c2", "evidence": "e2", "axis_row": "P9.9"}]
    kept = validate_findings(raw, ["P3.1"])
    assert len(kept) == 2
    assert kept[0]["severity"] == "high" and kept[0]["line"] == 12 and kept[0]["axis_row"] == "P3.1"
    assert kept[1]["axis_row_unknown"] == "P9.9"
    assert "axis_row" not in validate_findings(raw[:1], None)[0]


@pytest.mark.parametrize("raw", [
    [{"severity": "critical", "claim": "unsafe"}],                       # no evidence
    [None],
    [{"severity": "urgent", "claim": "c", "evidence": "e"}],
    [{"severity": "high", "claim": "c", "evidence": "e", "line": "forty"}],
    {"findings": []},
])
def test_an_invalid_finding_rejects_the_whole_list(raw):
    with pytest.raises(ValueError):
        validate_findings(raw, None)


def test_reviewer_output_must_be_only_json():
    assert parse_strict("[]") == [] and parse_strict('```json\n[{"a": 1}]\n```') == [{"a": 1}]
    for text in ("Review could not be completed; use [] as placeholder.", "Here you go:\n[]\nThanks", ""):
        with pytest.raises(ValueError):
            parse_strict(text)


INPUTS = {"C1": {"severity": "high", "file": "a", "line": 1, "claim": "auth missing", "evidence": "e"},
          "X1": {"severity": "medium", "file": "a", "line": 1, "claim": "route open", "evidence": "e"},
          "X2": {"severity": "low", "file": "b", "line": 2, "claim": "typo", "evidence": "e"},
          "C2": {"severity": "critical", "file": "c", "line": 3, "claim": "sql injection", "evidence": "e"}}


def test_a_complete_sort_is_numbered_and_blocks_on_confirmed_high():
    raw = [{"sources": ["C1", "X1"], "verdict": "confirmed", "reason": "routes.js:1 has no requireAuth"},
           {"sources": ["X2"], "verdict": "noise", "reason": "the word is spelled right"},
           {"sources": ["C2"], "verdict": "disputed", "reason": "the query may be parameterised upstream"}]
    items = validate_sort(raw, INPUTS)
    assert [i["id"] for i in items] == ["F1", "F2", "F3"] and items[0]["severity"] == "high"
    assert blocking(items) == ["F1", "F3"]  # F3: a reviewer said critical, and only a human may overrule that


def test_the_sort_cannot_lift_a_reviewers_high_on_its_own():
    raw = [{"sources": ["C1"], "verdict": "confirmed", "severity": "medium", "reason": "only internal callers"},
           {"sources": ["C2"], "verdict": "noise", "reason": "the value is a constant"},
           {"sources": ["X1"], "verdict": "disputed", "reason": "unclear"},
           {"sources": ["X2"], "verdict": "noise", "reason": "spelled right"}]
    items = validate_sort(raw, INPUTS)
    assert [i["raw_severity"] for i in items] == ["high", "critical", "medium", "low"]
    assert blocking(items) == ["F1", "F2"]  # a medium or low the sort sets aside stays set aside


@pytest.mark.parametrize("raw", [
    {},                                                                                   # not a list
    [],                                                                                   # accounts for nothing
    [{"sources": ["C1", "X1", "X2"], "verdict": "noise", "reason": "r"}],                 # C2 missing
    [{"sources": ["C1", "X1", "X2", "C2"], "verdict": "noise"}],                          # no reason
    [{"sources": ["C1", "X1", "X2", "C2"], "verdict": "fine", "reason": "r"}],            # bad verdict
    [{"sources": ["C1", "X1", "X2", "C2"], "verdict": "noise", "reason": "r"},
     {"sources": ["C2"], "verdict": "confirmed", "reason": "r"}],                         # C2 twice
    [{"sources": ["C1", "X1", "X2", "C2", "ZZ"], "verdict": "noise", "reason": "r"}],     # unknown id
])
def test_an_incomplete_or_invalid_sort_is_rejected(raw):
    with pytest.raises(ValueError):
        validate_sort(raw, INPUTS)


def test_parse_json_from_model_output():
    assert parse_json('```json\n[{"a": 1}]\n```') == [{"a": 1}]
    assert parse_json('Here you go:\n[]\nThanks') == []
    with pytest.raises(ValueError):
        parse_json("no json here")


def test_axis_extract_synthetic():
    spec = ("### Seed trigger→response table\n\n**Phase 2: Triaging risk**\n\n| Trigger | Response |\n|---|---|\n"
            "| The diff touches login | Require ASVS |\n| A migration is planned | Rehearse rollback |\n\n"
            "**Phase 6: Reviewing independently**\n\n| Trigger | Response |\n|---|---|\n| Same session reviews | Fresh reviewer |\n\n## 3. Next\n")
    rows = axis.extract(spec)
    assert [r.id for r in rows] == ["P2.1", "P2.2", "P6.1"]
    assert [r.id for r in axis.rows_for_review(rows, ["auth"])] == ["P2.1", "P6.1"]


@pytest.mark.skipif(not AXIS.exists(), reason=f"no axis spec at {AXIS}: set FACTORY_AXIS_SPEC to "
                    "warranting-agent-built-software.md, or run from the factory's home in grounded-forge")
def test_axis_extract_real_spec():
    rows = axis.load(AXIS)
    assert len(rows) >= 40 and {r.phase for r in rows} == set(range(1, 9))


INDEX = """# Index

## Phase-by-Phase Framework Guide

### Phase 5: Gating deterministically

| Purpose | Framework | Distillation File |
|---|---|---|
| A gate | Gates | `x-task.md` |

#### Runtime listeners: Phase 5

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| Lint is suppressed | Treat it as a finding (`weinberg-stable`) |
| A gate was skipped \\| once | Log it (`dekker-drift`, `vaughan-deviance`); see the AAR axis (`aar`) |

### Phase 7: Warranting the change

#### Runtime listeners: Phase 7

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| The pack is signed unread | Read it (`dekker-drift`) |

## Framework Categories

| Trigger | Response |
|---|---|
| not a listener | ignored |
"""


def test_listener_rows_from_the_distillation_index():
    rows = axis.extract_listeners(INDEX)
    assert [r.id for r in rows] == ["L5.1", "L5.2", "L7.1"]
    assert rows[1].trigger == "A gate was skipped \\| once"
    assert rows[1].sources == ("dekker-drift", "vaughan-deviance", "aar")
    assert [r.id for r in axis.rows_for_review(rows, [])] == ["L5.1", "L5.2"]
    assert axis.distillation_path("/c/warranting/INDEX.md", "dekker-drift") == Path("/c/warranting/dekker-drift-warranting.md")


def test_distillations_grounding_needs_an_index():
    from factory.ledger import DEFAULTS, config_problems, merge
    cfg = merge(DEFAULTS, {"commands": {"test": "t"}, "test_globs": ["t/**"], "review": {"grounding": "distillations"}})
    assert any("axis_index" in p for p in config_problems(cfg))
    assert not config_problems(merge(cfg, {"axis_index": "/x/INDEX.md"}))


def test_unwrap_takes_only_the_schema_key():
    from factory.stages.review import unwrap
    assert unwrap({"findings": [1]}, "findings") == [1]
    assert unwrap([1], "findings") == [1]
    with pytest.raises(ValueError):  # extra keys stay an object, which the validator rejects
        validate_findings(unwrap({"findings": [], "note": "x"}, "findings"), None)


def test_run_claude_passes_the_output_schema(tmp_path, monkeypatch):
    import json
    from factory import legs
    from factory.stages.review import FINDINGS_SCHEMA
    seen = {}

    def spawn(cmd, cwd, log, timeout_s, env, **kw):
        seen["cmd"] = cmd
        log.write_text(json.dumps({"type": "result", "result": "{}", "is_error": False}) + "\n")
        return {"exit": 0, "started": "s", "finished": "f", "duration_s": 0}

    monkeypatch.setattr(legs, "_spawn", spawn)
    legs.run_claude("p", tmp_path, tmp_path / "log.jsonl", model="opus", timeout_s=5, read_only=True,
                    json_schema=FINDINGS_SCHEMA)
    i = seen["cmd"].index("--json-schema")
    assert json.loads(seen["cmd"][i + 1]) == FINDINGS_SCHEMA
    legs.run_claude("p", tmp_path, tmp_path / "log.jsonl", model="opus", timeout_s=5, read_only=True)
    assert "--json-schema" not in seen["cmd"]


def test_a_confirmed_medium_blocks_where_the_change_reaches_personal_data_or_a_one_way_step():
    raw = [{"sources": ["X1"], "verdict": "confirmed", "reason": "routes.js:1 is open"},
           {"sources": ["C1"], "verdict": "confirmed", "severity": "low", "reason": "only internal callers"},
           {"sources": ["X2"], "verdict": "confirmed", "reason": "a typo"},
           {"sources": ["C2"], "verdict": "confirmed", "reason": "reachable"}]
    items = validate_sort(raw, INPUTS)
    assert bar(["migration", "auth"]) == ("critical", "high")
    assert blocking(items, bar(["auth"])) == ["F2", "F4"]  # F2: the sort can't lift a reviewer's high
    for cls in ("personal-data", "irreversible"):
        assert bar(["auth", cls]) == ("critical", "high", "medium")
        assert blocking(items, bar([cls])) == ["F1", "F2", "F4"]  # the medium blocks; the low stays a residual risk


def test_the_codex_reviewer_is_held_to_a_strict_schema(tmp_path, monkeypatch):
    import json
    from factory import legs
    from factory.stages.review import CODEX_FINDINGS_SCHEMA
    seen = {}

    def spawn(cmd, cwd, log, timeout_s, env, **kw):
        seen["cmd"] = cmd
        log.write_text("tokens used\n10\n")
        (tmp_path / "out.md").write_text('{"findings": []}')
        return {"exit": 0, "started": "s", "finished": "f", "duration_s": 0}

    def strict(node):  # OpenAI strict mode: every object closed, every property required
        if node.get("type") == "object":
            assert node["additionalProperties"] is False and set(node["required"]) == set(node["properties"])
        for child in [*(node.get("properties") or {}).values(), *([node["items"]] if "items" in node else [])]:
            strict(child)

    strict(CODEX_FINDINGS_SCHEMA)
    monkeypatch.setattr(legs, "_spawn", spawn)
    monkeypatch.setattr(legs, "codex_bin", lambda: "codex")
    schema = tmp_path / "schema.json"
    schema.write_text(json.dumps(CODEX_FINDINGS_SCHEMA))
    legs.run_codex("p", tmp_path, tmp_path / "log.txt", tmp_path / "out.md", model=None, timeout_s=5, output_schema=schema)
    assert seen["cmd"][seen["cmd"].index("--output-schema") + 1] == str(schema)
    # what the schema allows, the validator takes: nullable file, line and axis_row
    found = validate_findings([{"severity": "high", "file": None, "line": None, "claim": "c", "evidence": "e",
                                "axis_row": None}], ["P1.1"])
    assert found == [{"severity": "high", "file": None, "line": None, "claim": "c", "evidence": "e"}]


def test_a_sort_item_with_a_mistyped_field_is_rejected():
    for field, value in (("file", 7), ("line", "ten"), ("line", -1), ("claim", ["x"]), ("claim", " ")):
        raw = [{"sources": ["C1", "X1", "X2", "C2"], "verdict": "confirmed", "reason": "r", field: value}]
        with pytest.raises(ValueError, match=field):
            validate_sort(raw, INPUTS)


def test_the_sort_may_name_the_criterion_a_finding_breaks():
    raw = [{"sources": ["C1", "X1"], "verdict": "confirmed", "reason": "r", "breaks": "AC-6"},
           {"sources": ["X2"], "verdict": "noise", "reason": "r", "breaks": "anything else"},
           {"sources": ["C2"], "verdict": "disputed", "reason": "r", "breaks": "story"}]
    items = validate_sort(raw, INPUTS)
    assert [it.get("breaks") for it in items] == ["AC-6", None, "story"]
