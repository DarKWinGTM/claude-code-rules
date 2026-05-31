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


class ArticlePresentationTests(unittest.TestCase):
    def test_render_markdown_article_builds_toc_and_full_html(self):
        render_markdown_article = load_symbol(
            self,
            "governed_docs.article_presentation",
            "render_markdown_article",
        )

        markdown_text = """---
title: Governance Guide
summary: Easier governed-doc reading
updatedAt: 2026-06-01
---

# Governance Guide

## Scanner Layer

Readable paragraph.

### Detail

- First
- Second
"""

        rendered = render_markdown_article(markdown_text, source_rel_path="docs/guide.md")
        self.assertEqual(rendered.title, "Governance Guide")
        self.assertIn("Scanner Layer", rendered.content_toc)
        self.assertIn("gd-article-layout", rendered.full_html)
        self.assertIn("Readable paragraph.", rendered.content_html)

    def test_render_markdown_article_blocks_javascript_links(self):
        render_markdown_article = load_symbol(
            self,
            "governed_docs.article_presentation",
            "render_markdown_article",
        )

        markdown_text = "# Unsafe\n\n[click](javascript:alert('x'))"
        rendered = render_markdown_article(markdown_text, source_rel_path="docs/unsafe.md")
        self.assertNotIn("javascript:", rendered.content_html)
        self.assertIn("click", rendered.content_html)


if __name__ == "__main__":
    unittest.main()
