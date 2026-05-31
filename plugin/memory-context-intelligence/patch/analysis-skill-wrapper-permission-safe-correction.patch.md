# Analysis skill wrapper permission-safe correction patch

> **Current Version:** 0.1.61
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-28)
> **Status:** Phase 057 completed analysis skill wrapper permission-safe correction in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.61
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Phase 056 corrected historical breadth semantics, but transcript-visible local slash proof for `/memory-context-intelligence:analysis` still failed because the executable block in `skills/analysis/SKILL.md` used command shapes that the permission checker blocked before the runtime chain could run.

## 2) Analysis

The remaining mismatch was no longer inside `intake`, `signals`, or `presentation`. The blocker was the skill wrapper itself:
- the original inline Python heredoc pattern was rejected as expansion-obfuscation-like shell content
- the first wrapper rewrite still failed because simple shell expansion remained approval-blocked in the executable block
- the stable fix was to move wrapper logic into runtime-owned code and expose one fixed-command internal entrypoint that the skill can invoke without inline expansion

## 3) Change items

### 3.1 Skill wrapper contract
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`
- **Change type:** replacement
- **Before:** the skill executable block used a permission-blocked inline wrapper pattern and active contract text still described unresolved empty print-mode proof
- **After:** the executable block now invokes the fixed-command `memory-context-intelligence analysis-surface` path, and the active contract text now describes approved non-interactive local slash proof instead of the stale unresolved proof wording

### 3.2 Runtime wrapper ownership
- **Target artifact:** `../bin/memory-context-intelligence`, `../lib/analysis_surface.py`
- **Change type:** additive/replacement
- **Before:** wrapper logic lived inline in the skill executable block and could not be re-proved through the actual slash surface
- **After:** the wrapper logic now lives in `lib/analysis_surface.py`, and `bin/memory-context-intelligence` exposes the internal `analysis-surface` subcommand that the skill wrapper can call safely

### 3.3 Governed sync and version alignment
- **Target artifact:** `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../design/06-plugin-installability.design.md`, `../design/07-recall-scoping-and-time-window.design.md`, `../phase/SUMMARY.md`, `../phase/phase-057-analysis-skill-wrapper-permission-safe-correction.md`, `../changelog/changelog.md`, `../changelog/v0.1.61-completed-analysis-skill-wrapper-permission-safe-correction.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, `../.claude-plugin/plugin.json`, and this patch
- **Change type:** replacement/additive
- **Before:** active docs still described the slash-surface proof path as unresolved empty print-mode output and the local package version remained `0.9.13`
- **After:** active docs now describe the restored approved non-interactive local slash proof posture, and the package version is bumped to `0.9.14`

## 4) Verification

- focused analysis-skill contract tests must fail first, then pass after the wrapper correction
- the new runtime wrapper file must compile successfully
- the full runtime/source suite must pass after the wrapper correction
- one source-session slash run and one installed-local slash run must both return operator-facing output in checked scope when local command approval is intentionally granted

## 5) Rollback approach

If this correction wave is rolled back, restore the older inline wrapper only if the user explicitly wants that proof path back. Do not weaken the phase 056 breadth/order behavior and do not mutate `/additional/` unless a broader rollback is explicitly selected.
