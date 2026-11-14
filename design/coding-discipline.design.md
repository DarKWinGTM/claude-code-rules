# Design - Coding Discipline

> **Parent Rule:** [../coding-discipline.md](../coding-discipline.md)
> **Current Version:** 1.14
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [../changelog/coding-discipline.changelog.md](../changelog/coding-discipline.changelog.md)

---

## Target State

### Operational clarification

Choose storage by required lifetime, ownership, resume/reproduce dependency, recreation/recovery, loss impact, sensitivity and cleanup/rebuild lifecycle. Reusable logic belongs at the canonical source owner; approval/resume evidence needs retained private owner-controlled storage; disposable recreatable probes may be temporary. Sandbox/cache/container/tool workspaces and project `.tmp/` names confer no durability. Missing approval evidence cannot authorize an invented replacement baseline.


`coding-discipline.md` is the active runtime owner for maintainable code structure, proportionate verification, and tactical-to-strategic convergence.

Selected [runtime compaction](design/runtime-compaction.design.md) consolidates source-growth, decomposition, helper/comment and smell decisions into one operational form. Preserve canonical owner/representation stages, checked raw contracts, meaningful responsibility movement, semantic identifiers, debugging, architecture fitness and proportionate tests. A risk observation is not automatic permission for a runtime control or new state; prefer the simplest complete path within checked requirements.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for responsibility boundaries, helper/comment discipline, behavior-preserving refactor, debug/test depth, and tactical convergence.

### Structural assessment and approved refactoring

Inspect affected structure before material additions, during cumulative growth and before non-trivial closeout. Assess responsibilities, cohesion/coupling, change reasons, state/dependency lifecycles, side effects, callers and test boundaries. Length is a signal, not a hard LOC limit or automatic split; a large cohesive unit may stay local. Do not silently let small edits accumulate unrelated responsibilities, or broaden assessment into repository-wide cleanup.

Before any refactor, including local or low-risk extraction/splitting, present a concrete proportional plan and obtain explicit user approval. The plan identifies checked pressure and the simpler sufficient alternative, before/after responsibilities and dependencies, scope/exclusions, protected behavior/callers/failures/side effects, ordered small transformations, functional and structural proof, risks and stop/recovery. A short chat plan is sufficient for a small transformation; no mandatory new artifact. An approved plan covering the transformation can be reused without asking again. A feature/fix request is not consent to restructure existing code; ordinary scoped edits that do not restructure it are not automatically refactors. Classify the actual transformation, not its label.

[Execution](execution-and-goal-frame.design.md) owns continuation and material-deviation consultation; structural advice is not mutation authority. Meaningful improvement moves responsibilities/decisions, reduces original-unit burden or clarifies state/dependency/test boundaries while preserving behavior. More helpers/files, a facade or passing tests alone is not structural proof.

### Contract-first coding

Study decision-changing facts and the selected behavior before choosing predicates, representations or structure. Build sufficient understanding of data meaning, operation applicability, ownership, lifecycle, consumers and failure consequences; select the simplest complete implementation and matching proof. Scale effort to uncertainty, without a worksheet or process gate for every condition.

- Compare compatible meanings/units/stages and contract-defined relationships, not names or one sample. Required/optional depends on the operation; distinguish empty, known zero, unknown and invalid when their meanings differ. Diagnostic fields gain authority only through a contract.
- Keep canonical values and decisions at their owners. Consumers reuse results while inputs and assumptions remain valid, preserving checks for mutation, fresh/trust/transaction/recovery boundaries and genuine contradictions. Shared editors do not create another persisted policy owner.
- Scope conditions and outcomes to lifecycle/terminal contracts. Preserve independent delivery/integrity/settlement dimensions; reconcile producer/selector and consumer contracts rather than weakening a correct rejecting guard.
- Match access/persistence and protections to actual consumers, writers, sensitivity and failure models. Preserve raw/policy/domain stages, audit/fidelity/round-trip/history recovery, atomicity, authorization, privacy and real concurrency needs. Correctness and performance require different evidence.
- For material proposed representations, identify the purpose, actual consumer or explicit protocol/operator/privacy/audit/history/recovery contract, and what existing data cannot supply. Unknown purpose calls for bounded diagnosis, not speculative creation or deletion from a missing code reader. Compare reuse, derivation, transformation, copy/snapshot and persistence by validity lifetime, mutation/isolation, trust, privacy, consistency, recovery and carrying cost. One semantic owner need not mean one object or format. A read-heavy projection can justify refresh/write cost and acceptable staleness; immutable historical truth is not a disposable view. Rebuildability is not deletion permission or a reason to add a new pipeline.
- Before selecting a hash, determine the required guarantee: local equality/indexing, content/change identity, logical-operation idempotency, integrity/authenticity or secret protection. Choose inputs and primitives against sensitivity, collision consequences and threat/entropy requirements. Separate exact bytes, deterministic serialization and normalized domain meaning; sorted keys alone do not define universal equality. Preserve precision, units, absence/null and ordering when meaningful. Neither a universal canonicalizer nor direct comparison is prescribed. Trusted digests may be reused only while bound inputs and assumptions remain valid; a retained digest alone cannot validate fresh bytes. An unkeyed hash provides neither source authentication nor confidentiality, and password-specific work factors do not apply to every high-entropy token. Operation intent is independent of content equality: retries retain the selected logical identity, while identical parameters can describe intentional new operations.
- Place computation by tracing owner → inputs → result/digest → consumer → invalidation. Avoid unchanged parse/normalize/clone/serialize/hash/snapshot work that adds no function or is discarded/overwritten; reuse must preserve immutable snapshots, mutable isolation and evaluation/error/side-effect ordering. Distinct events, mutation, fresh reads and trust/transaction/recovery requirements can justify fresh work, including hashing inside loops. Do not add a cache/memoizer or move all work outside loops by default.
- Assess loop frequency, touched cardinality and per-item traversal/sorting/serialization/hash plus downstream rebuild/write work proportionately. Deterministic rehash is not nonce generation. Volatile time/random/counter/generated-version inputs can change a stable identity and trigger self-invalidating rebuilds; distinguish this conditional mechanism from an observed incident. Preserve genuine freshness/audit truth without arbitrarily excluding fields. Nonce uniqueness, salt and unpredictability follow the applicable protocol/security contract; never reuse a required-unique nonce as an optimization or invent hash-until-condition search to solve ordinary equality/versioning. Required security work may intentionally be expensive. Use checked implementations rather than designing cryptography.
- Match performance claims to the changed lifecycle. A primitive benchmark, fewer hashes or passing correctness checks is not whole-path CPU/memory evidence; representative matching measurements are needed only for the performance claim actually selected, not a benchmark campaign for every edit.

These are one general development method, not project-specific exceptions, independent rules or new additional trials. Refactor approval, scope, deletion authority and claim thresholds remain with their existing owners.

Research rationale: [Google review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html) supports understandable current-need design; [materialized-view guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view) illustrates contextual duplication trade-offs, not a selected infrastructure pattern. [RFC8785](https://www.rfc-editor.org/rfc/rfc8785.html) is Informational and constrains canonical JSON inputs, not arbitrary domain equality; [RFC5116 §§2.1/3.1](https://www.rfc-editor.org/rfc/rfc5116.html#section-3.1) illustrates scoped AEAD nonce requirements, not a universal nonce/replay rule. [NIST hash](https://csrc.nist.gov/projects/hash-functions)/[MAC](https://csrc.nist.gov/projects/message-authentication-codes), [OWASP password guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) and [operation-intent case study](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) support distinct guarantees; none selects one algorithm for all data. [Abseil measurement guidance](https://abseil.io/fast/70) limits primitive-to-application extrapolation; [build timestamps](https://reproducible-builds.org/docs/timestamps/) are a changing-output example, not proof of an application feedback incident. Engineering advice informs choices; normative requirements bind only their applicable contracts. No local performance or causal model benefit is established.

### Complexity and test-evidence admission

Judge added complexity against a simpler complete alternative, including required correctness, security, clarity and change boundaries. Identify what that alternative would lose, then weigh the benefit against added state/transitions, execution paths, dependencies, indirection, change propagation and setup/runtime/maintenance cost, including support work created by the addition itself. A possible benefit or new boundary is not automatic justification. Defer reversible generalization for hypothetical needs without postponing hard-to-reverse contract analysis or required safeguards. Passing tests for an addition establishes only their checked correctness, not the addition's necessity; do not replace this judgment with LOC ratios, element quotas or a mandatory worksheet.

Before expanding tests, fixtures or runners, identify the material evidence gap and the fault existing proof cannot distinguish; reuse or extend the fitting case first. Multiple layers for one behavior are justified when they catch distinct faults. A new helper, coverage percentage or test-to-product LOC ratio alone justifies neither test growth nor removal. Weigh confidence against setup/runtime cost, brittleness and maintenance while preserving selected acceptance and safety proof. Scope/closure remains with Execution; no new Rule, runner, numerical score or universal test-per-function mandate is introduced.

### Caller-first design, prevention and proof binding

For material interfaces, start with concrete caller usage, input/output and failure semantics, then derive types/signatures, module boundaries and implementation. Trace indirect consumers where their contracts change the decision; do not impose a design arena or worksheet on small edits. Choose the smallest effective code, type/schema, validator, Tool, Skill or Rule at its checked owner. Existing coverage is an integration point for useful enrichment, not a declaration that the incumbent is best; a correction alone grants no architecture expansion.

When claiming workflow coverage, connect the selected core contract to the owner case/selector admission, execution/assertions actually reached, terminal outcome and remaining proof. Reuse existing runner/report evidence and preserve its gaps, not a new mandatory inventory/runner/receipt. General proof selection remains here; detailed receipt accounting stays with its selected procedure and evidence thresholds stay with [Evidence Discipline](evidence-discipline.design.md).

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

Review the complexity/test-evidence variants in [Case 07](../playground/cases/case-07-coding-change-with-verification-discipline.md): hypothetical machinery versus a simpler complete path, unrelated caller coupling, required hard-to-reverse/safety work, existing-proof reuse, distinct-fault layers and passing-test/LOC-ratio limits. Existing `script/test-runtime-safety.mjs` checks the written admission clauses; it does not evaluate generated model behavior or prove reduced engineering cost.

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.

Case 18 validation must confirm a sanitizer/field regression repairs the existing path without new infrastructure, an invented path remains architecture-incomplete despite passing functional tests, ordinary repair stays proportionate, and a verified capability expansion proceeds only through the canonical design/safety/approval boundary.

[Case 07](../playground/cases/case-07-coding-change-with-verification-discipline.md) supplies virtual contract-first acceptance variants: optional-but-malformed, semantic comparison, valid-zero/unknown, reuse/revalidation, canonical/new-contradiction, terminal/independent outcomes, selector/correct-guard, actual writers/controls, editor authority and audit/recovery preservation. Its contextual-data pairs additionally protect legitimate projections/history, unknown-purpose diagnosis, purpose/input-bound hashing, exact-byte versus semantic guarantees, operation intent, discarded computation versus fresh validation, loop invalidation and required nonce/salt/freshness. Existing written-contract checks and one selected guided reader are complementary bounded proof, not a new evaluation framework. Clause/scenario review and installer tests prove their named text/installation scope, not future model compliance or causal improvement.

---

## P073-12 Runtime Compaction Refinement

Compact Integration and cross-owner consumer wording to canonical owner pointers while preserving activation, local consequence, exact error-prevention literals, body sufficiency, and every existing safety, verification, approval, and stop gate.
