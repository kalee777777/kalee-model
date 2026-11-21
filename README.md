# kalee-model

[![M8ven Score](https://m8ven.ai/badge/mcp/kalee777777/kalee-model)](https://m8ven.ai/mcp/kalee777777/kalee-model?s=readme)

**Turn your judgment into a versioned operating system your AI agents can run.**

> **What this is / is not:** kalee-model is a *file-based agent skill* — `SKILL.md`, JSON contracts and one validator script. It is **not a networked MCP server**: there is no server runtime, no network calls and no secrets handling. It runs *inside* any MCP-capable coding agent (Claude Code / Cursor / Trae / ZCode) by reading files from your repo. See [CHANGELOG.md](CHANGELOG.md) for release history.

You already trust your gut on the calls that matter — pricing, hiring, walk-away. The problem: judgment lives in one head, evaporates under a busy week, and every AI assistant you hire starts from zero. kalee-model distills *how you decide* into three versioned artifacts — a **constitution**, a **decision log**, a **style pack** — plus agent workflows that use them:

```
mirror    →  pre-send review of anything outbound, against your own principles
deputy    →  pre-judgment on low-stakes calls (grading, triage) — you review disagreements only
recall    →  "how did I play this last time?" — retrieval over your logged decisions
sparring  →  red-team your next negotiation before you walk in
strategy  →  compare directions, tradeoffs, counterarguments and minimum experiments
plan      →  turn a selected direction into work packages with acceptance evidence
review    →  compare expected and actual outcomes, then update the original decision
```

Originated in a B2B industrial-export workflow. This public repository contains a sanitized principle scaffold, generic starter templates and playbooks; private decisions, customer records and project plans are not included. The strategy and project modes are trial protocols whose value should be checked against your own real outcomes.

---

## Why not just a prompt collection?

| | Prompt packs / personal wikis | kalee-model |
|---|---|---|
| Honesty | vibes, plausibility | **every principle must cite ≥1 logged case** — the validator fails otherwise |
| Weaknesses | ignored | **compensation field is mandatory** — a known weakness must ship with a process that covers it, not willpower |
| Agent safety | hope | **"mirror never masters" red lines** — five judgment types the model may advise on but never decide |
| Drift | quietly rots | weekly freshness check + versioned revisions (ratify / mirror / decision / manual / product) |
| Reuse | copy-paste | drop-in `SKILL.md`, business and strategy workflows, any agent that can read your files |

The core trick is the **anchor rule**: a principle that cannot point to a real decision you actually made — with the options you actually faced — is an opinion, not a principle. The schema enforces it; `check_distill.py` refuses to pass until it holds.

## The five layers

| Layer | Artifact | What it holds |
|---|---|---|
| L1 Constitution | `data/kalee-model.json` → principles | 20–30 first-principles, each with case anchors + compensation notes |
| L2 Rubrics | same file → rubrics | business standards plus strategy / project planning / outcome review, linked to your playbooks |
| L3 Playbooks | your existing SOPs/skills | not rebuilt — referenced |
| L4 Style pack | `references/style-pack.md` slots | how you sound: rules + exemplar slots you fill with your own best drafts |
| L5 Decision log | `data/decision-log.json` | situation / options / decision / **reasoning** / expected signal / outcome |

## Quick start

```bash
git clone https://github.com/kalee777777/kalee-model.git
cd kalee-model
mkdir -p data
cp templates/kalee-model.template.json data/kalee-model.json
cp templates/decision-log.template.json data/decision-log.json
python3 scripts/check_distill.py            # validates schema + anchors (WARN until you fill it)
python3 -m unittest discover -s tests       # run the validator's test suite (no dependencies)
```

1. **Log 10 real decisions first.** After any call you make (grade a lead, pick a price, kill a thread), spend 30 seconds on three questions: *why this option, what else was on the table, what signal would prove it right.* Refuse to answer? Log `reasoning: "unknown"` — a weekly sweep batch-asks them later.
2. **Draft your constitution**, 20–30 principles, each citing ≥1 logged case. Steal the structure from `references/principles.md`; rewrite every line in your own decisions' words.
3. **Wire an agent in.** Drop `SKILL.md` + `references/` into `.agents/skills/kalee-model/` of any repo your agent reads (Cursor rules / Claude CLAUDE.md / Trae — same pattern). Point it at `data/*.json`.
4. **Choose a workflow.** Review a draft, recall precedents, rehearse a negotiation, compare directions, plan a project or review its outcome. Load only the matching reference.
5. **Use your existing task system.** Inspect its actual schema, check for duplicate work and verify writes. This repository supplies the planning protocol, not a task service, scheduler or automatic reminder.

## New in v1.2

- **Strategy analysis:** evidence/inference/unknown labels, credible alternatives, opportunity costs, the strongest objection and conditions that would reverse the recommendation.
- **Project planning:** a charter, resource-aware dependencies, concrete work packages and acceptance evidence; technical completion and business success stay separate.
- **Outcome review:** preserve the original prediction, update the original case by ID and distinguish judgment errors from execution gaps or changed conditions.
- **Honest review metrics:** count actual completed draft-version reviews once; simulations and missing history do not become success statistics.

Examples:

```text
Strategy analysis: should our small consulting team start with training or a paid pilot?
Compare alternatives using our existing assets. Show the strongest objection and a minimum experiment.

Project planning: turn the selected pilot into work packages.
Identify dependencies, unknown capacity, acceptance evidence and decisions I need to make.

Outcome review: compare the pilot with its original assumptions.
Recommend whether to continue, narrow the scope or stop, and update the original decision record.
```

The new rubrics are optional trial playbooks. Existing users can add R06–R08 from `references/rubrics.md` or the model template after checking for conflicting IDs. Do **not** overwrite an existing private `data/` directory with starter templates. Validate your data after any edit.

## The red lines (steal these verbatim)

The model **advises, never decides**, on five judgment types:

1. Anything sent to a customer
2. Price numbers
3. Any commitment
4. Judgments about people
5. New-market entry

And one meta-rule: **the mirror must never become the master.** A distilled self is your *past average* — great for the 80% repeatable calls, blind on the frontier 20%. Divergence between you and the model is a signal to read, not a vote to follow.

## 中文用户

**把你的判断蒸馏成 AI 可执行的操作系统。** 三件资产：判断宪法（20–30 条原则，每条必须挂真实决策案例，校验脚本强制）、决策日志（情境/备选/判断/依据/预期信号，30 秒三问随手落库）、风格包（对外文字的样例槽位）。支持照镜子（按原则审稿）、分身预审、案例检索与谈判陪练。v1.2 新增三种试用模式：战略分析（方向比较、机会成本、最强反对意见、最小验证）、项目规划（资源与依赖、工作包、验收证据、接入已有任务系统）、结果复盘（保留原预期，按原案例 ID 回填实绩）。原有数据无需重建，更新时不要覆盖自己的 data/。适用于任何支持 MCP/可读文件目录的 AI 编码助手（Claude Code / Cursor / Trae / ZCode 等）。配套实战方法论见：[AI 外贸课程体系](https://www.kestrelmetal.com/)（中文，60+ 门外贸 AI 实操课）。

## License

MIT — see [LICENSE](LICENSE).
