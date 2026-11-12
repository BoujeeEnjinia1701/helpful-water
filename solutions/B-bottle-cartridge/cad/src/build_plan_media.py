"""Helpful Water B prototype build plan pictures (HWB-BLD-001, STANDARDS section 18), option B1.

Run from the solution folder, one group per process on a small machine:
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py components("B1"), so the pictures and the model never disagree:
    docs/05-build-plan/overview.png       every component pulled apart, numbered in build order
    cad/drawings/HWB-DWG-101 to 107       making sketches for the seven made components
    docs/05-build-plan/joint-NN.png       close-ups of the joints that need explaining (cut open)
    docs/05-build-plan/step-NN.png        one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
import copy
import functools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Compound, Pos  # noqa: E402
import model as M  # noqa: E402

OUT = ROOT / "docs/05-build-plan"
DWG = ROOT / "cad/drawings"
DATE = "2026-11-11"
PROJECT = "Helpful Water B"


@functools.lru_cache(None)
def parts():
    return {q["name"]: q for q in M.components("B1", context=True)}


def find(prefix):
    return [q for n, q in parts().items() if n.startswith(prefix)]


def P_(prefix, name=None, color=None, explode=None):
    qs = find(prefix)
    shape = qs[0]["shape"] if len(qs) == 1 else Compound(children=[copy.copy(q["shape"]) for q in qs])
    return Part(name or qs[0]["name"], shape, color or qs[0]["color"], qs[0]["bom"], tuple(explode if explode is not None else qs[0]["explode"]))


COL = {"collar": "#D6D3C4", "housing": "#2B4A43", "capsule": "#1F2937", "carbon": "#111111", "module": "#E7E5DF",
       "seal": "#111827", "mesh": "#9CA3AF", "spout": "#CFCAB8", "valve": "#0F766E", "cover": "#B45309", "pad": "#F4F1E6"}


def module_part(explode=(0, 0, 0)):
    qs = [q for q in parts().values() if q["bom"] == 8]
    return Part("Hollow-fibre module (bought)", Compound(children=[copy.copy(q["shape"]) for q in qs]), COL["module"], 8, explode)


def capsule_filled(explode=(0, 0, 0)):
    qs = [q for q in parts().values() if q["bom"] in (3, 4, 9, 10)]
    return Part("Carbon capsule, filled", Compound(children=[copy.copy(q["shape"]) for q in qs]), COL["capsule"], 3, explode)


def header_orings(explode=(0, 0, 0)):
    return P_("Header O-ring", "Header O-rings (2)", COL["seal"], explode)


def build_order():
    """The components in build order (section 3 of the plan), pulled apart for the overview."""
    return [
        P_("Neck collar", "Neck collar (made)", COL["collar"], (0, 0, -90)),
        P_("Neck gasket", "Neck gasket", COL["seal"], (0, 0, -120)),
        P_("Duckbill", "Duckbill air valve", COL["seal"], (45, 0, -90)),
        P_("Mesh prefilter", "Mesh disc", COL["mesh"], (0, 0, -50)),
        P_("Collar O-ring", "Collar O-ring", COL["seal"], (0, 0, -65)),
        P_("Carbon capsule body", "Carbon capsule body (made)", COL["capsule"], (0, 0, -20)),
        P_("Retention pad, lower", "Retention pads (2)", COL["pad"], (0, 0, -8)),
        P_("Carbon bed", "Carbon fill", COL["carbon"], (0, 0, 4)),
        P_("Carbon capsule lid", "Carbon capsule lid (made)", COL["capsule"], (0, 0, 18)),
        module_part((0, 0, 50)),
        header_orings((0, 0, 50)),
        P_("Housing", "Housing (made)", COL["housing"], (70, 0, 120)),
        P_("Spout gasket", "Spout gasket", COL["seal"], (0, 0, 250)),
        P_("Spout with", "Spout (made)", COL["spout"], (0, 0, 262)),
        P_("Valve O-ring", "Valve O-ring", COL["seal"], (0, 0, 276)),
        P_("Push-pull", "Push-pull valve (made)", COL["valve"], (0, 0, 292)),
        P_("Dust cover", "Dust cover (made)", COL["cover"], (25, 0, 312)),
        P_("Hinge pin", "Hinge pin", COL["seal"], (40, 0, 312)),
    ]


def overview():
    """Components laid out in build order in two rows (small parts first row, large parts second)."""
    ps = build_order()
    rows = [ps[:9], ps[9:]]
    laid, z_row = [], {0: 230.0, 1: 0.0}
    for r, row in enumerate(rows):
        x = 0.0
        for p in row:
            bb = p.shape.bounding_box()
            w = bb.max.X - bb.min.X
            off = (x - bb.min.X, -bb.center().Y, z_row[r] - bb.min.Z)
            laid.append(Part(p.name, p.shape, p.color, p.bom, off))
            x += w + 18.0
    p = bv.overview(laid, OUT / "overview.png", "Helpful Water B1 squeeze cartridge: prototype components",
                    elev=14, azim=-80, size=(13, 8), key=True)
    print("wrote", p)


SHEETS = {
    101: ("Neck collar", "Neck collar", "Polypropylene (food-contact grade); FDM print for the prototype, injection moulded at scale", [
        "36 mm across the skirt, 40 mm over the spigot thread, 40.5 mm tall",
        "Inside the 17 mm skirt: 28 mm PCO 1881 female thread, 2.7 mm pitch",
        "Deck 7.5 mm thick with an 18 mm inlet bore; 3 mm side air bore",
        "6 mm counterbore 4.6 mm deep for the duckbill valve",
        "Above: 40 x 3 mm male thread for the housing, 10 mm long",
        "Seal land 36.6 mm with a 2.4 mm wide groove for a 33.4 x 2 O-ring",
        "Print skirt-down, 0.15 mm layers, 100 % infill; ream the bores",
        "Check: screws onto a 1881 and a 1810 neck by hand with the gasket"]),
    102: ("Carbon capsule body", "Carbon capsule body", "Polypropylene, black; FDM print", [
        "Cup 34 mm across, 37 mm tall; 30 mm bore for a 20 mm carbon bed",
        "29.8 mm plug spigot drops into the collar bore",
        "Floor with seven 3 mm holes on a 14 mm circle and the centre",
        "Print floor-down, 100 % infill; deburr the holes",
        "Check: a lower pad sits flat on the 24 mm step inside"]),
    103: ("Carbon capsule lid", "Carbon capsule lid", "Polypropylene, black; FDM print", [
        "Plug lid 29.9 mm into the capsule bore, 34 mm flange 1.2 mm thick",
        "Seven holes (4 mm centre, 3.2 mm on a 16 mm circle)",
        "Two finger notches in the flange rim to pull the capsule",
        "Check: pressed in, holds the upper pad and the carbon"]),
    104: ("Housing", "Housing", "Polypropylene; FDM print (largest part), injection moulded at scale", [
        "41 mm across (44 mm at the grip band), 165 mm long, 37 mm bore",
        "Bottom: 40 x 3 mm female thread, 10 mm deep, inside the grip band",
        "Top: 4 mm end wall with a 10.4 mm bore for the module nipple",
        "Above it: 20 x 2 mm male thread spigot for the spout",
        "Print upright, 0.15 mm layers, 4 perimeters; bore smooth for the O-rings",
        "Check the bore with the module: two O-rings slide in with light force",
        "Check: 2 m of known potable test water head holds with no seep"]),
    105: ("Spout with", "Spout", "Polypropylene; FDM print", [
        "24 mm across, 27 mm tall; 20 x 2 mm female thread inside",
        "Nozzle 12 mm across with a 5 mm bore and four 2 mm side ports",
        "1.4 mm groove on the nozzle for a 10 x 1.2 O-ring",
        "Hinge lug with a 1.6 mm pin hole on one side",
        "Check: screws down onto the spout gasket by hand, nozzle bore clear"]),
    106: ("Push-pull", "Push-pull drink valve", "Polypropylene, coloured; FDM print or a bought sports-cap valve of the same bore", [
        "Sleeve 15.4 mm across, 12.2 mm bore, 13.6 mm tall",
        "4.9 mm sealing plug under the top; four 2 mm outlet holes",
        "Closed: the plug sits in the nozzle bore; open: pull up 4 mm",
        "Check: slides with the O-ring fitted; no leak closed at a hard squeeze"]),
    107: ("Dust cover", "Dust cover", "Polypropylene; FDM print", [
        "Cap 19 mm across, 20 mm tall over the valve",
        "Two hinge cheeks with 1.6 mm holes on the spout lug",
        "Hinge pin 1.5 x 9 mm stainless, pressed through",
        "Check: flips open and shut, covers the valve fully"]),
}


def sheets(which=None):
    for no, (prefix, title, material, notes) in SHEETS.items():
        if which and str(no) not in which:
            continue
        q = find(prefix)[0]
        part = Part(title, q["shape"], "#0F766E", q["bom"])
        neigh = [Part(n, x["shape"], "#D1D5DB") for n, x in parts().items() if x["kind"] in ("made", "bought") and not n.startswith(prefix)
                 and abs(x["shape"].bounding_box().center().Z - q["shape"].bounding_box().center().Z) < 120]
        p = bv.component_sheet(part, neigh, PROJECT, f"HWB-DWG-{no}", f"B1 {title}: making sketch", material, notes, DATE,
                               out_dir=str(DWG))
        print("wrote", p)


def joints(which=None):
    J = {
        1: ("Collar on the bottle neck: thread, neck gasket and duckbill", ["Neck collar", "Neck gasket", "Duckbill", "Mesh prefilter"], True),
        2: ("Housing on the collar: 40 x 3 thread, collar O-ring and the capsule plug", ["Neck collar", "Collar O-ring", "Housing", "Carbon capsule body", "Mesh prefilter"], True),
        3: ("Module header in the housing: two O-rings, the only dirty-to-clean seal", ["Module header", "Header O-ring", "Potting", "Housing", "Fibre bundle"], True),
        4: ("Spout, push-pull valve and dust cover on its hinge pin", ["Housing", "Spout gasket", "Spout with", "Valve O-ring", "Push-pull", "Dust cover", "Hinge pin"], True),
    }
    win = {1: (-20, 25), 2: (5, 40), 3: (125, 185), 4: (150, 215)}
    from build123d import Box
    for k, (title, names, cut) in J.items():
        if which and str(k) not in which:
            continue
        z0, z1 = win[k]
        box = Pos(0, 0, (z0 + z1) / 2) * Box(120, 120, z1 - z0)
        ps = []
        for n in names:
            for q in find(n):
                try:
                    s = q["shape"] & box
                    if s.volume > 1e-3:
                        ps.append(Part(q["name"], s, q["color"] if q["material_name"] != "hdpe_recycled" else "#4F7A70"))
                except Exception:
                    pass
        p = bv.joint(ps, OUT / f"joint-{k:02d}.png", title, subtitle="Cut through the axis; front half removed", cut="+Y", elev=10, azim=-70)
        print("wrote", p)


def steps(which=None):
    S = [
        ("Step 1: slide the hollow-fibre module into the housing from below, header first",
         [], [module_part((0, 0, -230)), header_orings((0, 0, -230))], [P_("Housing", "Housing", COL["housing"], (0, 0, 0))]),
        ("Step 2: fit the duckbill, the neck gasket, the mesh disc and the collar O-ring to the collar",
         [P_("Neck collar", "Neck collar")], [P_("Duckbill", "Duckbill air valve", COL["seal"], (30, 0, 0)), P_("Neck gasket", "Neck gasket", COL["seal"], (0, 0, -40)),
                                          P_("Mesh prefilter", "Mesh disc", COL["mesh"], (0, 0, 40)), P_("Collar O-ring", "Collar O-ring", COL["seal"], (0, 0, 60))], []),
        ("Step 3: fill the capsule: lower pad, 6.8 g of rinsed carbon, upper pad, then press the lid in",
         [P_("Carbon capsule body", "Capsule body")], [P_("Retention pad, lower", "Lower pad", COL["pad"], (0, 0, 60)), P_("Carbon bed", "Carbon fill", COL["carbon"], (0, 0, 80)),
                                                   P_("Retention pad, upper", "Upper pad", COL["pad"], (0, 0, 100)), P_("Carbon capsule lid", "Lid", COL["capsule"], (0, 0, 120))], []),
        ("Step 4: drop the filled capsule into the collar, plug first",
         [P_("Neck collar", "Neck collar"), P_("Collar O-ring", "Collar O-ring"), P_("Mesh prefilter", "Mesh disc")], [capsule_filled((0, 0, 70))], []),
        ("Step 5: screw the housing (with its module) down onto the collar until the grip band meets it",
         [P_("Neck collar", "Neck collar"), capsule_filled()], [P_("Housing", "Housing", COL["housing"], (0, 0, 120)), module_part((0, 0, 120))], []),
        ("Step 6: spout gasket on the housing spigot, then screw the spout down hand tight",
         [P_("Housing", "Housing")], [P_("Spout gasket", "Spout gasket", COL["seal"], (0, 0, 30)), P_("Spout with", "Spout", COL["spout"], (0, 0, 45))], []),
        ("Step 7: O-ring into the nozzle groove, then push the drink valve on",
         [P_("Spout with", "Spout"), P_("Housing", "Housing")], [P_("Valve O-ring", "Valve O-ring", COL["seal"], (0, 0, 25)), P_("Push-pull", "Push-pull valve", COL["valve"], (0, 0, 40))], []),
        ("Step 8: hang the dust cover on the spout lug and press the hinge pin through",
         [P_("Spout with", "Spout"), P_("Push-pull", "Push-pull valve"), P_("Housing", "Housing")],
         [P_("Dust cover", "Dust cover", COL["cover"], (0, 0, 35)), P_("Hinge pin", "Hinge pin", COL["seal"], (0, -25, 0))], []),
        ("Step 9: screw the cartridge onto a filled 1 L PET bottle (known potable test water only)",
         [], [Part("B1 cartridge", Compound(children=[copy.copy(q["shape"]) for q in parts().values() if q["kind"] != "context"]), COL["housing"], None, (0, 0, 60))],
         [P_("PET bottle", "1 L PET bottle")]),
    ]
    for k, (title, done, new, ctx) in enumerate(S, 1):
        if which and str(k) not in which:
            continue
        p = bv.step(done, new, OUT / f"step-{k:02d}.png", title, context=ctx, elev=12, azim=-60, size=(7, 8))
        print("wrote", p)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    rest = sys.argv[2:]
    if what in ("overview", "all"):
        overview()
    if what in ("sheets", "all"):
        sheets(rest)
    if what in ("joints", "all"):
        joints(rest)
    if what in ("steps", "all"):
        steps(rest)
