# Evidence-First Counter-Analysis and Retraction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed — verified and released in v10.59
> **Target Design:** [../design/design.md](../design/design.md) v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

v10.58 made Claude more proactive in non-trivial design, but a checked conversation pattern showed that Claude could still accept a user's false current-system premise, praise a broader replacement route, design downstream architecture, and only reverse position after the user independently discovered contrary evidence.

## 2) Analysis

Risk: High for project-specific architecture. A valid goal can be routed into destructive or wasteful expansion when the premise about current ownership, sibling roles, or completed scope is not checked first. Reflexive disagreement is also wrong; the correction must be evidence-shaped.

Target behavior:

```text
valid goal + checkable premise
→ inspect current ownership/dependencies/completed baseline
→ supported: agree at checked strength and complete design
→ false: preserve goal, correct premise, explain consequence, recommend supported route
→ incomplete: run/select discriminating check
→ prior recommendation disproved: retract and re-anchor explicitly
```

## 3) Change Items

### ECA-001 - Premise-before-expansion gate
- **Target:** `../execution-and-goal-frame.md` and triad.
- **Before:** concern/claim/path separation exists, but material expansion can still inherit an unchecked current-system premise.
- **After:** separate outcome, premise, path, and action; inspect ownership, sibling roles, readers/writers, state, dependencies, and completed verification before broader endorsement.

### ECA-002 - Completed-baseline protection and counter-analysis
- **Target:** `../execution-and-goal-frame.md` and triad.
- **Before:** a clean broader analogy can reopen verified narrow work without evidence that its gate is defective.
- **After:** checked completed scope remains active; false-premise routes are interrupted before downstream design; broader architecture must be evidence-earned and carry material obligations.

### ECA-003 - Evidence-shaped agreement
- **Target:** `../communication-register.md` and triad.
- **Before:** truth-over-pleasing exists, but agreement-shaped factual/quality wording and passive reversal remain under-specified.
- **After:** allowed-direction acceptance, factual confirmation, and best-route endorsement stay distinct; supported agreement remains allowed without artificial dissent.

### ECA-004 - Explicit recommendation retraction
- **Target:** `../communication-register.md` and triad.
- **Before:** Claude may silently switch position or say the user was right after contrary evidence appears.
- **After:** withdraw/revise the recommendation, name the failed premise and contrary evidence, state the corrected route, and keep the remaining gate visible.

### ECA-005 - Scenario projection
- **Target:** Cases 14, 17, and 05 plus `playground/matrix.md`.
- **After:** false, supported, incomplete, completed-baseline, and invalidated-assistant-recommendation branches are inspectable without a new scenario family.

## 4) Verification

Candidate checks:
- execution triad aligns at `1.30`; communication triad aligns at `1.25`;
- focused static checks find premise-before-expansion, completed-baseline, counter-analysis, and explicit-retraction contracts;
- Cases 14/17/05 cover all acceptance branches;
- no unsupported `you are right` behavior or forced disagreement remains;
- the other 17 Runtime Rules remain unchanged for this patch's scope.

Candidate semantics, scenarios, canonical/root installation, annotated `v10.59` tag, GitHub Release identity, and fresh-public-tag checks pass.

## 5) Rollback Approach

Before publication, revert only this patch's two triads and scenario projections. Preserve rollover/history artifacts. After publication, use a later corrective release; never force-move the public tag.
