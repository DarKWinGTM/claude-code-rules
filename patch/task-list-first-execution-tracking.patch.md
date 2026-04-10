# Task-List-First Execution Tracking Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.4
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes Claude Code task-list usage more proactive for non-trivial work.

Why this change matters:
- the user sees the built-in task list as a valuable live execution surface because it shows what will be done, what is in progress, and what is already complete
- the current RULES stack already governs durable `TODO.md` tracking and startup artifact posture, but it does not yet explicitly define the built-in task list as the live execution surface for non-trivial active work
- this refinement should improve execution visibility without creating a new first-class doctrine chain

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../todo-standards.md`
- `../artifact-initiation-control.md`
- `../project-documentation-standards.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should increase live task visibility without turning task lists into heavy mandatory overhead for trivial work
- the refinement should preserve the distinction between built-in live task tracking and durable `TODO.md` repository tracking

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards` primary owner
- **Change type:** additive

**Before**
```text
The chain already treated `TODO.md` as the execution-tracking layer and required early TODO posture resolution for meaningful governed work, but it did not yet define Claude Code's built-in task list as the live execution surface for non-trivial active work.
```

**After**
```text
The chain now explicitly distinguishes:
- built-in task list = live execution-tracking surface for non-trivial active work
- `TODO.md` = durable repository/project execution-tracking artifact
It also defines when proactive task-list usage is expected and how task state should be kept current.
```

### Change Item 2
- **Target location:** `artifact-initiation-control` startup companion
- **Change type:** additive

**Before**
```text
Startup posture already resolved design/changelog/TODO/phase/patch before meaningful work drifted, but it did not yet explicitly require early live task tracking when non-trivial tracked work needed visible execution state.
```

**After**
```text
The chain now explicitly includes early live task-list initialization in startup posture when non-trivial tracked work would materially benefit from visible pending / in_progress / completed state.
```

### Change Item 3
- **Target location:** `project-documentation-standards` repository-model companion
- **Change type:** additive

**Before**
```text
The repository role model already treated `TODO.md` as the execution-tracking document, but it did not yet clearly distinguish durable repository tracking from live built-in task tracking during active work.
```

**After**
```text
The chain now explicitly distinguishes:
- built-in task list = live in-session execution surface for non-trivial work
- `TODO.md` = durable repository/project tracking
without turning the built-in task list into a governed document artifact.
```

### Change Item 4
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded task-list-first execution-tracking refinement wave.
```

**After**
```text
Master governance surfaces now record the task-list-first refinement wave, and the touched runtime rules can be reinstalled into `~/.claude/rules/` so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `todo-standards` explicitly distinguishes live built-in task tracking from durable `TODO.md` tracking
- [ ] `todo-standards` explicitly defines non-trivial task-list triggers and update discipline
- [ ] `artifact-initiation-control` explicitly includes early live task-list posture for non-trivial tracked work
- [ ] `project-documentation-standards` explicitly keeps built-in task tracking as a live execution surface rather than a governed document artifact
- [ ] master design/README/TODO/changelog/phase surfaces record the bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the durable-vs-live tracking distinction in `todo-standards`
- narrow trigger/update language before removing the task-list-first posture entirely
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to a state where non-trivial work can drift forward with no visible live execution tracking even when the user would materially benefit from it
