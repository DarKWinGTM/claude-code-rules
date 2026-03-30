# Phase Linkage Hardening Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.7
> **Target Rule:** [../phase-implementation.md](../phase-implementation.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the narrow RULES refinement that hardens explicit phase-to-patch linkage without rewriting the broader phase/patch model.

Target artifacts:
- `phase-implementation.md`
- `design/phase-implementation.design.md`
- `project-documentation-standards.md`
- `design/project-documentation-standards.design.md`
- `phase-implementation-template.md`

Why the change mattered:
- phase-first startup behavior was already strong enough
- patch semantics were already defined strongly enough
- the remaining gap was that patch participation in phased work could still remain too implicit inside the live phase workspace

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../phase-implementation-template.md`
- `../design/phase-implementation.design.md`
- `../design/project-documentation-standards.design.md`

Review concern:
- the refinement should stay narrow
- it should harden explicit phase-to-patch linkage without creating a reverse-link requirement from patch back to phase across the whole system

---

## 3) Change Items

### Change Item 1
- **Target location:** `phase-implementation.md` → source-input synthesis and field contract
- **Change type:** additive

**Before**
```markdown
Phase planning may consume patch artifacts when patch-derived work matters, but the live phase workspace did not yet require explicit declaration of that linkage strongly enough.
```

**After**
```markdown
When phased work uses a governed patch artifact, `phase/SUMMARY.md` and the relevant child phase files must declare that linkage explicitly.
Use `none` only when patch is truly not required, not as a placeholder for an unresolved decision.
```

### Change Item 2
- **Target location:** `project-documentation-standards.md` → repository verification model
- **Change type:** additive

**Before**
```markdown
The repository role model separated phase and patch correctly, but did not explicitly verify live phase-to-patch linkage as a checklist item.
```

**After**
```markdown
The repository verification model now checks that phased work with governed patch artifacts shows explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files.
```

### Change Item 3
- **Target location:** `phase-implementation-template.md` → helper guidance
- **Change type:** additive

**Before**
```markdown
The helper explained patch as an optional source input, but did not teach explicit phase-to-patch declaration strongly enough.
```

**After**
```markdown
The helper now teaches that when patch is in scope, `phase/SUMMARY.md` and the relevant child phase files should name the applicable patch explicitly.
```

---

## 4) Verification

- [ ] Confirm `phase-implementation.md` now makes explicit phase-to-patch linkage a live workspace requirement when patch is in scope
- [ ] Confirm `project-documentation-standards.md` now checks for explicit patch linkage in phased work
- [ ] Confirm the helper template teaches the same expectation
- [ ] Confirm the change does not create a broad reverse-link requirement from patch back to phase

---

## 5) Rollback Approach

If this refinement is judged too strong:
- keep the corrected patch model and startup artifact gate intact
- narrow only the explicit linkage wording
- preserve the workspace-proven principle that patch participation in phased work should not remain implicit when patch is materially in scope
