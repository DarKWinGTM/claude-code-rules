import contextlib
import importlib
import io
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


class ScanCommandTests(unittest.TestCase):
    def test_scan_command_returns_report_only_summary(self):
        run_scan_command = load_symbol(
            self,
            "governed_docs.commands.scan",
            "run_scan_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "README.md")
            write_file(workspace_root / "TODO.md")

            output = run_scan_command(workspace_root)

        self.assertIn("governed-docs scan report", output)
        self.assertIn("README.md", output)
        self.assertIn("TODO.md", output)
        self.assertIn("No files were edited.", output)

    def test_main_returns_error_code_for_missing_target_path(self):
        main = load_symbol(self, "governed_docs.commands.scan", "main")

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            try:
                exit_code = main([])
            except Exception as exc:
                self.fail(f"expected main() to return an error code instead of raising: {exc}")

        self.assertEqual(exit_code, 1)
        self.assertIn("explicit target workspace path", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
