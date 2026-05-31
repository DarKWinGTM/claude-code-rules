# governed-docs operator skill and agent entry surfaces patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-04, the public/operator entry-surface wave for `governed-docs`.

## Analysis

Before this slice:
- runtime behavior existed only as internal modules and direct Python entry points
- there was no stable plugin manifest, executable router, skill surface set, or agent scaffold set
- operator-facing entry paths were still design-only

After this slice:
- governed-docs exposes its runtime through a plugin manifest, bin router, skills, and agent scaffolds
- command routing preserves the explicit target-path contract
- public/operator entry remains separate from hidden mutation authority

## Change Items

### 1) Add plugin manifest and executable router
- **Target artifact:** `.claude-plugin/plugin.json`, `bin/governed-docs`, `src/governed_docs/cli.py`
- **Change type:** additive
- **Before state:** no stable operator entry router existed
- **After state:** operator-facing command routing exists for scan/review/repair-plan/phase-audit/release-gate/present-md

### 2) Add skill wrappers
- **Target artifact:** `skills/**/SKILL.md`
- **Change type:** additive
- **Before state:** no plugin-local skill entry surfaces existed
- **After state:** each primary command now has a governed-docs-owned skill surface that keeps the explicit target-path requirement visible

### 3) Add agent scaffolds and entry-surface tests
- **Target artifact:** `agents/*.md`, `tests/test_entry_surfaces.py`, `tests/test_cli_router.py`
- **Change type:** additive
- **Before state:** no custom-agent scaffolds or focused entry-surface proof route existed
- **After state:** bounded agent roles exist and entry-surface routing is covered by focused tests

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 40 tests passed
- the suite includes `test_manifest_skills_and_agents_exist`, `test_bin_router_executes_scan`, and CLI routing tests for `scan`, `repair-plan`, and `present-md`

Covers:
- manifest / skill / agent / hook surface existence
- operator bin routing
- explicit target-path routing behavior through the CLI layer

Does not cover:
- autonomous multi-agent orchestration
- deployment/runtime proof outside the plugin workspace

## Rollback approach

If this slice needs containment or partial rollback:
- keep runtime modules intact even if a wrapper surface must be narrowed
- preserve the explicit target-path contract on any surviving entry surface
- do not convert wrapper rollback into hidden direct-execution shortcuts
