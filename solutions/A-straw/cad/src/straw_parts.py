"""Helpers for the Helpful Water A filter straw model (kit 1.9, STANDARDS section 24).

Turned parts are drawn as revolved (r, z) profiles about the straw axis (global Z, intake at z = 0). O-rings are
tori at their free cross-section seated on the groove floor; the squeeze against the bore is designed interference
(listed in model.ALLOWED_CONTACTS). Bayonet grooves, lugs, slots and hole patterns are real cuts, so every part is
drawable on its own. Dimensions in millimetres.
"""
from __future__ import annotations

import math

from build123d import (Axis, Box, Circle, Cone, Cylinder, Plane, Polygon, Pos, Rot, Sketch, Torus, extrude, revolve,
                       Compound)


def revolved(pts):
    """Solid of revolution about Z from a closed (r, z) polyline (r >= 0)."""
    face = Plane.XZ * Polygon(*pts, align=None)
    return revolve(face, Axis.Z, 360)


def tube(r_in, r_out, z0, z1):
    return revolved([(r_in, z0), (r_out, z0), (r_out, z1), (r_in, z1)])


def o_ring(groove_d, cs, z):
    """O-ring seated on a groove floor of diameter groove_d (male gland) at height z, free cross-section cs."""
    return Pos(0, 0, z) * Torus(groove_d / 2 + cs / 2, cs / 2)


def o_ring_bore(bore_d, cs, z):
    """O-ring seated in a female gland whose floor is bore_d (ring outside diameter = bore_d)."""
    return Pos(0, 0, z) * Torus(bore_d / 2 - cs / 2, cs / 2)


def groove_cut(r_floor, r_out, z0, z1):
    """Annular cutter for a male gland: removes material between r_floor and r_out over z0..z1."""
    return tube(r_floor, r_out + 1.0, z0, z1)


def bayonet_cutter(r_in, r_out, z_groove0, z_groove1, z_end, width, angles=(0.0, 180.0)):
    """Female bayonet in a bore: an annular groove (r_in..r_out, z_groove0..z_groove1) and axial entry slots of
    the given width from the groove to the bore end at z_end, at the listed angles (degrees)."""
    cut = tube(r_in - 0.05, r_out, z_groove0, z_groove1)
    lo, hi = sorted((z_groove0, z_end))
    for a in angles:
        slot = Pos(0, 0, (lo + hi) / 2) * Box((r_out - r_in) + 0.1, width, hi - lo)
        cut = cut + Rot(0, 0, a) * Pos((r_in + r_out) / 2, 0, 0) * slot
    return cut


def lugs(r_in, r_out, z0, z1, width, angles=(90.0, 270.0)):
    """Two (or more) bayonet lugs on a spigot, as rounded pads between r_in and r_out."""
    out = None
    for a in angles:
        pad = Rot(0, 0, a) * Pos((r_in + r_out) / 2, 0, (z0 + z1) / 2) * Box(r_out - r_in, width, z1 - z0)
        out = pad if out is None else out + pad
    return out


def hole_ring(r_ring, n, d, z0, z1, phase=0.0):
    """Cutter: n axial holes of diameter d on a ring of radius r_ring."""
    out = None
    for i in range(n):
        a = phase + 2 * math.pi * i / n
        c = Pos(r_ring * math.cos(a), r_ring * math.sin(a), (z0 + z1) / 2) * Cylinder(d / 2, z1 - z0)
        out = c if out is None else out + c
    return out


def radial_slots(r_in, r_out, n, width, z0, z1, phase=0.0):
    """Cutter: n radial slots through a wall between r_in and r_out."""
    out = None
    for i in range(n):
        a = phase + 360.0 * i / n
        s = Rot(0, 0, a) * Pos((r_in + r_out) / 2, 0, (z0 + z1) / 2) * Box(r_out - r_in + 0.2, width, z1 - z0)
        out = s if out is None else out + s
    return out


def hex_grid_points(radius, pitch):
    pts = []
    rows = int(radius // (pitch * 0.866)) + 1
    for j in range(-rows, rows + 1):
        y = j * pitch * 0.866
        off = (pitch / 2) if j % 2 else 0.0
        for i in range(-rows - 1, rows + 2):
            x = i * pitch + off
            if math.hypot(x, y) <= radius:
                pts.append((x, y))
    return pts


def mesh_disc(d, t, z, pitch=1.6, hole=0.9):
    """Woven mesh disc drawn as a perforated disc (the real aperture, 250 um, is too fine to model)."""
    sk = Sketch() + Circle(d / 2)
    for x, y in hex_grid_points(d / 2 - 1.2, pitch):
        sk -= Pos(x, y) * Circle(hole / 2)
    return Pos(0, 0, z) * extrude(sk, t)


def fibre_bundle(d, z0, z1, n_lobes=48, lobe_d=0.8):
    """Hollow-fibre bundle as one solid: a cylinder whose rim is scalloped by the outer fibres."""
    r = d / 2
    sk = Sketch() + Circle(r)
    for i in range(n_lobes):
        a = 2 * math.pi * i / n_lobes
        sk -= Pos(r * math.cos(a), r * math.sin(a)) * Circle(lobe_d * 0.45)
    return Pos(0, 0, z0) * extrude(sk, z1 - z0)


def potted_block(d, z0, z1, open_face=None, lumen_pitch=1.7, lumen_d=0.5, depth=0.6):
    """Potting block (cylinder). open_face 'top' or 'bottom' shows the cut fibre lumens as shallow holes."""
    blk = tube(0, d / 2, z0, z1)
    if open_face:
        zf = z1 if open_face == "top" else z0
        cut = None
        for x, y in hex_grid_points(d / 2 - 0.9, lumen_pitch):
            c = Pos(x, y, zf - depth / 2 if open_face == "top" else zf + depth / 2) * Cylinder(lumen_d / 2, depth)
            cut = c if cut is None else cut + c
        blk = blk - cut
    return blk


def slotted_cage(r_in, r_out, z0, z1, n=6, win_w=5.0, win_h=18.0, rows=4, margin=6.0):
    """Perforated module shell: a tube with rows of axial windows so feed water reaches the fibres."""
    shell = tube(r_in, r_out, z0, z1)
    span = (z1 - z0 - 2 * margin)
    pitch = span / rows
    cut = None
    for k in range(rows):
        zc = z0 + margin + pitch * (k + 0.5)
        c = radial_slots(r_in - 0.3, r_out + 0.3, n, win_w, zc - win_h / 2, zc + win_h / 2, phase=(30.0 if k % 2 else 0.0))
        cut = c if cut is None else cut + c
    return shell - cut


def split_ring(d_mean, wire, z=0.0):
    """Stainless split key ring (two turns), drawn as two stacked tori."""
    return Compound([Pos(0, 0, z) * Torus(d_mean / 2, wire / 2), Pos(0, 0, z + wire) * Torus(d_mean / 2, wire / 2)])


def cord_loop(points, d):
    """A cord through points, as round segments (lanyard)."""
    from build123d import Sphere
    segs = []
    for a, b in zip(points, points[1:]):
        L = math.dist(a, b)
        mid = tuple((a[i] + b[i]) / 2 for i in range(3))
        dx, dy, dz = ((b[i] - a[i]) / L for i in range(3))
        ry = math.degrees(math.atan2(math.hypot(dx, dy), dz))
        rz = math.degrees(math.atan2(dy, dx))
        segs.append(Pos(*mid) * Rot(0, 0, rz) * Rot(0, ry, 0) * Cylinder(d / 2, L))
        segs.append(Pos(*b) * Sphere(d / 2))
    out = segs[0]
    for s in segs[1:]:
        out = out + s
    return out
