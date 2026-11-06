"""The merge check: a target repo's CI passes only a tree that a valid signed pack names."""
import json

from conftest import sh
from test_warrant import passing_run

from factory import cli
from factory.stages import release, warrant

NOTES = "refs/notes/factory"


def signed(change):
    passing_run(change)
    assert warrant.run(change) is True
    ok, msg = warrant.sign(change, "Chris")
    assert ok, msg
    return [e for e in change.ledger.events() if e["stage"] == "sign"][-1]


def released(change):
    sig = signed(change)
    assert release.run(change) is True
    return sig


def ci_clone(change, tmp_path):
    """What a CI runner sees: a fresh clone of the repo with the factory's notes fetched, and no ledger."""
    clone = tmp_path / "ci"
    sh(tmp_path, "git", "clone", "-q", str(change.repo), str(clone))
    sh(clone, "git", "fetch", "-q", "origin", f"{NOTES}:{NOTES}")
    assert not (clone / ".factory" / "changes").exists()
    return clone


def note(clone, commit) -> dict:
    return json.loads(sh(clone, "git", "notes", "--ref", NOTES, "show", commit))


def rewrite_note(clone, commit, record):
    sh(clone, "git", "notes", "--ref", NOTES, "add", "-f", "-m", json.dumps(record), commit)


def test_release_attaches_a_sealed_attestation_to_the_signed_commit(change):
    sig = released(change)
    record = json.loads(change.git("notes", "--ref", NOTES, "show", sig["commit"]))
    for k in ("change", "by", "at", "pack_sha256", "commit", "tree", "warrant_event", "seal"):
        assert record[k] == sig[k]
    assert record["pack"] == (change.dir / "warranty.md").read_text()
    att = [e for e in change.ledger.events() if e.get("check") == "attestation"][-1]
    assert att["status"] == "pass" and att["tree"] == sig["tree"] and att["notes_ref"] == NOTES


def test_release_without_a_signature_attaches_nothing(change):
    passing_run(change)
    warrant.run(change)
    assert release.run(change) is False
    assert change.git("notes", "--ref", NOTES, "list", check=False) == ""


def test_ci_passes_the_signed_tree_and_refuses_any_other(change, tmp_path):
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    assert release.verify_merge(clone, sig["tree"]) is None
    other = sh(clone, "git", "rev-parse", "HEAD^{tree}").strip()  # main, without the change
    assert other != sig["tree"]
    assert "no valid signed pack" in release.verify_merge(clone, other)


def test_a_merge_commit_with_the_signed_tree_passes(change, tmp_path):
    """Merge strategy doesn't matter: a no-ff merge of an up-to-date branch has the signed tree."""
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    sh(clone, "git", "-c", "user.name=t", "-c", "user.email=t@t", "merge", "-q", "--no-ff", "-m", "merge",
       sig["commit"])
    tree = sh(clone, "git", "rev-parse", "HEAD^{tree}").strip()
    assert tree == sig["tree"]
    assert release.verify_merge(clone, tree) is None


def test_code_that_differs_from_the_signed_pack_fails(change, tmp_path):
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    sh(clone, "git", "-c", "user.name=t", "-c", "user.email=t@t", "merge", "-q", "--no-ff", "-m", "merge",
       sig["commit"])
    (clone / "src" / "greet.sh").write_text("rm -rf ~\n")  # one more edit before the merge lands
    sh(clone, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-am", "sneak")
    tree = sh(clone, "git", "rev-parse", "HEAD^{tree}").strip()
    assert "no valid signed pack" in release.verify_merge(clone, tree)


def test_an_edited_attestation_fails(change, tmp_path):
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    record = note(clone, sig["commit"])
    for field, value in (("by", "Someone Else"), ("pack", record["pack"] + "\nall clear\n")):
        rewrite_note(clone, sig["commit"], {**record, field: value})
        problem = release.verify_merge(clone, sig["tree"])
        assert problem and ("seal" in problem or "pack" in problem), problem


def test_an_attestation_whose_commit_does_not_have_its_tree_fails(change, tmp_path):
    """A record that names the signed tree but sits on, or names, a commit with other code doesn't count."""
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    record = note(clone, sig["commit"])
    main = sh(clone, "git", "rev-parse", "main").strip()
    fields = {**record, "commit": main}
    fields["seal"] = warrant.seal(fields)  # even with a recomputed seal
    rewrite_note(clone, main, fields)
    sh(clone, "git", "notes", "--ref", NOTES, "remove", sig["commit"])
    problem = release.verify_merge(clone, sig["tree"])
    assert problem and "tree" in problem


def test_no_notes_fails_closed(change, tmp_path):
    sig = signed(change)  # signed, never released: no attestation was written
    clone = tmp_path / "ci"
    sh(tmp_path, "git", "clone", "-q", str(change.repo), str(clone))
    assert "no valid signed pack" in release.verify_merge(clone, sig["tree"])


def test_the_local_ledger_counts_where_the_operator_runs_the_check(change):
    """On the operator's machine the ledger is there: a valid signature passes even before release."""
    sig = signed(change)
    assert release.verify_merge(change.repo, sig["tree"]) is None
    assert "no valid signed pack" in release.verify_merge(change.repo, change.git("rev-parse", "main^{tree}"))


def test_the_cli_exits_0_only_for_the_signed_tree(change, tmp_path, capsys):
    sig = released(change)
    clone = ci_clone(change, tmp_path)
    assert cli.main(["verify-merge", "--repo", str(clone), "--tree", sig["tree"]]) == 0
    assert sig["change"] in capsys.readouterr().out
    other = sh(clone, "git", "rev-parse", "HEAD^{tree}").strip()
    assert cli.main(["verify-merge", "--repo", str(clone), "--tree", other]) == 1
    assert cli.main(["verify-merge", "--repo", str(clone), "--tree", "not-a-sha"]) == 1
