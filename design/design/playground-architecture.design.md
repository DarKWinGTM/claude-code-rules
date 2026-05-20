# Playground Architecture - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.25
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-20)
> **Section:** Governed playground family for RULES behavior scenarios
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Purpose

This shard defines the active architecture for the governed `playground/` family.

It exists so RULES can show how the current rules change AI behavior in practice without turning README into a scenario dump, without mixing checked facts with invented demonstrations, and without expanding the runtime install payload beyond the active 18-rule set.

For `v10.20 / P112`, the family should also prefer transcript-grounded observed cases from real Claude Code session JSONL transcripts on this machine, richer multi-turn scenario traces, and more realistic blocker / correction / retry shapes when checked evidence supports them.

For `v10.23 / P115`, the family may also add a focused case family showing dominant-session-language ownership, candidate-goal-first successor recommendations, and selective promotion into advisory `/goal` form when current RULES behavior justifies that scenario split.

For `v10.24 / P116`, the family may also add a focused case family showing end-to-end language alignment across candidate-goal labels, promoted `/goal`, wrapper labels, recap lines, and exact-literal preservation when current RULES behavior justifies that scenario split.

For `v10.25 / P117`, the family may also add a focused case family showing more proactive candidate-goal surfacing at real decision boundaries plus the requested decision-ready explanation shape when current RULES behavior justifies that scenario split.

---

## Family Role

The `playground/` family is a governed non-runtime repository surface.

Its job is to:
- show scenario families where current RULES materially change AI behavior
- keep those scenario families grounded in checked current rule behavior
- separate checked historical observations from illustrative virtual exploration
- record transcript-derived observed cases with exact checked paths and anchor hints when transcripts are the evidence source
- provide a repeatable update path for future observed cases

It is not:
- an active runtime rule
- a replacement for design/changelog/TODO/phase/patch authority
- a README before/after dump
- an installer payload surface

---

## Behavior Evidence Model

Every playground case should prefer concrete example-driven explanation over abstract summary alone.

Required presentation shape inside scenario files:
- one realistic multi-turn dialogue, usually 3-6 turns when the case is non-trivial
- one lightweight flow diagram showing where RULES change the assistant's path
- one explicit separation between `rule-enforced fact`, `observed case`, and `virtual variant`
- one clear label showing whether the dialogue is virtual, transcript-grounded, or mixed
- transcript-path and anchor-hint recording whenever the observed case is derived from session JSONL evidence

Realism cues should come from checked evidence where available, such as:
- user correction or scope repair
- tool or file evidence arriving mid-flow
- blocker or missing-context gate
- retry or narrower next-best check
- completion-claim downgrade or disproval
- worker-routed broad follow-up instead of raw context flooding

Every playground case must keep three layers visibly separate:

### 1) Rule-enforced fact
This is the behavior currently required by checked RULES.

Contract:
- it must trace to current runtime rule owners
- it may state what the assistant should do, avoid, or ask under the governed condition
- it must not claim capabilities outside checked current rules

### 2) Observed case
This is a recorded example from checked repo/work history where the relevant rules already shaped behavior.

Contract:
- it must cite checked repo artifacts, release records, or recorded workflow evidence
- transcript-derived observed cases must record exact checked transcript paths and short anchor hints
- it should say what the observed evidence proves in scope when that boundary matters
- if no checked observed example exists yet, the case must say so explicitly
- missing observed evidence is not permission to invent one

### 3) Virtual variant
This is an explicitly labeled illustrative or matrix-driven scenario used to explore plausible branches.

Contract:
- it must stay labeled virtual
- it must not be phrased as historical fact
- it may show several possible states when those states are still governed by the same checked rule behavior

---

## Required Family Files

The playground family should include:
- `playground/README.md`
- `playground/coverage.md`
- `playground/matrix.md`
- `playground/templates/case-template.md`
- `playground/observed/YYYY-MM.md`
- `playground/cases/*.md`

Baseline and expansion posture for this wave:
- the original P111 baseline remains 10 scenario-family case files
- P112 may add transcript-grounded scenario families when checked evidence reveals uncovered patterns

---

## Scenario Coverage Contract

The playground must:
- preserve the original 10 baseline scenario families
- map all 18 active runtime rule files to at least one scenario family
- allow additional scenario families when checked transcript evidence justifies new coverage
- keep scenario-family naming semantic rather than version-shaped
- allow one rule to appear in several scenario families when that better reflects real behavior

Original baseline scenario families:
1. authority collision resolver
2. evidence-calibrated diagnosis
3. safe refusal and recovery
4. destructive action and topology gate
5. communication and presentation calibration
6. audience-safe disclosure split
7. coding change with verification discipline
8. execution continuity and worker routing
9. governed artifact lifecycle
10. external, memory, and portability boundary

Grounded expansion patterns already justified by checked transcript evidence in this wave:
11. status ladder and completion-claim audit
12. workflow-blocked visual QA

Additional focused scenario-family expansion justified by current governed behavior coverage in the current family:
13. language-aware candidate-goal promotion
14. end-to-end language-aligned goal surface
15. proactive goal surfacing and decision-ready explanation

---

## Virtual Matrix Contract

The playground matrix is a virtual-case exploration surface, not a history surface.

It should cover several axes such as:
- request type
- evidence state
- scope clarity
- risk level
- expected rule response
- turn count
- user behavior
- evidence source
- failure mode
- tool discovery or lane shape
- completion state
- artifact role
- verification posture
- communication surface

Contract:
- matrix rows must remain virtual unless explicitly linked to a checked observed record
- each matrix row should point back to one or more scenario families
- matrix output should help future case expansion without bypassing the checked fact / observed / virtual boundary

---

## Update Flow Contract

The playground should keep growing through observed additions, not by rewriting old scenarios into broad narrative prose.

Recommended update flow:
1. classify a new incident or prompt/workflow event into an existing scenario family when possible
2. record the checked evidence in the current monthly observed log, using exact transcript path plus anchor hints when transcript-derived
3. update the relevant case file's observed section and realism trace
4. open a new scenario family only when the current families no longer cover the behavior honestly and checked transcript evidence supports the split
5. keep the coverage matrix current when new rule owners or new scenario families appear

---

## Runtime Boundary

The playground family remains outside the active runtime install payload.

Contract:
- the active runtime install set remains exactly 18 root runtime rule files
- `playground/` must not be copied into `<project-root>/.claude/rules/`
- installer scripts do not gain `playground/` as install scope in this wave
- README install guidance may point to `playground/` as repo content, but not as runtime payload

---

## README Boundary

README may point to the playground family, but only compactly.

Contract:
- top-level README keeps a pointer-level section or equivalent navigation hook
- scenario bodies, matrices, and observed logs live under `playground/`
- playground's own README may index scenario families in more detail
- top-level README must not absorb the playground into a broad before/after or marketing dump

---

## Verification Contract

Playground closeout or proof should confirm:
- all required family files exist
- the original 10 baseline scenario-family files remain present
- any added scenario-family files are justified by checked transcript evidence
- each scenario visibly separates `rule-enforced fact`, `observed case`, and `virtual variant`
- transcript-derived observed cases cite exact checked transcript paths and anchor hints
- updated dialogues use richer multi-turn traces where relevant
- `playground/coverage.md` maps all 18 active runtime rules to at least one scenario family
- `playground/matrix.md` uses explicit virtual-case axes plus realism axes
- README keeps only a compact pointer to the playground family
- `playground/` stays outside the runtime install payload and the active runtime count remains 18
- `git diff --check` remains clean after source edits when source work is in scope

---

## Boundary and Extension Path

Current active boundary:
- playground is repository-governed documentation/support content
- it is not a runtime rule family
- it is not an install payload surface
- it may reference checked repo history, but must not silently become changelog authority

Future extension is allowed only after a checked design update selects it explicitly, such as:
- more scenario families when checked transcript evidence justifies them
- finer subdirectories under `playground/`
- richer observed logs, comparative analysis, or trace packs
- automation that helps classify or update cases without weakening the evidence boundary
