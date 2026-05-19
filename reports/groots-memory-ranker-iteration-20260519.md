# Groots Memory Ranker Iteration - 2026-05-19

## Scope

This iteration focused on Groots memory retrieval quality and benchmark fidelity on the LoCoMo sample-0 `both-wrong` hard set.

The hard set contains 31 questions that were previously missed by either memU, Groots memory, or both. It is intentionally small so Groots memory changes can be tested quickly without repeatedly rerunning the full benchmark.

## Changes Evaluated

- Included LoCoMo visual captions and image queries in Groots source transcripts so the Groots backend receives the same visual facts that memU receives.
- Replaced insertion-order fixture retrieval with the Groots fielded text scorer, so the benchmark exercises the real TypeScript retrieval logic instead of an underpowered test bridge.
- Improved the ranker by removing English chargram noise from query scoring, adding candidate-set IDF weighting, and adding field-length normalization.
- Normalized the extractor's `people_profile` output to Groots' canonical `profile` memory type.
- Kept a negative experiment out of the final Groots code: appending every item evidence string to runtime snippets reduced accuracy from 23/31 to 16/31 by increasing context noise.

## Results

| Run | Store | Accuracy | Single Hop | Multi Hop | Open Domain | Temporal | Time |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Before ranker, visual fresh | fresh | 18/31 (58.1%) | 9/14 | 1/2 | 7/11 | 1/4 | about 6 min |
| Ranker, existing visual store | reused | 23/31 (74.2%) | 12/14 | 2/2 | 6/11 | 3/4 | 49s |
| Ranker, fresh end-to-end | fresh | 22/31 (71.0%) | 10/14 | 2/2 | 8/11 | 2/4 | 358s |

Report artifacts:

- `reports/results/groots-ts-gpt-5.4-mini-s0-both-wrong-v3-ranker-qa-only.md`
- `reports/results/groots-ts-gpt-5.4-mini-s0-both-wrong-v3-ranker-fresh.md`

## Latency

For the best QA-only run, Groots retrieve latency across 31 questions:

- average: 1.829s
- p50: 1.884s
- p95: 2.061s
- max: 2.295s

For the fresh end-to-end run, Groots retrieve latency across 31 questions:

- average: 1.962s
- p50: 1.803s
- p95: 2.632s
- max: 5.059s

Most per-query retrieval time is still the LLM query planner call. The benchmark fixture also pays repeated Bun process startup cost, because each fixture command starts a new TypeScript process.

## Current Gaps

- Cross-session entity attribution is still weak. Example: Caroline's "home country" requires connecting a later "moved from my home country" statement to a separate Sweden-root memory.
- Some source/session questions need sibling evidence from the same session, not only independently ranked items.
- The extractor can still compress away answer-slot details, especially visual details and exact reason phrases.
- Some remaining benchmark misses are answer-synthesis or dataset ambiguity rather than pure memory retrieval failures.

## Next Best Work

- Add a clean source-neighbor expansion API so top items can bring adjacent source facts without dumping all evidence into the context.
- Improve extractor prompts around speaker attribution and first-person ownership.
- Add persistent fixture execution for benchmark speed and lower latency variance.
- Add focused tests for ranker behavior on rare exact terms, common-term noise, and visual answer-slot retrieval.
