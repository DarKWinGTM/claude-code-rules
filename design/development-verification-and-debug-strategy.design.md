# Development Verification and Debug Strategy Design
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/development-verification-and-debug-strategy.changelog.md](../changelog/development-verification-and-debug-strategy.changelog.md)
---
## Target State
Development verification becomes a normal part of non-trivial AI coding work. The assistant should not treat coding as complete merely because files were edited, configured, scaffolded, or made checklist-ready; it should identify the changed behavior, choose a proportionate debug/test strategy, run or define the relevant checks when practical, and report evidence limits honestly.

This design makes verification strategic rather than rigid. It requires the verification decision, not the same artifact or same command every time.
---
## Behavior Model
Non-trivial coding/debug/refactor/integration work should follow this shape:

```text
understand behavior
  → assess risk and safety boundary
  → choose debug/test signal
  → choose verification depth
  → implement
  → run targeted checks or record not-run reason
  → report coverage and limits
```

The intended verification depth is proportionate:
- trivial no-behavior work can use review/no-test with reason
- small behavior changes prefer unit or focused tests
- refactors prefer affected regression tests
- integrations prefer fake/contract/integration checks
- scenario-like flows prefer TestKit or equivalent scenario harnesses
- payment/auth/runtime/provider/privacy work requires fake/local-first plus explicit smoke/live decision
---
## TestKit Role
TestKit is a strategic option for scenario-like or system-flow behavior, not a mandatory artifact for every task. The runtime rule should require a TestKit/scenario decision when relevant:
- existing test covers it
- new focused test is better
- new TestKit scenario is warranted
- smoke/live check is required and gated
- not applicable with reason

This keeps coding accuracy high without turning every small edit into a full test-harness ceremony.
---
## Evidence and Closeout Target
Closeout wording should distinguish:
- prepared/checklist-ready
- configured/wired
- implemented/edited only
- tested partially
- verified in the named scope
- fake/local verified
- smoke checked
- live/provider/runtime verified
- fixed in checked failure scope
- stable over time

A useful coding closeout should record what was run, what passed/failed, what behavior it covers, what remains untested, and confidence at the evidence strength actually held.
---
## Integration Target
- `maintainable-code-structure-and-decomposition.md` keeps structure/refactor responsibility while this owner handles verification strategy.
- `accurate-communication.md` keeps evidence-strength wording aligned with coding verification states.
- `phase-implementation.md` records Development Verification / TestKit Coverage for phase-backed coding work when material.
- `todo-standards.md` keeps live verification slices visible for non-trivial coding work.
- `project-documentation-standards.md` records repository-level documentation role boundaries for coding verification coverage.
- `execution-continuity-and-mode-selection.md` prevents stopping after implementation when verification remains the implied next safe slice.
---
## Non-Goals
- Do not require a new TestKit scenario for every code edit.
- Do not force live/provider/runtime checks without approval and environment readiness.
- Do not make testing ceremony heavier than the behavior risk justifies.
- Do not replace project-specific test architecture or runtime topology rules.
- Do not use passing fake/local tests as proof of live behavior.
---
## Verification Expectations
- Non-trivial coding work has an explicit verification strategy.
- Debug work identifies signal/reproduction/hypothesis when practical.
- TestKit/scenario decisions are visible when scenario-like behavior exists.
- Phase/TODO/closeout surfaces preserve verification coverage when material.
- Evidence wording does not overclaim from edits, partial tests, or fake/local checks.
