import importlib
import sys
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PLUGIN_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def load_symbol(case: unittest.TestCase, module_name: str, symbol_name: str):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        case.fail(f"expected module '{module_name}' to exist: {exc}")

    if not hasattr(module, symbol_name):
        case.fail(f"expected symbol '{symbol_name}' in module '{module_name}'")

    return getattr(module, symbol_name)


class DoctrineEvaluatorTests(unittest.TestCase):
    def test_missing_expected_top_level_surface_becomes_structure_drift(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=["README.md"],
            skipped_surfaces=[],
            scanner_warnings=[],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        self.assertEqual(len(evaluation.findings), 1)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "drift")
        self.assertEqual(finding.problem_class, "structure-drift")
        self.assertIn("README.md", finding.subject)

    def test_active_authority_surface_becomes_compliant(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        discovered_surface_type = load_symbol(
            self,
            "governed_docs.scan_result",
            "DiscoveredSurface",
        )
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[
                discovered_surface_type(
                    path=Path("/tmp/governed-docs/TODO.md"),
                    relative_path="TODO.md",
                    surface_family="todo",
                    inventory_class="active authority surface",
                )
            ],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=[],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "compliant")
        self.assertIsNone(finding.problem_class)
        self.assertIn("TODO.md", finding.subject)

    def test_legacy_phase_identifier_warning_becomes_legacy_but_allowed(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["legacy-phase-identifier:phase-001a"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "legacy-but-allowed")
        self.assertEqual(finding.problem_class, "phase-grammar-drift")
        self.assertIn("phase-001a", finding.subject)

    def test_ambiguous_authority_warning_becomes_needs_basis(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["ambiguous-authority:README.md"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "ambiguous-needs-basis")
        self.assertEqual(finding.problem_class, "role-drift")
        self.assertIn("README.md", finding.subject)

    def test_safe_auto_repair_warning_is_marked_explicitly(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["safe-auto-repair:design/design.md backlink sync"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "safe-auto-repair")
        self.assertEqual(finding.problem_class, "structure-drift")
        self.assertIn("backlink sync", finding.subject)

    def test_blocked_preservation_risk_warning_stays_blocked(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["blocked-preservation-risk:todo/history/2026-06-01.md"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "blocked")
        self.assertEqual(finding.problem_class, "preservation-risk")
        self.assertIn("todo/history/2026-06-01.md", finding.subject)

    def test_rollover_pressure_warning_maps_to_rollover_pressure(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["rollover-pressure:TODO.md"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "drift")
        self.assertEqual(finding.problem_class, "rollover-pressure")
        self.assertIn("TODO.md", finding.subject)

    def test_release_sync_warning_maps_to_release_sync_drift(self):
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")
        evaluate_scan_result = load_symbol(
            self,
            "governed_docs.doctrine_evaluator",
            "evaluate_scan_result",
        )

        scan_result = scan_result_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            discovered_surfaces=[],
            missing_expected_top_level_surfaces=[],
            skipped_surfaces=[],
            scanner_warnings=["release-sync-drift:README.md vs changelog/changelog.md"],
            mutated=False,
        )

        evaluation = evaluate_scan_result(scan_result)
        finding = evaluation.findings[0]
        self.assertEqual(finding.classification, "drift")
        self.assertEqual(finding.problem_class, "release-sync-drift")
        self.assertIn("README.md", finding.subject)


if __name__ == "__main__":
    unittest.main()
