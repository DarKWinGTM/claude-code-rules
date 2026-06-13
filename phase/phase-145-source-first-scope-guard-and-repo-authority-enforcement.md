# P145 — Source-First Scope Guard and Repo-Authority Enforcement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P145
> **Status:** Completed / Released
> **Target Release:** v10.53
> **Design References:** none
> **Patch References:** [../patch/source-first-scope-guard-and-repo-authority-enforcement.patch.md](../patch/source-first-scope-guard-and-repo-authority-enforcement.patch.md)
> **Session:** 8b04beb0-b5ef-4500-a3f5-558bcedd088a
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make source-first scope explicit for RULES maintenance so future work starts from the checked source-controlled repository, treats `/home/node/.claude/rules` as a downstream install target, and keeps runtime-first edits outside the default path unless the task is explicitly runtime-only.

---

## Why This Phase Exists

The previous release wave correctly closed the source update, install, push, and repo release path, but the user found the workflow hard to trust because the work started from runtime diagnosis and only later converged back into the source repository.

The maintainer contract already required README update, runtime install, source push, and repo release. What it still lacked was one explicit source-first guard that says where RULES work should begin.

P145 closes that gap by making the repo-authority boundary explicit instead of leaving it as an implicit expectation.

---

## Expected Output

- repo-root `CLAUDE.md` explicitly says RULES work starts from the checked source-controlled repository first
- `/home/node/.claude/rules` is explicitly treated as a downstream install target rather than source authority
- runtime-first edits are outside the default path unless the task is explicitly runtime-only emergency or install-verification work
- release-facing README wording reflects the new source-first guard
- touched TODO/phase/changelog/patch surfaces align to one `v10.53 / P145` baseline once release verification completes

---

## Action Checklist

- [x] Add the source-first scope guard to repo-root `CLAUDE.md`.
- [x] Update README release-facing wording for the new guard.
- [x] Sync `TODO.md`, `phase/SUMMARY.md`, this phase file, and the patch artifact.
- [x] Sync `changelog/changelog.md` and `changelog/changelog/v10.53-released-source-first-scope-guard-and-repo-authority-enforcement.changelog.md`.
- [x] Complete runtime install/update verification, push, tag, release, and post-release local checkout sync.

---

## Out of Scope

- changing the active 19-rule runtime payload itself
- reopening the governed `/goal` route-support doctrine closed in `v10.52 / P144`
- broad installer redesign
- unrelated plugin or non-RULES waves

---

## Completion Gate

- repo-root `CLAUDE.md` makes source-first scope explicit in checked source
- README explains the new guard without contradicting the maintainer closeout contract
- touched TODO/phase/changelog/patch surfaces align to `v10.53 / P145`
- runtime install/update verification is rerun from the checked source repo
- selected runtime parity checks pass in checked scope
- push to `master`, tag `v10.53`, and GitHub release verification all pass before closeout is claimed at released strength

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is maintainer-contract, release-surface, and repo-boundary work only.
- **Checks run:** touched-owner anchor verification, TODO/phase/master-changelog/detail sync, runtime install/update rerun from the checked source repo, selected runtime parity checks, `git push` verification, tag verification, GitHub release verification, and post-release local checkout sync verification.
- **Confidence:** released and verified in checked scope.

---

## Current Status

P145 is completed.

Current checked progress:
- repo-root `CLAUDE.md` now says RULES work starts from the checked source-controlled repository first
- `/home/node/.claude/rules` is explicitly treated as a downstream install target, not source authority
- README, `TODO.md`, `phase/SUMMARY.md`, this phase file, `patch/source-first-scope-guard-and-repo-authority-enforcement.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.53-released-source-first-scope-guard-and-repo-authority-enforcement.changelog.md` align to `v10.53 / P145` in checked scope
- runtime install/update verification was rerun from the checked source repo, selected runtime parity checks passed, push to `master` passed, tag `v10.53` passed, GitHub release verification passed, and the local RULES checkout was resynced to the released files
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.53
