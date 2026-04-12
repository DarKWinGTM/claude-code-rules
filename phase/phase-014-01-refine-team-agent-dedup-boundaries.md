# Phase 014-01 - Refine team-agent dedup boundaries

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 014-01
> **Status:** Completed
> **Design References:** [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/operational-failure-handling.design.md](../design/operational-failure-handling.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md)
> **Patch References:** [../patch/team-agent-dedup-and-stale-presence-boundary.patch.md](../patch/team-agent-dedup-and-stale-presence-boundary.patch.md)

---

## Objective

Refine the team-agent governance owner set so overlapping teammates are not spawned without distinct purpose, and duplicate-looking team-agent presence is inspected before respawn.

## Why this phase exists

The user reported duplicate-looking team agents and explicitly asked that team agents with redundant work be shut down or avoided. The checked local team directory state suggests that some duplicate-looking presence can also be stale or partially cleaned up. This phase closes that gap without creating a new first-class doctrine chain.

## Action points / execution checklist

- [x] update `custom-agent-selection-priority` as the primary selection/dedup owner
- [x] update `authority-and-scope` as the team-expansion boundary owner
- [x] update `operational-failure-handling` as the stale/duplicate-presence handling owner
- [x] update `accurate-communication` as the reporting owner for duplicate-looking team-agent state
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Verification

- team-agent creation now prefers reuse-before-spawn
- overlapping teammates now require a distinct role or explicit user request
- duplicate-looking team-agent presence is no longer treated as immediate respawn justification
- reporting distinguishes observed duplicate-looking state from inferred real overlap

## Exit criteria

- the team-agent dedup boundary is clearly split across selection, authority, operational handling, and reporting ownership
- stale duplicate-looking team presence is treated as an inspect-first case
- the implementation remains a bounded refinement wave rather than a new doctrine chain
