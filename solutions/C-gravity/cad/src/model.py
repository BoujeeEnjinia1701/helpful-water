"""Helpful Water C: household gravity filter. Parametric model (kit 1.9 interface, STANDARDS section 24), detail level D3.

Run from the solution folder:  python .kit/cad_check.py --export
Every main dimension is in PARAMS (cad/src/params.py); docs/04-calcs/sizing.py (HWC-CAL-001) and
docs/04-calcs/stem_check.py read the same file.

Options (HWC-OPT-001; chosen by Amish on 2026-11-11):
  C1  Two-bucket hollow-fibre filter on a timber stand: raw 20 L bucket on the top shelf (cloth prefilter in the
      lid, settling zone below a raised strainer outlet, dosing port for solution D, ball valve), a silicone hose
      down to a bought, pre-potted outside-in hollow-fibre module standing on the stand leg, a clean-side tee with
      a luer backflush port, and a hose up into a closed 20 L clean bucket with a tap on the lower shelf.
  C2  Ceramic candle filter: two stacked 20 L buckets on a stool; four ceramic candles stand in the upper bucket
      and drain through its floor into the lower bucket, which has the tap.
  C3  Plastic biosand filter: a 900 mm HDPE body with drainage gravel, separating gravel and 540 mm of fine sand
      under a diffuser plate; the outlet tube sets a 50 mm standing water layer and runs to a clean bucket.

Axes: Z up, floor at z = 0, the user stands on the -Y side (front). CONCEPT, NOT FOR FABRICATION.

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
from __future__ import annotations

import functools
import math
import sys
from pathlib import Path

from build123d import Box, Cylinder, Pos, Rot, Compound, Plane

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]
import cad_parts as cp  # noqa: E402
from cad_parts import part  # noqa: E402
import c_parts as H  # noqa: E402
from params import PARAMS  # noqa: E402

P = PARAMS
TITLE = "Helpful Water C: household gravity filter"
OPTIONS = {"C1": "Two-bucket hollow-fibre filter", "C2": "Ceramic candle filter", "C3": "Plastic biosand filter"}
PRINCIPLES = {
    "C1": "Gravity (0.4 to 0.66 m) drives settled, prefiltered raw water from a 20 L bucket through a bought 0.1 um "
          "outside-in hollow-fibre module into a closed 20 L bucket with a tap; syringe backflush; chlorine from D "
          "can be dosed in the raw bucket first.",
    "C2": "Four ceramic microfiltration candles stand in the upper of two stacked 20 L buckets; about 0.3 m of water "
          "drains through the ceramic walls into the lower bucket with the tap; candles are scrubbed, not backflushed.",
    "C3": "A biologically active sand bed (CAWST version 10 layers) in a plastic body: batches of 18 L poured onto a "
          "diffuser filter down through 540 mm of fine sand; a biolayer ripens over weeks; outlet to a clean bucket.",
}
CHOSEN = "C1"   # carried to the drawing, BOM and build plan; the concept choice was made by Amish on 2026-11-11
OPTION_VIEWS = {"C1": dict(el=16, az=-50, scale="person", keep_context=True, ground_z=0),
                "C2": dict(el=16, az=-50, scale="person", keep_context=True, ground_z=0),
                "C3": dict(el=16, az=-50, scale="person", keep_context=True, ground_z=0)}
# Seals and gaskets are modelled at their compressed fit; hoses are pushed over barbs; the cloth is pinched by its
# clamp ring; wing nuts and tap nuts run on thread ridges; lids snap over rims; media fill their containers.
ALLOWED_CONTACTS = [("gasket", ""), ("Gasket", ""), ("hose", ""), ("Hose", ""), ("cloth", ""), ("Cloth", ""),
                    ("nut", "fitting"), ("nut", "tap"), ("Wing nut", ""), ("Potting", "Module"), ("Fibre bundle", ""),
                    ("Pinch clamp", ""), ("P-clip", "Module"), ("lid", "bucket"), ("Lid", "bucket"),
                    ("gravel", ""), ("sand", ""), ("Strainer", "fitting"), ("Candle base", "Candle shell")]

T = P["TIMBER"]
LC = P["LEG_C"]
TOP = P["TOP_Z"]
LOW = P["LOW_Z"]
SH = P["SHELF_T"]


def _p(name, shape, mat, kind="made", bom=None, group="shell", explode=(0, 0, 0), color=None):
    return part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode, color=color)


RAW_BLUE = "#3B6E8F"     # raw (dirty) side colour: blue bucket and lid, so users never mix them up
CLEAN_WHITE = "#ECEBE4"

BOM = {"raw_bucket": 1, "raw_lid": 2, "clamp_ring": 3, "cloth": 4, "fill_cover": 5, "d_collar": 6, "d_cap": 7,
       "bulkhead": 8, "strainer": 9, "valve": 10, "tag": 11, "barbs": 12, "hose": 13, "module": 14, "p_clip": 15,
       "tee": 16, "pinch": 17, "clean_bucket": 18, "clean_lid": 19, "inlet": 20, "vent": 21, "screen": 22,
       "tap": 23, "labels": 24, "timber": 25, "plywood": 26, "brace": 27, "coach": 28, "bolts": 29, "screws": 30,
       "syringe": 31, "check_valve": 32}


# ------------------------------------------------------------------------------------------------------------
# Shared assemblies
# ------------------------------------------------------------------------------------------------------------
TAPER = math.degrees(math.atan((P["BKT_TOP_OD"] - P["BKT_BOT_OD"]) / 2 / (P["BKT_H"] - P["BKT_RIM"][1] - 3.0)))


def wall_r(z_local):
    """Outer radius of the bucket wall at height z_local above its foot."""
    bo, to = P["BKT_BOT_OD"] / 2, P["BKT_TOP_OD"] / 2
    return bo + (to - bo) * (z_local - 3.0) / (P["BKT_H"] - P["BKT_RIM"][1] - 3.0)


def raw_lid_set(cx, cy, z_foot, bom=True, d_port=True, prefix="Raw"):
    """Raw (or upper) bucket lid with the cloth prefilter fill ring, its cover and the solution D dosing port."""
    zr = z_foot + P["BKT_H"]
    fx, fy = -30.0, 25.0
    dx, dy = 88.0, -62.0
    holes = [(fx, fy, P["FILL_D"])] + ([(dx, dy, P["D_PORT_D"])] if d_port else [])
    zt = zr + P["LID_T"] + 0.2
    out = []
    E = lambda dz: (0, 0, dz)
    out.append(_p(f"{prefix} lid (fill and dosing holes cut)", Pos(cx, cy, 0) * H.bucket_lid(P, zr, holes), "hdpe_natural", "bought",
                  BOM["raw_lid"], "shell", E(160), RAW_BLUE))
    cloth = H.disc(P["FILL_D"] + 18, 0.8, zt) + H.disc(P["FILL_D"] - 22, 0.8, zt - 18.0) + \
        H.tube(P["FILL_D"] - 21.0, P["FILL_D"] - 22.6, 18.0, zt - 18.0)
    out.append(_p("Prefilter cloth, cotton folded to 8 layers", Pos(cx + fx, cy + fy, 0) * cloth, "canvas", "bought",
                  BOM["cloth"], "internal", E(220)))
    ring = H.ring(P["FILL_D"] + 30, P["FILL_D"] - 24, 4.0, zt + 0.8) + H.tube(P["FILL_D"] - 23.0, P["FILL_D"] - 30, 22.0, zt - 21.2)
    for k in range(4):
        ring = ring + Rot(0, 0, 45 + 90 * k) * Pos((P["FILL_D"] + 30) / 2 - 2, 0, zt + 2.8) * H.soft(Box(6, 14, 4), 1.0)
    out.append(_p("Cloth clamp ring", Pos(cx + fx, cy + fy, 0) * H.soft(ring, 0.6), "hdpe_natural", "made",
                  BOM["clamp_ring"], "shell", E(250), "#D9D6CC"))
    cov = H.disc(P["FILL_D"] + 38, 3.0, zt + 5.2) + H.tube(P["FILL_D"] + 38, P["FILL_D"] + 33, 5.2, zt)
    cov = cov + Pos(0, 0, zt + 8.2 + 6) * H.soft(Box(60, 14, 12), 3.0)
    cov = cov - Pos(0, 0, zt + 8.2 + 5) * Box(40, 16, 6)
    out.append(_p("Fill cover with handle", Pos(cx + fx, cy + fy, 0) * cov, "hdpe_natural", "made", BOM["fill_cover"],
                  "shell", E(290), RAW_BLUE))
    if d_port:
        dp = P["D_PORT_D"]
        col = H.ring(dp + 16, dp - 8, 3.0, zt) + H.tube(dp - 0.6, dp - 8, 16.0, zt - 13.0)
        col = col + H.thread(dp / 2 + 1.0, 1.2, 3.0, 2.2, internal=False, z0=zt + 5.5) + H.tube(dp + 2.0, dp - 8, 9.0, zt + 3.0)
        out.append(_p("Dosing port collar for solution D", Pos(cx + dx, cy + dy, 0) * H.soft(col, 0.3), "hdpe_natural", "made",
                      BOM["d_collar"], "shell", E(230), "#D9D6CC"))
        cap = H.disc(dp + 10, 3.0, zt + 13.5) + H.tube(dp + 10, dp + 5.2, 10.5, zt + 3.0)
        for k in range(12):
            cap = cap + Rot(0, 0, 30 * k) * Pos((dp + 10) / 2, 0, zt + 9.0) * Box(1.6, 3.0, 9.0)
        out.append(_p("Dosing port cap", Pos(cx + dx, cy + dy, 0) * cap, "hdpe_natural", "made", BOM["d_cap"], "shell",
                      E(270), RAW_BLUE))
    return out


def clean_bucket_set(cx, cy, z_foot, inlet_xy, vent_xy, tap=True, label=True, d_port_xy=None):
    """Closed clean bucket: bucket with tap, lid with the inlet fitting and a screened vent."""
    out = []
    holes = [(inlet_xy[0] - cx, inlet_xy[1] - cy, 22.0), (vent_xy[0] - cx, vent_xy[1] - cy, 16.0)]
    if d_port_xy:
        holes.append((d_port_xy[0] - cx, d_port_xy[1] - cy, P["D_PORT_D"]))
    zr = z_foot + P["BKT_H"]
    zt = zr + P["LID_T"] + 0.2
    bkt = Pos(cx, cy, 0) * H.bucket(P, z_foot)
    tap_parts = []
    if tap:
        r = wall_r(P["TAP_H"])
        tap_parts = H.drum_tap((cx, cy - r, z_foot + P["TAP_H"]), P["BKT_WALL"])
        bkt = bkt - tap_parts[3]
    out.append(_p("Clean bucket (tap hole cut)", bkt, "hdpe_natural", "bought", BOM["clean_bucket"], "shell", (0, 0, 0), CLEAN_WHITE))
    out.append(_p("Clean lid (inlet and vent holes cut)", Pos(cx, cy, 0) * H.bucket_lid(P, zr, holes), "hdpe_natural", "bought", BOM["clean_lid"],
                  "shell", (0, 0, 120), CLEAN_WHITE))
    ix, iy = inlet_xy
    inl = H.disc(40.0, 3.0, zt) + H.tube(21.4, 12.0, 10.0, zt - 9.0) + H.tube(16.0, 7.0, 12.0, zt + 3.0)
    inl = inl + Pos(0, 0, zt + 15.0 + 6.0) * (H.Cone(P["HOSE_ID"] / 2 + 0.4, P["HOSE_ID"] / 2 - 0.6, 3.5) - Cylinder(3.5, 5))
    inl = inl + H.tube(P["HOSE_ID"] - 1.0, 7.0, 10.0, zt + 15.0) - H.disc(7.0, 40.0, zt - 12.0)
    inl = inl + H.ring(21.4, 17.0, 3.0, zt - 12.0)
    out.append(_p("Clean inlet fitting", Pos(ix, iy, 0) * H.soft(inl, 0.3), "hdpe_natural", "made", BOM["inlet"], "shell", (0, 0, 160), "#D9D6CC"))
    vx, vy = vent_xy
    vent = H.disc(34.0, 2.5, zt) + H.tube(15.4, 10.0, 9.0, zt - 8.5) + Pos(0, 0, zt + 2.5) * H.tube(34.0, 28.0, 8.0, 0.0)
    vent = vent + H.disc(34.0, 2.0, zt + 12.0)
    for k in range(6):
        vent = vent - Rot(0, 0, 60 * k) * Pos(15.5, 0, zt + 6.5) * Rot(0, 90, 0) * Cylinder(2.0, 6.0)
    vent = vent - H.disc(10.0, 20.0, zt - 10.0)
    try:
        vent = H.chamfer(vent.edges().group_by(H.Axis.Z)[-1], 0.6)      # break the top edge only
    except Exception:
        pass
    out.append(_p("Vent cap", Pos(vx, vy, 0) * vent, "hdpe_natural", "made", BOM["vent"], "shell", (0, 0, 160), "#D9D6CC"))
    scr = H.disc(27.5, 0.4, zt + 2.6) + H.ring(27.5, 25.0, 1.0, zt + 2.6)
    out.append(_p("Insect screen disc, stainless", Pos(vx, vy, 0) * scr, "stainless", "bought", BOM["screen"], "internal", (0, 0, 175)))
    if tap:
        out.append(_p("Drum tap, 3/4 in", tap_parts[0], "hdpe_natural", "bought", BOM["tap"], "shell", (0, -60, 0), "#1F5F8B"))
        out.append(_p("Tap nut", tap_parts[1], "hdpe_natural", "bought", BOM["tap"], "internal", (0, 40, 0)))
        out.append(_p("Tap gasket", tap_parts[2], "epdm", "bought", BOM["tap"], "internal", (0, -30, 0)))
    if label:
        zl = z_foot + 0.45 * P["BKT_H"]
        lab = Pos(cx, cy - wall_r(0.45 * P["BKT_H"]) - 0.8, zl) * Rot(TAPER, 0, 0) * cp.label_plate(70.0, 90.0, 0.6)
        out.append(_p("Label: treated water, refill line, weekly chlorine rinse", lab, "label", "bought", BOM["labels"], "shell", (0, -40, 0)))
    return out


# ------------------------------------------------------------------------------------------------------------
# C1 two-bucket hollow-fibre filter on a timber stand
# ------------------------------------------------------------------------------------------------------------
# the module stands just right of the front right leg, its P-clip tabs screwed to the leg's front face (HWC-DDR-002)
MOD_X, MOD_Y = LC + T / 2 + P["MOD_OD"] / 2 + 2.0, -(LC + T / 2 + P["MOD_OD"] / 2 + 2.0)
CLIP_SCREW_X = LC
INLET_XY = (70.0, P["CLEAN_Y"] - 75.0)
VENT_XY = (-70.0, P["CLEAN_Y"] - 65.0)


def stand_parts():
    out = []
    E = (0, 0, 0)
    holes = []      # cutters for fastener holes, applied to the timber afterwards
    feet, legs, rails = [], [], []
    for sx in (1, -1):
        feet.append([f"Foot {'right' if sx > 0 else 'left'}, 45 x 45 x {P['FOOT_L']:.0f}", H.timber(T, P["FOOT_L"], T, (sx * LC, 0, T / 2))])
    for sx in (1, -1):
        for sy in (-1, 1):
            nm = f"Leg {'front' if sy < 0 else 'back'} {'right' if sx > 0 else 'left'}, 45 x 45 x {TOP - SH - T:.0f}"
            legs.append([nm, H.timber(T, T, TOP - SH - T, (sx * LC, sy * LC, T + (TOP - SH - T) / 2))])
    for sx in (1, -1):
        rails.append([f"Lower rail {'right' if sx > 0 else 'left'}, 45 x 45 x 420", H.timber(T, 420.0, T, (sx * (LC + T), 0, LOW - T / 2))])
    shelf_up = H.timber(420.0, 420.0, SH, (0, 0, TOP - SH / 2))
    low = H.timber(2 * (LC + T * 1.5), 420.0, SH, (0, 0, LOW + SH / 2))
    for sx in (1, -1):
        for sy in (1, -1):
            low = low - Pos(sx * LC, sy * LC, LOW + SH / 2) * Box(T + 1.0, T + 1.0, SH + 4)
    braces = []
    for sx in (1, -1):
        L = math.hypot(2 * LC + T, 700.0)
        ang = math.degrees(math.atan2(700.0, 2 * LC + T))
        b = Pos(sx * (LC + T / 2 + 10.0), 0, 150 + 350) * Rot(ang, 0, 0) * H.soft(Box(20.0, L, 70.0), 2.0)
        b = b & Pos(0, 0, 510) * Box(1000, 2 * LC + T, 740)       # trim the ends square, clear of the lower shelf
        braces.append([f"Diagonal brace {'right' if sx > 0 else 'left'}, 70 x 20", b])
    fast = []
    # coach screws: shelf into leg tops, feet up into legs
    for sx in (1, -1):
        for sy in (-1, 1):
            s = Pos(sx * LC, sy * LC, TOP) * cp.coach_screw(8, 80)
            fast.append(("Coach screw M8 x 80, shelf to leg", s, BOM["coach"]))
            holes.append(Pos(sx * LC, sy * LC, TOP - 40) * Cylinder(4.2, 82))
            s2 = Pos(sx * LC, sy * LC, 0) * Rot(180, 0, 0) * cp.coach_screw(8, 80)
            s2 = Pos(0, 0, 6.0) * s2
            fast.append(("Coach screw M8 x 80, foot to leg", s2, BOM["coach"]))
            holes.append(Pos(sx * LC, sy * LC, 46) * Cylinder(4.2, 86))
            holes.append(Pos(sx * LC, sy * LC, 3.0) * Cylinder(8.0, 6.2))
    # bolts: lower rails to legs, along X
    for sx in (1, -1):
        for sy in (-1, 1):
            origin = (sx * (LC + 1.5 * T), sy * LC, LOW - T / 2)
            for nm, sh in cp.hex_bolt_set(8, 2 * T):
                fast.append((nm.replace("(ISO", f"rail {('R' if sx > 0 else 'L')}{('F' if sy < 0 else 'B')} (ISO"),
                             H.placed(sh, origin, "+x" if sx > 0 else "-x"), BOM["bolts"]))
            holes.append(H.placed(Pos(0, 0, -T) * Cylinder(4.5, 2 * T + 2), origin, "+x" if sx > 0 else "-x"))
    # wood screws: lower shelf to rails, braces to legs
    for sx in (1, -1):
        for y in (-150.0, 150.0):
            fast.append(("Wood screw 5 x 30, shelf to rail", Pos(sx * (LC + T), y, LOW + SH) * H.pan_screw(5, 30), BOM["screws"]))
            holes.append(Pos(sx * (LC + T), y, LOW + SH - 14) * Cylinder(2.3, 31))
        for sy, z in ((-1, 180.0), (1, 820.0)):
            org = (sx * (LC + T / 2 + 20.0), sy * LC, z)
            fast.append(("Wood screw 5 x 30, brace to leg", H.placed(H.pan_screw(5, 30), org, "+x" if sx > 0 else "-x"), BOM["screws"]))
            holes.append(H.placed(Pos(0, 0, -15) * Cylinder(2.3, 31), org, "+x" if sx > 0 else "-x"))
    face_y = -(LC + T / 2)
    for z in (P["MOD_TOP_Z"] - 70.0, P["MOD_TOP_Z"] - P["MOD_L"] + 70.0):       # P-clip screws into the front right leg
        holes.append(Pos(CLIP_SCREW_X, face_y + 15.0, z) * Rot(90, 0, 0) * Cylinder(2.3, 32))
    cut = Compound(children=holes)

    def drill(s):
        try:
            return s - cut
        except Exception:
            return s
    for nm, s in feet:
        out.append(_p(nm, drill(s), "timber", "made", BOM["timber"], "stand", (0, 0, -80)))
    for nm, s in legs:
        out.append(_p(nm, drill(s), "timber", "made", BOM["timber"], "stand", (0, 0, 0)))
    for nm, s in rails:
        out.append(_p(nm, drill(s), "timber", "made", BOM["timber"], "stand", (0, 0, -30)))
    out.append(_p("Upper shelf, plywood 18 mm", drill(shelf_up), "plywood", "made", BOM["plywood"], "stand", (0, 0, 60)))
    out.append(_p("Lower shelf, plywood 18 mm, notched", drill(low), "plywood", "made", BOM["plywood"], "stand", (0, 0, -10)))
    for nm, s in braces:
        out.append(_p(nm, drill(s), "timber", "made", BOM["brace"], "stand", (0, 0, 0)))
    for nm, s, b in fast:
        out.append(_p(nm, s, "zinc_plated", "fastener", b, "stand"))
    return out


def raw_side_parts():
    out = []
    zf = TOP
    z_out = zf + P["BKT_FLOOR"] + P["OUTLET_H"]
    r = wall_r(P["BKT_FLOOR"] + P["OUTLET_H"])
    bh = H.bulkhead(P["BULKHEAD_BORE"], (r, 0, z_out), "+x", P["BKT_WALL"], 20.0)
    bkt = H.bucket(P, zf) - bh[4]
    E = lambda dx=0, dz=0: (dx, 0, dz)
    out.append(_p("Raw bucket (outlet hole cut, fill line marked)", bkt, "hdpe_natural", "bought", BOM["raw_bucket"], "shell", E(0, 0), RAW_BLUE))
    out.append(_p("Raw outlet bulkhead fitting", bh[0], "hdpe_natural", "bought", BOM["bulkhead"], "internal", E(70), "#C9C3B3"))
    out.append(_p("Raw outlet nut (bulkhead fitting)", bh[1], "hdpe_natural", "bought", BOM["bulkhead"], "internal", E(90)))
    out.append(_p("Inner gasket (bulkhead fitting)", bh[2], "epdm", "bought", BOM["bulkhead"], "internal", E(40)))
    out.append(_p("Outer gasket (bulkhead fitting)", bh[3], "epdm", "bought", BOM["bulkhead"], "internal", E(80)))
    out.append(_p("Strainer 250 um on the raw outlet", H.strainer(P["BULKHEAD_BORE"], (r, 0, z_out), "+x", P["BKT_WALL"]),
                  "stainless", "bought", BOM["strainer"], "internal", E(-60)))
    x_v = r + 20.0
    vb, lever = H.ball_valve(P["VALVE_BORE"], 50.0, (x_v, 0, z_out), "+x")
    out.append(_p("Ball valve 1/2 in, polypropylene", vb, "hdpe_natural", "bought", BOM["valve"], "shell", E(110), "#1F5F8B"))
    out.append(_p("Ball valve lever", lever, "hdpe_natural", "bought", BOM["valve"], "shell", E(110), "#B3261E"))
    tagp = Pos(x_v + 25.0, -7.5, z_out + 52.0) * (H.soft(Box(30.0, 2.0, 40.0), 0.6) - Pos(0, 0, 14) * Rot(90, 0, 0) * Cylinder(2.5, 4))
    out.append(_p("Valve tag: shut 30 minutes after dosing", tagp, "hdpe_natural", "made", BOM["tag"], "shell", E(110), "#E3B21C"))
    x_b = x_v + 50.0
    out.append(_p("Hose barb 3/8 in (raw)", H.barb(P["HOSE_ID"], P["BARB_BORE"], 22.0, (x_b, 0, z_out), "+x"),
                  "hdpe_natural", "bought", BOM["barbs"], "internal", E(130)))
    # raw hose: from the barb down outside the shelf edge to the module inlet (falls all the way, no high loop)
    zt = P["MOD_TOP_Z"]
    pts = [(x_b + 8.0, 0, z_out), (x_b + 40.0, -30, z_out - 25), (x_b + 45.0, -150, 820), (MOD_X + 30, MOD_Y - 10, 730),
           (MOD_X, MOD_Y, zt + 30.0), (MOD_X, MOD_Y, zt + 10.0)]
    hs, L = H.hose(pts, P["HOSE_OD"], P["HOSE_ID"], tangents=[(1, 0, 0), (0, 0, -1)])
    out.append(_p(f"Raw hose, silicone 9.5 x 14, about {L / 1000:.2f} m", hs, "epdm", "bought", BOM["hose"], "internal", E(150, -50), "#A9C7D6"))
    return out


def module_parts():
    m = H.module(P, MOD_X, MOD_Y, P["MOD_TOP_Z"])
    E = (0, -120, 0)
    out = [_p("Module top cap with raw inlet", m["cap"], "hdpe_natural", "bought", BOM["module"], "internal", E, "#2B4A43"),
           _p("Module shell", m["shell"], "polycarbonate", "bought", BOM["module"], "internal", E),
           _p("Fibre bundle, looped, outside-in, 0.1 um", m["bundle"], "insulated_white", "bought", BOM["module"], "internal", E),
           _p("Potting block (module)", m["potting"], "label", "bought", BOM["module"], "internal", E),
           _p("Module header with clean outlet", m["header"], "hdpe_natural", "bought", BOM["module"], "internal", E, "#2B4A43"),
           _p("Module bleed screw (priming vent)", m["bleed"], "hdpe_natural", "fastener", BOM["module"], "internal", E, "#B3261E")]
    face_y = -(LC + T / 2)
    for k, z in enumerate((P["MOD_TOP_Z"] - 70.0, P["MOD_TOP_Z"] - P["MOD_L"] + 70.0)):
        od = P["MOD_OD"]
        band = Pos(MOD_X, MOD_Y, z) * (Cylinder(od / 2 + 2.0, 14.0) - Cylinder(od / 2 + 0.05, 16.0))
        x0 = CLIP_SCREW_X - 12.0
        tab = Pos((x0 + MOD_X) / 2, face_y - 1.0, z) * Box(MOD_X - x0, 1.9, 14.0)
        tab = tab - Pos(MOD_X, MOD_Y, z) * Cylinder(od / 2 + 0.05, 20)
        clip = band + tab - Pos(CLIP_SCREW_X, face_y - 4, z) * Rot(90, 0, 0) * Cylinder(2.6, 12)
        out.append(_p(f"P-clip {k + 1}, nylon, 50 mm", clip, "hdpe_natural", "bought", BOM["p_clip"], "stand", (0, -80, 0)))
        out.append(_p(f"Wood screw 5 x 30, P-clip {k + 1}", H.placed(H.pan_screw(5, 30), (CLIP_SCREW_X, face_y - 2.0, z), "-y"),
                      "zinc_plated", "fastener", BOM["screws"], "stand"))
    return out


def clean_side_parts():
    out = []
    zb = P["MOD_TOP_Z"] - P["MOD_L"] - 10.0       # bottom of the header nipple
    tee, cap = H.tee_backflush((MOD_X, MOD_Y, zb), P)
    out.append(_p("Clean-side tee with luer backflush port", tee, "hdpe_natural", "bought", BOM["tee"], "internal", (0, -150, -40), "#D9D6CC"))
    # luer check valve on the backflush port (HWC-DEC-001 F5): lets the syringe pump air or water in, stroke after stroke
    cv = Pos(MOD_X, MOD_Y - 27.6, zb - 14.0) * Rot(90, 0, 0) * (H.hexagon(12.0, 6.0, -3.0) + Pos(0, 0, 7.0) * Cylinder(4.5, 8.0)
                                                               - Cylinder(1.5, 30))
    out.append(_p("Luer check valve on the backflush port", cv, "hdpe_natural", "bought", BOM["check_valve"], "internal", (0, -175, -40), "#0F766E"))
    out.append(_p("Backflush port cap", Pos(0, -15.5, 0) * cap, "hdpe_natural", "bought", BOM["tee"], "internal", (0, -200, -40), "#B3261E"))
    z_low = LOW + SH
    zt = z_low + P["BKT_H"] + P["LID_T"] + 0.2
    ix, iy = INLET_XY
    pts = [(MOD_X - 26.0, MOD_Y, zb - 14.0), (MOD_X - 60.0, MOD_Y - 12, zb + 10), (95.0, MOD_Y - 8, zt - 30.0),
           (ix + 2.0, iy - 45.0, zt + 70.0), (ix, iy - 8.0, zt + 62.0), (ix, iy, zt + 40.0), (ix, iy, zt + 22.0)]
    hs, L = H.hose(pts, P["HOSE_OD"], P["HOSE_ID"], tangents=[(-1, 0, 0), (0, 0, -1)])
    out.append(_p(f"Clean hose, silicone 9.5 x 14, about {L / 1000:.2f} m", hs, "epdm", "bought", BOM["hose"], "internal", (0, -150, 0), "#E6EEF0"))
    # pinch clamp on the clean hose, just after the tee: closed for backflush and the air test
    path_pt = (MOD_X - 50.0, MOD_Y - 8.0, zb + 1.0)
    pl = Plane(origin=path_pt, z_dir=(-1, -0.1, 0.6))
    clamp = pl.location * (H.soft(Box(30.0, 22.0, 10.0), 1.5) - Cylinder(P["HOSE_OD"] / 2 + 0.6, 14) - Pos(12, 0, 0) * Box(10, 3, 12))
    out.append(_p("Pinch clamp on the clean hose", clamp, "hdpe_natural", "bought", BOM["pinch"], "internal", (0, -170, 0), "#0F766E"))
    out += clean_bucket_set(0.0, P["CLEAN_Y"], z_low, INLET_XY, VENT_XY)
    return out


def c1_context():
    cup = H.tube(80.0, 75.0, 110.0, 2.0) + H.disc(80.0, 2.0, 0.0)
    return [_p("Cup under the tap (context)", Pos(0, P["CLEAN_Y"] - wall_r(P["TAP_H"]) - 28.0, 0) * cup, "pe_tank_white", "context", None, "context")]


def option_c1(context=True):
    parts = stand_parts() + raw_side_parts()
    parts += raw_lid_set(0.0, 0.0, TOP)
    zl = TOP + 0.45 * P["BKT_H"]
    lab = Pos(0, -wall_r(0.45 * P["BKT_H"]) - 0.8, zl) * Rot(TAPER, 0, 0) * cp.label_plate(80.0, 100.0, 0.6)
    parts.append(_p("Label: settle, dose (D), wait 30 min, open valve; no virus claim", lab, "label", "bought", BOM["labels"], "shell", (0, -40, 0)))
    parts += module_parts() + clean_side_parts()
    if context:
        parts += c1_context()
    return parts


# ------------------------------------------------------------------------------------------------------------
# C2 ceramic candles, two stacked buckets on a stool
# ------------------------------------------------------------------------------------------------------------
def option_c2(context=True):
    zs = P["STOOL_H"]
    out = clean_bucket_set(0.0, 0.0, zs, (95.0, 60.0), (-95.0, 60.0), tap=True, label=True)
    # the lower bucket's lid becomes the stack ring: keep the bucket and tap, replace the lid
    out = [q for q in out if not q["name"].startswith(("Clean lid", "Clean inlet", "Vent cap", "Insect"))]
    zr = zs + P["BKT_H"]
    ring = H.bucket_lid(P, zr, [(0, 0, 200.0)])
    zt = zr + P["LID_T"] + 0.2
    ring = ring + H.ring(274.0, 268.0, 12.0, zt)
    for k in range(8):
        ring = ring - Rot(0, 0, 45 * k + 22.5) * Pos(120, 0, zt) * Cylinder(2.0, 10)       # air vents
    out.append(_p("Stack ring (cut lid with locating lip)", ring, "hdpe_natural", "made", 40, "shell", (0, 0, 80), CLEAN_WHITE))
    zu = zt
    floor_top = zu + P["BKT_FLOOR"] + 2.0
    pos = [(P["CANDLE_R"] * math.cos(math.radians(45 + 90 * k)), P["CANDLE_R"] * math.sin(math.radians(45 + 90 * k))) for k in range(P["CANDLES"])]
    up = H.bucket(P, zu)
    for x, y in pos:
        up = up - Pos(x, y, zu + 2.5) * Cylinder(7.0, 10)
    out.append(_p("Upper (raw) bucket, four candle holes", up, "hdpe_natural", "bought", 41, "shell", (0, 0, 160), RAW_BLUE))
    for k, (x, y) in enumerate(pos, 1):
        sh, base = H.candle(P, x, y, floor_top)
        out.append(_p(f"Candle shell {k}, ceramic", sh, "concrete", "bought", 42, "internal", (0, 0, 260), "#E7DCC8"))
        out.append(_p(f"Candle base {k} with 1/4 in stem", base, "hdpe_natural", "bought", 42, "internal", (0, 0, 230)))
        out.append(_p(f"Candle gasket {k}", Pos(x, y, 0) * H.flat_gasket(40.0, 13.4, 2.0, floor_top), "epdm", "bought", 42, "internal", (0, 0, 210)))
        out.append(_p(f"Wing nut {k}", H.wing_nut(x, y, zu + 2.0), "hdpe_natural", "fastener", 42, "internal", (0, 0, 120)))
    out += raw_lid_set(0.0, 0.0, zu, prefix="Upper")
    if context:
        st = H.timber(280.0, 280.0, 30.0, (0, 0, zs - 15.0))
        for sx in (1, -1):
            for sy in (1, -1):
                st = st + H.timber(40.0, 40.0, zs - 30.0, (sx * 110, sy * 110, (zs - 30.0) / 2))
        out.append(_p("Stool (context)", st, "timber", "context", None, "context"))
        cup = H.tube(80.0, 75.0, 110.0, 2.0) + H.disc(80.0, 2.0, 0.0)
        out.append(_p("Cup (context)", Pos(0, -wall_r(P["TAP_H"]) - 28.0, 0) * cup, "pe_tank_white", "context", None, "context"))
    return out


# ------------------------------------------------------------------------------------------------------------
# C3 plastic biosand filter and a clean bucket
# ------------------------------------------------------------------------------------------------------------
def option_c3(context=True):
    od, idd, h = P["BSF_OD"], P["BSF_ID"], P["BSF_H"]
    fl = 5.0
    prof = [(0, 0), (od / 2 - 8, 0), (od / 2, 8), (od / 2, h - 10), (od / 2 + 4, h - 10), (od / 2 + 4, h), (idd / 2, h), (idd / 2, fl), (0, fl)]
    body = H.revolved(prof)
    for zz in (150, 350, 550, 750):
        body = body + Pos(0, 0, zz) * H.Torus(od / 2, 2.0)
    L = P["BSF_LAYERS"]
    z1 = fl + L["drainage_gravel"]
    z2 = z1 + L["separating_gravel"]
    z3 = z2 + L["fine_sand"]
    z_out = z3 + P["BSF_STANDING"]
    tx = idd / 2 - 14.0
    rr = idd / 2
    bh = H.bulkhead(8.0, (rr + (od - idd) / 2, 0, z_out), "+x", (od - idd) / 2, 18.0)
    body = body - bh[4]
    out = [_p("Biosand body, HDPE, 400 x 900 (outlet hole cut)", body, "hdpe_natural", "bought", 50, "shell", (0, 0, 0), "#2B4A43")]
    chan = Pos(tx, 0, (fl + z_out) / 2) * Cylinder(7.5, z_out)
    for nm, za, zb_, mat, col in (("Drainage gravel, 6 to 12 mm", fl, z1, "concrete", "#8C8A83"),
                                  ("Separating gravel, 0.7 to 6 mm", z1, z2, "sand", "#A89A7A"),
                                  ("Fine sand, under 0.7 mm, washed", z2, z3, "sand", "#C8B48A")):
        bed = H.disc(idd - 0.4, zb_ - za, za)
        try:
            bed = H.chamfer(bed.edges().group_by(H.Axis.Z)[-1], 1.0)
        except Exception:
            pass
        out.append(_p(nm, bed - chan, mat, "bought", 51, "internal", (0, 0, 0), col))
    tube_ = Pos(tx, 0, (fl + 2 + z_out - 8) / 2) * (Cylinder(7.0, z_out - 10 - fl) - Cylinder(5.0, z_out - 8))
    tube_ = tube_ + Pos(tx, 0, fl + 2) * (Cylinder(7.0, 4.0) - Cylinder(5.0, 6.0))
    elbow = Pos(tx, 0, z_out) * H.Sphere(7.0) - Pos(tx, 0, z_out) * H.Sphere(5.0)
    arm = Pos((tx + rr - 5.5) / 2, 0, z_out) * Rot(0, 90, 0) * (Cylinder(7.0, rr - 5.5 - tx) - Cylinder(5.0, rr - tx + 2))
    out.append(_p("Outlet tube, PE 14 x 10, with elbow", tube_ + elbow + arm, "hdpe_natural", "bought", 52, "internal", (0, 0, 0), "#D9D6CC"))
    out.append(_p("Outlet bulkhead fitting", bh[0], "hdpe_natural", "bought", 53, "internal", (60, 0, 0)))
    out.append(_p("Outlet nut (bulkhead fitting)", bh[1], "hdpe_natural", "bought", 53, "internal", (80, 0, 0)))
    out.append(_p("Inner gasket (bulkhead fitting)", bh[2], "epdm", "bought", 53, "internal", (40, 0, 0)))
    out.append(_p("Outer gasket (bulkhead fitting)", bh[3], "epdm", "bought", 53, "internal", (70, 0, 0)))
    zd = 790.0
    screw_holes = []
    dif = H.disc(idd - 6.0, 4.0, zd) + H.ring(idd - 6.0, idd - 20.0, 12.0, zd + 4.0) + Pos(0, 0, zd + 14) * H.soft(Box(120, 18, 16), 4)
    for i in range(-4, 5):
        for j in range(-4, 5):
            if math.hypot(i * 36, j * 36) < idd / 2 - 25 and (i, j) != (0, 0):
                dif = dif - Pos(i * 36.0, j * 36.0, zd + 2) * Cylinder(1.5, 8)
    dif = dif - Pos(0, 0, zd + 14) * Box(80, 20, 8)
    out.append(_p("Diffuser plate, perforated", dif, "hdpe_natural", "made", 54, "internal", (0, 0, 220), "#D9D6CC"))
    for k, a in enumerate((90.0, 270.0), 1):
        ang = Rot(0, 0, a) * Pos(rr - 10.0, 0, zd - 10.0) * (Box(20.0, 60.0, 2.0) + Pos(9.0, 0, -9.0) * Box(2.0, 60.0, 20.0))
        ang = H.soft(ang, 0.4)
        sc = Rot(0, 0, a) * Pos(rr - 2.0, 0, zd - 16.0) * Rot(0, -90, 0) * H.pan_screw(4, 12)
        ang = ang - Rot(0, 0, a) * Pos(rr - 1.0, 0, zd - 16.0) * Rot(0, 90, 0) * Cylinder(2.1, 30)
        screw_holes.append(Rot(0, 0, a) * Pos(rr + 4.0, 0, zd - 16.0) * Rot(0, 90, 0) * Cylinder(2.1, 14))
        out.append(_p(f"Diffuser support angle {k}, aluminium 20 x 20 x 2", ang, "aluminium", "made", 55, "internal", (0, 0, 180)))
        out.append(_p(f"Support screw {k}, 4 x 12 stainless", sc, "stainless", "fastener", 56, "internal", (0, 0, 180)))
    out[0]["shape"] = out[0]["shape"] - Compound(children=screw_holes)
    lid = H.revolved([(0, h + 0.2), (od / 2 + 7, h + 0.2), (od / 2 + 7, h - 14), (od / 2 + 9, h - 14), (od / 2 + 9, h + 4), (0, h + 4)])
    lid = lid + Pos(0, 0, h + 10) * H.soft(Box(140, 24, 14), 4)
    out.append(_p("Biosand lid", lid, "hdpe_natural", "made", 57, "shell", (0, 0, 300), "#2B4A43"))
    # clean bucket on a block beside the filter, hose from the outlet
    cx = od / 2 + 230.0
    zf = P["BLOCK_H"]
    out += clean_bucket_set(cx, 0.0, zf, (cx - 80.0, 30.0), (cx + 60.0, 70.0), d_port_xy=(cx + 30.0, -80.0))
    zt = zf + P["BKT_H"] + P["LID_T"] + 0.2
    xb = rr + (od - idd) / 2 + 18.0
    pts = [(xb - 12.0, 0, z_out), (xb + 40, 0, z_out - 15), (cx - 80.0, 30.0, zt + 70), (cx - 80.0, 30.0, zt + 22.0)]
    hs, L_ = H.hose(pts, P["HOSE_OD"], P["HOSE_ID"], tangents=[(1, 0, 0), (0, 0, -1)])
    out.append(_p("Outlet hose, silicone 9.5 x 14", hs, "epdm", "bought", 58, "internal", (0, 0, 0), "#E6EEF0"))
    out.append(_p("Hose barb 3/8 in (outlet)", H.barb(P["HOSE_ID"], P["BARB_BORE"] - 1.0, 14.0, (xb - 2.0, 0, z_out), "+x"), "hdpe_natural", "bought", 58, "internal"))
    if context:
        blk = H.timber(320.0, 320.0, zf, (cx, 0, zf / 2))
        out.append(_p("Block under the clean bucket (context)", blk, "concrete", "context", None, "context"))
    return out


@functools.lru_cache(None)
def _components(option, context=True):
    return tuple({"C1": option_c1, "C2": option_c2, "C3": option_c3}[option](context))


def components(option="C1", context=True):
    return [dict(q) for q in _components(option, context)]


if __name__ == "__main__":
    import time
    for o in (sys.argv[1:] or list(OPTIONS)):
        t = time.time()
        ps = components(o)
        print(o, len([p for p in ps if p["kind"] != "context"]), "parts", f"{time.time() - t:.1f} s")
        for p in ps:
            bb = p["shape"].bounding_box()
            print(f"   {p['kind']:8s} {p['name'][:52]:52s} x {bb.min.X:6.0f}..{bb.max.X:6.0f} y {bb.min.Y:6.0f}..{bb.max.Y:6.0f} z {bb.min.Z:6.0f}..{bb.max.Z:6.0f} {cp.mass_kg(p):7.3f} kg")
