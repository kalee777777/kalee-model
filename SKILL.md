---
name: kalee-model
description: Judgment OS grounded in your principles and decision log. Use for business-draft review, strategy analysis, direction tradeoffs, project planning, outcome review, case recall and negotiation practice; also mirror / final-draft / log-a-decision / ask-my-past-self / spar. Compare alternatives and counterarguments, turn selected directions into verifiable work, and learn from actual outcomes. Not for generic knowledge questions or simple task lists without a judgment component. Disclose gaps in relevant case coverage.
metadata:
  version: "1.2.0"
---

# kalee-model — Judgment OS

Distill your judgment into versioned artifacts, then let agents run it. Origin repo ships two JSON truth sources:

| File | Holds |
|---|---|
| `data/kalee-model.json` | constitution (principles with case anchors + compensation) · rubrics · revisions · stats |
| `data/decision-log.json` | decision traces: situation / options / decision / **reasoning** / expected signal / outcome |

Validator: `python3 scripts/check_distill.py` — FAIL must be 0 after touching either file.

## Choose the mode

Read the current constitution and relevant cases first, then load only the reference needed for the request. Counts and ratification status come from the current data, not a fixed number in this document.

| Request | Deliverable | Read |
|---|---|---|
| Strategy analysis / compare directions | Options, tradeoffs, strongest objection, reversal conditions, minimum experiment | [strategy.md](references/strategy.md) |
| Project planning / execute a selected direction | Charter, work packages, dependencies, acceptance criteria and task-system mapping | [project-planning.md](references/project-planning.md) |
| Outcome review / strategic retrospective | Expected versus observed results, update of the original case | [outcome-review.md](references/outcome-review.md) |
| Mirror / final-draft / recall / spar | Existing business review, capture and rehearsal workflows | Relevant sections below |

The new modes are trial playbooks, not automatically ratified principles or a claim of predictive accuracy. Distinguish user statements, agent proposals, approved choices and observed outcomes. Use cases within their applicable domains and disclose evidence gaps. Domain research and task execution use the user's available tools; this repository does not ship a scheduler or service integration.

The existing human-decision boundaries remain. Continue actions already authorized; an analysis, plan or simulation does not itself authorize new spending, external messages or commitments.

## Business and capture verbs

### 1. `mirror` — pre-send review
Before anything outbound: check the draft against the constitution + style pack and output a **divergence report** (not a rewrite). Log each completed draft-version review to revisions (`type: mirror`), including reviews with no divergence; include an artifact/version pointer and deduplicate retries. Increment `stats.mirrorChecks` once per real review, never for simulations. Leave disagreement rate unknown without a complete denominator. ⚠️ On the five red-line judgment types (customer sends / price numbers / commitments / judgments about people / new-market entry) the mirror **advises only — the human decides**.

### 2. `final-draft` — capture the judgment trace
When the user finalizes a draft: diff final vs agent draft, annotate the edit intent, log it (`type: email-final`, `source: hook-diff`). Store diff summary + file pointers, never full text in the log.

### 3. `log-a-decision` — three questions, ≤30s
Any judgment point (grading / pricing / commitment / strategy / kill-decision) gets logged before the session ends: ① why this option ② what else was on the table ③ what signal proves it right. Refusal → `reasoning: "unknown"` (weekly sweep asks later; never block, never nag).

### 4. `ask-my-past-self` — case retrieval
Before negotiations/decisions: search the decision log by type/tag/keyword and surface the closest cases with their reasoning and outcomes.

### 5. `spar <counterpart> [standard/savage/tricky]` — negotiation sandbox
Red-team agent plays the counterpart (driven by your profile notes on them: fears / angle / decision weight), blue side answers **only by citing a principle + a logged case**. Three rounds → report card (violations / hardest attacks / ammo hit-rate) → the human writes their own version; the diff is the training. Savage lines never leave the session. Protocol: [references/sparring.md](references/sparring.md).

## Weekly sweep (backstop)

Scan `reasoning: "unknown"` entries + any confirmed actions missing a log entry → batch-ask ≤5 items, once. Watch case additions, mirror checks and disagreement rate alongside actual usage. Flat counts may mean no use or a broken capture hook; inspect evidence before diagnosing. Review due project checkpoints in the existing task system; this protocol does not create background jobs.

## Revision discipline

Anyone (you or an agent) may **propose** changes → revisions entry (`ratify / mirror / decision / manual / product`) → weekly batch → human approves or rejects. Add-only: principles are `retired`, never deleted. Any principle touching a known personal weakness **must** carry a `compensation` field — weakness is covered by process, not willpower. The validator enforces both.

## references

- [principles.md](references/principles.md) — a real 30-principle constitution (sanitized) as your drafting scaffold
- [rubrics.md](references/rubrics.md) — business judgment domains plus strategy, project planning and outcome-review trial modes
- [style-pack.md](references/style-pack.md) — style rules + exemplar slot system
- [sparring.md](references/sparring.md) — red/blue sparring protocol
- [quarterly-review.md](references/quarterly-review.md) — quarterly model review + fine-tune option checklist
