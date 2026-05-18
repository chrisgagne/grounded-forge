#!/usr/bin/env python3
"""Scaffold a new corpus directory.

Use: python3 scripts/create-corpus.py {target-path} [--tier commons|local] [--tasks t1,t2,...] [--non-interactive]
Or:  npm run create-corpus -- {target-path}

Creates a self-contained corpus tree at the target path:

  {target}/
    sources/
      ingest/.gitkeep         # operator drops material here
      original/.gitkeep       # one .source.md sidecar per source (skill-authored)
      converted/.gitkeep      # one converted markdown per source
    references/
      REFERENCE-INDEX.md      # stub catalogue
    distillations/{task}/
      {TASK}-DISTILLATION-INDEX.md  # stub situation router (one per task)
    lenses/
      LENS-INDEX.md           # stub lens catalogue
    apps/.gitkeep             # built profile outputs
    distros/.gitkeep          # packaged release artefacts
    README.md                 # corpus-level: purpose, owner, scope, licence

Tier is inferred from the target path (corpus.commons/* vs corpus.local/*)
or supplied with --tier. Refuses if the target exists and is non-empty.
Auto-creates the parent tier directory if missing.

Requires Python 3.9+ (uses PEP 585 generic syntax: list[str]).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent

VALID_TIERS = ("commons", "local")


def tier_from_path(target: Path) -> str | None:
    """Infer tier from a path like corpus.commons/foo or corpus.local/bar.

    Returns None when tier cannot be inferred, including when an absolute
    path resolves outside the repo root (the operator likely intends the
    --tier flag to apply in that case).
    """
    if target.is_absolute():
        try:
            parts = target.resolve().relative_to(REPO_ROOT).parts
        except ValueError:
            return None
    else:
        parts = target.parts
    if not parts:
        return None
    first = parts[0]
    if first == "corpus.commons":
        return "commons"
    if first == "corpus.local":
        return "local"
    return None


def prompt(message: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{message}{suffix}: ").strip()
    return answer or (default or "")


def task_slug_to_index_name(slug: str) -> str:
    """decision-making -> DECISION-MAKING-DISTILLATION-INDEX.md"""
    return slug.upper().replace("_", "-") + "-DISTILLATION-INDEX.md"


def task_slug_to_title(slug: str) -> str:
    """decision-making -> Decision-Making"""
    return "-".join(w.capitalize() for w in slug.replace("_", "-").split("-"))


def reference_index_stub(corpus_name: str) -> str:
    return dedent(
        f"""\
        # {corpus_name}: REFERENCE-INDEX

        Corpus catalogue. One row per source, ordered by relevance to the
        operator's strongest task domains. This is the *what is X* index;
        the per-task distillation indexes are the *when to reach for X*
        indexes.

        | Author / Source | Topic | Scope | One-line summary |
        |---|---|---|---|
        | _add rows as references land_ | | | |

        ## What goes here

        Every deep reference under `references/` gets an entry. Topic is
        the source's domain; scope is `open` / `open-nc` / `copyrighted` /
        `confidential` / `personal` (matches the deep ref's **Scope:**
        line). The one-line summary names the central claim or angle, not
        a generic genre tag.
        """
    )


def distillation_index_stub(task_slug: str, task_title: str, corpus_name: str) -> str:
    return dedent(
        f"""\
        # {task_title} distillations: index

        Situation router for the *{task_slug}* task axis of the
        **{corpus_name}** corpus. Two routing layers, phase-routing
        (macro) and runtime listener (micro), populated as
        distillations land.

        ## How to use

        Two layers, two query shapes.

        **Macro (phase-routing).** Query names a phase or situation type
        ("we're in contributing-factor analysis", "this is a
        stakeholder-management question"). Find the matching row in the
        *Phases / Situations* table; read the named distillations.

        **Micro (runtime listener).** Query carries an observable
        trigger from the room ("the team keeps saying X", "someone is
        stuck on Y"). Find the matching row in the *Runtime listener
        tables* (one per phase); read the cited distillation for the
        teach-in-the-moment script. The listener layer is populated
        only when the task spec at `tasks/{task_slug}.md` carries field
        2a (a seed trigger->response table); older 2D-only axes carry
        phase-routing only.

        Cite back through the deep reference for verification in both
        cases.

        ## Phases / Situations (macro / phase-routing)

        | Phase / Situation | Reach for | Reach-for-when |
        |---|---|---|
        | _add rows as distillations land_ | | |

        ## Runtime listener tables (micro / trigger -> framework)

        Per-phase tables. Inherits the seed trigger->response table
        from the task spec's field 2a. Each row: a real-time-recognisable
        trigger paired with the framework that fires plus a
        teach-in-the-moment script and a cite to the source's
        distillation.

        _Listener tables are seeded by `creating-applications` from the
        task spec's field 2a and grown by `creating-distillations` Pass
        G as each source lands. Remove this section if the task spec
        does not carry field 2a (lens-neutral 2D axis)._

        ### Phase 1 listener table

        | Trigger | Response (framework + teach script) | Source |
        |---|---|---|
        | _add rows as distillations land_ | | |
        """
    )


def lens_index_stub() -> str:
    return dedent(
        """\
        # LENS-INDEX

        Lens catalogue. A lens shapes a distillation through a perspective,
        role, or methodology stance, applied at ingestion time (Pass G of
        `creating-distillations`) where the operator declares the lens
        materially reweights what's salient for a distillation, or at retrieval
        time as a cheap reweight where it does not.

        | Kind | Slug | Purpose | Reach for when | Native vocabulary & salience |
        |---|---|---|---|---|
        | _add rows as lens specs land_ | | | | |

        ## What goes here

        Three kinds of lens are first-class:
        - **archetype**: a role-in-circumstance (e.g. `engineering-manager-post-incident`).
        - **real-person**: a named real person grounded in their published material.
        - **frame**: a non-personifiable frame of attention (e.g. `loss-aversion-lens`).

        Each lens has its own spec at `lenses/{slug}.md`. The
        `creating-lenses` skill (at the substrate level) walks the operator
        through scoping a new lens before this index gets a new row.
        """
    )


def corpus_readme_stub(corpus_name: str, tier: str, tasks: list[str]) -> str:
    task_lines = "\n".join(f"- `distillations/{t}/`" for t in tasks)
    licence_note = (
        "Everything in this corpus must be redistributable under an open or open-nc licence. "
        "See `../../CONTRIBUTING.md` for the admission rule."
        if tier == "commons"
        else "This corpus is gitignored by default. Mixed scopes are fine here; "
        "the operator decides what's redistributable and what isn't."
    )
    return dedent(
        f"""\
        # {corpus_name}

        A corpus under the `corpus.{tier}/` tier.

        ## What this corpus is for

        _One paragraph: the domain, the kind of question the corpus is built
        to answer, who curated it, what task axes it serves._

        ## Task axes

        {task_lines}

        ## Scope and licence

        {licence_note}

        ## Layout

        ```
        sources/ingest/        # drop material here, then run ingesting-resources
        sources/original/      # one .source.md sidecar per ingested source
        sources/converted/     # the markdown Pass C reads
        references/            # light + deep references; REFERENCE-INDEX.md
        distillations/{{task}}/   # per-task projections; per-task index
        lenses/                # optional lens specs; LENS-INDEX.md
        .claude/skills/        # corpus-bound skills (substrate skills stay at repo root)
        apps/                  # build output per profile
        distros/               # tarballs from `npm run package` (empty until shipped)
        ```
        """
    )


def scaffold(target: Path, tier: str, tasks: list[str], corpus_name: str) -> None:
    # sources/
    (target / "sources" / "ingest").mkdir(parents=True, exist_ok=True)
    (target / "sources" / "original").mkdir(parents=True, exist_ok=True)
    (target / "sources" / "converted").mkdir(parents=True, exist_ok=True)
    (target / "sources" / "ingest" / ".gitkeep").touch()
    (target / "sources" / "original" / ".gitkeep").touch()
    (target / "sources" / "converted" / ".gitkeep").touch()

    # references/
    (target / "references").mkdir(parents=True, exist_ok=True)
    (target / "references" / "REFERENCE-INDEX.md").write_text(
        reference_index_stub(corpus_name)
    )

    # distillations/{task}/
    for task in tasks:
        task_dir = target / "distillations" / task
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / ".gitkeep").touch()
        index_path = task_dir / task_slug_to_index_name(task)
        index_path.write_text(
            distillation_index_stub(task, task_slug_to_title(task), corpus_name)
        )

    # lenses/
    (target / "lenses").mkdir(parents=True, exist_ok=True)
    (target / "lenses" / "LENS-INDEX.md").write_text(lens_index_stub())

    # apps/ and distros/
    (target / "apps").mkdir(parents=True, exist_ok=True)
    (target / "apps" / ".gitkeep").touch()
    (target / "distros").mkdir(parents=True, exist_ok=True)
    (target / "distros" / ".gitkeep").touch()

    # .claude/skills/ — corpus-bound skills (those that cite this corpus's
    # references or task axes) live here. Substrate skills (corpus-agnostic)
    # stay at the repo-root .claude/skills/. The build resolver checks
    # corpus first, then substrate.
    (target / ".claude" / "skills").mkdir(parents=True, exist_ok=True)
    (target / ".claude" / "skills" / ".gitkeep").touch()

    # corpus-level README
    (target / "README.md").write_text(corpus_readme_stub(corpus_name, tier, tasks))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a new corpus directory under corpus.commons/ or corpus.local/."
    )
    parser.add_argument(
        "target",
        type=Path,
        help="Target path (e.g. corpus.local/my-corpus/ or corpus.commons/anthropic-cookbook/)",
    )
    parser.add_argument(
        "--tier",
        choices=VALID_TIERS,
        default=None,
        help="Tier override (commons or local). Default: infer from target path.",
    )
    parser.add_argument(
        "--tasks",
        default=None,
        help="Comma-separated task-axis slugs (e.g. decision-making,risk-assessment). "
        "Default: prompt interactively; or decision-making in non-interactive mode.",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Skip prompts; use defaults.",
    )
    args = parser.parse_args()

    target: Path = args.target
    if target.exists() and any(target.iterdir()):
        print(f"Refusing: target {target} exists and is non-empty.", file=sys.stderr)
        return 1

    tier = args.tier or tier_from_path(target)
    if tier is None:
        print(
            f"Cannot infer tier from {target}. Place the corpus under "
            f"corpus.commons/ or corpus.local/, or pass --tier.",
            file=sys.stderr,
        )
        return 1

    # Auto-create parent tier directory if missing.
    parent_tier = REPO_ROOT / f"corpus.{tier}"
    parent_tier.mkdir(parents=True, exist_ok=True)

    corpus_name = target.name
    tasks: list[str] = []
    if args.tasks:
        tasks = [t.strip() for t in args.tasks.split(",") if t.strip()]
    elif args.non_interactive:
        tasks = ["decision-making"]
    else:
        raw = prompt(
            "Task axes (comma-separated slugs, e.g. decision-making,risk-assessment)",
            default="decision-making",
        )
        tasks = [t.strip() for t in raw.split(",") if t.strip()]

    if not tasks:
        print("At least one task axis is required.", file=sys.stderr)
        return 1

    target.mkdir(parents=True, exist_ok=True)
    scaffold(target, tier, tasks, corpus_name)

    print(f"\nCorpus scaffolded at {target}/")
    print(f"  tier:   {tier}")
    print(f"  tasks:  {', '.join(tasks)}")
    print(f"  files:  references/, distillations/{{task}}/, lenses/, sources/, apps/, distros/")
    print()
    if tier == "local":
        print(
            "This corpus is gitignored. To share it publicly when ready, move "
            "the folder to corpus.commons/; the layout doesn't change."
        )
    else:
        print(
            "Reminder: everything in corpus.commons/ must be redistributable "
            "under an open or open-nc licence. See CONTRIBUTING.md."
        )
    print()
    print("Next: drop source material into sources/ingest/, then run the")
    print("ingesting-resources skill to land deep + light references and")
    print("task projections.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
