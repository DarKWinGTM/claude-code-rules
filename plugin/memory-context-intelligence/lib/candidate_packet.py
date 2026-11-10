#!/usr/bin/env python3
"""Phase-013 candidate packet builder and gated /additional/ emitter.

This helper turns the phase_013_candidate_input produced by orchestration into a
promotion-ready candidate packet. It can also preview or explicitly write one
additional-stage trial rule file under a caller-selected additional root.

It never mutates main RULES. Writes require --approved-write and are blocked on
packet stop gates, unsafe paths, invalid standalone material, duplicate targets,
or any existing destination. Existing trial artifacts are never overwritten.
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
SINGLE_TOPIC_ARTIFACT_SCOPE = "single-topic-only"
FORBIDDEN_MULTI_TOPIC_INPUT_KEYS = (
    "selected_topics",
    "selected_topic_ids",
    "packet_topics",
    "additional_topics",
    "combined_topics",
)
REQUIRED_STANDALONE_HEADINGS = (
    "## Candidate summary",
    "## Trial rule draft",
    "### Core principle",
    "### Draft operating clauses",
    "### Before behavior",
    "### After behavior",
    "## Signal and evidence basis",
    "## Owner-domain mapping",
    "## Trial-first rationale",
    "## Risks",
    "## Success criteria",
    "## Rollback notes",
    "## Stop gates",
    "## Leader verification needs",
    "## Promotion boundary",
)
FORBIDDEN_DEPENDENCY_PATTERNS = (
    ("memsearch-path", re.compile(r"\.memsearch(?:/|\\)")),
    ("dated-memory-shard", re.compile(r"\b\d{4}-\d{2}-\d{2}\.md\b")),
    ("transcript-jsonl", re.compile(r"(?:transcript[^\s]*|[^\s]+)\.jsonl\b", re.IGNORECASE)),
    ("temporary-path", re.compile(r"(?:^|[\s`(])/(?:tmp|var/tmp)/")),
    ("absolute-home-path", re.compile(r"(?:^|[\s`(])/home/")),
    ("raw-path-line", re.compile(r"\b[^\s`]+\.(?:md|py|json|jsonl|txt):\d+\b")),
    ("packet-report-path", re.compile(r"packet[-_]report[^\s`]*", re.IGNORECASE)),
    ("content-preview-dependency", re.compile(r"content_preview", re.IGNORECASE)),
)


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
    packet.add_argument(
        "--integration-anchor",
        action="append",
        default=[],
        help="Repeatable integration anchor for the trial artifact owner mapping.",
    )
    packet.add_argument(
        "--selected-for-additional-trial",
        action="store_true",
        help="Record explicit later user selection for additional-stage trial creation only.",
    )

    emit = subparsers.add_parser("emit", help="Preview or explicitly write one additional-stage trial artifact.")
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

    emit_selected = subparsers.add_parser(
        "emit-selected",
        help="Preview or atomically write independently packetized selected topics.",
    )
    emit_selected.add_argument(
        "--packet-report",
        action="append",
        required=True,
        help="Repeat for every independently built selected-topic packet report.",
    )
    emit_selected.add_argument(
        "--additional-root",
        default=None,
        help="Additional-stage root ending in 'additional'.",
    )
    emit_selected.add_argument(
        "--approved-write",
        action="store_true",
        help="Write the complete preflighted set. Omit for dry-run preview only.",
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


def assert_single_topic_candidate_input(candidate_input: dict[str, Any]) -> None:
    for key in FORBIDDEN_MULTI_TOPIC_INPUT_KEYS:
        if as_list(candidate_input.get(key)):
            raise CandidatePacketError(
                f"{key} is not allowed for candidate packet building; multi-topic packet-derived output must split into separate per-topic artifacts."
            )
    selected_topic_count = candidate_input.get("selected_topic_count")
    if selected_topic_count not in (None, 1):
        raise CandidatePacketError(
            "phase_013_candidate_input must describe exactly one selected topic before packet building; multi-topic packet-derived output must split into separate per-topic artifacts."
        )
    artifact_topic_scope = candidate_input.get("artifact_topic_scope")
    if artifact_topic_scope not in (None, SINGLE_TOPIC_ARTIFACT_SCOPE):
        raise CandidatePacketError(
            "phase_013 candidate input must keep single-topic artifact scope before packet building."
        )
    if candidate_input.get("multi_topic_combination_allowed") not in (None, False):
        raise CandidatePacketError(
            "phase_013 candidate input must not allow multi-topic combination; split into separate per-topic artifacts first."
        )


def assert_single_topic_packet(packet: dict[str, Any]) -> None:
    if packet.get("selected_topic_count") != 1:
        raise CandidatePacketError("candidate packet must carry exactly one single selected topic before additional emission.")
    if packet.get("artifact_topic_scope") != SINGLE_TOPIC_ARTIFACT_SCOPE:
        raise CandidatePacketError("candidate packet must keep single-topic artifact scope before additional emission.")
    if packet.get("multi_topic_combination_allowed") is not False:
        raise CandidatePacketError(
            "candidate packet must disallow multi-topic combination before additional emission."
        )


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
    assert_single_topic_candidate_input(candidate_input)
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


def evaluate_candidate_entailment(
    topic: dict[str, Any],
    trace_anchors: list[dict[str, Any]],
) -> dict[str, Any]:
    basis = topic.get("candidate_entailment_basis")
    if not isinstance(basis, dict):
        basis = {}

    selected_signal_ids = dedupe_text(
        as_text_list(basis.get("source_signal_ids"))
        or as_text_list(topic.get("source_signal_ids"))
    )
    matching_signal_ids = {
        str(anchor.get("signal_id"))
        for anchor in trace_anchors
        if isinstance(anchor, dict)
        and anchor.get("signal_id") in selected_signal_ids
    }
    supported_mechanism = str(basis.get("supported_mechanism") or "").strip()
    transferable_pattern = str(
        basis.get("transferable_observed_pattern")
        or topic.get("why_surfaced")
        or ""
    ).strip()

    if not selected_signal_ids or not matching_signal_ids:
        decision = "context-only"
        support_reason = "No bounded trace anchor matches the candidate's selected source signal ids."
    elif not supported_mechanism:
        decision = "reject"
        support_reason = "Matching trace evidence exists, but no evidence-supported mechanism was recorded."
    elif matching_signal_ids == set(selected_signal_ids):
        decision = "retain"
        support_reason = "Every selected source signal has matching bounded trace support."
    else:
        decision = "narrow"
        support_reason = "Only part of the selected signal set has matching trace support, so the candidate is narrowed to the recorded supported mechanism."

    return {
        "decision": decision,
        "selected_signal_ids": selected_signal_ids,
        "trace_anchor_count": len(
            [
                anchor
                for anchor in trace_anchors
                if isinstance(anchor, dict)
                and str(anchor.get("signal_id") or "") in matching_signal_ids
            ]
        ),
        "support_reason": support_reason,
        "transferable_observed_pattern": transferable_pattern,
        "supported_mechanism": supported_mechanism,
        "eligible_for_additional_trial": decision in {"retain", "narrow"},
    }


def normalize_evidence_basis(
    topic: dict[str, Any],
    selected_trace_anchors: list[dict[str, Any]],
    source_anchors: list[dict[str, Any]],
    conflicts_uncertainty: list[str],
    entailment: dict[str, Any],
) -> dict[str, Any]:
    source_classes: list[str] = []
    for anchor in selected_trace_anchors:
        if not isinstance(anchor, dict):
            continue
        source_classes.extend(as_text_list(anchor.get("source_classes")))
    for anchor in source_anchors:
        if not isinstance(anchor, dict):
            continue
        source_classes.extend(as_text_list(anchor.get("source_classes")))
        source_type = str(anchor.get("source_type") or "").strip()
        if source_type:
            source_classes.append(source_type)

    session_count = len(
        {
            str(anchor.get("session_id"))
            for anchor in selected_trace_anchors
            if isinstance(anchor, dict) and anchor.get("session_id")
        }
    )
    shard_count = len(
        {
            str(anchor.get("shard"))
            for anchor in selected_trace_anchors
            if isinstance(anchor, dict) and anchor.get("shard")
        }
    )
    limits = [
        "The evidence basis is bounded to selected trace anchors and does not prove exhaustive recurrence.",
        "Supporting source or governance context cannot replace missing trace support.",
    ]
    if entailment.get("decision") == "narrow":
        limits.append("Only part of the selected signal set had matching trace support, so the mechanism was narrowed.")
    if conflicts_uncertainty:
        limits.append("Recorded conflicts or uncertainty require leader review before later promotion decisions.")

    return {
        "source_classes": dedupe_text(source_classes) or ["trace_evidence"],
        "current_session_confirmation": str(topic.get("current_session_confirmation") or "not recorded"),
        "trace_record_count": len(selected_trace_anchors),
        "session_count": session_count,
        "shard_count": shard_count,
        "confidence": str(topic.get("confidence") or "not recorded"),
        "evidence_label": str(topic.get("evidence_label") or "not recorded"),
        "transferable_observed_pattern": str(entailment.get("transferable_observed_pattern") or "not recorded"),
        "mechanism_support": str(entailment.get("supported_mechanism") or "not recorded"),
        "conflicts_uncertainty": dedupe_text(conflicts_uncertainty),
        "limits": limits,
        "excluded_scope": [
            "Raw memory-shard, transcript, temporary-file, absolute-path, and content-preview dependencies are excluded from emitted doctrine.",
            "Main RULES mutation and promotion approval are outside this trial packet.",
        ],
    }


def build_trial_rule_draft(
    topic: dict[str, Any],
    entailment: dict[str, Any],
) -> dict[str, Any]:
    core_principle = str(entailment.get("supported_mechanism") or "").strip()
    purpose = str(topic.get("purpose") or "").strip()
    expected_impact = str(topic.get("expected_behavior_impact") or "").strip()
    expected_output = str(topic.get("expected_output") or "").strip()
    transferable_pattern = str(entailment.get("transferable_observed_pattern") or "").strip()

    operating_clauses = dedupe_text(
        [
            purpose,
            f"Apply the selected mechanism only where bounded trace evidence supports it." if core_principle else "",
            expected_output,
            "Keep trial-stage behavior separate from Main RULES promotion authority.",
        ]
    )
    return {
        "core_principle": core_principle,
        "operating_clauses": operating_clauses,
        "before_behavior": transferable_pattern or "The observed workflow left the evidence-supported behavior implicit.",
        "after_behavior": expected_impact or core_principle,
    }


def build_candidate_packet(
    candidate_input: dict[str, Any],
    *,
    owner_domain: str | None = None,
    main_rule_target: str | None = None,
    integration_anchors: list[str] | None = None,
    additional_name: str | None = None,
    additional_relative_path: str | None = None,
    selected_for_additional_trial: bool = False,
) -> dict[str, Any]:
    topic = selected_topic_from(candidate_input)
    trace_anchors = [
        anchor
        for anchor in as_list(candidate_input.get("trace_anchors"))
        if isinstance(anchor, dict)
    ]
    source_anchors = [
        anchor
        for anchor in as_list(candidate_input.get("source_anchors"))
        if isinstance(anchor, dict)
    ]
    input_stop_gates = as_text_list(candidate_input.get("blocking_stop_gates"))
    conflicts_uncertainty = as_text_list(candidate_input.get("conflicts_uncertainty"))
    input_leader_needs = as_text_list(candidate_input.get("leader_verification_needs"))

    rule_name = slugify(str(additional_name or topic.get("title") or topic.get("id") or ""))
    proposed_relative_path = normalize_relative_path(
        additional_relative_path or f"memory-context-intelligence/{rule_name}.md"
    )
    owner_mapping = infer_owner_mapping(topic, owner_domain, main_rule_target)
    owner_mapping["integration_anchors"] = dedupe_text(as_text_list(integration_anchors))

    entailment = evaluate_candidate_entailment(topic, trace_anchors)
    selected_signal_ids = set(as_text_list(entailment.get("selected_signal_ids")))
    selected_trace_anchors = [
        anchor
        for anchor in trace_anchors
        if str(anchor.get("signal_id") or "") in selected_signal_ids
    ]
    normalized_evidence = normalize_evidence_basis(
        topic,
        selected_trace_anchors,
        source_anchors,
        conflicts_uncertainty,
        entailment,
    )
    trial_rule_draft = build_trial_rule_draft(topic, entailment)

    stop_gates = list(input_stop_gates)
    if not trace_anchors:
        stop_gates.append("trace evidence anchors are missing")
    if not entailment["eligible_for_additional_trial"]:
        stop_gates.append(
            f"candidate entailment decision '{entailment['decision']}' is not eligible for additional-stage trial emission"
        )
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
        "artifact_topic_scope": SINGLE_TOPIC_ARTIFACT_SCOPE,
        "selected_topic_count": 1,
        "multi_topic_combination_allowed": False,
        "selected_for_additional_trial": bool(selected_for_additional_trial),
        "main_rules_promotion_approved": False,
        "candidate_entailment": entailment,
        "signal_evidence_basis": signal_evidence_basis,
        "normalized_evidence_basis": normalized_evidence,
        "trial_rule_draft": trial_rule_draft,
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
            "If the trial needs revision, use a new distinct additional-stage destination; existing trial artifact bytes remain preserved.",
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
        "artifact_topic_scope": SINGLE_TOPIC_ARTIFACT_SCOPE,
        "selected_topic_count": 1,
        "multi_topic_combination_allowed": False,
        "selected_for_additional_trial": bool(selected_for_additional_trial),
        "main_rules_promotion_approved": False,
        "candidate_packet": packet,
        "candidate_packet_built": True,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
        "notes": [
            "Candidate packet building is local and deterministic.",
            "Packet/additional-stage flow stays one selected topic per artifact.",
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
    assert_single_topic_packet(packet)
    summary = packet.get("candidate_summary", {}) if isinstance(packet.get("candidate_summary"), dict) else {}
    owner = packet.get("owner_domain_mapping", {}) if isinstance(packet.get("owner_domain_mapping"), dict) else {}
    proposed = packet.get("proposed_additional_rule", {}) if isinstance(packet.get("proposed_additional_rule"), dict) else {}
    evidence = packet.get("normalized_evidence_basis", {}) if isinstance(packet.get("normalized_evidence_basis"), dict) else {}
    entailment = packet.get("candidate_entailment", {}) if isinstance(packet.get("candidate_entailment"), dict) else {}
    draft = packet.get("trial_rule_draft", {}) if isinstance(packet.get("trial_rule_draft"), dict) else {}

    title = str(summary.get("title") or proposed.get("name") or "Memory context candidate")
    source_signal_ids = as_text_list(summary.get("source_signal_ids"))
    integration_anchors = as_text_list(owner.get("integration_anchors"))
    source_classes = as_text_list(evidence.get("source_classes"))
    return "\n".join(
        [
            f"# Additional trial rule: {title}",
            "",
            "> **Status:** Trial-only additional-stage material",
            f"> **Source:** memory-context-intelligence selected {summary.get('topic_id') or 'topic'}",
            f"> **Selected signal basis:** {', '.join(source_signal_ids) or 'not recorded'}",
            f"> **Intended main-rule target:** {owner.get('intended_main_rule_target', 'needs-leader-verification')}",
            f"> **Integration anchors:** {', '.join(integration_anchors) or 'none'}",
            "> **Main RULES mutation:** Not performed",
            "",
            "## Topic scope",
            "",
            "This additional-stage artifact is scoped to one selected topic per artifact.",
            "Multi-topic packet-derived output must split into separate per-topic artifacts.",
            "This file must not combine multiple selected topics.",
            "",
            "## Candidate summary",
            "",
            f"- Purpose: {summary.get('purpose') or 'not recorded'}",
            f"- Why surfaced: {summary.get('why_surfaced') or 'not recorded'}",
            f"- Expected behavior impact: {summary.get('expected_behavior_impact') or 'not recorded'}",
            f"- Expected output: {summary.get('expected_output') or 'not recorded'}",
            f"- Entailment decision: {entailment.get('decision') or 'not recorded'}",
            f"- Entailment basis: {entailment.get('support_reason') or 'not recorded'}",
            "",
            "## Trial rule draft",
            "",
            "### Core principle",
            "",
            str(draft.get("core_principle") or "No evidence-supported core principle was recorded."),
            "",
            "### Draft operating clauses",
            "",
            render_bullets(as_list(draft.get("operating_clauses"))),
            "",
            "### Before behavior",
            "",
            str(draft.get("before_behavior") or "The observed behavior was not recorded."),
            "",
            "### After behavior",
            "",
            str(draft.get("after_behavior") or "The intended trial behavior was not recorded."),
            "",
            "## Signal and evidence basis",
            "",
            f"- Source classes: {', '.join(source_classes) or 'not recorded'}",
            f"- Current-session confirmation: {evidence.get('current_session_confirmation') or 'not recorded'}",
            f"- Trace records: {evidence.get('trace_record_count', 0)}",
            f"- Sessions represented: {evidence.get('session_count', 0)}",
            f"- Evidence shards represented: {evidence.get('shard_count', 0)}",
            f"- Confidence: {evidence.get('confidence') or 'not recorded'}",
            f"- Evidence label: {evidence.get('evidence_label') or 'not recorded'}",
            f"- Transferable observed pattern: {evidence.get('transferable_observed_pattern') or 'not recorded'}",
            f"- Mechanism support: {evidence.get('mechanism_support') or 'not recorded'}",
            "- Conflicts and uncertainty:",
            render_bullets(as_list(evidence.get("conflicts_uncertainty"))),
            "- Evidence limits:",
            render_bullets(as_list(evidence.get("limits"))),
            "- Excluded scope:",
            render_bullets(as_list(evidence.get("excluded_scope"))),
            "",
            "## Owner-domain mapping",
            "",
            f"- Owner domain: {owner.get('owner_domain') or 'needs-leader-verification'}",
            f"- Intended main-rule target: {owner.get('intended_main_rule_target') or 'needs-leader-verification'}",
            f"- Mapping basis: {owner.get('mapping_basis') or 'not recorded'}",
            f"- Integration anchors: {', '.join(integration_anchors) or 'none'}",
            "- This mapping remains trial-stage routing and does not approve Main RULES promotion.",
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
            "This file is additional-stage trial material only. It does not modify Main RULES, approve promotion, prove live behavior, or authorize replacement or deletion of an existing trial artifact.",
            "",
        ]
    )


def validate_standalone_artifact(material: str) -> dict[str, Any]:
    missing_headings = [
        heading
        for heading in REQUIRED_STANDALONE_HEADINGS
        if heading not in material
    ]
    forbidden_dependencies = [
        label
        for label, pattern in FORBIDDEN_DEPENDENCY_PATTERNS
        if pattern.search(material)
    ]
    main_rules_not_performed = "Main RULES mutation:** Not performed" in material
    selected_topic_count = 1 if "one selected topic per artifact" in material else 0
    valid = (
        not missing_headings
        and not forbidden_dependencies
        and main_rules_not_performed
        and selected_topic_count == 1
    )
    return {
        "valid": valid,
        "ok": valid,
        "missing_headings": missing_headings,
        "missing_sections": missing_headings,
        "forbidden_dependencies": forbidden_dependencies,
        "selected_topic_count": selected_topic_count,
        "main_rules_mutation_declared_not_performed": main_rules_not_performed,
    }


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
    root = Path(additional_root).expanduser().absolute()
    if root.name != "additional":
        raise CandidatePacketError("Additional root basename must be exactly 'additional'.")
    if root.is_symlink():
        raise CandidatePacketError("Additional root must not be a symlink.")

    safe_relative_path = normalize_relative_path(relative_path)
    relative = PurePosixPath(safe_relative_path)
    if not relative.parts or relative.parts[0] != "memory-context-intelligence":
        raise CandidatePacketError(
            "Additional relative path must start with the memory-context-intelligence namespace."
        )
    if len(relative.parts) < 2:
        raise CandidatePacketError("Additional relative path must include a file below the namespace.")

    unresolved_destination = root.joinpath(*relative.parts)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise CandidatePacketError(
                f"Additional destination path must not contain symlink components: {current}"
            )

    resolved_root = root.resolve(strict=False)
    destination = unresolved_destination.resolve(strict=False)
    try:
        destination.relative_to(resolved_root)
    except ValueError as exc:
        raise CandidatePacketError("Resolved additional destination escapes the selected additional root.") from exc
    return resolved_root, destination


def preflight_selected_emission(
    packet_reports: list[dict[str, Any]],
    *,
    additional_root: str | None = None,
) -> dict[str, Any]:
    if not packet_reports:
        raise CandidatePacketError("At least one selected-topic packet report is required.")

    selected_root = default_additional_root(additional_root)
    items: list[dict[str, Any]] = []
    destinations: set[str] = set()
    resolved_root: Path | None = None

    for packet_report in packet_reports:
        packet = packet_report.get("candidate_packet")
        if not isinstance(packet, dict):
            raise CandidatePacketError("packet_report.candidate_packet is required for emission.")
        assert_single_topic_packet(packet)
        if packet.get("selected_for_additional_trial") is not True:
            raise CandidatePacketError(
                "Selected-topic emission requires selected_for_additional_trial=True from an explicit later user request."
            )
        if packet_report.get("selected_for_additional_trial") not in (None, True):
            raise CandidatePacketError("Packet report trial-selection state conflicts with the candidate packet.")
        if packet.get("main_rules_promotion_approved") is not False:
            raise CandidatePacketError("Additional-stage emission requires main_rules_promotion_approved=False.")
        if packet_report.get("main_rules_promotion_approved") not in (None, False):
            raise CandidatePacketError("Packet report must not approve Main RULES promotion.")
        if as_text_list(packet.get("stop_gates")):
            raise CandidatePacketError("Selected-topic emission refused because packet stop gates are present.")

        proposed = packet.get("proposed_additional_rule")
        if not isinstance(proposed, dict):
            raise CandidatePacketError("candidate_packet.proposed_additional_rule is required for emission.")
        relative_path = normalize_relative_path(str(proposed.get("relative_path") or ""))
        root, destination = resolve_destination(selected_root, relative_path)
        resolved_root = root
        destination_key = str(destination)
        if destination_key in destinations:
            raise CandidatePacketError(
                f"Selected-topic emission contains duplicate destination: {relative_path}"
            )
        destinations.add(destination_key)
        if destination.exists() or destination.is_symlink():
            raise CandidatePacketError(
                f"Selected-topic emission refuses existing destination: {relative_path}"
            )

        material = render_additional_rule(packet_report)
        validation = validate_standalone_artifact(material)
        if not validation["valid"]:
            raise CandidatePacketError(
                f"Selected-topic emission refused invalid standalone artifact: {relative_path}"
            )
        items.append(
            {
                "destination_path": destination_key,
                "destination_relative_path": relative_path,
                "preview_material": material,
                "bytes_planned": len(material.encode("utf-8")),
                "standalone_validation": validation,
                "selected_for_additional_trial": True,
                "main_rules_promotion_approved": False,
            }
        )

    return {
        "tool": "memory-context-intelligence",
        "mode": "emit-selected",
        "status": "preflight-passed",
        "emission_model": EMISSION_MODEL,
        "all_destinations_preflighted": True,
        "selected_for_additional_trial": True,
        "main_rules_promotion_approved": False,
        "additional_root": str(resolved_root),
        "items": items,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def emit_selected_additional(
    packet_reports: list[dict[str, Any]],
    *,
    additional_root: str | None = None,
    approved_write: bool = False,
) -> dict[str, Any]:
    report = preflight_selected_emission(
        packet_reports,
        additional_root=additional_root,
    )
    created_files: list[Path] = []
    if approved_write:
        try:
            for item in report["items"]:
                destination = Path(item["destination_path"])
                destination.parent.mkdir(parents=True, exist_ok=True)
                root, rechecked_destination = resolve_destination(
                    report["additional_root"],
                    item["destination_relative_path"],
                )
                if str(root) != report["additional_root"] or rechecked_destination != destination:
                    raise CandidatePacketError(
                        f"Additional destination changed after preflight: {item['destination_relative_path']}"
                    )
                with destination.open("x", encoding="utf-8") as handle:
                    created_files.append(destination)
                    handle.write(item["preview_material"])
        except (OSError, CandidatePacketError) as exc:
            for created in reversed(created_files):
                try:
                    created.unlink()
                except OSError:
                    pass
            raise CandidatePacketError(
                f"Selected-topic batch write failed; files created by this call were rolled back: {exc}"
            ) from exc

    status = "emitted" if approved_write else "preview"
    for item in report["items"]:
        item.update(
            {
                "status": status,
                "approved_write": approved_write,
                "dry_run": not approved_write,
                "artifact_topic_scope": SINGLE_TOPIC_ARTIFACT_SCOPE,
                "selected_topic_count": 1,
                "multi_topic_combination_allowed": False,
                "additional_emission_performed": approved_write,
                "main_rules_mutation_performed": False,
                "install_or_publication_performed": False,
            }
        )
    report.update(
        {
            "status": status,
            "approved_write": approved_write,
            "dry_run": not approved_write,
            "additional_emission_performed": approved_write,
            "notes": [
                "Dry-run preview only; no file was written."
                if not approved_write
                else "The complete selected-topic set passed preflight and was written with exclusive create semantics.",
                "Existing additional-stage artifacts were not overwritten.",
                "Main RULES mutation was not performed.",
            ],
        }
    )
    return report


def emit_additional(
    packet_report: dict[str, Any],
    *,
    additional_root: str | None = None,
    approved_write: bool = False,
) -> dict[str, Any]:
    return emit_selected_additional(
        [packet_report],
        additional_root=additional_root,
        approved_write=approved_write,
    )["items"][0]


def build_packet_from_args(args: argparse.Namespace) -> dict[str, Any]:
    if bool(args.orchestration_report) == bool(args.candidate_input):
        raise CandidatePacketError("Provide exactly one of --orchestration-report or --candidate-input.")
    source = load_json_input(args.orchestration_report or args.candidate_input)
    candidate_input = extract_candidate_input(source)
    return build_candidate_packet(
        candidate_input,
        owner_domain=args.owner_domain,
        main_rule_target=args.main_rule_target,
        integration_anchors=args.integration_anchor,
        additional_name=args.additional_name,
        additional_relative_path=args.additional_relative_path,
        selected_for_additional_trial=args.selected_for_additional_trial,
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
            )
        elif args.command == "emit-selected":
            packet_reports = [load_json_input(path) for path in args.packet_report]
            report = emit_selected_additional(
                packet_reports,
                additional_root=args.additional_root,
                approved_write=args.approved_write,
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
