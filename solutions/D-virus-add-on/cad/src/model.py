"""Helpful Water D: chlorine add-on for viruses. Parametric model (kit 1.9 interface, STANDARDS section 24), D3.

Run from the solution folder:  python .kit/cad_check.py --export
Every main dimension is in PARAMS; docs/04-calcs/sizing.py (HWD-CAL-001) and docs/04-calcs/stem_check.py read it.

Options (HWD-OPT-001; the choice is proposed, awaiting Amish):
  D1  Tablet dose cap: a cap for the 28 mm PCO 1881 bottle neck (B's neck; also the fill port proposed for C's raw
      bucket lid) with a keyed tablet well that takes one NaDCC tablet matched to the container (1 L or 20 L), a
      clear screw plug to see the tablet dissolve, and a flip-over ball timer that runs about 45 minutes at 25 C (at least 30 up to 40 C).
  D2  Metered liquid doser: a 150 mL bottle of 1.25 % sodium hypochlorite with a squeeze-to-fill metering chamber
      (3.0 mL per 20 L) and a dropper tip (5 drops per 1 L), carrying the same flip-over ball timer.
  D3  Erosion feeder: a perforated tube of chlorine tablets hung in C's 20 L raw-water bucket with a sleeve that
      sets how many holes are open. Dropped on the STEM check (HWD-STM-001 X1): a constant release cannot hold the
      dose in range when the standing time varies from 30 minutes to a day. Modelled to D3 so it can be compared.

Axes: Z up. D1: the bottle neck's sealing lip at z = 0, the cap above it. D2 and D3 stand on a table at z = 0.
Fasteners: window screws (D1, D2), flip-cap hinge pin (D2), sleeve set screw and cap screws (D3).
CONCEPT, NOT FOR FABRICATION.

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
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

TITLE = "Helpful Water D: chlorine add-on for viruses"
OPTIONS = {"D1": "Tablet dose cap with ball timer", "D2": "Metered liquid doser with ball timer",
           "D3": "Erosion feeder in the raw bucket (dropped)"}
PRINCIPLES = {
    "D1": "One NaDCC tablet matched to the container (1 L or 20 L) sits in a keyed well in the bottle or bucket-port "
          "cap; shaking dissolves it to about 2 mg/L free chlorine; a flip-over ball timer shows the 30 minute wait "
          "before the water goes to the filter.",
    "D2": "A squeeze fills a 3.0 mL chamber from a bottle of 1.25 % sodium hypochlorite (CDC Safe Water System "
          "dose for 20 L); a dropper tip gives 5 drops for 1 L; the same ball timer shows the wait.",
    "D3": "Chlorine tablets in a perforated tube hung in the raw-water bucket dissolve slowly; a sleeve sets the "
          "open holes. Dropped: the dose grows with standing time and cannot stay in range.",
}
CHOSEN = "D1"   # carried to the drawing, BOM and build plan; the concept choice itself is proposed, awaiting Amish
OPTION_VIEWS = {"D1": dict(el=18, az=-55, scale="hand", keep_context=True),
                "D2": dict(el=18, az=-55, scale="hand", keep_context=True, ground_z=0),
                "D3": dict(el=22, az=-55, scale="none", keep_context=True, ground_z=0)}
# O-rings and gaskets are modelled at their compressed fit, so they touch their glands; the timer fluid fills its
# tube; threads interleave at half a pitch; the tether and labels lie on the faces they are stuck or snapped to.
ALLOWED_CONTACTS = [("O-ring", ""), ("liner", ""), ("gasket", ""), ("Timer fluid", ""), ("Tether", ""), ("label", ""),
                    ("Label", ""), ("Tablet", "well"), ("Tablet", "feeder"), ("Tablet", "Follower"), ("spring", ""),
                    ("Cord", ""), ("Dip tube", ""), ("Dropper tip", "")]

PARAMS = {
    # bottle neck (PCO 1881, approximate; hw_parts.NECK)
    "NECK_T": H.NECK["T"], "NECK_BORE": H.NECK["BORE"], "NECK_PITCH": H.NECK["PITCH"], "NECK_H_1881": 17.0,
    "BOTTLE_D": 80.0, "BOTTLE_H": 262.0, "BOTTLE_L": 1.0,
    # dose cap body (D1) and doser head (D2): skirt, deck, crown
    "SKIRT_OD": 36.0, "SKIRT_ID": 28.2, "SKIRT_H": 17.0, "DECK": (1.5, 5.5), "DECK_BORE": 17.0, "CROWN_OD": 40.0,
    "CROWN_TOP": 30.0, "WELL_BORE": 20.4, "PLUG_BORE": 22.4, "PLUG_THREAD_Z": 23.0, "PLUG_PITCH": 2.0,
    # tablet wells (keyed so a 20 L tablet cannot enter the 1 L well; HWD-DEC-001 F2)
    "WELL_1L": 9.5, "WELL_20L": 14.5, "WELL_TOP": 21.5, "PLUG_STOP": 21.0,
    "FREE_H": {"1L": 8.0, "20L": 11.0},             # height under the plug stop: two tablets fit, three do not (F3)
    "INSERT_GROOVE": 17.9,                          # O-ring groove root; 22 % squeeze in the 20.4 bore (F5, F10)
    "ORING_CS": (1.6, 0.08), "FIT_TOL": (0.05, 0.03),   # O-ring section and tolerance; bore and groove tolerance (F10)
    # tablets (NaDCC); physical sizes are assumed and are measured from the bought strips (HWD-DEC-001 C1)
    "TAB_1L": dict(nadcc_mg=3.5, cl_mg=2.0, d=8.0, t=3.5), "TAB_20L": dict(nadcc_mg=67.0, cl_mg=40.0, d=13.0, t=5.0),
    # ball timer (flip-over; sizes set by HWD-CAL-001 section 5)
    "TIMER_AXIS": (24.25, 0.0, 17.75), "TIMER_TUBE": (6.0, 4.0, 18.0), "TIMER_CAP_T": 1.5, "BALL_D": 2.0,
    "TIMER_SLOT": (20.5, 28.0, 14.0, 6.5, 29.0),    # x0, x1, half width in y, z0, z1 (cap coordinates)
    "BOSS": (19.0, 28.0, 17.5),                     # x0, x1, half width in y
    # D2 doser
    "DOSER_BOTTLE": (50.0, 110.0), "CHAMBER": (22.0, 18.0, 24.0), "STANDPIPE": (5.0, 2.5, 12.8), "DOSE_ML": 3.0,
    "HYPO_PCT": 1.25, "DROP_ORIFICE": 2.0, "DROPS_1L": 5,   # Tate drop from a 2.0 mm orifice (F9)
    # D3 feeder in a 20 L bucket
    "BUCKET": (300.0, 262.0, 340.0), "FEEDER_TUBE": (32.0, 26.6, 160.0), "FEEDER_Z": 70.0, "FEED_TAB": (25.0, 12.0),
    "FEED_HOLES": 12,
}
P = PARAMS


def _p(name, shape, mat, kind="made", bom=None, group="shell", explode=(0, 0, 0), color=None):
    return part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode, color=color)


TABLET = dict(mat="hdpe_natural", color="#F4F4EE")   # pressed tablet: white; density near a polymer is close enough here


def _edge(shape, r=0.4):
    return cp.break_edges(shape, r)


# ------------------------------------------------------------------------------------------------------------
# Shared: cap body (skirt on the neck, deck, crown with a timer boss) and the flip-over ball timer.
# Local coordinates: the neck's sealing lip at z = 0.
# ------------------------------------------------------------------------------------------------------------
def crown_body(well=True, chamber_seat=False, windows=False):
    d0, d1 = P["DECK"]
    body = H.tube(P["SKIRT_OD"], P["SKIRT_ID"], P["SKIRT_H"], -15.5)
    body = body + H.thread(P["SKIRT_ID"] / 2, 1.15, P["NECK_PITCH"], 1.75, internal=True, z0=-12.15)
    for k in range(12):
        body = body + Rot(0, 0, 30 * k + 15) * Pos(P["SKIRT_OD"] / 2, 0, -7.0) * Box(1.6, 2.4, 15.0)
    body = body + H.disc(P["CROWN_OD"], d1 - d0, d0)
    zt = P["CROWN_TOP"]
    if well:
        crown = H.tube(P["CROWN_OD"], P["WELL_BORE"], P["PLUG_THREAD_Z"] - 0.5 - d1, d1)
        crown = crown + H.tube(P["CROWN_OD"], P["PLUG_BORE"], zt - (P["PLUG_THREAD_Z"] - 0.5), P["PLUG_THREAD_Z"] - 0.5)
        crown = crown + H.thread(P["PLUG_BORE"] / 2 + 0.05, 1.0, P["PLUG_PITCH"], 3.0, internal=True, z0=P["PLUG_THREAD_Z"] + 1.0)
        body = body + crown - H.disc(P["DECK_BORE"], 10.0, -1.0)
        core = H.ring(36.0, 28.4, 12.0, zt - 12.0) - Pos(16.0, 0, zt - 6.0) * Box(14.0, 38.0, 14.0)
        body = body - core                                  # coring groove from the top: even walls for moulding
    else:
        crown = H.tube(P["CROWN_OD"], 26.0, zt - d1, d1)
        body = body + crown
        if windows:
            for a in (180, 135, 225):
                body = body - Rot(0, 0, a) * Pos(17.5, 0, 17.0) * Box(8.0, 9.0, 14.0)
    if chamber_seat:
        seat = H.tube(17.9, 14.0, 3.0, d1)
        body = body + seat - H.ring(18.0, 16.4, 1.6, d1 + 0.7)
        body = body - H.disc(5.2, 10.0, -1.0)            # standpipe socket through the deck (dip tube inside it)
        body = body - Pos(-11.0, 0, 0) * H.disc(2.0, 10.0, -1.0)   # air return bore
    # timer boss and slot
    x0, x1, hw = P["BOSS"]
    sx0, sx1, shw, sz0, sz1 = P["TIMER_SLOT"]
    boss = Pos((x0 + x1) / 2, 0, (d1 + zt) / 2) * Box(x1 - x0, 2 * hw, zt - d1)
    try:
        boss = fillet(boss.edges().filter_by(Axis.Z).group_by(Axis.X)[-1], 3.0)
    except Exception:
        pass
    body = body + boss
    body = body - Pos((sx0 + sx1 + 0.2) / 2, 0, (sz0 + sz1) / 2) * Box(sx1 + 0.2 - sx0, 2 * shw, sz1 - sz0)
    ax, ay, az = P["TIMER_AXIS"]
    body = body - Pos(sx0 - 0.8, 0, az) * Rot(0, 90, 0) * Cylinder(1.1, 2.0)            # inner trunnion bearing
    for sy in (1, -1):
        body = body - Pos(x1 - 3.0, sy * 15.75, az) * Rot(0, 90, 0) * Cylinder(0.8, 6.2)  # pilot holes, window screws
    return body


def timer_parts(z_off=0.0, bom0=None, explode=(0, 0, 0)):
    """Flip-over ball timer: clear tube, two end caps with O-rings, a 2 mm stainless ball in silicone fluid, a hub
    with trunnions, a clear window plate with two screws and a scale label. Returns part dicts (cap coordinates
    shifted by z_off)."""
    B = bom0 or {}
    ax, ay, az = P["TIMER_AXIS"]
    az = az + z_off
    to, ti, tl = P["TIMER_TUBE"]
    ct = P["TIMER_CAP_T"]
    zb, zt = az - tl / 2, az + tl / 2
    E = lambda d: (explode[0] + d[0], explode[1] + d[1], explode[2] + d[2])
    T = lambda s: Pos(ax, ay, 0) * s
    out = []
    tube = H.tube(to, ti, tl, zb)
    try:
        tube = chamfer(tube.edges().group_by(Axis.Z)[0] + tube.edges().group_by(Axis.Z)[-1], 0.2)
    except Exception:
        pass
    out.append(_p("Timer tube, clear", T(tube), "polycarbonate", "made", B.get("tube"), "shell", E((0, 0, 0))))
    for i, (zc, sgn) in enumerate(((zb, -1), (zt, 1))):
        cap = H.disc(to, ct, zc if sgn > 0 else zc - ct) + H.disc(ti - 0.05, 1.5, zc - 1.5 if sgn > 0 else zc)
        cap = cap - H.ring(ti, ti - 1.0, 0.6, (zc - 1.0) if sgn > 0 else (zc + 0.4))
        out.append(_p(f"Timer end cap {'top' if sgn > 0 else 'bottom'}", T(_edge(cap, 0.2)), "hdpe_natural", "made",
                      B.get("cap"), "shell", E((0, 0, 6 * sgn))))
        oz = (zc - 0.7) if sgn > 0 else (zc + 0.7)
        out.append(_p(f"Timer end O-ring {'top' if sgn > 0 else 'bottom'}, 3.0 x 0.5", T(H.o_ring(3.0, 0.5, oz)), "epdm",
                      "bought", B.get("oring"), "internal", E((0, 0, 4 * sgn))))
    zf0, zf1 = zb + 1.5, zt - 1.5
    bd = P["BALL_D"]
    ball_z = zf1 - bd / 2 - 0.05
    ball = Pos(0, 0, ball_z) * cp.Sphere(bd / 2) if hasattr(cp, "Sphere") else None
    if ball is None:
        from build123d import Sphere
        ball = Pos(0, 0, ball_z) * Sphere(bd / 2)
    fluid = H.disc(ti - 0.02, zf1 - zf0, zf0)
    try:
        fluid = chamfer(fluid.edges(), 0.3)
    except Exception:
        pass
    fluid = fluid - ball
    out.append(_p("Timer ball, 2 mm stainless", T(ball), "stainless", "bought", B.get("ball"), "internal", E((0, 0, 10))))
    out.append(_p("Timer fluid, silicone (sealed)", T(fluid), "polycarbonate", "bought", B.get("fluid"), "internal", E((0, 0, 0))))
    sx0, sx1, shw, sz0, sz1 = P["TIMER_SLOT"]
    hub = Pos(0, 0, az) * Box(7.2, 8.0, 6.0) - Pos(0, 0, az) * Cylinder(to / 2 + 0.01, 7.0)
    hub = hub + Pos(-3.6 - 0.55, 0, az) * Rot(0, 90, 0) * Cylinder(1.0, 1.1) + Pos(3.6 + 0.55, 0, az) * Rot(0, 90, 0) * Cylinder(1.0, 1.1)
    hub = _edge(hub, 0.3)
    out.append(_p("Timer hub with trunnions", T(hub), "hdpe_natural", "made", B.get("hub"), "shell", E((0, -12, 0))))
    x0, x1, hw = P["BOSS"]
    zc = (P["DECK"][1] + P["CROWN_TOP"]) / 2 + z_off
    win = Pos(x1 + 0.75, 0, zc) * Box(1.5, 2 * hw, P["CROWN_TOP"] - P["DECK"][1])
    win = win - Pos(x1 + 0.75, 0, az) * Rot(0, 90, 0) * Cylinder(1.1, 3.0)
    for sy in (1, -1):
        win = win - Pos(x1 + 0.75, sy * 15.75, az) * Rot(0, 90, 0) * Cylinder(1.1, 3.0)
    out.append(_p("Timer window, clear", _edge(win, 0.3), "polycarbonate", "made", B.get("window"), "shell", E((18, 0, 0))))
    for i, sy in enumerate((1, -1)):
        s = Pos(x1 + 1.5, sy * 15.75, az) * Rot(0, 90, 0) * H.hex_socket_screw(2.0, 6.0)
        out.append(_p(f"Window screw {i + 1}, 2.2 x 6.5 pan head", s, "stainless", "fastener", B.get("screw"), "shell", E((28, 0, 0))))
    lab = Pos(x1 + 1.55, 0, zc) * Box(0.1, 2 * hw - 9.0, P["CROWN_TOP"] - P["DECK"][1] - 2.0)
    lab = lab - Pos(x1 + 1.55, 0, az) * Box(0.4, 9.0, 24.0)       # clear strip over the tube
    out.append(_p("Timer scale label (START, 30 min)", lab, "label", "bought", B.get("label"), "shell", E((30, 0, 0))))
    return out


# ------------------------------------------------------------------------------------------------------------
# D1 tablet dose cap
# ------------------------------------------------------------------------------------------------------------
BOM = {"cap": 1, "liner": 2, "insert1": 3, "insert20": 4, "oring_insert": 5, "plug": 6, "oring_plug": 7, "tether": 8,
       "tube": 9, "tcap": 10, "toring": 11, "ball": 12, "fluid": 13, "hub": 14, "window": 15, "screw": 16,
       "tlabel": 17, "label": 18, "tab1": 19, "tab20": 20}
TIMER_BOM = dict(tube=BOM["tube"], cap=BOM["tcap"], oring=BOM["toring"], ball=BOM["ball"], fluid=BOM["fluid"],
                 hub=BOM["hub"], window=BOM["window"], screw=BOM["screw"], label=BOM["tlabel"])


def well_floor(size):
    return P["PLUG_STOP"] - P["FREE_H"][size]


def well_insert(bore, colour_ribs=1, size="1L"):
    d1 = P["DECK"][1]
    z0, h = d1, P["WELL_TOP"] - d1
    zf = well_floor(size)
    s = H.disc(P["WELL_BORE"] - 0.4, h, z0) - H.disc(bore, P["WELL_TOP"] - zf + 1.0, zf)
    s = s - H.ring(P["WELL_BORE"] - 0.3, P["INSERT_GROOVE"], 1.9, P["WELL_TOP"] - 4.5)   # O-ring groove
    for k in range(4):                                                # floor slots, narrower than any tablet
        s = s - Rot(0, 0, 45 + 90 * k) * Pos(2.8, 0, (z0 + zf) / 2) * Box(3.4, 1.5, zf - z0 + 2.0)
    s = s - H.disc(1.6, zf - z0 + 2.0, z0 - 1.0)
    if zf - z0 > 4.0:                                                # hollow a thick floor from below (even walls)
        s = s - H.ring(18.4, 10.2, zf - z0 - 1.5, z0 - 0.01)
    for k in range(colour_ribs):                                      # key ribs on the top face show the size
        s = s - Rot(0, 0, 120 * k) * Pos((bore / 2 + P["WELL_BORE"] / 2) / 2, 0, z0 + h) * Box(1.0, 1.0, 1.2)
    return _edge(s, 0.2)


def plug():
    zt = P["CROWN_TOP"]
    zc0 = P["PLUG_THREAD_Z"] - 0.5
    core = H.disc(20.0, zt - zc0, zc0) + H.disc(9.0, zc0 - P["PLUG_STOP"] + 0.01, P["PLUG_STOP"])   # stop spigot (F3)
    core = core + H.thread(10.0 - 0.05, 1.0, P["PLUG_PITCH"], 2.6, internal=False, z0=P["PLUG_THREAD_Z"] + 2.0)
    head = H.disc(27.0, 5.0, zt)
    head = head - H.ring(26.2, 22.6, 1.3, zt - 0.01)
    for k in range(12):
        head = head - Rot(0, 0, 30 * k) * Pos(13.5, 0, zt + 2.5) * Cylinder(0.9, 6.0)
    lug = Pos(-15.6, 0, zt + 4.0) * (Box(4.0, 5.0, 2.0) - Pos(-0.6, 0, 0) * Cylinder(1.0, 3.0))
    return _edge(core + head + lug, 0.25)


def tether():
    zt = P["CROWN_TOP"]
    band = H.ring(41.4, 40.0, 2.0, zt - 4.0)
    strap = Pos(-21.0, 0, zt + 0.25) * Box(1.2, 3.0, 8.5)
    top = Pos(-17.65, 0, zt + 5.4) * Box(7.9, 3.0, 1.2)
    try:
        return band + strap + top
    except Exception:
        return Compound([band, strap, top])


def crown_label():
    shell = H.tube(40.3, 40.02, 15.0, 9.5)
    return shell & Pos(-16.0, 0, 17.0) * Box(22.0, 44.0, 20.0)


def option_d1(context=True, insert="1L"):
    E = lambda dz: (0, 0, dz)
    tab = P["TAB_1L"] if insert == "1L" else P["TAB_20L"]
    bore = P["WELL_1L"] if insert == "1L" else P["WELL_20L"]
    d1 = P["DECK"][1]
    out = [
        _p("Dose cap body with PCO 1881 thread and timer boss", _edge(crown_body(), 0.3), "hdpe_natural", "made", BOM["cap"], "shell", E(-40)),
        _p("Neck liner (flat, silicone)", H.flat_gasket(27.6, 20.5, 1.5, 0.0), "epdm", "bought", BOM["liner"], "internal", E(-60)),
        _p("Tablet well insert, 1 L (blue, 9.5 mm bore)" if insert == "1L" else "Tablet well insert, 20 L (orange, 14.5 mm bore)",
           well_insert(bore, 1 if insert == "1L" else 2, insert), "hdpe_natural", "made",
           BOM["insert1"] if insert == "1L" else BOM["insert20"], "internal", E(30), "#2563EB" if insert == "1L" else "#EA580C"),
        _p("Well insert O-ring 17.2 x 1.6", H.o_ring(P["INSERT_GROOVE"], 1.6, P["WELL_TOP"] - 3.55), "epdm", "bought", BOM["oring_insert"], "internal", E(38)),
        _p("Tablet, NaDCC 3.5 mg (1 L)" if insert == "1L" else "Tablet, NaDCC 67 mg (20 L)",
           H.tablet(tab["d"], tab["t"], well_floor(insert) + 0.05), TABLET["mat"], "bought", BOM["tab1"] if insert == "1L" else BOM["tab20"], "internal", E(50),
           TABLET["color"]),
        _p("Well plug, clear, with tether lug", plug(), "polycarbonate", "made", BOM["plug"], "shell", E(70)),
        _p("Plug O-ring 22.6 x 1.6", H.o_ring(22.6, 1.6, P["CROWN_TOP"] + 0.8), "epdm", "bought", BOM["oring_plug"], "internal", E(62)),
        _p("Tether band and strap", tether(), "epdm", "made", BOM["tether"], "shell", E(45)),
        _p("Pictogram label on the crown", crown_label(), "label", "bought", BOM["label"], "shell", (-20, 0, 0)),
    ]
    out += timer_parts(0.0, TIMER_BOM, (0, 0, 0))
    if context:
        out += d1_context()
    return out


def d1_context():
    import context_parts
    bottle = H.pet_bottle_1l(0.0, P["BOTTLE_D"], P["BOTTLE_H"])
    out = [_p("PET bottle 1 L (context)", bottle, "glass", "context", None, "context")]
    hand = context_parts.forearm_hand(side="right", pose="grip", grip_d=80.0, forearm_len=110.0)
    hand = Pos(-78, -44, -150) * Rot(90, 0, 0) * hand
    out.append(_p("Hand (scale)", hand, "skin", "context", None, "context"))
    return out


# ------------------------------------------------------------------------------------------------------------
# D2 metered liquid doser (bottle stands on z = 0; its neck lip at Z2)
# ------------------------------------------------------------------------------------------------------------
Z2 = P["DOSER_BOTTLE"][1]
BOM2 = {"bottle": 31, "liner": 32, "head": 33, "dip": 34, "standpipe": 35, "chamber": 36, "oring_ch": 37, "spout": 38,
        "flip": 39, "pin": 40, "dropper": 41, "label": 42}
TIMER_BOM2 = dict(tube=43, cap=44, oring=45, ball=46, fluid=47, hub=48, window=49, screw=50, label=51)


def option_d2(context=True):
    S = lambda s: Pos(0, 0, Z2) * s
    E = lambda dz: (0, 0, dz)
    d1 = P["DECK"][1]
    co, ci, chh = P["CHAMBER"]
    so, si, sh = P["STANDPIPE"]
    out = [
        _p("Doser bottle 150 mL, 1.25 % sodium hypochlorite (opaque HDPE)", H.small_bottle(Z2, *P["DOSER_BOTTLE"]),
           "pe_tank_white", "bought", BOM2["bottle"], "shell", E(-60)),
        _p("Neck liner (flat, silicone)", S(H.flat_gasket(27.6, 20.5, 1.5, 0.0)), "epdm", "bought", BOM2["liner"], "internal", E(-20)),
        _p("Doser head with PCO 1881 thread, chamber seat and timer boss",
           S(_edge(crown_body(well=False, chamber_seat=True, windows=True), 0.3)), "hdpe_natural", "made", BOM2["head"], "shell", E(0)),
    ]
    dip = H.tube(4.0, 2.5, Z2 + d1 - 1.0 - 3.0, 3.0)
    out.append(_p("Dip tube 4 x 2.5 PE", dip, "hdpe_natural", "bought", BOM2["dip"], "internal", E(-40)))
    sp = H.tube(so, si, sh, d1) + H.tube(5.15, 4.05, d1 - 0.5, 0.5) + H.ring(7.0, si, 0.8, d1)
    out.append(_p("Standpipe (sets the 3.0 mL level)", S(_edge(sp, 0.15)), "hdpe_natural", "made", BOM2["standpipe"], "internal", E(20)))
    ch = H.tube(co, ci, chh, d1 + 0.8)
    for k in range(4):                                     # graduation ribs on the outside (3 mL line)
        ch = ch + Rot(0, 0, 90 * k + 45) * Pos(co / 2, 0, d1 + 0.8 + sh) * Box(0.8, 3.0, 0.6)
    out.append(_p("Metering chamber, clear, 3.0 mL", S(_edge(ch, 0.2)), "polycarbonate", "made", BOM2["chamber"], "shell", E(30)))
    out.append(_p("Chamber O-ring 16.4 x 1.6", S(H.o_ring(16.4, 1.6, d1 + 1.5)), "epdm", "bought", BOM2["oring_ch"], "internal", E(25)))
    zs = d1 + 0.8 + chh
    spc = H.disc(co + 3.0, 2.0, zs) + H.tube(co + 3.0, co + 0.2, 4.0, zs - 4.0)
    spc = spc + Pos(4.5, 0, 0) * H.tube(6.0, 4.0, 7.0, zs + 2.0) + Pos(-4.5, 0, 0) * H.tube(5.0, 3.2, 4.0, zs + 2.0)
    spc = spc - Pos(4.5, 0, 0) * H.disc(4.0, 3.0, zs - 0.5) - Pos(-4.5, 0, 0) * H.disc(3.2, 3.0, zs - 0.5)
    lug = Pos(0, 13.5, zs + 3.0) * (Box(5.0, 3.0, 4.0) - Rot(0, 90, 0) * Cylinder(0.8, 6.0))
    lug = lug + Pos(0, 12.2, zs + 1.0) * Box(5.0, 1.0, 2.0)
    out.append(_p("Spout cap with pour spout and dropper port", S(_edge(spc + lug, 0.2)), "hdpe_natural", "made", BOM2["spout"], "shell", E(50)))
    drop = Pos(-4.5, 0, 0) * (H.disc(3.15, 3.5, zs + 2.0) + Pos(0, 0, zs + 5.5) * chamfer(Cylinder(2.5, 4.0).edges().group_by(Axis.Z)[-1], 1.0)
                              - H.disc(1.2, 12.0, zs))
    out.append(_p("Dropper tip insert, LDPE, 2.0 mm orifice", S(drop), "hdpe_natural", "bought", BOM2["dropper"], "internal", E(60)))
    flip = H.disc(co + 3.0, 1.5, zs + 10.0) + H.tube(co + 3.0, co, 7.5, zs + 2.5)
    flip = flip - Pos(0, 13.5, zs + 3.5) * Box(5.4, 3.4, 6.0)
    for sx in (1, -1):
        flip = flip + Pos(sx * 3.3, 13.5, zs + 3.0) * (Box(1.5, 4.0, 4.0) - Rot(0, 90, 0) * Cylinder(0.8, 3.0))
    flip = flip + Pos(0, -12.5, zs + 10.5) * Box(6.0, 3.0, 1.5)
    out.append(_p("Flip cap, child-resistant latch", S(_edge(flip, 0.2)), "hdpe_natural", "made", BOM2["flip"], "shell", E(70), "#B91C1C"))
    pin = Pos(0, 13.5, zs + 3.0) * Rot(0, 90, 0) * H.pin(1.5, 8.6)
    out.append(_p("Flip cap hinge pin 1.5 x 8.6, stainless", S(pin), "stainless", "fastener", BOM2["pin"], "shell", (0, 20, 70)))
    lab = H.tube(50.3, 50.02, 55.0, 25.0) & Pos(-12.0, 0, 52.5) * Box(30.0, 54.0, 56.0)
    out.append(_p("Dose label (pictograms, 1 L and 20 L)", lab, "label", "bought", BOM2["label"], "shell", (-30, 0, 0)))
    for q in timer_parts(Z2, TIMER_BOM2, (0, 0, 0)):
        out.append(q)
    if context:
        import context_parts
        hand = context_parts.forearm_hand(side="right", pose="grip", grip_d=50.0)
        hand = Pos(-55, -30, -10) * Rot(90, 0, 0) * hand
        out.append(_p("Hand (scale)", hand, "skin", "context", None, "context"))
    return out


# ------------------------------------------------------------------------------------------------------------
# D3 erosion feeder hung in C's 20 L raw-water bucket (dropped)
# ------------------------------------------------------------------------------------------------------------
BOM3 = {"hook": 61, "cord": 62, "clip": 63, "topcap": 64, "tube": 65, "sleeve": 66, "setscrew": 67, "botcap": 68,
        "ballast": 69, "ballast_screw": 70, "tablet": 71, "follower": 72, "spring": 73, "oring": 74, "tag": 75, "washer": 76}


def option_d3(context=True):
    bt, bb, bh = P["BUCKET"]
    to, ti, tl = P["FEEDER_TUBE"]
    z0 = P["FEEDER_Z"]
    x = 0.0
    E = lambda dz: (0, 0, dz)
    out = []
    tube = H.tube(to, ti, tl, z0)
    for r in range(3):
        for k in range(P["FEED_HOLES"] // 3):
            a = 90 * k + 45 * (r % 2)
            tube = tube - Rot(0, 0, a) * Pos(to / 2 - 1.3, 0, z0 + 12 + 14 * r) * Rot(0, 90, 0) * Cylinder(2.5, 6.0)
    tube = tube + H.thread(to / 2 - 0.05, 1.0, 2.5, 3.0, internal=False, z0=z0 + tl - 9.0)
    tube = tube - Pos(-(to / 2 - 1.3), 0, z0 + 5.0) * Rot(0, 90, 0) * Cylinder(1.4, 4.0)
    out.append(_p("Feeder tube, PVC 32 x 2.7, 12 holes 5 mm", _edge(tube, 0.3), "hdpe_natural", "made", BOM3["tube"], "shell", E(0)))
    sl = H.tube(to + 4.4, to + 0.4, 50.0, z0 + 11.0)
    for k in range(4):
        sl = sl - Rot(0, 0, 90 * k) * Pos(to / 2 + 1.0, 0, z0 + 11.0 + 23.0) * Box(6.0, 9.0, 40.0)
    sl = sl - Pos(0, -(to / 2 + 1.2), z0 + 57.0) * Rot(90, 0, 0) * Cylinder(1.4, 6.0)
    out.append(_p("Adjusting sleeve with four windows", _edge(sl, 0.3), "hdpe_recycled", "made", BOM3["sleeve"], "shell", E(0)))
    out.append(_p("Sleeve set screw M3 x 3, flat point", Pos(0, -(to / 2 + 2.2), z0 + 57.0) * Rot(90, 0, 0) * H.hex_socket_screw(3.0, 2.1),
                  "stainless", "fastener", BOM3["setscrew"], "shell", (0, -20, 0)))
    bc = H.disc(to + 6.0, 6.0, z0 - 6.0) + H.tube(to + 6.0, to + 0.2, 10.0, z0) - H.disc(14.0, 4.0, z0 - 6.01)
    bc = bc - Pos(-(to / 2 + 1.8), 0, z0 + 5.0) * Rot(0, 90, 0) * Cylinder(1.4, 6.0)
    out.append(_p("Bottom cap with ballast seat", _edge(bc, 0.4), "hdpe_natural", "made", BOM3["botcap"], "shell", E(-40)))
    out.append(_p("Ballast disc, stainless 30 x 4", _edge(H.disc(30.0, 4.0, z0 - 10.0) - H.disc(3.2, 6.0, z0 - 11.0), 0.4), "stainless",
                  "bought", BOM3["ballast"], "internal", E(-60)))
    out.append(_p("Ballast screw M3 x 10", Pos(0, 0, z0 - 10.0) * Rot(180, 0, 0) * H.hex_socket_screw(3.0, 8.0), "stainless", "fastener",
                  BOM3["ballast_screw"], "internal", E(-75)))
    out.append(_p("Cap retaining screw M3 x 6", Pos(-(to / 2 + 3.0), 0, z0 + 5.0) * Rot(0, -90, 0) * H.hex_socket_screw(3.0, 4.0),
                  "stainless", "fastener", BOM3["setscrew"], "shell", (-20, 0, -40)))
    out.append(_p("Bottom cap O-ring 26 x 2", H.o_ring(26.6, 2.0, z0 + 2.0), "epdm", "bought", BOM3["oring"], "internal", E(-30)))
    fd, ft = P["FEED_TAB"]
    for i in range(3):
        out.append(_p(f"Tablet {i + 1}, calcium hypochlorite 25 x 12 (in feeder)", H.tablet(fd, ft, z0 + 0.5 + i * (ft + 0.3)), TABLET["mat"],
                      "bought", BOM3["tablet"], "internal", E(10 + 15 * i), TABLET["color"]))
    zf = z0 + 0.5 + 3 * (ft + 0.3)
    out.append(_p("Follower disc", _edge(H.disc(ti - 0.6, 2.0, zf) + H.disc(8.0, 4.0, zf + 2.0), 0.3), "hdpe_natural", "made", BOM3["follower"], "internal", E(60)))
    zs0, zs1 = zf + 6.0, z0 + tl - 2.0
    spring = Pos(0, 0, zs0) * __import__("build123d").Helix(8.0, zs1 - zs0, 8.0)
    from build123d import sweep as _sw, Circle as _C, Plane as _Pl
    try:
        prof = _Pl(origin=(8.0, 0, zs0), z_dir=(0, 1, 0)) * _C(0.6)
        sp = _sw(prof.face() if hasattr(prof, "face") else prof, Pos(0, 0, 0) * spring)
    except Exception:
        sp = H.ring(17.2, 14.8, zs1 - zs0, zs0)
    out.append(_p("Follower spring, stainless", sp, "stainless", "bought", BOM3["spring"], "internal", E(80)))
    tc = H.disc(to + 6.0, 4.0, z0 + tl) + H.tube(to + 6.0, to + 2.2, 10.0, z0 + tl - 10.0)
    tc = tc + H.thread(to / 2 + 1.1 + 0.05, 1.0, 2.5, 3.0, internal=True, z0=z0 + tl - 7.75)
    tc = tc + Pos(0, 0, z0 + tl + 4.0) * (Pos(0, 0, 5.0) * Box(4.0, 14.0, 10.0) - Pos(0, 0, 6.0) * Rot(0, 90, 0) * Cylinder(3.0, 6.0))
    out.append(_p("Top cap with cord eye", _edge(tc, 0.4), "hdpe_natural", "made", BOM3["topcap"], "shell", E(40)))
    out.append(_p("Top cap O-ring 26 x 2", H.o_ring(28.4, 1.5, z0 + tl - 11.0), "epdm", "bought", BOM3["oring"], "internal", E(30)))
    # hook on the bucket rim at x = +rim, cord from the top-cap eye up to it
    xr = bt / 2
    hk = Pos(xr - 2.0, 0, bh - 6.0) * Box(5.0, 16.0, 30.0) + Pos(xr + 4.0, 0, bh + 10.5) * Box(17.0, 16.0, 5.0)
    hk = hk + Pos(xr + 10.0, 0, bh + 2.0) * Box(4.0, 16.0, 20.0)
    hk = hk - Pos(xr - 2.0, 0, bh - 16.0) * Rot(90, 0, 0) * Cylinder(3.0, 20.0)
    out.append(_p("Rim hook", _edge(hk, 0.8), "hdpe_recycled", "made", BOM3["hook"], "shell", (40, 0, 40)))
    zt = z0 + tl + 10.0
    zh = bh - 16.0
    pts = [(0, 0, zt), (0, 0, zt + 20), (xr * 0.5, 0, zh - 10), (xr - 2.0, 0, zh)]
    try:
        cord = cp.rope(pts, 3.0)
    except Exception:
        cord = Pos(xr / 2, 0, (zt + zh) / 2) * Box(3.0, 3.0, zh - zt)
    out.append(_p("Cord, 3 mm polyester", cord, "rope", "bought", BOM3["cord"], "shell", (20, 0, 20)))
    for i, (cx, cz) in enumerate(((0.0, zt + 8.0), (xr - 8.0, zh - 2.0))):
        clip = Pos(cx, 0, cz) * (Box(3.0, 8.0, 12.0) - Box(3.2, 5.0, 9.0))
        out.append(_p(f"Cord clip {i + 1}, stainless", clip, "stainless", "bought", BOM3["clip"], "shell", (20, 0, 20)))
    out.append(_p("Washer under cord clip, M3", Pos(0, 0, zt + 1.0) * H.ring(7.0, 3.2, 0.5, 0.0), "stainless", "fastener", BOM3["washer"], "shell", (0, 0, 40)))
    tag = Pos(xr * 0.25, 0, (zt + zh) / 2 - 10) * Box(1.0, 30.0, 40.0)
    out.append(_p("Warning tag on the cord", _edge(tag, 0.3), "label", "bought", BOM3["tag"], "shell", (0, 0, 0)))
    if context:
        out.append(_p("Bucket 20 L, raw water (context, solution C)", H.bucket_20l(bt, bb, bh), "pe_tank_white", "context", None, "context"))
    return out


@functools.lru_cache(None)
def _components(option, context=True):
    return tuple({"D1": option_d1, "D2": option_d2, "D3": option_d3}[option](context))


def components(option="D1", context=True):
    return [dict(q) for q in _components(option, context)]


if __name__ == "__main__":
    for o in (sys.argv[1:] or OPTIONS):
        ps = components(o)
        print(o, len([p for p in ps if p["kind"] != "context"]), "parts")
        for p in ps:
            bb = p["shape"].bounding_box()
            print(f"   {p['kind']:8s} {p['name'][:50]:50s} z {bb.min.Z:7.1f} .. {bb.max.Z:7.1f}  {cp.mass_kg(p)*1000:7.2f} g  vol {p['shape'].volume:9.1f}")
