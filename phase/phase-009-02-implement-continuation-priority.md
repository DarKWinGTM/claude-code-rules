# Phase 009-02 - Implement continuation-priority behavior

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 009-02
> **Status:** Implemented - Pending Review
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md)
> **Patch References:** [../patch/continuation-priority-and-option-offering.patch.md](../patch/continuation-priority-and-option-offering.patch.md)

---

## Objective

Implement a continuation-first behavior model so active work proceeds by default and options are shown only when user choice, approval, or clarification is genuinely required.

## Action points / execution checklist
- [ ] update `accurate-communication` as primary owner
- [ ] narrow `answer-presentation` next-stage usage
- [ ] narrow `explanation-quality` next-step defaults and defer owner semantics
- [ ] add anti-unnecessary-option guidance to `authority-and-scope`
- [ ] sync changelog/TODO/master docs and install touched runtime rules

## Verification
- continuation-first behavior is explicit
- next-stage blocks become optional presentation tools rather than interruption defaults
- explanation closing guidance no longer implies user-facing next steps are required mid-objective
- authority rule discourages unnecessary option branching
