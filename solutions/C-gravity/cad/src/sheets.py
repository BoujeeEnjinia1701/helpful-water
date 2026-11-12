"""Helpful Water C drawing set and STL export for the carried option C1 (two-bucket hollow-fibre filter; the concept
choice is proposed, awaiting Amish, HWC-DEC-001 D1).

Run from the solution folder:  python cad/src/sheets.py [ga|section|stl]   (no argument: all three; one per process
on a small machine)
    cad/drawings/HWC-DWG-001   general arrangement of C1 on its stand
    cad/drawings/HWC-DWG-002   section through the raw outlet, the module and the clean bucket (water path)
    cad/stl/*.stl              each made part, for viewing and printing
Making sketches for each made part (HWC-DWG-101 onward) are drawn by cad/src/build_plan_media.py. Sheets are generated
from cad/src/model.py and never edited by hand. Figures in the notes come from HWC-CAL-001 (docs/04-calcs/sizing.py).
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
OUTSIDE = ("Raw bucket", "Raw lid", "Fill cover", "Clean bucket", "Clean lid", "Leg", "Foot", "Upper shelf", "Lower shelf",
           "Lower rail", "Diagonal", "Module shell", "Module top", "Module header", "Raw hose", "Clean hose", "Ball valve",
           "Drum tap", "Dosing port cap")


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())


def c1(context=False):
    return M.components("C1", context=context)


def ga():
    parts = [q for q in c1() if q["name"].startswith(OUTSIDE)]
    work = DWG / "_views_ga"
    views = project_views(Compound(children=[q["shape"] for q in parts]), work)
    r = res()
    s = Sheet(project="Helpful Water C", title="C1 two-bucket hollow-fibre filter on its timber stand: general arrangement",
              dwg_no="HWC-DWG-001", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="Food-grade HDPE buckets; PP fittings; silicone hose; bought hollow-fibre module; softwood and plywood stand. See bom/bom.csv",
              revisions=[("P1", "Preliminary GA from the TRL 3 model (HWC-CAL-001)", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale")
    s.add_notes("Key dimensions (mm) and data", [
        f"Footprint 520 x {P['FOOT_L']:.0f} (feet); {r['c1_size_mm']['height']:.0f} tall with the raw lid",
        f"Upper shelf top {P['TOP_Z']:.0f}; lower shelf top {P['LOW_Z'] + P['SHELF_T']:.0f}; raw rim {r['raw']['rim_z_mm']:.0f}",
        f"Raw outlet {P['OUTLET_H']:.0f} above the raw floor: {r['raw']['settle_zone_l']:.1f} L settling zone",
        f"Fill line {P['FILL_L']:.0f} L; batch {r['raw']['batch_l']:.1f} L; clean refill line {P['REFILL_L']:.0f} L",
        f"Head {r['head']['head_m'][0]:.2f} to {r['head']['head_m'][1]:.2f} m ({r['head']['head_kpa'][0]:.1f} to {r['head']['head_kpa'][1]:.1f} kPa)",
        f"Module {P['U_FIBRES']} looped fibres 0.8/0.5, {r['area_m2']:.2f} m2, 0.1 um; {P['MOD_OD']:.0f} x {P['MOD_L']:.0f}",
        f"Flow (estimate): {r['c1']['clean']['q_mean_lph']:.0f} L/h clean, {r['c1']['fouled']['q_mean_lph']:.0f} L/h before backflush",
        f"45 L a day in {r['c1']['clean']['hours_per_day']:.1f} to {r['c1']['fouled']['hours_per_day']:.1f} h of filtering (estimate)",
        f"Tip angle loaded {r['stability']['feet_560']['tip_deg']:.0f} deg on the 560 mm feet",
        "Backflush: 60 mL luer syringe at the tee, pinch clamp shut",
        "Not a virus barrier; dose chlorine (solution D) in the raw bucket first",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWC-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWC-DWG-001.svg, .pdf, .png")


SECTION = ("Raw bucket", "Raw outlet", "Inner gasket", "Outer gasket", "Strainer", "Ball valve", "Hose barb", "Module",
           "Fibre bundle", "Potting", "Clean-side tee", "Backflush", "Clean bucket", "Clean lid", "Clean inlet", "Drum tap",
           "Tap nut", "Tap gasket", "Upper shelf", "Lower shelf")


def section():
    keep = []
    for q in c1():
        if not q["name"].startswith(SECTION):
            continue
        y0 = M.MOD_Y if q["name"].startswith(("Module", "Fibre", "Potting", "Clean-side tee", "Backflush")) else (
            P["CLEAN_Y"] if q["name"].startswith(("Clean bucket", "Clean lid", "Drum tap", "Tap", "Lower shelf")) else 0.0)
        if q["name"].startswith("Clean inlet"):
            y0 = M.INLET_XY[1]
        try:
            sh = q["shape"] & Pos(0, y0 + 2000, 0) * Box(6000, 4000, 6000)
            if sh.volume > 1e-3:
                keep.append(sh)
        except Exception:
            pass
    work = DWG / "_views_sec"
    views = project_views(Compound(children=keep), work, center_lines=False)
    s = Sheet(project="Helpful Water C", title="C1 water path: section through the raw outlet, module and clean bucket",
              dwg_no="HWC-DWG-002", rev="P1", author="Amish Chadha", date=DATE, concept=True, scale=None,
              material="See HWC-DWG-001 and bom/bom.csv",
              revisions=[("P1", "Preliminary section from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; each group cut on its own axis")
    s.add_notes("Water path (front view, top to bottom)", [
        "1 Fill through the cloth ring; settle 1 h (overnight above 50 NTU)",
        "2 Where viruses are a risk: dose D at the port; valve shut 30 min",
        "3 Sludge stays below the 250 um strainer outlet, 50 mm up",
        "4 Ball valve and raw hose fall to the module's top inlet",
        "5 Shell side: outside of the fibres; air rises back up the hose",
        "6 Through the fibre walls into the lumens (outside-in)",
        "7 Lumens open in the potting into the header at the bottom",
        "8 Tee: luer backflush port; pinch clamp on the clean hose",
        "9 Clean hose rises to the inlet in the closed clean lid",
        "10 Clean bucket: screened vent, tap 45 mm up, no dipping",
        "Clean side runs above atmospheric pressure: leaks drip out",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWC-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWC-DWG-002.svg, .pdf, .png")


def stl():
    out = ROOT / "cad/stl"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.stl"):
        old.unlink()
    parts = [q for q in c1() if q["kind"] == "made" and q["bom"] not in (25, 26, 27)]
    for q in parts:
        n = M.cp_slug(q["name"]) if hasattr(M, "cp_slug") else "".join(ch if ch.isalnum() else "-" for ch in q["name"].lower()).strip("-")
        while "--" in n:
            n = n.replace("--", "-")
        export_stl(q["shape"], str(out / f"hwc-c1-{n[:40]}.stl"), tolerance=0.1, angular_tolerance=0.3)
    print("wrote", len(list(out.glob("*.stl"))), "STL files to cad/stl/ (printed parts; the timber is cut, not printed)")


if __name__ == "__main__":
    fns = {"ga": ga, "section": section, "stl": stl}
    for w in sys.argv[1:] or list(fns):
        fns[w]()
