// Factory Review: the factory-warranty app's review stage and library as a connector, at
// review.groundedforge.com. Same Worker as AAR Maker; these are its words and the app it packs.
// {{workflows}} becomes the list of workflow names, {{origin}} the Worker's origin (escaped),
// {{cursor}} Cursor's install link.
const REPO = "https://github.com/chrisgagne/grounded-forge/tree/main/corpus.commons/chrisgagne-agent-built-software";

export default {
  id: "factory-review",
  title: "Factory Review",
  version: "0.1.0",
  contact: "https://github.com/chrisgagne/grounded-forge/issues", // support and privacy requests; shown on /privacy
  app: "../../corpus.commons/chrisgagne-agent-built-software/apps/factory-warranty",
  task: "warranting-agent-built-software",

  instructions: "Factory Review: the review stage of a software factory for AI-built changes, and the open "
    + "library behind it: distillations of 17 openly licensed sources (NIST SSDF and SP 800-218A, the "
    + "CISA attestation form, OWASP's ASVS and LLM and agentic top tens, Microsoft's engineering "
    + "playbook, UK government assurance guidance, METR's productivity trial, SWE-bench and others) "
    + "projected onto eight stages of a change's life, from specifying it to releasing it. To review a "
    + "change or help someone decide whether to sign it off, call get_workflow with name "
    + "\"review-change\" and follow it. Before answering from the library, call get_workflow with name "
    + "\"guide\" once per conversation: it sets the discipline (demonstrated, not asserted; never sign "
    + "for the person) and the retrieval order. The guide and workflows were written for a folder "
    + "install; where they name a file, use the matching tool: task-index.json, its "
    + "task-index.shard-*.json files or WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md → route, "
    + "{slug}-warranting-agent-built-software.md → read_distillation, concept-index.json → list_topics "
    + "and find_concepts, slug-table.json → list_sources, a skill file → get_workflow. The factory "
    + "harness itself (factory/) isn't served: it runs on the person's own machine, from " + REPO + ". "
    + "Cite only what a tool returned; if the library does not cover something, say so. Every source "
    + "is open and licensed for commercial use; [V] passages are verbatim under each source's licence, "
    + "each distillation's Source line names it, and share-alike sources keep their attribution and "
    + "licence when quoted. The guide's NOTICE.md says what this connector is and isn't; its LICENSE-CONTENT.md and "
    + "DISCLAIMER.md set out the terms.",

  notice: `# Using Factory Review

Factory Review is a hosted connector run by Approach Perfect, Limited (the Supplier named in DISCLAIMER.md). It serves the factory-warranty library and its review workflow to your own AI assistant.

- **It reviews nothing itself.** Your assistant does the reviewing, on your model provider's service and under their terms. The connector receives only what its tools are called with: workflow and section names, source ids and search words. Your code reaches it only if your assistant puts some in a search.
- **A review is not a warranty.** The sign-off sheet says what the code shows and what it doesn't. It isn't a sign-off, and nothing in it is the Supplier's warranty of any change. Whoever signs a change is responsible for it.
- **What's logged:** your GitHub username, the tool called and the library file it read, never the words of a search. Cloudflare keeps the logs for a few days.
- **No service promise.** It's free, it may change or stop at any time, and access can be withdrawn.
- **Terms.** DISCLAIMER.md applies to everything served here, including clause 6 on the risks of using large language models: don't put confidential or regulated material into a review without your own security review. Each source keeps its own licence (LICENSE-CONTENT.md).
`,

  guidePreface: "> **Using this guide through the Factory Review connector.** It was written for a folder install. "
    + "Where it names a file, use the matching tool: `task-index.json`, its `task-index.shard-*.json` files or "
    + "`WARRANTING-AGENT-BUILT-SOFTWARE-DISTILLATION-INDEX.md` → `route`; `{slug}-warranting-agent-built-software.md` "
    + "→ `read_distillation`; `concept-index.json` → `list_topics` and `find_concepts`; `slug-table.json` → "
    + "`list_sources`; a skill in `.claude/skills/` → `get_workflow`. The factory harness (`factory/`) and the "
    + "repository's `docs/` aren't served; they're in the public repository, " + REPO + ". To review a change, "
    + "follow `get_workflow(\"review-change\")`. What this connector is and isn't: "
    + "`get_workflow(\"guide\", \"NOTICE.md\")`.",

  tools: {
    get_workflow: {
      title: "Get a workflow or the guide",
      description: "Use this first when someone asks to review a change, pull request or diff, or asks "
        + "whether they can sign a change off: get_workflow(\"review-change\") is the factory's review "
        + "stage and its sign-off sheet. Call get_workflow(\"guide\") once at the start of any "
        + "conversation that uses this library: it sets the discipline, the retrieval order, the "
        + "licensing terms, and how file paths in the workflows map to these tools. Workflows: "
        + "{{workflows}}. With no file, returns the workflow's SKILL.md and lists its other files. Long "
        + "files come in parts: read every part. Follow the workflow.",
    },
    route: {
      title: "Route a change's stage",
      description: "The task index: the stage router for warranting agent-built software. With no "
        + "section, lists its sections: for each of eight phases (1 specifying, 2 triaging risk, 3 "
        + "locking the tests, 4 building in the sandbox, 5 gating, 6 reviewing, 7 warranting, 8 "
        + "releasing and operating) a situation table and a runtime-listener table (a trigger a "
        + "practitioner notices → the response the sources call for), plus the named disagreements "
        + "between sources. With a section, returns its rows and the sources they point to.",
      section: "Section name or a unique part of one, e.g. \"Runtime listeners: Phase 6\" or \"Named disagreements\".",
    },
    read_distillation: {
      description: "One distillation: a single openly licensed source (NIST SSDF, OWASP ASVS, the CISA "
        + "attestation form, Microsoft's engineering playbook, the UK Duck and Aqua books, METR's trial, "
        + "...) projected onto the eight phases, with a gate question, the evidence that answers it and "
        + "red flags, and evidence markers [V] [AP] [AR] [AE] [BT]. Its Source line names the source's "
        + "licence. Returns the whole distillation, or one section of it when `section` is given.",
      source: "A 3-character id from route/find_concepts, or a slug (e.g. owasp-asvs-5-0).",
    },
    find_concepts: { query: "Concept name or synonym, e.g. \"code review\"." },
    list_sources: { query: "Optional words to match, e.g. \"owasp\"." },
  },

  pages: {
    privacy: `<p>Signing in shares your public GitHub username with Factory Review, nothing else: no email, no repositories.</p>
<p>What's logged: your GitHub username, which tool was called and which library file it read. Never what you type, and never your code. Logs are kept by Cloudflare for a few days.</p>`,
    landing: `<h1>Factory Review</h1>
<p>The review stage of a software factory for AI-built changes, served as an MCP connector. Your own Claude or ChatGPT reviews a change with the factory's brief, checks it against an open library (NIST, OWASP, CISA, UK government assurance guidance and research on AI-assisted development), and writes a plain-words sign-off sheet that keeps what the code shows apart from what someone only said.</p>
<p><strong>What it isn't:</strong> the rest of the factory. Locked tests, sandboxed checks and a tamper-evident log need the harness on your own machine (<a href="${REPO}">grounded-forge</a>). And in our tests on the ReviewBench benchmark, the brief found no more than a plain “review this as a careful senior engineer” prompt on either Claude or OpenAI's model; it beat the labs' own review commands only at their default settings. Running a second model family's review beside it found the most. The results are in the repository.</p>
<p>Connector URL: <code>{{origin}}/mcp</code></p>
<p><strong>Claude</strong> (web, desktop or mobile): Settings → Connectors → Add custom connector, paste the URL, then sign in with GitHub. Open the connector and set Read-only tools to <em>Always allow</em>, or Claude will ask before every library read.</p>
<p><strong>Claude Code:</strong> <code>claude mcp add --transport http factory-review {{origin}}/mcp</code>, then <code>/mcp</code> to sign in.</p>
<p><strong>ChatGPT:</strong> Settings → Plugins, add a server (Streamable HTTP, the URL above, no token), then sign in with GitHub. Start your first message with “Use Factory Review to…”: ChatGPT won't use it unless asked.</p>
<p><strong>Cursor:</strong> <a href="{{cursor}}">Add to Cursor</a>, or add <code>"factory-review": { "url": "{{origin}}/mcp" }</code> under <code>mcpServers</code> in <code>~/.cursor/mcp.json</code>, then sign in with GitHub when Cursor asks.</p>
<p><strong>First run:</strong> “Use Factory Review to review this change before I sign it off.” Bring the diff or pull request and what it was meant to do.</p>
{{privacy}}
<p class="mute"><small>Built by Chris Gagné, with Claude and Codex. The library's licence terms are served with it: ask the assistant for Factory Review's licence.</small></p>`,
  },

  selftest: {
    licenceWord: "share-alike",
    phase: "Runtime listeners: Phase 6",
    slug: "owasp-asvs-5-0",
    slugText: "Application Security Verification Standard",
    sectionPath: "distillations/warranting-agent-built-software/owasp-asvs-5-0-warranting-agent-built-software.md",
    section: "Phase 6",
    concept: "code review",
    sourceQuery: "owasp",
    minSources: 15,
  },
};
