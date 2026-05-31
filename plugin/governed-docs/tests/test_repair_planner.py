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


class RepairPlannerTests(unittest.TestCase):
    def build_evaluation(self, finding):
        doctrine_evaluation_type = load_symbol(
            self,
            "governed_docs.finding_models",
            "DoctrineEvaluation",
        )
        return doctrine_evaluation_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            findings=[finding],
            mutated=False,
        )

    def build_finding(self, **kwargs):
        doctrine_finding_type = load_symbol(
            self,
            "governed_docs.finding_models",
            "DoctrineFinding",
        )
        return doctrine_finding_type(**kwargs)

    def test_structure_drift_becomes_open_repair_patch_item(self):
        plan_repairs = load_symbol(
            self,
            "governed_docs.repair_planner",
            "plan_repairs",
        )

        evaluation = self.build_evaluation(
            self.build_finding(
                subject="Missing expected top-level surface: README.md",
                classification="drift",
                problem_class="structure-drift",
                reason="A required governed surface is missing from the checked target path.",
                evidence=["README.md"],
            )
        )

        repair_plan = plan_repairs(evaluation)
        self.assertEqual(len(repair_plan.items), 1)
        item = repair_plan.items[0]
        self.assertEqual(item.recommended_action, "open-repair-patch")
        self.assertEqual(item.approval_boundary, "review-required")
        self.assertIn("README.md", item.subject)

    def test_safe_auto_repair_becomes_bounded_normalize_candidate(self):
        plan_repairs = load_symbol(
            self,
            "governed_docs.repair_planner",
            "plan_repairs",
        )

        evaluation = self.build_evaluation(
            self.build_finding(
                subject="design/design.md backlink sync",
                classification="safe-auto-repair",
                problem_class="structure-drift",
                reason="Deterministic low-risk repair candidate.",
                evidence=["design/design.md backlink sync"],
            )
        )

        repair_plan = plan_repairs(evaluation)
        item = repair_plan.items[0]
        self.assertEqual(item.recommended_action, "bounded-normalize-candidate")
        self.assertEqual(item.approval_boundary, "policy-check")

    def test_blocked_finding_stays_blocked(self):
        plan_repairs = load_symbol(
            self,
            "governed_docs.repair_planner",
            "plan_repairs",
        )

        evaluation = self.build_evaluation(
            self.build_finding(
                subject="todo/history/2026-06-01.md",
                classification="blocked",
                problem_class="preservation-risk",
                reason="Preservation-sensitive surface must remain blocked.",
                evidence=["todo/history/2026-06-01.md"],
            )
        )

        repair_plan = plan_repairs(evaluation)
        item = repair_plan.items[0]
        self.assertEqual(item.recommended_action, "block-closeout")
        self.assertEqual(item.approval_boundary, "manual-resolution")

    def test_ambiguous_finding_requires_basis_before_repair(self):
        plan_repairs = load_symbol(
            self,
            "governed_docs.repair_planner",
            "plan_repairs",
        )

        evaluation = self.build_evaluation(
            self.build_finding(
                subject="README.md",
                classification="ambiguous-needs-basis",
                problem_class="role-drift",
                reason="Authority ownership is ambiguous.",
                evidence=["README.md"],
            )
        )

        repair_plan = plan_repairs(evaluation)
        item = repair_plan.items[0]
        self.assertEqual(item.recommended_action, "ask-for-basis")
        self.assertEqual(item.approval_boundary, "basis-required")


if __name__ == "__main__":
    unittest.main()
