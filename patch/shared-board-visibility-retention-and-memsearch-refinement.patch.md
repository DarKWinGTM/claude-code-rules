# Shared Board Visibility, Retention, and Memsearch Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md) v1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that strengthens three remaining parts of the shared execution coordination model:
- visible session-held task identity
- clearer handoff lifecycle and retention matrix semantics
- deeper optional memsearch operating guidance

Why this change matters:
- session-held work should be easier to identify at scan time on the shared board
- handoff status should remain followable beyond a generic request/accept intuition
- retention should depend more explicitly on task class and coordination state
- optional memsearch should be usable as a recall accelerator without outranking stronger checked execution surfaces

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../shared-execution-coordination.md`
- `../todo-standards.md`
- `../memory-governance-and-session-boundary.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the new wording should improve visibility and lifecycle clarity without turning the system into a rigid task-schema bureaucracy
- optional memsearch guidance should stay optional and should not revive claude-peers-like future role drift

---

## 3) Change Items

### Change Item 1
- **Target location:** `shared-execution-coordination` primary owner
- **Change type:** additive

**Before**
```text
The coordination owner already covered shared-board semantics, handoff naming boundaries, and anti-overclear direction, but visible session-id policy, lifecycle detail, retention matrix semantics, and memsearch operating detail were still looser than desired.
```

**After**
```text
The coordination owner now makes session-held work more visibly distinguishable, defines a clearer handoff lifecycle, makes retention depend more explicitly on task class/state, and explains how optional memsearch should be used after stronger execution surfaces identify the relevant continuation target.
```

### Change Item 2
- **Target location:** `todo-standards` live task-board companion
- **Change type:** additive

**Before**
```text
The task-board companion already discouraged sender-phase leakage in cross-session requests, but it did not yet explicitly require stronger visible session identity for session-held or blocked-on-session work.
```

**After**
```text
The task-board companion now explicitly asks session-held, handoff, and blocked-on-session tasks to identify the relevant session visibly enough for fast scanability.
```

### Change Item 3
- **Target location:** `memory-governance-and-session-boundary` optional recall companion
- **Change type:** additive

**Before**
```text
The memory-governance chain already treated memsearch-like layers as optional supplemental context bridges, but it did not yet explain clearly enough how to use them after stronger execution surfaces have already identified the active continuation target.
```

**After**
```text
The memory-governance chain now explicitly says optional recall extensions may accelerate recall after stronger coordination surfaces identify the target, and that their output must not outrank checked task/phase/design/implementation evidence.
```

---

## 4) Verification

- [x] `shared-execution-coordination` explicitly defines visible session-held task identity guidance
- [x] `shared-execution-coordination` explicitly defines a clearer handoff lifecycle
- [x] `shared-execution-coordination` explicitly defines a retention matrix principle
- [x] `shared-execution-coordination` explicitly deepens optional memsearch operating guidance without making it required
- [x] `todo-standards` reinforces visible session identity for session-held task-board items
- [x] `memory-governance-and-session-boundary` reinforces post-identification optional recall behavior without upgrading memsearch into authority
- [x] master design/README/TODO/changelog/phase surfaces record wave `038` coherently
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too detailed:
- keep the session-visible identity and retention protections intact while narrowing verbosity before removing the refinement entirely
- preserve the optional memsearch boundary so optional recall does not become required infrastructure
- preserve the patch and phase history instead of silently erasing the refinement wave
