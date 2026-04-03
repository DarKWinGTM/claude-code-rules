# Continuation Priority and Option Offering Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Draft
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch tightens RULES behavior so active requested work continues by default instead of pausing mid-objective to report status, show optional next actions, or ask the user to choose among continuations that do not actually require a user decision.

## 2) Analysis

Risk level: Medium

Several communication/presentation/explanation chains already narrowed mandatory option-offering, but the combined behavior still leans toward next-stage signaling and next-step prompting in places where the assistant could safely continue execution. The fix should make continuation the default, while preserving user-choice gates when the next step is genuinely preference-sensitive, risky, blocked, or approval-dependent.

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` continuation-vs-option guidance
- **Change type:** replacement

**Before**
```text
The chain narrows mandatory option-offering, but still centers next-stage and next-action guidance strongly enough that mid-process reporting can win over continued execution.
```

**After**
```text
The chain makes execution-first behavior explicit: when the assistant can safely continue the requested work without clarification or approval, it should continue instead of pausing to offer optional next actions or stage narration.
```

### Change Item 2
- **Target location:** `answer-presentation` next-stage layout pattern
- **Change type:** replacement

**Before**
```text
Next-stage blocks are presented as a preferred forward-moving answer shape whenever the current explanation is already sufficient.
```

**After**
```text
Next-stage blocks remain available as optional presentation tools, but they are not a reason to interrupt active execution when the assistant can continue the user’s requested work directly.
```

### Change Item 3
- **Target location:** `explanation-quality` closing and decision-usefulness rules
- **Change type:** replacement

**Before**
```text
Explanation-heavy answers still lean toward exposing next moves/options strongly enough that progress updates can displace continued execution.
```

**After**
```text
Explanation-quality explicitly defers continuation-vs-option policy to accurate-communication and treats next-step guidance as conditional, not default, when the assistant is still mid-objective and can continue safely.
```

### Change Item 4
- **Target location:** `authority-and-scope` option framing posture
- **Change type:** additive

**Before**
```text
Authority-and-scope treats assistant-generated options as advisory and overrideable, but does not explicitly discourage generating unnecessary option branches in the first place.
```

**After**
```text
Authority-and-scope keeps options advisory and also warns against generating user-choice branches when one continuation path is already implied and executable.
```

---

## 4) Verification

- [ ] `accurate-communication` becomes the clear primary owner for continuation-vs-option policy
- [ ] `answer-presentation` and `explanation-quality` defer rather than reintroduce option-first drift
- [ ] active requested work no longer pauses by default for optional next-step prompts
- [ ] options are still available when user choice is genuinely required

---

## 5) Rollback Approach

If this tightening proves too aggressive, restore the prior usefulness-based wording while keeping the anti-artificial-option boundary intact. Do not revert to mandatory next-step or always-show-options behavior.
