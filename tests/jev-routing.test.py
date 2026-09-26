"""Offline tests of coverage preservation and eval bookkeeping; no model calls."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("jev_routing", ROOT / "docs/evals/harness/jev_routing.py")
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = Path(self.tmp.name)
        self.write("slug-table.json", {"slugs": {"000": "alpha", "001": "beta"}})
        self.write("concept-index.json", {"concepts": {
            "rare": {"name": "Rare", "aliases": ["unusual"], "sources": [
                {"id": "000", "context": "qualified context"}, {"id": "001"}]}}})
        self.write("distillations/decision-making/task-index.json", {"sections": [
            {"section": "Framing", "rows": [["Act", "001", "When needed"]]}]})
        for slug in ["alpha", "beta"]:
            p = self.app / f"distillations/decision-making/{slug}-decision-making.md"
            p.write_text("# " + slug)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, data):
        pilot.write_json(self.app / name, data)

    def test_all_sources_and_associations_survive(self):
        rs = pilot.records(self.app)
        self.assertEqual([r["id"] for r in rs], ["000", "001"])
        self.assertEqual(sum(len(r["concepts"]) for r in rs), 2)
        self.assertEqual(sum(len(r["situations"]) for r in rs), 1)
        self.assertEqual(rs[0]["concepts"][0]["context"], "qualified context")

    def test_compact_schema_preserves_context(self):
        self.write("concept-index.json", {"concepts": [
            ["rare", "Rare", ["unusual"], ["000", "001"], {"001": "specific"}]]})
        rs = pilot.records(self.app)
        self.assertEqual(rs[1]["concepts"][0]["context"], "specific")
        self.assertEqual(rs[0]["concepts"][0]["aliases"], ["unusual"])

    def test_missing_evidence_fails_instead_of_silent_drop(self):
        (self.app / "distillations/decision-making/beta-decision-making.md").unlink()
        with self.assertRaisesRegex(ValueError, "absent distillation"):
            pilot.records(self.app)

    def test_uncatalogued_distillation_fails_instead_of_disappearing(self):
        (self.app / "distillations/decision-making/orphan-decision-making.md").write_text("# Orphan")
        with self.assertRaisesRegex(ValueError, "catalogue disagree"):
            pilot.records(self.app)

    def test_pagination_preserves_every_row_once(self):
        record = {"id": "000", "slug": "alpha", "concepts": [
            {"text": str(i) + "é" * 40} for i in range(30)], "situations": []}
        with patch.object(pilot, "MAX_STATE_BYTES", 400):
            pieces = list(pilot.states("query", record))
        self.assertGreater(len(pieces), 1)
        rows = [r["concept"] for p in pieces for r in p["routing_rows"]]
        self.assertEqual(rows, record["concepts"])
        self.assertTrue(all(len(json.dumps(p, ensure_ascii=False).encode()) <= 400 for p in pieces))

    def test_oversized_row_fails_loudly(self):
        record = {"id": "000", "slug": "alpha", "concepts": [{"text": "x" * 30000}], "situations": []}
        with self.assertRaisesRegex(ValueError, "exceeds"):
            list(pilot.states("q", record))

    def test_jev_uses_all_sources_not_top_k(self):
        def fake(payload, key):
            return {"model": pilot.JEV_MODEL, "answers": {"relevant": {"noul": 0.4}},
                    "usage": {"input_tokens": 10}}
        with patch.object(pilot, "jev_request", side_effect=fake) as call:
            result = pilot.route(self.app, "q", self.app / "receipts", "not-a-real-key")
        self.assertEqual(call.call_count, 2)
        self.assertEqual(len(result["selected_paths"]), 2)
        self.assertEqual(result["input_tokens"], 20)
        self.assertEqual(sum(r["rows_evaluated"] for r in result["sources"]), 3)

    def test_empty_selection_requires_fallback(self):
        response = {"model": pilot.JEV_MODEL, "answers": {"relevant": {"noul": 0.1}},
                    "usage": {"input_tokens": 10}}
        with patch.object(pilot, "jev_request", return_value=response):
            result = pilot.route(self.app, "q", self.app / "receipts", "not-a-real-key")
        self.assertTrue(result["empty_shortlist_requires_full_catalogue_fallback"])
        self.assertEqual(result["selected_paths"], [])

    def test_cached_receipt_cannot_mask_changed_question(self):
        response = {"model": pilot.JEV_MODEL, "answers": {"relevant": {"noul": 0.5}},
                    "usage": {"input_tokens": 10}}
        with patch.object(pilot, "jev_request", return_value=response) as call:
            pilot.route(self.app, "q", self.app / "receipts", "not-a-real-key")
            pilot.route(self.app, "q", self.app / "receipts", "not-a-real-key")
            self.assertEqual(call.call_count, 2)
            with self.assertRaisesRegex(ValueError, "Request changed"):
                pilot.route(self.app, "changed", self.app / "receipts", "not-a-real-key")

    def test_credential_file_is_data_not_shell(self):
        p = self.app / "env"
        p.write_text("export TYPESAFE_API_KEY='literal$(not-executed)'\n")
        self.assertEqual(pilot.load_key(p), "literal$(not-executed)")

    def test_current_only_report_does_not_claim_a_comparison(self):
        self.write("gold-anchors.json", {"q01": []})
        self.write("runs/q01/repeat-1/current/execution.json", {
            "status": "complete", "elapsed_seconds": 2, "usage": {"input_tokens": 50}, "commands": []})
        with patch.object(pilot, "check_snapshot", return_value={}):
            pilot.report(self.app)
        self.assertIn("No Jev-versus-current result exists yet", (self.app / "REPORT.md").read_text())
        summary = pilot.read_json(self.app / "summary.json")
        self.assertIsNone(summary[0]["shortlist_anchor_hits"])


if __name__ == "__main__":
    unittest.main()
