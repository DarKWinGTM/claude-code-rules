# Strict File Hygiene Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-04-25)

---

## 1) Goal

Prevent unnecessary junk files, duplicate authorities, and version-suffixed file drift, while explicitly allowing required governed startup artifacts and preventing shared runtime destination non-members from being treated as junk by co-location alone.

---

## 2) Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| duplicate versions | confusion about which file is authoritative | edit existing authority file |
| unrequested junk docs | overgrown project and noise | do not create non-required summaries |
| startup governance blocked by hygiene | meaningful governed work drifts without structure | allow governed startup artifacts when required |
| shared runtime destination non-member treated as project junk | other-owner runtime files can be misclassified by co-location alone | resolve owner/project scope before hygiene classification |
| suffix versions | Git history is bypassed | keep standard filenames |

---

## 3) Core Contract

### 3.1 Existing Authority First
If the correct authority file already exists, edit it instead of creating a duplicate.

### 3.2 No-Junk-Artifact Rule
Do not create speculative summaries, checkpoint files, duplicate plans, or version-suffixed copies.

This is a creation/duplication hygiene rule.
It does not by itself authorize deletion of existing, newly encountered, untracked repository files, or destination/runtime files outside the current source-owned install set.

### 3.3 Ask-When-Unclear Rule
If artifact necessity is unclear, ask instead of creating speculative documentation.

### 3.4 Shared-Destination Non-Member Boundary
A destination/runtime file outside the current source-owned active runtime install set is not junk by default merely because it is co-located in a shared runtime destination.

Owner/project scope must be resolved before any junk, cleanup, or deletion classification is considered for such files.

### 3.5 Governed-Startup Exception
Required governed startup artifacts resolved through `artifact-initiation-control` are allowed and are not treated as junk files.

This exception applies to required startup instances of:
- design
- changelog
- TODO
- phase
- patch

It does not authorize arbitrary summary docs or duplicate artifacts.
It also does not authorize deletion of newly encountered files merely because they do not match the assistant's current expected artifact set.

### 3.6 Naming Hygiene Rule
Do not create versioned filenames such as:
- `-v1`, `-v2`
- `_final`, `_draft`
- `_backup`, `_old`
- `.bak` unless explicitly requested for safety

### 3.7 Portable-Artifact Hygiene Rule
Reusable helper/support artifacts should avoid machine-local hardcoded defaults when a portable placeholder or late-bound resolution model should be used instead.

Required guidance:
- shared artifacts should not normalize one machine as the default environment
- machine-local exact values need an explicit machine-scoped reason when they appear in reusable artifacts
- broader anti-hardcoding ownership belongs to `portable-implementation-and-hardcoding-control.md`

---

## 4) Allowed vs Not Allowed

### Allowed
- functional code/config required for system operation
- documents explicitly requested by the user
- required governed startup artifacts resolved through `artifact-initiation-control`
- temporary files in `/tmp` when intentionally short-lived

### Not Allowed
- versioned copies such as `file-v2`, `_final`, `_draft`, `_backup`, `_old`
- checkpoint/summary/plan files not requested and not required by startup governance
- work-summary/change-summary files that are neither requested nor required
- duplicate authority artifacts when an existing file already serves the role
- treating untracked/newly seen files as junk or disposable by cleanup instinct alone
- treating destination/runtime files outside the current source-owned install set as junk merely because they share a runtime directory
- using hygiene, cleanup, isolation, worktree, sandbox, or runtime co-location rationale as deletion authority by themselves

---

## 5) Decision Flow

```text
AI wants to create a file
  ↓
Does the correct authority file already exist?
  → YES: edit the existing file
  → NO: continue
  ↓
Is it functional code/config?
  → YES: create allowed
  → NO: continue
  ↓
Is it a governed startup artifact required now by artifact-initiation-control?
  → YES: create allowed
  → NO: continue
  ↓
Did the user explicitly ask for it?
  → YES: create allowed
  → NO: do not create

AI wants to classify or remove a newly encountered file
  ↓
Is it outside the current source-owned install set in a shared runtime destination?
  → YES: resolve owner/project scope first; do not treat as junk by co-location
  → NO/UNKNOWN: continue
  ↓
Has the file been checked against master surfaces / governed history?
  → NO: check first
  → YES: continue
  ↓
Is there stronger delete authorization than hygiene/cleanup rationale?
  → NO: do not delete
  → YES: follow the destructive-confirmation owner
```

---

## 6) Verification Checklist

- [ ] Existing authority files are reused instead of duplicated
- [ ] No junk summary/checkpoint/version-copy files are introduced
- [ ] Required governed startup artifacts are not blocked by hygiene
- [ ] Ambiguous artifact need is handled by asking, not by drifting
- [ ] Newly encountered files are not treated as disposable before master-surface / governed-history checks
- [ ] Destination/runtime non-members are not treated as junk merely because they sit outside the current source-owned install set
- [ ] Hygiene wording is not usable as standalone deletion authority

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Duplicate files | 0% |
| Unrequested junk docs | 0% |
| File relevance | 100% |
| Governed startup artifact false blocks | 0 critical cases |
| Shared runtime destination non-member false junk classification | 0 critical cases |

---

## 8) Integration

| Rule | Relationship |
|------|-------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup artifact posture owner |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository document-role model |
| [no-variable-guessing.design.md](no-variable-guessing.design.md) | Do not guess required file identities |
| [authority-and-scope.design.md](authority-and-scope.design.md) | User authority and runtime co-location ownership boundary remain decisive |

---

> Full history: [../changelog/strict-file-hygiene.changelog.md](../changelog/strict-file-hygiene.changelog.md)
