# Direct Human-Readable Wording Over Metaphor-Heavy Shorthand Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.12
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that tightens communication quality when technically plausible wording still forces the reader to decode metaphor-heavy internal shorthand before understanding the practical meaning.

Why this change matters:
- the user identified a concrete failure case where wording like `เอา capability พวกนี้ขึ้นมาบนผิว package` was harder to understand than a direct statement of what the user could actually do
- official plain-language guidance consistently prefers everyday words, active voice, and direct action/result wording over jargon, metaphor, or abstraction-heavy phrasing
- the existing owner set already covered glosses, explanation quality, natural professional tone, and presentation layout, but it did not yet explicitly reject metaphor-heavy internal shorthand as a default communication shape

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../explanation-quality.md`
- `../natural-professional-communication.md`
- `../answer-presentation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should improve human readability without suppressing necessary technical precision
- the system should still allow technical terms when they are materially useful, but it should prefer direct action/result wording and immediate plain-language glosses over metaphor-first system phrasing

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain already supported human-language glosses and natural-professional wording, but it did not yet explicitly say that metaphor-heavy internal shorthand should lose to direct action/result wording when both can express the same practical meaning.
```

**After**
```text
The chain now prefers direct human-readable wording that states what the user can do, what changed, or what result is visible.
It explicitly warns against metaphor-heavy or architecture-first phrasing when a plain action/result statement would be clearer.
```

### Change Item 2
- **Target location:** `explanation-quality` explanation-flow owner
- **Change type:** additive

**Before**
```text
The chain already required plain-language-first explanation and scope clarification, but it did not yet explicitly force metaphor-heavy or architecture-first wording through a direct human-readable translation step before deeper explanation relied on it.
```

**After**
```text
The chain now requires architecture-first, metaphor-heavy, or internal-shorthand wording to be translated into direct human-readable action/result language before deeper explanation depends on it.
```

### Change Item 3
- **Target location:** `natural-professional-communication` style owner
- **Change type:** additive

**Before**
```text
The chain already rejected robotic and over-performed tone, but it did not yet say clearly that abstract system language is not automatically professional if the reader still has to decode what practically changed.
```

**After**
```text
The chain now rejects metaphor-heavy or management-style abstraction as a default professional style when a direct human-readable action/result statement would be clearer.
```

### Change Item 4
- **Target location:** `answer-presentation` layout owner
- **Change type:** additive

**Before**
```text
The chain already supported glossary blocks and compact fact-oriented layouts, but it did not yet explicitly say that if an abstract internal term remains visible, a short gloss or direct implication should sit near it.
```

**After**
```text
The chain now requires short gloss-near-term support so structured answers do not leave metaphor-heavy or abstract internal phrases visually unexplained.
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded human-readable wording refinement wave.
```

**After**
```text
Master governance surfaces now record the new bounded refinement wave, and the touched runtime rules can be reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [x] `accurate-communication` explicitly prefers direct human-readable action/result wording over metaphor-heavy internal shorthand
- [x] `explanation-quality` explicitly translates architecture-first or metaphor-heavy wording into direct human-readable explanation before deeper reasoning depends on it
- [x] `natural-professional-communication` explicitly rejects abstraction-heavy wording as a default professional style when it reduces immediate understanding
- [x] `answer-presentation` provides gloss-near-term layout support for abstract internal phrasing when such terms still appear
- [x] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the direct-human-readable preference in `accurate-communication`
- narrow the presentation-layer gloss requirement into a softer layout preference in `answer-presentation`
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior that treats metaphor-heavy internal shorthand as an acceptable default explanation style when a direct action/result statement would be clearer
