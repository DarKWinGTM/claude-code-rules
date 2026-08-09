from __future__ import annotations

import json
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_MANIFEST = PACKAGE_ROOT / ".claude-plugin" / "plugin.json"
ANALYSIS_SKILL = PACKAGE_ROOT / "skills" / "analysis" / "SKILL.md"
INIT_SKILL = PACKAGE_ROOT / "skills" / "init" / "SKILL.md"


def skill_version(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("version: "):
            return line.removeprefix("version: ")
    raise AssertionError(f"Missing skill version in {path}")


class PluginManifestTests(unittest.TestCase):
    def test_plugin_manifest_and_public_skills_track_current_version(self) -> None:
        payload = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(payload["name"], "memory-context-intelligence")
        self.assertEqual(payload["version"], "0.9.31")
        self.assertEqual(skill_version(ANALYSIS_SKILL), payload["version"])
        self.assertEqual(skill_version(INIT_SKILL), payload["version"])
        self.assertIn("description", payload)


if __name__ == "__main__":
    unittest.main()
