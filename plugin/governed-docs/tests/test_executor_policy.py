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


class ExecutorPolicyTests(unittest.TestCase):
    def build_plan_item(self, **kwargs):
        repair_plan_item_type = load_symbol(
            self,
            "governed_docs.generated_artifacts",
            "RepairPlanItem",
        )
        return repair_plan_item_type(**kwargs)

    def test_bounded_normalize_candidate_enters_auto_normalize_mode(self):
        decide_execution = load_symbol(
            self,
            "governed_docs.executor_policy",
            "decide_execution",
        )

        item = self.build_plan_item(
            subject="design/design.md backlink sync",
            classification="safe-auto-repair",
            problem_class="structure-drift",
            recommended_action="bounded-normalize-candidate",
            approval_boundary="policy-check",
            evidence=["design/design.md backlink sync"],
            preservation_notes=["Candidate remains reviewable and subject to executor policy before any mutation."],
        )

        decision = decide_execution(item)
        self.assertEqual(decision.mode, "bounded-auto-normalize")
        self.assertTrue(decision.allowed)

    def test_blocked_item_stays_blocked(self):
        decide_execution = load_symbol(
            self,
            "governed_docs.executor_policy",
            "decide_execution",
        )

        item = self.build_plan_item(
            subject="todo/history/2026-06-01.md",
            classification="blocked",
            problem_class="preservation-risk",
            recommended_action="block-closeout",
            approval_boundary="manual-resolution",
            evidence=["todo/history/2026-06-01.md"],
            preservation_notes=["Blocked findings must not auto-progress into normalization or closeout."],
        )

        decision = decide_execution(item)
        self.assertEqual(decision.mode, "blocked")
        self.assertFalse(decision.allowed)


if __name__ == "__main__":
    unittest.main()
