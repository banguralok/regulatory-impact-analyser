# Regulatory Impact Analyser

An AI-powered tool that helps financial institutions rapidly assess the impact of regulatory changes on their internal data landscape — mapping new or amended regulations to existing data elements, systems, and compliance gaps.

## Problem

When regulators publish new rules (Basel 3.1, DORA, climate risk disclosures, Reg K amendments), compliance and data teams at banks face a manual, time-intensive process to:
- Parse dense regulatory text
- Identify which data elements are newly required or redefined
- Map those elements against internal data dictionaries and system schemas
- Prioritise remediation work

This process typically takes weeks and is prone to gaps.

## What This Tool Does

- **Regulatory Parser** — Ingests regulatory documents (eCFR, PDF, XML) and extracts structured data elements, definitions, and obligations
- **Gap Mapper** — Compares extracted regulatory requirements against a bank's existing data dictionary
- **Impact Reporter** — Produces a prioritised gap report showing what data is missing, redefined, or at risk
- **On-Premise Ready** — Designed to run within a bank's secure environment; no data leaves the institution

## Target Users

Compliance officers, data governance teams, and regulatory change management functions at Tier 1–3 banks and building societies.

## Current Status

🚧 Early-stage prototype — actively in development.

Pilot focus: **Title 12 CFR Part 211 (Regulation K)** — International Banking Operations

## Tech Stack

- Python 3.11+
- Regulatory source: [eCFR API](https://www.ecfr.gov/developers/documentation/api/v1)
- NLP / LLM layer: Anthropic Claude API (on-premise deployment pathway via Claude for Enterprise)
- Output: CSV / JSON gap reports

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
python src/parsers/ecfr_parser.py --regulation "12 CFR Part 211"
```

## Roadmap

- [x] Reg K (12 CFR Part 211) — data element extraction pilot
- [ ] Gap mapping engine v1
- [ ] Basel 3.1 parser
- [ ] DORA Article mapping
- [ ] UI layer for compliance teams
- [ ] On-premise deployment packaging

## Contributing

This is a pre-seed stage project. If you work in bank compliance, data governance, or regtech and want to collaborate or provide feedback, reach out via GitHub Issues.

---

*Built at the intersection of banking technology, regulatory compliance, and applied AI.*
