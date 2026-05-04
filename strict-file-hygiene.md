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
- **Existing file first:** if the right authority file exists and still fits the role, edit it instead of creating a duplicate or parallel authority.
- **No junk docs:** do not create unnecessary summaries, duplicate plans, checkpoint/work-summary files, or version-suffixed copies such as `-v2`, `_final`, `_backup`, `_draft`, or `_old` unless the user explicitly requests them.
- **Ask when unclear:** unclear artifact necessity is a question, not permission to create speculative files or silently skip a required governed startup artifact.
- **Governed-startup exception:** required design/changelog/TODO/phase/patch startup artifacts resolved through `artifact-initiation-control` may be created proactively and are not junk.
  Required guidance:
  - governed design, changelog, TODO, phase, and patch artifacts may be created proactively when startup clearly requires them
  - ambiguous startup need still requires asking instead of silently skipping or drifting
  - this exception applies only to required governed startup artifacts, not arbitrary summaries or duplicate docs
  - it does not authorize deletion of newly encountered files merely because they do not match the expected artifact set
- **Shared-destination boundary:** destination/runtime files outside the current source-owned active runtime install set are not junk merely because they share a runtime directory; resolve owner/project scope before classification.
- **Portable-artifact hygiene:** reusable helpers/support artifacts avoid machine-local defaults unless explicitly machine-scoped; broader portability defers to `portable-implementation-and-hardcoding-control.md`.
- **No deletion by hygiene:** hygiene, cleanup, isolation, worktree, sandbox, runtime co-location, untracked state, or missing recognition is never standalone deletion authority; removal needs stronger semantic authority plus the destructive-confirmation owner.
---
## Allowed vs Not Allowed
Allowed creation:
- functional code/config required for operation
- documents explicitly requested by the user
- required governed startup artifacts from `artifact-initiation-control`
- intentionally short-lived temporary files in `/tmp`
Not allowed:
- versioned copies such as `file-v2`, `_final`, `_draft`, `_backup`, or `_old`
- checkpoint/summary/plan/work-summary files not requested and not required by startup governance
- duplicate authority artifacts when an existing file already serves the role
- treating untracked/newly seen files as junk or disposable by cleanup instinct alone
- treating destination/runtime files outside the current source-owned install set as junk merely because they share a runtime directory
- using hygiene, cleanup, isolation, worktree, sandbox, or runtime co-location rationale as deletion authority by itself
---
## Operational Rules
1. **Existing file first:** if the right authority file already exists, edit it.
2. **Ask when unclear:** if artifact necessity is unclear, ask before creating or skipping a required governed startup artifact.
3. **Startup-governance exception:** if `artifact-initiation-control` requires the artifact now, creation is allowed and should include a brief reason.
4. **Shared destination caution:** destination/runtime non-members need owner/project scope resolution before hygiene classification.
5. **No deletion by hygiene:** file removal needs stronger semantic authority plus the destructive-confirmation owner; hygiene alone is not deletion authorization.
---
## Decision Flow
```text
AI wants to create a file
  ↓
Correct authority file exists?
  → YES: edit existing file
  → NO: create only if functional code/config, required governed startup artifact, user-requested document, or allowed short-lived /tmp file
  → Otherwise: do not create

AI wants to classify/remove a newly encountered file
  ↓
Shared runtime destination and outside current source-owned install set?
  → YES: resolve owner/project scope first
  ↓
Master surfaces / governed history checked?
  → NO: check first and keep classification unresolved
  ↓
Stronger semantic authority plus destructive confirmation exists?
  → YES: follow the destructive-confirmation owner
  → NO: do not delete
```
Cleanup, hygiene, isolation, sandbox, worktree, runtime co-location, and git state can explain why a file looks suspicious, but they do not decide whether it is disposable. If a file's semantic role is unclear, preserve it and resolve authority first; do not convert review/classification into removal automatically.
---
## Verification Checklist
- [ ] Existing authority files are reused and no duplicate/junk/version-copy files are introduced.
- [ ] Required governed startup artifacts are not blocked by hygiene; ambiguous need is asked about early.
- [ ] Newly encountered or shared-destination files are not treated as disposable before owner, master-surface, and governed-history checks.
- [ ] Hygiene wording is not usable as standalone deletion authority.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Duplicate or unrequested junk files | 0 critical cases |
| Governed startup artifact false blocks | 0 critical cases |
| Hygiene-as-deletion-authority incidents | 0 critical cases |
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
