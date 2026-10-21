# Operation Outcome Reconciliation and Bounded Input

> **Current Version:** 1.0
> **Session:** 8176a2ea-c50d-48aa-9367-d0328016f821
> **Status:** active
> **Created At:** 2026-10-21T14:40:02Z
> **Creation Evidence:** direct creator event in session 8176a2ea-c50d-48aa-9367-d0328016f821
> **Target Design:** [Action Safety](../design/action-safety.design.md) v1.8; [Safe I/O](../design/safe-io.design.md) v1.10
> **Full history:** [v10.75](../changelog/changelog/v10.75-operation-outcome-and-bounded-input.changelog.md)

## Context

The user selected two bounded refinements, source-root implementation, installation into the existing user runtime target, governed sync, Git push and release. Prior analysis did not establish five novel defects; these are selected preventive contracts, not historical-incident fixes. The active inventory remains nineteen Runtime Rules.

## Analysis

Action Safety already classifies failures but does not explicitly separate an unknown side-effect outcome from a known-no-effect transient. Safe I/O bounds displayed intake/output but does not explicitly require bounding oversized evidence before parsing or whole-input allocation. Existing owners absorb both changes. User-scope Skill extractions use a separately managed owner and are excluded from this release payload.

## Change Items

### Unknown operation outcome before replay (additive)

**Targets:** `action-safety.md`, Part D; its existing design/changelog triad.

**Before/current anchor:** Part D begins `Classify before retry; apply a matching case profile before generic defaults.` The classification and budget tables follow without an explicit unknown-outcome gate.

**After/target insertion before the classification table:**

```text
An unknown outcome after dispatch is not a known-no-effect failure. Before replaying a consequential operation after timeout, lost response or controller failure, reconcile the same operation's identity and canonical completion witness through an authorized existing path, or verify an existing idempotent replay contract covers that identity, payload and window. Preserve independently committed/completed effects. If neither establishes completion, no effect or safe replay, use `OPERATION_OUTCOME_UNKNOWN` / `NO_RETRY_UNTIL_CHANGE` and name the missing witness or enabling state; no new writer, state, probe or rollback path is authorized. Known-no-effect failure or checked safe replay retains its matching profile, budget, approval and provider wait.
```

Add the matching `OPERATION_OUTCOME_UNKNOWN` case row with zero replay attempts until that gate resolves; retain all prior classification, budgets and profiles.

### Bound input before parsing (additive)

**Targets:** `safe-io.md`, Bounded File Intake; its existing design/changelog triad.

**Before/current anchor:** Bounded File Intake ends `On tool-limit overflow narrow ranges/search rather than repeat full reads.` Display/range caps do not explicitly bound preparse allocation.

**After/target insertion before Aggregate Burst Gate:**

```text
For large, unknown or untrusted evidence, choose input byte, individual-record size and retained-result bounds before decoding, parsing or materializing it. Stream bounded windows and cap/reject oversized records before parse; account for decoded expansion. Output truncation is not a memory bound; count-only limits do not cap record bytes or decoded expansion. Use a fixed byte watermark for concurrently appended logs; report skipped records, byte limits and partial coverage. If the available format/tool cannot honor these bounds, stop for a narrower artifact or supported bounded mechanism rather than load everything. Known small files and exact bounded reads stay direct. These intake bounds do not authorize Product/runtime resource policy, cgroup/container changes or a new runner.
```

### Governed proof and navigation (restructuring)

**Targets:** master design/changelog/README/TODO/phase; existing playground Cases 02/04 and virtual matrix.

**Before:** v10.74/P073-19 settled-doc-synthesis baseline is closed.

**After:** v10.75/P073-20 is a sibling in the existing Runtime-owner/install family, with two owner version advances and explicit allowed/stop/near-miss scenarios. Preserve prior history and unrelated plugin/support/diagram/TODO changes. No new root Rule, diagram, generic test framework or plugin mutation.

## Verification

Use affected source/metadata/history/link/preservation checks, paired full-context synthetic interpretation, existing Bash and available PowerShell installer fixtures, exact nineteen-file source-to-runtime bytes/modes/body/ordered-manifest proof, and source-root scoped publication plus fresh public tag installation. Record each layer separately; source/fixture parity does not prove active-session reload, model benefit or historical incident repair. Skill landing remains separately verified or explicitly pending.

## Rollback Approach

Retain exact pre-change source fingerprints and unrelated working-state fingerprints. Before installation preserve the existing nineteen Runtime files and manifest outside normal discovery with owner-only recovery metadata. Restore only through an explicit scoped decision, never automatic fallback. Git commits/tags are non-force and immutable; a publication failure does not reset or replace the canonical root. Managed Skill intents and their nontransactional promoter are outside this Patch's rollback authority.
