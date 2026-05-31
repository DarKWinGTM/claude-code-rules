from governed_docs.executor_policy import decide_execution


class PolicyBlockedError(RuntimeError):
    """Raised when a requested normalization is not allowed by executor policy."""



def preview_normalization(repair_plan_item) -> str:
    decision = decide_execution(repair_plan_item)
    if not decision.allowed:
        raise PolicyBlockedError(decision.reason)

    return (
        'governed-docs normalization preview\n'
        f'Subject: {repair_plan_item.subject}\n'
        f'Recommended action: {repair_plan_item.recommended_action}\n'
        'Mode: bounded-auto-normalize\n'
        'This is a preview only. No files were edited.'
    )
