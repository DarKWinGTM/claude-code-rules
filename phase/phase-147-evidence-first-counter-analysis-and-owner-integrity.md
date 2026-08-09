# Phase 147 - Evidence-First Counter-Analysis and Owner Integrity

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 147
> **Status:** Active — implementation complete; integration verification pending
> **Target Release:** v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md), [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/communication-register.design.md](../design/communication-register.design.md), [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md)
> **Patch References:** [../patch/evidence-first-counter-analysis-and-retraction.patch.md](../patch/evidence-first-counter-analysis-and-retraction.patch.md), [../patch/changelog-role-vocabulary-correction.patch.md](../patch/changelog-role-vocabulary-correction.patch.md), [../patch/internal-helper-authority-boundary.patch.md](../patch/internal-helper-authority-boundary.patch.md)

---

## Objective

Make Claude verify decision-changing premises before endorsing broader architecture, preserve a checked completed baseline until evidence shows a real gap, correct unsupported agreement or prior recommendations explicitly, align changelog repair routing to real owners, and let bounded helper work reduce user research burden without widening objective or authority.

## Lineage Decision

- P146 is released and closed.
- P147-01 overlaps P146's proactive-design concern, but P147-02 and P147-03 repair independent changelog and authority contracts with distinct outputs and gates.
- A P146 child would not truthfully contain the combined correction family; P147 is therefore a new major.
- Each child closes independently before parent release convergence.

## Child Map

- **P147-01:** [phase-147-01-premise-before-expansion-and-explicit-retraction.md](phase-147-01-premise-before-expansion-and-explicit-retraction.md)
  - Output: premise-before-expansion, completed-baseline protection, proactive counter-analysis, evidence-shaped agreement, and explicit recommendation retraction.
  - Gate: false/supported/incomplete premise branches and invalidated-recommendation behavior pass through Cases 14/17/05 and focused static checks.
- **P147-02:** [phase-147-02-changelog-role-vocabulary-correction.md](phase-147-02-changelog-role-vocabulary-correction.md)
  - Output: active same-chain version detail and inactive reference history route to their actual governed owners with no fallback owner.
  - Gate: triad, master changelog, README, Case 09, and link/literal checks align.
- **P147-03:** [phase-147-03-internal-helper-authority-boundary.md](phase-147-03-internal-helper-authority-boundary.md)
  - Output: advisory new objective/durable expansion is distinct from internally selected bounded helper topology under the canonical routing owner.
  - Gate: one-helper, real-Team-dependency, reuse, user-restriction, subordinate-output, and leader-verification branches pass through Cases 01/14.

## Shared Boundaries

- Keep exactly the existing 19 Active Runtime Rule filenames.
- Leader/Main owns Active Rule edits, final integration, README, canonical/root installation, git, tag, Release, and final verification.
- Helpers remain bounded analysis/review/testing support; no helper becomes objective or source authority.
- Do not mutate, clean, delete, push, reset, stash, merge, or rebase the dirty backup checkout.
- Do not change ticket application/data paths, installer behavior, worker-routing doctrine, or document-governance doctrine in this wave.
- README receives surgical current-state/release-anchor edits only.
- Rollover preserves history and never authorizes deletion.

## Lane Map

1. P147-01 reasoning and communication triads plus Cases 14/17/05.
2. P147-02 phase/TODO triad plus master changelog vocabulary and Case 09.
3. P147-03 authority triad plus Cases 01/14; worker routing remains byte-identical.
4. Governed synchronization, rollover, playground matrix, and README candidate alignment.
5. Verification, canonical/root installation, publication, and fresh-clone proof.
6. Post-release read-only 19-Rule duplication/conflict/context audit.

## Development Verification / TestKit Coverage

Verification route: existing scenario families, focused static assertions, unchanged Bash/PowerShell installer fixture matrices, disposable installation, and fresh public clone.

Required branches:
- false premise warns before downstream design and preserves the completed baseline;
- supported premise allows evidence-earned broader design with material obligations;
- incomplete evidence selects a discriminating check;
- invalidated assistant advice is explicitly retracted and re-anchored;
- bounded helper work is internally invokable while durable expansion remains advisory;
- changelog active detail and inactive history resolve to real owners with no fallback path.

Current evidence: four changed triads pass focused semantic/version checks and `git diff --check`; rollover reference/body checks pass. Broader scenario, fixture, install, parity, and release gates remain pending.

## Risks and Rollback

Risks:
- premise checks can become ceremony for trivial work;
- correction can become reflexive disagreement;
- helper authority can be mistaken for objective expansion;
- candidate docs can overclaim release state before publication.

Rollback/containment:
- before publication, revert only P147's clean-lane allowlist;
- stop canonical synchronization on overlapping unrelated edits;
- preserve exact rollover snapshots and bidirectional references;
- after publication, use a later corrective release and never force-move the public tag.

## Exit Criteria

- All three children reach `verified` independently.
- Exactly four runtime/design/changelog triads advance; the other 15 Runtime Rules remain byte-identical to v10.58.
- Active inventory and Bash/PowerShell manifests remain ordered-identical at 19.
- Playground branches, fixture matrices, disposable install, body sufficiency, parity, manifest order, and unrelated-file preservation pass.
- Canonical source and installed root Rules match the verified candidate.
- Clean master, annotated v10.59 tag, GitHub Release, and fresh public tag clone resolve to one released result.
- The post-release efficiency audit is delivered separately and does not mutate v10.59.
