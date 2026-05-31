# README Core Capabilities List and Doctrine Framing Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/design.md](../design/design.md) v10.35
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the released `v10.35 / P127` wave.

It packages one bounded front-page refinement so the README Core Capabilities section stops presenting capability meaning through a grid and phase/release execution chronology, and instead explains the current operating model as a readable doctrine-grounded list.

---

## Analysis

The checked README section had two problems at once:
- the capability block used a grid/table that scanned awkwardly for dense doctrine-like copy
- the `Runtime Context Discipline` cell had drifted into a long phase/release narrative, which made the README behave more like an execution/history surface than a front page

The checked authority direction already pointed the other way:
- `document-governance.md` says README is the current front page, not the history book
- the active design summary keeps current-state doctrine and authority boundaries separate from execution-history detail

The better posture is therefore:
- use a readable list instead of a grid
- explain each capability from active doctrine and current-state behavior
- keep phase/release execution chronology out of capability meaning
- preserve current-state visibility without turning README into a phase summary

---

## Change Items

### 1) Core Capabilities layout rewrite

- **Target artifact:** `README.md` Core Capabilities section
- **Change type:** replacement
- **Current state:** the section used a `<table>` / grid-style presentation
- **Target state:** the section uses a readable markdown list
- **Review point:** no mixed grid/list halfway state remains in the capability block

### 2) Capability wording authority shift

- **Target artifact:** `README.md` Core Capabilities section
- **Change type:** replacement
- **Current state:** capability meaning, especially Runtime Context Discipline, drifted into phase/release execution narration
- **Target state:** capability wording explains active doctrine and current-state behavior directly
- **Review point:** README capability meaning stays front-page scoped and does not replay execution chronology as the explanation itself

### 3) README authority clarification

- **Target artifact:** `document-governance.md` and its design/changelog companions
- **Change type:** refinement
- **Current state:** README was already defined as front-page/current-state authority, but capability/current-state phrasing was not yet explicit enough for this rewrite wave
- **Target state:** README capability/current-state sections are explicitly front-page scoped and doctrine-grounded
- **Review point:** the rewrite is backed by active authority rather than only by editorial preference

### 4) Release-surface sync

- **Target artifact:** touched README/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** latest released baseline was `v10.34 / P126`
- **Target state:** touched master surfaces open and later close `v10.35 / P127` consistently
- **Review point:** release-facing wording matches the actual pushed and released state

---

## Verification

Required checks before release closeout:
- the README Core Capabilities section no longer uses the old grid/table block
- every capability is presented as a readable list item with practical current-state behavior
- capability wording no longer uses phase numbering or execution timeline as the explanation basis
- checked authority references support the rewrite direction
- touched README/changelog/TODO/phase/patch surfaces align to `v10.35 / P127`
- runtime install into a checked project-local `.claude/rules/` target passes for the 18 active runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- branch push, remote default-branch verification, and GitHub release verification pass

---

## Before / After

### Before

```text
Core Capabilities
  → 2x2 grid/table layout
  → Runtime Context Discipline explained via release/phase history
  → capability meaning mixed with execution chronology
```

### After

```text
Core Capabilities
  → readable markdown list
  → each capability explains active doctrine/current-state behavior directly
  → Runtime Context Discipline stays front-page scoped instead of phase-summary shaped
```

---

## Implementation Status

P127 is completed.

The README capability block is now list-based, current-state/doctrine-grounded, and no longer explains capability meaning through phase/release chronology. Touched README/changelog/TODO/phase/patch surfaces were synchronized, runtime install-boundary proof plus 18/18 parity/body-sufficiency verification passed, `git diff --check` passed, branch/default-branch push verification passed, and GitHub release verification passed.
