import os
import subprocess
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]


class EntrySurfaceTests(unittest.TestCase):
    def test_manifest_skills_and_agents_exist(self):
        expected_paths = [
            PLUGIN_ROOT / '.claude-plugin' / 'plugin.json',
            PLUGIN_ROOT / 'skills' / 'scan' / 'SKILL.md',
            PLUGIN_ROOT / 'skills' / 'review' / 'SKILL.md',
            PLUGIN_ROOT / 'skills' / 'repair-plan' / 'SKILL.md',
            PLUGIN_ROOT / 'skills' / 'phase-audit' / 'SKILL.md',
            PLUGIN_ROOT / 'skills' / 'release-gate' / 'SKILL.md',
            PLUGIN_ROOT / 'skills' / 'present-md' / 'SKILL.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-scout.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-doctrine-evaluator.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-repair-architect.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-normalizer.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-release-auditor.md',
            PLUGIN_ROOT / 'agents' / 'governed-docs-phase-lineage-auditor.md',
            PLUGIN_ROOT / '.claude' / 'hooks' / 'governed-docs-reminder.sh',
        ]
        for path in expected_paths:
            self.assertTrue(path.exists(), f"expected path to exist: {path}")

    def test_bin_router_executes_scan(self):
        env = {**os.environ, 'PYTHONPATH': str(PLUGIN_ROOT / 'src')}
        proc = subprocess.run(
            [str(PLUGIN_ROOT / 'bin' / 'governed-docs'), 'scan', str(PLUGIN_ROOT)],
            cwd=str(PLUGIN_ROOT),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn('governed-docs scan report', proc.stdout)


if __name__ == '__main__':
    unittest.main()
