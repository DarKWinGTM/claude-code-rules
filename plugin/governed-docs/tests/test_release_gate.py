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


class ReleaseGateTests(unittest.TestCase):
    def build_finding(self, **kwargs):
        doctrine_finding_type = load_symbol(
            self,
            "governed_docs.finding_models",
            "DoctrineFinding",
        )
        return doctrine_finding_type(**kwargs)

    def build_evaluation(self, findings):
        doctrine_evaluation_type = load_symbol(
            self,
            "governed_docs.finding_models",
            "DoctrineEvaluation",
        )
        return doctrine_evaluation_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            findings=findings,
            mutated=False,
        )

    def test_release_gate_blocks_blocked_findings(self):
        evaluate_release_gate = load_symbol(
            self,
            "governed_docs.release_gate",
            "evaluate_release_gate",
        )

        evaluation = self.build_evaluation([
            self.build_finding(
                subject="todo/history/2026-06-01.md",
                classification="blocked",
                problem_class="preservation-risk",
                reason="Preservation-sensitive surface remains blocked.",
                evidence=["todo/history/2026-06-01.md"],
            )
        ])

        verdict = evaluate_release_gate(evaluation, verification_passed=True)
        self.assertEqual(verdict.verdict, "blocked")

    def test_release_gate_returns_rework_for_drift(self):
        evaluate_release_gate = load_symbol(
            self,
            "governed_docs.release_gate",
            "evaluate_release_gate",
        )

        evaluation = self.build_evaluation([
            self.build_finding(
                subject="Missing expected top-level surface: README.md",
                classification="drift",
                problem_class="structure-drift",
                reason="Required governed surface is missing.",
                evidence=["README.md"],
            )
        ])

        verdict = evaluate_release_gate(evaluation, verification_passed=True)
        self.assertEqual(verdict.verdict, "rework")

    def test_release_gate_returns_pass_with_notes_for_legacy_allowed(self):
        evaluate_release_gate = load_symbol(
            self,
            "governed_docs.release_gate",
            "evaluate_release_gate",
        )

        evaluation = self.build_evaluation([
            self.build_finding(
                subject="phase-001a",
                classification="legacy-but-allowed",
                problem_class="phase-grammar-drift",
                reason="Legacy form remains allowed as historical evidence.",
                evidence=["phase-001a"],
            )
        ])

        verdict = evaluate_release_gate(evaluation, verification_passed=True)
        self.assertEqual(verdict.verdict, "pass-with-notes")

    def test_release_gate_returns_pass_when_verification_and_findings_are_clean(self):
        evaluate_release_gate = load_symbol(
            self,
            "governed_docs.release_gate",
            "evaluate_release_gate",
        )

        evaluation = self.build_evaluation([
            self.build_finding(
                subject="Active governed surface present: TODO.md",
                classification="compliant",
                problem_class=None,
                reason="Governed surface exists in checked scope.",
                evidence=["TODO.md"],
            )
        ])

        verdict = evaluate_release_gate(evaluation, verification_passed=True)
        self.assertEqual(verdict.verdict, "pass")


if __name__ == "__main__":
    unittest.main()
