# Safe I/O (File Reading + Terminal Output)
> **Current Version:** 1.10
> **Design:** [design/safe-io.design.md](design/safe-io.design.md) v1.10
> **Session:** 8176a2ea-c50d-48aa-9367-d0328016f821
> **Full history:** [changelog/safe-io.changelog.md](changelog/safe-io.changelog.md)

## Rule Statement

**Core Principle: Read/capture the smallest useful scope without flooding context or hiding failures. Verify paths, start governed chains at their compact parent, and narrow or route a material aggregate burst before further raw absorption. Oversized entrypoints need preservation-first maintenance, not deletion.**

## Bounded File Intake

Prefer `Read` for known files and search tools for paths/symbols; Bash reading only when dedicated tools do not fit or shell output is requested. Verify existence/source authority before local claims. Large source uses targeted `offset`/`limit`; report partial scope. Logs/maps/SVG/HTML/unknown JSON/generated/minified/base64/binary-like files use bounded previews/search, not raw full reads unless exact content is necessary. On tool-limit overflow narrow ranges/search rather than repeat full reads.

For large, unknown or untrusted evidence, choose input byte, individual-record size and retained-result bounds before decoding, parsing or materializing it. Stream bounded windows and cap/reject oversized records before parse; account for decoded expansion. Output truncation is not a memory bound; count-only limits do not cap record bytes or decoded expansion. Use a fixed byte watermark for concurrently appended logs; report skipped records, byte limits and partial coverage. If the available format/tool cannot honor these bounds, stop for a narrower artifact or supported bounded mechanism rather than load everything. Known small files and exact bounded reads stay direct. These intake bounds do not authorize Product/runtime resource policy, cgroup/container changes or a new runner.

## Aggregate Burst Gate

Before broad intake define the factual question, likely owner and raw-content versus filtered-result need. A worker-fit burst has one decisive high-risk signal or two moderate signals: repo-wide search plus follow-up reads, multiple authority surfaces, parent plus multiple shards, mixed code/docs/output, dense documents, noisy tests/builds/logs or repeated post-compact offset/reread churn.

Narrow first; if the burst remains, invoke [worker-routing-and-context.md](worker-routing-and-context.md)'s net-benefit/topology gate before “one more” raw read. Detection is not automatic delegation. Known bounded files, exact edit/verification ranges, final anchors, tight interactive sequence, high overlap, unavailable tooling or explicit direction may justify direct handling; state a narrow exception only when a beneficial unresolved burst remains. This owner controls capture/detection, routing controls workers/briefs/permissions/handoffs.

## Parent-first Governed Reading

Read the declared active design/changelog parent for authority/shape/map before opening the selected flat sibling or same-stem child. Do not infer a subfolder from filename or absorb all shards. Report parent/child checked scope; design children are active target truth, not automatically history. Open `changelog/done/` only through active reference or history/audit/rollback/provenance need. Keep observed example, extracted doctrine, selected target and verified equivalence distinct under [document-governance.md](document-governance.md).

If active entrypoint size/failed reads/compact thrash blocks useful intake, inspect only enough current state for [document-integrity.md](document-integrity.md)'s lossless rollover. Resume at compact active entry; retained history stays reference-driven.

## Commands and Temporary Output

Use direct low-output tools when sufficient. Before high-output shell/log/build/search/HTTP work choose deterministic line/character caps, capture/filter strategy and session-unique temporary output or an existing project-owned output root under its contract. Never dump unknown recursive output, bodies, generated/minified/binary/base64 into the conversation.

Temporary captures are run artifacts, not the default home for reusable tool/test implementation; [coding-discipline.md](coding-discipline.md) owns that lifecycle. Avoid ordinary stray repo-local debug artifacts without excluding legitimate source tools or governed test fixtures.

Keep command, exit status, material stderr and failure summary visible. Disclose truncation/partial scope and persisted output location; caps are not verification and cannot hide a failure. Prefer focused reruns/searches over blind expansion; cross-file/multi-pass output passes the aggregate gate. Temporary cleanup is permitted; repo-file removal still needs [action-safety.md](action-safety.md)'s destructive confirmation.

## Boundaries

No whole-system claim from bounded excerpts, late routing after raw flood, parent/map bypass, repeated unbounded reads or silent output loss. [evidence-discipline.md](evidence-discipline.md) governs claim scope; document and safety owners preserve authority/history/approval while this contract keeps I/O responsive.
