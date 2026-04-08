# Phase 023-01 - Rules-first over memory boundary

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 023-01
> **Status:** Completed
> **Design References:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/portable-implementation-and-hardcoding-control.design.md](../design/portable-implementation-and-hardcoding-control.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/document-consistency.design.md](../design/document-consistency.design.md)
> **Patch References:** [../patch/rules-first-over-memory-and-portable-support-artifacts.patch.md](../patch/rules-first-over-memory-and-portable-support-artifacts.patch.md)

---

## Objective

Refine the authority and portability owner set so a user-declared RULES-first issue is fixed through RULES rather than memory, and reusable support/package source artifacts remain portable by default.

## Why this phase exists

The user explicitly said these issues should be solved in RULES, not mainly through memory. The same workflow family also exposed that plugin-owned docs, scripts, skills, and agents need a clearer portable-by-default boundary when they are maintained as reusable source artifacts.

## Action points / execution checklist

- [x] update `authority-and-scope` as the RULES-first-vs-memory-first owner
- [x] update `portable-implementation-and-hardcoding-control` as the support/package portability owner
- [x] update `project-documentation-standards` as the repository-layer support-asset portability owner
- [x] update `document-consistency` as the local-execution-path vs source-artifact-reference owner
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] create a bounded governed patch artifact for this refinement wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Verification

- [x] a user-declared RULES-first issue now routes to RULES refinement rather than memory-first persistence
- [x] reusable support/package source artifacts are explicitly kept portable by default
- [x] local execution paths are no longer semantically interchangeable with reusable source-artifact references

## Exit criteria

- [x] rules-first-vs-memory-first authority is explicit in the owning chain
- [x] support/package artifact portability is explicit in the owning chains
- [x] the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
