"""Helpful Water C product appearance model (kit 1.9), TRL 3, carried option C1 (two-bucket hollow-fibre filter on a
timber stand; the concept choice was made by Amish on 2026-11-11). Built from components("C1") in cad/src/model.py with
every part used as it is, plus a 1.75 m mannequin standing beside the stand for scale and the cup under the tap.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION. Photoreal renders need
Blender (.kit/photoreal.py), which runs on Amish's Mac from the scenes written by `python .kit/export_views.py <dir>`.

Groups: "shell" (buckets, lids, stand, tap, valve), "internal" (module, hoses, fittings), "context" (person, cup).

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import model as M  # noqa: E402

TITLE = "Helpful Water C: household gravity filter"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "stand", "context"], "explode": False, "el": 14, "az": -50, "args": ["--lens=50"],
     "note": "C1 household gravity filter: blue raw bucket on the top shelf, hollow-fibre module on the front leg, white clean "
             "bucket with a tap below; a 1.75 m person stands beside it; studio view from the front right, about 14 deg elevation"},
    {"name": "studio", "groups": ["shell", "internal", "stand"], "explode": False, "el": 18, "az": -40, "args": ["--lens=70"],
     "note": "The filter on its own: timber stand, raw bucket with cloth fill ring and dosing port, module, clean bucket and tap"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 14, "az": -58, "args": ["--lens=60"],
     "note": "The water path pulled apart: raw bucket and lid parts, outlet fittings, hoses, module, tee and clean bucket"},
]


def product_parts():
    import context_parts
    from build123d import Pos
    out = []
    for q in M.components("C1", context=True):
        q = dict(q)
        if q["kind"] == "context":
            q["group"] = "context"
        out.append(q)
    man = Pos(-650, -120, 0) * context_parts.mannequin(1750.0, "stand")
    out.append(dict(name="Person, 1.75 m (scale)", shape=man, color="#9C9C9E", material="clay", material_name="skin",
                    kind="context", bom=None, group="context", explode=(0, 0, 0), note=""))
    return out
