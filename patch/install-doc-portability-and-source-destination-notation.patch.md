# Install-Doc Portability and Source-Destination Notation Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/portable-implementation-and-hardcoding-control.design.md](../design/portable-implementation-and-hardcoding-control.design.md) v1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the refinement wave that turns public onboarding/install path posture into an explicit portability concern rather than leaving it as ad hoc README wording.

Why this change matters:
- cloneable plugin repositories exposed a governance gap where public install docs could still teach one checked workstation path as the default source path
- the older portability owner covered hardcoding broadly, but did not yet foreground public onboarding/install docs strongly enough
- adjacent document and consistency owners also needed explicit support for source-side versus destination/runtime notation

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../portable-implementation-and-hardcoding-control.md`
- `../project-documentation-standards.md`
- `../document-consistency.md`
- `../README.md`
- `../design/design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should strengthen install-doc portability without turning every exact local path into a violation when the path is intentionally a checked local fact or a machine-scoped contract

---

## 3) Change Items

### Change Item 1
- **Target location:** `portable-implementation-and-hardcoding-control` owner scope
- **Change type:** replacement

**Before**
```text
The chain governed portable implementation defaults and anti-hardcoding discipline broadly, but public onboarding/install docs were not yet called out strongly as a first-class portability surface.
```

**After**
```text
The chain explicitly governs public onboarding/install guidance, requires portable source-side guidance by default, and forbids treating one workstation absolute path or internal umbrella workspace root as the public default install path.
```

### Change Item 2
- **Target location:** `project-documentation-standards` README/install-doc enforcement layer
- **Change type:** replacement

**Before**
```text
The repository documentation model required portable shared docs generally, but it did not yet define a clear README/install-doc rule for repo-root source guidance versus destination/runtime notation.
```

**After**
```text
The repository documentation model now requires public onboarding/install docs to:
- prefer repo-root or equivalent portable source guidance when possible
- avoid workstation-specific absolute paths as public defaults
- separate source-side notation from destination/runtime notation
- scope exact local paths explicitly when they are shown as local examples
```

### Change Item 3
- **Target location:** `document-consistency` reference-role model
- **Change type:** replacement

**Before**
```text
Document consistency distinguished portable shared references from checked local facts, but did not yet explicitly model source-side install references versus destination/runtime references.
```

**After**
```text
Document consistency now keeps five roles distinct:
- portable shared references
- source-side install references
- destination/runtime references
- checked local facts
- machine-scoped examples
```

### Change Item 4
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded install-doc portability refinement wave.
```

**After**
```text
Master governance surfaces now record the refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `portable-implementation-and-hardcoding-control` explicitly covers public onboarding/install docs and source-vs-destination notation
- [ ] `project-documentation-standards` explicitly enforces portable README/install-doc defaults
- [ ] `document-consistency` keeps source-side and destination/runtime references distinct
- [ ] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- narrow the portability owner back to shared-artifact defaults while preserving the clearer install-doc wording in the secondary owners where still valid
- keep the patch and phase history rather than silently erasing the wave
- do not revert to teaching one checked workstation path as the public default install model
