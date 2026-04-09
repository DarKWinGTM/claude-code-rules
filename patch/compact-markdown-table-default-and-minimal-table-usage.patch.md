# Compact Markdown Table Default and Minimal Table Usage Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/answer-presentation.design.md](../design/answer-presentation.design.md) v1.16
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that standardizes answer-table behavior around a lighter and more economical default.

Why this change matters:
- the user wants tables to remain available because they can improve understanding, but wants them to be less heavy and less decorative
- the current RULES set already says tables are for real comparison or structured facts, but it did not yet say directly that compact markdown tables are the default table form or that full-frame ASCII / boxed tables should not be the default answer shape
- official guidance converges on the same direction: use tables for structured/comparison content, not for cosmetic neatness, and prefer lists when a list is enough

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../answer-presentation.md`
- `../explanation-quality.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should preserve real table use for comparison and structured facts
- it should reduce unnecessary visual weight without turning every structured block back into prose
- it should keep `flow-diagram-no-frame.md` out of primary ownership because this wave is about ordinary answer tables, not diagrams

---

## 3) Change Items

### Change Item 1
- **Target location:** `answer-presentation` primary owner
- **Change type:** additive

**Before**
```text
The chain already said tables are only for genuine comparison or structured facts, but it did not yet explicitly standardize compact markdown tables as the default table form or reject full-frame ASCII/boxed tables as the ordinary default answer-table shape.
```

**After**
```text
The chain now explicitly prefers compact markdown tables when a table is genuinely useful, rejects full-frame ASCII / boxed tables as the default ordinary answer-table shape, and makes list-first alternatives explicit for sequence and simple status pairs.
```

### Change Item 2
- **Target location:** `explanation-quality` supporting owner
- **Change type:** additive

**Before**
```text
The chain already limited comparison tables to real comparison situations, but it did not yet explicitly connect that rule to compact markdown tables or say directly that sequence/simple-status explanations should prefer list-based forms instead of heavier tables.
```

**After**
```text
The chain now explicitly says compact markdown tables are the default when a table is justified and that sequence/simple-status content should prefer numbered lists or bullets unless side-by-side scan materially helps.
```

### Change Item 3
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded compact-table refinement wave.
```

**After**
```text
Master governance surfaces now record the new bounded refinement wave, and the touched runtime rules can be reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [x] `answer-presentation` explicitly standardizes compact markdown tables as the default table form when a table is materially useful
- [x] `answer-presentation` explicitly rejects full-frame ASCII / boxed tables as the default ordinary answer-table shape
- [x] `answer-presentation` explicitly prefers lists for sequence and simple status pairs when table structure adds little
- [x] `explanation-quality` explicitly reinforces compact-table choice and list-first alternatives in explanation flow
- [x] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the rule that tables are only for real comparison or structured facts
- narrow example/anti-pattern language before removing the compact-table default entirely
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to a default where ordinary structured facts are presented in heavier boxed tables when compact markdown tables or lists would do the job more clearly
