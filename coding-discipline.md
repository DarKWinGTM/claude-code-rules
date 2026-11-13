# Coding Discipline
> **Current Version:** 1.13
> **Design:** [design/coding-discipline.design.md](design/coding-discipline.design.md) v1.13
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/coding-discipline.changelog.md](changelog/coding-discipline.changelog.md)
> **Absorbed:** maintainable-code-structure-and-decomposition v1.2, development-verification-and-debug-strategy v1.1, tactical-strategic-programming v1.3

## Rule Statement

**Core Principle: Choose the smallest complete implementation inside the selected direction and checked owner. Keep responsibilities, canonical state and side effects clear; add structure and verification only for material needs; preserve behavior during refactor; and close at the objective's selected proof level. Temporary paths or material debt require convergence, correctly owned final-form work does not.**

พูดง่าย ๆ: โค้ดต้องครบและแก้ง่าย แต่ไม่เพิ่ม abstraction, state, guard หรือขั้นทดสอบเพียงเพราะทำได้; รักษาความหมายและขอบเขตที่จำเป็นจริง.

## Part A — Maintainable Code Structure

### Responsibility and smallest useful decomposition

Maintainability means low future change cost: understandable intent, clear ownership, testability and visible side effects, not file/helper counts. Group by reason to change; separate business rules/orchestration/UI/persistence/integration/validation/formatting/config/operations only when ownership/change/test axes differ. Reuse project structure.

Before a material condition/representation/structure, trace behavior, valid inputs, failures, owner, lifecycle, callers and proof. Derive controls from checked contracts, not a familiar pattern/sample. Compare realistic alternatives including the simpler sufficient route; no mandatory worksheet/checklist per `if` or small edit. Assess accumulated concerns/aliases: small additions can hide another owner. Length/smells prompt investigation, not verdicts; retain uncertainty where ownership is unclear.

An addition is overengineering when a simpler complete alternative preserves behavior/safety/clarity and supported benefit cannot justify its burden. Ask what the alternative loses; possible benefit or new boundary alone does not earn added machinery. Weigh state/transitions, paths, dependencies, indirection, change propagation and setup/runtime/maintenance cost, including work created only to support the addition. Defer hypothetical reversible generalization, not analysis of hard-to-reverse contracts or required safeguards. Passing tests proves checked correctness, not necessity. Compare meaning/cost, not quotas or scores.

Inspect affected structure before material additions, during cumulative growth and before non-trivial closeout. Check responsibilities, cohesion/coupling, change reasons, state/dependency lifecycles, side effects, callers and test boundaries. A large cohesive unit may stay local; no hard LOC limits or automatic splitting. Do not silently accumulate mixed responsibilities through small edits or turn affected-code assessment into repository-wide cleanup.

Structural transformations below are recommendations, not permission to refactor existing code; apply the plan and approval gate before mutation.

| Checked condition | Required proportionate decision |
|---|---|
| cohesive responsibility, inline flow clearer | keep local; do not extract obvious expressions, assignments or wrappers |
| meaningful concept/process/test/side-effect step | extract only if the name and boundary reduce cognitive load and improve clarity/testability |
| different ownership, change reason, state/dependency lifecycle or test boundary | split a cohesive responsibility family; keep navigation/call flow easier afterward |
| shared behavior with the same meaning and reason to change | extract; coincidentally similar business rules may remain duplicated rather than falsely coupled |
| another value for an existing concept | identify canonical owner/form first; reuse it unless a distinct stage, lifecycle or contract earns a new representation |
| speculative interface/factory/strategy/plugin-like variation | avoid, simplify or justify from current variation/isolation evidence, not imagined futures |
| immediate repair safer than a justified structural split | bounded tactical edit with target owner, remaining material debt and convergence trigger |

For material interface design, start with concrete caller usage, input/output and failure semantics, then types/signatures and module boundaries before implementation. Trace affected consumers where their contracts change the decision; do not impose a design arena on small edits.

Helpers must earn indirection: a real concept, rule, process, reusable behavior or useful test/side-effect boundary should be clearer than inline code. Single-use helpers need meaningful names. Avoid trivial one-line/pass-through wrappers, excessive parameter threading and call-chain hopping; inline helpers with no semantic value.

For checked God-function/file pressure, inventory responsibilities, compare under/over-decomposition and propose a cohesive family seam. Preserve behavior; verify functional and structural improvement after approved execution. Progress means moved responsibility/decisions, reduced burden or clearer state/dependency/test boundaries, not files/aliases/facades/delegation. Batch by responsibility, not helper/task/phase/patch.

### Refactor plan and approval

Before any refactor of existing code, including local or low-risk extraction, splitting, renaming or reorganization, present a concrete proportional plan and obtain explicit user approval before mutation. A feature/fix request is not consent to restructure existing code; ordinary scoped edits that do not restructure it are not automatically refactors. Classify the actual transformation, not its label; local/tiny/tactical/behavior-preserving labels do not bypass approval.

The plan states checked pressure and the simpler sufficient alternative; before/after responsibilities and dependencies; scope/exclusions and protected behavior/callers/failures/side effects; ordered small transformations; functional and structural proof; risks and stop/recovery. A short chat plan suffices for a small refactor, with no mandatory new artifact. Reuse approval when an existing approved plan covers the transformation; [Execution](execution-and-goal-frame.md) owns continuation, material-deviation consultation and independent authorized work.

### Semantic source naming

Function, variable, helper, class, type, module and test-helper identifiers describe domain meaning, behavior, state or responsibility—not phase/document/ticket/patch/changelog/roadmap/review provenance. Necessary chronology belongs in governed documents or bounded useful source comments. Preserve literal tokens only for real external/domain contracts: protocol/stored values, API fields, migration identifiers, compatibility aliases or operator-facing literals. Derive names from checked project meaning, not placeholder examples.

### Canonical state and deliberate transformations

Understand state meaning, units, provenance and lifecycle before comparisons/prerequisites. Required/optional is operation-specific; preserve contract distinctions between absent, empty, known zero, unknown and invalid. Validate supplied/required data without inferring equality/arithmetic/presence/fallback from names or one shape. Diagnostic metadata governs decisions only by explicit contract.

One concept has one evident owner/canonical representation within its responsibility boundary. Parse/validate at ingress, normalize at semantic owner, resolve policy at its layer, format at egress. Consumers use canonical decisions, not repeated coercion/defaults/compatibility/adjudication. Reuse checks/computation while inputs/assumptions remain valid; mutation, fresh reads, trust or transaction/recovery may require recheck. A new function/consumer alone is not a trust boundary; canonical values cannot override new contradictions/safeguards.

Before another state slot, inspect owner, writers/readers, mutation and normalization. Preserve distinct raw/validated/domain/policy/persisted/audit/presentation stages and legible transitions. Match access/persistence to consumers, avoiding purposeless broad traversal/per-entity copies. Keep fidelity, diagnostics, audit/history/recovery/round-trip and required fresh/race checks; fewer keys/copies alone is not improvement. Shared editors need not move persistence or create policy authority.

Expose dependency/state/transform flow, binding env/config at edges rather than ambient state. Scope initialization/processing/retry/recovery to their lifecycle. Outcomes follow owning completion/failure contracts, not sticky first errors/latest events alone; preserve delivery/integrity/settlement independently. Before weakening rejection, trace producer/selector → state → consumer and reconcile selection/acceptance at the owner. Separate pure work/side effects when useful; keep normalization/errors/logging at boundaries. Move behavior/add types only for clearer responsibility or real error reduction.

### Names, comments and governed references

Names/structure explain normal flow. Comments explain non-obvious why/rules/order/constraints/side effects/contracts/compatibility/security/performance/concurrency/operational consequences—not syntax or unverified behavior. Prefer clearer code; update/remove stale nearby comments. Broad policy/spec/architecture stays governed.

Citations must lower maintenance cost: prefer stable design/contract rationale. Restrict phase/changelog/patch/ticket/route provenance to bridges/migration/compatibility/rollback or costly rediscovery. Ordinary source names/branches need no chronology tags. Comments stay verified, useful and local.

### Refactor and implementation completeness

Refactor preserves externally visible behavior unless change is explicitly selected. Separate structure and behavior changes when practical; use small transformations when behavior risk is high. Run relevant focused/regression tests, type checks, lint or bounded verification; incomplete proof limits claims of fixed/clean/stable.

Before non-trivial closeout, inspect material behavior, state/dependency, integration, failure, security, needed observability and verification gaps in the selected outcome. Happy path alone is insufficient when scope depends on errors, retries/idempotency, persistence, concurrency, rollback, cleanup or external contracts. Cover each material obligation or explicitly mark deferred, blocked, not applicable or out of scope with owner/reason where needed.

Choose the smallest effective prevention mechanism at its checked owner: code, type/schema, validator, Tool, Skill or Rule. Existing coverage identifies an absorption point, not proof that enrichment is unnecessary; merge useful complementary detail without duplicating authority. A correction alone does not authorize new architecture or persistent machinery.

Risk/test obligations do not themselves authorize guards/state/paths/queues/architecture. Derive controls from checked requirements, real readers/writers, sensitivity, lifecycle and failures—not imagined topology. A demonstrated fault/concrete in-scope risk earns a control only if better than a simpler complete path; required safety need not await incidents. Preserve identity/authorization/integrity/atomicity/privacy/recovery. Consult execution/safety owners for material acceptance/ownership/cost/scope changes; no speculative compatibility or negative proof beyond affected roles.

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

Strategy, not ceremony: stronger existing proof may replace a new scenario; a harness can replace fragile ad hoc checks. Each check protects changed behavior/material contract or closes the gate. Include representative valid forms and nearest failure/unchanged boundaries, not one fixture-shaped Product rule. Correctness, architecture and performance need distinct matching evidence. Expand for decision-changing risk/failure, not broad reruns/reassurance; live checks require selected scope, approval, safety and readiness.

Before tests/fixtures/runners, name the material evidence gap and failure existing proof cannot distinguish. Reuse or extend the fitting case first; multiple layers earn their place by catching distinct faults. Files/functions/coverage/LOC ratios alone justify neither growth nor removal. A behavior-preserving helper does not itself require a new test when proof suffices. Weigh confidence against setup/runtime cost, brittleness and maintenance; preserve selected acceptance and safety proof. Prefer observable contracts unless private order/isolation/resource behavior is required.

For selected workflow coverage connect selected core contract → owner case and selector admission → execution and assertions reached → terminal outcome → remaining proof. A registered or selected case is not executed coverage. Reuse the existing runner/report owner, retaining gaps; not a new inventory, runner or receipt mandate for small work or sufficient proof. Receipt reconciliation is a selected procedure, not test-admission authority.

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

Before a substantive workflow/browser/test script, inspect existing tools, harnesses, fixtures and test owners. Reuse/extend the semantic owner, not a parallel throwaway runner. Reproducible orchestration, assertions, setup/cleanup and evidence normalization are source-tool candidates from the first run; separate logic from run config/output. Never copy credentials, browser profiles or secret-bearing captures into source.

Choose storage by role/owner, required lifetime, resume/reproduce dependencies, recreation/recovery, consequences of loss, sensitivity/access and actual cleanup/rebuild lifecycle. Reusable source/test/tool logic belongs at its canonical owner. A run-bound approval manifest, snapshot or evidence needed to resume belongs in a retained, owner-controlled location for the entire required lifetime, with suitable access and an explicit recovery/retirement condition. Disposable, safely recreatable scratch/probes may use temporary storage. This applies to temp directories, sandbox filesystems, cache, ephemeral/container storage and tool workspaces; a project `.tmp/` name does not guarantee durability. If approval-bound evidence is missing, preserve the gap: an approved baseline must not be invented or replaced without its owning approval.

Short-lived discriminating probes need no permanent framework. When reuse becomes required, absorb validated logic into the fitting owner before tooling closeout, not just move the raw file or retain two implementations. Missing owner/permission leaves a pointer and blocked/deferred obligation, not Suite assignment, a parallel runner or legacy-temp sweep. [safe-io.md](safe-io.md) owns bounded capture; placement/retention follows this lifecycle contract.

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

- material/cumulative source growth or a smell → affected-structure assessment and proportional proposal; detection alone is not refactor permission
- refactor → concrete plan and explicit user approval before mutation, then behavior preservation and functional/structural proof
- selected implementation → completeness and Part B matching proof; do not silently add a refactor
- bug/missing value → discrimination and regression/gap classification before architecture
- changed architecture/state authority → selected path proof plus safety delta/approval; former-path inactivity only for affected migration scope
- temporary debt/path → Part C target and closure trigger; final-form local work needs no ceremonial track

Never replace semantic decisions with line counts, template architecture, identifier counts, facades or helper proliferation. Never infer capacity gaps from symptoms, safety from local/fake passes, stability from one smoke, or migration completion from target tests while dual paths remain. Verification, guards, comments and abstractions must serve the selected outcome—not manufacture future work.

## Integration

Claim thresholds: [evidence-discipline.md](evidence-discipline.md), [accurate-communication.md](accurate-communication.md). Scope/proof/artifacts: [execution-and-goal-frame.md](execution-and-goal-frame.md), [phase-todo-artifact.md](phase-todo-artifact.md), [document-governance.md](document-governance.md). Risk/worker/binding: [action-safety.md](action-safety.md), [worker-routing-and-context.md](worker-routing-and-context.md), [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md). Presentation: [explanation-and-presentation.md](explanation-and-presentation.md).
