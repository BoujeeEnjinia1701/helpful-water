"""Helpful Water D prototype build plan pictures (HWD-BLD-001, STANDARDS section 18), option D1.

Run from the solution folder, one group per process on a small machine:
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py components("D1"), so the pictures and the model never disagree:
    docs/05-build-plan/overview.png       every component pulled apart, numbered in build order
    cad/drawings/HWD-DWG-101 to 107       making sketches for the made components
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
from build123d import Compound, Pos, Box  # noqa: E402
import model as M  # noqa: E402

OUT = ROOT / "docs/05-build-plan"
DWG = ROOT / "cad/drawings"
DATE = "2026-11-11"
PROJECT = "Helpful Water D"
COL = {"cap": "#D6D3C4", "seal": "#111827", "insert": "#2563EB", "insert20": "#EA580C", "plug": "#9FB7C4",
       "tablet": "#F4F4EE", "timer": "#7DA3B5", "ball": "#9CA3AF", "fluid": "#C7DDE6", "label": "#F4F1E6", "tether": "#1F2937"}


@functools.lru_cache(None)
def parts():
    return {q["name"]: q for q in M.components("D1", context=True)}


def find(prefix):
    return [q for n, q in parts().items() if n.startswith(prefix)]


def P_(prefix, name=None, color=None, explode=None):
    qs = find(prefix)
    shape = qs[0]["shape"] if len(qs) == 1 else Compound(children=[copy.copy(q["shape"]) for q in qs])
    return Part(name or qs[0]["name"], shape, color or qs[0]["color"], qs[0]["bom"], tuple(explode if explode is not None else qs[0]["explode"]))


def timer_capsule(explode=(0, 0, 0), name="Timer capsule (filled and sealed)"):
    qs = [q for n, q in parts().items() if n.startswith(("Timer tube", "Timer end", "Timer ball", "Timer fluid", "Timer hub"))]
    return Part(name, Compound(children=[copy.copy(q["shape"]) for q in qs]), COL["timer"], 9, explode)


def insert20(explode=(0, 0, 0)):
    return Part("Tablet well insert 20 L (orange)", Pos(60, 0, 0) * M.well_insert(M.P["WELL_20L"], 2, "20L"), COL["insert20"], 4, explode)


def build_order():
    return [
        P_("Dose cap body", "Dose cap body (made)", COL["cap"], (0, 0, -40)),
        P_("Tablet well insert", "Well insert 1 L (made)", COL["insert"], (0, 0, 20)),
        P_("Well insert O-ring", "Insert O-ring", COL["seal"], (0, 0, 30)),
        P_("Well plug", "Well plug (made)", COL["plug"], (0, 0, 60)),
        P_("Plug O-ring", "Plug O-ring", COL["seal"], (0, 0, 50)),
        P_("Tether", "Tether (made)", COL["tether"], (0, 0, 40)),
        P_("Timer tube", "Timer tube (cut)", COL["timer"], (45, 0, 0)),
        P_("Timer end cap", "Timer end caps (made)", COL["cap"], (45, 0, 0)),
        P_("Timer end O-ring", "Timer O-rings", COL["seal"], (45, 0, 0)),
        P_("Timer ball", "Steel ball", COL["ball"], (45, 0, 0)),
        P_("Timer hub", "Timer hub (made)", COL["cap"], (45, -12, 0)),
        P_("Timer window", "Timer window (made)", COL["plug"], (65, 0, 0)),
        P_("Window screw", "Window screws (2)", COL["ball"], (75, 0, 0)),
        P_("Timer scale label", "Timer scale label", COL["label"], (80, 0, 0)),
        P_("Pictogram label", "Pictogram label", COL["label"], (-30, 0, 0)),
        P_("Neck liner", "Neck liner", COL["seal"], (0, 0, -70)),
        P_("Tablet,", "Tablet (bought)", COL["tablet"], (0, 0, 80)),
    ]


def overview():
    ps = build_order()
    rows = [ps[:6], ps[6:]]
    laid, z_row = [], {0: 70.0, 1: 0.0}
    for r, row in enumerate(rows):
        x = 0.0
        for p in row:
            bb = p.shape.bounding_box()
            w = bb.max.X - bb.min.X
            off = (x - bb.min.X, -bb.center().Y, z_row[r] - bb.min.Z)
            laid.append(Part(p.name, p.shape, p.color, p.bom, off))
            x += w + 14.0
    p = bv.overview(laid, OUT / "overview.png", "Helpful Water D1 tablet dose cap: prototype components",
                    elev=16, azim=-75, size=(13, 8), key=True)
    print("wrote", p)


SHEETS = {
    101: ("Dose cap body", "Dose cap body", "Polypropylene (food-contact grade); FDM print for the prototype, injection moulded at scale", [
        "36 mm across the skirt, 40 mm crown, 46 mm tall; timer boss to 52 mm",
        "Inside the 17 mm skirt: 28 mm PCO 1881 female thread, 2.7 mm pitch",
        "Deck 4 mm thick with a 17 mm water bore; well bore 20.4 mm above it",
        "Top 7.5 mm: 22.4 mm female thread, 2 mm pitch, for the plug",
        "Side slot 7.5 x 28 x 22.5 mm with a 2.2 mm bearing hole for the timer",
        "Two 1.6 mm pilot holes for the window screws, 31.5 mm apart",
        "Print skirt-down, 0.15 mm layers, 100 % infill; ream the well bore to 20.4 +/-0.05",
        "Check: screws onto a 1881 neck by hand and seals on the liner"]),
    102: ("Tablet well insert", "Tablet well insert 1 L", "Polypropylene, blue; FDM print. The 20 L insert is the same in orange with a 14.5 mm bore, floor top 4.5 mm above its base", [
        "20.0 mm across, 16 mm tall; 9.5 mm tablet bore",
        "Floor top 7.5 mm above the insert base: 8 mm free under the plug stop",
        "Four 1.5 mm slots and a 1.6 mm hole through the floor",
        "Hollow under the floor from below for even walls",
        "O-ring groove root 17.9 +/-0.03 mm, 1.9 mm wide, 4.5 mm below the top",
        "One key notch on the top face (two on the 20 L insert)",
        "Check: a 20 L tablet will not enter the 1 L bore"]),
    103: ("Well plug", "Well plug", "Clear PETG print for the prototype; clarified PP at scale (not PC, which crazes in chlorine concentrate)", [
        "Head 27 mm across, 5 mm thick, 12 finger notches",
        "Core 20 mm with a 2 mm pitch male thread, 7.5 mm long",
        "9 mm stop spigot 1.5 mm long under the core",
        "Face O-ring groove 22.6 to 26.2 mm under the head, 1.3 mm deep",
        "Lug on the head rim with a 2 mm hole for the tether",
        "Print head-down; polish the head top to see the tablet",
        "Check: 3.5 turns home; the O-ring seals with the bottle upside down"]),
    104: ("Tether", "Tether band and strap", "TPU 95A print", [
        "Band 41.4 x 40 x 2 mm, sits on the crown 2 mm below its top",
        "Strap 1.2 x 3 mm, up and across to the plug lug",
        "Check: the plug can be lifted off and turned without the strap tearing"]),
    105: ("Timer hub", "Timer hub with trunnions", "Polypropylene; FDM print", [
        "Block 7.2 x 8 x 6 mm with a 6.0 mm bore for the timer tube",
        "Two trunnions 2 mm across, 1.1 mm long, on the axis",
        "Slides to the middle of the tube; a drop of adhesive holds it",
        "Check: turns freely in the slot, stays where it is put"]),
    106: ("Timer end cap top", "Timer end cap", "Polypropylene; FDM print or turned (two needed)", [
        "Cap 6 mm across, 1.5 mm thick, with a 3.95 x 1.5 mm spigot",
        "Groove on the spigot for a 3.0 x 0.5 mm O-ring",
        "Check: pushes into the tube with the O-ring and stays"]),
    107: ("Timer window", "Timer window", "Clear polycarbonate sheet 1.5 mm, laser cut or printed in clear PETG", [
        "Plate 9 x 35 x 24.5 mm (lies across the slot opening)",
        "2.2 mm bearing hole for the outer trunnion at the slot centre",
        "Two 2.2 mm screw holes 15.75 mm either side",
        "Scale label goes on the outside with its clear strip over the tube",
        "Check: the capsule turns end over end behind it"]),
}


def sheets(which=None):
    for no, (prefix, title, material, notes) in SHEETS.items():
        if which and str(no) not in which:
            continue
        q = find(prefix)[0]
        part = Part(title, q["shape"], "#0F766E", q["bom"])
        neigh = [Part(n, x["shape"], "#D1D5DB") for n, x in parts().items() if x["kind"] in ("made", "bought") and not n.startswith(prefix)
                 and abs(x["shape"].bounding_box().center().Z - q["shape"].bounding_box().center().Z) < 40]
        p = bv.component_sheet(part, neigh, PROJECT, f"HWD-DWG-{no}", f"D1 {title}: making sketch", material, notes, DATE,
                               out_dir=str(DWG))
        print("wrote", p)


SHORT = {"Dose cap body": "Cap body", "Timer end cap top": "End cap", "Timer end cap bottom": "End cap", "Timer tube": "Clear tube",
         "Timer ball": "Steel ball", "Timer hub": "Hub and trunnions", "Timer window": "Clear window", "Window screw 1": "Screw",
         "Window screw 2": "Screw", "Neck liner (flat": "Neck liner", "PET bottle 1 L (context)": "Bottle neck"}


def joints(which=None):
    J = {
        1: ("Cap on the bottle neck: PCO 1881 thread and silicone liner", ["Dose cap body", "Neck liner", "PET bottle", "Tablet well insert"], (-15, 12)),
        2: ("Tablet well: keyed insert, its O-ring, the tablet and the plug stop", ["Dose cap body", "Tablet well insert", "Well insert O-ring", "Tablet,", "Well plug", "Plug O-ring"], (4, 37)),
        3: ("Ball timer: capsule on its trunnions in the slot, window and screws", ["Dose cap body", "Timer tube", "Timer end cap", "Timer ball",
                                                                              "Timer hub", "Timer window", "Window screw"], (4, 32)),
    }
    for k, (title, names, (z0, z1)) in J.items():
        if which and str(k) not in which:
            continue
        box = Pos(0, 0, (z0 + z1) / 2) * Box(140, 140, z1 - z0)
        ps = []
        for n in names:
            for q in find(n):
                try:
                    s = q["shape"] & box
                    if s.volume > 1e-3:
                        ps.append(Part(SHORT.get(q["name"].split(",")[0].split(" with")[0], q["name"]), s, q["color"] if "PET" not in q["name"] else "#DCE7EA"))
                except Exception:
                    pass
        p = bv.joint(ps, OUT / f"joint-{k:02d}.png", title, subtitle="Cut through the axis; front half removed", cut="+Y", elev=10, azim=-70)
        print("wrote", p)


def steps(which=None):
    cap = lambda: P_("Dose cap body", "Dose cap body")
    S = [
        ("Step 1: build the timer capsule: bottom cap in, fluid and ball in, top cap in, hub to the middle",
         [], [P_("Timer tube", "Timer tube", COL["timer"], (0, 0, 0)), P_("Timer end cap bottom", "Bottom cap", COL["cap"], (0, 0, -12)),
              P_("Timer ball", "Ball", COL["ball"], (0, 0, 22)), P_("Timer end cap top", "Top cap", COL["cap"], (0, 0, 30)),
              P_("Timer hub", "Hub", COL["cap"], (0, -14, 0))], []),
        ("Step 2: drop the capsule into the side slot, inner trunnion into its bearing hole",
         [cap()], [timer_capsule((22, 0, 0))], []),
        ("Step 3: fit the window over the slot (outer trunnion in its hole) and drive the two screws",
         [cap(), timer_capsule()], [P_("Timer window", "Timer window", COL["plug"], (20, 0, 0)), P_("Window screw", "Screws", COL["ball"], (32, 0, 0))], []),
        ("Step 4: stick the scale label on the window and the pictogram label on the crown",
         [cap(), timer_capsule(), P_("Timer window", "Timer window")], [P_("Timer scale label", "Scale label", COL["label"], (15, 0, 0)),
                                                                     P_("Pictogram label", "Pictogram label", COL["label"], (-20, 0, 0))], []),
        ("Step 5: press the silicone liner into the skirt, up against the deck",
         [cap()], [P_("Neck liner", "Neck liner", COL["seal"], (0, 0, -40))], []),
        ("Step 6: roll the O-ring onto the blue insert and press the insert into the well, slots down",
         [cap()], [P_("Well insert O-ring", "Insert O-ring", COL["seal"], (0, 0, 45)), P_("Tablet well insert", "1 L insert", COL["insert"], (0, 0, 35))], []),
        ("Step 7: tether band on the crown, O-ring on the plug, then screw the plug home",
         [cap(), P_("Tablet well insert", "1 L insert")], [P_("Tether", "Tether", COL["tether"], (0, 0, 20)), P_("Plug O-ring", "Plug O-ring", COL["seal"], (0, 0, 35)),
                                                        P_("Well plug", "Well plug", COL["plug"], (0, 0, 45))], []),
        ("Step 8: screw the cap onto a 1 L bottle of known potable test water (no tablet yet)",
         [], [Part("D1 dose cap", Compound(children=[copy.copy(q["shape"]) for n, q in parts().items() if q["kind"] != "context" and not n.startswith("Tablet,")]),
                   COL["cap"], None, (0, 0, 40))], [P_("PET bottle", "1 L PET bottle")]),
    ]
    for k, (title, done, new, ctx) in enumerate(S, 1):
        if which and str(k) not in which:
            continue
        p = bv.step(done, new, OUT / f"step-{k:02d}.png", title, context=ctx, elev=14, azim=-50, size=(7, 7))
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
