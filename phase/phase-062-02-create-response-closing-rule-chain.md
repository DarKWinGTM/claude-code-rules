# Phase 062-02 - Create response-closing rule chain

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 062-02
> **Status:** Completed
> **Design References:** [../design/response-closing-and-action-framing.design.md](../design/response-closing-and-action-framing.design.md)
> **Patch References:** [../patch/accurate-communication-owner-extraction.patch.md](../patch/accurate-communication-owner-extraction.patch.md)

---

## Objective

Create the first-class rule chain that owns concise response closing, action framing, and advisory proposal wording.

## Why this phase exists

`accurate-communication` had accumulated a dense end-of-response subdomain covering synthesis, recommendation framing, alternative preservation, and advisory proposals. This phase creates one explicit owner for that domain without moving execution-mode or authority behavior into a closing-only chain.

## Entry conditions / prerequisites

- the extraction remains bounded to response-closing/action/proposal framing rather than execution-mode or user-authority ownership
- the governed patch artifact for this wave is already established

## Action points / execution checklist

- [x] create `response-closing-and-action-framing.md`
- [x] create its design companion
- [x] create its changelog authority file
- [x] keep the chain bounded to concise synthesis, recommendation-with-reason wording, alternative preservation, closed-topic summary handling, and goal-qualified advisory proposals

## Out of scope

- execution-mode continue vs stop ownership
- user-authority and branch-choice ownership
- explanation-flow ownership for stage/full-set logic
- presentation-layout ownership for closing block shapes

## Affected artifacts

- `response-closing-and-action-framing.md`
- `design/response-closing-and-action-framing.design.md`
- `changelog/response-closing-and-action-framing.changelog.md`
- bounded patch and phase artifacts for wave `062`

## Verification

- [x] a first-class response-closing/action owner now exists
- [x] advisory proposal framing is explicitly bounded and non-queued
- [x] the chain does not absorb execution-mode or authority ownership

## Risks / rollback notes

- over-broad extraction could accidentally absorb continuation or branch-choice ownership that belongs elsewhere
- rollback should narrow the chain before removing it entirely
- preserve wave history instead of silently deleting the new owner

## Next possible phases

- `062-03` integrate the communication owner split across touched companion surfaces
- `062-04` run a postflight overlap audit

## Exit criteria

- [x] the response-closing chain exists and is reviewable
- [x] it remains bounded to its intended semantic domain
