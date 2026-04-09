# Purpose-First Communication Framing Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.13
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that tightens communication efficiency when an answer is technically correct but still makes the reader wait too long to understand what the message is doing.

Why this change matters:
- the user identified a concrete failure mode where the explanation only became clear after reading several detailed lines, even though the real point could be stated in one direct sentence first
- official plain-language and content-design guidance consistently favors putting the most important information first, front-loading content, and using direct active wording
- the existing owner set already covered human-readable wording, explanation flow, layout, and tone, but it did not yet explicitly require a purpose-first opening for diagnosis, tests, recommendations, proposals, and implementation updates

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../explanation-quality.md`
- `../answer-presentation.md`
- `../natural-professional-communication.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should improve immediate understanding without forcing a rigid extra sentence into naturally clear short answers
- the opening should remain evidence-aligned and not become a license for stronger claims than the checked evidence supports

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain already required clear, evidence-honest wording, but it did not yet explicitly require diagnosis, test, recommendation, proposal, or implementation-update answers to open with one direct sentence saying what the message is doing.
```

**After**
```text
The chain now explicitly requires a main-point-first operational framing sentence when that orientation materially helps the reader.
It also adds trigger, decision-framework, example, anti-pattern, and quality-metric support for that behavior.
```

### Change Item 2
- **Target location:** `explanation-quality` explanation-flow owner
- **Change type:** additive

**Before**
```text
The chain already supported plain-language-first explanation, but it did not yet force operational explanations through a purpose-first step before deeper mechanism detail.
```

**After**
```text
The chain now adds a purpose-first explanation step and status-framing support so the explanation purpose is visible before the mechanism expands.
```

### Change Item 3
- **Target location:** `answer-presentation` layout owner
- **Change type:** additive

**Before**
```text
The chain already placed the main point early when helpful, but it did not yet provide a dedicated purpose-first framing trigger/pattern for diagnosis, tests, recommendations, proposals, and implementation updates.
```

**After**
```text
The chain now gives operational answers a compact purpose-first layout shape, including trigger, pattern, snapshot example, and canonical purpose-first example support.
```

### Change Item 4
- **Target location:** `natural-professional-communication` style owner
- **Change type:** additive

**Before**
```text
The chain already rejected robotic and abstraction-heavy wording, but it did not yet say clearly that natural professional style should front-load the operational purpose instead of making the reader wait through warm-up framing.
```

**After**
```text
The chain now treats purpose-before-detail wording as part of sounding like a strong human operator.
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record this bounded purpose-first communication refinement wave.
```

**After**
```text
Master governance surfaces now record the new bounded refinement wave, and the touched runtime rules can be reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [x] `accurate-communication` explicitly requires main-point-first operational framing for diagnosis, tests, recommendations, proposals, and implementation updates when that orientation materially helps the reader
- [x] `explanation-quality` explicitly adds a purpose-first explanation step before deeper mechanism detail
- [x] `answer-presentation` explicitly adds purpose-first framing support in trigger/pattern/example form
- [x] `natural-professional-communication` explicitly treats purpose-before-detail wording as part of natural professional style for operational answers
- [x] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the core main-point-first requirement in `accurate-communication`
- narrow the layout and style examples rather than removing the operational framing requirement entirely
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior that makes the reader reconstruct the purpose from later detail when one direct opening sentence would make the answer immediately understandable
