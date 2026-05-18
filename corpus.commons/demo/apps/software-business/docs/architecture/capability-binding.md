# Capability binding

How grounded-forge apps declare expected runtime capabilities — `chat-export`, `issue-tracker`, `notes-archive` — without naming the concrete MCPs that fulfill them, and without forcing the substrate skill layer to carry MCP awareness.

## The problem

The two learning-ceremony profiles in this repo, `aar-mode` and `retro-mode`, ride on top of work-tools the user already owns. A retro needs the chat transcript from whichever chat product the team uses. An AAR needs timeline detail from whichever issue-tracker the engagement runs on. Neither profile should name those servers, and neither should hardcode the absence of them either.

The current state is honest about the gap and not much else. The retro template makes the lead the universal adapter: *"Paste chat output back into the window so you can synthesise."* This works, but it's an unconditional paste step even when the chat is one MCP call away. The AAR template names concrete servers in prose: *"call your issue-tracker / chat / build-system MCP tools directly if they are available."* This is a list, not a contract. The skill that needs the data has no structured way to ask. The profile that benefits from the data has no structured way to declare. The user who owns the servers has no structured way to bind them.

The substrate skill layer is the canary. Today the substrate skills (`matching-references`, `answer-from-library`, `audit-attribution`) are correctly MCP-blind: they read the curated indexes and the file system, nothing else. The day a substrate skill declares `requires_capabilities: [issue-tracker]` is the day every consumer of the forge has to reason about MCPs. The bright line is worth defending.

## Prior art, briefly

A short reconnaissance pass across BMAD-METHOD, OpenClaw, Hermes, OpenHands V1, Claude Code plugins, CrewAI, and Cline showed only Hermes cleanly splits *abstract capability* from *concrete binding*. Hermes skills declare `requires_toolsets:` and `fallback_for_toolsets:` in frontmatter; concrete fulfillment comes from plugins, env vars, or an auto-promoted fallback skill. This is the pattern the spec borrows, translated as `recommends_capabilities:` at the profile boundary and a user-owned `~/.claude/capabilities.toml`.

OpenHands V1, Claude Code plugins, and CrewAI all bundle the concrete server with the skill: per-skill `mcp_tools.mcpServers:`, plugin-shipped `.mcp.json`, `tools=[SerperDevTool()]`. This is the right pattern for a utility plugin that *is* the integration. It is the wrong pattern for a facilitator app that rides on whichever issue-tracker the user already owns.

BMAD-METHOD has no external-binding layer; external tools are the host IDE's problem. Cline routes by keyword, not capability. Neither is a fit for the matrix architecture's question, which is *how does an app declare what it benefits from, without enumerating who fulfills it*.

OpenClaw's eligibility gates — a skill that needs `slack` simply disappears when no Slack token is present — are the closest thing to graceful degradation as a structural feature. Hermes' `fallback_for_*` is the richer expression: the skill stays, it just runs the degraded path.

The spec inverts the common pattern. **Capability is declared by the app, bound by the user, never named by the skill.**

## The model

An app **conforms** to capability-binding when its substrate skills declare nothing, its corpus-bound skills degrade gracefully on unbound capabilities, and its profile recommends capabilities at the app level rather than the skill level.

| Skill location | Capability declaration | Capability use |
|---|---|---|
| Substrate (repo `.claude/skills/`) | MUST NOT declare | MUST NOT call MCPs |
| Corpus-bound framework-application | SHOULD NOT declare | MAY call MCPs opportunistically; MUST degrade gracefully when unbound |
| Corpus-bound integration-heavy | MAY declare `requires_capabilities:` | MUST declare `fallback_for_capabilities:` or fail closed with a clear binding instruction |
| Build profile ([`builds.yaml`](../../builds.yaml)) | SHOULD declare `recommends_capabilities:` when the app benefits | — |
| Build profile CLAUDE.md template | SHOULD describe recommended capabilities + behaviour without them | — |

Substrate is `MUST NOT`, not `SHOULD NOT`, because substrate skills ship to every app the forge compiles. The substrate layer is corpus-agnostic by construction (see [CLAUDE.md, *Skills layout: substrate vs corpus-bound*](../../CLAUDE.md)); MCP awareness anywhere in that layer forces every downstream consumer — including consumers whose corpora have no concept of Slack or Shortcut — to reason about bindings they will never use. The matrix architecture's whole point is that the reference axis and the substrate skill set are invariant across applications ([`overview.md`](overview.md), [`matrix-pattern.md`](matrix-pattern.md)). Capability declarations are not invariant; they live one layer up.

The profile carries the recommendation, not the individual skills inside it, because the app as a whole benefits while only one or two skills actually use the binding. A retro session benefits from `chat-export` once per retro, regardless of how many distillations the facilitator reads. Pushing the declaration down into per-skill frontmatter spreads a single app-level recommendation across N skills and turns a coherent app-time decision into N skill-time decisions. The CLAUDE.md template is where the model first reads the recommendation; it stays the right surface for the *behavioural* answer too: what the app does when bound vs unbound.

Graceful degradation is `MUST`, not `SHOULD`, because a skill that hard-fails on a missing MCP is non-conforming. The retro profile's paste-mode is the conformance exemplar: the lead pastes; the retro continues; the framework citations and distillations work exactly the same. The `MAY declare requires_capabilities:` row exists for the rare case where the skill's job is structurally impossible without the binding (`/aar-start [bug-id]` cannot synthesise a bug-id it cannot fetch). Even there, the obligation is to fail closed with a binding instruction, not to fail open with hallucinated detail.

**Capability vocabulary.** Three names cover the worked example: `chat-export` (pull a chat transcript), `issue-tracker` (create or query work items), `notes-archive` (search the user's notes corpus). Vocabulary governance is an open question (§5); the spec does not commit to a list.

**Binding shape.** The user owns `~/.claude/capabilities.toml`. Sketch only:

```toml
[capabilities]
chat-export   = "mcp__slack__channel_history"
issue-tracker = "mcp__shortcut__create_story"
notes-archive = "fs:~/notes/"
```

The resolver that consumes this file is a follow-up doc (§5). The contract is what's specified here.

## Worked example

The `retro-mode` profile is the public-corpus case; `aar-mode` follows the same shape.

**(a) [`builds.yaml`](../../builds.yaml) addition.** A new optional key on the profile, parallel to `skills:` and `distillations:`:

```yaml
recommends_capabilities:
  - name: chat-export
    purpose: "Pull retro chat transcript without human paste"
    fallback: "Lead pastes chat output into the window"
  - name: issue-tracker
    purpose: "Create follow-up tickets for retro experiments"
    fallback: "Lead copies action items to their tracker manually"
```

**(b) CLAUDE.md template diff.** A retro template that lists *"Paste chat output"* as one of the lead's three unconditional jobs becomes a `SHOULD`-conditional paragraph under capability-binding:

> *Before* — *"The lead's three jobs: read prompts aloud, run countdowns, paste chat output."*
>
> *After* — *"Read prompts aloud. Run countdowns. When `chat-export` is bound, pull the transcript directly at the end of each timeboxed segment; when unbound, ask the lead to paste. When `issue-tracker` is bound, draft follow-up tickets at Phase 4 close; when unbound, output the experiment as markdown for the lead to copy."*

The retro continues either way. The conformance test is the unbound path: every framework citation, every distillation read, every facilitation move still works.

**(c) The skill-level case.** No retro skill declares anything. The capability hint sits at the app boundary; the model reads CLAUDE.md once at session start and picks the right path at runtime. Contrast with a hypothetical `aar-start` skill: `/aar-start [bug-id]` literally cannot run without an issue-tracker, so it is the rare `MAY declare requires_capabilities: [issue-tracker]` case, paired with a `fallback_for_capabilities:` route that points the user at a hand-led mode that doesn't need the tracker. Same app, two skills, one declaration. The app-level recommendation still belongs in `builds.yaml`; the skill-level declaration is the exception, justified by structural impossibility.

## Open questions

Three deferrable questions. None block the spec.

1. **Resolver mechanism.** A hook, a template-loader, or build-time substitution of capability blocks into the compiled CLAUDE.md. Build-time substitution is the simplest answer and introduces no new runtime primitives, but the spec stays mechanism-neutral until the first resolver lands.
2. **Capability vocabulary governance.** Who decides `chat-export` is the right name vs `chat-transcript` vs `conversation-history`. A flat list under `docs/reference/` is the likely answer; not now.
3. **Install-time UX.** First version is honest: the user reads CLAUDE.md, sees what the app recommends, writes their own `capabilities.toml`. A `claude mcp list`-sourced dropdown is later.
