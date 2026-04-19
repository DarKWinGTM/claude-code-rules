# Legacy History Authority Boundary Clarification Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.60
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded clarification wave that makes older shared-board / session-title history read as historical context rather than current active RULES authority.

Why this matters:
- the active RULES boundary now keeps general task/phase/language doctrine in Main RULES while coordination-specific session grammar stays outside Main RULES current doctrine
- some older master/history records still describe prior shared-board/session-title refinements in language that can read broader than the current active boundary
- the goal is to clarify the historical reading without rewriting the underlying historical fact that those older waves existed

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`

Review concern:
- the clarification should mark legacy coordination-flavored records as historical only without falsifying or erasing the existing history
- current active doctrine should remain owned by the present RULES runtime/design surfaces rather than by older rollout records
- this wave should stay RULES-side and should not reopen plugin/package edits

---

## 3) Change Items

### Change Item 1
- **Target location:** master design / overview surfaces
- **Change type:** additive

**Before**
```text
The active repository model already separated current governed authority from support/package layers, but it did not yet explicitly say that older coordination-flavored history remains historical context only after the active ownership split.
```

**After**
```text
Master design / overview surfaces now state that older shared-board/session-title rollout records remain historical context only and do not override the current active Main RULES boundary.
```

### Change Item 2
- **Target location:** `TODO.md` and `phase/SUMMARY.md`
- **Change type:** additive

**Before**
```text
Master execution/history surfaces still recorded older coordination-flavored rollout waves, but they did not yet carry a bounded clarification that those records are historical rather than current active authority.
```

**After**
```text
`TODO.md` and `phase/SUMMARY.md` now record a bounded clarification wave so readers can distinguish legacy coordination-history records from the current active RULES authority set.
```

### Change Item 3
- **Target location:** `changelog/changelog.md`
- **Change type:** additive

**Before**
```text
The master changelog did not yet record a dedicated clarification wave for this legacy-history authority boundary.
```

**After**
```text
The master changelog now records a bounded clarification wave stating that older shared-board/session-title records remain historical context only after the active ownership split.
```

---

## 4) Verification

- [x] master design / overview surfaces now state that older coordination-flavored rollout records are historical only
- [x] `TODO.md` and `phase/SUMMARY.md` now carry a bounded clarification rather than leaving the distinction implicit
- [x] `changelog/changelog.md` records the clarification wave coherently
- [x] the clarification does not reopen plugin/package edits or move current active doctrine back into Main RULES history lines

---

## 5) Rollback Approach

If the clarification proves too broad:
- preserve the current active RULES boundary that keeps coordination-specific session grammar outside Main RULES current doctrine
- narrow only the historical-clarification wording
- keep the older history records intact rather than erasing them
- do not roll back into a state where older coordination-flavored history can again be misread as current active Main RULES authority
