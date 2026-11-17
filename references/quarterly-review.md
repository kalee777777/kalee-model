# Quarterly review + fine-tune option

## Quarterly model review (first week of each quarter)

The agent preps six artifacts (all auto-derived; you show up to judge):

| # | Artifact | Source | What to look at |
|---|---|---|---|
| 1 | Disagreement-rate trend + top-5 mirror divergences | revisions (`type: mirror`) + stats | a spike = model stale *or* you drifted — both need handling |
| 2 | Constitution change queue | pending revision proposals | approve / reject each |
| 3 | Log health | validator output + weekly deltas | <5/wk for 4 weeks = capture hook died |
| 4 | Principle hit-rates | how often each P__ got cited | zero-hit principles are retirement candidates (retired, never deleted) |
| 5 | Style-pack swaps | mirror style diffs + your feedback | ±2 slots per quarter |
| 6 | Product-side question quality | if you expose an ask-yourself tool to users | blind-spot list → next case-sprint theme |

Output: constitution version bump (ratify) + next quarter's case-sprint theme + style-pack version.

## Fine-tuning a small model — the option checklist

**Trigger line: ≥300 logged cases, ≥50% with real reasoning and reviewed outcomes.** Below that, "big model + constitution injection" wins — that's not a compromise, it's the correct architecture (the retrieval can say "no coverage"; a fine-tune will hallucinate a judgment).

When triggered, five questions (any "no" = keep shelving):

1. **Data spec**: do the cases form situation→judgment→reasoning triples that survive sanitization?
2. **Uplift**: how far does injection trail a fine-tune in blind tests? <15% isn't worth the ops
3. **Volume**: are call rates high enough that injection latency/cost is a bottleneck at all?
4. **Failure cost**: a wrong fine-tuned judgment given confidently (to you or a customer) vs retrieval honestly returning "no coverage" — asymmetric, favors injection
5. **Ops**: who runs training/eval/rollback — no automated eval set, no project

Default posture (v1.0): injection in production, fine-tune is a dormant option — revisit only on a 10× volume change.
