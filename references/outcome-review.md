# Outcome review — trial playbook

Compare a real decision with what happened. Use this for strategic reviews, project milestones and business-result updates. Simulations are practice artifacts, not observed outcomes.

## Preserve the original prediction

Locate the original decision ID, plan, tasks and supporting evidence. Keep the original decision, reasoning and expected outcome intact. Compare each material assumption or expected signal with the observed result and observation date.

Distinguish a mistaken judgment, incomplete execution, changed external conditions and insufficient evidence. Do not invent a causal explanation when the evidence cannot separate them. An exit can be a good outcome; a lucky success does not automatically establish a principle. Report technical delivery and business effect separately.

Recommend continuing, changing or stopping, with reasons and reversal conditions. Execute adjustments already within the user's authorization; identify genuinely new consequential choices for the human.

## Update the existing record

Use the existing schema: `type: strategy` or `gate` where appropriate; concise context, expected outcome, outcome and tags. Keep detailed plans in linked files.

1. Find the original case by ID. Re-read the latest file before editing and preserve unrelated records.
2. Append a dated result and evidence pointer to its `outcome`. Preserve earlier review entries and the original expectations.
3. If a tool only appends cases, do not use it as if it supported updates. Use an available update operation or edit the file directly when authorized.
4. If the review produces a new decision, create a new case that references the original ID in its context. Do not rewrite the old choice to make the prediction appear correct.
5. If no prior expectation exists, say this is a retrospective review without a recorded prediction. Do not fabricate one after the event.
6. Run `python3 scripts/check_distill.py` after editing either truth source. Keep `stats.casesTotal` consistent with the actual log.

Close completed tasks with evidence. Keep result-collection work open if the outcome remains unknown. Use the user's existing review mechanism; this skill does not run a background process by itself.

## Metrics and learning

Count one `mirrorChecks` event per genuinely completed draft-version review, including reviews with no divergence. Record a `type: mirror` revision with the artifact/version pointer and findings, and deduplicate repeated processing of the same version. Do not count project planning, simulations or schema checks as mirror reviews. Leave disagreement rate unknown when its denominator is incomplete; do not reconstruct missing history from memory.

Evaluate evidence quality, testable assumptions, resource feasibility, acceptance criteria and prediction-versus-outcome differences. Adoption rate and case volume are usage measures, not decision accuracy. Propose principle changes through the existing human-ratification process; adopting these modes does not ratify new principles automatically.
