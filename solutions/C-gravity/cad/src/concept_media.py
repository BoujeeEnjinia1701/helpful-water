"""Helpful Water C concept media from the TRL 3 model (option C1, the two-bucket hollow-fibre filter carried to the
drawing, BOM and build plan; the concept choice was made by Amish on 2026-11-11).

Run from the solution folder:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry comes from
cad/src/model.py; flow values come from HWC-CAL-001 (docs/04-calcs/sizing_results.json) and are estimates.
Scale: a 1.75 m person beside the unit (household scale). CONCEPT, NOT FOR FABRICATION.

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

PROJECT, TITLE, DWG, DATE = "Helpful Water C", "C1 two-bucket hollow-fibre household gravity filter", "HWC-DWG-010", "2026-11-11"
MD = ROOT / "media"


def res():
    return json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())


def parts(context=True, small=True):
    out = []
    for q in M.components("C1", context=context):
        if q["kind"] == "context" and not context:
            continue
        if not small and q["kind"] == "fastener":
            continue
        alpha = 0.55 if q["name"].startswith("Module shell") else 1.0
        out.append(Part(q["name"], q["shape"], q["color"], q["bom"], tuple(q["explode"]), alpha))
    return out


def hero():
    return K._render(K.with_scale_figure(parts()), MD / "hero.png", title=f"{PROJECT}: household gravity filter", size=(8, 7),
                     note="C1: blue raw bucket on the top shelf, hollow-fibre module on the front leg, white clean bucket with a tap "
                          "below. Seen from the front right and above, 18 deg elevation. Grey figure: 1.75 m person for scale",
                     elev=18, azim=-55)


def cutaway():
    """Each group is cut through its own axis (raw bucket at y = 0, module at its axis, clean bucket at its centre),
    front half removed, so the settling zone, the fibre bundle and the clean inlet all show."""
    from build123d import Box, Pos
    ps = [p for p in parts(context=False, small=False) if not p.name.startswith(("Diagonal", "Leg back", "Foot", "Lower rail", "Label"))]
    out = []
    for p in ps:
        n = p.name
        if n.startswith(("Module", "Fibre", "Potting", "P-clip", "Clean-side tee", "Backflush", "Pinch")):
            y0 = M.MOD_Y
        elif n.startswith(("Leg front", "Raw hose", "Clean hose", "Clean inlet", "Vent", "Insect")):
            y0 = -1e4
        elif n.startswith(("Clean", "Drum tap", "Tap", "Lower shelf")):
            y0 = M.P["CLEAN_Y"]
        else:
            y0 = 0.0
        try:
            sh = p.shape & Pos(0, y0 + 2000, 0) * Box(6000, 4000, 6000)
            if sh.volume > 1e-3:
                out.append(Part(n, sh, p.color, p.bom, p.explode, 1.0))
        except Exception:
            out.append(p)
    return K._render(out, MD / "cutaway.png", azim=-90, elev=8, size=(7, 9),
                     title=f"{PROJECT}: cutaway of the C1 filter",
                     note="Each part cut through its own axis, front half removed; seen from the front, 8 deg elevation. Raw "
                          "water settles below the strainer outlet, runs through the valve and hose to the top of the module, "
                          "passes the fibre walls from outside in, and rises from the tee into the closed clean bucket")


def bom_names():
    out = {}
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        n, _, rest = r["item"].partition(" ")
        out[int(n)] = rest.split(" (")[0]
    return out


def exploded():
    names = bom_names()
    seen, ps = set(), []
    for p in parts(context=False, small=False):
        if p.bom is None or p.bom in (25, 26, 27):
            continue
        label = names.get(p.bom, p.name) if p.bom not in seen else ""
        seen.add(p.bom)
        ps.append(Part(label or " ", p.shape, p.color, p.bom if label else None, p.explode, p.alpha))
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, size=(9, 11), elev=14, azim=-58,
                     title=f"{PROJECT}: exploded view of the C1 water path",
                     note="Seen from the front right, 14 deg elevation; numbers match bom/bom.csv; the timber stand "
                          "(items 25 to 30) is left out for clarity")


def flow():
    r = res()
    c, f = r["c1"]["clean"], r["c1"]["fouled"]
    st = c["stages_at_mean"]
    return K.flow_diagram(
        [("Cloth prefilter, settle 1 h; dose D, 30 min", f"{r['raw']['batch_l']:.1f} L batch"),
         ("Gravity head, raw bucket to clean inlet", f"{r['head']['head_kpa'][0]:.1f} to {r['head']['head_kpa'][1]:.1f} kPa"),
         ("Strainer, valve, hoses, fittings", f"{(st['hose_kpa'] + st['fittings_kpa']) * 1000:.0f} Pa"),
         ("Hollow fibres, outside-in, 0.1 um", f"{st['membrane_kpa']:.1f} kPa"),
         ("Lumens and header", f"{st['lumen_kpa'] * 1000:.0f} Pa"),
         ("Closed clean bucket with tap", f"{c['q_mean_lph']:.0f} L/h clean, {f['q_mean_lph']:.0f} fouled (est.)")],
        MD / "flow.png", f"{PROJECT}: water path through C1 and the pressure each stage takes at the mean head, clean module "
                         "(estimates, HWC-CAL-001); 45 L a day in about 1.5 to 2.8 h of filtering; viruses are not removed "
                         "unless chlorine (solution D) is dosed in the raw bucket first", "")


def web():
    return K.export_web_model(parts(context=False, small=False), "media", title=f"{PROJECT}: {TITLE}")


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    r = res()
    keep = ("Raw bucket", "Raw lid", "Fill cover", "Clean bucket", "Clean lid", "Leg", "Foot", "Upper shelf", "Lower shelf",
            "Lower rail", "Diagonal", "Module shell", "Module top", "Module header", "Raw hose", "Clean hose", "Ball valve",
            "Drum tap", "Dosing port cap")
    ps = [p for p in parts(context=False, small=False) if p.name.startswith(keep)]
    shown = K.with_scale_figure(ps)
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P1", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Detailed TRL 3 model for concept communication",
              revisions=[("P1", "Concept sheet from the TRL 3 model", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 113, label="Isometric view", sublabel="Not to scale; figure is a 1.75 m person")
    s.add_notes("Key figures (estimates, HWC-CAL-001)", [
        f"Stand {r['c1_size_mm']['width']:.0f} x {r['c1_size_mm']['depth']:.0f} mm, {r['c1_size_mm']['height']:.0f} mm tall",
        "Two 20 L food-grade buckets; raw rim at 1.27 m",
        f"Head {r['head']['head_m'][0]:.2f} to {r['head']['head_m'][1]:.2f} m; module 0.1 um, {r['area_m2']:.2f} m2",
        f"Flow {r['c1']['clean']['q_mean_lph']:.0f} L/h clean, {r['c1']['fouled']['q_mean_lph']:.0f} L/h fouled",
        f"45 L a day (5 people) in {r['c1']['clean']['hours_per_day']:.1f} to {r['c1']['fouled']['hours_per_day']:.1f} h",
        "Designed to reduce bacteria and protozoa; untested",
        "No virus claim: dose chlorine (solution D) first",
        f"Parts USD {r['bom_usd']:.0f} against a USD 60 target"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w_ in sys.argv[1:] or list(fns):
        print(w_, "->", fns[w_]())
