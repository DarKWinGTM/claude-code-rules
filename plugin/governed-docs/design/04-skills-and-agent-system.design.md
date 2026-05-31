# Skills and Agent System

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the operator-facing skills and the custom agent set for the governed-docs companion.

## 2) User-facing command contract

Every user-facing skill should require one explicit target workspace path argument.

Base rule:
- the command must name the project/workspace root it wants to inspect or maintain
- the plugin must not silently fall back to ambient cwd
- omission of the target path is a hard stop, not a warning-only condition

Why:
- one session may operate around several neighboring repos or governed trees
- the same document family names may exist in more than one project
- the maintenance companion must not guess where to act

Example operator shape:
- `/governed-docs:scan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
- `/governed-docs:phase-audit /home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
- `/governed-docs:review /home/node/workplace/AWCLOUD/TEMPLATE/RULES/`

## 3) Skill set

### `/governed-docs:scan`

Purpose:
- inspect current governed state
- surface inventory, anomalies, severity, and likely next step

Typical use:
- early maintenance check on an explicitly named workspace path
- broad governed-doc inspection for one explicitly named governed tree
- current-state sanity scan without relying on ambient cwd

### `/governed-docs:review`

Purpose:
- perform a consistency-sensitive governed-doc review before closeout, release, or no-drift claims

Typical use:
- after a broad doc sync wave
- before release wording is treated as ready
- before stronger completion claims

### `/governed-docs:repair-plan`

Purpose:
- turn findings into a repair package with exact scope, preservation notes, and approval boundary

Typical use:
- when drift is known but mutation is not yet approved
- when repair spans several governed surfaces

### `/governed-docs:normalize`

Purpose:
- apply bounded deterministic normalization where the action policy allows it

Typical use:
- backlink/shard-map synchronization
- safe pointer insertion
- compact formatting normalization
- release wording refresh from already-verified evidence

### `/governed-docs:phase-audit`

Purpose:
- focus specifically on phase filename grammar, lineage pressure, and malformed numbering patterns

Typical use:
- when phase numbering looks irregular
- when legacy-only vs forward-valid phase forms need review
- when current-phase / child-phase / new-major fit is under question

### `/governed-docs:release-gate`

Purpose:
- produce a release/closeout gate decision for the governed-document layer

Typical use:
- before claiming release-ready
- before closing a broad governed sync wave
- after install/parity/proof evidence is gathered

### `/governed-docs:present-md`

Purpose:
- render one governed-docs-owned Markdown/doc source into one page inside the root `preview/` portal structure

Typical use:
- preview one governed document as an article-style page
- verify the governed-docs-owned presentation contract without borrowing NodeClaw ownership
- update one bounded page under `preview/**` from one explicit target workspace path plus one explicit source path

### `/governed-docs:present-sync`

Purpose:
- rebuild and resync the full root `preview/` portal across governed source families

Typical use:
- after design / changelog / TODO / phase / patch updates
- when the preview portal needs a fresh index + manifest + family page rebuild
- when stale preview pages should be pruned from `preview/**`

## 4) Custom agent set

### `governed-docs-scout`
- read-only
- collects inventories, structure state, phase filename evidence, and drift candidates

### `governed-docs-doctrine-evaluator`
- read-only
- compares scout findings against RULES doctrine and classifies them

### `governed-docs-repair-architect`
- read-only planning role
- chooses the safest repair path and owning surface

### `governed-docs-normalizer`
- edit-capable but bounded
- performs only deterministic low-risk normalization once approved by policy

### `governed-docs-release-auditor`
- read-only
- audits release/closeout wording, proof alignment, and cross-surface current-state agreement

### `governed-docs-phase-lineage-auditor`
- specialized read-only lane
- focuses on phase numbering, lineage fit, legacy-only forms, and malformed grammar cases

### `governed-docs-present-inventory-scout`
- read-only
- discovers eligible preview-source docs and classifies them by family

### `governed-docs-present-architect`
- read-only planning role
- shapes portal IA, family grouping, and preview shell structure

### `governed-docs-present-renderer`
- bounded presentation helper
- focuses on page-shell readability and family page consistency inside `preview/**`

### `governed-docs-present-sync-auditor`
- read-only audit lane
- verifies source ↔ preview parity, stale-page pruning, and bounded mutation to `preview/**`

## 4) Why split skills and agents this way

The split keeps operator intent separate from execution roles:
- skills define user-facing entry surfaces and common workflows
- agents define specialist responsibilities for bounded slices

This matches the strongest reusable patterns already present in the ecosystem:
- reviewer / auditor / sweeper separation from `supervisor-audit-agent-system`
- evidence/provenance-sensitive analysis from `memory-context-intelligence`

## 5) Non-goals for the agent system

The agent system must not imply that:
- findings are automatically proof
- repair architect output is semantic authority
- a normalizer can rewrite any governed file once it sees drift
- a phase-lineage finding alone authorizes a rename or lineage rewrite

---

> Agent rule: split by responsibility, not by decorative role naming. Each agent should answer one clear question that the main session can verify.
