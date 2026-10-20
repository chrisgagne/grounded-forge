You are choosing four open-source projects for a pre-registered comparison of AI code reviewers on real bug fixes and real clean changes from project history. The builder and the operator of the system under test must not choose them; you do. Eight projects are already used and must not be picked again: node-semver, date-fns, yargs-parser, js-yaml, markdown-it, decimal.js, immutable-js, jsdiff (see ./projects.json).

Pick four JavaScript or TypeScript libraries that ALL hold:
1. Open-source licence (MIT, ISC, Apache-2.0 or BSD), public on GitHub.
2. A library, not an application or framework: self-contained logic (parsing, formatting, data structures, validation, math, text, URLs, encoding and the like), with no native code and no network or browser needed to run its tests.
3. At least five years of history with many small bug fixes that add or change a regression test in the same commit, and many small non-fix commits (features, refactors) that touch source code.
4. A different area from the eight above where you can, and from each other.
5. Not so well known that a reviewer would likely remember a given fix's commit from training data alone: prefer solid, widely used but not top-ten-famous libraries.

You can't browse; pick from what you know, and rank eight candidates so the operator can fall back down the list if a clone fails. The operator clones the first four that clone and does nothing else with the list.

Your final message is ONLY a JSON array of eight objects, no prose and no code fence, best first, each in the format of ./projects.json: {"name": "<folder name>", "repo": "https://github.com/OWNER/NAME", "area": "...", "why": "one sentence on why it meets the rules"}.
