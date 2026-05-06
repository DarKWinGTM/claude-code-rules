# Development Verification and Debug Strategy
> **Current Version:** 1.0
> **Design:** [design/development-verification-and-debug-strategy.design.md](design/development-verification-and-debug-strategy.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/development-verification-and-debug-strategy.changelog.md](changelog/development-verification-and-debug-strategy.changelog.md)
---
## Rule Statement
**Core Principle: Non-trivial coding, debugging, refactoring, integration, and runtime-behavior work must carry a proportionate verification strategy before completion claims, so development proceeds through behavior understanding, debug signal selection, implementation, targeted testing, and evidence-calibrated closeout instead of edit-only confidence.**
This rule owns coding-time verification strategy, debug path selection, testing depth, TestKit/scenario decision, reproduction and regression discipline, and verification closeout shape. It does not replace maintainable code structure, phase planning, TODO tracking, safety approvals, evidence wording, runtime topology control, or project-specific test harness design.

พูดง่าย ๆ: AI ไม่ควร coding แบบ “แก้แล้วจบ”; งานที่มี behavior จริงควรรู้ว่าจะพิสูจน์ยังไงว่าดีขึ้นหรือไม่พัง และต้องบอกขอบเขตที่ยังไม่ได้พิสูจน์ด้วย.
---
## Core Contract
### 1) Verification strategy as a coding default
Before or alongside non-trivial coding work, identify the behavior under change, the risk of being wrong, the debug signal that would show failure/success, and the smallest useful verification depth. Do not wait until after implementation to invent testing posture.

Required guidance:
- classify whether the work changes behavior, structure only, integration, config/runtime behavior, data flow, security-sensitive behavior, or documentation/governance only
- choose verification depth from the actual behavior/risk/signal available, not from a rigid command template
- make the TestKit/scenario decision explicit when behavior is scenario-like, multi-step, integration-heavy, or safety-sensitive
- if verification is not applicable or not practical, state the narrow reason and preserve evidence limits
- do not claim fixed, working, stable, or release-ready from edits alone

### 2) Verification depth model
Use the smallest verification layer that gives meaningful signal.

| Work shape | Default verification posture |
|---|---|
| typo, docs-only, metadata-only, no behavior change | review or no test with reason |
| small pure logic or UI behavior change | unit or focused test when available |
| refactor intended to preserve behavior | existing focused/regression tests for the affected behavior |
| integration, adapter, API, database, queue, or event behavior | integration/fake-adapter/contract test when practical |
| multi-step user/system flow | scenario harness, TestKit, or equivalent workflow test |
| payment, auth, secrets, quota, runtime, provider, external dependency, or privacy-sensitive behavior | fake/local first plus explicit smoke/live decision and safety boundary |
| production/shared-state/destructive path | approval-sensitive verification gate plus rollback/containment owner |

This model is strategy, not ceremony. A stronger existing test may replace a new scenario; a scenario harness may replace several fragile ad hoc checks; a live check remains conditional on user approval, safety, and environment readiness.

### 3) Debug strategy contract
For bug-fix, failure, flaky behavior, or complex integration work, keep a debug path visible enough to guide implementation.

Required guidance:
- identify the observed failure or reproduction target when available
- state the working hypothesis without treating it as proven cause
- define the signal that would confirm the fix or invalidate the hypothesis
- prefer a failing test, focused reproduction, TestKit scenario, fixture, fake adapter, log/report, or failure injection when practical
- if reproduction is unavailable, state what evidence is missing and use bounded diagnostics rather than guessing

### 4) TestKit / scenario decision contract
For non-trivial coding work, select one verification route explicitly:
- `existing_test`: an existing focused/regression test covers the behavior
- `new_focused_test`: a small new test should be added
- `new_testkit_scenario`: a scenario/TestKit path should be added or extended
- `smoke_check`: a lightweight end-to-end or runtime check is appropriate
- `live_check_required`: live/provider/runtime verification is needed and approval/environment gating applies
- `not_applicable_with_reason`: no meaningful test applies to this slice, with a short reason

Do not create TestKit scenarios for every task by reflex. Do not skip the decision silently when behavior risk is material.

### 5) Evidence boundary and closeout discipline
Verification evidence must be reported at its true strength.

| Evidence held | Do not claim |
|---|---|
| code edited only | fixed, verified, working |
| unit/focused tests passed | whole system or live dependency works |
| fake/local TestKit scenario passed | real provider/runtime/deploy works |
| smoke check passed once | stable over time |
| no test run | verified behavior |

Coding closeout should include the compact verification record when material:
```text
Verification:
- Ran: <commands/scenarios/checks or not run>
- Result: <passed/failed/not run>
- Covers: <behavior/scope>
- Does not cover: <live/provider/runtime/deploy/edge cases if material>
- Confidence: <evidence-calibrated wording>
```

### 6) Phase, TODO, and continuation behavior
For phase-backed coding work, phase records should show `Development Verification / TestKit Coverage` or equivalent when verification materially affects exit criteria. Live task lists should include or preserve a verification slice for non-trivial coding work when implementation and verification are distinct outcomes. Execution continuity should continue from implementation into verification when no real stop gate exists.
---
## Trigger Model
| Trigger | Required behavior |
|---|---|
| non-trivial coding feature | choose verification depth and TestKit/scenario decision before closeout |
| bug/debug request | define observed failure/reproduction, hypothesis, signal, fix, and regression check when practical |
| refactor | preserve behavior and rerun affected tests or state verification limits |
| integration/provider/runtime/payment/auth/privacy work | fake/local verification first, then explicit smoke/live decision and safety boundary |
| scenario-like flow | prefer TestKit/scenario harness or explain why focused tests are stronger |
| implementation completed but not tested | continue to verification when safe instead of stopping at edit-only progress |
| trivial no-behavior change | avoid ceremony; mark test not applicable with reason when needed |
---
## Anti-Pattern Boundary
Avoid edit-only completion, testing as an afterthought, mandatory TestKit creation for trivial work, fake/local pass presented as live proof, refactor without behavior-preservation checks, debugging from guesses without a signal, adding tests that do not cover the changed behavior, running broad/noisy tests without worker filtering when appropriate, and reporting fixed/stable beyond checked evidence.

Better behavior: understand behavior, choose a proportionate verification route, implement, run targeted checks, preserve not-tested scope, and report evidence at the correct strength.
---
## Verification Checklist
- [ ] non-trivial coding work identified behavior under change and verification target
- [ ] debug/failure signal was identified for bug or complex integration work
- [ ] TestKit/scenario decision was explicit when scenario-like behavior or integration risk existed
- [ ] verification depth matched behavior risk without over-ceremony
- [ ] fake/local/live/provider/runtime boundaries were not blurred
- [ ] closeout separated edited, tested, working, fixed, stable, and not-tested scope
- [ ] phase/TODO/continuation surfaces preserved a verification slice when material
---
## Quality Metrics
| Metric | Target |
|---|---|
| Non-trivial coding work with explicit verification strategy | High |
| Debug signal clarity for bug/integration work | High |
| TestKit/scenario decision visibility | High when relevant |
| Edit-only fixed/working claims | 0 critical cases |
| Fake/local evidence overclaim | 0 critical cases |
| Over-ceremony for trivial work | Low |
---
## Integration
Related rules:
- [maintainable-code-structure-and-decomposition.md](maintainable-code-structure-and-decomposition.md) - code structure and behavior-preserving refactor posture
- [accurate-communication.md](accurate-communication.md) - evidence-strength wording for edited/tested/fixed/stable claims
- [phase-implementation.md](phase-implementation.md) - phase-backed verification and closeout surfaces
- [todo-standards.md](todo-standards.md) - live task-list verification slices
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - continue from implementation into verification when safe
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - worker filtering for broad/noisy test/log output
- [runtime-topology-control.md](runtime-topology-control.md) - runtime mutation and live/smoke verification gates
---
> **Full history:** [changelog/development-verification-and-debug-strategy.changelog.md](changelog/development-verification-and-debug-strategy.changelog.md)
