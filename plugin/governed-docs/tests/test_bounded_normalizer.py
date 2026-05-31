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


class BoundedNormalizerTests(unittest.TestCase):
    def build_plan_item(self, **kwargs):
        repair_plan_item_type = load_symbol(
            self,
            "governed_docs.generated_artifacts",
            "RepairPlanItem",
        )
        return repair_plan_item_type(**kwargs)

    def test_preview_normalization_blocks_non_allowed_item(self):
        preview_normalization = load_symbol(
            self,
            "governed_docs.normalizer",
            "preview_normalization",
        )
        policy_blocked_error = load_symbol(
            self,
            "governed_docs.normalizer",
            "PolicyBlockedError",
        )

        item = self.build_plan_item(
            subject="Missing expected top-level surface: README.md",
            classification="drift",
            problem_class="structure-drift",
            recommended_action="open-repair-patch",
            approval_boundary="review-required",
            evidence=["README.md"],
            preservation_notes=["Repair should stay reviewable before any mutation."],
        )

        with self.assertRaises(policy_blocked_error):
            preview_normalization(item)

    def test_preview_normalization_allows_safe_candidate(self):
        preview_normalization = load_symbol(
            self,
            "governed_docs.normalizer",
            "preview_normalization",
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

        preview = preview_normalization(item)
        self.assertIn("bounded-auto-normalize", preview)
        self.assertIn("No files were edited.", preview)

    def test_hook_guardrail_message_is_advisory_only(self):
        build_guardrail_message = load_symbol(
            self,
            "governed_docs.hook_guardrails",
            "build_guardrail_message",
        )

        message = build_guardrail_message("closeout")
        self.assertIn("advisory/support-only", message)
        self.assertIn("closeout", message)


if __name__ == "__main__":
    unittest.main()
