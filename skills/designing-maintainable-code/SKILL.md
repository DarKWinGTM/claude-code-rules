---
name: designing-maintainable-code
description: Use when designing code or reviewing excessive complexity.
---

# Designing Maintainable Code

> **Current Version:** 1.0
> **Design:** [design/designing-maintainable-code.design.md](design/designing-maintainable-code.design.md) v1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Full history:** [changelog/designing-maintainable-code.changelog.md](changelog/designing-maintainable-code.changelog.md)

Choose structure that reduces the total burden of understanding, using and changing the selected code. A small implementation can still be incomplete; a longer cohesive one can be clearer than layers of wrappers. Assess the affected owner, not an unsolicited repository-wide redesign.

## Procedure

1. **Start with concrete use.** Read caller usage, inputs/outputs, failures, side effects and protected behavior. Separate required contracts from observations, preferences and speculative future needs. Identify the existing owner before proposing another module, state slot or path.
2. **Find the boundary's value.** Group responsibility by domain meaning, hidden knowledge, reason to change, dependency lifecycle and useful test boundary. Ask what a proposed unit hides and what callers no longer need to know. Compare that benefit with interface/parameter/state costs, call-chain hopping and change propagation. A cohesive flow may stay local; distinct responsibilities may earn a split proposal. Length and file/helper counts are signals to inspect, not verdicts.
3. **Distinguish shared meaning from coincidental similarity.** Reuse a rule with the same semantics and reason to change. Keep independently evolving policies separate when unifying them creates flags or branches for unlike callers. Extract a meaningful process or boundary only when its name and contract reduce understanding cost; avoid pass-through wrappers and speculative genericity. Do not remove an existing abstraction solely because duplication is possible.
4. **Trace data and work lifecycles.** Follow owner → inputs → transformation/result → consumer → invalidation. For each material representation or repeated parse/normalize/copy/serialize/hash, identify purpose, writers/readers, mutation, valid lifetime and recovery. Compare reuse, derivation, transformation, snapshot and persistence. Raw, validated, policy, audit/history and presentation data can have different contracts; one semantic owner need not mean one object or format.
5. **Compare the simpler complete alternative.** State what the addition preserves that the simpler route cannot, and count the carrying cost it creates: state transitions, dependencies, interfaces, synchronization, retained data, refresh/rebuild and downstream work. Reuse unchanged results only while inputs and assumptions stay valid. Preserve required fresh observations, authorization, mutable isolation, precision, failure/side-effect ordering and recovery; asynchronous or trust boundaries may justify repeated work. Choose a hash's required guarantee before changing its inputs or primitive. Do not add a cache or pipeline merely to avoid repeated expressions.
6. **Recommend and select proof.** Keep functional preservation, structural improvement and performance as distinct claims. Use affected regression/contract checks for behavior and inspect responsibility/dependency/call-flow changes for structure. Fewer operations or a microbenchmark alone does not prove application CPU/RAM benefit; measure a representative workload only when that claim is selected. Propose the smallest supported change, or retain the current code. Before any actual refactor, present its concrete plan and obtain explicit user approval; assessment is not mutation permission.

## Output

State the checked pressure and owner, recommended decision versus the simpler complete alternative, supported benefit/cost, protected behavior/state/failures, and matching proof or next discriminator. Valid decisions include keep local, extract, split, reuse, retain justified duplication/representation and unresolved. Name missing evidence without inventing architecture, safeguards or a required benchmark. Use only the depth the selected decision needs.
