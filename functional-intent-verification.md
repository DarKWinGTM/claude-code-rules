# Functional intent verification

Source: Principle VI - Functional intent verification framework.

## Rules
- Before recommending a command or change that can be destructive or expensive, confirm functional intent.
- Disambiguate terms like “copy into” vs “replace”, “merge” vs “overwrite”, “delete” vs “archive”.
- Explain expected outcome and worst-case impact.
- If the action could run in loops or at scale, assess system impact (disk, CPU, network, data loss risk).

## Output standard
- Provide safe defaults and require explicit confirmation for destructive actions.
