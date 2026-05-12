# Edit-Capable Governed-Document Repair Delegation Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active
> **Target Design:** [../design/design.md](../design/design.md) v10.02
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

P094 is a governance-only release that extends worker-first reading into bounded edit-capable repair.

The target behavior is not worker autonomy over governed meaning. It is delegated, meaning-preserving repair under explicit scope and leader verification.

---

## Analysis

P093 reduced leader context load by requiring worker-first filtering before broad governance/code aggregate reads.

A remaining failure mode appears after detection: clear document repair can still fall back to the leader, forcing the leader to absorb context and perform low-risk restructuring while the primary objective waits.

The target behavior should be:
- allow native edit-capable workers such as `general-purpose` to repair bounded governed-document issues
- require explicit file/section ownership and non-overlapping edit boundaries
- preserve document meaning, authority role, history reachability, and cross-references
- block deletion, silent summarization-away, status upgrades, or authority-moving edits
- require worker handoff with anchors, preservation notes, checks, unresolved risks, and leader verification needs
- keep final sync/no-drift/closeout/release-ready claims with the leader

---

## Change Items

### 1) Worker-routing owner

- **Target artifacts:** `native-worker-agent-routing-and-context-control.md` and design/changelog companions
- **Change type:** additive
- **Current state:** worker routing supports broad read/filter lanes and edit-capable lanes when edit ownership is explicit.
  It does not define a first-class governed-document repair lane for native edit-capable workers.
- **Target state:** define bounded edit-capable governed-document repair delegation.
  Workers may edit only within explicit non-overlapping scope and must return preservation-aware handoff evidence for leader verification.

### 2) Context-load and density owner

- **Target artifacts:** `context-load-and-document-density-control.md` and design/changelog companions
- **Change type:** additive
- **Current state:** clear low-risk touched-doc God-line repair is expected, and broad/meaning-risky cases must be planned.
  Delegating that repair to edit-capable workers is not explicit.
- **Target state:** add delegated repair as an action route for context-heavy document-density and God-artifact repair.
  Delegated repair is allowed only when it is meaning-preserving, bounded, low-risk, and leader-verifiable.

### 3) Document-consistency owner

- **Target artifacts:** `document-consistency.md` and design/changelog companions
- **Change type:** additive
- **Current state:** no-drift and release-ready claims require worker-first broad-read compliance and repaired/planned God pressure.
  Worker-edited governed documents do not yet have a dedicated preservation verification gate.
- **Target state:** add a delegated-repair consistency gate.
  Broad sync/no-drift/closeout/release-ready claims require leader verification that worker-edited governed documents preserved meaning, authority role, history reachability, and cross-references.

### 4) Master and release surfaces

- **Target artifacts:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, and P094 phase/patch records
- **Change type:** synchronization
- **Current state:** v10.01 / P093 is released; P094 phase and patch records are active for v10.02 source synchronization.
- **Target state:** v10.02 / P094 is recorded as active, then released after gates pass.
  Runtime install count remains 47.

---

## Verification

Before closeout:
- README Bash install array contains exactly 47 active runtime files.
- README PowerShell install array contains exactly the same 47 active runtime files.
- Runtime install copied only the README-listed source-owned active runtime rules for the current 47-file set.
- Source/runtime parity and source/destination active runtime body sufficiency passed for 47/47 files.
- Touched owner chains define delegated edit-capable repair consistently.
- Delegated repair wording does not authorize deletion, semantic damage, history loss, authority-role mutation, or unchecked final claims.
- Touched active docs avoid new God-line or God-document overload.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- README, master design, master changelog, TODO, phase, and patch records align to v10.02 / P094.
- `master` push and GitHub release `v10.02` verification must pass before closeout.

---

## Rollback Approach

If rollback is needed:
- revert the P094/v10.02 delegated repair changes through a governed rollback
- reinstall the prior v10.01 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, unrelated runtime destination files, or other-owner files as cleanup

---

## Current Status

Patch remains active/pre-release. Runtime install, 47/47 source/runtime parity, source/destination active runtime body sufficiency, and density/God-artifact review passed. Push and GitHub release `v10.02` verification remain pending.
