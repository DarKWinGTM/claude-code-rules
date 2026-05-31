# P127 — README Core Capabilities List and Doctrine Framing

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P127
> **Status:** Completed / Released
> **Target Release:** v10.35
> **Design References:**
> - [../design/design.md](../design/design.md) v10.35
> - [../design/document-governance.design.md](../design/document-governance.design.md) v1.10
> **Patch References:** [../patch/readme-core-capabilities-list-and-doctrine-framing.patch.md](../patch/readme-core-capabilities-list-and-doctrine-framing.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine the README Core Capabilities section so it presents the current operating model as a readable list grounded in active doctrine/current-state behavior rather than phase/execution numbering.

---

## Why This Phase Exists

The checked README capability block had become hard to scan and too execution-shaped at the same time. The grid/table layout was awkward for dense doctrine-like copy, and `Runtime Context Discipline` had drifted into phase/release chronology. That made the README front page behave more like an execution/history surface than a current-state overview.

P127 exists to repair that front-page meaning without reopening the larger phase grammar doctrine wave. The target is a front-page rewrite, not a new execution doctrine family.

---

## Expected Output

- the README Core Capabilities section no longer uses the old grid/table block
- every capability is presented as a readable list item
- capability wording explains active doctrine/current-state behavior directly
- capability wording does not use phase 1/2/3/4 or execution timeline as the explanation basis
- `Runtime Context Discipline` stays front-page scoped instead of replaying release history
- touched README/changelog/TODO/phase/patch surfaces close `v10.35 / P127` consistently
- runtime install into a checked project-local `.claude/rules/` target, 18/18 parity/body sufficiency, branch push, remote default-branch verification, and GitHub release `v10.35` verification all pass

---

## Action Checklist

- [x] Confirm the current README capability block and the governing authority lines that define README as a current-state front page.
- [x] Replace the Core Capabilities grid/table with a readable list.
- [x] Rewrite capability wording so it explains active doctrine/current-state behavior instead of execution chronology.
- [x] Tighten README/front-page authority wording in the touched document-governance owner chain.
- [x] Sync touched master surfaces in changelog, TODO, phase, and patch.
- [x] Re-install the active runtime rules into a checked project-local `.claude/rules/` target and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [x] Commit the release wave, push the branch, update the remote default branch, and verify GitHub release `v10.35`.

---

## Out of Scope

- changing the Core Capabilities section into a phase summary
- using phase numbering as the meaning of a capability
- inventing new doctrine that is not grounded in the active design/runtime authorities
- widening the wave into unrelated README/layout cleanup
- changing the 18-rule runtime install scope
- bringing `playground/` into the runtime install payload

---

## Completion Gate

- the old grid/table capability block is gone
- every capability is expressed as a readable list item with practical current-state behavior
- the README capability section does not use phase/execution chronology as its explanation basis
- checked design/current-state authority supports the rewrite direction
- touched README/changelog/TODO/phase/patch surfaces align to `v10.35 / P127`
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.35` verification pass

---

## Current Status

P127 is completed.

Current checked progress:
- the README capability block is now list-based and doctrine-grounded
- `Runtime Context Discipline` now stays front-page scoped instead of replaying release chronology
- the touched document-governance owner chain now explicitly backs README capability/current-state presentation as front-page/current-state meaning
- touched README/changelog/TODO/phase/patch surfaces are updated in source scope
- runtime install into a checked project-local `.claude/rules/` target, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch verification, and GitHub release `v10.35` verification passed
