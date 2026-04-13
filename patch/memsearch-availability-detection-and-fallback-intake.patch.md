# Memsearch Availability Detection and Fallback Intake Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md) v1.4
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes receive-side recall intake explicitly detect whether memsearch-style optional recall extensions are available before relying on them.

Why this change matters:
- optional recall layers are plugin extensions and may or may not exist in the current environment
- a receiving session should not assume memsearch availability from prior sessions or prior machines
- the intake path should use memsearch when present, but should fall back immediately when it is absent or the availability/probe step fails
- optional-recall absence should not become a blocker for task intake or continuation

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../shared-execution-coordination.md`
- `../memory-governance-and-session-boundary.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the new wording should add explicit availability/probe behavior without turning optional recall into required infrastructure
- fallback wording should remain immediate and low-drama rather than creating an unnecessary failure workflow for a missing optional extension

---

## 3) Change Items

### Change Item 1
- **Target location:** `shared-execution-coordination` primary owner
- **Change type:** additive

**Before**
```text
The coordination owner already said optional memsearch may be used when available and should not outrank stronger execution surfaces, but it did not yet explicitly tell receive-side intake to check whether the extension is actually available before assuming it exists.
```

**After**
```text
The coordination owner now explicitly says receive-side continuation should check whether memsearch is available before relying on it, and should fall back immediately to native memory plus checked execution surfaces when the extension is absent or the probe step fails.
```

### Change Item 2
- **Target location:** `memory-governance-and-session-boundary` optional recall companion
- **Change type:** additive

**Before**
```text
The memory-governance chain already treated memsearch-like layers as optional supplemental context bridges, but it did not yet explicitly say that availability must be checked rather than assumed from prior sessions or prior machines.
```

**After**
```text
The memory-governance chain now explicitly says receive-side optional recall should check extension availability first, and should fall back immediately when the extension is unavailable or the availability/probe step fails.
```

---

## 4) Verification

- [x] `shared-execution-coordination` explicitly defines availability/probe-first behavior before optional memsearch use
- [x] `shared-execution-coordination` explicitly defines immediate fallback when the optional extension is absent or probe fails
- [x] `memory-governance-and-session-boundary` reinforces the same optional-extension availability boundary
- [x] optional recall remains supplemental and does not become required infrastructure
- [x] master design/README/TODO/changelog/phase surfaces record wave `040` coherently
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too procedural:
- keep the availability-first and immediate-fallback protections intact while narrowing wording detail before removing the refinement entirely
- preserve the optional-extension boundary so missing memsearch does not become a workflow blocker
- preserve the patch and phase history instead of silently erasing the refinement wave
