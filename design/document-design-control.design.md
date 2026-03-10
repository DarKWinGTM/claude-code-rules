# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.8
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2 (2026-03-08)

---

## 1) Goal

Define one deterministic structure for design documents that stays aligned with UDVC-1 governance and keeps active design state separate from historical records.

---

## 2) Scope

Applies to:

- `design/*.design.md`
- master design documents maintained in `design/`
- design-to-changelog pair behavior
- support-artifact boundaries when content should not behave like a governed design doc

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

Historical detail belongs in changelog files.

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
- [ ] Historical detail is delegated to changelog
- [ ] Runtime rule references use `Design`, not `Based on`
- [ ] Rule/design/changelog versions are aligned where applicable
- [ ] Links resolve correctly

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Active-state-only design-body compliance | 100% |
| Navigator compliance in paired design docs | 100% |
| Ambiguous governed-looking support artifacts | 0 |
| Broken design/changelog links | 0 |
| Stale historical guidance inside active design bodies | 0 critical cases |

---

## 9) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Version authority and metadata contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role boundaries |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |

---

> Full history: [../changelog/document-design-control.changelog.md](../changelog/document-design-control.changelog.md)
