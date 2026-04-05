# Governing-Basis Clarification Before Branching Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.9
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that tightens how the assistant should behave when multiple materially different governing bases, policies, or decision frames remain live.

Why this change matters:
- the user reported a real failure mode where the assistant kept exploring multi-branch pricing semantics instead of first asking which governing basis should control the answer
- once the user chose the basis directly, the problem collapsed quickly and the remaining work became straightforward
- the current rules already discourage unnecessary option branching and over-explaining, but they do not yet make governing-basis clarification explicit as an ask-first boundary before deep branch analysis

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
- the refinement should reduce unnecessary deep branching without turning the system into a generic ask-more-questions doctrine
- the clarification should happen only when multiple materially different bases remain live and the answer would change depending on which one is chosen

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain already owned continuation-vs-option behavior, but it did not yet say explicitly that materially outcome-changing basis ambiguity should trigger a compact clarification before deep branch analysis.
```

**After**
```text
The chain now requires the assistant to ask for governing-basis selection first when multiple materially different policies/frames remain live and the answer would materially differ depending on which one is chosen.
```

### Change Item 2
- **Target location:** `authority-and-scope` authority boundary owner
- **Change type:** additive

**Before**
```text
Residual ambiguity already returned a bounded context request, but the chain did not yet make governing-basis selection explicitly user-owned when multiple plausible bases remained unresolved.
```

**After**
```text
The chain now states that unresolved governing-basis selection belongs to the user unless checked authority or evidence already settles the basis.
```

### Change Item 3
- **Target location:** `evidence-grounded-burden-of-proof` epistemic owner
- **Change type:** additive

**Before**
```text
The chain handled unresolved uncertainty generally, but it did not yet model unresolved governing-basis ambiguity as its own first-class uncertainty state.
```

**After**
```text
The chain now treats unresolved governing-basis selection as an explicit uncertainty state and requires clarification before one interpretive branch becomes the active frame without enough proof.
```

### Change Item 4
- **Target location:** `explanation-quality` explanation restraint owner
- **Change type:** additive

**Before**
```text
The chain discouraged over-explaining generally, but it did not yet explicitly forbid deepening several mutually exclusive downstream branches before the active basis was chosen.
```

**After**
```text
The chain now prefers one short clarification gate over a long multi-branch explanation when the governing basis is unresolved.
```

### Change Item 5
- **Target location:** `answer-presentation` layout owner
- **Change type:** additive

**Before**
```text
The chain supported compact proposals and compact variable-role blocks, but it did not yet give governing-basis ambiguity its own compact form-like clarification layout.
```

**After**
```text
The chain now provides a compact clarification block for governing-basis selection with short basis choices and one short `Why it matters` line.
```

### Change Item 6
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded governing-basis-clarification refinement wave.
```

**After**
```text
Master governance surfaces now record the refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [x] `accurate-communication` explicitly asks for governing-basis selection before deep branch analysis when materially different frames remain live
- [x] `authority-and-scope` explicitly makes unresolved governing-basis selection user-owned unless checked authority/evidence already settles it
- [x] `evidence-grounded-burden-of-proof` models unresolved governing-basis ambiguity as a first-class uncertainty state rather than permission for silent branch selection
- [x] `explanation-quality` explicitly prefers one short clarification gate over long multi-branch explanation when the basis is unresolved
- [x] `answer-presentation` provides a compact form-like clarification layout for governing-basis selection
- [x] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the evidence and authority distinction that unresolved governing-basis selection should not silently become active truth
- narrow the clarification trigger so it applies only to clearly outcome-changing basis ambiguity
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior that treats materially different policy/frame choices as harmless complexity to explore without basis selection first
