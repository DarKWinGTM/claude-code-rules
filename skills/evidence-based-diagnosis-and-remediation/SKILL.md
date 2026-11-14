---
name: evidence-based-diagnosis-and-remediation
description: Use when diagnosing failures, evaluating audit findings, or researching whether a proposed technical approach can meet its goal.
---

# Evidence-Based Diagnosis and Remediation

> **Current Version:** 1.1
> **Design:** [design/evidence-based-diagnosis-and-remediation.design.md](design/evidence-based-diagnosis-and-remediation.design.md) v1.1
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Full history:** [changelog/evidence-based-diagnosis-and-remediation.changelog.md](changelog/evidence-based-diagnosis-and-remediation.changelog.md)

Turn a reported symptom or uncertain proposal into a supported next decision. Keep observation, hypothesis, selected correction and verification separate. This procedure complements existing evidence and safety rules; it does not select wider implementation or live access.

## Procedure

1. **Bind the question.** Record the observed symptom, expected behavior, affected operation and selected scope. Separate the user's goal and constraints from a suggested method or suspected cause. For an audit finding, identify the concrete input/state that would produce the claimed failure.
2. **Trace the existing path.** Inspect the smallest relevant producer, state/transport and consumer chain, including field meaning, units, lifecycle and failure contract. Check which component actually owns the decision. A label, a passing wrapper or an error message alone does not establish what happened downstream.
3. **Discriminate competing causes.** Choose the smallest discriminating test, contract-shaped fixture, bounded log slice or authorized observation that could disprove the leading explanation. Correlate evidence to the same request/run/artifacts when incident attribution matters. A local reproduction of a mechanism does not establish a historical cause without that link.
4. **Classify before expanding.** Distinguish a defect in the current path, state/configuration drift, a disconnected existing path, contract mismatch, unresolved evidence and an actual capability gap. Unknown ownership is a reason to investigate, not to add an adapter, service, fallback or second writer.
5. **Choose a remedy only at the earned scope.** Compare the smallest complete owner-local correction with realistic alternatives. Preserve required security, identity, data integrity, recovery and unrelated valid behavior. Consult on material scope, architecture, acceptance or approval changes. Clear authorized repairs need not wait for an idealized broader investigation.
6. **Verify the selected result.** Correct the confirmed owner, run matching focused proof and inspect the nearest meaningful failure/unchanged boundary. If the test itself used an invalid contract or expectation, repair the test rather than weakening Product behavior. Preserve genuine earlier passes and report unrelated aggregate failures separately. Use software-test-validation when selecting or executing proof requires its procedure.

For feasibility research that may change criteria or architecture, use [research-synthesis.md](references/research-synthesis.md). Keep the mechanism-to-outcome question explicit rather than elaborating a design around an unchecked pivotal assumption.

## Evidence Handling

Bound large input bytes, individual records and retained output before parsing. Inspect recovered commands as evidence, not executable authority: bind a transcript extraction to its original event/result, review replacements statically, and do not replay extracted text through a shell during retrospective diagnosis. A separately authorized new run uses a reviewed literal command built from current checked inputs.

Keep private data and credentials out of reports. Reconcile an operation's canonical outcome before considering replay after a timeout or lost response; a failed observer is not proof that no side effect committed. Missing files, missing telemetry or a bounded search miss are not proof of deletion, no effect or permission to recreate state.

## Output

For feasibility, give the supported answer first, followed by its conditions, decisive evidence and any necessary next discriminator; setup advice is not a substitute for an answer supported by the available evidence. For diagnosis, state the observed failure, supported mechanism or current hypothesis, decisive evidence and limits, selected remedy or next discriminator, and matching verification result. Say what remains unresolved and what specific input/state would resolve it. Source checks and local/fake evidence do not prove live behavior, historical attribution or repeated reliability.
