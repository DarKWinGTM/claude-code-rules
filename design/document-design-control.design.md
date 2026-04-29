# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.10
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-04-29)

---

## 1) Goal

Define one deterministic structure for design documents that stays aligned with UDVC-1 governance, keeps active design state separate from historical records, preserves implementation-relevant knowledge extracted from external docs/specs when later work still depends on it, and keeps design as active blueprint authority rather than a completed-work `done/` surface.

---

## 2) Scope

Applies to:

- `design/*.design.md`
- master design documents maintained in `design/`
- design-to-changelog pair behavior
- support-artifact boundaries when content should not behave like a governed design doc
- the boundary that `design/` remains active target-state space and does not use `design/done/` by default

---

## 3) Core Standards

### 3.1 Naming and Location

- Governed design documents use `<name>.design.md`.
- Governed design documents live under `design/`.
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
| Navigator compliance in paired design docs | 100% |
| External-doc-derived implementation truth captured when material | High |
| Ambiguous governed-looking support artifacts | 0 |
| Broken design/changelog links | 0 |
| Stale historical guidance inside active design bodies | 0 critical cases |
| Default `design/done/` usage for governed blueprint docs | 0 critical cases |

---

## 9) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Version authority and metadata contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role boundaries and completed documentation surface model |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |

---

> Full history: [../changelog/document-design-control.changelog.md](../changelog/document-design-control.changelog.md)
