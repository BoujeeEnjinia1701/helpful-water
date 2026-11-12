"""Helpful Water C part helpers: 20 L buckets and lids, bulkhead fittings, a ball valve, hose barbs and swept hoses,
a tee with a backflush port, a drum tap, a bought hollow-fibre module, ceramic candles, wing nuts, timber and
plywood, as build123d solids in millimetres (kit 1.9 detail level D3).

These sit beside .kit/cad_parts.py (steel stock and ISO fasteners) because a household gravity filter is made of
bought plastic containers and fittings. Every helper returns a valid solid with real features (bucket rims and
stacking rings, hex flats, thread ridges, barbs, fibre bundles with potting), so no made or bought part is a bare
box or cylinder. Bucket and fitting sizes are assumed typical values, measured from the bought parts before use.

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""
from __future__ import annotations

import math
from build123d import (Axis, Box, Cylinder, Torus, Pos, Rot, Face, Wire, Helix, sweep, revolve, Polyline, make_face,
                       Cone, fillet, chamfer, Spline, Vector, Plane, Compound, Sphere)


# ---------------------------------------------------------------------------------------------------------
# Primitives with features (all along +Z unless stated)
# ---------------------------------------------------------------------------------------------------------
def tube(od, id_, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * (Cylinder(od / 2, h) - Cylinder(id_ / 2, h + 2))


def disc(d, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * Cylinder(d / 2, h)


def ring(od, id_, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * (Cylinder(od / 2, h) - Cylinder(id_ / 2, h + 1))


def soft(shape, r):
    """Round every edge where possible (moulded or sawn parts), else chamfer, else leave it."""
    for op in (fillet, chamfer):
        try:
            out = op(shape.edges(), r)
            if out.is_valid:
                return out
        except Exception:
            pass
    return shape


def revolved(profile_rz):
    pts = [(r, 0, z) for r, z in profile_rz]
    return revolve(make_face(Polyline(*pts, close=True)), Axis.Z, 360)


def thread(r_root, depth, pitch, turns, internal=False, z0=0.0):
    """Helical thread ridge as a solid (trapezoid profile)."""
    h = Helix(pitch, pitch * turns, r_root)
    s = -1 if internal else 1
    pts = [(r_root - s * 0.05, 0, -0.4 * pitch), (r_root + s * depth, 0, -0.08 * pitch),
           (r_root + s * depth, 0, 0.08 * pitch), (r_root - s * 0.05, 0, 0.4 * pitch)]
    return Pos(0, 0, z0) * sweep(Face(Wire.make_polygon(pts, close=True)), h, is_frenet=True)


def o_ring(id_, cs, z):
    return Pos(0, 0, z) * Torus(id_ / 2 + cs / 2, cs / 2)


def flat_gasket(od, id_, t, z0=0.0):
    return soft(ring(od, id_, t, z0), t * 0.3)


def hexagon(af, h, z0=0.0):
    """Hex prism across flats af, chamfered at both ends as a moulded or machined nut is."""
    from build123d import RegularPolygon, extrude
    pr = Pos(0, 0, z0) * extrude(RegularPolygon(af / math.sqrt(3), 6), h)
    try:
        cap = Pos(0, 0, z0 + h / 2) * Cylinder(af / math.sqrt(3), h)
        cap = chamfer(cap.edges(), af / math.sqrt(3) - af / 2 * 0.96)
        return pr & cap
    except Exception:
        return pr


def placed(shape, origin, direction):
    """Move a shape built along +Z from the origin so its axis runs along direction ('+x', '-x', '+y', '-y',
    '+z', '-z') from origin."""
    rot = {"+z": Rot(0, 0, 0), "-z": Rot(180, 0, 0), "+x": Rot(0, 90, 0), "-x": Rot(0, -90, 0),
           "+y": Rot(-90, 0, 0), "-y": Rot(90, 0, 0)}[direction]
    return Pos(*origin) * rot * shape


# ---------------------------------------------------------------------------------------------------------
# Containers
# ---------------------------------------------------------------------------------------------------------
def bucket(P, z0=0.0):
    """Food-grade 20 L HDPE pail: tapered wall, 3 mm floor with a foot ring, rim bead, two stacking rings and
    two handle ears. Bottom of the foot at z0."""
    bo, to, H, w, fl = P["BKT_BOT_OD"] / 2, P["BKT_TOP_OD"] / 2, P["BKT_H"], P["BKT_WALL"], P["BKT_FLOOR"]
    rim_r, rim_h = P["BKT_RIM"][0] / 2, P["BKT_RIM"][1]
    prof = [(0, 2.0), (bo - 6, 2.0), (bo - 6, 0.0), (bo - 2, 0.0), (bo, 3.0), (to, H - rim_h), (rim_r, H - rim_h),
            (rim_r, H - 2.0), (to - 0.5, H), (to - w, H), (to - w, H - rim_h), (bo - w, fl + 2.0), (bo - w - 3, fl + 2.0),
            (0, fl + 2.0)]
    b = revolved(prof)
    for zf in (0.72, 0.80):
        z = H * zf
        r = bo + (to - bo) * z / H
        b = b + Pos(0, 0, z) * Torus(r, 1.6)
    for s in (1, -1):
        ear = Pos(s * (to + 2.5), 0, H - rim_h - 14) * Box(8.0, 22.0, 22.0)
        ear = ear - Pos(s * (to + 2.5), 0, H - rim_h - 14) * Rot(0, 90, 0) * Cylinder(2.5, 12)
        b = b + soft(ear, 1.0)
    return Pos(0, 0, z0) * b


def bucket_lid(P, z_rim_top, holes=()):
    """Snap lid over the rim bead: top plate with a stiffening ring and a skirt; holes = [(x, y, d), ...]."""
    rim_r = P["BKT_RIM"][0] / 2
    t, sk = P["LID_T"], P["LID_SKIRT"]
    prof = [(0, 0.2), (rim_r + 0.6, 0.2), (rim_r + 0.6, -sk + 3), (rim_r + 2.6, -sk + 3), (rim_r + 2.6, t + 0.2),
            (0, t + 0.2)]
    lid = Pos(0, 0, z_rim_top) * revolved(prof)
    lid = lid + Pos(0, 0, z_rim_top + t + 0.2) * Torus(rim_r - 2.0, 1.2)
    for x, y, d in holes:
        lid = lid - Pos(x, y, z_rim_top + 1.5) * Cylinder(d / 2, t + 6)
    return lid


def bulkhead(bore, origin, direction, wall_t, out_len=20.0):
    """Bulkhead tank fitting through a container wall. Local frame: wall outer face at z = 0, inner face at
    z = -wall_t, the fitting's outer end at z = out_len. Inside: flange and gasket; outside: gasket, hex nut on the
    threaded shank. Returns (body, nut, gasket_in, gasket_out, hole_cutter)."""
    sh = bore + 8.0
    fl = sh + 14.0
    zf = -wall_t - 1.5
    body = tube(fl, bore, 3.5, zf - 3.5) + tube(sh, bore, out_len - (zf - 3.5) + 0.0, zf - 3.5)
    body = body + thread(sh / 2 - 0.05, 0.8, 1.8, 5.0, internal=False, z0=3.0)
    nut = hexagon(sh + 9, 6.0, 1.5) - disc(sh + 1.8, 8.0, 0.5)
    g_in = flat_gasket(fl - 1.0, sh + 0.4, 1.5, zf)
    g_out = flat_gasket(sh + 8.0, sh + 0.4, 1.5, 0.0)
    cut = disc(sh + 0.6, wall_t + 8.0, -wall_t - 4.0)
    return [placed(x, origin, direction) for x in (body, nut, g_in, g_out, cut)]


def strainer(bore, origin, direction, wall_t, length=34.0):
    """Stainless mesh strainer cap on the inner end of a bulkhead: a perforated tube with an end disc."""
    sh = bore + 8.0
    z1 = -wall_t - 5.0
    s = tube(sh + 4.0, sh + 0.4, 6.0, z1 - 6.0) + tube(sh + 4.0, sh + 3.0, length, z1 - 6.0 - length) + disc(sh + 4.0, 0.8, z1 - 6.0 - length)
    for r in range(4):
        for k in range(8):
            z = z1 - 12.0 - r * 7.0
            s = s - Rot(0, 0, 45 * k + 22.5 * (r % 2)) * Pos(sh / 2 + 1.7, 0, z) * Rot(0, 90, 0) * Cylinder(1.8, 4.0)
    return placed(s, origin, direction)


def barb(od, bore, length, origin, direction, ridges=3):
    """Hose barb spigot with conical ridges."""
    b = tube(od - 1.0, bore, length, 0.0)
    for k in range(ridges):
        z = length - 4.0 - k * 5.0
        if z < 2:
            break
        b = b + Pos(0, 0, z) * (Cone(od / 2 + 0.4, od / 2 - 0.6, 3.5) - Cylinder(bore / 2, 5))
    return placed(b, origin, direction)


def ball_valve(bore, length, origin, direction):
    """Compact polypropylene ball valve: body with hex ends and a lever handle on its stem. Returns (body, lever)."""
    body = hexagon(bore + 14, 9.0, 0.0) + Pos(0, 0, length / 2) * soft(Cylinder(bore / 2 + 10, length - 18), 2.0)
    body = body + hexagon(bore + 14, 9.0, length - 9.0) - disc(bore, length + 2, -1)
    stem = Pos(-(bore / 2 + 10), 0, length / 2) * Rot(0, 90, 0) * Cylinder(4.0, 12.0)
    body = body + stem
    lever = Pos(-(bore / 2 + 18.5), 0, length / 2 + 18) * soft(Box(5.0, 12.0, 52.0), 1.5)
    lever = lever - Pos(-(bore / 2 + 18.5), 0, length / 2 + 38) * Rot(0, 90, 0) * Cylinder(2.0, 8.0)
    return placed(body, origin, direction), placed(lever, origin, direction)


def hose(points, od, id_, tangents=None):
    """Flexible tube swept along a smooth spline through the points (Frenet frame; falls back to a spline without
    end tangents if the sweep fails). Returns (solid, path length in mm)."""
    pts = [Vector(*p) for p in points]
    tries = []
    if tangents:
        tries.append(dict(tangents=[Vector(*t) for t in tangents]))
    tries.append({})
    for kw in tries:
        path = Spline(*pts, **kw)
        pl = Plane(origin=path.position_at(0), z_dir=path.tangent_at(0))
        prof = Face(Wire.make_circle(od / 2, pl)) - Face(Wire.make_circle(id_ / 2, pl))
        for fr in (True, False):
            try:
                s = sweep(prof, path, is_frenet=fr)
                if s.is_valid and s.volume > 0.5 * math.pi * (od * od - id_ * id_) / 4 * path.length:
                    return s, path.length
            except Exception:
                pass
    raise ValueError("hose sweep failed")


def tee_backflush(origin, P):
    """Clean-side tee below the module: vertical run from the module outlet, a horizontal outlet barb toward -X and
    a backflush branch toward -Y with a female luer port. Returns (tee, cap). origin is the top of the run."""
    od = 16.0
    run = Pos(0, 0, -12) * Cylinder(od / 2, 24) - Pos(0, 0, -12) * Cylinder(4.5, 26)
    side = Pos(-14, 0, -14) * Rot(0, 90, 0) * Cylinder(od / 2 - 1, 16) - Pos(-14, 0, -14) * Rot(0, 90, 0) * Cylinder(3.5, 30)
    port = Pos(0, -14, -14) * Rot(90, 0, 0) * Cylinder(6.0, 16) - Pos(0, -14, -14) * Rot(90, 0, 0) * Cylinder(2.2, 30)
    tee = soft(run + side, 0.8) + port
    for k in range(2):
        tee = tee + Pos(-24 - k * 5, 0, -14) * Rot(0, -90, 0) * (Cone(P["HOSE_ID"] / 2 + 0.4, P["HOSE_ID"] / 2 - 0.6, 3.5) - Cylinder(3.5, 5))
    tee = tee - Pos(0, 0, -14) * Cylinder(3.5, 8)
    tee = tee + Pos(0, -22.5, -14) * Rot(90, 0, 0) * (Cylinder(7.5, 1.5) - Cylinder(2.2, 3))   # luer lugs
    cap = Pos(0, -27.6, -14) * Rot(90, 0, 0) * (soft(Cylinder(7.0, 8.0), 0.8) - Pos(0, 0, 1.5) * Cylinder(5.0, 6.0))
    return Pos(*origin) * tee, Pos(*origin) * cap


def drum_tap(origin, wall_t):
    """Polyethylene drum tap (spigot) on a 3/4 in threaded shank, pointing -Y out of a wall whose outer face is at
    origin (inner face at +wall_t), push lever on top. Returns (tap, nut, gasket, hole_cutter)."""
    sh = Pos(0, 7.0, 0) * Rot(90, 0, 0) * (Cylinder(12.5, 17.0) - Cylinder(5.0, 19.0))
    flange = Pos(0, -4.5, 0) * Rot(90, 0, 0) * (hexagon(32, 6.0, -3.0) - Cylinder(5.0, 8.0))
    body = Pos(0, -21.0, 0) * soft(Box(26, 26, 34), 3.0) - Pos(0, -21.0, 0) * Rot(90, 0, 0) * Cylinder(5.0, 30)
    spout = Pos(0, -26, -24) * (Cylinder(7.0, 22) - Cylinder(4.0, 24))
    lever = Pos(0, -24, 20) * soft(Box(16, 30, 6), 1.5)
    tap = sh + flange + body + spout + lever
    nut = Pos(0, wall_t + 3.5, 0) * Rot(90, 0, 0) * (hexagon(36, 7.0, -3.5) - Cylinder(12.9, 10))
    gasket = Pos(0, -0.75, 0) * Rot(90, 0, 0) * flat_gasket(31, 25.4, 1.5, -0.75)
    cut = Pos(0, wall_t / 2, 0) * Rot(90, 0, 0) * Cylinder(12.8, wall_t + 8)
    return [Pos(*origin) * s for s in (tap, nut, gasket, cut)]


# ---------------------------------------------------------------------------------------------------------
# Hollow-fibre module (bought, pre-potted), header at the bottom
# ---------------------------------------------------------------------------------------------------------
def fibre_bundle(d, h, z0):
    """Bundle of looped hollow fibres: fibre mass with the loop end rounded and grooves between fibre groups."""
    core = disc(d, h - d * 0.25, z0)
    end = Pos(0, 0, z0 + h - d * 0.25) * Cylinder(d / 2, d * 0.5)
    try:
        end = fillet(end.edges().group_by(Axis.Z)[-1], d * 0.24)
    except Exception:
        pass
    end = end & Pos(0, 0, z0 + h - d * 0.25 + d * 0.125) * Cylinder(d, d * 0.25)
    b = core + end
    for k in range(6):
        b = b - Rot(0, 0, 60 * k) * Pos(d / 2, 0, z0 + h * 0.45) * Cylinder(0.7, h * 0.8)
    return b


def module(P, x, y, z_top):
    """Bought outside-in module standing upright: top cap with the raw inlet barb, shell, looped fibre bundle,
    potting block and header with the clean outlet nipple at the bottom. Returns dict of solids."""
    L, od, idd = P["MOD_L"], P["MOD_OD"], P["MOD_ID"]
    zb = z_top - L
    shell = tube(od, idd, L - 40.0, zb + 20.0)
    for k in range(3):
        shell = shell + ring(od + 2.0, od - 0.5, 3.0, zb + 70 + k * 70)      # grip rings
    cap = disc(od + 4, 6.0, z_top - 20.0 + 14.0) + tube(od + 4, od + 0.2, 14.0, z_top - 20.0)
    cap = cap - disc(8.0, 10.0, z_top - 8.0)
    cap = cap + tube(12.0, 7.0, 8.0, z_top) + Pos(0, 0, z_top + 12) * (Cone(P["HOSE_ID"] / 2 + 0.4, P["HOSE_ID"] / 2 - 0.6, 3.5) - Cylinder(3.5, 5))
    cap = cap + tube(P["HOSE_ID"] - 1.0, 7.0, 8.0, z_top + 8.0)
    header = tube(od + 4, od + 0.2, 14.0, zb + 6.0) + disc(od + 4, 6.0, zb)
    header = header - disc(8.0, 10.0, zb - 2.0)
    header = header + tube(12.0, 7.0, 10.0, zb - 10.0)
    pot = disc(idd, P["POTTING_H"], zb + 20.0)
    try:
        pot = chamfer(pot.edges().group_by(Axis.Z)[-1], 0.8)
    except Exception:
        pass
    bundle = fibre_bundle(P["BUNDLE_D"], L - 40.0 - P["POTTING_H"] - 8.0, zb + 20.0 + P["POTTING_H"])
    # bleed screw on the side of the top cap: opened at first fill until water shows, so shell air cannot pocket
    boss = Pos(od / 2 + 2.0 + 3.0, 0, z_top - 12.0) * Rot(0, 90, 0) * (Cylinder(4.0, 6.0) - Cylinder(1.6, 8.0))
    cap = cap + boss - Pos(od / 2 - 1.0, 0, z_top - 12.0) * Rot(0, 90, 0) * Cylinder(1.2, 10.0)
    bleed = Pos(od / 2 + 8.0, 0, z_top - 12.0) * Rot(0, 90, 0) * (hexagon(7.0, 3.0, 0.0) + Pos(0, 0, -3.0) * Cylinder(1.5, 6.0))
    m = dict(shell=soft(shell, 0.4), cap=cap, header=header, potting=pot, bundle=bundle, bleed=bleed)
    return {k: Pos(x, y, 0) * v for k, v in m.items()}


def p_clip(od, x, y, z, face_x):
    """Nylon P-clip round a tube of outside diameter od, its tab screwed to a face at x = face_x (tab toward -X)."""
    band = Pos(x, y, z) * (Cylinder(od / 2 + 2.0, 14.0) - Cylinder(od / 2 + 0.1, 16.0))
    tab = Pos((face_x + x - od / 2) / 2, y, z) * Box(abs(x - od / 2 - face_x) + 1.0, 14.0, 14.0)
    tab = tab - Pos((face_x + x - od / 2) / 2, y, z) * Cylinder(od / 2 + 0.1, 20)
    tab = tab - Pos(face_x + 4.0, y, z) * Rot(0, 90, 0) * Cylinder(2.6, 10)
    return band + tab


def pan_screw(d, length):
    """Pan-head wood or plastic screw, head on top at z 0..0.7d, shank down."""
    head = Pos(0, 0, 0.35 * d) * Cylinder(d, 0.7 * d)
    try:
        head = fillet(head.edges().group_by(Axis.Z)[-1], 0.3 * d)
    except Exception:
        pass
    shank = Pos(0, 0, -length / 2) * Cylinder(d / 2 * 0.9, length)
    try:
        shank = chamfer(shank.edges().group_by(Axis.Z)[0], d * 0.3)
    except Exception:
        pass
    return head + shank - Pos(0, 0, 0.7 * d) * Box(d * 1.2, d * 0.25, d * 0.6)


# ---------------------------------------------------------------------------------------------------------
# Timber and board
# ---------------------------------------------------------------------------------------------------------
def timber(sx, sy, sz, centre):
    """Planed timber or board with 2 mm arrised edges, centred at centre."""
    return Pos(*centre) * soft(Box(sx, sy, sz), 2.0)


# ---------------------------------------------------------------------------------------------------------
# Ceramic candle (C2)
# ---------------------------------------------------------------------------------------------------------
def candle(P, x, y, z_floor):
    """Ceramic candle standing on a container floor at z_floor: domed ceramic shell, plastic base and a threaded
    1/4 in stem through the floor. Returns (shell, base_with_stem)."""
    od, L = P["CANDLE_OD"], P["CANDLE_L"]
    shell = tube(od, od - 10, L - 18, 14.0) + Pos(0, 0, L - 4.0) * soft(Cylinder(od / 2, 8.0), 3.5)
    base = disc(od + 2, 6.0, 8.0) + disc(od - 12, 8.0, 2.0)
    stem = tube(13.0, 5.0, 30.0, -28.0) + thread(6.45, 0.6, 1.34, 12, internal=False, z0=-26.0)
    base = base + stem
    return Pos(x, y, z_floor) * shell, Pos(x, y, z_floor) * base


def wing_nut(x, y, z_top):
    """Polypropylene wing nut on the candle stem, top face at z_top (under the floor)."""
    hub = tube(18.0, 13.2, 10.0, -10.0)
    wings = None
    for s in (1, -1):
        w = Pos(s * 14.0, 0, -6.0) * soft(Box(14.0, 3.0, 10.0), 1.0)
        wings = w if wings is None else wings + w
    return Pos(x, y, z_top) * (hub + wings)
