# Document Consistency and Cross-Reference Validation
> **Current Version:** 1.14
> **Design:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.14
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)
---
## Rule Statement
**Core Principle: Keep names, paths, identifiers, and cross-references consistent across checked scope while separating portable shared references, source-side references, governed design parent indexes, governed design child shards, source-owned active runtime files, active runtime body sufficiency, shared runtime destinations, other-owner runtime files, checked local facts, and machine-scoped examples.**
This rule owns cross-reference consistency, change propagation, and reference verification across files, sections, symbols, commands, and config values.
---
## Core Contract
### Consistency requirements
Required guidance:
- keep names, paths, identifiers, and references consistent across the response or checked artifact set
- verify concrete references or mark them unknown/unverified, and verify impacted files/sections before sync/no-drift claims
- update or describe dependencies when a change impacts multiple files/sections
- separate portable shared references, checked local facts, machine-scoped examples, source-side install paths, destination/runtime paths, governed design parent indexes, governed design child shards, source-owned active runtime install scope, shared runtime destinations, other-owner runtime files, and local execution paths
- keep governed design parent indexes and child shards aligned so shard maps, parent scope, and child target-state authority do not drift
- keep other-owner runtime files outside the current project's parity/install target set unless owner/project scope is explicitly selected or verified
- include active runtime body sufficiency when claiming source/runtime parity, no-drift, release readiness, or active runtime install success
- defer broader portability and anti-hardcoding to `portable-implementation-and-hardcoding-control.md`
### Reference roles and checks
| Type | Preferred form | Check |
|---|---|---|
| File/source path | `<workspace-root>/src/config.js`, `<repo-root>`, or repo-root `./`; exact path only as scoped local fact | Glob / Read / command context |
| Governed design parent index | `design/<slug>.design.md` as compact active index and authority gateway | Read parent index and verify shard map |
| Governed design child shard | `design/<slug>/<slice>.design.md` as active target-state detail | Parent shard map + targeted Read |
| Destination/runtime path | `<install-root>/skills`, `<user-runtime-rules>` | config/source contract check |
| Source-owned active runtime files | checked current-project install set with substantive root bodies, not every shared-destination file or metadata-only stub | checked source inventory + body-sufficiency check |
| Shared destination / other-owner runtime file | destination may contain several owners; non-members need owner/project scope | source/destination contract + owner resolution |
| Local execution path | exact current-machine/harness path only | execution context |
| Symbol / command / config | `getUserById`, `npm run build`, `DATABASE_URL` | search, run when needed, or read config source |
### Verification triggers
Verify before asserting:
- concrete references, cross-file sync/no-drift, rename/move/update impact, or ambiguous references
- mixed source/destination wording, parent-index-to-child-shard alignment, shard map completeness, orphan/stale shard status, or conflicting shard authority
- parity scope vs shared-destination ownership, active runtime body sufficiency, or worker-first aggregate-read gate compliance for broad scan claims
- worker-edited governed docs before sync/no-drift/closeout/release-ready claims
- tool-path leakage into reusable source or junk/disposal classification

If the checked scope is limited, report the non-finding as scoped rather than global absence.
---
### God-file consistency checks

Cross-document consistency includes checking that a sync did not move content into the wrong owner or overload one active file.

Required guidance:
- verify that current state, target-state design, version history, execution tracking, phase execution, patch review, and rollback detail remain in their owning surfaces
- when a touched document is split, sharded, or rolled over, verify parent/index links and child/history/done references
- include God Phase and God Patch split decisions in no-drift review when phase or patch files are touched
- do not claim sync/no-drift if active docs became role-overloaded even though versions and links match

### God artifact automation gate

Consistency review must verify that detected touched-scope God artifact pressure has an owned outcome.

A no-drift, sync, closeout, or release-ready claim is invalid when any touched governed document still has unresolved God pressure that is neither repaired nor represented as a visible governed repair slice.

Required checks:
- repaired local split, shard, rollover, or phase/patch split is reflected in links and indexes
- planned repair has a visible owner in task, TODO, phase, patch, or changelog context
- broad deferred repair is labeled as deferred and not hidden inside completion wording
- unresolved ambiguity is surfaced as a blocker, not converted into clean sync wording

### Worker-first aggregate-read consistency gate

Consistency review must verify that broad sync, no-drift, closeout, and release-ready claims were assembled through the worker-first aggregate-read gate when broad governance/code scanning was required.

A broad claim is invalid when the leader skipped worker-first filtering for a worker-fit aggregate read and no narrow direct-handling exception was recorded.

Required checks:
- worker handoff returned filtered findings, conflicts, exact anchors, and leader verification needs
- leader verified selected anchors before final sync/no-drift/release-ready wording
- direct leader handling is limited to narrow known files, exact edit/verify ranges, or a stated narrow exception
- skipped or incomplete gate handling is surfaced as a blocker, not converted into clean release wording

### Delegated-repair consistency gate

No sync, no-drift, closeout, or release-ready claim is valid when worker-edited governed documents have not been leader-verified. Worker handoff is input, not proof.

Leader verification must check:
- meaning preservation and authority-role boundaries
- history/done reachability and cross-reference resolution
- version alignment across runtime, design, and changelog surfaces
- phase and patch links when those surfaces are touched
- README install-array safety when install/onboarding surfaces are touched
- source-owned runtime install scope and active runtime body sufficiency

Skipped or incomplete delegated-repair verification is a blocker, not a clean sync result.

## Verification Flow
```text
Create reference
  ↓
Does it exist or resolve?
  → YES: use precise reference
  → NO: mark unknown/unverified
  ↓
What role?
  → portable shared / source-side / governed design parent index / governed design child shard / source-owned active runtime / shared runtime destination / other-owner runtime / checked local fact / machine-scoped example
  ↓
Consistent with related references?
  → YES: continue
  → NO: fix inconsistency
```
Change impact flow: identify affected references → list dependencies → update related references → verify consistency.
---
## Output and Cross-Section Standards
Use precise portable placeholders for shared examples (`<workspace-root>/src/config.js`, `<repo-root>`, `<install-root>`, `<user-runtime-rules>`), exact values only as checked local facts, stable line/symbol references when useful (`config.js:42`, `getUserById()`), and explicit labels:
```markdown
✅ Verified: `<workspace-root>/src/config.js`
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found In Checked Scope: `/missing/file.js`
```
Avoid vague references such as “the config file”, “that function”, “the variable somewhere”, or one workstation path acting as both source and destination/runtime path.
When exact local values are useful in a report, label them as checked local facts; when writing reusable source artifacts, prefer placeholders or env/config resolution. Source-owned active runtime install scope should point to the checked source inventory, not every file already present in a shared runtime destination. Source/runtime parity wording should name both source-owned install scope and body sufficiency; a hash match to a metadata-only root is not enough for no-drift. Other-owner runtime files stay outside parity/install claims unless their owner/project scope is explicitly selected or verified.
When modifying, scan related references, identify dependencies, update affected sections/imports/paths/symbols/config/install wording deterministically, and verify consistency. For sharded active designs, verify the compact parent index references the intended child shards, child shards identify or fit the parent scope, stale or orphan shards are not treated as active truth without checked linkage, and selected-shard reads are reported as scoped evidence rather than whole-design proof.
Change-impact expectations:
- renaming or moving files updates imports, links, install examples, and dependent paths
- renaming symbols updates usages and references where the checked scope supports a sync claim
- changing config keys or commands updates related docs, examples, and verification instructions
- normalizing install docs keeps source-side, destination/runtime, source-owned active runtime install scope, shared destination, and other-owner runtime wording separate
- claiming active runtime parity or no-drift checks root runtime body sufficiency as well as metadata, links, and hashes
When classifying a new file as junk/disposable/non-governed/safe-to-remove, first scan master surfaces and dependent history; resolve shared-destination owner scope; keep classification unresolved if checked scope is incomplete; and never treat missing recognition or co-location as disposal proof.
---
## Verification Checklist

- [ ] No-drift claims include God-file role-boundary checks for touched active governance documents.
- [ ] Broad sync/no-drift/closeout/release-ready claims include worker-first aggregate-read gate compliance or a recorded narrow exception.
- [ ] Worker-edited governed docs were leader-verified before clean sync/no-drift/closeout/release-ready claims.
- [ ] Split, shard, rollover, phase, and patch references remain reachable after God-file repair.

## Quality Metrics
| Metric | Target |
|---|---|
| Naming/reference consistency, verification, and dependency updates | High / 100% when claiming sync |
| Active runtime body-sufficiency verification | High / 100% when claiming parity or no-drift |
| Delegated-repair consistency verification | High / 100% when worker-edited governed docs are included |
| Portable/local, source/destination, and source-owned/shared-destination/other-owner separation | High |
| Scoped non-finding and unresolved owner wording | High |
| Compact design index and child-shard consistency | High |
---
## Integration
Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - verify values, not only existence
- [zero-hallucination.md](zero-hallucination.md) - do not fabricate references
- [functional-intent-verification.md](functional-intent-verification.md) - verify execution intent when references affect actions
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable/local and source/destination notation discipline
- [document-design-control.md](document-design-control.md) - compact design index and governed child shard role boundaries
- [unified-version-control-system.md](unified-version-control-system.md) - active runtime body-sufficiency and version-governance validation
- [authority-and-scope.md](authority-and-scope.md) - runtime co-location is not ownership authority
---
