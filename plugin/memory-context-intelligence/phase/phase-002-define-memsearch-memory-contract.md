# Phase 002 - Define memsearch memory contract

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 002
> **Status:** Completed
> **Design References:** [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Define the producer contract for memsearch-generated memory that this capsule depends on.

## Why this phase exists

The capsule is intentionally not generic optional-memory design. It depends specifically on memsearch-produced memory and therefore needs an explicit contract for scope, provenance, freshness, and unavailable behavior.

## Action points

- [x] define expected `.memsearch/memory/` source shape
- [x] define provenance expectations
- [x] define freshness and stale-handling posture
- [x] define missing/unavailable behavior as blocked or dormant
- [x] define the line between producer context and semantic authority

## Verification

- memsearch requirement is explicit and local to the capsule
- unavailable behavior does not invent context
- memory remains non-authoritative

## Exit criteria

- the dependency contract is explicit enough for later analysis behavior design
- the dependency does not accidentally become global root RULES infrastructure doctrine
