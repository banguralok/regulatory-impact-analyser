# Regulatory Impact Analyser

An AI-powered tool that helps financial institutions rapidly assess the impact of regulatory changes on their internal data landscape — mapping new or amended regulations to existing data elements, systems, and compliance gaps.

---

## Problem

When regulators publish new rules (Basel 3.1, DORA, climate risk disclosures, Reg K amendments), compliance and data teams at banks face a manual, time-intensive process to:
- Parse dense regulatory text
- Identify which data elements are newly required or redefined
- Map those elements against internal data dictionaries and system schemas
- Prioritise remediation work

This process typically takes weeks, involves multiple teams, and is prone to gaps. At large institutions, it often runs in parallel silos — legal, compliance, data, and technology — with no single source of truth.

---

## What This Tool Does

- **Regulatory Parser** — Ingests regulatory documents (eCFR, PDF, XML) and extracts structured data elements, definitions, and obligations
- **Gap Mapper** — Compares extracted regulatory requirements against a bank's existing data dictionary
- **Impact Reporter** — Produces a prioritised gap report showing what data is missing, redefined, or at risk
- **On-Premise Ready** — Designed to run within a bank's secure environment; no data leaves the institution

## Target Users

Compliance officers, data governance teams, and regulatory change management functions at Tier 1–3 banks and building societies.

---

## Product Roadmap

### MVP — Pilot (Now → Month 6)
*Goal: Prove core value with a single regulation in a controlled environment*

| Feature | Description |
|---|---|
| eCFR Regulatory Parser | Ingest and parse US federal regulations via the eCFR API (Title 12 pilot) |
| Data Element Extractor | LLM-assisted extraction of reportable fields, definitions, and obligation types (must/shall/may) |
| CSV Data Dictionary Ingestion | Accept a bank's existing data dictionary as a flat CSV/Excel file |
| Gap Identification Engine | Match extracted regulatory elements against the data dictionary; flag missing, partial, or redefined fields |
| Confidence Scoring | Assign a match confidence score (0–1) to each mapped element |
| Gap Report Output | Export prioritised gap report as CSV with element name, section reference, gap type, and recommended action |
| Reg K Pilot Coverage | Full coverage of Title 12 CFR Part 211 (Regulation K) as the pilot regulation |

---

### Release 1 — Early Adopter (Month 6 → Month 12)
*Goal: Expand regulation coverage, harden the pipeline, onboard first paying clients*

| Feature | Description |
|---|---|
| Multi-Regulation Support | Support Basel 3.1 and DORA in addition to Reg K |
| PDF Regulatory Ingestion | Parse regulations distributed as PDF (EU/UK regulatory formats) |
| Amendment Delta Detection | Compare two versions of a regulation and surface only what changed — reduces noise for established teams |
| Data Dictionary Connector | Native connectors for common bank data catalogue formats (Collibra, IBM IGC CSV exports) |
| Obligation Classification | Classify each element by obligation type: reporting, capital, liquidity, conduct |
| Prioritisation Engine | Rank gaps by regulatory deadline, data criticality, and system ownership |
| User Dashboard (Web UI) | Browser-based interface for compliance teams to review, filter, and annotate gap reports |
| Audit Trail | Immutable log of every analysis run — regulation version, dictionary version, output hash |
| Role-Based Access | Separate views for compliance analyst, data owner, and senior reviewer |
| On-Premise Deployment Package | Docker-based deployment; runs entirely within the institution's network |

---

### Release 2 — Scale (Year 2)
*Goal: Become the system of record for regulatory data impact tracking*

| Feature | Description |
|---|---|
| Regulation Watch | Automated monitoring of eCFR, FCA, EBA, and BIS feeds; alerts when a tracked regulation is amended |
| Full Regulation Library | Pre-built parsers for 20+ regulations across US, EU, and UK jurisdictions |
| Historical Impact Archive | Track how a regulation's data requirements have evolved across versions over time |
| System Lineage Mapping | Map regulatory elements not just to data dictionary fields but to upstream source systems |
| Remediation Workflow | Built-in task assignment and tracking for gap remediation — assign to data owner, set deadline, track sign-off |
| API Layer | REST API so banks can integrate impact analysis into their existing regulatory change management workflows |
| LLM Fine-Tuning | Fine-tune extraction models on bank-specific data taxonomy for higher accuracy |
| Multi-Tenant SaaS Option | Cloud-hosted option (data never leaves tenant boundary) for smaller institutions without on-prem infrastructure |
| Reporting Pack | Automated board-level and regulator-ready summary reports — regulation by regulation exposure summary |
| SSO & Enterprise Auth | SAML/OIDC integration for enterprise identity providers |

---

## Current Status

🚧 Early-stage prototype — actively in development.

Pilot focus: **Title 12 CFR Part 211 (Regulation K)** — International Banking Operations

---

## Tech Stack

- Python 3.11+
- Regulatory source: [eCFR API](https://www.ecfr.gov/developers/documentation/api/v1)
- NLP / LLM layer: Anthropic Claude API (on-premise deployment pathway via Claude for Enterprise)
- Output: CSV / JSON gap reports

---

## Repository Structure

```
regulatory-impact-analyser/
├── src/
│   ├── parsers/        # Regulatory document ingestion (eCFR, PDF, XML)
│   ├── extractors/     # Data element & definition extraction
│   ├── mappers/        # Gap mapping against data dictionaries
│   └── models/         # Data models and schemas
├── data/
│   ├── raw/            # Source regulatory documents
│   ├── processed/      # Extracted, structured outputs
│   └── schemas/        # Reference data dictionary schemas
├── docs/               # Architecture decisions, research notes
├── notebooks/          # Exploratory analysis and prototyping
└── tests/              # Unit and integration tests
```

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/banguralok/regulatory-impact-analyser.git
cd regulatory-impact-analyser

# Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run the Reg K parser pilot
python src/parsers/ecfr_parser.py --title 12 --part 211
```

---

## Contributing

This is a pre-seed stage project. If you work in bank compliance, data governance, or regtech and want to collaborate or provide feedback, reach out via GitHub Issues.

---

*Built at the intersection of banking technology, regulatory compliance, and applied AI.*
