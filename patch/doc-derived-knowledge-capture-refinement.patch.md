# Doc-Derived Knowledge-Capture Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/document-design-control.design.md](../design/document-design-control.design.md) v1.9
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes doc-derived knowledge capture explicit across the governed document system.

Why this matters:
- the governed document stack already separates design, phase, patch, TODO, and changelog roles clearly
- but implementation-critical knowledge learned from docs/specs/provider references can still remain trapped in transient reading memory rather than being normalized into governed artifacts
- once the session is compacted or handed off, that missing capture forces unnecessary re-reading and increases the chance of rebuilding the same understanding from scratch
- the repository needs a clearer rule that implementation-relevant extracted knowledge must be externalized into the right governed artifact before or alongside later execution that still depends on it

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../document-design-control.md`
- `../phase-implementation.md`
- `../document-patch-control.md`
- `../execution-continuity-and-mode-selection.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`

Review concern:
- strengthen doc/spec knowledge capture without turning design/phase/patch into copied source-document dumps
- preserve the role split where design owns extracted implementation truth, phase owns live execution consequences, patch owns reviewable change basis, and changelog remains history only

---

## 3) Change Items

### Change Item 1
- **Target location:** `document-design-control`
- **Change type:** additive

**Before**
```text
Document-design-control already enforced active-state-only design bodies, but it did not explicitly require implementation-critical knowledge from external docs/specs to be normalized into design before later multi-step execution depended on it.
```

**After**
```text
Document-design-control now explicitly requires implementation-critical knowledge extracted from external docs/specs/provider references to be normalized into the governed design layer before or alongside later multi-step execution that still depends on it.
```

### Change Item 2
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase-implementation defined the live `/phase` workspace well, but it did not explicitly say strongly enough that phase execution should reuse normalized design truth instead of relying on transient doc-reading memory after compact or handoff.
```

**After**
```text
Phase-implementation now explicitly says the live phase workspace should reuse normalized design truth when external docs/specs materially constrain the implementation, and phase files should make the execution-relevant constraints visible enough that later slices do not need to rediscover them from scratch.
```

### Change Item 3
- **Target location:** `document-patch-control`
- **Change type:** additive

**Before**
```text
Document-patch-control already defined before/after change representation, but it did not explicitly require the external-requirement basis of a change to stay visible enough for review when docs/specs materially constrained the implementation.
```

**After**
```text
Document-patch-control now explicitly requires patch context/analysis to surface the external-requirement basis when that basis materially explains the change surface, while keeping design as the target-state truth layer.
```

### Change Item 4
- **Target location:** `execution-continuity-and-mode-selection`
- **Change type:** additive

**Before**
```text
Execution continuity already knew how to keep work moving, but it did not explicitly stop for required knowledge capture when implementation-critical external knowledge had just been learned and later work would still depend on it.
```

**After**
```text
Execution continuity now includes a capture-before-continue boundary so later multi-step execution does not keep relying on transient doc-reading memory when the knowledge should first be externalized into governed artifacts.
```

### Change Item 5
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master/history surfaces did not yet record this bounded doc-derived knowledge-capture refinement wave.
```

**After**
```text
Master/history surfaces now record the doc-derived knowledge-capture refinement coherently and make it visible that the governed document system is not only for status tracking but also for preserving implementation-relevant truth extracted from external references.
```

---

## 4) Verification

- [x] `document-design-control` now explicitly requires doc-derived implementation truth capture in the governed design layer when later work still depends on it
- [x] `phase-implementation` now explicitly points later execution back to normalized design truth instead of transient doc-reading memory
- [x] `document-patch-control` now explicitly surfaces external-requirement basis when review depends on it
- [x] `execution-continuity-and-mode-selection` now stops for capture before continuing when implementation-critical external knowledge has not yet been externalized
- [x] touched master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve design as the target-state truth owner for extracted external-contract knowledge
- narrow the new capture-before-continue wording before removing it entirely
- preserve patch visibility for externally driven change basis where review still depends on that explanation
- do not roll back into a state where later implementation slices depend routinely on transient doc-reading memory after compact or handoff
