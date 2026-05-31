# Preview Portal and Sync

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-06-01)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Replace the current single-file article preview output with a governed-docs-owned `preview/` portal and sync layer that presents `design/`, `changelog/`, `TODO.md`, `phase/`, and `patch/` in a readable web shell while keeping semantic authority in the source docs.

## 2) Root path contract

The new v2 preview root should be:

```text
preview/
```

Required v1.1 shape:

```text
preview/
  index.html
  manifest.json
  design/<slug>/index.html
  changelog/<slug>/index.html
  todo/index.html
  phase/index.html
  patch/<slug>/index.html
  assets/
```

Why this root is selected:
- the user explicitly rejected `generated/`
- `preview/` is shorter and operator-readable
- `index.html` becomes a stable entrypoint for the presentation layer
- family-scoped nested pages allow one portal to present many governed sources without flattening everything into one file

## 3) Ownership and authority boundary

`preview/` is a presentation/support surface only.

It must not become:
- semantic authority for governed doc meaning
- release history authority
- phase-planning authority
- patch review authority
- a hidden replacement for the source Markdown/doc surfaces

Source-of-truth remains in:
- `design/`
- `changelog/`
- `TODO.md`
- `phase/`
- `patch/`

The preview layer may be regenerated from those sources, but it must not rewrite them.

## 4) Command model

### `present-md`

`present-md` remains the single-document renderer.

New target behavior:
- takes explicit target workspace path
- takes one explicit Markdown/doc source path
- renders exactly one preview page into the `preview/` tree
- updates only the necessary page output for that source

Preferred target mapping examples:
- `design/07-article-markdown-presentation.design.md` → `preview/design/07-article-markdown-presentation/index.html`
- `changelog/changelog.md` → `preview/changelog/changelog/index.html`
- `TODO.md` → `preview/todo/index.html`
- `phase/SUMMARY.md` → `preview/phase/index.html`

### `present-sync`

`present-sync` is the new full-site sync command.

Required behavior:
- requires one explicit target workspace path
- inventories eligible governed sources
- rebuilds `preview/index.html`
- rebuilds `preview/manifest.json`
- rebuilds family pages under `preview/<family>/<slug>/index.html`
- prunes stale preview pages that no longer have source backing
- mutates only `preview/**`

## 5) Eligible source families

The sync layer should support these families in the first implementation wave:
- `design/`
- `changelog/`
- `TODO.md`
- `phase/`
- `patch/`

Recommended family behavior:
- `design/` → one preview page per active design doc
- `changelog/` → one preview page per relevant changelog parent/detail doc selected by the sync inventory
- `TODO.md` → one compact task/current-state page
- `phase/` → one current-phase overview page sourced from `phase/SUMMARY.md` plus selected active child phase pages if needed
- `patch/` → one preview page per active patch artifact

## 6) Inventory and sync model

The sync layer should be driven by an explicit preview inventory.

Minimum manifest fields:
- `workspacePath`
- `generatedAt`
- `portalTitle`
- `documents[]`
  - `family`
  - `sourceRelPath`
  - `slug`
  - `title`
  - `summary`
  - `updatedAt`
  - `outputRelPath`
  - `status`

The manifest should be written to:

```text
preview/manifest.json
```

The sync process should compare source inventory against existing manifest/output state so it can:
- add missing pages
- update changed pages
- remove stale pages

## 7) UI / UX direction

The preview layer should behave as a compact documentation portal, not a loose folder of unrelated HTML files.

Selected UI direction from `/ui-ux-pro-max:ui-ux-pro-max` guidance:
- pattern: documentation/FAQ landing portal
- style: Minimalism + Swiss Style
- typography: Inter for heading and body
- visual priorities: high readability, strong hierarchy, low ornament, keyboard reachability, clear navigation

Required portal shell:
- top header with portal title and sync timestamp
- search/input placeholder area or non-interactive reserved search slot if full search is deferred
- left family navigation
- central document/article panel
- right-side TOC / metadata rail when a page includes section headings

Required UX boundaries:
- visible keyboard focus states
- skip-to-content support
- no reliance on color alone
- no decorative emoji icons as structural icons
- readable measure for long-form text
- sticky navigation must not obscure content
- dark/light readable contrast baseline

## 8) Subagent set

The new preview wave should add bounded helper agents:
- `governed-docs-present-inventory-scout`
- `governed-docs-present-architect`
- `governed-docs-present-renderer`
- `governed-docs-present-sync-auditor`

Boundaries:
- scout: discovers and classifies source docs read-only
- architect: shapes portal IA and page grouping
- renderer: assists with presentation-shell/page-generation work
- sync-auditor: verifies source ↔ preview parity and stale-page cleanup

These helpers remain support surfaces only and do not own semantic truth.

## 9) Safety boundary

The preview wave must preserve:
- explicit target workspace path requirement
- no ambient cwd fallback
- no rewrite of governed source docs
- no mutation outside `preview/**`
- no promotion of preview HTML into source authority
- no hidden background hook path that silently mutates preview state by default

If automation is added later, v1.1 still stays hook-light:
- reminder-first
- explicit sync command as the real mutation owner
- no silent always-on background regeneration path by default

## 10) Verification orientation

This preview wave is complete only when:
- `present-md` writes into the selected `preview/` structure
- `present-sync` exists in checked scope
- portal entry `preview/index.html` and `preview/manifest.json` are generated
- all targeted families are represented in the sync inventory/output model
- focused tests cover path safety, family routing, manifest generation, stale-page pruning, and bounded mutation scope
- smoke checks prove sync mutates only `preview/**`
- source docs remain unchanged after sync

---

> Preview rule: `preview/` is the governed-docs-owned web presentation layer, but source authority remains in the governed document families that feed it.