# Session Coordination Bridge Overview

This skill supports one practical coordination model for multi-session Claude Code work.

## Layer model

Shared task list
- live coordination board
- holds request, ownership, blocker, handoff, and completion state

Phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state
- semantic truth for what the work means
- source of the next real unfinished slice

Memory
- continuity support only
- useful when it matches the current path and still fits the current objective

memsearch
- optional recall accelerator
- never assume it exists
- use only after availability is checked

`claude-peers-mcp`
- optional live signaling layer
- useful for direct cross-session messaging when available
- not required for the baseline coordination model

## Core boundary

The board is not the source of truth for architecture or meaning.
It is the source of truth for coordination state.

พูดง่าย ๆ คือ board บอกว่าใครทำอะไรอยู่ แต่ไม่ได้แทน design, phase, TODO, หรือ code state.

## Why this skill exists

Without a support surface like this, the operator can drift into three bad patterns:
- assuming optional tooling exists because it existed in another session or machine
- treating request-layer task titles as if they were already the receiver's execution structure
- clearing or replacing the board too aggressively and losing coordination continuity

## What this skill should improve

- cleaner handoff intake
- clearer request titles
- better receiving-side remap behavior
- safer optional-tool detection
- cleaner sync-back after progress or completion
