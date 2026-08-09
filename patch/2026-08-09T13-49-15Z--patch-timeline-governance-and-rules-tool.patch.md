# Patch Timeline Governance and RULES Tool

> **Current Version:** 1.0
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Status:** active
> **Created At:** 2026-08-09T13:49:15Z
> **Creation Evidence:** Single UTC instant captured by the exclusive Node.js bootstrap that created this file with `wx`; the same instant produced this filename and metadata.
> **Target Design:** [RULES System](../design/design.md) v10.64; [Document Governance](../design/document-governance.design.md) v1.20; [Phase, TODO, and Artifact Initiation](../design/phase-todo-artifact.design.md) v1.35; [Document Integrity](../design/document-integrity.design.md) v1.13
> **Full history:** [Patch changelog](../changelog/patch-timeline-governance-and-rules-tool.changelog.md)

---

## Context

Governed Patch artifacts describe their semantic topic but currently lack deterministic chronological identity derived from verified artifact creation time. This patch reviews the RULES doctrine, reusable Tool, verification, installation, and release changes that establish that identity without Patch IDs or a Patch index.

## Analysis

The selected contract uses one verified UTC instant for the filename and `Created At` metadata. Legacy migration remains evidence-gated; mtime/ctime and indirect chronology are not accepted as creation proof. Exact governed references are rewritten only through an approved hash-bound manifest, while suspended archives and serialized payloads remain excluded.

## Change Items

### 1. Patch identity doctrine — `replacement`

**Before:** semantic Patch filenames are self-identifying but not chronologically sortable and Patch metadata does not record original creation time.

**After:** `document-governance.md` owns `YYYY-MM-DDTHH-mm-ssZ--<semantic-slug>.patch.md`, matching `Created At` metadata, Creation Evidence, preservation semantics, and explicit no-ID/no-index boundaries.

### 2. Patch creation lifecycle — `additive`

**Before:** startup chooses whether Patch is needed but does not require one-time UTC capture or exclusive creation.

**After:** `phase-todo-artifact.md` requires one-time UTC capture, shared filename/metadata derivation, collision refusal, and exact Phase references.

### 3. Legacy rename integrity — `additive`

**Before:** general rename propagation exists without Patch-specific evidence, manifest, exclusion, and preservation requirements.

**After:** `document-integrity.md` owns evidence-backed manifests, exact reference propagation, source/reference hashes, suspended-archive preservation, and former-path inactivity proof.

### 4. Reusable Patch timeline Tool — `additive`

**Target:** `script/patch-timeline.mjs`

**Before:** the path did not exist, so RULES had no executable interface for deterministic Patch inventory, evidence audit, planning, creation, apply, verification, or rollback.

**After:** the new dependency-free Node.js ESM exports the reviewable behavior anchors below and exposes the matching CLI commands:

```javascript
parsePatchFilename(name)
inventoryPatches({ root, archivePrefixes, excludePrefixes, evidenceByPath })
buildManifest({ root, archivePrefixes, excludePrefixes, evidenceByPath })
createPatch({ root, patchDir, slug, title, creationEvidence, session, targetDesign, fullHistory, execute, approvedManifestSha256 })
applyManifest({ root, manifest, execute, approvedManifestSha256, journalPath })
verifyManifest({ root, manifest })
rollbackJournal({ root, journal, execute, approvedJournalSha256 })
```

```text
inventory → audit-evidence → plan → create | apply → verify → rollback
```

Dry-run defaults, exact approval hashes, exclusive creation, source/reference hash and mode preflight, owner-only manifest/journal output, file-and-directory-synced journal persistence before mutation, descriptor-bound Linux directory operations with ancestor-symlink rejection, same-directory synced staging plus no-clobber source publication, atomic reference replacement, exact-target reference resolution, archive sentinels, and restartable partial-state-aware rollback bound the mutation path. Unknown CLI flags fail closed. Focused `node:test` fault boundaries exercise ordinary interruption and symlink-substitution recovery; no kernel power-loss claim is made without a dedicated crash/filesystem harness.

## Verification

- The 32 focused Tool tests cover timestamp parsing, creation evidence, stable preview-to-execute timestamp replay, single-line metadata enforcement, exclusive create, manifest count parity, deterministic exact references with URI exclusions, durable journal ordering, source/reference publication interruption boundaries, final hash/mode revalidation before replacement or removal, restartable rollback, ancestor-symlink substitution, apply/verify/rollback, CLI contract alignment, and archive preservation.
- Playground positive and forbidden-negative assertions cover the combined doctrine.
- NodeClaw read-only inventory/audit/plan returned 576 selected, 199 preserved, 0 mutation rows, and 576 evidence blockers; repeated before/after witnesses kept all 775 Patch paths, bytes, modes, aggregate SHA-256, and Git status unchanged.
- The existing Bash/PowerShell installer matrices and a two-pass disposable candidate install pass with exactly 19 Runtime Rules and no Tool installation.
- Exact 27-path candidate/canonical parity and two canonical root-install passes prove 19/19 byte-and-mode parity, 19 manifest rows, Tool exclusion, unrelated-file preservation, no quarantine, and identical converged state.
- Publication and fresh public master/tag verification remain pending and must pass before closeout.

## Rollback Approach

Before publication, revert only the clean candidate allowlist. Canonical synchronization and root installation stop on overlap or parity drift. NodeClaw receives no mutation in this wave. After publication, preserve the annotated tag immutably and correct defects through a later release.
