# Status, Documentation, Memory, and Public-Surface Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.91
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P085-01 follows a memory-driven review of repeated work patterns. The selected scope covers five refinements: readiness-versus-completion wording, README current-state release sync, memory index hygiene, mechanism-first coordination design, and direct-user-transparent audience/public-surface disclosure control.

This patch is non-code/governance-only. It changes runtime rule doctrine and governed records; no product code or TestKit scenario is in scope.

Out of scope by explicit user direction: post-compact/resume gate enforcement or redesign.

---

## 2) Analysis

The current RULES system already has strong evidence wording, development verification, documentation-role, memory, worker-routing, and topology owners. The review found missing operational edges:

```text
Prepared is not live.
README is the current front page, not the history book.
MEMORY.md is an index, not the whole memory body.
Coordination design must start from the real mechanism, not an imagined transport.
Direct-user transparency is different from public-surface disclosure.
```

The target behavior should:
- prevent completion wording from outrunning evidence strength
- keep release README updates focused on current install/status/quality signals
- treat memory index bloat and loader warnings as maintenance triggers
- require mechanism classification before broad coordination/runtime design claims
- minimize sensitive/internal disclosure in generated public/operator/customer-facing artifacts while preserving full disclosure to the direct authorized user

---

## 3) Change Items

### SDM-001 — Readiness versus completion wording

- **Target artifacts:** `../accurate-communication.md`, `../development-verification-and-debug-strategy.md`, plus paired design/changelog files
- **Change type:** additive + metadata alignment

**Before**
```text
Rules already separate edited/tested/fixed and fake/local/live evidence, but status vocabulary can still collapse prepared/configured/tested/verified/live/fixed/stable states.
```

**After**
```text
Rules define a clearer status ladder: prepared, configured, implemented, tested, verified-in-scope, runtime/live-verified, fixed, and stable. Completion wording must name the evidence and avoid treating checklist readiness, local tests, fake adapters, or one-shot smoke checks as live/stable proof.
```

### SDM-002 — README current-state sync discipline

- **Target artifacts:** `../project-documentation-standards.md`, `../document-changelog-control.md`, `../README.md`, plus paired design/changelog files
- **Change type:** additive + metadata alignment

**Before**
```text
README and changelog roles are distinct, but release sync can still drift into changelog-style dumping inside README current sections.
```

**After**
```text
README release sync updates current-state sections: version/status cards, install arrays, active runtime count, latest refinement, quality signals, and current safety/runtime notes. Detailed version timeline belongs in changelog, not README body dumps.
```

### SDM-003 — Memory index hygiene maintenance trigger

- **Target artifacts:** `../memory-governance-and-session-boundary.md`, paired design/changelog files
- **Change type:** additive + metadata alignment

**Before**
```text
Root MEMORY.md is index-only, but overflow, loader warning, truncation, and entry-length recovery are not operationally explicit enough.
```

**After**
```text
Root MEMORY.md overflow or loader warnings are maintenance signals. Recovery should compact index entries, move detail into topic files, split or archive stale inactive entries, preserve path-scope pointers, and avoid deleting memory content merely because the index is too large.
```

### SDM-004 — Mechanism-first coordination design

- **Target artifacts:** `../native-worker-agent-routing-and-context-control.md`, `../runtime-topology-control.md`, plus paired design/changelog files
- **Change type:** additive + metadata alignment

**Before**
```text
Worker routing and runtime topology require intent and topology checks, but coordination-design work can still jump from desired behavior to assumed hook/transport capability.
```

**After**
```text
Coordination design must classify the actual mechanism first: passive shared board, local hook, injected context, tmux transport, recall/memsearch, official Agent Team, external plugin/MCP, or unavailable/unsupported mechanism. Design claims and runtime mutations must match checked mechanism capability.
```

### SDM-005 — Audience/public-surface disclosure owner

- **Target artifacts:** new `../audience-surface-disclosure-control.md`, `../design/audience-surface-disclosure-control.design.md`, `../changelog/audience-surface-disclosure-control.changelog.md`, `../natural-professional-communication.md`, and master records
- **Change type:** new active runtime rule + companion sync

**Before**
```text
Direct communication can be transparent with the user, and public onboarding is portable, but no first-class rule owns audience classification for generated public/operator/customer-facing artifacts.
```

**After**
```text
Direct authorized user/project-owner communication stays complete and transparent. Generated public, customer-facing, operator-facing, log, demo, or externally shared artifacts should disclose only audience-appropriate details and avoid leaking secrets, supplier identities, internal security mechanisms, credentials, private endpoints, raw user data, or implementation details that do not belong on that surface.
```

### SDM-006 — Master governance release sync

- **Target artifacts:** `../README.md`, `../design/design.md`, `../changelog/changelog.md`, `../TODO.md`, `../phase/SUMMARY.md`, this patch file, and `../phase/phase-085-01-status-doc-memory-surface-refinement.md`
- **Change type:** companion sync only

**Before**
```text
Master records are synchronized through v9.90 / P075-03 goal-first working-frame behavior with 44 active runtime rules.
```

**After**
```text
Master records record v9.91 / P085-01, active runtime count increases to 45 only if the new audience-surface disclosure owner is installed and verified, and runtime install/parity/body-sufficiency verification runs before release completion claims.
```

---

## 4) Verification

- [x] Runtime rule changes are limited to the listed active runtime owners plus the new audience-surface owner.
- [x] Readiness/completion wording distinguishes prepared/configured/implemented/tested/verified/live/fixed/stable states.
- [x] README current-state sync guidance does not turn README into changelog history.
- [x] Memory index overflow guidance treats loader warnings as maintenance signals without deleting memory content by cleanup instinct.
- [x] Mechanism-first coordination guidance stays Main RULES-level and does not import plugin-specific shared-board grammar.
- [x] Audience-surface disclosure preserves full direct-user transparency while constraining generated public/operator/customer-facing artifacts.
- [x] README Bash and PowerShell install arrays match the active runtime count.
- [x] Runtime install copies only README-listed active runtime rule files.
- [x] Source/runtime parity and body sufficiency pass for the active runtime install set.
- [x] No plugin/project-owned runtime destination files are touched.
- [x] Git push and GitHub release `v9.91` are verified.

---

## 5) Rollback Approach

If P085-01 proves too broad:
- narrow or revert only the selected status/documentation/memory/mechanism/audience-surface wording and companion record entries
- preserve P075-03 goal-first behavior unless separately challenged
- preserve P084 development verification, P081 worker routing, and P073-10 active runtime body-sufficiency boundaries
- if the new audience-surface owner is removed, update active runtime count, README install arrays, master design inventory, runtime install, and release records coherently
- do not delete or manage destination/runtime files outside the current source-owned active runtime install set as part of rollback
