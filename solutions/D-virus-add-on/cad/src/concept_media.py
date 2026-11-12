"""Helpful Water D concept media from the TRL 3 model (option D1, the tablet dose cap carried to the drawing, BOM and
build plan; the concept choice is proposed, awaiting Amish).

Run from the solution folder:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry comes from
cad/src/model.py; dose, residual and CT values come from HWD-CAL-001 (docs/04-calcs/sizing_results.json) and are
estimates. Scale: a hand holding the 1 L PET bottle (context parts). CONCEPT, NOT FOR FABRICATION.

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

PROJECT, TITLE, DWG, DATE = "Helpful Water D", "D1 tablet dose cap on a 1 L PET bottle", "HWD-DWG-010", "2026-11-11"
MD = ROOT / "media"


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())["results"]


def parts(context=True, small=True):
    out = []
    for q in M.components("D1", context=context):
        if q["kind"] == "context" and not context:
            continue
        if not small and q["kind"] == "fastener":
            continue
        col = "#9C9C9E" if "Hand" in q["name"] else ("#DCE7EA" if "PET" in q["name"] else q["color"])
        alpha = 0.55 if "PET" in q["name"] else 1.0
        out.append(Part(q["name"], q["shape"], col, q["bom"], tuple(q["explode"]), alpha))
    return out


def hero():
    return K._render(parts(), MD / "hero.png", title=f"{PROJECT}: chlorine add-on for viruses", size=(7, 8),
                     note="D1 tablet dose cap on a 1 L PET bottle (28 mm PCO 1881 neck). Seen from the front right and above, "
                          "15 deg elevation. Grey: a hand and the bottle, for scale. Co-treatment: chlorinate, wait, then filter",
                     elev=15, azim=-50)


def cutaway():
    ps = [p for p in parts(context=False, small=False)]
    return K._render(K.cutaway_parts(ps), MD / "cutaway.png", azim=-90, elev=8, size=(7, 7),
                     title=f"{PROJECT}: cutaway of the D1 dose cap",
                     note="Front half removed; seen from the front, 8 deg elevation. Turned over, bottle water floods the well through "
                          "the floor slots and dissolves the tablet; the ball timer (right) runs about 45 min once flipped (at least 30 up to 40 C)")


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
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, size=(9, 9), elev=14, azim=-40,
                     title=f"{PROJECT}: exploded view of the D1 dose cap",
                     note="Seen from the front right, 14 deg elevation; numbers match bom/bom.csv; cap parts pulled apart along the axis, timer window outward")


def flow():
    r = res()
    s = r["scenarios"]["clear"]
    return K.flow_diagram(
        [("Raw water, 1 L or 20 L", "under 50 NTU"),
         ("One matched tablet", "2.0 mg/L (est.)"),
         ("Shake, flip timer", f"{s['c30']:.1f} mg/L at 30 min"),
         ("Wait 30 to 120 min", f"CT {s['ct30_epa']:.0f} mg min/L"),
         ("Filter A, B or C", "cysts, bacteria, taste"),
         ("Drink or store", "no residual after carbon")],
        MD / "flow.png", f"{PROJECT}: dose, wait, then filter (estimates for clear water, HWD-CAL-001; "
                         "4-log virus CT at 5 C is 8 mg min/L, US EPA; no virus claim until tested)", "")


def web():
    return K.export_web_model(parts(context=False), "media", title=f"{PROJECT}: {TITLE}")


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    r = res()
    ps = [p for p in parts(context=False, small=False) if p.name.startswith(("Dose cap", "Well plug", "Timer window", "Tether"))]
    shown = ps + [p for p in parts() if p.name.startswith("PET")]
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P1", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Detailed TRL 3 model for concept communication",
              revisions=[("P1", "Concept sheet from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 113, label="Isometric view", sublabel="Not to scale; with the 1 L PET bottle")
    sz = r["d1_size_mm"]
    s.add_notes("Key figures (estimates, HWD-CAL-001)", [
        f"Cap {sz['x']:.0f} x {sz['y']:.0f} x {sz['z']:.0f} mm, about {r['mass_g']['D1']:.0f} g",
        "Fits 28 mm PCO 1881 necks; C bucket port proposed",
        "One NaDCC tablet: 3.5 mg per 1 L or 67 mg per 20 L",
        f"About 2.0 mg/L; {r['scenarios']['clear']['c30']:.1f} mg/L at 30 min (clear)",
        f"Ball timer about {r['timer']['t_nominal_min']:.0f} min; cold water: 2 or 3 runs",
        "Chlorinate, wait, then filter with A, B or C",
        f"Parts USD {r['cost']['bom_usd']:.2f} against a USD 10 target"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w_ in sys.argv[1:] or list(fns):
        print(w_, "->", fns[w_]())
