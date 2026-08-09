# Single-Authority Migration and Quarantine Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed — released and fresh-public-clone verified
> **Target Design:** [../design/design.md](../design/design.md) v10.58
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Before this patch, the installer preserved retired Markdown beneath `.claude/rules/.claude-code-rules-legacy-backup/`. Recursive Rules discovery could traverse that directory, so preserved material could remain active. Obsolete unchanged manifest-owned files were also deleted instead of quarantined.

## 2) Analysis

Risk: High for runtime authority and preservation; Medium for installer implementation.

Target state: one verified active authority, former material outside active discovery, no automatic fallback or dual read/write, and controlled restoration only through explicit approved replacement from an exact known-good source.

## 3) Change Items

### SAM-001 - Canonical migration lifecycle
- **Target:** `../action-safety.md` and triad
- **After:** migration/cutover, compatibility bridge, quarantine, inactivity proof, and controlled restoration have one operational owner; active bridges block completion.

### SAM-002 - Source and evidence consequences
- **Target:** `../coding-discipline.md`, `../evidence-discipline.md`, `../execution-and-goal-frame.md`, `../accurate-communication.md` and changed triads
- **After:** one active source after cutover; positive/negative proof; exact migration status wording; continuation while disconnection/proof remains.

### SAM-003 - Governed authority integrity
- **Target:** `../document-governance.md`, `../document-integrity.md` and triads
- **After:** active maps/install sets identify only current authority; quarantine/history cannot be active input/fallback; no-drift/migration-complete requires active reference/discovery proof.

### SAM-004 - External quarantine installer
- **Target:** `../script/setup-claude-code-rules.sh`, `../script/setup-claude-code-rules.ps1`, `../.gitignore`
- **Before:** quarantine lives below the active rules tree and obsolete unchanged manifest-owned files are deleted.
- **After:** quarantine lives at `<project-root>/.claude/quarantine/claude-code-rules/<run-id>/`; unchanged obsolete owned files are moved; prior installer-owned in-tree quarantine is evacuated intact; unknown/modified/unmatched/other-owner files remain untouched; normal install never reads quarantine; the complete 19-file payload and manifest are staged before replacement; bounded rollback state covers quarantine moves, active replacements, and manifest replacement if commit fails.

### SAM-005 - Matched fixture matrix
- **Target:** `../script/test-setup-claude-code-rules.sh`, `../script/test-setup-claude-code-rules.ps1`, installer/verification designs, Case 04, coverage, matrix
- **After:** historical candidate, manifest-owned, modified/unmatched, unrelated sentinel, evacuation, 19/19 parity/body, poisoning/unavailability, idempotency, controlled restoration, duplicate/traversal/managed-path-link rejection, and no-mutation preflight cases are covered equivalently.

## 4) Verification

Passed in candidate scope:
- nine planned triads align, the other ten runtime chains remain unchanged, and the Active Runtime Rule inventory remains 19;
- the exact 50-path allowlist and allowlisted local Markdown-link checks pass;
- Bash and PowerShell installers define the same ordered 19-file manifest contract;
- both disposable installer fixture matrices pass, including external quarantine, former-path removal from active rules, poisoning/offline rename independence, idempotency, controlled restoration, duplicate manifest rejection, linked `.claude`/rules/quarantine ancestor rejection, valid/broken manifest and active-target link rejection, deterministic no-mutation preflight failure, traversal rejection, and active-name collision rejection.

Passed in combined checked scope:
- final literals, force words, body-sufficiency, file-mode, README, and combined scenario gates;
- canonical/root parity 19/19, exact manifest order, unrelated-file preservation, retired-source absence below the active tree, and quarantine inactivity for the no-quarantine install.

Released-scope verification:
- clean `master`, peeled annotated tag, GitHub Release identity, and fresh-public-clone reproduction passed;
- positive target proof and negative former-path inactivity proof support `migration complete` in the named released scope.

## 5) Rollback Approach

Before publication, revert only scoped clean-lane changes. During installer commit, the implemented rollback journal restores installer-owned quarantine moves, active replacements, and manifest replacement if commit fails; this path is implementation-reviewed at candidate strength and is not claimed as fixture-injected proof. Runtime restoration requires explicit approval, exact known-good source/tag/commit verification, deliberate replacement through the normal installer, unrelated-file preservation, and post-restore one-authority verification. After publication, use a corrective release and never force-move the tag.
