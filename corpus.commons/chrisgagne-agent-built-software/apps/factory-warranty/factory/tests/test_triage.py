import json

from factory.stages import triage
from factory.stages.triage import assess


def test_keywords_in_the_story_map_to_classes():
    r = assess("# Add login\n\nUsers sign in with a password; store their email address.", "", {})
    assert {"auth", "personal-data"} <= set(r["classes"])
    assert r["phase"] == "plan" and r["unplanned"] == []
    assert "V6 Authentication" in r["classes"]["auth"]["review_focus"]


def test_path_rules_builtin_and_configured():
    diff = "+++ b/migrations/0005_add_tags.up.sql\n+CREATE TABLE tags (id int);\n"
    r = assess("Add tags to notes", "", {"personal-data": ["src/users/**"]},
               changed=["migrations/0005_add_tags.up.sql", "src/users/repo.js"], diff=diff)
    assert {"migration", "personal-data"} <= set(r["classes"])
    assert r["classes"]["migration"]["required_gates"] == ["gate:rollback"]
    assert set(r["unplanned"]) == {"migration", "personal-data"}


def test_planned_classes_are_not_unplanned():
    r = assess("Add a migration that adds a tags table", "", {},
               changed=["migrations/0005_add_tags.up.sql"], diff="")
    assert "migration" in r["classes"] and r["unplanned"] == []


def test_diff_patterns_outside_tests():
    diff = ("+++ b/src/notes/repo.js\n+  db.exec('DELETE FROM notes');\n"
            "+++ b/package.json\n+    \"left-pad\": \"^1.3.0\",\n"
            "+++ b/test/notes.test.js\n+  db.exec('DROP TABLE notes');\n")
    r = assess("Speed up note listing", "", {}, changed=["src/notes/repo.js", "package.json", "test/notes.test.js"],
               diff=diff, test_globs=["test/**"])
    assert {"irreversible", "dependency"} <= set(r["unplanned"])
    assert all(e["source"] != "test/notes.test.js" for e in r["classes"]["irreversible"]["evidence"])


def test_a_drop_in_a_down_migration_is_the_rollback_not_an_irreversible_step():
    diff = ("+++ b/migrations/0005_add_phone.up.sql\n+ALTER TABLE users ADD COLUMN phone TEXT;\n"
            "+++ b/migrations/0005_add_phone.down.sql\n+ALTER TABLE users DROP COLUMN phone;\n")
    r = assess("Add a phone number with a migration", "", {}, diff=diff,
               changed=["migrations/0005_add_phone.up.sql", "migrations/0005_add_phone.down.sql"])
    assert "irreversible" not in r["classes"] and r["unplanned"] == []
    assert r["classes"]["migration"]["required_gates"] == ["gate:rollback"]
    up = "+++ b/migrations/0005_x.up.sql\n+ALTER TABLE users DROP COLUMN date_of_birth;\n"
    r = assess("Add a migration", "", {}, changed=["migrations/0005_x.up.sql"], diff=up)
    assert r["unplanned"] == ["irreversible"]


def test_llm_client_imports_beyond_openai_and_anthropic():
    for line in ("import { generateText } from 'ai';", "const { ChatOllama } = require('@langchain/ollama');",
                 "from litellm import completion", "import google.genai as genai",
                 "import { Mistral } from '@mistralai/mistralai';"):
        r = assess("Tidy the summary", "", {}, changed=["src/x.js"], diff=f"+++ b/src/x.js\n+{line}\n")
        assert "llm-agent" in r["classes"], line
    r = assess("Tidy", "", {}, changed=["src/x.js"], diff="+++ b/src/x.js\n+import aiHelpers from './ai-helpers';\n")
    assert "llm-agent" not in r["classes"]


def test_story_keywords_alone_never_block():
    r = assess("Rotate the session secret and fix the login page", "", {}, changed=["src/views/home.html"], diff="")
    assert "auth" in r["classes"] and r["unplanned"] == []


def test_triage_stage_blocks_on_unplanned_class_until_accepted(change):
    wt = change.worktree
    (wt / "src" / "auth").mkdir()
    (wt / "src" / "auth" / "check.sh").write_text("true\n")
    change.commit_all("touch auth")
    change.record("build", "pass", check="outcome")
    assert triage.run(change) is False
    risk = json.loads((change.dir / "risk.json").read_text())
    assert risk["unplanned"] == ["auth"]
    assert "class:auth" in change.outcome("triage")["blocking"]
    assert (change.dir / "decisions-needed.md").exists()
    from factory.stages.warrant import accept
    ok, _ = accept(change, "class:auth", "auth tweak agreed with the client", "Chris")
    assert ok and change.stage_ready("triage")[0]


def test_the_spec_legs_notes_are_not_the_plan():
    acceptance = ("## AC-1: The rule names the forms it doesn't follow\ncheck: tests/test_rule.py :: names_them\n\n"
                  "## Summary\n\n- AC-1 is close to documentation. Drop it if you count it as documentation.\n")
    assert "irreversible" not in assess("Flag eval on built strings", acceptance, {})["classes"]
    acceptance = "## AC-1: Drop the notes table\ncheck: tests/test_notes.py :: dropped\n"
    assert "irreversible" in assess("Tidy up", acceptance, {})["classes"]


def test_a_word_in_the_story_adds_focus_but_not_gates():
    r = assess("No migrations needed; see test/migrations.test.js", "", {}, changed=["src/notes/routes.js"], diff="")
    assert r["classes"]["migration"]["strength"] == "keyword only"
    assert r["classes"]["migration"]["required_gates"] == []
    r = assess("Add tags", "", {}, changed=["migrations/0005_tags.up.sql"], diff="")
    assert r["classes"]["migration"]["required_gates"] == ["gate:rollback"]


def test_secret_matches_are_redacted_in_evidence():
    key = "sk-ant-api03-" + "A" * 40
    r = assess("Add staging config", "", {}, changed=["config/staging.json"],
               diff=f'+++ b/config/staging.json\n+  "apiKey": "{key}"\n')
    assert key not in json.dumps(r)
    assert "[redacted]" in r["classes"]["secrets"]["evidence"][-1]["match"]
