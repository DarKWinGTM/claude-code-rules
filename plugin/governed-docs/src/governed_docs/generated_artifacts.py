from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class RepairPlanItem:
    subject: str
    classification: str
    problem_class: str
    recommended_action: str
    approval_boundary: str
    evidence: List[str] = field(default_factory=list)
    preservation_notes: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class RepairPlan:
    target_workspace_path: Path
    checked_scope: str
    items: List[RepairPlanItem]
    mutated: bool = False



def build_repair_plan_artifact(repair_plan: RepairPlan) -> str:
    lines = [
        "# governed-docs repair plan artifact",
        f"Checked scope: {repair_plan.checked_scope}",
        f"Target workspace: {repair_plan.target_workspace_path}",
        "Items:",
    ]

    if repair_plan.items:
        for item in repair_plan.items:
            lines.append(f"- Subject: {item.subject}")
            lines.append(f"  Classification: {item.classification}")
            lines.append(f"  Problem class: {item.problem_class}")
            lines.append(f"  Recommended action: {item.recommended_action}")
            lines.append(f"  Approval boundary: {item.approval_boundary}")
            if item.evidence:
                lines.append("  Observed facts:")
                for fact in item.evidence:
                    lines.append(f"  - {fact}")
            if item.preservation_notes:
                lines.append("  Preservation notes:")
                for note in item.preservation_notes:
                    lines.append(f"  - {note}")
    else:
        lines.append("- none")

    lines.append(f"Mutated: {repair_plan.mutated}")
    return "\n".join(lines)
