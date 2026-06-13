# Source-First Scope Guard and Repo-Authority Enforcement Patch

> **Current Version:** 1.0
> **Session:** 8b04beb0-b5ef-4500-a3f5-558bcedd088a
> **Status:** Complete / Released
> **Target Design:** none
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P145 wave.

It packages one bounded repository-maintenance refinement: future RULES work should start from the checked source-controlled repository first, while `/home/node/.claude/rules` stays a downstream install target rather than a source-authority workspace.

---

## Analysis

Before this wave:
- the repo-root maintainer contract already required README update, runtime install, source push, and repo release before a RULES wave counted as done
- but it did not yet say explicitly that work must begin from the checked source repo instead of the installed runtime copy
- that gap made it easier for runtime-first diagnosis work to look like source-authority editing, even when the work later converged back into the repo correctly

The better posture is:
- make source-first scope explicit in repo-root `CLAUDE.md`
- reflect that guard in release-facing README wording
- keep the active runtime payload unchanged
- rerun install/update verification from the checked source repo so maintainer closeout remains real rather than only declarative

---

## Change Items

### 1) Repo-root maintainer contract hardening

- **Target artifacts:** `CLAUDE.md`
- **Change type:** bounded project-contract refinement
- **Current state:** closeout is explicit, but source-first authority is still implicit.
- **Target state:** repo-root `CLAUDE.md` says RULES work starts from the checked source-controlled repository first and treats `/home/node/.claude/rules` as a downstream install target.
- **Review point:** the guard should prevent scope drift without turning runtime-only emergency or install-verification tasks into forbidden actions.

### 2) Release-facing README sync

- **Target artifacts:** `README.md`
- **Change type:** current-state / maintainer-guidance synchronization
- **Current state:** release-facing README explains v10.52 goal-route-support changes but not the new source-first scope guard.
- **Target state:** current release note and current-source-state block explain the source-first guard while preserving the maintainer closeout contract and the 19-rule runtime payload truth.
- **Review point:** README should stay current-state focused rather than drifting into a long retrospective narrative.

### 3) Current execution-surface sync

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-145-source-first-scope-guard-and-repo-authority-enforcement.md`, and this patch file
- **Change type:** active phase/TODO synchronization
- **Current state:** active current-state surfaces still point to `v10.51 / P143` as the latest released baseline.
- **Target state:** active current-state surfaces reflect `v10.53 / P145` as the latest released baseline and record the new source-first guard wave.
- **Review point:** touched surfaces must not outrun the real push/tag/release evidence.

### 4) Release-history synchronization

- **Target artifacts:** `changelog/changelog.md` and `changelog/changelog/v10.53-released-source-first-scope-guard-and-repo-authority-enforcement.changelog.md`
- **Change type:** release-history synchronization
- **Current state:** latest released baseline is `v10.52 / P144`.
- **Target state:** master release-history surfaces advance to `v10.53 / P145` only because push/tag/release verification is completed in this wave.
- **Review point:** release wording must match the checked evidence held at closeout.

---

## Verification

Required checks before strong closeout wording:
- repo-root `CLAUDE.md` explicitly states the source-first scope guard
- README current-state/release wording reflects the new guard and still describes the 19-rule runtime payload correctly
- TODO/phase/patch/master-changelog/detail surfaces align to `v10.53 / P145`
- runtime install/update verification is rerun from the checked source repo
- selected runtime parity checks pass in checked scope
- push to `master`, tag `v10.53`, and GitHub release verification all pass
- post-release local RULES checkout sync matches the released source files in checked scope

---

## Rollback Approach

If the new guard proves too rigid, soften only the source-first wording while keeping the maintainer closeout contract and downstream runtime-install boundary intact; do not roll back into a posture where installed runtime copies can silently become the default editing authority for RULES source work.

---

## Implementation Status

P145 is completed.

The source-first guard is now explicit in repo-root `CLAUDE.md`, release-facing README wording is aligned, active current-state surfaces align to `v10.53 / P145`, runtime install/update verification was rerun from the checked source repo, selected runtime parity checks passed, push to `master` passed, tag `v10.53` passed, GitHub release verification passed, and the local RULES checkout was resynced to the released files. Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.53
