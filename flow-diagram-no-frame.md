# Flow Diagram Rule: No Frame / No Box

> **Current Version:** 1.2
> **Design:** [design/flow-diagram-no-frame.design.md](design/flow-diagram-no-frame.design.md) v1.2
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/flow-diagram-no-frame.changelog.md](changelog/flow-diagram-no-frame.changelog.md)

---

## Rule Statement

**Core Principle: Text diagrams must avoid decorative frames, box-drawing borders, and fragile layout characters; use simple arrows, indentation, labels, and short lines so diagrams remain readable across terminals, markdown renderers, and compacted transcripts.**

This rule owns text-flow diagram formatting. It does not require diagrams for every explanation; it only governs diagrams when a diagram is useful.

---

## Core Contract

### 1) No box/frame characters

Do not use Unicode box-drawing frames, ASCII boxes, long border lines, or decorative diagram containers.

Banned patterns include:
- Unicode box characters such as `┌`, `┐`, `└`, `┘`, `─`, `│`, `╔`, `╗`, `╚`, `╝`
- ASCII boxes using `+---+`, `|`, `.---.`, or repeated border lines
- long decorative separators inside diagram code blocks
- frames around nodes merely for visual styling

### 2) Use simple relationship markers

Allowed diagram tools:
- arrows: `→`, `↓`
- indentation for hierarchy
- short tree markers only when they do not create a box frame
- numbered lists when sequence is clearer
- labels and short text blocks instead of framed nodes

Required guidance:
- use arrows only for real sequence or dependency relationships
- keep line width short enough to survive terminal wrapping
- split complex diagrams into smaller flows
- prefer prose or ordered lists when a diagram would reduce clarity

### 3) Diagram purpose first

A diagram should clarify sequence, branching, dependency, or handoff. It should not be decorative.

Required guidance:
- introduce what the diagram shows when context matters
- keep each node label concise
- avoid repeating the same relationship already clear in nearby prose
- do not use visual complexity to compensate for unclear explanation

---

## Canonical Patterns

Step chain:

```text
User submits request
  → Validate input
  → Check authorization
  → Execute allowed action
  → Report result and verification limit
```

Vertical flow:

```text
Startup
  ↓
Load config
  ↓
Validate dependencies
  ↓
Start service
```

Decision flow:

```text
Request received
  ↓
Authorized?
  → YES: continue in scoped mode
  → NO: ask for context or refuse with path
```

Hierarchy:

```text
RULES/
  design/
  changelog/
  phase/
  patch/
```

---

## Anti-Patterns

Avoid:
- framed boxes around every step
- decorative separators as diagram structure
- wide diagrams that wrap unpredictably
- mixed box styles and arrows in one diagram
- diagrams that hide the main point behind layout
- using diagrams where a numbered list is clearer

Better behavior: use plain labels, arrows, and indentation; keep the diagram short and semantically useful.

---

## Verification Checklist

- [ ] Diagram has no Unicode or ASCII box frames.
- [ ] Diagram uses arrows/indentation only for real relationships.
- [ ] Lines are short enough to avoid fragile wrapping.
- [ ] Diagram adds clarity beyond prose.
- [ ] Complex flow is split or replaced with ordered steps.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Box/frame characters in diagrams | 0 |
| Rendering consistency | High |
| Diagram readability | High |
| Decorative diagram usage | Low |
| Line-wrap fragility | Low |

---

## Integration

Related rules:
- [answer-presentation.md](answer-presentation.md) - decides when diagrams improve scanability
- [explanation-quality.md](explanation-quality.md) - owns explanation flow and diagram placement
- [safe-terminal-output.md](safe-terminal-output.md) - keeps output readable in terminal contexts
- [document-consistency.md](document-consistency.md) - keeps labels and references consistent

---

> **Full history:** [changelog/flow-diagram-no-frame.changelog.md](changelog/flow-diagram-no-frame.changelog.md)
