# Coding Discipline
> **Current Version:** 1.9
> **Design:** [design/coding-discipline.design.md](design/coding-discipline.design.md) v1.9
> **Session:** b8a3c38a-53b5-4d7d-a9ac-6a6f082911b2
> **Full history:** [changelog/coding-discipline.changelog.md](changelog/coding-discipline.changelog.md)
> **Absorbed:** maintainable-code-structure-and-decomposition v1.2, development-verification-and-debug-strategy v1.1, tactical-strategic-programming v1.3

## Rule Statement

**Core Principle: Choose the smallest complete implementation inside the selected direction and checked owner. Keep responsibilities, canonical state and side effects clear; add structure and verification only for material needs; preserve behavior during refactor; and close at the objective's selected proof level. Temporary paths or material debt require convergence, correctly owned final-form work does not.**

พูดง่าย ๆ: โค้ดต้องครบและแก้ง่าย แต่ไม่เพิ่ม abstraction, state, guard หรือขั้นทดสอบเพียงเพราะทำได้; รักษาความหมายและขอบเขตที่จำเป็นจริง.

## Part A — Maintainable Code Structure

### Responsibility and smallest useful decomposition

Maintainability is low future change cost: readers can understand, test, modify and repair code with little surprise. Optimize readable intent, clear ownership, testability and visible side effects—not file/helper counts. Group by reason to change; keep cohesive logic together and separate business rules, orchestration, UI, persistence, integrations, validation, formatting, config or operational handling only when their ownership/change/test axes differ. Reuse fitting project structure.

Before selecting a material condition, representation or structure, understand the requested behavior, valid inputs, failure consequences, semantic owner, lifecycle, callers and useful proof. Trace the existing path; derive predicates and controls from checked contracts rather than a familiar pattern or one sample. Compare only realistic alternatives, including a simpler sufficient route. Scale this work to the decision: no mandatory worksheet, document or checklist for every `if` or small edit. Assess accumulated concerns and aliases together; individually small additions can create a hidden owner. Length and smells are investigation signals, not verdicts; preserve uncertainty when ownership or decomposition is unclear.

| Checked condition | Required proportionate decision |
|---|---|
| cohesive responsibility, inline flow clearer | keep local; do not extract obvious expressions, assignments or wrappers |
| meaningful concept/process/test/side-effect step | extract only if the name and boundary reduce cognitive load and improve clarity/testability |
| different ownership, change reason, state/dependency lifecycle or test boundary | split a cohesive responsibility family; keep navigation/call flow easier afterward |
| shared behavior with the same meaning and reason to change | extract; coincidentally similar business rules may remain duplicated rather than falsely coupled |
| another value for an existing concept | identify canonical owner/form first; reuse it unless a distinct stage, lifecycle or contract earns a new representation |
| speculative interface/factory/strategy/plugin-like variation | avoid, simplify or justify from current variation/isolation evidence, not imagined futures |
| immediate repair safer than a justified structural split | bounded tactical edit with target owner, remaining material debt and convergence trigger |

Helpers must earn indirection: a real concept, rule, process, reusable behavior or useful test/side-effect boundary should be clearer than inline code. Single-use helpers need meaningful names. Avoid trivial one-line/pass-through wrappers, excessive parameter threading and call-chain hopping; inline helpers with no semantic value.

For checked God-function/file pressure, inventory responsibility clusters, weigh under- versus over-decomposition, choose a cohesive family/subsystem seam, preserve behavior, and verify both behavior and structural improvement. Clear low-risk touched repair should proceed; bound broad/runtime-critical repair rather than big-bang rewrite. Progress requires moved responsibility/decision ownership, reduced original burden or materially clearer state/dependency/test boundaries—not extra files, aliases, facades or delegation chains. Batch by responsibility, not one helper/task/phase/patch.

### Semantic source naming

Function, variable, helper, class, type, module and test-helper identifiers describe domain meaning, behavior, state or responsibility—not phase/document/ticket/patch/changelog/roadmap/review provenance. Necessary chronology belongs in governed documents or bounded useful source comments. Preserve literal tokens only for real external/domain contracts: protocol/stored values, API fields, migration identifiers, compatibility aliases or operator-facing literals. Derive names from checked project meaning, not placeholder examples.

### Canonical state and deliberate transformations

Variables, fields, parameters and config/stored/derived values represent domain/process state. Understand their meaning, units, provenance and lifecycle before comparing them or making them prerequisites. Required/optional applies to the selected operation; absence, empty, known zero, unknown and invalid are distinct where the contract distinguishes them. Validate supplied data and required inputs without inventing equality, arithmetic, presence or fallback rules from field names or one observed shape. Diagnostic metadata becomes a decision input only through an explicit contract, not mere availability.

Within a responsibility boundary, one concept has one evident current owner and canonical representation for ordinary consumers. Parse/validate at ingress, normalize at the semantic owner, resolve policy at its owning layer and format at egress. Consumers use canonical values/decisions rather than repeating coercion, defaults, compatibility interpretation or adjudication. Reuse validation/transformation/computation only while its input and relevant assumptions remain valid; mutation, fresh reads, trust changes or transaction/recovery contracts may require another check. A new function or consumer alone is not a new trust boundary. Canonical results do not override genuine new contradictions or required safeguards.

Before adding another identifier/state slot, inspect owner, writers/readers, mutation boundary and normalization path. Keep genuine raw, validated, normalized-domain, policy-resolved, persisted, audit and presentation stages when their contracts differ; make transitions legible instead of minimizing names. Match access and persistence to consumer needs, avoiding repeated broad traversal or per-entity copies without a distinct purpose. Retain fidelity, diagnostics, audit, historical recovery, comparison/round-trip needs and required fresh/race checks; fewer keys/copies alone is not improvement. A shared editor or management surface need not move persistence or create a second policy authority.

Make dependency/state/transform flow explicit; avoid hidden ambient state and bind environment/config at edges. Scope initialization, ordinary processing, retry and recovery conditions to their lifecycle; define outcome transitions from the owning completion/failure contract rather than a sticky first error or latest event alone. Preserve independent dimensions such as delivery, integrity and settlement. Trace producer/selector → state → consumer before weakening a rejecting guard: reconcile incompatible selection and acceptance contracts at their actual owner. Separate pure transformation from side effects when useful; keep normalization, errors and logging at their boundary. Move behavior or introduce a type only when it clarifies responsibility or reduces real errors.

### Names, comments and governed references

Names/structure explain normal flow; concise comments explain otherwise non-obvious purpose, why, business rule, order, constraint, side effect, external contract, compatibility, security/performance/concurrency caveat or operational consequence. Prefer clearer code over compensating comments. Do not narrate syntax, every line or unverified behavior. Update/remove stale nearby comments after changes; keep broad policy/spec/architecture in governed documents.

A governed citation must lower maintenance cost. Prefer stable design/contract rationale; phase/changelog/patch/ticket/route provenance stays narrow to temporary bridges, migration, compatibility, rollback or costly-to-rediscover reviewed changes. Do not tag ordinary functions/helpers/classes/branches with execution chronology. Comments must remain true, verified, useful and local.

### Refactor and implementation completeness

Refactor preserves externally visible behavior unless change is explicitly selected. Separate structure and behavior changes when practical; use small transformations when behavior risk is high. Run relevant focused/regression tests, type checks, lint or bounded verification; incomplete proof limits claims of fixed/clean/stable.

Before non-trivial closeout, inspect material behavior, state/dependency, integration, failure, security, needed observability and verification gaps in the selected outcome. Happy path alone is insufficient when scope depends on errors, retries/idempotency, persistence, concurrency, rollback, cleanup or external contracts. Cover each material obligation or explicitly mark deferred, blocked, not applicable or out of scope with owner/reason where needed.

A risk observation or test obligation does not itself authorize a production guard, new state/path, queue or architecture. Choose controls from checked requirements and the actual writers, readers, data sensitivity, lifecycle and failure model—not an imagined topology. A demonstrated failure or concrete in-scope risk earns a control only when it improves the authorized outcome better than a simpler path; required safety need not wait for an incident. Preserve identity, authorization, integrity, atomicity, privacy and recovery obligations even when simplifying. Consult on material acceptance, ownership, cost or scope changes through the execution/safety owners; do not invent speculative compatibility layers or extend negative proof beyond affected roles.

## Part B — Development Verification Strategy

### Select the smallest meaningful proof

Before or alongside non-trivial work, identify changed behavior/type of change, material risk, failure/success signal and useful proof depth. Do not invent testing posture after implementation. Scenario-like, multi-step, integration or safety work requires an explicit TestKit/scenario decision; no meaningful/practical test must carry its narrow reason. Edits/scaffolds alone never prove working/fixed/release-ready.

| Work shape | Verification posture |
|---|---|
| typo/docs/metadata with no behavior change | review or no test with reason |
| small pure logic/UI change | focused/unit test when available |
| behavior-preserving refactor | existing affected focused/regression tests |
| API/adapter/database/queue/event integration | practical integration/fake-adapter/contract check |
| multi-step user/system flow | scenario/TestKit or equivalent workflow check |
| payment/auth/secrets/quota/runtime/provider/privacy | fake/local first; explicit smoke/live choice with safety/environment gate |
| production/shared-state/destructive operation | approval-sensitive verification with rollback/containment owner |

Strategy, not ceremony: a stronger existing test may replace a new scenario; a harness may replace fragile ad hoc checks. Each test/review should reproduce/protect changed behavior, check a material contract or close the selected gate. Include representative valid forms and the nearest meaningful failure/unchanged boundary; do not teach production logic one fixture shape. Correctness, architecture conformance and performance are distinct claims requiring matching evidence. Expand only for a decision-changing failure/risk, not broad noisy reruns or reassurance reviews. Live checks remain conditional on selected scope, approval, safety and readiness.

Select one route explicitly for non-trivial coding: `existing_test`, `new_focused_test`, `new_testkit_scenario`, `smoke_check`, `live_check_required`, or `not_applicable_with_reason`. Do not reflexively create TestKit for every task or silently skip a material verification decision.

### Debug and root-cause discrimination

For bugs/failures/flakiness/integration, identify observed symptom/reproduction, working hypothesis and smallest discriminating signal before fixing. Prefer a failing focused test, fixture/fake, scenario, log/report or failure injection that separates realistic causes. Missing reproduction calls for bounded diagnostics and an evidence limit; implementation before confirmed cause is hypothesis-driven. Re-anchor after correction; do not shotgun-edit several speculative causes. Cause/confidence thresholds belong to [evidence-discipline.md](evidence-discipline.md).

### Regression versus architecture gap

A missing field/output/route/config/consumer value does not prove missing architecture. Trace the active design contract, current owner/producer/state or transport, readers/writers/consumers/dependencies and last-known-working path before adding infrastructure.

| Classification | Meaning and next action |
|---|---|
| `existing-path regression` | governed path exists but is defective → repair current owner |
| `state/config drift` | state/config differs from selected contract → bounded correction |
| `dormant_or_disconnected_existing_path` | implementation exists but intended active edges are disconnected → reconnect verified path |
| `contract mismatch` | producer/state/transport/consumer expectations disagree → reconcile contract |
| `unresolved` | evidence does not distinguish realistic branches → discriminating diagnosis, not infrastructure |
| `verified_capability_gap` | checked path absent/incapable or active design selects new architecture → proposal through safety delta/approval gate |

Use the smallest check separating the leading classification from realistic competitors. A verified gap justifies a proposal, never automatic mutation. [action-safety.md](action-safety.md) owns design-conformance delta classification and authorization.

### Functional and architecture-fitness proof

Architecture-bearing work has separate functional and design-conformance obligations. Positive proof must exercise the selected producer→state/transport→consumer chain and approved target selection. Negative proof proportionately checks affected/relied-upon source/import/config/build/deployment/install/runtime/test-discovery edges against unauthorized alternate owners/routes/services/clients/adapters/transports/registries/state keys, dual read/write, shadow paths and fallback. Do not turn bounded repair into whole-system absence ritual or a production guard by default.

Tests for an unapproved/divergent path prove only its invented behavior, not architecture/completion. Report mixed evidence explicitly:
```text
functional behavior: passed
architecture conformance: failed
one-authority invariant: failed
completion: blocked
```

### Canonical-state verification

Normalization/state consolidation proof checks the semantic path: representative external/prior forms map correctly; required idempotence holds; ordinary consumers use canonical meaning; retained raw/persisted/compatibility/audit/presentation forms satisfy distinct contracts; former aliases/writers/fallback owners/normalization paths are inactive in checked scope. Renaming, deleting variables or centralizing syntax alone does not prove one-source-of-truth convergence.

### Closeout and continuation

| Evidence | Maximum scoped claim |
|---|---|
| source edited, no check | implemented / not tested, not working/fixed |
| focused/unit/regression passed | tested / verified-in-scope, not whole-system/live |
| fake/local scenario passed | fake/local verified-in-scope, not provider/deploy |
| one smoke passed | runtime-checked once, not stability |
| real provider/runtime/deploy checked | runtime/live-verified, not repeated reliability |
| matching reproduced failure corrected and checked | fixed in checked scope, not all edge cases |

For material closeout report checks/commands and result, covered scope, relevant exclusions and evidence-calibrated confidence. [accurate-communication.md](accurate-communication.md) owns status wording; [execution-and-goal-frame.md](execution-and-goal-frame.md) owns selected proof, continuation and closure. Continue safe required verification after implementation, not milestone-only stopping. Phase records include `Development Verification / TestKit Coverage` or equivalent when exit criteria depend on it; preserve a distinct verification task only when acceptance/owner/resume boundaries justify separation.

## Part C — Tactical/Strategic Programming

### Source tools and temporary work

Before writing a substantive workflow/browser/test script, inspect fitting project tools, harnesses, fixtures and test owners. Reuse or extend the authorized semantic owner rather than a parallel throwaway runner in temporary storage. Orchestration, assertions, setup/cleanup or evidence normalization needed for reproducibility/continued use are source-tool candidates from the first run. Keep reusable logic separate from run arguments/config and outputs; never copy credentials, browser profiles or secret-bearing captures into source.

A genuinely short-lived discriminating probe/inline transform without a durable role may remain temporary; do not create a permanent tool/framework for every command. If a probe becomes a reusable requirement, absorb validated relevant logic into the fitting owner before claiming that tooling complete, not just move the raw file or retain a second implementation. Missing owner/permission leaves a pointer and explicit blocked/deferred obligation; it does not authorize Suite assignment, a parallel runner or a legacy temporary-file sweep. [safe-io.md](safe-io.md) owns output capture, not source-tool lifecycle.

### Tactical scope and convergence

Tactical work is valid within selected strategy, or the checked current owner/contract when no separate strategy is selected: final-form local changes, focused diagnosis, reversible experiments, containment and bounded implementation. `TACTICAL` does not mean temporary debt. Correctly owned final-form work may close through proportionate proof without strategic ceremony or extra design/phase/convergence artifacts.

Tactical steps must not redefine architecture, ownership or scope. A separately declared target and convergence path is mandatory for workaround/compatibility bridge/provisional owner, material structure debt, emerging architecture or target divergence. Name target, bounded current slice, remaining temporary structure/debt, absorption/promotion/replacement/retirement path and closure trigger. If material target/closure is unclear, clarify before the temporary structure becomes authority. Expose this framing only when it changes a decision or preserves a real obligation.

Prefer local, reversible, low-blast-radius work; bound it so convergence remains feasible. No machine-local path/host/install assumption becomes a portable default unless explicitly machine-scoped; [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) owns edge binding. Persisting workarounds/patch stacks require retirement, absorption or formal promotion, not hidden permanence.

| Mode | Role |
|---|---|
| `TACTICAL` | bounded local execution/repair |
| `STRATEGIC` | target architecture/direction and staged program |
| `TACTICAL_WITH_STRATEGIC_TRACK` | bounded tactical work with emerging/material-debt target and convergence |

After migration cutover keep one active source/path/authority for the migrated role. Disconnect former imports/switches/env flags/factory branches/aliases/dual reads-writes/shadow/build-config-deploy-test discovery/target-failure fallback unless an explicitly approved temporary bridge owns them. Retained former code is execution-disconnected quarantine/inactive history, never normal discovery, fallback or restoration source. [action-safety.md](action-safety.md) owns bridge lifecycle/approval, deliberate known-good restoration and one-authority verification; [evidence-discipline.md](evidence-discipline.md) owns two-sided proof. While an approved bridge remains, migration is not complete.

[document-governance.md](document-governance.md) owns artifact forms: design is target truth, phase is staged execution, TODO durable tracking, and timestamped `patch/YYYY-MM-DDTHH-mm-ssZ--<semantic-slug>.patch.md` before/after review. Do not invent generic/root Patch forms or require artifacts for every local final-form change. Absorb validated temporary learning into the correct strategic owner at closure.

## Trigger Dispatch and Boundaries

- material source/state growth or a smell → Part A ownership/representation/decomposition gate; detection alone is not repair
- refactor or selected implementation → behavior preservation/completeness and Part B matching proof
- bug/missing value → discrimination and regression/gap classification before architecture
- changed architecture/state authority → selected path proof plus safety delta/approval; former-path inactivity only for affected migration scope
- temporary debt/path → Part C target and closure trigger; final-form local work needs no ceremonial track

Never replace semantic decisions with line counts, template architecture, identifier counts, facades or helper proliferation. Never infer capacity gaps from symptoms, safety from local/fake passes, stability from one smoke, or migration completion from target tests while dual paths remain. Verification, guards, comments and abstractions must serve the selected outcome—not manufacture future work.

## Integration

Claim thresholds: [evidence-discipline.md](evidence-discipline.md), [accurate-communication.md](accurate-communication.md). Scope/proof/artifacts: [execution-and-goal-frame.md](execution-and-goal-frame.md), [phase-todo-artifact.md](phase-todo-artifact.md), [document-governance.md](document-governance.md). Risk/worker/binding: [action-safety.md](action-safety.md), [worker-routing-and-context.md](worker-routing-and-context.md), [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md). Presentation: [explanation-and-presentation.md](explanation-and-presentation.md).
