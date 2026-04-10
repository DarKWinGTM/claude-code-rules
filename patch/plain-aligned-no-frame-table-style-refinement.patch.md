# Plain Aligned No-Frame Table Style Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/answer-presentation.design.md](../design/answer-presentation.design.md) v1.18
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that corrects the default table style used by the answer presentation and explanation owners.

Why this change matters:
- the user clarified that the real issue is table style, not reducing table usage in general
- the current owner wording still over-specifies `compact markdown pipe table` language that does not match the chosen house style
- the selected style is a light plain aligned no-frame table that remains table-shaped without becoming boxed or visually heavy

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
- the refinement should correct style without turning into a doctrine that discourages tables in general
- list-first alternatives should remain intact for sequence and simple status content

---

## 3) Change Items

### Change Item 1
- **Target location:** `answer-presentation` primary owner
- **Change type:** replacement

**Before**
```text
The owner chain said to prefer a compact markdown pipe table by default when a table is useful.
```

**After**
```text
The owner chain now explicitly prefers a light plain aligned no-frame table by default when a table is useful.
```

### Change Item 2
- **Target location:** `explanation-quality` supporting owner
- **Change type:** replacement

**Before**
```text
The explanation chain said that when a table is justified, the default table form should be a compact markdown table.
```

**After**
```text
The explanation chain now aligns to the same light plain aligned no-frame table style while preserving real comparison-table usage.
```

### Change Item 3
- **Target location:** canonical examples and anti-pattern wording
- **Change type:** additive

**Before**
```text
The current examples and anti-patterns reject boxed/full-frame tables, but they do not yet anchor the chosen plain aligned no-frame house style strongly enough.
```

**After**
```text
The touched owners now include a canonical plain aligned no-frame table example and clearer wording that the problem is boxed/heavy framing, not table usage itself.
```

### Change Item 4
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded table-style correction wave.
```

**After**
```text
Master governance surfaces now record the new bounded refinement wave, and the touched runtime rules can be reinstalled into `~/.claude/rules/` so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `answer-presentation` explicitly prefers the chosen light plain aligned no-frame table style when a table is genuinely useful
- [ ] `explanation-quality` explicitly aligns to the same chosen style for real comparison-table cases
- [ ] boxed/full-frame table defaults remain disallowed
- [ ] sequence and simple status content still keep list-first alternatives
- [ ] master design/README/TODO/changelog/phase surfaces record the bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the rejection of boxed/full-frame table defaults
- narrow the style-specific wording before removing the chosen plain aligned no-frame default entirely
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to a state where the default style is described vaguely enough that the wrong table form is repeatedly chosen
