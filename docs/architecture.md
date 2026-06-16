# Architecture Overview

## Design Principles

1. **On-premise first** — All processing runs within the institution's environment. No regulatory or internal data is transmitted externally.
2. **Modular pipeline** — Each stage (parse → extract → map → report) is independently testable and replaceable.
3. **Regulation-agnostic core** — Regulation-specific logic lives in parser configs; the core engine is reusable.

## Pipeline

```
[Regulatory Source]
       |
       v
[Parser Layer]       <- eCFR API / PDF / XML ingestion
       |
       v
[Extraction Layer]   <- LLM-assisted data element & obligation extraction
       |
       v
[Mapping Layer]      <- Comparison against internal data dictionary
       |
       v
[Gap Report]         <- CSV / JSON output
```

## Key Design Decisions

### ADR-001: eCFR API as primary regulatory source
- **Decision**: Use the eCFR JSON API rather than scraping HTML or parsing PDFs where possible
- **Rationale**: Structured, versioned, maintained by the US Government Publishing Office
- **Trade-off**: US federal regulations only; EU/UK requires separate PDF pipeline

### ADR-002: LLM extraction over rule-based NLP
- **Decision**: Use Claude API for data element extraction rather than hand-crafted regex/NLP rules
- **Rationale**: Regulatory language is highly variable; LLMs generalise better across regulation types
- **Trade-off**: Requires prompt engineering and output validation

### ADR-003: CSV as primary gap report output
- **Decision**: Output gap reports as CSV first
- **Rationale**: Compliance teams live in Excel; lowest friction for pilot adoption
- **Trade-off**: v2 will add structured DB and dashboard output
