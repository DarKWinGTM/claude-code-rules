# Easy Explanation Continuity and Plain Thai Register Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active
> **Target Design:** [../design/explanation-quality.design.md](../design/explanation-quality.design.md) v2.17
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that keeps easy explanations easy all the way through when the user explicitly asks for simpler wording, plain Thai, or less jargon.

Why this change matters:
- the current owner set already supports plain-language openings, human-language glosses, easy-to-picture framing, and direct human-readable rewrites
- but a remaining failure mode still exists where the answer starts simple and then drifts back into internal English labels, abstract system wording, or jargon-heavy headings
- the user explicitly identified that the clearest explanations were the ones that stayed simple through the full answer rather than using one short easy opener and then rebounding into harder wording

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../explanation-quality.md`
- `../accurate-communication.md`
- `../answer-presentation.md`
- `../natural-professional-communication.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should tighten continuity and sequencing, not create a new standalone doctrine chain
- the system should stay accurate and technically honest while keeping plain Thai or human wording as the visible default register when the user explicitly asks for easier explanation

---

## 3) Change Items

### Change Item 1
- **Target location:** `explanation-quality` explanation-flow owner
- **Change type:** additive

**Before**
```text
The chain already required plain-language-first explanation and easy-to-picture openings, but it did not yet explicitly prevent a simple opening from drifting back into jargon-heavy explanation later in the same answer.
```

**After**
```text
The chain now includes an easy-explanation continuity principle so easy explanations stay in plain human language through the full answer, including a short plain-language re-anchor after dense technical blocks.
```

### Change Item 2
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain already supported human-language glosses and direct human-readable wording, but it did not yet explicitly say that a request for easier explanation should persist across the whole answer instead of one short gloss followed by jargon-heavy detail.
```

**After**
```text
The chain now keeps plain Thai or direct human wording as the main register across the whole answer when the user explicitly asks for easier explanation, and requires human-meaning-first headings plus re-anchors after dense technical blocks.
```

### Change Item 3
- **Target location:** `answer-presentation` layout owner
- **Change type:** additive

**Before**
```text
The chain already supported easy-to-picture phase/progress presentation and gloss-near-term layout behavior, but it did not yet provide a dedicated easy-explanation layout pattern that kept plain-language headings visually primary.
```

**After**
```text
The chain now includes an easy-explanation pattern that prefers grouped explanation blocks with plain-language headings and keeps technical labels secondary when the user explicitly asks for simpler wording.
```

### Change Item 4
- **Target location:** `natural-professional-communication` style owner
- **Change type:** additive

**Before**
```text
The chain already rejected metaphor-heavy abstraction as a default professional style, but it did not yet explicitly keep easy explanations in an everyday Thai register across the full answer.
```

**After**
```text
The chain now includes an easy-explanation register principle so plain Thai wording remains the visible default register across the answer instead of drifting back into internal English or abstract system language.
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, phase summary, and runtime install state did not yet record the bounded easy-explanation continuity wave.
```

**After**
```text
Master governance surfaces now record the bounded easy-explanation continuity refinement wave, and the touched runtime rules can be reinstalled into `~/.claude/rules/` so the runtime copies match source authority.
```

---

## 4) Verification

- [ ] `explanation-quality` now keeps easy explanations in plain language through the full answer instead of only at the opening
- [ ] `accurate-communication` now keeps plain Thai / less-jargon requests active across the whole answer
- [ ] `answer-presentation` now supports easy-explanation layouts with plain-language headings
- [ ] `natural-professional-communication` now keeps easy explanations in an everyday Thai register instead of drifting back into abstract system language
- [ ] master design/README/TODO/changelog/phase surfaces record the bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the core easy-explanation continuity rule in `explanation-quality`
- narrow the presentation-layer easy-explanation pattern before weakening the wording owner guidance
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior where a short easy opening is treated as sufficient while the rest of the answer rebounds into jargon-heavy wording
