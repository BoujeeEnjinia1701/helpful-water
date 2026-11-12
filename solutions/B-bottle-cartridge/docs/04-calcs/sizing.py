#!/usr/bin/env python3
"""HWB-CAL-001 sizing calculations for Helpful Water B (bottle cartridge). Run from the solution folder:

    python docs/04-calcs/sizing.py

Reads the dimensions in cad/src/model.py PARAMS and writes docs/04-calcs/sizing_results.json, which the STEM check
(docs/04-calcs/stem_check.py) and the calculation note (01-sizing.md) use. First-order engineering estimates only:
every assumption is named in ASSUMED and marked "assumed" in the note. No result here is a measured or tested value.

Licence: Apache-2.0 (Helpful Engineering licensing guide). Design Molecule Labs with Helpful Engineering.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad/src"), str(ROOT / ".kit")]
import model as M  # noqa: E402

P = M.PARAMS
G = 9.80665
RHO = 998.0          # water, 20 C, kg/m3
MU = 1.0e-3          # water viscosity at 20 C, Pa s
MU_10C = 1.307e-3    # water viscosity at 10 C, Pa s (cold-source rating, independent review 2026-11-11)
GAMMA = 0.0728       # surface tension of water at 20 C, N/m

ASSUMED = {
    # membrane (to confirm from the supplier's clean-water flux at stated pressure; HWB-DEC-001 C1)
    "LP_CLEAN_LMH_BAR": 1000.0,    # clean-water permeability of the bought module, L/(m2 h bar); assumed design value
    "LP_FOULED_SHARE": 0.5,        # share of clean permeability left just before a backflush is due; assumed
    "LP_UPPER_LMH_BAR": 4500.0,    # upper reference: Toyobo PVDF 0.1 um fibre, 108 m3/(m2 day 100 kPa), US 8,708,161 B2
    # hand squeeze (Camry dynamometer norms via Topend Sports, checked 2026-11-11; contact model assumed)
    "GRIP_KG": {"child_10_11_weak": 11.8, "child_10_11_mid": 17.5, "elderly_f_weak": 14.7, "elderly_m_weak": 21.3,
                "adult": 35.0},   # weak child = girls' boundary (11.8 kg, below the boys' 12.6; independent review 2026-11-11);
                      # adult value is an assumed typical figure, not from the cited table
    "SQUEEZE_SHARE": 0.40,         # share of maximum grip a user holds for a 20 to 30 s squeeze; assumed
    "WALL_LOSS": 0.80,             # share of squeeze force that reaches the water (PET wall stiffness); assumed
    "CONTACT_H_M": 0.080,          # height of the hand's contact band on the bottle; assumed
    # carbon
    "BED_VOID": 0.40, "SPHERICITY": 0.75, "CARBON_LIFE_L": 150.0,   # carbon taste life is assumed until breakthrough is measured
    # use
    "L_PER_DAY": 2.0, "DESIGN_LIFE_MONTHS": 9.0,
    "DUCKBILL_CRACK_KPA": 0.5,     # typical small silicone duckbill cracking pressure; assumed, supplier data to confirm
    # B3 press
    "PRESS_N": {"adult": 150.0, "elderly_or_child": 80.0}, "LIP_FRICTION_N": 10.0,
    # backflush
    "SYRINGE_BORE_MM": 26.7, "BACKFLUSH_PUSH_N": {"gentle": 30.0, "hard": 100.0},
    # costs at scale (estimates for the MKT note; not quotes)
    "SCALE_COST_USD": {"module": 3.20, "moulded_parts": 1.40, "carbon_capsule": 0.35, "seals_mesh_valve": 0.60,
                       "assembly_qc_pack": 1.50},
}
A = ASSUMED


# ------------------------------------------------------------------------------------------------------------
def membrane_area(opt):
    n, od, leg = P["U_FIBRES"], P["FIBRE_OD"] * 1e-3, P["LEG"][opt] * 1e-3
    return n * math.pi * od * 2 * leg       # outside area, m2 (outside-in flow)


def potting_packing():
    ends = 2 * P["U_FIBRES"] * math.pi * (P["FIBRE_OD"] / 2) ** 2
    return ends / (math.pi * (P["HEADER_ID"] / 2) ** 2)


def bed_dp(q_m3s, mu=MU):
    """Ergun equation through the carbon bed (dirty side)."""
    d = A["SPHERICITY"] * P["GAC_DP_MM"] * 1e-3
    e = A["BED_VOID"]
    area = math.pi * (P["BED_D"] * 1e-3 / 2) ** 2
    v = q_m3s / area
    L = P["BED_H"] * 1e-3
    return L * (150 * mu * (1 - e) ** 2 * v / (e ** 3 * d ** 2) + 1.75 * RHO * (1 - e) * v ** 2 / (e ** 3 * d))


def lumen_dp(q_m3s, opt, mu=MU):
    """Hagen-Poiseuille in the fibre lumens with uniform permeation (mean drop = 1/3 of the full-flow drop over a leg),
    plus full flow through the potting length."""
    legs = 2 * P["U_FIBRES"]
    q = q_m3s / legs
    d = P["FIBRE_ID"] * 1e-3
    L = P["LEG"][opt] * 1e-3
    k = 128 * mu / (math.pi * d ** 4)
    return k * q * (L / 3 + P["POTTING_H"] * 1e-3)


def outlet_dp(q_m3s, valve=True, mu=MU):
    """Nipple and nozzle bores (Hagen-Poiseuille) plus the valve ports (K = 1.5 on 4 x 2 mm holes)."""
    dp = 0.0
    for d_mm, L_mm in ((P["NIPPLE"][1], 12.0), (P["NOZZLE"][1], 13.0)):
        d = d_mm * 1e-3
        dp += 128 * mu * L_mm * 1e-3 * q_m3s / (math.pi * d ** 4)
        v = q_m3s / (math.pi * d ** 2 / 4)
        dp += 0.5 * RHO * v ** 2          # one velocity head per contraction
    if valve:
        v = q_m3s / (4 * math.pi * 0.002 ** 2 / 4)
        dp += 1.5 * 0.5 * RHO * v ** 2
    return dp


def mesh_dp(q_m3s):
    open_area = 0.36 * math.pi * (P["INLET_D"] * 1e-3 / 2) ** 2
    v = q_m3s / open_area
    return 1.0 * 0.5 * RHO * v ** 2


def flow_at(p_pa, opt, lp_lmh_bar, valve=True, mu=MU):
    """Solve p = membrane + bed + lumen + outlet + mesh for Q (m3/s) by bisection."""
    area = membrane_area(opt)
    lp = lp_lmh_bar / 1000 / 3600 / 1e5 * MU / mu   # m3/(m2 s Pa); permeability scales with 1 / viscosity
    def total(q):
        return q / (lp * area) + bed_dp(q, mu) + lumen_dp(q, opt, mu) + outlet_dp(q, valve, mu) + mesh_dp(q)
    lo, hi = 0.0, 1e-3
    for _ in range(80):
        mid = (lo + hi) / 2
        if total(mid) > p_pa:
            hi = mid
        else:
            lo = mid
    q = lo
    return dict(q_ml_min=q * 6e7, membrane_kpa=q / (lp * area) / 1e3, bed_kpa=bed_dp(q, mu) / 1e3, lumen_kpa=lumen_dp(q, opt, mu) / 1e3,
                outlet_kpa=outlet_dp(q, valve, mu) / 1e3, mesh_kpa=mesh_dp(q) / 1e3)


def squeeze_kpa(grip_kg):
    f = grip_kg * G * A["SQUEEZE_SHARE"] * A["WALL_LOSS"]
    return f / (P["BOTTLE_D"] * 1e-3 * A["CONTACT_H_M"]) / 1e3


def gravity_b2(lp, mu=MU):
    """Inverted 1 L bottle draining through the B2 cartridge; head from the water surface to the drip point,
    less the duckbill cracking pressure (the vent tube makes the air pocket follow atmospheric pressure)."""
    lip = M.B2_TOP
    drip = lip - (P["HOUSING_TOP"]["B2"] + P["END_WALL"] + 27.0)       # spout tip below the lip
    body_area = math.pi * (P["BOTTLE_D"] / 2 - 0.5) ** 2 * 1e-6           # m2
    vol_left, t, z = 1.0e-3, 0.0, lip + 72.0 + 1.0e-3 / body_area * 1e3   # full: water up to about 271 mm above the lip
    qs = []
    z_full = z
    dt = 2.0
    while vol_left > 0:
        head = max(0.0, (z - drip) * 1e-3 * RHO * G - A["DUCKBILL_CRACK_KPA"] * 1e3)
        q = flow_at(head, "B2", lp, valve=False, mu=mu)["q_ml_min"] / 6e7
        qs.append(q)
        dv = q * dt
        vol_left -= dv
        area = body_area if z > lip + 72 else math.pi * (0.0135 + (z - lip) / 72 * 0.0265) ** 2
        z -= dv / area * 1e3
        t += dt
        if t > 7200:
            break
    return dict(head_full_kpa=(z_full - drip) * 1e-3 * RHO * G / 1e3, head_empty_kpa=(lip - drip) * 1e-3 * RHO * G / 1e3,
                minutes_per_litre=t / 60, mean_ml_min=1000 / (t / 60))


def b3_press(force_n, lp):
    co, ci, _ = P["CUP"]
    area = math.pi * (ci * 1e-3 / 2) ** 2
    p = max(0.0, force_n - A["LIP_FRICTION_N"]) / area
    r = flow_at(p, "B3", lp, valve=False)
    r["press_kpa"] = p / 1e3
    return r


def b3_volumes():
    po, pi, pl = P["PRESS"]
    clean = math.pi * (pi / 2) ** 2 * (pl - 10) - math.pi * (P["HOUSING_OD"] / 2) ** 2 * (P["HOUSING_TOP"]["B3"] + P["END_WALL"] - 9)
    return dict(clean_ml=clean / 1000, fill_line_ml=350.0)


def masses():
    """B1 dry mass from the model's volumes with real densities (the kit's render densities differ)."""
    dens = {"pp": 905, "epdm": 1150, "stainless": 7950, "carbon": A and P["GAC_BULK"] * 1000, "pvdf": 1780, "pu": 1100}
    out, total = {}, 0.0
    for q in M.components("B1", context=False):
        v = q["shape"].volume * 1e-9
        n = q["name"]
        if "Carbon bed" in n:
            m = v * dens["carbon"]
        elif "Fibre bundle" in n:
            legs = 2 * P["U_FIBRES"]
            wall = math.pi / 4 * ((P["FIBRE_OD"] * 1e-3) ** 2 - (P["FIBRE_ID"] * 1e-3) ** 2) * P["LEG"]["B1"] * 1e-3
            m = legs * wall * dens["pvdf"] * 0.30        # porous wall about 70 % voids (assumed)
        elif "Potting" in n:
            m = v * dens["pu"] * (1 - potting_packing() * (P["FIBRE_ID"] / P["FIBRE_OD"]) ** 2)
        elif q["material_name"] == "epdm":
            m = v * dens["epdm"]
        elif q["material_name"] == "stainless":
            m = v * dens["stainless"] * (0.36 if "Mesh" in n else 1.0)
        elif q["material_name"] == "label":
            m = v * 300                                   # nonwoven pads
        else:
            m = v * dens["pp"]
        out[n] = round(m * 1000, 2)
        total += m
    return out, total * 1000


def hold_up_clean_ml():
    """Clean-side wet volume downstream of the potting: header plenum, nipple, spout and nozzle bores."""
    plen = math.pi * (P["HEADER_ID"] / 2) ** 2 * 6.0
    nip = math.pi * (P["NIPPLE"][1] / 2) ** 2 * 18.0
    spout = math.pi * (11.0 / 2) ** 2 * 4.0 + math.pi * (P["NOZZLE"][1] / 2) ** 2 * 13.0
    return (plen + nip + spout) / 1000


def lumen_volume_ml():
    """Clean water held inside the fibre lumens (legs plus potting length); capillary forces keep it there."""
    legs = 2 * P["U_FIBRES"]
    return legs * math.pi * (P["FIBRE_ID"] / 2) ** 2 * (P["LEG"]["B1"] + P["POTTING_H"]) / 1000


def shell_water_ml():
    """Dirty-side water around the fibres inside the guard sleeve, plus the carbon bed voids and pores (wet mass)."""
    so, si = P["SLEEVE"]
    legs = 2 * P["U_FIBRES"]
    around = (math.pi * (si / 2) ** 2 - legs * math.pi * (P["FIBRE_OD"] / 2) ** 2) * P["LEG"]["B1"] / 1000
    bed_ml = math.pi * (P["BED_D"] / 20) ** 2 * P["BED_H"] / 10
    carbon = bed_ml * A["BED_VOID"] + bed_ml * P["GAC_BULK"] * 0.4     # GAC holds about 0.4 mL/g in its pores (assumed)
    return around + carbon


def bubble_point(d_um):
    return 4 * GAMMA / (d_um * 1e-6) / 1e3      # kPa, wetted pore, contact angle 0


def run():
    r = {"assumed": A}
    r["area_m2"] = {o: membrane_area(o) for o in M.OPTIONS}
    r["packing"] = potting_packing()
    lpc, lpf = A["LP_CLEAN_LMH_BAR"], A["LP_CLEAN_LMH_BAR"] * A["LP_FOULED_SHARE"]
    r["squeeze_kpa"] = {k: squeeze_kpa(v) for k, v in A["GRIP_KG"].items()}
    r["squeeze_kpa"]["adult_max"] = squeeze_kpa(A["GRIP_KG"]["adult"]) / A["SQUEEZE_SHARE"]
    r["b1"] = {k: {"clean": flow_at(p * 1e3, "B1", lpc), "fouled": flow_at(p * 1e3, "B1", lpf)} for k, p in r["squeeze_kpa"].items()}
    r["b1_at_10kpa"] = {"clean": flow_at(10e3, "B1", lpc), "fouled": flow_at(10e3, "B1", lpf)}
    r["b1_at_10kpa_upper"] = flow_at(10e3, "B1", A["LP_UPPER_LMH_BAR"])
    r["b2"] = {"clean": gravity_b2(lpc), "fouled": gravity_b2(lpf)}
    # cold source water (10 C): independent review 2026-11-11
    r["b1_10c"] = {k: {"clean": flow_at(r["squeeze_kpa"][k] * 1e3, "B1", lpc, mu=MU_10C), "fouled": flow_at(r["squeeze_kpa"][k] * 1e3, "B1", lpf, mu=MU_10C)}
                   for k in ("child_10_11_weak", "elderly_f_weak", "adult")}
    r["b2_10c"] = {"clean": gravity_b2(lpc, MU_10C), "fouled": gravity_b2(lpf, MU_10C)}
    r["b3"] = {k: {"clean": b3_press(f, lpc), "fouled": b3_press(f, lpf)} for k, f in A["PRESS_N"].items()}
    r["b3_volumes"] = b3_volumes()
    # carbon
    bed_ml = math.pi * (P["BED_D"] / 20) ** 2 * P["BED_H"] / 10
    r["carbon"] = dict(bed_ml=bed_ml, mass_g=bed_ml * P["GAC_BULK"], ebct_s={k: bed_ml / v["clean"]["q_ml_min"] * 60 for k, v in r["b1"].items()},
                       ebct_b2_s=bed_ml / r["b2"]["clean"]["mean_ml_min"] * 60, life_l=A["CARBON_LIFE_L"],
                       capsules_per_year=A["L_PER_DAY"] * 365 / A["CARBON_LIFE_L"])
    # mass and volume
    parts, total = masses()
    r["mass_parts_g"] = parts
    r["mass_b1_dry_g"] = total
    r["hold_up_clean_ml"] = hold_up_clean_ml()
    r["lumen_ml"] = lumen_volume_ml()
    r["clean_wet_ml"] = r["hold_up_clean_ml"] + r["lumen_ml"]
    r["lumen_capillary_rise_mm"] = 4 * GAMMA / (RHO * G * P["FIBRE_ID"] * 1e-3) * 1e3
    r["first_flush_ml"] = 50.0          # discard after storage: more than twice the wet clean side (HWB-DEC-001 F6)
    r["mass_b1_wet_g"] = total + r["clean_wet_ml"] + shell_water_ml()
    bb = None
    for q in M.components("B1", context=False):
        b = q["shape"].bounding_box()
        bb = b if bb is None else bb.add(b)
    r["b1_size_mm"] = dict(length=bb.max.Z - bb.min.Z, diameter=max(bb.max.X - bb.min.X, bb.max.Y - bb.min.Y))
    # mechanics: hoop stress in the housing wall
    t = (P["HOUSING_OD"] - P["HOUSING_ID"]) / 2
    r["hoop_mpa"] = {"squeeze_max": r["squeeze_kpa"]["adult_max"] * 1e3 * (P["HOUSING_ID"] / 2) / t / 1e6}
    # backflush
    sa = math.pi * (A["SYRINGE_BORE_MM"] * 1e-3 / 2) ** 2
    r["backflush_kpa"] = {k: f / sa / 1e3 for k, f in A["BACKFLUSH_PUSH_N"].items()}
    r["hoop_mpa"]["backflush_hard"] = r["backflush_kpa"]["hard"] * 1e3 * (P["HOUSING_ID"] / 2) / t / 1e6
    # flat end wall (independent review 2026-11-11): circular plate, uniform load, simply supported (1.24 p a2 / t2,
    # nu 0.3) as the bound, clamped (0.75) as the lower value; a = half the bore, t = END_WALL
    a2t2 = (P["HOUSING_ID"] / 2) ** 2 / P["END_WALL"] ** 2
    r["end_wall_mpa"] = {"squeeze_max_ss": 1.24 * r["squeeze_kpa"]["adult_max"] * 1e3 * a2t2 / 1e6,
                         "blocked_backflush_ss": 1.24 * r["backflush_kpa"]["hard"] * 1e3 * a2t2 / 1e6,
                         "blocked_backflush_clamped": 0.75 * r["backflush_kpa"]["hard"] * 1e3 * a2t2 / 1e6}
    r["end_wall_t_for_factor5_mm"] = (P["HOUSING_ID"] / 2) * math.sqrt(1.24 * r["backflush_kpa"]["hard"] * 1e3 / (10e6 / 5))
    # in the backflush procedure the collar end is open (capsule out, cartridge off the bottle), so the shell is near
    # atmospheric pressure; the clean-side pressure pushes on the potting face instead
    r["potting_push_n"] = r["backflush_kpa"]["hard"] * 1e3 * math.pi * (P["HEADER_ID"] * 1e-3 / 2) ** 2
    r["housing_thread_axial_n"] = r["backflush_kpa"]["hard"] * 1e3 * math.pi * (P["HOUSING_ID"] * 1e-3 / 2) ** 2
    r["housing_thread_shear_mpa"] = r["housing_thread_axial_n"] / (math.pi * P["SPIGOT_ROOT_D"] * 10.0 * 0.5)
    # integrity (air test by squeezing an empty bottle through the wetted cartridge)
    r["bubble_kpa"] = {"0.1um_pore": bubble_point(0.1), "17um_defect": bubble_point(17), "50um_defect": bubble_point(50),
                       "broken_lumen_500um": bubble_point(500)}
    r["air_test_smallest_defect_um"] = 4 * GAMMA / (r["squeeze_kpa"]["adult"] * 1e3) * 1e6
    # sieving ratios
    r["sieve_ratio"] = {"bacteria_0.5um": 0.5 / P["PORE_UM"], "crypto_4um": 4.0 / P["PORE_UM"], "giardia_8um": 8.0 / P["PORE_UM"],
                        "virus_0.02_0.3um": [0.02 / P["PORE_UM"], 0.3 / P["PORE_UM"]]}
    # B2 stability (fixed design: base radius from the model)
    w_bottle, w_stand = 1.0 + 0.03, 0.42
    z_cg = (w_bottle * (M.B2_TOP + 140.0) + w_stand * 190.0) / (w_bottle + w_stand)
    r["b2_stability"] = {"z_cg_mm": z_cg, "base_r_mm_v0": 65.0, "base_r_mm": M.B2_BASE_R,
                         "tip_deg_v0": math.degrees(math.atan(65.0 / z_cg)), "tip_deg": math.degrees(math.atan(M.B2_BASE_R / z_cg)),
                         "tip_force_n": (w_bottle + w_stand) * G * M.B2_BASE_R / z_cg}
    # duckbill refill (S19): tipped, the valve sits under the bottle's water; upright it sits in air
    r["duckbill_open_kpa"] = {"upright": A["DUCKBILL_CRACK_KPA"],
                              "tipped_full": A["DUCKBILL_CRACK_KPA"] + RHO * G * (P["BOTTLE_H"] - 20.0) * 1e-3 / 1e3}
    # B2 vent tube (S21): 4 x 0.8 tube, 2.4 mm bore, 230 mm long; Bond number below 3.37 (on diameter) keeps a water plug
    vbore = 2.4e-3
    r["b2_vent"] = {"bore_mm": vbore * 1e3, "bond": RHO * G * vbore ** 2 / GAMMA,
                    "purge_kpa": (RHO * G * 0.230 + 4 * GAMMA / vbore) / 1e3 + A["DUCKBILL_CRACK_KPA"]}
    # freezing
    r["freeze_expansion"] = 0.09
    # neck fit
    r["neck"] = dict(skirt_mm=15.5, h1881=P["NECK_H_1881"], h1810=P["NECK_H_1810"], clear_1881=P["NECK_H_1881"] - 15.5,
                     clear_1810=P["NECK_H_1810"] - 15.5)
    # cost and life
    sc = sum(A["SCALE_COST_USD"].values())
    life_l = A["L_PER_DAY"] * 30.4 * A["DESIGN_LIFE_MONTHS"]
    caps = max(0, math.ceil(life_l / A["CARBON_LIFE_L"]) - 1)
    life_cost = sc + caps * A["SCALE_COST_USD"]["carbon_capsule"]
    r["cost"] = dict(scale_unit_usd=sc, life_l=life_l, extra_capsules=caps, life_cost_usd=life_cost, usd_per_l=life_cost / life_l,
                     usd_per_user_year=life_cost * 12 / A["DESIGN_LIFE_MONTHS"])
    import csv
    rows = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
    r["bom_usd"] = sum(float(x["qty"]) * float(x["unit_cost_usd"]) for x in rows)
    r["bom_prototype_usd"] = sum(float(x["qty"]) * float(x["unit_cost_usd"]) for x in rows if "tool" not in x["make_buy"])
    return r


if __name__ == "__main__":
    res = run()
    (ROOT / "docs/04-calcs/sizing_results.json").write_text(json.dumps(res, indent=1, default=float))
    f = lambda x: round(x, 3)
    print("membrane area m2:", {k: f(v) for k, v in res["area_m2"].items()}, "packing", f(res["packing"]))
    print("squeeze kPa:", {k: round(v, 1) for k, v in res["squeeze_kpa"].items()})
    for k, v in res["b1"].items():
        c, d = v["clean"], v["fouled"]
        print(f"B1 {k:18s} clean {c['q_ml_min']:6.0f} mL/min (membrane {c['membrane_kpa']:.2f}, bed {c['bed_kpa']:.2f}, lumen {c['lumen_kpa']:.2f}, outlet {c['outlet_kpa']:.2f} kPa)  fouled {d['q_ml_min']:6.0f}")
    print("B1 at 10 kPa:", round(res["b1_at_10kpa"]["clean"]["q_ml_min"]), round(res["b1_at_10kpa"]["fouled"]["q_ml_min"]), "upper", round(res["b1_at_10kpa_upper"]["q_ml_min"]))
    print("B2:", {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in res["b2"].items()})
    print("B3:", {k: (round(v["clean"]["press_kpa"], 1), round(v["clean"]["q_ml_min"]), round(v["fouled"]["q_ml_min"])) for k, v in res["b3"].items()}, res["b3_volumes"])
    print("carbon:", {k: (v if not isinstance(v, dict) else {kk: round(vv, 1) for kk, vv in v.items()}) for k, v in res["carbon"].items()})
    print("B1 dry mass g:", round(res["mass_b1_dry_g"], 1), "size", {k: round(v) for k, v in res["b1_size_mm"].items()}, "clean hold-up mL", round(res["hold_up_clean_ml"], 2))
    print("hoop MPa", {k: round(v, 2) for k, v in res["hoop_mpa"].items()}, "backflush kPa", {k: round(v) for k, v in res["backflush_kpa"].items()})
    print("bubble kPa", {k: round(v, 1) for k, v in res["bubble_kpa"].items()}, "air test smallest defect um", round(res["air_test_smallest_defect_um"], 1))
    print("B2 stability", {k: round(v, 1) for k, v in res["b2_stability"].items()})
    print("10 C:", {k: (round(v["clean"]["q_ml_min"]), round(v["fouled"]["q_ml_min"])) for k, v in res["b1_10c"].items()},
          "B2 min/L", round(res["b2_10c"]["clean"]["minutes_per_litre"], 1), round(res["b2_10c"]["fouled"]["minutes_per_litre"], 1))
    print("lumens mL", round(res["lumen_ml"], 1), "clean wet mL", round(res["clean_wet_ml"], 1), "capillary mm", round(res["lumen_capillary_rise_mm"]),
          "wet mass g", round(res["mass_b1_wet_g"]))
    print("end wall MPa", {k: round(v, 2) for k, v in res["end_wall_mpa"].items()}, "t for factor 5", round(res["end_wall_t_for_factor5_mm"], 1),
          "potting N", round(res["potting_push_n"]), "thread MPa", round(res["housing_thread_shear_mpa"], 2))
    print("duckbill kPa", {k: round(v, 2) for k, v in res["duckbill_open_kpa"].items()}, "vent", {k: round(v, 2) for k, v in res["b2_vent"].items()})
    print("cost", {k: round(v, 3) for k, v in res["cost"].items()}, "BOM", round(res["bom_usd"], 2))
