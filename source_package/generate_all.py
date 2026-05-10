"""Generate all 15 archetype xlsx + json files into ./archetypes/."""
import os
from pvw_builder import build_archetype
from specs_terminals import ALL_TERMINAL_SPECS
from specs_hubs_services import ALL_HUB_SERVICE_SPECS

OUT = "./archetypes"
os.makedirs(OUT, exist_ok=True)

# Note: container is not in ALL_TERMINAL_SPECS — it was the prototype
# To regenerate it, add its spec here. For now this generates the other 14.
all_specs = ALL_TERMINAL_SPECS + ALL_HUB_SERVICE_SPECS

print(f"Generating {len(all_specs)} archetypes into {OUT}/...")
print()

for spec in all_specs:
    out_xlsx, out_json, n_fields = build_archetype(spec, OUT)
    print(f"  ✓ {spec['archetype_id']:35s} {n_fields:3d} fields")

print()
print(f"Done: {len(all_specs)} archetypes generated")
