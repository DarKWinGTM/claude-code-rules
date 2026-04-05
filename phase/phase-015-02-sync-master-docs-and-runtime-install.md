# Phase 015-02 - Sync master docs and runtime install

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 015-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/governing-basis-clarification-before-branching.patch.md](../patch/governing-basis-clarification-before-branching.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the governing-basis clarification refinement.

## Why this phase exists

The owner-chain refinement only becomes operationally real when the master inventories, README, changelog, TODO, and phase summary all show it, and when the touched runtime rules in `~/.claude/rules/` match the updated source files.

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check the installed runtime copies against source

## Verification

- master design inventory shows the new touched-chain versions and role descriptions
- README teaches the governing-basis clarification refinement at a high level
- master changelog and TODO record the bounded refinement wave
- phase summary indexes the new `015` rollout family
- installed runtime files match the updated source copies for the touched rules

## Exit criteria

- repository-level governance reflects the governing-basis clarification refinement coherently
- runtime install parity is restored for all touched rules
- the `015` phase family is visible and reviewable from `phase/SUMMARY.md`
