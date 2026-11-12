#!/usr/bin/env python3
"""HWC-CAL-001 sizing calculations for Helpful Water C (household gravity filter). Run from the solution folder:

    python docs/04-calcs/sizing.py

Reads the dimensions in cad/src/params.py (PARAMS, shared with cad/src/model.py) and the BOM total, and writes
docs/04-calcs/sizing_results.json, which the STEM check (docs/04-calcs/stem_check.py) and the calculation note
(01-sizing.md) use. First-order engineering estimates only: every assumption is named in ASSUMED and marked
"assumed" in the note. No result here is a measured or tested value.

Licence: Apache-2.0 (Helpful Engineering licensing guide). Design Molecule Labs with Helpful Engineering.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad/src")]
from params import PARAMS as P  # noqa: E402

G = 9.80665
RHO = 998.0          # water at 20 C, kg/m3
MU = 1.0e-3          # water viscosity at 20 C, Pa s
GAMMA = 0.0728       # surface tension of water at 20 C, N/m

ASSUMED = {
    # membrane (to confirm from the supplier's clean-water flux at a stated pressure; HWC-DEC-001 C1)
    "LP_CLEAN_LMH_BAR": 1000.0,   # clean-water permeability, L/(m2 h bar); same design value as solutions A and B
    "LP_FOULED_SHARE": 0.5,       # share of clean permeability left when a backflush is due
    "MODULE_LIFE_L": 30000.0,     # module life to retirement, litres; assumed (LifeStraw Family 2.0 is rated 30,000 L)
    # fittings: loss coefficients (K) for bulkhead, strainer, ball valve, barbs, tee, lid inlet; typical handbook values
    "K_FITTINGS": {"bulkhead_entry": 0.5, "strainer": 2.0, "ball_valve_open": 0.2, "barbs_and_tee": 4.0, "exit": 1.0},
    # stand
    "STAND_KG": 9.0, "BUCKET_KG": 1.2, "TIP_CRITERION_DEG": 15.0,
    # humans
    "PUSH_HEIGHT_M": 1.0,         # height of an accidental push or a child pulling on the shelf
    "SYRINGE_PUSH_N": {"gentle": 30.0, "hard": 100.0},
    "TAP_CD": 0.6,
    # ceramic candles (C2): British Berkefeld data, 2 candles give 2 L/h in the 12 L system (checked 2026-11-11)
    "CANDLE_LPH_FULL": 1.0,       # one candle, upper chamber full (about 0.3 m of water over the candle base)
    "CANDLE_LIFE_L": 10000.0,     # Engineering for Change listing, per candle
    # biosand (C3): CAWST 2009 fact sheet
    "BSF_MAX_LPM": 0.4, "BSF_BATCH_L": 18.0, "BSF_PAUSE_MIN_H": 1.0, "BSF_RIPEN_DAYS": 30,
    "SAND_BULK": 1600.0,          # kg/m3, dry sand and gravel; assumed
    # chlorine co-treatment interface (solution D): CDC Safe Water System and EPA CT tables
    "CL_DOSE_MGL": {"clear": 1.875, "turbid": 3.75},      # 3.75 and 7.5 %-mL per 20 L
    "CL_RESIDUAL_30MIN_MGL": 0.5,                          # conservative free chlorine after 30 min (assumed)
    "CT_VIRUS_4LOG": {"5C": 8.0, "10C": 6.0, "20C": 3.0},  # mg min/L, pH 6 to 9
    "CT_CRYPTO": 15300.0,                                  # mg min/L (CDC hyperchlorination guidance)
    "PVDF_CL_LIFETIME_PPMH": 3.0e6,                        # LG Water Solutions PVDF UF lifetime chlorine tolerance
    # costs at scale (estimates for MKT; not quotes)
    "SCALE_COST_USD": {"module": 8.0, "two_buckets_lids": 6.0, "tap_valve_fittings": 3.5, "hoses": 1.2,
                       "printed_or_moulded_parts": 1.5, "stand_local_timber": 6.0, "assembly_qc_pack": 3.0},
}
A = ASSUMED


# ------------------------------------------------------------------------------------------------------------
def bucket_inside():
    rb = (P["BKT_BOT_OD"] / 2 - P["BKT_WALL"]) / 1000
    rt = (P["BKT_TOP_OD"] / 2 - P["BKT_WALL"]) / 1000
    H = (P["BKT_H"] - P["BKT_FLOOR"]) / 1000
    return rb, rt, H


def vol_to_depth(h):
    """Inside volume (m3) of the tapered bucket up to depth h (m)."""
    rb, rt, H = bucket_inside()
    r = rb + (rt - rb) * h / H
    return math.pi * h / 3 * (rb * rb + rb * r + r * r)


def depth_for(v_m3):
    lo, hi = 0.0, bucket_inside()[2]
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if vol_to_depth(mid) < v_m3 else (lo, mid)
    return (lo + hi) / 2


def area_at(h):
    rb, rt, H = bucket_inside()
    r = rb + (rt - rb) * h / H
    return math.pi * r * r


def membrane_area():
    return P["U_FIBRES"] * math.pi * P["FIBRE_OD"] * 1e-3 * 2 * P["LEG_LEN"] * 1e-3     # outside area, m2


AREA = membrane_area()


def network_kpa(q_lph, lp_share=1.0):
    """Pressure taken by each stage at flow q (L/h)."""
    q = q_lph / 3.6e6                                      # m3/s
    lp = A["LP_CLEAN_LMH_BAR"] * lp_share / 100.0          # L/(m2 h kPa)
    membrane = q_lph / (lp * AREA)
    # lumens: each U fibre has two legs; permeate collects along the leg, so the mean lumen loss is half the full
    # Hagen-Poiseuille loss of the leg's total flow
    q_leg = q / (2 * P["U_FIBRES"])
    d = P["FIBRE_ID"] * 1e-3
    lumen = 128 * MU * P["LEG_LEN"] * 1e-3 * q_leg / (math.pi * d ** 4) / 2 / 1000
    dh = P["HOSE_ID"] * 1e-3
    hose = 128 * MU * (P["HOSE_RAW_L"] + P["HOSE_CLEAN_L"]) * q / (math.pi * dh ** 4) / 1000
    v_barb = q / (math.pi * (P["BARB_BORE"] * 1e-3) ** 2 / 4)
    fittings = sum(A["K_FITTINGS"].values()) * RHO * v_barb ** 2 / 2 / 1000
    return dict(membrane_kpa=membrane, lumen_kpa=lumen, hose_kpa=hose, fittings_kpa=fittings,
                total_kpa=membrane + lumen + hose + fittings)


def flow_at(head_kpa, lp_share=1.0):
    lo, hi = 0.0, 500.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if network_kpa(mid, lp_share)["total_kpa"] < head_kpa else (lo, mid)
    return (lo + hi) / 2


def levels():
    floor_z = P["TOP_Z"] + P["BKT_FLOOR"]
    outlet_z = floor_z + P["OUTLET_H"]
    full_z = floor_z + depth_for(P["FILL_L"] / 1000) * 1000
    discharge_z = P["LOW_Z"] + P["SHELF_T"] + P["BKT_H"] + P["LID_T"] + P["CLEAN_INLET_TOP"]
    return floor_z, outlet_z, full_z, discharge_z


def batch(lp_share):
    """Falling-head drain of one raw batch from the fill line to the outlet, 10 s steps."""
    floor_z, outlet_z, full_z, discharge_z = levels()
    h = (full_z - floor_z) / 1000
    h_end = (outlet_z - floor_z) / 1000 + 0.005
    t, vol = 0.0, 0.0
    while h > h_end:
        head = (floor_z / 1000 + h - discharge_z / 1000) * RHO * G / 1000
        q = flow_at(head, lp_share) / 3.6e6
        dv = q * 10.0
        vol += dv
        h -= dv / area_at(h)
        t += 10.0
    return dict(minutes=t / 60, litres=vol * 1000)


def stokes_mm_per_h(d_um, rho_p=2650.0, mu=MU):
    d = d_um * 1e-6
    return G * d * d * (rho_p - RHO) / (18 * mu) * 3.6e6


def bom_total():
    f = ROOT / "bom/bom.csv"
    if not f.exists():
        return None
    return round(sum(float(r["unit_cost_usd"]) * float(r["qty"]) for r in csv.DictReader(f.open())), 2)


def main():
    res = {"assumed": A, "area_m2": round(AREA, 4)}
    demand = P["PERSONS"] * P["L_PER_PERSON_DAY"]
    res["demand"] = dict(l_per_day=demand, sphere_range=[P["PERSONS"] * 5.5, P["PERSONS"] * 9.0],
                         who_basic_l_per_day=P["PERSONS"] * 7.5)
    floor_z, outlet_z, full_z, discharge_z = levels()
    v_dead = vol_to_depth(P["OUTLET_H"] / 1000) * 1000
    brim = vol_to_depth(bucket_inside()[2]) * 1000
    res["overflow"] = dict(worst_batch_l=round(brim - v_dead, 2), clean_free_l=round(brim - P["REFILL_L"], 2))
    res["raw"] = dict(fill_l=P["FILL_L"], fill_depth_mm=round(full_z - floor_z, 1), settle_zone_l=round(v_dead, 2),
                      batch_l=round(P["FILL_L"] - v_dead, 2), rim_z_mm=P["TOP_Z"] + P["BKT_H"],
                      brim_l=round(vol_to_depth(bucket_inside()[2]) * 1000, 1))
    h_min = (outlet_z - discharge_z) / 1000 * RHO * G / 1000
    h_max = (full_z - discharge_z) / 1000 * RHO * G / 1000
    res["head"] = dict(outlet_z=outlet_z, full_z=round(full_z, 1), discharge_z=discharge_z,
                       head_m=[round((outlet_z - discharge_z) / 1000, 3), round((full_z - discharge_z) / 1000, 3)],
                       head_kpa=[round(h_min, 2), round(h_max, 2)], mean_kpa=round((h_min + h_max) / 2, 2))
    flows = {}
    for state, share in (("clean", 1.0), ("fouled", A["LP_FOULED_SHARE"])):
        q_mean = flow_at((h_min + h_max) / 2, share)
        stages = network_kpa(q_mean, share)
        b = batch(share)
        n_batches = demand / b["litres"]
        flows[state] = dict(q_full_lph=round(flow_at(h_max, share), 1), q_empty_lph=round(flow_at(h_min, share), 1),
                            q_mean_lph=round(q_mean, 1), q_mean_ml_min=round(q_mean / 0.06, 0),
                            stages_at_mean={k: round(v, 3) for k, v in stages.items()},
                            batch_min=round(b["minutes"], 1), batch_l=round(b["litres"], 2),
                            batches_per_day=round(n_batches, 2), hours_per_day=round(n_batches * b["minutes"] / 60, 2))
    res["c1"] = flows
    for state in flows:
        cyc = 1.5 + flows[state]["batch_min"] / 60          # 1 h settle + 30 min contact, then the batch
        flows[state]["elapsed_h_per_day"] = round(flows[state]["batches_per_day"] * cyc, 1)
    # clean side: pressure at the module outlet (bottom) is positive whenever the discharge point is above it
    mod_bottom = P["MOD_TOP_Z"] - P["MOD_L"]
    res["clean_side_kpa_at_module"] = round((discharge_z - mod_bottom) / 1000 * RHO * G / 1000, 2)
    res["module_raw_side_kpa_max"] = round((full_z - P["MOD_TOP_Z"]) / 1000 * RHO * G / 1000 + (P["MOD_L"]) / 1000 * RHO * G / 1000, 2)
    # settling
    res["stokes_mm_per_h"] = {f"{d}um": round(stokes_mm_per_h(d), 1) for d in (2, 5, 10, 20, 50)}
    res["stokes_5c_mm_per_h"] = {f"{d}um": round(stokes_mm_per_h(d, mu=1.52e-3), 1) for d in (10, 20)}
    res["settle_depth_mm"] = round(full_z - outlet_z, 1)
    res["settle_h"] = {"20C": round(res["settle_depth_mm"] / stokes_mm_per_h(10), 2),
                       "5C": round(res["settle_depth_mm"] / stokes_mm_per_h(10, mu=1.52e-3), 2)}
    # stability of the C1 stand: worst case raw bucket full, clean bucket empty
    m_raw = P["FILL_L"] + A["BUCKET_KG"]
    z_raw = (P["TOP_Z"] + (full_z - P["TOP_Z"]) / 2) / 1000
    z_clean = (P["LOW_Z"] + P["SHELF_T"] + P["BKT_H"] / 2) / 1000
    m = m_raw + A["BUCKET_KG"] + A["STAND_KG"]
    zg = (m_raw * z_raw + A["BUCKET_KG"] * z_clean + A["STAND_KG"] * 0.45) / m
    stab = {}
    for label, half in (("frame_420", 0.210), ("feet_560", P["FOOT_L"] / 2000)):
        stab[label] = dict(half_base_m=half, cg_m=round(zg, 3), tip_deg=round(math.degrees(math.atan(half / zg)), 1),
                           push_n=round(m * G * half / A["PUSH_HEIGHT_M"], 0))
    res["stability"] = stab
    res["mass_full_kg"] = round(P["FILL_L"] + 20.0 + 2 * A["BUCKET_KG"] + A["STAND_KG"] + 1.0, 1)
    # tap
    h_tap = (depth_for(5.0 / 1000) * 1000 - P["TAP_H"]) / 1000          # cup timed with 5 L in the bucket
    h_tap_full = (depth_for(0.018) * 1000 - P["TAP_H"]) / 1000
    a_tap = math.pi * (P["TAP_BORE"] / 1000) ** 2 / 4
    q_tap = [A["TAP_CD"] * a_tap * math.sqrt(2 * G * max(h, 0.01)) * 6e4 for h in (h_tap, h_tap_full)]
    res["tap"] = dict(head_m=[round(h_tap, 3), round(h_tap_full, 3)], l_per_min=[round(q, 2) for q in q_tap],
                      cup_250ml_s=round(0.25 / q_tap[0] * 60, 1))
    # backflush and integrity
    a_s = math.pi * (A and P["SYRINGE_BORE_MM"] / 1000) ** 2 / 4
    res["backflush_kpa"] = {k: round(v / a_s / 1000, 1) for k, v in A["SYRINGE_PUSH_N"].items()}
    res["bubble_point_kpa_0p1um"] = round(4 * GAMMA / 0.1e-6 / 1000, 0)
    res["air_test"] = dict(test_kpa=100.0, push_n=round(100e3 * a_s, 1),
                           smallest_defect_um=round(4 * GAMMA / 100e3 * 1e6, 2))
    # chlorine interface (solution D in the raw bucket)
    ct = A["CL_RESIDUAL_30MIN_MGL"] * 30
    res["chlorine"] = dict(ct_30min=ct, virus_4log_ct_5c=A["CT_VIRUS_4LOG"]["5C"],
                           crypto_hours_at_dose=round(A["CT_CRYPTO"] / A["CL_DOSE_MGL"]["clear"] / 60, 0), dose_clear=A["CL_DOSE_MGL"]["clear"],
                           pvdf_exposure_ppmh_life=round(A["CL_DOSE_MGL"]["turbid"] * 24 * 365 * 3, 0),
                           pvdf_share_of_limit=round(A["CL_DOSE_MGL"]["turbid"] * 24 * 365 * 3 / A["PVDF_CL_LIFETIME_PPMH"], 4))
    # clean-side hold-up between batches
    d_h = P["HOSE_ID"] / 1000
    lumens_ml = 2 * P["U_FIBRES"] * P["LEG_LEN"] * math.pi * P["FIBRE_ID"] ** 2 / 4 / 1000
    res["lumens_ml"] = round(lumens_ml, 1)
    res["hold_up_clean_ml"] = round(math.pi * d_h ** 2 / 4 * P["HOSE_CLEAN_L"] * 1e6 + lumens_ml + 5.0, 0)   # + 5 mL in the tee (assumed)
    res["air_test"]["strokes"] = "displace the lumen water (about 52 mL), then pump air strokes through the check valve until a firm 56 N push holds"
    # C2 ceramic candles: flow falls as the upper chamber drains (linear with mean head over the candle)
    q2 = P["CANDLES"] * A["CANDLE_LPH_FULL"]
    batch2 = P["FILL_L"] - 1.0
    hours2 = batch2 / (q2 * 0.6)          # mean 60 % of full-chamber flow over a draining batch (assumed)
    res["c2"] = dict(q_full_lph=q2, batch_l=batch2, batch_hours=round(hours2, 1),
                     hours_per_day=round(demand / batch2 * hours2, 1),
                     candle_area_m2=round(math.pi * P["CANDLE_OD"] / 1000 * P["CANDLE_L"] / 1000, 4),
                     life_l=A["CANDLE_LIFE_L"] * P["CANDLES"])
    # C3 biosand
    r3 = P["BSF_ID"] / 2000
    a3 = math.pi * r3 * r3
    beds = sum(P["BSF_LAYERS"].values()) / 1000
    res["c3"] = dict(area_m2=round(a3, 4), loading_lph_m2_at_max=round(A["BSF_MAX_LPM"] * 60 / a3, 0),
                     batch_min=round(A["BSF_BATCH_L"] / A["BSF_MAX_LPM"] / 0.7, 0),   # mean 70 % of the initial rate (assumed)
                     batches_per_day=round(demand / A["BSF_BATCH_L"], 2),
                     media_kg=round(a3 * beds * A["SAND_BULK"], 0), ripening_days=A["BSF_RIPEN_DAYS"])
    # sizes, masses, cost
    tot = bom_total()
    res["bom_usd"] = tot
    if tot:
        res["cost_per_litre_usd"] = round(tot / A["MODULE_LIFE_L"], 4)
        res["module_life_years"] = round(A["MODULE_LIFE_L"] / demand / 365, 2)
        res["cost_per_person_year_usd"] = round(tot / res["module_life_years"] / P["PERSONS"], 2)
    res["scale_cost_usd"] = round(sum(A["SCALE_COST_USD"].values()), 2)
    res["c1_size_mm"] = dict(width=P["FOOT_L"], depth=P["FOOT_L"], height=round(P["TOP_Z"] + P["BKT_H"] + P["LID_T"] + 30, 0))
    out = ROOT / "docs/04-calcs/sizing_results.json"
    out.write_text(json.dumps(res, indent=1, default=float))
    c = res["c1"]
    print(f"area {AREA:.3f} m2; head {res['head']['head_kpa']} kPa; clean {c['clean']['q_mean_lph']} L/h, batch "
          f"{c['clean']['batch_min']} min; fouled {c['fouled']['q_mean_lph']} L/h, {c['fouled']['hours_per_day']} h/day")
    print("stability", res["stability"])
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
