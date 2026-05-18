# Comparative eval methodology

The eval is comparative because the architectural claim is comparative. The matrix projects sources to task domains once at ingestion; the question is whether that pre-projection produces better answers per token than the alternatives: generic Claude, Claude with research forced, or Claude with the raw source corpus in context. This harness collects four method-answers to the same prompt, then asks a blind LLM judge to rank them on a 5-criterion rubric.

## The four methods

| Method | What it is | Where it lives |
|---|---|---|
| **A** | Naive Claude: Claude.ai/desktop or Claude Code, no tools attached. The lower bound: what you get from the model alone. | Claude.ai or Claude Code |
| **B** | Claude with research forced: Claude.ai's deep-research subagent flow, multi-step, with web retrieval. The "well-informed Claude" baseline. | Claude.ai web app only |
| **C** | Claude with the corpus's converted markdown sources in context: drop the `.md` files into the session and let the model work through them. | Claude.ai or Claude Code with files attached |
| **D** | Framework-task-matrix: `claude .` opened in a built grounded-forge app folder. | Claude Code |

The harness does not automate any of the four methods. The operator runs each in its natural product surface and pastes the answer text into `{manual-dir}/{prompt-stem}-{A|B|C|D}.md`. Each method's product surface is different (Claude.ai's research subagent, Claude.ai with attached files, Claude Code with a built app) and those surfaces are not interchangeable with a single SDK call. The harness's contribution is the blind-judge protocol, not method execution.

A note on Method B's reproducibility: B is the Claude.ai web app's Research feature, which runs a deep-research subagent flow over several minutes. Claude Code can be told to web-search via the `WebSearch` tool, but that lands closer to A than to B. B's multi-step retrieval flow is not reducible to a tool call. A user can run B manually in Claude.ai and paste the result into Claude Code as context, but that workaround does not transfer to automated tooling: anywhere the matrix is invoked programmatically (the demo app, `/answer-from-library`, a subagent in a pipeline) cannot consume B's output. B is a comparison the maintainer and architect-buyer can run; not a comparison a forker can wire into their dev loop.

A note on Method A's web search: across the eval rounds, Claude with web search *available* never chose to invoke it. The naive A method is therefore the lower bound under the operator's natural product surface. A forced-web-search variant (Claude Code with `WebSearch` invocation required) would likely land between this A and B. That variant has not yet been measured.

## The judge

A separate Claude API session, blind to which method produced which answer and blind to method labels. The judge receives:

- The original prompt
- The four answers in a randomised order, labelled `answer_1` through `answer_4`
- A scoring rubric with five 1–10 criteria

The judge returns a ranking with per-answer per-criterion scores and a rationale. The harness then decodes `answer_N` back to method codes A/B/C/D for the run record.

### The rubric

The harness's default rubric is `essay`, shipped at [`harness/judge-prompts/essay.md`](harness/judge-prompts/essay.md). Five criteria, each scored 1–10:

1. **Evidence-grounding**: Are claims grounded in named sources, frameworks, scholars, or specific arguments? Or general assertions in the form of "studies show" or "experts agree"?
2. **Internal coherence**: Does the answer commit to a position and develop it consistently, or hedge between competing views without integration?
3. **Specificity**: Does the answer name specific frameworks, authors, mechanisms, and distinctions, or stay at consensus generality?
4. **Defensibility**: Is the position the answer takes one a domain expert could defend with citations, or fluent-but-unanchored prose? *Guardrail (added post-eval-round-1): the judge is instructed not to mark answers down for citing scholars or arguments outside its training prior; unfamiliarity is not unverifiability. This is a partial mitigation for the known limit below; see the rubric file for the exact wording.*
5. **Adherence to prompt**: Did the response deliver what was asked, in the shape and at the length the prompt specified?

A `named_scholars` count is also extracted as a separate audit field (not a 1–10 score): how many distinct named scholars or named authors appear in the answer's body. This is a citation-density indicator, not a ranking criterion.

A simpler 5-criterion variant ships at [`harness/judge-prompts/default.md`](harness/judge-prompts/default.md) for non-essay prompts. The rubric file is the canonical reference; this section is a synopsis.

## What the eval supports

This rubric measures *answer-quality-as-perceived-by-an-LLM-judge*. It does not directly measure:

- Operational cost (tokens, latency, dollars): these are reported per automated method but not for the manual-paste methods, because Claude.ai and Claude Code do not expose token use through the same channel as the SDK
- Hallucination rate, in the strict sense: the judge can mark down a defensibility score for citations it does not recognise, but it cannot independently verify citations against the source
- Per-claim auditability: the matrix's distinctive value-add, and the surface this rubric is structurally blind to (see *known limitations* below)
- End-user latency, multi-turn behaviour, or production-running characteristics

For a single-source-grounded benchmark of a specific deep reference's fidelity to its source, see Pass I in the [9-pass ingestion protocol](../architecture/ingestion-protocol.md) and the calibration fixture at [`tests/audit-fixtures/`](../../tests/audit-fixtures/).

## Known limitations of this rubric

The eval rounds surfaced a structural limit the next rubric rework is designed to address. The limit is honestly named because it is load-bearing for what the eval can and cannot demonstrate.

**The judge's `evidence_grounding` and `defensibility` criteria collapse to *"is this in my training prior?"*** The judge is an LLM with no separate authority to consult. When it scores whether a citation is defensible, it is checking the citation against its own training data.

- On **canonical material** (sources in training-data density) that mostly maps to truth, and the rubric works.
- On **non-canonical material** (operator-curated, private, or thinly-represented in training data) it maps to *recognise-the-derivative-cluster*. Methods that read the operator's material get marked down for being unverifiable; methods that read the canonical-derivative cluster (B's research path, for example) get marked up for being recognisable.

This means there is no corpus on which the single-LLM-as-judge rubric can fairly measure the matrix's distinctive value-add (per-claim auditability on operator-curated non-canonical material) because the verification surface (the judge's training prior) is precisely what the matrix is built to defend against dominating the answer.

Candidates for the next eval-rubric rework: a calibrated heuristic critic that reads against operator-marked ground truth rather than against judge-prior; an operator-as-judge framing for specific traditions; an audit-trace fidelity score; the missing forced-web-search variant of A.

## Findings to date

The qualitative findings from the internal eval rounds are summarised in the *Audit receipts and evals* section of the [root README](../../README.md#audit-receipts-and-evals), including the canonical-material vs non-canonical-material split, the filename-as-key-into-training-prior effect, and the post-migration token-cost numbers. The full per-round outputs are gitignored at `_evals/results/` because the corpora used extend beyond the demo corpus; the qualitative summary in the README is the public-facing record.

## Running the harness

The harness is a thin blind-judge runner: ~200 lines of Python that load four pre-collected method answers, shuffle them under a blind labelling, send a system prompt with the rubric, and write a JSON result with the decoded ranking and scores. The rubric is a markdown file at [`harness/judge-prompts/`](harness/judge-prompts/) you can read and edit directly without touching Python; the script reads whichever rubric you name.

**Requires:** Python 3.9+, `anthropic` SDK ≥ 0.92.0, `ANTHROPIC_API_KEY` in environment.

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...

# Collect the four method-answers manually for one prompt, save to _evals/manual/:
#   _evals/manual/e01-stakeholder-conflict-A.md
#   _evals/manual/e01-stakeholder-conflict-B.md
#   _evals/manual/e01-stakeholder-conflict-C.md
#   _evals/manual/e01-stakeholder-conflict-D.md

# Run the judge:
python docs/evals/harness/eval.py e01-stakeholder-conflict
```

The script loads the prompt from [`harness/prompts/`](harness/prompts/), the four paste-results from `_evals/manual/` (gitignored), the rubric from [`harness/judge-prompts/essay.md`](harness/judge-prompts/essay.md) (default), and writes the decoded JSON result to `_evals/results/`. The prompt files include both `e*-` epistemic essay prompts (which default to the `essay` rubric) and `p*-` decision-domain prompts.

The judge runs once per invocation. For multi-seed comparisons, run the script multiple times with different `--seed` values; each output JSON carries the seed in its filename.

### Useful flags

- `--seed N`: shuffle seed for the blind labelling (default 1). Change to test rank stability.
- `--rubric NAME`: pick a rubric file under `harness/judge-prompts/` (default: `essay`). The `default` rubric is a simpler 5-criterion variant for non-essay prompts.
- `--model MODEL`: override the judge model (default: `claude-opus-4-7`).
- `--prompts-dir`, `--manual-dir`, `--out-dir`: point at different directories (e.g. a forker's own prompt set or paste-result location).

### Modifying the rubric

The rubric is just a system prompt. The `essay` rubric scores 5 criteria 1-10 plus a `named_scholars` audit count; the `default` rubric scores 5 different criteria. To change scoring criteria, edit the rubric markdown file directly. To add a new rubric, drop a new file into `harness/judge-prompts/` and pass its stem as `--rubric`. The Python code reads whichever file you name; it doesn't bake the rubric in.

## Prior art

A four-method long-context-vs-RAG comparative is structurally close to the long-context-versus-retrieval evaluations in the 2024–2026 literature (FILM, Needle-in-a-Haystack, NoLiMa, LongBench, RULER families). This harness differs in scope: it tests one specific architectural variant (pre-projected distillations) against the standard alternatives on a deliberately narrow set of prompts, with the blind judge as the comparator. It is not a general-purpose long-context benchmark. The motivation for separating generation from evaluation is from [Anthropic's harness-design article](https://www.anthropic.com/engineering/writing-tools-for-agents): a separate evaluator with explicit calibration is more tractable than a generator critical of its own work.
