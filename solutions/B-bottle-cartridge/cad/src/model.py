"""Helpful Water B: bottle cartridge. Parametric model (kit 1.9 interface, STANDARDS section 24), detail level D3.

Run from the solution folder:  python .kit/cad_check.py --export
Every main dimension is in PARAMS; docs/04-calcs/sizing.py (HWB-CAL-001) and docs/04-calcs/stem_check.py read it.

Options (HWB-OPT-001; chosen by Amish on 2026-11-11):
  B1  Squeeze cartridge: screws onto a 28 mm PCO 1881 PET bottle neck; squeezing the bottle drives water through a
      316L mesh, a replaceable coconut-carbon capsule and a bought, pre-potted hollow-fibre module (outside-in, looped
      fibres potted at the clean outlet end) to a push-pull drink valve. A duckbill valve lets air back into the
      bottle on release. Backflush with a 60 mL syringe from the outlet, carbon capsule removed.
  B2  Gravity drip: the same cartridge stack, inverted, with a longer module; the filled bottle hangs upside down
      on it in a three-leg stand and drips into a cup; a vent tube and duckbill let air into the bottle.
  B3  Press: a rigid cup and a press tube with the cartridge in its foot; pushing the press down drives water up
      through mesh, carbon and fibres into the press tube (no bottle).

Axes: Z up. B1 is modelled upright on the bottle with the neck's sealing lip at z = 0 (in use the bottle is tipped
and squeezed). B2 and B3 stand on a table at z = 0. Fasteners: hinge pin (B1), stand screws (B2), press screws (B3).
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import functools
import math
import sys
from pathlib import Path

from build123d import Box, Cylinder, Pos, Rot, Compound, fillet, chamfer, Axis

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import cad_parts as cp  # noqa: E402
from cad_parts import part  # noqa: E402
import hw_parts as H  # noqa: E402

TITLE = "Helpful Water B: bottle cartridge"
OPTIONS = {"B1": "Squeeze cartridge", "B2": "Gravity drip stand", "B3": "Press cup"}
PRINCIPLES = {
    "B1": "Screws onto a 28 mm PET bottle neck; a hand squeeze drives water through mesh, a carbon capsule and an "
          "outside-in hollow-fibre module to a push-pull drink valve; syringe backflush.",
    "B2": "The same cartridge inverted under a hanging bottle in a stand; gravity head (about 3 to 5 kPa) drips water "
          "through it into a cup; a vent tube lets air into the bottle. No squeeze effort.",
    "B3": "A rigid cup and a press tube with the cartridge in its foot; arm or body weight on the lid drives water up "
          "through the cartridge into the press tube (about 30 to 50 kPa). No bottle.",
}
CHOSEN = "B1"   # carried to the drawing, BOM and build plan; the concept choice was made by Amish on 2026-11-11
OPTION_VIEWS = {"B1": dict(el=18, az=-55, scale="hand", keep_context=True),
                "B2": dict(el=18, az=-55, scale="none", keep_context=True, ground_z=0),
                "B3": dict(el=18, az=-55, scale="none", keep_context=True, ground_z=0)}
# O-rings and gaskets are modelled at their compressed fit, so they touch their glands; seals and media fill
# their seats; threads interleave at half a pitch.
ALLOWED_CONTACTS = [("O-ring", ""), ("gasket", ""), ("Lip seal", ""), ("Carbon bed", "pad"), ("Fibre bundle", "potting"),
                    ("Fibre bundle", "guard sleeve"), ("Potting", "header"), ("Duckbill", "")]

PARAMS = {
    # bottle neck (PCO 1881, approximate; hw_parts.NECK)
    "NECK_T": H.NECK["T"], "NECK_BORE": H.NECK["BORE"], "NECK_PITCH": H.NECK["PITCH"], "NECK_H_1881": 17.0, "NECK_H_1810": 21.0,
    "BOTTLE_D": 80.0, "BOTTLE_H": 262.0, "BOTTLE_WALL": 0.30,
    # collar (neck adapter)
    "COLLAR_OD": 36.0, "COLLAR_ID": 28.2, "COLLAR_SKIRT": 17.0, "DECK": (1.5, 9.0), "INLET_D": 18.0,
    "SPIGOT_ROOT_D": 37.6, "SPIGOT_PITCH": 3.0, "SEAL_LAND_D": 36.6,
    # housing
    "HOUSING_OD": 41.0, "HOUSING_ID": 37.0, "HOUSING_TOP": {"B1": 160.0, "B2": 220.0, "B3": 160.0}, "END_WALL": 4.0,
    # carbon capsule (dirty side, upstream of the membrane; HWB-DEC-001 F1)
    "CAPSULE_OD": 34.0, "CAPSULE_ID": 30.0, "BED_D": 29.8, "BED_H": 20.0, "PAD_T": 1.5,
    "GAC_BULK": 0.49, "GAC_MESH": "12 x 40 US sieve (0.42 to 1.68 mm)", "GAC_DP_MM": 0.9,
    # hollow-fibre module (bought, pre-potted; dimensions are the design request to the supplier)
    "FIBRE_OD": 0.80, "FIBRE_ID": 0.50, "U_FIBRES": 400, "BUNDLE_D": 30.5, "POTTING_H": 10.0,
    "LEG": {"B1": 86.5, "B2": 146.5, "B3": 86.5}, "HEADER_OD": 36.6, "HEADER_ID": 31.0, "SLEEVE": (34.0, 32.0),
    "PORE_UM": 0.1,
    # outlet
    "NIPPLE": (10.0, 6.0), "SPOUT_OD": 24.0, "NOZZLE": (12.0, 5.0),
    # seals: O-ring cross-section and inside diameters
    "ORING_CS": 2.0, "ORING_ID": 33.4,
    # mesh prefilter
    "MESH_UM": 150, "MESH_D": 29.6,
    # B2 stand
    "STAND_R": 50.0, "STAND_LEG": (12.0, 1.5), "STAND_H": 180.0, "CRADLE_Z": 186.0,
    # B3 press
    "CUP": (76.0, 70.0, 200.0), "PRESS": (69.0, 65.0, 240.0), "PRESS_FOOT_Z": 20.0,
}
P = PARAMS


def _p(name, shape, mat, kind="made", bom=None, group="shell", explode=(0, 0, 0)):
    return part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode)


def _edge(shape, r=0.4):
    return cp.break_edges(shape, r)


# ------------------------------------------------------------------------------------------------------------
# Cartridge core, local coordinates: neck sealing lip at z = 0, the cartridge growing up +Z.
# ------------------------------------------------------------------------------------------------------------
def collar(neck=True, flange=None, vent=True):
    """Neck collar: female PCO 1881 skirt (if neck), deck with inlet bore and radial vent bore, male spigot thread
    for the housing and a seal land with an O-ring groove. flange=(od, t) adds an outer flange (B3 press foot)."""
    d0, d1 = P["DECK"]
    body = H.disc(P["COLLAR_OD"], d1 - d0, d0)
    if neck:
        body = body + H.tube(P["COLLAR_OD"], P["COLLAR_ID"], P["COLLAR_SKIRT"], -15.5)
        body = body + H.thread(P["COLLAR_ID"] / 2, 1.15, P["NECK_PITCH"], 1.75, internal=True, z0=-12.15)
        # grip ribs on the skirt
        for k in range(12):
            body = body + Rot(0, 0, 30 * k) * Pos(P["COLLAR_OD"] / 2, 0, -7.0) * Box(1.6, 2.4, 15.0)
    spig = H.tube(P["SPIGOT_ROOT_D"], 30.0, 10.0, d1)
    spig = spig + H.thread(P["SPIGOT_ROOT_D"] / 2 - 0.05, 1.2, P["SPIGOT_PITCH"], 2.2, internal=False, z0=10.5)
    land = H.tube(P["SEAL_LAND_D"], 30.0, 6.0, 19.0) - H.ring(37.0, 33.4, 2.4, 21.0)
    body = body + spig + land
    if flange:
        od, t = flange
        body = body + H.ring(od, P["COLLAR_OD"] - 0.5, t, d0)
    body = body - H.disc(P["INLET_D"], 30.0, -1.0)
    if vent:
        # radial air or vent bore at z = 5 with a counterbore for the duckbill valve
        body = body - Pos(12.0, 0, 5.0) * Rot(0, 90, 0) * Cylinder(1.5, 14.0)
        body = body - Pos(14.0 + 2.25, 0, 5.0) * Rot(0, 90, 0) * Cylinder(3.0, 4.6)
    if flange:
        for k in range(3):
            body = body - Rot(0, 0, 120 * k + 60) * Pos(flange[0] / 2 - 2.0, 0, 6.5) * Rot(0, 90, 0) * Cylinder(1.45, 8.0)
    return body


def duckbill():
    """Silicone duckbill check valve, 6 mm flange, lips pointing inward (opens to let air in)."""
    flange = Pos(17.6, 0, 5.0) * Rot(0, 90, 0) * Cylinder(2.9, 1.0)
    barrel = Pos(16.0, 0, 5.0) * Rot(0, 90, 0) * (Cylinder(2.2, 2.4) - Cylinder(1.2, 3.0))
    lips = Pos(14.4, 0, 5.0) * Rot(0, 90, 0) * (Cylinder(2.2, 0.8) - Box(0.3, 5.0, 1.0))
    return flange + barrel + lips


def capsule_body():
    """Carbon capsule cup: spigot that plugs into the collar bore, slotted floor, body for the 20 mm bed."""
    spig = H.tube(29.8, 24.0, 13.0, 12.0)
    floor = H.disc(24.2, 1.5, 12.0)
    holes = None
    for k in range(7):
        r = 0 if k == 0 else 7.0
        a = 60 * k
        h = Pos(r * math.cos(math.radians(a)), r * math.sin(math.radians(a)), 12.75) * Cylinder(1.5, 3.0)
        holes = h if holes is None else holes + h
    body = H.tube(P["CAPSULE_OD"], P["CAPSULE_ID"], 24.0, 25.0) + H.ring(29.8, 24.0, 1.0, 24.0)
    s = spig + floor - holes + body
    return s


def capsule_lid():
    plug = H.disc(29.9, 1.0, 48.0)
    flange = H.disc(P["CAPSULE_OD"], 1.2, 49.0)
    lid = plug + flange
    for k in range(6):
        a = 60 * k
        lid = lid - Pos(8.0 * math.cos(math.radians(a)), 8.0 * math.sin(math.radians(a)), 49.0) * Cylinder(1.6, 4.0)
    lid = lid - Pos(0, 0, 49.0) * Cylinder(2.0, 4.0)
    # two finger notches in the flange rim for pulling the capsule out
    for sx in (1, -1):
        lid = lid - Pos(sx * 17.0, 0, 49.6) * Box(3.0, 6.0, 1.2)
    return lid


def module(leg, z_base):
    """Bought, pre-potted hollow-fibre module: end cap, perforated guard sleeve, looped fibre bundle, potting block,
    header cup with two O-ring grooves and a clean outlet nipple. Returns dict of solids, local z from z_base."""
    so, si = P["SLEEVE"]
    z_cap = z_base
    z_sl = z_cap + 1.5
    z_pot = z_sl + leg + 1.5          # potting starts where the sleeve ends
    endcap = H.disc(so, 1.5, z_cap)
    for k in range(6):
        endcap = endcap - Pos(9.0 * math.cos(math.radians(60 * k)), 9.0 * math.sin(math.radians(60 * k)), z_cap + 0.75) * Cylinder(2.0, 3.0)
    sleeve = H.perforated_sleeve(so, si, z_pot - z_sl, z_sl, rows=max(4, int(leg / 16)))
    bundle = H.fibre_bundle(P["BUNDLE_D"], z_pot - (z_sl + 1.5), z_sl + 1.5)
    potting = H.disc(P["HEADER_ID"], P["POTTING_H"], z_pot)
    try:
        potting = chamfer(potting.edges().group_by(Axis.Z)[0], 0.6)
    except Exception:
        pass
    zh = z_pot
    header = H.tube(P["HEADER_OD"], P["HEADER_ID"], 16.0, zh) + H.disc(P["HEADER_OD"], 4.0, zh + 16.0)
    header = header - H.ring(37.0, 33.4, 2.4, zh + 4.0) - H.ring(37.0, 33.4, 2.4, zh + 11.0)
    header = header + H.tube(P["NIPPLE"][0], P["NIPPLE"][1], 12.0, zh + 20.0)
    header = header - H.disc(P["NIPPLE"][1], 6.0, zh + 18.0)
    return dict(endcap=endcap, sleeve=sleeve, bundle=bundle, potting=potting, header=header,
                oring_z=(zh + 5.2, zh + 12.2), top=zh + 20.0)


def housing(z_top, spout_thread=True, grip=True):
    """Housing: female thread over the collar spigot, bore for capsule and module, end wall with nipple bore and
    a male thread spigot for the spout."""
    lower = H.tube(44.0, 40.4, 10.0, 9.0) + H.thread(20.2 + 0.05, 1.2, P["SPIGOT_PITCH"], 2.0, internal=True, z0=12.0)
    body = H.tube(P["HOUSING_OD"], P["HOUSING_ID"], z_top - 19.0, 19.0)
    wall = H.disc(P["HOUSING_OD"], P["END_WALL"], z_top) - H.disc(10.4, 10.0, z_top - 1.0)
    s = lower + body + wall
    if spout_thread:
        spig = H.tube(20.0, 10.4, 10.0, z_top + P["END_WALL"]) + H.thread(10.0 - 0.05, 1.0, 2.0, 4.0, internal=False, z0=z_top + 5.0)
        s = s + spig
    if grip:
        for k in range(16):
            s = s + Rot(0, 0, 22.5 * k) * Pos(22.2, 0, 14.0) * Box(1.2, 2.0, 9.0)
    return s


def spout(z0, valve=True):
    """Spout: internal thread onto the housing spigot, top plate and nozzle with an O-ring groove and side ports."""
    tubez = H.tube(P["SPOUT_OD"], 22.4, 11.2, z0) + H.thread(11.2 + 0.05, 1.0, 2.0, 3.5, internal=True, z0=z0 + 2.0)
    plate = H.disc(P["SPOUT_OD"], 3.0, z0 + 11.2) - H.disc(5.0, 5.0, z0 + 10.0)
    no, ni = P["NOZZLE"]
    noz = H.tube(no, ni, 12.8, z0 + 14.2)
    if valve:
        noz = noz - H.ring(13.0, 10.0, 1.4, z0 + 17.2)
        for a in (0, 90, 180, 270):
            noz = noz - Rot(0, 0, a) * Pos(4.5, 0, z0 + 24.0) * Rot(0, 90, 0) * Cylinder(1.0, 4.0)
        lug = Pos(13.5, 0, z0 + 11.0) * (Box(3.0, 5.0, 6.0) - Rot(90, 0, 0) * Cylinder(0.8, 6.0))
        lug = lug + Pos(12.6, 0, z0 + 11.0) * Box(1.6, 5.0, 6.0)
        noz = noz + lug
    return tubez + plate + noz


# ------------------------------------------------------------------------------------------------------------
# B1 squeeze cartridge
# ------------------------------------------------------------------------------------------------------------
BOM = {"collar": 1, "housing": 2, "capsule": 3, "lid": 4, "spout": 5, "valve": 6, "cover": 7, "module": 8,
       "carbon": 9, "pads": 10, "mesh": 11, "oring_big": 12, "gasket_neck": 13, "gasket_spout": 14, "oring_small": 15,
       "duckbill": 16, "pin": 17, "syringe": 18}


def core_parts(opt, neck=True, flange=None, top_bom=True, vent_valve=True):
    """Cartridge stack in local coordinates for any option (lip at z = 0)."""
    zt = P["HOUSING_TOP"][opt]
    leg = P["LEG"][opt]
    m = module(leg, 50.5)
    out = []
    E = lambda dz: (0, 0, dz)
    out.append(_p("Neck collar with PCO 1881 thread" if neck else "Press foot with cartridge spigot",
                  _edge(collar(neck, flange, vent_valve), 0.3), "hdpe_natural", "made", BOM["collar"], "shell", E(-60)))
    if neck:
        out.append(_p("Neck gasket (flat, EPDM)", H.flat_gasket(27.6, 20.5, 1.5, 0.0), "epdm", "bought", BOM["gasket_neck"], "internal", E(-75)))
    if vent_valve:
        out.append(_p("Duckbill air valve (silicone)", duckbill(), "epdm", "bought", BOM["duckbill"], "internal", (30, 0, -60)))
    out.append(_p("Mesh prefilter disc, 150 um 316L", H.mesh_disc(P["MESH_D"], 0.25, 9.2), "stainless", "bought", BOM["mesh"], "internal", E(-30)))
    out.append(_p("Collar O-ring 33.4 x 2", H.o_ring(P["ORING_ID"], P["ORING_CS"], 22.2), "epdm", "bought", BOM["oring_big"], "internal", E(-45)))
    out.append(_p("Carbon capsule body", _edge(capsule_body(), 0.25), "hdpe_black", "made", BOM["capsule"], "internal", E(-10)))
    out.append(_p("Retention pad, lower", H.pad(29.6, P["PAD_T"], 25.0), "label", "bought", BOM["pads"], "internal", E(-2)))
    out.append(_p("Carbon bed, 12 x 40 coconut GAC", H.carbon_bed(P["BED_D"] - 0.2, P["BED_H"], 26.5), "matte_black", "bought", BOM["carbon"], "internal", E(6)))
    out.append(_p("Retention pad, upper", H.pad(29.6, P["PAD_T"], 46.5), "label", "bought", BOM["pads"], "internal", E(14)))
    out.append(_p("Carbon capsule lid", _edge(capsule_lid(), 0.2), "hdpe_black", "made", BOM["lid"], "internal", E(22)))
    gx = 20 if opt != "B1" else 0
    out.append(_p("Module end cap", m["endcap"], "hdpe_natural", "bought", BOM["module"], "internal", E(40)))
    out.append(_p("Module guard sleeve, perforated", m["sleeve"], "hdpe_natural", "bought", BOM["module"], "internal", E(40)))
    out.append(_p("Fibre bundle, looped, outside-in", m["bundle"], "insulated_white", "bought", BOM["module"], "internal", E(40)))
    out.append(_p("Potting block (module)", m["potting"], "label", "bought", BOM["module"], "internal", E(40)))
    out.append(_p("Module header with clean nipple", _edge(m["header"], 0.2), "hdpe_natural", "bought", BOM["module"], "internal", E(40)))
    for i, z in enumerate(m["oring_z"]):
        out.append(_p(f"Header O-ring {i + 1}, 33.4 x 2", H.o_ring(P["ORING_ID"], P["ORING_CS"], z), "epdm", "bought", BOM["oring_big"], "internal", E(40)))
    out.append(_p("Housing", _edge(housing(zt, spout_thread=top_bom), 0.3), "polycarbonate" if opt == "B3" else "hdpe_recycled",
                  "made", BOM["housing"], "shell", E(230)))
    return out, zt


def _cover_and_pin(z0):
    cover = H.tube(19.0, 16.4, 18.0, z0 + 17.8) + H.disc(19.0, 1.5, z0 + 35.8)
    cheek = None
    for sy in (1, -1):
        c = Pos(13.5, sy * 3.6, z0 + 12.6) * Box(3.0, 2.0, 7.6) + Pos(12.0, sy * 3.6, z0 + 17.4) * Box(6.0, 2.0, 2.0)
        cheek = c if cheek is None else cheek + c
    cover = cover + cheek - Pos(13.5, 0, z0 + 11.0) * Rot(90, 0, 0) * Cylinder(0.8, 12.0)
    pinp = Pos(13.5, 0, z0 + 11.0) * Rot(90, 0, 0) * H.pin(1.5, 9.0)
    return cover, pinp


def option_b1(context=True):
    parts, zt = core_parts("B1")
    zs = zt + P["END_WALL"]           # spout sits on the housing spigot root
    E = lambda dz: (0, 0, dz)
    parts.append(_p("Spout gasket (flat, EPDM)", H.flat_gasket(19.8, 11.0, 1.2, zs + 10.0), "epdm", "bought", BOM["gasket_spout"], "internal", E(250)))
    parts.append(_p("Spout with nozzle and hinge lug", _edge(spout(zs, valve=True), 0.25), "hdpe_natural", "made", BOM["spout"], "shell", E(262)))
    zv = zs + 16.0
    valve = H.tube(15.4, 12.2, 12.0, zv) + H.disc(15.4, 1.6, zv + 12.0)
    for k in range(4):
        valve = valve - Pos(4.0 * math.cos(math.radians(90 * k + 45)), 4.0 * math.sin(math.radians(90 * k + 45)), zv + 12.8) * Cylinder(1.0, 3.0)
    valve = valve + H.disc(4.9, 3.0, zv + 9.0)
    parts.append(_p("Push-pull drink valve", _edge(valve, 0.25), "hdpe_natural", "made", BOM["valve"], "shell", E(290)))
    parts.append(_p("Valve O-ring 10 x 1.2", H.o_ring(10.0, 1.2, zs + 17.9), "epdm", "bought", BOM["oring_small"], "internal", E(276)))
    cover, pinp = _cover_and_pin(zs)
    parts.append(_p("Dust cover", _edge(cover, 0.2), "hdpe_natural", "made", BOM["cover"], "shell", (20, 0, 310)))
    parts.append(_p("Hinge pin 1.5 x 9, stainless", pinp, "stainless", "fastener", BOM["pin"], "shell", (20, 0, 310)))
    if context:
        parts += b1_context()
    return parts


def b1_context():
    import context_parts
    bottle = H.pet_bottle_1l(0.0, P["BOTTLE_D"], P["BOTTLE_H"])
    out = [_p("PET bottle 1 L (context)", bottle, "glass", "context", None, "context")]
    hand = context_parts.forearm_hand(side="right", pose="grip", grip_d=80.0)
    hand = Pos(-78, -44, -150) * Rot(90, 0, 0) * hand     # fingers round the bottle body, forearm toward -X
    out.append(_p("Hand (scale)", hand, "skin", "context", None, "context"))
    return out


# ------------------------------------------------------------------------------------------------------------
# B2 gravity drip stand
# ------------------------------------------------------------------------------------------------------------
B2_BASE_R = 115.0   # base ring outer radius after the stability fix (HWB-DEC-001 F3); was 65
B2_TOP = 306.0   # world z of the collar's neck lip (cartridge inverted under the hanging bottle)


def _flip(shape):
    """Local cartridge coordinates (lip at 0, growing up) to B2 world (lip at B2_TOP, growing down)."""
    return Pos(0, 0, B2_TOP) * Rot(180, 0, 0) * shape


def option_b2(context=True):
    core, zt = core_parts("B2")
    out = []
    for q in core:
        q = dict(q)
        q["shape"] = _flip(q["shape"])
        ex = q["explode"]
        q["explode"] = (ex[0], ex[1], -ex[2])
        out.append(q)
    zs = zt + P["END_WALL"]
    out.append(_p("Spout gasket (flat, EPDM)", _flip(H.flat_gasket(19.8, 11.0, 1.2, zs + 10.0)), "epdm", "bought", 14, "internal", (0, 0, -130)))
    out.append(_p("Drip spout", _flip(_edge(spout(zs, valve=False), 0.25)), "hdpe_natural", "made", 5, "shell", (0, 0, -140)))
    # vent tube: radial leg in the deck, then up through the neck into the bottle (local -z)
    vt = Pos(7.0, 0, 5.0) * Rot(0, 90, 0) * (Cylinder(2.0, 4.0) - Cylinder(1.2, 5.0))
    up = Pos(5.0, 0, 5.0 - 115.0) * (Cylinder(2.0, 230.0) - Cylinder(1.2, 231.0))
    try:
        vtube = vt + up
    except Exception:
        vtube = Compound([vt, up])
    out.append(_p("Vent tube 4 x 0.8 silicone", _flip(vtube), "epdm", "bought", 19, "internal", (0, 0, 120)))
    # stand: base ring, three legs, cradle ring, six screws
    zc = B2_TOP - 23.0                  # the housing's grip band rests on the cradle lip
    base = H.ring(130.0, 96.0, 6.0, 0.0) + H.ring(2 * B2_BASE_R, 2 * B2_BASE_R - 24.0, 6.0, 0.0)
    for k in range(3):
        base = base + Rot(0, 0, 90 + 120 * k + 60) * Pos((48.0 + B2_BASE_R - 12.0) / 2 + 10, 0, 3.0) * Box(B2_BASE_R - 52.0, 16.0, 6.0)
    cradle = H.ring(130.0, 42.6, 8.0, zc - 8.0)
    legs, screws = [], []
    for k in range(3):
        a = math.radians(90 + 120 * k)
        x, y = P["STAND_R"] * 1.15 * math.cos(a), P["STAND_R"] * 1.15 * math.sin(a)
        base = base + Pos(x, y, 3.0) * Cylinder(9.0, 6.0) - Pos(x, y, 3.0) * Cylinder(2.25, 8.0)
        cradle = cradle + Pos(x, y, zc - 4.0) * Cylinder(9.0, 8.0) - Pos(x, y, zc - 4.0) * Cylinder(2.25, 10.0)
        L = zc - 8.0 - 6.0
        legs.append(_p(f"Stand leg {k + 1}, aluminium tube 12 x 1.5", Pos(x, y, 6.0) * cp.round_tube(12.0, 1.5, L), "aluminium", "made", 21, "stand", (0, 0, 0)))
        screws.append(_p(f"Leg screw {k + 1}a, 4 x 12 pan head", Pos(x, y, 0.0) * Rot(180, 0, 0) * H.hex_socket_screw(4.0, 10.0), "zinc_plated", "fastener", 23, "stand"))
        screws.append(_p(f"Leg screw {k + 1}b, 4 x 12 pan head", Pos(x, y, zc) * H.hex_socket_screw(4.0, 10.0), "zinc_plated", "fastener", 23, "stand"))
    # cradle lip that the housing flange (grip band) rests in
    cradle = cradle + H.ring(60.0, 42.6, 4.0, zc)
    out.append(_p("Stand base ring", _edge(base, 0.6), "hdpe_recycled", "made", 20, "stand", (0, 0, -40)))
    out += legs
    out.append(_p("Stand cradle ring", _edge(cradle, 0.6), "hdpe_recycled", "made", 22, "stand", (0, 0, 60)))
    out += screws
    if context:
        bottle = Pos(0, 0, B2_TOP) * Rot(180, 0, 0) * H.pet_bottle_1l(0.0, P["BOTTLE_D"], P["BOTTLE_H"])
        out.append(_p("PET bottle 1 L, inverted (context)", bottle, "glass", "context", None, "context"))
        cup = H.tube(84.0, 80.0, 105.0, 0.0) + H.disc(84.0, 2.0, 0.0)
        out.append(_p("Drinking cup (context)", cup, "pe_tank_white", "context", None, "context"))
    return out


# ------------------------------------------------------------------------------------------------------------
# B3 press cup
# ------------------------------------------------------------------------------------------------------------
def option_b3(context=True):
    zf = P["PRESS_FOOT_Z"]
    core, zt = core_parts("B3", neck=False, flange=(64.8, 7.5), top_bom=False, vent_valve=False)
    out = []
    for q in core:
        q = dict(q)
        q["shape"] = Pos(0, 0, zf) * q["shape"]
        out.append(q)
    co, ci, ch = P["CUP"]
    cup = H.tube(co, ci, ch - 3.0, 3.0) + H.disc(co, 3.0, 0.0) + H.ring(co + 4.0, ci, 3.0, ch - 3.0)
    for k in range(3):
        cup = cup + Rot(0, 0, 120 * k) * Pos(co / 2, 0, 3.0) * Box(4.0, 8.0, 6.0)
    out.append(_p("Outer cup", _edge(cup, 0.5), "polycarbonate", "made", 31, "shell", (0, 0, -80)))
    lip = H.ring(70.3, 64.0, 1.9, zf + 1.5)
    try:
        lip = fillet(lip.edges(), 0.8)
    except Exception:
        pass
    out.append(_p("Lip seal ring (EPDM)", lip, "epdm", "bought", 32, "internal", (0, 0, -30)))
    po, pi, pl = P["PRESS"]
    zp = zf + 3.5
    press = H.tube(po, pi, pl, zp)
    for k in range(3):
        press = press - Rot(0, 0, 120 * k + 60) * Pos(po / 2 - 0.1, 0, zf + 6.5) * Rot(0, 90, 0) * H.countersink_cut(3.0, 8.0)
    out.append(_p("Press tube", _edge(press, 0.4), "polycarbonate", "made", 33, "shell", (0, 0, 120)))
    lid = H.disc(po + 8.0, 4.0, zp + pl) + H.tube(pi - 0.2, pi - 4.0, 8.0, zp + pl - 8.0)
    lid = lid + Pos(30.0, 0, zp + pl + 4.0) * Pos(0, 0, 7.0) * Cylinder(6.0, 14.0)
    lid = lid - Pos(30.0, 0, zp + pl - 2.0) * Cylinder(2.5, 40.0)
    lid = lid + Pos(-14.0, 0, zp + pl + 5.0) * (Box(34.0, 50.0, 6.0))
    out.append(_p("Press lid with spout and palm pad", _edge(lid, 0.5), "hdpe_natural", "made", 34, "shell", (0, 0, 180)))
    cap = Pos(30.0, 0, 0) * (H.tube(14.4, 12.2, 9.0, zp + pl + 13.0) + H.disc(14.4, 1.5, zp + pl + 22.0))
    out.append(_p("Spout cap", _edge(cap, 0.2), "hdpe_natural", "made", 35, "shell", (0, 0, 200)))
    for k in range(3):
        a = 120 * k + 60
        s = Rot(0, 0, a) * Pos(po / 2 - 0.15, 0, zf + 6.5) * Rot(0, 90, 0) * H.countersunk_screw(3.0, 7.0)
        out.append(_p(f"Press screw {k + 1}, 3 x 8 countersunk", s, "stainless", "fastener", 36, "shell"))
    if context:
        import context_parts
        hand = context_parts.forearm_hand(side="right", pose="flat")
        hand = Pos(-20, -55, zp + pl + 15.0) * Rot(0, 0, 90) * hand
        out.append(_p("Hand (scale)", hand, "skin", "context", None, "context"))
    return out


@functools.lru_cache(None)
def _components(option, context=True):
    return tuple({"B1": option_b1, "B2": option_b2, "B3": option_b3}[option](context))


def components(option="B1", context=True):
    return [dict(q) for q in _components(option, context)]


if __name__ == "__main__":
    for o in OPTIONS:
        ps = components(o)
        print(o, len([p for p in ps if p["kind"] != "context"]), "parts")
        for p in ps:
            bb = p["shape"].bounding_box()
            print(f"   {p['kind']:8s} {p['name'][:45]:45s} z {bb.min.Z:7.1f} .. {bb.max.Z:7.1f}  {cp.mass_kg(p)*1000:6.1f} g")
