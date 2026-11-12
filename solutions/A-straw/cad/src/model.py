"""Helpful Water A: filter straw. Parametric model (kit 1.9 interface, STANDARDS section 24), detail level D3.

Run from the solution folder:  python .kit/cad_check.py --export
Every main dimension is in PARAMS; docs/04-calcs/sizing.py (HWA-CAL-001) and stem_check.py (HWA-STM-001) read it.

Axes: Z along the straw from the intake face (z = 0) to the mouthpiece tip (z = 205 mm); +X is the side of the
backflush port. Envelope from the Rev A component specification (Helpful Engineering, 2026-10-14): 205 mm long,
26 mm OD, 22 mm bore, 2 mm wall.

Options (HWA-OPT-001; chosen by Amish on 2026-11-11):
  A1  Hollow-fibre straw (Rev A, made constructable): intake cap with a captive 316L mesh, a bought pre-potted
      outside-in hollow-fibre module sealed by two O-rings, a clean header with a capped backflush socket that
      bypasses the carbon, a removable carbon cartridge and a bayonet mouthpiece.
  A2  Ceramic tube straw: a sintered ceramic microfiltration tube hangs from a sealed head; the dirty lower shell
      twists off so the user can scrub the tube without opening the clean side. Dropped: flow at suction fails.
  A3  Copper and charcoal straw (viability shortlist): rolled copper mesh then a long carbon bed. Dropped: copper
      contact time and charcoal do not reduce bacteria or protozoa in a sip.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from build123d import Box, Cone, Cylinder, Pos, Rot

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import cad_parts as cp  # noqa: E402
from cad_parts import part  # noqa: E402
import straw_parts as S  # noqa: E402

TITLE = "Helpful Water A: filter straw"
OPTIONS = {"A1": "Hollow-fibre straw with backflush", "A2": "Ceramic tube straw, scrub to clean",
           "A3": "Copper and charcoal straw (dropped)"}
PRINCIPLES = {
    "A1": "Suction draws water through a 316L mesh, then from outside to inside through about 220 hollow fibres into a "
          "clean header and a small carbon bed; a capped socket on the header lets clean water be pushed back through "
          "the fibres without passing the carbon.",
    "A2": "Suction draws water through the wall of a sintered ceramic tube into its bore and a carbon bed; the dirty "
          "lower shell twists off so the tube can be scrubbed. Dropped: about 10 mL/min at suction.",
    "A3": "Water passes rolled copper mesh, then a long charcoal bed. Dropped: seconds of copper contact and charcoal do "
          "not reduce bacteria or protozoa.",
}
CHOSEN = "A1"   # carried to the drawing, BOM and build plan; the concept choice was made by Amish on 2026-11-11 (HWA-DEC-001)
_HAND = dict(el=18, az=-58, scale="none", keep_context=True)
OPTION_VIEWS = {"A1": dict(_HAND), "A2": dict(_HAND), "A3": dict(_HAND)}
# O-rings are squeezed against their bores by design (24 % squeeze); the squeeze shows as overlap
ALLOWED_CONTACTS = [("O-ring", "")]

PARAMS = {
    # envelope (Rev A section 03)
    "L": 205.0, "OD": 26.0, "ID": 22.0, "WALL": 2.0,
    # axial stations (mm from the intake face)
    "Z_CAP_TOP": 12.0, "Z_SPIGOT_TOP": 22.0, "Z_SEAT": (22.0, 24.0), "SEAT_ID": 17.0,
    "Z_MODULE": (24.0, 150.0), "Z_BOT_POT": (30.0, 38.0), "Z_TOP_POT": (140.0, 150.0), "Z_COLLAR": (135.0, 150.0),
    "Z_HEADER": (150.0, 156.0), "Z_PORT": 153.0, "Z_CART": (156.0, 180.0), "Z_BED": (158.4, 178.4),
    "Z_HOUSING": (12.0, 190.0), "Z_MOUTH": (180.0, 205.0), "Z_DIP_LINE": 110.0,
    # membrane (Rev A section 04 item 4, made to fill the bore: HWA-DEC-001 F2)
    "FIBRE_OD": 0.8, "FIBRE_ID": 0.5, "N_FIBRES": 220, "BUNDLE_D": 17.2, "CAGE": (17.8, 21.0),
    "ACTIVE_L": 102.0,           # bundle between the potting faces, 38 to 140 mm
    # carbon cartridge (Rev A item 7)
    "BED_D": 16.0, "BED_H": 20.0, "GAC_DENSITY": 0.49,   # g/mL, 12 x 40 coconut shell GAC (Envirosupply sheet)
    # seals: AS568-018 (18.77 x 1.78 mm), EPDM, in male glands with the floor at 19.3 mm (HWA-DEC-001 F1)
    "ORING_ID": 18.77, "ORING_CS": 1.78, "GLAND_FLOOR_D": 19.3, "GLAND_W": 2.4, "SPIGOT_OD": 21.8,
    # bayonets
    "LUG_W": 4.0, "LUG_H": 1.1, "LUG_R": (10.9, 11.6), "BAY_GROOVE_R": 11.8, "BAY_SLOT_W": 4.6,
    # mesh prefilter (Rev A item 2): 316L, 250 um aperture baseline
    "MESH_D": 17.0, "MESH_T": 0.4, "MESH_UM": 250,
    # backflush socket (luer-slip, shortened) on +X at the header
    "PORT_R": (11.0, 15.0), "PORT_BOSS_D": 8.0, "PORT_HOLE": (4.3, 3.9), "PORT_PASS_D": 2.0,
    # mouthpiece (Rev A item 9): bore 5 mm, contact diameter 10 mm
    "MOUTH_BORE": 5.0, "MOUTH_TIP_D": 10.0,
    # option A2 ceramic tube
    "CER_OD": 17.0, "CER_ID": 9.0, "Z_CER": (28.0, 146.0),
    # option A3 copper and charcoal
    "Z_CU": (30.0, 90.0), "Z_A3_BED": (94.4, 178.4), "A3_BED_D": 17.2,
}
P = PARAMS
R_OUT, R_IN = P["OD"] / 2, P["ID"] / 2
R_SP = P["SPIGOT_OD"] / 2
R_FLOOR = P["GLAND_FLOOR_D"] / 2
CS = P["ORING_CS"]
GW = P["GLAND_W"]

# colours for the renders (materials come from cad_parts.MATERIALS; colours are overridden for polypropylene parts)
C_HOUSING, C_CAP, C_MOUTH = "#2F7F86", "#1F5F66", "#E9EEF0"
C_FIBRE, C_POT, C_CAGE = "#F4F2EC", "#D8C9A0", "#CFD6D9"


def _p(name, shape, mat, kind="made", bom=None, explode=(0, 0, 0), color=None, group="shell", note=""):
    return part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode, color=color, note=note)


def _male_gland(solid, z_mid):
    return solid - S.groove_cut(R_FLOOR, R_SP, z_mid - GW / 2, z_mid + GW / 2)


def _oring(name, z, bom, explode=(0, 0, 0)):
    return _p(name, S.o_ring(P["GLAND_FLOOR_D"], CS, z), "epdm", "bought", bom, explode)


# ---------------------------------------------------------------------------------------------------------
# shared parts
# ---------------------------------------------------------------------------------------------------------
def intake_cap(bom=1, explode=(0, 0, -60)):
    """Intake cap: head 0 to 12 mm with eight side slots and six bottom holes; spigot 12 to 22 mm into the bore with
    two bayonet lugs, a grit O-ring gland and a counterbore for the captive mesh disc."""
    zt, zs = P["Z_CAP_TOP"], P["Z_SPIGOT_TOP"]
    prof = [(0, 0), (R_OUT, 0), (R_OUT, zt), (R_SP, zt), (R_SP, zs), (8.5, zs), (8.5, 20.0), (8.0, 20.0), (8.0, zt),
            (9.0, zt), (9.0, 2.0), (0, 2.0)]
    s = S.revolved(prof)
    s = s - S.radial_slots(10.5, R_OUT + 0.2, 8, 2.5, 3.0, 10.0, phase=22.5)
    s = s - S.hole_ring(5.0, 6, 2.5, -0.1, 2.1)
    s = _male_gland(s, 18.0)
    s = s + S.lugs(P["LUG_R"][0] - 0.05, P["LUG_R"][1], 13.2, 13.2 + P["LUG_H"], P["LUG_W"])
    return [_p("Intake cap", s, "hdpe_natural", "made", bom, explode, C_CAP),
            _oring("O-ring, intake cap (grit seal)", 18.0, 6, explode)]


def mesh_and_ring(bom_mesh=2, bom_ring=3):
    return [_p("Prefilter mesh disc, 316L 250 um", S.mesh_disc(P["MESH_D"], P["MESH_T"], 20.0), "stainless", "bought", bom_mesh, (0, 0, -35)),
            _p("Mesh retaining ring", S.tube(6.5, 8.5, 20.4, 22.0), "hdpe_natural", "made", bom_ring, (0, 0, -30), C_CAP)]


def housing_shell(z0, z1, seat=True, bay_bottom=True, bay_top=True, port=False, name="Housing body", bom=4,
                  explode=(0, 0, 0), dip=True):
    prof = [(R_IN, z0), (R_OUT, z0), (R_OUT, z1), (R_IN, z1)]
    s = S.revolved(prof)
    if seat:
        s = s + S.tube(P["SEAT_ID"] / 2, R_IN + 0.01, *P["Z_SEAT"])
    gr, w = P["BAY_GROOVE_R"], P["BAY_SLOT_W"]
    if bay_bottom:
        s = s - S.bayonet_cutter(R_IN, gr, z0 + 1.0, z0 + 2.5, z0, w)
    if bay_top:
        s = s - S.bayonet_cutter(R_IN, gr, z1 - 2.0, z1 - 0.5, z1, w)
    if dip:   # dip line: a shallow V groove round the outside
        zd = P["Z_DIP_LINE"]
        s = s - S.revolved([(R_OUT - 0.4, zd), (R_OUT + 0.1, zd - 0.6), (R_OUT + 0.1, zd + 0.6)])
    if port:
        zp, (r0, r1) = P["Z_PORT"], P["PORT_R"]
        boss = Pos(0, 0, zp) * Rot(0, 90, 0) * Pos(0, 0, (r0 + r1) / 2) * Cylinder(P["PORT_BOSS_D"] / 2, r1 - r0)
        s = s + cp.break_edges(boss, 0.6)
        d0, d1 = P["PORT_HOLE"]
        sock = Pos(0, 0, zp) * Rot(0, 90, 0) * Pos(0, 0, r1 - 2.5) * Cone(d1 / 2, d0 / 2, 5.0)
        pas = Pos(0, 0, zp) * Rot(0, 90, 0) * Pos(0, 0, (R_IN - 0.5 + r1) / 2) * Cylinder(P["PORT_PASS_D"] / 2, r1 - R_IN + 1)
        s = s - sock - pas
    return _p(name, s, "hdpe_natural", "made", bom, explode, C_HOUSING)


def carbon_cartridge(z0=None, z1=None, bed=None, bed_d=None, legs=True, bom=(7, 8, 9, 10), explode=(35, 0, 45), tag=""):
    """Carbon cartridge: cup with an inlet grid, a 316L inlet screen, the granular bed, a fines pad on top; one O-ring
    seals cup to bore (clean to clean); three legs stand on the module collar and keep the header open."""
    z0, z1 = z0 or P["Z_CART"][0], z1 or P["Z_CART"][1]
    b0, b1 = bed or P["Z_BED"]
    rb = (bed_d or P["BED_D"]) / 2
    body = S.revolved([(rb, z0 + 2.0), (rb, z1), (R_SP, z1), (R_SP, z0), (0, z0), (0, z0 + 2.0)])
    body = body - S.hole_ring(4.5, 6, 2.0, z0 - 0.1, z0 + 2.1) - Pos(0, 0, z0 + 1.0) * Cylinder(1.25, 2.2)
    body = _male_gland(body, z0 + 6.0)
    if legs:
        for a in (60, 180, 300):
            body = body + Rot(0, 0, a) * Pos(10.0, 0, z0 - 3.0) * Box(1.8, 3.0, 6.0)
    screen = S.mesh_disc(2 * rb, 0.4, z0 + 2.0, pitch=1.3, hole=0.7)
    bedsolid = cp.break_edges(S.tube(0, rb - 0.001, z0 + 2.4, b1), 0.4)
    pad = S.revolved([(0, b1), (rb - 0.001, b1), (rb - 0.001, z1), (0, z1)])
    pad = pad - S.hole_ring(rb * 0.55, 8, 0.6, z1 - 0.3, z1 + 0.1)
    ex, ey, ez = explode
    return [_p(f"Carbon cartridge body{tag}", body, "hdpe_natural", "made", bom[0], explode, "#3D4C52"),
            _p(f"Carbon inlet screen, 316L{tag}", screen, "stainless", "bought", bom[1], (ex, ey, ez - 25)),
            _p(f"Activated carbon bed, coconut GAC{tag}", bedsolid, "matte_black", "bought", bom[2], (ex, ey, ez + 25), "#202326"),
            _p(f"Carbon fines pad{tag}", pad, "canvas", "bought", bom[3], (ex, ey, ez + 50), "#ECE7DA"),
            _oring(f"O-ring, carbon cartridge{tag}", z0 + 6.0, 6, explode)]


def mouthpiece(bom=11, explode=(0, 0, 40)):
    """Mouthpiece: spigot 180 to 190 mm with an outlet grid, two O-ring glands and two bayonet lugs; tapered head to
    a 10 mm tip with a 5 mm bore."""
    z0, z1 = P["Z_MOUTH"]
    zs = P["Z_HOUSING"][1]
    rt, rb_ = P["MOUTH_TIP_D"] / 2, P["MOUTH_BORE"] / 2
    prof = [(rb_, z0 + 1.5), (7.0, z0 + 1.5), (7.0, zs), (rb_, zs + 1.0), (rb_, z1), (rt, z1), (rt, z1 - 4.0),
            (12.5, zs + 3.0), (R_OUT, zs + 1.0), (R_OUT, zs), (R_SP, zs), (R_SP, z0), (0.0, z0), (0.0, z0 + 1.5)]
    s = S.revolved(prof)
    s = s - S.hole_ring(4.2, 6, 2.0, z0 - 0.1, z0 + 1.6) - Pos(0, 0, z0 + 0.75) * Cylinder(1.0, 1.7)
    s = _male_gland(s, z0 + 3.0)
    s = _male_gland(s, z0 + 6.0)
    s = s + S.lugs(P["LUG_R"][0] - 0.05, P["LUG_R"][1], zs - 1.8, zs - 1.8 + P["LUG_H"], P["LUG_W"])
    s = s - S.radial_slots(R_OUT - 0.5, R_OUT + 0.5, 12, 1.2, zs + 0.2, zs + 0.9)   # grip ribs on the collar
    return [_p("Mouthpiece", s, "hdpe_natural", "made", bom, explode, C_MOUTH),
            _oring("O-ring, mouthpiece inner", z0 + 3.0, 6, explode),
            _oring("O-ring, mouthpiece outer", z0 + 6.0, 6, explode)]


def mouth_cap(bom=12, explode=(0, 0, 70)):
    z1 = P["Z_MOUTH"][1]
    rt = P["MOUTH_TIP_D"] / 2
    s = S.revolved([(0, z1 - 2.0), (2.45, z1 - 2.0), (2.45, z1 + 1.0), (rt, z1 + 1.0), (rt, z1 - 4.0), (rt + 1.6, z1 - 4.0),
                    (rt + 1.6, z1 + 3.0), (0, z1 + 3.0)])
    eye = Pos(0, 0, z1 + 5.5) * Rot(90, 0, 0) * (Cylinder(3.2, 2.0) - Cylinder(1.6, 2.2))
    s = s + eye
    return [_p("Mouthpiece cap", s, "hdpe_natural", "made", bom, explode, C_CAP)]


def intake_cover(bom=14, explode=(0, 0, -95)):
    s = S.revolved([(0, -2.0), (R_OUT + 1.2, -2.0), (R_OUT + 1.2, 9.0), (R_OUT, 9.0), (R_OUT, 0.0), (0, 0.0)])
    s = s - S.radial_slots(R_OUT + 0.9, R_OUT + 1.5, 16, 0.8, 1.0, 8.0)
    return [_p("Intake cover", s, "epdm", "made", bom, explode, "#2B3A3D")]


def lanyard(bom_ring=15, bom_cord=16, explode=(0, 0, 100)):
    z1 = P["Z_MOUTH"][1]
    ring = Pos(-0.5, 0, z1 + 11.5) * Rot(0, 90, 0) * S.split_ring(12.0, 1.0)
    pts = [(0, 0, z1 + 18.5), (0, -6, z1 + 35.0), (0, -4, z1 + 65.0), (0, 4, z1 + 65.0), (0, 6, z1 + 35.0), (0, 0, z1 + 18.5)]
    cord = S.cord_loop(pts, 2.0)
    return [_p("Split ring, stainless 12 mm", ring, "stainless", "fastener", bom_ring, explode),
            _p("Lanyard cord", cord, "rope", "bought", bom_cord, explode)]


# ---------------------------------------------------------------------------------------------------------
# option A1: hollow-fibre straw with backflush
# ---------------------------------------------------------------------------------------------------------
def membrane_module(bom=5, explode=(35, 0, 0)):
    """Bought pre-potted module: perforated cage, bottom potting (closes the fibre ends), fibre bundle, top potting
    (open lumens facing the header) and the header collar with two O-ring glands (machined if not supplied)."""
    m0, m1 = P["Z_MODULE"]
    rc0, rc1 = P["CAGE"][0] / 2, P["CAGE"][1] / 2
    cage = S.slotted_cage(rc0, rc1, m0, P["Z_COLLAR"][0], n=6, win_w=4.0, win_h=16.0, rows=5, margin=4.0)
    cage = cage - S.radial_slots(rc0 - 0.3, rc1 + 0.3, 6, 3.0, m0 - 0.1, m0 + 4.0)   # bottom feet between slots
    bpot = S.potted_block(P["CAGE"][0], *P["Z_BOT_POT"])
    bpot = cp.break_edges(bpot, 0.4)
    bundle = S.fibre_bundle(P["BUNDLE_D"], P["Z_BOT_POT"][1], P["Z_TOP_POT"][0], n_lobes=56)
    rp = 8.65
    tpot = S.potted_block(2 * rp, *P["Z_TOP_POT"], open_face="top")
    c0, c1 = P["Z_COLLAR"]
    collar = S.revolved([(rp, c0 + 5.0), (rp, c1), (R_SP, c1), (R_SP, c0), (rc0, c0), (rc0, c0 + 5.0)])
    collar = _male_gland(collar, 141.5)
    collar = _male_gland(collar, 145.5)
    return [_p("Module cage (perforated shell)", cage, "hdpe_natural", "bought", bom, explode, C_CAGE),
            _p("Bottom potting block (closes fibre ends)", bpot, "hdpe_natural", "bought", bom, explode, C_POT),
            _p("Hollow-fibre bundle, about 220 fibres", bundle, "insulated_white", "bought", bom, explode, C_FIBRE),
            _p("Top potting block (open lumens)", tpot, "hdpe_natural", "bought", bom, explode, C_POT),
            _p("Module header collar", collar, "hdpe_natural", "bought", bom, explode, "#BFC8CC"),
            _oring("O-ring, module lower (clean/dirty seal)", 141.5, 6, explode),
            _oring("O-ring, module upper (clean/dirty seal)", 145.5, 6, explode)]


def port_plug(bom=13, explode=(-45, 0, 0)):
    zp, (r0, r1) = P["Z_PORT"], P["PORT_R"]
    d0, d1 = P["PORT_HOLE"]
    plug = Pos(0, 0, zp) * Rot(0, 90, 0) * (Pos(0, 0, r1 - 2.25) * Cone(d1 / 2 - 0.02, d0 / 2 - 0.02, 4.5)
                                            + Pos(0, 0, r1 + 0.4) * Cylinder(3.6, 0.8))
    plug = plug + Pos(r1 + 0.4, 0, zp + 6.0) * Box(0.8, 3.0, 9.0)      # tether strap up to the band
    band = S.tube(R_OUT, R_OUT + 0.8, 158.0, 164.0)
    return [_p("Backflush port plug (tethered)", plug, "epdm", "made", bom, explode, "#C2410C"),
            _p("Tether band", band, "epdm", "made", bom, explode, "#C2410C")]


def option_a1():
    out = []
    out += intake_cover()
    out += intake_cap()
    out += mesh_and_ring()
    out.append(housing_shell(*P["Z_HOUSING"], port=True))
    out += membrane_module()
    out += carbon_cartridge()
    out += port_plug()
    out += mouthpiece()
    out += mouth_cap()
    out += lanyard()
    return out


# ---------------------------------------------------------------------------------------------------------
# option A2: ceramic tube straw (dropped at the STEM check: flow)
# ---------------------------------------------------------------------------------------------------------
def option_a2():
    out = []
    out += intake_cover(bom=None)
    out += intake_cap(bom=None)
    out += mesh_and_ring(None, None)
    out.append(housing_shell(P["Z_HOUSING"][0], 140.0, name="Lower shell (dirty side, twists off)", bom=None, dip=True))
    # head: spigot 130 to 140 into the lower shell, body 140 to 190
    head = S.revolved([(R_IN, 140.0), (R_IN, 190.0), (R_OUT, 190.0), (R_OUT, 140.0), (R_SP, 140.0), (R_SP, 130.0),
                       (9.0, 130.0), (9.0, 140.0)])
    head = _male_gland(head, 133.0)
    head = head + S.lugs(P["LUG_R"][0] - 0.05, P["LUG_R"][1], 137.2, 137.2 + P["LUG_H"], P["LUG_W"])
    head = head - S.bayonet_cutter(R_IN, P["BAY_GROOVE_R"], 188.0, 189.5, 190.0, P["BAY_SLOT_W"])
    out.append(_p("Head (clean side, stays closed)", head, "hdpe_natural", "made", None, (0, 0, 40), C_HOUSING))
    out.append(_oring("O-ring, head to lower shell", 133.0, None, (0, 0, 40)))
    z0, z1 = P["Z_CER"]
    ro, ri = P["CER_OD"] / 2, P["CER_ID"] / 2
    cer = S.revolved([(0, z0), (ro - 3.0, z0), (ro - 1.0, z0 + 1.0), (ro, z0 + 3.5), (ro, z1), (ri, z1), (ri, z0 + 4.0),
                      (0, z0 + 4.0)])
    out.append(_p("Ceramic filter tube, sintered, closed end", cer, "concrete", "bought", None, (0, 0, -20), "#EDE6D8"))
    out.append(_p("Element gasket, silicone", S.tube(ri, ro, z1, z1 + 1.0), "epdm", "bought", None, (0, 0, 40)))
    col = S.revolved([(3.0, z1 + 1.0), (3.0, 150.0), (R_SP, 150.0), (R_SP, 140.0), (ro + 0.05, 140.0), (ro + 0.05, z1 + 1.0)])
    col = _male_gland(col, 144.0)
    col = _male_gland(col, 148.5)
    out.append(_p("Element collar (bonded to the tube)", col, "hdpe_natural", "made", None, (0, 0, 40), "#BFC8CC"))
    out.append(_oring("O-ring, element collar lower", 144.0, None, (0, 0, 40)))
    out.append(_oring("O-ring, element collar upper", 148.5, None, (0, 0, 40)))
    out += carbon_cartridge(bom=(None, None, None, None))
    out += mouthpiece(bom=None)
    out += mouth_cap(bom=None)
    out += lanyard(None, None)
    pad = cp.break_edges(Pos(36.0, 0, 60.0) * Box(14.0, 6.0, 40.0), 1.5)
    out.append(_p("Scrub pad (supplied)", pad, "canvas", "bought", None, (0, 0, 0), "#D9C27A"))
    return out


# ---------------------------------------------------------------------------------------------------------
# option A3: copper and charcoal straw (dropped at the STEM check: efficacy)
# ---------------------------------------------------------------------------------------------------------
def option_a3():
    out = []
    out += intake_cover(bom=None)
    out += intake_cap(bom=None)
    out += mesh_and_ring(None, None)
    out.append(housing_shell(*P["Z_HOUSING"], port=False, name="Housing body (no port)", bom=None))
    z0, z1 = P["Z_CU"]
    cu = S.tube(2.0, 2.4, z0, z1)       # rolled mesh drawn as four thin wraps (about 25 % solid, like a real roll)
    for r in (4.6, 7.0, 9.4):
        cu = cu + S.tube(r, r + 0.4, z0, z1)
    cu = cu - S.radial_slots(1.5, 10.5, 8, 1.0, z0 + 3.0, z1 - 3.0)
    out.append(_p("Copper mesh roll (rolled C11000 mesh)", cu, "brass", "bought", None, (0, 0, -25), "#B87333"))
    out.append(_p("Copper retainer screen, 316L", S.mesh_disc(2 * R_IN - 0.4, 0.4, z0 - 0.4), "stainless", "bought", None, (0, 0, -25)))
    out.append(_p("Spacer ring", S.tube(8.0, R_IN - 0.05, z1, z1 + 2.0), "hdpe_natural", "made", None, (0, 0, 20), C_CAP))
    out += carbon_cartridge(z0=z1 + 2.0, z1=180.0, bed=P["Z_A3_BED"], bed_d=P["A3_BED_D"], legs=False,
                            bom=(None, None, None, None), explode=(0, 0, 50), tag=" (long bed)")
    out += mouthpiece(bom=None)
    out += mouth_cap(bom=None)
    out += lanyard(None, None)
    return out


def components(option="A1"):
    return {"A1": option_a1, "A2": option_a2, "A3": option_a3}[option]() + [hand_part()]


def hand_part():
    return part("Hand (scale)", place_hand(), "skin", kind="context", group="context")


def place_hand():
    import context_parts
    h = context_parts.forearm_hand(side="left", pose="grip", grip_d=27.0, forearm_len=160.0)
    return HAND_LOC * h


from build123d import Location  # noqa: E402
HAND_LOC = Location()   # set by _fit_hand() below


def _fit_hand():
    """Find where the grip pose wraps its fingers and place that on the straw between z 60 and 100 mm."""
    global HAND_LOC
    import context_parts
    h = context_parts.forearm_hand(side="left", pose="grip", grip_d=27.0, forearm_len=160.0)
    bb = h.bounding_box()
    # the fingers curl round a cylinder across Y below the palm, near x = 0.65 of the hand length
    gx = 95.0
    gz = -27.0 / 2 - 5.0
    # rotate so +Y (grip axis) becomes +Z and the forearm points away (-X stays -X), then move the grip axis to the straw
    HAND_LOC = Pos(0, 0, 80.0) * Rot(90, 0, 0) * Pos(-gx, 0, -gz)


_fit_hand()


if __name__ == "__main__":
    for k in OPTIONS:
        ps = components(k)
        real = [q for q in ps if q["kind"] != "context"]
        m = sum(cp.mass_kg(q) for q in real) * 1000
        print(k, len(real), "parts", f"{m:.1f} g")
