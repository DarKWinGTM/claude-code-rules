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
  <b>v9.80</b><br><sub>Current Release</sub>
</td>
<td align="center" width="200">
  <b>42</b><br><sub>Active Runtime Rules</sub>
</td>
<td align="center" width="200">
  <b>Verified</b><br><sub>Runtime Parity Gate</sub>
</td>
<td align="center" width="200">
  <b>Subagent-first</b><br><sub>Intent-first Routing</sub>
</td>
</tr>
</table>

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
- [📂 Design Documentation Structure](#-design-documentation-structure)
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

Use the script for your platform. Both install the current active runtime rules only.

### Bash — Linux / macOS

```bash
# Clone once
if [ ! -d "claude-code-rules" ]; then
  git clone https://github.com/DarKWinGTM/claude-code-rules.git
fi

cd claude-code-rules || exit 1

# Install active runtime rules into ~/.claude/rules/
mkdir -p "$HOME/.claude/rules"

rule_files=(
  accurate-communication.md
  technical-snapshot-communication.md
  response-closing-and-action-framing.md
  answer-presentation.md
  anti-mockup.md
  anti-sycophancy.md
  artifact-initiation-control.md
  authority-and-scope.md
  custom-agent-selection-priority.md
  dan-safe-normalization.md
  document-consistency.md
  document-changelog-control.md
  document-design-control.md
  document-patch-control.md
  emergency-protocol.md
  evidence-grounded-burden-of-proof.md
  explanation-quality.md
  external-verification-and-source-trust.md
  flow-diagram-no-frame.md
  functional-intent-verification.md
  memory-governance-and-session-boundary.md
  natural-professional-communication.md
  native-worker-agent-routing-and-context-control.md
  no-variable-guessing.md
  operational-failure-handling.md
  phase-implementation.md
  portable-implementation-and-hardcoding-control.md
  project-documentation-standards.md
  recovery-contract.md
  refusal-classification.md
  refusal-minimization.md
  runtime-topology-control.md
  safe-file-reading.md
  safe-terminal-output.md
  strict-file-hygiene.md
  tactical-strategic-programming.md
  todo-standards.md
  unified-version-control-system.md
  zero-hallucination.md
  high-signal-communication.md
  execution-continuity-and-mode-selection.md
  goal-set-review-and-priority-balance.md
)

for file in "${rule_files[@]}"; do
  cp "$file" "$HOME/.claude/rules/$file"
done
```

### PowerShell — Windows

```powershell
# Clone once
if (-not (Test-Path "claude-code-rules")) {
  git clone https://github.com/DarKWinGTM/claude-code-rules.git
}

Set-Location claude-code-rules

# Install active runtime rules into ~/.claude/rules/
$rulesDir = Join-Path $HOME ".claude/rules"
New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null

$ruleFiles = @(
  "accurate-communication.md",
  "technical-snapshot-communication.md",
  "response-closing-and-action-framing.md",
  "answer-presentation.md",
  "anti-mockup.md",
  "anti-sycophancy.md",
  "artifact-initiation-control.md",
  "authority-and-scope.md",
  "custom-agent-selection-priority.md",
  "dan-safe-normalization.md",
  "document-consistency.md",
  "document-changelog-control.md",
  "document-design-control.md",
  "document-patch-control.md",
  "emergency-protocol.md",
  "evidence-grounded-burden-of-proof.md",
  "explanation-quality.md",
  "external-verification-and-source-trust.md",
  "flow-diagram-no-frame.md",
  "functional-intent-verification.md",
  "memory-governance-and-session-boundary.md",
  "natural-professional-communication.md",
  "native-worker-agent-routing-and-context-control.md",
  "no-variable-guessing.md",
  "operational-failure-handling.md",
  "phase-implementation.md",
  "portable-implementation-and-hardcoding-control.md",
  "project-documentation-standards.md",
  "recovery-contract.md",
  "refusal-classification.md",
  "refusal-minimization.md",
  "runtime-topology-control.md",
  "safe-file-reading.md",
  "safe-terminal-output.md",
  "strict-file-hygiene.md",
  "tactical-strategic-programming.md",
  "todo-standards.md",
  "unified-version-control-system.md",
  "zero-hallucination.md",
  "high-signal-communication.md",
  "execution-continuity-and-mode-selection.md",
  "goal-set-review-and-priority-balance.md"
)

foreach ($file in $ruleFiles) {
  Copy-Item $file (Join-Path $rulesDir $file) -Force
}
```

### Notes

- Already cloned the repo? Skip the clone step and run the install block only.
- Need project-specific install instead? Change the destination from `~/.claude/rules/` to `./.claude/rules/`.
- This runtime-only install copies active rule files only. Governed design/changelog/TODO/phase/patch artifacts, inactive `phase/done/`, `patch/done/`, and `changelog/done/` history surfaces, plus `phase-implementation-template.md` remain in the repository for maintenance and synchronized updates; files already present in a shared runtime destination but outside this 42-file source-owned set are not cleanup targets by default.

### 🤖 AI-Assisted Install Prompts

If you want an AI CLI to install or adapt this repo for you, paste one of these prompts directly into that tool.

**Claude Code — native install into `~/.claude/rules/`**

```text
Install this rules repo for me from:
https://github.com/DarKWinGTM/claude-code-rules

Requirements:
- clone the repo if needed
- read the README Quick Start section first
- install only the active runtime rule set into ~/.claude/rules/
- do not install files from suspend/, support/, plugin/, design/, changelog/, phase/, patch/, or TODO.md
- verify the installed files after copying
- report exactly what was installed
```

**Codex CLI — adapt active rules into `AGENTS.md`**

```text
Use this repo as the source of truth:
https://github.com/DarKWinGTM/claude-code-rules

Please:
- clone or inspect the repo
- read the README Quick Start and active root rule set
- create/update AGENTS.md for this project so Codex follows the same active rule intent
- adapt the rules into Codex-native instructions instead of copying Claude-specific runtime structure blindly
- ignore files under suspend/, support/, plugin/, design/, changelog/, phase/, patch/, and TODO.md unless explicitly needed as reference
- keep the result concise but faithful to the active rules
- summarize which source rules were mapped into AGENTS.md
```

**Gemini CLI — adapt active rules into `GEMINI.md`**

```text
Use this repo as the source of truth:
https://github.com/DarKWinGTM/claude-code-rules

Please:
- clone or inspect the repo
- read the README Quick Start and active root rule set
- create/update GEMINI.md for this project so Gemini CLI follows the same active rule intent
- adapt the rules into Gemini-native instructions instead of copying Claude-specific runtime structure blindly
- ignore files under suspend/, support/, plugin/, design/, changelog/, phase/, patch/, and TODO.md unless explicitly needed as reference
- keep the result concise but faithful to the active rules
- summarize which source rules were mapped into GEMINI.md
```

**When to use which prompt**
- Use the **Claude Code** prompt when you want direct runtime installation into `~/.claude/rules/`
- Use the **Codex CLI** prompt when you want equivalent behavior through `AGENTS.md`
- Use the **Gemini CLI** prompt when you want equivalent behavior through `GEMINI.md`

---

## ✨ Features

<div align="center">

### 🎯 Core Capabilities

<table>
<tr>
<td width="50%">

#### 🔍 Evidence-First Accuracy
- Seek practical proof before substantial reasoning when material
- Separate fact, inference, hypothesis, and scoped non-finding
- Use evidence as grounding, not an automatic decision lock
- No guessing local paths, values, symbols, or config

</td>
<td width="50%">

#### 🛡️ Anti-Sycophancy
- Evidence-seeking agreement, design, recommendation, and challenge
- User preference/direction stays separate from factual proof
- Factual agreement requires checked evidence
- Claim-focused corrections remain allowed when evidence conflicts

</td>
</tr>
<tr>
<td width="50%">

#### 🔒 Security First
- Real systems over simulations
- No mock implementations by default
- Verified configurations before strong claims
- Destructive/high-impact actions require intent clarity

</td>
<td width="50%">

#### Runtime Context Discipline
- 42 active runtime rules only
- P073 source compression completed and audited
- P073/P077/P078/P079 runtime install parity was verified only after explicit install gates
- P080 source governance is synchronized and runtime install parity is verified for the 42-rule set
- P081 source governance is synchronized for v9.80; runtime install parity is verified for the 42 active rule set; git push completed and GitHub release `v9.80` is published
- Completed `phase/`, `patch/`, and `changelog` history can move to inactive `done/` surfaces
- Non-runtime governance artifacts stay out of runtime install

</td>
</tr>
</table>

</div>

---

## 📁 Rule Files

<div align="center">

### 🔴 Core Policies (3 rules)

> **Fundamental principles that govern all AI behavior**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`anti-mockup.md`](anti-mockup.md) | Real systems over simulations | No fake implementations |
| [`anti-sycophancy.md`](anti-sycophancy.md) | Evidence-seeking agreement/disagreement | Honest feedback that can accept user direction without factual endorsement, seek practical evidence before substantial alignment or challenge, and correct claims when evidence conflicts |
| [`zero-hallucination.md`](zero-hallucination.md) | Verify-first factual discipline | Fact, preference/direction, inference, hypothesis, uncertainty, scoped non-findings, factual endorsement, and proof-aware assumptions stay separate |

---

### 🟡 Quality & Safety (30 rules)

> **Ensure consistent, safe, and well-documented outputs**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`accurate-communication.md`](accurate-communication.md) | Clear, honest communication | No vague claims, no over-strong contradiction wording, acknowledgement without factual endorsement, evidence-backed agreement, user-owned preference/direction separation, reusable partial-evidence technical snapshot wording, stronger human-language glosses, easy-explanation continuity so plain Thai explanations stay simple through the full answer, clearer explanation of variables/fields/config keys/internal labels when answers depend on them, goal-qualified proposal wording for advisory future-work ideas, honest duplicate-looking Team Agent reporting with observed-vs-inferred state separation, governing-basis clarification before deep branch analysis, compact post-compact re-anchor wording, explicit memory-derived-context disclosure wording for path-matched remembered context, natural-professional wording, direct human-readable action/result wording preferred over metaphor-heavy internal shorthand, main-point-first framing for diagnosis/test/recommendation/proposal/update answers, evidence-honest phase closeout delivery/feature/impact wording, continuation-first guidance, clearer recommendation-plus-reason next-step wording that still preserves alternatives when multiple paths are real, and active summaries that keep resolved topics available for reasoning without repeating them as current issues by default |
| [`artifact-initiation-control.md`](artifact-initiation-control.md) | Startup artifact governance | Resolve design/changelog/TODO/phase/patch posture before meaningful governed work drifts, resolve phase posture from sufficiently clear governed design when staged execution is warranted, initialize live task tracking early when non-trivial work needs visible execution state, treat phase-backed live task tracking as expected startup behavior, keep initialized live task lists as the continuing surface for the active objective, keep newly encountered unclear files in classification-first posture rather than disposal-first posture, and keep patch non-default during greenfield startup unless a real before/after review surface exists |
| [`authority-and-scope.md`](authority-and-scope.md) | Decision hierarchy | User authority respected, checked master/governed repo surfaces outrank git-state cleanup heuristics when classifying file meaning, runtime co-location is not ownership authority, destination/runtime files outside the current source-owned install set require owner/project scope resolution before classification or cleanup, fresh user directives override previously offered assistant options, unnecessary option branching is discouraged when one safe continuation path already exists, future-work proposals stay advisory until explicitly selected, user-declared RULES-first issues stay RULES-first instead of being diverted into memory-first fixes, memory applicability now defers to the dedicated memory-governance owner, non-matching path-scoped remembered context cannot override the current repo/objective, unresolved governing-basis selection stays user-owned unless authority/evidence already settles it, compacted-session continuation re-anchors to the latest active directive and active frame, and overlapping team expansion stays advisory unless a distinct new role is actually needed |
| [`custom-agent-selection-priority.md`](custom-agent-selection-priority.md) | Custom agent selection priority | Prefer the best visible custom/specialist agent after native worker routing has already classified intent, selected the needed worker capability, and chosen a direct/subagent/multi-subagent/team scale; do not turn agent availability into a routing or Agent Team escalation decision |
| [`dan-safe-normalization.md`](dan-safe-normalization.md) | Prompt-wrapper normalization | Safer intent evaluation before decisioning |
| [`document-consistency.md`](document-consistency.md) | Cross-reference validation | Keeps portable, source-side, source-owned active runtime, shared runtime destination, other-owner runtime, destination/runtime, local execution, and reusable source-artifact references from drifting into each other so parity/install wording does not turn shared-destination co-location into ownership, and requires governed reference/history checks before junk/disposal classification |
| [`document-changelog-control.md`](document-changelog-control.md) | Version tracking system | Active changelogs stay version authority while `changelog/done/` can hold inactive completed/older history when active scans would become too large |
| [`document-design-control.md`](document-design-control.md) | Design document standards | Active blueprint/target-state structure, no default `design/done/`, and required capture of implementation-relevant truth extracted from external docs/specs/provider references when later work still depends on it |
| [`document-patch-control.md`](document-patch-control.md) | Patch Control | Governed before/after patch/review artifacts outside the live `/phase` workspace, with `patch/done/` as inactive completed patch history rather than junk or active phase input by default |
| [`emergency-protocol.md`](emergency-protocol.md) | Crisis response | Fast, safe reactions |
| [`evidence-grounded-burden-of-proof.md`](evidence-grounded-burden-of-proof.md) | Evidence-seeking proof-aware judgment | One first-class authority for practical evidence-seeking before substantial reasoning, ordinary-evidence-versus-binding-constraint thresholds, burden-of-proof thresholds for factual endorsement and contradiction, user-owned preference/direction separation, fact/inference/hypothesis separation, scoped negative-evidence semantics, unresolved governing-basis uncertainty handling, remembered path-matched context as a distinct evidence/claim state, post-compact needs-recheck handling for compacted carry-forward exact detail, and explicit limits on using git-state evidence for disposal conclusions |
| [`external-verification-and-source-trust.md`](external-verification-and-source-trust.md) | External verification and source trust | Proactive web-backed fact checking, source ranking, corroboration, honest source-conflict handling, and external evidence grounding for recommendation/design judgments |
| [`functional-intent-verification.md`](functional-intent-verification.md) | Intent validation | Clarifies destructive, ambiguous, or high-impact intent before execution, with a real delete guard that blocks cleanup/isolation rationale from acting as deletion authorization |
| [`memory-governance-and-session-boundary.md`](memory-governance-and-session-boundary.md) | Memory governance and session boundary | Treat memory as scoped reusable context rather than active authority, keep root `MEMORY.md` as an active index only, use `global/path/archive` semantics, make path the primary applicability key, keep session IDs as provenance only, keep archived memory inactive by default, and keep any optional external recall generic, supplemental, availability-checked, and subordinate to stronger checked execution surfaces |
| [`operational-failure-handling.md`](operational-failure-handling.md) | Operational failure policy | Bounded retry ceilings, honest cooldown guidance, and stop/escalation behavior for technical failures, including duplicate-looking Team Agent handling that treats stale or duplicate-looking presence as inspect-before-respawn rather than respawn-first churn |
| [`phase-implementation.md`](phase-implementation.md) | Phase planning semantics | First-class `/phase` + `SUMMARY.md` model with major/subphase identities, design-to-phase execution synthesis when staged execution is warranted, current-phase-first but phase-context-aware live task-list linkage, explicit phase-to-patch linkage when patch is in scope, `phase/done/` as inactive completed phase history, phase closeout reporting that states delivered work/impact/verification/next state, bounded next-work discovery from active phase surfaces, and session-aligned wording for phase-linked task entries |
| [`runtime-topology-control.md`](runtime-topology-control.md) | Runtime topology discipline | Bounded inspect-first, one-authority-at-a-time runtime mutation posture that prevents debug-by-expansion and requires explicit approval for additive or authority-changing topology moves |
| [`technical-snapshot-communication.md`](technical-snapshot-communication.md) | Technical snapshot communication | First-class owner for bounded technical snapshot wording, exact/partial/inferred separation, scoped local-fact snapshot communication, and concise diagnostic snapshot state reporting |
| [`response-closing-and-action-framing.md`](response-closing-and-action-framing.md) | Response closing and action framing | First-class owner for concise end-of-response synthesis, clear action framing, recommendation-with-reason wording, alternative preservation, closed-topic summary handling, phase-backed closeout synthesis for delivered work, feature/improvement, impact, verification basis, and next phase state, and advisory goal-qualified proposal framing |
| [`recovery-contract.md`](recovery-contract.md) | Blocked-response contract | Every constrained/refused path has actionable next steps |
| [`tactical-strategic-programming.md`](tactical-strategic-programming.md) | Tactical vs strategic doctrine | Tactical entry stays fast, but every tactical move must point toward a declared strategic target and convergence path |
| [`natural-professional-communication.md`](natural-professional-communication.md) | Communication style doctrine | Default to calm, human-readable, non-robotic, non-character-driven professional communication, keep easy explanations in an everyday Thai register when the user asks for simpler wording, reject metaphor-heavy or management-style abstraction when direct wording would be clearer, and front-load the operational purpose when the answer would otherwise bury it behind warm-up framing |
| [`refusal-classification.md`](refusal-classification.md) | Deterministic refusal taxonomy | Consistent block decisions and traceable output modes |
| [`refusal-minimization.md`](refusal-minimization.md) | False-refusal reduction | Prefer recoverable constrained/context paths when authorized |
| [`strict-file-hygiene.md`](strict-file-hygiene.md) | File hygiene | Prevent junk files while allowing required governed startup artifacts, keep hygiene/cleanup wording from acting as deletion authority, and prevent shared runtime destination co-location from making other-owner runtime files junk by default |
| [`todo-standards.md`](todo-standards.md) | Task management | Durable TODO tracking plus same-objective built-in task-list reuse, append-not-replace behavior, completed-task visibility, current-phase-first but phase-context-aware live execution visibility, required inspection of relevant governed `/phase` context before shaping task entries when that context exists, task creation aligned to active phase or clearly implied staged context, bounded use of already-authored `/phase` planning data for continuity and draft next-work discovery, task wording that follows the actual active session language pattern with Thai-led default wording for Thai-led sessions, preserved natural Thai+English mix when that is the real session pattern, and technical labels left in technical form when forced translation would reduce clarity, task-list-first next-work discovery with bounded fallback, explicit required TODO sync as companion work when `TODO.md` is needed, and deferral of broader shared-board coordination semantics to the external coordination owner when applicable |
| [`project-documentation-standards.md`](project-documentation-standards.md) | Project documentation standards | Standardized docs for all projects plus startup artifact gate, completed documentation surface governance for `phase/done/`, `patch/done/`, and `changelog/done/`, no-default-`design/done/` blueprint boundary, governed companion status for required design/changelog/TODO/phase/patch surfaces, phase-shaped task creation alignment, runtime installs scoped to the current project/source-owned active runtime rule set, other-owner runtime destination file boundary, live-task-list-vs-durable-TODO distinction, non-default startup patch posture, and portable public onboarding/install guidance |
| [`portable-implementation-and-hardcoding-control.md`](portable-implementation-and-hardcoding-control.md) | Portable implementation control | Keep shared artifacts, reusable support/package source artifacts, and public onboarding/install guidance portable by default, bind environment-specific values late, and prevent machine-local hardcoding drift |
| [`execution-continuity-and-mode-selection.md`](execution-continuity-and-mode-selection.md) | Execution continuity and mode selection | Separates discussion mode from execution mode, re-checks intent when pasted logs/paths/snippets could be behavior/RULES evidence rather than project authorization, keeps startup governance as an execution precondition, keeps work moving when execution mode is active, discovers the next unfinished slice from execution surfaces, and sends broad continuation through subagent-first worker routing before leader raw absorption |
| [`unified-version-control-system.md`](unified-version-control-system.md) | Unified version governance | Single deterministic UDVC-1 controller |

---

### 🔵 Presentation & Readability (5 rules)

> **Improve answer structure, clarity, and visual scanability**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`answer-presentation.md`](answer-presentation.md) | Answer presentation standards | Readable and orderly responses with purpose-first framing near the start of diagnosis/test/recommendation/proposal/update answers, more proactive support for light readable tables when side-by-side structure materially improves comprehension without reviving a custom table-format rule, compact titled snapshots, small fact tables, stronger grouped scope-boundary sections, full-set-first / next-stage presentation, natural-flow formatting, compact governing-basis clarification blocks, compact post-compact re-anchor blocks for compacted-session continuation, compact memory-status blocks for remembered path-scoped context, compact variable-role structures for identifier-heavy explanations, compact phase-backed closeout blocks for delivered work, feature/improvement, impact, verification, and next phase state, compact near-term gloss support for abstract internal phrasing, and compact proposal layouts that distinguish advisory future-work ideas from queued execution |
| [`explanation-quality.md`](explanation-quality.md) | Explanation structure quality | Plain-language-first, proof-aware, step-by-step reasoning that shows checked evidence, what it proves, what it suggests, what it does not prove, and whether it is a hard constraint or ordinary grounding input when that distinction matters; also includes a purpose-first explanation step for diagnosis/test/recommendation/proposal/update answers, phase-backed closeout explanation that starts with practical delivered feature/improvement and user/system meaning before governance detail, more proactive support for light tables in diagnostic and multi-field clarification when side-by-side scanability materially improves understanding, stronger what-it-is/what-it-is-not, now-versus-later, user-visible-outcome, short-recap, whole-set-first, stage-progression, good-operator explanation flow, stop-before-overexplaining boundaries, direct translation of architecture-first or metaphor-heavy wording into human-readable action/result language, a governing-basis clarification boundary before deep multi-branch explanation, a compact post-compact re-anchor boundary before explanation resumes after compaction, explicit support for unpacking variables/fields/config keys/internal labels before deeper reasoning, explicit deferral of continuation-vs-option policy to accurate-communication, and goal-qualified proposal framing when future ideas are offered after bounded completion |
| [`flow-diagram-no-frame.md`](flow-diagram-no-frame.md) | Clean ASCII diagrams | Better readability |
| [`high-signal-communication.md`](high-signal-communication.md) | High-signal response tightening | Removes low-value extra content and repeated wording without replacing the main communication-owner chains |
| [`goal-set-review-and-priority-balance.md`](goal-set-review-and-priority-balance.md) | Goal review and priority balance | Keeps the full active goal set visible so work on A does not crowd out B and C |

---

### 🟢 Best Practices (4 rules)

> **Optimize your daily workflow efficiency**

| Rule | Purpose | Key Benefit |
|:-----|:--------|:------------|
| [`no-variable-guessing.md`](no-variable-guessing.md) | Read before reference | No wrong assumptions, including keeping git-state file signals as weak local evidence only |
| [`native-worker-agent-routing-and-context-control.md`](native-worker-agent-routing-and-context-control.md) | Native worker routing | Classifies intent before project exploration, routes broad/noisy/high-context/multi-surface work by required capability, prefers standalone subagent lanes first, and keeps Agent Team workflow as an exceptional coordination escalation while the leader remains synthesis and verification owner |
| [`safe-file-reading.md`](safe-file-reading.md) | Plan-before-read | Efficient file handling |
| [`safe-terminal-output.md`](safe-terminal-output.md) | Output management | No terminal flooding |

**📊 Active Runtime Rules: 42**

Latest refinement: P081 refines native worker routing so pasted technical evidence is classified by user intent before project exploration, broad independent work is standalone-subagent-first, worker selection is capability-based rather than hardcoded by tool name, and Agent Team workflow remains an exceptional coordination escalation.
</div>

---

## 📦 Installation

The Quick Start block above is still the canonical runtime-only install block. The methods below use the same active 42-rule set and describe when to use each path without repeating the long file list.

### 🎯 Method 1: Full Installation (Recommended)

**Use this when:** you want the full active runtime set installed globally.

Fastest path:
1. Clone the repository.
2. Run the Quick Start block exactly as shown above.
3. Run the verification commands below.

If you already cloned the repo earlier, you do **not** need to repeat the clone step. Just return to the repo root, keep the same Quick Start file list, and rerun only the install portion against `~/.claude/rules/`.

### 🎯 Method 2: Pick Your Rules

**Use this when:** you only want a small subset of the runtime rules.

```bash
# Example: Install just the anti-sycophancy rule
curl -o ~/.claude/rules/anti-sycophancy.md \
  https://raw.githubusercontent.com/DarKWinGTM/claude-code-rules/master/anti-sycophancy.md
```

### 🎯 Method 3: Project-Specific

**Use this when:** you want the same active runtime set, but only inside the current project.

1. Create `./.claude/rules/` in the project root.
2. Reuse the same Quick Start command pattern.
3. Change only the destination path from `~/.claude/rules/` to `./.claude/rules/`.

This keeps the install set identical while scoping the rules to one repository.

> Source-side note: public commands in this README are expressed from the repo root.
> Destination/runtime note: installation targets are shown separately as `~/.claude/rules/` or `./.claude/rules/`.

### 📍 Installation Paths

| Location | Scope | Path | Use Case |
|----------|-------|------|----------|
| **Global** | All projects | `~/.claude/rules/*.md` | Default recommendation |
| **Project** | Current project only | `./.claude/rules/*.md` | Project-specific needs |

### ✅ Verify Installation

> Global install: verify under `~/.claude/rules/`.
> Project-specific install: verify under `./.claude/rules/` instead.

```bash
# Global install check
claude --version
head -20 ~/.claude/rules/anti-sycophancy.md
ls ~/.claude/rules/answer-presentation.md
ls ~/.claude/rules/phase-implementation.md
ls ~/.claude/rules/artifact-initiation-control.md

# Project-specific install check (run from project root)
head -20 ./.claude/rules/anti-sycophancy.md
ls ./.claude/rules/answer-presentation.md
ls ./.claude/rules/phase-implementation.md
ls ./.claude/rules/artifact-initiation-control.md
```

---

## 📂 Design Documentation Structure

| Location | Purpose | File Type |
|----------|---------|-----------|
| `./design/*.design.md` | Active design specifications and target-state truth | Design docs; no default `design/done/` |
| `*.md` (root) | Active runtime rules | Rules files |
| `./changelog/changelog.md` | Master repository-wide history | Master changelog |
| `./changelog/*.changelog.md` | Per-chain authoritative active history/current version state | Active changelogs |
| `./changelog/done/*.changelog.md` | Older or completed detailed history outside active scans | Inactive history for audit/rollback/provenance/trace |
| `./phase/SUMMARY.md` | Governed summary/index for live phase planning, one-way source-input rollup, and review rollup | Phase summary doc |
| `./phase/phase-NNN-<phase-name>.md` | Governed active major-phase execution detail | Active major phase docs |
| `./phase/phase-NNN-NN-<subphase-name>.md` | Governed active subphase execution detail | Active subphase docs |
| `./phase/done/phase-NNN-*.md` | Completed phase detail retained outside active scans | Inactive completed phase history |
| `./patch/<context>.patch.md` or `./<context>.patch.md` | Governed active patch/review artifacts outside live phase planning | Active patch docs |
| `./patch/done/<context>.patch.md` | Completed patch artifacts retained outside active scans | Inactive completed patch history |
| `./phase-implementation-template.md` | Root helper for phased planning | Helper artifact that also exposes active phase family, planned next phase(s), activation boundary, and next checkpoint guidance for future `/phase` authoring |

> **💡 Single Source of Truth Principle:**
> - Design files (`.design.md`) define active target state and do not use a default `design/done/` surface
> - Per-chain active changelogs (`*.changelog.md`) remain the authority for current governed chain history/version state
> - `changelog/done/`, `phase/done/`, and `patch/done/` are inactive-by-default history surfaces for audit, rollback, provenance, or trace reconstruction
> - `changelog/changelog.md` records repository-level synchronization history
> - `README.md` remains overview-only, not chain authority
> - Older coordination-flavored rollout records in `TODO.md`, `phase/SUMMARY.md`, and `changelog/changelog.md` remain historical context only; current active authority stays in the active runtime rules and design docs

---

## 🔗 Integration Guide

This section defines how `design`, `changelog`, `runtime rules`, `TODO`, and governed phase-planning artifacts should be updated together.

### Document Roles

| Document | Role | Update Trigger |
|----------|------|----------------|
| `design/*.design.md` | Target behavior/specification | Requirement or policy change |
| `*.md` (root runtime rules) | Active runtime behavior | Approved design change requires runtime sync |
| `changelog/changelog.md` | Master repository-wide synchronization history | Repository-level governed sync events |
| `changelog/*.changelog.md` | Authoritative active per-chain version history | Any rule/design update with version impact |
| `changelog/done/*.changelog.md` | Inactive completed or older detailed history | History/audit/rollback/provenance/trace needs only |
| `phase/SUMMARY.md` | Governed summary/index for live phased execution | Phased implementation work needs one summary file with a phase map, source-input extraction rollup, review rollup, and global coordination |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Governed active phase-detail layer | Multi-stage execution detail under `/phase`, including design references, optional patch references, design extraction, optional patch extraction, review flow, reviewer checklist, review outcome, and execution detail |
| `phase/done/phase-NNN-*.md` | Inactive completed phase history | Completed phase detail should leave active scans but remain traceable |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Governed active patch/review artifact layer | Patch or review work that is separate from live phase planning but may feed the phase layer one-way when relevant |
| `patch/done/<context>.patch.md` | Inactive completed patch history | Completed patch artifacts should leave active review scans but remain traceable |
| `phase-implementation-template.md` | Root helper for phased planning readability | Reusable authoring support when staged execution matters, including active phase family, planned next phase(s), activation boundary, and next checkpoint guidance |
| `TODO.md` | Execution and progress tracking | Work starts/completes or task state changes |

### Startup Artifact Gate

Before meaningful governed work drifts, the repository now expects startup artifact posture to be resolved through `artifact-initiation-control.md`.

That means design / changelog / TODO / phase / patch should be explicitly resolved as:
- use existing
- create now
- ask now
- not required

Required governed companions should stay visible when the checked work shape still requires them; the live task list helps run the work, but it does not replace required design/changelog/TODO/phase/patch surfaces.

When governed design is sufficiently clear and staged execution is warranted, phase posture should resolve to `use existing` or `create now`; the phase layer may derive execution order, current child phase files, and current-phase live tasks from that governed design instead of waiting for a separate retrospective planning prompt.

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
  → update design target state
  → synchronize runtime rule wording
  → record per-chain changelog version + summary
  → record repository-level sync in changelog/changelog.md when applicable
  → update TODO pending/completed/history
  → update phase/patch companion records when in scope
  → move completed phase/patch/changelog detail to `done/` only when active scan bloat justifies inactive history separation
  → install only the 42 source-owned active runtime rules when an install gate is explicitly in scope
  → verify links, versions, active install scope, and source/runtime parity only when a runtime install gate is in scope
```


### Verification Checklist

- Design file links to the correct changelog file
- Changelog unified row maps to an existing detailed section
- Runtime rule version/header aligns with changelog current version
- README active runtime install list still contains exactly the 42 source-owned root rule files
- `phase/SUMMARY.md` exists when phased execution is used and names governing patch artifacts or explicit `none`
- `phase/SUMMARY.md` keeps the phase map, source inputs, cross-phase handoffs, TODO/changelog coordination, verification, and rollback/containment picture current
- child phase files include design references, patch references or explicit `none`, objective, entry conditions, action checklist, affected artifacts, TODO/changelog coordination, verification, closeout, exit criteria, risks/rollback notes, and next possible phases when relevant
- phase-backed closeout explains delivered work, feature/improvement, user/system impact, verification basis, and next phase state when useful
- sufficiently clear governed design can be synthesized into phase order and current-phase live tasks when staged execution is warranted
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
  → recovery-contract.md
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
  → safe-file-reading.md + safe-terminal-output.md
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
  → artifact-initiation-control.md
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
  → project-documentation-standards.md
  → strict-file-hygiene.md
  → document-consistency.md
  → README / TODO / phase / patch records
```

**What was synchronized:**
- runtime co-location was clarified as non-ownership authority
- destination files outside the current source-owned install set require owner/project scope resolution before classification or cleanup
- documentation, hygiene, and reference owners were aligned to preserve the source-owned/shared-destination/other-owner distinction

#### Example 9: Phase Closeout Feature and Impact Reporting

```text
response-closing-and-action-framing.md
  → phase-implementation.md
  → answer-presentation.md
  → accurate-communication.md
  → explanation-quality.md
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
  → artifact-initiation-control.md startup phase posture
  → phase-implementation.md execution synthesis
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
  → phase/SUMMARY.md phase map and source inputs
  → phase-NNN / phase-NNN-NN child execution files
  → current-phase live task list
  → closeout with delivered work, impact, verification, and next phase state
```

**What this gives you:**
- staged work gets a deterministic phase workspace instead of ad hoc planning drift
- sufficiently clear governed design can become phase order and current-phase live tasks when staged execution is warranted
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
<b>Reserved</b><br>
<sub>Placeholder slot for future visual asset parity</sub>
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

| Signal | Current README Meaning | Impact |
|--------|-------------------------|--------|
| Active runtime scope | 42 source-owned root rule files | Keeps install scope explicit |
| Runtime install boundary | P073, P077, P078, P079, P080, and P081 install parity were verified after explicit install gates; P081 kept the 42-rule active set and left other-owner runtime files observed-only | Avoids overclaiming source/runtime scope and protects other-owner runtime files |
| Evidence discipline | Practical proof-seeking, fact, preference/direction, factual endorsement, inference, hypothesis, uncertainty, memory, scoped non-finding, and ordinary-evidence-vs-binding-constraint boundaries stay separate | Reduces overclaim, floating recommendation, sycophantic agreement, and hallucination risk |
| Phase execution | Clear governed design can drive phase posture, order, and current-phase tasks when staged work is warranted | Reduces retrospective phase backfill |
| Completed history surfaces | `phase/done/`, `patch/done/`, and `changelog/done/` are inactive by default; `design/done/` is not a default pattern | Reduces active scan bloat without deleting governed history |
| Shared destination boundary | Co-located runtime files outside the source-owned set are not cleanup targets by default | Prevents other-owner file damage |

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
| **No Sycophancy** | Use evidence-seeking proof-aware agreement: accept user direction without factual endorsement, agree when evidence supports it, seek proof before substantial recommendations or challenges, and correct claims when evidence conflicts |
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
  <b>Version</b>: 9.80 |
  <b>Last Updated</b>: 2026-05-04 |
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
