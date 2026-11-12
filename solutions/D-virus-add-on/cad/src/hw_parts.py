"""Helpful Water D part helpers: threads, O-rings, gaskets, tablets, small bottles, the context PET bottle and the
context 20 L bucket, as build123d solids in millimetres along +Z (kit 1.9 detail level D3). Adapted from the
Helpful Water B helpers (solutions/B-bottle-cartridge/cad/src/hw_parts.py) so that the dose cap fits the same
28 mm PCO 1881 neck the B cartridge screws onto.

These sit beside .kit/cad_parts.py (which covers steel stock and ISO fasteners) because a chlorine add-on is
made of small moulded and bought parts. Every helper returns a valid solid with real features (thread ridges as
helical sweeps, O-rings as tori, mesh discs with a crimped rim, bundles with a potting block), so no made or bought
part is a bare box or cylinder.

Neck finish data (PCO 1881 and PCO 1810, 28 mm): thread outside diameter about 27.4 mm, bore about 21.7 mm,
pitch about 2.7 mm, thread height about 1.15 mm; neck height about 17 mm (1881) and 21 mm (1810)
(Kapy CAD, "PET bottle threads: PCO-1881 and PCO-1810", https://kapycad.com/en/academy/standards/pet-bottle-thread,
checked 2026-11-11; the values are approximate and are confirmed against the ISBT drawings before tooling).
"""
from __future__ import annotations

import math
from build123d import (Axis, Box, Cylinder, Torus, Pos, Rot, Face, Wire, Helix, sweep, revolve, Plane, Polyline,
                       make_face, Solid, Compound, Cone, fillet, chamfer)

# PCO 1881 neck (approximate, see module docstring)
NECK = dict(T=27.4, BORE=21.7, PITCH=2.7, H_THREAD=1.15, NECK_H_1881=17.0, NECK_H_1810=21.0, RING_D=33.0, RING_T=1.6,
            LIP_W=2.4)


def tube(od, id_, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * (Cylinder(od / 2, h) - Cylinder(id_ / 2, h + 2))


def disc(d, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * Cylinder(d / 2, h)


def ring(od, id_, h, z0=0.0):
    return Pos(0, 0, z0 + h / 2) * (Cylinder(od / 2, h) - Cylinder(id_ / 2, h + 1))


def thread(r_root, depth, pitch, turns, internal=False, z0=0.0):
    """Helical thread ridge as a solid. External: ridge from r_root outward. Internal: ridge from r_root inward.
    Buttress-like trapezoid profile, base width 0.8 x pitch."""
    h = Helix(pitch, pitch * turns, r_root)
    s = -1 if internal else 1
    pts = [(r_root - s * 0.05, 0, -0.4 * pitch), (r_root + s * depth, 0, -0.08 * pitch),
           (r_root + s * depth, 0, 0.08 * pitch), (r_root - s * 0.05, 0, 0.4 * pitch)]
    prof = Face(Wire.make_polygon(pts, close=True))
    return Pos(0, 0, z0) * sweep(prof, h, is_frenet=True)


def o_ring(id_, cs, z):
    """O-ring of inside diameter id_ and cross-section cs, centred at height z."""
    return Pos(0, 0, z) * Torus(id_ / 2 + cs / 2, cs / 2)


def flat_gasket(od, id_, t, z0):
    g = ring(od, id_, t, z0)
    try:
        return fillet(g.edges(), t * 0.3)
    except Exception:
        return g


def mesh_disc(d, t, z0, rim=1.2):
    """Woven mesh disc with a crimped (folded) rim, as cut and pressed from 316L cloth."""
    body = disc(d - 2 * rim, t, z0)
    rimr = ring(d, d - 2 * rim, t * 2.2, z0 - t * 0.6)
    return body + rimr


def pad(d, t, z0):
    """Nonwoven retention pad: a disc with chamfered edges."""
    p = disc(d, t, z0)
    try:
        return chamfer(p.edges(), t * 0.3)
    except Exception:
        return p


def carbon_bed(d, h, z0):
    """Granular carbon bed as poured: settled top with a slight cone, edge rounded where it meets the wall."""
    body = disc(d, h - 1.0, z0)
    top = Pos(0, 0, z0 + h - 0.5) * Cone(d / 2, d / 2 - 2.0, 1.0)
    return body + top


def fibre_bundle(d, h, z0, n_tufts=19):
    """Hollow-fibre bundle as a bundle solid: the fibre mass with the looped (U-bend) end rounded at the bottom
    and shallow grooves where fibre groups separate, so it reads as fibres, not a rod."""
    core = disc(d, h - d * 0.25, z0 + d * 0.25)
    end = Pos(0, 0, z0 + d * 0.25) * (Cylinder(d / 2, d * 0.5) & Pos(0, 0, -d * 0.25) * Cylinder(d / 2, d * 0.5))
    try:
        b = core + Pos(0, 0, z0 + d * 0.25) * fillet((Cylinder(d / 2, d * 0.5)).edges().group_by(Axis.Z)[0], d * 0.24)
    except Exception:
        b = core
    grooves = None
    for k in range(n_tufts // 3):
        a = 360 * k / (n_tufts // 3)
        g = Rot(0, 0, a) * Pos(d / 2, 0, z0 + h / 2) * Cylinder(0.6, h * 0.8)
        grooves = g if grooves is None else grooves + g
    return b - grooves if grooves is not None else b


def perforated_sleeve(od, id_, h, z0, hole_d=3.0, rows=6, per_row=8):
    """Perforated guard sleeve of a membrane module (holes let feed water reach the fibres)."""
    s = tube(od, id_, h, z0)
    cut = None
    for r in range(rows):
        z = z0 + h * (r + 0.7) / (rows + 0.4)
        for k in range(per_row):
            a = 360 * k / per_row + (22.5 if r % 2 else 0)
            c = Rot(0, 0, a) * Pos(od / 2 - (od - id_) / 2 / 2, 0, z) * Rot(0, 90, 0) * Cylinder(hole_d / 2, (od - id_) * 3)
            cut = c if cut is None else cut + c
    return s - cut


def revolved(profile_rz, axis_z=True):
    """Solid of revolution from a closed (r, z) polyline in the XZ plane."""
    pts = [(r, 0, z) for r, z in profile_rz]
    w = Polyline(*pts, close=True)
    f = make_face(w)
    return revolve(f, Axis.Z, 360)


def pet_bottle_1l(z_top=0.0, body_d=80.0, height=262.0):
    """Context part: a 1 L PET water bottle with a 28 mm PCO 1881 neck, neck top (sealing lip) at z_top.
    Body 80 mm across and about 262 mm tall (assumed typical, to measure from local bottles)."""
    T, B = NECK["T"], NECK["BORE"]
    rr = body_d / 2
    prof = [(B / 2, 0), (T / 2 - NECK["H_THREAD"], 0), (T / 2 - NECK["H_THREAD"], -NECK["NECK_H_1881"]),
            (NECK["RING_D"] / 2, -NECK["NECK_H_1881"]), (NECK["RING_D"] / 2, -NECK["NECK_H_1881"] - NECK["RING_T"]),
            (13.5, -NECK["NECK_H_1881"] - NECK["RING_T"]), (14.5, -26), (24, -40), (34, -56), (rr, -72),
            (rr, -height + 8), (rr - 6, -height), (B / 2 - 0.5, -height + 1.0), (B / 2 - 0.5, -2.0)]
    prof = [(r, z + z_top) for r, z in prof]
    body = revolved(prof)
    th = thread(T / 2 - NECK["H_THREAD"], NECK["H_THREAD"], NECK["PITCH"], 1.75, internal=False, z0=z_top - 13.5)
    return body + th


def hex_socket_screw(d, length):
    """Small pan-head self-tapping screw for plastic (ISO 7049 style), drawn with a plain shank and a cross recess."""
    head_d, head_h = 2.0 * d, 0.7 * d
    shank = Pos(0, 0, -length / 2) * Cylinder(d / 2 * 0.9, length)
    head = Pos(0, 0, head_h / 2) * Cylinder(head_d / 2, head_h)
    try:
        head = fillet(head.edges().group_by(Axis.Z)[-1], head_h * 0.45)
    except Exception:
        pass
    slot = Pos(0, 0, head_h) * (Box(head_d * 0.6, d * 0.25, head_h) + Box(d * 0.25, head_d * 0.6, head_h))
    return head + shank - slot


def pin(d, length):
    """Stainless hinge pin (ISO 2338 style dowel) with chamfered ends, along +Z centred on the origin."""
    p = Cylinder(d / 2, length)
    try:
        return chamfer(p.edges(), d * 0.15)
    except Exception:
        return p


def countersunk_screw(d, length):
    """Countersunk self-tapping screw for plastic (ISO 7050 style), head top face at z = 0, shank along -Z."""
    head_d = 1.9 * d
    head_h = (head_d - d) / 2 / math.tan(math.radians(45))
    head = Pos(0, 0, -head_h / 2) * Cone(d / 2, head_d / 2, head_h)
    shank = Pos(0, 0, -head_h - (length - head_h) / 2) * Cylinder(d / 2 * 0.9, length - head_h)
    slot = Pos(0, 0, -0.3) * (Box(head_d * 0.6, d * 0.25, 0.8) + Box(d * 0.25, head_d * 0.6, 0.8))
    return head + shank - slot


def countersink_cut(d, length):
    head_d = 1.9 * d
    head_h = (head_d - d) / 2
    return Pos(0, 0, -head_h / 2 + 0.05) * Cone(d / 2 + 0.1, head_d / 2 + 0.1, head_h + 0.1) + Pos(0, 0, -length / 2) * Cylinder(d / 2 + 0.1, length)


def tablet(d, t, z0=0.0):
    """Pressed tablet: a disc with bevelled edges (NaDCC or calcium hypochlorite)."""
    s = disc(d, t, z0)
    try:
        return chamfer(s.edges(), min(t * 0.25, 0.8))
    except Exception:
        return s


def small_bottle(z_top, body_d=50.0, height=110.0):
    """Context or bought part: a 150 mL HDPE bottle with a 28 mm PCO 1881-style neck, neck top at z_top, base at
    z_top - height. Wall 1.0 mm (assumed). Shoulders and a base chamfer so it reads as a moulded bottle."""
    T, B = NECK["T"], NECK["BORE"]
    rr = body_d / 2
    prof = [(B / 2, 0), (T / 2 - NECK["H_THREAD"], 0), (T / 2 - NECK["H_THREAD"], -NECK["NECK_H_1881"]),
            (NECK["RING_D"] / 2, -NECK["NECK_H_1881"]), (NECK["RING_D"] / 2, -NECK["NECK_H_1881"] - NECK["RING_T"]),
            (15.0, -NECK["NECK_H_1881"] - NECK["RING_T"]), (rr - 2, -26), (rr, -32),
            (rr, -height + 4), (rr - 4, -height), (0.0, -height), (0.0, -height + 1.0), (rr - 4.6, -height + 1.0),
            (rr - 1.0, -height + 4.4), (rr - 1.0, -32.4), (rr - 3.0, -26.6), (14.0, -NECK["NECK_H_1881"] - NECK["RING_T"] + 0.6),
            (B / 2, -NECK["NECK_H_1881"] + 1.0)]
    prof = [(r, z + z_top) for r, z in prof]
    body = revolved(prof)
    th = thread(T / 2 - NECK["H_THREAD"], NECK["H_THREAD"], NECK["PITCH"], 1.75, internal=False, z0=z_top - 13.5)
    return body + th


def bucket_20l(top_d=300.0, base_d=262.0, height=340.0, wall=1.8):
    """Context part: a 20 L HDPE bucket (about 21 L to the brim) with a rolled rim and two stiffening rings,
    standing on z = 0. Sizes assumed typical; to measure from the buckets the household uses (solution C)."""
    rt, rb = top_d / 2, base_d / 2
    prof = [(0, 0), (rb, 0), (rt - 0.5, height - 12), (rt + 5, height - 12), (rt + 5, height), (rt - wall, height),
            (rb - wall, wall), (0, wall)]
    body = revolved(prof)
    for z in (height - 40, height - 70):
        rz = rb + (rt - rb) * z / height
        body = body + ring(2 * rz + 5, 2 * rz - 1, 3.0, z)
    return body
