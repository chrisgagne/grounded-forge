# Jev-assisted routing pilot

This experiment asks whether Jev can reduce the cost of selecting evidence while
preserving the distinctions the current `answer-from-corpus` skill retrieves.
It changes no production skill, index, distillation or build output.

## Comparison

- **Current:** the existing compiled decision app and its unchanged skill, invoked
  in a fresh Codex CLI session.
- **Jev:** the same app, answering model, effort and output requirements. A routing
  override supplies paths selected by Jev instead of the answering model's initial
  whole-index scan. Classification, lens handling, question decomposition, complete
  distillation reads, synthesis and citation discipline remain with the answering model.

This is a controlled single-turn test of the compiled skill, not a reproduction of
an ongoing desktop conversation. Both arms run without web access, other agents,
other skills or external corpus files. The subject is asked for 250–450 words, or a
shorter honest no-coverage response. The app files are copied unchanged from the
working tree, including uncommitted edits, and hashed before the first subject run.
Do not rebuild the app during the round. Project-mode retrieval and
`advise-from-corpus` are not tested by this pilot.

The answering model is pinned to `gpt-6-astra`, effort `xhigh`, matching the local
Codex configuration inspected on 25 September 2026. Jev is pinned to `jev-1.13.0`.
CLI authentication uses the operator's existing ChatGPT login. The runner does not
extract or copy login credentials. Jev needs `TYPESAFE_API_KEY`, supplied through
the environment or a local environment file; the key is removed from the eval
subject's environment and never included in receipts.

## Routing treatment

The deterministic router builds one record per shipped source, containing every
concept association and every task-index row for that source. No lexical shortlist
precedes Jev. Large records are split at row boundaries; all segments are evaluated.
A UTF-8 byte cap of 24,000 on state leaves room below Jev's state/question limit.
An oversized single row fails explicitly. Source selection uses the maximum
segment relevance probability with a fixed, deliberately inclusive threshold of
0.35; there is no top-k cut-off. This threshold is an uncalibrated pilot hypothesis.

Jev sees only routing metadata and the user's question. It does not grade answers
or rewrite evidence. The generator reads the complete selected distillations. An
empty selection requires the ordinary catalogue route, and incomplete sub-claim
coverage permits the same fallback. Fallback work belongs in total cost and time.
The resulting experiment measures this whole policy, including its recovery path.

API contract and limits: [TypeSafe API](https://docs.typesafe.ai/api),
[model specifications](https://docs.typesafe.ai/models). The price used for the
separately labelled Jev estimate is $0.042 per million input tokens as inspected
on 25 September 2026. Record actual token usage; do not treat this rate as permanent.

## Cases and grading

The versioned [case set](harness/jev-routing-cases.json) contains 20 cases: named
lookups, diagnosis, synthesis, supplied-role lenses, absent coverage and partial
coverage. Four cases (`q01`, `q05`, `q17`, `q19`) are development cases; the other
16 are held out from threshold or prompt tuning. A first run per case is a pilot;
three fresh runs per arm are the planned repeatability check after execution works.
Do not tune against held-out results and then describe them as held out.

Source anchors were chosen before output generation and checked verbatim against
the frozen app. They are non-exhaustive, agent-authored evidence checks, not
human-adjudicated ground truth. Alternative valid evidence is admissible. The
current system is a comparator, not the answer key. No-coverage cases require a
semantic audit, not a score derived from having zero gold anchors.
The cases deliberately probe known source distinctions; they are not a random
sample of production questions. Grounding is checked against the compiled
distillation tier. This does not re-audit those distillations against raw sources.

Record:

- All API requests and responses, selected source paths, file-read command traces,
  complete final answers, model settings and wall-clock timings.
- Jev shortlist inclusion of anchor-bearing files, and anchor text visibly returned
  in tool output. The latter is evidence of exposure, not proof of use or full reads.
- Blinded, fresh-context grading with full evidence files: supported, unsupported
  and contradicted claims; quotation errors; lost distinctions; usefulness; honest
  coverage boundaries. The judge may inspect additional app evidence.
- Codex input, cached-input and output tokens. Its subscription-backed CLI does not
  expose a dollar charge: report this as unavailable, not zero. Jev API cost is
  estimated separately. Timing is cold-session application latency; provider-side
  prompt caching may persist and must be reported through usage counters.

The first judge uses the same model in a fresh context, with arm identities hidden
and the retrieval trace removed from the answer. This is independent context, not
an independent model family. Human review of disagreements and a sample of ties is
required before an adoption decision. Complete supporting evidence is provided;
recognising a citation from training is not a grading criterion.

A cheaper answer that omits needed evidence fails the purpose of the experiment.
Report paired case-level changes and all important failures; avoid declaring
equivalence from a small sample or treating repeated runs as independent questions.

## Commands

From the repository root, using an unused output directory under `_evals/`:

```bash
python3 docs/evals/harness/jev_routing.py prepare --out _evals/jev-routing-YYYY-MM-DD
python3 docs/evals/harness/jev_routing.py run --out _evals/jev-routing-YYYY-MM-DD \
  --ids q01,q05,q17,q19 --env-file /absolute/path/to/private.env
python3 docs/evals/harness/jev_routing.py run --out _evals/jev-routing-YYYY-MM-DD \
  --repeats 3 --env-file /absolute/path/to/private.env
python3 docs/evals/harness/jev_routing.py grade --out _evals/jev-routing-YYYY-MM-DD
python3 docs/evals/harness/jev_routing.py report --out _evals/jev-routing-YYYY-MM-DD
python3 tests/jev-routing.test.py
```

`--arms current` runs only the baseline while Jev access is being configured.
If a repeat is collected one arm at a time this way, its latency comparison is
order-confounded and exploratory. Use subsequent fresh repeats with both arms
enabled for the randomised-order comparison; the runner must not present a staged
baseline as a randomised paired trial. Preserve the cached-token counters.
Completed subject runs and identical Jev requests are resumable; failed subject
runs are retained and require a new run directory. Corpus/case changes invalidate
the frozen round. Do not commit `_evals/` snapshots, transcripts or outputs.
The existing blind-paste harness remains available and unchanged.
