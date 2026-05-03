# Changelog - Custom Agent Selection Priority

> **Parent Document:** [../custom-agent-selection-priority.md](../custom-agent-selection-priority.md)
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-05-04 | **[Added capability-fit specialist selection boundary](#version-13)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 1.2 | 2026-05-03 | **[Clarified selection-after-routing boundary](#version-12)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 1.1 | 2026-04-04 | **[Added reuse-before-spawn guidance for overlapping team-agent roles](#version-11)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.0 | 2026-03-31 | **[Created first-class custom-agent-selection-priority rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new design/runtime/changelog triad that governs selection priority for user custom agents, clear-best-fit specialist preference, and the distinction between discovery failures and selection behavior | |

---

<a id="version-13"></a>
## Version 1.3: Added capability-fit specialist selection boundary

**Date:** 2026-05-04
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `custom-agent-selection-priority.md` from v1.2 to v1.3.
- Updated `design/custom-agent-selection-priority.design.md` from v1.2 to v1.3.
- Clarified that this chain selects the best visible specialist for the required capability after native worker routing has already classified intent, worker need, and worker scale.
- Added capability-fit wording so specialist selection is not hardcoded to tool names or candidate labels.
- Added a boundary preventing custom-agent selection from escalating standalone subagent-fit work into Agent Team workflow.
- Generalized reuse-before-spawn from teammate-only wording to worker/specialist reuse where applicable.

### Summary
Custom-agent-selection-priority now works as a downstream capability-fit selector: native worker routing decides whether and what kind of worker is needed, then this rule chooses the best visible specialist without turning agent availability into a routing decision.

---

<a id="version-12"></a>
## Version 1.2: Clarified selection-after-routing boundary

**Date:** 2026-05-03
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `custom-agent-selection-priority.md` from v1.1 to v1.2.
- Updated `design/custom-agent-selection-priority.design.md` from v1.1 to v1.2.
- Clarified that `native-worker-agent-routing-and-context-control.md` owns worker-scale routing and leader-context control before this chain selects a best-fit specialist.
- Added routing-before-selection guidance so custom-agent availability is not treated as proof that delegation is appropriate.
- Preserved custom-agent priority, discovery-boundary, and reuse-before-spawn semantics.

### Summary
Custom-agent-selection-priority now explicitly works downstream of native worker routing: it chooses the best available specialist once delegation or specialist handling is already the selected path.

---

<a id="version-11"></a>
## Version 1.1: Added reuse-before-spawn guidance for overlapping team-agent roles

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `custom-agent-selection-priority.md` from v1.0 to v1.1.
- Updated `design/custom-agent-selection-priority.design.md` from v1.0 to v1.1.
- Added a reuse-before-spawn rule so an already-active teammate covering the same role should be reused before another same-role teammate is spawned.
- Added distinct-role justification guidance so parallel teammates must have clearly partitioned work rather than duplicate-looking overlap.
- Added anti-pattern coverage for spawning a second teammate with the same role and no distinct partition.

### Summary
Custom-agent-selection-priority now prefers reusing an existing matching teammate before adding another overlapping role to the same team.

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
