# governed-docs article Markdown presentation patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-07, the governed-docs-owned Markdown article-presentation slice.

## Analysis

Before this slice:
- the article-presentation request existed only as a later proposal
- there was no governed-docs-specific presentation design, renderer, or preview command
- article-style presentation risked being borrowed directly from NodeClaw rather than implemented under governed-docs ownership

After this slice:
- governed-docs has its own article-presentation design and renderer
- `present-md` can generate a local article-style HTML preview from a Markdown source inside the named target workspace
- unsafe link schemes are blocked and preview output is kept as a generated runtime artifact rather than a governed source rewrite

## Change Items

### 1) Add governed-docs-specific presentation design
- **Target artifact:** `design/07-article-markdown-presentation.design.md`
- **Change type:** additive
- **Before state:** article presentation existed only as a proposal
- **After state:** governed-docs has a checked design for metadata, safe Markdown handling, TOC behavior, and output ownership

### 2) Add renderer and preview command
- **Target artifact:** `src/governed_docs/article_presentation.py`, `src/governed_docs/commands/present_md.py`, `src/governed_docs/cli.py`
- **Change type:** additive / refinement
- **Before state:** no governed-docs-owned article renderer or preview command existed
- **After state:** the plugin can render article-style HTML and write a generated preview under `generated/article-preview/`

### 3) Add focused tests and skill wrapper
- **Target artifact:** `tests/test_article_presentation.py`, `tests/test_present_md_command.py`, `tests/test_cli_router.py`, `skills/present-md/SKILL.md`
- **Change type:** additive / refinement
- **Before state:** no focused proof route existed for safe-link handling, path containment, or preview writing
- **After state:** the preview path is covered by focused tests and an operator-facing skill surface

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 40 tests passed
- `./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md` → generated `generated/article-preview/07-article-markdown-presentation-design.html` and reported `No governed files were edited.`

Covers:
- safe-link blocking
- TOC / full HTML rendering
- source-path containment inside the named target workspace
- local preview output generation

Does not cover:
- external hosting or browser integration outside the local preview artifact
- broader editorial or publishing workflows

## Rollback approach

If this slice needs containment or partial rollback:
- keep the governed-docs-specific design as the ownership boundary
- remove preview-generation routing before widening sanitization scope unsafely
- preserve the rule that preview output is generated runtime state, not a governed source rewrite
