"""A tiny shell-script target repo for the harness's own tests: no network, no models."""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from factory import isolation
from factory.ledger import Change

RULES = """rules:
  - id: no-danger
    languages: [generic]
    pattern: DANGER_CALL
    message: dangerous call
    severity: ERROR
"""


def sh(cwd: Path, *args: str) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


def make_app(root: Path, **config) -> Path:
    """A git repo with src/greet.sh, a test that checks it, and .factory/config.yaml."""
    app = root / "app"
    (app / "src").mkdir(parents=True)
    (app / "test").mkdir()
    (app / ".factory").mkdir()
    (app / "src" / "greet.sh").write_text('echo "Hello, $1"\n')
    (app / "test" / "run.sh").write_text(
        'fail=0\nfor t in test/*.test.sh; do sh "$t" || { echo "FAIL $t"; fail=1; }; done\nexit $fail\n')
    (app / "test" / "greet.test.sh").write_text('[ "$(sh src/greet.sh Ann)" = "Hello, Ann" ]\n')
    rules = root / "rules.yml"
    rules.write_text(RULES)
    cfg = {"commands": {"install": "true", "test": "sh test/run.sh"}, "test_globs": ["test/**"],
           "risk_paths": {"auth": ["src/auth/**"]}, "review": {"grounding": "none"},
           "gate": {"semgrep_config": str(rules)}, "worktree_root": str(root / "worktrees"),
           # Inside another sandbox (the factory's gate running this suite), sandbox-exec can't apply a profile and
           # every command would be refused, so a test app turns OS isolation off there; the isolation tests skip.
           "isolation": {"os_sandbox": isolation.available()[0]}}
    cfg.update(config)
    (app / ".factory" / "config.yaml").write_text(yaml.safe_dump(cfg))
    sh(app, "git", "init", "-q", "-b", "main")
    sh(app, "git", "add", "-A")
    sh(app, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "baseline")
    return app


@pytest.fixture
def app(tmp_path) -> Path:
    return make_app(tmp_path)


@pytest.fixture
def change(app, tmp_path) -> Change:
    story = tmp_path / "story.md"
    story.write_text("# Greet politely\n\nGreetings should say Hello.\n")
    return Change.create(app, story, change_id="c1")
