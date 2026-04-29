# Runtime Destination Adjacent Owner Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.73
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P074-01 updated `authority-and-scope.md` so runtime co-location is not ownership authority. P074-02 deliberately excludes `authority-and-scope.md` and extends the same boundary into adjacent active runtime owners that already govern repository document roles, hygiene/junk classification, and reference terminology.

This patch separates the two work types:

### Runtime active rule changes

These are behavior/semantic rule changes:
- `project-documentation-standards.md`
- `strict-file-hygiene.md`
- `document-consistency.md`

### Development docs / governed record sync only

These are companion record updates only, not runtime-rule improvement targets:
- paired `design/*.design.md`
- paired `changelog/*.changelog.md`
- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `phase/phase-074-02-sync-runtime-destination-boundary-adjacent-owners.md`
- `patch/runtime-rules-semantic-compression-inventory.patch.md`

---

## 2) Analysis

Risk level: Medium

Dependencies:
- P074-01 completed `authority-and-scope.md` runtime co-location non-ownership boundary.
- P073-08 completed runtime install/parity for the 41 README-installed active runtime files.
- `~/.claude/rules/` can contain runtime rules owned by other projects/plugins.

Review concerns:
- Do not edit `authority-and-scope.md` in this phase.
- Do not treat README, TODO, phase, patch, design, or changelog files as active runtime rule targets.
- Do not change the 41-file active runtime install list.
- Do not classify, manage, or delete other project/plugin runtime files in the shared destination.

---

## 3) Change Items

### RDOA-001 — `project-documentation-standards.md` runtime boundary

- **Target artifact:** `../project-documentation-standards.md`
- **Target locations:** `## Role Boundaries`, `## New or Unclear File Classification`, `## Public Onboarding and Install Guidance`, verification checklist
- **Change type:** additive

**Before**
```text
Runtime installs should target active runtime rule files only, and governed planning/support surfaces are not runtime-rule install targets.
```

**After**
```text
Runtime installs target the current project/source-owned active runtime rule files only. Shared runtime destinations may contain other project/plugin-owned runtime rules that remain out of scope unless their owner/project is explicitly selected or verified.
```

**Preserved behavior**
- Design/changelog/TODO/phase/patch/support surfaces remain companion governance/support records, not runtime install targets.
- Startup artifact posture and document-role boundaries remain unchanged.

### RDOA-002 — `strict-file-hygiene.md` shared destination non-member boundary

- **Target artifact:** `../strict-file-hygiene.md`
- **Target locations:** `## Rule Statement`, `## Core Contract`, `## Allowed vs Not Allowed`, decision flow, verification checklist
- **Change type:** additive

**Before**
```text
Hygiene blocks junk creation and duplicate artifacts, and hygiene/cleanup/isolation is not deletion authority.
```

**After**
```text
A destination/runtime file outside the current source-owned install set is not junk by default merely because it is co-located in a shared runtime destination.
```

**Preserved behavior**
- Hygiene remains primarily creation/duplication control.
- File removal still requires stronger semantic authority and destructive confirmation.

### RDOA-003 — `document-consistency.md` runtime ownership vocabulary

- **Target artifact:** `../document-consistency.md`
- **Target locations:** rule statement, consistency requirements, reference types, verification triggers, verification flow, cross-section validation
- **Change type:** additive

**Before**
```text
The rule distinguishes source-side install paths, destination/runtime paths, local execution paths, checked local facts, and portable references.
```

**After**
```text
The rule also distinguishes source-owned active runtime files, shared runtime destinations, and other-owner runtime files so wording does not blur parity scope with destination-directory ownership.
```

**Preserved behavior**
- Existing source/destination notation remains intact.
- Reference checks and scoped non-finding discipline remain unchanged.

### RDOA-004 — Paired design/changelog sync

- **Target artifacts:** paired design/changelog files for the three touched runtime owners
- **Change type:** companion sync only

**Before**
```text
Companion records do not yet describe the adjacent-owner runtime destination boundary.
```

**After**
```text
Companion records describe the same target state and version history for the three runtime owner changes.
```

### RDOA-005 — Master records and P073 patch-inventory sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../patch/runtime-rules-semantic-compression-inventory.patch.md`
- **Change type:** companion sync only

**Before**
```text
Master and P073 records describe P074-01's authority owner but do not yet record P074-02's adjacent-owner reinforcement.
```

**After**
```text
Master and P073 records distinguish runtime active rule changes from development docs/governed record sync, preserve the 41-file parity scope, and add a runtime destination ownership golden scenario to the P073 patch inventory.
```

Golden scenario to add:
```text
Runtime destination ownership scenario: a plugin/project-owned runtime rule may exist in `~/.claude/rules/` outside the Main RULES 41-file install set; it remains out of scope and is not a cleanup target unless its owning project/plugin is explicitly selected.
```

---

## 4) Verification

- [x] `authority-and-scope.md` is not edited in P074-02.
- [x] Only the three listed active runtime rule files receive runtime behavior/semantic changes.
- [x] Development docs/governed record changes are clearly companion sync only.
- [x] README active runtime install list remains 41 files.
- [x] `TODO.md`, `README.md`, `phase/SUMMARY.md`, design, changelog, phase, and patch files are not described as runtime rule targets.
- [x] Runtime install copies only the 41 active runtime rule files.
- [x] Source/runtime parity passes for the active runtime install set.
- [x] Other project/plugin runtime files in the destination remain untouched.

---

## 5) Rollback Approach

If P074-02 proves too broad:
- revert only the three adjacent runtime owner changes and their companion record entries
- preserve P074-01 `authority-and-scope.md` unless that phase is separately challenged
- keep the core boundary that runtime destination co-location does not imply current source/project ownership
- do not delete or manage destination/runtime files outside the current source-owned install set as part of rollback
