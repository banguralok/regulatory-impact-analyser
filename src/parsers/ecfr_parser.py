"""
eCFR Parser - fetches and parses regulatory text from the eCFR API.

Pilot regulation: Title 12 CFR Part 211 (Regulation K)
eCFR API docs: https://www.ecfr.gov/developers/documentation/api/v1
"""

import requests
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

ECFR_BASE_URL = "https://www.ecfr.gov/api/versioner/v1"


class ECFRParser:
    """Fetches regulatory content from the eCFR API and extracts structured section data."""

    def __init__(self, title: int, part: int):
        self.title = title
        self.part = part
        self.regulation_ref = f"Title {title} CFR Part {part}"

    def fetch_structure(self) -> dict:
        url = f"{ECFR_BASE_URL}/structure/current/title-{self.title}.json"
        logger.info(f"Fetching structure for {self.regulation_ref}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    def extract_sections(self, structure: dict) -> list:
        sections = []
        self._walk_structure(structure.get("children", []), sections)
        logger.info(f"Extracted {len(sections)} sections from {self.regulation_ref}")
        return sections

    def _walk_structure(self, nodes: list, sections: list, depth: int = 0):
        for node in nodes:
            node_type = node.get("type", "")
            identifier = node.get("identifier", "")

            if node_type == "part" and identifier != str(self.part):
                continue

            if node_type == "section":
                sections.append({
                    "section": identifier,
                    "label": node.get("label", ""),
                    "label_description": node.get("label_description", ""),
                    "reserved": node.get("reserved", False),
                })

            children = node.get("children", [])
            if children:
                self._walk_structure(children, sections, depth + 1)

    def save_structure(self, output_path: str):
        structure = self.fetch_structure()
        sections = self.extract_sections(structure)
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(sections, f, indent=2)
        logger.info(f"Saved {len(sections)} sections to {output_path}")
        return sections


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Parse a CFR regulation from eCFR")
    parser.add_argument("--title", type=int, default=12)
    parser.add_argument("--part", type=int, default=211)
    parser.add_argument("--output", type=str, default="data/processed/ecfr_structure.json")
    args = parser.parse_args()

    ecfr = ECFRParser(title=args.title, part=args.part)
    sections = ecfr.save_structure(args.output)
    print(f"\nParsed {len(sections)} sections from Title {args.title} CFR Part {args.part}")
    print(f"Output saved to {args.output}")
