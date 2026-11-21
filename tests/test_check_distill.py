#!/usr/bin/env python3
"""Tests for scripts/check_distill.py — the kalee-model validator.

Zero-dependency (stdlib only): builds minimal valid fixtures in temp dirs,
mutates one aspect per test, and asserts the validator's exit code and
message. Run from the repo root:

    python3 -m unittest discover -s tests -v
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_distill.py"
TEMPLATES = ROOT / "templates"


def run_validator(data_dir):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(data_dir)],
        capture_output=True, text=True,
    )


class Fixture:
    """Minimal valid model + log; mutate via set/remove then write to a temp dir."""

    MODEL = {
        "version": "1.0.0",
        "updatedAt": "2026-01-01",
        "identity": "operated-self",
        "principles": [{
            "id": "P01",
            "text": "Charge for value, not for hours",
            "applies": "any pricing decision",
            "exception": "internal experiments",
            "origin": "case",
            "caseRefs": ["c1"],
            "compensation": None,
            "since": "1.0.0",
            "status": "active",
        }],
        "revisions": [],
        "stats": {"casesTotal": 1},
    }

    CASE = {
        "id": "c1",
        "date": "2026-01-01",
        "type": "pricing",
        "context": "A repeat buyer pushed for last year's price on a larger order",
        "decision": "Held the new price, offered a volume tier instead",
        "reasoning": "Cost floor moved; the tier keeps the deal without resetting the anchor",
        "source": "manual",
        "sensitivity": "internal",
    }

    def __init__(self):
        self.model = json.loads(json.dumps(self.MODEL))
        self.cases = [json.loads(json.dumps(self.CASE))]

    def set_model(self, key, value):
        self.model[key] = value

    def set_principle(self, key, value):
        self.model["principles"][0][key] = value

    def set_case(self, key, value):
        self.cases[0][key] = value

    def write(self):
        tmp = tempfile.mkdtemp(prefix="km-test-")
        Path(tmp, "kalee-model.json").write_text(json.dumps(self.model, ensure_ascii=False))
        Path(tmp, "decision-log.json").write_text(json.dumps({"cases": self.cases}, ensure_ascii=False))
        return tmp


class TestShipShape(unittest.TestCase):
    """The starter templates themselves must pass (README quick-start promise)."""

    def test_templates_pass(self):
        tmp = tempfile.mkdtemp(prefix="km-tpl-")
        Path(tmp, "kalee-model.json").write_text(TEMPLATES.joinpath("kalee-model.template.json").read_text())
        Path(tmp, "decision-log.json").write_text(TEMPLATES.joinpath("decision-log.template.json").read_text())
        r = run_validator(tmp)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("FAIL=0", r.stdout)
        self.assertIn("passing", r.stdout)

    def test_missing_files_exit_1(self):
        r = run_validator(tempfile.mkdtemp(prefix="km-empty-"))
        self.assertEqual(r.returncode, 1)
        self.assertIn("missing", r.stdout)


class TestConstitutionContract(unittest.TestCase):
    def _fail_contains(self, fx, needle):
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(needle, r.stdout)

    def test_version_must_be_semver(self):
        fx = Fixture(); fx.set_model("version", "1.2")
        self._fail_contains(fx, "version not semver")

    def test_identity_must_be_operated_self(self):
        fx = Fixture(); fx.set_model("identity", "raw-instinct")
        self._fail_contains(fx, "identity must be 'operated-self'")

    def test_updatedat_must_be_iso_date(self):
        fx = Fixture(); fx.set_model("updatedAt", "01/02/2026")
        self._fail_contains(fx, "updatedAt must be YYYY-MM-DD")

    def test_principle_ids_must_be_unique(self):
        fx = Fixture()
        dup = json.loads(json.dumps(fx.model["principles"][0]))
        fx.model["principles"].append(dup)
        self._fail_contains(fx, "principle ids not unique")

    def test_principle_missing_field(self):
        fx = Fixture()
        del fx.model["principles"][0]["applies"]
        self._fail_contains(fx, "P01 missing field applies")

    def test_principle_bad_status(self):
        fx = Fixture(); fx.set_principle("status", "paused")
        self._fail_contains(fx, "P01 bad status")

    def test_weakness_without_compensation_fails_en(self):
        fx = Fixture()
        fx.set_principle("applies", "anything requiring discipline")
        self._fail_contains(fx, "touches weakness")

    def test_weakness_without_compensation_fails_zh(self):
        fx = Fixture()
        fx.set_principle("text", "涉及长期关系体谅的原则")
        self._fail_contains(fx, "touches weakness")

    def test_weakness_with_compensation_passes(self):
        fx = Fixture()
        fx.set_principle("applies", "anything requiring discipline")
        fx.set_principle("compensation", "forced review-step checklist before send")
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("touches weakness", r.stdout)


class TestDecisionLogContract(unittest.TestCase):
    def _fail_contains(self, fx, needle):
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(needle, r.stdout)

    def test_case_ids_must_be_unique(self):
        fx = Fixture()
        dup = json.loads(json.dumps(fx.cases[0]))
        fx.cases.append(dup)
        self._fail_contains(fx, "case ids not unique")

    def test_case_missing_field(self):
        fx = Fixture()
        del fx.cases[0]["context"]
        self._fail_contains(fx, "c1 missing field context")

    def test_case_bad_date(self):
        fx = Fixture(); fx.set_case("date", "2026-1-1")
        self._fail_contains(fx, "c1 bad date")

    def test_case_bad_type(self):
        fx = Fixture(); fx.set_case("type", "vibes")
        self._fail_contains(fx, "c1 bad type")

    def test_case_bad_source(self):
        fx = Fixture(); fx.set_case("source", "guessed")
        self._fail_contains(fx, "c1 bad source")

    def test_case_bad_sensitivity(self):
        fx = Fixture(); fx.set_case("sensitivity", "public")
        self._fail_contains(fx, "c1 bad sensitivity")


class TestAnchorRule(unittest.TestCase):
    """The load-bearing check: principles must cite real, existing decisions."""

    def test_principle_with_no_case_refs_fails(self):
        fx = Fixture(); fx.set_principle("caseRefs", [])
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("P01 cites no case", r.stdout)

    def test_principle_citing_ghost_case_fails(self):
        fx = Fixture(); fx.set_principle("caseRefs", ["c404"])
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("P01 cites non-existent case: c404", r.stdout)

    def test_valid_anchor_passes(self):
        r = run_validator(Fixture().write())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("anchored 1/1", r.stdout)

    def test_orphan_case_is_info_not_failure(self):
        fx = Fixture()
        fx.cases.append({**json.loads(json.dumps(Fixture.CASE)), "id": "c2"})
        fx.set_model("stats", {"casesTotal": 2})
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("cases not cited by any principle", r.stdout)


class TestWarningsDoNotBlock(unittest.TestCase):
    def _warn_in(self, fx, needle):
        r = run_validator(fx.write())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn(needle, r.stdout)

    def test_reasoning_unknown_warns(self):
        fx = Fixture(); fx.set_case("reasoning", "unknown")
        self._warn_in(fx, "weekly sweep")

    def test_outcome_without_expected_warns(self):
        fx = Fixture(); fx.set_case("outcome", "deal closed at held price")
        self._warn_in(fx, "no expectedOutcome")

    def test_revisions_order_warns(self):
        fx = Fixture()
        fx.set_model("revisions", [
            {"date": "2026-01-01", "type": "manual"},
            {"date": "2026-02-01", "type": "manual"},
        ])
        self._warn_in(fx, "reverse-chronological")

    def test_stats_mismatch_warns(self):
        fx = Fixture(); fx.set_model("stats", {"casesTotal": 99})
        self._warn_in(fx, "stats.casesTotal=99")

    def test_fewer_than_20_cases_warns(self):
        self._warn_in(Fixture(), "<20 starter baseline")


if __name__ == "__main__":
    unittest.main()
