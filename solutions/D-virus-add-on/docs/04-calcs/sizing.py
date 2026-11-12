#!/usr/bin/env python3
"""HWD-CAL-001 sizing calculations for Helpful Water D (chlorine add-on for viruses). Run from the solution folder:

    python docs/04-calcs/sizing.py

Reads the dimensions in cad/src/model.py PARAMS and writes docs/04-calcs/sizing_results.json, which the STEM check
(docs/04-calcs/stem_check.py) and the calculation note (01-sizing.md) use. First-order estimates only: every
assumption is named in ASSUMED and marked "assumed" in the note. No result here is a measured or tested value.

Sections: 1 dose arithmetic (NaDCC and hypochlorite); 2 free chlorine residual model; 3 CT against inactivation data;
4 pH and temperature; 5 ball timer; 6 overdose and by-products; 7 D2 liquid strength over shelf life; 8 D3 erosion
feeder range; 9 effort, mass and size; 10 cost and cost per litre.

Licence: Apache-2.0 (Helpful Engineering licensing guide). Design Molecule Labs with Helpful Engineering.
"""
from __future__ import annotations

import csv
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad/src"), str(ROOT / ".kit")]
import model as M  # noqa: E402

P = M.PARAMS
G = 9.80665

# ---- cited data (sources in 01-sizing.md; checked 2026-11-11) ------------------------------------------------------
CITED = {
    # IFRC catalogue WASDCHLA01: household tablets 3.5 mg NaDCC = 2 mg Cl per 1 L; 67 mg = 40 mg Cl per 20 L (2 mg/L);
    # IFRC tablet-choice note: 67 mg household tablet per 20 to 25 L; turbidity bands 0-5, 5-50, >50 NTU (do not chlorinate)
    "TAB": {"1L": (3.5, 2.0), "20L": (67.0, 40.0), "5L": (33.0, 20.0), "1L_emergency": (8.5, 5.0)},
    "NTU_BANDS": (5.0, 50.0),
    # CDC Safe Water System (Lantagne et al., NAE 2006): 1.25 % NaOCl, one 3 mL cap per 20 L clear, two caps turbid;
    # free chlorine below 2.0 mg/L at 1 h (acceptability), above 0.2 mg/L at 24 h (protection)
    "SWS": {"pct": 1.25, "cap_ml": 3.0, "litres": 20.0, "max_1h": 2.0, "min_24h": 0.2},
    "WHO_MIN_30MIN": 0.5,          # mg/L after >= 30 min at pH < 8 (WHO GDWQ, via WEDC Mobile Note 7)
    "WHO_GV": 5.0,                 # mg/L, chlorine guideline value (WHO chlorine fact sheet 2022)
    "WHO_POINT_OF_USE": (0.2, 1.0),  # IFRC tablet note: ideal free chlorine at point of use
    "TASTE": {"detect_naocl": 0.70, "detect_nadcc": 0.73, "accept_naocl": 1.16, "accept_nadcc": 1.26},  # Crider et al. 2018
    # EPA CT for 4-log virus inactivation by free chlorine, pH 6 to 9 and pH 10 (mg min/L) by temperature (C)
    "CT_VIRUS_4LOG": {0.5: 12, 5: 8, 10: 6, 15: 4, 20: 3, 25: 2},
    "CT_VIRUS_4LOG_PH10": {0.5: 90, 5: 60, 10: 45, 15: 30, 20: 22, 25: 15},
    # CDC chlorine timetable at 1 mg/L, pH 7.5, 25 C (minutes, so CT in mg min/L)
    "CT_CDC_1MGL": {"E. coli O157:H7": 1.0, "Hepatitis A virus": 16.0, "Giardia": 45.0, "Cryptosporidium": 15300.0},
    "CT_NOROVIRUS_GII_2LOG": 13.0,  # Dunkin et al. 2017, human norovirus GII, 2-log (molecular), produce wash water
    "AKVO_CONTACT_MIN": {">18 C": 30, "10-18 C": 60, "<10 C": 120},     # Akvopedia NaDCC page
    "AKVO_PH": (5.5, 7.5), "AKVO_PH_UNRELIABLE": 9.0,
    "PKA_HOCL_20C": 7.54,             # kept for reference; the model now uses Morris (1966), pKa = 3000/T - 10.0686 + 0.0253 T
    "NADCC_GV": 50.0, "CYA_GV": 40.0,   # WHO NaDCC chemical fact sheet, mg/L
    "SHELF": {"tablet_strip_y": 5.0, "tablet_tub_y": 3.0, "liquid_months": 3.0},  # Akvopedia
    "HYPO_HALF_LIFE_COOL_Y": 1.0,      # WEDC Mobile Note 7: can lose half its strength in a year, sealed, cool and dark
    "HYPO_WARM": (13.0, 8.0, 75.0),     # E4C WaterGuard: 13 % product fell to 8 % in 75 days at 80 F (27 C), sealed
    "PDMS_VTC": 0.61,                   # Dow XIAMETER PMX-200 data sheet, high-viscosity grades
    "PDMS_EXPANSION_PER_K": 9.6e-4,     # Dow PMX-200 data sheet, volumetric expansion coefficient
    "ORING_STATIC_SQUEEZE": (15.0, 30.0),  # % squeeze, static radial gland (as cited in HWD-STM-001 S26)
    "SURFACE_TENSION_N_M": 0.072,       # water at 25 C; 1.25 % hypochlorite taken as water
    "HARKINS_BROWN": (0.60, 0.72),      # Harkins-Brown correction to Tate's law over the usual drop range
}
MW = {"NaDCC": 219.95, "NaDCC_2H2O": 255.98, "Cl2": 70.906, "CYA": 129.07}

ASSUMED = {
    # residual model C(t): instant demand d30 consumed over the first 30 min (time constant 6 min), then first order k
    "SCEN": {
        "clear":        dict(dose=2.0, d30=0.30, k_h=0.035, ntu="under 5 NTU"),
        "turbid_double": dict(dose=4.0, d30=1.00, k_h=0.070, ntu="5 to 50 NTU, settled, double dose"),
        "turbid_single": dict(dose=2.0, d30=1.00, k_h=0.070, ntu="5 to 50 NTU, single dose (misuse case)"),
    },
    "TAU_MIN": 6.0,
    # timer: Faxen wall factor, nominal fall time with 10 % margin over 30 min
    "TIMER_TARGET_MIN": 45.0, "VISC_TOL": 0.10, "PDMS_EA_J_MOL": 15000.0,   # activation energy assumed (VTC 0.61 back-calculates 14.8 kJ/mol)
    "TIMER_T_MAX_C": 40.0, "TIMER_FILL_C": 25.0, "TIMER_T_RANGE_C": (-10.0, 60.0),   # timer at air temperature; storage range
    "BOTTLES_L": (0.5, 1.0, 1.5, 2.0),
    "RHO_BALL": 7900.0, "RHO_FLUID": 975.0,
    # D2 drops and liquid decay in heat
    # D3 standing times in a household raw-water bucket
    "STAND_H": (0.5, 24.0),
    # use
    "L_PER_DAY_PERSONAL": 3.0, "HOUSEHOLD": 5, "L_PER_PERSON_DAY": 5.0, "LIFE_Y": 2.0,
    # scale cost estimates (not quotes)
    "SCALE_COST_USD": {"moulded_parts": 0.45, "seals": 0.10, "timer": 0.35, "labels": 0.10, "assembly_qc_pack": 0.40},
    "TAB_COST_HUMANITARIAN_USD": 0.011,   # CHF 0.01 pre-budget, about USD 0.011 (exchange rate assumed)
    "TAB_COST_RETAIL_USD": 10.99 / 50,
}
A = ASSUMED


def residual(dose, d30, k_h, t_min):
    tau = A["TAU_MIN"]
    if t_min <= 30:
        return dose - d30 * (1 - math.exp(-t_min / tau)) / (1 - math.exp(-30 / tau))
    return (dose - d30) * math.exp(-k_h * (t_min - 30) / 60)


def ct(dose, d30, k_h, t_min, n=600):
    h = t_min / n
    return sum(residual(dose, d30, k_h, (i + 0.5) * h) * h for i in range(n))


def ct_epa(dose, d30, k_h, t_min):
    """US EPA definition for a batch: residual at the end of contact x contact time (lower than the integral)."""
    return residual(dose, d30, k_h, t_min) * t_min


def t_for_ct(dose, d30, k_h, target):
    t, acc, h = 0.0, 0.0, 0.05
    while acc < target and t < 24 * 60:
        acc += residual(dose, d30, k_h, t + h / 2) * h
        t += h
    return t


def pka_hocl(t_c):
    """Morris (1966): pKa of HOCl by temperature, 7.54 at 25 C, 7.58 at 20 C, 7.75 at 5 C."""
    tk = t_c + 273.15
    return 3000.0 / tk - 10.0686 + 0.0253 * tk


def hocl_share(ph, t_c=20.0):
    return 1 / (1 + 10 ** (ph - pka_hocl(t_c)))


def faxen(lam):
    return 1 - 2.104 * lam + 2.09 * lam ** 3 - 0.95 * lam ** 5


def haberman_sayre(lam):
    """Wall factor (velocity ratio) for a sphere on the axis of a tube; valid to d/D about 0.8 (Faxen only to about 0.3)."""
    return (1 - 2.105 * lam + 2.0865 * lam ** 3 - 1.7068 * lam ** 5 + 0.72603 * lam ** 6) / (1 - 0.75857 * lam ** 5)


def visc_ratio(t_c):
    """PDMS viscosity at t_c over viscosity at 25 C (Arrhenius with the assumed activation energy)."""
    return math.exp(A["PDMS_EA_J_MOL"] / 8.314 * (1 / (t_c + 273.15) - 1 / 298.15))


def tate_drop_ml(orifice_mm, f):
    """Tate's law with the Harkins-Brown factor; LDPE does not wet, so the drop pins at the orifice."""
    return 2 * math.pi * (orifice_mm / 2000.0) * CITED["SURFACE_TENSION_N_M"] / (1000.0 * G) * f * 1e6


def bom_total():
    tot = 0.0
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        tot += float(r["qty"]) * float(r["unit_cost_usd"])
    return tot


def bom_split():
    dev, cons = 0.0, 0.0
    for r in csv.DictReader((ROOT / "bom/bom.csv").open()):
        v = float(r["qty"]) * float(r["unit_cost_usd"])
        if "NaDCC tablets" in r["item"]:
            cons += v
        else:
            dev += v
    return dev, cons


def main():
    r = {}
    # 1 dose arithmetic -------------------------------------------------------------------------------------------
    # each NaDCC carries two active Cl; each releases one HOCl, counted as one Cl2 of available chlorine: 2 x 70.906 / MW
    f = {"anhydrous": 2 * MW["Cl2"] / MW["NaDCC"], "dihydrate": 2 * MW["Cl2"] / MW["NaDCC_2H2O"]}
    r["nadcc_available_cl"] = {k: round(v, 3) for k, v in f.items()}
    r["tablet_cl_share"] = {k: round(v[1] / v[0], 3) for k, v in CITED["TAB"].items()}
    doses = {
        "D1_1L_one": CITED["TAB"]["1L"][1] / 1.0, "D1_1L_two": 2 * CITED["TAB"]["1L"][1] / 1.0,
        "D1_20L_one": CITED["TAB"]["20L"][1] / 20.0, "D1_20L_two": 2 * CITED["TAB"]["20L"][1] / 20.0,
        "D1_20L_one_25L": CITED["TAB"]["20L"][1] / 25.0,
        "D1_1L_in_1_5L": CITED["TAB"]["1L"][1] / 1.5,
    }
    c = P["HYPO_PCT"] * 10.0        # g/L, so mg/mL
    doses["D2_20L_one_cap"] = c * P["DOSE_ML"] / 20.0
    doses["D2_20L_two_caps"] = 2 * c * P["DOSE_ML"] / 20.0
    hb = CITED["HARKINS_BROWN"]
    drop = [tate_drop_ml(P["DROP_ORIFICE"], f_) for f_ in hb]
    drop_briefed = [tate_drop_ml(1.2, f_) for f_ in hb]
    doses["D2_1L_drops_low"] = c * P["DROPS_1L"] * drop[0]
    doses["D2_1L_drops_high"] = c * P["DROPS_1L"] * drop[1]
    doses["D2_1L_3_drops_1_2mm_low"] = c * 3 * drop_briefed[0]
    doses["D2_1L_3_drops_1_2mm_high"] = c * 3 * drop_briefed[1]
    r["drop_ml"] = {"orifice_mm": P["DROP_ORIFICE"], "drops_1L": P["DROPS_1L"], "range": [round(v, 4) for v in drop],
                    "briefed_1_2mm_range": [round(v, 4) for v in drop_briefed]}
    # bottle volume range for the 1 L tablet (one and two tablets)
    r["bottle_range"] = {str(v): {"one": round(CITED["TAB"]["1L"][1] / v, 2), "two": round(2 * CITED["TAB"]["1L"][1] / v, 2)}
                         for v in A["BOTTLES_L"]}
    r["dose_mg_l"] = {k: round(v, 3) for k, v in doses.items()}
    co, ci, chh = P["CHAMBER"]
    so, si, sh = P["STANDPIPE"]
    r["chamber_ml"] = round(math.pi / 4 * (ci ** 2 - so ** 2) * sh / 1000.0, 3)
    r["d2_bottle_litres_treated"] = round(150.0 / P["DOSE_ML"] * 20.0)
    # 2 residual model ---------------------------------------------------------------------------------------------
    sc = {}
    for k, s in A["SCEN"].items():
        sc[k] = dict(c30=round(residual(s["dose"], s["d30"], s["k_h"], 30), 3), c60=round(residual(s["dose"], s["d30"], s["k_h"], 60), 3),
                     c24h=round(residual(s["dose"], s["d30"], s["k_h"], 24 * 60), 3),
                     consumed_24h=round(s["dose"] - residual(s["dose"], s["d30"], s["k_h"], 24 * 60), 3),
                     ct30=round(ct(s["dose"], s["d30"], s["k_h"], 30), 2), ct60=round(ct(s["dose"], s["d30"], s["k_h"], 60), 2),
                     ct120=round(ct(s["dose"], s["d30"], s["k_h"], 120), 2), ntu=s["ntu"], dose=s["dose"],
                     ct30_epa=round(ct_epa(s["dose"], s["d30"], s["k_h"], 30), 2), ct120_epa=round(ct_epa(s["dose"], s["d30"], s["k_h"], 120), 2))
        sc[k]["t_ct_virus_4log_5c_min"] = round(t_for_ct(s["dose"], s["d30"], s["k_h"], CITED["CT_VIRUS_4LOG"][5]), 1)
        sc[k]["t_ct_virus_4log_0c_min"] = round(t_for_ct(s["dose"], s["d30"], s["k_h"], CITED["CT_VIRUS_4LOG"][0.5]), 1)
        sc[k]["t_ct_hav_cdc_min"] = round(t_for_ct(s["dose"], s["d30"], s["k_h"], CITED["CT_CDC_1MGL"]["Hepatitis A virus"]), 1)
        sc[k]["t_ct_giardia_min"] = round(t_for_ct(s["dose"], s["d30"], s["k_h"], CITED["CT_CDC_1MGL"]["Giardia"]), 1)
        sc[k]["days_ct_crypto"] = round(CITED["CT_CDC_1MGL"]["Cryptosporidium"] / max(0.05, sc[k]["c30"]) / 1440, 1)
    r["scenarios"] = sc
    # 3 CT margins -------------------------------------------------------------------------------------------------
    cl = sc["clear"]
    r["ct_margin"] = {
        "virus_4log_5c_at_30min": round(cl["ct30_epa"] / CITED["CT_VIRUS_4LOG"][5], 2),
        "virus_4log_0c_at_30min": round(cl["ct30_epa"] / CITED["CT_VIRUS_4LOG"][0.5], 2),
        "virus_4log_0c_at_120min": round(cl["ct120_epa"] / CITED["CT_VIRUS_4LOG"][0.5], 2),
        "virus_4log_ph10_5c_at_120min": round(cl["ct120_epa"] / CITED["CT_VIRUS_4LOG_PH10"][5], 2),
        "norovirus_gii_2log_at_30min": round(cl["ct30_epa"] / CITED["CT_NOROVIRUS_GII_2LOG"], 2),
        "hav_cdc_at_30min": round(cl["ct30_epa"] / CITED["CT_CDC_1MGL"]["Hepatitis A virus"], 2),
        "giardia_at_30min": round(cl["ct30_epa"] / CITED["CT_CDC_1MGL"]["Giardia"], 2),
        "crypto_at_30min": round(cl["ct30_epa"] / CITED["CT_CDC_1MGL"]["Cryptosporidium"], 5),
        "turbid_double_virus_5c_at_30min": round(sc["turbid_double"]["ct30_epa"] / CITED["CT_VIRUS_4LOG"][5], 2),
    }
    # 4 pH ---------------------------------------------------------------------------------------------------------
    r["pka_hocl"] = {str(tc): round(pka_hocl(tc), 2) for tc in (5, 20, 25)}
    r["hocl_share"] = {str(ph): round(hocl_share(ph), 3) for ph in (6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0)}
    r["hocl_share_5c"] = {str(ph): round(hocl_share(ph, 5.0), 3) for ph in (7.0, 7.5, 8.0, 8.5, 9.0)}
    # informative only: the EPA table already covers pH 6 to 9, so HOCl weighting is not a pass test (it double counts pH)
    r["hocl_ct30_clear"] = {str(ph): round(cl["ct30_epa"] * hocl_share(ph), 2) for ph in (6.0, 7.0, 7.5, 8.0, 8.5, 9.0)}
    # 5 ball timer -------------------------------------------------------------------------------------------------
    to, ti, tl = P["TIMER_TUBE"]
    fall_mm = tl - 2 * 1.5 - P["BALL_D"]
    lam = P["BALL_D"] / ti
    v = fall_mm / 1000.0 / (A["TIMER_TARGET_MIN"] * 60)
    v0_per_mu = 2 / 9 * (A["RHO_BALL"] - A["RHO_FLUID"]) * G * (P["BALL_D"] / 2000.0) ** 2
    wall = haberman_sayre(lam)
    mu = wall * v0_per_mu / v
    re_ = A["RHO_FLUID"] * v * P["BALL_D"] / 1000.0 / mu
    cold = visc_ratio(10.0)
    tn, lo_ = A["TIMER_TARGET_MIN"], 1 - A["VISC_TOL"]
    nominal_needed = 30.0 / (lo_ * visc_ratio(A["TIMER_T_MAX_C"]))
    # run counts: smallest count whose low-tolerance total at the warm end of each band reaches the contact time
    bands = {">18 C": (18.0, 30), "10-18 C": (18.0, 60), "<10 C": (10.0, 120)}
    runs = {k: next(n for n in range(1, 9) if n * tn * lo_ * visc_ratio(tw) >= need) for k, (tw, need) in bands.items()}
    runs[">18 C"] = 1
    vol_ml = math.pi / 4 * ti ** 2 * (tl - 2 * 1.5) / 1000.0
    tmin, tmax = A["TIMER_T_RANGE_C"]
    r["timer"] = dict(fall_mm=fall_mm, lam=round(lam, 3), faxen=round(faxen(lam), 4), wall_haberman_sayre=round(wall, 4),
                      mu_pa_s=round(mu, 1), cst=round(mu / A["RHO_FLUID"] * 1e6, -3), reynolds=re_, t_nominal_min=tn,
                      nominal_needed_min=round(nominal_needed, 1),
                      t_low_min=round(tn * lo_, 1), t_10c_min=round(tn * cold, 1), cold_ratio=round(cold, 2),
                      t_35c_min=round(tn * visc_ratio(35.0), 1), t_40c_low_min=round(tn * lo_ * visc_ratio(40.0), 1),
                      t_briefed_34_40c_low_min=round(34.0 * lo_ * visc_ratio(40.0), 1),
                      runs_needed=runs, runs_total_min={k: round(runs[k] * tn * lo_ * visc_ratio(bands[k][0]), 0) for k in runs},
                      fluid_ml=round(vol_ml, 3),
                      expansion_ul=[round(vol_ml * CITED["PDMS_EXPANSION_PER_K"] * (x - A["TIMER_FILL_C"]) * 1000, 1) for x in (tmin, tmax)],
                      expansion_share=round(CITED["PDMS_EXPANSION_PER_K"] * (tmax - A["TIMER_FILL_C"]), 3))
    # 6 overdose and by-products -----------------------------------------------------------------------------------
    m1, c1 = CITED["TAB"]["1L"]
    m20, c20 = CITED["TAB"]["20L"]
    cya_per_nadcc = MW["CYA"] / MW["NaDCC"]
    r["overdose"] = {
        "wrong_tablet_20L_in_1L_cl": c20, "wrong_tablet_20L_in_1L_nadcc": m20, "wrong_tablet_cya": round(m20 * cya_per_nadcc, 1),
        "two_1L_tabs_cl": 2 * c1, "three_1L_tabs_cl": 3 * c1, "cya_at_4mgl": round(2 * m1 * cya_per_nadcc, 2),
        "tab_1L_d_mm": P["TAB_1L"]["d"], "tab_20L_d_mm": P["TAB_20L"]["d"], "well_1L_mm": P["WELL_1L"], "well_20L_mm": P["WELL_20L"],
        "keyed": P["TAB_20L"]["d"] > P["WELL_1L"] and P["TAB_1L"]["d"] < P["WELL_1L"],
        "wrong_tablet_1L_in_20L_cl": round(c1 / 20.0, 2), "two_1L_in_20L_cl": round(2 * c1 / 20.0, 2),
        "three_fit_if_t_below_mm": {"1L": round(P["FREE_H"]["1L"] / 3, 2), "20L": round(P["FREE_H"]["20L"] / 3, 2)},
        "well_ml": {"1L": round(math.pi / 4 * P["WELL_1L"] ** 2 * P["FREE_H"]["1L"] / 1000, 2),
                    "20L": round(math.pi / 4 * P["WELL_20L"] ** 2 * P["FREE_H"]["20L"] / 1000, 2)},
    }
    r["overdose"]["well_conc_g_l"] = {"1L": round(c1 / r["overdose"]["well_ml"]["1L"], 1),      # mg/mL = g/L
                                      "20L": round(c20 / r["overdose"]["well_ml"]["20L"], 1)}
    # insert O-ring squeeze with tolerances (F10)
    cs, cst_ = P["ORING_CS"]
    tb, tg = P["FIT_TOL"]
    depth = lambda bore, root: (bore - root) / 2
    sq = lambda c_, d_: (c_ - d_) / c_ * 100
    r["oring_squeeze_pct"] = {
        "nominal": round(sq(cs, depth(P["WELL_BORE"], P["INSERT_GROOVE"])), 1),
        "min": round(sq(cs - cst_, depth(P["WELL_BORE"] + tb, P["INSERT_GROOVE"] - tg)), 1),
        "max": round(sq(cs + cst_, depth(P["WELL_BORE"] - tb, P["INSERT_GROOVE"] + tg)), 1),
        "briefed_17_8_print_tol_min": round(sq(cs - cst_, depth(P["WELL_BORE"] + 0.1, 17.8 - 0.1)), 1),
        "stretch_pct": round((P["INSERT_GROOVE"] / 17.2 - 1) * 100, 1)}
    # membrane exposure if the A to C fibres stay soaked in dosed water all year (mg h/L)
    r["membrane_exposure_mg_h_l_year"] = round(sc_c30 * 8760, -2) if (sc_c30 := sc["clear"]["c30"]) else 0
    # 7 D2 liquid strength over shelf life ---------------------------------------------------------------------------
    hl_cool_d = CITED["HYPO_HALF_LIFE_COOL_Y"] * 365
    c0, c1_, days = CITED["HYPO_WARM"]
    k_warm = math.log(c0 / c1_) / days
    r["d2_decay"] = {"cool_3mo_share": round(0.5 ** (91 / hl_cool_d), 3), "warm_3mo_share": round(math.exp(-k_warm * 91), 3),
                     "warm_half_life_days": round(math.log(2) / k_warm, 0),
                     "dose_20L_warm_3mo": round(doses["D2_20L_one_cap"] * math.exp(-k_warm * 91), 2),
                     "dose_20L_warm_6mo": round(doses["D2_20L_one_cap"] * math.exp(-k_warm * 182), 2),
                     "note": "the warm rate is for a 13 % product; dilute 1.25 % decays more slowly, so this is a bound"}
    # 8 D3 erosion feeder --------------------------------------------------------------------------------------------
    t0, t1 = A["STAND_H"]
    lo, hi = 1.0, CITED["WHO_GV"]
    r["d3"] = {"stand_ratio": t1 / t0, "allowed_ratio": hi / lo, "allowed_ratio_target": 4.0 / 2.0,
               "dose_at_24h_if_2mgl_at_30min": round(2.0 * t1 / t0, 1), "dose_at_30min_if_5mgl_at_24h": round(5.0 * t0 / t1, 3)}
    # 9 effort, mass and size --------------------------------------------------------------------------------------
    mass = {}
    for opt in M.OPTIONS:
        ps = [q for q in M.components(opt, context=False) if q["kind"] != "context"]
        mass[opt] = round(sum(M.cp.mass_kg(q) for q in ps) * 1000, 1)
    r["mass_g"] = mass
    cap = [q for q in M.components("D1", context=False)]
    bbs = [q["shape"].bounding_box() for q in cap]
    r["d1_size_mm"] = dict(x=round(max(b.max.X for b in bbs) - min(b.min.X for b in bbs), 1),
                           y=round(max(b.max.Y for b in bbs) - min(b.min.Y for b in bbs), 1),
                           z=round(max(b.max.Z for b in bbs) - min(b.min.Z for b in bbs), 1))
    grip = {"child_10_11_weak": 12.6, "elderly_f_weak": 14.7}   # kg, Camry norms via Topend Sports (as in HWB-CAL-001)
    r["effort"] = {
        "d2_squeeze_kpa_needed": round((P["DOSER_BOTTLE"][1] + P["CHAMBER"][2]) / 1000 * 1000 * G / 1000 + 0.5, 2),
        "d2_squeeze_n_assumed": 10.0, "grip_n": {k: round(v * G, 0) for k, v in grip.items()},
        "cap_close_torque_nm_assumed": 1.0, "plug_turns": round(P["CROWN_TOP"] - P["PLUG_THREAD_Z"], 1) / P["PLUG_PITCH"],
    }
    # 10 cost and cost per litre --------------------------------------------------------------------------------------
    tot = bom_total()
    dev, cons = bom_split()
    scale = sum(A["SCALE_COST_USD"].values())
    life_l_personal = A["L_PER_DAY_PERSONAL"] * 365 * A["LIFE_Y"]
    life_l_house = A["HOUSEHOLD"] * A["L_PER_PERSON_DAY"] * 365 * A["LIFE_Y"]
    tab_h = A["TAB_COST_HUMANITARIAN_USD"]
    r["cost"] = {
        "bom_usd": round(tot, 2), "device_usd": round(dev, 2), "consumables_usd": round(cons, 2), "target_usd": 10.0,
        "scale_device_usd": round(scale, 2),
        "per_litre_1L_tabs_humanitarian": round(tab_h / 1.0 + scale / life_l_personal, 4),
        "per_litre_1L_tabs_retail": round(A["TAB_COST_RETAIL_USD"] + scale / life_l_personal, 4),
        "per_litre_20L_tabs_humanitarian": round(tab_h / 20.0 + scale / life_l_house, 5),
        "per_person_year_1L_tabs_humanitarian": round(tab_h * A["L_PER_DAY_PERSONAL"] * 365 + scale / A["LIFE_Y"], 2),
        "per_household_year_20L_tabs": round(tab_h * A["HOUSEHOLD"] * A["L_PER_PERSON_DAY"] * 365 / 20 + scale / A["LIFE_Y"], 2),
        "tablets_per_household_year_20L": round(A["HOUSEHOLD"] * A["L_PER_PERSON_DAY"] * 365 / 20),
        "life_litres_personal": life_l_personal, "life_litres_household": life_l_house,
        "d2_bottle_usd_e4c": 0.33, "d2_per_litre": round(0.33 / r["d2_bottle_litres_treated"], 5),
    }
    out = ROOT / "docs/04-calcs/sizing_results.json"
    out.write_text(json.dumps(dict(cited=CITED, assumed=A, results=r), indent=1, default=str))
    print(json.dumps(r, indent=1, default=str))


if __name__ == "__main__":
    main()
