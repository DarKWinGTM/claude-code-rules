# Phase 073 - Init Configuration Surface

> **Current Version:** 0.1.77
> **Target Design:** [../design/design.md](../design/design.md) v0.1.77
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-02)
> **Status:** Completed in checked scope
> **Patch References:** [../patch/init-configuration-surface.patch.md](../patch/init-configuration-surface.patch.md)

---

## Objective

Add `/memory-context-intelligence:init` as a usable setup/config surface, move the default config location to user scope under `~/.claude`, and make the analysis path consume stored scope defaults only when the operator did not explicitly narrow the run.

## Delivered

- added `skills/init/SKILL.md` as the public setup surface
- added `analysis.scope_policy` to the shared config contract
- switched default config discovery/suggested path to `~/.claude/memory-context-intelligence.config.json`
- made intake honor stored default scope only when explicit narrowing was absent
- exposed stored `scope_policy` in runtime payloads
- updated analysis guidance so `/analysis` points operators to `/init` for setup

## Verification

Focused checks completed:
- `tests/test_config_policy.py`
- `tests/test_intake.py`
- `tests/test_init_skill_contract.py`
- `tests/test_analysis_surface.py`
- `tests/test_analysis_skill_contract.py`
- `tests/test_plugin_manifest.py`

## Boundaries preserved

- `/memory-context-intelligence:analysis` remains the review surface
- `/memory-context-intelligence:init` is setup/config only
- `trace_evidence` remains the live promotion anchor
- `review` and `packet` remain non-public
- no main RULES mutation was performed by this plugin wave
