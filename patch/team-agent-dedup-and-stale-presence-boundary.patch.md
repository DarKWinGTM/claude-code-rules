# Team-Agent Dedup and Stale-Presence Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md) v1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that tightens how assistant-created team agents should be selected, reused, and cleaned up.

Why this change matters:
- the user reported duplicate-looking team agents such as repeated `pricing-reviewer` entries and explicitly asked that overlapping team agents should not be created unless they have distinct real work
- checked local team state showed that `pricing-boundary-followup` no longer had a live `config.json`, which means at least some duplicate-looking team presence can be stale or partially cleaned up rather than truly active useful agents
- the current rules already discourage unnecessary branching and additive expansion in adjacent areas, but they do not yet make `reuse-before-spawn`, distinct-role justification, and stale-team-presence handling explicit for team agents

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../custom-agent-selection-priority.md`
- `../authority-and-scope.md`
- `../operational-failure-handling.md`
- `../accurate-communication.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should reduce overlapping team-agent creation and duplicate-looking stale presence without making legitimate parallel teams harder to use when roles are genuinely distinct

---

## 3) Change Items

### Change Item 1
- **Target location:** `custom-agent-selection-priority` selection owner
- **Change type:** additive

**Before**
```text
The chain preferred the best-fit specialist but did not yet state explicitly that an already-active matching teammate should be reused instead of spawning another overlapping teammate.
```

**After**
```text
The chain now requires reuse-before-spawn for team agents and forbids materially duplicate teammate roles unless the tasks are explicitly partitioned and independently justified.
```

### Change Item 2
- **Target location:** `authority-and-scope` authority boundary owner
- **Change type:** additive

**Before**
```text
Assistant-generated proposals and options were advisory, but team expansion did not yet have an explicit boundary against adding overlapping teammates without a distinct role or explicit user direction.
```

**After**
```text
Assistant-created team expansion is now bounded: adding teammates requires either distinct non-overlapping work, a justified partition, or explicit user request.
```

### Change Item 3
- **Target location:** `operational-failure-handling` stale/duplicate state owner
- **Change type:** additive

**Before**
```text
The chain classified generic technical failures, but duplicate-looking or stale team-agent presence was not yet modeled as an operational case that should be inspected before respawn.
```

**After**
```text
The chain now treats duplicate-looking or stale team-agent presence as an inspect-first operational case: verify team state, request shutdown/cleanup if needed, and only respawn when the role is truly absent.
```

### Change Item 4
- **Target location:** `accurate-communication` reporting owner
- **Change type:** additive

**Before**
```text
The chain governed evidence-honest communication generally, but duplicate team-agent reports were not yet explicitly framed as a scoped fact-vs-inference problem.
```

**After**
```text
The chain now requires duplicate team-agent reports to separate:
- observed duplicate-looking UI/state
- checked local team facts
- inference about whether the duplicate is real overlap or stale presence
```

### Change Item 5
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded team-agent dedup/stale-presence refinement wave.
```

**After**
```text
Master governance surfaces now record the refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `custom-agent-selection-priority` explicitly requires reuse-before-spawn and distinct-role justification for team agents
- [ ] `authority-and-scope` explicitly prevents overlapping team expansion from becoming a default assistant move
- [ ] `operational-failure-handling` models duplicate-looking or stale team-agent presence as an inspect-first case rather than a respawn-first case
- [ ] `accurate-communication` explicitly separates observed duplicate-looking state from inferred real overlap in team-agent reporting
- [ ] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the reuse-before-spawn rule in `custom-agent-selection-priority`
- narrow the stale-presence handling in `operational-failure-handling` to a softer inspect-first recommendation rather than a stronger case profile if necessary
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to behavior that treats duplicate-looking team-agent presence as harmless noise or a reason to blindly spawn more agents
