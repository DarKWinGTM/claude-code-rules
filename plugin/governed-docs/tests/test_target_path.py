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


class TargetPathTests(unittest.TestCase):
    def test_missing_target_path_hard_stops(self):
        target_path_error = load_symbol(self, "governed_docs.target_path", "TargetPathError")
        resolve_target_workspace_path = load_symbol(
            self,
            "governed_docs.target_path",
            "resolve_target_workspace_path",
        )

        with self.assertRaises(target_path_error) as context:
            resolve_target_workspace_path(None)

        self.assertIn("explicit target workspace path", str(context.exception))

    def test_nonexistent_target_path_hard_stops(self):
        target_path_error = load_symbol(self, "governed_docs.target_path", "TargetPathError")
        resolve_target_workspace_path = load_symbol(
            self,
            "governed_docs.target_path",
            "resolve_target_workspace_path",
        )

        missing_path = PLUGIN_ROOT / "tests" / "does-not-exist"
        with self.assertRaises(target_path_error) as context:
            resolve_target_workspace_path(missing_path)

        self.assertIn("does not exist", str(context.exception))

    def test_file_target_path_hard_stops(self):
        target_path_error = load_symbol(self, "governed_docs.target_path", "TargetPathError")
        resolve_target_workspace_path = load_symbol(
            self,
            "governed_docs.target_path",
            "resolve_target_workspace_path",
        )

        file_path = PLUGIN_ROOT / "tests" / "test_target_path.py"
        with self.assertRaises(target_path_error) as context:
            resolve_target_workspace_path(file_path)

        self.assertIn("directory", str(context.exception))


if __name__ == "__main__":
    unittest.main()
