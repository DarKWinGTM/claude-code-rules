from __future__ import annotations

import json
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_MANIFEST = PACKAGE_ROOT / ".claude-plugin" / "plugin.json"


class PluginManifestTests(unittest.TestCase):
    def test_plugin_manifest_is_valid_json_and_tracks_current_version(self) -> None:
        payload = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(payload["name"], "memory-context-intelligence")
        self.assertEqual(payload["version"], "0.9.25")
        self.assertIn("description", payload)


if __name__ == "__main__":
    unittest.main()
