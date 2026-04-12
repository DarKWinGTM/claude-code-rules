# Phase 026-02 - Integrate memory-governance companions

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 026-02
> **Status:** Completed
> **Design References:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/memory-governance-and-session-boundary.patch.md](../patch/memory-governance-and-session-boundary.patch.md)

---

## Objective

Integrate the new memory-governance chain into adjacent owner chains without blurring their existing authority boundaries.

## Why this phase exists

A new first-class memory-governance chain is not sufficient by itself. The adjacent authority, wording, burden-of-proof, and presentation owners need narrow integration so the repository teaches one coherent memory model without duplicating ownership.

## Entry conditions / prerequisites

- `026-01` exists and the new chain is already defined
- this integration remains narrow and should not turn companion chains into duplicate memory-governance owners
- live memory migration remains out of scope for this wave

## Action points / execution checklist

- [x] update `authority-and-scope` with narrow memory-applicability / stale-branch boundaries
- [x] update `accurate-communication` with memory-derived-context disclosure wording
- [x] update `evidence-grounded-burden-of-proof` with memory-aware evidence/recheck handling
- [x] update `answer-presentation` with a compact memory-status / scope-re-anchor presentation shape
- [x] update touched design/changelog artifacts for the companion owner chains
- [x] keep the integration narrow and defer deeper ownership to `memory-governance-and-session-boundary`

## Out of scope

- making adjacent chains co-own the memory taxonomy
- reorganizing live memory files
- broad compact/post-compact doctrine rewrites beyond what the new chain requires

## Affected artifacts

- `authority-and-scope.md`
- `accurate-communication.md`
- `evidence-grounded-burden-of-proof.md`
- `answer-presentation.md`
- touched design/changelog companions for those four chains

## TODO coordination

- record this wave as governance-integration work only after sync is complete
- do not mark live-memory migration done in this phase

## Changelog coordination

- add per-chain changelog entries for the four touched companion owners
- add one repository-level master changelog entry after sync is complete

## Verification

- [x] `authority-and-scope` defers memory applicability semantics to the new chain while preserving RULES-first and stale-branch boundaries
- [x] `accurate-communication` distinguishes memory-derived historical context from current verified fact
- [x] `evidence-grounded-burden-of-proof` treats memory-derived context as different from observed local fact
- [x] `answer-presentation` gains one compact visible pattern for memory status / matched scope / needs-recheck detail
- [x] companion chains remain narrow integrations rather than duplicate owners

## Risks / rollback notes

- companion edits could overstep and duplicate memory governance inside adjacent chains
- rollback should narrow the companion wording first before touching the new owner chain
- preserve the bounded wave history instead of silently erasing the integration record

## Next possible phases

- `026-03` sync master docs and runtime install parity
- `026-04` run postflight memory-governance audit

## Exit criteria

- [x] adjacent owners acknowledge the new memory-governance contract coherently
- [x] no companion owner re-owns the memory taxonomy unnecessarily
- [x] the touched companion chains remain aligned with the new first-class owner
