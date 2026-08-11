# Design - Action Safety

> **Parent Rule:** [../action-safety.md](../action-safety.md)
> **Current Version:** 1.6
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/action-safety.changelog.md](../changelog/action-safety.changelog.md)

---

## Target State

`action-safety.md` is the active runtime owner for destructive/high-impact action safety, runtime topology control, emergency posture, and operational failure handling.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for functional intent verification, destructive confirmation, runtime topology control, emergency protocol, and retry/failure handling.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on former root files.

P144 refinement: topology vocabulary must distinguish operational runtime workers/jobs/entities from Claude subagents/teammates; authorized bounded destructive work follows explicit action-and-scope confirmation rather than refusal classification; public read-only lookup is evidence gathering while consequential authenticated/private, mutating, sending/publishing, payment/purchase, deployment, account/shared-state, sensitive-data, meaningful-cost, or terms-acceptance actions retain approval gates; and only the smallest safe reversible emergency containment/diagnostic action may precede full startup when delay materially increases immediate harm, followed immediately by normal governance and recovery synchronization.

P146 refinement: completed migrations and authority replacements must converge to one verified active authority. Any compatibility bridge is temporary, bounded, observable, and retirement-gated; former material may remain only as execution-disconnected quarantine or inactive history outside runtime/install/import/config/build/deployment/test discovery. Quarantine is preservation, not fallback, restoration source, authority, or deletion permission. Restoration is an explicitly approved deliberate replacement from an independently verified exact known-good source/tag/commit selected outside quarantine, followed by one-authority proof.

P073-12 refinement: `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE` is a `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE` failure profile that blocks unchanged same-role respawn while state is unresolved. `worker-routing-and-context.md` owns inspection and the reuse/steer/wait/partition/respawn lifecycle decision.

v1.5 refinement: authenticated/private access begins with a bounded capability preflight covering target and evidence objective, network reachability, tool/browser support, approved session mechanism, user authorization, consequential-action approval, and accessible bounded substitutes. A guest/login response or `401` shows that required authentication was not established for the request. A `403` shows refusal and may reflect missing authentication or insufficient authorization; it does not identify which by itself. None alone proves failure of the authenticated Product. One evidence-backed target or mechanism correction may run when it materially changes the checked mechanism; if the corrected route still lacks authorized supported capability, the failure remains `DETERMINISTIC_NON_RETRIABLE` / `NO_RETRY_UNTIL_CHANGE`. The correction must not bypass approval or secret-handling boundaries, and raw credentials, cookies, tokens, private keys, or session-state dumps must not become convenience substitutes.

P150 / v1.6 refinement: this owner must provide the canonical design-conformance architecture delta preflight for material route, service, client, adapter, queue/event transport, registry, state key, credential transport, reader/writer, fallback, or authority-owner changes. The preflight binds the active design slice, current owner/producer/state/readers/writers/consumers/dependencies/last-known-working path, proposed delta, existing-owner absorption check, security boundary, authority change, approval state, and rollback/retirement direction. Missing or ambiguous inputs remain `OBSERVE_ONLY`. A fork exists when another owner/path is introduced for an already governed role even when described as private, internal, temporary, diagnostic, adapter-shaped, compatibility-shaped, or fallback. Ordinary in-authority repair remains `REPAIR_IN_PLACE`; `ADDITIVE_EXPANSION`, explicit multi-authority mode, or authority-baseline change remains approval-gated.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Require migration/cutover closure to prove one active authority, disconnected former execution edges, retired bridges, and inactive quarantine/history.
- Keep restoration explicit, approved, exact-source-bound, replacement-only, and followed by single-authority verification; never create an automatic fallback engine.
- Require authenticated/private capability and authorization preflight before access, preserve approval and secret boundaries, allow only one discriminating evidence-backed mechanism correction, and stop unchanged retries until a named relevant state changes.
- Own the architecture delta classes and approval boundary for material architecture-bearing source mutation after execution triggers the preflight.
- Require active design and the existing architecture path to be checked before authority expansion; incomplete state remains `OBSERVE_ONLY` and ordinary in-authority repair remains proportionate.
- Treat another owner/route/transport/client/registry/state key/reader-writer/fallback for an already governed role as a fork regardless of private, internal, temporary, diagnostic, adapter, compatibility, or fallback labeling.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact 19-Rule set is selected.

Historical detail remains in changelog or execution-disconnected quarantine/provenance surfaces, never as parallel runtime authority, fallback, or normal restoration source.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.

Architecture-delta validation must confirm Case 18 keeps unresolved architecture at `OBSERVE_ONLY`, selects `REPAIR_IN_PLACE` for a bounded existing-path regression, blocks unapproved alternate owners/routes/transports/clients/keys/read-write paths/fallbacks, and permits only an exact design-backed and explicitly approved verified capability expansion or replacement with rollback/retirement direction.
