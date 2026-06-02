from __future__ import annotations

import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
INIT_SKILL = PACKAGE_ROOT / "skills" / "init" / "SKILL.md"


class InitSkillContractTests(unittest.TestCase):
    def test_init_skill_exists_and_describes_question_choice_setup(self) -> None:
        text = INIT_SKILL.read_text(encoding="utf-8")
        self.assertIn("/memory-context-intelligence:init", text)
        self.assertIn("question/choice dialogs", text)
        self.assertIn("Comprehensive default (Recommended)", text)
        self.assertIn("day / session / lookback", text)
        self.assertIn("Write config now", text)
        self.assertIn("~/.claude/memory-context-intelligence.config.json", text)
        self.assertIn("setup/config surface", text)


if __name__ == "__main__":
    unittest.main()
