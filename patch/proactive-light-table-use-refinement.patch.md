# Proactive Light-Table Use Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/answer-presentation.design.md](../design/answer-presentation.design.md) v1.25
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes light tables more proactively usable in RULES explanations.

Why this matters:
- the current active doctrine already allows tables, but its wording still biases too strongly toward comparison-only or narrowly structured-fact use
- explanations can become easier to scan when several fields, states, facts, or distinctions are visible side by side
- the refinement should make table use more proactive without pushing the system into heavy or forced table formatting everywhere

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
- `../changelog/changelog.md`

Review concern:
- broaden table use enough that explanations become easier to scan without reviving a table-for-everything posture
- preserve numbered-list-first behavior for sequence and prose-first behavior for mechanism / implication where cells would reduce readability

---

## 3) Change Items

### Change Item 1
- **Target location:** `answer-presentation`
- **Change type:** additive

**Before**
```text
The active presentation owner allowed tables mostly for genuine comparison or structured facts, while the trigger wording remained conservative enough that tables were often underused unless explicitly requested.
```

**After**
```text
The active presentation owner now encourages light tables more proactively when side-by-side structure materially improves comprehension for analytical clarification, diagnostic fact sets, multi-field explanation, or structured distinctions.
```

### Change Item 2
- **Target location:** `explanation-quality`
- **Change type:** additive

**Before**
```text
The active explanation-flow owner still treated tables mainly as comparison-oriented, with list-first fallbacks dominating other explanation shapes.
```

**After**
```text
The active explanation-flow owner now allows light tables for multi-field clarification and diagnostic explanation when side-by-side scanability helps, while still preserving list-first sequence behavior and prose for mechanism / implication.
```

### Change Item 3
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master surfaces did not yet record this bounded proactive-table refinement wave.
```

**After**
```text
Master/design/history surfaces now record the proactive light-table refinement coherently without reviving a separate first-class table-owner system.
```

---

## 4) Verification

- [x] `answer-presentation` now explicitly allows more proactive light-table use when side-by-side structure materially improves comprehension
- [x] `explanation-quality` no longer reads as effectively comparison-table-only
- [x] numbered-list-first behavior for sequence remains intact
- [x] prose for mechanism / implication remains intact
- [x] touched master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve light-table support for comparison and small structured fact sets
- narrow proactive-table wording before removing it entirely
- do not roll back into a state where table use becomes so conservative that analytical and diagnostic explanations routinely stay harder to scan than necessary
