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


class GeneratedArtifactsTests(unittest.TestCase):
    def test_repair_plan_artifact_contains_checked_scope_and_actions(self):
        repair_plan_item_type = load_symbol(
            self,
            "governed_docs.generated_artifacts",
            "RepairPlanItem",
        )
        repair_plan_type = load_symbol(
            self,
            "governed_docs.generated_artifacts",
            "RepairPlan",
        )
        build_repair_plan_artifact = load_symbol(
            self,
            "governed_docs.generated_artifacts",
            "build_repair_plan_artifact",
        )

        repair_plan = repair_plan_type(
            target_workspace_path=Path("/tmp/governed-docs"),
            checked_scope="/tmp/governed-docs",
            items=[
                repair_plan_item_type(
                    subject="Missing expected top-level surface: README.md",
                    classification="drift",
                    problem_class="structure-drift",
                    recommended_action="open-repair-patch",
                    approval_boundary="review-required",
                    preservation_notes=["Repair should stay reviewable before any mutation."],
                )
            ],
            mutated=False,
        )

        artifact = build_repair_plan_artifact(repair_plan)
        self.assertIn("Checked scope: /tmp/governed-docs", artifact)
        self.assertIn("open-repair-patch", artifact)
        self.assertIn("review-required", artifact)
        self.assertIn("Repair should stay reviewable before any mutation.", artifact)


if __name__ == "__main__":
    unittest.main()
