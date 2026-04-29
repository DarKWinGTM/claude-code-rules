# Strict File Hygiene Rule
> **Current Version:** 1.5
> **Design:** [design/strict-file-hygiene.design.md](design/strict-file-hygiene.design.md) v1.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/strict-file-hygiene.changelog.md](changelog/strict-file-hygiene.changelog.md)
---
## Rule Statement
**Core Principle: Prevent unnecessary junk files and duplicate artifacts, while explicitly allowing required governed startup artifacts when `artifact-initiation-control` determines they must exist now.**
This is a creation/duplication hygiene rule. It does not by itself authorize deletion of existing, newly encountered, untracked repository files, or destination/runtime files outside the current source-owned install set.
---
## Core Contract
### Existing-File-First
If a file already exists and remains the right authority, edit it instead of creating a duplicate.
### No-Junk-Docs
Do not create unnecessary summaries, duplicate plans, checkpoint files, work summaries, or version-suffixed copies.
### Ask when unclear
If document necessity is unclear, ask instead of creating speculative files.
### Shared-destination non-member boundary
A destination/runtime file outside the current source-owned active runtime install set is not junk by default merely because it is co-located in a shared runtime destination.
Resolve owner/project scope before any junk, cleanup, or deletion classification is considered.
### Governed-startup exception
Required startup artifacts resolved through `artifact-initiation-control` are not junk files.
Required guidance:
- governed design / changelog / TODO / phase / patch artifacts may be created proactively when startup clearly requires them
- if startup artifact need is ambiguous, ask immediately rather than silently skipping or drifting
- this exception applies only to required governed startup artifacts, not arbitrary summaries or duplicate docs
- it does not authorize deletion of newly encountered files merely because they do not match the expected artifact set
### Version-suffix hygiene
Do not create filename copies such as `-v2`, `_final`, `_backup`, `_draft`, `_old`, or similar unless the user explicitly requests them.
### Portable-artifact hygiene
Do not create reusable artifacts that embed machine-local defaults when portable placeholder or late-bound resolution should be used.
Required guidance:
- shared helper/support artifacts should avoid machine-specific hardcoded defaults
- exact local values in reusable artifacts need explicit machine scope
- broader portability defers to `portable-implementation-and-hardcoding-control.md`
---
## Allowed vs Not Allowed
Allowed:
- functional code/config required for operation
- documents explicitly requested by the user
- required governed startup artifacts from `artifact-initiation-control`
- intentionally short-lived temporary files in `/tmp`
Not allowed:
- versioned copies such as `file-v2`, `_final`, `_draft`, `_backup`, `_old`
- checkpoint/summary/plan/work-summary files not requested and not required by startup governance
- duplicate authority artifacts when an existing file already serves the role
- treating untracked/newly seen files as junk or disposable by cleanup instinct alone
- treating destination/runtime files outside the current source-owned install set as junk merely because they share a runtime directory
- using hygiene, cleanup, isolation, worktree, sandbox, or runtime co-location rationale as deletion authority by itself
---
## Operational Rules
1. **Existing file first:** if the right authority file already exists, edit it.
2. **Ask when unclear:** if artifact necessity is unclear, ask first.
3. **Startup-governance exception:** if `artifact-initiation-control` requires the artifact now, creation is allowed.
4. **State brief reason:** if creating a governed startup artifact, keep the reason explicit.
5. **Shared destination caution:** destination/runtime non-members need owner/project scope resolution before hygiene classification.
6. **No deletion by hygiene:** file removal needs stronger semantic authority plus the destructive-confirmation owner; hygiene alone is not deletion authorization.
---
## Decision Flow
```text
AI wants to create a file
  ↓
Correct authority file exists?
  → YES: edit existing file
  → NO: continue
  ↓
Functional code/config?
  → YES: create allowed
  → NO: continue
  ↓
Governed startup artifact required now?
  → YES: create allowed
  → NO: continue
  ↓
User explicitly asked for it?
  → YES: create allowed
  → NO: do not create

AI wants to classify/remove a newly encountered file
  ↓
Is it outside the current source-owned install set in a shared runtime destination?
  → YES: resolve owner/project scope first; do not treat as junk by co-location
  → NO/UNKNOWN: continue
  ↓
Checked master surfaces / governed history?
  → NO: check first
  → YES: continue
  ↓
Stronger delete authorization than hygiene/cleanup?
  → NO: do not delete
  → YES: follow destructive-confirmation owner
```
---
## Verification Checklist
- [ ] Existing authority files are reused instead of duplicated
- [ ] No junk summary/checkpoint/version-copy files are introduced
- [ ] Required governed startup artifacts are not blocked by hygiene
- [ ] Ambiguous artifact need is handled by asking, not drifting
- [ ] Newly encountered files are not treated as disposable before master-surface / governed-history checks
- [ ] Destination/runtime non-members are not treated as junk merely because they sit outside the current source-owned install set
- [ ] Hygiene wording is not usable as standalone deletion authority
---
## Quality Metrics
| Metric | Target |
|---|---|
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
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable defaults and anti-hardcoding
- [authority-and-scope.md](authority-and-scope.md) - user authority and runtime co-location ownership boundary remain decisive
---
> **Full history:** [changelog/strict-file-hygiene.changelog.md](changelog/strict-file-hygiene.changelog.md)
