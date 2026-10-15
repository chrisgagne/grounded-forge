import json

import pytest

from factory.ledger import Change, Ledger, LedgerError


def test_append_assigns_ids_and_chains(tmp_path):
    led = Ledger(tmp_path / "ledger.json")
    a = led.append("gate", "pass", check="tests", cmd="npm test", exit=0)
    b = led.append("gate", "info", check="note")
    assert (a["id"], b["id"]) == ("e001", "e002")
    assert a["prev"] == "0" * 64 and b["prev"] != a["prev"]
    Ledger.verify(led.events())


def test_status_must_be_known(tmp_path):
    with pytest.raises(LedgerError):
        Ledger(tmp_path / "l.json").append("gate", "ok")


def test_blocked_and_skipped_need_a_reason(tmp_path):
    led = Ledger(tmp_path / "l.json")
    for status in ("blocked", "skipped"):
        with pytest.raises(LedgerError):
            led.append("gate", status)
    assert led.append("gate", "skipped", reason="not configured")["status"] == "skipped"


def test_status_must_agree_with_exit_code(tmp_path):
    led = Ledger(tmp_path / "l.json")
    with pytest.raises(LedgerError):
        led.append("gate", "pass", exit=1)
    with pytest.raises(LedgerError):
        led.append("gate", "fail", exit=0)
    led.append("gate", "fail", exit=2)


def test_editing_an_earlier_event_breaks_the_chain_and_stops_appends(tmp_path):
    led = Ledger(tmp_path / "l.json")
    led.append("gate", "fail", check="tests", exit=1)
    led.append("gate", "info", check="x")
    events = json.loads(led.path.read_text())
    events[0]["status"], events[0]["exit"] = "pass", 0
    led.path.write_text(json.dumps(events))
    with pytest.raises(LedgerError, match="edited"):
        Ledger.verify(led.events())
    with pytest.raises(LedgerError):
        led.append("gate", "info", check="y")


def test_removing_an_event_is_detected(tmp_path):
    led = Ledger(tmp_path / "l.json")
    for i in range(3):
        led.append("gate", "info", check=str(i))
    events = json.loads(led.path.read_text())
    led.path.write_text(json.dumps(events[1:]))
    with pytest.raises(LedgerError):
        Ledger.verify(led.events())


def test_ledger_offers_no_update_or_delete(tmp_path):
    led = Ledger(tmp_path / "l.json")
    assert not any(hasattr(led, name) for name in ("update", "delete", "remove", "set", "replace"))


def test_stage_readiness_follows_order_and_acceptance(change):
    code = change.code_state()
    for stage in ("spec", "tests", "build", "triage", "gate"):
        change.record(stage, "pass", check="outcome", **code)
    change.record("review", "blocked", check="outcome", reason="F1", blocking=["F1"], acceptable=True, **code)
    assert change.stage_ready("review")[0] is False
    change.record("accept", "info", check="acceptance", item="F1", reason="known, tracked", by="Chris")
    assert change.stage_ready("review")[0] is True
    change.record("build", "pass", check="outcome", **code)  # a rebuild makes everything after it stale
    assert change.stage_ready("triage")[0] is False


def anchored(tmp_path, n=3):
    led = Ledger(tmp_path / "l.json", anchor=tmp_path / "anchor" / "c.json")
    for i in range(n):
        led.append("gate", "info", check=str(i))
    return led, json.loads(led.path.read_text())


def test_an_edited_last_event_is_detected(tmp_path):
    led, events = anchored(tmp_path)
    events[-1]["status"] = "pass"
    led.path.write_text(json.dumps(events))
    with pytest.raises(LedgerError, match="last event"):
        led.events()


def test_truncation_is_detected(tmp_path):
    led, events = anchored(tmp_path)
    led.path.write_text(json.dumps(events[:1]))
    with pytest.raises(LedgerError, match="anchor records 3"):
        led.events()
    with pytest.raises(LedgerError):
        led.append("gate", "info", check="after truncation")


def test_a_rewritten_history_with_a_valid_chain_is_detected(tmp_path):
    from factory.ledger import GENESIS, canonical, sha256_bytes
    led, events = anchored(tmp_path)
    events[0]["status"] = "fail"
    prev = GENESIS
    for e in events:  # recompute the whole chain, as a careful forger would
        e["prev"] = prev
        prev = sha256_bytes(canonical(e))
    led.path.write_text(json.dumps(events))
    Ledger.verify(events)  # the chain alone is fine
    with pytest.raises(LedgerError, match="anchor"):
        led.events()


def test_a_missing_anchor_is_detected(tmp_path):
    led, _ = anchored(tmp_path)
    led.anchor.unlink()
    with pytest.raises(LedgerError, match="missing"):
        led.events()


def _append_many(args):
    path, anchor, tag = args
    led = Ledger(path, anchor=anchor)
    for i in range(15):
        led.append("gate", "info", check=f"{tag}{i}")


def test_concurrent_processes_lose_no_events(tmp_path):
    import multiprocessing as mp
    path, anchor = tmp_path / "l.json", tmp_path / "a.json"
    with mp.get_context("spawn").Pool(4) as pool:
        pool.map(_append_many, [(path, anchor, t) for t in "abcd"])
    events = Ledger(path, anchor=anchor).events()
    assert len(events) == 60 and len({e["check"] for e in events}) == 60


def test_a_change_ledger_is_anchored_outside_the_change_folder(change):
    assert change.ledger.anchor.exists() and change.dir not in change.ledger.anchor.parents
    assert ".git" in change.ledger.anchor.parts


def test_one_factory_process_per_change(change):
    with change.exclusive():
        with pytest.raises(SystemExit, match="another factory process"):
            with Change(change.repo, change.id).exclusive():
                pass
    with change.exclusive():  # released
        pass


def test_a_stage_command_runs_only_after_the_stage_it_follows_is_ready(change, monkeypatch):
    from factory import cli
    ran = []
    for name, mod in cli.STAGES.items():
        monkeypatch.setattr(mod, "run", lambda c, *a, _n=name, **k: ran.append(_n) or True)
    args = type("A", (), {})()
    code = change.code_state()
    assert cli.run_stage(change, "build", args) is False and ran == []  # no tests yet
    for stage in ("spec", "tests", "build"):
        change.record(stage, "pass", check="outcome", **code)
    assert cli.run_stage(change, "gate", args) is False  # triage hasn't run on the build
    refused = [e for e in change.ledger.events() if e.get("check") == "order"]
    assert [e["stage"] for e in refused] == ["build", "gate"] and all(e["status"] == "blocked" for e in refused)
    change.record("triage", "pass", check="outcome", **code)
    change.record("gate", "blocked", check="outcome", reason="surface", blocking=["surface"], acceptable=True, **code)
    assert cli.run_stage(change, "review", args) is False  # the gate's block isn't accepted
    change.record("accept", "info", check="acceptance", item="surface", reason="intended", by="Chris")
    assert cli.run_stage(change, "review", args) is True and ran == ["review"]
    assert cli.run_stage(change, "triage", args) is True  # after a build, triage follows the build
    assert cli.precondition(change, "spec") is None and cli.precondition(change, "warrant") is None
