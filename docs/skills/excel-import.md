# Excel Import Skill

Rules for bulk import/migration from existing Excel sheets.

## Strategy
- Support CSV/Excel via pandas/openpyxl
- Map columns to internal asset schema
- Validate required fields: asset ID, name, category, make, serial
- Report errors row-by-row; do not block import of valid rows
- Deduplicate by asset ID

## Migration
- Current data lives in Excel + paper
- Hospital to provide real sheets (none available now → default plan)
