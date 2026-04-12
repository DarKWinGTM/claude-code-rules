# Shared Execution Coordination Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md) v1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that turns shared multi-session execution coordination into a first-class RULES owner instead of leaving the behavior scattered across tracking, phase, execution, repository, and memory owners.

Why this change matters:
- shared task-list behavior already works in practice, but the protocol is still spread across several chains
- multi-session coordination needs explicit ownership for session lease, handoff, retention/aging, and anti-overclear behavior
- optional extensions such as memsearch may strengthen context continuity, but the coordination model must still work without them
- future optional peer-messaging layers such as `claude-peers-mcp` should remain explicitly future-optional until a later wave adopts them

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../shared-execution-coordination.md`
- `../todo-standards.md`
- `../phase-implementation.md`
- `../execution-continuity-and-mode-selection.md`
- `../project-documentation-standards.md`
- `../memory-governance-and-session-boundary.md`
- `../authority-and-scope.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the new coordination owner must not swallow the narrower existing owners and become a super-rule
- retention/aging policy must improve task-history continuity without making the board impossible to maintain
- optional memsearch and future-optional peer messaging must stay optional rather than becoming hidden required dependencies

---

## 3) Change Items

### Change Item 1
- **Target location:** new first-class coordination owner
- **Change type:** additive

**Before**
```text
Shared execution coordination behavior existed only as scattered semantics across task, phase, execution-continuity, repository, and memory-owner chains.
```

**After**
```text
A new first-class `shared-execution-coordination` chain now owns shared-board semantics, session lease/handoff protocol, continuity-first retention, anti-overclear policy, optional memsearch support, and future-optional peer-messaging boundaries.
```

### Change Item 2
- **Target location:** task / phase / execution / repository / memory / authority companions
- **Change type:** additive

**Before**
```text
The existing owners already covered useful slices of the behavior, but multi-session coordination semantics were not explicitly deferred to one shared owner.
```

**After**
```text
The touched companion chains now keep their existing narrow roles while explicitly deferring shared-board multi-session coordination protocol details to `shared-execution-coordination`.
```

### Change Item 3
- **Target location:** master surfaces and install set
- **Change type:** additive

**Before**
```text
The master surfaces did not include the new first-class coordination owner, and the runtime install set still reflected the prior 39-rule state.
```

**After**
```text
The master surfaces now record wave `036`, include the new coordination owner, and update the active runtime install set from 39 to 40 rules.
```

---

## 4) Verification

- [x] `shared-execution-coordination` exists as a governed runtime/design/changelog triad
- [x] the new chain explicitly keeps the shared task list as execution coordination rather than semantic truth
- [x] the new chain explicitly defines session lease, handoff, retention/aging, anti-overclear, optional memsearch support, and future-optional peer-messaging boundaries
- [x] touched companion rules now defer multi-session coordination protocol details to the new coordination owner
- [x] master design/README/TODO/changelog/phase surfaces record wave `036` coherently
- [x] touched runtime rules are reinstalled and parity-checked
- [x] postflight review confirms the new owner did not swallow the narrower existing owners

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the shared execution board concept intact while narrowing what the new owner controls
- preserve the existing working task-list continuity and next-work-discovery behavior rather than reverting to scattered undefined coordination semantics
- preserve the patch and phase history instead of silently erasing the wave
- do not regress into a state where shared-board retention and handoff semantics drift ad hoc across several chains again
