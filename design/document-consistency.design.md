# Document Consistency Rule

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.14
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-12)

---

## P094 Target-State Refinement: Delegated-Repair Consistency Gate

Document consistency now treats worker-edited governed documents as requiring leader verification before clean sync, no-drift, closeout, or release-ready claims.

The gate checks:
- meaning preservation and authority-role boundaries
- history/done reachability and cross-reference resolution
- version alignment
- phase/patch links when touched
- README install-array safety when relevant
- source-owned runtime install scope

Worker handoff is input, not proof.

---

## P093 Target-State Refinement: Worker-Gate No-Drift Check

Document consistency now checks worker-first aggregate-read gate compliance before broad sync, no-drift, closeout, or release-ready claims.

A broad claim is not clean when worker-fit aggregate reading was handled directly without a recorded narrow exception.

The worker handoff supplies filtered findings, conflicts, exact anchors, and leader verification needs; the leader still verifies selected anchors before final wording.

---

## P092 Target-State Refinement: God Artifact Automation Gate

Document consistency now checks that detected touched-scope God artifact pressure has an owned result.

Clean sync requires repair, visible repair planning, or an explicit blocker.
Version and link alignment alone are not enough.

---

## P091 Target-State Refinement: God-File Consistency

Consistency checks now include document role boundaries.

A synced artifact set can still drift if one active document absorbs unrelated roles or if a split, shard, or rollover loses required links.

No-drift claims should include this role-capacity check when touched governance docs are material.

## 1. Overview

### 1.1 Purpose

Set document consistency standards to:

- maintain consistency of names, paths, identifiers
- make cross-references accurate and verifiable
- update references when changes are made
- use precise references instead of vague descriptions
- keep source-side references distinct from destination/runtime references in onboarding/install docs
- distinguish governed design parent indexes, governed design child shards, source-owned active runtime files, active runtime body sufficiency, shared runtime destinations, and other-owner runtime files
- keep compact design index shard maps and child-shard authority boundaries aligned
- keep local execution paths distinct from reusable source-artifact references so tool-local paths do not silently become source contracts
- verify worker-edited governed documents before using them in clean sync/no-drift/closeout claims

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Inconsistent naming | Confused, can't find | Maintain consistency |
| Broken references | Links not working | Verify existence |
| Metadata-only active runtime roots | Install/parity claims can pass while runtime behavior is absent | Check body sufficiency for active runtime files |
| Stale references | Outdated information | Update all affected |
| Stale or orphan design shards | Child shards may look active while missing from the compact parent index | Verify parent shard map, child parent scope, and checked shard coverage |
| Vague descriptions | Don't know what this is referring to | Use precise refs |
| Source/destination blur | Readers cannot tell where an artifact comes from versus where it installs/runs | Separate reference roles explicitly |
| Parity scope blurred with destination ownership | Files in a shared runtime destination can be mistaken as owned or junk based on co-location alone | Separate source-owned install set, shared destination, and other-owner runtime vocabulary |
| File looks untracked/new so it gets treated as cleanup noise before reference checks | Governed references/history can be destroyed before the repo meaning is checked | Require master-surface, owner-scope, and cross-reference checks before disposal classification |
| Worker-edited governed docs are treated as clean from handoff alone | Meaning, links, or authority roles can drift without leader proof | Require delegated-repair consistency verification before clean claims |

### 1.3 Solution

Create a Consistency Framework that:

1. checks naming consistency
2. verifies references before use
3. updates dependencies when changing
4. always uses precise references
5. keeps portable shared references, source-side references, governed design parent indexes, governed design child shards, source-owned active runtime files, active runtime body sufficiency, shared runtime destinations, other-owner runtime files, destination/runtime references, and checked local facts semantically distinct

---

## 2. Core Rules

### 2.1 Consistency Requirements

- Keep names, paths, identifiers consistent across the whole response
- When referencing, ensure it exists or mark as unknown/unverified
- If change impacts multiple sections/files, describe dependencies
- Keep portable shared references distinct from checked local facts or machine-scoped examples
- Keep source-side references distinct from destination/runtime references when both appear in onboarding/install docs
- Keep governed design parent indexes distinct from governed child shards while verifying shard maps, parent scope, and selected-shard coverage
- Keep current source-owned active runtime install scope distinct from the shared runtime destination directory
- Keep active runtime body sufficiency distinct from metadata/header parity and hash parity when claiming install success or no-drift
- Keep other-owner runtime files distinct from the current project's parity/install target set unless their owner/project is explicitly selected or verified
- Treat worker-edited governed documents as unverified until the leader checks meaning preservation, role boundaries, links, and version scope
- Defer broader portable-default and anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 2.2 Reference Types

| Type | Example | Verification Method |
|------|---------|---------------------|
| File paths | `<workspace-root>/src/config.js` for portable examples, or exact checked local path when scoped | Glob / Read |
| Source-side install path | `<repo-root>` or `./` when the command is run from the repo root | Read / command-context verification |
| Governed design parent index | `design/<slug>.design.md` | Read parent index and verify shard map |
| Governed design child shard | `design/<slug>/<slice>.design.md` | Parent shard map + targeted Read |
| Destination/runtime path | `<install-root>`, `<user-runtime-rules>` | Read config/source contract when applicable |
| Source-owned active runtime files | checked README-listed active runtime rule set with substantive root bodies | Source inventory + body-sufficiency check |
| Shared runtime destination | `<user-runtime-rules>` as a destination that may contain several owners' files | Source/destination contract check |
| Other-owner runtime file | runtime-destination file outside current source-owned install set | Owner/project scope resolution |
| Symbols | `getUserById` | Grep |
| Commands | `npm run build` | Test execution |
| Config | `DATABASE_URL` | Read config source |

### 2.3 Shared Verification Trigger Model (WS-5)

Apply verification before finalizing references or consistency claims when triggers are present:

| Trigger | Typical Signal | Required Action |
|---------|----------------|-----------------|
| Concrete reference | file path, symbol, command, config key/value | verify existence/validity with tools before asserting |
| Cross-file consistency claim | "fully synchronized", "all references updated", "no drift" | verify all impacted files/sections before confirming |
| Rename/move/update impact | path or identifier changed in one place | trace and update dependent references deterministically |
| Ambiguous or unresolved reference | missing file/symbol or uncertain mapping | mark status explicitly and avoid unstated assumptions |
| Mixed source/destination wording | install docs blur clone/source path with installed/runtime path | separate the reference roles explicitly and normalize wording |
| Sharded active design references | parent index shard map, child scope, or selected-shard evidence may drift | verify parent-to-child links, child parent scope, and checked shard coverage |
| Parity scope blurred with destination ownership | install/parity wording treats the whole runtime destination as current-project owned | distinguish source-owned install set, shared destination, and other-owner runtime files |
| Active runtime body sufficiency | parity/no-drift wording checks metadata or hashes but not whether runtime behavior exists | verify substantive active runtime body before parity, no-drift, or release claims |
| Disposal or junk classification | file may still be referenced by governed repo surfaces or owned by another runtime source | check master surfaces, dependent references, and owner/project scope before classifying the file as cleanup noise |
| Worker-edited governed docs | worker changed governed artifacts | leader checks preservation, roles, links, versions, install safety, and runtime scope |

---

## 3. Implementation

### 3.1 Verification Flow

```text
Create Reference
  ↓
Does it exist or resolve?
  → YES: Use precise reference
  → NO: Mark as unknown/unverified
  ↓
What reference role is it?
  → portable shared reference
  → source-side reference
  → governed design parent index
  → governed design child shard
  → source-owned active runtime file
  → shared runtime destination
  → other-owner runtime file
  → destination/runtime reference
  → checked local fact
  → machine-scoped example
  ↓
Is it consistent with other references?
  → YES: Continue
  → NO: Fix inconsistency
```

### 3.2 Change Impact Analysis

```text
Making a Change
  ↓
Identify all affected references
  ↓
List dependencies
  ↓
Update all references
  ↓
Verify consistency
```

---

## 4. Output Standards

### 4.1 Precise References

**Preferred:**
- File paths: `<workspace-root>/src/config.js` for portable examples, or an exact path only when explicitly scoped as a checked local fact
- Source-side install guidance: `<repo-root>` or `./` when the command is explicitly intended for the repo root
- Destination/runtime guidance: `<install-root>`, `<user-runtime-rules>`, `<user-runtime-skills>`, `<user-runtime-agents>`
- Source-owned runtime install scope: the checked source inventory, not every file in the shared destination
- Other-owner runtime files: destination files outside the current source-owned install set until owner/project scope is explicitly selected or verified
- Line numbers: `config.js:42`
- Symbols: `getUserById()` function in `user.service.ts`

**Avoid:**
- "The config file"
- "That function we created earlier"
- "The variable somewhere in the code"
- one exact workstation path acting as both source path and destination/runtime path without explanation

### 4.1.1 Delegated-repair consistency labels

When worker-edited governed documents participate in a clean claim, report them as checked only after leader verification covers:
- meaning preservation
- authority-role boundaries
- history/done reachability
- cross-reference resolution
- runtime/design/changelog version alignment
- phase/patch links when touched
- README install-array safety when relevant
- source-owned runtime install scope

### 4.2 Verification Labels

```markdown
✅ Verified: `<workspace-root>/src/config.js` (portable example) or exact checked local path when scoped
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found: `/missing/file.js`
```

---

## 5. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Naming Consistency | 100% | Same thing = same name |
| Reference Verification | High | Check before referencing |
| Dependency Updates | 100% | All affected updated |
| Reference Precision | 100% | Specific, not vague |
| Portable-vs-local separation | High | Reference role stays explicit |
| Source-vs-destination separation | High |
| Source-owned/shared-destination/other-owner separation | High | Install-doc roles stay explicit |
| Active runtime body-sufficiency validation | High | Parity/no-drift claims check substantive runtime bodies |
| Delegated-repair consistency verification | High | Worker-edited governed docs are leader-verified before clean claims |
| Compact design index and child-shard consistency | High | Parent index shard maps and child scopes align |

---

## 6. Cross-Section Validation

### 6.1 Document Scanning

When modifying:
1. scan entire document for related references
2. identify all cross-section dependencies
3. update affected sections
4. verify consistency throughout

When classifying a newly encountered file as junk/disposable/non-governed:
1. scan the master repo surfaces that could assign governed meaning
2. identify whether dependent references or history entries already explain the file
3. if the file is in a shared runtime destination but outside the current source-owned install set, resolve owner/project scope first
4. keep the classification unresolved if the checked scope is still incomplete
5. do not treat missing immediate recognition or destination co-location as disposal proof

### 6.2 Change Propagation

| Change Type | Required Actions |
|-------------|------------------|
| Rename file | Update all imports/references |
| Move file | Update all paths |
| Rename symbol | Update all usages |
| Change config | Update all references |
| Normalize install docs | Update source-side, source-owned install scope, shared destination, and other-owner runtime wording separately |
| Shard active design | Verify compact parent index shard map, child parent/scope, orphan/stale shard status, and selected-shard claim boundaries |

---

## 7. Integration

### 7.1 Related Rules

| Rule | Relationship |
|------|-------------|
| no-variable-guessing | Verify values, not just existence |
| zero-hallucination | Don't fabricate references |
| functional-intent-verification | Verify intent of references |
| portable-implementation-and-hardcoding-control | Owns broader anti-hardcoding semantics and source-side versus destination/runtime notation discipline |
| document-design-control | Owns compact parent design index and governed child shard semantics |
| unified-version-control-system | Owns controller-level active runtime body-sufficiency validation |
| native-worker-agent-routing-and-context-control | Owns bounded edit-capable worker routing before delegated repair |
| context-load-and-document-density-control | Owns delegated repair routing for context-heavy God artifact pressure |
| authority-and-scope | Owns the runtime co-location non-ownership boundary |

### 7.2 Tool Usage

- **Glob**: Find file references
- **Grep**: Find symbol references
- **Read**: Verify content references

---

> Full history: [../changelog/document-consistency.changelog.md](../changelog/document-consistency.changelog.md)
