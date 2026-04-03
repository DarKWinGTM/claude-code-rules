# Phase 011-02 - Sync master docs and runtime install

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 011-02
> **Status:** In Progress
> **Design References:** [../design/design.md](../design/design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/recommended-option-and-why-this-first.patch.md](../patch/recommended-option-and-why-this-first.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the recommendation-format refinement.

## Why this phase exists

The wording/layout refinement only becomes operationally real when the master inventories, README, changelog, TODO, and phase summary all show it, and when the touched runtime rules in `~/.claude/rules/` match the updated source files.

## Action points / execution checklist
- [ ] update `design/design.md`
- [ ] update `README.md`
- [ ] update `changelog/changelog.md`
- [ ] update `TODO.md`
- [ ] update `phase/SUMMARY.md`
- [ ] reinstall touched runtime rules into `~/.claude/rules/`
- [ ] parity-check the installed runtime copies against source

## Verification
- master design inventory shows the new touched-chain versions and role descriptions
- README teaches the recommendation-plus-reason behavior at a high level
- master changelog and TODO record the bounded refinement wave
- phase summary indexes the new `011` rollout family
- installed runtime files match the updated source copies for the touched rules

## Exit criteria
- repository-level governance reflects the recommendation-format refinement coherently
- runtime install parity is restored for all touched rules
- the `011` phase family is visible and reviewable from `phase/SUMMARY.md`
