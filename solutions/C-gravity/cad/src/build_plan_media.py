"""Helpful Water C prototype build plan pictures (HWC-BLD-001, STANDARDS section 18), option C1.

Run from the solution folder, one group per process on a small machine:
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py components("C1"), so the pictures and the model never disagree:
    docs/05-build-plan/overview.png       every component pulled apart, numbered in build order
    cad/drawings/HWC-DWG-101 to 113       making sketches for the made components
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
PROJECT = "Helpful Water C"


@functools.lru_cache(None)
def parts():
    return {q["name"]: q for q in M.components("C1", context=True)}


def find(prefix):
    return [q for n, q in parts().items() if n.startswith(prefix)]


def P_(prefix, name=None, color=None, explode=(0, 0, 0)):
    qs = find(prefix)
    if not qs:
        raise KeyError(prefix)
    shape = qs[0]["shape"] if len(qs) == 1 else Compound(children=[copy.copy(q["shape"]) for q in qs])
    return Part(name or qs[0]["name"], shape, color or qs[0]["color"], qs[0]["bom"], tuple(explode))


def group(prefixes, name, color, explode=(0, 0, 0)):
    qs = [q for p in prefixes for q in find(p)]
    return Part(name, Compound(children=[copy.copy(q["shape"]) for q in qs]), color, qs[0]["bom"], tuple(explode))


COL = {"timber": "#A9784A", "ply": "#C9A46E", "raw": M.RAW_BLUE, "clean": "#D6D3C4", "module": "#2B4A43", "seal": "#111827",
       "fit": "#9CA3AF", "hose": "#7FB2C8", "steel": "#6B7280", "made": "#0F766E", "valve": "#1F5F8B"}


def build_order():
    return [
        group(["Foot"], "Feet (2, made)", COL["timber"], (0, 0, -60)),
        group(["Leg"], "Legs (4, made)", COL["timber"], (0, 0, 0)),
        group(["Lower rail"], "Lower rails (2, made)", COL["timber"], (0, 0, -20)),
        group(["M8"], "Rail bolts (4 sets)", COL["steel"], (0, 0, -20)),
        P_("Upper shelf", "Upper shelf (made)", COL["ply"], (0, 0, 80)),
        P_("Lower shelf", "Lower shelf (made)", COL["ply"], (0, 0, 20)),
        group(["Diagonal"], "Diagonal braces (2, made)", COL["timber"], (0, 0, 0)),
        group(["Coach screw", "Wood screw 5 x 30, shelf", "Wood screw 5 x 30, brace"], "Coach and wood screws", COL["steel"], (0, 0, 0)),
        P_("Raw bucket", "Raw bucket (bought, drilled)", COL["raw"], (0, 0, 260)),
        group(["Raw outlet", "Inner gasket", "Outer gasket"], "Outlet bulkhead fitting", COL["fit"], (90, 0, 260)),
        P_("Strainer", "Strainer", COL["fit"], (-40, 0, 260)),
        group(["Ball valve"], "Ball valve", COL["valve"], (140, 0, 260)),
        P_("Valve tag", "Valve tag (made)", "#E3B21C", (160, 0, 300)),
        P_("Hose barb", "Hose barb", COL["fit"], (180, 0, 260)),
        P_("Raw lid", "Raw lid (bought, cut)", COL["raw"], (0, 0, 420)),
        P_("Prefilter cloth", "Prefilter cloth", "#B8AD8F", (0, 0, 470)),
        P_("Cloth clamp", "Cloth clamp ring (made)", COL["made"], (0, 0, 510)),
        P_("Fill cover", "Fill cover (made)", COL["raw"], (0, 0, 560)),
        P_("Dosing port collar", "Dosing port collar (made)", COL["made"], (0, 0, 500)),
        P_("Dosing port cap", "Dosing port cap (made)", COL["raw"], (0, 0, 540)),
        group(["Module", "Fibre", "Potting"], "Hollow-fibre module (bought)", COL["module"], (120, -120, 0)),
        group(["P-clip", "Wood screw 5 x 30, P-clip"], "P-clips and screws", COL["fit"], (60, -80, 0)),
        P_("Raw hose", "Raw hose", COL["hose"], (200, -60, 120)),
        group(["Clean-side tee", "Backflush port cap"], "Tee with backflush port", COL["fit"], (120, -160, -60)),
        P_("Pinch clamp", "Pinch clamp", COL["made"], (60, -200, -60)),
        P_("Clean hose", "Clean hose", "#B8D8E4", (40, -200, 0)),
        P_("Clean bucket", "Clean bucket (bought, drilled)", COL["clean"], (0, -120, -40)),
        group(["Drum tap", "Tap nut", "Tap gasket"], "Drum tap", COL["valve"], (0, -260, -40)),
        P_("Clean lid", "Clean lid (bought, drilled)", COL["clean"], (0, -120, 120)),
        P_("Clean inlet", "Clean inlet fitting (made)", COL["made"], (0, -120, 170)),
        group(["Vent cap", "Insect screen"], "Vent cap and screen (made)", COL["made"], (0, -120, 170)),
        group(["Label"], "Labels (2)", "#F4F1E6", (0, -240, 0)),
    ]


def overview():
    p = bv.overview(build_order(), OUT / "overview.png", "Helpful Water C1 household gravity filter: prototype components",
                    elev=16, azim=-55, size=(13, 10), key=True)
    print("wrote", p)


SHEETS = {
    101: ("Leg front right", "Leg (four alike)", "Planed softwood 45 x 45 mm, dry; saw cut square", [
        "837 mm long, 45 x 45 mm; four alike",
        "Top end: 8.4 mm pilot hole 80 mm deep, centred, for the shelf coach screw",
        "Bottom end: 8.4 mm pilot hole 80 mm deep for the foot coach screw",
        "9 mm cross hole, side to side, 52.5 mm above the bottom end, for the rail bolt",
        "Front right leg only: two 4.6 mm holes in the front face, on the centre line, 385 and 535 mm up, for the P-clip screws",
        "Arris every edge by 2 mm; oil with a food-safe oil, never a wood preservative",
        "Check: square ends; legs stand on a flat floor without rocking"]),
    102: ("Foot right", "Foot (two alike)", "Planed softwood 45 x 45 mm", [
        "560 mm long; two alike; the legs sit 187.5 mm either side of the middle",
        "Two 8.4 mm holes through, 375 mm apart, counterbored 16 mm x 6 mm underneath",
        "The 560 mm length is the stability fix: the loaded stand needs 15 deg to tip",
        "Check: both feet flat and parallel, 375 mm apart"]),
    103: ("Lower rail right", "Lower rail (two alike)", "Planed softwood 45 x 45 mm", [
        "420 mm long; two alike; bolted to the outside of the left and right leg pairs",
        "Two 9 mm holes across, 375 mm apart, 22.5 mm from the top face",
        "Two 4.6 mm pilot holes in the top face for the lower shelf screws, 300 mm apart",
        "Check: top faces level at 120 mm above the floor once bolted"]),
    104: ("Upper shelf", "Upper shelf", "Exterior plywood 18 mm", [
        "420 x 420 mm; corners and edges rounded 2 mm",
        "Four 9 mm holes 187.5 mm from the centre each way, countersunk for the coach screw heads",
        "Seal the edges with food-safe oil; the raw bucket stands in the middle",
        "Check: sits flat on the four leg tops; the raw valve clears the right edge"]),
    105: ("Lower shelf", "Lower shelf", "Exterior plywood 18 mm", [
        "510 x 420 mm with four 46 x 46 mm notches round the legs",
        "Four 5 mm holes over the rails for the shelf screws",
        "The clean bucket stands 75 mm forward of centre so its tap overhangs the front",
        "Check: drops over the legs onto the rails; top face at 138 mm"]),
    106: ("Diagonal brace right", "Diagonal brace (two alike)", "Planed softwood 70 x 20 mm", [
        "About 900 mm long, ends cut at the brace angle so it stays inside the frame",
        "Runs from 180 mm up at the front leg to 820 mm up at the back leg, on the outside",
        "One 5 mm screw into each leg; stops the frame racking front to back",
        "Check: the frame does not lean when pushed at the top shelf"]),
    107: ("Cloth clamp", "Cloth clamp ring", "Polypropylene (or PETG); FDM print, 0.2 mm layers", [
        "190 mm across, 136 mm bore; 4 mm flange; 22 mm spigot 137 mm across",
        "Four grip lugs on the flange rim",
        "The spigot pushes the folded cloth into the 160 mm fill hole and holds it",
        "Check: presses in by hand over 8 layers of cloth and lifts out for washing"]),
    108: ("Fill cover", "Fill cover", "Polypropylene; FDM print", [
        "198 mm across, 3 mm top, 5 mm skirt that sits over the clamp ring",
        "Handle 60 x 14 x 12 mm with a finger slot",
        "Keeps dust and hands off the cloth between fills",
        "Check: sits over the ring without rocking"]),
    109: ("Dosing port collar", "Dosing port collar", "Polypropylene; FDM print", [
        "76 mm flange on the lid, 59.4 mm spigot through the 60 mm hole",
        "External thread, 3 mm pitch, for the cap; bore 52 mm",
        "The interface for a solution D doser; size to agree with solution D",
        "Check: the cap screws on by hand and seals against dust"]),
    110: ("Dosing port cap", "Dosing port cap", "Polypropylene; FDM print", [
        "70 mm across with a 10.5 mm knurled skirt",
        "Screws onto the collar thread",
        "Check: turns on and off with wet hands"]),
    111: ("Clean inlet", "Clean inlet fitting", "Polypropylene; FDM print, 100 % infill", [
        "40 mm flange on the clean lid, 21.4 mm spigot through a 22 mm hole",
        "Retaining collar under the lid; 3/8 in barb on top, 7 mm bore",
        "The clean hose pushes 15 mm over the barb",
        "Check: the hose stays on with a firm pull; the fitting does not spin loose"]),
    112: ("Vent cap", "Vent cap", "Polypropylene; FDM print", [
        "34 mm across, six 4 mm side ports under a closed top",
        "15.4 mm spigot through the 16 mm lid hole; stainless screen disc inside",
        "Lets air out while filling and in while drawing water; keeps insects out",
        "Check: no direct line of sight into the bucket through the ports"]),
    113: ("Valve tag", "Valve tag", "Polypropylene, yellow; FDM print", [
        "30 x 40 x 2 mm with a 5 mm hole; pictogram: tablet, clock, 30, valve shut",
        "Hangs on the valve lever on a cable tie",
        "Check: readable from the front of the stand"]),
}


def sheets(which=None):
    for no, (prefix, title, material, notes) in SHEETS.items():
        if which and str(no) not in which:
            continue
        q = find(prefix)[0]
        part = Part(title, q["shape"], "#0F766E", q["bom"])
        c = q["shape"].bounding_box().center()
        neigh = [Part(n, x["shape"], "#D1D5DB") for n, x in parts().items() if x["kind"] in ("made", "bought") and not n.startswith(prefix)
                 and (x["shape"].bounding_box().center() - c).length < 450]
        view = None
        if prefix.startswith("Diagonal"):
            from build123d import Rot
            import math
            view = Rot(-math.degrees(math.atan2(700.0, 2 * M.LC + M.T)), 0, 0) * Pos(-q["shape"].bounding_box().center()) * q["shape"]
        p = bv.component_sheet(part, neigh, PROJECT, f"HWC-DWG-{no}", f"C1 {title}: making sketch", material, notes, DATE,
                               out_dir=str(DWG), view_shape=view)
        print("wrote", p)


def joints(which=None):
    J = {
        1: ("Raw outlet: bulkhead through the bucket wall, gaskets, strainer, valve and barb",
            ["Raw bucket", "Raw outlet", "Inner gasket", "Outer gasket", "Strainer", "Ball valve", "Hose barb", "Raw hose", "Upper shelf"],
            ((60, 290), (-40, 40), (900, 1010))),
        2: ("Raw lid: cloth pinched by the clamp ring in the fill hole, cover over it, dosing port beside",
            ["Raw lid", "Prefilter cloth", "Cloth clamp", "Fill cover", "Dosing port", "Raw bucket"],
            ((-160, 160), (-160, 160), (1215, 1300))),
        3: ("Module on the front right leg: two P-clips, raw hose onto the top inlet",
            ["Module", "Fibre", "Potting", "P-clip", "Wood screw 5 x 30, P-clip", "Leg front right", "Raw hose"],
            ((140, 240), (-280, -150), (330, 700))),
        4: ("Clean side: tee under the module, luer backflush port and cap, pinch clamp on the clean hose",
            ["Module header", "Clean-side tee", "Backflush port cap", "Pinch clamp", "Clean hose"],
            ((100, 230), (-290, -190), (300, 400))),
        5: ("Clean lid: inlet fitting with the hose on its barb, screened vent cap",
            ["Clean lid", "Clean inlet", "Vent cap", "Insect screen", "Clean hose", "Clean bucket"],
            ((-110, 110), (-190, -100), (480, 580))),
        6: ("Clean bucket: drum tap through the wall, gasket outside, nut inside, 45 mm up",
            ["Clean bucket", "Drum tap", "Tap nut", "Tap gasket", "Lower shelf"],
            ((-50, 50), (-270, -150), (120, 240))),
        7: ("Stand: rail bolted through the leg, lower shelf screwed down, foot screw from below",
            ["Leg front right", "Lower rail right", "Lower shelf", "Foot right", "M8x105 hex bolt rail RF", "M8 washer rail RF", "M8 hex nut rail RF",
             "Wood screw 5 x 30, shelf to rail", "Coach screw M8 x 80, foot"],
            ((140, 280), (-280, -120), (0, 160))),
    }
    for k, (title, names, win) in J.items():
        if which and str(k) not in which:
            continue
        (x0, x1), (y0, y1), (z0, z1) = win
        box = Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)
        ps = []
        for n in names:
            for q in find(n):
                try:
                    s = q["shape"] & box
                    if s.volume > 1e-3:
                        ps.append(Part(q["name"], s, q["color"]))
                except Exception:
                    pass
        cut = "+Y" if k in (1, 2, 3, 6) else None
        p = bv.joint(ps, OUT / f"joint-{k:02d}.png", title, subtitle="Cut through the axis; front half removed" if cut else "Close-up",
                     cut=cut, elev=14, azim=-60)
        print("wrote", p)


def steps(which=None):
    stand_done = [group(["Foot", "Leg", "Lower rail", "M8", "Upper shelf", "Lower shelf", "Diagonal", "Coach", "Wood screw 5 x 30, shelf",
                         "Wood screw 5 x 30, brace"], "Stand", COL["timber"])]
    raw_full = group(["Raw bucket", "Raw outlet", "Inner gasket", "Outer gasket", "Strainer", "Ball valve", "Valve tag", "Hose barb",
                      "Raw lid", "Prefilter", "Cloth clamp", "Fill cover", "Dosing port", "Label: settle"], "Raw bucket set", COL["raw"])
    mod = group(["Module", "Fibre", "Potting"], "Module", COL["module"])
    S = [
        ("Step 1: stand the four legs on the two feet and drive the coach screws up from below",
         [], [group(["Leg"], "Legs", COL["timber"], (0, 0, 150)), group(["Coach screw M8 x 80, foot"], "Foot screws", COL["steel"], (0, 0, -60))],
         [group(["Foot"], "Feet", COL["timber"])]),
        ("Step 2: bolt the two lower rails to the outside of the left and right leg pairs, 75 to 120 mm up",
         [group(["Foot", "Leg", "Coach screw M8 x 80, foot"], "Feet and legs", COL["timber"])],
         [group(["Lower rail"], "Rails", COL["timber"], (0, 0, 0)), group(["M8"], "Bolt sets", COL["steel"], (0, 0, 0))], []),
        ("Step 3: screw the upper shelf onto the leg tops and the lower shelf onto the rails",
         [group(["Foot", "Leg", "Lower rail", "M8", "Coach screw M8 x 80, foot"], "Frame", COL["timber"])],
         [P_("Upper shelf", "Upper shelf", COL["ply"], (0, 0, 150)), P_("Lower shelf", "Lower shelf", COL["ply"], (0, 0, 150)),
          group(["Coach screw M8 x 80, shelf", "Wood screw 5 x 30, shelf"], "Screws", COL["steel"], (0, 0, 150))], []),
        ("Step 4: screw the two diagonal braces to the outside of the left and right legs",
         [group(["Foot", "Leg", "Lower rail", "M8", "Upper shelf", "Lower shelf", "Coach", "Wood screw 5 x 30, shelf"], "Frame", COL["timber"])],
         [group(["Diagonal", "Wood screw 5 x 30, brace"], "Braces", COL["timber"], (0, 0, 0))], []),
        ("Step 5: drill the raw bucket, fit the bulkhead with a gasket each side, the strainer inside, then the valve and barb",
         [P_("Raw bucket", "Raw bucket")],
         [group(["Raw outlet", "Inner gasket", "Outer gasket"], "Bulkhead", COL["fit"], (60, 0, 0)), P_("Strainer", "Strainer", COL["fit"], (-50, 0, 0)),
          group(["Ball valve", "Valve tag"], "Valve and tag", COL["valve"], (90, 0, 0)), P_("Hose barb", "Barb", COL["fit"], (120, 0, 0))], []),
        ("Step 6: cut the raw lid, lay the folded cloth over the fill hole, press the clamp ring in, fit the dosing collar and caps",
         [P_("Raw lid", "Raw lid")],
         [P_("Prefilter cloth", "Cloth", "#B8AD8F", (0, 0, 40)), P_("Cloth clamp", "Clamp ring", COL["made"], (0, 0, 70)),
          P_("Fill cover", "Cover", COL["raw"], (0, 0, 110)), group(["Dosing port"], "Dosing collar and cap", COL["made"], (0, 0, 70))], []),
        ("Step 7: stand the raw bucket on the upper shelf with its valve to the right; snap the lid on",
         stand_done, [Part("Raw bucket set", raw_full.shape, COL["raw"], None, (0, 0, 200))], []),
        ("Step 8: clip the module upright to the front right leg, inlet on top, and screw the two P-clips on",
         stand_done + [raw_full], [mod.__class__(mod.name, mod.shape, mod.color, None, (0, -120, 0)),
                                    group(["P-clip", "Wood screw 5 x 30, P-clip"], "P-clips", COL["fit"], (0, -80, 0))], []),
        ("Step 9: push the raw hose over the valve barb and the module inlet; it must fall all the way, with no high loop",
         stand_done + [raw_full, mod], [P_("Raw hose", "Raw hose", COL["hose"], (60, -60, 0))], []),
        ("Step 10: drill the clean bucket and lid; fit the tap, the inlet fitting and the vent cap with its screen",
         [P_("Clean bucket", "Clean bucket")],
         [group(["Drum tap", "Tap nut", "Tap gasket"], "Tap", COL["valve"], (0, -60, 0)), P_("Clean lid", "Clean lid", COL["clean"], (0, 0, 80)),
          P_("Clean inlet", "Inlet", COL["made"], (0, 0, 130)), group(["Vent cap", "Insect screen"], "Vent", COL["made"], (0, 0, 130))], []),
        ("Step 11: stand the clean bucket on the lower shelf with its tap to the front",
         stand_done + [raw_full, mod],
         [group(["Clean bucket", "Clean lid", "Clean inlet", "Vent cap", "Insect screen", "Drum tap", "Tap nut", "Tap gasket", "Label: treated"],
                "Clean bucket set", COL["clean"], (0, -200, 0))], []),
        ("Step 12: tee onto the module outlet, cap on the backflush port, clean hose to the lid inlet, pinch clamp open",
         stand_done + [raw_full, mod, group(["Clean bucket", "Clean lid", "Clean inlet", "Vent cap", "Drum tap"], "Clean bucket", COL["clean"])],
         [group(["Clean-side tee", "Backflush port cap"], "Tee", COL["fit"], (0, -60, -40)), P_("Clean hose", "Clean hose", "#B8D8E4", (0, -60, 0)),
          P_("Pinch clamp", "Pinch clamp", COL["made"], (0, -80, 0))], []),
    ]
    for k, (title, done, new, ctx) in enumerate(S, 1):
        if which and str(k) not in which:
            continue
        p = bv.step(done, new, OUT / f"step-{k:02d}.png", title, context=ctx, elev=16, azim=-55, size=(8, 8))
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
