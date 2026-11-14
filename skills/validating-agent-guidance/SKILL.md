---
name: validating-agent-guidance
description: Use when authoring or reviewing agent instructions, Skills and workflows, or extracting reusable guidance from work history.
---

# Validating Agent Guidance

> **Current Version:** 1.0
> **Design:** [design/validating-agent-guidance.design.md](design/validating-agent-guidance.design.md) v1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Full history:** [changelog/validating-agent-guidance.changelog.md](changelog/validating-agent-guidance.changelog.md)

Check whether the actual draft supports the intended decisions, including the nearest case that should not trigger it. Separate instruction clarity, source/package correctness, synthetic interpretation and real-world benefit.

## Procedure

1. **Bind intent and permission.** Identify the behavior being changed, current instruction owner, selected outcome, allowed evaluation channels and useful proof. A concern or requested precaution is not evidence of an earlier failure. Existing instruction coverage may be enriched where a distinct procedure is useful; do not create a duplicate authority.
2. **Define discriminating cases.** State expected outcomes before running a check. Pair an allowed case with a stop/near-miss case where the relevant prerequisite is absent or contradicted. Cover continued decisions across turns when persistence of an accepted choice is material. Avoid making every hypothetical edge a new test campaign.
3. **Capture a baseline where practical.** Use existing guidance or no added guidance with the same case/context. Record actual behavior; if the baseline already succeeds, do not invent a failure or claim improvement. When evaluation is unavailable or prohibited, name the limited source review and leave any explicitly required behavior proof unresolved.
4. **Test the actual draft.** Bind the complete final text and necessary reader context, not a summary or an earlier version. Use an independent fresh context when authorized and useful; otherwise use the permitted bounded check and disclose its limit. Read-only or no-tool restrictions remain intact; another agent or channel cannot bypass them.
5. **Inspect and refine.** Compare observed decisions with the expected outcomes. Fix only the unclear condition, ordering or missing distinction, then rerun affected cases. Check relevant final-artifact content and references; proportional whitespace-only changes do not justify a new broad campaign.
6. **Separate acceptance from application.** A queued proposal is not a landed file. Use the actual supported tool schema and distinguish acceptance, application, installation and discovery. Do not invent a tool, invoke unavailable machinery or write around a protected owner to finish a checklist.

For history-based discovery, follow [history-discovery.md](references/history-discovery.md). That procedure preserves provenance and accepted/rejected dispositions; it does not automatically promote lessons or modify instructions.

## Output

Report the draft binding, selected cases and expected outcomes, actual result, baseline behavior, allowed channel, remaining ambiguity and proof limits. Synthetic interpretation is not measured user benefit, live behavior or causal improvement. Source/package checks and model compliance are separate claims; keep an unavailable required gate pending rather than re-labeling it passed.
