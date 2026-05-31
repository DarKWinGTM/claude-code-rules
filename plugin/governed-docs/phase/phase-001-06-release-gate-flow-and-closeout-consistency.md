# P001-06 — release-gate flow and closeout consistency

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-06
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/release-gate-flow-and-closeout-consistency.patch.md](../patch/release-gate-flow-and-closeout-consistency.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [05-generated-artifacts-and-hook-posture.design.md](../design/05-generated-artifacts-and-hook-posture.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)
- [04-skills-and-agent-system.design.md](../design/04-skills-and-agent-system.design.md)

## Objective

Implement the governed-document release-gate flow so closeout and release-shaped wording can be checked against evidence strength, cross-surface consistency, and the current implementation state.

## Why this phase existed

The plugin needed a dedicated gate for deciding whether governed-document work is ready for stronger completion wording. Earlier layers could scan, classify, and plan, but they still could not answer the final question: does the checked governed surface set support a pass / pass-with-notes / rework / blocked verdict?

## Expected Output

- release-gate module and command surface
- verdict states `pass`, `pass-with-notes`, `rework`, and `blocked`
- checks for wording strength, cross-surface current-state agreement, and unresolved drift status
- focused tests proving gate outcomes stay aligned to checked evidence

## Completion Gate

- release-gate output is derived from checked implementation state and supporting governed surfaces rather than wishful completion wording
- verdicts remain distinct and testable
- gate results do not overclaim release-ready status beyond checked scope
- focused tests pass for verdict branching and evidence-strength handling

## Out of Scope

- non-doc runtime/deploy proof outside the selected governed surface scope
- generic framework extraction beyond RULES-specific v1
- public/operator wording that hides evidence limits

## Affected Artifacts

Implementation surfaces created:
- `src/governed_docs/release_gate.py`
- `src/governed_docs/commands/release_gate.py`
- `tests/test_release_gate.py`

Operator route exercised through existing entry surfaces:
- `src/governed_docs/cli.py`
- `bin/governed-docs`

Governed sync surfaces updated during closeout:
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `patch/release-gate-flow-and-closeout-consistency.patch.md`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Ran: `./bin/governed-docs release-gate /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs`
- Result: 40 tests passed; release-gate returned `Verdict: pass` for the governed-docs workspace after README/front-page sync
- Covers: verdict branching logic, release-gate command routing, checked governed-surface completeness for the current plugin chain, and evidence-bounded pass wording in checked local scope
- Does not cover: broader external deployment/runtime truth outside the selected plugin workspace
- Confidence: verified in checked scope for the release-gate slice

## Risks / Rollback Notes

Contained risks:
- overclaiming readiness from partial implementation
- collapsing evidence-grounded notes into oversimplified verdicts
- mixing governed-doc gate results with unrelated runtime/deploy truth

Containment used:
- verdict states stay explicit and testable
- checked scope stays visible in the gate output
- release-gate remains a governed-doc closeout surface, not a universal deployment truth source

## Closeout Summary

Delivered result:
- governed-docs now has a real release-gate module, command surface, and verdict model in checked scope
- the plugin-local chain now includes its README front page, allowing the active governed-surface set to pass the release-gate check in checked local scope

Impact:
- closeout wording can now be driven from a defined gate instead of from ad hoc completion summaries

Next phase state:
- P001-07 is completed in checked scope as the final article-presentation slice
