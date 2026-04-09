# Phase 025-02 - Sync master docs and runtime install

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 025-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md)
> **Patch References:** [../patch/compact-markdown-table-default-and-minimal-table-usage.patch.md](../patch/compact-markdown-table-default-and-minimal-table-usage.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the compact-table / list-first refinement.

## Why this phase exists

The owner-chain refinement only becomes operationally real when the master inventories, README, changelog, TODO, and phase summary all show it, and when the touched runtime rules in `~/.claude/rules/` match the updated source files.

## Entry conditions / prerequisites

- `025-01` is complete and the touched owner chains are already updated
- the bounded patch artifact for wave `025` already exists
- the runtime install target remains limited to the touched owner rules only

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check the installed runtime copies against source

## Out of scope

- reopening semantic owner scope beyond sync/consistency needs
- changing unrelated runtime rules or reopening older rollout families
- creating git/release artifacts before semantic sync and audit are complete

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for `answer-presentation.md` and `explanation-quality.md` under `~/.claude/rules/`

## TODO coordination

- move wave `025` into completed history in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure the two touched per-chain changelogs align with their new runtime/design versions
- ensure the repository-level master changelog records wave `025`

## Verification

- [x] master design inventory shows the new touched-chain versions and role descriptions
- [x] README teaches the compact-table refinement at a high level
- [x] master changelog and TODO record the bounded refinement wave
- [x] phase summary indexes the new `025` rollout family
- [x] installed runtime files match the updated source copies for the touched rules

## Risks / rollback notes

- sync drift can survive even when the owner chains themselves are correct, so master-surface and runtime-copy checks remain required
- rollback should restore prior master-surface/runtime-copy state only if the wave itself is intentionally reverted, not merely because one sync artifact needed cleanup
- preserve wave `025` history rather than silently removing the rollout record

## Next possible phases

- no additional phase is required for this bounded refinement wave once sync and parity are complete
- push/release work should happen only after postflight audit passes

## Exit criteria

- [x] repository-level governance reflects the new refinement coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `025` phase family is visible and reviewable from `phase/SUMMARY.md`
