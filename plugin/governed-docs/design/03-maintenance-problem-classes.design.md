# Maintenance Problem Classes

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the recurring maintenance/drift classes that the plugin must detect and classify so it behaves like a governance companion rather than a generic formatter.

## 2) Class A — Role Drift

Meaning:
- one surface starts acting like another surface's authority

Examples:
- README turning into a changelog timeline dump
- changelog turning into a phase or TODO dump
- phase artifact turning into patch review content
- design accumulating history instead of target-state truth

Expected plugin behavior:
- detect the role-overload pattern
- identify the correct owning surface
- recommend redistribution or repair, not blind text cleanup

## 3) Class B — Structure Drift

Meaning:
- parent/shard/detail structure no longer matches the selected chain shape

Examples:
- shard map missing an active file
- orphan child shard
- same-stem and flat-sibling modes mixed ambiguously
- parent no longer acts as the authority gateway

Expected plugin behavior:
- classify current chain shape
- detect mismatch against selected shape
- prepare safe structure-repair guidance or bounded pointer normalization

## 4) Class C — Rollover Pressure

Meaning:
- active entrypoints stay technically valid but are no longer cheap to scan or maintain

Examples:
- `TODO.md` or `phase/SUMMARY.md` grows beyond practical active-scan limits
- completed detail overwhelms active content
- repeated compact-thrash or giant mixed bullets appear

Expected plugin behavior:
- detect soft/hard pressure
- distinguish preservation work from cleanup deletion
- propose daily-first rollover or history/done redistribution paths

## 5) Class D — Phase Grammar Drift

Meaning:
- phase naming or lineage semantics drift away from the checked RULES grammar

Examples:
- malformed phase identifiers
- unsupported deeper hybrid forms
- legacy-only alpha forms being reused as if they were forward-valid precedent
- current-phase / child-phase / new-major selection not matching lineage rules

Expected plugin behavior:
- classify filename inventory
- separate observed legacy forms from forward-valid grammar
- flag ambiguous lineage decisions for approval instead of auto-correcting them

## 6) Class E — Release Sync Drift

Meaning:
- release-facing surfaces disagree or claim stronger status than the checked evidence supports

Examples:
- README says released while supporting evidence or changelog/phase surfaces disagree
- TODO closeout wording stronger than the checked install/parity/release proof
- patch, phase, and changelog describe different current release states

Expected plugin behavior:
- compare the touched release surfaces
- distinguish wording drift from proof drift
- block closeout when the evidence boundary is not met

## 7) Class F — Preservation Risk

Meaning:
- a tempting maintenance action would destroy authority, lineage, or history

Examples:
- deleting done/history material because it looks inactive
- renaming phase files because a pattern looks odd without checking lineage and explicit doctrine
- treating cleanup or co-location as disposal proof

Expected plugin behavior:
- escalate to approval or block state
- refuse auto-normalization when the risk is semantic rather than cosmetic

## 8) Why class-based design matters

Without class-based detection, the plugin would reduce everything to syntax or formatting. The actual RULES pain is deeper:
- some odd forms are allowed only as legacy evidence
- some problems require redistribution, not correction in place
- some issues are evidence/writing-strength problems, not structure problems
- some maintenance work must stop because preservation risk is higher than tidiness value

---

> Classification rule: the plugin should first know what kind of problem it is looking at before deciding whether it can safely propose or perform any repair.
