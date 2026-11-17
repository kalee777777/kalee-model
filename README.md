# kalee-model

**Turn your judgment into a versioned operating system your AI agents can run.**

You already trust your gut on the calls that matter — pricing, hiring, walk-away. The problem: judgment lives in one head, evaporates under a busy week, and every AI assistant you hire starts from zero. kalee-model distills *how you decide* into three versioned artifacts — a **constitution**, a **decision log**, a **style pack** — plus the four agent verbs that use them:

```
mirror    →  pre-send review of anything outbound, against your own principles
deputy    →  pre-judgment on low-stakes calls (grading, triage) — you review disagreements only
recall    →  "how did I play this last time?" — retrieval over your logged decisions
sparring  →  red-team your next negotiation before you walk in
```

Field-tested on a B2B industrial-export desk: a 30-principle constitution, 46-case decision log, and a 20-exemplar style pack in daily production, wired into MCP-capable coding agents.

---

## Why not just a prompt collection?

| | Prompt packs / personal wikis | kalee-model |
|---|---|---|
| Honesty | vibes, plausibility | **every principle must cite ≥1 logged case** — the validator fails otherwise |
| Weaknesses | ignored | **compensation field is mandatory** — a known weakness must ship with a process that covers it, not willpower |
| Agent safety | hope | **"mirror never masters" red lines** — five judgment types the model may advise on but never decide |
| Drift | quietly rots | weekly freshness check + versioned revisions (ratify / mirror / decision / manual / product) |
| Reuse | copy-paste | four verbs, drop-in `SKILL.md`, any MCP-capable agent (Claude Code, Cursor, Trae, ZCode…) |

The core trick is the **anchor rule**: a principle that cannot point to a real decision you actually made — with the options you actually faced — is an opinion, not a principle. The schema enforces it; `check_distill.py` refuses to pass until it holds.

## The five layers

| Layer | Artifact | What it holds |
|---|---|---|
| L1 Constitution | `data/kalee-model.json` → principles | 20–30 first-principles, each with case anchors + compensation notes |
| L2 Rubrics | same file → rubrics | grading / triage / pricing / style / timing standards, linked to your playbooks |
| L3 Playbooks | your existing SOPs/skills | not rebuilt — referenced |
| L4 Style pack | `references/style-pack.md` slots | how you sound: rules + exemplar slots you fill with your own best drafts |
| L5 Decision log | `data/decision-log.json` | situation / options / decision / **reasoning** / expected signal / outcome |

## Quick start

```bash
git clone https://github.com/kalee777777/kalee-model.git
cd kalee-model
mkdir data
cp templates/kalee-model.template.json data/kalee-model.json
cp templates/decision-log.template.json data/decision-log.json
python3 scripts/check_distill.py            # validates schema + anchors (WARN until you fill it)
```

1. **Log 10 real decisions first.** After any call you make (grade a lead, pick a price, kill a thread), spend 30 seconds on three questions: *why this option, what else was on the table, what signal would prove it right.* Refuse to answer? Log `reasoning: "unknown"` — a weekly sweep batch-asks them later.
2. **Draft your constitution**, 20–30 principles, each citing ≥1 logged case. Steal the structure from `references/principles.md`; rewrite every line in your own decisions' words.
3. **Wire an agent in.** Drop `SKILL.md` + `references/` into `.agents/skills/kalee-model/` of any repo your agent reads (Cursor rules / Claude CLAUDE.md / Trae — same pattern). Point it at `data/*.json`.
4. **Run the four verbs** before your next negotiation: mirror the draft, ask recall for precedents, spar one round, then decide yourself.

## The red lines (steal these verbatim)

The model **advises, never decides**, on five judgment types:

1. Anything sent to a customer
2. Price numbers
3. Any commitment
4. Judgments about people
5. New-market entry

And one meta-rule: **the mirror must never become the master.** A distilled self is your *past average* — great for the 80% repeatable calls, blind on the frontier 20%. Divergence between you and the model is a signal to read, not a vote to follow.

## 中文用户

**把你的判断蒸馏成 AI 可执行的操作系统。** 三件资产：判断宪法（20–30 条原则，每条必须挂真实决策案例，校验脚本强制）、决策日志（情境/备选/判断/依据/预期信号，30 秒三问随手落库）、风格包（对外文字的样例槽位）。四个 agent 动词：照镜子（发出前按自己宪法审稿）、分身（低风险判断预审，只看分歧项）、问过去的我（同类案例弹药）、陪练（红蓝对抗沙盘演练下一场谈判）。适用于任何支持 MCP/可读文件目录的 AI 编码助手（Claude Code / Cursor / Trae / ZCode 等）。配套实战方法论见：[AI 外贸课程体系](https://www.kestrelmetal.com/)（中文，60+ 门外贸 AI 实操课）。

## License

MIT — see [LICENSE](LICENSE).
