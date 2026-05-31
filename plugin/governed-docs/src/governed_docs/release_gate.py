from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class ReleaseGateVerdict:
    target_workspace_path: Path
    checked_scope: str
    verdict: str
    notes: List[str] = field(default_factory=list)



def evaluate_release_gate(doctrine_evaluation, verification_passed: bool) -> ReleaseGateVerdict:
    notes = []
    verdict = 'pass'

    if not verification_passed:
        return ReleaseGateVerdict(
            target_workspace_path=doctrine_evaluation.target_workspace_path,
            checked_scope=doctrine_evaluation.checked_scope,
            verdict='rework',
            notes=['Verification did not pass in checked scope.'],
        )

    classifications = [finding.classification for finding in doctrine_evaluation.findings]

    if 'blocked' in classifications or 'ambiguous-needs-basis' in classifications:
        verdict = 'blocked'
    elif 'drift' in classifications:
        verdict = 'rework'
    elif 'legacy-but-allowed' in classifications or 'safe-auto-repair' in classifications:
        verdict = 'pass-with-notes'

    for finding in doctrine_evaluation.findings:
        notes.append(f'{finding.classification} | {finding.problem_class} | {finding.subject}')

    return ReleaseGateVerdict(
        target_workspace_path=doctrine_evaluation.target_workspace_path,
        checked_scope=doctrine_evaluation.checked_scope,
        verdict=verdict,
        notes=notes,
    )
