# Rules-First Over Memory and Portable Support Artifacts Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md) v2.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that closes two related workflow failures:
- the assistant treating a user-declared RULES-first issue like a memory-first problem
- reusable support/package artifacts such as plugin-owned docs, scripts, skills, or agents drifting into machine-specific absolute paths as if they were portable source contracts

Why this change matters:
- the user explicitly said these issues should be fixed in RULES, not mainly through memory
- the existing portability owners already guarded public onboarding/install docs and shared artifacts, but support/package source artifacts needed a clearer portable-by-default boundary
- the authority model already preserved fresh user directives, but it did not yet state strongly enough that RULES-first should beat memory-first when the user explicitly names that governing basis

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../authority-and-scope.md`
- `../portable-implementation-and-hardcoding-control.md`
- `../project-documentation-standards.md`
- `../document-consistency.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should strengthen RULES-first behavior without suppressing legitimate memory use for unrelated historical preference/context cases
- the portability extension should keep support/package source artifacts portable by default without blocking valid local execution paths used only during a current tool run

---

## 3) Change Items

### Change Item 1
- **Target location:** `authority-and-scope` authority owner
- **Change type:** additive

**Before**
```text
The chain already treated fresh user directives as authoritative, but it did not yet explicitly say that if the user declares a problem should be solved in RULES rather than memory, the assistant must not use a memory write as the substitute remedy for that same issue.
```

**After**
```text
The chain now explicitly requires RULES refinement to be the primary path when the user says the issue belongs in RULES rather than memory.
Memory may not be used as the substitute fix for that same issue.
```

### Change Item 2
- **Target location:** `portable-implementation-and-hardcoding-control` portability owner
- **Change type:** additive

**Before**
```text
The chain already governed shared artifacts and public onboarding/install docs, but it did not yet call out plugin-owned docs, scripts, skills, and agents clearly enough as portable source artifacts when they are maintained for reuse.
```

**After**
```text
The chain now explicitly treats support/package source artifacts such as plugin-owned docs, scripts, skills, and agents as portable-by-default when they are maintained as reusable source artifacts.
It also flags workstation-specific absolute paths embedded into such source artifacts as a distinct portability failure class.
```

### Change Item 3
- **Target location:** `project-documentation-standards` repository-role owner
- **Change type:** additive

**Before**
```text
The chain already modeled `plugin/**` as a support / extension layer, but it did not yet state clearly enough that those package-local source artifacts must also remain portable by default when they are maintained as reusable source content.
```

**After**
```text
The chain now makes that portability boundary explicit for package-local support assets such as optional skills, agents, scripts, and plugin-owned docs.
```

### Change Item 4
- **Target location:** `document-consistency` reference-role owner
- **Change type:** additive

**Before**
```text
The chain already separated source-side references from destination/runtime references, but it did not yet explicitly separate local execution paths from reusable source-artifact references.
```

**After**
```text
The chain now distinguishes local execution paths used only for the current machine or harness turn from reusable source-artifact references, so tool-local paths do not silently become skill/plugin/source contracts.
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record this bounded rules-first / portable-support-artifact refinement wave.
```

**After**
```text
Master governance surfaces now record the new bounded refinement wave, and the touched runtime rules can be reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `authority-and-scope` explicitly keeps user-declared RULES-first handling above memory-first convenience for the same issue
- [ ] `portable-implementation-and-hardcoding-control` explicitly treats reusable support/package source artifacts as portable-by-default
- [ ] `project-documentation-standards` explicitly keeps package-local support assets portable by default when they are reusable source artifacts
- [ ] `document-consistency` explicitly separates local execution paths from reusable source-artifact references
- [ ] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the RULES-first-over-memory rule in `authority-and-scope`
- narrow the support/package-artifact portability extension to the most reusable package-owned source surfaces only
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior that lets memory writes substitute for a user-declared RULES-first fix or lets local execution paths silently become portable source contracts
