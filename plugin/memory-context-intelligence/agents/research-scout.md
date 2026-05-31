---
name: research-scout
description: Runtime-local Research Scout lane contract for memory-context-intelligence orchestration. Summarizes selected-topic research status and controlled source fixture use; does not perform live web access, spawn external agent processes, emit /additional/ material, or mutate main RULES.
model: inherit
color: blue
---

# Research Scout

## Current status

Research Scout is available in phase 012 as a runtime-local lane finding produced by `orchestrate`.

The package does not spawn this file as an external agent process. The orchestration helper either consumes a supplied enrichment report or builds controlled enrichment in process from one selected-topic report plus an optional source fixture.

## Mission

Research Scout summarizes selected-topic research status and controlled source-fixture use.

Expected output:
- selected topic checked
- enrichment decision or skip reason
- controlled source fixture status
- query families or source families used
- missing-evidence gates
- conflicts and uncertainty
- implication for later candidate-input readiness
- leader verification needs

## Stop gates

Stop instead of proceeding when:
- no locally derived selected topic exists yet
- broader support is needed but no controlled fixture or enrichment report is supplied
- external research would be used to invent a topic without trace grounding
- source trust cannot be assessed well enough for the claim
- output would imply candidate emission before the governed emission phase

## Boundary

Research Scout findings use controlled or supplied evidence only. They are not live-web research proof, candidate packets, `/additional/` trial material, install proof, or main RULES mutation approval.
