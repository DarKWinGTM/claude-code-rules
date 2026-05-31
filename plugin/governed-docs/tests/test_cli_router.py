import importlib
import sys
import tempfile
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


def write_file(path: Path, content: str = "test"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class CliRouterTests(unittest.TestCase):
    def test_dispatch_scan_routes_to_scan_command(self):
        dispatch_command = load_symbol(self, "governed_docs.cli", "dispatch_command")

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "TODO.md")
            exit_code, output, is_error = dispatch_command(["scan", str(workspace_root)])

        self.assertEqual(exit_code, 0)
        self.assertFalse(is_error)
        self.assertIn("governed-docs scan report", output)

    def test_dispatch_repair_plan_routes_to_repair_planner(self):
        dispatch_command = load_symbol(self, "governed_docs.cli", "dispatch_command")

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "TODO.md")
            exit_code, output, is_error = dispatch_command(["repair-plan", str(workspace_root)])

        self.assertEqual(exit_code, 0)
        self.assertFalse(is_error)
        self.assertIn("repair plan artifact", output)

    def test_dispatch_present_md_routes_to_article_presentation(self):
        dispatch_command = load_symbol(self, "governed_docs.cli", "dispatch_command")

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "docs" / "guide.md", "# Guide\n\nReadable body.")
            exit_code, output, is_error = dispatch_command(
                ["present-md", str(workspace_root), "docs/guide.md"]
            )

        self.assertEqual(exit_code, 0)
        self.assertFalse(is_error)
        self.assertIn("Article preview generated", output)


if __name__ == "__main__":
    unittest.main()
