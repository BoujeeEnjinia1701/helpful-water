"""Helpful Water A filter straw: product appearance model (kit 1.9), TRL 3, option A1 (recommended; awaiting Amish).

Built from components("A1") in cad/src/model.py with every part used as it is, so every main dimension comes from
the model. Only scale context is added: the adult hand from .kit/context_parts.py that model.py already places, and a
half-cut copy of the straw for the cutaway render. APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.
Groups: "shell" (visible outside), "internal" (module, carbon, O-rings), "context" (hand), "cut" (half section).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Pos  # noqa: E402
import model as M  # noqa: E402

TITLE = "Helpful Water A: hollow-fibre filter straw with backflush"
_INTERNAL = ("Module", "potting", "bundle", "O-ring", "Carbon", "carbon", "mesh", "Mesh")

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 18, "az": -58, "args": ["--lens=60"],
     "note": "Held in an adult hand, seen from the front right and slightly above (about 18 deg elevation); 205 mm long, "
             "26 mm across; mouthpiece cap and lanyard fitted, backflush plug in its socket"},
    {"name": "studio", "groups": ["shell", "internal"], "explode": False, "el": 24, "az": -40, "args": [],
     "note": "Studio view from the front right and above (about 24 deg elevation): intake cap and cover at the bottom, dip line, "
             "tethered backflush plug on the clean header, bayonet mouthpiece and cap"},
    {"name": "cutaway", "groups": ["cut"], "explode": False, "el": 10, "az": -90, "args": [],
     "note": "Half section seen from the front (about 10 deg elevation): mesh in the intake cap, hollow-fibre bundle between its "
             "potting blocks, the two collar O-rings, the clean header with the backflush socket, the carbon bed and the mouthpiece"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 24, "az": -55, "args": [],
     "note": "Exploded view from the front right and above (about 24 deg elevation): module and carbon cartridge to the right, "
             "plug and band to the left, caps and lanyard above and below"},
]


def product_parts():
    out = []
    cutter = Pos(0, 60, 100) * Box(200, 120, 500)
    for q in M.components("A1"):
        d = dict(q)
        if q["kind"] == "context":
            d["group"] = "context"
            out.append(d)
            continue
        d["group"] = "internal" if any(k in q["name"] for k in _INTERNAL) else "shell"
        out.append(d)
        if q["name"] in ("Lanyard cord", "Split ring, stainless 12 mm"):
            continue
        try:
            h = q["shape"] & cutter
            if h.volume > 1e-3:
                c = dict(q)
                c["shape"], c["group"], c["name"] = h, "cut", q["name"] + " (section)"
                out.append(c)
        except Exception:
            pass
    return out


if __name__ == "__main__":
    from collections import Counter
    print(Counter(p["group"] for p in product_parts()))
