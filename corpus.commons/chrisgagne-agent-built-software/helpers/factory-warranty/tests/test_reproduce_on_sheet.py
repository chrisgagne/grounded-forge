"""With review.reproduce on, each blocking finding gets the reproduction step, and its outcome reaches the decisions
the person must make and the warranty pack. It never changes what blocks."""
import json

from conftest import make_app
from test_run_e2e import fake_claude, fake_codex

from factory import cli, legs, reproduce
from factory.ledger import Change


def test_a_blocking_finding_carries_what_the_factory_ran(tmp_path, monkeypatch, capsys):
    calls = []

    def fake_reproduce(finding, base, head, work, **kw):
        calls.append(finding["id"])
        assert (base / "src").is_dir() and (head / "src" / "bye.sh").exists()  # both trees, before and after
        return {"outcome": "shown", "why": "after the change, `sh src/bye.sh 'a;b'` prints the name unquoted",
                "leg": {"cost_usd": 0.1}}

    monkeypatch.setattr(legs, "run_claude", fake_claude)
    monkeypatch.setattr(legs, "run_codex", fake_codex)
    monkeypatch.setattr(reproduce, "reproduce", fake_reproduce)
    app = make_app(tmp_path, review={"grounding": "none", "reproduce": True})
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n\n`src/bye.sh NAME` prints Bye, NAME.\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 1
    change_id = capsys.readouterr().out.split("change ", 1)[1].split()[0]
    change = Change(app, change_id)
    assert calls == ["F1"] and change.outcome("review")["blocking"] == ["F1"]  # still blocks
    items = json.loads((change.dir / "review" / "findings.json").read_text())
    assert items[0]["shown"]["outcome"] == "shown"
    assert "[shown: after the change" in (change.dir / "decisions-needed.md").read_text()
    assert cli.main(["accept", "--repo", str(app), "--change", change_id, "--item", "F1",
                     "--reason", "names come from our own CLI", "--by", "Chris"]) == 0
    assert cli.main(["run", "--repo", str(app), "--change", change_id]) == 0
    pack = (change.dir / "warranty.md").read_text()
    assert "F1: **Shown.** after the change" in pack


def test_off_by_default(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(legs, "run_claude", fake_claude)
    monkeypatch.setattr(legs, "run_codex", fake_codex)
    monkeypatch.setattr(reproduce, "reproduce", lambda *a, **k: (_ for _ in ()).throw(AssertionError("ran")))
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n\n`src/bye.sh NAME` prints Bye, NAME.\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 1
