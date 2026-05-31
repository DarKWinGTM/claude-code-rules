#!/usr/bin/env python3
"""Phase-013 candidate packet builder and gated /additional/ emitter.

This helper turns the phase_013_candidate_input produced by orchestration into a
promotion-ready candidate packet. It can also preview or explicitly write one
additional-stage trial rule file under a caller-selected additional root.

It never mutates main RULES. Writes require --approved-write and are blocked on
packet stop gates, unsafe paths, or existing files unless --allow-overwrite is
provided.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any

PACKET_MODEL = "phase-013-candidate-packet-v1"
EMISSION_MODEL = "phase-013-additional-emission-v1"
DEFAULT_ADDITIONAL_ROOT = "~/.claude/rules/additional"


class CandidatePacketError(ValueError):
    """Raised when candidate packet input or emission target is invalid."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence packet|emit",
        description=(
            "Build phase-013 candidate packets and preview or explicitly write "
            "trial-stage material to an additional root. No main RULES mutation."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    packet = subparsers.add_parser("packet", help="Build a candidate packet from phase_013_candidate_input.")
    packet.add_argument(
        "--orchestration-report",
        help="JSON report containing phase_013_candidate_input, usually from orchestrate.",
    )
    packet.add_argument(
        "--candidate-input",
        help="JSON object that is already a phase_013_candidate_input payload.",
    )
    packet.add_argument(
        "--owner-domain",
        help="Explicit owner domain mapping for the intended main RULES target.",
    )
    packet.add_argument(
        "--main-rule-target",
        help="Explicit intended main-rule target, e.g. rules/evidence-discipline.md.",
    )
    packet.add_argument(
        "--additional-name",
        help="Explicit trial rule name. Defaults to a slug from the selected topic title.",
    )
    packet.add_argument(
        "--additional-relative-path",
        help="Relative path below the selected additional root. Defaults to memory-context-intelligence/<name>.md.",
    )

    emit = subparsers.add_parser("emit", help="Preview or explicitly write additional-stage trial material.")
    emit.add_argument("--packet-report", required=True, help="Candidate packet JSON path from the packet command.")
    emit.add_argument(
        "--additional-root",
        default=None,
        help="Additional-stage root. Defaults to MEMORY_CONTEXT_INTELLIGENCE_ADDITIONAL_ROOT, MCI_ADDITIONAL_ROOT, or ~/.claude/rules/additional.",
    )
    emit.add_argument(
        "--approved-write",
        action="store_true",
        help="Actually write the file. Omit for dry-run preview only.",
    )
    emit.add_argument(
        "--allow-overwrite",
        action="store_true",
        help="Allow replacing an existing emitted trial file. Omit to refuse overwrites.",
    )
    return parser.parse_args(argv)


def load_json_input(path_value: str | None) -> dict[str, Any]:
    if not path_value:
        raise CandidatePacketError("A JSON input path is required.")
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise CandidatePacketError(f"JSON input must be an object: {path}")
    return loaded


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def as_text_list(value: Any) -> list[str]:
    result: list[str] = []
    for item in as_list(value):
        if item is None:
            continue
        text = str(item).strip()
        if text:
            result.append(text)
    return result


def dedupe_text(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def slugify(value: str, fallback: str = "memory-context-candidate") -> str:
    lowered = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:80].strip("-") or fallback


def extract_candidate_input(report: dict[str, Any]) -> dict[str, Any]:
    candidate_input = report.get("phase_013_candidate_input")
    if isinstance(candidate_input, dict):
        return candidate_input
    if isinstance(report.get("selected_topic"), dict):
        return report
    raise CandidatePacketError("Input must contain phase_013_candidate_input or be a candidate input object.")


def selected_topic_from(candidate_input: dict[str, Any]) -> dict[str, Any]:
    topic = candidate_input.get("selected_topic")
    if not isinstance(topic, dict):
        raise CandidatePacketError("phase_013_candidate_input.selected_topic is required for packet building.")
    topic_id = str(topic.get("id") or "").strip()
    title = str(topic.get("title") or "").strip()
    if not topic_id or not title:
        raise CandidatePacketError("selected_topic requires non-empty id and title.")
    return topic


def normalize_relative_path(relative_path: str) -> str:
    raw = str(relative_path or "").replace("\\", "/").strip()
    if not raw:
        raise CandidatePacketError("Additional relative path is required.")
    if raw.startswith("~"):
        raise CandidatePacketError("Additional relative path must not start with '~'.")
    path = PurePosixPath(raw)
    if path.is_absolute():
        raise CandidatePacketError("Additional relative path must not be absolute.")
    parts = path.parts
    if not parts or any(part in {"", ".", ".."} for part in parts):
        raise CandidatePacketError("Additional relative path must not contain empty, '.', or '..' segments.")
    if any(part.startswith(".") for part in parts):
        raise CandidatePacketError("Additional relative path must not contain hidden path segments.")
    safe_path = path.as_posix()
    if not safe_path.endswith(".md"):
        safe_path = f"{safe_path}.md"
    return safe_path


def infer_owner_mapping(topic: dict[str, Any], owner_domain: str | None, main_rule_target: str | None) -> dict[str, Any]:
    if owner_domain or main_rule_target:
        return {
            "owner_domain": owner_domain or "needs-leader-verification",
            "intended_main_rule_target": main_rule_target or "needs-leader-verification",
            "mapping_basis": "explicit-cli-override" if owner_domain and main_rule_target else "partial-explicit-cli-override",
            "leader_verification_required": True,
        }

    text = " ".join(
        str(topic.get(key) or "")
        for key in ("title", "purpose", "why_surfaced", "expected_behavior_impact", "high_level_mechanism", "expected_output")
    ).lower()
    keyword_map = [
        (("completion", "verified", "verification", "evidence", "fixed", "stable"), "evidence-and-accurate-communication", "rules/evidence-discipline.md + rules/accurate-communication.md"),
        (("phase", "todo", "goal", "execution"), "phase-todo-and-execution", "rules/phase-todo-artifact.md + rules/execution-and-goal-frame.md"),
        (("worker", "agent", "delegate", "subagent", "teammate"), "worker-routing", "rules/worker-routing-and-context.md"),
        (("memory", "recall", "scope"), "memory-governance", "rules/memory-governance-and-session-boundary.md"),
        (("design", "changelog", "document", "patch", "reference"), "document-governance", "rules/document-governance.md + rules/document-integrity.md"),
    ]
    for keywords, domain, target in keyword_map:
        if any(keyword in text for keyword in keywords):
            return {
                "owner_domain": domain,
                "intended_main_rule_target": target,
                "mapping_basis": "bounded-topic-keyword-inference",
                "leader_verification_required": True,
            }
    return {
        "owner_domain": "needs-leader-verification",
        "intended_main_rule_target": "needs-leader-verification",
        "mapping_basis": "unresolved-from-candidate-input",
        "leader_verification_required": True,
    }


def build_candidate_packet(
    candidate_input: dict[str, Any],
    *,
    owner_domain: str | None = None,
    main_rule_target: str | None = None,
    additional_name: str | None = None,
    additional_relative_path: str | None = None,
) -> dict[str, Any]:
    topic = selected_topic_from(candidate_input)
    trace_anchors = as_list(candidate_input.get("trace_anchors"))
    source_anchors = as_list(candidate_input.get("source_anchors"))
    input_stop_gates = as_text_list(candidate_input.get("blocking_stop_gates"))
    conflicts_uncertainty = as_text_list(candidate_input.get("conflicts_uncertainty"))
    input_leader_needs = as_text_list(candidate_input.get("leader_verification_needs"))

    rule_name = slugify(str(additional_name or topic.get("title") or topic.get("id") or ""))
    proposed_relative_path = normalize_relative_path(
        additional_relative_path or f"memory-context-intelligence/{rule_name}.md"
    )
    owner_mapping = infer_owner_mapping(topic, owner_domain, main_rule_target)

    stop_gates = list(input_stop_gates)
    if not trace_anchors:
        stop_gates.append("trace evidence anchors are missing")
    if owner_mapping["owner_domain"] == "needs-leader-verification":
        stop_gates.append("owner domain must be verified before approved additional emission")
    if owner_mapping["intended_main_rule_target"] == "needs-leader-verification":
        stop_gates.append("intended main-rule target must be verified before approved additional emission")

    leader_verification_needs = dedupe_text(
        input_leader_needs
        + (["Review recorded conflicts or uncertainty as trial limitations before relying on additional-stage behavior."] if conflicts_uncertainty else [])
        + [
            "Verify the selected topic still reflects the original memory trace and bounded signal anchors.",
            "Verify the owner-domain mapping and intended main-rule target before treating the packet as promotion-ready.",
            "Verify the proposed additional-stage path is trial-only and not a main RULES mutation path.",
            "Review emitted trial material before any live additional-stage trial or future main RULES promotion decision.",
        ]
    )

    candidate_summary = {
        "topic_id": topic.get("id"),
        "title": topic.get("title"),
        "purpose": topic.get("purpose"),
        "why_surfaced": topic.get("why_surfaced"),
        "expected_behavior_impact": topic.get("expected_behavior_impact"),
        "high_level_mechanism": topic.get("high_level_mechanism"),
        "expected_output": topic.get("expected_output"),
        "confidence": topic.get("confidence"),
        "evidence_label": topic.get("evidence_label"),
        "source_signal_ids": topic.get("source_signal_ids", []),
    }

    signal_evidence_basis = {
        "model_version": candidate_input.get("model_version"),
        "lane_ids": candidate_input.get("lane_ids", []),
        "trace_anchor_count": len(trace_anchors),
        "source_anchor_count": len(source_anchors),
        "trace_anchors": trace_anchors,
        "source_anchors": source_anchors,
        "conflicts_uncertainty": conflicts_uncertainty,
        "evidence_label": topic.get("evidence_label"),
        "evidence_strength_note": (
            "Candidate packet evidence is bounded input for leader review; it is not main RULES authority, "
            "live trial proof, or promotion approval."
        ),
    }

    packet = {
        "candidate_summary": candidate_summary,
        "signal_evidence_basis": signal_evidence_basis,
        "owner_domain_mapping": owner_mapping,
        "proposed_additional_rule": {
            "name": rule_name,
            "relative_path": proposed_relative_path,
            "display_path": f"<additional-root>/{proposed_relative_path}",
            "path_model": "relative-to-selected-additional-root",
            "trial_stage_only": True,
        },
        "trial_first_rationale": [
            "The candidate originates from bounded memory and orchestration evidence, not from a completed main RULES design/change process.",
            "The additional stage lets the user observe practical behavior before any governed main RULES merge is considered.",
            "Main RULES mutation remains a later, explicitly selected promotion path after trial evidence exists.",
        ],
        "risks": dedupe_text(
            [
                "Owner-domain mapping may be incomplete until leader verification confirms the correct main-rule target.",
                "Bounded memory evidence can surface useful patterns but may not represent exhaustive project behavior.",
                "Additional-stage material could be over-trusted if trial-only status is not kept visible.",
                "Main RULES must not be mutated by packet building or additional emission.",
            ]
            + conflicts_uncertainty
        ),
        "success_criteria": dedupe_text(
            [
                str(topic.get("expected_output") or "A reviewable additional-stage trial rule exists for the selected candidate."),
                str(topic.get("expected_behavior_impact") or "The trial rule improves future assistant behavior in the checked scope."),
                "The trial stays isolated under the selected additional root and does not mutate main RULES.",
                "Leader review can trace the candidate summary back to signal and source anchors.",
                "A later promotion decision can name evidence that the trial improved behavior in practice.",
            ]
        ),
        "rollback_notes": [
            "Rollback is scoped to the emitted additional-stage trial file only; main RULES rollback is not needed because main RULES are not mutated.",
            "Retire, replace, or remove the emitted trial file only after explicit action-and-scope confirmation.",
            "If the trial needs revision, prefer a new distinct additional-stage file unless overwrite is explicitly approved for the same destination.",
        ],
        "stop_gates": dedupe_text(stop_gates),
        "leader_verification_needs": leader_verification_needs,
    }

    status = "packet-built" if not packet["stop_gates"] else "packet-built-with-stop-gates"
    return {
        "tool": "memory-context-intelligence",
        "mode": "packet",
        "status": status,
        "candidate_packet_model": PACKET_MODEL,
        "candidate_packet": packet,
        "candidate_packet_built": True,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
        "notes": [
            "Candidate packet building is local and deterministic.",
            "No additional-stage file was written by packet mode.",
            "Main RULES mutation was not performed.",
        ],
    }


def render_bullets(values: list[Any]) -> str:
    if not values:
        return "- none recorded"
    return "\n".join(f"- {json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (dict, list)) else value}" for value in values)


def render_additional_rule(packet_report: dict[str, Any]) -> str:
    packet = packet_report.get("candidate_packet")
    if not isinstance(packet, dict):
        raise CandidatePacketError("packet_report.candidate_packet is required for rendering.")
    summary = packet.get("candidate_summary", {}) if isinstance(packet.get("candidate_summary"), dict) else {}
    owner = packet.get("owner_domain_mapping", {}) if isinstance(packet.get("owner_domain_mapping"), dict) else {}
    proposed = packet.get("proposed_additional_rule", {}) if isinstance(packet.get("proposed_additional_rule"), dict) else {}
    evidence = packet.get("signal_evidence_basis", {}) if isinstance(packet.get("signal_evidence_basis"), dict) else {}

    title = str(summary.get("title") or proposed.get("name") or "Memory context candidate")
    return "\n".join(
        [
            f"# Additional trial rule: {title}",
            "",
            "> **Status:** Trial-only additional-stage material",
            "> **Source:** memory-context-intelligence phase-013 candidate packet",
            f"> **Intended main-rule target:** {owner.get('intended_main_rule_target', 'needs-leader-verification')}",
            "> **Main RULES mutation:** Not performed",
            "",
            "## Candidate summary",
            "",
            f"- Topic ID: {summary.get('topic_id')}",
            f"- Purpose: {summary.get('purpose') or 'not recorded'}",
            f"- Why surfaced: {summary.get('why_surfaced') or 'not recorded'}",
            f"- Expected behavior impact: {summary.get('expected_behavior_impact') or 'not recorded'}",
            f"- Expected output: {summary.get('expected_output') or 'not recorded'}",
            f"- Confidence: {summary.get('confidence') or 'not recorded'}",
            f"- Evidence label: {summary.get('evidence_label') or 'not recorded'}",
            "",
            "## Signal and evidence basis",
            "",
            f"- Model version: {evidence.get('model_version') or 'not recorded'}",
            f"- Trace anchors: {evidence.get('trace_anchor_count', 0)}",
            f"- Source anchors: {evidence.get('source_anchor_count', 0)}",
            f"- Evidence note: {evidence.get('evidence_strength_note') or 'bounded evidence input only'}",
            "",
            "## Owner-domain mapping",
            "",
            f"- Owner domain: {owner.get('owner_domain') or 'needs-leader-verification'}",
            f"- Intended main-rule target: {owner.get('intended_main_rule_target') or 'needs-leader-verification'}",
            f"- Mapping basis: {owner.get('mapping_basis') or 'not recorded'}",
            "",
            "## Trial-first rationale",
            "",
            render_bullets(as_list(packet.get("trial_first_rationale"))),
            "",
            "## Risks",
            "",
            render_bullets(as_list(packet.get("risks"))),
            "",
            "## Success criteria",
            "",
            render_bullets(as_list(packet.get("success_criteria"))),
            "",
            "## Rollback notes",
            "",
            render_bullets(as_list(packet.get("rollback_notes"))),
            "",
            "## Stop gates",
            "",
            render_bullets(as_list(packet.get("stop_gates"))),
            "",
            "## Leader verification needs",
            "",
            render_bullets(as_list(packet.get("leader_verification_needs"))),
            "",
            "## Promotion boundary",
            "",
            "This file is additional-stage trial material only. It is evidence for later review, not a main RULES merge, install claim, publication claim, or stable doctrine by itself.",
            "",
        ]
    )


def default_additional_root(cli_root: str | None = None) -> str:
    if cli_root:
        return cli_root
    import os

    return (
        os.environ.get("MEMORY_CONTEXT_INTELLIGENCE_ADDITIONAL_ROOT")
        or os.environ.get("MCI_ADDITIONAL_ROOT")
        or DEFAULT_ADDITIONAL_ROOT
    )


def resolve_destination(additional_root: str, relative_path: str) -> tuple[Path, Path]:
    root = Path(additional_root).expanduser().resolve()
    root_text = str(root)
    if root.name == "rules" or root_text.endswith("/TEMPLATE/RULES"):
        raise CandidatePacketError("Additional root must be the additional-stage root, not a main RULES root.")
    safe_relative_path = normalize_relative_path(relative_path)
    destination = (root / safe_relative_path).resolve()
    try:
        destination.relative_to(root)
    except ValueError as exc:
        raise CandidatePacketError("Resolved additional destination escapes the selected additional root.") from exc
    return root, destination


def emit_additional(
    packet_report: dict[str, Any],
    *,
    additional_root: str | None = None,
    approved_write: bool = False,
    allow_overwrite: bool = False,
) -> dict[str, Any]:
    packet = packet_report.get("candidate_packet")
    if not isinstance(packet, dict):
        raise CandidatePacketError("packet_report.candidate_packet is required for emission.")
    proposed = packet.get("proposed_additional_rule")
    if not isinstance(proposed, dict):
        raise CandidatePacketError("candidate_packet.proposed_additional_rule is required for emission.")
    relative_path = normalize_relative_path(str(proposed.get("relative_path") or ""))
    root, destination = resolve_destination(default_additional_root(additional_root), relative_path)
    material = render_additional_rule(packet_report)

    stop_gates = as_text_list(packet.get("stop_gates"))
    if approved_write and stop_gates:
        raise CandidatePacketError("Approved additional write refused because packet stop gates are present.")
    if approved_write and destination.exists() and not allow_overwrite:
        raise CandidatePacketError("Approved additional write refused because destination exists and --allow-overwrite was not provided.")

    if approved_write:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(material, encoding="utf-8")

    return {
        "tool": "memory-context-intelligence",
        "mode": "emit",
        "status": "emitted" if approved_write else "preview",
        "emission_model": EMISSION_MODEL,
        "approved_write": approved_write,
        "allow_overwrite": allow_overwrite,
        "dry_run": not approved_write,
        "additional_root": str(root),
        "destination_path": str(destination),
        "destination_relative_path": relative_path,
        "preview_material": material,
        "bytes_planned": len(material.encode("utf-8")),
        "additional_emission_performed": approved_write,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
        "notes": [
            "Dry-run preview only; no file was written." if not approved_write else "Approved write completed under the selected additional root.",
            "Main RULES mutation was not performed.",
        ],
    }


def build_packet_from_args(args: argparse.Namespace) -> dict[str, Any]:
    if bool(args.orchestration_report) == bool(args.candidate_input):
        raise CandidatePacketError("Provide exactly one of --orchestration-report or --candidate-input.")
    source = load_json_input(args.orchestration_report or args.candidate_input)
    candidate_input = extract_candidate_input(source)
    return build_candidate_packet(
        candidate_input,
        owner_domain=args.owner_domain,
        main_rule_target=args.main_rule_target,
        additional_name=args.additional_name,
        additional_relative_path=args.additional_relative_path,
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.command == "packet":
            report = build_packet_from_args(args)
        elif args.command == "emit":
            packet_report = load_json_input(args.packet_report)
            report = emit_additional(
                packet_report,
                additional_root=args.additional_root,
                approved_write=args.approved_write,
                allow_overwrite=args.allow_overwrite,
            )
        else:
            raise CandidatePacketError(f"Unsupported command: {args.command}")
    except (OSError, json.JSONDecodeError, CandidatePacketError) as exc:
        print(f"memory-context-intelligence {args.command}: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
