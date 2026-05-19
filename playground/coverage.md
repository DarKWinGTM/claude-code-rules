# Playground Coverage Matrix

## Goal

This file proves that the playground baseline covers all 18 active runtime rules through grounded scenario families.

---

## Scenario family map

| Scenario family | Primary purpose | Governing rules |
|---|---|---|
| Authority collision resolver | Resolve conflicting instructions, stale framing, and authority order safely | `authority-and-scope.md`, `evidence-discipline.md`, `accurate-communication.md`, `execution-and-goal-frame.md`, `memory-governance-and-session-boundary.md` |
| Evidence-calibrated diagnosis | Separate symptom, evidence, hypothesis, and scoped non-findings | `evidence-discipline.md`, `accurate-communication.md`, `communication-register.md`, `explanation-and-presentation.md`, `safe-io.md` |
| Safe refusal and recovery | Normalize risky/underspecified asks and keep a safe recovery path | `refusal-and-recovery.md`, `authority-and-scope.md`, `evidence-discipline.md`, `action-safety.md`, `communication-register.md` |
| Destructive action and topology gate | Stop unsafe deletion, overwrite, topology drift, and bad retry loops | `action-safety.md`, `document-integrity.md`, `evidence-discipline.md`, `authority-and-scope.md`, `accurate-communication.md` |
| Communication and presentation calibration | Keep responses natural, evidence-calibrated, and role-aware | `communication-register.md`, `accurate-communication.md`, `explanation-and-presentation.md`, `audience-surface-disclosure-control.md` |
| Audience-safe disclosure split | Separate direct-user transparency from public/operator-safe disclosure | `audience-surface-disclosure-control.md`, `accurate-communication.md`, `communication-register.md`, `evidence-discipline.md` |
| Coding change with verification discipline | Keep code maintainable and completion claims matched to proof | `coding-discipline.md`, `evidence-discipline.md`, `accurate-communication.md`, `portable-implementation-and-hardcoding-control.md` |
| Execution continuity and worker routing | Keep work moving safely while routing broad evidence to the smallest effective lane | `execution-and-goal-frame.md`, `worker-routing-and-context.md`, `phase-todo-artifact.md`, `safe-io.md`, `accurate-communication.md` |
| Governed artifact lifecycle | Open, sync, shard, compact, and preserve governed docs correctly | `phase-todo-artifact.md`, `document-governance.md`, `document-integrity.md`, `safe-io.md`, `authority-and-scope.md` |
| External, memory, and portability boundary | Keep external facts current, memory scoped, and shared artifacts portable | `external-verification-and-source-trust.md`, `memory-governance-and-session-boundary.md`, `portable-implementation-and-hardcoding-control.md`, `evidence-discipline.md`, `document-governance.md`, `document-integrity.md` |

---

## Active runtime rule coverage

| Runtime rule file | Covered by scenario families |
|---|---|
| `accurate-communication.md` | authority collision resolver; evidence-calibrated diagnosis; destructive action and topology gate; communication and presentation calibration; audience-safe disclosure split; coding change with verification discipline; execution continuity and worker routing |
| `action-safety.md` | safe refusal and recovery; destructive action and topology gate |
| `audience-surface-disclosure-control.md` | communication and presentation calibration; audience-safe disclosure split |
| `authority-and-scope.md` | authority collision resolver; safe refusal and recovery; destructive action and topology gate; governed artifact lifecycle |
| `coding-discipline.md` | coding change with verification discipline |
| `communication-register.md` | evidence-calibrated diagnosis; safe refusal and recovery; communication and presentation calibration; audience-safe disclosure split |
| `document-governance.md` | governed artifact lifecycle; external, memory, and portability boundary |
| `document-integrity.md` | destructive action and topology gate; governed artifact lifecycle; external, memory, and portability boundary |
| `evidence-discipline.md` | authority collision resolver; evidence-calibrated diagnosis; safe refusal and recovery; destructive action and topology gate; audience-safe disclosure split; coding change with verification discipline; external, memory, and portability boundary |
| `execution-and-goal-frame.md` | authority collision resolver; execution continuity and worker routing |
| `explanation-and-presentation.md` | evidence-calibrated diagnosis; communication and presentation calibration |
| `external-verification-and-source-trust.md` | external, memory, and portability boundary |
| `memory-governance-and-session-boundary.md` | authority collision resolver; external, memory, and portability boundary |
| `phase-todo-artifact.md` | execution continuity and worker routing; governed artifact lifecycle |
| `portable-implementation-and-hardcoding-control.md` | coding change with verification discipline; external, memory, and portability boundary |
| `refusal-and-recovery.md` | safe refusal and recovery |
| `safe-io.md` | evidence-calibrated diagnosis; execution continuity and worker routing; governed artifact lifecycle |
| `worker-routing-and-context.md` | execution continuity and worker routing |

---

## Coverage result

Coverage outcome for the baseline playground:
- all 18 active runtime rules are mapped to at least one scenario family
- several rules intentionally appear in more than one family because the same owner shapes behavior across several situations
- the matrix is rule-grounded, not capability-invented
