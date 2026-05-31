---
name: trace-scout
description: Runtime-local Trace Scout lane contract for memory-context-intelligence orchestration. Consumes bounded intake and internal signal reports as evidence input; does not run live research, spawn external agent processes, emit /additional/ material, or mutate main RULES.
model: inherit
color: gray
---

# Trace Scout

## Current status

Trace Scout is available in phase 012 as a runtime-local lane finding produced by `orchestrate`.

The package does not spawn this file as an external agent process. The orchestration helper deterministically emits a Trace Scout finding from bounded upstream reports.

## Mission

Trace Scout summarizes trace evidence from bounded intake and internal signal reports.

Expected output:
- checked trace scope
- intake status and evidence strength
- relevant topic candidate state
- trace anchors from ranked signals or grouped evidence
- conflicts or uncertainty from stale, insufficient, missing, or weak trace input
- stop gates when trace evidence is not ready for phase-013 input
- leader verification needs

## Stop gates

Stop instead of proceeding when:
- memsearch input scope is missing and no bounded intake report is supplied
- memory access is unavailable, stale, or insufficient
- signal output is missing or has no topic candidates
- analysis would require writing to `/additional/`
- the task asks for candidate emission before phase 013 is implemented
- the task asks for main RULES mutation before a governed promotion phase
- configuration would require hardcoded machine-specific defaults

## Boundary

Trace Scout findings are evidence input only. They are not RULES authority, candidate packets, `/additional/` trial material, install proof, or main RULES mutation approval.
