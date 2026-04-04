# Goal-Qualified Proposal Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.7
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that keeps future-work proposals allowed, but stops them from reading like implied queued execution.

Why this change matters:
- proposing ideas is useful when the user benefits from seeing a credible future concept
- the failure mode is not proposal itself; it is proposal text that sounds like the assistant already committed the user to the next wave
- the existing continuation and recommendation refinements already narrowed option drift, but they did not yet require future-work proposals to carry an explicit goal/output contract

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../authority-and-scope.md`
- `../explanation-quality.md`
- `../answer-presentation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should preserve good proposal behavior without suppressing genuinely useful ideas, while making sure future-work concepts remain clearly advisory and evaluable

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain allowed recommendations and next-step guidance, but it did not yet require future-work proposals to state a concrete goal, improvement, and output/result.
```

**After**
```text
The chain now allows future-work proposals only when they are goal-qualified and clearly advisory.
A proposal must state:
- the goal
- what it would improve or change
- the output, artifact, or result it would produce
- optional success condition when useful
```

### Change Item 2
- **Target location:** `authority-and-scope` proposal boundary owner
- **Change type:** additive

**Before**
```text
Assistant-generated options were advisory, but future-work proposals were not yet explicitly separated from active execution state.
```

**After**
```text
Assistant-generated future-work proposals are now explicitly advisory only and do not create an active branch, implied commitment, or pending continuation unless the user selects them.
```

### Change Item 3
- **Target location:** `explanation-quality` closing/landing support owner
- **Change type:** additive

**Before**
```text
The chain supported clean endings and next-step guidance, but future ideas could still be phrased like automatic continuation after bounded completion.
```

**After**
```text
The chain now reinforces that future-work ideas after bounded completion should be framed as proposals with a goal, improvement, and expected output/result rather than as automatic continuation.
```

### Change Item 4
- **Target location:** `answer-presentation` layout support owner
- **Change type:** additive

**Before**
```text
The chain supported recommendation and next-stage layouts, but it did not yet expose a compact proposal block for future-work ideas.
```

**After**
```text
The chain now adds a compact proposal layout shape using:
- `Proposal`
- `Goal`
- `Improvement`
- `Output`
- optional `Success condition`
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded proposal-boundary refinement wave.
```

**After**
```text
Master governance surfaces now record the refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `accurate-communication` explicitly allows proposals while requiring goal-qualified advisory wording
- [ ] `authority-and-scope` explicitly prevents proposals from becoming implied queued execution
- [ ] `explanation-quality` reinforces proposal framing after bounded completion
- [ ] `answer-presentation` provides a compact proposal layout shape
- [ ] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the proposal-is-advisory boundary in `authority-and-scope`
- narrow the proposal formatting guidance in `answer-presentation` to a softer house-style preference
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to future-work wording that blurs advisory ideas into implied execution
