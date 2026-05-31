#!/usr/bin/env python3
"""Phase-014 deterministic historical replay for memory-context-intelligence.

This helper runs the existing runtime chain over a bounded historical memory
sample and returns one structured replay report. It is preview/no-write only: no
approved additional writes, install, publication, live web access, external agent
process spawning, or main RULES mutation are available from this command.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

LIB_ROOT = Path(__file__).resolve().parent
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

import candidate_packet
import intake
import orchestration
import presentation
import research_enrichment
import signals

REPLAY_MODEL = "phase-014-historical-replay-v1"
QUALITY_FIELDS = (
    "purpose",
    "why_surfaced",
    "expected_behavior_impact",
    "high_level_mechanism",
    "expected_output",
)
BOUNDARY_KEYS = (
    "additional_emission_performed",
    "main_rules_mutation_performed",
    "install_or_publication_performed",
    "live_web_access_performed",
    "external_agent_process_spawned",
)


class HistoricalReplayError(ValueError):
    """Raised when replay input or stage execution is invalid."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence replay",
        description=(
            "Run a deterministic bounded historical replay through intake, signals, "
            "present/choose, enrichment, orchestration, packet, and dry-run emit preview. "
            "No writes or main RULES mutation are available."
        ),
    )
    parser.add_argument(
        "--memory-root",
        help=(
            "Explicit memsearch memory root. If omitted, intake may use "
            "MEMORY_CONTEXT_INTELLIGENCE_MEMORY_ROOT or MCI_MEMORY_ROOT."
        ),
    )
    parser.add_argument("--scope", action="append", default=[], help="Optional intake scope filter. May repeat.")
    parser.add_argument("--max-shards", type=int, default=3, help="Daily shards to consider through intake.")
    parser.add_argument("--max-records", type=int, default=8, help="Records to emit/analyze through replay.")
    parser.add_argument("--max-chars", type=int, default=6000, help="Total intake sample chars.")
    parser.add_argument("--max-shard-bytes", type=int, default=65536, help="Bytes read per memory shard.")
    parser.add_argument("--max-age-days", type=int, default=30, help="Freshness threshold for latest shard.")
    parser.add_argument("--max-topics", type=int, default=5, help="Maximum topic candidates to promote in replay.")
    parser.add_argument("--topic-id", help="Topic id or rank to choose. Defaults to the first replay topic.")
    parser.add_argument(
        "--output-mode",
        choices=presentation.OUTPUT_MODES,
        default="auto",
        help="Presentation/choose output mode.",
    )
    parser.add_argument("--language", help="Presentation language hint or fixed-language selector.")
    parser.add_argument(
        "--sources-fixture",
        help="Optional controlled/recorded source fixture for enrichment. Omit for explicit no-live-web skip.",
    )
    parser.add_argument("--max-sources", type=int, default=8, help="Maximum fixture sources to evaluate.")
    parser.add_argument("--owner-domain", help="Optional explicit owner-domain mapping for packet review.")
    parser.add_argument("--main-rule-target", help="Optional intended main-rule target for packet review.")
    parser.add_argument("--additional-name", help="Optional additional-stage trial rule name for packet preview.")
    parser.add_argument(
        "--additional-relative-path",
        help="Optional safe relative additional-stage path for packet preview.",
    )
    parser.add_argument(
        "--additional-root",
        help="Optional additional-stage root used only to resolve the dry-run preview destination.",
    )
    parser.add_argument(
        "--skip-emit-preview",
        action="store_true",
        help="Skip the dry-run emit preview stage. Writes are still unavailable either way.",
    )
    return parser.parse_args(argv)


def load_json_fixture(path_value: str | None) -> dict[str, Any] | list[dict[str, Any]] | None:
    if not path_value:
        return None
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if isinstance(loaded, dict):
        return loaded
    if isinstance(loaded, list) and all(isinstance(item, dict) for item in loaded):
        return loaded
    raise HistoricalReplayError("Sources fixture must be an object with sources[] or a list of source objects.")


def stage_entry(stage: str, status: str, *, ok: bool, summary: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "stage": stage,
        "status": status,
        "ok": ok,
        "summary": summary or {},
    }


def choose_replay_topic(signals_report: dict[str, Any], requested_topic_id: str | None) -> str:
    topics = signals_report.get("topic_candidates", [])
    if not isinstance(topics, list) or not topics:
        raise HistoricalReplayError("Replay cannot choose a topic because signals produced no topic candidates.")
    if requested_topic_id:
        return requested_topic_id
    first = topics[0]
    topic_id = first.get("id") or first.get("rank") or "1"
    return str(topic_id)


def topic_quality_notes(signals_report: dict[str, Any]) -> list[dict[str, Any]]:
    topics = signals_report.get("topic_candidates", [])
    if not isinstance(topics, list) or not topics:
        return [
            {
                "topic_id": None,
                "quality": "no-topic-candidates",
                "note": "No promotable topic candidates were produced from the bounded replay input.",
            }
        ]

    notes: list[dict[str, Any]] = []
    for topic in topics:
        if not isinstance(topic, dict):
            continue
        missing_fields = [field for field in QUALITY_FIELDS if not str(topic.get(field) or "").strip()]
        title = str(topic.get("title") or "").strip()
        label_like = len(title.split()) <= 2
        quality = "reviewable" if not missing_fields and not label_like else "needs-review"
        notes.append(
            {
                "topic_id": topic.get("id"),
                "title": title,
                "quality": quality,
                "confidence": topic.get("confidence"),
                "evidence_label": topic.get("evidence_label"),
                "missing_explanation_fields": missing_fields,
                "label_like_title": label_like,
                "note": (
                    "Topic has the core explanation fields needed for replay review."
                    if quality == "reviewable"
                    else "Topic should be reviewed before live additional-stage trial use."
                ),
            }
        )
    return notes


def weak_signal_findings(signals_report: dict[str, Any]) -> list[dict[str, Any]]:
    ranked = signals_report.get("ranked_signals", [])
    topics = signals_report.get("topic_candidates", [])
    if not isinstance(ranked, list):
        ranked = []
    if not isinstance(topics, list):
        topics = []
    promoted_signal_ids = {
        str(signal_id)
        for topic in topics
        if isinstance(topic, dict)
        for signal_id in topic.get("source_signal_ids", []) or []
    }

    findings: list[dict[str, Any]] = []
    for signal in ranked:
        if not isinstance(signal, dict):
            continue
        signal_id = str(signal.get("id") or "")
        confidence = str(signal.get("confidence") or "unknown")
        evidence_label = str(signal.get("evidence_label") or "")
        promoted = signal_id in promoted_signal_ids
        weak = confidence == "low" or any(
            marker in evidence_label for marker in ("single-observation", "insufficient", "stale")
        )
        if weak or (promoted and confidence == "low"):
            findings.append(
                {
                    "signal_id": signal.get("id"),
                    "rank": signal.get("rank"),
                    "kind": signal.get("kind"),
                    "confidence": confidence,
                    "evidence_label": evidence_label,
                    "promoted_to_topic": promoted,
                    "finding": "possible-false-positive" if promoted and confidence == "low" else "kept-advisory-or-low-confidence",
                    "note": (
                        "Low-confidence signal was promoted and needs leader review before phase-015."
                        if promoted and confidence == "low"
                        else "Weak or single-observation signal remains a replay review finding, not promotion proof."
                    ),
                }
            )
    if not findings:
        findings.append(
            {
                "signal_id": None,
                "finding": "no-low-confidence-promotion-detected",
                "note": "Replay did not detect low-confidence signals being promoted as hard constraints.",
            }
        )
    return findings


def lane_behavior_summary(orchestration_report: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(orchestration_report, dict):
        return []
    lanes = orchestration_report.get("lane_findings", [])
    if not isinstance(lanes, list):
        return []
    return [
        {
            "lane_id": lane.get("lane_id"),
            "lane_name": lane.get("lane_name"),
            "status": lane.get("status"),
            "evidence_input_only": bool(lane.get("evidence_input_only")),
            "stop_gate_count": len(lane.get("stop_gates", []) or []),
            "conflict_or_uncertainty_count": len(lane.get("conflicts_uncertainty", []) or []),
            "leader_verification_need_count": len(lane.get("leader_verification_needs", []) or []),
        }
        for lane in lanes
        if isinstance(lane, dict)
    ]


def packet_safety_findings(packet_report: dict[str, Any] | None, emit_preview: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(packet_report, dict):
        return {"packet_built": False, "safe_for_phase_015": False, "findings": ["packet was not built"]}
    packet = packet_report.get("candidate_packet", {}) if isinstance(packet_report.get("candidate_packet"), dict) else {}
    proposed = packet.get("proposed_additional_rule", {}) if isinstance(packet.get("proposed_additional_rule"), dict) else {}
    stop_gates = packet.get("stop_gates", []) or []
    findings = [
        "Packet building emitted structured stdout only.",
        "Proposed additional path is relative to the selected additional root.",
        "Trial-stage-only status remains visible in packet output.",
    ]
    if stop_gates:
        findings.append("Packet has stop gates that must be cleared before any approved additional-stage write.")
    if isinstance(emit_preview, dict):
        findings.append("Emit stage ran in dry-run preview mode only.")
    return {
        "packet_built": bool(packet_report.get("candidate_packet_built")),
        "packet_status": packet_report.get("status"),
        "stop_gate_count": len(stop_gates),
        "stop_gates": stop_gates,
        "leader_verification_need_count": len(packet.get("leader_verification_needs", []) or []),
        "proposed_additional_relative_path": proposed.get("relative_path"),
        "trial_stage_only": bool(proposed.get("trial_stage_only")),
        "emit_preview_status": emit_preview.get("status") if isinstance(emit_preview, dict) else "skipped",
        "findings": findings,
        "safe_for_phase_015": not stop_gates,
    }


def any_boundary_flag(reports: list[dict[str, Any] | None], key: str) -> bool:
    return any(bool(report.get(key)) for report in reports if isinstance(report, dict))


def authority_boundary_audit(reports: list[dict[str, Any] | None], emit_preview: dict[str, Any] | None) -> dict[str, Any]:
    audit = {
        "approved_write_available_in_replay": False,
        "approved_write_requested": False,
        "emit_preview_performed": isinstance(emit_preview, dict),
        "emit_preview_dry_run": bool(emit_preview.get("dry_run")) if isinstance(emit_preview, dict) else None,
        "additional_emission_performed": any_boundary_flag(reports, "additional_emission_performed"),
        "main_rules_mutation_performed": any_boundary_flag(reports, "main_rules_mutation_performed"),
        "install_or_publication_performed": any_boundary_flag(reports, "install_or_publication_performed"),
        "live_web_access_performed": any_boundary_flag(reports, "live_web_access_performed"),
        "external_agent_process_spawned": any_boundary_flag(reports, "external_agent_process_spawned"),
        "preview_destination_path": emit_preview.get("destination_path") if isinstance(emit_preview, dict) else None,
    }
    audit["authority_boundary_ok"] = not any(
        bool(audit[key])
        for key in (
            "approved_write_requested",
            "additional_emission_performed",
            "main_rules_mutation_performed",
            "install_or_publication_performed",
            "live_web_access_performed",
            "external_agent_process_spawned",
        )
    )
    return audit


def adjustments_needed(
    *,
    topic_notes: list[dict[str, Any]],
    weak_findings: list[dict[str, Any]],
    orchestration_report: dict[str, Any] | None,
    packet_findings: dict[str, Any],
    boundary_audit: dict[str, Any],
) -> list[str]:
    adjustments: list[str] = []
    if any(note.get("quality") in {"needs-review", "no-topic-candidates"} for note in topic_notes):
        adjustments.append("Review topic quality before phase-015; weak or label-like topics should not enter live trial.")
    if any(item.get("finding") == "possible-false-positive" for item in weak_findings):
        adjustments.append("Tighten signal thresholds or manually reject promoted low-confidence signals before live trial.")
    if isinstance(orchestration_report, dict):
        summary = orchestration_report.get("result_summary", {}) if isinstance(orchestration_report.get("result_summary"), dict) else {}
        if int(summary.get("stop_gate_count") or 0) > 0:
            adjustments.append("Resolve orchestration stop gates or carry them as explicit phase-015 trial blockers.")
    if packet_findings.get("stop_gate_count"):
        adjustments.append("Clear packet stop gates before any approved additional-stage emission in a later phase.")
    if not boundary_audit.get("authority_boundary_ok"):
        adjustments.append("Stop before phase-015 and investigate authority-boundary violation signals.")
    return adjustments


def build_replay_report(args: argparse.Namespace) -> dict[str, Any]:
    stage_statuses: list[dict[str, Any]] = []
    source_fixture = load_json_fixture(args.sources_fixture)

    intake_args = argparse.Namespace(
        memory_root=args.memory_root,
        scope=args.scope,
        max_shards=args.max_shards,
        max_records=args.max_records,
        max_chars=args.max_chars,
        max_shard_bytes=args.max_shard_bytes,
        max_age_days=args.max_age_days,
    )
    intake_report = intake.build_report(intake_args)
    stage_statuses.append(
        stage_entry(
            "intake",
            str(intake_report.get("status")),
            ok=intake_report.get("status") in {"available", "stale"},
            summary={
                "records": len(intake_report.get("records", []) or []),
                "daily_shards_considered": (intake_report.get("source", {}) or {}).get("daily_shards_considered", []),
                "bounded_subset_only": (intake_report.get("scope", {}) or {}).get("bounded_subset_only"),
            },
        )
    )

    signals_report = signals.build_report(intake_report, max_records=args.max_records, max_topics=args.max_topics)
    stage_statuses.append(
        stage_entry(
            "signals",
            str(signals_report.get("status")),
            ok=signals_report.get("status") in {"available", "low-confidence"},
            summary=signals_report.get("limits", {}),
        )
    )

    presentation_report = presentation.build_presentation(
        signals_report,
        output_mode=args.output_mode,
        language=args.language,
    )
    stage_statuses.append(
        stage_entry(
            "present",
            str(presentation_report.get("status")),
            ok=presentation_report.get("status") == "available",
            summary={"topics_presented": len(presentation_report.get("topic_list", []) or [])},
        )
    )

    selection_report: dict[str, Any] | None = None
    enrichment_report: dict[str, Any] | None = None
    orchestration_report: dict[str, Any] | None = None
    packet_report: dict[str, Any] | None = None
    emit_preview: dict[str, Any] | None = None

    try:
        selected_topic_id = choose_replay_topic(signals_report, args.topic_id)
        selection_report = presentation.build_selection(
            signals_report,
            topic_id=selected_topic_id,
            output_mode=args.output_mode,
            language=args.language,
        )
        stage_statuses.append(
            stage_entry(
                "choose",
                str(selection_report.get("status")),
                ok=selection_report.get("status") == "selected",
                summary={"selected_topic_id": selection_report.get("selected_topic_id")},
            )
        )

        enrichment_report = research_enrichment.build_enrichment(
            selection_report,
            source_fixture=source_fixture,
            max_sources=args.max_sources,
        )
        stage_statuses.append(
            stage_entry(
                "enrich",
                str(enrichment_report.get("status")),
                ok=enrichment_report.get("status") in {"research-skipped", "research-enriched"},
                summary={
                    "decision": (
                        (enrichment_report.get("enrichment_decision") or {}).get("gate_result")
                        or (enrichment_report.get("enrichment_decision") or {}).get("result")
                    )
                    if isinstance(enrichment_report.get("enrichment_decision"), dict)
                    else None,
                    "live_web_access_performed": enrichment_report.get("live_web_access_performed"),
                },
            )
        )

        orchestration_report = orchestration.build_orchestration(
            intake_report=intake_report,
            signals_report=signals_report,
            selection_report=selection_report,
            enrichment_report=enrichment_report,
            max_sources=args.max_sources,
        )
        stage_statuses.append(
            stage_entry(
                "orchestrate",
                str(orchestration_report.get("status")),
                ok=orchestration_report.get("status") in {"orchestrated", "orchestrated-with-stop-gates"},
                summary=orchestration_report.get("result_summary", {}),
            )
        )

        packet_report = candidate_packet.build_candidate_packet(
            orchestration_report["phase_013_candidate_input"],
            owner_domain=args.owner_domain,
            main_rule_target=args.main_rule_target,
            additional_name=args.additional_name,
            additional_relative_path=args.additional_relative_path,
        )
        stage_statuses.append(
            stage_entry(
                "packet",
                str(packet_report.get("status")),
                ok=packet_report.get("status") in {"packet-built", "packet-built-with-stop-gates"},
                summary={
                    "candidate_packet_built": packet_report.get("candidate_packet_built"),
                    "stop_gate_count": len((packet_report.get("candidate_packet", {}) or {}).get("stop_gates", []) or []),
                },
            )
        )

        if args.skip_emit_preview:
            stage_statuses.append(stage_entry("emit-preview", "skipped", ok=True, summary={"dry_run": True}))
        else:
            emit_preview = candidate_packet.emit_additional(
                packet_report,
                additional_root=args.additional_root,
                approved_write=False,
                allow_overwrite=False,
            )
            stage_statuses.append(
                stage_entry(
                    "emit-preview",
                    str(emit_preview.get("status")),
                    ok=emit_preview.get("status") == "preview" and emit_preview.get("dry_run") is True,
                    summary={
                        "dry_run": emit_preview.get("dry_run"),
                        "additional_emission_performed": emit_preview.get("additional_emission_performed"),
                        "destination_relative_path": emit_preview.get("destination_relative_path"),
                    },
                )
            )
    except (HistoricalReplayError, presentation.SelectionError, candidate_packet.CandidatePacketError) as exc:
        stage_statuses.append(stage_entry("downstream-chain", "blocked", ok=False, summary={"reason": str(exc)}))

    reports = [
        intake_report,
        signals_report,
        presentation_report,
        selection_report,
        enrichment_report,
        orchestration_report,
        packet_report,
        emit_preview,
    ]
    topic_notes = topic_quality_notes(signals_report)
    weak_findings = weak_signal_findings(signals_report)
    lane_summary = lane_behavior_summary(orchestration_report)
    packet_findings = packet_safety_findings(packet_report, emit_preview)
    boundary_audit = authority_boundary_audit(reports, emit_preview)
    adjustments = adjustments_needed(
        topic_notes=topic_notes,
        weak_findings=weak_findings,
        orchestration_report=orchestration_report,
        packet_findings=packet_findings,
        boundary_audit=boundary_audit,
    )

    blocked = any(not item["ok"] and item["stage"] not in {"orchestrate", "packet"} for item in stage_statuses)
    if blocked or not boundary_audit["authority_boundary_ok"]:
        status = "replay-blocked"
    elif adjustments:
        status = "replay-completed-with-adjustments"
    else:
        status = "replay-completed"

    return {
        "tool": "memory-context-intelligence",
        "mode": "replay",
        "status": status,
        "historical_replay_model": REPLAY_MODEL,
        "bounded_historical_input": {
            "memory_root_source": (intake_report.get("source", {}) or {}).get("memory_root_source"),
            "daily_shards_discovered": (intake_report.get("source", {}) or {}).get("daily_shards_discovered"),
            "daily_shards_considered": (intake_report.get("source", {}) or {}).get("daily_shards_considered", []),
            "scope_filters": (intake_report.get("scope", {}) or {}).get("filters", []),
            "records_sampled": len(intake_report.get("records", []) or []),
            "bounded_subset_only": True,
        },
        "selected_topic": {
            "topic_id": selection_report.get("selected_topic_id") if isinstance(selection_report, dict) else None,
            "title": (selection_report.get("selected_topic", {}) or {}).get("title")
            if isinstance(selection_report, dict)
            else None,
            "confidence": (selection_report.get("selected_topic", {}) or {}).get("confidence")
            if isinstance(selection_report, dict)
            else None,
            "evidence_label": (selection_report.get("selected_topic", {}) or {}).get("evidence_label")
            if isinstance(selection_report, dict)
            else None,
        },
        "stage_statuses": stage_statuses,
        "topic_quality_notes": topic_notes,
        "false_positive_weak_signal_findings": weak_findings,
        "orchestration_lane_behavior_summary": lane_summary,
        "candidate_packet_safety_findings": packet_findings,
        "no_write_authority_boundary_audit": boundary_audit,
        "adjustments_needed_before_phase_015": adjustments,
        "notes": [
            "Historical replay uses bounded memory intake and deterministic runtime-local helpers only.",
            "Replay does not offer approved writes; emit preview is dry-run only when enabled.",
            "Replay output is validation evidence for phase 014, not live /additional/ trial proof or main RULES promotion approval.",
        ],
        "live_web_access_performed": False,
        "external_agent_process_spawned": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = build_replay_report(args)
    except (OSError, json.JSONDecodeError, HistoricalReplayError) as exc:
        print(f"memory-context-intelligence replay: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
