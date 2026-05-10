# PVW.one — Archetype Builder (source code)

This is the source code that generates the 15 PVW.one archetypes (Excel + JSON Schema).

## What's here

| File | Purpose |
|---|---|
| `pvw_builder.py` | The library — Excel/JSON generation logic, palette, helpers |
| `specs_terminals.py` | Specs for the 8 terminal archetypes |
| `specs_hubs_services.py` | Specs for the 7 hub + mandatory service archetypes |
| `generate_all.py` | Entry point — runs builder over all specs |

## How to use

```bash
# Requirements
pip install openpyxl

# Generate all 15 archetypes
python3 generate_all.py
# Output: ./archetypes/ARCHETYPE_*.xlsx + archetype_*.schema.json
```

## How to modify

### Add a field to an archetype
Open the relevant `specs_*.py` file, find the `identity` or `equipment` list,
add a tuple: `(field_id, label, unit, type, default_S, default_M, default_L, notes)`
Re-run `generate_all.py`.

### Change a default value
Edit the relevant default in the spec, re-run.

### Change carbon scenario decay curves
Edit `make_carbon_defaults()` in `pvw_builder.py` — adjust `BAU_factors`,
`FEU_factors`, `ACC_factors`.

### Add a new archetype
1. Create a new spec dict with same structure (see existing examples)
2. Add it to the list in `generate_all.py`
3. Re-run

## Versioning

Current PVW model version: **1.0.0** (defined in `pvw_builder.py` as `PVW_VERSION`).
Bump it when you make breaking changes; minor when you add fields.

## What this code is NOT

- Not production-grade (no tests, no CI, no validation pipeline)
- Specs are Python — non-developer collaborators cannot edit easily
- Single-author code — when this scales, refactor into proper module + YAML specs
