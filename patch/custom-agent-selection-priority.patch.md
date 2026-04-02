# Custom Agent Selection Priority Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md) v1.0
> **Target Rule:** [../custom-agent-selection-priority.md](../custom-agent-selection-priority.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/custom-agent-selection-priority.changelog.md](../changelog/custom-agent-selection-priority.changelog.md)

---

## 1) Context

This patch captures the introduction of a first-class rule chain for custom-agent selection priority.

Why this change matters:
- the user’s custom agents in `~/.claude/agents/` represent a deliberate specialist ecosystem
- without a clear rule, generic handling or broader fallbacks can absorb work that should go to a better-fit custom specialist
- loader/discovery problems are real, but they are a different problem from selection behavior

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../authority-and-scope.md`
- `../functional-intent-verification.md`
- `../anti-sycophancy.md`
- `../natural-professional-communication.md`

Review concern:
- the new chain should strengthen custom-agent preference without encouraging arbitrary over-delegation or pretending that undiscovered agents are usable

---

## 3) Change Items

### Change Item 1
- **Target location:** delegation behavior model
- **Change type:** additive

**Before**
```text
The RULES stack did not have one explicit owner for preferring the user’s custom specialist pool when a task clearly matched one of those agents.
```

**After**
```text
A dedicated rule now defines user custom agents as the primary specialist pool when visible and clearly better fit than generic handling or broader fallback agents.
```

### Change Item 2
- **Target location:** discovery vs selection distinction
- **Change type:** additive

**Before**
```text
Custom-agent discovery problems and custom-agent selection behavior were easy to conflate.
```

**After**
```text
The new chain explicitly distinguishes runtime discovery failures from assistant selection behavior.
```

### Change Item 3
- **Target location:** anti-pattern handling
- **Change type:** additive

**Before**
```text
Ignoring a clear custom specialist was not explicitly governed as its own anti-pattern.
```

**After**
```text
Ignoring a clear visible custom specialist and defaulting to generic handling is now an explicit anti-pattern.
```

---

## 4) Verification

- [ ] Confirm the design/runtime/changelog triad exists for the new chain
- [ ] Confirm the rule defines primary specialist-pool preference for visible user custom agents
- [ ] Confirm the rule distinguishes discovery problems from selection behavior
- [ ] Confirm the patch remains readable as a before/after governance artifact

---

## 5) Rollback Approach

If the chain causes over-delegation or boundary confusion:
- narrow the preference wording so it applies only to strong best-fit cases
- preserve the distinction between discovery and selection
- keep the triad and patch history rather than silently deleting the ownership experiment
