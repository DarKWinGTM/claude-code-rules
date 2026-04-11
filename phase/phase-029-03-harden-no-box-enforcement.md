# Phase 029-03 - Harden no-box enforcement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 029-03
> **Status:** Completed
> **Design References:** [../design/table-format-and-usage.design.md](../design/table-format-and-usage.design.md)
> **Patch References:** [../patch/table-format-and-usage-centralization.patch.md](../patch/table-format-and-usage-centralization.patch.md)

---

## Objective

Harden the central table owner so ordinary assistant answers still use the canonical no-frame format for generic table requests and explicitly treat box-drawing framed output as non-compliant.

## Why this phase exists

The earlier centralization and no-box refinement established the owner and the prohibition, but a real user test still produced a boxed Unicode table while describing it as plain no-frame. This phase tightens the central rule at the visible output-shape level.

## Entry conditions / prerequisites

- `029-01` and `029-02` are already complete
- the central table owner already exists
- a real user-driven behavior test showed that boxed output still appeared despite the rule being loaded

## Action points / execution checklist

- [x] strengthen the central rule so generic table requests still require the canonical no-frame style
- [x] add character-level no-box enforcement for Unicode box-drawing frame characters
- [x] add a send-time visible-shape self-check requirement
- [x] update the central design/changelog artifacts to match the hardening
- [x] keep the refinement bounded to the central table owner rather than reopening adjacent-chain ownership transfer again

## Out of scope

- direct behavior testing in this phase
- reopening adjacent non-table owner boundaries
- changing unrelated communication or memory doctrine

## Affected artifacts

- `table-format-and-usage.md`
- `design/table-format-and-usage.design.md`
- `changelog/table-format-and-usage.changelog.md`

## TODO coordination

- record this slice as no-box enforcement hardening after master sync is complete
- leave user-driven real-world validation outside this phase

## Changelog coordination

- add one per-chain changelog entry for the hardening
- add one repository-level master changelog entry after master sync is complete

## Verification

- [x] generic table requests still bind to the canonical no-frame style
- [x] box-drawing frame characters are explicitly treated as non-compliant for ordinary assistant answers
- [x] send-time visible-shape checking is now stated explicitly
- [x] the hardening remains bounded to the central table owner

## Risks / rollback notes

- wording could become too abstract if it talks about compliance without naming visible frame characters directly
- rollback should narrow the new hardening wording first before weakening the no-box contract itself
- preserve the wave history because it records a real user-observed enforcement gap

## Next possible phases

- `029-04` sync master docs and runtime install parity after the hardening
- later user-driven real-world validation outside the implementation wave

## Exit criteria

- [x] the central table owner now expresses character-level no-box enforcement
- [x] the central rule now states a visible-shape self-check before send
- [x] the hardening remains bounded and reviewable
