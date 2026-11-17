---
name: kalee-model
description: Judgment OS — distills how YOU decide into a constitution + decision log, and runs four verbs with any agent: mirror (pre-send review against your principles), deputy (pre-judgment on low-stakes calls), recall (case retrieval — "how did I play this last time"), sparring (red-team your next negotiation). Use whenever the user says mirror / final-draft / log-a-decision / ask-my-past-self / spar, or a judgment point (grading / pricing / commitment / strategy) occurs in session and must be captured. NOT for generic prompt libraries — this only works on your own logged decisions.
version: "1.0.0"
---

# kalee-model — Judgment OS

Distill your judgment into versioned artifacts, then let agents run it. Origin repo ships two JSON truth sources:

| File | Holds |
|---|---|
| `data/kalee-model.json` | constitution (principles with case anchors + compensation) · rubrics · revisions · stats |
| `data/decision-log.json` | decision traces: situation / options / decision / **reasoning** / expected signal / outcome |

Validator: `python3 scripts/check_distill.py` — FAIL must be 0 after touching either file.

## The four verbs

### 1. `mirror` — pre-send review
Before anything outbound: check the draft against the constitution + style pack and output a **divergence report** (not a rewrite). Log disagreements to revisions (`type: mirror`). ⚠️ On the five red-line judgment types (customer sends / price numbers / commitments / judgments about people / new-market entry) the mirror **advises only — the human decides**.

### 2. `final-draft` — capture the judgment trace
When the user finalizes a draft: diff final vs agent draft, annotate the edit intent, log it (`type: email-final`, `source: hook-diff`). Store diff summary + file pointers, never full text in the log.

### 3. `log-a-decision` — three questions, ≤30s
Any judgment point (grading / pricing / commitment / strategy / kill-decision) gets logged before the session ends: ① why this option ② what else was on the table ③ what signal proves it right. Refusal → `reasoning: "unknown"` (weekly sweep asks later; never block, never nag).

### 4. `ask-my-past-self` — case retrieval
Before negotiations/decisions: search the decision log by type/tag/keyword and surface the closest cases with their reasoning and outcomes.

### 5. `spar <counterpart> [standard/savage/tricky]` — negotiation sandbox
Red-team agent plays the counterpart (driven by your profile notes on them: fears / angle / decision weight), blue side answers **only by citing a principle + a logged case**. Three rounds → report card (violations / hardest attacks / ammo hit-rate) → the human writes their own version; the diff is the training. Savage lines never leave the session. Protocol: [references/sparring.md](references/sparring.md).

## Weekly sweep (backstop)

Scan `reasoning: "unknown"` entries + any confirmed actions missing a log entry → batch-ask ≤5 items, once. Watch weekly deltas: cases added (healthy ≥5/wk), mirror checks, disagreement rate. Two flat weeks = capture hook has silently died — fix the protocol wiring.

## Revision discipline

Anyone (you or an agent) may **propose** changes → revisions entry (`ratify / mirror / decision / manual / product`) → weekly batch → human approves or rejects. Add-only: principles are `retired`, never deleted. Any principle touching a known personal weakness **must** carry a `compensation` field — weakness is covered by process, not willpower. The validator enforces both.

## references

- [principles.md](references/principles.md) — a real 30-principle constitution (sanitized) as your drafting scaffold
- [rubrics.md](references/rubrics.md) — judgment handbook: grading / triage / pricing / style / timing
- [style-pack.md](references/style-pack.md) — style rules + exemplar slot system
- [sparring.md](references/sparring.md) — red/blue sparring protocol
- [quarterly-review.md](references/quarterly-review.md) — quarterly model review + fine-tune option checklist
