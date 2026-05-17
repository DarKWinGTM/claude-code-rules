# Templates - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.09
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Section:** Standard templates
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Runtime Rule Template

```markdown
# <Rule Name>

> **Current Version:** X.Y
> **Design:** [design/<rule>.design.md](design/<rule>.design.md) vX.Y
> **Session:** <session-id> (<date>)
> **Full history:** [changelog/<rule>.changelog.md](changelog/<rule>.changelog.md)
```

## Design Parent Template

```markdown
# <Document Name>

## 0) Document Control

> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <session-id> (<date>)
> **Full history:** [../changelog/<chain>.changelog.md](../changelog/<chain>.changelog.md)
```

## Changelog Parent Template

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <session-id> (<date>)
```

## Broad-Chain Normalization Template

For broad active chains:

```text
design/<slug>.design.md
  -> compact active parent index

design/<slug>/
  -> active child target-state shards

changelog/<chain>.changelog.md
  -> compact active parent authority

changelog/<chain>/v*.changelog.md
  -> parent-indexed version detail shards
```

Use the same stem for parent file and child directory when normalized mode is selected.
