"""Helpful Water B concept media from the TRL 3 model (option B1, the squeeze cartridge carried to the drawing, BOM
and build plan; the concept choice is proposed, awaiting Amish).

Run from the solution folder:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry comes from
cad/src/model.py; flow values come from HWB-CAL-001 (docs/04-calcs/sizing_results.json) and are estimates.
Scale: a hand holding the 1 L PET bottle (context parts), not the 1.75 m person. CONCEPT, NOT FOR FABRICATION.

Licence: Apache-2.0 (software used with the hardware, Helpful Engineering licensing guide).
"""
import csv
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
import model as M  # noqa: E402

PROJECT, TITLE, DWG, DATE = "Helpful Water B", "B1 squeeze cartridge on a 1 L PET bottle", "HWB-DWG-010", "2026-11-11"
MD = ROOT / "media"


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())


def parts(context=True, small=True):
    out = []
    for q in M.components("B1", context=context):
        if q["kind"] == "context" and not context:
            continue
        if not small and q["kind"] == "fastener":
            continue
        col = "#9C9C9E" if "Hand" in q["name"] else ("#DCE7EA" if "PET" in q["name"] else q["color"])
        alpha = 0.55 if "PET" in q["name"] else 1.0
        out.append(Part(q["name"], q["shape"], col, q["bom"], tuple(q["explode"]), alpha))
    return out


def hero():
    return K._render(parts(), MD / "hero.png", title=f"{PROJECT}: bottle cartridge", size=(7, 8),
                     note="B1 squeeze cartridge screwed onto a 1 L PET bottle (28 mm PCO 1881 neck). Seen from the front right "
                          "and above, 15 deg elevation. Grey: a hand and the bottle, for scale", elev=15, azim=-55)


def cutaway():
    ps = [p for p in parts(context=False, small=False)]
    return K._render(K.cutaway_parts(ps), MD / "cutaway.png", azim=-90, elev=10, size=(6, 8),
                     title=f"{PROJECT}: cutaway of the B1 cartridge",
                     note="Front half removed; seen from the front, 10 deg elevation. Bottle water rises through the mesh and the "
                          "carbon capsule, passes the fibre walls from outside in, and leaves through the header and spout")


def bom_names():
    out = {}
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        n, _, rest = r["item"].partition(" ")
        out[int(n)] = rest.split(" (")[0]
    return out


def exploded():
    names = bom_names()
    seen, ps = set(), []
    for p in parts(context=False, small=True):
        if p.bom is None:
            continue
        label = names.get(p.bom, p.name) if p.bom not in seen else ""
        seen.add(p.bom)
        ps.append(Part(label or " ", p.shape, p.color, p.bom if label else None, p.explode))
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, size=(8, 10), elev=12, azim=-60,
                     title=f"{PROJECT}: exploded view of the B1 cartridge",
                     note="Seen from the front right, 12 deg elevation; numbers match bom/bom.csv; parts pulled apart along the axis")


def flow():
    r = res()
    a = r["b1"]["adult"]["clean"]
    return K.flow_diagram(
        [("Hand squeeze on the bottle", f"{r['squeeze_kpa']['adult']:.0f} kPa (est.)"),
         ("316L mesh, 150 um: grit", f"{a['mesh_kpa'] * 1000:.0f} Pa"),
         ("Carbon capsule (dirty side): taste target", f"{a['bed_kpa']:.2f} kPa"),
         ("Hollow fibres, outside-in, 0.1 um", f"{a['membrane_kpa']:.1f} kPa"),
         ("Lumens, header, spout, valve", f"{a['lumen_kpa'] + a['outlet_kpa']:.2f} kPa"),
         ("To the mouth or a cup", f"{a['q_ml_min']:.0f} mL/min (est.)")],
        MD / "flow.png", f"{PROJECT}: water path through the B1 cartridge and pressure used by each stage at an adult squeeze, "
                         "clean module (estimates, HWB-CAL-001); backflush runs the other way with a 60 mL syringe; viruses are not removed", "")


def web():
    return K.export_web_model(parts(context=False), "media", title=f"{PROJECT}: {TITLE}")


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    r = res()
    ps = [p for p in parts(context=False, small=False) if p.name.startswith(("Neck collar", "Housing", "Spout", "Push", "Dust"))]
    shown = ps + [p for p in parts() if p.name.startswith("PET")]
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P1", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Detailed TRL 3 model for concept communication",
              revisions=[("P1", "Concept sheet from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 113, label="Isometric view", sublabel="Not to scale; with the 1 L PET bottle")
    s.add_notes("Key figures (estimates, HWB-CAL-001)", [
        f"Cartridge {r['b1_size_mm']['length']:.0f} mm long, 44 mm across, about {r['mass_b1_dry_g']:.0f} g dry",
        "Fits 28 mm PCO 1881 and 1810 necks; 38 mm by adapter",
        f"Hollow fibre 0.1 um, {r['area_m2']['B1']:.2f} m2; carbon capsule {r['carbon']['mass_g']:.0f} g",
        f"Flow, clean: {r['b1']['adult']['clean']['q_ml_min']:.0f} mL/min adult, {r['b1']['child_10_11_weak']['clean']['q_ml_min']:.0f} weak child",
        "Designed to reduce bacteria and protozoa; untested",
        "No virus claim: co-treat with chlorine (solution D)",
        f"Parts USD {r['bom_usd']:.2f} against a USD 20 target"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w_ in sys.argv[1:] or list(fns):
        print(w_, "->", fns[w_]())
