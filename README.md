<a id="top"></a>
<div align="center">

<!-- Hero Banner -->
<img src="img/repo-banner.png" alt="Claude Code Rules" width="800">

<!-- Hero Title -->
<h1>
  🏛️
  Claude Code Rules & Framework
  🏛️
</h1>

<p>
  <i>Your Claude Code AI assistant, elevated to professional standards</i>
</p>

<!-- Current State Cards -->
<table>
<tr>
<td align="center" width="200">
  <b>v10.40</b><br><sub>P132 Released</sub>
</td>
<td align="center" width="200">
  <b>18</b><br><sub>Active Runtime Rules</sub>
</td>
<td align="center" width="200">
  <b>Released</b><br><sub>Verified and published</sub>
</td>
<td align="center" width="200">
  <b>Companion Plugins</b><br><sub>Discoverable plugin docs</sub>
</td>
</tr>
</table>

> **Current release note:** `v10.40 / P132` makes the two companion plugins easier to discover and use: `governed-docs` and `memory-context-intelligence` now have richer plugin READMEs with plugin-local image assets, and the root README now introduces both plugins clearly while preserving the boundary that they install separately from the active runtime rule payload.

<!-- CTA Buttons -->
<p>
  <a href="#-quick-start">
    <img src="https://img.shields.io/badge/⚡_Quick_Start-5_seconds-brightgreen?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCI+PHBhdGggZmlsbD0iIzI1RTEyNiIgZD0iTTEzIDJoLTh2MmMwIC4zNS4wNy42OS4xOCAxLjAzLjM1IDEuMDguOTkgMS44MyAxLjgzLjk5LjM0LjM1LjY5LjQyIDEuMDMuMTIuNDkuMDUuOTguMjIgMS40Ni40OWwtMS44My0uMzVjLS4zNS0uMDctLjY5LS4xNC0xLjAzLS4xOC0uMzUtLjA1LS42OS0uMTItMS4wMy0uMzUtMS4wOC0uOTktMS44My0xLjgzLS45OS0uMzQtLjM1LS42OS0uNDItMS4wMy0uMTItLjQ5LS4wNS0uOTgtLjIyLTEuNDYtLjQ5bDEuODMuMzV6Ii8+PC9zdmc+">
  </a>
  <a href="#-rule-files">
    <img src="https://img.shields.io/badge/📁_Rules-Policies-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0Y5NzgxNiIgZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyszQuNDggMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bS0yIDE1bC01IDUgNS01IDUtNS01IDV6Ii8+PC9zdmc+">
  </a>
  <a href="#-installation">
    <img src="https://img.shields.io/badge/📦_Install-Copy_&_Paste-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iIzI1ODFGNiIgZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEydjJMMTQgN2g0bDItMnYtMmgybC0yIDJoLTRsLTItMnYtMmgybC0yIDJ2MmgybDItMnYtMmgybC0yIDJoLTRMNCAydjJ6Ii8+PC9zdmc+">
  </a>
</p>

---

</div>

## 📑 Table of Contents

- [⚡ Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📁 Rule Files](#-rule-files)
- [📦 Installation](#-installation)
- [🔌 Companion Plugins](#-companion-plugins)
- [📂 Design Documentation Structure](#-design-documentation-structure)
- [🧪 Playground](#-playground)
- [🔗 Integration Guide](#-integration-guide)
- [🎓 Framework Highlights](#-framework-highlights)
- [🖼️ Visual Guide](#️-visual-guide)
- [📊 Before & After](#-before--after)
- [📊 Current Quality Signals](#-current-quality-signals)
- [🔒 Safety Commitments](#-safety-commitments)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## ⚡ Quick Start

Use the launcher for your platform. The primary install target is the current project's `.claude/rules/` directory. The launcher is the operator entrypoint; the helper scripts remain the execution layer underneath and keep the current compact 18-rule runtime set with owner-aware manifest cleanup inside that project-local destination.

### Bash — Linux / macOS

Clone-first install into a target project:

```bash
git clone https://github.com/DarKWinGTM/claude-code-rules.git
cd claude-code-rules || exit 1
./script/launcher.sh --project-root "/path/to/project"
```

If you are already inside the target project and cloned RULES beside it:

```bash
../claude-code-rules/script/launcher.sh --project-root "$PWD"
```

Manual/helper path from a local clone:

```bash
./script/setup-claude-code-rules.sh --project-root "/path/to/project"
```

### PowerShell — Windows

Clone-first install into a target project:

```powershell
git clone https://github.com/DarKWinGTM/claude-code-rules.git
Set-Location claude-code-rules
.\script\launcher.ps1 -ProjectRoot "C:\path\to\project"
```

If you are already inside the target project and cloned RULES beside it:

```powershell
..\claude-code-rules\script\launcher.ps1 -ProjectRoot (Get-Location).Path
```

Manual/helper path from a local clone:

```powershell
.\script\setup-claude-code-rules.ps1 -ProjectRoot "C:\path\to\project"
```

### Notes

- The primary install target is `<project-root>/.claude/rules/`.
- The launcher is the primary operator path; helper scripts stay available as the execution layer and manual path.
- If you run the launcher from the RULES repo root, pass `--project-root` / `-ProjectRoot` explicitly.
- This wave supports Claude Code only. Codex CLI and Gemini CLI are not supported for this install surface in current scope.
- This runtime-only install copies active rule files only.
- Cleanup is owner-aware, not wildcard-by-filename.
- Manifest cleanup removes only files previously installed by this repo and still matching the last recorded install snapshot inside the same project-local target.
- Legacy cleanup checks old candidate filenames against this repo's git history; only exact historical blob matches are quarantined out of the active project-local runtime path.
- Files already present in the target `.claude/rules/` directory but outside this repo's recorded install ownership or repo-history proof are preserved by default.
- Governed design/changelog/TODO/phase/patch artifacts, inactive history/done surfaces, and `phase-implementation-template.md` remain in the repository for maintenance and synchronized updates.

### 🤖 AI-Assisted Install Prompt

If you want Claude Code to install this repo for you into the current project's `.claude/rules/` target, use this prompt:

```text
Install this rules repo for me from:
https://github.com/DarKWinGTM/claude-code-rules

Requirements:
- clone the repo first
- run the launcher script from the cloned repo, not a raw helper fetch as the default path
- install only the active runtime rule set into the current project's .claude/rules/
- use manifest-owned cleanup only inside that same project-local target
- do not delete unrelated co-located rules in that project-local .claude/rules/ directory
- do not install files from suspend/, support/, plugin/, design/, changelog/, phase/, patch/, or TODO.md
- verify the installed files after copying
- report exactly what was installed
```

Codex CLI and Gemini CLI are not supported for this install surface in the current wave.

---

## ✨ Features

### 🎯 Core Capabilities

These capabilities summarize the current operating model at the front-page level. They are grounded in active doctrine and current-state behavior, not in phase-by-phase execution history.

- **Evidence-First Accuracy** — Evidence-grounded reasoning is the current baseline for material claims.
  - Seek practical proof before substantial reasoning when the question depends on current facts
  - Keep verified fact, inference, hypothesis, and scoped non-finding separate
  - Use evidence as grounding rather than an automatic decision lock
  - Avoid guessing local paths, values, symbols, or config

- **Anti-Sycophancy** — User direction is respected without turning agreement into false proof.
  - Evaluate proposals before agreement-shaped wording
  - Keep safe user-selected direction separate from factual or quality endorsement
  - Use checked evidence for material agreement, recommendation, and challenge
  - Prefer claim-focused corrections and constructive dissent when fit or proof conflicts

- **Security First** — Safety and action boundaries remain first-pass concerns.
  - Prefer real systems over simulated success when implementation truth matters
  - Avoid mock implementations by default unless the scope explicitly calls for them
  - Verify configurations before making strong runtime or readiness claims
  - Require intent clarity before destructive or high-impact actions

- **Runtime Context Discipline** — The runtime layer stays compact, body-sufficient, and limited to doctrine the assistant must apply now.
  - Keep the 18 active runtime rules focused on live behavioral guidance rather than historical rollout detail
  - Keep design as target-state authority, changelog as version/history authority, and TODO/phase as execution surfaces
  - Verify install scope, parity, and body sufficiency before claiming runtime synchronization
  - Preserve the project-local `.claude/rules/` install contract while keeping non-runtime governance artifacts out of the runtime payload

---

## 📁 Rule Files

<div align="center">

### 🔴 Core Chains (4 rules)

> **Foundational decision, safety, evidence, and refusal behavior**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`authority-and-scope.md`](authority-and-scope.md) | Decision hierarchy | Deterministic precedence for user direction, hard boundaries, governed repo authority, and advisory future work |
| [`evidence-discipline.md`](evidence-discipline.md) | Evidence discipline | Verify-first factual reasoning, scoped lookup discipline, proof-aware uncertainty, and real-over-mock behavior |
| [`refusal-and-recovery.md`](refusal-and-recovery.md) | Refusal and recovery chain | Normalized intent classification plus recoverable blocked-path responses |
| [`action-safety.md`](action-safety.md) | Action safety | Intent verification, destructive confirmation, topology discipline, emergency posture, and retry boundaries |

---

### 🟡 Communication & Explanation (4 rules)

> **How answers should read, explain, and disclose**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`accurate-communication.md`](accurate-communication.md) | Evidence-honest wording | Keeps claims, status, progress, and scope wording aligned to checked evidence |
| [`communication-register.md`](communication-register.md) | Tone and agreement calibration | Natural professional register, high-signal trimming, and evidence-calibrated disagreement |
| [`explanation-and-presentation.md`](explanation-and-presentation.md) | Explanation, layout, and closing shape | Plain-language-first explanation, readable structure, clean text diagrams, and concise action framing |
| [`audience-surface-disclosure-control.md`](audience-surface-disclosure-control.md) | Audience-aware disclosure | Full direct-user transparency while keeping public/operator surfaces appropriately scoped |

---

### 🔵 Execution & Coordination (4 rules)

> **How governed work is started, tracked, phased, and routed**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`coding-discipline.md`](coding-discipline.md) | Coding execution discipline | Maintainable structure, proportionate verification, and tactical-to-strategic convergence |
| [`execution-and-goal-frame.md`](execution-and-goal-frame.md) | Execution continuity and goal framing | Keeps work moving from active surfaces with clear goal/output/gate reasoning |
| [`worker-routing-and-context.md`](worker-routing-and-context.md) | Worker routing and context control | Uses the smallest effective worker lane and protects leader context from raw overload |
| [`phase-todo-artifact.md`](phase-todo-artifact.md) | Artifact initiation, phase, and TODO doctrine | Resolves startup posture early, governs live `/phase`, and keeps TODO vs live task roles distinct |

---

### 🟢 Governance & Runtime Context (6 rules)

> **How documentation, installs, I/O, memory, portability, and external checking stay coherent**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`document-governance.md`](document-governance.md) | Document governance baseline | One deterministic authority model for README, design, changelog, patch, completed history, and UDVC-1 |
| [`document-integrity.md`](document-integrity.md) | Document integrity | Cross-reference consistency, rollover boundaries, and no-drift / no-delete-by-hygiene discipline |
| [`safe-io.md`](safe-io.md) | Safe file and terminal I/O | Bounded reading/output, parent-index-first reads, and rollover signals for oversized entrypoints |
| [`external-verification-and-source-trust.md`](external-verification-and-source-trust.md) | External source trust | Proactive web-backed verification, source ranking, and conflict-aware evidence grounding |
| [`memory-governance-and-session-boundary.md`](memory-governance-and-session-boundary.md) | Memory governance | Keeps memory scoped, compact, path-aware, and subordinate to checked current evidence |
| [`portable-implementation-and-hardcoding-control.md`](portable-implementation-and-hardcoding-control.md) | Portability defaults | Prevents machine-local assumptions from becoming shared contracts |

**📊 Active Runtime Rules: 18**

Current source state:
- P127 / v10.35 refines the README front-page capability presentation on top of the released `v10.34 / P126` baseline.
- Core Capabilities now explain active doctrine and current-state behavior in a readable list instead of a grid with phase-heavy runtime-history narration.
- Runtime Context Discipline now stays front-page scoped: current runtime shape, authority boundaries, and install-discipline expectations are summarized without turning README into a phase summary.
- The governed `playground/` family remains non-runtime and outside the installer payload.
- The active runtime install set remains 18 root rules and `playground/` stays outside the installer payload.
- The untracked `plugin/` tree remains preserved and out of staged wave scope.
</div>

---

## 📦 Installation

The Quick Start block above is the canonical launcher-first install path. The methods below keep the same compact 18-rule runtime set while making project-local `.claude/rules/` the default target.

### 🎯 Method 1: Full Project-Local Installation (Recommended)

**Use this when:** you want the full active runtime set inside the current project.

Fastest path:
1. Clone the RULES repo.
2. Run the launcher for your platform from that clone.
3. Point it at the target project root.
4. Run the verification commands below.

If you already cloned the repo earlier, you do **not** need to repeat the clone step. Return to the repo root and rerun the launcher locally against the project you want to govern.

### 🎯 Method 2: Pick One Rule (Project-Local)

**Use this when:** you only want a small subset of the runtime rules in one project.

```bash
mkdir -p ./.claude/rules
curl -o ./.claude/rules/evidence-discipline.md \
  https://raw.githubusercontent.com/DarKWinGTM/claude-code-rules/master/evidence-discipline.md
```

### 🎯 Method 3: Optional Global Fallback

**Use this when:** you intentionally want the same launcher-driven install model under your home directory.

- Use the same cloned repo.
- Run the launcher scripts.
- Set `--project-root "$HOME"` for Bash or `-ProjectRoot $HOME` for PowerShell.
- Treat this as an explicit fallback, not the primary recommendation for this wave.

> Source-side note: public commands in this README are expressed from the repo root.
> Destination/runtime note: the primary target in this wave is `<project-root>/.claude/rules/`; global install is only the same launcher/helper model pointed at `$HOME` intentionally.

### 📍 Installation Paths

| Location | Scope | Path | Use Case |
|----------|-------|------|----------|
| **Project** | Current project only | `<project-root>/.claude/rules/*.md` | Default recommendation |
| **Global fallback** | All projects | `$HOME/.claude/rules/*.md` | Explicit opt-in only |

### ✅ Verify Installation

> Recommended: verify under the current project's `.claude/rules/` target.
> Optional global fallback: verify under `$HOME/.claude/rules/` only if you intentionally used that target.

```bash
# Project-local install check (run from project root)
claude --version
head -20 ./.claude/rules/evidence-discipline.md
ls ./.claude/rules/action-safety.md
ls ./.claude/rules/phase-todo-artifact.md
ls ./.claude/rules/document-governance.md
ls ./.claude/rules/worker-routing-and-context.md

# Optional global fallback check
head -20 "$HOME/.claude/rules/evidence-discipline.md"
ls "$HOME/.claude/rules/action-safety.md"
ls "$HOME/.claude/rules/phase-todo-artifact.md"
ls "$HOME/.claude/rules/document-governance.md"
ls "$HOME/.claude/rules/worker-routing-and-context.md"
```

---

## 🔌 Companion Plugins

This repo also carries local marketplace plugins that sit **beside** the 18 active runtime rules.

พูดง่าย ๆ คือ runtime rules ยังเป็นแกนหลักของพฤติกรรม Claude Code ใน `.claude/rules/` ส่วน plugin พวกนี้เป็นเครื่องมือเสริมที่ช่วยงานเฉพาะด้านและติดตั้งแยกจาก `plugin/` ตามความต้องการ

Current companion plugins worth knowing:

- **`governed-docs`** — maintenance companion for governed document families
  - scans repo-governed docs against RULES doctrine
  - generates repair-plan / release-gate style review output
  - provides an index-backed preview flow for governed document navigation
  - README: [`plugin/governed-docs/README.md`](plugin/governed-docs/README.md)

- **`memory-context-intelligence`** — evidence-first workflow reflection companion
  - reads bounded historical work evidence and surfaces candidate workflow / RULES improvement topics
  - keeps `trace_evidence` as the live anchor while still using memory/governance context carefully
  - provides a guided init flow plus the analysis surface for historical-first review
  - README: [`plugin/memory-context-intelligence/README.md`](plugin/memory-context-intelligence/README.md)

Boundary:
- these plugins are **not** part of the active 18-rule runtime payload copied into `.claude/rules/`
- they are companion tools you install separately from the local plugin marketplace under `plugin/`

---

## 📂 Design Documentation Structure

| Location | Purpose | File Type |
|----------|---------|-----------|
| `./design/<slug>.design.md` | Compact active parent design index/gateway for governed chains | Active design parent |
| `./design/<slug>/*.design.md` | Active child target-state shards in same-stem nested mode | Active design shards |
| `./design/*.design.md` beside a compact parent | Flat sibling design shards when the current folder already scopes the chain | Active design sibling shards |
| `./diagram/STRUCTURE.md` | Bodyful whole-project detailed visual structure authority when a governed diagram lane is opened | Active diagram global anchor |
| `./diagram/<subject>.design.md` | Default integrated Kroki-compatible subject diagram as a zoom-in / decomposition view of the global structure | Active subject diagram |
| `./diagram/<subject>/*.design.md` | Kroki-compatible child visual shards only after a real visual split trigger | Active diagram child shards |
| `*.md` (root) | Active runtime rules | Rules files |
| `./changelog/changelog.md` | Compact master repository-wide current-version authority and shard map | Master changelog parent |
| `./changelog/*.changelog.md` | Per-chain authoritative active parent history/current version state | Active parent changelogs |
| `./changelog/<chain>/v*.changelog.md` | Same-chain detailed version entries in same-stem nested mode | Version detail shards |
| `./changelog/v*.changelog.md` beside a compact parent | Flat sibling version-detail shards when the current folder already scopes the chain | Version detail sibling shards |
| `./changelog/done/*.changelog.md` | Legacy/archive/fallback detailed history outside active scans | Inactive history for audit/rollback/provenance/trace |
| `./todo/history/*.md` | Daily TODO movement and pre-rollover snapshots outside the active TODO entrypoint | Referenced inactive TODO history |
| `./todo/done/*.md` | Large completed TODO/task detail outside the active TODO entrypoint | Referenced inactive TODO detail |
| `./phase/SUMMARY.md` | Compact governed summary/index for live phase planning and current roadmap state | Phase summary doc |
| `./phase/history/*.md` | Daily phase movement and pre-rollover phase-summary snapshots outside the active summary | Referenced inactive phase history |
| `./phase/phase-NNN-<phase-name>.md` | Governed active major-phase execution detail | Active major phase docs |
| `./phase/phase-NNN-NN-<subphase-name>.md` | Governed active subphase execution detail | Active subphase docs |
| `./phase/phase-NNN-NN-NN-<child-phase-name>.md` | Governed active nested child-phase execution detail inside one bounded parent family | Active nested child phase docs |
| `./phase/done/phase-NNN-*.md` | Completed phase detail retained outside active scans | Inactive completed phase history |
| `./patch/<context>.patch.md` or `./<context>.patch.md` | Governed active patch/review artifacts outside live phase planning | Active patch docs |
| `./patch/done/<context>.patch.md` | Completed patch artifacts retained outside active scans | Inactive completed patch history |
| `./phase-implementation-template.md` | Root helper for phased planning | Helper artifact that also exposes active phase family, planned next phase(s), activation boundary, and next checkpoint guidance for future `/phase` authoring |
| `./playground/README.md` | Compact entrypoint for governed behavior playground material | Playground family index |
| `./playground/cases/*.md`, `./playground/coverage.md`, `./playground/matrix.md` | Scenario families, rule coverage mapping, and virtual-case exploration outside runtime install scope | Governed non-runtime playground content |

> **💡 Single Source of Truth Principle:**
> - Governed design/changelog chains should classify chain shape before parent files absorb more detail
> - `diagram/STRUCTURE.md` is the bodyful top-level whole-project detailed visual structure authority when a governed diagram lane is opened
> - governed `diagram/` source is mandatory Kroki-compatible and supports all formats that are both Kroki-compatible and governance-suitable
> - `diagram/<subject>.design.md` is the default bodyful integrated subject diagram as a zoom-in / decomposition view of the global structure; split only when visual complexity or genuinely different visual questions justify it
> - Diagram structure must not auto-mirror design shards, inline answer/phase-local text diagrams do not become governed source truth automatically, and `design/` remains semantic authority when text and diagram differ
> - Flat sibling shards are valid when the current folder already scopes the chain and the compact parent clearly exposes the shard map
> - Broad active design chains should still strongly prefer same-stem parent/index + shard pairs (`design/<slug>.design.md` + `design/<slug>/`) and do not use a default `design/done/` surface
> - Per-chain active changelogs (`*.changelog.md`) remain the authority for current governed chain history/version state
> - Broad active changelog chains should still strongly prefer same-stem parent/index + shard pairs (`changelog/<chain>.changelog.md` + `changelog/<chain>/`)
> - Chain-scoped version detail shards hold indexed same-chain detail without becoming separate version authority, whether they appear in flat sibling mode or same-stem nested mode
> - `todo/history/`, `todo/done/`, `phase/history/`, `phase/done/`, `patch/done/`, and `changelog/done/` are inactive-by-default referenced history/detail surfaces for audit, rollback, provenance, or trace reconstruction
> - `changelog/changelog.md` records repository-level synchronization history
> - `README.md` remains overview-only, not chain authority
> - `TODO.md` and `phase/SUMMARY.md` stay compact current-state entrypoints; moved history remains reachable through their `history/` and `done/` references
> - Older coordination-flavored rollout records in `TODO.md`, `phase/SUMMARY.md`, and `changelog/changelog.md` remain historical context only; current active authority stays in the active runtime rules and design docs

---

## 🧪 Playground

For governed behavior scenarios, coverage mapping, and virtual-case exploration, start at [`./playground/README.md`](playground/README.md).

Boundary:
- `playground/` is a governed non-runtime family
- it is not part of the 18-file `.claude/rules/` install payload
- README stays pointer-level; detailed cases live under `playground/`

---

## 🔗 Integration Guide

This section defines how `design`, `diagram`, `changelog`, `runtime rules`, `TODO`, and governed phase-planning artifacts should be updated together.

### Document Roles

| Document | Role | Update Trigger |
|----------|------|----------------|
| `design/*.design.md` | Target behavior/specification | Requirement or policy change |
| `diagram/STRUCTURE.md` and `diagram/*.design.md` | Governed Kroki-compatible visual synthesis / relationship explanation | A whole-repo or subject-level visual explanation needs active source truth |
| `*.md` (root runtime rules) | Active runtime behavior | Approved design change requires runtime sync |
| `changelog/changelog.md` | Master repository-wide synchronization history | Repository-level governed sync events |
| `changelog/*.changelog.md` | Authoritative active per-chain version history | Any rule/design update with version impact |
| `changelog/done/*.changelog.md` | Inactive completed or older detailed history | History/audit/rollback/provenance/trace needs only |
| `todo/history/*.md` | Referenced inactive TODO history | Daily movement, pre-rollover snapshots, and audit trail when active `TODO.md` is compacted |
| `todo/done/*.md` | Referenced inactive TODO detail | Large completed task/wave detail retained outside the active TODO entrypoint |
| `phase/SUMMARY.md` | Compact governed summary/index for live phased execution | Current phase roadmap/index and links to referenced history/done shards |
| `phase/history/*.md` | Referenced inactive phase history | Daily phase movement and pre-rollover summary snapshots when active `phase/SUMMARY.md` is compacted |
| `phase/phase-NNN-<phase-name>.md`, `phase/phase-NNN-NN-<subphase-name>.md`, and `phase/phase-NNN-NN-NN-<child-phase-name>.md` | Governed active phase-detail layer | Multi-stage execution detail under `/phase`, including design references, optional patch references, design extraction, optional patch extraction, review flow, reviewer checklist, review outcome, and execution detail |
| `phase/done/phase-NNN-*.md` | Inactive completed phase history | Completed phase detail should leave active scans but remain traceable |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Governed active patch/review artifact layer | Patch or review work that is separate from live phase planning but may feed the phase layer one-way when relevant |
| `patch/done/<context>.patch.md` | Inactive completed patch history | Completed patch artifacts should leave active review scans but remain traceable |
| `phase-implementation-template.md` | Root helper for phased planning readability | Reusable authoring support when staged execution matters, including active phase family, planned next phase(s), activation boundary, and next checkpoint guidance |
| `TODO.md` | Execution and progress tracking | Work starts/completes or task state changes |

### Startup Artifact Gate

Before meaningful governed work drifts, the repository now expects startup artifact posture to be resolved through `phase-todo-artifact.md`.

That means design / changelog / TODO / phase / patch should be explicitly resolved as:
- use existing
- create now
- ask now
- not required

Required governed companions should stay visible when the checked work shape still requires them; the live task list helps run the work, but it does not replace required design/changelog/TODO/phase/patch surfaces.

When governed design is sufficiently clear and staged execution is warranted, phase posture should resolve to `use existing` or `create now`; the phase layer may derive execution order, current child phase files, and current-phase live tasks from that governed design instead of waiting for a separate retrospective planning prompt. If phase posture resolves to `create now`, identity still goes through `phase-todo-artifact.md` so the outcome may be current-phase update, existing-family subphase, new major phase, or ask-now lineage handling.

For greenfield startup / baseline formation, patch should normally resolve to `not required` unless a real existing before/after review surface or explicit user request justifies patch packaging.

Once startup posture is settled and the active path is clear, execution should keep moving without re-pausing over the same gate.

When phased work also uses governed patch artifacts, the live phase workspace should now declare that linkage explicitly in `phase/SUMMARY.md` and the relevant child phase files.

### Completed Documentation Surfaces

Use inactive `done/` surfaces to reduce active scan bloat without deleting governed history:
- `phase/done/` for completed phase execution detail
- `patch/done/` for completed patch/review artifacts
- `changelog/done/` for older or completed detailed history

Do not create a default `design/done/` pattern. Design remains the active blueprint and target-state authority.

Open `done/` surfaces only when history, audit, rollback, provenance, or trace reconstruction is needed. Files in `done/` are not junk and completed status is not deletion authorization.

### Recommended Update Flow

```text
Change request received
  → resolve startup artifact posture first when the work is meaningfully governed
  → if staged work is warranted, synthesize phase posture/order/tasks from clear governed design
  → before opening a new major phase, apply phase lineage selection: current phase, existing-family subphase, new major, or ask-now
  → update design target state
  → synchronize runtime rule wording
  → record per-chain changelog version + summary
  → record repository-level sync in changelog/changelog.md when applicable
  → update TODO pending/completed/history
  → update phase/patch companion records when in scope
  → roll oversized active TODO or phase-summary history into referenced daily-first `history/` and `done/` shards before broad active-file absorption continues
  → move completed phase/patch/changelog detail to `done/` only when active scan bloat justifies inactive history separation
  → install only the 18 source-owned active runtime rules when an install gate is explicitly in scope
  → verify links, versions, active install scope, source/runtime parity, and active runtime body sufficiency only when a runtime install gate is in scope
```


### Verification Checklist

- Design file links to the correct changelog file
- Changelog unified row maps to an existing detailed section
- Runtime rule version/header aligns with changelog current version
- README active runtime install list still contains exactly the 18 source-owned root rule files
- `TODO.md` and `phase/SUMMARY.md` stay compact enough for active current-state reads and reference their relevant `history/` and `done/` shards
- `phase/SUMMARY.md` exists when phased execution is used and names governing patch artifacts or explicit `none`
- `phase/SUMMARY.md` keeps the phase map, source inputs, cross-phase handoffs, TODO/changelog coordination, verification, and rollback/containment picture current
- child phase files include design references, patch references or explicit `none`, objective, entry conditions, action checklist, affected artifacts, TODO/changelog coordination, verification, closeout, exit criteria, risks/rollback notes, and next possible phases when relevant
- phase-backed closeout explains delivered work, feature/improvement, user/system impact, verification basis, and next phase state when useful
- sufficiently clear governed design can be synthesized into phase order and current-phase live tasks when staged execution is warranted
- phase identity selection checks lineage before opening a new major phase and can resolve to current-phase update, existing-family subphase, new major, or ask-now posture
- TODO pending section contains pending-only items (`- [ ]`)
- TODO history has a dated entry for completed milestone work
- inactive `phase/done/`, `patch/done/`, and `changelog/done/` surfaces are consulted only for history/audit/rollback/provenance/trace needs
- no default `design/done/` pattern is introduced because design remains active blueprint authority
- files in `done/` are not treated as junk or deletion-authorized by completed status
- runtime install/parity checks do not classify or clean other-owner files in shared runtime destinations

### Real Examples (This Repository)

#### Example 1: Deterministic Recovery Contract Synchronization (WS-1)

```text
design/recovery-contract.design.md
  → refusal-and-recovery.md
  → changelog/recovery-contract.changelog.md
  → TODO.md (history/progress)
```

**What was synchronized:**
- Deterministic response keys were aligned across design and runtime (`decision_output`, `refusal_class`, `reason`, `what_can_be_done_now`, `how_to_proceed`)
- Changelog recorded the runtime/design version sync event
- TODO recorded completion in the hardening program history

#### Example 2: Verification + Output-Cap Consolidation (WS-5)

```text
design/safe-file-reading.design.md + design/safe-terminal-output.design.md
  → safe-io.md + safe-io.md
  → changelog/safe-file-reading.changelog.md + changelog/safe-terminal-output.changelog.md
  → TODO.md (WS-5 completion)
```

**What was synchronized:**
- Shared verification-trigger model applied across related rules
- Deterministic output-cap wording standardized (`head -100 | head -c 5000`, risky-file variant)
- Changelog and TODO were updated to preserve traceability

#### Example 3: TODO Governance Alignment (WS-6)

```text
TODO.md pending section audit
  → remove completed items from pending block
  → remove duplicate pending headings
  → add closure row in TODO history
```

**What was synchronized:**
- Pending section kept pending-only (`- [ ]`)
- Duplicate heading drift removed
- Program closure logged in dated history row

#### Example 4: Final `/phase` Review Model Rollout

```text
phase/SUMMARY.md
  → source-input extraction summary table
  → overview flow diagram
  → review summary table
  → phase/phase-NNN-*.md / phase/phase-NNN-NN-*.md
  → TODO.md history
```

**What was synchronized:**
- `/phase` became the live phase-planning namespace
- `SUMMARY.md` became the required summary/index for live phased execution
- child phase files were required to carry design extraction, review flow, reviewer checklist, and standardized review outcomes
- `SUMMARY.md` was extended to carry source-input rollup and review rollup views for faster approval
- the model gained an explicit Definition of Done and stop rule so governance expansion does not continue by default after completion
- communication rules were narrowed so next-step options are suggested only when genuinely useful rather than treated as a mandatory ending pattern

#### Example 5: One-Way Design + Patch Phase Synthesis

```text
design/*.design.md + patch/<context>.patch.md or root <context>.patch.md
  → phase/SUMMARY.md
  → phase/phase-NNN-*.md / phase/phase-NNN-NN-*.md
  → TODO.md history
```

**What was synchronized:**
- `phase-implementation` was extended from design-only extraction into one-way source synthesis
- `phase/SUMMARY.md` can now show both design inputs and patch inputs when patch-derived work matters
- child phase files can now carry optional patch references and patch-to-phase extraction alongside design traceability
- patch artifacts remained outside the live phase workspace
- design and patch documents did not gain a reverse-link requirement back to phase

#### Example 6: Startup Artifact Governance Rollout

```text
artifact-initiation-control.design.md
  → phase-todo-artifact.md
  → changelog/artifact-initiation-control.changelog.md
  → phase/SUMMARY.md + phase/phase-004-*.md
  → TODO.md history
```

**What was synchronized:**
- a new first-class startup-governance owner was created
- startup artifact posture now resolves before meaningful governed work drifts
- `project-documentation-standards`, `phase-implementation`, `todo-standards`, and `strict-file-hygiene` were aligned to the new startup contract
- the rollout itself opened `phase-004` from the start instead of being backfilled later

#### Example 7: P073 Runtime Compression and Install Parity

```text
41 active runtime rules
  → source-only semantic compression program
  → final semantic parity and aggregate reduction audit
  → explicit runtime install gate
  → source/runtime hash parity verification
```

**What was synchronized:**
- the active runtime scope stayed limited to the then-README-installed 41 root rule files
- final source state was recorded at 4,051 lines / 31,316 words / 231,675 bytes
- runtime install into `~/.claude/rules/` happened only after the separate install gate opened
- parity passed with no missing active files or hash mismatches
- co-located runtime files outside the source-owned install set remained observed-only and untouched

#### Example 8: Runtime Destination Ownership Boundary

```text
authority-and-scope.md
  → document-governance.md
  → document-integrity.md
  → document-integrity.md
  → README / TODO / phase / patch records
```

**What was synchronized:**
- runtime co-location was clarified as non-ownership authority
- destination files outside the current source-owned install set require owner/project scope resolution before classification or cleanup
- documentation, hygiene, and reference owners were aligned to preserve the source-owned/shared-destination/other-owner distinction

#### Example 9: Phase Closeout Feature and Impact Reporting

```text
explanation-and-presentation.md
  → phase-todo-artifact.md
  → explanation-and-presentation.md
  → accurate-communication.md
  → explanation-and-presentation.md
```

**What was synchronized:**
- phase-backed closeouts now report delivered work, feature/improvement, user/system impact, verification basis, and next phase state when relevant
- closeout wording remains evidence-honest and does not turn edited or partially verified work into fixed/stable claims
- audit/checklist detail no longer dominates the user-facing completion message

#### Example 11: Completed Documentation Surface Governance

```text
active phase / patch / changelog surfaces
  → completed history surfaces under done/ when scan bloat grows
  → active design remains blueprint truth
```

**What was synchronized:**
- `phase/done/`, `patch/done/`, and `changelog/done/` are inactive-by-default history surfaces
- broad current-state scans start from active docs and avoid `done/` unless history/audit/rollback/provenance/trace is needed
- `design/done/` is not a default pattern because design remains target-state authority
- completed history is not junk and does not authorize deletion

#### Example 10: Design-to-Phase Execution Synthesis

```text
governed design target state
  → phase-todo-artifact.md startup phase posture
  → phase-todo-artifact.md execution synthesis
  → current child phase files and current-phase live tasks
```

**What was synchronized:**
- sufficiently clear governed design can now drive phase posture and execution order when staged execution is warranted
- `/phase` may derive current child phase files and current-phase live tasks from design truth without replacing design as target-state authority
- real stop gates remain: design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, and approval-sensitive scope change

---

## 🎓 Framework Highlights

### 🧭 Current Phase Execution Model

**The current phased execution model uses `phase/SUMMARY.md` plus child phase files as the live execution workspace, while design stays target-state authority and patch stays before/after review authority.**

```text
governed design target state
  → startup artifact posture
  → phase identity selection: current phase / existing-family subphase / new major / ask-now
  → phase/SUMMARY.md phase map and source inputs
  → phase-NNN / phase-NNN-NN child execution files
  → current-phase live task list with visible phase context
  → closeout with delivered work, impact, verification, and next phase state
```

**What this gives you:**
- staged work gets a deterministic phase workspace instead of ad hoc planning drift
- sufficiently clear governed design can become phase order and current-phase live tasks when staged execution is warranted
- phase-shaped follow-up work checks family lineage before opening a new major phase, so related work can stay in the current phase or become an existing-family subphase when that is the truthful identity
- non-trivial phase-backed built-in task entries visibly carry phase ID, phase name, phase family, or clearly implied stage context in the subject or description
- patch inputs can feed phase planning one-way without turning `/patch` into the live phase namespace
- child phase files keep execution fields close to the actual phase: objective, entry conditions, actions, affected artifacts, verification, closeout, exit criteria, risks, and next possible phases
- closeout wording explains what changed and why it matters before audit/checklist detail dominates the message
- real stop gates remain intact for design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, and approval-sensitive scope change
- completed phase detail can leave active scans through `phase/done/` without becoming junk or replacing `phase/SUMMARY.md`

---

### 🧠 TRAAC (Task Runtime Adaptive AI Compression)

<div align="center">

**Complexity calibration so simple work stays direct and risky/system work gets deeper review**

```text
Simple work      → direct answer or short implementation path
Moderate work    → structured stepwise reasoning
High-risk work   → deeper comparison, security, and integration review
Critical work    → stronger verification, mitigation, and stop-gate handling
```

| Input | What it changes | Result |
|--------|-----------------|--------|
| Manual action steps | How much sequencing is needed | Avoids under-planning multi-step work |
| Decision points | Whether alternatives must be compared | Prevents premature path collapse |
| Dependencies | How much integration risk exists | Keeps external systems visible |
| Security requirements | How strict the review must be | Deepens auth/payment/data/destructive work |

</div>

---

### 👥 TUMIX Multi-Perspective Review

**Use Developer, Security, and Architect lenses when a task really spans implementation, risk, and architecture together.**

```text
Developer lens  ──┐
Security lens   ──┼──→ One evidence-backed recommendation
Architect lens  ──┘
```

**How it works:**
1. **Developer lens** → feasibility, implementation shape, and maintainability
2. **Security lens** → authorization, secrets, data, destructive-action, and abuse-risk boundaries
3. **Architect lens** → system ownership, integration, rollout, and future changeability
4. **Synthesis** → one practical recommendation with trade-offs when they matter

**Boundary:** this is perspective coverage, not automatic teammate spawning for every task.

---

### 📚 RoT (Retrieval of Thoughts)

<div align="center">

**Reuse previously validated reasoning patterns only after rechecking them against the current context**

| Action | Benefit |
|--------|---------|
| **Recognize** recurring problem shapes | Avoids solving the same pattern from zero every time |
| **Adapt** the candidate pattern | Keeps reuse tied to the current task, repo, and constraints |
| **Validate** before relying on it | Prevents stale memory or old fixes from becoming false authority |

**Boundary:** cached patterns accelerate reasoning, but checked current evidence still wins.

</div>

---

## 🖼️ Visual Guide

<div align="center">

### 🔴 Core Policies Visual

<table>
<tr>
<td align="center" width="33%">
<img src="img/anti-sycophancy.png" width="280"><br>
<b>Anti-Sycophancy</b><br>
<sub>Evidence-calibrated agreement</sub>
</td>
<td align="center" width="33%">
<img src="img/anti-mockup.png" width="280"><br>
<b>Anti-Mockup</b><br>
<sub>Real systems over fake surfaces</sub>
</td>
<td align="center" width="33%">
<img src="img/zero-hallucination.png" width="280"><br>
<b>Zero Hallucination</b><br>
<sub>Verify before strong claims</sub>
</td>
</tr>
</table>

---

### 🟡 Quality & Safety Visual

<table>
<tr>
<td align="center" width="25%">
<img src="img/authority-and-scope.png" width="200"><br>
<b>Authority & Scope</b><br>
<sub>User authority inside safe boundaries</sub>
</td>
<td align="center" width="25%">
<img src="img/emergency-protocol.png" width="200"><br>
<b>Emergency Protocol</b><br>
<sub>Rapid response</sub>
</td>
<td align="center" width="25%">
<img src="img/document-consistency.png" width="200"><br>
<b>Document Consistency</b><br>
<sub>Cross-reference check</sub>
</td>
<td align="center" width="25%">
<img src="img/functional-intent-verification.png" width="200"><br>
<b>Functional Intent</b><br>
<sub>Intent validation</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<img src="img/document-changelog-control.png" width="200"><br>
<b>Document Changelog Control</b><br>
<sub>Version tracking system</sub>
</td>
<td align="center" width="25%">
<img src="img/document-design-control.png" width="200"><br>
<b>Document Design Control</b><br>
<sub>Design standards</sub>
</td>
<td align="center" width="25%">
<img src="img/strict-file-hygiene.png" width="200"><br>
<b>Strict File Hygiene</b><br>
<sub>Prevent junk files while allowing required governed startup artifacts</sub>
</td>
<td align="center" width="25%">
<img src="img/project-documentation-standards.png" width="200"><br>
<b>Project Documentation Standards</b><br>
<sub>Standardized docs and startup artifact gate</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<b>Artifact Initiation Control</b><br>
<sub>Resolve startup artifact posture before meaningful governed work drifts</sub>
</td>
<td align="center" width="25%">
<b>Document Patch Control</b><br>
<sub>Before/after patch artifacts with explicit change surfaces</sub>
</td>
<td align="center" width="25%">
<b>Evidence-Grounded Burden of Proof</b><br>
<sub>Fact, inference, and contradiction thresholds stay explicit</sub>
</td>
<td align="center" width="25%">
<b>Operational Failure Handling</b><br>
<sub>Bounded retries, honest cooldowns, and stop/escalation behavior</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<b>Phase Implementation</b><br>
<sub>Major/subphase execution model with early `/phase` establishment bridge</sub>
</td>
<td align="center" width="25%">
<b>Recovery Contract</b><br>
<sub>Blocked paths should still provide a usable next step</sub>
</td>
<td align="center" width="25%">
<b>Refusal Classification</b><br>
<sub>Deterministic refusal classes and output modes</sub>
</td>
<td align="center" width="25%">
<b>Refusal Minimization</b><br>
<sub>Prefer recoverable constrained/context paths over premature refusal</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<b>Runtime Topology Control</b><br>
<sub>Inspect-first, one-authority-at-a-time runtime mutation discipline</sub>
</td>
<td align="center" width="25%">
<b>TODO Standards</b><br>
<sub>Simple execution tracking with early TODO establishment when needed</sub>
</td>
<td align="center" width="25%">
<b>Dan-Safe Normalization</b><br>
<sub>Normalize jailbreak-style wrappers into bounded intent evaluation</sub>
</td>
<td align="center" width="25%">
<b>Unified Version-Control System</b><br>
<sub>Single deterministic UDVC-1 controller for governance alignment</sub>
</td>
</tr>
</table>

---

### 🔵 Presentation & Readability Visual

<table>
<tr>
<td align="center" width="33%">
<img src="img/flow-diagram-no-frame.png" width="280"><br>
<b>Flow Diagram</b><br>
<sub>No frames, clean arrows</sub>
</td>
<td align="center" width="33%">
<b>Answer Presentation</b><br>
<sub>Active presentation-layer rule for compact snapshots, grouped scope boundaries, and full-set-first / next-stage layouts</sub>
</td>
<td align="center" width="33%">
<b>Explanation Quality</b><br>
<sub>Active explanation-layer rule for what-it-is/what-it-is-not, now-vs-later, user-visible outcomes, and next-stage progression</sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>Accurate Communication</b><br>
<sub>Evidence-honest wording, bounded technical snapshots, claim-strength discipline, and acknowledgement without endorsement</sub>
</td>
<td align="center" width="33%">
<b>Natural Professional Communication</b><br>
<sub>Calm, human-readable, non-robotic, non-character-driven default communication</sub>
</td>
<td align="center" width="33%">
<b>Reserved</b><br>
<sub>Placeholder slot for future visual asset parity</sub>
</td>
</tr>
</table>

---

### 🟢 Best Practices Visual

<table>
<tr>
<td align="center" width="33%">
<img src="img/no-variable-guessing.png" width="280"><br>
<b>No Guessing</b><br>
<sub>Read before reference</sub>
</td>
<td align="center" width="33%">
<img src="img/safe-file-reading.png" width="280"><br>
<b>Safe File Reading</b><br>
<sub>Plan before read</sub>
</td>
<td align="center" width="33%">
<img src="img/safe-terminal-output.png" width="280"><br>
<b>Safe Terminal</b><br>
<sub>Output management</sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>Tactical Strategic Programming</b><br>
<sub>Tactical speed with mandatory strategic target and convergence path</sub>
</td>
<td align="center" width="33%">
<b>Maintainable Code Structure</b><br>
<sub>Responsibility boundaries without rigid templates</sub>
</td>
<td align="center" width="33%">
<b>Reserved</b><br>
<sub>Placeholder slot for future visual asset parity</sub>
</td>
</tr>
</table>

</div>

---

## 📊 Before & After

### ❌ Without Rules

```text
User: "Set up database connection"
       ↓
AI: "Here's the connection string:
     DATABASE_URL=postgres://localhost:5432/mydb"

Result: ❌ Guessed values
        ❌ No verification
        ❌ Potentially wrong
        ❌ User frustrated
```

---

### ✅ With Rules

```text
User: "Set up database connection"
       ↓
AI: "Let me check your .env file first..."
     [Reading configuration...]
     "Found your existing config:
      DATABASE_URL=postgres://prod-server:5432/app_db

      Should I use this, or do you want to change it?"

Result: ✅ Verified from actual files
        ✅ No guessing
        ✅ User confirmation
        ✅ Professional interaction
```

**The difference?** Professional AI behavior that respects your existing configuration.

---

## 📊 Current Quality Signals

<div align="center">

### Active runtime scope

- Current README meaning: 18 source-owned root runtime rules form the active merged install set.
- Impact: keeps install scope explicit after root-rule compression.

### Runtime install boundary

- Current README meaning: the Quick Start block installs the compact 18-rule source-owned active runtime set and uses owner-aware cleanup instead of filename-only deletion.
- Source state: this README reflects the released `v10.38 / P130` always-on plan-file-backed goal model while the active runtime install set remains 18 root rules, created governed `/goal` output now authors plan-first and references the prepared route file, and `playground/` stays outside the install payload.
- Ownership guard: manifest-owned files are removed only when they still match the last recorded install snapshot, and legacy pre-manifest files are quarantined only when their content exactly matches this repo's git history for that rule path.
- Boundary: files already present in a shared runtime destination but outside this repo's recorded install ownership or repo-history proof are not cleanup targets by default.
- Impact: protects install scope and other-owner runtime files while still allowing safe cleanup of this repo's old runtime leftovers, including legacy installs from before the merged-rule transition.

### Governed document capacity and automation

- Current README meaning: active governance documents stay role-bounded, and detected touched-scope God pressure must get an owner outcome.
- Repair routes: repair clear local overload now, shard active design truth, roll over accumulated history/detail, split God Phase/God Patch candidates, or plan a visible repair slice.
- Impact: keeps active docs cheaper to read, edit, diff, and verify.

### Evidence discipline

- Current README meaning: proof-seeking and claim-state boundaries stay separate.
- Scope: fact, preference/direction, factual endorsement, inference, hypothesis, uncertainty, memory, scoped non-finding, and binding constraints.
- Impact: reduces overclaim, floating recommendation, sycophantic agreement, and hallucination risk.

### Phase execution

- Current README meaning: governed design can drive phase posture, order, and tasks.
- Lineage: phase-shaped follow-up checks current phase, subphase, new major, or ask-now posture.
- Live tasks: non-trivial phase-backed entries visibly carry phase context.
- Closeout: roadmap context can support next-phase recommendations at true closeout.
- Coding gates: material coding phases preserve Development Verification / TestKit Coverage when it affects exit criteria.
- Impact: reduces retrospective phase backfill, phase-hidden task drift, silent closeout dead-ends, and edit-only coding closeout.

### Completed/history surfaces

- Current README meaning: history, detail, and done surfaces are referenced or inactive by role, not deletion authority.
- Included surfaces: `todo/history/`, `todo/done/`, `phase/history/`, `phase/done/`, `patch/done/`, `changelog/<chain>/v*.changelog.md` for indexed version detail, and `changelog/done/` for legacy/archive/fallback history.
- Boundary: `design/done/` is not a default pattern.
- Impact: reduces active scan bloat without deleting governed history.

### Shared destination boundary

- Current README meaning: co-located runtime files outside the source-owned set are not cleanup targets by default.
- Impact: prevents other-owner file damage.

</div>

---

## 🔒 Safety Commitments

<div align="center">

### ✅ Operating Commitments

| Commitment | Description |
|-----------|-------------|
| **No Mock/Stub by Default** | Prefer real systems and clearly label or avoid fake implementations unless explicitly requested |
| **No Guessing** | Verify local paths, values, symbols, and configuration before treating them as known |
| **Evidence-Honest Claims** | Match wording strength to checked evidence and disclose scoped non-findings |
| **No Sycophancy** | Evaluate user proposals before agreement-shaped wording, accept safe user direction without factual or quality endorsement, seek proof before substantial recommendations or challenges, and correct claims when evidence conflicts |
| **Destructive-Action Guard** | Cleanup, hygiene, isolation, or worktree rationale never authorizes deletion by itself |

**The practical goal is safe, evidence-grounded AI behavior that keeps user authority intact.**

</div>

---

## 🤝 Contributing

<div align="center">

These rules evolve based on real-world usage:

- 🔄 **Real-world usage patterns** → What actually works
- 💬 **User feedback** → Your experience matters
- 🔐 **Safety considerations** → Stronger boundaries and safer defaults
- ⚡ **Context discipline** → Keeping runtime guidance useful without unnecessary bloat

### 📝 Contribution Guidelines

**Pull requests welcome!** Please ensure:
1. New rules follow existing format
2. Include clear documentation
3. Add visual assets if applicable
4. Update changelog
5. Respect completion boundaries — do not add new mandatory capability blocks to a completed governance model unless the change is explicitly justified and intentionally approved

**We value:** Quality over quantity, clarity over complexity, and bounded governance over endless expansion

</div>

---

## 📜 License

<div align="center">

**MIT License** - Feel free to adapt for your own use case.

> Attribution appreciated but not required.

</div>

---

## 🙏 Acknowledgments

<div align="center">

Personal rule set and configuration framework for Claude Code CLI.

**Inspired by:**
- Constitutional AI principles (Anthropic)
- Best practices for AI assistant development
- Real-world production experience
- Community feedback and contributions

**Built with ❤️ for the Claude Code community**

</div>

---

<div align="center">

---

<p>
  <b>Version</b>: 10.38 |
  <b>Last Updated</b>: 2026-06-02 |
  <b>Framework</b>: Sophisticated AI Framework with Constitutional Governance
</p>

<p>
  <a href="#top">⬆️ Back to Top</a>
</p>

---

<p>
  <sub>Made with 💙 by developers who care about AI quality</sub>
</p>

</div>
