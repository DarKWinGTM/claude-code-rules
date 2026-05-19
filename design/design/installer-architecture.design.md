# Installer Architecture - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.18
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-19)
> **Section:** Project-local Claude Code install architecture
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Purpose

This shard defines the active installer architecture for the RULES source chain when the selected install surface is Claude Code project-local `.claude/rules/`.

It exists so launcher scripts, helper scripts, README guidance, phase execution, and future refinements share one durable target-state contract instead of leaving install behavior spread across patch-only or README-only logic.

---

## Supported Install Surface

The active install surface is:
- primary target: `<project-root>/.claude/rules/`
- optional fallback target: `$HOME/.claude/rules/`

Contract:
- project-local install is the default recommendation
- global install is an explicit fallback, not the primary model
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

The installer model supports three execution modes that must converge to the same target contract:
- launcher-driven local-repo execution from an existing RULES checkout as the primary operator path
- direct helper execution from a local RULES checkout as a secondary/manual path
- remote-bootstrap helper execution only as a fallback convenience path when explicitly selected

Contract:
- all modes must end by installing the same active runtime set into the same chosen target shape
- launcher-first is UX-primary, while helper scripts remain the execution layer underneath
- the helper may resolve local source first and bootstrap only when local source is unavailable or when fallback mode is explicitly used
- repo URL and ref override are allowed only as explicit source-selection inputs, not as hidden policy changes

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
- helper scripts perform the actual copy/install, manifest ownership, and legacy quarantine behavior
- launcher scripts delegate into helpers instead of re-implementing cleanup or parity logic
- direct helper execution remains allowed for manual or fallback use, but should not replace launcher-first UX in current guidance

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

The active cleanup contract is owner-aware:
- install only the active source-owned runtime rule set
- remove only manifest-owned files that still match the previously recorded install snapshot
- quarantine legacy files only when their content exactly matches historical blobs from this repo
- preserve unrelated co-located files by default

Not allowed:
- wildcard cleanup by filename alone
- deleting files merely because they are untracked, old-looking, or co-located
- treating other harness/runtime artifacts as RULES-owned without checked ownership evidence

---

## Active Runtime Set Contract

The installer contract remains bound to the active 18-rule runtime set.

Required guidance:
- helper scripts install only the current README-listed source-owned runtime root files
- design/changelog/TODO/phase/patch/helper/plugin surfaces remain outside the runtime install payload
- parity and body-sufficiency proof must be checked against the same 18-file set

---

## Verification Contract

Installer closeout or proof should confirm:
- launcher scripts exist and drive the selected operator path correctly
- helper scripts exist and target the selected install surface correctly
- the active runtime set count remains 18
- source/destination parity passes for 18/18 files
- source/destination body sufficiency passes for 18/18 files
- manifest cleanup and legacy quarantine stay owner-aware
- `git diff --check` remains clean after source edits when source work is in scope

Recommended proof shape:
- target path used
- launcher path used
- installed file count
- parity result
- body sufficiency result
- cleanup boundary statement

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
