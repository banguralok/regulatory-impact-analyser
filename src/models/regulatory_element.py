"""
Data models for regulatory elements extracted from source documents.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class ObligationType(Enum):
    MUST = "must"
    SHALL = "shall"
    SHOULD = "should"
    MAY = "may"
    MUST_NOT = "must_not"


@dataclass
class RegulatoryElement:
    """Represents a single data element or obligation extracted from a regulation."""
    element_id: str
    regulation: str
    section: str
    subsection: Optional[str]
    element_name: str
    definition: Optional[str]
    obligation_type: ObligationType
    raw_text: str
    tags: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "element_id": self.element_id,
            "regulation": self.regulation,
            "section": self.section,
            "subsection": self.subsection,
            "element_name": self.element_name,
            "definition": self.definition,
            "obligation_type": self.obligation_type.value,
            "raw_text": self.raw_text,
            "tags": ", ".join(self.tags),
        }


@dataclass
class GapRecord:
    """Represents a gap between a regulatory requirement and an institution's data dictionary."""
    element_id: str
    element_name: str
    regulation: str
    section: str
    gap_type: str
    existing_field: Optional[str]
    similarity_score: float
    priority: str
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "element_id": self.element_id,
            "element_name": self.element_name,
            "regulation": self.regulation,
            "section": self.section,
            "gap_type": self.gap_type,
            "existing_field": self.existing_field or "NOT FOUND",
            "similarity_score": round(self.similarity_score, 3),
            "priority": self.priority,
            "notes": self.notes,
        }
