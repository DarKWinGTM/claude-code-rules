# Table Format and Usage Centralization Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/table-format-and-usage.design.md](../design/table-format-and-usage.design.md) v1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded governance wave that turns table semantics into a first-class centralized RULES owner.

Why this change matters:
- the user wants table behavior to be clear enough for consistent enforcement
- table semantics currently remain split across `answer-presentation` and `explanation-quality`
- the selected light plain aligned no-frame table style should have one primary owner instead of several partial owners
- memory must not influence table doctrine beyond the governing RULES contract

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../answer-presentation.md`
- `../explanation-quality.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- centralization must be real ownership transfer, not just a new file layered on top of old owners
- adjacent chains should still mention table behavior where relevant, but only in defer/reference form
- the change should improve consistency without letting the new rule overreach into all layout or explanation concerns

---

## 3) Change Items

### Change Item 1
- **Target location:** new first-class central owner
- **Change type:** additive

**Before**
```text
Ordinary answer-table semantics were split across adjacent presentation and explanation owners.
```

**After**
```text
A new first-class `table-format-and-usage` rule chain owns ordinary answer-table usage, default style, list-versus-table boundary, and table anti-pattern semantics.
```

### Change Item 2
- **Target location:** `answer-presentation` owner boundary
- **Change type:** replacement

**Before**
```text
`answer-presentation` held the primary ordinary answer-table style guidance and list-versus-table detail directly.
```

**After**
```text
`answer-presentation` now keeps broader layout/scanability ownership, but defers ordinary answer-table semantics to `table-format-and-usage`.
```

### Change Item 3
- **Target location:** `explanation-quality` owner boundary
- **Change type:** replacement

**Before**
```text
`explanation-quality` held explanation-side comparison-table style and table-versus-list detail directly.
```

**After**
```text
`explanation-quality` now keeps explanation-flow ownership, but defers explanation-side table semantics to `table-format-and-usage`.
```

### Change Item 4
- **Target location:** master governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record a centralized table owner, and the runtime install set did not include one.
```

**After**
```text
Master governance surfaces record the new centralized table owner, and the runtime install set includes `table-format-and-usage.md` with parity-checked installed copies.
```

---

## 4) Verification

- [ ] `table-format-and-usage.md` exists as the first-class owner of ordinary answer-table semantics
- [ ] `answer-presentation` now defers ordinary answer-table ownership instead of holding the full doctrine directly
- [ ] `explanation-quality` now defers explanation-side table semantics instead of holding the full doctrine directly
- [ ] the selected light plain aligned no-frame style remains the default ordinary answer-table form
- [ ] boxed/full-frame and generic markdown-pipe ordinary defaults remain disallowed
- [ ] sequence and simple status content still keep lighter non-table alternatives
- [ ] master design/README/TODO/changelog/phase surfaces record the new centralized rule chain coherently
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the centralization proves too broad:
- keep the new rule chain as the owner candidate long enough to evaluate the overlap clearly
- narrow adjacent defer/reference wording first instead of deleting the central owner immediately
- preserve the centralization patch and phase history rather than silently erasing the wave
- do not revert to a state where table ownership becomes ambiguous again across several chains
