"""Helpful Water A filter straw: sizing and first-principles checks (HWA-CAL-001).

Run from the solution folder:  python docs/04-calcs/sizing.py
Writes docs/04-calcs/sizing_results.json and prints every number quoted in 01-sizing.md.

Geometry comes from PARAMS in cad/src/model.py; masses come from the model solids; costs from bom/bom.csv.
Everything here is a paper estimate for a TRL 3 design; nothing is measured. Assumptions are numbered A1 to A12
in 01-sizing.md and marked "assumed" here. Sections follow the CAL note:
  2 geometry   3 membrane permeability cases   4 pressure budget and flow at the persona efforts
  5 carbon bed (empty-bed contact time, mass, pressure drop)   6 seals   7 backflush and air-hold check
  8 options A2 and A3   9 envelope and mass   10 cost and cost per litre   11 results against the requirements
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad/src"), str(ROOT / ".kit")]
import model as M  # noqa: E402

P = M.PARAMS
RHO, G = 998.0, 9.81
MU = {20: 1.002e-3, 5: 1.519e-3, 25: 0.890e-3}   # Pa s, water at 20, 5 and 25 C
LMH_BAR = 1.0 / (1000 * 3600 * 1e5)       # 1 L/(m2 h bar) in m/(s Pa)
ML_MIN = 1e-6 / 60                         # 1 mL/min in m3/s
res = {}

# ---------------------------------------------------------------------------------------------------------
# 2. Geometry
# ---------------------------------------------------------------------------------------------------------
N, dof, dif, La = P["N_FIBRES"], P["FIBRE_OD"] / 1000, P["FIBRE_ID"] / 1000, P["ACTIVE_L"] / 1000
A_mem = N * math.pi * dof * La                       # outer (feed-side) area, outside-in
pack = N * (P["FIBRE_OD"] ** 2) / P["BUNDLE_D"] ** 2
res.update(A_mem=A_mem, packing=pack)
revA = {n: n * math.pi * dof * L for n in (40, 60, 80) for L in (0.090, 0.110)}
res["A_revA_max"] = max(revA.values())
res["A_revA_min"] = min(revA.values())

# ---------------------------------------------------------------------------------------------------------
# 3. Membrane permeability cases. SepraPor datasheet (Meissner, checked 2026-11-11): MF 0.2 um >= 3,300; MF 0.1 um
#    >= 1,800; UF 100 kDa 215 to 550 L/(m2 h bar), normalised to 25 C (independent review, 2026-11-11). Converted
#    here to 20 C by the viscosity ratio 0.890/1.002. Assumed (A1): a straw fibre of 0.8/0.5 mm has the same
#    permeability per outer area as the 1.0 mm lumen datasheet fibres, whose area basis (lumen or outer) the sheet
#    does not state; supplier to confirm (TA, HWA-DEC-001 C3).
# ---------------------------------------------------------------------------------------------------------
LP25 = {"MF 0.2 um": 3300.0, "MF 0.1 um": 1800.0, "UF 100 kDa (high)": 550.0, "UF 100 kDa (low)": 215.0}
LP = {k: v * MU[25] / MU[20] for k, v in LP25.items()}
res["LP25"] = LP25
res["LP"] = {k: round(v, 0) for k, v in LP.items()}


def stages(Q, lp, mu, lift_m=0.155, A=A_mem, n=N, la=La, wet=1.0):
    """Pressure drop of each stage (Pa) at flow Q (m3/s). wet is the wetted share of the active fibre length
    (1 for a primed shell; less when air is trapped in the shell above the outside water level)."""
    d = {}
    d["lift"] = RHO * G * lift_m                                  # A3: mouth 155 mm above the water surface, straw upright
    # intake slots and mesh: orifice losses, 8 slots 2.5 x 7 mm, mesh 17 mm disc 35 % open (A4)
    a_slot = 8 * 2.5e-3 * 7e-3
    a_mesh = math.pi / 4 * 0.017 ** 2 * 0.35
    d["intake"] = 0.5 * RHO * (Q / (0.6 * a_slot)) ** 2 + 0.5 * RHO * (Q / (0.6 * a_mesh)) ** 2
    d["membrane"] = Q / (lp * LMH_BAR * (MU[20] / mu) * A * wet)
    # lumen: Hagen-Poiseuille, one open end, flow rising linearly along the wetted length (factor 1/2), then the full
    # fibre flow through the dry part of the active length and the 10 mm top potting (independent review)
    r_l = 128 * mu * (Q / n) / (math.pi * dif ** 4)
    d["lumen"] = r_l * (0.5 * la * wet + la * (1 - wet) + 0.010)
    # carbon inlet grid: six 2.0 mm and one 2.5 mm holes, 2 mm long (laminar plus orifice)
    holes = [2.0e-3] * 6 + [2.5e-3]
    a_g = sum(math.pi / 4 * h ** 2 for h in holes)
    d["grids"] = 2 * (0.5 * RHO * (Q / (0.6 * a_g)) ** 2)              # inlet grid and mouthpiece grid (similar)
    # inlet screen 150 um, 16 mm, 30 % open
    a_s = math.pi / 4 * 0.016 ** 2 * 0.30
    d["screen"] = 0.5 * RHO * (Q / (0.6 * a_s)) ** 2
    # carbon bed: Ergun, dp 0.84 mm (12 x 40 geometric mean), sphericity 0.75, voidage 0.42 (A5)
    dp, phi, eps, Lb = 0.84e-3, 0.75, 0.42, P["BED_H"] / 1000
    A_b = math.pi / 4 * (P["BED_D"] / 1000) ** 2
    u = Q / A_b
    de = phi * dp
    d["carbon"] = Lb * (150 * mu * (1 - eps) ** 2 * u / (eps ** 3 * de ** 2) + 1.75 * RHO * (1 - eps) * u ** 2 / (eps ** 3 * de))
    # fines pad: Darcy, k = 3e-11 m2 assumed (A6), 1.6 mm
    d["pad"] = mu * u * 1.6e-3 / 3e-11
    # mouthpiece bore 5 mm x 15 mm and exit velocity head
    db = P["MOUTH_BORE"] / 1000
    d["mouth"] = 128 * mu * 0.015 * Q / (math.pi * db ** 4) + 0.5 * RHO * (Q / (math.pi / 4 * db ** 2)) ** 2
    return d


def flow_at(S_pa, lp, mu=MU[20], **kw):
    """Flow (mL/min) at a user suction S (Pa), by bisection on the stage sum."""
    if sum(stages(0.0, lp, mu, **kw).values()) >= S_pa:
        return 0.0
    lo, hi = 0.0, 5000 * ML_MIN
    for _ in range(80):
        mid = (lo + hi) / 2
        if sum(stages(mid, lp, mu, **kw).values()) > S_pa:
            hi = mid
        else:
            lo = mid
    return lo / ML_MIN


# Persona suction (assumed, A2): child 5 kPa, elderly 7 kPa, Rev A test point 10 kPa, adult 15 kPa sustained sip.
# STANDARDS 25.6 gives 5 to 15 kPa for user suction; adults reach about 30 to 40 kPa at maximum effort against an
# oral screen (Wertsen and Stenberg 2017), far above a comfortable sip.
PERSONAS = {"child": 5000.0, "elderly": 7000.0, "revA": 10000.0, "adult": 15000.0}
res["flow"] = {k: {p: round(flow_at(s, lp), 1) for p, s in PERSONAS.items()} for k, lp in LP.items()}
res["flow_cold"] = {k: {p: round(flow_at(s, lp, MU[5]), 1) for p, s in PERSONAS.items()} for k, lp in LP.items()}
res["flow_tilted"] = {k: round(flow_at(PERSONAS["child"], lp, lift_m=0.05), 1) for k, lp in LP.items()}
# Immersion and priming (independent review M2). The dirty shell is closed at the top by the potting and wetted fibres
# do not pass air (bubble point hundreds of kPa), so air trapped in the shell stays above the outside water level and
# only the fibre length below it filters. Dipped to the 110 mm dip line: lift 95 mm; primed (shell full) or not.
Z_ACT = (P["Z_BOT_POT"][1], P["Z_TOP_POT"][0])
wet_dip = (P["Z_DIP_LINE"] - Z_ACT[0]) / (Z_ACT[1] - Z_ACT[0])
lift_dip = (P["L"] - P["Z_DIP_LINE"]) / 1000
res["wet_dip"] = wet_dip
res["wet_shallow"] = (50.0 - Z_ACT[0]) / (Z_ACT[1] - Z_ACT[0])      # water surface at z = 50 mm (155 mm lift)
res["flow_dip_primed"] = {k: {p: round(flow_at(s, LP[k], lift_m=lift_dip), 1) for p, s in PERSONAS.items()}
                          for k in ("MF 0.2 um", "MF 0.1 um")}
res["flow_dip_unprimed"] = {k: {p: round(flow_at(s, LP[k], lift_m=lift_dip, wet=wet_dip), 1) for p, s in PERSONAS.items()}
                            for k in ("MF 0.2 um", "MF 0.1 um")}
res["flow_shallow_unprimed"] = {k: round(flow_at(10000, LP[k], wet=res["wet_shallow"]), 1) for k in ("MF 0.2 um", "MF 0.1 um")}
# Permeability needed for 200 mL/min at 10 kPa (upright, 155 mm lift) and at the dip line, primed
def _lp_needed(lift_m):
    other = sum(v for k, v in stages(200 * ML_MIN, 1e9, MU[20], lift_m=lift_m).items() if k != "membrane")
    return 200 * ML_MIN / (A_mem * (10000 - other)) / LMH_BAR
res["LP_needed_200"] = {"upright 155 mm lift": round(_lp_needed(0.155), 0), "dip line": round(_lp_needed(lift_dip), 0)}
# Persona effort (independent review M8): minutes of sipping for 1.5 L, primed, upright
res["minutes_1p5L"] = {k: {p: round(1500 / max(F, 1e-6), 0) for p, F in v.items()} for k, v in
                       {k: {p: flow_at(s, LP[k]) for p, s in PERSONAS.items()} for k in ("MF 0.2 um", "MF 0.1 um")}.items()}
res["minutes_1p5L_child_cold"] = {k: round(1500 / flow_at(PERSONAS["child"], LP[k], MU[5]), 0) for k in ("MF 0.2 um", "MF 0.1 um")}
# Fouling on turbid water (independent review M1): cake filtration, R = R_m + alpha m / A; 50 mg/L suspended solids,
# specific cake resistance 1e13 to 1e14 m/kg (assumed A13, to measure in TE); 10 kPa, upright, primed, before backflush.
def _flow_fouled(lp, litres, alpha, tss=0.050):
    rm = 1 / (lp * LMH_BAR * MU[20])
    rc = alpha * tss * litres / 1000 / A_mem            # tss in kg/m3, litres in L
    return flow_at(10000, lp * rm / (rm + rc))
res["flux_design_LMH"] = 200 * 60 / 1000 / A_mem
res["flow_fouled"] = {k: {f"{a:.0e}": {str(v): round(_flow_fouled(LP[k], v, a), 0) for v in (1, 5, 20)} for a in (1e13, 1e14)}
                      for k in ("MF 0.2 um", "MF 0.1 um")}
# Rev A geometry (80 fibres x 110 mm) at 10 kPa, 0.1 um MF
res["flow_revA80"] = round(flow_at(10000, LP["MF 0.1 um"], A=80 * math.pi * dof * 0.110, n=80, la=0.110), 1)
res["flow_revA40"] = round(flow_at(10000, LP["MF 0.1 um"], A=40 * math.pi * dof * 0.090, n=40, la=0.090), 1)
res["flow_revA80_02"] = round(flow_at(10000, LP["MF 0.2 um"], A=80 * math.pi * dof * 0.110, n=80, la=0.110), 1)
# longer active length if the body grows to 245 mm (UR-012 allows under 250 mm): 145 mm active (HWA-DEC-001 D3)
A_long = N * math.pi * dof * 0.145
res["A_long"] = A_long
res["flow_long"] = {k: {p: round(flow_at(s, lp, A=A_long, la=0.145, lift_m=0.195), 1) for p, s in PERSONAS.items()}
                    for k, lp in LP.items() if k.startswith("MF")}
# suction needed for 200 and 400 mL/min
def suction_for(q_mlmin, lp, mu=MU[20]):
    return sum(stages(q_mlmin * ML_MIN, lp, mu).values())
res["S200"] = {k: round(suction_for(200, lp) / 1000, 2) for k, lp in LP.items()}
res["S400"] = {k: round(suction_for(400, lp) / 1000, 2) for k, lp in LP.items()}
res["budget200_mf01"] = {k: round(v / 1000, 3) for k, v in stages(200 * ML_MIN, LP["MF 0.1 um"], MU[20]).items()}
res["budget200_mf02"] = {k: round(v / 1000, 3) for k, v in stages(200 * ML_MIN, LP["MF 0.2 um"], MU[20]).items()}
def _carbon(dp, eps, q=200 * ML_MIN, phi=0.75):
    u = q / (math.pi / 4 * (P["BED_D"] / 1000) ** 2); de = phi * dp; mu = MU[20]
    return P["BED_H"] / 1000 * (150 * mu * (1 - eps) ** 2 * u / (eps ** 3 * de ** 2) + 1.75 * RHO * (1 - eps) * u ** 2 / (eps ** 3 * de))
res["carbon_range_kPa"] = (round(_carbon(0.84e-3, 0.45) / 1000, 2), round(_carbon(0.6e-3, 0.38) / 1000, 2))
res["sip_child_s"] = round(200 / max(res["flow"]["MF 0.1 um"]["child"], 1e-6) * 60, 0)

# ---------------------------------------------------------------------------------------------------------
# 5. Carbon bed
# ---------------------------------------------------------------------------------------------------------
V_bed = math.pi / 4 * P["BED_D"] ** 2 * P["BED_H"] / 1000          # mL
res["V_bed_mL"] = V_bed
res["m_bed_g"] = (V_bed * 0.48, V_bed * 0.50)
res["EBCT_s"] = {q: round(V_bed / q * 60, 2) for q in (100, 200, 400)}

# ---------------------------------------------------------------------------------------------------------
# 6. Seals: AS568-018 in a male gland, floor 19.3 mm, bore 22.0 mm
# ---------------------------------------------------------------------------------------------------------
cs, idr, floor, bore, w = P["ORING_CS"], P["ORING_ID"], P["GLAND_FLOOR_D"], P["ID"], P["GLAND_W"]
depth = (bore - floor) / 2
res["gland"] = dict(depth=depth, squeeze=(cs - depth) / cs, stretch=floor / idr - 1,
                    fill=(math.pi / 4 * cs ** 2) / (depth * w), extrusion_gap=(bore - P["SPIGOT_OD"]) / 2)
# tolerance stack (independent review): cross-section 1.78 +- 0.08 mm; depth +- 0.10 mm as printed, +- 0.05 mm reamed
res["squeeze_range_printed"] = ((cs - 0.08 - (depth + 0.10)) / (cs - 0.08), (cs + 0.08 - (depth - 0.10)) / (cs + 0.08))
res["squeeze_range_reamed"] = ((cs - 0.08 - (depth + 0.05)) / (cs - 0.08), (cs + 0.08 - (depth - 0.05)) / (cs + 0.08))
res["revA_ring_od"] = 20 + 2 * 2      # 20 x 2 mm ring: outside diameter 24 mm, against a 22 mm bore

# ---------------------------------------------------------------------------------------------------------
# 7. Backflush and the air-hold integrity check (20 mL syringe, plunger bore about 20 mm, assumed A8)
# ---------------------------------------------------------------------------------------------------------
gamma = 0.072
res["laplace_broken_kPa"] = 4 * gamma / dif / 1000                   # an open, broken fibre lets air through at this
res["laplace_02um_kPa"] = 4 * gamma / 0.4e-6 / 1000                  # ideal for a 0.4 um largest pore (upper bound)
v0, v1 = 20.0, 13.3
res["air_hold_kPa"] = (v0 / v1 - 1) * 101.325                        # isothermal compression of 20 mL of air to 13.3 mL
# the water in the lumens and header must leave through the walls before air reaches them (independent review), so
# the plunger reaches 51 kPa only at the 13.3 mL gas volume less the lumen and header volume
V_lumen = N * math.pi / 4 * P["FIBRE_ID"] ** 2 * (P["ACTIVE_L"] + 10) / 1000
V_header = math.pi / 4 * P["ID"] ** 2 * (P["Z_HEADER"][1] - P["Z_HEADER"][0]) / 1000
res["V_lumen_mL"], res["V_header_mL"] = V_lumen, V_header
res["air_hold_mark_mL"] = v1 - V_lumen - V_header
res["air_hold_min_defect_um"] = 4 * gamma / (res["air_hold_kPa"] * 1000) * 1e6   # smallest defect the check opens
res["thumb_overpressure_kPa"] = 60.0 / (math.pi / 4 * 0.020 ** 2) / 1000         # a firm 60 N push (assumed)
res["thumb_N"] = res["air_hold_kPa"] * 1000 * math.pi / 4 * 0.020 ** 2
bf_kpa = 50.0
def _backflush(lp, p=bf_kpa * 1000):
    """Membrane in reverse plus the luer tip and 2 mm socket passage, 1.5 velocity heads each (independent review)."""
    a = math.pi / 4 * (P["PORT_PASS_D"] / 1000) ** 2
    lo, hi = 0.0, 1e-4
    for _ in range(80):
        q = (lo + hi) / 2
        dp = q / (lp * LMH_BAR * A_mem) + 2 * 1.5 * 0.5 * RHO * (q / a) ** 2
        lo, hi = (q, hi) if dp < p else (lo, q)
    return lo / ML_MIN
res["backflush_mLmin_50kPa"] = {k: round(_backflush(LP[k]), 0) for k in ("MF 0.2 um", "MF 0.1 um")}
res["backflush_s_20mL"] = {k: round(20 / v * 60, 1) for k, v in res["backflush_mLmin_50kPa"].items()}
# open backflush socket submerged (plug out, dipped past the dip line): orifice flow at 10 kPa (independent review M4)
res["socket_bypass_mLmin"] = 0.6 * math.pi / 4 * (P["PORT_PASS_D"] / 1000) ** 2 * math.sqrt(2 * 10000 / RHO) / ML_MIN

# ---------------------------------------------------------------------------------------------------------
# 8. Options A2 and A3
# ---------------------------------------------------------------------------------------------------------
# A2 ceramic: permeability from ceramic pot filters (Akvopedia: 1 to 3 L/h from a pot about 30 cm across and 25 cm
# deep); assumed (A9) wetted area 0.31 m2, mean head 0.12 m, wall 15 mm, so k = Lp mu t.
A_pot = math.pi * 0.15 ** 2 + 2 * math.pi * 0.15 * 0.25
Lp_pot = (2.0 / 1000 / 3600) / (A_pot * RHO * G * 0.12)              # m/(s Pa)
k_cer = Lp_pot * MU[20] * 0.015
ro, ri, Lc = P["CER_OD"] / 2000, P["CER_ID"] / 2000, (P["Z_CER"][1] - P["Z_CER"][0] - 12) / 1000
tmp = 10000 - RHO * G * 0.155 - 1500                                  # Rev A suction less lift and carbon (about 1.5 kPa)
q_cer = 2 * math.pi * k_cer * Lc * tmp / (MU[20] * math.log(ro / ri))
res["A2_flow_mLmin"] = q_cer / ML_MIN
# best case: thin 0.2 um alumina membrane layer at 1,500 L/(m2 h bar) on the 17 mm tube (A10)
res["A2_flow_best_mLmin"] = 1500 * LMH_BAR * (math.pi * 2 * ro * Lc) * tmp / ML_MIN
res["Lp_pot_LMHbar"] = Lp_pot / LMH_BAR
# A3 copper: void volume of the copper roll (about 75 % open) over the flow; copper pots need hours
V_cu = math.pi / 4 * P["ID"] ** 2 * (P["Z_CU"][1] - P["Z_CU"][0]) / 1000 * 0.75
res["A3_contact_s"] = V_cu / 200 * 60
res["A3_needed_s"] = 16 * 3600                                       # 16 h storage in a copper pot (Sudha et al. 2012)

# ---------------------------------------------------------------------------------------------------------
# 9. Envelope and mass from the model
# ---------------------------------------------------------------------------------------------------------
import cad_parts as cp  # noqa: E402
parts = [q for q in M.components("A1") if q["kind"] != "context"]
body = [q for q in parts if q["name"] not in ("Lanyard cord", "Split ring, stainless 12 mm", "Intake cover", "Mouthpiece cap")]
bb = None
for q in body:
    b = q["shape"].bounding_box()
    bb = b if bb is None else bb.add(b)
res["length_mm"] = bb.max.Z - bb.min.Z
res["width_mm"] = max(bb.max.X - bb.min.X, bb.max.Y - bb.min.Y)
res["across_port_mm"] = bb.max.X - bb.min.X
res["mass_g"] = sum(cp.mass_kg(q) for q in parts) * 1000
res["mass_dry_body_g"] = sum(cp.mass_kg(q) for q in body) * 1000
wet = math.pi / 4 * P["ID"] ** 2 * 126 / 1000 * 0.75 + V_bed * 0.6 + 2
res["water_held_mL"] = wet          # dirty bay and fibres, carbon pores, header (estimate)
res["mass_full_g"] = res["mass_g"] + wet

# ---------------------------------------------------------------------------------------------------------
# 10. Cost and cost per litre
# ---------------------------------------------------------------------------------------------------------
rows = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
tot = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
refill_items = ("7 ", "8 ", "9 ", "10 ")
refill = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows if r["item"].startswith(refill_items)) + 0.25
res["bom_total"] = tot
res["refill"] = refill
LIFE_MEM, LIFE_C = 2000.0, 500.0    # assumed (A11, A12)
n_refill = LIFE_MEM / LIFE_C - 1
res["cpl_proto"] = (tot + n_refill * refill) / LIFE_MEM
res["cpl_mass"] = (3.0 + n_refill * 0.15) / LIFE_MEM                 # USD 3 unit (mid of USD 1 to 5), USD 0.15 refill (assumed)
res["cpl_tablets"] = 0.02

if __name__ == "__main__":
    (ROOT / "docs/04-calcs/sizing_results.json").write_text(json.dumps(res, indent=1, default=float))
    for k, v in res.items():
        print(k, "=", v)
    print("wrote docs/04-calcs/sizing_results.json")
