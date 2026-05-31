import importlib
import os
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


class SurfaceScannerTests(unittest.TestCase):
    def test_scanner_inventories_active_authority_surfaces(self):
        scan_governed_surfaces = load_symbol(
            self,
            "governed_docs.surface_scanner",
            "scan_governed_surfaces",
        )
        scan_result_type = load_symbol(self, "governed_docs.scan_result", "ScanResult")

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "README.md")
            write_file(workspace_root / "TODO.md")
            write_file(workspace_root / "phase" / "SUMMARY.md")

            result = scan_governed_surfaces(workspace_root)

        self.assertIsInstance(result, scan_result_type)
        discovered = {
            (surface.relative_path, surface.surface_family, surface.inventory_class)
            for surface in result.discovered_surfaces
        }
        self.assertIn(
            ("README.md", "readme", "active authority surface"),
            discovered,
        )
        self.assertIn(
            ("TODO.md", "todo", "active authority surface"),
            discovered,
        )
        self.assertIn(
            ("phase/SUMMARY.md", "phase-summary", "active authority surface"),
            discovered,
        )
        self.assertFalse(result.mutated)

    def test_scanner_classifies_history_and_done_surfaces_as_inactive(self):
        scan_governed_surfaces = load_symbol(
            self,
            "governed_docs.surface_scanner",
            "scan_governed_surfaces",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "todo" / "history" / "2026-06-01.md")
            write_file(workspace_root / "phase" / "done" / "phase-001.md")

            result = scan_governed_surfaces(workspace_root)

        discovered = {
            (surface.relative_path, surface.surface_family, surface.inventory_class)
            for surface in result.discovered_surfaces
        }
        self.assertIn(
            ("todo/history/2026-06-01.md", "todo-history", "inactive history/done surface"),
            discovered,
        )
        self.assertIn(
            ("phase/done/phase-001.md", "phase-done", "inactive history/done surface"),
            discovered,
        )

    def test_scanner_uses_explicit_target_path_instead_of_ambient_cwd(self):
        scan_governed_surfaces = load_symbol(
            self,
            "governed_docs.surface_scanner",
            "scan_governed_surfaces",
        )

        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as target_tmp_dir, tempfile.TemporaryDirectory() as cwd_tmp_dir:
            target_root = Path(target_tmp_dir)
            cwd_root = Path(cwd_tmp_dir)
            write_file(cwd_root / "README.md")
            os.chdir(cwd_root)
            try:
                result = scan_governed_surfaces(target_root)
            finally:
                os.chdir(original_cwd)

        discovered_relative_paths = {
            surface.relative_path for surface in result.discovered_surfaces
        }
        self.assertNotIn("README.md", discovered_relative_paths)
        self.assertEqual(result.target_workspace_path, target_root.resolve())

    def test_scanner_includes_design_changelog_and_patch_roots(self):
        scan_governed_surfaces = load_symbol(
            self,
            "governed_docs.surface_scanner",
            "scan_governed_surfaces",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            write_file(workspace_root / "design" / "design.md")
            write_file(workspace_root / "changelog" / "changelog.md")
            write_file(workspace_root / "patch" / "governed-docs.patch.md")

            result = scan_governed_surfaces(workspace_root)

        discovered = {
            (surface.relative_path, surface.surface_family, surface.inventory_class)
            for surface in result.discovered_surfaces
        }
        self.assertIn(
            ("design/design.md", "design-parent", "active authority surface"),
            discovered,
        )
        self.assertIn(
            ("changelog/changelog.md", "changelog-parent", "active authority surface"),
            discovered,
        )
        self.assertIn(
            ("patch/governed-docs.patch.md", "patch", "active authority surface"),
            discovered,
        )


if __name__ == "__main__":
    unittest.main()
