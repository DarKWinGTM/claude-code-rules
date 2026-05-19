# P110 — Project-Local Claude Code Install Architecture and Explanation Clarity Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P110
> **Status:** Active / In Progress
> **Target Release:** v10.18
> **Design References:**
> - [../design/design.md](../design/design.md) v10.18
> **Patch References:** [../patch/project-local-claude-code-remote-install-helpers.patch.md](../patch/project-local-claude-code-remote-install-helpers.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Normalize project-local Claude Code install architecture into a dedicated design surface, add launcher scripts over the Bash and PowerShell helper execution layer, and teach RULES to explain code/config/system identifiers in easy-to-understand, non-character, role-aware language.

---

## Why This Phase Exists

The current README still carries long inline Bash and PowerShell installer bodies.

That shape has four problems:
- installer logic lives in documentation instead of executable helper files
- the old examples bias toward `~/.claude/rules/` rather than project-local `.claude/rules/`
- the README still exposes broader cross-harness adaptation wording that should not be treated as support for this install surface
- easy explanations still rely too often on raw identifiers without clearly translating what they are, what they do, and why they matter in the system

P110 exists to make project-local Claude Code install the primary path, keep owner-aware manifest cleanup, avoid overclaiming Codex/Gemini support for a surface they do not natively consume, and make explanation doctrine more meaning-first and role-aware.

---

## Expected Output

- `script/setup-claude-code-rules.sh` exists as a project-local Claude Code installer helper.
- `script/setup-claude-code-rules.ps1` exists as a project-local Claude Code installer helper.
- `design/design/installer-architecture.design.md` exists as the dedicated installer architecture surface.
- Both helpers default to `<project-root>/.claude/rules/` and preserve owner-aware manifest cleanup.
- README Quick Start uses clone → launcher as the primary install path while helpers remain the execution layer underneath.
- README no longer presents Codex CLI or Gemini CLI as supported for this install surface.
- Communication/explanation owners now require meaning-first identifier explanation, parent → child walkthroughs for nested keys when useful, UI-versus-storage separation when relevant, and anti-over-explanation limits.
- The active runtime install set remains exactly 18 root runtime files.
- Project-local install proof passes 18/18 source/destination parity and body sufficiency.
- `git diff --check` passes.

---

## Action Checklist

- [x] Confirm released baseline is `v10.17 / P109`.
- [x] Confirm `v10.18` and `phase-110*` are absent in checked scope.
- [x] Confirm `script/` does not already exist in source scope.
- [x] Create `script/setup-claude-code-rules.sh`.
- [x] Create `script/setup-claude-code-rules.ps1`.
- [x] Create a dedicated installer architecture design surface.
- [x] Switch README Quick Start to clone + launcher install guidance.
- [x] Remove Codex/Gemini support claims for this install surface from touched README sections.
- [x] Add explanation clarity doctrine across the selected communication/explanation owners.
- [x] Sync touched design/changelog/TODO/phase/patch surfaces to P110 pre-release state.
- [x] Run project-local install proof and `git diff --check`. 

---

## Out of Scope

- Codex CLI support for this install surface.
- Gemini CLI support for this install surface.
- User-level-first install design.
- Multi-harness or non-Claude support expansion for this install surface.
- Runtime rule count expansion beyond 18.
- `plugin/` edits or release-scope expansion.

---

## Completion Gate

- Helper scripts exist at the two required paths.
- A dedicated installer architecture design surface exists and governs the selected install model.
- README uses clone → launcher as the primary install path while helpers remain the execution layer underneath.
- The selected install surface is project-local `.claude/rules/`.
- Owner-aware manifest cleanup is preserved.
- No Codex/Gemini support claim remains for this install surface in touched scope.
- Communication/explanation owners explicitly require meaning-first identifier explanation, parent → child walkthroughs when useful, UI-versus-storage separation when relevant, and anti-over-explanation limits.
- Project-local install proof passes with 18/18 source/destination parity and body sufficiency.
- `git diff --check` passes.

---

## Current Status

P110 is active in pre-release implementation for `v10.18`.

Completed so far:
- released baseline is `v10.17 / P109`
- `v10.18` is absent in checked scope
- `phase-110*` is absent in checked scope
- `script/` was absent before this wave opened

Still pending:
- release selection is not part of the current goal
