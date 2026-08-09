# Phase 146-02 - Single-Authority Migration and Quarantine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Parent Phase:** [phase-146-active-runtime-strategic-completeness-and-authority-convergence.md](phase-146-active-runtime-strategic-completeness-and-authority-convergence.md)
> **Phase ID:** 146-02
> **Status:** Active
> **Target Release:** v10.58
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/action-safety.design.md](../design/action-safety.design.md), [../design/coding-discipline.design.md](../design/coding-discipline.design.md), [../design/evidence-discipline.design.md](../design/evidence-discipline.design.md), [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/document-governance.design.md](../design/document-governance.design.md), [../design/document-integrity.design.md](../design/document-integrity.design.md), [../design/design/installer-architecture.design.md](../design/design/installer-architecture.design.md), [../design/design/verification-and-integration.design.md](../design/design/verification-and-integration.design.md)
> **Patch References:** [../patch/single-authority-migration-and-quarantine.patch.md](../patch/single-authority-migration-and-quarantine.patch.md)

---

## Objective

Require migrations and authority replacements to finish with one verified active source/path/authority, preserving former material only as execution-disconnected quarantine or inactive history and using explicit deliberate restoration instead of automatic fallback.

## Selected Semantic Obligations

1. Target behavior and current/target authority are identified and verified.
2. Compatibility bridges are temporary, named, observable, owner-bound, and retirement-gated.
3. Cutover selects one active authority.
4. Former imports, reads/writes, flags, aliases, factories, config/build/deployment/test-discovery edges, shadow paths, and automatic fallback are removed or execution-disconnected.
5. Quarantine is outside active discovery and is not authority, normal source, fallback, restoration source, or deletion permission.
6. Migration proof combines positive target behavior with negative former-path inactivity; one grep non-finding is insufficient.
7. Normal runtime/install/retry/restart/rebuild/deployment/test paths do not read quarantine.
8. Quarantine poisoning, rename, or unavailability does not affect normal target behavior.
9. Controlled restoration requires explicit approval, exact known-good source verification, deliberate replacement, unrelated-file preservation, and one-authority reproof.
10. Migration-complete wording remains blocked while any bridge/link/proof gate is open.

## Installer Scope

- Move installer quarantine to `<project-root>/.claude/quarantine/claude-code-rules/<run-id>/`.
- Rename active `legacy_*` identifiers toward retired/quarantine semantics; retain the prior literal path only as a migration input.
- Quarantine unchanged obsolete manifest-owned files instead of deleting them.
- Evacuate installer-owned prior in-tree quarantine intact without interpreting contents; stop on collision/ambiguity.
- Preserve unknown, modified, unmatched, and other-owner files.
- Stage the complete 19-file payload and manifest before replacement, and maintain bounded rollback state for quarantine moves, active replacements, and manifest replacement if commit fails.
- Add matched Bash/PowerShell fixture tests for historical candidates, manifest ownership, duplicate/traversal/managed-path-link rejection, no-mutation preflight failure, evacuation, idempotency, poisoning, parity, and controlled restoration.

## Development Verification / TestKit Coverage

Verification route: `new_focused_test` plus existing playground Case 04.

Required proof:
- active manifests ordered-identical at 19;
- disposable source/destination parity and body sufficiency 19/19;
- no source-owned former `.md` remains below the active rules tree;
- external quarantine is not consulted during normal install;
- unmatched/modified/unrelated files remain byte-identical;
- rerun is idempotent and never restores quarantine;
- controlled restoration fixture installs one verified known-good source through the normal path and leaves one active authority;
- matched Bash and PowerShell matrices pass equivalent ownership, quarantine, disconnection, restoration, duplicate/traversal/managed-path-link rejection, no-mutation preflight, and collision cases.

## Current Disposition

- Canonical cutover owner, source-convergence consumer, evidence/status/document projections, execution continuation, and Case 04/matrix: implemented; focused checks passed in the clean candidate scope.
- Bash and PowerShell installers: implemented with external execution-disconnected quarantine, fail-closed ownership preflight, staged 19-file payload plus manifest replacement, and bounded rollback journals for commit-phase failure; rollback is implementation-reviewed at candidate strength, not fixture-injected proof.
- Matched Bash and PowerShell fixture matrices: tested and passed in candidate scope.
- Canonical synchronization and root installation: verified in scope with 19/19 source/runtime parity and body sufficiency, exact 19-row manifest order, preservation of four unrelated runtime files, no retired source-owned Rule below the active tree, and no quarantine creation for the no-quarantine install.
- Terminal disposition: not yet verified; publication identity and fresh-public-clone gates remain.

## Risks and Rollback

- A hidden directory inside `.claude/rules/` can still be recursively discovered.
- Broad moves can overwrite unrelated files or lose historical material.
- A restoration helper can accidentally create permanent fallback authority.
- A commit-phase interruption can leave quarantine, active payload, and manifest state inconsistent if transactional rollback does not run as designed.

Containment: fail closed on ownership ambiguity or destination collision; stage the payload and manifest before replacement; retain rollback state for installer-owned moves/replacements; never broad-delete; never read quarantine during normal execution; require explicit restoration approval and exact source proof. Commit-failure rollback remains implementation-reviewed, not fixture-injected proof.

## Exit Criteria

- Five migration-focused triads plus shared `coding-discipline`/`execution-and-goal-frame` changes align to planned versions.
- Bash and PowerShell fixtures pass all required cases.
- Canonical/root installation proves external quarantine, 19/19 parity/body, and unrelated-file preservation.
- Fresh public clone reproduces installer, scenario, and single-authority proof.
