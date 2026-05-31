from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionDecision:
    mode: str
    allowed: bool
    reason: str



def decide_execution(repair_plan_item) -> ExecutionDecision:
    if repair_plan_item.recommended_action == 'bounded-normalize-candidate':
        return ExecutionDecision(
            mode='bounded-auto-normalize',
            allowed=True,
            reason='Policy allows bounded low-risk normalization candidates to proceed to previewable execution.',
        )

    if repair_plan_item.recommended_action == 'block-closeout':
        return ExecutionDecision(
            mode='blocked',
            allowed=False,
            reason='Blocked findings must remain blocked until manually resolved.',
        )

    if repair_plan_item.recommended_action == 'open-repair-patch':
        return ExecutionDecision(
            mode='guarded-execute',
            allowed=False,
            reason='Repair requires reviewable patch planning before any execution.',
        )

    if repair_plan_item.recommended_action == 'ask-for-basis':
        return ExecutionDecision(
            mode='advisory',
            allowed=False,
            reason='A governing basis must be selected before execution can narrow the path.',
        )

    return ExecutionDecision(
        mode='advisory',
        allowed=False,
        reason='Item remains report-only unless a stricter policy decision is made later.',
    )
