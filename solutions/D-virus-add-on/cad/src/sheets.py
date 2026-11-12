"""Helpful Water D drawing set and STL export for the carried option D1 (tablet dose cap; the concept choice is
proposed, awaiting Amish, HWD-DEC-001 D1).

Run from the solution folder:  python cad/src/sheets.py [ga|section|stl]   (no argument: all three, one per process
on a small machine)
    cad/drawings/HWD-DWG-001   general arrangement of the D1 dose cap (outside parts)
    cad/drawings/HWD-DWG-002   half section showing the water path, the tablet well, the seals and the timer
    cad/stl/*.stl              the cap assembly and each made part, for viewing and printing
Making sketches for each made part (HWD-DWG-101 onward) are drawn by cad/src/build_plan_media.py. Sheets are generated
from cad/src/model.py and never edited by hand. Figures in the notes come from HWD-CAL-001 (docs/04-calcs/sizing.py).
CONCEPT, NOT FOR FABRICATION.

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
from build123d import Compound, Box, Pos, export_stl  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-11-11"
DWG = ROOT / "cad/drawings"
OUTSIDE = ("Dose cap body", "Well plug", "Tether", "Timer window", "Window screw")


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())["results"]


def d1(context=False):
    return M.components("D1", context=context)


def ga():
    parts = [q for q in d1() if q["name"].startswith(OUTSIDE)]
    work = DWG / "_views_ga"
    views = project_views(Compound(children=[q["shape"] for q in parts]), work)
    r = res()
    sz = r["d1_size_mm"]
    s = Sheet(project="Helpful Water D", title="D1 tablet dose cap on a 28 mm PCO 1881 neck: general arrangement",
              dwg_no="HWD-DWG-001", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="PP cap body, inserts and timer caps; clear PC or PETG plug, timer tube and window; silicone or EPDM seals. See bom/bom.csv",
              revisions=[("P1", "Preliminary GA from the TRL 3 model (HWD-CAL-001)", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; outside parts")
    s.add_notes("Key dimensions (mm) and data", [
        f"Overall {sz['x']:.0f} x {sz['y']:.0f} x {sz['z']:.0f} including the timer boss",
        f"Skirt {P['SKIRT_OD']:.0f} OD, 28 mm PCO 1881 female thread, 17 deep",
        f"Crown {P['CROWN_OD']:.0f} OD; tablet well bore {P['WELL_BORE']:.1f}; plug thread {P['PLUG_BORE']:.1f} x {P['PLUG_PITCH']:.0f}",
        f"Keyed inserts: 1 L bore {P['WELL_1L']}, 20 L bore {P['WELL_20L']}",
        f"Free height under the plug stop: {P['FREE_H']['1L']:.0f} (1 L), {P['FREE_H']['20L']:.0f} (20 L)",
        f"Timer tube 6 x 4 x 18, ball 2.0, fall 13; about {r['timer']['t_nominal_min']:.0f} min at 25 C (estimate)",
        f"Dose about 2.0 mg/L; {r['scenarios']['clear']['c30']:.1f} mg/L at 30 min (estimate)",
        f"Mass about {r['mass_g']['D1']:.0f} g without the bottle (estimate)",
        "Neck liner 27.6 x 20.5 x 1.5 silicone",
        "Plug face O-ring 22.6 x 1.6, 19 % squeeze",
        "Chlorine does not inactivate Cryptosporidium: filter after the wait",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWD-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWD-DWG-001.svg, .pdf, .png")


def section():
    cut = Pos(0, 100, 0) * Box(200, 200, 600)
    keep = []
    for q in d1():
        if q["kind"] == "fastener":
            continue
        try:
            sh = q["shape"] & cut
            if sh.volume > 1e-3:
                keep.append(sh)
        except Exception:
            pass
    work = DWG / "_views_sec"
    views = project_views(Compound(children=keep), work, center_lines=False)
    s = Sheet(project="Helpful Water D", title="D1 tablet dose cap: half section through the well and the timer",
              dwg_no="HWD-DWG-002", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="See HWD-DWG-001 and bom/bom.csv",
              revisions=[("P1", "Preliminary section from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; half removed")
    s.add_notes("Water path and parts (front view)", [
        "1 Bottle neck lip seals on the silicone liner",
        "2 17 mm bore in the deck opens to the well insert",
        "3 Floor slots 1.5 wide let water in, hold the tablet",
        "4 Tablet sits on the floor; two fit, three do not",
        "5 Clear plug with a 9 mm stop spigot closes the well",
        "6 Plug face O-ring seals on the crown top",
        "7 Timer in its own slot, outside the water space",
        "8 Ball 2 mm in sealed silicone fluid; flip to start",
        "Turn the bottle over and shake: the tablet dissolves",
        "Stand it up, flip the timer, wait, then filter",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWD-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWD-DWG-002.svg, .pdf, .png")


def stl():
    out = ROOT / "cad/stl"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.stl"):
        old.unlink()
    parts = [q for q in d1() if q["kind"] != "context"]
    export_stl(Compound(children=[q["shape"] for q in parts]), str(out / "hwd-d1-dose-cap-assembly.stl"), tolerance=0.05, angular_tolerance=0.2)
    names = {1: "dose-cap-body", 3: "well-insert-1l", 6: "well-plug", 8: "tether", 10: "timer-end-cap", 14: "timer-hub", 15: "timer-window"}
    for b, n in names.items():
        sel = [q["shape"] for q in parts if q["bom"] == b and q["kind"] == "made"]
        export_stl(Compound(children=sel), str(out / f"hwd-d1-{n}.stl"), tolerance=0.03, angular_tolerance=0.2)
    w20 = M.well_insert(P["WELL_20L"], 2, "20L")
    export_stl(w20, str(out / "hwd-d1-well-insert-20l.stl"), tolerance=0.03, angular_tolerance=0.2)
    print("wrote", len(list(out.glob("*.stl"))), "STL files to cad/stl/")


if __name__ == "__main__":
    fns = {"ga": ga, "section": section, "stl": stl}
    for w in sys.argv[1:] or list(fns):
        fns[w]()
