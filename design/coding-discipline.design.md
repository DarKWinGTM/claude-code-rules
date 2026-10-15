# Design - Coding Discipline

> **Parent Rule:** [../coding-discipline.md](../coding-discipline.md)
> **Current Version:** 1.9
> **Session:** b8a3c38a-53b5-4d7d-a9ac-6a6f082911b2
> **Full history:** [../changelog/coding-discipline.changelog.md](../changelog/coding-discipline.changelog.md)

---

## Target State

`coding-discipline.md` is the active runtime owner for maintainable code structure, proportionate verification, and tactical-to-strategic convergence.

Selected [runtime compaction](design/runtime-compaction.design.md) consolidates source-growth, decomposition, helper/comment and smell decisions into one operational form. Preserve canonical owner/representation stages, checked raw contracts, meaningful responsibility movement, semantic identifiers, debugging, architecture fitness and proportionate tests. A risk observation is not automatic permission for a runtime control or new state; prefer the simplest complete path within checked requirements.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for responsibility boundaries, helper/comment discipline, behavior-preserving refactor, debug/test depth, and tactical convergence.

### Contract-first coding

Study decision-changing facts and the selected behavior before choosing predicates, representations or structure. Build sufficient understanding of data meaning, operation applicability, ownership, lifecycle, consumers and failure consequences; select the simplest complete implementation and matching proof. Scale effort to uncertainty, without a worksheet or process gate for every condition.

- Compare compatible meanings/units/stages and contract-defined relationships, not names or one sample. Required/optional depends on the operation; distinguish empty, known zero, unknown and invalid when their meanings differ. Diagnostic fields gain authority only through a contract.
- Keep canonical values and decisions at their owners. Consumers reuse results while inputs and assumptions remain valid, preserving checks for mutation, fresh/trust/transaction/recovery boundaries and genuine contradictions. Shared editors do not create another persisted policy owner.
- Scope conditions and outcomes to lifecycle/terminal contracts. Preserve independent delivery/integrity/settlement dimensions; reconcile producer/selector and consumer contracts rather than weakening a correct rejecting guard.
- Match access/persistence and protections to actual consumers, writers, sensitivity and failure models. Preserve raw/policy/domain stages, audit/fidelity/round-trip/history recovery, atomicity, authorization, privacy and real concurrency needs. Correctness and performance require different evidence.

These are one general development method, not project-specific exceptions, fourteen independent rules or new additional trials.

### Reusable tools and temporary work

Before writing a substantive workflow, browser or test script, inspect the fitting project tools, harnesses, fixtures and test owner. Reuse or extend the authorized semantic owner instead of implementing a parallel throwaway runner in temporary storage. Durable orchestration, assertions, setup/cleanup and evidence normalization are source-tool candidates from the first run when reproducibility or continued use is part of the objective, not only after repeated copies appear. Keep source logic separate from run arguments/config and outputs; never absorb credentials, browser profiles or secret-bearing captures into source.

A genuinely short-lived discriminating probe or inline transform without a durable role may remain temporary; do not create a permanent framework for every command. If a probe becomes a reusable requirement, absorb only validated relevant logic into the fitting owner before claiming that tooling complete, rather than move the raw file or retain a second implementation. Missing authority/permission leaves an explicit blocked/deferred obligation and evidence pointer; it does not authorize a Suite assignment, parallel runner or legacy temporary-file sweep. [Safe I/O](safe-io.design.md) owns bounded output capture, not this source lifecycle.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for maintainable code structure, proportionate verification, coding/debug root-cause narrowing, and tactical-to-strategic convergence.

P138 refinement: this owner should now require semantic/domain/behavior-first identifiers and bounded governed-doc source-comment linkage, so source names and comments explain implementation meaning without turning comments into duplicate documentation or stale governance pointers.

P146 refinement: this owner must add a proportional implementation-completeness check for material behavior, state/dependency boundaries, integration contracts, failure handling, required observability, and verification without speculative abstraction. After migration cutover, source structure must converge to one active implementation; former imports, flags, factories, aliases, dual read/write, shadow paths, discovery edges, and automatic fallback are removed or execution-disconnected unless an explicitly bounded temporary bridge remains under `action-safety.md`.

P150 / v1.6 refinement: this owner must distinguish an existing-path regression from a verified capability gap before infrastructure is added. A missing field, output, route result, or consumer-visible value does not prove missing architecture. Diagnosis maps the expected producer, state/transport, readers, writers, consumers, active design contract, and last-known-working evidence, then classifies existing-path regression, state/config drift, dormant/disconnected path, contract mismatch, unresolved state, or verified capability gap. Architecture-bearing changes also require functional proof through the selected path plus negative architecture-fitness proof against unauthorized alternate owner/route/client/transport/registry/state key/dual read-write/shadow/fallback/discovery. Functional tests for an unapproved path cannot satisfy architecture or completion gates.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Preserve semantic/domain/behavior-first naming as coding-time clarity doctrine rather than documentation ceremony.
- Keep governed-doc citations in source comments bounded to useful purpose, process, constraint, side-effect, or external-contract pointers.
- Require non-trivial implementation completeness without turning the gate into speculative abstraction or mandatory ceremony.
- Require post-cutover source convergence and keep any temporary compatibility code explicitly bounded, observable, and retirement-gated.
- Require regression-versus-capability-gap diagnosis before new infrastructure, using the existing producer/state/readers/writers/consumers path and last-known-working evidence when available.
- Require architecture fitness for architecture-bearing changes: functional proof through the selected design path plus negative no-alternate-authority checks.
- Keep passing tests for an unapproved or design-divergent path below the architecture/completion threshold while preserving ordinary focused verification for bounded in-authority repair.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact 19-Rule set is selected.

Historical detail remains in changelog or execution-disconnected quarantine/provenance surfaces, never as parallel runtime authority or source implementation.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.

Case 18 validation must confirm a sanitizer/field regression repairs the existing path without new infrastructure, an invented path remains architecture-incomplete despite passing functional tests, ordinary repair stays proportionate, and a verified capability expansion proceeds only through the canonical design/safety/approval boundary.

[Case 07](../playground/cases/case-07-coding-change-with-verification-discipline.md) supplies virtual contract-first acceptance variants: optional-but-malformed, semantic comparison, valid-zero/unknown, reuse/revalidation, canonical/new-contradiction, terminal/independent outcomes, selector/correct-guard, actual writers/controls, editor authority and audit/recovery preservation. Clause/scenario review and installer tests prove their named text/installation scope, not future model compliance or causal improvement.

---

## P073-12 Runtime Compaction Refinement

Compact Integration and cross-owner consumer wording to canonical owner pointers while preserving activation, local consequence, exact error-prevention literals, body sufficiency, and every existing safety, verification, approval, and stop gate.
