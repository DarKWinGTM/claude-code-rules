# RULES Plugin Extension History

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.31
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd (2026-04-17)

---

## 1) Goal

Preserve the historical design context for the former RULES plugin-extension line after active plugin/package ownership moved out of RULES and the local `RULES/plugin` shell was removed.

---

## 2) Current model

The active model is now:
- root RULES = generic communication/evidence/governance rules plus global task-list doctrine
- shared-board-specific coordination semantics stay outside Main RULES active doctrine
- no active `plugin/` package remains under `TEMPLATE/RULES/`

พูดง่าย ๆ:
- RULES = semantic/generic doctrine
- externalized coordination layer = not part of Main RULES current doctrine
- this design file = historical record only

---

## 3) Boundary

### 3.1 What this historical chain is

This chain now exists to:
- preserve design history for the former RULES plugin-extension line
- keep old phase/patch/changelog records interpretable without pretending that the old package surface still exists
- document the retirement boundary clearly enough that old plugin-topology waves are not mistaken for the current state

### 3.2 What this historical chain is not

It is **not** meant to:
- describe a current install surface under RULES
- describe an active plugin shell under `TEMPLATE/RULES/`
- claim active compact lifecycle hook ownership
- claim active shared-task coordination runtime ownership
- act like a second semantic authority stack

---

## 4) Retained historical surface

The retained historical surface is now:
- this design file = historical boundary for the former plugin-extension line
- `changelog/rules-plugin-extension.changelog.md` = historical chain history
- related `phase/phase-017*` through `phase/phase-058*` records = rollout history
- related `patch/*plugin*` and compact/tmux bridge patch artifacts = review/change history

Active coordination/package ownership is externalized and does not remain part of Main RULES current doctrine.

---

## 5) Verification targets

This historical-boundary design is successful when:
- root RULES docs no longer point readers to an active `RULES/plugin` shell
- active coordination runtime/package ownership is not described as part of Main RULES current doctrine
- old plugin-extension phases remain readable as history without being taught as current install/runtime topology
- the removal of the local RULES plugin shell is explicit enough that later readers do not expect `plugin/README.md`, package metadata, hooks, or scripts to still exist here

---

## 6) Integration

Related documents:
- `design/design.md`
- former coordination-chain history only
- `README.md`
- `phase/SUMMARY.md`
- historical root README / phase / patch records only, without turning external ownership into Main RULES active doctrine

---

> Full history: [../changelog/rules-plugin-extension.changelog.md](../changelog/rules-plugin-extension.changelog.md)
