# RULES Diagram Companion Pattern Implementation Plan

> **Status:** Superseded implementation plan. This worktree record preserves the old direction only as historical context.
>
> **For agentic workers:** Do **not** execute this file as current truth. The active doctrine moved to a dedicated `diagram/` visual lane and withdrew the fragmented companion baseline.

## Original goal

The earlier goal was to add governed-docs support for RULES design-lane diagram companions so the plugin could classify, render, preview, and review diagram companion shards without creating a new artifact family or moving diagram authority out of `design/**`.

## Why this plan is no longer active

The revised doctrine now requires:
- a dedicated `diagram/` visual lane
- `diagram/STRUCTURE.md` as the top-level visual anchor
- integrated subject diagrams by default under `diagram/<subject>.design.md`
- split only when visual complexity genuinely justifies it
- tooling/plugin behavior to stay downstream of the doctrine rather than defining it

That means the old assumptions below are no longer acceptable as active implementation truth:
- every diagram lives in `design/**`
- same-stem per-topic design companions are the baseline
- diagram split should track design-shard boundaries
- governed-docs should be implemented first and let doctrine follow later

## Current replacement basis

Use this design file instead when shaping future implementation work:
- `docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md`

## Historical note

This file is retained only so the earlier attempted direction stays traceable during rollback/revision work. It is a provenance artifact, not an active plan.
