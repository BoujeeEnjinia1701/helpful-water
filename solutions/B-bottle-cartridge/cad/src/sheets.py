"""Helpful Water B drawing set and STL export for the carried option B1 (squeeze cartridge; the concept choice is
proposed, awaiting Amish, HWB-DEC-001 D1).

Run from the solution folder:  python cad/src/sheets.py [ga|section|stl]   (no argument: all three, one per process
on a small machine)
    cad/drawings/HWB-DWG-001   general arrangement of the B1 cartridge (outside parts)
    cad/drawings/HWB-DWG-002   half section showing the flow path, seals and stages
    cad/stl/*.stl              the cartridge assembly and each made part, for viewing and printing
Making sketches for each made part (HWB-DWG-101 onward) are drawn by cad/src/build_plan_media.py. Sheets are generated
from cad/src/model.py and never edited by hand. Figures in the notes come from HWB-CAL-001 (docs/04-calcs/sizing.py).
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
OUTSIDE = ("Neck collar", "Housing", "Spout with", "Push-pull", "Dust cover")


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())


def b1(context=False):
    return M.components("B1", context=context)


def ga():
    parts = [q for q in b1() if q["name"].startswith(OUTSIDE)]
    work = DWG / "_views_ga"
    views = project_views(Compound(children=[q["shape"] for q in parts]), work)
    r = res()
    s = Sheet(project="Helpful Water B", title="B1 squeeze cartridge on a 28 mm PCO 1881 bottle neck: general arrangement",
              dwg_no="HWB-DWG-001", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="PP housing, collar, capsule and spout; EPDM or silicone seals; 316L mesh; bought hollow-fibre module. See bom/bom.csv",
              revisions=[("P1", "Preliminary GA from the TRL 3 model (HWB-CAL-001)", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; outside parts")
    s.add_notes("Key dimensions (mm) and data", [
        f"Overall {r['b1_size_mm']['length']:.0f} long x {P['HOUSING_OD'] + 3:.0f} across the grip band",
        "Fits 28 mm PCO 1881 and PCO 1810 necks; 38 mm by adapter",
        f"Housing {P['HOUSING_OD']:.0f} OD, {P['HOUSING_ID']:.0f} bore; 40 x 3 thread to the collar",
        f"Module {P['U_FIBRES']} looped fibres 0.8/0.5, {r['area_m2']['B1']:.2f} m2, 0.1 um",
        f"Carbon capsule {P['BED_D']:.0f} x {P['BED_H']:.0f}, about {r['carbon']['mass_g']:.0f} g coconut GAC",
        f"Flow (estimate, clean): {r['b1']['adult']['clean']['q_ml_min']:.0f} mL/min at {r['squeeze_kpa']['adult']:.0f} kPa",
        f"Weak child {r['squeeze_kpa']['child_10_11_weak']:.0f} kPa: {r['b1']['child_10_11_weak']['clean']['q_ml_min']:.0f} mL/min (estimate)",
        f"Dry mass about {r['mass_b1_dry_g']:.0f} g (estimate)",
        "Duckbill air valve in the collar; push-pull valve and dust cover",
        "Backflush: 60 mL syringe at the nozzle, capsule removed",
        "Not a virus barrier; co-treat with chlorine where viruses are a risk",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWB-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWB-DWG-001.svg, .pdf, .png")


def section():
    cut = Pos(0, 100, 0) * Box(200, 200, 600)
    keep = []
    for q in b1():
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
    s = Sheet(project="Helpful Water B", title="B1 squeeze cartridge: half section through the flow path",
              dwg_no="HWB-DWG-002", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="See HWB-DWG-001 and bom/bom.csv",
              revisions=[("P1", "Preliminary section from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; half removed")
    s.add_notes("Flow path (front view, bottom to top)", [
        "1 Bottle water enters the 18 mm inlet bore of the collar",
        "2 150 um 316L mesh disc on the collar deck",
        "3 Carbon capsule (dirty side): pads, 20 mm GAC bed",
        "4 Shell side of the module: outside of the fibres",
        "5 Through the fibre walls into the lumens (outside-in)",
        "6 Lumens open in the potting into the clean header",
        "7 Two header O-rings: the only dirty-to-clean seal",
        "8 Nipple, spout and push-pull valve to the mouth or a cup",
        "Air returns to the bottle through the duckbill in the collar",
        "Collar O-ring and neck gasket keep bottle water in",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWB-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWB-DWG-002.svg, .pdf, .png")


def stl():
    out = ROOT / "cad/stl"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.stl"):
        old.unlink()
    parts = [q for q in b1() if q["kind"] != "context"]
    export_stl(Compound(children=[q["shape"] for q in parts]), str(out / "hwb-b1-cartridge-assembly.stl"), tolerance=0.1, angular_tolerance=0.3)
    names = {1: "neck-collar", 2: "housing", 3: "carbon-capsule-body", 4: "carbon-capsule-lid", 5: "spout", 6: "drink-valve", 7: "dust-cover"}
    for b, n in names.items():
        sel = [q["shape"] for q in parts if q["bom"] == b and q["kind"] == "made"]
        export_stl(Compound(children=sel), str(out / f"hwb-b1-{n}.stl"), tolerance=0.05, angular_tolerance=0.2)
    print("wrote", len(list(out.glob("*.stl"))), "STL files to cad/stl/")


if __name__ == "__main__":
    fns = {"ga": ga, "section": section, "stl": stl}
    for w in sys.argv[1:] or list(fns):
        fns[w]()
