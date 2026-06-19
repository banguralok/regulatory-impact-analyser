# Regulatory Impact Analyser

A tool that helps financial institutions assess the data impact of regulatory changes — extracting data elements and obligations from regulatory text and mapping them against an institution's existing data dictionary to surface gaps.

---

## Problem

When regulators publish new or amended rules, compliance and data teams at banks must manually work through dense regulatory text to identify which data elements are newly required, redefined, or affected. That output then needs to be cross-referenced against internal data dictionaries and system inventories before any remediation work can begin.

This process is slow, largely manual, and inconsistent across teams. Legal, compliance, data, and technology functions often work through the same regulation independently, with no shared structured output.

The result is duplicated effort, missed elements, and late discovery of data gaps — often close to regulatory deadlines.

---

## What This Tool Does

- **Regulatory Parser** — Ingests regulatory text from the eCFR API and extracts structured sections, definitions, and obligations
- **Data Element Extractor** — Identifies reportable data fields and their obligation types (mandatory, permissive, prohibited) from regulatory language
- **Gap Mapper** — Compares extracted elements against a bank's data dictionary and flags missing, partial, or redefined fields
- **Gap Report** — Outputs a structured, prioritised gap report in CSV format for review by compliance and data teams

**Deployment model:** Designed to run within an institution's own environment. No regulatory text or internal data is sent to external services during analysis.

---

## Who It Is For

Regulatory change management, data governance, and compliance functions at financial institutions — particularly teams that currently manage this process manually in spreadsheets.

---

## Product Roadmap

### MVP — Pilot (Now → Month 6)
*Objective: Demonstrate end-to-end gap identification for a single regulation against a sample data dictionary*

| Feature | Description |
|---|---|
| eCFR Regulatory Parser | Fetch and parse US federal regulations via the eCFR API; extract section structure and text |
| Data Element Extractor | Extract reportable fields, definitions, and obligation types from regulatory text using an LLM |
| CSV Data Dictionary Ingestion | Accept an institution's data dictionary as a flat CSV or Excel file |
| Gap Identification | Match extracted regulatory elements against the data dictionary; classify each as matched, partial, or missing |
| Confidence Scoring | Assign a match confidence score to each mapped element based on field name and definition similarity |
| Gap Report (CSV) | Export a structured gap report with element name, regulation section, gap classification, confidence score, and notes |
| Reg K Pilot | End-to-end pipeline validated against Title 12 CFR Part 211 (Regulation K) as the pilot regulation |

---

### Release 1 — Early Adopter (Month 6 → Month 12)
*Objective: Harden the pipeline, expand regulation coverage, and make it usable by non-technical compliance staff*

| Feature | Description |
|---|---|
| Basel 3.1 Parser | Extend the parser to cover Basel 3.1 capital and reporting requirements |
| DORA Parser | Add coverage for the EU Digital Operational Resilience Act (DORA) data obligations |
| PDF Ingestion | Parse regulatory documents distributed as PDF, for regulations not available via structured APIs |
| Amendment Delta Detection | Given two versions of a regulation, identify only what changed — reduces re-analysis effort when amendments are minor |
| Obligation Classification | Tag each extracted element by obligation category: reporting, capital, liquidity, or operational |
| Prioritisation Engine | Rank identified gaps by regulatory deadline and data field criticality |
| Web UI | Browser-based interface for compliance analysts to review, filter, comment on, and export gap reports — no command line required |
| Versioned Audit Log | Record of each analysis run including regulation version used, dictionary version, and output — for internal governance purposes |
| Role-Based Access | Separate access levels for analyst, data owner, and approver |
| On-Premise Deployment | Docker-based packaging so the tool runs entirely within the institution's infrastructure |

---

### Release 2 — Expansion (Year 2)
*Objective: Broaden regulation coverage, deepen integration with bank workflows, and reduce time-to-analysis further*

| Feature | Description |
|---|---|
| Regulation Monitoring | Monitor selected regulatory feeds (eCFR, FCA, EBA) for amendments and notify when a tracked regulation changes |
| Expanded Regulation Library | Add parsers for additional regulations based on client demand and jurisdiction coverage priorities |
| Historical Version Tracking | Store and compare regulation versions over time to show how data requirements have evolved |
| Source System Mapping | Extend gap output to include the upstream system that should supply each data element, not just the dictionary field |
| Remediation Tracking | Assign gaps to data owners, set target dates, and track progress to closure within the tool |
| REST API | Allow integration with existing regulatory change management or data governance platforms via API |
| Extraction Tuning | Improve extraction accuracy for a specific institution's data taxonomy based on feedback from prior analysis runs |
| Enterprise Auth | SAML/OIDC integration for institutions with existing identity providers |

---

## Current Status

In development. The eCFR parser and core data models are built. The extraction and gap mapping pipeline is the active workstream.

Pilot regulation: **Title 12 CFR Part 211 (Regulation K)** — International Banking Operations.

---

## Tech Stack

- Python 3.11+
- Regulatory source: [eCFR API](https://www.ecfr.gov/developers/documentation/api/v1)
- LLM layer: Anthropic Claude API
- Output: CSV / JSON

---

## Repository Structure

```
regulatory-impact-analyser/
├── src/
│   ├── parsers/        # Regulatory document ingestion (eCFR, PDF)
│   ├── extractors/     # Data element and obligation extraction
│   ├── mappers/        # Gap mapping against data dictionaries
│   └── models/         # Core data models
├── data/
│   ├── raw/            # Source regulatory documents
│   ├── processed/      # Structured extraction outputs
│   └── schemas/        # Sample data dictionary schemas
├── docs/               # Architecture decisions and design notes
├── notebooks/          # Exploratory analysis
└── tests/              # Unit tests
```

---

## Getting Started

```bash
git clone https://github.com/banguralok/regulatory-impact-analyser.git
cd regulatory-impact-analyser

python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

python src/parsers/ecfr_parser.py --title 12 --part 211
```

---

## Contact

For questions or feedback, open a GitHub Issue.
