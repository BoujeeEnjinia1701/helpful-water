"""Helpful Water D product appearance model (kit 1.9), TRL 3, carried option D1 (tablet dose cap; the concept
choice was made by Amish on 2026-11-11). Built from components("D1") in cad/src/model.py with every part used as it is,
plus the 1 L PET bottle and a hand from model.py's context parts for scale. APPEARANCE MODEL ONLY: no tolerances, no
fabrication detail. CONCEPT, NOT FOR FABRICATION. Photoreal renders need Blender (.kit/photoreal.py), which runs on
Amish's Mac from the scenes written by `python .kit/export_views.py <dir>`.

Groups: "shell" (outside parts), "internal" (well insert, tablet, seals, timer inside), "context" (bottle and hand).

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import model as M  # noqa: E402

TITLE = "Helpful Water D: chlorine co-treatment add-on"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 15, "az": -50, "args": ["--lens=60"],
     "note": "D1 tablet dose cap on a 1 L PET bottle with a 28 mm PCO 1881 neck, held in a hand; studio view from the "
             "front right, about 15 deg elevation"},
    {"name": "studio", "groups": ["shell", "internal"], "explode": False, "el": 20, "az": -40, "args": ["--lens=80"],
     "note": "The dose cap on its own: grip ribs, clear well plug on its tether, and the flip-over ball timer behind its window"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 14, "az": -40, "args": ["--lens=60"],
     "note": "Exploded along the axis: liner, cap body, keyed well insert, tablet, plug, tether and the timer parts"},
]


def product_parts():
    out = []
    for q in M.components("D1", context=True):
        q = dict(q)
        if q["kind"] == "context":
            q["group"] = "context"
        out.append(q)
    return out
