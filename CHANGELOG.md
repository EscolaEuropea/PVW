# PVW.one — Changelog

## v1.1.0 — 2026-05-10

### Changed across ALL 15 archetypes
- **Added `XL` to size_tier enum** in instance_metadata and identity. The S/M/L taxonomy proved insufficient for real-world operators that aggregate multiple terminals or operate at exceptional scale.
- **Added `default_XL` column** to schema sheets in all archetype Excel files. Default values are heuristic estimates (~2.5× size-L); operators should refine when implementing instances.
- **Added `CHANGELOG` sheet** to all archetype Excel files for version traceability.

### Cruise archetype — additional changes
The `terminal_cruise` archetype gained 8 new fields based on Barcelona implementation learnings:

**New IDENTITY fields:**
- `homeport_or_portofcall` (enum: homeport / port_of_call / mixed)
- `seasonal_peak_months` (string; e.g. "April-October")
- `construction_status` (enum: operational / under_construction / planned / decommissioning)

**New EQUIPMENT fields:**
- `solar_pv_capacity_kwp` (number)
- `rainwater_harvesting_system` (boolean)
- `ops_planned` (boolean)
- `ops_planned_year` (integer)
- `lng_ship_compatibility` (boolean)

### Rationale
Five Barcelona cruise instances (GPH, Palacruceros, Helix, MSC H, RCG G) revealed:
- GPH operates 4 terminals with 2.1M pax/year — beyond size-L scope (justifies XL)
- All terminals are clearly homeport vs port-of-call; this is fundamental to the operating model
- Modern Carnival (1,350 solar panels) and MSC (rooftop solar) terminals all include PV — not optional
- OPS planning is universal during 2025-2027 FuelEU transition; needed to distinguish "planned" from "operational"
- RCG Terminal G is under construction with 2027 ops — needed `construction_status`

### Backward compatibility
- All v1.0.0 instances remain syntactically valid against v1.1.0 schemas
- New fields are optional with defaults provided in archetype Excel
- All 17 Barcelona instances now reference `@1.1.0` archetypes after migration

### Migration path
For instance authors:
1. Update `instance_metadata.archetype_ref` from `@1.0.0` → `@1.1.0`
2. Optionally populate new fields (defaults are L0 fidelity)
3. For cruise size-L operators that aggregate multiple terminals: consider XL
