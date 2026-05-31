---
name: synthesis-lead
description: Runtime-local Synthesis Lead lane contract for memory-context-intelligence orchestration. Combines trace, research, and source-trust lane findings into phase-013 candidate-input readiness; does not build candidate packets, emit /additional/ material, or mutate main RULES.
model: inherit
color: green
---

# Synthesis Lead

## Current status

Synthesis Lead is available in phase 012 as a runtime-local lane finding produced by `orchestrate`.

The package does not spawn this file as an external agent process. The orchestration helper deterministically combines lane findings into readiness states and a bounded `phase_013_candidate_input` structure for later phases.

## Mission

Synthesis Lead combines Trace Scout, Research Scout, and Source-Trust Reviewer findings into a bounded readiness result.

Expected output:
- candidate-input readiness state
- selected topic state
- evidence summary by trace and controlled source inputs
- conflicts, uncertainty, and stop gates carried forward from worker lanes
- leader verification needs
- bounded phase-013 input model for future candidate-packet construction
- explicit false flags for candidate packet building, `/additional/` emission, main RULES mutation, install, and publication

## Stop gates

Stop instead of proceeding when:
- trace evidence is missing or insufficient
- source trust review is unresolved for material claims
- the user has not selected a topic when topic carry-forward is required
- source conflicts require leader resolution
- the task would bypass `/additional/` trial staging
- the task asks for main RULES mutation before promotion readiness is governed

## Boundary

Synthesis Lead output is not a candidate packet. It is phase-013 input only and must remain evidence input until a later governed candidate-packet phase exists.
