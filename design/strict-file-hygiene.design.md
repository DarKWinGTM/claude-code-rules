# Strict File Hygiene Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.2
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-03-28)

---

## 1) Goal

Prevent unnecessary junk files, duplicate authorities, and version-suffixed file drift, while explicitly allowing required governed startup artifacts when startup governance determines they must exist now.

---

## 2) Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| duplicate versions | confusion about which file is authoritative | edit existing authority file |
| unrequested junk docs | overgrown project and noise | do not create non-required summaries |
| startup governance blocked by hygiene | meaningful governed work drifts without structure | allow governed startup artifacts when required |
| suffix versions | Git history is bypassed | keep standard filenames |

---

## 3) Core Contract

### 3.1 Existing Authority First
If the correct authority file already exists, edit it instead of creating a duplicate.

### 3.2 No-Junk-Artifact Rule
Do not create speculative summaries, checkpoint files, duplicate plans, or version-suffixed copies.

### 3.3 Ask-When-Unclear Rule
If artifact necessity is unclear, ask instead of creating speculative documentation.

### 3.4 Governed-Startup Exception
Required governed startup artifacts resolved through `artifact-initiation-control` are allowed and are not treated as junk files.

This exception applies to required startup instances of:
- design
- changelog
- TODO
- phase
- patch

It does not authorize arbitrary summary docs or duplicate artifacts.

### 3.5 Naming Hygiene Rule
Do not create versioned filenames such as:
- `-v1`, `-v2`
- `_final`, `_draft`
- `_backup`, `_old`
- `.bak` unless explicitly requested for safety

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
```

---

## 6) Verification Checklist

- [ ] Existing authority files are reused instead of duplicated
- [ ] No junk summary/checkpoint/version-copy files are introduced
- [ ] Required governed startup artifacts are not blocked by hygiene
- [ ] Ambiguous artifact need is handled by asking, not by drifting

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Duplicate files | 0% |
| Unrequested junk docs | 0% |
| File relevance | 100% |
| Governed startup artifact false blocks | 0 critical cases |

---

## 8) Integration

| Rule | Relationship |
|------|-------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup artifact posture owner |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository document-role model |
| [no-variable-guessing.design.md](no-variable-guessing.design.md) | Do not guess required file identities |
| [authority-and-scope.design.md](authority-and-scope.design.md) | User authority remains decisive |

---

> Full history: [../changelog/strict-file-hygiene.changelog.md](../changelog/strict-file-hygiene.changelog.md)
