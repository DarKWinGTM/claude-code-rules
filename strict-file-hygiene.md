# Strict File Hygiene Rule

> **Current Version:** 1.2
> **Design:** [design/strict-file-hygiene.design.md](design/strict-file-hygiene.design.md) v1.2
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/strict-file-hygiene.changelog.md](changelog/strict-file-hygiene.changelog.md)

---

## Rule Statement

**Core Principle: Prevent unnecessary junk files and duplicate artifacts, while explicitly allowing required governed startup artifacts when `artifact-initiation-control` determines they must exist now.**

---

## Core Principles

### 1) Existing-File-First Principle
If a file already exists and remains the right authority, edit it instead of creating a duplicate.

### 2) No-Junk-Docs Principle
Do not create unnecessary summaries, duplicate plans, checkpoint files, or version-suffixed copies.

### 3) Ask-When-Unclear Principle
If document necessity is unclear, ask instead of creating speculative files.

### 4) Governed-Startup Exception Principle
Required startup artifacts resolved through `artifact-initiation-control` are not junk files.

Required guidance:
- governed design / changelog / TODO / phase / patch artifacts may be created proactively when the startup contract clearly requires them
- if startup artifact need is still ambiguous, ask immediately rather than silently skipping or drifting
- this exception applies only to required governed startup artifacts, not to arbitrary summaries or duplicate docs

### 5) Version-Suffix Hygiene Principle
Do not create versioned filename copies such as `-v2`, `_final`, `_backup`, or similar unless the user explicitly requests them.

---

## Allowed vs Not Allowed

### Allowed
- functional code/config required for system operation
- documents explicitly requested by the user
- required governed startup artifacts resolved through `artifact-initiation-control`
- temporary files in `/tmp` when they are intentionally short-lived

### Not allowed
- versioned copies such as `file-v2`, `_final`, `_draft`, `_backup`, `_old`
- checkpoint/summary/plan files not requested and not required by startup governance
- work-summary / change-summary files that are neither requested nor required
- duplicate authority artifacts when an existing file already serves the role

---

## Operational Rules

1. **Existing file first**: If the right authority file already exists, edit it.
2. **Ask when unclear**: If artifact necessity is unclear, ask first.
3. **Startup-governance exception**: If `artifact-initiation-control` says the artifact is required now, creation is allowed.
4. **State brief reason**: If creating a governed startup artifact, keep the reason explicit in the work narrative.

---

## Decision Flow

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

## Verification Checklist

- [ ] Existing authority files are reused instead of duplicated
- [ ] No junk summary/checkpoint/version-copy files are introduced
- [ ] Required governed startup artifacts are not blocked by hygiene
- [ ] Ambiguous artifact need is handled by asking, not by drifting

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Duplicate files | 0% |
| Unrequested junk docs | 0% |
| File relevance | 100% |
| Governed startup artifact false blocks | 0 critical cases |

---

## Integration

Related rules:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup artifact posture owner
- [project-documentation-standards.md](project-documentation-standards.md) - repository document-role model
- [no-variable-guessing.md](no-variable-guessing.md) - do not guess required file identities
- [authority-and-scope.md](authority-and-scope.md) - user authority remains decisive

---

> **Full history:** [changelog/strict-file-hygiene.changelog.md](changelog/strict-file-hygiene.changelog.md)
