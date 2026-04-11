# Phase 029-02 - Transfer table ownership from adjacent chains

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 029-02
> **Status:** Completed
> **Design References:** [../design/table-format-and-usage.design.md](../design/table-format-and-usage.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md)
> **Patch References:** [../patch/table-format-and-usage-centralization.patch.md](../patch/table-format-and-usage-centralization.patch.md)

---

## Objective

Narrow the adjacent owner chains so ordinary answer-table semantics now defer to the new central table owner.

## Why this phase exists

A new central rule is not enough by itself. If `answer-presentation` and `explanation-quality` still hold the same table doctrine directly, the repository would keep overlapping ownership instead of gaining real centralization.

## Entry conditions / prerequisites

- `029-01` exists and the new central table owner is already defined
- ownership transfer remains narrow and should not strip adjacent chains of their broader non-table responsibilities
- the selected ordinary answer-table default remains the same while ownership moves

## Action points / execution checklist

- [x] update `answer-presentation` with defer/reference wording for ordinary answer-table semantics
- [x] update `explanation-quality` with defer/reference wording for explanation-side table semantics
- [x] update touched design companions for those adjacent chains
- [x] update touched per-chain changelogs for those adjacent chains
- [x] keep adjacent ownership narrow and avoid over-centralizing unrelated layout/explanation concerns

## Out of scope

- removing all table mentions from adjacent chains entirely
- centralizing general headings, snapshots, or explanation-flow doctrine into the new chain
- reopening unrelated previous waves

## Affected artifacts

- `answer-presentation.md`
- `explanation-quality.md`
- `design/answer-presentation.design.md`
- `design/explanation-quality.design.md`
- `changelog/answer-presentation.changelog.md`
- `changelog/explanation-quality.changelog.md`

## TODO coordination

- record this wave as ownership transfer only after downstream sync is complete
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- add per-chain changelog entries for the two adjacent owners
- add one repository-level master changelog entry after master sync is complete

## Verification

- [x] `answer-presentation` now defers ordinary answer-table semantics to `table-format-and-usage.md`
- [x] `explanation-quality` now defers explanation-side table semantics to `table-format-and-usage.md`
- [x] adjacent chains still retain their broader layout / explanation-flow ownership
- [x] the selected no-frame table default remains intact after the transfer
- [x] adjacent chains no longer look like full co-owners of the same table doctrine

## Risks / rollback notes

- transfer wording could be too weak and leave ownership ambiguous
- transfer wording could be too broad and accidentally strip useful adjacent context
- rollback should narrow the defer wording first rather than deleting the central owner or restoring diffuse ownership silently

## Next possible phases

- `029-03` sync master docs and runtime install parity
- `029-04` run postflight centralization audit

## Exit criteria

- [x] centralization is a real ownership transfer rather than a merely additive rule
- [x] adjacent owners remain coherent after the transfer
- [x] the selected table contract remains stable while ownership moves to the new chain
