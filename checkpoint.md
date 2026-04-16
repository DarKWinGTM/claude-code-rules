# RULES Checkpoint

> **Created:** 2026-04-14
> **Last Updated:** 2026-04-16
> **Purpose:** continuation checkpoint for the current RULES repo state during the coordination fork split
> **Scope:** current RULES repo state + current split status between `claude-code-rules@darkwingtm` and `claude-session-coordination@darkwingtm`
> **Status:** handoff-ready reference artifact, not a new semantic authority layer

---

## 0) Short resume first

The active model is now the split model.

Current reality:
- `claude-code-rules@darkwingtm` = reduced Rules migration/reference package
- `claude-session-coordination@darkwingtm` = active compact + coordination runtime package
- root RULES = semantic authority for policy / semantics / governance

What is already done:
- the new coordination package exists under `TEMPLATE/PLUGIN/claude-session-coordination/`
- active compact hooks and active coordination hooks/scripts/skills have been cut over to the coordination package
- the reduced RULES package now keeps no active plugin hooks
- moved coordination scripts / skill docs / phase history from waves `044`–`054` now live under `TEMPLATE/PLUGIN/claude-session-coordination/` as package-owned history
- root RULES still keep semantic authority for shared execution coordination doctrine and the broader governance model

What is still open:
- final cleanup/verification of the split packet
- real shared-task-list runtime verification for the active `TaskCreated` validator inside `claude-session-coordination@darkwingtm`
- final git-packet audit before any git update/push

---

## 1) Current package roles

### Reduced Rules package
From the checked package files:
- package name = `claude-code-rules`
- package version = `1.8.6`
- package role = reduced Rules migration/reference package
- active plugin hooks = none

### Active coordination package
From the checked package files:
- package name = `claude-session-coordination`
- package version = `0.1.0`
- package role = active compact + coordination runtime package
- active plugin hooks = compact lifecycle hooks + bounded `TaskCreated` validator

---

## 2) What the next session must not lose

### A. Do not revive the older topology as current truth
Do not treat either:
- the old phase-042 split correction
- or the later phase-043 unified package model
as the current active topology.

Both are now historical context.
The active target is the current split model.

### B. Board vs truth boundary still holds
Keep treating:
- shared board = coordination / visible history
- phase / TODO / design / checked implementation state = semantic truth

### C. Optional tooling is still optional
Keep treating:
- memsearch = optional recall helper
- `claude-peers-mcp` = optional/future live signaling layer, not required semantic infrastructure

### D. Current remaining work is cleanup + verification
The open work is no longer broad topology design.
The remaining work is mainly:
- cleanup of split wording/history/package-local references
- verification of active runtime behavior
- git-packet shaping

---

## 3) Current status now

### Repo status
Current checked repo status is effectively:
- recent fork-cutover waves are documented and synchronized
- master changelog is at **v9.50**
- `phase/SUMMARY.md` includes rollout families through **058**
- `TODO.md` keeps the cleanup/verification follow-up items visible
- the repo-level docs now point at the active split model

### Coordination-model status
Current checked RULES position is:
- shared board = coordination layer
- semantic truth stays in phase/TODO/design/code
- memory = continuity support only
- memsearch = optional
- `claude-peers-mcp` = optional/future only

### Current operational open thread in this repo
The still-open repo-facing thread is:
- final cleanup/verification before git update readiness

This includes:
1. package-local reference cleanup in `claude-session-coordination`
2. RULES-side history/summary wording cleanup
3. runtime verification for the active shared-task validator
4. final git packet audit

---

## 4) Recommended continuation path for a new session

### Step 1 — re-anchor to current truth
Read these first:
1. `checkpoint.md`
2. `README.md`
3. `plugin/README.md`
4. `shared-execution-coordination.md`
5. `design/rules-plugin-extension.design.md`
6. `TODO.md`
7. `phase/SUMMARY.md`
8. `phase/phase-055-01-freeze-session-coordination-ownership-split.md`
9. `phase/phase-056-01-reduce-rules-plugin-active-scope.md`
10. `../PLUGIN/claude-session-coordination/README.md`

### Step 2 — preserve the active basis
Use this as the active basis:
- current intended model = reduced Rules package + active coordination runtime split
- current public install targets = `claude-code-rules@darkwingtm` and `claude-session-coordination@darkwingtm`
- current coordination stack = board first, truth surfaces second, optional tools later

### Step 3 — finish the remaining repo work in order
1. package-local cleanup in `TEMPLATE/PLUGIN/claude-session-coordination/`
2. RULES-side summary/history wording cleanup
3. shared-task validator verification under a real `CLAUDE_CODE_TASK_LIST_ID`
4. final git-packet audit

### Step 4 — do not push early
The user explicitly asked to avoid git update until the packet is actually ready.
So the next session should audit first, then report readiness, and only then move to git actions if requested again.

---

## 5) Checked file pointers for continuation

### RULES repo
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `phase/phase-055-01-freeze-session-coordination-ownership-split.md`
- `phase/phase-056-01-reduce-rules-plugin-active-scope.md`
- `design/rules-plugin-extension.design.md`
- `shared-execution-coordination.md`
- `plugin/README.md`
- `plugin/.claude-plugin/plugin.json`
- `plugin/.claude-plugin/marketplace.json`
- `plugin/hooks/hooks.json`
- `changelog/changelog.md`

### Coordination package
- `../PLUGIN/claude-session-coordination/README.md`
- `../PLUGIN/claude-session-coordination/hooks/hooks.json`
- `../PLUGIN/claude-session-coordination/scripts/shared-task-hook-probe.sh`
- `../PLUGIN/claude-session-coordination/skills/session-coordination-bridge/SKILL.md`
- `../PLUGIN/claude-session-coordination/phase/SUMMARY.md`
- `../PLUGIN/claude-session-coordination/TODO.md`

---

## 6) Final handoff sentence

> The active target is now the split package model where `claude-code-rules@darkwingtm` is reduced and `claude-session-coordination@darkwingtm` owns the plugin runtime; continue from cleanup/runtime-verification/git-packet audit work, not by reopening the older unified-plugin topology as if it were still current.
