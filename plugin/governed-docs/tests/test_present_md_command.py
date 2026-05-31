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


class PresentMdCommandTests(unittest.TestCase):
    def test_present_md_command_writes_design_preview_index_page(self):
        run_present_md_command = load_symbol(
            self,
            "governed_docs.commands.present_md",
            "run_present_md_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            source_path = workspace_root / "design" / "guide.design.md"
            source_path.parent.mkdir(parents=True, exist_ok=True)
            source_path.write_text("# Guide\n\nReadable body.", encoding="utf-8")

            output = run_present_md_command(workspace_root, "design/guide.design.md")
            expected_output = workspace_root / "preview" / "design" / "guide" / "index.html"

            self.assertTrue(expected_output.exists())
            self.assertIn(str(expected_output), output)

        self.assertIn("Article preview generated", output)

    def test_present_md_command_writes_todo_preview_index_page(self):
        run_present_md_command = load_symbol(
            self,
            "governed_docs.commands.present_md",
            "run_present_md_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            source_path = workspace_root / "TODO.md"
            source_path.write_text("# TODO\n\n- [ ] Example", encoding="utf-8")

            output = run_present_md_command(workspace_root, "TODO.md")
            expected_output = workspace_root / "preview" / "todo" / "index.html"

            self.assertTrue(expected_output.exists())
            self.assertIn(str(expected_output), output)

        self.assertIn("Article preview generated", output)

    def test_present_md_command_blocks_path_escape(self):
        present_md_path_error = load_symbol(
            self,
            "governed_docs.commands.present_md",
            "PresentMdPathError",
        )
        run_present_md_command = load_symbol(
            self,
            "governed_docs.commands.present_md",
            "run_present_md_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            with self.assertRaises(present_md_path_error):
                run_present_md_command(workspace_root, "../escape.md")


if __name__ == "__main__":
    unittest.main()
