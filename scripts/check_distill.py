#!/usr/bin/env python3
"""check_distill.py — kalee-model validator (constitution + decision log)

Rules (README §"Why not just a prompt collection"):
  FAIL = structural/contract breakage · WARN = operational health hints

Checks:
  1. schema completeness + unique ids (both files)
  2. identity == operated-self (distill the system-backed self, not raw instinct)
  3. EVERY principle cites >=1 case that actually exists          (the anchor rule)
  4. principles touching a weakness keyword MUST carry compensation (weakness -> process)
  5. enum validity: type / source / sensitivity / status
  6. revisions in reverse-chronological order; outcome implies expectedOutcome (WARN)

Usage: python3 scripts/check_distill.py [data_dir]   (default: <repo>/data)
Exit 1 on any FAIL. WARN does not block — but read them.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data"

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# bilingual on purpose — write your constitution in whatever language you think in
WEAKNESS_KEYS = ["discipline", "inclusi", "empathy", "optimis", "纪律", "包容", "体谅", "乐观"]
TYPES = {"grading", "pricing", "email-final", "email-draft", "strategy", "gate", "other"}
SOURCES = {"hook-confirm", "hook-diff", "manual", "backfill"}
SENS = {"internal", "sanitizable"}

fails, warns = [], []


def fail(m):
    fails.append(m)


def warn(m):
    warns.append(m)


def main():
    model_p, log_p = DATA / "kalee-model.json", DATA / "decision-log.json"
    for p in (model_p, log_p):
        if not p.exists():
            print(f"✘ missing: {p}")
            sys.exit(1)

    model = json.loads(model_p.read_text())
    log = json.loads(log_p.read_text())

    # ---------- constitution ----------
    if not SEMVER.match(model.get("version", "")):
        fail(f"version not semver: {model.get('version')!r}")
    if model.get("identity") != "operated-self":
        fail("identity must be 'operated-self' (distill the system-backed self)")
    if not DATE.match(str(model.get("updatedAt", ""))):
        fail("updatedAt must be YYYY-MM-DD")

    principles = model.get("principles", [])
    pids = [p.get("id") for p in principles]
    if len(pids) != len(set(pids)):
        fail("principle ids not unique")
    for p in principles:
        pid = p.get("id", "?")
        for f in ("text", "applies", "exception", "origin", "caseRefs", "since", "status"):
            if f not in p:
                fail(f"{pid} missing field {f}")
        if p.get("status") not in ("active", "retired"):
            fail(f"{pid} bad status: {p.get('status')!r}")
        blob = "".join(str(p.get(k, "")) for k in ("text", "applies", "exception"))
        hit = [k for k in WEAKNESS_KEYS if k in blob.lower() or k in blob]
        if hit and not p.get("compensation"):
            fail(f"{pid} touches weakness {hit} but has no compensation (weakness ships as process, not willpower)")

    # ---------- decision log ----------
    cases = log.get("cases", [])
    cids = [c.get("id") for c in cases]
    if len(cids) != len(set(cids)):
        fail("case ids not unique")
    cidset = set(cids)
    for c in cases:
        cid = c.get("id", "?")
        for f in ("date", "type", "context", "decision", "reasoning", "source", "sensitivity"):
            if not c.get(f):
                fail(f"{cid} missing field {f}")
        if not DATE.match(str(c.get("date", ""))):
            fail(f"{cid} bad date")
        if c.get("type") not in TYPES:
            fail(f"{cid} bad type: {c.get('type')!r}")
        if c.get("source") not in SOURCES:
            fail(f"{cid} bad source: {c.get('source')!r}")
        if c.get("sensitivity") not in SENS:
            fail(f"{cid} bad sensitivity: {c.get('sensitivity')!r}")
        if c.get("reasoning") == "unknown":
            warn(f"{cid} reasoning=unknown — weekly sweep should ask")
        if c.get("outcome") and not c.get("expectedOutcome"):
            warn(f"{cid} has outcome but no expectedOutcome")

    # ---------- the anchor rule ----------
    for p in principles:
        pid = p.get("id", "?")
        refs = p.get("caseRefs") or []
        if not refs:
            fail(f"{pid} cites no case (every principle needs >=1 real anchor)")
        for r in refs:
            if r not in cidset:
                fail(f"{pid} cites non-existent case: {r}")

    # ---------- revisions ----------
    revs = model.get("revisions", [])
    dates = [r.get("date") for r in revs]
    if dates and dates != sorted(dates, reverse=True):
        warn("revisions not in reverse-chronological order")

    # ---------- health ----------
    if len(cases) < 20:
        warn(f"only {len(cases)} cases (<20 starter baseline)")
    stats = model.get("stats", {})
    if stats.get("casesTotal") != len(cases):
        warn(f"stats.casesTotal={stats.get('casesTotal')} != actual {len(cases)}")

    anchored = {r for p in principles for r in (p.get("caseRefs") or [])}
    orphans = sorted(cidset - anchored)
    print(f"constitution {len(principles)} principles · log {len(cases)} cases · anchored {len(anchored & cidset)}/{len(cids)}")
    for w in warns:
        print(f"⚠ {w}")
    if orphans:
        print(f"ℹ cases not cited by any principle (fine to keep): {', '.join(orphans)}")
    if fails:
        for f_ in fails:
            print(f"✘ {f_}")
        print(f"\nFAIL={len(fails)}  WARN={len(warns)}  → NOT passing")
        sys.exit(1)
    print(f"\nFAIL=0  WARN={len(warns)}  → passing")


if __name__ == "__main__":
    main()
