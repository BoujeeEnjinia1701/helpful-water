"""Helpful Water A filter straw: concept media from the TRL 3 model (option A1, chosen by Amish on 2026-11-11).

Run from the solution folder:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process. Geometry comes from
cad/src/model.py; flow values come from HWA-CAL-001 (docs/04-calcs/sizing_results.json) and are estimates.
Uses the pieces of .kit/concept.py render_all one at a time, with a hand (not a 1.75 m person) for scale.
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

PROJECT, TITLE, DWG, DATE = "Helpful Water A: filter straw", "Hollow-fibre filter straw with backflush (option A1)", "HWA-DWG-010", "2026-11-11"
MD = ROOT / "media"
RES = ROOT / "docs/04-calcs/sizing_results.json"


def parts(context=False, small=True):
    out = []
    for q in M.components("A1"):
        if q["kind"] == "context" and not context:
            continue
        if not small and q["kind"] == "fastener":
            continue
        out.append(Part(q["name"], q["shape"], q["color"], q["bom"], tuple(q["explode"])))
    return out


def hero():
    return K._render(parts(context=True), MD / "hero.png", title=PROJECT, size=(8, 7),
                     note="Option A1 (chosen by Amish on 2026-11-11). Seen from the front right and above, 24 deg elevation. "
                          "Grey: an adult hand for scale; the straw is 205 mm long and 26 mm across")


def cutaway():
    ps = [p for p in parts() if p.name not in ("Lanyard cord", "Split ring, stainless 12 mm")]
    return K._render(K.cutaway_parts(ps), MD / "cutaway.png", azim=-90, elev=6, size=(6, 10), title=f"{PROJECT}: cutaway",
                     note="Front half removed; seen from the front, 6 deg elevation. Water rises from the intake (bottom) through "
                          "the mesh, into the fibres from outside, up their bores to the header, through the carbon and out of "
                          "the mouthpiece. The orange plug on the right closes the backflush socket on the header")


def bom_names():
    out = {}
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        n, _, rest = r["item"].partition(" ")
        out[int(n)] = rest.split(" (")[0]
    return out


def exploded():
    names = bom_names()
    seen, ps = set(), []
    for p in parts():
        if p.bom is None:
            continue
        nm = names.get(p.bom, p.name)
        ps.append(Part(nm, p.shape, p.color, p.bom, p.explode))
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, size=(9, 9), title=f"{PROJECT}: exploded view",
                     note="Seen from the front right and above, 24 deg elevation; numbers match bom/bom.csv. Module and carbon "
                          "cartridge pulled out to the right; backflush plug and tether band to the left")


def flow():
    r = json.loads(RES.read_text())
    b = r["budget200_mf02"]
    stages = [("Source water at the intake", "0 kPa"),
              ("Intake cap and 250 um mesh", f"{b['intake'] * 1000:.0f} Pa"),
              ("Hollow fibres, outside to inside", f"{b['membrane']:.1f} kPa"),
              ("Fibre bores to the clean header", f"{b['lumen']:.1f} kPa"),
              ("Carbon bed, screen and pad", f"{b['carbon'] + b['pad'] + b['grids'] + b['screen']:.1f} kPa"),
              ("Mouthpiece, 5 mm bore", f"{b['mouth'] * 1000:.0f} Pa")]
    return K.flow_diagram(stages, MD / "flow.png",
                          f"{PROJECT}: water path and suction used at 200 mL/min with a 0.2 um fibre (estimates, HWA-CAL-001); "
                          f"lifting the water 155 mm to the mouth adds {b['lift']:.1f} kPa; the backflush socket on the header is plugged while drinking", "")


def web():
    ps = [p for p in parts() if p.name != "Lanyard cord"]
    return K.export_web_model(ps, "media", title=f"{PROJECT}: {TITLE}")


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    r = json.loads(RES.read_text())
    ps = [p for p in parts() if p.name not in ("Lanyard cord", "Split ring, stainless 12 mm")]
    shown = ps + [p for p in parts(context=True) if p.name == "Hand (scale)"]
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig")["iso"]
    f = r["flow"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P2", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Detailed TRL 3 model for concept communication",
              revisions=[("P1", "Concept sheet from the TRL 3 model", DATE, "AC"),
                         ("P2", "Flows at 20 C after the independent STEM review", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 118, label="Isometric view", sublabel="Not to scale; grey is an adult hand for scale")
    s.add_notes("Key figures (estimates, HWA-CAL-001)", [
        f"205 mm long, 26 mm body, {r['across_port_mm']:.1f} mm across the port; {r['mass_g']:.0f} g",
        f"About {M.P['N_FIBRES']} fibres 0.8/0.5 mm, {r['A_mem']:.3f} m2, outside-in",
        f"Flow at 10 kPa, clean: {f['MF 0.1 um']['revA']:.0f} (0.1 um) to {f['MF 0.2 um']['revA']:.0f} (0.2 um) mL/min",
        f"Child at 5 kPa: {f['MF 0.1 um']['child']:.0f} to {f['MF 0.2 um']['child']:.0f} mL/min",
        f"Carbon 16 x 20 mm, {r['m_bed_g'][0]:.1f} g, contact {r['EBCT_s']['200']:.1f} s at 200 mL/min",
        "Backflush socket on the clean header; carbon bypassed",
        f"Prototype parts USD {r['bom_total']:.2f} (target USD 25)",
        "Reduces bacteria and protozoa by design; no virus claim"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w_ in sys.argv[1:] or list(fns):
        print(w_, "->", fns[w_]())
