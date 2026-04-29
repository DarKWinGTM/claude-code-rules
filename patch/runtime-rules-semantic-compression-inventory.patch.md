# Runtime Rules Semantic Compression Inventory Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Phase 073-08 Runtime Install Parity Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.73
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch is the pre-execution inventory for a semantic-preserving compression wave across the active root runtime rule set.

The user-selected target is Conservative/Balanced compression:
- target aggregate reduction: 35-45%
- preserve all existing capability and safety behavior
- create complete patch coverage before phase execution
- use one master inventory patch instead of one patch file per rule
- keep the compression wave source-only through P073-07 before any separate runtime install gate

P073-08 later executed that separate runtime install/parity gate by installing the 41 README-installed active runtime rule files into `~/.claude/rules/` and verifying source/runtime hash parity. P074-02 later reinforced that destination co-location does not make other project/plugin-owned runtime files part of this source-owned install set.

Scope is limited to the active root runtime rule files listed in the README install set. The governed companion surfaces remain synchronized support layers, not the primary compression scope. Shared runtime-destination files outside this source-owned set remain other-owner/out-of-scope unless their owner/project is explicitly selected or verified.

Out of compression scope unless explicitly selected later:
- `README.md`
- `TODO.md`
- `checkpoint.md`
- `phase-implementation-template.md`
- `design/**`
- `changelog/**`
- `phase/**`
- `patch/**`
- `support/**`
- `suspend/**`
- `archive/**`

---

## 2) Analysis

Risk level: High

Why the risk is high:
- the RULES set is runtime behavior, not normal prose documentation
- many repeated paragraphs exist because they protect edge cases from prior incidents
- the compression target is large enough that accidental semantic loss is plausible without traceability
- several rules are hard-boundary or safety-adjacent owner chains

Compression mode:
- Conservative for high-risk authority, safety, evidence, phase/task, and memory owners
- Balanced for lower-risk communication, presentation, style, and support owners
- aggregate target is 35-45%, not a fixed per-file quota

Dependencies:
- `../README.md`
- `../design/design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`
- all 41 active root runtime rule files listed below

Review concern:
- no required runtime behavior may move only into design/changelog/phase/patch surfaces
- duplicated wording may be removed only when an equivalent owner or preserved wording remains in runtime scope
- force words such as `must`, `never`, `confirm`, `verify`, and `ask first` must not be weakened by summarization

---

## 3) Baseline Measurement

Measured before compression on 2026-04-24.

P073-01 froze the initial pre-compression source baseline at 7,298 lines / 53,088 words / 375,828 bytes. P073-02 refreshed the then-current active pre-compression baseline before high-risk runtime rule body compression started.

| Metric | Historical P073-02 active pre-compression baseline |
|---|---:|
| Active runtime rule files | 41 |
| Total lines | 7,341 |
| Total words | 53,627 |
| Total bytes | 379,491 |
| Target aggregate line/word/byte reduction | 35-45% |

P073-02 refresh note: only RSC-009 changed relative to the P073-01 inventory baseline at that measurement point. P073-02 has now compressed the high-risk contract-owner subset source-only; later P073 compression phases remain pending and must begin from a fresh active-runtime-only re-anchor that excludes out-of-scope delegation or cleanup authority.

Baseline by file:

| Patch ID | Rule file | Lines | Words | Bytes | Risk tier | Target band |
|---|---|---:|---:|---:|---|---|
| RSC-001 | `accurate-communication.md` | 569 | 4,848 | 34,306 | High | 25-40% |
| RSC-002 | `technical-snapshot-communication.md` | 164 | 1,013 | 7,554 | Medium | 25-40% |
| RSC-003 | `response-closing-and-action-framing.md` | 167 | 1,311 | 9,278 | Medium | 25-40% |
| RSC-004 | `answer-presentation.md` | 645 | 4,931 | 32,451 | Medium | 35-50% |
| RSC-005 | `anti-mockup.md` | 5 | 15 | 186 | High | 0-10% |
| RSC-006 | `anti-sycophancy.md` | 172 | 866 | 6,287 | High | 20-35% |
| RSC-007 | `artifact-initiation-control.md` | 207 | 1,473 | 10,294 | High | 20-35% |
| RSC-008 | `authority-and-scope.md` | 180 | 1,708 | 11,830 | High | 15-30% |
| RSC-009 | `custom-agent-selection-priority.md` | 177 | 1,437 | 9,818 | Medium | 25-40% |
| RSC-010 | `dan-safe-normalization.md` | 5 | 14 | 207 | High | 0-10% |
| RSC-011 | `document-consistency.md` | 162 | 952 | 7,230 | High | 20-35% |
| RSC-012 | `document-changelog-control.md` | 5 | 18 | 238 | High | 0-10% |
| RSC-013 | `document-design-control.md` | 115 | 740 | 5,832 | High | 15-30% |
| RSC-014 | `document-patch-control.md` | 318 | 1,889 | 13,243 | High | 20-35% |
| RSC-015 | `emergency-protocol.md` | 5 | 17 | 219 | High | 0-10% |
| RSC-016 | `evidence-grounded-burden-of-proof.md` | 264 | 2,435 | 17,340 | High | 15-30% |
| RSC-017 | `explanation-quality.md` | 641 | 5,410 | 35,561 | Medium | 35-50% |
| RSC-018 | `external-verification-and-source-trust.md` | 215 | 1,315 | 9,492 | High | 20-35% |
| RSC-019 | `flow-diagram-no-frame.md` | 5 | 22 | 233 | Medium | 0-10% |
| RSC-020 | `functional-intent-verification.md` | 185 | 962 | 7,012 | High | 15-30% |
| RSC-021 | `memory-governance-and-session-boundary.md` | 240 | 1,476 | 10,385 | High | 20-35% |
| RSC-022 | `natural-professional-communication.md` | 203 | 1,345 | 9,473 | Medium | 30-45% |
| RSC-023 | `no-variable-guessing.md` | 163 | 953 | 6,768 | High | 20-35% |
| RSC-024 | `operational-failure-handling.md` | 375 | 2,606 | 19,877 | High | 20-35% |
| RSC-025 | `phase-implementation.md` | 261 | 2,273 | 15,681 | High | 15-30% |
| RSC-026 | `portable-implementation-and-hardcoding-control.md` | 248 | 1,585 | 11,940 | High | 20-35% |
| RSC-027 | `project-documentation-standards.md` | 262 | 2,420 | 18,200 | High | 15-30% |
| RSC-028 | `recovery-contract.md` | 5 | 14 | 192 | High | 0-10% |
| RSC-029 | `refusal-classification.md` | 5 | 14 | 207 | High | 0-10% |
| RSC-030 | `refusal-minimization.md` | 5 | 14 | 201 | High | 0-10% |
| RSC-031 | `runtime-topology-control.md` | 246 | 1,600 | 12,091 | High | 20-35% |
| RSC-032 | `safe-file-reading.md` | 5 | 18 | 222 | High | 0-10% |
| RSC-033 | `safe-terminal-output.md` | 5 | 18 | 234 | High | 0-10% |
| RSC-034 | `strict-file-hygiene.md` | 146 | 769 | 5,887 | High | 15-30% |
| RSC-035 | `tactical-strategic-programming.md` | 174 | 1,116 | 8,250 | Medium | 25-40% |
| RSC-036 | `todo-standards.md` | 235 | 2,051 | 13,529 | High | 15-30% |
| RSC-037 | `unified-version-control-system.md` | 5 | 15 | 231 | High | 0-10% |
| RSC-038 | `zero-hallucination.md` | 179 | 1,062 | 7,423 | High | 20-35% |
| RSC-039 | `high-signal-communication.md` | 98 | 482 | 3,293 | Medium | 25-40% |
| RSC-040 | `execution-continuity-and-mode-selection.md` | 161 | 1,560 | 10,873 | High | 20-35% |
| RSC-041 | `goal-set-review-and-priority-balance.md` | 114 | 860 | 5,923 | Medium | 25-40% |

---

## 4) High-Risk Contract Registry

These contracts are non-removable. Compression may relocate or shorten wording only when the runtime rule set still expresses the same behavior at equal strength.

| Contract ID | Contract | Must remain owned by |
|---|---|---|
| HRC-001 | Verified fact, observed local fact, inference, hypothesis, unresolved uncertainty, post-compact needs-recheck, unresolved governing basis, recalled path-matched context, and not-found-in-checked-scope remain separate claim states | `evidence-grounded-burden-of-proof.md` plus wording deferrals |
| HRC-002 | Scoped non-finding must not become global absence | `evidence-grounded-burden-of-proof.md`, `zero-hallucination.md`, `no-variable-guessing.md` |
| HRC-003 | User-directed contradiction requires contrary evidence and should challenge the claim, not the person | `anti-sycophancy.md`, `evidence-grounded-burden-of-proof.md`, `accurate-communication.md` |
| HRC-004 | Destructive delete requires explicit confirmation tied to action and scope | `functional-intent-verification.md` |
| HRC-005 | Cleanup, hygiene, isolation, worktree, or sandbox rationale is not deletion authorization | `strict-file-hygiene.md`, `functional-intent-verification.md`, `authority-and-scope.md` |
| HRC-006 | Git working state is observed local evidence only, not semantic file authority | `authority-and-scope.md`, `evidence-grounded-burden-of-proof.md`, `no-variable-guessing.md` |
| HRC-007 | Startup artifact posture is resolved before meaningful governed work drifts | `artifact-initiation-control.md`, `project-documentation-standards.md` |
| HRC-008 | Design is target-state truth, changelog is version authority, TODO is durable tracking, and built-in task list is live execution surface | `project-documentation-standards.md`, `document-design-control.md`, `todo-standards.md` |
| HRC-009 | Relevant `/phase` context must shape task creation when available | `phase-implementation.md`, `todo-standards.md` |
| HRC-010 | Future phase context may inform draft continuity but is not active execution until opened/selected | `phase-implementation.md`, `todo-standards.md` |
| HRC-011 | Implementation-critical external docs/spec/provider knowledge must be normalized into design before later work depends on it | `document-design-control.md`, `execution-continuity-and-mode-selection.md`, `phase-implementation.md`, `document-patch-control.md` |
| HRC-012 | Main RULES must not re-own exact plugin/shared-board title grammar or retired bridge/memsearch doctrine | `project-documentation-standards.md`, `authority-and-scope.md`, `memory-governance-and-session-boundary.md` |
| HRC-013 | Memory is context, not authority; path scope is primary applicability; session IDs are provenance only | `memory-governance-and-session-boundary.md`, `authority-and-scope.md`, `evidence-grounded-burden-of-proof.md` |
| HRC-014 | Runtime install remains active root runtime rule files only, excluding design/changelog/TODO/phase/patch/support/helper artifacts | `README.md`, `project-documentation-standards.md`, `strict-file-hygiene.md` |
| HRC-015 | Runtime topology mutation must inspect before mutate and additive/authority-changing expansion requires approval | `runtime-topology-control.md`, `functional-intent-verification.md` |
| HRC-016 | Operational retry budgets do not reset across tools for the same objective and deterministic failures need a real state/input/permission/policy/context change | `operational-failure-handling.md` |

---

## 5) Rule Coverage and Change Items

### RSC-001 — `accurate-communication.md`
- **Change type:** restructuring
- **Compression intent:** keep evidence-strength wording, purpose-first operational framing, direct human-readable wording, memory disclosure, and continuation wording; defer full evidence taxonomy to `evidence-grounded-burden-of-proof.md`, snapshot wording to `technical-snapshot-communication.md`, and closing/proposal wording to `response-closing-and-action-framing.md`.
- **Before:** Broad communication owner repeats detailed evidence tables, snapshot guidance, closing guidance, post-compact guidance, and several examples now owned by specialist rules.
- **After:** Shorter communication owner focused on wording quality and claim-strength expression, with explicit specialist deferrals.
- **Preserve:** HRC-001, HRC-002, HRC-003, HRC-011, HRC-013.

### RSC-002 — `technical-snapshot-communication.md`
- **Change type:** restructuring
- **Compression intent:** keep exact/partial/inferred snapshot wording and scoped local-fact boundaries; remove repeated generic evidence doctrine already owned by burden-of-proof.
- **Before:** Snapshot owner repeats broad evidence-state and communication ideas.
- **After:** Focused snapshot wording owner with compact examples.
- **Preserve:** HRC-001, HRC-002.

### RSC-003 — `response-closing-and-action-framing.md`
- **Change type:** restructuring
- **Compression intent:** keep concise synthesis, recommendation-with-reason, alternative preservation, closed-topic summary, and proposal-advisory boundaries; remove repeated execution-continuity and explanation-flow material.
- **Before:** Closing owner overlaps with explanation and presentation owners.
- **After:** Focused end-of-response/action framing owner.
- **Preserve:** HRC-003, HRC-013.

### RSC-004 — `answer-presentation.md`
- **Change type:** restructuring
- **Compression intent:** keep layout/pattern ownership, light table guidance, diagnostic snapshot layout, scope-boundary layout, and memory-status presentation; move repeated explanation mechanisms back to `explanation-quality.md` and wording semantics to `accurate-communication.md`.
- **Before:** Large pattern library repeats explanation and wording rules.
- **After:** Compact presentation owner with fewer canonical examples and clear deferrals.
- **Preserve:** HRC-001, HRC-011, HRC-013.

### RSC-005 — `anti-mockup.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal anti-mockup pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** real-system-over-mock contract.

### RSC-006 — `anti-sycophancy.md`
- **Change type:** restructuring
- **Compression intent:** keep truth-over-pleasing and claim-focused disagreement; defer detailed burden thresholds to `evidence-grounded-burden-of-proof.md`.
- **Before:** Repeats contradiction ladder and evidence threshold semantics.
- **After:** Shorter disagreement-posture owner with explicit threshold deferral.
- **Preserve:** HRC-003.

### RSC-007 — `artifact-initiation-control.md`
- **Change type:** restructuring
- **Compression intent:** keep startup posture resolution and live task-list initialization gate; shorten repeated document role definitions by deferring to `project-documentation-standards.md`.
- **Before:** Repeats role-map and task/phase behavior already owned elsewhere.
- **After:** Focused startup-gate owner.
- **Preserve:** HRC-007, HRC-008, HRC-009.

### RSC-008 — `authority-and-scope.md`
- **Change type:** restructuring
- **Compression intent:** keep precedence hierarchy, user authority, fresh-directive override, governing-basis ownership, memory deferral, and git-state authority boundary; remove repeated examples where equivalent safety owners preserve them.
- **Before:** Contains detailed overlap with file-disposal, memory, and evidence owners.
- **After:** Compact authority/precedence owner with clear deferrals.
- **Preserve:** HRC-005, HRC-006, HRC-012, HRC-013.

### RSC-009 — `custom-agent-selection-priority.md`
- **Change type:** restructuring
- **Compression intent:** keep custom-agent preference, no-forced-delegation, and reuse-before-spawn behavior; shorten repeated team/agent failure wording that belongs to `operational-failure-handling.md`.
- **Before:** Contains selection order, custom specialist preference, no-forced-delegation, and duplicate/stale-team overlap.
- **After:** Focused agent-selection owner that preserves custom specialist preference and reuse-before-spawn behavior.
- **Preserve:** custom specialist preference, no duplicate same-role spawn behavior, and no-forced-delegation.

### RSC-010 — `dan-safe-normalization.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal normalization pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** bounded intent evaluation for jailbreak-style wrappers.

### RSC-011 — `document-consistency.md`
- **Change type:** restructuring
- **Compression intent:** keep cross-reference validation, source/destination/local reference distinction, and dependent-reference checks; defer absence semantics to burden-of-proof and local lookup mechanics to no-variable-guessing.
- **Before:** Repeats anti-guessing and disposal semantics.
- **After:** Focused reference-consistency owner.
- **Preserve:** HRC-002, HRC-006, HRC-014.

### RSC-012 — `document-changelog-control.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal changelog-control pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** changelog as version authority.

### RSC-013 — `document-design-control.md`
- **Change type:** restructuring
- **Compression intent:** keep design active-state body and doc-derived knowledge capture; shorten general project document-role material by deferring to `project-documentation-standards.md`.
- **Before:** Focused but can still reduce repeated integration prose.
- **After:** Compact design-owner rule.
- **Preserve:** HRC-008, HRC-011.

### RSC-014 — `document-patch-control.md`
- **Change type:** restructuring
- **Compression intent:** keep patch identity, required metadata, before/after representation, external-requirement basis, and phase/patch boundary; shorten repeated phase semantics by deferring to `phase-implementation.md`.
- **Before:** Long patch contract repeats repository role model and phase behavior.
- **After:** Focused patch owner.
- **Preserve:** HRC-008, HRC-011.

### RSC-015 — `emergency-protocol.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal emergency pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** emergency boundary behavior.

### RSC-016 — `evidence-grounded-burden-of-proof.md`
- **Change type:** restructuring
- **Compression intent:** keep canonical taxonomy and threshold matrix; reduce examples and repeated application prose only.
- **Before:** Core owner contains many examples and repeated operational application details.
- **After:** Still canonical evidence owner, shorter but equally explicit.
- **Preserve:** HRC-001, HRC-002, HRC-003, HRC-006, HRC-013.

### RSC-017 — `explanation-quality.md`
- **Change type:** restructuring
- **Compression intent:** keep explanation flow, layered reasoning, easy explanation, table/list guidance, scope boundaries, and post-compact explanation; move layout examples to `answer-presentation.md` and claim-strength wording to `accurate-communication.md`.
- **Before:** Very large explanation owner with repeated canonical examples.
- **After:** Focused explanation-flow owner with fewer examples.
- **Preserve:** HRC-001, HRC-011, HRC-013.

### RSC-018 — `external-verification-and-source-trust.md`
- **Change type:** restructuring
- **Compression intent:** keep source trust ladder, corroboration, conflict honesty, and recommendation-before-verification contract; reduce repeated zero-hallucination phrasing.
- **Before:** Repeats factual-discipline language.
- **After:** Focused external verification owner.
- **Preserve:** external source verification and conflict honesty.

### RSC-019 — `flow-diagram-no-frame.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal no-frame diagram pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** no framed/boxed diagram rule.

### RSC-020 — `functional-intent-verification.md`
- **Change type:** restructuring
- **Compression intent:** keep clarify-before-execute, destructive confirmation, scope/impact, cleanup-is-not-authorization, and safe defaults; shorten repeated disposal authority details by deferring to `authority-and-scope.md` and `strict-file-hygiene.md`.
- **Before:** Repeats file-disposal and evidence logic.
- **After:** Focused intent/confirmation owner.
- **Preserve:** HRC-004, HRC-005.

### RSC-021 — `memory-governance-and-session-boundary.md`
- **Change type:** restructuring
- **Compression intent:** keep memory taxonomy, path-primary applicability, session provenance, root index, archive inactive, optional recall boundary; reduce repeated evidence/communication wording.
- **Before:** Repeats memory disclosure and burden concepts.
- **After:** Focused memory governance owner.
- **Preserve:** HRC-012, HRC-013.

### RSC-022 — `natural-professional-communication.md`
- **Change type:** restructuring
- **Compression intent:** keep natural tone/register, purpose-before-detail, easy-explanation register, and low-drama communication; defer explanation mechanics to `explanation-quality.md` and layout to `answer-presentation.md`.
- **Before:** Repeats purpose-first and easy-explanation rules.
- **After:** Focused tone/register owner.
- **Preserve:** user-facing clarity and Thai/plain-language register behavior.

### RSC-023 — `no-variable-guessing.md`
- **Change type:** restructuring
- **Compression intent:** keep read-before-reference, local-scope declaration, scoped not-found language, and configuration/path/symbol lookup mechanics; defer broader evidence semantics to burden-of-proof.
- **Before:** Repeats negative-evidence and contradiction rules.
- **After:** Focused local lookup owner.
- **Preserve:** HRC-002, HRC-006.

### RSC-024 — `operational-failure-handling.md`
- **Change type:** restructuring
- **Compression intent:** keep failure classes, retry budgets, same-objective aggregate cap, profile model, cooldown honesty, and stop/escalation behavior; reduce repeated recovery/refusal wording.
- **Before:** Long operational owner includes many examples and repeated boundaries.
- **After:** Focused failure/retry owner.
- **Preserve:** HRC-016.

### RSC-025 — `phase-implementation.md`
- **Change type:** restructuring
- **Compression intent:** keep phase identity, `/phase` file model, phase-to-patch linkage, current-phase task linkage, doc-derived constraint carry-through, and future-phase draft boundary; shorten repository role repetition by deferring to `project-documentation-standards.md`.
- **Before:** Repeats TODO/project documentation behavior.
- **After:** Focused phase semantics owner.
- **Preserve:** HRC-009, HRC-010, HRC-011.

### RSC-026 — `portable-implementation-and-hardcoding-control.md`
- **Change type:** restructuring
- **Compression intent:** keep portable-core, late-binding, local-fact separation, adapter boundary, canonical notation, and public onboarding guidance; shorten repeated reference-role text by deferring to `document-consistency.md`.
- **Before:** Repeats install/reference notation semantics.
- **After:** Focused portability owner.
- **Preserve:** HRC-014 and anti-hardcoding behavior.

### RSC-027 — `project-documentation-standards.md`
- **Change type:** restructuring
- **Compression intent:** keep repository document-role model, startup gate integration, runtime install boundary, public onboarding portability, master-surface consultation, and patch/phase/TODO role split; shorten per-artifact details owned by individual document rules.
- **Before:** Large repository map repeats phase, patch, TODO, design details.
- **After:** Compact repository-level role map and integration owner.
- **Preserve:** HRC-007, HRC-008, HRC-011, HRC-014.

### RSC-028 — `recovery-contract.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal recovery pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** recovery path requirement.

### RSC-029 — `refusal-classification.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal refusal classification pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** refusal taxonomy boundary.

### RSC-030 — `refusal-minimization.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal refusal minimization pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** avoid false refusals while keeping hard boundaries.

### RSC-031 — `runtime-topology-control.md`
- **Change type:** restructuring
- **Compression intent:** keep topology posture, delta classes, authority baseline, inspect-before-mutate, additive expansion approval, and multi-authority exception; reduce repeated failure/intent confirmation text by deferring to operational and functional-intent owners.
- **Before:** Repeats approval and failure handling.
- **After:** Focused topology owner.
- **Preserve:** HRC-015.

### RSC-032 — `safe-file-reading.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal safe-file-reading pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** plan-before-read boundary via active design/runtime contract.

### RSC-033 — `safe-terminal-output.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal safe-terminal-output pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** plan-before-execute output safety boundary.

### RSC-034 — `strict-file-hygiene.md`
- **Change type:** restructuring
- **Compression intent:** keep existing-file-first, no-junk-docs, governed-startup exception, version-suffix hygiene, portable-artifact hygiene, and no deletion authority; reduce repeated disposal-confirmation details owned by functional intent and authority.
- **Before:** Repeats cleanup/deletion semantics in several places.
- **After:** Focused creation/duplication hygiene owner.
- **Preserve:** HRC-005, HRC-014.

### RSC-035 — `tactical-strategic-programming.md`
- **Change type:** restructuring
- **Compression intent:** keep tactical entry, strategic target, convergence path, bounded tactical scope, and no permanent tactical drift; shorten repeated artifact-map and trigger prose.
- **Before:** Strategy owner includes long tables and examples.
- **After:** Compact tactical/strategic owner.
- **Preserve:** tactical work must have strategic target and convergence path.

### RSC-036 — `todo-standards.md`
- **Change type:** restructuring
- **Compression intent:** keep durable-vs-live distinction, task-list triggers, current-phase-first task shaping, same-objective retention, future-phase boundary, and task language/register behavior; reduce repeated phase/project role definitions.
- **Before:** Repeats phase and project documentation behavior.
- **After:** Focused TODO/live task-list owner.
- **Preserve:** HRC-008, HRC-009, HRC-010.

### RSC-037 — `unified-version-control-system.md`
- **Change type:** preserve/minimal
- **Compression intent:** no meaningful compression because the runtime file is already minimal.
- **Before:** Minimal version-control pointer.
- **After:** Keep or only normalize metadata if needed.
- **Preserve:** unified version-control boundary.

### RSC-038 — `zero-hallucination.md`
- **Change type:** restructuring
- **Compression intent:** keep verify-first factual discipline and source-priority behavior; defer detailed taxonomy and contradiction thresholds to `evidence-grounded-burden-of-proof.md`.
- **Before:** Repeats claim-state and negative-evidence details.
- **After:** Focused factual-discipline owner.
- **Preserve:** HRC-001, HRC-002.

### RSC-039 — `high-signal-communication.md`
- **Change type:** restructuring
- **Compression intent:** keep high-signal pruning gate and never-remove-required-content boundary; shorten examples and repeated communication-owner references.
- **Before:** Supplemental owner repeats active owner warnings.
- **After:** Compact pruning-only rule.
- **Preserve:** required content must not be stripped.

### RSC-040 — `execution-continuity-and-mode-selection.md`
- **Change type:** restructuring
- **Compression intent:** keep discussion-vs-execution mode, startup-gate-first boundary, continuous-execution default, active next-work discovery, capture-before-continue, and stop-gate rules; reduce repeated task/phase/TODO role descriptions.
- **Before:** Repeats task/phase/documentation details.
- **After:** Focused execution-mode owner.
- **Preserve:** HRC-007, HRC-009, HRC-011.

### RSC-041 — `goal-set-review-and-priority-balance.md`
- **Change type:** restructuring
- **Compression intent:** keep full goal-set visibility, priority balance, structure-first behavior, and anti-fixation; reduce repeated trigger tables/examples.
- **Before:** Medium-length goal owner with repeated rationale.
- **After:** Compact priority-balance owner.
- **Preserve:** current subtask must not crowd out remaining primary goals.

---

## 6) Master Drift Change Items

### MD-001 — `phase/SUMMARY.md` latest-phase metadata
- **Target location:** `phase/SUMMARY.md` document control and context
- **Change type:** replacement

**Before**
```text
Status says active summary is synchronized through phase 069, while the summary already contains phase 070-072 entries.
```

**After**
```text
Status and context should reflect the new phase 073 inventory wave once opened, and the phase-family count should match the indexed families.
```

### MD-002 — `design/design.md` master version alignment
- **Target location:** `design/design.md` document control
- **Change type:** replacement

**Before**
```text
design/design.md metadata shows Current Version 9.61 while changelog/changelog.md shows Current Version 9.65.
```

**After**
```text
Master design metadata should be synchronized in the source-only phase-073 opening wave before compression uses it as the active inventory baseline.
```

### MD-003 — source-only runtime boundary
- **Target location:** `README.md`, patch inventory, phase 073 files
- **Change type:** additive

**Before**
```text
Prior waves often bundled runtime install after source updates.
```

**After**
```text
Phase 073 compression inventory and source refactor stay source-only first. Runtime install into ~/.claude/rules/ is intentionally deferred to a separate later gate.
```

---

## 7) Verification

- [x] Patch inventory covers all 41 active root runtime rule files from the README install list.
- [x] Baseline line/word/byte counts are recorded before compression.
- [x] Every runtime rule has a patch item ID from `RSC-001` through `RSC-041`.
- [x] High-risk contracts are identified before compression begins.
- [x] Known master drift candidates are patch-covered before phase execution.
- [x] Source-only boundary is explicit.
- [x] P073-02 verified that compressed high-risk owner behavior still satisfies the applicable high-risk contracts.
- [x] P073-02 measured touched high-risk owner reduction: 9.9% lines, 23.1% words, and 21.7% bytes.
- [x] P073-02 verified source-only boundaries: no runtime install, no `CLAUDE.md` edits, and no plugin/package surface edits.
- [x] P073-03 re-anchored the compression scope to active root runtime rule files only and recorded the current 41-file baseline: 7,141 lines / 50,141 words / 356,403 bytes.
- [x] P073-04 compressed seven evidence/safety/operations runtime owners source-only, reducing the touched set from 13,424 to 10,854 words while preserving semantic anchors and active-runtime/source-only boundaries.
- [x] P073-05 compressed eleven communication/presentation/strategy/support runtime owners source-only, reducing the touched set from 20,565 to 12,032 words while preserving semantic anchors and active-runtime/source-only boundaries.
- [x] P073-06 synchronized repository-level governed source records for completed runtime compression through P073-05 while keeping per-rule changelog mass bumps, final aggregate audit, and runtime install deferred.
- [x] P073-07 verified final active-runtime semantic parity for all 41 README-installed root rule files.
- [x] P073-07 measured final active-runtime state at 4,051 lines / 31,316 words / 231,675 bytes.
- [x] P073-07 confirmed aggregate reductions: 44.82% lines / 41.60% words / 38.95% bytes from the P073-02 patch baseline, and 43.27% lines / 37.54% words / 35.00% bytes from the P073-03 runtime-only re-anchor baseline.
- [x] P073-07 verified governed source-record consistency and kept runtime install deferred; no runtime install, `CLAUDE.md` edit, plugin/hook/custom-agent edit, release, or push was claimed.
- [x] P073-08 installed the 41 README-installed active runtime rule files into `~/.claude/rules/`.
- [x] P073-08 verified runtime parity: 41 active source files, 41 active destination copies, no missing source files, no missing destination files, no hash mismatches, and `PARITY_PASS True`.
- [x] P073-08 recorded destination markdown files outside the active install set as observed-only and untouched in the checked scope; that observation was not a complete ownership inventory and did not authorize cleanup.
- [x] P073-08 kept the boundary narrow: no `CLAUDE.md` edit, no plugin/hook/custom-agent edit, no deletion cleanup, no release, and no push.
- [x] P074-02 golden scenario added: a plugin/project-owned runtime rule may exist in `~/.claude/rules/` outside the Main RULES 41-file install set; it remains out of scope and is not a cleanup target unless its owning project/plugin is explicitly selected or verified.

---

## 8) Rollback Approach

If semantic compression appears to weaken behavior:
- stop at the current phase boundary
- keep this inventory patch as the baseline coverage artifact
- restore the affected rule file from pre-compression source state
- preserve the owner map and high-risk registry for a narrower Conservative retry
- do not proceed to runtime install until source semantic parity passes

If post-install active runtime parity fails:
- recopy only the affected README-installed active runtime rule file from source
- rerun source/runtime hash parity before claiming runtime alignment
- keep cleanup of destination files outside the active install set outside this patch unless separately owner-scoped and authorized; runtime-destination co-location alone is not proof of Main RULES ownership

If the aggregate reduction target conflicts with semantic preservation:
- semantic preservation wins
- report the lower safe reduction instead of forcing the 35-45% target
- ask the user before moving into aggressive compression
