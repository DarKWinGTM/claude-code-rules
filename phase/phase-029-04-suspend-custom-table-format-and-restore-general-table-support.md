# Phase 029-04 - Suspend custom table-format and restore general table support

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 029-04
> **Status:** Completed
> **Design References:** [../design/table-format-and-usage.design.md](../design/table-format-and-usage.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md)
> **Patch References:** [../patch/table-format-and-usage-centralization.patch.md](../patch/table-format-and-usage-centralization.patch.md)

---

## Objective

Suspend the custom `table-format-and-usage` experiment from the active RULES system while restoring general support for using tables when they genuinely help.

## Why this phase exists

After real-world testing, the user decided the custom table-format experiment was too costly and too complex to keep active. The file needed to be preserved for future redesign without leaving it in the active runtime rule path.

## Entry conditions / prerequisites

- the central table owner wave already exists
- the user explicitly chose suspension rather than deletion
- general table support should remain active through the adjacent presentation and explanation owners

## Action points / execution checklist

- [x] remove the custom table-format owner from the active runtime path
- [x] preserve the file for later redesign instead of deleting it
- [x] restore general support for tables when they genuinely help
- [x] synchronize touched design/changelog/master surfaces and runtime copies

## Out of scope

- deleting the preserved suspended experiment
- reopening the earlier table-style correction wave
- broad communication or memory changes in the same slice

## Affected artifacts

- `suspend/table-format-and-usage.md`
- `design/table-format-and-usage.design.md`
- `answer-presentation.md`
- `explanation-quality.md`
- touched master surfaces for the suspension wave

## TODO coordination

- record the suspension wave in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure touched per-chain changelogs record the suspension/removal from active runtime state
- ensure the master changelog records the bounded suspension wave

## Verification

- [x] custom table-format behavior is no longer part of the active runtime rule set
- [x] the preserved experiment remains available for later redesign
- [x] general table support remains active in the presentation and explanation owners

## Risks / rollback notes

- mixed state could survive if the preserved file remains readable as if it were active
- rollback should be explicit and synchronized across source/master/install surfaces
- preserve the suspension history instead of silently erasing it

## Next possible phases

- none required for this bounded suspension slice
- any later reactivation should open a new rollout family rather than silently reusing the old active path

## Exit criteria

- [x] the custom experiment is preserved but not active
- [x] general table support remains available
- [x] the suspension slice is visible and reviewable
