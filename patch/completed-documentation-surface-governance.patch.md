# Completed Documentation Surface Governance Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.76
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P077 responds to large-project documentation scan bloat: completed phase, patch, and changelog details can become useful history but noisy active context.

พูดง่าย ๆ: งานที่เสร็จแล้วควรออกจาก active scan ได้ แต่ต้องไม่กลายเป็นขยะ ไม่ถูกลบโดยอัตโนมัติ และยังต้อง trace กลับได้เมื่อต้อง audit/rollback/history.

This patch keeps the change narrow:
- `project-documentation-standards.md` owns the repository-wide completed documentation surface model.
- `phase-implementation.md` owns `phase/done/` semantics.
- `document-patch-control.md` owns `patch/done/` semantics.
- `document-changelog-control.md` owns `changelog/done/` semantics.
- `document-design-control.md` owns the no-default-`design/done/` boundary.

This is a non-code governance patch. It changes documentation/rule semantics only; no application code or runtime install destination files are modified by this patch.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `document-design-control.md` already defines design as active target-state truth.
- `document-changelog-control.md` owns version authority and history behavior.
- `phase-implementation.md` owns live phase workspace semantics.
- `document-patch-control.md` owns patch/review artifact semantics.
- `project-documentation-standards.md` owns the repository document-role model.
- `strict-file-hygiene.md` and `functional-intent-verification.md` already prevent cleanup/deletion from being inferred from hygiene or completion status.

Review concerns:
- Do not make `done/` mean deletion, junk, or disposal authority.
- Do not let `phase/done/` replace `phase/SUMMARY.md` or the live phase namespace.
- Do not let `patch/done/` become active phase input by default.
- Do not let `changelog/done/` replace active changelog version authority.
- Do not introduce a default `design/done/` pattern because design remains active blueprint and target-state authority.
- Do not broaden runtime install scope; active runtime install remains the README-listed 41 root rule files.

---

## 3) Change Items

### CDSG-001 — Repository-wide completed documentation surface model

- **Target artifact:** `../project-documentation-standards.md`
- **Target design:** `../design/project-documentation-standards.design.md`
- **Change type:** additive / restructuring

**Before**
```text
Project documentation standards defined README, design, changelog, TODO, phase, patch, helper, and support roles, but did not define inactive completed-history surfaces for scan-bloat control.
```

**After**
```text
Completed documentation surfaces are first-class inactive history surfaces:
- phase/done/ for completed phase execution detail
- patch/done/ for completed patch/review artifacts
- changelog/done/ for older or completed detailed version history
- no default design/done/ because design remains active blueprint authority
```

**Preserved behavior**
- Current-state scans start from active surfaces.
- `done/` surfaces are opened only for history, audit, rollback, provenance, or trace reconstruction.
- Files in `done/` are not junk and completed status is not deletion authorization.

### CDSG-002 — Design remains active blueprint authority

- **Target artifact:** `../document-design-control.md`
- **Target design:** `../design/document-design-control.design.md`
- **Change type:** additive

**Before**
```text
Design docs were active-state target truth and historical detail belonged in changelog, but the completed-documentation `done/` boundary for design was not explicit.
```

**After**
```text
Governed design docs stay active blueprint and target-state authority. Do not introduce a default design/done/ pattern; move historical explanation through changelog governance instead.
```

**Preserved behavior**
- Design remains current implementation-relevant target-state truth.
- External-doc/spec-derived implementation truth still belongs in design when later work depends on it.
- Active design bodies still exclude audit/remediation/rollout history.

### CDSG-003 — Completed changelog history surface

- **Target artifact:** `../document-changelog-control.md`
- **Target design:** `../design/document-changelog-control.design.md`
- **Change type:** additive / restructuring

**Before**
```text
Active changelogs owned governed version/history authority, but there was no explicit inactive completed-history surface for older detailed changelog content.
```

**After**
```text
Active changelogs remain current version authority, current index, and navigation surfaces. changelog/done/ may retain older or completed detailed history outside active scans.
```

**Preserved behavior**
- Active changelog remains the authoritative current version surface.
- Moved history remains reachable when trace/audit/rollback requires it.
- Design-specific history stays under changelog governance, not design/done/.

### CDSG-004 — Completed phase history surface

- **Target artifact:** `../phase-implementation.md`
- **Target design:** `../design/phase-implementation.design.md`
- **Change type:** additive

**Before**
```text
/phase was the live execution workspace with SUMMARY.md and active child phase files, but completed phase history placement was not explicit.
```

**After**
```text
phase/done/ may hold completed phase-detail files as inactive-by-default history. Active execution scans start with phase/SUMMARY.md and active child phase files in phase/.
```

**Preserved behavior**
- `phase/SUMMARY.md` remains mandatory when phased planning is used.
- Active child phase files remain in `phase/`.
- `phase/done/` does not replace live phase planning.
- Completed phase history is not deletion authority.

### CDSG-005 — Completed patch history surface

- **Target artifact:** `../document-patch-control.md`
- **Target design:** `../design/document-patch-control.design.md`
- **Change type:** additive / synchronization

**Before**
```text
Active patches lived in patch/<context>.patch.md or root <context>.patch.md. Patch-control metadata also had prior version drift between runtime/design and changelog.
```

**After**
```text
patch/done/<context>.patch.md is allowed as inactive completed patch history. Active patch/review scans start with active patch/<context>.patch.md and root <context>.patch.md surfaces. Patch-control runtime/design/changelog are synchronized through v2.7.
```

**Preserved behavior**
- Patch artifacts remain governed before/after review artifacts outside live phase planning.
- Generic `patch.md` remains disallowed.
- Live phase files still do not belong in patch artifacts.
- Completed patches are not active phase inputs by default.

### CDSG-006 — Master records and README current-state sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-077-01-completed-documentation-surface-governance.md`, this patch file
- **Change type:** companion sync

**Before**
```text
Master records described P076 as the latest governed source state and did not describe completed documentation surface governance.
```

**After**
```text
Master records describe P077/v9.76 as completed documentation surface governance: phase/done/, patch/done/, and changelog/done/ are inactive history surfaces; design/done/ is not a default governed pattern; completed history is not junk or deletion authority.
```

**Preserved behavior**
- README remains a current-state/onboarding surface, not a changelog dump.
- Changelog remains version authority.
- TODO remains durable tracking.
- Source runtime install scope remains the same 41 active root runtime rule files.

---

## 4) Verification

- [x] Runtime rule changes are limited to completed-history semantics and owner-specific boundaries.
- [x] `phase/done/`, `patch/done/`, and `changelog/done/` are inactive by default.
- [x] `design/done/` is not introduced as a default governed design pattern.
- [x] Active design remains target-state truth.
- [x] Active changelog remains current version authority.
- [x] Active phase workspace still starts from `phase/SUMMARY.md` and active child phase files.
- [x] Active patch/review scans still start from active patch/root patch artifacts.
- [x] Completed history is not classified as junk and does not authorize deletion.
- [x] README updates current sections rather than embedding a changelog dump.
- [x] README active runtime install list remains 41 files.
- [x] Source runtime install scope is unchanged.
- [x] No runtime destination files outside the source repo are modified.

---

## 5) Rollback Approach

If P077 proves too broad:
- remove or narrow only the completed-history surface wording in `project-documentation-standards.md`
- remove or narrow owner-specific `phase/done/`, `patch/done/`, and `changelog/done/` language
- keep the no-default-`design/done/` boundary unless the user explicitly selects a different design-history model
- preserve existing active design/changelog/phase/patch authority semantics
- preserve the rule that completed history is not junk and not deletion authorization
- do not change the 41-file active runtime install boundary or delete/manage destination files outside the current source-owned install set
