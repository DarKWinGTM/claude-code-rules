# Phase 006 - Define native-agent orchestration

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 006
> **Status:** Completed
> **Design References:** [../design/04-native-agent-orchestration.design.md](../design/04-native-agent-orchestration.design.md), [../design/03-research-enrichment.design.md](../design/03-research-enrichment.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Define how native agent lanes should support gathering, research, source-trust review, and synthesis inside the full-power evidence-backed method.

## Why this phase exists

The user wants this concept to emphasize depth and efficiency rather than separate lightweight modes. Native agent lanes help the future skill/plugin gather and review evidence with lower leader-context overload while preserving user authority and RULES boundaries.

## Action points

- [x] define native agent lanes
- [x] define when agent use is justified
- [x] define output contract for delegated lanes
- [x] define boundaries so agents do not become hidden authority

## Verification

- native agents are documented as part of the full-power method
- agent lanes are bounded and read-only in their evidence role
- leader synthesis responsibility remains explicit
- no active runtime `agents/` surface was created in this wave

## Exit criteria

- the capsule now has a native-agent orchestration concept that supports deeper and more efficient topic analysis without turning agents into direct RULES mutators
