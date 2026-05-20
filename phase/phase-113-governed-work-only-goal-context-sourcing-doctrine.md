# P113 — Governed-Work-Only Goal Context Sourcing Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P113
> **Status:** Completed / Released
> **Target Release:** v10.21
> **Design References:**
> - [../design/design.md](../design/design.md) v10.21
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/governed-work-only-goal-context-sourcing-doctrine.patch.md](../patch/governed-work-only-goal-context-sourcing-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so advisory `/goal` behavior stays concise by default for trivial non-governed next steps, but becomes design-first and governed-surface-sourced for bounded repo-governed successor work where execution context materially defines what done means.

---

## Why This Phase Exists

The released `v10.20 / P112` wave left the original `/goal` doctrine intact from P107.

That baseline already allows bounded, transcript-provable `/goal` suggestions, but it still leaves one important behavior gap: RULES does not yet explicitly distinguish small non-governed next steps from repo-governed successor work that depends on design truth, active execution context, release/current-state truth, or before/after review boundaries.

Without that distinction, `/goal` can still drift in two bad directions:
- it can stay too vague for governed repo work because the command is not sourced from the right authority surfaces
- it can become too heavy for trivial next steps because governed context gets dragged into work that does not need it

---

## Expected Output

- exact trigger conditions state when governed-surface context becomes mandatory for `/goal` construction
- governed `/goal` sourcing is design-first, then active execution surfaces, with changelog/patch/README included only when they materially shape completion, review, or current-state impact
- trivial non-governed next steps stay ordinary prose or a very light `/goal`, not a governed-surface dump
- touched runtime/design/changelog chains align to the new governed-work-only doctrine
- master README/design/changelog/TODO/phase/patch surfaces are opened and later closed out consistently for `v10.21 / P113`
- active runtime install scope remains 18
- runtime install, source/runtime parity, source/destination body sufficiency, and `git diff --check` pass before release closeout
- GitHub release `v10.21` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [x] Confirm the clean isolated worktree stays the active execution surface for P113.
- [x] Update the `/goal` runtime owners with governed-work-only trigger, sourcing, and compact-output doctrine.
- [x] Sync the touched owner design companions and owner changelog parents.
- [x] Open P113 master surfaces in README, design, changelog, TODO, phase, and patch.
- [x] Preserve at least two concrete example `/goal` outputs: one governed non-release example and one governed release-closeout example.
- [x] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [x] Commit the source release state and push the branch.
- [x] Create and verify GitHub release `v10.21`.
- [x] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- forcing heavy governed context into trivial non-governed next steps
- turning `/goal` into a long template dump or mini-spec
- changing advisory `/goal` behavior into selected execution
- expanding the active runtime install set beyond 18 root runtime rules
- drifting into unrelated plugin/runtime work outside this repo
- treating changelog, patch, or README as mandatory `/goal` inputs when they do not materially shape completion, review, or current-state impact

---

## Completion Gate

- the touched active doctrine explicitly distinguishes trivial non-governed next steps from bounded governed repo successor work
- exact trigger conditions explicitly state when governed-surface context becomes mandatory
- governed `/goal` sourcing is explicitly design-first, then active execution surfaces, with material-only changelog/patch/README inclusion
- at least two example `/goal` outputs exist for audit and review
- touched runtime/design/changelog files align to `v10.21 / P113`
- active runtime install scope remains 18 and install/parity/body-sufficiency checks pass
- `git diff --check` passes
- branch push and GitHub release `v10.21` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P113 is released as `v10.21`.

Release verification summary:
- the isolated worktree stayed the active execution surface for this wave
- the three primary `/goal` runtime owners now explicitly distinguish trivial non-governed next steps from bounded governed repo successor work
- exact mandatory governed-surface trigger conditions are now explicit in active doctrine
- governed `/goal` sourcing is now design-first, then active execution surfaces, with changelog/patch/README included only when they materially shape completion, review, or current-state impact
- two concrete `/goal` outputs are preserved for governed non-release and governed release-closeout review
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` passed
- branch push passed
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.21
- release tag `v10.21` resolves to commit `53f80777bd3b0ec9d5ad84165bcd58e6e726c4f2`
- Published at `2026-05-20T07:54:14Z`.
