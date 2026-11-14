# Maintainable Code Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.0
> **Full history:** [../changelog/designing-maintainable-code.changelog.md](../changelog/designing-maintainable-code.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Help design or assess affected code whose responsibilities, abstractions, representations or repeated work create a material change/comprehension cost. Cover both under-decomposition and unnecessary indirection. This is an on-demand procedure, not a universal architecture, a score, or permission to restructure code.

Use it before a material structural addition or when accumulated growth affects the selected outcome. Small local changes need only their relevant contract check; do not turn every conditional into a worksheet. Diagnosis and test execution retain their existing procedure owners.

## Procedure Contract

Start with concrete caller usage, accepted inputs, outputs, failures, side effects, selected constraints and the existing semantic owner. Trace responsibility, hidden knowledge, dependencies, readers/writers and lifecycles before selecting file/module boundaries. Compare an owner-local implementation with extraction or a cohesive responsibility split; explain what knowledge and change propagation the boundary removes versus interface, parameter, state and navigation costs it introduces.

Reuse behavior when domain meaning and reason to change agree, not merely when expressions look alike. A longer cohesive unit can stay local; unlike policies can remain duplicated. Generalize for checked current variation, not speculative future consumers. Existing abstractions may also be retained or simplified when the evidence supports that choice.

Trace representations and computation through owner, inputs, transformation/result, consumer and invalidation. Compare reuse, derivation, normalization, copy/snapshot and persistence by valid lifetime, isolation, trust, consistency, recovery and carrying cost. Raw, validated, policy, historical and presentation forms can have distinct contracts. A current code reader is not the only legitimate consumer; history, audit, operator and protocol requirements matter. Unknown purpose is neither creation nor deletion permission.

Preserve freshness, security, identity, precision, required mutable isolation, failure/side-effect ordering and recovery. Repeated work across a mutation, fresh request or asynchronous boundary may be necessary. A retained result/digest is reusable only while its inputs and assumptions remain valid. Choose the required hash guarantee before primitive/input changes; neither fewer hashes nor fewer copies proves whole-path performance.

Output is a supported boundary/representation/work recommendation against the simpler complete alternative, with cost, protected behavior, affected owners and matching proof or next discriminator. Keeping the current implementation or leaving the decision unresolved is legitimate. Actual refactoring follows the existing concrete-plan and explicit-approval gate; this Skill does not execute a redesign by implication.

## Research Rationale and Limits

The checked sources support criteria, not a universally best decomposition or a measured benefit for a local system:

- [Parnas, original report](https://prl.khoury.northeastern.edu/img/p-tr-1971.pdf), printed pages14–18: information hiding isolates design decisions and their change impact rather than making every processing step a module. The illustrative comparison also warns that a careless implementation can increase runtime overhead; structural and performance claims are distinct.
- [Ousterhout, Modular Design](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign): ask about a module's unique value, hidden knowledge and minimum exposed interface. Shallow wrappers add interface cost; some interdependent long methods can stay intact. Somewhat generic interfaces can meet current needs without speculative features. Author heuristics are not size thresholds adopted by this procedure.
- [Metz, The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction): accumulating parameters/branches for unlike callers can reveal a wrong abstraction. Retaining duplication can be safer in that case; this is not an instruction to duplicate genuinely shared rules.
- [Google reviewer guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html): inspect design fit, comprehension and error risk, and avoid speculative genericity. This is organizational guidance, not empirical proof of a universal layout.
- [OWASP security principles](https://devguide.owasp.org/en/02-foundations/03-security-principles/): economy of mechanism coexists with complete mediation and fail-safe behavior. Simplicity is not permission to remove required fresh authorization checks.
- [Materialized View pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view): a derived representation can serve real query/consumer needs, balanced against refresh, storage, staleness, consistency and lifecycle costs. A rebuildable projection is not equivalent to immutable audit/history, and guidance about disposability does not approve local deletion.
- [Abseil Fast70](https://abseil.io/fast/70): mechanism counters and microbenchmarks can support investigation; application/service outcomes need matching evidence. Maintainability-only work does not acquire an automatic benchmark requirement.

## Invariants and Failure Boundaries

- LOC, file/helper/abstraction counts and test passes do not establish structural necessity or quality.
- Do not impose a cache, pipeline, generic canonicalizer, framework or alternate owner to solve an unverified symptom.
- Missing purpose or proof leaves a bounded question, not guessed state, deletion, authority transfer or a global absence claim.
- Keep functionally required guards, fresh/race checks, snapshots and durable recovery even when they resemble repeated work.
- Assessment is not refactor, deployment, deletion or live-operation approval. Preserve selected scope and unrelated behavior.

## Ownership and Development

This local design owns the procedure's target/rationale; `SKILL.md` owns invocation guidance and local history records changes. The library design owns shared curation, source-first development and separately selected deployment. Every new or extracted Skill gets its own fitting local design instead of moving its target truth into the shared catalog. Maintainer research/history are not mandatory runtime reading.

## Verification

Use existing source-library metadata, membership, reference, portability and written-contract tests. Pair keep-local versus split, shared semantics versus independent policies, and reusable immutable work versus required freshness/isolation cases against the actual draft. Preserve no-change and unresolved outcomes. Baseline success is valid, and synthetic interpretation is not causal model benefit, historical attribution, application speed or live proof. A selected refactor needs affected behavior and structural proof; a performance claim additionally needs representative workload evidence at its claimed boundary.
