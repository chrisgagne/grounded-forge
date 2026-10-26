# Extend or clear the demo corpus

The OpenStax portion of the demo ships with image classification incomplete for six of twelve books. Two procedures, depending on what you want.

## Complete the image classification

Inside a Claude Code session opened at this repo root, run the `ingesting-images` skill against the source you want fully classified. The `/skill-name` invocations below are Claude Code slash-commands that call the skills under `.claude/skills/`:

```
/ingesting-images psychology-2e
```

Or against every source whose entries are flagged PARTIAL:

```
/ingesting-images all
```

Rough Opus 4.7 cost: a few hundred thousand tokens per source for 300–700 images, depending on how many already-extracted images the source has and how many turn out to be substantive. Visual inspection is per-image; no shortcut.

## Clear the demo and start fresh

```
npm run remove-corpus:openstax
```

That removes every OpenStax source from the demo corpus in one command, one [`removing-resources`](../../.claude/skills/removing-resources/SKILL.md) run per source: originals retired to `sources/removed/`, references, distillations and image entries deleted, each source taken off the concept index and the distillation indexes. Surviving sources' distillations that cited an OpenStax book are listed in `_planning/removals/demo/`; rewrite them with the skill's rewrite step before you build. Then run [`ingesting-resources`](../../.claude/skills/ingesting-resources/SKILL.md) on your own books, papers, or reports. The full forking walkthrough is at [`build-your-library.md`](build-your-library.md).

## See also

- [`docs/reference/known-limitations.md`](../reference/known-limitations.md): what ships partial and why.
- [`.claude/skills/ingesting-images/SKILL.md`](../../.claude/skills/ingesting-images/SKILL.md): the skill's full runbook.
- [`.claude/skills/ingesting-resources/SKILL.md`](../../.claude/skills/ingesting-resources/SKILL.md): the 9-pass protocol runbook for new sources.
