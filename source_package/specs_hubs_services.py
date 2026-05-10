"""Specs for Hub archetypes (8, 10, 11) and mandatory Services (12-15)."""
from pvw_builder import make_carbon_defaults
from specs_terminals import common_identity_terminal, common_relations_terminal_extra


# ─────────────────────────────────────────────────────
# 8 — Biorefinery / e-Fuels Hub
# ─────────────────────────────────────────────────────
SPEC_BIOREFINERY = {
    "archetype_id": "hub_biorefinery_efuels",
    "name": "Biorefinery / e-Fuels Hub",
    "category": "Industrial Hub",
    "definition": "An industrial site producing renewable fuels from biomass (HVO from used cooking oil, "
                  "tallow, vegetable oils) and/or e-fuels (e-methanol, e-SAF, e-diesel from green H2 + "
                  "captured CO2). Typically a converted petroleum refinery or a greenfield green facility. "
                  "Often co-located with a port for inbound feedstock and outbound finished product.",
    "tier_S": "≤ 200 000 t/year output · single product line · pilot/early commercial",
    "tier_M": "200 000 – 800 000 t/year · 2-3 product lines · regional supply",
    "tier_L": "≥ 800 000 t/year · multi-line + e-fuels · industrial integrated complex",
    "identity": common_identity_terminal(150000, 500000, 1200000, "t/year output") + [
        ("primary_pathway", "Primary production pathway", "—", "enum",
         "HVO (UCO/tallow)", "HVO + biomethane", "HVO + biomethane + e-fuels",
         "HVO / biomethane / e-methanol / e-SAF / pyrolysis / etc."),
        ("seveso_classification", "Seveso classification", "—", "enum",
         "Lower-tier", "Upper-tier", "Upper-tier", ""),
        ("feedstock_storage_capacity_m3", "Feedstock storage capacity", "m³", "integer", 30000, 100000, 300000, ""),
        ("product_storage_capacity_m3", "Product storage capacity", "m³", "integer", 50000, 150000, 400000, ""),
    ],
    "equipment": [
        ("hydrotreatment_capacity_t_yr", "Hydrotreatment capacity (HVO)", "t/year", "integer", 200000, 500000, 1000000, ""),
        ("biomethane_capacity_nm3_yr", "Biomethane upgrading capacity", "Nm³/year", "integer", 0, 30000000, 80000000, ""),
        ("electrolyser_capacity_mw", "Electrolyser capacity (e-fuels)", "MW", "integer", 0, 0, 200, "Green H2 production"),
        ("co2_capture_capacity_t_yr", "CO2 capture capacity (e-fuels)", "t/year", "integer", 0, 0, 250000, ""),
        ("e_methanol_capacity_t_yr", "e-Methanol synthesis capacity", "t/year", "integer", 0, 0, 100000, ""),
        ("internal_h2_pipeline_km", "Internal hydrogen pipeline", "km", "number", 0, 0, 5, ""),
        ("quay_length_m", "Quay length (own jetty)", "m", "integer", 0, 250, 500, "Some hubs port-adjacent without own jetty"),
        ("quay_max_draft_m", "Maximum quay draft", "m", "number", 0, 12.0, 16.0, ""),
        ("rail_loading_bays", "Rail tank car loading bays", "bays", "integer", 2, 6, 12, ""),
        ("truck_loading_bays", "Tank truck loading bays", "bays", "integer", 4, 10, 24, ""),
    ],
    "relations": [
        ("feedstock_supplier_uco", "UCO / waste oil supplier", "inbound", "weekly",
         "5-15", "20-50", "50+", "Restaurants, collectors, traders"),
        ("feedstock_supplier_agro", "Agricultural feedstock supplier", "inbound", "weekly",
         "5-10", "15-30", "30+", "Vegetable oils, tallow"),
        ("renewable_electricity_supplier", "Renewable electricity supplier (PPA)", "inbound", "continuous",
         "1-2 PPAs", "2-4 PPAs", "4+ PPAs", "For e-fuels"),
        ("co2_source", "CO2 source (capture or biogenic)", "inbound", "continuous",
         "0-1", "1-2", "2-3", "Cement, biomethane plant, etc."),
        ("offtaker_road_fuel_distributor", "Road fuel distributor (offtaker)", "outbound", "continuous",
         "2-5", "5-15", "15+", ""),
        ("offtaker_aviation_saf", "SAF aviation offtaker", "outbound", "continuous",
         "0", "0-2", "2-5", "Airlines, jet fuel suppliers"),
        ("offtaker_marine_bunker", "Marine bunker offtaker", "outbound", "continuous",
         "0-2", "2-5", "5-10", ""),
        ("certification_body", "Sustainability certification body", "regulator", "continuous",
         "1", "1-2", "2-3", "ISCC EU, REDcert, etc."),
        ("port_authority", "Port authority", "regulator", "continuous", "1", "1", "1", ""),
        ("national_environment_authority", "National environment / industrial regulator", "regulator", "continuous",
         "1", "1", "1", ""),
    ],
    "sources": [
        ("electricity_grid", "Grid electricity (process)", "scope_2"),
        ("process_heat", "Process heat (steam, hydrogen feed)", "scope_1"),
        ("hydrogen_supply_emissions", "Hydrogen supply (grey/blue/green attributed)", "scope_3"),
        ("fugitive_voc_emissions", "Fugitive VOC emissions", "scope_1"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            12000),
        ("process_heat",                8500),
        ("hydrogen_supply_emissions",   2500),
        ("fugitive_voc_emissions",      400),
        ("staff_commuting",             400),
    ]),
}


# ─────────────────────────────────────────────────────
# 10 — Freight Village (Interporto / Logistics Park)
# ─────────────────────────────────────────────────────
SPEC_FREIGHT_VILLAGE = {
    "archetype_id": "freight_village",
    "name": "Freight Village",
    "category": "Logistics Hub",
    "definition": "An inland intermodal logistics platform combining road-rail terminals, warehousing, "
                  "customs services, distribution centres, and ancillary services. Acts as a hinterland "
                  "extension of seaports for container and trailer flows. Terms: Interporto (IT), "
                  "Centre Routier / Plateforme Logistique (FR), Güterverkehrszentrum (DE), "
                  "Centro de Transportes (ES), Freight Village (UK).",
    "tier_S": "≤ 1 000 000 m² · 1 intermodal terminal · regional",
    "tier_M": "1 000 000 – 4 000 000 m² · 1-2 intermodal terminals · multi-modal",
    "tier_L": "≥ 4 000 000 m² · 2+ intermodal terminals · international gateway",
    "identity": common_identity_terminal(800000, 2500000, 5000000, "m² total area") + [
        ("intermodal_terminal_qty", "Intermodal terminals on site", "terminals", "integer", 1, 1, 3, ""),
        ("warehouse_total_m2", "Total warehouse floor area", "m²", "integer", 100000, 400000, 1500000, ""),
        ("distribution_centres_qty", "Distribution centres", "DCs", "integer", 5, 25, 80, ""),
        ("offices_total_m2", "Total office floor area", "m²", "integer", 5000, 25000, 80000, ""),
        ("on_site_companies", "Companies operating on site", "companies", "integer", 20, 100, 350, ""),
        ("on_site_workforce", "On-site workforce (all tenants)", "FTEs", "integer", 1500, 6000, 20000, ""),
    ],
    "equipment": [
        ("rail_tracks_total_qty", "Total rail tracks (intermodal)", "tracks", "integer", 4, 10, 20, ""),
        ("rail_tracks_total_length_m", "Total rail track length (operational)", "m", "integer", 3000, 10000, 25000, ""),
        ("intermodal_cranes_qty", "Reach stackers / RMG cranes (intermodal)", "machines", "integer", 4, 12, 30, ""),
        ("annual_intermodal_units", "Annual intermodal units handled", "UTI/year", "integer", 100000, 400000, 1000000, ""),
        ("truck_parking_slots", "Truck parking slots", "slots", "integer", 100, 500, 2000, ""),
        ("car_parking_slots", "Car parking slots", "slots", "integer", 500, 2000, 8000, ""),
        ("gate_lanes_qty", "Total gate lanes (incoming + outgoing)", "lanes", "integer", 4, 12, 30, ""),
        ("customs_offices_on_site", "Customs offices on site", "offices", "integer", 1, 1, 3, "Often AEO Centro Doganale"),
        ("ev_charging_stations_qty", "EV charging stations (heavy + light)", "stations", "integer", 0, 8, 30, ""),
        ("solar_pv_capacity_mw", "Solar PV installed capacity", "MW", "number", 0.5, 5.0, 30.0, "Rooftop typical"),
    ],
    "relations": [
        ("port_authority_connected", "Connected seaport(s)", "outbound", "continuous",
         "1", "1-2", "2-4", "Hinterland link"),
        ("rail_freight_operator", "Rail freight operator", "outbound", "daily",
         "1-2", "3-5", "5-10", ""),
        ("logistics_tenant_3pl", "Logistics tenant (3PL)", "tenant", "continuous",
         "5-15", "20-50", "50+", "DHL, Kuehne+Nagel, DSV, etc."),
        ("retailer_distribution_centre", "Retailer DC tenant", "tenant", "continuous",
         "2-5", "10-30", "30-80", "Amazon, Inditex, IKEA, etc."),
        ("manufacturer_dc", "Manufacturer DC tenant", "tenant", "continuous",
         "2-5", "5-15", "15-30", ""),
        ("road_haulage_companies", "Road haulage companies (transit)", "service", "continuous",
         "100+", "300+", "1000+", ""),
        ("freight_forwarder_offices", "Freight forwarder offices", "tenant", "continuous",
         "5-10", "15-40", "40+", ""),
        ("customs_authority", "Customs authority", "regulator", "continuous",
         "1", "1", "1", ""),
        ("regional_authority", "Regional / municipal authority", "regulator", "continuous",
         "1", "1", "1", "Often shareholder of the village"),
        ("port_community_system", "Port Community System (digital link)", "digital", "continuous",
         "1", "1", "1", ""),
    ],
    "sources": [
        ("electricity_grid", "Grid electricity (warehouses, offices, intermodal cranes)", "scope_2"),
        ("buildings_heat", "Buildings heat / HVAC", "scope_1+2"),
        ("intermodal_diesel", "Intermodal diesel (reach stackers, shunting)", "scope_1"),
        ("road_traffic_emissions", "On-site road traffic (attributed share)", "scope_3"),
        ("staff_commuting", "Staff commuting (high — large workforce)", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid",            8500),
        ("buildings_heat",              4200),
        ("intermodal_diesel",           2800),
        ("road_traffic_emissions",      9500),
        ("staff_commuting",             3500),
    ]),
}


# ─────────────────────────────────────────────────────
# 11 — Multi-Energy Bunker Hub
# ─────────────────────────────────────────────────────
SPEC_BUNKER_HUB = {
    "archetype_id": "hub_multi_energy_bunker",
    "name": "Multi-Energy Bunker Hub",
    "category": "Energy Hub",
    "definition": "A port-based operator delivering fuels and energy to ships AND to land transport: "
                  "marine bunkering (IFO/MGO, LNG, bio-LNG, biofuels, future fuels), land filling stations "
                  "(petrol/diesel, CNG/LNG, H2, EV charging), with own barge berth for STS bunkering "
                  "operations. Embodies the dual maritime + road energy transition.",
    "tier_S": "≤ 100 000 t/year bunkering · 1 land station · single delivery mode",
    "tier_M": "100 000 – 400 000 t/year · multi-fuel marine + land · TtS+STS",
    "tier_L": "≥ 400 000 t/year · multi-fuel marine + multi-station land · TtS+STS+pipeline+rail",
    "identity": common_identity_terminal(80000, 250000, 600000, "t/year bunkering") + [
        ("seveso_classification", "Seveso classification", "—", "enum", "Upper-tier", "Upper-tier", "Upper-tier", ""),
        ("marine_fuels_handled", "Marine fuels handled", "—", "enum",
         "MGO + IFO", "MGO + IFO + LNG + bio-LNG", "All including methanol + e-fuels",
         ""),
        ("land_station_types", "Land station types operated", "—", "enum",
         "petrol+diesel", "petrol+diesel+CNG+LNG+EV", "petrol+diesel+CNG+LNG+H2+EV+MCS",
         ""),
        ("storage_capacity_total_m3", "Total fuel storage capacity", "m³", "integer", 30000, 120000, 400000, ""),
    ],
    "equipment": [
        ("barge_berth_qty", "Barge berths (own infrastructure)", "berths", "integer", 1, 1, 2, ""),
        ("barge_berth_length_m", "Barge berth length", "m", "integer", 60, 80, 120, ""),
        ("cryogenic_loading_arms_qty", "Cryogenic loading arms (LNG/bio-LNG)", "arms", "integer", 0, 4, 6, ""),
        ("liquid_loading_arms_qty", "Liquid loading arms (IFO/MGO/biofuel)", "arms", "integer", 2, 4, 8, ""),
        ("annual_barge_loadings", "Annual barge loadings", "loadings/year", "integer", 100, 280, 600, ""),
        ("tts_truck_loading_bays", "TtS truck loading bays", "bays", "integer", 1, 2, 4, ""),
        ("land_petrol_diesel_dispensers", "Land — petrol/diesel dispensers", "dispensers", "integer", 4, 8, 16, ""),
        ("land_cng_dispensers", "Land — CNG dispensers", "dispensers", "integer", 0, 2, 4, ""),
        ("land_lng_dispensers", "Land — LNG dispensers (truck)", "dispensers", "integer", 0, 2, 4, ""),
        ("land_h2_dispensers_350bar", "Land — H2 350 bar dispensers (heavy)", "dispensers", "integer", 0, 2, 4, ""),
        ("land_h2_dispensers_700bar", "Land — H2 700 bar dispensers (light)", "dispensers", "integer", 0, 2, 4, ""),
        ("land_ev_chargers_dc_fast", "Land — EV DC fast chargers (CCS)", "stations", "integer", 0, 6, 16, ""),
        ("land_ev_chargers_mcs", "Land — EV Megawatt Chargers (MCS)", "stations", "integer", 0, 0, 4, "For heavy trucks"),
        ("alternative_fuels_status", "Future fuels infrastructure", "—", "string",
         "planned: methanol/H2", "operational: bio-LNG; piloting: methanol",
         "operational: methanol+bio-LNG; piloting: ammonia",
         "Status: planned/pilot/operational"),
    ],
    "relations": [
        ("oil_refinery", "Oil refinery (IFO/MGO supplier)", "inbound", "weekly",
         "1-2", "2-3", "3+", "ENI, TotalEnergies, Repsol, etc."),
        ("lng_terminal", "LNG regasification terminal (LNG/bio-LNG)", "inbound", "weekly",
         "0-1", "1-2", "2-3", "Enagás, Snam, OLT, etc."),
        ("biofuel_producer", "Biofuel producer (HVO, FAME, bio-LNG)", "inbound", "weekly",
         "0-1", "2-4", "4-8", "Neste, ENI Sustainable Mobility, etc."),
        ("h2_producer", "Hydrogen producer (grey/blue/green)", "inbound", "weekly",
         "0", "1-2", "2-4", "Air Liquide, Linde, etc."),
        ("electricity_grid_operator", "Electricity grid operator", "inbound", "continuous",
         "1", "1", "1", ""),
        ("renewable_ppa_operator", "Renewable energy PPA / on-site solar", "inbound", "continuous",
         "0-1", "1-2", "2-4", ""),
        ("ferry_operator_marine", "Ferry/Ro-Pax operator (marine bunker customer)", "outbound", "per call",
         "5-10", "15-30", "30+", ""),
        ("cruise_operator_marine", "Cruise operator (marine bunker customer)", "outbound", "per call",
         "0-2", "5-15", "20+", ""),
        ("container_line_marine", "Container line (marine bunker customer)", "outbound", "per call",
         "5-10", "15-30", "30+", ""),
        ("downstream_bunker_barge", "Downstream bunker barge operator", "outbound", "weekly",
         "0-1", "1-2", "2-4", ""),
        ("road_haulier_fleet", "Road haulier fleet (land station customer)", "outbound", "continuous",
         "20-50", "100-300", "500+", ""),
        ("public_transport_operator", "Public transport operator (bus, taxi)", "outbound", "continuous",
         "1-2", "2-5", "5-10", ""),
        ("port_authority", "Port authority", "regulator", "continuous", "1", "1", "1", ""),
        ("harbour_master", "Harbour Master (bunker authorisation)", "regulator", "per operation", "1", "1", "1", ""),
        ("customs_authority", "Customs authority (excise on fuels)", "regulator", "continuous", "1", "1", "1", ""),
    ],
    "sources": [
        ("electricity_grid_compressors", "Grid electricity (pumps, compressors, BOG, EV chargers)", "scope_2"),
        ("methane_fugitive", "Fugitive methane (LNG handling, CO2e via GWP)", "scope_1"),
        ("h2_fugitive", "Fugitive H2 emissions (CO2e equivalent)", "scope_1"),
        ("on_site_combustion", "On-site combustion (heaters, gensets)", "scope_1"),
        ("internal_truck_movements", "Internal truck movements", "scope_1"),
        ("staff_commuting", "Staff commuting", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("electricity_grid_compressors",  1800),
        ("methane_fugitive",              900),
        ("h2_fugitive",                   25),
        ("on_site_combustion",            400),
        ("internal_truck_movements",      180),
        ("staff_commuting",               150),
    ]),
}


# ─────────────────────────────────────────────────────
# 12 — Pilotage Service
# ─────────────────────────────────────────────────────
SPEC_PILOTAGE = {
    "archetype_id": "service_pilotage",
    "name": "Pilotage Service",
    "category": "Mandatory Service",
    "definition": "A mandatory technical-nautical service: licensed pilots board incoming/outgoing "
                  "vessels at a designated boarding station and advise the master during port "
                  "manoeuvres. Typically granted under exclusive licence to a single operator per "
                  "port (corporación de prácticos / corporazione dei piloti / pilots corporation).",
    "tier_S": "≤ 4 000 ops/year · 6-8 pilots · single boarding station",
    "tier_M": "4 000 – 10 000 ops/year · 10-15 pilots · 2 launches",
    "tier_L": "≥ 10 000 ops/year · 18+ pilots · 3+ launches · 24/7 dispatch",
    "identity": [
        ("operator_legal_name", "Operator legal name", "—", "string",
         "[Pilotage corporation S]", "[Pilotage corporation M]", "[Pilotage corporation L]", ""),
        ("operator_short_name", "Commercial name", "—", "string", "—", "—", "—", ""),
        ("port_unlocode", "Port (UN/LOCODE)", "—", "enum", "—", "—", "—", ""),
        ("port_name", "Port name", "—", "string", "—", "—", "—", ""),
        ("country_iso2", "Country (ISO 3166-1 alpha-2)", "—", "enum", "—", "—", "—", ""),
        ("legal_form", "Legal form", "—", "enum", "S.L.P.", "S.L.P.", "S.L.P.",
         "S.L.P. (ES) / Corporazione (IT) / equivalent"),
        ("licence_type", "Licence type", "—", "enum", "Exclusive", "Exclusive", "Exclusive",
         "Almost always exclusive per port"),
        ("licence_end_year", "Licence end year", "year", "integer", "—", "—", "—", ""),
        ("year_founded", "Year founded", "year", "integer", "—", "—", "—", ""),
        ("annual_pilotage_operations", "Annual pilotage operations", "ops/year", "integer", 2500, 7000, 15000, ""),
        ("number_of_pilots", "Number of licensed pilots", "pilots", "integer", 7, 12, 22, ""),
        ("workforce_total_fte", "Total workforce (incl. boat crews + admin)", "FTE", "integer", 18, 35, 65, ""),
        ("size_tier", "Size tier", "—", "enum", "S", "M", "L", ""),
        ("isps_certified", "ISPS code certification", "bool", "boolean", True, True, True, ""),
        ("iso_9001", "ISO 9001 quality", "bool", "boolean", True, True, True, ""),
        ("service_24_7", "Service 24/7", "bool", "boolean", True, True, True, ""),
    ],
    "equipment": [
        ("pilot_launches_qty", "Pilot launches", "launches", "integer", 2, 3, 5, ""),
        ("launch_typical_length_m", "Typical launch length", "m", "number", 12, 14, 16, ""),
        ("launch_typical_speed_kn", "Typical launch speed", "kn", "integer", 22, 25, 28, ""),
        ("pilot_boarding_distance_nm", "Pilot boarding station distance", "NM", "number", 1.0, 1.5, 3.0, ""),
        ("ppu_units_qty", "Pilot Portable Units (PPU)", "units", "integer", 7, 12, 22, "ECDIS-style tablets"),
        ("vhf_radios_qty", "VHF radios", "units", "integer", 12, 18, 30, ""),
        ("control_room_24_7", "Control room 24/7 staffed", "bool", "boolean", True, True, True, ""),
        ("avg_op_duration_min", "Average operation duration", "min", "integer", 60, 90, 120, ""),
        ("avg_fuel_per_op_l", "Average launch fuel per op", "L MGO", "integer", 35, 60, 100, ""),
    ],
    "relations": [
        ("vessel_calls", "Vessels (all categories)", "service", "per call",
         "2 500", "7 000", "15 000+", "All commercial vessels above thresholds"),
        ("port_authority", "Port authority (concession)", "regulator", "continuous", "1", "1", "1", ""),
        ("harbour_master", "Harbour Master (licensing)", "regulator", "continuous", "1", "1", "1", ""),
        ("vts_operator", "VTS (Vessel Traffic Service)", "digital", "continuous", "1", "1", "1", ""),
        ("towage_operator", "Towage operator (joint manoeuvre)", "service", "per call", "1", "1", "1", ""),
        ("mooring_operator", "Mooring operator (joint manoeuvre)", "service", "per call", "1", "1", "1", ""),
        ("ship_agent", "Ship agent (booking)", "service", "per call", "many", "many", "many", ""),
        ("pcs_operator", "Port Community System", "digital", "continuous", "1", "1", "1", ""),
    ],
    "sources": [
        ("pilot_launch_mgo", "Pilot launch MGO", "scope_1"),
        ("office_electricity", "Office / control room electricity", "scope_2"),
        ("staff_travel_training", "Staff training travel", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("pilot_launch_mgo",        480),
        ("office_electricity",      18),
        ("staff_travel_training",   12),
    ]),
}


# ─────────────────────────────────────────────────────
# 13 — Towage Service
# ─────────────────────────────────────────────────────
SPEC_TOWAGE = {
    "archetype_id": "service_towage",
    "name": "Towage Service",
    "category": "Mandatory Service",
    "definition": "A mandatory technical-nautical service: powerful tugboats assist vessels during "
                  "berthing, unberthing, and emergency manoeuvres. Number of tugs per operation is "
                  "set by Harbour Master based on vessel size, weather, and cargo. Typically granted "
                  "under exclusive licence (or UTE) to a single operator per port.",
    "tier_S": "≤ 3 000 ops/year · 3-4 tugs · 1-2 escort-capable",
    "tier_M": "3 000 – 8 000 ops/year · 5-7 tugs · ASD primary fleet",
    "tier_L": "≥ 8 000 ops/year · 8+ tugs · ASD + escort + FiFi-2",
    "identity": [
        ("operator_legal_name", "Operator legal name", "—", "string",
         "[Towage company S]", "[Towage company M]", "[Towage UTE / company L]", ""),
        ("operator_short_name", "Commercial name", "—", "string", "—", "—", "—", ""),
        ("port_unlocode", "Port (UN/LOCODE)", "—", "enum", "—", "—", "—", ""),
        ("port_name", "Port name", "—", "string", "—", "—", "—", ""),
        ("country_iso2", "Country (ISO 3166-1 alpha-2)", "—", "enum", "—", "—", "—", ""),
        ("parent_group", "Parent group", "—", "string", "—", "—", "—",
         "Boluda / DP World (P&O Reyser) / Remolcanosa / Ibaizabal / Svitzer"),
        ("legal_form", "Legal form", "—", "enum", "S.A.", "S.A. / UTE", "UTE", ""),
        ("licence_type", "Licence type", "—", "enum", "Exclusive", "Exclusive", "Exclusive", ""),
        ("licence_end_year", "Licence end year", "year", "integer", "—", "—", "—", ""),
        ("annual_towage_operations", "Annual towage operations", "ops/year", "integer", 1800, 5500, 12000, ""),
        ("workforce_total_fte", "Total workforce", "FTE", "integer", 35, 80, 180, ""),
        ("size_tier", "Size tier", "—", "enum", "S", "M", "L", ""),
        ("isps_certified", "ISPS code certification", "bool", "boolean", True, True, True, ""),
        ("iso_9001", "ISO 9001", "bool", "boolean", True, True, True, ""),
        ("iso_14001", "ISO 14001", "bool", "boolean", True, True, True, ""),
        ("iso_45001", "ISO 45001", "bool", "boolean", True, True, True, ""),
        ("service_24_7", "Service 24/7", "bool", "boolean", True, True, True, ""),
    ],
    "equipment": [
        ("asd_harbour_tugs_qty", "ASD harbour tugs", "tugs", "integer", 3, 4, 6, ""),
        ("asd_escort_tugs_qty", "ASD escort-capable tugs", "tugs", "integer", 0, 1, 2, ""),
        ("fifi_tugs_qty", "FiFi-1 / FiFi-2 firefighting tugs", "tugs", "integer", 0, 1, 2, ""),
        ("reserve_tugs_qty", "Reserve / training tugs", "tugs", "integer", 1, 1, 2, ""),
        ("avg_bollard_pull_t", "Average bollard pull (primary fleet)", "t", "integer", 55, 65, 78, ""),
        ("max_bollard_pull_t", "Maximum bollard pull in fleet", "t", "integer", 65, 80, 95, ""),
        ("avg_tugs_per_operation", "Average tugs per operation", "tugs", "number", 1.5, 2.0, 2.5, ""),
        ("avg_op_duration_min", "Average operation duration", "min", "integer", 50, 60, 75, ""),
        ("avg_fuel_per_tug_op_l", "Average fuel per tug-op", "L", "integer", 200, 250, 320, "Marine diesel"),
        ("hybrid_tugs_qty", "Hybrid tugs in fleet", "tugs", "integer", 0, 0, 1, "Diesel-electric"),
    ],
    "relations": [
        ("vessel_calls", "Vessels above tug threshold", "service", "per call",
         "1 800", "5 500", "12 000+", "Container, cruise, tanker, bulk"),
        ("pilots_corporation", "Pilots corporation (joint manoeuvre)", "service", "per call", "1", "1", "1", ""),
        ("mooring_operator", "Mooring operator (joint manoeuvre)", "service", "per call", "1", "1", "1", ""),
        ("port_authority", "Port authority (concession)", "regulator", "continuous", "1", "1", "1", ""),
        ("harbour_master", "Harbour Master (operational authority)", "regulator", "continuous", "1", "1", "1", ""),
        ("ship_agent", "Ship agent (booking)", "service", "per call", "many", "many", "many", ""),
        ("bunker_supplier", "Bunker fuel supplier", "inbound", "weekly", "1", "1-2", "2-3", ""),
        ("tug_shipyard_newbuild", "Tug shipyard (newbuild)", "inbound", "every 5-10 yr", "1-2", "2-3", "3-5",
         "Sanmar, Damen, Astilleros Armón, Zamakona"),
        ("tug_shipyard_drydock", "Tug shipyard (dry-dock / repair)", "inbound", "annual", "1", "1-2", "1-2", ""),
        ("class_society", "Class society", "regulator", "5-yr survey", "1", "1", "1", "DNV, BV, RINA"),
        ("pcs_operator", "Port Community System", "digital", "continuous", "1", "1", "1", ""),
    ],
    "sources": [
        ("tug_fleet_diesel", "Tug fleet diesel (MGO equivalent)", "scope_1"),
        ("office_workshop_electricity", "Office + workshop electricity", "scope_2"),
        ("workshop_heat_ancillary", "Workshop heat / ancillary", "scope_1+2"),
    ],
    "defaults_M": make_carbon_defaults([
        ("tug_fleet_diesel",            7350),
        ("office_workshop_electricity", 90),
        ("workshop_heat_ancillary",     60),
    ]),
}


# ─────────────────────────────────────────────────────
# 14 — Mooring Service
# ─────────────────────────────────────────────────────
SPEC_MOORING = {
    "archetype_id": "service_mooring",
    "name": "Mooring Service",
    "category": "Mandatory Service",
    "definition": "A mandatory technical-nautical service: trained crews catch, secure, and release "
                  "the lines (hawsers) that hold a vessel to the quay. Operates from small launches "
                  "(boteros) and on the quay. High-risk physical work requiring strict ISO 45001 "
                  "occupational H&S protocols. Typically exclusive concession per port, often a "
                  "worker cooperative or JV.",
    "tier_S": "≤ 3 000 ops/year · 30 mooring men · 1 launch",
    "tier_M": "3 000 – 7 000 ops/year · 60 mooring men · 1-2 launches",
    "tier_L": "≥ 7 000 ops/year · 100+ mooring men · 2+ launches",
    "identity": [
        ("operator_legal_name", "Operator legal name", "—", "string",
         "[Mooring company S]", "[Mooring company M]", "[Mooring company L]", ""),
        ("operator_short_name", "Commercial name", "—", "string", "—", "—", "—", ""),
        ("port_unlocode", "Port (UN/LOCODE)", "—", "enum", "—", "—", "—", ""),
        ("port_name", "Port name", "—", "string", "—", "—", "—", ""),
        ("country_iso2", "Country (ISO 3166-1 alpha-2)", "—", "enum", "—", "—", "—", ""),
        ("legal_form", "Legal form", "—", "enum", "Cooperative", "S.L. / Cooperative", "S.L. / JV",
         "Workers cooperatives common in Italy and Spain"),
        ("licence_type", "Licence type", "—", "enum", "Exclusive", "Exclusive", "Exclusive", ""),
        ("licence_end_year", "Licence end year", "year", "integer", "—", "—", "—", ""),
        ("annual_mooring_operations", "Annual mooring operations", "ops/year", "integer", 1800, 5500, 12000, ""),
        ("number_of_mooring_men", "Number of mooring men", "operators", "integer", 30, 60, 110, ""),
        ("workforce_total_fte", "Total workforce", "FTE", "integer", 40, 80, 140, ""),
        ("size_tier", "Size tier", "—", "enum", "S", "M", "L", ""),
        ("isps_certified", "ISPS code certification", "bool", "boolean", True, True, True, ""),
        ("iso_45001", "ISO 45001 (occupational H&S)", "bool", "boolean", True, True, True, "Critical"),
        ("service_24_7", "Service 24/7", "bool", "boolean", True, True, True, ""),
    ],
    "equipment": [
        ("mooring_launches_qty", "Mooring launches (boteros)", "launches", "integer", 1, 2, 3, ""),
        ("foremen_qty", "Foremen / shift supervisors", "people", "integer", 4, 8, 14, ""),
        ("avg_crew_per_op", "Average crew size per operation", "people", "integer", 4, 5, 7, ""),
        ("avg_op_duration_min", "Average operation duration", "min", "integer", 25, 30, 45, ""),
        ("avg_fuel_per_op_l", "Launch fuel per operation", "L", "integer", 6, 8, 12, "MGO"),
        ("light_vehicles_qty", "Light vehicles (in-port crew transport)", "vehicles", "integer", 2, 4, 8, ""),
        ("heaving_lines_total", "Heaving lines (operational + spare)", "lines", "integer", 50, 100, 200, ""),
        ("vhf_radios_qty", "VHF radios", "units", "integer", 15, 30, 50, ""),
    ],
    "relations": [
        ("vessel_calls", "Vessels (all categories)", "service", "per call",
         "1 800", "5 500", "12 000+", "All commercial vessels"),
        ("pilots_corporation", "Pilots corporation (orders mooring)", "service", "per call", "1", "1", "1", ""),
        ("towage_operator", "Towage operator (joint manoeuvre)", "service", "per call", "1", "1", "1", ""),
        ("terminal_operator", "Terminal / berth operator", "service", "continuous",
         "5-10", "10-25", "25+", "Mooring works on terminal's quay"),
        ("port_authority", "Port authority", "regulator", "continuous", "1", "1", "1", ""),
        ("harbour_master", "Harbour Master", "regulator", "continuous", "1", "1", "1", ""),
        ("trade_unions", "Trade unions", "service", "continuous", "1-2", "2-3", "3+", "CCOO, UGT, USOC"),
        ("ship_agent", "Ship agent (booking)", "service", "per call", "many", "many", "many", ""),
        ("pcs_operator", "Port Community System", "digital", "continuous", "1", "1", "1", ""),
    ],
    "sources": [
        ("mooring_launch_fuel", "Mooring launch fuel (MGO)", "scope_1"),
        ("light_vehicles_fuel", "Light vehicles (in-port)", "scope_1"),
        ("office_electricity", "Office + workshop electricity", "scope_2"),
    ],
    "defaults_M": make_carbon_defaults([
        ("mooring_launch_fuel",     110),
        ("light_vehicles_fuel",     30),
        ("office_electricity",      25),
    ]),
}


# ─────────────────────────────────────────────────────
# 15 — Port Reception Facilities (MARPOL)
# ─────────────────────────────────────────────────────
SPEC_MARPOL = {
    "archetype_id": "service_marpol_reception",
    "name": "Port Reception Facilities (MARPOL)",
    "category": "Mandatory Service",
    "definition": "Mandatory infrastructure under IMO MARPOL Convention and EU Directive 2019/883: "
                  "facilities for receiving ship-generated waste (oily residues, NLS, sewage, garbage, "
                  "EGCS sludge). Operators are licensed concessionaires of the Port Authority. Three "
                  "operational layers: collection (sea-side barges + land-side trucks), storage "
                  "(customs-bonded), treatment (waste-to-fuel recovery + recycling).",
    "tier_S": "≤ 30 000 t/year MARPOL · 1 collection barge · single-stream",
    "tier_M": "30 000 – 100 000 t/year · 2 collection barges · multi-line treatment",
    "tier_L": "≥ 100 000 t/year · 2+ barges · vertically integrated recovery + recycling",
    "identity": [
        ("operator_legal_name", "Operator legal name", "—", "string",
         "[PRF operator S]", "[PRF operator M]", "[PRF operator L]", ""),
        ("operator_short_name", "Commercial name", "—", "string", "—", "—", "—", ""),
        ("port_unlocode", "Port (UN/LOCODE)", "—", "enum", "—", "—", "—", ""),
        ("port_name", "Port name", "—", "string", "—", "—", "—", ""),
        ("country_iso2", "Country (ISO 3166-1 alpha-2)", "—", "enum", "—", "—", "—", ""),
        ("parent_group", "Parent group", "—", "string", "—", "—", "—", "Often part of waste-management groups"),
        ("first_concession_year", "Year of first concession", "year", "integer", "—", "—", "—", ""),
        ("concession_end_year", "Concession end year", "year", "integer", "—", "—", "—", ""),
        ("marpol_annexes_covered", "MARPOL annexes covered", "—", "string",
         "I, V", "I, II, IV, V", "I, II, IV, V, VI",
         "I=oily, II=NLS, IV=sewage, V=garbage, VI=air"),
        ("hazardous_waste_licensed", "Hazardous waste licence (national)", "bool", "boolean",
         False, True, True, ""),
        ("annual_marpol_received_t", "Annual MARPOL waste received", "t/year", "integer", 18000, 60000, 180000, ""),
        ("annual_ship_deliveries", "Annual ship-deliveries", "deliveries/year", "integer", 1800, 4000, 9000, ""),
        ("workforce_total_fte", "Total workforce", "FTE", "integer", 25, 60, 130, ""),
        ("size_tier", "Size tier", "—", "enum", "S", "M", "L", ""),
        ("isps_certified", "ISPS code certification", "bool", "boolean", True, True, True, ""),
        ("iso_14001", "ISO 14001", "bool", "boolean", True, True, True, ""),
        ("iso_9001", "ISO 9001", "bool", "boolean", True, True, True, ""),
        ("plant_area_m2", "Treatment plant area", "m²", "integer", 5000, 15000, 40000, ""),
        ("treatment_capacity_t_yr", "Annual treatment capacity", "t/year", "integer", 35000, 110000, 250000, ""),
        ("storage_capacity_oily_m3", "Storage capacity — oily liquids", "m³", "integer", 1000, 3500, 12000, ""),
    ],
    "equipment": [
        ("marpol_i_ii_barge_qty", "MARPOL I/II collection barges (oily)", "barges", "integer", 1, 1, 2, ""),
        ("marpol_v_barge_qty", "MARPOL V collection barges (garbage)", "barges", "integer", 0, 1, 2, ""),
        ("largest_barge_capacity_m3", "Largest barge capacity", "m³", "integer", 100, 230, 500, ""),
        ("tank_trucks_adr_qty", "Tank trucks (ADR)", "trucks", "integer", 2, 4, 10, ""),
        ("box_trucks_qty", "Box / garbage trucks", "trucks", "integer", 2, 6, 14, ""),
        ("forklifts_cranes_qty", "Forklifts / yard cranes", "machines", "integer", 1, 3, 8, ""),
        ("hydrocarbon_line_capacity_t_yr", "Hydrocarbon recovery line capacity", "t/year", "integer", 18000, 50000, 130000,
         "Recovers IFO 380"),
        ("water_line_capacity_t_yr", "Industrial water line capacity", "t/year", "integer", 8000, 25000, 70000, ""),
        ("solid_waste_line_capacity_t_yr", "Solid waste line capacity", "t/year", "integer", 5000, 15000, 40000, ""),
        ("hazardous_recovery_line_capacity_t_yr", "Hazardous recovery line", "t/year", "integer", 0, 5000, 15000, ""),
        ("wwtp_on_site", "On-site WWTP (industrial water treatment)", "bool", "boolean", False, True, True, ""),
        ("laboratory_on_site", "Laboratory (waste characterisation)", "bool", "boolean", True, True, True, ""),
        ("annual_recovered_ifo_t", "Annual recovered IFO 380", "t/year", "integer", 4000, 18000, 50000, ""),
        ("annual_recycled_materials_t", "Annual recycled materials", "t/year", "integer", 1500, 6000, 18000, ""),
    ],
    "relations": [
        ("cruise_lines_waste_source", "Cruise lines (high-volume waste)", "inbound", "per call",
         "5 000 t/yr", "30 000 t/yr", "80 000 t/yr", ""),
        ("container_lines_waste_source", "Container lines", "inbound", "per call",
         "3 000 t/yr", "20 000 t/yr", "55 000 t/yr", ""),
        ("ferry_ropax_waste_source", "Ferry / Ro-Pax", "inbound", "per call",
         "2 500 t/yr", "15 000 t/yr", "30 000 t/yr", ""),
        ("tankers_waste_source", "Tankers (slops critical)", "inbound", "per call",
         "1 500 t/yr", "8 000 t/yr", "25 000 t/yr", ""),
        ("bunker_market_offtaker", "Bunker market (recovered IFO)", "outbound", "continuous",
         "1-2", "2-5", "5+", "Major revenue stream"),
        ("recycler_paper_plastic", "Recyclers (paper/plastic/metal)", "outbound", "continuous",
         "2-5", "5-10", "10+", ""),
        ("incinerator", "Waste-to-energy / incinerator", "outbound", "continuous", "1", "1", "1-2", ""),
        ("port_authority", "Port authority", "regulator", "continuous", "1", "1", "1", ""),
        ("harbour_master", "Harbour Master (MARPOL inspection)", "regulator", "per delivery", "1", "1", "1", ""),
        ("national_environment_authority", "National environment authority", "regulator", "annual", "1", "1", "1", ""),
        ("emsa_safesseanet_waste", "EMSA SafeSeaNet waste module", "digital", "per call", "1", "1", "1", "EU 2019/883 PRR"),
        ("customs_authority", "Customs (bonded waste)", "regulator", "continuous", "1", "1", "1", ""),
        ("ship_agent", "Ship agent (booking)", "service", "per call", "many", "many", "many", ""),
        ("pcs_operator", "Port Community System", "digital", "continuous", "1", "1", "1", ""),
    ],
    "sources": [
        ("plant_electricity", "Plant electricity", "scope_2"),
        ("plant_heat_process", "Plant heat (process)", "scope_1+2"),
        ("collection_barges_mgo", "Collection barges (MGO)", "scope_1"),
        ("truck_fleet_fuel", "Tank truck + box truck fleet", "scope_1"),
        ("yard_equipment_diesel", "Forklifts / yard equipment", "scope_1"),
        ("incineration_residue_offsite", "Incineration of residue (attributed)", "scope_3"),
    ],
    "defaults_M": make_carbon_defaults([
        ("plant_electricity",                1200),
        ("plant_heat_process",               800),
        ("collection_barges_mgo",            350),
        ("truck_fleet_fuel",                 280),
        ("yard_equipment_diesel",            90),
        ("incineration_residue_offsite",     700),
    ]),
}


ALL_HUB_SERVICE_SPECS = [SPEC_BIOREFINERY, SPEC_FREIGHT_VILLAGE, SPEC_BUNKER_HUB,
                         SPEC_PILOTAGE, SPEC_TOWAGE, SPEC_MOORING, SPEC_MARPOL]
