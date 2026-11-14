---
name: technical-communication
description: Use when explaining technical behavior, reviewing user-facing technical copy, or communicating findings, results and next actions.
---

# Technical Communication

> **Current Version:** 1.0
> **Design:** [design/technical-communication.design.md](design/technical-communication.design.md) v1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Full history:** [changelog/technical-communication.changelog.md](changelog/technical-communication.changelog.md)

Explain checked meaning before relying on identifiers. Give the reader enough mechanism and consequence to understand the result or make the next decision, without turning the answer into a transcript or another policy layer.

## Procedure

1. **Identify the reader's question.** Determine whether they need a definition, comparison, diagnosis, command, status or decision. Match the working language, requested depth and audience. Acknowledgment checks need a direct answer, not a new plan.
2. **Resolve meaning from evidence.** For an unfamiliar term or field, explain what it represents, what it controls and what changes if it changes. Check its real producer, consumer, units and contract rather than guessing from its name. Explain nested values from parent to child only where that helps.
3. **Lead with the point.** Use meaning → mechanism → consequence: what is known, how it works and what it means for the reader. Put a material limit, dependency or required action beside the relevant conclusion. Use a compact comparison table or ordered steps only when the relationship calls for them.
4. **Calibrate results.** Distinguish inspected, edited, configured, queued, tested, installed and published states using what actually happened. Include the matching check and material remainder. An HTTP success, a build or a fake/local pass supports its own layer, not complete operation, live adoption or stability. If an attempt was reverted, say what was undone and what remains.
5. **Make the requested output complete.** A complete inventory retains every in-scope item and its disposition before recommendations. For one shell recipe, provide one coherent command/subshell with checked inputs and consistent formats, options and dependent steps. If inputs are missing, label it a template rather than ready-to-run; preserve pipeline failures and necessary overwrite/privilege warnings. Distinguish syntax review from execution and tested output.
6. **Correct unsupported advice explicitly.** State the failed premise, contrary evidence, corrected interpretation and practical consequence. Preserve the valid goal and settled choices. Do not silently reverse course, restate the old proposal or ask for a constraint already supplied.
7. **Finish at the useful next decision.** Report the actual outcome or exact enabling action. If the reader asks what happens now, give one next action and its owner rather than repeating resolved history. A proposal or explanation does not authorize source edits, tests or downstream operations.

## Output

Use a short orientation followed by only the structure needed for the task. State checked facts directly, keep inference and unresolved questions identifiable, and disclose relevant untested scope without over-caveating complete proof. For external copy, omit unnecessary sensitive internals while still giving the authorized owner the full relevant basis.

Example: “The service returned HTTP 200, but its response did not match the expected data shape. Connectivity is confirmed; successful data processing is not.” This explains the boundary without inventing the cause or claiming the API is fully supported.
