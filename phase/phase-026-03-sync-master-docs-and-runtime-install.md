# Phase 026-03 - Sync master docs and runtime install

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 026-03
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/memory-governance-and-session-boundary.patch.md](../patch/memory-governance-and-session-boundary.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the new memory-governance owner chain and companion integrations are complete.

## Why this phase exists

The new chain only becomes operationally real when the repository-level inventory, README, changelog, TODO, and phase summary all show it coherently, and when the touched runtime rule files installed under `~/.claude/rules/` match the updated source copies.

## Entry conditions / prerequisites

- `026-01` and `026-02` are complete
- the new chain and touched companion owners already have aligned source-side design/runtime/changelog artifacts
- runtime install target remains limited to the touched owner rules only

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check installed runtime copies against source

## Out of scope

- live memory migration under `~/.claude/projects/.../memory/`
- changing unrelated runtime rules or reopening older rollout families
- creating push/release artifacts before semantic sync and audit are complete

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for `memory-governance-and-session-boundary.md`, `authority-and-scope.md`, `accurate-communication.md`, `evidence-grounded-burden-of-proof.md`, and `answer-presentation.md` under `~/.claude/rules/`

## TODO coordination

- move wave `026` into completed history once sync is complete
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure the new chain changelog aligns with its runtime/design versions
- ensure touched companion-chain changelogs align with their new runtime/design versions
- ensure the repository-level master changelog records wave `026`

## Verification

- [x] master design inventory shows the new chain and the updated active runtime count
- [x] README teaches the memory-governance refinement at a high level
- [x] master changelog and TODO record the bounded governance wave
- [x] phase summary indexes the new `026` rollout family
- [x] installed runtime files match the updated source copies for the touched rules

## Risks / rollback notes

- sync drift can survive even when the new chain and companion owners are semantically correct, so master-surface and runtime-copy checks remain required
- rollback should restore prior master-surface/runtime-copy state only if the wave itself is intentionally reverted, not merely because one sync artifact needed cleanup
- preserve wave `026` history rather than silently removing the rollout record

## Next possible phases

- `026-04` run postflight memory-governance audit
- a later separate wave may apply the new contract to the live `/memory` tree after this governance wave is stable

## Exit criteria

- [x] repository-level governance reflects the new memory-governance owner coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `026` phase family is visible and reviewable from `phase/SUMMARY.md`
