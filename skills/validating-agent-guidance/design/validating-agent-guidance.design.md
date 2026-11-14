# Validating Agent Guidance Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.0
> **Full history:** [../changelog/validating-agent-guidance.changelog.md](../changelog/validating-agent-guidance.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Evaluate whether an actual instruction draft supports its intended decisions, including the nearest case that should not trigger it. Keep instruction clarity, source/package validity, synthetic interpretation and measured benefit separate.

## Procedure Contract

Input is the selected instruction change, existing owner, intended outcome, allowed evaluation channels and relevant proof. State expected decisions before choosing the smallest allowed and stop/near-miss cases.

Capture a practical baseline without inventing a failure when it already succeeds. Test the complete final draft and necessary reader context, not an isolated sentence or earlier version. Use a fresh context only when authorized and useful; another channel does not bypass a restriction. Refine demonstrated ambiguity and rerun affected cases.

For history-based lessons, [history discovery](../references/history-discovery.md) owns bounded intake, speaker/provenance, accepted/rejected dispositions, trace entailment and comparison with current guidance. The entrypoint does not reproduce that procedure or require history mining for ordinary draft review.

Output binds the draft, expected/actual decisions, baseline, allowed channel, source checks, remaining ambiguity and proof limits. Distinguish queued acceptance, application, installation and discovery using the supported mechanism.

## Invariants and Failure Boundaries

- A request, concern, correctly handled precaution or assistant proposal does not prove an earlier failure or accepted lesson.
- Repeated summaries of one event do not establish recurrence. Candidate claims and changes must follow from their own evidence.
- Existing coverage is an absorption point for a distinct useful procedure, not permission for duplicate authority or automatic rejection of enrichment.
- When evaluation is unavailable or prohibited, name the source-review limit and preserve any explicitly required unresolved gate.
- Synthetic interpretation is not causal improvement, live behavior or measured user benefit. A queued change is not a landed file.

## Ownership and Development

This Skill owns guidance evaluation and provenance-bound lesson extraction, not permission to publish, install or bypass a protected writer. The parent library owns source-first maintenance and deployment boundaries; this local chain records its target and history without absorbing private evidence or installed-library records.

## Verification

Use existing Skill-library checks for metadata, local version/link alignment, portability and written validation/history contracts. Behavioral changes need proportionate paired allowed/near-miss cases against the actual draft and permitted context. The initial governance addition preserves operational text and the history reference; metadata checks do not establish a new behavioral improvement.
