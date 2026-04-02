# Changelog - Custom Agent Selection Priority

> **Parent Document:** [../custom-agent-selection-priority.md](../custom-agent-selection-priority.md)
> **Current Version:** 1.0
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-03-31 | **[Created first-class custom-agent-selection-priority rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new design/runtime/changelog triad that governs selection priority for user custom agents, clear-best-fit specialist preference, and the distinction between discovery failures and selection behavior | |

---

<a id="version-10"></a>
## Version 1.0: Created first-class custom-agent-selection-priority rule chain

**Date:** 2026-03-31
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/custom-agent-selection-priority.design.md` as the active target-state design for custom-agent selection priority.
- Created runtime `custom-agent-selection-priority.md` as a first-class rule defining:
  - primary specialist-pool preference for visible user custom agents
  - best-fit-before-generic handling
  - no-forced-delegation boundaries
  - distinction between discovery failure and selection behavior
  - anti-patterns around ignoring clear user custom specialists
- Positioned the chain as the semantic owner of custom-agent selection priority while keeping adjacent authority boundaries intact for:
  - `authority-and-scope.md`
  - `functional-intent-verification.md`
  - `natural-professional-communication.md`
  - `anti-sycophancy.md`

### Summary
Created a first-class `custom-agent-selection-priority` rule chain so user custom agents can be treated as the primary specialist pool when they are visible and clearly fit the task, without pretending that prompt rules control runtime discovery.
