# Governed Surface Inventory

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define which surfaces the plugin must understand, which surfaces it may inspect directly, and which surfaces provide doctrine inputs rather than maintenance targets.

All inventory work starts from one explicit workspace root supplied by the operator. The plugin should build its inventory relative to that path rather than guessing from ambient cwd.

## 2) Doctrine input surfaces

These are not the plugin's maintenance outputs. They are the sources it must read to understand what compliant state means.

Primary doctrine inputs:
- `document-governance.md`
- `document-integrity.md`
- `phase-todo-artifact.md`
- `authority-and-scope.md`
- `evidence-discipline.md`
- `accurate-communication.md`
- related design companions and active changelog parents where needed

Purpose:
- parent/shard/changelog model
- active-entrypoint rules
- phase identity and lineage behavior
- rollover / preservation doctrine
- evidence-strength wording and closeout gating

## 3) Governed maintenance target surfaces

These are the main target families the plugin should inspect and support.

### README surface
- `README.md`
- current-state and onboarding wording
- release/current-version alignment checks
- front-page vs changelog/phase drift

### Design surface
- `design/*.design.md`
- `design/<slug>/*.design.md`
- parent/shard shape
- shard map reachability
- target-state vs history pollution

### Changelog surface
- `changelog/*.changelog.md`
- `changelog/<chain>/v*.changelog.md`
- `changelog/done/*.changelog.md`
- parent authority, version alignment, detail-shard navigation, and fallback-history boundary

### TODO surface
- `TODO.md`
- `todo/history/**`
- `todo/done/**`
- active index vs historical spillover
- rollover pressure and pending-only discipline

### Phase surface
- `phase/SUMMARY.md`
- `phase/phase-*.md`
- `phase/history/**`
- `phase/done/**`
- phase grammar, lineage fit, roadmap alignment, and active-entrypoint compactness

### Patch surface
- `patch/*.patch.md`
- `patch/done/**`
- before/after review shape
- patch-vs-phase boundary
- metadata alignment

## 4) Contextual evidence surfaces

The plugin may need these for stronger judgments, but they are not the main governed targets.

Examples:
- checked git branch/ref state
- install manifest or runtime parity outputs
- release/tag metadata
- generated review artifacts from the plugin itself

These support a decision. They do not override doctrine inputs.

## 5) Inventory classes the scanner should emit

The scanner should classify results into inventory classes such as:
- active authority surface
- active child shard
- active version-detail shard
- inactive history/done surface
- doctrine input surface
- contextual evidence surface
- out-of-scope neighbor surface

## 6) Out-of-scope surfaces for v1

V1 should not try to maintain everything near RULES.

Out of scope by default:
- implementation code not acting as governed documentation
- plugin runtime internals of unrelated capsules
- user-global runtime destinations outside the checked maintenance goal
- arbitrary co-located files whose meaning is unresolved
- external repos that merely resemble the RULES governance model

---

> Inventory principle: the plugin should know which files matter, why they matter, and which doctrine owner decides their meaning before it proposes any maintenance action.
