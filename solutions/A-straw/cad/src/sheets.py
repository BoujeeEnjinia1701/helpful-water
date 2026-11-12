"""Helpful Water A filter straw: drawing set and STL export for option A1 (recommended; choice awaiting Amish).

Run from the solution folder:  python cad/src/sheets.py [ga|section|stl]   (no argument: all three)
    cad/drawings/HWA-DWG-001   general arrangement, assembled straw with caps fitted
    cad/drawings/HWA-DWG-002   half-section arrangement: flow path, seals, header and backflush socket
    cad/stl/*.stl              the assembly and each made part, for viewing and printing
Making sketches for each made part (HWA-DWG-101 onward) are drawn by cad/src/build_plan_media.py.
Sheets are generated from cad/src/model.py and never edited by hand; figures come from HWA-CAL-001.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
from build123d import Box, Compound, Pos, export_stl  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-11-11"
DWG = ROOT / "cad/drawings"
R = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
PROJECT = "Helpful Water A: filter straw"
MAT = "PP parts (printed for the prototype); 316L mesh; EPDM O-rings; bought fibre module; GAC. See bom/bom.csv"


def body_parts():
    return [q for q in M.components("A1") if q["kind"] in ("made", "bought") and q["name"] != "Lanyard cord"]


def ga():
    parts = body_parts()
    work = DWG / "_views_ga"
    views = project_views(Compound(children=[q["shape"] for q in parts]), work)
    s = Sheet(project=PROJECT, title="Hollow-fibre filter straw with backflush (option A1): general arrangement, caps fitted",
              dwg_no="HWA-DWG-001", rev="P2", author="Amish Chadha", date=DATE, concept=True, scale=None, material=MAT,
              revisions=[("P1", "Preliminary GA from the TRL 3 model (HWA-CAL-001)", DATE, "AC"),
                         ("P2", "Flow at 20 C and seal tolerances after the independent STEM review", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"])
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Not to scale; lanyard cord not shown")
    f = R["flow"]
    s.add_notes("Key dimensions (mm) and data", [
        "Body 26 OD x 22 bore x 2 wall; 205 long without caps",
        f"Intake cap 0 to 22 (bayonet); seat ring 22 to 24, bore {P['SEAT_ID']:.0f}",
        "Module 24 to 150: potting 30 to 38 and 140 to 150",
        f"About {P['N_FIBRES']} fibres 0.8/0.5, active 102; {R['A_mem']:.3f} m2",
        "Clean header 150 to 156; backflush socket at 153 on +X",
        "Carbon cartridge 156 to 180: bed 16 dia x 20 (4.0 mL)",
        "Mouthpiece 180 to 205; tip 10 dia, bore 5",
        "O-rings AS568-018 in 19.3 +-0.05 glands; bore 22.0 +-0.05",
        f"Dip line at {P['Z_DIP_LINE']:.0f}: immerse no deeper",
        f"Flow at 10 kPa {f['MF 0.1 um']['revA']:.0f} to {f['MF 0.2 um']['revA']:.0f} mL/min (clean, estimate)",
        f"Mass about {R['mass_g']:.0f} g; parts USD {R['bom_total']:.2f}",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWA-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWA-DWG-001.svg, .pdf, .png")


def section():
    cutter = Pos(0, 50, 100) * Box(200, 100, 400)       # keeps +Y half: seen from -Y the cut face shows
    parts = []
    for q in body_parts():
        if q["name"] in ("Split ring, stainless 12 mm", "Mesh retaining ring"):
            continue
        try:
            h = q["shape"] & cutter
            if h.volume > 1e-3:
                parts.append(h)
        except Exception:
            pass
    work = DWG / "_views_sec"
    views = project_views(Compound(children=parts), work, center_lines=False)
    s = Sheet(project=PROJECT, title="Hollow-fibre filter straw (option A1): half section through the flow path and seals",
              dwg_no="HWA-DWG-002", rev="P2", author="Amish Chadha", date=DATE, concept=True, scale=None, material=MAT,
              revisions=[("P1", "Preliminary half section from the TRL 3 model", DATE, "AC"),
                         ("P2", "Air check restated after the independent STEM review", DATE, "AC")])
    s.add_ortho(views, ["front", "top", "right"], dims=True)
    s.add_svg(views["iso"], 276, 32, 140, 70, label="Isometric view", sublabel="Half section, front half removed; not to scale")
    s.add_notes("Flow path and clean/dirty boundaries", [
        "Dirty side: intake cap slots, mesh, bay, around the fibres",
        "Boundary 1: fibre walls (0.1 or 0.2 um rating, to decide)",
        "Boundary 2: top potting, bought pre-potted module",
        "Boundary 3: two O-rings on the module collar",
        "Clean side: lumens, header 150 to 156, carbon, mouthpiece",
        "Mouthpiece: two O-rings; joint kept above the dip line",
        "Backflush: plug out, cap on; syringe into the socket;",
        "water runs header, lumens, fibre walls, out of the intake",
        "Carbon dead-ended by the cap plug during backflush",
        "Air check: syringe to the 6 mL mark (50 kPa), plunger holds",
        "PRELIMINARY, NOT FOR FABRICATION",
    ], x=276, y=118, width=140)
    s.save(DWG / "HWA-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/HWA-DWG-002.svg, .pdf, .png")


def stl():
    out = ROOT / "cad/stl"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.stl"):
        old.unlink()
    parts = body_parts()
    export_stl(Compound(children=[q["shape"] for q in parts]), str(out / "hwa-straw-assembly.stl"), tolerance=0.05, angular_tolerance=0.3)
    for q in parts:
        if q["kind"] == "made":
            name = q["name"].lower().replace(" ", "-").replace(",", "").replace("(", "").replace(")", "")
            export_stl(q["shape"], str(out / f"hwa-{name}.stl"), tolerance=0.03, angular_tolerance=0.2)
    print("wrote", len(list(out.glob("*.stl"))), "STL files to cad/stl/")


if __name__ == "__main__":
    fns = {"ga": ga, "section": section, "stl": stl}
    for w in sys.argv[1:] or list(fns):
        fns[w]()
