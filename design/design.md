# Claude Code Rules System

## Master Design Document

> **Parent Scope:** RULES System Design
> **Current Version:** 2.3
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-22)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## I. Document Control

### I.1 Version Information

**Current Version:** 2.3
**Last Updated:** 2026-02-22
**Status:** Active

### I.2 Change Summary

| Version | Date | Summary | Session ID |
|---------|------|---------|------------|
| 2.3 | 2026-02-22 | **Added consolidated best-practices section (P2 closure)** - Introduced unified operational best practices to reduce guidance fragmentation and standardized cross-document execution behavior | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 2.2 | 2026-02-22 | **Completed WS-1 + WS-4 runtime/design/changelog/TODO synchronization batch** - Harmonized deterministic precedence, policy coherence, and governance structure across active runtime rules and master docs | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 2.1 | 2026-02-22 | **Synchronized metadata and fixed runtime/design version drift** - Raised master design header/session baseline to 2.1 for the active synchronization phase | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 2.0 | 2026-02-22 | **Logged Cross-Rule Determinism and Performance Hardening Survey** - Added repository-wide issue themes, workstreams, and design-first execution gate (design/changelog/TODO before implementation) | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 1.9 | 2026-02-21 | **Recorded Documentation Integrity Audit Findings (Review Gate)** - Logged verified defects in master docs for review-first remediation (no root-rule activation in this phase) | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 1.8 | 2026-02-21 | **Designed False-Refusal Minimization Suite** - Added principle-first architecture for authorized pentest workflows (`refusal-minimization`, `refusal-classification`, `recovery-contract`, `dan-safe-normalization`) | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 1.7 | 2026-02-01 | **Integrated Document Patch Control** - Added to rule hierarchy and inventory | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.6 | 2026-01-21 | Removed Session ID from TODO standard | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.5 | 2026-01-21 | Added todo-standards and project-documentation-standards to rule hierarchy, updated rule count to 16 | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.4 | 2026-01-21 | Removed Session ID from Rules File Standard Template (not required for rules files) | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.3 | 2026-01-21 | Restructured to systematic format (Sections I-VIII), added Rules File Standard Template | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.2 | 2026-01-20 | Updated document-changelog-control to v4.3 | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.1 | 2026-01-20 | Added Image Generation Framework | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.0 | 2026-01-16 | Initial master design | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |

---

## II. Overview

### II.1 Purpose

**Claude Code Rules System** is a rule set that governs AI behavior in Claude Code to:

- Maintain accuracy and reliability
- Prevent common failures (hallucination, terminal flooding, etc.)
- Preserve user control over AI behavior
- Enforce high-quality operating standards

### II.2 Rule Categories

| Category | Rules | Purpose |
|----------|-------|---------|
| **Accuracy & Truth** | zero-hallucination, anti-sycophancy, no-variable-guessing | Verified and reliable information |
| **Output Safety** | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | Output flood prevention |
| **User Control** | authority-and-scope, emergency-protocol, functional-intent-verification, refusal-classification, recovery-contract | Preserve user authority and recovery paths |
| **Adversarial Workflow** | refusal-minimization, dan-safe-normalization | Reduce false refusals in authorized pentest workflows |
| **Quality** | document-consistency, document-changelog-control, document-design-control, document-patch-control, anti-mockup, strict-file-hygiene | Output quality and governance |


### II.3 Scope

This design document covers:
- Architecture of the rules system
- Standards for creating rules files
- Version tracking and changelog integration
- Quality metrics and compliance
- Usage guidelines

### II.4 Language Governance (Mandatory)

- All design documents under `design/*.md` must be English-only.
- All changelog documents under `changelog/*.md` must be English-only.
- All runtime rule files at the repository root (`*.md` rules excluding `README.md` and `TODO.md`) must be English-only.
- Language normalization must preserve document structure, links, versions, and original meaning.

---

## III. Architecture

### III.1 Rule Hierarchy

```
Claude Code Rules System
  ├─ Core Rules (Must Follow)
  │   ├─ authority-and-scope
  │   ├─ zero-hallucination
  │   └─ anti-sycophancy
  │
  ├─ Safety Rules (Prevent Harm)
  │   ├─ safe-file-reading
  │   ├─ safe-terminal-output
  │   ├─ emergency-protocol
  │   └─ functional-intent-verification
  │
  ├─ Adversarial Workflow Rules (Authorized Pentest)
  │   ├─ refusal-minimization
  │   ├─ refusal-classification
  │   ├─ recovery-contract
  │   └─ dan-safe-normalization
  │
  ├─ Quality Rules (Improve Output)
  │   ├─ document-consistency
  │   ├─ document-changelog-control (v4.4)
  │   ├─ document-design-control (v1.6)
  │   ├─ document-patch-control (v1.0)
  │   ├─ todo-standards (v2.0)
  │   ├─ project-documentation-standards
  │   ├─ anti-mockup
  │   ├─ no-variable-guessing
  │   ├─ flow-diagram-no-frame
  │   └─ strict-file-hygiene
  │
  └─ [Future Rules]
```

### III.2 Rule Dependencies

```
authority-and-scope (Foundation)
  ↓
zero-hallucination + anti-sycophancy (Truth)
  ↓
no-variable-guessing + document-consistency (Verification)
  ↓
safe-file-reading + safe-terminal-output (Safety)
  ↓
refusal-minimization + dan-safe-normalization (Authorized Adversarial Workflow)
  ↓
refusal-classification + recovery-contract (Decision + Recovery Contract)
  ↓
emergency-protocol + functional-intent-verification (Execution)
```

### III.3 Authorized Adversarial Workflow Decision Model

**Design Goal:** Reduce false refusal in authorized pentest workflows without weakening hard safety boundaries.

**Decision Output Contract:**

| Output | Meaning | Typical Action |
|--------|---------|----------------|
| `ALLOW_EXECUTE` | Request authorized and sufficiently scoped | Execute normally |
| `ALLOW_CONSTRAINED` | Request allowed with safety constraints | Execute in bounded mode |
| `NEED_CONTEXT` | Missing authorization/scope context | Ask for required context |
| `REFUSE_WITH_PATH` | Hard boundary violated or clearly prohibited | Refuse + provide recovery path |

**Refusal Class Contract:**

| Class | Meaning | User Override |
|-------|---------|---------------|
| `HARD_BLOCK` | Non-negotiable safety/legal/platform boundary | ❌ Not overridable |
| `SOFT_BLOCK` | Risk/ambiguity that can be reduced with constraints | ✅ User may choose constrained path |
| `WORKFLOW_BLOCK` | Missing process artifacts (scope/proof/context) | ✅ User can provide context to proceed |

**Execution Flow:**

```text
User Request
  ↓
Hard boundary check
  → Violation: REFUSE_WITH_PATH + HARD_BLOCK
  ↓
Authorization & scope completeness check
  → Missing artifacts: NEED_CONTEXT + WORKFLOW_BLOCK
  ↓
DAN-safe normalization (convert ambiguous/jailbreak framing → bounded authorized intent)
  ↓
Risk/constraint evaluation
  → Bounded execution needed: ALLOW_CONSTRAINED (+ optional SOFT_BLOCK rationale)
  → Fully authorized and bounded: ALLOW_EXECUTE
```

**Authority Rule:**
- User has decision priority for `SOFT_BLOCK` and `WORKFLOW_BLOCK` resolution paths
- AI enforces `HARD_BLOCK` without override

---

## IV. Sub-Rule Index

### IV.1 Current Rules (21 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | anti-mockup.md | anti-mockup.design.md | Real systems over mocks |
| 2 | anti-sycophancy.md | anti-sycophancy.design.md | Truth over pleasing |
| 3 | authority-and-scope.md | authority-and-scope.design.md | User authority |
| 4 | dan-safe-normalization.md | dan-safe-normalization.design.md | Normalize DAN-style prompts into authorized bounded tasks |
| 5 | document-consistency.md | document-consistency.design.md | Cross-reference validation |
| 6 | document-changelog-control.md | document-changelog-control.design.md v4.4 | Version tracking standard |
| 7 | document-design-control.md | document-design-control.design.md v1.6 | Design document standards |
| 8 | document-patch-control.md | document-patch-control.design.md v1.0 | Tactical implementation plans |
| 9 | emergency-protocol.md | emergency-protocol.design.md | Emergency response |
| 10 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md | No box diagrams |
| 11 | functional-intent-verification.md | functional-intent-verification.design.md | Verify before destructive |
| 12 | no-variable-guessing.md | no-variable-guessing.design.md | Read before reference |
| 13 | project-documentation-standards.md | project-documentation-standards.design.md | Project documentation standards |
| 14 | recovery-contract.md | recovery-contract.design.md | Standard recovery contract for blocked decisions |
| 15 | refusal-classification.md | refusal-classification.design.md | HARD/SOFT/WORKFLOW refusal taxonomy |
| 16 | refusal-minimization.md | refusal-minimization.design.md | Reduce false refusals while preserving hard boundaries |
| 17 | safe-file-reading.md | safe-file-reading.design.md | UOLF for file reading |
| 18 | safe-terminal-output.md | safe-terminal-output.design.md | UOLF for terminal output |
| 19 | strict-file-hygiene.md | strict-file-hygiene.design.md | Prevent non-functional files |
| 20 | todo-standards.md | todo-standards.design.md v2.0 | Simple TODO lists |
| 21 | zero-hallucination.md | zero-hallucination.design.md | Verified information only |

### IV.2 Reserved for Future Rules

| Category | Potential Rules | Purpose |
|----------|-----------------|---------|
| Security | code-review-security | Security review automation |
| Performance | performance-optimization | Performance guidelines |
| Testing | test-coverage | Testing requirements |
| Documentation | auto-documentation | Documentation generation |

---

## V. Standards & Frameworks

### V.1 Memory Hierarchy (Official Spec)

> **Source:** [Memory Management - Claude Code Docs](https://code.claude.com/docs/en/memory)

Claude Code uses a **hierarchical memory system** with 5 levels:

| Memory Type | Location | Purpose | Shared With | Priority |
|-------------|----------|---------|-------------|----------|
| **Enterprise Policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br>Linux: `/etc/claude-code/CLAUDE.md`<br>Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions | All users | 1 (Highest) |
| **Project Memory** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared instructions | Team via git | 2 |
| **Project Rules** | `./.claude/rules/*.md` | Modular, topic-specific rules | Team via git | 2 |
| **User Memory** | `~/.claude/CLAUDE.md` | Personal preferences | Just you (all projects) | 3 |
| **Project Local** | `./CLAUDE.local.md` | Personal project-specific | Just you (current project) | 4 (Lowest) |

### V.2 .claude/rules/ Format (Official Spec)

> **Source:** [Memory Management - Modular Rules](https://code.claude.com/docs/en/memory#modular-rules-with-clauderules)

**Directory Structure:**
```
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Topic-specific rules
│       ├── frontend/       # Subdirectories allowed
│       │   ├── react.md
│       │   └── styles.md
│       └── backend/
│           ├── api.md
│           └── database.md
```

**Path-Specific Rules (YAML frontmatter):**
```yaml
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
```

### V.3 Memory Import Syntax (Official Spec)

> **Source:** [Memory Management - CLAUDE.md Imports](https://code.claude.com/docs/en/memory#claudemd-imports)

**Syntax:** `@path/to/import`

```markdown
See @README for project overview and @package.json for available commands.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

**Features:**
- Relative and absolute paths supported
- Max recursion: 5 hops
- Can import from user home: `@~/.claude/my-project-instructions.md`

### V.4 Subagents Format (Official Spec)

> **Source:** [Subagents - Claude Code Docs](https://code.claude.com/docs/en/sub-agents)

**YAML Frontmatter:**
```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer...
```

**Scope:**
| Location | Priority |
|----------|----------|
| `--agents` CLI flag | 1 (highest) |
| `.claude/agents/` | 2 |
| `~/.claude/agents/` | 3 |
| Plugin's `agents/` | 4 (lowest) |

### V.5 Shared Frameworks

**UOLF (Universal Output Limit Framework)**
- Used by: safe-file-reading, safe-terminal-output
- MAX_OUTPUT_CHARS = 5000 (hard limit)
- Double limit: `<command> | head -100 | head -c 5000`

**Evidence-Based Framework**
- Used by: zero-hallucination, anti-sycophancy, no-variable-guessing
- Verify before stating claims
- Acknowledge uncertainty when unsure

**User Authority Framework**
- Used by: authority-and-scope, emergency-protocol, functional-intent-verification
- Priority: User > Safety > Rules > Defaults

---

## VI. Standard File Templates

### VI.1 Rules File Template (`.md`)
**Location:** Project Root (e.g., `anti-mockup.md`)
**Mandatory Structure:**
```markdown
# [Rule Name]

> **Current Version:** X.Y
> **Design:** [file.design.md](design/file.design.md) vX.Y

## Rule Statement
**Core Principle:** [One-line summary]

[Content...]

---

> Full history: [changelog/file.changelog.md](changelog/file.changelog.md)
```

### VI.2 Design Document Template (`.design.md`)
**Location:** `design/` directory (e.g., `design/anti-mockup.design.md`)
**Mandatory Structure:**
```markdown
# [Design Name]

## 0) Document Control
> **Parent Scope:** [System/Project Name]
> **Current Version:** X.Y
> **Session:** [UUID] (YYYY-MM-DD)

---

[Design Content Sections...]

---

> Full history: [changelog/file.changelog.md](../changelog/file.changelog.md)
```

### VI.3 Changelog File Template (`.changelog.md`)
**Location:** `changelog/` directory (e.g., `changelog/anti-mockup.changelog.md`)
**Mandatory Structure:**
```markdown
# Changelog - [Rule Name]

> **Parent Document:** [file.design.md](../design/file.design.md)

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[Headline](#Lx)** | [UUID] |
| | | Summary: ... | |

[Detailed Version Sections...]
```

### VI.4 Header Requirements (MANDATORY)

| Element | Required | Format |
|---------|----------|--------|
| **Current Version** | ✅ Yes | `> **Current Version:** X.X` |
| **Design Link** | Optional | `**Design:** [file.design.md](design/file.design.md) vX.X` |

### VI.5 Content Sections

**Rules files should include:**

1. **Rule Statement** - Core principle
2. **Core Requirements** - Mandatory actions
3. **Examples** - ✅ Correct/❌ Incorrect patterns
4. **Quality Metrics** - Measurable targets
5. **Integration** - Related rules

### VI.6 PROHIBITED Elements

| Element | Why Prohibited | Correct Alternative |
|---------|----------------|---------------------|
| **Version Table** | Version history belongs in changelog | Use changelog link |
| **Placeholders** | Violates changelog rules | Use real data or omit |
| **Mixed Formats** | Breaks consistency | Follow this template |

### VI.7 Changelog Integration

**Rules files MUST:**

1. **Link to changelog** (at end):
   ```markdown
   > Full history: [changelog/rule-name.changelog.md](changelog/rule-name.changelog.md)
   ```

2. **NOT have Version table** in rules file:
   - ❌ WRONG: Version table in rules file
   - ✅ RIGHT: Version table ONLY in changelog file

3. **Changelog file format:**
   - changelog/rule-name.changelog.md = Full history with detailed sections
   - changelog/changelog.md = Master changelog (for entire project)

### VI.8 Examples

**✅ Correct Rules File:**

```markdown
# Document Changelog Control

> **Current Version:** 4.3

## Rule Statement

Core Principle: Every document must have traceable version history with real session IDs.

---

[Content...]

---

> Full history: [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)
```

**❌ Incorrect Rules File:**

```markdown
# Some Rule

## Rule Statement
...

---

## Version  ← WRONG: Remove this table
| Version | Date | Notes |
| 1.0 | 2026-01-21 | Initial |
```

---

## VII. Quality Metrics

### VII.1 System-Wide Metrics

| Metric | Target | Rules Involved |
|--------|--------|----------------|
| Accuracy | 100% | zero-hallucination, anti-sycophancy |
| User Authority | Preserved | authority-and-scope, emergency-protocol, refusal-classification, recovery-contract |
| Output Safety | ≤ 5000 chars | safe-file-reading, safe-terminal-output |
| Verification | Default | no-variable-guessing, document-consistency |
| Transparency | 100% | anti-mockup |
| False Refusal Rate (Authorized Pentest) | Minimized with hard-boundary preservation | refusal-minimization, dan-safe-normalization |
| Decision Contract Coverage | 100% decision mapped to output class | refusal-classification, recovery-contract |
| Document Consistency | 100% | document-*, flow-diagram-no-frame |

### VII.2 Compliance Rate

- **Constitutional Compliance**: 100% (No exceptions)
- **User Override Respect**: 100%
- **Evidence-Based**: Default behavior
- **Hallucination**: 0%
- **Template Compliance**: 100% (all rules follow standard template)

---

## VIII. Creating New Rules

### VIII.1 Step-by-Step Process

**Step 1: Create Design Document**
```bash
touch design/[rule-name].design.md
```

**Step 2: Create Rules File**
```bash
touch [rule-name].md
```

**Step 3: Create Changelog**
```bash
touch changelog/[rule-name].changelog.md
```

**Step 4: Add to Master Design**
- Update Sub-Rule Index (Section IV)
- Update Rule Hierarchy (Section III)
- Add to Rule Categories (Section II)

**Step 5: Update README**
- Add rule to rules list
- Update documentation

### VIII.2 Rules File Template

```markdown
# [Rule Name]

> **Current Version:** 1.0
> **Session:** [UUID] (YYYY-MM-DD)

## Rule Statement

**Core Principle:** [One-line principle]

**Design:** [rule-name.design.md](design/rule-name.design.md) v1.0

This rule ensures...

---

## Core Requirements

### 1. [Category]

**Required Actions:**
- [Action 1]
- [Action 2]

---

## Examples

### ✅ Correct

[Example of correct usage]

### ❌ Incorrect

[Example of incorrect usage]

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| [Metric 1] | [Target] |

---

## Integration

Related Rules:
- [rule-1.md](rule-1.md)
- [rule-2.md](rule-2.md)

---

> Full history: [changelog/rule-name.changelog.md](changelog/rule-name.changelog.md)
```

### VIII.3 Checklist for New Rules

- [ ] Create `[rule-name].md` following standard template
- [ ] Create `[rule-name].design.md` with design details
- [ ] Create `changelog/[rule-name].changelog.md` for version tracking
- [ ] Add to master design (Section IV: Sub-Rule Index)
- [ ] Update rule hierarchy if needed
- [ ] Define quality metrics
- [ ] Specify related rules
- [ ] Update README.md
- [ ] Test rule with real scenarios
- [ ] Document examples

### VIII.4 Consolidated Best Practices (Operational Baseline)

To reduce guidance fragmentation, use this single baseline across design, runtime rules, changelog, and TODO workflows.

1. **Design-first synchronization path**
   - Apply updates in this order:
     - `design` target state
     - runtime rule wording
     - changelog traceability
     - TODO status/history
     - final verification pass

2. **Verification-first claims policy**
   - Do not claim completion/fix status without verified evidence.
   - Match statement confidence to validation depth (implemented, partially verified, fully verified).

3. **Deterministic blocked-response contract**
   - For blocked/non-execute outcomes, keep response schema explicit and stable:
     - `decision_output`
     - `refusal_class` (if applicable)
     - `reason`
     - actionable `next_step` / recovery path

4. **Cross-document integrity discipline**
   - Keep version references and links synchronized across `design`, runtime rules, and `changelog`.
   - Avoid duplicate or conflicting authority statements across related documents.

5. **TODO governance discipline**
   - Keep pending section pending-only.
   - Move completed work out of pending and record closure in history with clear scope.

6. **Closure verification checklist**
   - Before closing any documentation task, verify:
     - changed sections are synchronized,
     - links resolve,
     - version markers match authoritative changelog,
     - TODO dashboard totals reflect real pending state.

---

## IX. Documentation Integrity Audit Findings (Review Gate)

### IX.1 Phase Scope Decision (Design-Only)

- Current phase is **design/changelog governance hardening**
- **Root rule materialization is intentionally deferred**
- This section records verified defects as **potential improvement defects** pending review before any remediation TODO breakdown

### IX.2 Verified Findings (Audit Snapshot, then Log-Phase Status)

Snapshot basis: full integrity audits executed in this session before master-doc log updates.

**Critical (Snapshot)**
- `design/design.md:705` had broken history link path (`changelog/changelog.md` from within `design/` should use `../changelog/changelog.md`)
  - **Log-phase status:** Fixed in this pass (`../changelog/changelog.md`)

**Major (Snapshot)**
- `design/design.md:171-195` indexes 21 active rules including 4 root rules not materialized in current phase (`refusal-minimization.md`, `refusal-classification.md`, `recovery-contract.md`, `dan-safe-normalization.md`)
  - **Log-phase status:** Open (phase decision pending review)
- `changelog/changelog.md:464,531,532,581,614` had broken relative links in legacy version sections
  - **Log-phase status:** Normalized in this pass; re-audit still required before closure
- `changelog/changelog.md:13,18,24,30,36,39,45,53,61,67,74,84,93,100,108,115,122,126,129` uses `#version-XX` jump targets that may not resolve against actual heading slugs
  - **Log-phase status:** Open (anchor policy decision pending)
- `changelog/changelog.md:36` has a `2.4` row in unified table without a corresponding detailed `## Version 2.4` section
  - **Log-phase status:** Open
- `TODO.md:13` pending-count mismatch was previously flagged during snapshot pass
  - **Log-phase status:** Revalidated on 2026-02-22: counts are consistent (`142/158`, pending `16`); item reclassified to structure-only drift
- `TODO.md:414-427,439-452` completed blocks appear under pending area, causing status ambiguity
  - **Log-phase status:** Open

**Minor (Snapshot)**
- `TODO.md:455,459` duplicate heading `Future Enhancements`
  - **Log-phase status:** Open
- `design/design.md:402,419` duplicate subsection numbering (`### VI.7`) in template area
  - **Log-phase status:** Open
- `changelog/changelog.md:432,464,504,572,621,653,687` detailed version sections are out of descending order compared to unified table
  - **Log-phase status:** Open
- `document-changelog-control.md:5` and `todo-standards.md:5` still use placeholder-style session metadata text
  - **Log-phase status:** Open
- `changelog/accurate-communication.changelog.md:5,13,17,26,48` uses placeholder/non-real session markers (`(current session)`, `(current)`)
  - **Log-phase status:** Open

### IX.3 Improvement Candidate Statement

All findings in Section IX.2 are currently tracked as **candidate defects awaiting adjustment**.
They are intentionally recorded in design/main changelog first, then promoted into implementation TODO items after review approval.

### IX.4 Next-Step Contract (Post-Review)

1. Review and approve findings in master docs
2. Create explicit remediation TODO items from approved findings
3. Apply fixes in dependency order (metadata integrity -> links -> inventory/totals)
4. Re-run integrity audit and log closure in changelog

---

## X. Integration Examples

### X.1 Rule Enhancement Workflow

This example demonstrates the lifecycle of enhancing a rule from Draft to Completed.

**Scenario:** Updating `document-consistency.md` to v1.1.

1.  **Drafting (Patch):**
    *   Create `patches/consistency-rule-enhancement.patch.md`.
    *   Define Context, Analysis, and Implementation Plan.
    *   Status: `Draft`.

2.  **Implementation:**
    *   Update `document-consistency.md` (add content).
    *   Update `changelog/document-consistency.changelog.md` (add version entry).
    *   Mark Patch as `Status: In Progress` in TODO.md.

3.  **Verification:**
    *   Verify `document-consistency.md` matches design.
    *   Verify changelog link works.

4.  **Completion:**
    *   Update Patch status to `Completed` in the file.
    *   Move Patch to `patches/` if not already there.
    *   Update TODO.md to mark task as completed.

### X.2 File Relationship Diagram

```
[Design Layer]              [Rules Layer]               [History Layer]
design/*.design.md   ---->  *.md                 ---->  changelog/*.changelog.md
(Specifications)            (Active Rules)              (Version Tracking)
      ^                           ^                           ^
      |                           |                           |
      +---------------------------+---------------------------+
                                  |
                          [Tactical Layer]
                          patches/*.patch.md
                          (Transition Plans)
```

---

## XI. Cross-Rule Determinism and Performance Hardening Program (Design-First Gate)

### XI.1 Program Scope and Boundary

**Scope:**
- Runtime rules at repository root (`*.md`, excluding `README.md` and `TODO.md`)
- Design documents under `design/*.md`
- Changelog documents under `changelog/*.md`
- Governance tracker at `TODO.md`

**Boundary for this phase:**
- This phase records issues, defines workstreams, and sets execution order
- Runtime behavior implementation is intentionally deferred until design approval

### XI.2 Verified Issue Themes (Survey Consolidation)

| Theme ID | Theme | Verified Signals | Primary Risk |
|----------|-------|------------------|--------------|
| TH-1 | Deterministic precedence and terminology conflicts | Priority/tie-break ambiguity across authority, documentation, and refusal contracts | Non-deterministic policy decisions under overlap |
| TH-2 | Session metadata and version-reference integrity drift | Placeholder/non-real session markers and stale cross-rule version references | Reduced auditability and trust in governance lineage |
| TH-3 | Master documentation integrity defects | Anchor target mismatch, missing detailed section coverage, ordering/numbering drift, duplicate headings | Navigation breakage and weak traceability |
| TH-4 | Verification policy overlap and performance overhead | Parallel “verify-first” requirements across multiple rules with no shared trigger model | Repeated tool calls, latency increase, response bloat |
| TH-5 | Blocked-response contract overlap | Multiple rules require similar blocked output fields without a compact unified schema | Token expansion and inconsistent blocked-mode formatting |
| TH-6 | TODO governance drift | Pending section includes completed blocks; duplicate heading structure | Planning ambiguity and operational noise |

### XI.3 Workstream Model (Design/Changelog/TODO before Runtime Implementation)

#### WS-1: Deterministic Precedence and Terms Contract
- **Objective:** Define an explicit conflict-resolution matrix and normalize ambiguous terms.
- **Scope Files:** `authority-and-scope.md`, `design/design.md`, `refusal-minimization.md`, `refusal-classification.md`, `recovery-contract.md`.
- **Acceptance Criteria:**
  - A single precedence matrix exists and is referenced by dependent rules.
  - Terms such as “higher-level safety policies” and blocked class/output coupling are explicitly defined.
  - No unresolved tie-break ambiguity remains in authoritative docs.
- **Dependencies:** None (foundational).

#### WS-2: Metadata and Version Integrity Normalization
- **Objective:** Remove placeholder session metadata and align cross-rule version references.
- **Scope Files:** `document-changelog-control.md`, `todo-standards.md`, `changelog/accurate-communication.changelog.md`, and all files with stale related-rule version pointers.
- **Acceptance Criteria:**
  - No placeholder/non-real session markers in active governance docs.
  - Referenced current versions match actual target documents.
  - Session metadata policy is applied consistently.
- **Dependencies:** WS-1 recommended first.

#### WS-3: Master Changelog Structural Integrity Repair
- **Objective:** Ensure unified table and detailed sections are fully coherent.
- **Scope Files:** `changelog/changelog.md`.
- **Acceptance Criteria:**
  - Every unified-table version row has resolvable detailed section coverage.
  - Anchor strategy is consistent and link-valid.
  - Detailed sections follow one ordering policy.
- **Dependencies:** WS-2.

#### WS-4: Documentation Policy Coherence (Design/Changelog/TODO/Patch)
- **Objective:** Resolve cross-rule contradictions on document structure, pair behavior, language policy, and patch naming.
- **Scope Files:** `document-design-control.md`, `document-changelog-control.md`, `project-documentation-standards.md`, `document-patch-control.md`, `design/design.md`.
- **Acceptance Criteria:**
  - Design/changelog pair behavior is internally consistent.
  - Patch naming standard is singular (`*.patch.md`) across all references.
  - Language governance has one authoritative rule path without contradiction.
- **Dependencies:** WS-1, WS-2.

#### WS-5: Verification and Output Overhead Consolidation
- **Objective:** Keep safety guarantees while reducing duplicated verification/output obligations.
- **Scope Files:** `zero-hallucination.md`, `anti-sycophancy.md`, `no-variable-guessing.md`, `document-consistency.md`, `safe-file-reading.md`, `safe-terminal-output.md`, refusal suite.
- **Acceptance Criteria:**
  - A shared verification trigger model is defined (not duplicated as parallel mandates).
  - Blocked-response schema is compact and non-redundant.
  - Response-length control guidance is deterministic across safety rules.
- **Dependencies:** WS-1, WS-4.

#### WS-6: TODO Governance Alignment
- **Objective:** Align `TODO.md` structure with selected TODO standard behavior.
- **Scope Files:** `TODO.md`, `todo-standards.md`.
- **Acceptance Criteria:**
  - Pending area contains pending tasks only.
  - Duplicate heading drift is removed.
  - Chosen TODO format policy (simple or extended) is explicitly codified and consistently applied.
- **Dependencies:** WS-4.

### XI.4 Execution Order (Phase Contract)

1. **Design hardening first:** WS-1 and WS-4
2. **Changelog integrity next:** WS-2 and WS-3
3. **TODO normalization after standards lock:** WS-6
4. **Performance consolidation specification:** WS-5 design only in this phase
5. **Runtime implementation:** deferred until design/changelog/TODO approval is complete

### XI.5 Status Note (Count Revalidation)

- Prior snapshot flagged pending-count mismatch in `TODO.md`.
- Revalidation on 2026-02-22 confirms numeric dashboard consistency (`142/158`, pending `16`).
- Remaining TODO defects are structural (placement/heading/format coherence), not numeric totals.

---

## Appendix A: Image Generation Framework

### A.1 Purpose

Framework for generating visual assets for the Claude Code Rules System.
Designed with A-PIRO (Automatic Prompt Intent Recognition Optimization).

### A.2 File Structure

```
/home/node/workplace/AWCLOUD/CLAUDE/claude-code-image-generator/
├── image_gen.py                 # Image generation script
├── image.prompt.design.md       # 140 prompts (10 styles × 14 rules)
├── generated_images/            # Generated images
└── design.md                     # Master design reference
```

### A.3 10 Visual Styles

| # | Style Name | Concept | Best For |
|---|------------|---------|----------|
| 1 | Citadel | Architectural fortress | Technical documentation |
| 2 | World Tree | Organic bioluminescent tree | Natural presentation |
| 3 | Orrery | Steampunk mechanical clock | Precision/engineering |
| 4 | Geometric | Abstract 3D shapes | Minimalist/modern |
| 5 | Constellation | Cosmic star patterns | Inspirational/cosmic |
| 6 | Zen Garden | Japanese balanced garden | Balance/harmony |
| 7 | Wardens | Cyberpunk guardians | Team/guardian narrative |
| 8 | Blueprint | Holographic HUD interface | Technical/HUD |
| 9 | Neural | Brain-like command center | AI/brain metaphor |
| 10 | Alchemical | Surrealist transformation | Artistic/philosophical |

### A.4 Generation Command

> **See:** [image.prompt.design.md](image.prompt.design.md) for complete prompt specifications

```bash
# Generate image for specific rule
python image_gen.py "<prompt>" --doc <rule-name>.md --aspect-ratio 16:9 --image-size 2K
```

---

> Full history: [changelog/changelog.md](../changelog/changelog.md)
