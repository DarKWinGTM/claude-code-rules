import importlib
import json
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


class PresentSyncCommandTests(unittest.TestCase):
    def test_present_sync_command_builds_preview_site_and_manifest(self):
        run_present_sync_command = load_symbol(
            self,
            "governed_docs.commands.present_sync",
            "run_present_sync_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            (workspace_root / "design").mkdir(parents=True, exist_ok=True)
            (workspace_root / "design" / "guide.design.md").write_text("# Guide\n\nReadable body.", encoding="utf-8")
            (workspace_root / "changelog").mkdir(parents=True, exist_ok=True)
            (workspace_root / "changelog" / "changelog.md").write_text("# Changelog\n\nLatest changes.", encoding="utf-8")
            (workspace_root / "patch").mkdir(parents=True, exist_ok=True)
            (workspace_root / "patch" / "wave.patch.md").write_text("# Patch\n\nReview me.", encoding="utf-8")
            (workspace_root / "phase").mkdir(parents=True, exist_ok=True)
            (workspace_root / "phase" / "SUMMARY.md").write_text("# Phase Summary\n\nCurrent work.", encoding="utf-8")
            (workspace_root / "TODO.md").write_text("# TODO\n\n- [ ] Example", encoding="utf-8")

            output = run_present_sync_command(workspace_root)

            preview_root = workspace_root / "preview"
            manifest_path = preview_root / "manifest.json"
            portal_index = preview_root / "index.html"
            design_page = preview_root / "design" / "guide" / "index.html"
            todo_page = preview_root / "todo" / "index.html"
            phase_page = preview_root / "phase" / "index.html"
            patch_page = preview_root / "patch" / "wave" / "index.html"

            self.assertTrue(manifest_path.exists())
            self.assertTrue(portal_index.exists())
            self.assertTrue(design_page.exists())
            self.assertTrue(todo_page.exists())
            self.assertTrue(phase_page.exists())
            self.assertTrue(patch_page.exists())

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertIn("documents", manifest)
            self.assertTrue(any(item["family"] == "design" for item in manifest["documents"]))
            self.assertTrue(any(item["family"] == "todo" for item in manifest["documents"]))
            self.assertIn(str(preview_root), output)
            self.assertIn("Preview site synced", output)

    def test_present_sync_command_prunes_stale_preview_pages(self):
        run_present_sync_command = load_symbol(
            self,
            "governed_docs.commands.present_sync",
            "run_present_sync_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            (workspace_root / "design").mkdir(parents=True, exist_ok=True)
            (workspace_root / "design" / "guide.design.md").write_text("# Guide\n\nReadable body.", encoding="utf-8")
            (workspace_root / "TODO.md").write_text("# TODO\n\n- [ ] Example", encoding="utf-8")
            (workspace_root / "phase").mkdir(parents=True, exist_ok=True)
            (workspace_root / "phase" / "SUMMARY.md").write_text("# Phase Summary\n\nCurrent work.", encoding="utf-8")

            stale_page = workspace_root / "preview" / "design" / "stale" / "index.html"
            stale_page.parent.mkdir(parents=True, exist_ok=True)
            stale_page.write_text("stale", encoding="utf-8")

            run_present_sync_command(workspace_root)

            self.assertFalse(stale_page.exists())

    def test_present_sync_command_keeps_source_docs_unchanged(self):
        run_present_sync_command = load_symbol(
            self,
            "governed_docs.commands.present_sync",
            "run_present_sync_command",
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            workspace_root = Path(tmp_dir)
            source_path = workspace_root / "TODO.md"
            original = "# TODO\n\n- [ ] Example"
            source_path.write_text(original, encoding="utf-8")
            (workspace_root / "phase").mkdir(parents=True, exist_ok=True)
            (workspace_root / "phase" / "SUMMARY.md").write_text("# Phase Summary\n\nCurrent work.", encoding="utf-8")

            run_present_sync_command(workspace_root)

            self.assertEqual(source_path.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
