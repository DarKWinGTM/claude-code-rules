# Compact / Post-Compact Governance Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.10
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that tightens how the RULES system should behave after `/compact`.

Why this change matters:
- compacted sessions can continue from compressed carry-forward state that no longer preserves every exact detail
- without an explicit re-anchor contract, the assistant can revive stale branches or treat compressed-away detail like fresh verified truth
- the repository already has owners for wording, authority, evidence, explanation, and layout, so this should be a bounded owner-set refinement rather than a new doctrine chain

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../authority-and-scope.md`
- `../evidence-grounded-burden-of-proof.md`
- `../explanation-quality.md`
- `../answer-presentation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should improve post-compact continuation without turning normal answers into generic replay blocks
- re-anchor should stay compact and should only surface needs-recheck detail when exactness materially matters

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain already handled continuation-first behavior and compact snapshots generally, but it did not yet say explicitly that compacted-session continuation should re-anchor the active objective and separate carried-forward facts from needs-recheck details.
```

**After**
```text
The chain now requires a short post-compact re-anchor before continuation when compaction may have compressed away exact checked detail.
```

### Change Item 2
- **Target location:** `authority-and-scope` authority boundary owner
- **Change type:** additive

**Before**
```text
The chain already protected fresh user directives and user-owned basis selection, but it did not yet explicitly prevent stale assistant framing from reviving after compact.
```

**After**
```text
The chain now requires post-compact continuation to re-anchor to the latest active user directive and active governing basis instead of stale assistant framing.
```

### Change Item 3
- **Target location:** `evidence-grounded-burden-of-proof` epistemic owner
- **Change type:** additive

**Before**
```text
The chain already separated fact, inference, hypothesis, and unresolved basis ambiguity, but it did not yet model compacted carry-forward exact detail as its own recheck-needed evidence state.
```

**After**
```text
The chain now treats compressed carry-forward exact detail as `POST_COMPACT_NEEDS_RECHECK` unless enough surviving evidence still preserves its exactness.
```

### Change Item 4
- **Target location:** `explanation-quality` explanation-flow owner
- **Change type:** additive

**Before**
```text
The chain already discouraged over-explaining and supported compact diagnostic snapshots, but it did not yet explicitly prefer one short post-compact re-anchor over replaying stale history.
```

**After**
```text
The chain now prefers one short post-compact re-anchor before explanation continues when compact may have compressed away exact context.
```

### Change Item 5
- **Target location:** `answer-presentation` layout owner
- **Change type:** additive

**Before**
```text
The chain already supported compact snapshots, scope-boundary blocks, and governing-basis clarification blocks, but it did not yet provide a canonical compact layout for post-compact continuation.
```

**After**
```text
The chain now provides a compact post-compact re-anchor block with `Current objective`, `Carried-forward facts`, `Needs recheck`, and `Next action`.
```

### Change Item 6
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded post-compact refinement wave.
```

**After**
```text
Master governance surfaces now record the compact/post-compact refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [x] `accurate-communication` explicitly adds post-compact re-anchor guidance
- [x] `authority-and-scope` explicitly prevents stale assistant framing from reviving after compact
- [x] `evidence-grounded-burden-of-proof` adds a post-compact needs-recheck state for compacted carry-forward exact detail
- [x] `explanation-quality` explicitly prefers one short re-anchor over long replay after compact
- [x] `answer-presentation` provides a compact post-compact re-anchor layout
- [x] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the distinction between carried-forward facts and needs-recheck post-compact detail
- narrow the trigger so it applies only when exactness materially affects the next move
- preserve the recorded phase/patch history rather than silently erasing the refinement wave
- do not revert to behavior that resumes from compact as if compressed-away detail were always still exact verified truth
