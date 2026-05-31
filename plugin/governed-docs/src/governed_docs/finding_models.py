from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass(frozen=True)
class DoctrineFinding:
    subject: str
    classification: str
    problem_class: Optional[str]
    reason: str
    evidence: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class DoctrineEvaluation:
    target_workspace_path: Path
    checked_scope: str
    findings: List[DoctrineFinding]
    mutated: bool = False
