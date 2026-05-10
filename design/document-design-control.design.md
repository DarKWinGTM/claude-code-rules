# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.12
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-10)

---

## P091 Target-State Refinement: Design God-File Prevention

Design documents should remain active target-state authority.

If target-state scope is broad, use a compact parent index with coherent child shards.

If size comes from history, execution, TODO, patch, audit, or rollout detail, move that content to the appropriate owner instead of the active design body.

## 1) Goal

Define one deterministic structure for design documents that stays aligned with UDVC-1 governance, keeps active design state separate from historical records, supports compact active design indexes with governed child shards for large design surfaces, preserves implementation-relevant knowledge extracted from external docs/specs when later work still depends on it, and keeps design as active blueprint authority rather than a completed-work `done/` surface.

---

## 2) Scope

Applies to:

- `design/*.design.md`
- `design/<slug>/*.design.md` governed child design shards when a compact parent index is needed
- master design documents maintained in `design/`
- design-to-changelog pair behavior
- support-artifact boundaries when content should not behave like a governed design doc
- the boundary that `design/` remains active target-state space and does not use `design/done/` by default

---

## 3) Core Standards

### 3.1 Naming and Location

- Governed design documents use `<name>.design.md`.
- Governed design documents live under `design/`.
- Large governed designs may use a compact parent index at `design/<slug>.design.md` and governed child shards under `design/<slug>/*.design.md`.
- Their authoritative changelog lives at `changelog/<name>.changelog.md` when the chain has a dedicated changelog.

### 3.2 Mandatory Metadata

Each governed design document includes:

- `Parent Scope`
- `Current Version`
- `Session`
- `Full history`

### 3.3 Active-State Body Rule

Design documents describe the current active target state.
They must not embed:

- detailed version-history tables
- audit snapshots
- remediation logs
- rollout-completion journals
- obsolete pending/activation instructions

Historical detail belongs in changelog files or, when volume needs inactive history separation, in `changelog/done/` under changelog governance.

### 3.3.1 No Default Design Done Surface

`design/` is active blueprint and target-state authority, not a completed-work archive.

Required guidance:
- do not create or normalize a default `design/done/` pattern
- keep implementation-relevant target truth in active design files until superseded or removed from the active target state
- move historical explanation to changelog surfaces instead of parking old blueprint state under `design/done/`
- if a legacy design snapshot must be retained, label it as historical/reference-only and keep it outside active design authority

### 3.3.2 Governed Design Sharding Rule

A governed design may be sharded when the active design body is too large for safe repeated reading or when distinct target-state slices are clearer as separate child documents.

Required structure:
- `design/<slug>.design.md` remains the compact active parent index and authority gateway
- `design/<slug>/*.design.md` contains governed active child design shards for coherent target-state slices
- child shards remain active design truth by default, not `design/done`, changelog history, or archive material
- parent index content must include purpose, authority boundary, current target-state summary, shard map, shard-selection/read guidance, and full-history navigation
- child shards should identify their parent index/scope and avoid conflicting with sibling shards or the parent summary
- broad shard review should start from the parent index and read only relevant shards unless an audit explicitly needs wider coverage

This pattern is not daily-first TODO/phase rollover. It keeps active design truth in active design surfaces while reducing context load and improving targeted reads.

### 3.4 Navigator Rule

When a paired changelog exists, design documents:

- keep version-history navigation limited to `Full history`
- do not embed detailed changelog sections
- do not duplicate historical summaries inside the active body

### 3.5 Rule-Chain Alignment

For rule-governed chains, design version must align with:

- runtime rule `Current Version`
- runtime rule `Design` reference version
- changelog `Current Version`

### 3.6 Doc-Derived Knowledge Capture Rule

When external documentation, API specifications, provider references, or comparable implementation authorities materially constrain the implementation, the implementation-relevant extracted knowledge must be normalized into the governed design layer before or alongside continued multi-step work that relies on it.

Required guidance:
- do not rely on transient reading memory alone for contract-critical external requirements
- capture the implementation-relevant truth in design before treating it as stable working context for later execution slices
- capture extracted knowledge rather than copied source prose
- if the external source materially determines request parameters, authentication requirements, callback expectations, field semantics, state transitions, acceptance criteria, or integration constraints, those constraints should be made visible in design
- compact/session continuity limits are part of the reason this capture is required; the governed design layer should preserve reusable implementation truth so later execution does not depend on re-reading the same source unnecessarily

### 3.7 Extraction Specificity Rule

A design capture derived from docs/specs should be specific enough that later implementation can answer:
- what the external source requires
- which part of the implementation is constrained by that requirement
- what values/fields/parameters/flows matter
- what should be sent, accepted, stored, validated, or rejected because of that requirement
- which details are active implementation truth versus source-side background detail that does not need to be carried forward

---

## 4) Support-Artifact Boundary

Not every reference artifact belongs in governed design space.
If a file is reference-only, prompt-only, media-only, or support-only, it should not remain in an ambiguous `.design.md` state unless it is fully normalized as a governed design document.

Use clearly non-governed placement or naming for support-only artifacts.

---

## 5) Reference and Anchor Policy

### 5.1 Canonical Version Anchors

Governance documents use canonical `#version-xy` anchors for version navigation.

### 5.2 Link Discipline

- Use resolvable relative paths.
- Keep design → changelog and changelog → design references consistent.
- Keep active design docs free of stale line-reference audit notes.

---

## 6) Required Design Template

```markdown
# <Document Name>

## 0) Document Control

> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <real-session-id> (YYYY-MM-DD)

---

<active design content>

---

> Full history: [../changelog/<name>.changelog.md](../changelog/<name>.changelog.md)
```

---

## 7) Verification Checklist

- [ ] File uses governed design naming only when it is truly a governed design document
- [ ] Required metadata fields are complete
- [ ] Design body is active-state only
- [ ] Historical detail is delegated to changelog or `changelog/done/` when inactive history separation is needed
- [ ] No default `design/done/` pattern is introduced for active blueprint governance
- [ ] Large sharded designs keep a compact active parent index and governed active child shards with clear shard maps and read guidance
- [ ] External-doc/spec-derived implementation truth is captured in design when later work still depends on it
- [ ] Captured knowledge is normalized and implementation-relevant rather than copied source prose
- [ ] Runtime rule references use `Design`, not `Based on`
- [ ] Rule/design/changelog versions are aligned where applicable
- [ ] Links resolve correctly

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Active-state-only design-body compliance | 100% |
| Compact design index and child-shard authority clarity | High |
| Navigator compliance in paired design docs | 100% |
| External-doc-derived implementation truth captured when material | High |
| Ambiguous governed-looking support artifacts | 0 |
| Broken design/changelog links | 0 |
| Stale historical guidance inside active design bodies | 0 critical cases |
| Default `design/done/` usage for governed blueprint docs | 0 critical cases |
| Link-only parent index or hidden child-shard authority drift | 0 critical cases |

---

## 9) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Version authority and metadata contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role boundaries and completed documentation surface model |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |

---

> Full history: [../changelog/document-design-control.changelog.md](../changelog/document-design-control.changelog.md)
