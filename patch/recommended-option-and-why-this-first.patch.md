# Recommended Option and Why-This-First Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.5
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch refines how Claude should present multiple next actions when one path is already better-supported than the others.

Why this change matters:
- the continuation-first refinement already reduced unnecessary option prompting
- but when options are still genuinely needed, the answer can still make the user do extra inference if it lists choices without clearly saying which one is recommended first
- a small recommendation-format refinement keeps user choice available while making the preferred path easier to understand and act on

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../explanation-quality.md`
- `../answer-presentation.md`

Review concern:
- the refinement should improve option clarity without reintroducing option-heavy interruption or making recommendation wording arbitrary instead of evidence-backed

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` next-action wording owner
- **Change type:** replacement

**Before**
```text
When multiple reasonable next actions exist, the rule allows short explicit options, but it does not yet require a clearly marked recommended path when one option is better-supported.
```

**After**
```text
When multiple reasonable next actions are shown and one path is better-supported, the rule names that path first as `Recommended` and follows it with a short plain-language `Why this first` reason.
```

### Change Item 2
- **Target location:** `explanation-quality` recommendation-heavy endings
- **Change type:** additive

**Before**
```text
Explanation-quality allows options when multiple next paths are real, but the ending examples do not yet show the preferred path plus a brief why-first rationale.
```

**After**
```text
Explanation-quality reinforces the same structure in explanation-heavy endings: if multiple next paths are shown and one is stronger, make that recommendation explicit and explain briefly why it should happen first.
```

### Change Item 3
- **Target location:** `answer-presentation` option-rich layout patterns
- **Change type:** additive

**Before**
```text
Answer-presentation supports comparison and next-stage layouts, but does not yet expose a preferred house-style label set for recommended-option blocks.
```

**After**
```text
Answer-presentation adds a clearer layout shape for option-rich answers using:
- `Recommended`
- `Why this first`
- `Other options`
```

---

## 4) Verification

- [ ] `accurate-communication` clearly owns recommendation-plus-reason wording when multiple options are shown
- [ ] `explanation-quality` reinforces the same pattern without taking over the owner role
- [ ] `answer-presentation` provides a clearer scannable layout for the pattern
- [ ] the refinement does not reintroduce option-first interruption drift

---

## 5) Rollback Approach

If the refinement proves too rigid:
- keep the recommendation-first behavior in `accurate-communication`
- relax the exact label wording in `answer-presentation` to house-style guidance rather than strong presentation preference
- do not revert to unranked multi-option endings when one path is already better-supported by the checked reasoning
