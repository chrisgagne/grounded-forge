// AAR Maker: the words the connector shows, and the app it packs. bundle.mjs writes this into
// src/bundle.json; src/mcp.js and src/index.js read it from there. {{workflows}} becomes the list
// of workflow names, {{origin}} the Worker's origin (escaped), {{cursor}} Cursor's install link.
export default {
  id: "aar-maker",
  title: "AAR Maker",
  version: "0.2.0",
  contact: "https://github.com/chrisgagne/grounded-forge/issues", // support and privacy requests; shown on /privacy
  app: "../../corpus.commons/demo/apps/aar-mode",
  task: "aar",

  instructions: "AAR Maker: a source-grounded After-Action Review assistant built on an open library: "
    + "distillations of openly licensed sources (US Army TC 25-20, the US Forest Service learning "
    + "review guide, the NHS Just Culture guide, the DOE human performance handbooks, the Columbia "
    + "accident report and others) projected onto AAR work. Before facilitating an AAR or "
    + "answering from the library, call start_retro_or_postmortem once per conversation (it returns "
    + "the guide, as get_workflow with name \"guide\" does): it "
    + "sets the discipline (blameless by default, local rationality, contributory factors not the "
    + "cause) and the retrieval order. For any after-action review, post-incident review, postmortem, "
    + "retrospective or lessons-learned conversation, call it before asking the user anything. Read every "
    + "part of a long file, and read the task index (route) before choosing distillations. The guide and workflows were written for a folder install; "
    + "where they name a file, use the matching tool: task-index.json or AAR-DISTILLATION-INDEX.md → "
    + "route, {slug}-aar.md → read_distillation, concept-index.json → list_topics and find_concepts, "
    + "slug-table.json → list_sources, lens-index.json → get_lenses, a skill or agent file → "
    + "get_workflow. Cite only "
    + "what a tool returned; if the library does not cover something, say so. The library is built "
    + "from open and open-nc sources: [V] passages are verbatim under each source's licence, each "
    + "distillation's Source line names that licence, and non-commercial terms apply to open-nc "
    + "material. The guide's NOTICE.md says what this connector is and isn't; its LICENSE-CONTENT.md and "
    + "DISCLAIMER.md set out the terms.",

  notice: `# Using AAR Maker

AAR Maker is a hosted connector run by Approach Perfect, Limited (the Supplier named in DISCLAIMER.md). It serves an after-action review library and its facilitation workflows to your own AI assistant.

- **It facilitates nothing itself.** Your assistant runs the review, on your model provider's service and under their terms. The connector receives only what its tools are called with: workflow and section names, source ids and search words. Your incident details reach it only if your assistant puts some in a search.
- **It isn't professional advice.** A review run with it is not legal, safety, clinical or HR advice (DISCLAIMER.md, clause 4), and its findings are yours to weigh.
- **What's logged:** your GitHub username, the tool called and the library file it read, never the words of a search. Cloudflare keeps the logs for a few days.
- **No service promise.** It's free, it may change or stop at any time, and access can be withdrawn.
- **Terms.** DISCLAIMER.md applies to everything served here, including clause 6 on the risks of using large language models: don't put confidential, personal or legally privileged incident material into a session without your own security review. Each source keeps its own licence, and non-commercial terms apply to open-nc material (LICENSE-CONTENT.md).
`,

  // The front door (src/mcp.js, START): claude.ai loads a connector's tools only when Claude
  // decides it needs them, so this name and description carry the words people use.
  start: {
    name: "start_retro_or_postmortem",
    title: "Start a retro, postmortem or after-action review",
    description: "Call this first, before answering from general knowledge, whenever someone wants "
      + "to run or write a retrospective (retro), postmortem, post-incident or incident review, "
      + "after-action review (AAR), debrief or lessons-learned session, or asks how to look back at "
      + "something that went wrong (an outage, a failed launch, a missed target, a clinical or "
      + "safety event) without blaming people. Call it before drafting a postmortem document too. "
      + "Returns AAR Maker's facilitation guide: a blameless review method drawn from US Army, "
      + "US Forest Service and NHS guidance, the first questions to ask, and how to cite its "
      + "library of 22 openly licensed sources (TC 25-20, the NHS Just Culture Guide and its "
      + "decision tree, the Forest Service Learning Review Guide and others).",
  },

  tools: {
    get_workflow: {
      title: "Get a workflow or the guide",
      description: "AAR Maker's guide and its facilitation and retrieval workflows for after-action "
        + "reviews, post-incident reviews, postmortems, retrospectives and lessons-learned conversations. "
        + "The guide (name \"guide\") sets out the AAR discipline, the retrieval order, the licensing "
        + "terms, and how file paths in the workflows map to these tools. Workflows: {{workflows}}. "
        + "With no file, returns the workflow's SKILL.md and lists its other files. Long files come "
        + "in parts.",
    },
    route: {
      title: "Route an AAR situation",
      description: "The AAR task index: the situation router that matches each phase of an "
        + "after-action review, post-incident review, postmortem or retrospective to the sources that fit. With no section, lists its sections "
        + "(Phases 0-5: scoping, timeline and local rationality, contributory factors, just-culture "
        + "sorting, action design, learning-loop closure). With a section, returns its rows (need → "
        + "source id, and when it applies) and the sources those rows point to.",
      section: "Section name or a unique part of one, e.g. \"Phase 4\" or \"Anti-Patterns\".",
    },
    read_distillation: {
      description: "One distillation: a single openly licensed source (TC 25-20, the Forest Service learning "
        + "review guide, NHS Just Culture, the DOE human performance handbooks, the Columbia accident "
        + "report, ...) projected onto AAR work, with evidence markers [V] [AP] [AR] [AE] [BT]. Its "
        + "Source line names the source's licence. Returns the whole distillation, or one section of "
        + "it when `section` is given.",
      source: "A 3-character id from route/find_concepts, or a slug (e.g. tc-25-20-army-aar).",
    },
    find_concepts: { query: "Concept name or synonym, e.g. \"just culture\"." },
    list_sources: { query: "Optional words to match, e.g. \"army\"." },
    get_lenses: {
      description: "Lenses that reweight what's salient for a named reader (builder, a PM bounded by a BA role, "
        + "agentic builder, a named consultant-coach): purpose, when each fits, and its "
        + "salience block. The full specs aren't served.",
    },
  },

  pages: {
    // What signing in shares and what's logged; shown on the landing and consent pages.
    privacy: `<p>Signing in shares your public GitHub username with AAR Maker, nothing else: no email, no repositories.</p>
<p>What's logged: your GitHub username, which tool was called and which library file it read. Never what you type, and never your incident details. Logs are kept by Cloudflare for a few days.</p>`,
    landing: `<h1>AAR Maker</h1>
<p>A source-grounded after-action review coach, served as an MCP connector. It runs a review blameless by default and draws on openly licensed sources: US Army TC 25-20, the US Forest Service learning review guide, NHS Just Culture, the DOE human performance handbooks, the Columbia accident report and others.</p>
<p>Connector URL: <code>{{origin}}/mcp</code></p>
<p><strong>Claude</strong> (web, desktop or mobile): Settings → Connectors → Add custom connector, paste the URL, then sign in with GitHub. Open the connector and set Read-only tools to <em>Always allow</em>, or Claude will ask before every library read.</p>
<p><strong>Claude Code:</strong> <code>claude mcp add --transport http aar-maker {{origin}}/mcp</code>, then <code>/mcp</code> to sign in.</p>
<p><strong>ChatGPT:</strong> Settings → Plugins, add a server (Streamable HTTP, the URL above, no token), then sign in with GitHub. Start your first message with “Use AAR Maker to…”: ChatGPT won't use it unless asked.</p>
<p><strong>Cursor:</strong> <a href="{{cursor}}">Add to Cursor</a>, or add <code>"aar-maker": { "url": "{{origin}}/mcp" }</code> under <code>mcpServers</code> in <code>~/.cursor/mcp.json</code>, then sign in with GitHub when Cursor asks.</p>
<p><strong>First run:</strong> “Help me run an after-action review of [the incident or project].” Bring the timeline and who was involved.</p>
{{privacy}}
<p class="mute"><small>Built by Chris Gagné. The library's licence terms are served with it: ask the assistant for AAR Maker's licence.</small></p>`,
  },

  // What selftest.mjs checks against this connector's bundle.
  selftest: {
    licenceWord: "non-commercial",
    phase: "Phase 4",
    slug: "tc-25-20-army-aar",
    slugText: "After-Action",
    sectionPath: "distillations/aar/tc-25-20-army-aar-aar.md",
    section: "Phase 3",
    concept: "just culture",
    sourceQuery: "army",
    minSources: 20,
  },
};
