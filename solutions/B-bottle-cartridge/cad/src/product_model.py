"""Helpful Water B product appearance model (kit 1.9), TRL 3, carried option B1 (squeeze cartridge; the concept
choice was made by Amish on 2026-11-11). Built from components("B1") in cad/src/model.py with every part used as it is,
plus the 1 L PET bottle and a hand from model.py's context parts for scale. APPEARANCE MODEL ONLY: no tolerances, no
fabrication detail. CONCEPT, NOT FOR FABRICATION. Photoreal renders need Blender (.kit/photoreal.py), which runs on
Amish's Mac from the scenes written by `python .kit/export_views.py <dir>`.

Groups: "shell" (outside parts), "internal" (module, carbon capsule, seals), "context" (bottle and hand).

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import model as M  # noqa: E402

TITLE = "Helpful Water B: bottle cartridge"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 15, "az": -55, "args": ["--lens=60"],
     "note": "B1 squeeze cartridge screwed onto a 1 L PET bottle with a 28 mm PCO 1881 neck, held in a hand; studio view "
             "from the front right, about 15 deg elevation"},
    {"name": "studio", "groups": ["shell"], "explode": False, "el": 20, "az": -55, "args": ["--lens=80"],
     "note": "The cartridge on its own: collar with grip ribs, housing, spout, push-pull valve and hinged dust cover"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 12, "az": -60, "args": ["--lens=60"],
     "note": "Exploded along the axis: collar, mesh, carbon capsule, hollow-fibre module, housing, spout, valve and cover"},
]


def product_parts():
    out = []
    for q in M.components("B1", context=True):
        q = dict(q)
        if q["kind"] == "context":
            q["group"] = "context"
        out.append(q)
    return out
