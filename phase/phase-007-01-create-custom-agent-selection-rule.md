# Phase 007-01 - Create custom-agent selection rule

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 007-01
> **Status:** In Progress
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md)
> **Patch References:** [../patch/custom-agent-selection-priority.patch.md](../patch/custom-agent-selection-priority.patch.md)

---

## Objective

Create the first-class rule chain that governs custom-agent selection priority.

## Why this phase exists

The RULES system already has custom agents, built-ins, plugin agents, and generic handling paths, but it does not yet have one semantic owner for saying that visible user custom agents should be treated as the primary specialist pool when task fit is clear.

## Design Extraction

- Source requirement: custom user agents should be preferred when they are visible and clearly fit the task
- Derived execution work: create the new design/runtime/changelog triad and patch artifact
- Target outcome: one durable owner exists for custom-agent selection priority

## Reviewer Checklist

- [x] new design file exists
- [x] runtime rule exists
- [x] changelog authority exists
- [x] patch artifact exists
- [x] the chain distinguishes selection behavior from runtime discovery behavior

## Verification

- new chain exists as a governed triad
- patch artifact shows the before/after governance need clearly
- custom-agent selection priority is now defined in one place

## Exit Criteria

- `design/custom-agent-selection-priority.design.md` exists
- `custom-agent-selection-priority.md` exists
- `changelog/custom-agent-selection-priority.changelog.md` exists
- `patch/custom-agent-selection-priority.patch.md` exists
