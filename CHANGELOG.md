# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project version
lives in `SKILL.md` metadata and `data/kalee-model.json`.

## [Unreleased]

- Added a zero-dependency test suite for the validator (`tests/test_check_distill.py`,
  run with `python3 -m unittest discover -s tests`) covering the constitution
  contract, decision-log contract, the anchor rule and WARN-not-block behavior.
- README: M8ven Trust Index badge, an explicit "what this is / is not" note
  (file-based agent skill, not a networked MCP server) and test instructions.

## [1.2.0] - 2026-11-17

- Strategy analysis mode: evidence/inference/unknown labels, credible
  alternatives, opportunity costs, strongest objection and reversal conditions,
  minimum experiment (`references/strategy.md`).
- Project planning mode: charter, resource-aware dependencies, work packages
  with acceptance evidence; technical completion and business success stay
  separate (`references/project-planning.md`).
- Outcome review mode: preserve the original prediction, update the original
  case by ID, distinguish judgment errors from execution gaps or changed
  conditions (`references/outcome-review.md`).
- Honest review metrics: count real completed draft-version reviews once;
  simulations and missing history do not become success statistics.

## [1.0.0] - 2026-11-17

- Initial public release: constitution / decision-log / style-pack templates,
  `scripts/check_distill.py` validator (anchor rule, compensation rule, enums),
  sanitized 30-principle scaffold, mirror / deputy / recall / sparring
  workflows, MIT license.
