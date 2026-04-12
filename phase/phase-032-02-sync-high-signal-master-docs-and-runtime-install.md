# Phase 032-02 - Sync high-signal master docs and runtime install

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 032-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/high-signal-communication.design.md](../design/high-signal-communication.design.md)
> **Patch References:** [../patch/high-signal-communication-active-rule-sync.patch.md](../patch/high-signal-communication-active-rule-sync.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the high-signal communication promotion wave.

## Why this phase exists

The per-chain promotion only becomes operationally real when the active runtime inventory, README install set, changelog, TODO, and phase summary all agree on the rule status, and when the installed runtime copy under `~/.claude/rules/` matches the updated source.

## Entry conditions / prerequisites

- `032-01` is complete and the high-signal chain itself is already coherent
- the bounded patch artifact for this wave already exists
- the runtime install target remains limited to the touched runtime rules only

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check the installed runtime copies against source

## Out of scope

- reopening unrelated rollout families
- changing untouched runtime rules beyond narrow metadata parity where already-authoritative changelogs require it
- git/release work before sync and verification finish

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for `high-signal-communication.md`, `todo-standards.md`, `phase-implementation.md`, and `artifact-initiation-control.md`

## TODO coordination

- move wave `032` into completed history in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure the `high-signal-communication` per-chain changelog aligns with v1.1
- ensure the repository-level master changelog records wave `032`

## Verification

- [x] master design inventory shows the active runtime count as 37 and includes `high-signal-communication`
- [x] README teaches the high-signal rule and installs the same 37-rule active runtime set
- [x] master changelog and TODO record the bounded wave
- [x] phase summary indexes the new `032` rollout family
- [x] installed runtime files match the updated source copies for all touched rules

## Risks / rollback notes

- sync drift can survive even when the chain itself is semantically correct, so master-surface and runtime-copy checks remain required
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted, not merely because one sync artifact needed cleanup
- preserve wave `032` history rather than silently removing the rollout record

## Next possible phases

- none required for this bounded refinement wave once sync and parity are complete
- install/release work may follow only after the postflight audit passes

## Exit criteria

- [x] repository-level governance reflects the high-signal promotion coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `032` phase family is visible and reviewable from `phase/SUMMARY.md`
