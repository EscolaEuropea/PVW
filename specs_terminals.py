"""Specs for terminal archetypes 2-7 + 9 (LNG)."""

# Common identity fields shared by all terminal archetypes (extends per type)
def common_identity_terminal(size_S_tier, size_M_tier, size_L_tier, throughput_unit):
    return [
        ("operator_legal_name", "Operator legal name", "—", "string",
         "[Small operator]", "[Medium operator]", "[Large operator]", "Registered legal name"),
        ("operator_short_name", "Operator commercial name", "—", "string", "—", "—", "—", ""),
        ("port_unlocode", "Port (UN/LOCODE)", "—", "enum", "—", "—", "—", "ISO UN/LOCODE"),
        ("port_name", "Port name", "—", "string", "—", "—", "—", ""),
        ("country_iso2", "Country (ISO 3166-1 alpha-2)", "—", "enum", "—", "—", "—", ""),
        ("location_lat", "Latitude (terminal centroid)", "deg", "number", "—", "—", "—", "WGS84"),
        ("location_lon", "Longitude (terminal centroid)", "deg", "number", "—", "—", "—", "WGS84"),
        ("year_operations_started", "Year operations started", "year", "integer", "—", "—", "—", ""),
        ("concession_holder", "Concession holder", "—", "string", "—", "—", "—", "May differ from operator"),
        ("concession_end_year", "Concession end year", "year", "integer", "—", "—", "—", ""),
        ("parent_group", "Parent group / shareholders", "—", "string", "—", "—", "—", ""),
        ("ownership_pct", "Ownership %", "%", "number", 100, 100, 100, "0-100"),
        ("annual_throughput", "Annual throughput", throughput_unit, "integer",
         size_S_tier, size_M_tier, size_L_tier, "Sized to terminal capacity"),
        ("size_tier", "Size tier (declarative)", "—", "enum", "S", "M", "L", "S/M/L"),
        ("isps_certified", "ISPS code certification", "bool", "boolean", True, True, True, ""),
        ("iso_9001", "ISO 9001 (quality)", "bool", "boolean", True, True, True, ""),
        ("iso_14001", "ISO 14001 (environment)", "bool", "boolean", True, True, True, ""),
        ("iso_45001", "ISO 45001 (occupational H&S)", "bool", "boolean", True, True, True, ""),
        ("aeo_status", "AEO certification", "—", "enum", "AEOF", "AEOF", "AEOF", "AEOC/AEOS/AEOF/none"),
        ("total_area_m2", "Total terminal area", "m²", "integer", 50000, 200000, 500000, ""),
        ("workforce_total_fte", "Total workforce", "FTE", "integer", 50, 200, 500, ""),
    ]

def common_relations_terminal_extra():
    """Standard counterparties present at any terminal."""
    return [
        ("port_authority", "Port authority", "regulator", "continuous",
         "1", "1", "1", "Concession granter"),
        ("customs", "Customs authority", "regulator", "per shipment",
         "1", "1", "1", ""),
        ("pcs_operator", "Port Community System (PCS)", "digital", "continuous",
         "1", "1", "1", "Portic / Uniport / etc."),
        ("pilotage_operator", "Pilotage service", "service", "per call",
         "1", "1", "1", ""),
        ("towage_operator", "Towage service", "service", "per call",
         "1", "1", "1", ""),
        ("mooring_operator", "Mooring service", "service", "per call",
         "1", "1", "1", ""),
        ("marpol_operator", "Port reception facility (MARPOL)", "service", "per call",
         "1", "1", "1", ""),
    ]


# ─────────────────────────────────────────────────────
# 2 — RoRo / Ro-Pax Terminal
# ─────────────────────────────────────────────────────
SPEC_RORO = {
    "archetype_id": "terminal_roro_ropax",
    "name": "RoRo / Ro-Pax Terminal",
    "category": "Terminal",
    "definition": "A RoRo/Ro-Pax Terminal handles roll-on/roll-off cargo and accompanying passengers. "
                  "Vessels self-load via stern/side ramps. Trailers, containers on MAFI, accompanied "
                  "trucks and passenger vehicles drive on/off. Ro-Pax adds passenger throughput "
                  "with terminal building, gangways, and check-in.",
    "tier_S": "≤ 250 000 trailers/year-eq · single ramp · regional service",
    "tier_M": "250 000 – 1 000 000 trailers/year-eq · 2-3 ramps · multi-route",
    "tier_L": "≥ 1 000 000 trailers/year-eq · 4+ ramps · hub for short-sea Mediterranean",
    "identity": common_identity_terminal(150000, 600000, 1500000, "trailer-eq/year") + [
        ("annual_passengers", "Annual passengers", "pax/year", "integer", 200000, 800000, 2500000, "Ro-Pax services"),
        ("annual_vehicles_accompanied", "Annual accompanied vehicles", "vehicles/year", "integer", 60000, 250000, 700000, ""),
        ("yard_area_m2", "Trailer staging yard area", "m²", "integer", 30000, 120000, 300000, ""),
        ("passenger_terminal_area_m2", "Passenger terminal building area", "m²", "integer", 800, 3500, 8000, "Ro-Pax only"),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 250, 600, 1200, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 8.0, 10.0, 12.0, ""),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 3, 5, ""),
        ("max_loa_m", "Maximum vessel LOA", "m", "integer", 200, 240, 280, ""),
        ("number_of_ramps", "Number of stern/side ramps", "ramps", "integer", 1, 3, 5, "Some berths have side ramps too"),
        ("max_ramp_load_t", "Maximum ramp load capacity", "t", "integer", 60, 120, 150, ""),
        ("trailer_parking_slots", "Trailer parking slots (yard)", "slots", "integer", 200, 800, 2000, ""),
        ("car_parking_slots", "Car parking slots (yard + check-in)", "slots", "integer", 100, 500, 1500, ""),
        ("gate_lanes_in", "Gate lanes — inbound", "lanes", "integer", 2, 4, 8, ""),
        ("gate_lanes_out", "Gate lanes — outbound", "lanes", "integer", 2, 3, 6, ""),
        ("on_dock_rail", "On-dock rail siding", "bool", "boolean", False, False, True, "Rail RoRo / autostrade ferroviarie"),
        ("rail_tracks_qty", "Rail tracks (if present)", "tracks", "integer", 0, 0, 2, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 16, 24, 24, ""),
        ("passenger_gangways_qty", "Passenger gangways", "gangways", "integer", 1, 3, 6, "Ro-Pax only"),
        ("ops_shore_power_available", "Ops/shore power available", "bool", "boolean", False, False, True, "AFIR mandates 2030"),
        ("modal_split_truck_pct", "Modal split — truck", "%", "number", 95, 90, 75, ""),
        ("modal_split_rail_pct", "Modal split — rail", "%", "number", 5, 10, 25, ""),
    ],
    "relations": [
        ("ferry_operator_main", "Main ferry/Ro-Pax operator", "inbound+outbound", "daily/weekly",
         "1-2 services", "3-5 services", "8+ services", "GNV, Grimaldi, Moby, Tirrenia, Baleària, etc."),
        ("ro_ro_cargo_operator", "Pure RoRo cargo operator", "inbound+outbound", "weekly",
         "1-2 services", "3-5 services", "10+ services", "Grimaldi, CLdN, Stena, etc."),
        ("road_haulier", "Road haulage company", "outbound", "continuous",
         "20-50", "100-300", "500+", ""),
        ("freight_forwarder", "Freight forwarder", "outbound", "continuous",
         "10-30", "60-150", "300+", ""),
        ("rail_operator", "Rail operator (rail RoRo)", "outbound", "daily",
         "0", "0-1", "1-3", "Autostrade ferroviarie"),
        ("passenger_services", "Passenger services / cafés / shops", "service", "continuous",
         "1-2 operators", "3-5 operators", "5+ operators", "Ro-Pax only"),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (terminal lighting, gates, building)", "scope_2"),
        ("yard_diesel", "Yard equipment diesel (tractors, mafi)", "scope_1"),
        ("vessels_at_berth_emissions", "Vessels at berth (auxiliary engines, attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": None,  # filled below
}

from pvw_builder import make_carbon_defaults

SPEC_RORO["defaults_M"] = make_carbon_defaults([
    ("electricity_grid",            1800),
    ("yard_diesel",                 2500),
    ("vessels_at_berth_emissions",  4500),
    ("staff_commuting",             400),
])


# ─────────────────────────────────────────────────────
# 3 — Cruise Terminal
# ─────────────────────────────────────────────────────
SPEC_CRUISE = {
    "archetype_id": "terminal_cruise",
    "name": "Cruise Terminal",
    "category": "Terminal",
    "definition": "A Cruise Terminal handles cruise ship calls: passenger embark/disembark, baggage, "
                  "provisioning, waste, fresh water and bunker scheduling. Operations are highly "
                  "scheduled (peaks at turnaround), with extensive passenger facilities (terminal "
                  "building, customs, immigration, transport hub).",
    "tier_S": "≤ 250 000 pax/year · 1 berth · seasonal port-of-call",
    "tier_M": "250 000 – 1 500 000 pax/year · 2-3 berths · year-round homeport",
    "tier_L": "≥ 1 500 000 pax/year · 4+ berths · major Mediterranean homeport",
    "identity": common_identity_terminal(150000, 800000, 2500000, "pax/year") + [
        ("annual_calls", "Annual cruise ship calls", "calls/year", "integer", 80, 350, 800, ""),
        ("homeport_calls_pct", "Share of calls as homeport (turnaround)", "%", "number", 20, 50, 75, ""),
        ("number_of_terminal_buildings", "Number of terminal buildings", "buildings", "integer", 1, 3, 7, ""),
        ("total_terminal_floor_m2", "Total terminal building floor area", "m²", "integer", 3000, 15000, 50000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 350, 1200, 3500, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 9.0, 11.0, 13.0, ""),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 3, 7, ""),
        ("max_loa_m", "Maximum vessel LOA", "m", "integer", 300, 340, 360, ""),
        ("max_pax_per_vessel", "Maximum pax capacity per vessel served", "pax", "integer", 3500, 5500, 7500, ""),
        ("passenger_gangways_qty", "Passenger gangways", "gangways", "integer", 2, 6, 14, ""),
        ("baggage_handling_lines", "Baggage handling lines", "lines", "integer", 2, 6, 14, ""),
        ("immigration_booths", "Immigration / passport control booths", "booths", "integer", 4, 12, 30, ""),
        ("bus_parking_slots", "Bus / coach parking slots", "slots", "integer", 10, 40, 100, "For excursions and homeport"),
        ("car_parking_slots", "Car parking slots", "slots", "integer", 100, 500, 2000, ""),
        ("ops_shore_power_available", "Ops/shore power available", "bool", "boolean", False, True, True, "AFIR mandates 2030"),
        ("ops_shore_power_kva", "Ops/shore power capacity per berth", "kVA", "integer", 0, 16000, 20000, "MV high-voltage typical"),
        ("provisioning_truck_bays", "Provisioning truck bays", "bays", "integer", 2, 6, 16, ""),
        ("waste_collection_bays", "Waste collection bays", "bays", "integer", 1, 3, 8, ""),
        ("fresh_water_bunker_capacity_m3h", "Fresh water bunker capacity per berth", "m³/h", "integer", 50, 100, 200, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 16, 20, 24, "Cruise ops often diurnal"),
        ("ops_days_per_year", "Operating days per year", "d", "integer", 200, 320, 365, "Highly seasonal in some ports"),
    ],
    "relations": [
        ("cruise_line_homeport", "Cruise line — homeport contracts", "inbound+outbound", "weekly",
         "1-2", "3-5", "6-10", "Costa, MSC, Royal Caribbean, Carnival, NCL"),
        ("cruise_line_port_of_call", "Cruise line — port of call", "inbound+outbound", "weekly",
         "5-10", "15-25", "30+", "Most major brands"),
        ("ground_handling_agents", "Ground handling agents (baggage, transfers)", "service", "per call",
         "1-2", "3-5", "5+", "Often subsidiaries of cruise lines"),
        ("excursion_operators", "Shore excursion operators", "service", "per call",
         "5-10", "20-50", "50+", ""),
        ("provisioning_suppliers", "Food/provisions suppliers", "inbound", "per call",
         "5-10", "20-40", "50+", ""),
        ("fresh_water_supplier", "Fresh water supplier (port utility)", "inbound", "per call",
         "1", "1", "1", "Usually port authority"),
        ("waste_management", "Waste management (cruise-specific)", "outbound", "per call",
         "1-2", "2-3", "3-5", "Often integrated with MARPOL operator"),
        ("bus_coach_companies", "Bus/coach companies (excursions)", "service", "per call",
         "5", "20", "50+", ""),
        ("rail_metro_connection", "Rail/metro connection (passenger access)", "service", "continuous",
         "0-1", "1", "1+", ""),
        ("airport_transfer_services", "Airport transfer services", "service", "per call",
         "2-5", "5-15", "15+", "Critical for homeport"),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (terminal buildings, lighting)", "scope_2"),
        ("ops_shore_power_supply", "Ops/shore power supplied to vessels (attributed)", "scope_2"),
        ("buildings_heat", "Terminal building HVAC", "scope_1+2"),
        ("vessels_at_berth_emissions", "Vessels at berth not on shore power (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
        ("bus_excursion_emissions", "Excursion bus traffic (attributed)", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            1500),
        ("ops_shore_power_supply",      2200),
        ("buildings_heat",              900),
        ("vessels_at_berth_emissions",  18000),
        ("staff_commuting",             500),
        ("bus_excursion_emissions",     1800),
    ]),
}


# ─────────────────────────────────────────────────────
# 4 — Vehicle Terminal (PCTC)
# ─────────────────────────────────────────────────────
SPEC_VEHICLE = {
    "archetype_id": "terminal_vehicle_pctc",
    "name": "Vehicle Terminal (PCTC)",
    "category": "Terminal",
    "definition": "A Vehicle Terminal handles Pure Car/Truck Carriers (PCTC) and high-and-heavy cargo. "
                  "Vehicles are driven on/off via stern ramps, then stored in vast surface yards "
                  "before dispatch by truck, rail, or feeder. Specialised in finished-vehicle logistics, "
                  "with PDI (Pre-Delivery Inspection) and value-added services often inland.",
    "tier_S": "≤ 200 000 units/year · 1-2 berths · single-brand or regional flow",
    "tier_M": "200 000 – 800 000 units/year · 2-3 berths · multi-brand with rail",
    "tier_L": "≥ 800 000 units/year · 4+ berths · automotive hub with PDI",
    "identity": common_identity_terminal(120000, 500000, 1200000, "vehicles/year") + [
        ("yard_capacity_units", "Yard parking capacity (vehicles)", "vehicles", "integer", 8000, 30000, 80000, "Static stock at any time"),
        ("yard_area_m2", "Yard area", "m²", "integer", 100000, 400000, 1000000, ""),
        ("pdi_capacity_units_yr", "Pre-Delivery Inspection capacity", "vehicles/year", "integer", 0, 100000, 400000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 250, 500, 1200, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 9.0, 11.0, 13.0, ""),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 3, 5, ""),
        ("max_loa_m", "Maximum PCTC LOA", "m", "integer", 200, 230, 265, ""),
        ("number_of_ramps", "Number of ramps", "ramps", "integer", 1, 3, 5, ""),
        ("yard_levels", "Yard parking levels", "levels", "integer", 1, 1, 2, "Multi-level lots in space-constrained ports"),
        ("driver_pool_qty", "Driver pool", "drivers", "integer", 30, 100, 300, "Move vehicles vessel-yard-truck"),
        ("on_dock_rail", "On-dock rail siding", "bool", "boolean", False, True, True, ""),
        ("rail_tracks_qty", "Rail tracks", "tracks", "integer", 0, 2, 5, ""),
        ("rail_track_length_m", "Useful rail track length", "m", "integer", 0, 600, 750, ""),
        ("car_carrier_truck_bays", "Car-carrier truck loading bays", "bays", "integer", 4, 10, 25, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 12, 20, 24, ""),
        ("modal_split_truck_pct", "Modal split — truck", "%", "number", 90, 70, 50, ""),
        ("modal_split_rail_pct", "Modal split — rail", "%", "number", 10, 30, 50, ""),
    ],
    "relations": [
        ("car_oem_manufacturer", "Car OEM / manufacturer", "inbound", "weekly",
         "1-2 brands", "3-5 brands", "8+ brands", "Toyota, Stellantis, BMW, etc."),
        ("pctc_shipping_line", "PCTC shipping line", "inbound+outbound", "weekly",
         "2-3", "5-8", "10+", "Wallenius Wilhelmsen, K Line, NYK, Grimaldi, etc."),
        ("car_carrier_haulage", "Car-carrier road haulage", "outbound", "continuous",
         "10-20", "50-100", "200+", ""),
        ("rail_operator", "Rail operator (auto-train)", "outbound", "daily",
         "0-1", "1-2", "2-4", ""),
        ("car_dealerships_distributors", "Car dealers / distributors", "outbound", "continuous",
         "50-200", "300-1000", "2000+", ""),
        ("pdi_workshop_provider", "PDI workshop provider", "service", "continuous",
         "0-1", "1-2", "2-4", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (yard lighting, offices)", "scope_2"),
        ("yard_vehicle_movements_fuel", "Vehicle movements within yard (fuel attributed)", "scope_3"),
        ("yard_diesel_equipment", "Yard equipment diesel (tractors)", "scope_1"),
        ("vessels_at_berth_emissions", "Vessels at berth (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",                1100),
        ("yard_vehicle_movements_fuel",     800),
        ("yard_diesel_equipment",           600),
        ("vessels_at_berth_emissions",      3500),
        ("staff_commuting",                 350),
    ]),
}


# ─────────────────────────────────────────────────────
# 5 — Multipurpose Terminal
# ─────────────────────────────────────────────────────
SPEC_MULTIPURPOSE = {
    "archetype_id": "terminal_multipurpose",
    "name": "Multipurpose Terminal",
    "category": "Terminal",
    "definition": "A Multipurpose Terminal handles mixed cargo: general cargo, project cargo, "
                  "minor bulks, occasional containers, sometimes RoRo. The terminal is more flexible "
                  "than specialised facilities and serves smaller volumes per cargo type. Common "
                  "in older / smaller ports or as overflow capacity in larger ports.",
    "tier_S": "≤ 200 000 t/year · 1 berth · niche cargo flows",
    "tier_M": "200 000 – 800 000 t/year · 2 berths · regional logistics hub",
    "tier_L": "≥ 800 000 t/year · 3+ berths · diversified multipurpose facility",
    "identity": common_identity_terminal(120000, 500000, 1200000, "t/year") + [
        ("cargo_mix_general_pct", "Cargo mix — general cargo", "%", "number", 40, 35, 30, ""),
        ("cargo_mix_project_pct", "Cargo mix — project cargo", "%", "number", 15, 20, 25, ""),
        ("cargo_mix_minor_bulk_pct", "Cargo mix — minor bulks", "%", "number", 35, 30, 25, ""),
        ("cargo_mix_container_pct", "Cargo mix — containers", "%", "number", 5, 10, 15, ""),
        ("cargo_mix_other_pct", "Cargo mix — other", "%", "number", 5, 5, 5, ""),
        ("warehouse_area_m2", "Covered warehouse area", "m²", "integer", 5000, 20000, 50000, ""),
        ("open_storage_area_m2", "Open storage area", "m²", "integer", 20000, 80000, 200000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 200, 400, 800, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 8.0, 10.0, 12.0, ""),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 2, 4, ""),
        ("mobile_harbour_cranes_qty", "Mobile harbour cranes", "cranes", "integer", 1, 3, 6, ""),
        ("max_lift_capacity_t", "Maximum lift capacity", "t", "integer", 80, 120, 200, ""),
        ("forklifts_qty", "Forklifts", "forklifts", "integer", 4, 12, 30, ""),
        ("reach_stackers_qty", "Reach stackers", "machines", "integer", 1, 3, 8, ""),
        ("on_dock_rail", "On-dock rail siding", "bool", "boolean", False, True, True, ""),
        ("rail_tracks_qty", "Rail tracks", "tracks", "integer", 0, 1, 3, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 12, 16, 20, ""),
    ],
    "relations": [
        ("breakbulk_shipping_line", "Breakbulk / general cargo shipping line", "inbound+outbound", "weekly",
         "1-3", "3-6", "6-12", ""),
        ("project_cargo_operator", "Project cargo / heavy lift operator", "inbound", "monthly",
         "0-2/year", "2-6/year", "6-15/year", ""),
        ("minor_bulk_trader", "Minor bulks trader (steel, fertiliser, etc.)", "inbound+outbound", "weekly",
         "5-10", "15-30", "30+", ""),
        ("warehouse_operator", "Warehouse / storage tenant", "service", "continuous",
         "1-3", "3-8", "8+", ""),
        ("road_haulier", "Road haulage company", "outbound", "continuous",
         "10-30", "30-80", "100+", ""),
        ("rail_operator", "Rail operator", "outbound", "weekly",
         "0", "0-1", "1-3", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (cranes, warehouse, lighting)", "scope_2"),
        ("yard_diesel", "Yard equipment diesel (forklifts, reach stackers)", "scope_1"),
        ("vessels_at_berth_emissions", "Vessels at berth (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            900),
        ("yard_diesel",                 1400),
        ("vessels_at_berth_emissions",  2200),
        ("staff_commuting",             250),
    ]),
}


# ─────────────────────────────────────────────────────
# 6 — Dry Bulk Terminal
# ─────────────────────────────────────────────────────
SPEC_DRYBULK = {
    "archetype_id": "terminal_dry_bulk",
    "name": "Dry Bulk Terminal",
    "category": "Terminal",
    "definition": "A Dry Bulk Terminal handles unpackaged dry commodities loaded/unloaded by gravity, "
                  "conveyor, or grab. Major flows: grains/agribulk, coal, iron ore, minerals, fertilisers, "
                  "cement. Storage in silos (agribulk) or open stockpiles (mineral). Often integrated with "
                  "rail or pipeline conveyor to inland processors.",
    "tier_S": "≤ 500 000 t/year · 1 berth · single commodity",
    "tier_M": "500 000 – 3 000 000 t/year · 1-2 berths · 2-3 commodities",
    "tier_L": "≥ 3 000 000 t/year · 2-3 berths · multi-commodity, deep-water, multimodal",
    "identity": common_identity_terminal(300000, 1500000, 5000000, "t/year") + [
        ("primary_commodity", "Primary commodity", "—", "enum", "grain", "grain+fertiliser", "grain+coal+iron ore",
         "grain / coal / iron ore / cement / fertiliser / mineral / etc."),
        ("silo_capacity_t", "Silo storage capacity", "t", "integer", 30000, 150000, 500000, "For agribulk"),
        ("open_stockpile_capacity_t", "Open stockpile capacity", "t", "integer", 0, 200000, 1500000, "For mineral, coal"),
        ("warehouse_capacity_t", "Covered warehouse capacity", "t", "integer", 5000, 30000, 100000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 200, 350, 700, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 11.0, 14.0, 18.0, "Capesize requires ≥17m"),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 2, 3, ""),
        ("max_loa_m", "Maximum vessel LOA", "m", "integer", 240, 290, 320, ""),
        ("ship_loaders_qty", "Ship loaders", "loaders", "integer", 1, 2, 4, "For exports"),
        ("ship_unloaders_qty", "Ship unloaders (continuous or grab)", "unloaders", "integer", 1, 2, 4, ""),
        ("loading_rate_tph", "Loading rate", "t/h", "integer", 1500, 4000, 8000, ""),
        ("unloading_rate_tph", "Unloading rate", "t/h", "integer", 1000, 3000, 6000, ""),
        ("conveyor_total_length_m", "Total conveyor system length", "m", "integer", 500, 2500, 8000, ""),
        ("hopper_qty", "Loading hoppers (truck/rail)", "hoppers", "integer", 2, 6, 14, ""),
        ("on_dock_rail", "On-dock rail siding", "bool", "boolean", False, True, True, ""),
        ("rail_tracks_qty", "Rail tracks", "tracks", "integer", 0, 2, 5, ""),
        ("dust_suppression_system", "Dust suppression system", "bool", "boolean", True, True, True, "Mandatory environmental"),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 16, 24, 24, ""),
    ],
    "relations": [
        ("commodity_trader", "Commodity trader", "inbound+outbound", "weekly",
         "2-5", "5-15", "15+", "Cargill, Bunge, ADM, Glencore, etc."),
        ("dry_bulk_shipping_line", "Dry bulk shipping operator", "inbound+outbound", "weekly",
         "5-10", "15-30", "30+", ""),
        ("inland_processor", "Inland processor / mill / power plant", "outbound", "weekly",
         "1-3", "3-8", "8-20", ""),
        ("rail_operator_freight", "Rail operator (bulk freight)", "outbound", "daily",
         "0-1", "1-2", "2-4", ""),
        ("road_haulier_bulk", "Bulk road haulage", "outbound", "continuous",
         "10-30", "30-80", "100+", ""),
        ("stevedoring_company", "Stevedoring company", "service", "continuous",
         "1", "1-2", "2-3", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (loaders, unloaders, conveyors)", "scope_2"),
        ("yard_diesel", "Yard equipment diesel (front loaders, dozers)", "scope_1"),
        ("dust_emissions", "Fugitive dust (PM10/2.5; CO2e equivalent small but reported)", "scope_1"),
        ("vessels_at_berth_emissions", "Vessels at berth (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            2500),
        ("yard_diesel",                 1200),
        ("dust_emissions",              50),
        ("vessels_at_berth_emissions",  3500),
        ("staff_commuting",             250),
    ]),
}


# ─────────────────────────────────────────────────────
# 7 — Liquid Bulk Terminal
# ─────────────────────────────────────────────────────
SPEC_LIQUIDBULK = {
    "archetype_id": "terminal_liquid_bulk",
    "name": "Liquid Bulk Terminal",
    "category": "Terminal",
    "definition": "A Liquid Bulk Terminal stores and transfers liquid commodities via pipeline: "
                  "petroleum products, crude oil, chemicals, vegetable oils, ethanol/biofuels. "
                  "Critical infrastructure typically Seveso-classified (upper or lower tier) due to "
                  "fire and toxicity hazards. Tank storage + manifold + jetty(s).",
    "tier_S": "≤ 200 000 m³ storage · 1 jetty · 1-2 product groups",
    "tier_M": "200 000 – 1 000 000 m³ storage · 2 jetties · multi-product",
    "tier_L": "≥ 1 000 000 m³ storage · 3+ jetties · refinery-grade infrastructure",
    "identity": common_identity_terminal(100000, 500000, 1500000, "m³ throughput/year") + [
        ("seveso_classification", "Seveso classification", "—", "enum",
         "Lower-tier", "Upper-tier", "Upper-tier",
         "Per EU Seveso III directive 2012/18/EU"),
        ("primary_product", "Primary product group", "—", "enum",
         "petroleum products", "petroleum + chemicals", "petroleum + chemicals + biofuels",
         "petroleum / crude / chemicals / vegoil / biofuels"),
        ("number_of_tanks", "Number of storage tanks", "tanks", "integer", 8, 25, 70, ""),
        ("total_storage_capacity_m3", "Total storage capacity", "m³", "integer", 100000, 500000, 2000000, ""),
        ("largest_tank_m3", "Largest single tank capacity", "m³", "integer", 30000, 60000, 120000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay/jetty length", "m", "integer", 200, 500, 1000, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 12.0, 16.0, 20.0, "VLCC requires 22m"),
        ("number_of_jetties", "Number of jetties", "jetties", "integer", 1, 2, 4, ""),
        ("max_loa_m", "Maximum vessel LOA", "m", "integer", 260, 300, 350, ""),
        ("loading_arms_per_jetty", "Loading arms per jetty", "arms", "integer", 4, 6, 10, ""),
        ("loading_rate_m3h", "Loading/unloading rate per jetty", "m³/h", "integer", 1500, 3500, 8000, ""),
        ("manifold_pumping_capacity_m3h", "Manifold pumping capacity", "m³/h", "integer", 2500, 6000, 15000, ""),
        ("vapour_recovery_system", "Vapour recovery system", "bool", "boolean", True, True, True, "EU directive"),
        ("fire_fighting_class", "Fire fighting class", "—", "enum",
         "FiFi-1", "FiFi-1", "FiFi-2", "FiFi-1=2400 m³/h, FiFi-2=7200 m³/h"),
        ("rail_tank_car_loading", "Rail tank car loading bays", "bays", "integer", 0, 4, 12, ""),
        ("truck_loading_bays", "Tank truck loading bays", "bays", "integer", 4, 10, 24, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 24, 24, 24, "Always 24/7"),
    ],
    "relations": [
        ("oil_major", "Oil major / IOC", "inbound+outbound", "weekly",
         "1-2", "2-4", "5+", "TotalEnergies, ENI, Repsol, BP, Shell, etc."),
        ("petroleum_trader", "Petroleum / chemical trader", "inbound+outbound", "weekly",
         "5-10", "15-30", "30+", "Vitol, Trafigura, Glencore, Mercuria, etc."),
        ("inland_pipeline_operator", "Inland pipeline operator", "outbound", "continuous",
         "0-1", "1-2", "2-3", ""),
        ("tank_truck_haulier", "Tank truck haulier (ADR)", "outbound", "continuous",
         "5-15", "20-50", "50+", "ADR-certified"),
        ("rail_operator_chemicals", "Rail operator (chemicals/petroleum)", "outbound", "weekly",
         "0", "1-2", "2-3", ""),
        ("refinery_operator", "Refinery operator (if integrated)", "service", "continuous",
         "0-1", "0-1", "1", "Some terminals are part of refinery complexes"),
        ("downstream_distributor", "Downstream fuel distributor", "outbound", "continuous",
         "5-15", "15-40", "40+", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (pumps, ancillary, lighting)", "scope_2"),
        ("steam_heat_process", "Steam/heat for product warming", "scope_1+2"),
        ("fugitive_voc_emissions", "Fugitive VOC emissions (CO2e equivalent)", "scope_1"),
        ("vessels_at_berth_emissions", "Vessels at berth (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            1800),
        ("steam_heat_process",          1500),
        ("fugitive_voc_emissions",      400),
        ("vessels_at_berth_emissions",  3000),
        ("staff_commuting",             200),
    ]),
}


# ─────────────────────────────────────────────────────
# 9 — LNG Regasification Terminal
# ─────────────────────────────────────────────────────
SPEC_LNG = {
    "archetype_id": "terminal_lng_regasification",
    "name": "LNG Regasification Terminal",
    "category": "Terminal",
    "definition": "An LNG Regasification Terminal receives LNG carriers, stores cryogenic LNG at "
                  "-162°C, regasifies it via vaporisers (open-rack, submerged-combustion, or "
                  "ambient-air), and injects natural gas into the national transmission grid. "
                  "May also support truck loading, ship-to-ship LNG bunkering, and rail loading.",
    "tier_S": "≤ 5 bcm/year regas capacity · 1 jetty · 1-2 tanks",
    "tier_M": "5 – 12 bcm/year regas capacity · 1-2 jetties · 2-3 tanks",
    "tier_L": "≥ 12 bcm/year regas capacity · 2+ jetties · 3+ tanks · multi-modal bunkering",
    "identity": common_identity_terminal(3, 8, 18, "bcm/year regas") + [
        ("number_of_tanks", "Number of LNG storage tanks", "tanks", "integer", 1, 3, 5, ""),
        ("total_storage_capacity_m3_lng", "Total LNG storage capacity", "m³ LNG", "integer", 150000, 450000, 900000, ""),
        ("largest_tank_m3_lng", "Largest single tank capacity", "m³ LNG", "integer", 150000, 160000, 180000, "Typical full-containment"),
        ("seveso_classification", "Seveso classification", "—", "enum", "Upper-tier", "Upper-tier", "Upper-tier", "LNG always upper-tier"),
        ("emergency_zone_radius_m", "Emergency planning zone radius", "m", "integer", 1000, 1500, 2500, ""),
    ],
    "equipment": [
        ("quay_length_m", "Jetty length", "m", "integer", 350, 450, 600, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 12.0, 14.0, 16.0, ""),
        ("number_of_jetties", "Number of jetties", "jetties", "integer", 1, 1, 2, ""),
        ("max_loa_m", "Maximum LNG carrier LOA", "m", "integer", 290, 320, 345, "Q-Max class = 345m"),
        ("max_carrier_capacity_m3", "Maximum LNG carrier capacity", "m³ LNG", "integer", 173000, 200000, 266000, "Q-Max = 266 000 m³"),
        ("unloading_arms_qty", "LNG unloading arms", "arms", "integer", 3, 4, 5, "3 liquid + 1 vapour return"),
        ("unloading_rate_m3h_lng", "LNG unloading rate", "m³/h", "integer", 8000, 14000, 18000, ""),
        ("vaporiser_qty", "Vaporiser units", "units", "integer", 4, 8, 14, ""),
        ("vaporiser_type", "Primary vaporiser type", "—", "enum",
         "ORV", "ORV", "ORV+SCV", "ORV (open-rack) / SCV (submerged combustion) / AAV (ambient air)"),
        ("regas_send_out_capacity_nm3h", "Send-out capacity", "Nm³/h", "integer", 600000, 1500000, 3500000, ""),
        ("truck_loading_bays_lng", "LNG truck loading bays", "bays", "integer", 0, 2, 6, ""),
        ("rail_tank_car_loading_bays_lng", "Rail LNG tank car loading bays", "bays", "integer", 0, 0, 2, ""),
        ("sts_bunkering_supported", "Ship-to-ship LNG bunkering supported", "bool", "boolean", False, True, True, ""),
        ("bog_recovery_system", "Boil-off-gas recovery system", "bool", "boolean", True, True, True, "Mandatory"),
        ("fire_fighting_class", "Fire fighting class", "—", "enum", "FiFi-2", "FiFi-2", "FiFi-2", "Mandatory for LNG"),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 24, 24, 24, ""),
    ],
    "relations": [
        ("lng_supplier_country", "LNG supplier country (sources)", "inbound", "monthly",
         "1-2", "3-5", "6-12", "USA, Qatar, Algeria, Nigeria, etc."),
        ("lng_carrier_operator", "LNG carrier operator", "inbound", "weekly",
         "5-10", "15-30", "30+", ""),
        ("national_gas_grid_operator", "National gas grid operator (TSO)", "outbound", "continuous",
         "1", "1", "1", "Enagás (ES), Snam (IT), GRTgaz (FR), etc."),
        ("gas_shipper", "Gas shipper / trader", "outbound", "continuous",
         "5-10", "15-30", "30+", ""),
        ("lng_truck_haulier", "LNG tank truck haulier", "outbound", "continuous",
         "0-2", "3-8", "10+", "ADR cryogenic"),
        ("lng_bunker_barge_operator", "LNG bunker barge / STS operator", "outbound", "weekly",
         "0", "0-1", "1-3", ""),
        ("rail_operator_lng", "Rail operator (LNG tank cars)", "outbound", "weekly",
         "0", "0", "0-1", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (pumps, control, ancillary)", "scope_2"),
        ("scv_combustion", "SCV vaporiser combustion (if used)", "scope_1"),
        ("bog_combustion", "BOG combustion (excess boil-off)", "scope_1"),
        ("methane_fugitive", "Fugitive methane emissions (CO2e via GWP)", "scope_1"),
        ("vessels_at_berth_emissions", "LNG carriers at berth (attributed)", "scope_3"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            8500),
        ("scv_combustion",              4500),
        ("bog_combustion",              1200),
        ("methane_fugitive",            900),
        ("vessels_at_berth_emissions",  2200),
        ("staff_commuting",             300),
    ]),
}

ALL_TERMINAL_SPECS = [SPEC_RORO, SPEC_CRUISE, SPEC_VEHICLE, SPEC_MULTIPURPOSE, SPEC_DRYBULK, SPEC_LIQUIDBULK, SPEC_LNG]


# ─────────────────────────────────────────────────────
# 1 — Container Terminal (added retroactively)
# ─────────────────────────────────────────────────────
SPEC_CONTAINER = {
    "archetype_id": "terminal_container",
    "name": "Container Terminal",
    "category": "Terminal",
    "definition": "A Container Terminal is a port facility specialised in handling intermodal "
                  "containers (TEU, FEU). It operates ship-to-shore (STS) gantry cranes on a "
                  "deep-water quay, transfers containers to and from a stacking yard via "
                  "horizontal-transport equipment (straddle carriers, RTGs, terminal tractors), "
                  "and dispatches via truck or rail to the hinterland.",
    "tier_S": "≤ 500 000 TEU/year · 1-2 STS cranes · single quay · feeder-vessel oriented",
    "tier_M": "500 000 – 1 500 000 TEU/year · 4-8 STS cranes · 1-2 deep-water berths · mainline + feeder mix",
    "tier_L": "≥ 1 500 000 TEU/year · 10+ STS cranes · 2+ deep-water berths · ULCV-capable · multi-modal hub",
    "identity": common_identity_terminal(300000, 1000000, 2500000, "TEU/year") + [
        ("yard_area_m2", "Container yard area", "m²", "integer", 100000, 350000, 700000, ""),
    ],
    "equipment": [
        ("quay_length_m", "Quay length", "m", "integer", 400, 800, 1600, ""),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 12.0, 14.0, 16.5, ""),
        ("number_of_berths", "Number of berths", "berths", "integer", 1, 2, 3, ""),
        ("max_loa_m", "Maximum vessel LOA", "m", "integer", 300, 366, 400, ""),
        ("sts_panamax_qty", "STS cranes — Panamax", "cranes", "integer", 1, 1, 0, "Up to ~13 rows outreach"),
        ("sts_post_panamax_qty", "STS cranes — Post-Panamax", "cranes", "integer", 1, 3, 4, "14-18 rows outreach"),
        ("sts_super_post_panamax_qty", "STS cranes — Super Post-Panamax", "cranes", "integer", 0, 2, 6, "19-24 rows outreach; for ULCV"),
        ("max_outreach_rows", "Maximum outreach (rows)", "rows", "integer", 16, 19, 24, ""),
        ("yard_equipment_type", "Yard equipment system", "—", "enum", "RTG", "Mixed (RTG + reach stackers)", "Straddle carriers + ASC", "RMG/RTG/ASC/SC/RS"),
        ("yard_machines_qty", "Yard machines", "machines", "integer", 8, 25, 80, ""),
        ("reefer_plugs_qty", "Reefer plugs", "plugs", "integer", 100, 350, 900, ""),
        ("gate_lanes_in", "Gate lanes — inbound", "lanes", "integer", 3, 5, 10, ""),
        ("gate_lanes_out", "Gate lanes — outbound", "lanes", "integer", 2, 3, 6, ""),
        ("ocr_gates", "OCR / automated gate access", "bool", "boolean", False, True, True, ""),
        ("on_dock_rail", "On-dock rail siding", "bool", "boolean", False, True, True, ""),
        ("rail_tracks_qty", "Number of rail tracks", "tracks", "integer", 0, 2, 6, ""),
        ("rail_track_length_m", "Useful rail track length per track", "m", "integer", 0, 700, 750, ""),
        ("ops_hours_per_day", "Operating hours per day", "h", "integer", 16, 24, 24, ""),
        ("ops_days_per_year", "Operating days per year", "d", "integer", 300, 360, 365, ""),
        ("modal_split_truck_pct", "Modal split — truck", "%", "number", 95, 80, 65, ""),
        ("modal_split_rail_pct", "Modal split — rail", "%", "number", 5, 20, 35, ""),
        ("modal_split_barge_pct", "Modal split — short-sea barge", "%", "number", 0, 0, 0, ""),
    ],
    "relations": [
        ("shipping_line_mainline", "Mainline container shipping line", "inbound+outbound", "weekly",
         "1-3 services", "5-10 services", "15+ services", "MSC, Maersk, CMA CGM"),
        ("shipping_line_feeder", "Feeder shipping line", "inbound+outbound", "daily/weekly",
         "5-10 services", "15-25 services", "30+ services", "X-Press Feeders, Unifeeder"),
        ("freight_forwarder", "Freight forwarder", "outbound", "continuous",
         "20-50", "100-300", "500+", ""),
        ("road_haulier", "Road haulage company", "outbound", "continuous",
         "30-80", "150-400", "800+", ""),
        ("rail_operator", "Rail operator", "outbound", "daily",
         "0-1", "1-3", "3-6", ""),
        ("inland_terminal", "Inland container terminal / dry port", "outbound", "continuous",
         "0-2", "2-5", "5-15", ""),
    ] + common_relations_terminal_extra(),
    "sources": [
        ("electricity_grid", "Grid electricity (cranes, lights, reefer)", "scope_2"),
        ("yard_diesel", "Yard equipment diesel (RTGs, reach stackers, tractors)", "scope_1"),
        ("on_dock_rail_diesel", "On-dock rail shunting diesel", "scope_1"),
        ("buildings_heat", "Buildings — heat / HVAC", "scope_1+2"),
        ("staff_commuting", "Staff commuting (attributed)", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",      3500),
        ("yard_diesel",           4200),
        ("on_dock_rail_diesel",   800),
        ("buildings_heat",        280),
        ("staff_commuting",       400),
    ]),
}

# Update the export list to include Container as #1
ALL_TERMINAL_SPECS = [SPEC_CONTAINER, SPEC_RORO, SPEC_CRUISE, SPEC_VEHICLE,
                     SPEC_MULTIPURPOSE, SPEC_DRYBULK, SPEC_LIQUIDBULK, SPEC_LNG]
