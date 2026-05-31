#!/usr/bin/env python3
"""Bounded native-agent lane orchestration for memory-context-intelligence.

This helper composes the existing intake/signals/choose/enrich outputs into four
runtime-local lane findings: Trace Scout, Research Scout, Source-Trust Reviewer,
and Synthesis Lead. It simulates native-agent orchestration deterministically in
process; it does not spawn external agents, build candidate packets, write
/additional/, install anything, or mutate main RULES.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

LANE_TRACE = "trace-scout"
LANE_RESEARCH = "research-scout"
LANE_SOURCE_TRUST = "source-trust-reviewer"
LANE_SYNTHESIS = "synthesis-lead"
LANE_ORDER = (LANE_TRACE, LANE_RESEARCH, LANE_SOURCE_TRUST, LANE_SYNTHESIS)


class OrchestrationError(ValueError):
    """Raised when orchestration input is malformed."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence orchestrate",
        description=(
            "Run deterministic runtime-local orchestration for Trace Scout, Research Scout, "
            "Source-Trust Reviewer, and Synthesis Lead. No external agent processes or writes."
        ),
    )
    parser.add_argument("--intake-report", help="Optional phase-008 intake JSON path.")
    parser.add_argument("--signals-report", help="Optional phase-009 signals JSON path.")
    parser.add_argument("--selection-report", help="Optional phase-010 choose JSON path.")
    parser.add_argument("--enrichment-report", help="Optional phase-011 enrich JSON path.")
    parser.add_argument(
        "--sources-fixture",
        help=(
            "Optional controlled/recorded source fixture. Used only with --selection-report "
            "when --enrichment-report is not supplied."
        ),
    )
    parser.add_argument(
        "--max-sources",
        type=int,
        default=8,
        help="Maximum controlled source records to pass to phase-011 enrichment, capped there at 20.",
    )
    return parser.parse_args(argv)


def load_json_input(path_value: str | None) -> dict[str, Any] | None:
    if not path_value:
        return None
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise OrchestrationError(f"JSON input must be an object: {path}")
    return loaded


def load_research_enrichment_module() -> Any:
    module_path = Path(__file__).with_name("research_enrichment.py")
    spec = importlib.util.spec_from_file_location("mci_research_enrichment_for_orchestration", module_path)
    if spec is None or spec.loader is None:
        raise OrchestrationError("Unable to load research_enrichment.py for orchestration.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_source_fixture(path_value: str | None) -> dict[str, Any] | list[dict[str, Any]] | None:
    if not path_value:
        return None
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if isinstance(loaded, dict):
        return loaded
    if isinstance(loaded, list) and all(isinstance(item, dict) for item in loaded):
        return loaded
    raise OrchestrationError("Sources fixture must be an object with sources[] or a list of source objects.")


def build_or_load_enrichment(
    selection_report: dict[str, Any] | None,
    enrichment_report: dict[str, Any] | None,
    *,
    source_fixture: dict[str, Any] | list[dict[str, Any]] | None = None,
    max_sources: int = 8,
) -> dict[str, Any] | None:
    if enrichment_report is not None:
        return enrichment_report
    if selection_report is None:
        return None
    research_enrichment = load_research_enrichment_module()
    return research_enrichment.build_enrichment(
        selection_report,
        source_fixture=source_fixture,
        max_sources=max_sources,
    )


def selected_topic(selection_report: dict[str, Any] | None, enrichment_report: dict[str, Any] | None) -> dict[str, Any] | None:
    if isinstance(selection_report, dict) and isinstance(selection_report.get("selected_topic"), dict):
        return selection_report["selected_topic"]
    if isinstance(enrichment_report, dict):
        summary = enrichment_report.get("enriched_topic_summary")
        if isinstance(summary, dict) and isinstance(summary.get("local_memory_signal"), dict):
            signal = summary["local_memory_signal"]
            return {
                "id": signal.get("topic_id"),
                "title": signal.get("title"),
                "purpose": signal.get("purpose"),
                "why_surfaced": signal.get("why_surfaced"),
                "confidence": signal.get("confidence"),
                "evidence_label": signal.get("evidence_label"),
                "source_signal_ids": signal.get("source_signal_ids", []),
                "carry_forward_allowed": True,
            }
    return None


def signal_anchors(signals_report: dict[str, Any] | None, limit: int = 12) -> list[dict[str, Any]]:
    anchors: list[dict[str, Any]] = []
    if not isinstance(signals_report, dict):
        return anchors
    for signal in signals_report.get("ranked_signals", []) or []:
        if not isinstance(signal, dict):
            continue
        for record in signal.get("records", []) or []:
            if not isinstance(record, dict):
                continue
            anchors.append(
                {
                    "signal_id": signal.get("id"),
                    "signal_rank": signal.get("rank"),
                    "shard": record.get("shard"),
                    "section": record.get("section"),
                    "content_preview": record.get("content_preview"),
                }
            )
            if len(anchors) >= limit:
                return anchors
    return anchors


def reviewed_source_anchors(enrichment_report: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(enrichment_report, dict):
        return []
    anchors: list[dict[str, Any]] = []
    for source in enrichment_report.get("reviewed_sources", []) or []:
        if not isinstance(source, dict):
            continue
        anchors.append(
            {
                "source_id": source.get("id"),
                "title": source.get("title"),
                "url": source.get("url"),
                "trust_tier": source.get("trust_tier"),
                "freshness": (source.get("freshness") or {}).get("classification")
                if isinstance(source.get("freshness"), dict)
                else None,
                "conflicting": source.get("conflicting"),
                "weak_source": source.get("weak_source"),
            }
        )
    return anchors


def lane_finding(
    *,
    lane_id: str,
    lane_name: str,
    status: str,
    checked_scope: list[str],
    anchors: list[dict[str, Any]],
    source_basis: list[str],
    findings: dict[str, Any],
    conflicts_uncertainty: list[str],
    stop_gates: list[str],
    leader_verification_needs: list[str],
) -> dict[str, Any]:
    return {
        "lane_id": lane_id,
        "lane_name": lane_name,
        "status": status,
        "checked_scope": checked_scope,
        "anchors": anchors,
        "source_basis": source_basis,
        "findings": findings,
        "conflicts_uncertainty": conflicts_uncertainty,
        "stop_gates": stop_gates,
        "leader_verification_needs": leader_verification_needs,
        "evidence_input_only": True,
    }


def trace_lane(
    intake_report: dict[str, Any] | None,
    signals_report: dict[str, Any] | None,
    topic: dict[str, Any] | None,
) -> dict[str, Any]:
    checked_scope: list[str] = []
    source_basis: list[str] = []
    conflicts_uncertainty: list[str] = []
    stop_gates: list[str] = []

    if isinstance(intake_report, dict):
        source = intake_report.get("source", {}) if isinstance(intake_report.get("source"), dict) else {}
        scope = intake_report.get("scope", {}) if isinstance(intake_report.get("scope"), dict) else {}
        checked_scope.append(
            f"intake status={intake_report.get('status')} filters={scope.get('filters', [])}"
        )
        source_basis.append("phase-008 intake report")
        freshness = intake_report.get("freshness", {}) if isinstance(intake_report.get("freshness"), dict) else {}
        if intake_report.get("status") in {"stale", "insufficient", "unavailable"}:
            conflicts_uncertainty.append(f"intake status is {intake_report.get('status')}")
        if freshness.get("classification") == "stale":
            conflicts_uncertainty.append("intake freshness is stale")
        if source.get("available") is False:
            stop_gates.append("memory trace source unavailable in intake report")

    ranked_signals = signals_report.get("ranked_signals", []) if isinstance(signals_report, dict) else []
    topic_candidates = signals_report.get("topic_candidates", []) if isinstance(signals_report, dict) else []
    if isinstance(signals_report, dict):
        checked_scope.append(
            f"signals status={signals_report.get('status')} ranked={len(ranked_signals or [])} topics={len(topic_candidates or [])}"
        )
        source_basis.append("phase-009 signals report")
    else:
        stop_gates.append("signals report missing; trace lane cannot inspect ranked trace signals")

    low_confidence = [
        str(signal.get("id"))
        for signal in ranked_signals or []
        if isinstance(signal, dict) and signal.get("confidence") == "low"
    ]
    if low_confidence:
        conflicts_uncertainty.append(f"low-confidence trace signals: {', '.join(low_confidence)}")
    if not topic_candidates and ranked_signals:
        conflicts_uncertainty.append("trace signals exist but no promotable topic candidates were produced")
    if topic is None:
        conflicts_uncertainty.append("no selected topic is present yet; later synthesis cannot build candidate input")

    status = "findings-available" if ranked_signals else "stopped"
    return lane_finding(
        lane_id=LANE_TRACE,
        lane_name="Trace Scout",
        status=status,
        checked_scope=checked_scope,
        anchors=signal_anchors(signals_report),
        source_basis=source_basis,
        findings={
            "ranked_signal_count": len(ranked_signals or []),
            "topic_candidate_count": len(topic_candidates or []),
            "selected_topic_id": topic.get("id") if isinstance(topic, dict) else None,
            "top_signal_ids": [
                signal.get("id") for signal in (ranked_signals or [])[:5] if isinstance(signal, dict)
            ],
        },
        conflicts_uncertainty=conflicts_uncertainty,
        stop_gates=stop_gates,
        leader_verification_needs=[
            "Verify material trace anchors against the original memory trace before phase-013 candidate packet input.",
            "Confirm the selected topic still matches the trace scope before carrying forward.",
        ],
    )


def research_lane(topic: dict[str, Any] | None, enrichment_report: dict[str, Any] | None) -> dict[str, Any]:
    if topic is None:
        return lane_finding(
            lane_id=LANE_RESEARCH,
            lane_name="Research Scout",
            status="stopped",
            checked_scope=[],
            anchors=[],
            source_basis=[],
            findings={"selected_topic_id": None, "research_evaluated": False},
            conflicts_uncertainty=["Research lane requires one selected topic."],
            stop_gates=["selected topic missing"],
            leader_verification_needs=["Select exactly one topic before research or synthesis carry-forward."],
        )

    if not isinstance(enrichment_report, dict):
        return lane_finding(
            lane_id=LANE_RESEARCH,
            lane_name="Research Scout",
            status="stopped",
            checked_scope=[f"selected topic={topic.get('id') or 'unknown'}"],
            anchors=[],
            source_basis=["phase-010 selected topic"],
            findings={"selected_topic_id": topic.get("id"), "research_evaluated": False},
            conflicts_uncertainty=["No enrichment report or controlled source fixture was supplied."],
            stop_gates=["research evidence missing"],
            leader_verification_needs=["Provide enrichment output or controlled source fixtures when broader support is needed."],
        )

    decision = enrichment_report.get("enrichment_decision", {}) if isinstance(enrichment_report.get("enrichment_decision"), dict) else {}
    plan = enrichment_report.get("source_query_plan", {}) if isinstance(enrichment_report.get("source_query_plan"), dict) else {}
    source_fixture = enrichment_report.get("source_fixture", {}) if isinstance(enrichment_report.get("source_fixture"), dict) else {}
    reviewed_sources = enrichment_report.get("reviewed_sources", []) or []
    conflicts_uncertainty: list[str] = []
    stop_gates: list[str] = []

    gate_result = str(decision.get("gate_result") or "unknown")
    if gate_result == "research-needed-no-sources":
        conflicts_uncertainty.append("Research was needed, but no controlled source fixture was available.")
        stop_gates.append("research-needed topic lacks controlled source evidence")
    elif enrichment_report.get("status") == "research-skipped":
        conflicts_uncertainty.append(str(decision.get("reason") or "Research was skipped by enrichment gate."))

    return lane_finding(
        lane_id=LANE_RESEARCH,
        lane_name="Research Scout",
        status=str(enrichment_report.get("status") or "unknown"),
        checked_scope=[
            f"selected topic={topic.get('id') or enrichment_report.get('selected_topic_id')}",
            f"enrichment gate={gate_result}",
            f"controlled sources reviewed={len(reviewed_sources)}",
        ],
        anchors=reviewed_source_anchors(enrichment_report),
        source_basis=[
            "phase-010 selected topic",
            "phase-011 enrichment decision/output",
            "controlled source fixture" if source_fixture.get("provided") else "no controlled source fixture",
        ],
        findings={
            "selected_topic_id": topic.get("id") or enrichment_report.get("selected_topic_id"),
            "research_needed": decision.get("research_needed"),
            "gate_result": gate_result,
            "query_plan_required": plan.get("required"),
            "query_families": plan.get("query_families", []),
            "source_fixture": source_fixture,
            "reviewed_source_count": len(reviewed_sources),
        },
        conflicts_uncertainty=conflicts_uncertainty,
        stop_gates=stop_gates,
        leader_verification_needs=[
            "Verify controlled source records directly before treating external support as phase-013 input.",
            "Confirm no live web refresh is being claimed from recorded fixture data.",
        ],
    )


def source_trust_lane(enrichment_report: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(enrichment_report, dict):
        return lane_finding(
            lane_id=LANE_SOURCE_TRUST,
            lane_name="Source-Trust Reviewer",
            status="stopped",
            checked_scope=[],
            anchors=[],
            source_basis=[],
            findings={"sources_reviewed": 0},
            conflicts_uncertainty=["Source-trust lane requires enrichment output with reviewed sources."],
            stop_gates=["source set missing"],
            leader_verification_needs=["Run or provide enrichment before source-trust review."],
        )

    reviewed_sources = enrichment_report.get("reviewed_sources", []) or []
    trust = enrichment_report.get("source_trust_notes", {}) if isinstance(enrichment_report.get("source_trust_notes"), dict) else {}
    freshness = enrichment_report.get("freshness_notes", {}) if isinstance(enrichment_report.get("freshness_notes"), dict) else {}
    conflicts = enrichment_report.get("conflict_handling", {}) if isinstance(enrichment_report.get("conflict_handling"), dict) else {}
    conflicts_uncertainty: list[str] = []
    stop_gates: list[str] = []

    if not reviewed_sources:
        conflicts_uncertainty.append("No reviewed sources are present; source-trust review has no source set.")
        if enrichment_report.get("status") != "research-skipped":
            stop_gates.append("reviewed source set missing")
    if conflicts.get("conflicts_found"):
        conflicts_uncertainty.append("Explicit source conflicts were found in the reviewed source set.")
        stop_gates.append("leader must resolve source conflicts before strengthening candidate claims")
    stale_or_unknown = freshness.get("stale_or_unknown_sources", []) or []
    if stale_or_unknown:
        conflicts_uncertainty.append(
            "stale or unknown source freshness: " + ", ".join(str(item) for item in stale_or_unknown)
        )
    weak_sources = trust.get("weak_sources", []) or []
    if weak_sources:
        conflicts_uncertainty.append("weak sources are context only: " + ", ".join(str(item) for item in weak_sources))

    status = "reviewed" if reviewed_sources else "not-needed-or-stopped"
    return lane_finding(
        lane_id=LANE_SOURCE_TRUST,
        lane_name="Source-Trust Reviewer",
        status=status,
        checked_scope=[
            f"reviewed sources={len(reviewed_sources)}",
            f"strong sources={len(trust.get('strong_sources', []) or [])}",
            f"weak sources={len(weak_sources)}",
        ],
        anchors=reviewed_source_anchors(enrichment_report),
        source_basis=["phase-011 source trust notes", "phase-011 freshness notes", "phase-011 conflict handling"],
        findings={
            "source_trust_notes": trust,
            "freshness_notes": freshness,
            "conflict_handling": conflicts,
        },
        conflicts_uncertainty=conflicts_uncertainty,
        stop_gates=stop_gates,
        leader_verification_needs=[
            "Inspect strong-source constraints before treating them as hard candidate constraints.",
            "Keep weak or conflicting sources out of hard constraints unless stronger evidence settles them.",
        ],
    )


def synthesis_lane(lanes: list[dict[str, Any]], topic: dict[str, Any] | None) -> dict[str, Any]:
    lane_by_id = {lane["lane_id"]: lane for lane in lanes}
    all_stop_gates = [gate for lane in lanes for gate in lane.get("stop_gates", [])]
    all_uncertainty = [item for lane in lanes for item in lane.get("conflicts_uncertainty", [])]
    all_leader_needs = []
    for lane in lanes:
        for need in lane.get("leader_verification_needs", []):
            if need not in all_leader_needs:
                all_leader_needs.append(need)

    trace_available = lane_by_id.get(LANE_TRACE, {}).get("status") == "findings-available"
    source_conflicts = bool(lane_by_id.get(LANE_SOURCE_TRUST, {}).get("stop_gates"))
    selected_topic_present = isinstance(topic, dict)

    if selected_topic_present and trace_available and not all_stop_gates:
        readiness = "ready-for-phase-013-input"
    elif selected_topic_present and trace_available:
        readiness = "phase-013-input-with-stop-gates"
    elif trace_available:
        readiness = "trace-only-needs-topic-selection"
    else:
        readiness = "blocked-insufficient-trace-input"

    findings = {
        "selected_topic": topic,
        "readiness_for_phase_013_candidate_packet_input": readiness,
        "candidate_packet_input_ready": readiness == "ready-for-phase-013-input",
        "candidate_packet_built": False,
        "trace_lane_status": lane_by_id.get(LANE_TRACE, {}).get("status"),
        "research_lane_status": lane_by_id.get(LANE_RESEARCH, {}).get("status"),
        "source_trust_lane_status": lane_by_id.get(LANE_SOURCE_TRUST, {}).get("status"),
        "source_conflicts_require_leader_review": source_conflicts,
        "phase_013_candidate_input": {
            "model_version": "phase-012-orchestration-result-v1",
            "selected_topic": topic,
            "lane_ids": [lane["lane_id"] for lane in lanes],
            "trace_anchors": lane_by_id.get(LANE_TRACE, {}).get("anchors", []),
            "source_anchors": lane_by_id.get(LANE_RESEARCH, {}).get("anchors", []),
            "blocking_stop_gates": all_stop_gates,
            "conflicts_uncertainty": all_uncertainty,
            "leader_verification_needs": all_leader_needs,
            "candidate_packet_built": False,
            "additional_emission_performed": False,
            "main_rules_mutation_performed": False,
        },
    }

    return lane_finding(
        lane_id=LANE_SYNTHESIS,
        lane_name="Synthesis Lead",
        status=readiness,
        checked_scope=[f"lanes synthesized={', '.join(lane['lane_id'] for lane in lanes)}"],
        anchors=[{"lane_id": lane["lane_id"], "status": lane["status"]} for lane in lanes],
        source_basis=["Trace Scout finding", "Research Scout finding", "Source-Trust Reviewer finding"],
        findings=findings,
        conflicts_uncertainty=all_uncertainty,
        stop_gates=all_stop_gates,
        leader_verification_needs=all_leader_needs
        + ["Treat this orchestration output as phase-013 input only, not as a candidate packet."],
    )


def boundary_flags() -> dict[str, Any]:
    return {
        "native_agent_orchestration_performed": True,
        "native_agent_orchestration_mode": "runtime-local-simulation",
        "external_agent_process_spawned": False,
        "live_web_access_performed": False,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def build_orchestration(
    *,
    intake_report: dict[str, Any] | None = None,
    signals_report: dict[str, Any] | None = None,
    selection_report: dict[str, Any] | None = None,
    enrichment_report: dict[str, Any] | None = None,
    source_fixture: dict[str, Any] | list[dict[str, Any]] | None = None,
    max_sources: int = 8,
) -> dict[str, Any]:
    enrichment = build_or_load_enrichment(
        selection_report,
        enrichment_report,
        source_fixture=source_fixture,
        max_sources=max_sources,
    )
    topic = selected_topic(selection_report, enrichment)
    trace = trace_lane(intake_report, signals_report, topic)
    research = research_lane(topic, enrichment)
    source_trust = source_trust_lane(enrichment)
    synthesis = synthesis_lane([trace, research, source_trust], topic)
    lanes = [trace, research, source_trust, synthesis]

    stop_gates = synthesis["stop_gates"]
    if synthesis["status"] == "ready-for-phase-013-input":
        status = "orchestrated"
    elif synthesis["status"] == "trace-only-needs-topic-selection":
        status = "trace-only-orchestrated"
    else:
        status = "orchestrated-with-stop-gates" if lanes else "stopped"

    return {
        "tool": "memory-context-intelligence",
        "mode": "orchestrate",
        "status": status,
        "orchestration_result_model": "phase-012-bounded-native-agent-lanes-v1",
        "lane_order": list(LANE_ORDER),
        "lane_findings": lanes,
        "selected_topic_id": topic.get("id") if isinstance(topic, dict) else None,
        "result_summary": {
            "lane_count": len(lanes),
            "stop_gate_count": len(stop_gates),
            "conflict_or_uncertainty_count": len(synthesis["conflicts_uncertainty"]),
            "phase_013_candidate_input_ready": synthesis["findings"]["candidate_packet_input_ready"],
        },
        "phase_013_candidate_input": synthesis["findings"]["phase_013_candidate_input"],
        "notes": [
            "Phase 012 orchestration is runtime-local and deterministic; no external agent process is spawned.",
            "Lane findings are evidence input for leader review, not final proof or RULES authority.",
            "Candidate packet building has not been performed by orchestrate mode.",
            "/additional/ emission has not been performed by orchestrate mode.",
            "Main RULES mutation has not been performed by orchestrate mode.",
        ],
        **boundary_flags(),
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        intake_report = load_json_input(args.intake_report)
        signals_report = load_json_input(args.signals_report)
        selection_report = load_json_input(args.selection_report)
        enrichment_report = load_json_input(args.enrichment_report)
        source_fixture = load_source_fixture(args.sources_fixture)
        report = build_orchestration(
            intake_report=intake_report,
            signals_report=signals_report,
            selection_report=selection_report,
            enrichment_report=enrichment_report,
            source_fixture=source_fixture,
            max_sources=args.max_sources,
        )
    except (OSError, json.JSONDecodeError, OrchestrationError) as exc:
        print(f"memory-context-intelligence orchestrate: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
