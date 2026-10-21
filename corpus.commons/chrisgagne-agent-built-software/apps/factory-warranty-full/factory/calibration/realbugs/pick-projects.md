You are choosing the source projects for a calibration set of real bugs. A software "factory" reviews code changes with AI reviewers; we will measure how often it catches real bugs by replaying reverted bug fixes from open-source history, plus real clean commits as controls. Neither the factory's builder nor its operator may choose the projects; you do.

Pick 8 open-source JavaScript or TypeScript projects on GitHub that meet ALL of these:
1. Permissive licence (MIT, ISC, BSD or Apache-2.0).
2. Mostly pure logic: parsing, formatting, dates, versions, data structures, CLI argument handling, text processing. Avoid projects whose main purpose is security, crypto, authentication, sandboxing or network protocols.
3. A long history (years) of small, well-described bug-fix commits that come with a regression test, in the default branch.
4. Plain JS/TS that a reviewer can understand from the diff and the surrounding files, without native code.
5. Small enough to clone (well under 500 MB of history).
6. Varied: no more than two projects from the same problem area.

Answer with only a JSON array, no prose, of 8 objects: {"name": "...", "repo": "https://github.com/OWNER/NAME", "area": "...", "why": "one sentence"}.
