# governed-docs preview portal and sync wave patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P002, the preview portal and sync wave.

## Analysis

Before this wave:
- `present-md` wrote one page under `generated/article-preview/`
- there was no preview portal root, manifest, or multi-family sync command
- the preview layer did not stay in the root `preview/` shape requested by the user

After this wave:
- the preview layer lives under `preview/`
- `present-md` remains the single-doc renderer
- `present-sync` rebuilds and prunes the full preview site
- preview output stays a presentation/support surface bounded to `preview/**`

## Change Items

### 1) Refactor preview path contract
- **Target artifact:** `src/governed_docs/commands/present_md.py`, `src/governed_docs/preview_paths.py`, related docs/tests
- **Change type:** replacement
- **Before state:** wrote to `generated/article-preview/<slug>.html`
- **After state:** writes to the root `preview/` family-aware path contract

### 2) Add full preview sync system
- **Target artifact:** `src/governed_docs/preview_site.py`, `src/governed_docs/commands/present_sync.py`, CLI routing, tests
- **Change type:** additive
- **Before state:** no site-wide sync command or manifest/index generation existed
- **After state:** `present-sync` builds and prunes the preview site in checked scope

### 3) Add portal shell and helper subagents
- **Target artifact:** preview shell output, `skills/present-sync/SKILL.md`, preview present-layer agent files, docs/tests
- **Change type:** additive
- **Before state:** single-page preview only
- **After state:** family-aware doc portal plus bounded helper surfaces

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 45 tests passed
- `./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md` → wrote `preview/design/07-article-markdown-presentation/index.html`
- `./bin/governed-docs present-sync /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → generated `preview/index.html` and `preview/manifest.json`
- selected source-hash verification confirmed that `TODO.md`, `phase/SUMMARY.md`, `design/design.md`, and `patch/preview-portal-and-sync-wave.patch.md` stayed unchanged across `present-sync`

Covers:
- root `preview/` path migration
- manifest/index generation
- stale-page pruning
- bounded mutation to `preview/**`
- no-source-rewrite behavior
- present-layer skill/agent entry surfaces

Does not cover:
- external hosting or deployment of the preview portal
- background auto-sync without an explicit command invocation

## Rollback approach

If this wave needs containment:
- preserve explicit target-path and source-path safety
- prefer reverting preview path/layout changes over widening source mutations
- keep preview support surfaces separate from governed source authority
