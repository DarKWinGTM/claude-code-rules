def build_guardrail_message(context_label: str) -> str:
    return (
        'governed-docs hook guardrail reminder\n'
        f'Context: {context_label}\n'
        'This reminder is advisory/support-only. It must not mutate governed docs or become hidden governance authority.'
    )
