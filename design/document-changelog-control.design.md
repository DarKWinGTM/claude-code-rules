# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.12
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-13)

---

### Chain-Scoped Version Detail Boundary

`changelog/<chain>.changelog.md` remains the active parent changelog and current version authority. Large same-chain version detail should prefer `changelog/<chain>/vX.YY-short-topic.changelog.md` shards when the parent would otherwise become expensive to read or verify.

`changelog/done/` remains available for legacy, archive, completed-history, or explicit fallback cases. Daily-first TODO and phase-summary rollover is owned by `governed-document-rollover-control.md`, so changelog files keep version authority without becoming the storage location for daily TODO/phase movement.

## P096-01 Target-State Refinement: Changelog Chain Version Detail Shards

The active changelog should stay current version authority, index, shard map, and navigation.

It should not become design target-state storage, phase execution, TODO tracking, README status, or an unbounded history dump.

Bulky same-chain version detail can move to chain-scoped version shards with active navigation preserved.

## 1) Goal

Define one deterministic documentation-version contract (UDVC-1) across runtime rules, design documents, changelog files, completed changelog history surfaces, TODO trackers, and patch artifacts.

---

## 2) Scope

Applies to governed documentation artifacts in this repository:

- root runtime rules (`*.md`, excluding overview-only/support documents)
- `design/*.design.md`
- `changelog/*.changelog.md`
- `changelog/<chain>/v*.changelog.md` when same-chain version detail is retained outside the active parent changelog
- `changelog/done/*.changelog.md` when legacy, archive, completed-history, or explicit fallback detail is retained outside the active scan surface
- `TODO.md`
- `patch/<context>.patch.md` or root `<context>.patch.md`

---

## 3) UDVC-1 Core Contract

### 3.1 Single Authority Per Chain

- Each governed chain has one authoritative active parent changelog.
- The active parent changelog controls latest version state, current index, shard map when present, and forward navigation for that chain.
- Runtime, design, and patch artifacts reference that authority through `Full history` links.
- Same-chain detailed version entries may move under `changelog/<chain>/vX.YY-short-topic.changelog.md`, but only as detail shards that the active parent changelog indexes.
- Completed or older legacy/archive/fallback history may move under `changelog/done/`, but only as inactive-by-default history that the active changelog still points to when navigation or audit continuity requires it.

### 3.2 Rule-Chain Alignment

For rule-governed chains, these values must match:

- runtime rule `Current Version`
- runtime rule `Design` reference version
- design `Current Version`
- changelog `Current Version`

### 3.3 Session Integrity

- Active metadata uses real session identifiers from the active environment.
- Placeholder values are not allowed in active metadata.
- `LEGACY-*` markers are allowed only for preserved historical records where the original active session is unavailable.

---

## 4) Mandatory Metadata Contract

### 4.1 Runtime Rule Header Contract

Root runtime rules use this canonical header contract:

- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the only allowed label for root runtime design references.
`Based on:` is retired for root runtime rule metadata.

### 4.2 Design / Patch Metadata

Required active metadata:

- `Current Version`
- `Session`
- `Full history`

### 4.3 Changelog Metadata

Required active metadata:

- `Parent Document`
- `Current Version`
- `Session`

---

## 5) Pair Behavior

When a design/changelog pair exists for one governed chain:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| `*.design.md` | Active-state design body + `Full history` navigation | Embedded version tables, detailed changelog sections, historical rollout logs |
| `*.changelog.md` | Current version authority, current index, shard map when present, detailed version sections when small enough, and `Version History (Unified)` | Table-only history, design-state guidance, or unindexed shard offload |

Historical detail belongs in changelog files, not in the active design body. README release sync should consume changelog state only to update current sections; detailed version timelines remain in changelog rather than being copied into README.

### 5.1 Chain-Scoped Version Detail Shards and Completed History Surface

`changelog/<chain>/vX.YY-short-topic.changelog.md` is the preferred split target when a large active changelog needs to retain detailed same-chain version entries outside the compact parent.

Required version-shard guidance:
- the active parent changelog remains the current version authority and primary navigation surface
- each version detail shard belongs to one parent chain and links back to that parent
- the parent must map versions to shards so readers are not forced to discover files by guessing
- a version detail shard is not an independent changelog authority
- exact historical content should be preserved during migration unless an explicit governed rewrite is selected

`changelog/done/` may hold legacy, archive, completed-history, or explicit fallback changelog detail when chain-scoped version shards are not the right shape.

Required `done` guidance:
- `changelog/done/` is inactive by default for ordinary current-state scans
- consult `changelog/done/` only when history, audit, rollback, provenance, or trace reconstruction needs it
- moving history into `changelog/done/` does not make it junk and does not authorize deletion
- design-specific history should move through changelog governance, not `design/done/`

---

## 6) Canonical Anchor Policy

- Version-table links use canonical `#version-xy` anchors.
- Line-number anchors are not the version-navigation standard.

---

## 7) Execution Order Contract

When synchronizing governed documentation:

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

---

## 8) Required Patterns

### 8.1 Runtime Rule Header

```markdown
# <Rule Name>

> **Current Version:** X.Y
> **Design:** [design/<rule>.design.md](design/<rule>.design.md) vX.Y
> **Session:** <real-session-id>
> **Full history:** [changelog/<rule>.changelog.md](changelog/<rule>.changelog.md)
```

### 8.2 Changelog Header

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <real-session-id>
```

### 8.3 Version Detail Shard Header

```markdown
# Changelog Detail - <Document> vX.YY <Topic>

> **Parent Changelog:** [../<doc>.changelog.md](../<doc>.changelog.md)
> **Version:** X.YY
> **Session:** <real-session-id>
```

### 8.4 Design Footer

```markdown
> Full history: [../changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

---

## 9) Verification Checklist

- [ ] Each governed chain has one authoritative parent changelog
- [ ] Runtime-rule header uses `Design`, not `Based on`
- [ ] Active runtime headers include `Session`
- [ ] Rule/design/changelog versions are aligned for governed rule chains
- [ ] Design files keep active guidance only
- [ ] Changelog parent files hold current version authority, index, shard map when present, and navigation
- [ ] Version detail shards are same-chain detail surfaces and link back to their parent
- [ ] Active changelogs retain current version authority when detail moves to version shards or `changelog/done/`
- [ ] `changelog/done/` is treated as legacy/archive/fallback history, not junk or deletion authority
- [ ] Version links use canonical `#version-xy` anchors
- [ ] Synchronization order was followed

---

## 10) Quality Metrics

| Metric | Target |
|--------|--------|
| Rule-chain alignment accuracy | 100% |
| Runtime header contract consistency | 100% |
| Active placeholder session markers | 0 |
| Historical detail left in active design bodies | 0 critical cases |
| Active changelog authority lost to version shards or `changelog/done/` | 0 critical cases |
| Broken `Full history` links | 0 |

---

## 11) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-design-control.design.md](document-design-control.design.md) | Active-state design-body contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository-wide document-role boundary and completed documentation surface model |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker boundary |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | UDVC-1 controller view |

---

> Full history: [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md)
