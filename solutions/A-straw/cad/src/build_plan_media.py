"""Helpful Water A filter straw: prototype build plan pictures (HWA-BLD-001, STANDARDS section 18).

Run from the solution folder:
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py components("A1"), so pictures and model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/HWA-DWG-101 to 108        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining (cut open)
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import functools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
import model as M  # noqa: E402

OUT = ROOT / "docs/05-build-plan"
DWG = ROOT / "cad/drawings"
DATE = "2026-11-11"
PROJECT = "Helpful Water A: filter straw"


@functools.lru_cache(None)
def raw():
    return {q["name"]: q for q in M.components("A1") if q["kind"] != "context"}


def P_(name, explode=None, color=None):
    q = raw()[name]
    return Part(name, q["shape"], color or q["color"], q["bom"], tuple(explode if explode is not None else q["explode"]))


# build order for the overview (made and bought components; O-rings shown once each)
ORDER = ["Housing body", "Intake cap", "Prefilter mesh disc, 316L 250 um", "Mesh retaining ring", "O-ring, intake cap (grit seal)",
         "Module cage (perforated shell)", "O-ring, module lower (clean/dirty seal)", "O-ring, module upper (clean/dirty seal)",
         "Carbon cartridge body", "Carbon inlet screen, 316L", "Activated carbon bed, coconut GAC", "Carbon fines pad",
         "O-ring, carbon cartridge", "Mouthpiece", "O-ring, mouthpiece inner", "O-ring, mouthpiece outer", "Mouthpiece cap",
         "Tether band", "Backflush port plug (tethered)", "Intake cover", "Split ring, stainless 12 mm", "Lanyard cord"]
MODULE = ["Module cage (perforated shell)", "Bottom potting block (closes fibre ends)", "Hollow-fibre bundle, about 220 fibres",
          "Top potting block (open lumens)", "Module header collar"]
LABEL = {"Module cage (perforated shell)": "Hollow-fibre module (bought, pre-potted)"}


OV_EX = {"Housing body": (0, 0, 0), "Intake cap": (0, 0, -70), "Prefilter mesh disc, 316L 250 um": (-40, 0, -60),
         "Mesh retaining ring": (-40, 0, -45), "O-ring, intake cap (grit seal)": (-40, 0, -100),
         "Module cage (perforated shell)": (40, 0, 0), "O-ring, module lower (clean/dirty seal)": (75, 0, -25),
         "O-ring, module upper (clean/dirty seal)": (75, 0, 0), "Carbon cartridge body": (40, 0, 65),
         "Carbon inlet screen, 316L": (75, 0, 40), "Activated carbon bed, coconut GAC": (75, 0, 80), "Carbon fines pad": (75, 0, 105),
         "O-ring, carbon cartridge": (40, 0, 35), "Mouthpiece": (0, 0, 50), "O-ring, mouthpiece inner": (-40, 0, 40),
         "O-ring, mouthpiece outer": (-40, 0, 65), "Mouthpiece cap": (0, 0, 85), "Tether band": (-45, 0, 15),
         "Backflush port plug (tethered)": (-45, 0, -20), "Intake cover": (0, 0, -110), "Split ring, stainless 12 mm": (0, 0, 115),
         "Lanyard cord": (0, 0, 130)}


def overview():
    ps = []
    for n in ORDER:
        p = P_(n, OV_EX[n])
        p.name = LABEL.get(n, n)
        ps.append(p)
    # the module drawn as one item: add its inner parts without a number by merging into the cage shape
    from build123d import Compound
    mod = [raw()[n]["shape"] for n in MODULE]
    i = ORDER.index("Module cage (perforated shell)")
    ps[i] = Part(ps[i].name, Compound(children=mod), "#CFD6D9", 5, OV_EX["Module cage (perforated shell)"])
    return bv.overview(ps, OUT / "overview.png", title=f"{PROJECT}: prototype components in build order",
                       subtitle="Every component, pulled apart and numbered in build order; plan, not yet built", size=(10, 9), key=True)


SHEETS = {
    101: ("Housing body", "Housing body: making sketch",
          "Polypropylene (PP-H or PP-R) printed vertically, 0.2 mm layers, 4 walls; PETG for dry fit only. Moulded PP at scale",
          ["Tube 26 mm outside, 22 mm bore, 178 mm long (12 to 190 mm on the straw)",
           "Seat ring inside at 10 to 12 mm from the bottom end: bore 17 mm",
           "Both ends: a 1.5 mm deep groove ring 1 mm in, with two 4.6 mm entry slots",
           "Socket boss 8 mm across at 141 mm from the bottom end, on one side",
           "Socket: taper 4.3 to 3.9 mm, 5 mm deep, 2 mm hole into the bore",
           "Dip line: shallow V groove 98 mm from the bottom end",
           "Ream the bore to 22.0 +-0.05 mm where the O-rings run (smooth, round)",
           "Check: a 21.8 mm plug gauge slides the full length"]),
    102: ("Intake cap", "Intake cap: making sketch", "Polypropylene printed with the spigot up; moulded PP at scale",
          ["Head 26 mm across x 12 mm; eight 2.5 mm slots round the side, six 2.5 mm holes in the end",
           "Spigot 21.8 mm x 10 mm; two lugs 4 x 1.1 mm, 0.7 mm proud, opposite each other",
           "O-ring groove floor 19.3 +-0.05 mm, 2.4 mm wide, centred 6 mm up the spigot",
           "Counterbore at the spigot top: 17 mm across, 2 mm deep, for the mesh and ring",
           "Fits: spigot into the housing bottom, lugs down the slots, quarter turn",
           "Check: O-ring fitted, cap turns a quarter turn by hand and stops"]),
    103: ("Mesh retaining ring", "Mesh retaining ring: making sketch", "Polypropylene printed flat",
          ["Ring 17 mm outside, 13 mm inside, 1.6 mm thick",
           "Press it into the cap counterbore over the mesh disc",
           "Fit: light press; the mesh must lie flat with no gap at its rim",
           "Check: the mesh does not move when the cap is tapped upside down"]),
    104: ("Carbon cartridge body", "Carbon cartridge body: making sketch", "Polypropylene printed with the open end up",
          ["Cup 21.8 mm outside, 16 mm bore, 24 mm tall; floor 2 mm",
           "Floor holes: six 2 mm on a 9 mm circle and one 2.5 mm in the middle",
           "O-ring groove floor 19.3 +-0.05 mm, 2.4 mm wide, 6 mm above the floor",
           "Three legs under the floor, 1.8 x 3 x 6 mm, at 60, 180 and 300 deg",
           "Legs stand on the module collar and hold the header open",
           "Check: the cup holds 4.0 mL of water to the brim"]),
    105: ("Mouthpiece", "Mouthpiece: making sketch", "Polypropylene printed tip up (smooth tip: sand and polish); food-grade silicone overmould is an option at scale",
          ["Spigot 21.8 mm x 10 mm with an outlet grid (six 2 mm and one 2 mm hole)",
           "Two O-ring grooves, floor 19.3 +-0.05 mm, 2.4 mm wide, at 3 and 6 mm from the end",
           "Two bayonet lugs 1.8 mm below the collar, opposite each other",
           "Collar 26 mm with 12 grip ribs; taper to a 10 mm tip, 4 mm straight; bore 5 mm",
           "Check: the tip has no ridges or sharp edges; bore clear by eye"]),
    106: ("Mouthpiece cap", "Mouthpiece cap: making sketch", "Polypropylene printed upright",
          ["Cup 13.2 mm outside over the 10 mm tip, 7 mm deep",
           "Plug 4.9 mm across, 3 mm long inside the cup: it seals the 5 mm bore",
           "Lanyard eye 6.4 mm across with a 3.2 mm hole on top",
           "Check: the cap snaps on and holds a 50 kPa push from the backflush syringe"]),
    107: ("Tether band", "Backflush plug and tether band: making sketch", "Platinum-cure silicone, Shore 50 A, cast in a printed two-part mould",
          ["Band 26 mm inside, 0.8 mm thick, 6 mm tall; stretches over the housing",
           "Strap 3 x 0.8 mm from the band down to the plug",
           "Plug: taper 4.3 to 3.9 mm x 4.5 mm with a 7.2 mm head",
           "Check: the plug seals the socket against a gentle suck with the intake covered"]),
    108: ("Intake cover", "Intake cover: making sketch", "Platinum-cure silicone, Shore 50 A, cast in a printed mould",
          ["Cup 28.4 mm outside, 26 mm inside, 11 mm deep; 2 mm end",
           "Sixteen grip ribs round the outside",
           "Check: it slips over the intake cap and stays on when shaken"]),
}


def sheets(which=None):
    for no, (name, title, mat, notes) in SHEETS.items():
        if which and str(no) not in which:
            continue
        part = P_(name)
        nb = [P_(n) for n in ("Housing body", "Intake cap", "Mouthpiece", "Carbon cartridge body") if n != name]
        if name == "Tether band":
            from build123d import Compound
            part = Part(name, Compound(children=[raw()["Tether band"]["shape"], raw()["Backflush port plug (tethered)"]["shape"]]), "#C2410C")
        print(bv.component_sheet(part, nb, PROJECT, f"HWA-DWG-{no}", title, mat, notes, DATE))


def _cut_window(names, z0, z1):
    from build123d import Box, Pos
    win = Pos(0, 0, (z0 + z1) / 2) * Box(60, 60, z1 - z0)
    out = []
    for n in names:
        q = raw()[n]
        try:
            s = q["shape"] & win
            if s.volume > 1e-3:
                out.append(Part(n, s, q["color"], q["bom"]))
        except Exception:
            pass
    return out


JOINTS = {
    1: ("Joint 1: intake cap, mesh and housing bottom (cut open)", ["Housing body", "Intake cap", "Prefilter mesh disc, 316L 250 um",
        "Mesh retaining ring", "O-ring, intake cap (grit seal)", "Module cage (perforated shell)"], (0, 34)),
    2: ("Joint 2: module collar and its two O-rings in the bore: the clean/dirty seal (cut open)", ["Housing body", "Module header collar",
        "Top potting block (open lumens)", "O-ring, module lower (clean/dirty seal)", "O-ring, module upper (clean/dirty seal)",
        "Hollow-fibre bundle, about 220 fibres", "Module cage (perforated shell)"], (128, 152)),
    3: ("Joint 3: clean header, backflush socket and carbon cartridge legs (cut open)", ["Housing body", "Module header collar",
        "Top potting block (open lumens)", "Carbon cartridge body", "Carbon inlet screen, 316L", "Activated carbon bed, coconut GAC",
        "O-ring, carbon cartridge", "Backflush port plug (tethered)", "Tether band"], (144, 168)),
    4: ("Joint 4: mouthpiece spigot, O-rings and bayonet in the housing top (cut open)", ["Housing body", "Mouthpiece", "O-ring, mouthpiece inner",
        "O-ring, mouthpiece outer", "Carbon fines pad", "Activated carbon bed, coconut GAC", "Carbon cartridge body"], (172, 206)),
}


def joints(which=None):
    for k, (title, names, (z0, z1)) in JOINTS.items():
        if which and str(k) not in which:
            continue
        print(bv.joint(_cut_window(names, z0, z1), OUT / f"joint-{k:02d}.png", title,
                       subtitle="Front half cut away; seen from the front right and above", cut="+Y", elev=20, azim=-70))


def _ps(names, ex=(0, 0, 0)):
    return [P_(n, ex) for n in names]


STEPS = {
    1: ("Step 1: seat the two O-rings on the module collar", [], ["Module cage (perforated shell)", "Module header collar"],
        ["O-ring, module lower (clean/dirty seal)", "O-ring, module upper (clean/dirty seal)"], (0, 0, 30)),
    2: ("Step 2: slide the module into the housing from the top until it stands on the seat ring", ["Housing body"], [],
        MODULE + ["O-ring, module lower (clean/dirty seal)", "O-ring, module upper (clean/dirty seal)"], (0, 0, 190)),
    3: ("Step 3: fill the carbon cartridge: screen, rinsed carbon, pad, then its O-ring", ["Carbon cartridge body"], [],
        ["Carbon inlet screen, 316L", "Activated carbon bed, coconut GAC", "Carbon fines pad", "O-ring, carbon cartridge"], (0, 0, 35)),
    4: ("Step 4: push the carbon cartridge in, legs first, onto the module collar", ["Housing body"], [],
        ["Carbon cartridge body", "Carbon inlet screen, 316L", "Activated carbon bed, coconut GAC", "Carbon fines pad", "O-ring, carbon cartridge"], (0, 0, 60)),
    5: ("Step 5: fit the mouthpiece O-rings, push the mouthpiece in, lugs down the slots, quarter turn", ["Housing body", "Carbon cartridge body"], [],
        ["Mouthpiece", "O-ring, mouthpiece inner", "O-ring, mouthpiece outer"], (0, 0, 40)),
    6: ("Step 6: press the mesh and ring into the intake cap, fit its O-ring, then twist the cap on", ["Housing body"], [],
        ["Intake cap", "Prefilter mesh disc, 316L 250 um", "Mesh retaining ring", "O-ring, intake cap (grit seal)"], (0, 0, -40)),
    7: ("Step 7: roll the tether band onto the housing and push the plug into the backflush socket", ["Housing body", "Mouthpiece", "Intake cap"], [],
        ["Tether band", "Backflush port plug (tethered)"], (0, 0, 45)),
    8: ("Step 8: fit the mouthpiece cap and intake cover; thread the split ring and lanyard", ["Housing body", "Mouthpiece", "Intake cap",
        "Tether band", "Backflush port plug (tethered)"], [], ["Mouthpiece cap", "Intake cover", "Split ring, stainless 12 mm", "Lanyard cord"], None),
}


def steps(which=None):
    for k, (title, done, ctx, new, ex) in STEPS.items():
        if which and str(k) not in which:
            continue
        if ex is None:
            newp = [P_("Mouthpiece cap", (0, 0, 25)), P_("Intake cover", (0, 0, -25)), P_("Split ring, stainless 12 mm", (0, 0, 25)),
                    P_("Lanyard cord", (0, 0, 25))]
        else:
            newp = _ps(new, ex)
        size = (7, 9.5) if k == 6 else (7, 8)
        print(bv.step(_ps(done), newp, OUT / f"step-{k:02d}.png", title, context=_ps(ctx), size=size, elev=20, azim=-60))


if __name__ == "__main__":
    cmd, args = (sys.argv[1] if len(sys.argv) > 1 else "all"), sys.argv[2:]
    if cmd in ("overview", "all"):
        print(overview())
    if cmd in ("sheets", "all"):
        sheets(args)
    if cmd in ("joints", "all"):
        joints(args)
    if cmd in ("steps", "all"):
        steps(args)
