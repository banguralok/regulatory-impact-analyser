"""Tests for core data models."""

import pytest
from src.models.regulatory_element import RegulatoryElement, GapRecord, ObligationType


def test_regulatory_element_to_dict():
    element = RegulatoryElement(
        element_id="REG-K-001",
        regulation="12 CFR Part 211",
        section="211.4",
        subsection="(a)",
        element_name="total assets",
        definition="The total consolidated assets of a banking organization",
        obligation_type=ObligationType.SHALL,
        raw_text="A U.S. banking organization shall maintain total assets...",
        tags=["reporting", "capital"],
    )
    d = element.to_dict()
    assert d["element_id"] == "REG-K-001"
    assert d["obligation_type"] == "shall"
    assert d["tags"] == "reporting, capital"


def test_gap_record_missing():
    gap = GapRecord(
        element_id="REG-K-001",
        element_name="total assets",
        regulation="12 CFR Part 211",
        section="211.4",
        gap_type="missing",
        existing_field=None,
        similarity_score=0.0,
        priority="high",
    )
    d = gap.to_dict()
    assert d["existing_field"] == "NOT FOUND"
    assert d["gap_type"] == "missing"
