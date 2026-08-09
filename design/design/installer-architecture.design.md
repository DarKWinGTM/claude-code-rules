# Installer Architecture - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.58
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045 (2026-08-09)
> **Section:** Project-local Claude Code install architecture
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Purpose

This shard defines the active installer architecture for the RULES source chain when the selected install surface is Claude Code project-local `.claude/rules/`.

It exists so launcher scripts, helper scripts, README guidance, phase execution, and future refinements share one durable target-state contract instead of leaving install behavior spread across patch-only or README-only logic.

---

## Supported Install Surface

The active install surface is `<project-root>/.claude/rules/`, selected through the explicit project-root input.

Contract:
- project-local install is the default recommendation
- user-level installation is represented only by explicitly selecting the user's home directory as `<project-root>`; it is not a separate implicit mode or authority
- unsupported non-native harnesses must not be counted as supported for this install surface
- current checked support for this shard is Claude Code only

---

## Primary Operator Path

The active recommended operator path is:
1. clone the RULES repo
2. enter the cloned repo
3. run the launcher script for the current platform
4. let the launcher dispatch into the helper/install layer for the selected target project

Contract:
- clone + launcher is the primary README and AI-guided install UX
- the launcher should make the selected project-local target explicit rather than silently implying a user-level-first install
- fallback paths may still exist, but they must not displace the launcher-first operator path in current guidance

---

## Execution Modes

The installer model supports three execution paths that converge to the same target contract:
- launcher-driven execution from an existing RULES checkout as the primary operator path
- direct helper execution with an explicit local source repo as the secondary/manual path
- bootstrap cloning only when no explicit or inferred local source is available

Contract:
- all paths install the same active runtime set into the selected project-root target
- launcher-first is UX-primary, while helper scripts remain the execution layer underneath
- explicit local source takes precedence over source inference; source inference takes precedence over bootstrap cloning
- repo URL and ref inputs apply to bootstrap cloning only and must not silently alter an explicit or inferred local source

---

## Launcher Contract

Launcher scripts are the entrypoint UX layer.

Contract:
- launcher scripts live at `script/launcher.sh` and `script/launcher.ps1`
- launcher scripts should call the helper scripts instead of duplicating install logic
- launcher scripts should keep the target project path explicit in operator-facing usage
- launcher scripts should preserve the project-local `.claude/rules/` target model and must not silently switch to user-level-first behavior
- launcher scripts may expose a smaller operator-focused interface than the helper layer, as long as they remain compatible with the same install contract underneath

---

## Helper Contract

Helper scripts are the execution layer.

Contract:
- helper scripts perform source resolution, active-target ownership preflight, staged copy/install, manifest ownership, and execution-disconnected quarantine handling
- launcher scripts delegate into helpers instead of re-implementing cleanup or parity logic
- direct helper execution remains allowed for manual or bootstrap use, but should not replace launcher-first UX in current guidance

---

## Source Resolution

The active source resolution order is:
1. explicit source repo argument when provided
2. local repo inference from the helper or launcher location when the script is run from a RULES checkout
3. bootstrap clone/fetch from the configured repo URL when no local source is available

Contract:
- source resolution must verify that the chosen source still looks like the RULES repo before install proceeds
- source resolution must not silently broaden install scope beyond the active runtime set
- temporary bootstrap material is implementation detail, not durable install ownership

---

## Install Ownership and Cleanup Contract

The active ownership and convergence contract is fail-closed:
- validate manifest filenames and hash fields, reject duplicate records, and reject symlinks/reparse points across the managed `.claude`/rules/quarantine path chain, manifest, and active targets before payload mutation
- preflight all active target names and every planned quarantine source/type; overwrite only the current source, a matching prior manifest snapshot, or an exact historical repository blob for that path
- stage the complete 19-file payload and manifest before replacing active targets
- keep a bounded rollback journal for quarantine moves, active-target replacements, and manifest replacement so a failed commit restores the pre-install state where the installer still owns the moved paths
- move unchanged obsolete manifest-owned files to `<project-root>/.claude/quarantine/claude-code-rules/<run-id>/` instead of deleting them
- move retired candidates only after exact historical repository-blob proof
- evacuate the prior installer-owned in-tree quarantine directory intact into external quarantine without interpreting its contents
- preserve modified manifest-owned, unmatched, unknown, unrelated, and other-owner files
- never read external quarantine as normal source, retry, reinstall, fallback, or restoration input

Not allowed:
- wildcard cleanup by filename alone
- deleting files merely because they are untracked, old-looking, co-located, or quarantined
- path-traversal or directory-like manifest entries
- overwriting an unowned or modified active-name collision
- treating other harness/runtime artifacts as RULES-owned without checked ownership evidence

---

## Active Runtime Set Contract

The installer contract remains bound to the active 19-rule runtime set.

Required guidance:
- helper scripts install only the current README-listed source-owned runtime root files
- design/changelog/TODO/phase/patch/helper/plugin surfaces remain outside the runtime install payload
- parity and body-sufficiency proof must be checked against the same 19-file set

---

## Verification Contract

Installer closeout or proof should confirm:
- launcher scripts exist and drive the selected operator path correctly
- helper scripts exist and target the selected install surface correctly
- manifest filenames/hash fields reject malformed, duplicate, traversal, or directory-like input before payload mutation
- symlink/reparse-point ancestors under the selected project boundary, direct linked rules/quarantine directories, and manifest/active-target links including broken links fail closed without mutating the external tree or replacing other-owner directory entries
- unowned or modified active-name collisions fail closed
- a deterministic later preflight failure leaves the project tree and prior in-tree quarantine unchanged; commit-phase failure uses the rollback journal instead of leaving a mixed payload
- the active runtime set and ordered Bash/PowerShell manifests remain identical at 19
- source/destination parity and body sufficiency pass for 19/19 files
- prior in-tree quarantine, unchanged obsolete manifest-owned files, and repository-matching retired candidates move to external quarantine
- modified, unmatched, unknown, unrelated, and other-owner files remain unchanged
- quarantine poisoning, rename, or unavailability does not affect normal reinstall
- idempotent reinstall creates no active duplicate and performs no automatic restoration
- controlled restoration uses an independently verified exact known-good source through the normal installer and re-establishes one active authority without reading quarantine
- matched Bash and PowerShell fixture matrices cover equivalent ownership, quarantine, disconnection, restoration, traversal, and collision cases
- `git diff --check` remains clean after source edits when source work is in scope

Recommended proof shape:
- selected project-root and source path/ref
- installed file count and manifest order
- parity and body-sufficiency results
- quarantine actions and checked inactivity scope
- unrelated/modified/unmatched preservation results
- fixture commands and platform results
- remaining canonical/root/fresh-clone limits

---

## Boundary and Extension Path

Current active boundary:
- Claude Code only for this install surface
- no Codex CLI support claim for `.claude/rules/`
- no Gemini CLI support claim for `.claude/rules/`
- launcher-first rollout is part of the active target state, but it must stay a thin UX layer over the helper contract rather than becoming a parallel install engine

Future extension is allowed only after a checked design update selects it explicitly, such as:
- broader launcher wrappers beyond the current Claude-only install surface
- native support for other harnesses using a non-user-level equivalent surface
- broader reusable packaging models

Until then, README, launcher, and helper wording should stay aligned to the current Claude-only install contract.
