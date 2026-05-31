# P001-05 — bounded executor policy and hook guardrails

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-05
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/bounded-executor-policy-and-hook-guardrails.patch.md](../patch/bounded-executor-policy-and-hook-guardrails.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [01-architecture-layers.design.md](../design/01-architecture-layers.design.md)
- [05-generated-artifacts-and-hook-posture.design.md](../design/05-generated-artifacts-and-hook-posture.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)

## Objective

Implement the bounded executor boundary, safe normalization allowlist, action-policy enforcement, and hook-light guardrails without letting automation outrun RULES authority or preservation boundaries.

## Why this phase existed

Earlier phases could observe, classify, and plan, but the plugin still needed a safe way to decide what may be executed automatically and what must remain blocked or approval-only.

## Expected Output

- executor-boundary and policy modules that separate advisory, guarded-execute, and bounded auto-normalize behavior
- explicit allowlist for deterministic low-risk classes only
- blocked/refusal handling for rename, deletion, lineage rewrite, authority reassignment, or unresolved preservation-risk classes
- hook-light reminder/guardrail scaffolds with no hidden mutation behavior
- focused tests proving blocked classes remain blocked and allowed classes stay bounded

## Completion Gate

- no executor path runs without an explicit target workspace path
- blocked classes remain blocked by default
- bounded auto-normalize candidates are reversible, reviewable, and limited to the approved low-risk class set
- hook behavior remains reminder-first / guardrail-second and does not mutate governed docs in the background
- focused tests pass for policy branching and blocked-class handling

## Out of Scope

- destructive cleanup
- governed file renames
- lineage reassignment
- authority reclassification
- broad background mutation hooks
- release-ready claims beyond checked policy behavior

## Affected Artifacts

Implementation surfaces created:
- `src/governed_docs/executor_policy.py`
- `src/governed_docs/normalizer.py`
- `src/governed_docs/hook_guardrails.py`
- `.claude/hooks/governed-docs-reminder.sh`
- `tests/test_executor_policy.py`
- `tests/test_bounded_normalizer.py`
- `tests/test_entry_surfaces.py`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Result: passed in checked scope
- Covers: policy branching for bounded-auto-normalize / blocked / guarded-execute / advisory modes, preview blocking for non-allowed items, preview allowance for safe candidates, advisory-only hook guardrail message/scaffold
- Does not cover: actual governed-file mutation, release-ready claims, hidden background hook activation
- Confidence: verified in checked scope for the executor-policy slice

## Risks / Rollback Notes

Contained risks:
- auto-normalize scope expanding too early
- hooks becoming hidden governance authority
- blocked classes being downgraded into convenience-based execution

Containment used:
- explicit policy decisions remain narrow and testable
- preview mode does not edit governed files
- hook scaffold is advisory/support-only and not treated as semantic authority

## Closeout Summary

Delivered result:
- governed-docs now has a bounded executor policy layer and a preview-only normalizer path for allowed low-risk candidates
- blocked classes remain blocked and hook guardrails stay support-only in checked scope

Impact:
- later release-gate and article presentation work can rely on a defined executor boundary without widening into unsafe mutation behavior

Next phase state:
- P001-06 is completed in checked scope as the release-gate layer
- no later phase requires reopening P001-05
