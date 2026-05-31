# Phase 003 - Define topic-list and choice flow

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 003
> **Status:** Completed
> **Design References:** [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Define the analysis UX so the capsule presents proposed improvement topics first and asks for user choice second.

## Why this phase exists

The user explicitly requested a list-first / choice-after pattern rather than immediate RULES changes or automatic topic expansion.

## Action points

- [x] define the first output layer as a topic list
- [x] define the second output layer as choice-based expansion
- [x] define topic-family coverage for the first design packet
- [x] keep direct RULES edits out of scope for this flow
- [x] define language-aware presentation for headings, descriptions, summaries, and choice prompts
- [x] preserve canonical technical identifiers in exact form
- [x] define interactive presentation configuration modes
- [x] define output-mode precedence
- [x] require each listed topic to explain purpose, behavior impact, high-level mechanism, and expected output before choice

## Verification

- list-first behavior is explicit
- choice-second behavior is explicit
- no auto-selection path is implied
- unchosen topics remain collapsed by default
- user-facing explanation follows the user's active working language where practical
- interactive output modes are explicit
- listed topics explain purpose, behavior impact, high-level mechanism, and expected output before choice
- identifiers and exact anchors are not loosely translated

## Exit criteria

- the interaction contract is precise enough for future skill/plugin implementation without ambiguity
