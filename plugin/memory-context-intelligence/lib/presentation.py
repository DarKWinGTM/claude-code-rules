#!/usr/bin/env python3
"""User-facing topic presentation and choose flow runtime.

This helper consumes the internal-only signals report from phase 009 and renders a
bounded list-first topic review. It can also record one selected topic as
structured fileless output. It does not run research enrichment, build candidate
packets, emit /additional/, or mutate main RULES.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

OUTPUT_MODES = ("auto", "native-first", "bilingual", "fixed")
SUPPORTED_LANGUAGES = ("en", "th")
TOPIC_FIELD_KEYS = (
    "purpose",
    "why_surfaced",
    "expected_behavior_impact",
    "high_level_mechanism",
    "expected_output",
    "research_need",
    "provenance_note",
    "source_scope_label",
    "source_mix_label",
    "historical_strength",
    "latest_seen",
    "current_session_confirmation",
)

RESEARCH_NOT_STARTED = (
    "Not evaluated in phase 010; research enrichment is a later phase and must "
    "not start before the user selects a topic."
)

LABELS = {
    "en": {
        "heading": "Memory-context topic candidates",
        "summary": "Review the topic list first, then choose exactly one topic before carry-forward.",
        "choice_prompt": "Choose one topic by id before any research enrichment, candidate packet building, or /additional/ emission.",
        "no_topics": "No promotable topic candidates were present in the signals report.",
        "selected_summary": "Selected topic recorded as fileless structured state.",
        "unselected_summary": "Unselected topics remain advisory only.",
        "topic_id": "Topic id",
        "rank": "Rank",
        "title": "Title",
        "purpose": "Purpose",
        "why_surfaced": "Why surfaced",
        "expected_behavior_impact": "Expected behavior impact",
        "high_level_mechanism": "High-level mechanism",
        "expected_output": "Expected output",
        "research_need": "Research need",
        "provenance_note": "Provenance",
        "source_scope_label": "Source scope",
        "source_mix_label": "Source mix",
        "historical_strength": "Historical strength",
        "latest_seen": "Latest seen",
        "current_session_confirmation": "Current-session confirmation",
    },
    "th": {
        "heading": "รายการหัวข้อจาก memory context",
        "summary": "อ่านรายการหัวข้อก่อน แล้วเลือกหนึ่งหัวข้อเท่านั้นก่อนส่งต่อขั้นถัดไป",
        "choice_prompt": "เลือกหนึ่งหัวข้อด้วย id ก่อนเริ่ม research enrichment, candidate packet หรือ /additional/ emission",
        "no_topics": "signals report ไม่มี topic candidate ที่พร้อมแสดง",
        "selected_summary": "บันทึกหัวข้อที่เลือกเป็น structured state แบบไม่เขียนไฟล์",
        "unselected_summary": "หัวข้อที่ไม่ได้เลือกยังเป็นคำแนะนำเท่านั้น",
        "topic_id": "Topic id",
        "rank": "ลำดับ",
        "title": "หัวข้อ",
        "purpose": "ใช้เพื่ออะไร",
        "why_surfaced": "ทำไมถึงถูกเสนอ",
        "expected_behavior_impact": "ผลต่อพฤติกรรมหรือ workflow",
        "high_level_mechanism": "กลไกระดับสูง",
        "expected_output": "ผลลัพธ์ที่คาดว่าจะได้",
        "research_need": "ความจำเป็นเรื่อง research",
        "provenance_note": "ที่มาของหลักฐาน",
        "source_scope_label": "ขอบเขตของแหล่งข้อมูล",
        "source_mix_label": "ชุดแหล่งข้อมูล",
        "historical_strength": "ความแรงของ pattern เชิงประวัติ",
        "latest_seen": "พบล่าสุดเมื่อ",
        "current_session_confirmation": "การยืนยันจาก current session",
    },
}

PROPOSAL_SECTION_LABELS = {
    "en": {
        "what_it_is": "What it is",
        "symptom": "Problem or symptom",
        "evidence_examples": "Evidence examples",
        "before_behavior": "Before behavior",
        "after_behavior": "After behavior",
        "improvement": "Why this improves things",
        "evidence": "Evidence used",
        "status": "Current status",
    },
    "th": {
        "what_it_is": "มันคืออะไร",
        "symptom": "อาการ/ปัญหา",
        "evidence_examples": "ตัวอย่างจากข้อมูลที่พบ",
        "before_behavior": "ก่อนปรับ (Before behavior)",
        "after_behavior": "หลังปรับ (After behavior)",
        "improvement": "ถ้าปรับแล้วจะดีขึ้นยังไง",
        "evidence": "หลักฐานที่ใช้",
        "status": "สถานะตอนนี้",
    },
}

STATUS_TAGS = ("candidate only", "advisory only", "not approved yet")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence presentation",
        description=(
            "Render phase-009 topic candidates as a user-facing list or record "
            "one selected topic as structured fileless state."
        ),
    )
    subparsers = parser.add_subparsers(dest="action", required=True)

    present = subparsers.add_parser("present", help="Render a list-first topic presentation.")
    add_common_arguments(present)

    choose = subparsers.add_parser("choose", help="Record one selected topic without starting later phases.")
    add_common_arguments(choose)
    choose.add_argument(
        "--topic-id",
        required=True,
        help="Topic id such as topic-001, or a numeric rank from the topic list.",
    )

    return parser.parse_args(argv)


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--signals-report",
        default="-",
        help="Path to phase-009 signals JSON. Use '-' or omit to read JSON from stdin.",
    )
    parser.add_argument(
        "--output-mode",
        choices=OUTPUT_MODES,
        default="auto",
        help="Presentation mode: auto, native-first, bilingual, or fixed.",
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Language hint for auto/native-first/bilingual or fixed language for fixed mode. Supported: en, th.",
    )


def load_json_input(path_value: str) -> dict[str, Any]:
    if path_value == "-":
        return json.load(sys.stdin)
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_language(value: str | None) -> str:
    if not value:
        return "en"
    normalized = value.strip().lower().replace("_", "-")
    if normalized.startswith("th"):
        return "th"
    if normalized.startswith("en"):
        return "en"
    return "en"


def detect_language(language_hint: str | None = None) -> str:
    if language_hint:
        return normalize_language(language_hint)
    for env_name in ("LC_ALL", "LC_MESSAGES", "LANG"):
        env_value = os.environ.get(env_name)
        if env_value:
            return normalize_language(env_value)
    return "en"


def active_language(output_mode: str, language: str | None = None) -> str:
    if output_mode == "fixed":
        return normalize_language(language)
    return detect_language(language)


def label(key: str, *, language: str, output_mode: str) -> str:
    native = LABELS[language][key]
    english = LABELS["en"][key]
    if output_mode == "bilingual" and native != english:
        return f"{native} / {english}"
    return native


def topic_candidates(signals_report: dict[str, Any]) -> list[dict[str, Any]]:
    raw_topics = signals_report.get("topic_candidates", [])
    if not isinstance(raw_topics, list):
        return []
    return [topic for topic in raw_topics if isinstance(topic, dict)]


def advisory_fallback_topics(signals_report: dict[str, Any]) -> list[dict[str, Any]]:
    raw_topics = signals_report.get("advisory_fallback_topics", [])
    if not isinstance(raw_topics, list):
        return []
    return [topic for topic in raw_topics if isinstance(topic, dict)]


def copy_topic_with_research_need(topic: dict[str, Any]) -> dict[str, Any]:
    copied = deepcopy(topic)
    copied.setdefault("research_need", RESEARCH_NOT_STARTED)
    return copied


def presentation_fields(topic: dict[str, Any], *, language: str, output_mode: str) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for key in TOPIC_FIELD_KEYS:
        value = topic.get(key, "")
        fields.append(
            {
                "key": key,
                "label": label(key, language=language, output_mode=output_mode),
                "value": value,
            }
        )
    return fields


def proposal_label(key: str, *, language: str) -> str:
    return PROPOSAL_SECTION_LABELS[language][key]


def canonical_status_line() -> str:
    return "; ".join(STATUS_TAGS)


def localized_title(title: str, *, language: str) -> str:
    if language != "th":
        return title
    overrides = {
        "Rewrite /memory-context-intelligence:analysis first response into operator-facing proposal output": "ทำให้คำตอบแรกของ /memory-context-intelligence:analysis ใช้งานได้ทันที",
        "Stop completion wording from outrunning verification": "หยุดสรุปว่างานเสร็จก่อนมีหลักฐานยืนยัน",
        "Clarify stop-gate handling before approval-sensitive work": "ทำให้ stop gate ก่อนงานที่ต้องขออนุมัติชัดขึ้น",
        "Clarify refresh and wait guidance before strong evidence claims": "ทำให้คำแนะนำเรื่อง refresh และ wait ไม่พาไปสรุปแรงเกินหลักฐาน",
        "Clarify evidence wording before strong claims": "ทำให้ถ้อยคำเรื่องหลักฐานชัดก่อนสรุปแรง",
        "Clarify which surface owns the user-facing analysis result": "แยกให้ชัดว่าใครเป็นเจ้าของผลลัพธ์ analysis ที่ผู้ใช้เห็น",
        "Turn recurring workflow findings into decision-ready proposals": "เปลี่ยน workflow finding ที่เกิดซ้ำให้เป็นข้อเสนอที่ตัดสินใจต่อได้ทันที",
        "Reduce repeated correction around workflow wording and review boundaries": "ลดการแก้ซ้ำเรื่องถ้อยคำ workflow และขอบเขตการ review",
        "Review workflow wording so repeated patterns read like actionable proposals": "ทบทวนถ้อยคำ workflow ให้ pattern ที่เจออ่านแล้วนำไปใช้ต่อได้",
    }
    return overrides.get(title, title)


def localized_topic_section_value(topic: dict[str, Any], *, key: str, language: str) -> str | None:
    if language != "th":
        return None
    title = str(topic.get("title") or "")
    overrides = {
        "Clarify evidence wording before strong claims": {
            "what_it_is": "ทบทวนจุดที่คำตอบอาจสรุปแรงเกินหลักฐาน เพื่อให้แยก fact, inference และ working hypothesis ออกจากกันให้ชัดก่อนตอบ",
            "symptom": "มี pattern ว่าคำตอบบางช่วงเริ่มใช้ถ้อยคำแรงเกินไป ทั้งที่หลักฐานยังไม่พอจะยืนยันข้อสรุปนั้นแบบตรง ๆ",
            "before_behavior": "ตอบแบบไหลไปสู่ข้อสรุปแรงก่อน แล้วค่อยย้อนมาอธิบายทีหลังว่าอะไรคือ fact ที่ยืนยันแล้วและอะไรยังเป็นเพียงการตีความ",
            "after_behavior": "เปิดเผยระดับความมั่นใจตั้งแต่ต้น ว่าอะไรคือ verified fact, อะไรเป็น inference, และอะไรยังเป็น working hypothesis ก่อนพาผู้ใช้อ่านต่อ",
            "improvement": "ช่วยให้ผู้ใช้เห็นทันทีว่าข้อความส่วนไหนยืนยันได้แล้ว และส่วนไหนยังต้องถือแบบระวังน้ำหนักหลักฐาน",
        },
        "Clarify which surface owns the user-facing analysis result": {
            "what_it_is": "ทบทวนว่าผลลัพธ์ analysis ที่ผู้ใช้เห็นควรถูกเล่าเป็นข้อเสนอที่ใช้งานได้ทันที ไม่ใช่ปล่อยให้กลายเป็น trace summary ภายในระบบ",
            "symptom": "มี pattern ที่ผลลัพธ์เริ่มเล่าแบบสรุป trace หรือ workflow ภายใน จนผู้ใช้ต้องเดาเองว่าประเด็นหลักและข้อเสนอจริงคืออะไร",
            "before_behavior": "เล่าผลลัพธ์แบบ generic trace-pattern summary ทำให้ผู้ใช้ยังต้องตีความต่อเองว่า analysis นี้กำลังเสนอให้แก้อะไร",
            "after_behavior": "ให้ analysis surface เป็นเจ้าของคำอธิบายหลักโดยตรง: บอกหัวข้อ ปัญหา สิ่งที่ควรเปลี่ยน และเหตุผลอย่างอ่านจบแล้วตัดสินใจต่อได้ทันที",
            "improvement": "ช่วยให้ output รอบแรกอ่านแล้วรู้เลยว่าหัวข้อคืออะไร ทำไมจึงถูกยกขึ้นมา และควรดูหรือทำอะไรต่อ",
        },
        "Turn recurring workflow findings into decision-ready proposals": {
            "what_it_is": "ทบทวน workflow finding ที่เกิดซ้ำ แล้วแปลงให้เป็นข้อเสนอที่ผู้ใช้ตัดสินใจต่อได้ทันที แทนที่จะค้างอยู่แค่ observation",
            "symptom": "มี pattern ที่เจอ blocker หรือ finding แล้วจบที่การบอกว่าเกิดอะไรขึ้น แต่ยังไม่ยกเป็น next step หรือ proposal ที่ใช้งานต่อได้จริง",
            "before_behavior": "สรุป workflow finding เป็น observation หรือ blocker note เฉย ๆ โดยยังไม่บอกชัดว่าผู้ใช้ควรเลือกทางไหนหรือเปลี่ยนอะไรต่อ",
            "after_behavior": "ยก finding เดิมขึ้นมาเป็น proposal ที่ชัดเจนขึ้น บอกทั้งสิ่งที่ควรเปลี่ยน เหตุผล และ next move ที่นำไปใช้ตัดสินใจต่อได้ทันที",
            "improvement": "ช่วยให้การ review workflow ไม่ค้างอยู่ที่การเล่าอาการ แต่จบลงด้วยข้อเสนอที่หยิบไปใช้ต่อได้เลย",
        },
    }
    return overrides.get(title, {}).get(key)


def short_recommendation_reason(topic: dict[str, Any], *, language: str) -> str:
    confirmation = str(topic.get("current_session_confirmation") or "")
    confidence = str(topic.get("confidence") or "")
    promotion_tier = str(topic.get("promotion_tier") or "promoted-candidate")
    if language == "th":
        if promotion_tier == "advisory-fallback" or confidence == "low":
            return "หัวข้อนี้ยังเป็นสัญญาณอ่อน แต่เป็น historical trace ที่แรงสุดในชุด advisory ตอนนี้ จึงถูกยกมาเป็นหัวข้อแรกแบบระวังน้ำหนักหลักฐาน"
        if confirmation == "confirmed-in-current-session":
            return "หัวข้อนี้มี pattern ซ้ำที่แรงพอและยังถูกยืนยันซ้ำใน current session ด้วย จึงเหมาะเป็นหัวข้อแรก"
        return "หัวข้อนี้มี historical trace ที่ชัดที่สุดในชุดที่เสนออยู่ตอนนี้ จึงเหมาะเป็นหัวข้อแรก"
    if promotion_tier == "advisory-fallback" or confidence == "low":
        return "This topic is still a weak signal, but it is the strongest advisory historical trace currently available, so it is surfaced first with caution."
    if confirmation == "confirmed-in-current-session":
        return "This topic has the strongest repeated pattern and is also confirmed in the current session, so it is the best first topic."
    return "This topic has the strongest repeated historical trace in the current candidate set, so it is the best first topic."


def default_bad_example(topic: dict[str, Any], *, language: str) -> str:
    title = str(topic.get("title") or "")
    if "analysis first response" in title.lower() or "/memory-context-intelligence:analysis" in title:
        if language == "th":
            return "เปิดมาด้วย progress summary, internal narration หรือชื่อหัวข้อดิบที่ยังไม่ช่วยให้ผู้ใช้ตัดสินใจต่อได้ทันที"
        return "The first response opens with progress-summary narration, internal pipeline wording, or raw topic names that still require a manual rewrite."
    if language == "th":
        return "ยังสื่อสารแบบกว้างหรือดิบเกินไปจนผู้ใช้ยังต้องตีความต่อเอง"
    return "The output still reads too raw or too generic, so the user must translate the meaning manually."


def default_good_example(topic: dict[str, Any], *, language: str) -> str:
    title = str(topic.get("title") or "")
    if "analysis first response" in title.lower() or "/memory-context-intelligence:analysis" in title:
        if language == "th":
            return "เปิดมาด้วยหัวข้อที่อ่านง่าย แนะนำหัวข้อแรกให้เลย และมี proposal ที่อธิบายปัญหา ตัวอย่าง หลักฐาน และสถานะครบในรอบแรก"
        return "The first response opens with human-readable topic titles, recommends the best first topic, and includes a proposal block with problem, examples, evidence, and status immediately."
    if language == "th":
        return "สรุปเป็นข้อเสนอที่อ่านง่าย บอกได้ทันทีว่าควรดูอะไรต่อและเพราะอะไร"
    return "The output reads like an actionable proposal, so the user can judge what to inspect next without a rewrite pass."


def render_evidence_examples(value: Any) -> str:
    if isinstance(value, list):
        examples = [str(item).strip() for item in value if str(item).strip()]
        return "\n".join(f"- {item}" for item in examples)
    text = str(value or "").strip()
    return f"- {text}" if text else ""



def proposal_sections(topic: dict[str, Any], *, language: str) -> list[dict[str, str]]:
    evidence_summary = str(topic.get("evidence_summary") or topic.get("provenance_note") or topic.get("source_mix_label") or "")
    what_it_is = localized_topic_section_value(topic, key="what_it_is", language=language) or str(topic.get("purpose") or topic.get("title") or "")
    symptom = localized_topic_section_value(topic, key="symptom", language=language) or str(
        topic.get("why_surfaced") or topic.get("expected_behavior_impact") or ""
    )
    sections: list[dict[str, str]] = [
        {
            "key": "what_it_is",
            "label": proposal_label("what_it_is", language=language),
            "value": what_it_is,
        },
        {
            "key": "symptom",
            "label": proposal_label("symptom", language=language),
            "value": symptom,
        },
    ]

    evidence_examples = render_evidence_examples(topic.get("evidence_examples"))
    if evidence_examples:
        sections.append(
            {
                "key": "evidence_examples",
                "label": proposal_label("evidence_examples", language=language),
                "value": evidence_examples,
            }
        )

    before_behavior = localized_topic_section_value(topic, key="before_behavior", language=language) or str(
        topic.get("before_behavior") or ""
    ).strip()
    if not before_behavior:
        before_behavior = default_bad_example(topic, language=language)
    sections.append(
        {
            "key": "before_behavior",
            "label": proposal_label("before_behavior", language=language),
            "value": before_behavior,
        }
    )

    after_behavior = localized_topic_section_value(topic, key="after_behavior", language=language) or str(
        topic.get("after_behavior") or ""
    ).strip()
    if not after_behavior:
        after_behavior = default_good_example(topic, language=language)
    sections.append(
        {
            "key": "after_behavior",
            "label": proposal_label("after_behavior", language=language),
            "value": after_behavior,
        }
    )

    improvement = localized_topic_section_value(topic, key="improvement", language=language) or str(
        topic.get("expected_behavior_impact") or topic.get("expected_output") or ""
    )
    sections.extend(
        [
            {
                "key": "improvement",
                "label": proposal_label("improvement", language=language),
                "value": improvement,
            },
            {
                "key": "evidence",
                "label": proposal_label("evidence", language=language),
                "value": evidence_summary,
            },
            {
                "key": "status",
                "label": proposal_label("status", language=language),
                "value": canonical_status_line(),
            },
        ]
    )
    return sections


def rendered_topic(topic: dict[str, Any], *, index: int, language: str, output_mode: str) -> dict[str, Any]:
    enriched = copy_topic_with_research_need(topic)
    canonical_title = str(enriched.get("title") or "")
    return {
        "display_index": index,
        "id": enriched.get("id"),
        "rank": enriched.get("rank", index),
        "title": localized_title(canonical_title, language=language),
        "canonical_title": canonical_title,
        "confidence": enriched.get("confidence"),
        "evidence_label": enriched.get("evidence_label"),
        "source_signal_ids": enriched.get("source_signal_ids", []),
        "source_mix_label": enriched.get("source_mix_label"),
        "provenance_note": enriched.get("provenance_note"),
        "current_session_confirmation": enriched.get("current_session_confirmation"),
        "status_line": canonical_status_line(),
        "short_why": enriched.get("why_surfaced"),
        "short_impact": enriched.get("expected_behavior_impact"),
        "advisory_only": True,
        "selected": False,
        "carry_forward_allowed": False,
        "fields": presentation_fields(enriched, language=language, output_mode=output_mode),
        "canonical_topic": enriched,
    }


def strongest_signal(signals_report: dict[str, Any]) -> dict[str, Any] | None:
    ranked = signals_report.get("ranked_signals", [])
    if not isinstance(ranked, list):
        return None
    for item in ranked:
        if isinstance(item, dict):
            return item
    return None


def parse_historical_strength(value: Any) -> tuple[int, int, int] | None:
    text = str(value or "").strip()
    parts = text.split()
    if len(parts) < 8:
        return None
    try:
        traces = int(parts[0])
        sessions = int(parts[4])
        shards = int(parts[7])
    except ValueError:
        return None
    return traces, sessions, shards


def build_historical_breadth_summary(signals_report: dict[str, Any], topic_list: list[dict[str, Any]], *, language: str) -> dict[str, Any]:
    promoted_signal_ids = {
        str(signal_id)
        for topic in topic_list
        for signal_id in topic.get("source_signal_ids", [])
        if signal_id
    }
    broad_patterns_ready = 0
    strongest_historical_strength = None
    for topic in topic_list:
        canonical_topic = topic.get("canonical_topic", {}) if isinstance(topic.get("canonical_topic"), dict) else {}
        strength = str(topic.get("historical_strength") or canonical_topic.get("historical_strength") or "")
        parsed = parse_historical_strength(strength)
        if strongest_historical_strength is None and strength:
            strongest_historical_strength = strength
        if parsed and parsed[1] >= 2 and parsed[2] >= 2:
            broad_patterns_ready += 1

    narrow_patterns_not_promoted = 0
    ranked = signals_report.get("ranked_signals", [])
    if isinstance(ranked, list):
        for signal in ranked:
            if not isinstance(signal, dict):
                continue
            if str(signal.get("id") or "") in promoted_signal_ids:
                continue
            parsed = parse_historical_strength(signal.get("historical_strength"))
            if parsed and parsed[1] == 1 and parsed[2] == 1 and signal.get("current_session_confirmation") == "historical-only":
                narrow_patterns_not_promoted += 1

    if language == "th":
        ordering_note = "จัดลำดับโดยให้ pattern แบบ multi-session/multi-shard มาก่อน และไม่ให้ historical pattern ที่แคบเกินไป collapse มาเป็น proposal หลักทันที"
    else:
        ordering_note = "Broader multi-session/multi-shard patterns are prioritized before the proposal block, while narrow historical-only signals stay out of the main proposal path."

    return {
        "broad_patterns_ready": broad_patterns_ready,
        "narrow_patterns_not_promoted": narrow_patterns_not_promoted,
        "strongest_historical_strength": strongest_historical_strength,
        "ordering_note": ordering_note,
    }


def build_no_topics_payload(signals_report: dict[str, Any], *, language: str, output_mode: str) -> dict[str, Any]:
    strongest = strongest_signal(signals_report)
    source = signals_report.get("source") if isinstance(signals_report.get("source"), dict) else {}
    limits = signals_report.get("limits") if isinstance(signals_report.get("limits"), dict) else {}
    policy_limited = bool(source.get("policy_limited"))
    policy_note = str(source.get("policy_note") or "").strip()
    records_analyzed = int(limits.get("records_analyzed") or source.get("records_received") or 0)
    signals_ranked = int(limits.get("signals_ranked") or 0)
    strongest_scope = ""
    strongest_confidence = None
    strongest_score = None
    strongest_label = None
    strongest_evidence_label = None
    if strongest:
        strongest_scope = str(strongest.get("source_scope_label") or strongest.get("provenance_note") or "")
        strongest_confidence = strongest.get("confidence")
        strongest_score = strongest.get("score")
        strongest_label = strongest.get("label")
        strongest_evidence_label = strongest.get("evidence_label")
    current_session_only = "current-session-only" in strongest_scope.lower()

    if language == "th":
        message = "การวิเคราะห์แบบ broader historical ยังไม่พบ pattern จาก trace ที่ซ้ำมากพอสำหรับเสนอเป็นหัวข้อ"
        details: list[str] = []
        if strongest_confidence or strongest_evidence_label:
            details.append(
                f"สัญญาณที่แรงสุดยังไม่ถึงระดับ repeated pattern และยังเป็น {strongest_confidence or 'unknown'}-confidence กับ {strongest_evidence_label or 'unknown'} จึงยังต่ำกว่า promotion gate"
            )
        strongest_strength = strongest.get("historical_strength") if strongest else None
        if strongest_strength and strongest.get("current_session_confirmation") == "historical-only":
            details.append(
                f"สัญญาณ historical-only ที่แรงสุดยังแคบเกินไป คือ {strongest_strength} จึงยังไม่ควรถูกมองเป็น broader historical review"
            )
        if records_analyzed or signals_ranked:
            details.append(
                f"รอบนี้วิเคราะห์ {records_analyzed} record และจัดอันดับ {signals_ranked} signal แต่ promote ได้ 0 topic candidate"
            )
        if policy_limited and policy_note:
            details.append(policy_note)
        recommended_next_step = "รอให้เกิด trace เชิงประวัติที่ซ้ำชัดขึ้น หรือมี recurrence ที่สดใหม่กว่านี้ก่อนค่อยเสนอหัวข้อ RULES/workflow"
    else:
        message = "Broader historical analysis did not find a repeated trace-backed pattern strong enough to propose yet."
        details = []
        if strongest_confidence or strongest_evidence_label:
            details.append(
                f"The strongest signal did not reach repeated pattern strength; it remained {strongest_confidence or 'unknown'}-confidence with {strongest_evidence_label or 'unknown'}, so it stayed below the promotion gate."
            )
        strongest_strength = strongest.get("historical_strength") if strongest else None
        if strongest_strength and strongest.get("current_session_confirmation") == "historical-only":
            details.append(
                f"The strongest remaining historical-only signal was still narrow at {strongest_strength}, so it did not qualify as broad historical review."
            )
        if records_analyzed or signals_ranked:
            details.append(
                f"This pass analyzed {records_analyzed} record(s) and ranked {signals_ranked} signal(s), but promoted 0 topic candidates."
            )
        if policy_limited and policy_note:
            details.append(policy_note)
        recommended_next_step = "Gather more repeated historical trace evidence or wait for fresher recurrence before proposing a RULES/workflow topic."

    return {
        "no_topics_message": message,
        "no_topics_details": details,
        "recommended_next_step": recommended_next_step,
        "no_topics_context": {
            "records_analyzed": records_analyzed,
            "signals_ranked": signals_ranked,
            "strongest_signal_id": strongest.get("id") if strongest else None,
            "strongest_signal_label": strongest_label,
            "strongest_signal_confidence": strongest_confidence,
            "strongest_signal_score": strongest_score,
            "strongest_signal_evidence_label": strongest_evidence_label,
            "source_scope_label": strongest.get("source_scope_label") if strongest else None,
        },
    }


def build_recommendation(topic_list: list[dict[str, Any]], *, language: str) -> dict[str, Any] | None:
    if not topic_list:
        return None
    first_topic = topic_list[0]
    canonical_topic = first_topic.get("canonical_topic", {})
    return {
        "recommended_topic_id": first_topic.get("id"),
        "title": first_topic.get("title"),
        "canonical_title": first_topic.get("canonical_title"),
        "why": short_recommendation_reason(canonical_topic, language=language),
        "source_mix_label": canonical_topic.get("source_mix_label"),
        "current_session_confirmation": canonical_topic.get("current_session_confirmation"),
        "status_line": canonical_status_line(),
    }


def topic_family_key(topic: dict[str, Any]) -> str:
    canonical_title = str(topic.get("canonical_title") or topic.get("title") or "").strip()
    if " — " in canonical_title:
        return canonical_title.split(" — ", 1)[0].strip()
    return canonical_title



def build_primary_proposal(topic_list: list[dict[str, Any]], *, language: str) -> dict[str, Any] | None:
    if not topic_list:
        return None
    topic = topic_list[0]
    canonical_topic = topic.get("canonical_topic", {})
    return {
        "id": topic.get("id"),
        "rank": topic.get("rank"),
        "title": topic.get("title"),
        "canonical_title": topic.get("canonical_title"),
        "source_mix_label": canonical_topic.get("source_mix_label"),
        "current_session_confirmation": canonical_topic.get("current_session_confirmation"),
        "evidence_summary": canonical_topic.get("evidence_summary") or canonical_topic.get("provenance_note"),
        "status_line": canonical_status_line(),
        "sections": proposal_sections(canonical_topic, language=language),
    }



def build_related_variants(topic_list: list[dict[str, Any]]) -> dict[str, Any]:
    if not topic_list:
        return {"family_key": "", "topics": []}
    primary = topic_list[0]
    family_key = topic_family_key(primary)
    variants: list[dict[str, Any]] = []
    for topic in topic_list[1:]:
        if topic_family_key(topic) != family_key:
            continue
        variants.append(
            {
                "id": topic.get("id"),
                "rank": topic.get("rank"),
                "title": topic.get("title"),
                "canonical_title": topic.get("canonical_title"),
                "confidence": topic.get("confidence"),
                "status_line": topic.get("status_line") or canonical_status_line(),
                "short_why": topic.get("short_why"),
                "short_impact": topic.get("short_impact"),
                "current_session_confirmation": topic.get("current_session_confirmation"),
                "source_mix_label": topic.get("source_mix_label"),
                "advisory_only": True,
                "carry_forward_allowed": False,
            }
        )
    return {
        "family_key": family_key,
        "topics": variants,
    }


def build_topic_cards(topic_list: list[dict[str, Any]], *, language: str) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for index, topic in enumerate(topic_list, start=1):
        canonical_topic = topic.get("canonical_topic", {})
        cards.append(
            {
                "display_index": index,
                "id": topic.get("id"),
                "rank": topic.get("rank"),
                "title": topic.get("title"),
                "canonical_title": topic.get("canonical_title"),
                "recommended_first": index == 1,
                "status_line": canonical_status_line(),
                "confidence": topic.get("confidence"),
                "short_why": topic.get("short_why"),
                "short_impact": topic.get("short_impact"),
                "source_mix_label": canonical_topic.get("source_mix_label"),
                "current_session_confirmation": canonical_topic.get("current_session_confirmation"),
                "historical_strength": canonical_topic.get("historical_strength"),
                "latest_seen": canonical_topic.get("latest_seen"),
                "evidence_summary": canonical_topic.get("evidence_summary") or canonical_topic.get("provenance_note"),
                "family_key": topic_family_key(topic),
                "sections": proposal_sections(canonical_topic, language=language),
                "advisory_only": True,
                "carry_forward_allowed": False,
            }
        )
    return cards


def build_next_action_options(topic_cards: list[dict[str, Any]], *, language: str) -> dict[str, Any] | None:
    if not topic_cards:
        return None

    first_topic_label = f"Topic {topic_cards[0].get('display_index', 1)}"
    if language == "th":
        return {
            "heading": "Next action options",
            "status_line": "advisory only; no topic selected yet",
            "options": [
                {
                    "id": "choose-topic-number",
                    "label": "เลือกหมายเลขหัวข้อ",
                    "action": f"พิมพ์เช่น \"เลือก {first_topic_label}\" เพื่อให้ผมช่วยร่าง change proposal หรือ goal draft สำหรับหัวข้อนั้น",
                    "advisory_only": True,
                    "carry_forward_allowed": False,
                },
                {
                    "id": "type-direct-request",
                    "label": "พิมพ์คำขอโดยตรง",
                    "action": "พิมพ์คำขอในแบบของคุณเองและระบุหัวข้อที่ต้องการปรับได้เลย โดยยังไม่ถือว่า execute อัตโนมัติ",
                    "advisory_only": True,
                    "carry_forward_allowed": False,
                },
                {
                    "id": "deepen-with-research",
                    "label": "ขอ research เพิ่มก่อน",
                    "action": "ขอ deep thinking, websearch, หรือ webfetch ในหัวข้อที่สนใจก่อน แล้วค่อยตัดสินใจว่าจะปรับอย่างไรต่อ",
                    "advisory_only": True,
                    "carry_forward_allowed": False,
                },
            ],
        }

    return {
        "heading": "Next action options",
        "status_line": "advisory only; no topic selected yet",
        "options": [
            {
                "id": "choose-topic-number",
                "label": "Choose a topic number",
                "action": f"Choose {first_topic_label} to turn that topic into a change proposal or goal draft.",
                "advisory_only": True,
                "carry_forward_allowed": False,
            },
            {
                "id": "type-direct-request",
                "label": "Type a direct request",
                "action": "Type a direct request in your own words and name the topic you want to adjust.",
                "advisory_only": True,
                "carry_forward_allowed": False,
            },
            {
                "id": "deepen-with-research",
                "label": "Ask for deeper research first",
                "action": "Ask for deep thinking, websearch, or webfetch on a topic before any adjustment.",
                "advisory_only": True,
                "carry_forward_allowed": False,
            },
        ],
    }


def build_presentation(
    signals_report: dict[str, Any], *, output_mode: str = "auto", language: str | None = None
) -> dict[str, Any]:
    if output_mode not in OUTPUT_MODES:
        raise ValueError(f"Unsupported output mode: {output_mode}")

    resolved_language = active_language(output_mode, language)
    topics = topic_candidates(signals_report)
    if len(topics) < 3:
        seen_signal_ids = {
            str(signal_id)
            for topic in topics
            for signal_id in topic.get("source_signal_ids", [])
            if signal_id
        }
        for fallback_topic in advisory_fallback_topics(signals_report):
            signal_ids = {
                str(signal_id)
                for signal_id in fallback_topic.get("source_signal_ids", [])
                if signal_id
            }
            if seen_signal_ids & signal_ids:
                continue
            topics.append(fallback_topic)
            seen_signal_ids.update(signal_ids)
            if len(topics) >= 3:
                break
    rendered = [
        rendered_topic(topic, index=index, language=resolved_language, output_mode=output_mode)
        for index, topic in enumerate(topics, start=1)
    ]
    topic_cards = build_topic_cards(rendered, language=resolved_language)
    next_action_options = build_next_action_options(topic_cards, language=resolved_language)
    status = "available" if rendered else "no-topics"
    no_topics_payload = build_no_topics_payload(signals_report, language=resolved_language, output_mode=output_mode) if not rendered else None

    return {
        "tool": "memory-context-intelligence",
        "mode": "present",
        "status": status,
        "output_mode": output_mode,
        "active_language": resolved_language,
        "internal_signals_report_mode": signals_report.get("mode"),
        "heading": label("heading", language=resolved_language, output_mode=output_mode),
        "summary": label("summary", language=resolved_language, output_mode=output_mode),
        "choice_prompt": label("choice_prompt", language=resolved_language, output_mode=output_mode),
        "no_topics_message": no_topics_payload["no_topics_message"] if no_topics_payload else None,
        "no_topics_details": no_topics_payload["no_topics_details"] if no_topics_payload else [],
        "recommended_next_step": no_topics_payload["recommended_next_step"] if no_topics_payload else None,
        "no_topics_context": no_topics_payload["no_topics_context"] if no_topics_payload else None,
        "topic_cards": topic_cards,
        "next_action_options": next_action_options,
        "selected_topic_id": None,
        "selection_required_before_carry_forward": True,
        "carry_forward_allowed": False,
        "unselected_topics_advisory_only": [topic.get("id") for topic in topics],
        "choose_flow_performed": False,
        "research_enrichment_performed": False,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


class SelectionError(ValueError):
    """Raised when a requested topic selection cannot be resolved."""


def find_topic(topics: list[dict[str, Any]], topic_id: str) -> tuple[dict[str, Any], str]:
    requested = topic_id.strip()
    if not requested:
        raise SelectionError("A non-empty --topic-id is required.")

    for topic in topics:
        if str(topic.get("id", "")) == requested:
            return topic, "id"

    if requested.isdigit():
        requested_rank = int(requested)
        for index, topic in enumerate(topics, start=1):
            rank = topic.get("rank", index)
            if rank == requested_rank or index == requested_rank:
                return topic, "rank"

    available = ", ".join(str(topic.get("id")) for topic in topics if topic.get("id")) or "none"
    raise SelectionError(f"Topic '{requested}' was not found. Available topic ids: {available}")


def advisory_unselected_topics(topics: list[dict[str, Any]], selected_id: str) -> list[dict[str, Any]]:
    unselected: list[dict[str, Any]] = []
    for topic in topics:
        topic_id = str(topic.get("id", ""))
        if topic_id == selected_id:
            continue
        unselected.append(
            {
                "id": topic.get("id"),
                "rank": topic.get("rank"),
                "title": topic.get("title"),
                "advisory_only": True,
                "selected": False,
                "carry_forward_allowed": False,
            }
        )
    return unselected


def build_selection(
    signals_report: dict[str, Any], *, topic_id: str, output_mode: str = "auto", language: str | None = None
) -> dict[str, Any]:
    if output_mode not in OUTPUT_MODES:
        raise ValueError(f"Unsupported output mode: {output_mode}")

    topics = topic_candidates(signals_report)
    selected, selection_method = find_topic(topics, topic_id)
    selected_topic = copy_topic_with_research_need(selected)
    selected_id = str(selected_topic.get("id"))
    resolved_language = active_language(output_mode, language)

    return {
        "tool": "memory-context-intelligence",
        "mode": "choose",
        "status": "selected",
        "output_mode": output_mode,
        "active_language": resolved_language,
        "selection_method": selection_method,
        "selected_topic_id": selected_topic.get("id"),
        "selected_topic": {
            **selected_topic,
            "selected": True,
            "advisory_only": False,
            "carry_forward_allowed": True,
        },
        "unselected_topics": advisory_unselected_topics(topics, selected_id),
        "selection_required_before_carry_forward": False,
        "carry_forward_allowed": True,
        "summary": label("selected_summary", language=resolved_language, output_mode=output_mode),
        "unselected_summary": label("unselected_summary", language=resolved_language, output_mode=output_mode),
        "notes": [
            "Exactly one selected topic is recorded in this fileless structured output.",
            "Only the selected topic may be carried forward to later phases.",
            "Unselected topics remain advisory only and are not automatically promoted.",
            "Research enrichment has not been performed by choose mode.",
            "Candidate packet building has not been performed by choose mode.",
            "/additional/ emission has not been performed by choose mode.",
            "Main RULES mutation has not been performed by choose mode.",
        ],
        "choose_flow_performed": True,
        "research_enrichment_performed": False,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        signals_report = load_json_input(args.signals_report)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"memory-context-intelligence presentation: failed to read signals JSON: {exc}", file=sys.stderr)
        return 2

    try:
        if args.action == "present":
            report = build_presentation(
                signals_report,
                output_mode=args.output_mode,
                language=args.language,
            )
        else:
            report = build_selection(
                signals_report,
                topic_id=args.topic_id,
                output_mode=args.output_mode,
                language=args.language,
            )
    except (SelectionError, ValueError) as exc:
        print(f"memory-context-intelligence presentation: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=os.sys.stdout, ensure_ascii=False, indent=2)
    os.sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
