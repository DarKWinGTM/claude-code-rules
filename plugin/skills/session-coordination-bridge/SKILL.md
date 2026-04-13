---
name: session-coordination-bridge
description: Coordinate work across Claude Code sessions through the shared task board first, optional recall second, and optional peer signaling when available.
version: 1.0.0
---

# Session Coordination Bridge

This skill is the active operator and support surface for the optional `claude-code-rules` plugin companion.

It complements the canonical RULES authorities at:
- `../../../shared-execution-coordination.md`
- `../../../todo-standards.md`
- `../../../phase-implementation.md`
- `../../../memory-governance-and-session-boundary.md`
- `../../../execution-continuity-and-mode-selection.md`

This skill exists to help an operator or maintainer:
- coordinate work across separate Claude Code sessions without collapsing them into one context
- use the shared task list as the live coordination board
- keep semantic truth in phase/TODO/design/checked implementation state rather than in the task list alone
- detect optional recall or peer tooling before relying on it
- remap request-layer work into the receiving session's own execution structure
- keep sync-back and no-clear-by-default behavior explicit

---

## When to use this skill

Use this skill when you need to:
- send work from one session to another through the shared board
- receive a shared-board request and continue it safely
- decide what belongs in the board, in phase/TODO, or in memory
- check whether memsearch is actually available before trying to use it
- check whether `claude-peers-mcp` or another peer-signaling layer is actually available before treating it like an active dependency
- keep task naming, request/held/blocked state, and sync-back behavior consistent

Do not use this skill when:
- the work is fully local to one session and no coordination layer is needed
- the user only needs normal implementation help rather than cross-session coordination help
- the real problem is semantic design or architecture inside the repo rather than session coordination workflow

---

## Coordination stack

Use this stack in order of authority and dependency:

1. **Shared task list**
   - live execution-coordination board
   - who owns what, what is blocked, what is requested, what is done

2. **Phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state**
   - semantic truth for what the work means
   - source of the next real unfinished slice

3. **Native memory**
   - continuity support only
   - never outranks checked execution surfaces

4. **memsearch or similar recall extension**
   - optional recall accelerator only
   - check availability first
   - fall back immediately if unavailable or probe fails

5. **`claude-peers-mcp` or similar peer signaling**
   - optional live coordination channel only
   - useful for direct signaling when available
   - never the only required path

พูดง่าย ๆ คือ board คือ state, phase/TODO/design/code คือ truth, memory คือ context, memsearch คือ optional recall boost, และ peer signaling คือ optional live bus.

---

## Default operator flow

1. identify the coordination mode:
   - send work
   - receive work
   - sync back progress
   - inspect board state
2. inspect the shared task list first
3. inspect the active phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state when meaning is still unclear
4. use native memory if it helps continuity
5. use memsearch only after checking availability and only when extra recall detail is still materially useful
6. use peer signaling only when it is available and materially improves the current handoff or unblock step
7. remap accepted work into the receiving session's own execution structure
8. sync the result back into the board and durable surfaces

---

## Quick rules

- task list first for coordination
- stronger execution surfaces first for semantic truth
- availability-first for optional tooling
- immediate fallback when optional tooling is absent
- request layer and execution layer are not the same thing
- receiving-side phase ownership stays with the receiver
- do not clear the board by default while the same objective is still active
- sync back completed or blocked state instead of leaving the board stale

---

## Support-doc map

- [overview.md](overview.md)
- [capability-detection.md](capability-detection.md)
- [coordination-flow.md](coordination-flow.md)
- [request-contract.md](request-contract.md)
- [examples.md](examples.md)

---

## Maintainer guidance

When extending this skill:
- keep root RULES as the semantic authority
- keep this skill as an operator bridge, not a second governance stack
- prefer support docs for heavier guidance instead of bloating `SKILL.md`
- do not turn optional tooling into required infrastructure
- do not let peer messaging replace shared-board history or checked execution surfaces

### Artifact taxonomy
- root RULES docs = semantic authority
- `plugin/` = unified Rules-owned plugin package
- `plugin/skills/session-coordination-bridge/` = operator bridge and support docs inside that package
- `plugin/hooks/` + `plugin/scripts/` = compact lifecycle reinforcement inside the same package

---

## Quality gate

Before accepting the coordination behavior as good enough, confirm:
- the board still acts as coordination, not semantic truth
- the receiving session can tell what the request means without guessing
- request-layer naming is distinct from receiving-side execution naming
- optional tooling was checked before use rather than assumed
- fallback remains immediate when optional tooling is absent
- sync-back behavior is visible enough that another session can continue safely
