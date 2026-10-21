"""The rules file the decision page lists says what the code does."""
import yaml

from factory.stages import review, warrant


def rules():
    return {r["id"]: r for r in yaml.safe_load(warrant.POLICY.read_text())["rules"]}


def test_every_rule_says_who_set_it_and_whether_it_is_confirmed():
    for r in rules().values():
        assert r["rule"] and r["source"] and r["set_by"] and r["status"] in ("PROPOSED", "confirmed")
        if r["status"] == "confirmed":
            assert r.get("confirmed_by") and r.get("confirmed_on")


def test_the_rules_match_the_code():
    r = rules()
    assert tuple(r["blocking-bar"]["values"]["blocking"]) == review.BLOCKING
    assert tuple(r["medium-blocks-on-personal-data-or-one-way-steps"]["values"]["lower_bar_classes"]) == review.LOWER_BAR
    assert set(r["second-person"]["values"]["classes"]) == set(warrant.SECOND_PERSON)
