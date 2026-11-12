"""Helpful Water A filter straw: STEM check calculations (HWA-STM-001, STANDARDS sections 20 and 25.6).

Run from the solution folder:  python docs/04-calcs/sizing.py      (writes sizing_results.json)
                               python docs/04-calcs/stem_check.py  (writes stem_results.csv, stem_results_dropped.csv
                                                                    and refreshes the two tables in docs/01b-stem-check.md)
Rows S1 to S32 check the recommended option A1 after the fixes made under Amish's standing instruction of 2026-10-23
(HWA-DEC-001 F1 to F11; F6 to F11 follow the independent review of 2026-11-11; S27 to S32 are claims it found missing). Rows X1 to X6 check the dropped options A2 (ceramic tube) and A3 (copper and charcoal); they sit
in their own table and file so the verdict of the carried design is not mixed with theirs.
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad/src")]
from stem_check import Check, WITHIN, PLAUSIBLE, FIX, FAILS  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
R = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
CAL = "HWA-CAL-001"
c = Check(ROOT / "docs/04-calcs/stem_results.csv")
F = R["flow"]
F2, F1 = F["MF 0.2 um"], F["MF 0.1 um"]
DP, DU = R["flow_dip_primed"], R["flow_dip_unprimed"]
REV = "independent review 2026-11-11"

# --- Physics: fluid mechanics (hydraulics, STANDARDS 25.6) ---------------------------------------------------------
# Permeabilities are the SepraPor minima normalised to 25 C, converted to 20 C (x 0.888): 0.2 um 2,930; 0.1 um 1,600.
c.cited("S1", f"Rev A's 40 to 80 fibres ({R['A_revA_min']:.3f} to {R['A_revA_max']:.3f} m2) cannot give 200 mL/min at 10 kPa with any listed "
        f"grade; filling the bore with about {P['N_FIBRES']} fibres raises the area {R['A_mem'] / R['A_revA_max']:.1f} times",
        "Physics", "Fluid mechanics", "Darcy flux J = Lp x TMP over the outer fibre area; SepraPor minima at 25 C converted to 20 C",
        f"80 fibres x 110 mm: {R['flow_revA80']:.0f} mL/min (0.1 um) to {R['flow_revA80_02']:.0f} mL/min (0.2 um); 40 x 90 mm: "
        f"{R['flow_revA40']:.0f} mL/min. Fixed by a full-bore bundle ({R['A_mem']:.3f} m2, packing {R['packing']:.0%}, no central tube); the "
        "fix is necessary, not sufficient: the flow target then rests on the grade (S2, S3)", WITHIN, closed_by="HWA-DEC-001 F2; " + CAL + " section 4")
c.cited("S2", "Full-bore bundle with a 0.2 um MF fibre gives at least the 150 mL/min of PR-002 (HWA-DEC-001 D3) at 10 kPa, clean water, 20 C, straw upright",
        "Physics", "Fluid mechanics", "Stage sum: lift, intake, membrane, lumen and potting (Hagen-Poiseuille), grids, carbon (Ergun), pad (Darcy), mouth",
        f"{F2['revA']:.0f} mL/min at 10 kPa; 200 mL/min needs {R['S200']['MF 0.2 um']:.1f} kPa, or Lp {R['LP_needed_200']['upright 155 mm lift']:,.0f} "
        f"L/(m2 h bar) at 20 C, above the grade's listed minimum (2,930). Dipped to the dip line and primed: {DP['MF 0.2 um']['revA']:.0f}; "
        f"245 mm body: {R['flow_long']['MF 0.2 um']['revA']:.0f}. Against the decided 150 mL/min upper-bound target the 0.2 um grade has about 19 % margin; "
        f"uncertainties (pad, carbon, area basis) run mostly downward ({REV}), so TC confirms it",
        WITHIN, closed_by="Fix: target set to 150 mL/min, HWA-DEC-001 D3 (Amish, 2026-11-11); test TC at TRL 4")
c.cited("S3", "The 0.1 um MF fibre gives less than the 150 mL/min target and is used only if the 0.2 um grade fails the retention criteria of HWA-DEC-001 D2",
        "Physics", "Fluid mechanics", "Same stage sum", f"{F1['revA']:.0f} mL/min at 10 kPa; 200 mL/min needs {R['S200']['MF 0.1 um']:.1f} kPa. "
        "The shortfall is accepted only as the safety trade-off D2 defines (thin bacteria); the 245 mm body is the TRL 4 revision if trials need it", WITHIN,
        closed_by="Fix: grade selection rule HWA-DEC-001 D2 and target D3 (Amish, 2026-11-11)")
c.cited("S4", "A true ultrafiltration fibre (100 kDa) cannot give usable flow at suction in this envelope, so the membrane must be a microfiltration grade",
        "Physics", "Fluid mechanics", "SepraPor UF 100 kDa 215 to 550 L/(m2 h bar) at 25 C",
        f"{F['UF 100 kDa (low)']['revA']:.0f} to {F['UF 100 kDa (high)']['revA']:.0f} mL/min at 10 kPa. Fixed: PR-004 floor 1,800 L/(m2 h bar) "
        f"at 25 C (1,600 at 20 C), the floor for usable flow ({F1['revA']:.0f} mL/min); PR-002 itself needs "
        f"{R['LP_needed_200']['upright 155 mm lift']:,.0f} at 20 C, which no listed grade guarantees (S2)", WITHIN, closed_by="HWA-DEC-001 F3")
c.cited("S5", "The 400 mL/min that straw users want is not reachable at a comfortable 10 kPa sip, so it is not a requirement; PR-002 states 150 mL/min as an upper bound",
        "Physics", "Fluid mechanics", "Stage sum; 400 mL/min threshold from the concept validation questions",
        f"{F1['revA']:.0f} to {F2['revA']:.0f} mL/min, under half; 400 mL/min needs {R['S400']['MF 0.2 um']:.0f} to {R['S400']['MF 0.1 um']:.0f} kPa. "
        "Not reachable in this envelope; stated to users as a known limit", WITHIN, closed_by="Fix: HWA-DEC-001 D3 (Amish, 2026-11-11)")
c.cited("S6", f"A child at 5 kPa draws {F1['child']:.0f} to {F2['child']:.0f} mL/min and an elderly user at 7 kPa {F1['elderly']:.0f} to "
        f"{F2['elderly']:.0f} mL/min; 1.5 L takes a child {R['minutes_1p5L']['MF 0.2 um']['child']:.0f} to {R['minutes_1p5L']['MF 0.1 um']['child']:.0f} min of sipping",
        "Biology", "Human physiology and biomechanics", "Persona suction assumed 5 and 7 kPa (STANDARDS 25.6 range 5 to 15 kPa); sustained sip suction "
        "of children and older adults is to assess (Wertsen and Stenberg 2017 measured adult lip force only)",
        f"Stage sum; at 5 C the child needs {R['minutes_1p5L_child_cold']['MF 0.2 um']:.0f} to {R['minutes_1p5L_child_cold']['MF 0.1 um']:.0f} min "
        f"per 1.5 L; tilting to 50 mm lift gives {R['flow_tilted']['MF 0.1 um']:.0f} to {R['flow_tilted']['MF 0.2 um']:.0f} mL/min; fatigue and lip seal "
        "on the 10 mm tip to test (TH)", PLAUSIBLE, closed_by="")
b = R["budget200_mf02"]
c.order_of_magnitude("S7", "At 200 mL/min the carbon bed costs about 1 kPa of suction", "Physics", "Fluid mechanics", claimed=1.0,
                     estimate=b["carbon"], unit="kPa", law=f"Ergun, 12 x 40 GAC, sphericity 0.75, voidage 0.42 (assumed); range "
                     f"{R['carbon_range_kPa'][0]:.1f} to {R['carbon_range_kPa'][1]:.1f} kPa for 0.6 to 0.84 mm and voidage 0.38 to 0.45",
                     closed_by=f"{CAL} section 4 (membrane {b['membrane']:.1f}, lift {b['lift']:.1f}, pad {b['pad']:.1f}, lumen {b['lumen']:.1f} kPa)")
c.claim("S8", "Lumen and potting pressure drop is small beside the membrane (single open end, 0.5 mm lumen, 102 mm active, 10 mm potting)",
        "Physics", "Fluid mechanics", "Hagen-Poiseuille with flow rising along the fibre, full flow through the potting", b["lumen"], 1.0, "kPa",
        closed_by=f"{CAL} section 4")
c.claim("S9", "Upright with a shallow dip (water surface at 50 mm) the 155 mm lift to the mouth costs 1.5 kPa; at the dip line 0.9 kPa",
        "Physics", "Fluid mechanics", "Hydrostatics rho g h; the flow cases assume a primed shell (S28)", round(b["lift"], 2), 1.6, "kPa",
        closed_by=f"{CAL} section 4")
c.order_of_magnitude("S10", "Water at 5 C flows about a third slower than at 20 C", "Physics", "Fluid mechanics", claimed=0.66,
                     estimate=R["flow_cold"]["MF 0.2 um"]["revA"] / F2["revA"], unit="ratio",
                     law="Viscosity 1.52 against 1.00 mPa s; flux falls as 1/viscosity, lift does not", closed_by=f"{CAL} section 4")
# --- Biology: microbiology (separation) ---------------------------------------------------------------------------
c.cited("S11", "A microfiltration fibre with a supplier-validated absolute rating is designed to retain most bacteria and protozoan cysts; "
        "removal is claimed only from laboratory log reductions, and thin bacteria such as Leptospira are not claimed",
        "Biology", "Microbiology", "Size exclusion; STANDARDS 25.6 organism sizes; bacterial retention challenge with Brevundimonas diminuta "
        "(0.3 to 0.4 um, ASTM F838 method); Leptospira about 0.1 um across passes 0.2 um membranes (Standard Methods 9260 I)",
        "Most bacteria 0.5 to 5 um, cysts 3 to 15 um; but the smallest relevant bacteria are 0.1 to 0.4 um, below a 0.2 um nominal label. "
        "Fixed: PR-001 asks for an absolute rating with a B. diminuta challenge report; Leptospira added to the exclusions unless tested (TA, TB)",
        WITHIN, closed_by="HWA-DEC-001 F10; PR-001, PR-006")
c.cited("S12", "Viruses (0.02 to 0.3 um) are not reliably retained, so no virus claim is made and the product says so",
        "Biology", "Microbiology", "Size exclusion; HWP-CLM-001", "Enteric viruses 0.027 to 0.09 um, below the 0.1 to 0.2 um rating", WITHIN,
        closed_by="HWP-CLM-001; PR-008")
c.cited("S13", "The 250 um mesh stops grit and debris only, not silt, microbes or chemicals", "Physics", "Fluid mechanics",
        "Sieving; Rev A item 2", "Silt 2 to 63 um and clay under 2 um pass a 250 um aperture; the membrane is the fouling point (S27)", WITHIN,
        closed_by="PR-013")
c.cited("S27", "Clean-water flows are upper bounds: turbid water builds a cake on the fibres and the flow falls between backflushes",
        "Physics", "Fluid mechanics", f"Cake filtration R = Rm + alpha m / A; design flux {R['flux_design_LMH']:.0f} L/(m2 h) against tens of L/(m2 h) "
        "sustained in surface-water plants; 50 mg/L solids, alpha 1e13 to 1e14 m/kg (assumed A13)",
        f"0.2 um at 10 kPa after 1, 5 and 20 L: {R['flow_fouled']['MF 0.2 um']['1e+13']['1']:.0f}, {R['flow_fouled']['MF 0.2 um']['1e+13']['5']:.0f}, "
        f"{R['flow_fouled']['MF 0.2 um']['1e+13']['20']:.0f} to {R['flow_fouled']['MF 0.2 um']['1e+14']['1']:.0f}, {R['flow_fouled']['MF 0.2 um']['1e+14']['5']:.0f}, "
        f"{R['flow_fouled']['MF 0.2 um']['1e+14']['20']:.0f} mL/min. Settle or cloth-strain cloudy water; backflush interval in litres from TE",
        PLAUSIBLE, closed_by="")
c.cited("S28", "Once primed, the dirty shell stays full of water while the intake is under water; air trapped in it cuts the working membrane area",
        "Physics", "Fluid mechanics", "The shell is closed at the top by the potting and wetted fibres hold air to their bubble point, so trapped air "
        "sits above the outside water level (hydrostatics; Young-Laplace)",
        f"At the dip line, primed {DP['MF 0.1 um']['revA']:.0f} to {DP['MF 0.2 um']['revA']:.0f} mL/min; with the shell drained above the outside level "
        f"({R['wet_dip']:.0%} wetted) {DU['MF 0.1 um']['revA']:.0f} to {DU['MF 0.2 um']['revA']:.0f}; shallow dip unprimed "
        f"{R['flow_shallow_unprimed']['MF 0.1 um']:.0f} to {R['flow_shallow_unprimed']['MF 0.2 um']:.0f}. Dry fibres prime on first use; between uses the "
        "intake cover keeps the shell full; a re-prime method or vent to test (TC, D10). Degassing under suction may add bubbles", PLAUSIBLE, closed_by="")
# --- Chemistry: adsorption --------------------------------------------------------------------------------------
c.order_of_magnitude("S14", "The 16 x 20 mm carbon bed holds about 2 g, not 5 g", "Chemistry", "Physical chemistry", claimed=2.0,
                     estimate=R["m_bed_g"][0], unit="g", law="Bed volume 4.0 mL x apparent density 0.48 to 0.50 g/mL (12 x 40 coconut GAC sheet)",
                     closed_by=f"{CAL} section 5")
c.cited("S15", f"With an empty-bed contact time of {R['EBCT_s']['200']:.1f} s at 200 mL/min the carbon is intended to reduce free chlorine taste only",
        "Chemistry", "Physical chemistry", "Chlorine reduction on GAC is fast; straws with a few grams of carbon are sold as NSF/ANSI 42 for chlorine "
        "(retailer listing, not verified against the NSF database); organics and odours need minutes",
        "EBCT 0.6 to 2.4 s across 100 to 400 mL/min at about 60 m/h superficial velocity through a 20 mm bed, fast and shallow even for dechlorination; "
        "claim limited to chlorine taste, measured under NSF/ANSI 42 before any claim", PLAUSIBLE, closed_by="")
c.cited("S16", "Carbon life is set by a measured breakthrough curve, not assumed", "Chemistry", "Analytical chemistry",
        "Rev A section 07 (carbon life)", "Replacement interval to be set from HWP-VER-001 TG; 500 L is a planning assumption only", WITHIN, closed_by="PR-015")
c.cited("S31", "The straw does no disinfection; with a chlorine co-treatment the contact time is completed in the container before sipping, and the carbon "
        "then removes the residual", "Chemistry", "Physical chemistry", "Free chlorine passes MF membranes; GAC removes it in about a second (S15); CT "
        "needs minutes (HWP-CLM-001)", f"EBCT {R['EBCT_s']['200']:.1f} s against a contact time of 30 min; instruction: dose, wait, then drink through the "
        "straw; the membrane's free-chlorine tolerance (ppm h) to confirm (C2)", WITHIN, closed_by="HWP-CLM-001; HWA-DEC-001 F11")
# --- Engineering: seals and tolerances --------------------------------------------------------------------------
g = R["gland"]
sp, sr = R["squeeze_range_printed"], R["squeeze_range_reamed"]
c.cited("S17", "AS568-018 O-rings (18.77 x 1.78 mm) in male glands with a 19.3 mm floor seal a 22.0 mm bore",
        "Engineering and technology", "Manufacturing tolerances", "Static radial gland practice: squeeze 15 to 30 %, stretch under 5 %, fill under 85 %",
        f"Nominal squeeze {g['squeeze']:.0%}, stretch {g['stretch']:.1%}, fill {g['fill']:.0%}, radial gap {g['extrusion_gap']:.2f} mm. Tolerance stack "
        f"as printed (+-0.1 mm) {sp[0]:.0%} to {sp[1]:.0%}, outside the range; fixed: bores and gland floors reamed or turned to +-0.05 mm, "
        f"{sr[0]:.0%} to {sr[1]:.0%}. The Rev A 20 x 2 mm ring (outside {R['revA_ring_od']} mm) cannot enter a 22 mm bore", WITHIN,
        closed_by="HWA-DEC-001 F1, F9")
c.cited("S18", "Backflush water enters the clean header and leaves through the fibre walls and the intake without passing the carbon",
        "Physics", "Fluid mechanics", "Continuity: with the mouthpiece cap plugging the 5 mm bore the carbon branch is dead-ended",
        "Socket on the header at 153 mm, below the carbon cartridge; the cap plug must be fitted first (instruction and pictogram); with the cap "
        "off the flush runs out of the mouthpiece instead and the fibres are not cleaned", WITHIN, closed_by="HWA-DEC-001 F4")
bf = R["backflush_mLmin_50kPa"]
c.cited("S19", f"A 20 mL syringe at 50 kPa backflushes at about {bf['MF 0.1 um']:.0f} to {bf['MF 0.2 um']:.0f} mL/min with a {R['thumb_N']:.0f} N thumb force",
        "Physics", "Fluid mechanics", "Membrane resistance in reverse plus the luer tip and 2 mm passage (1.5 velocity heads each); force = pressure x "
        "plunger area (20 mm bore, assumed)", f"20 mL in about {R['backflush_s_20mL']['MF 0.2 um']:.1f} to {R['backflush_s_20mL']['MF 0.1 um']:.1f} s; "
        "20 mL is about 0.35 L/m2, so the number of strokes is set in TE; the syringe is filled with water already treated, never from the source (F11)",
        PLAUSIBLE, closed_by="")
c.cited("S30", "A firm push on the syringe stays within the membrane's reverse-pressure rating",
        "Physics", "Fluid mechanics", "Pressure = force / plunger area; SepraPor lists a maximum TMP of 1.0 bar (0.2 um) and 1.4 bar (0.1 um) and gives no "
        "backflush rating", f"60 N on a 20 mm plunger gives {R['thumb_overpressure_kPa']:.0f} kPa static, about twice the 0.2 um rating; the module's reverse "
        "rating is to confirm (C2) and a pressure limit is set by D11", PLAUSIBLE, closed_by="")
# --- Integrity and silent failure -------------------------------------------------------------------------------
c.cited("S20", "A plunger-hold air check through the backflush socket shows a broken fibre or a failed collar seal (gross defects only)",
        "Physics", "Fluid mechanics", "Young-Laplace: a wetted 0.2 um pore holds air to hundreds of kPa; an open 0.5 mm lumen passes air above 0.6 kPa; "
        "isothermal compression of the syringe, header and lumen gas", f"The water in the lumens ({R['V_lumen_mL']:.1f} mL) and header ({R['V_header_mL']:.1f} mL) "
        f"leaves first, so {R['air_hold_kPa']:.0f} kPa is reached at the {R['air_hold_mark_mL']:.0f} mL mark (fix F7, not 13.3 mL); it opens defects of "
        f"{R['air_hold_min_defect_um']:.1f} um and larger, not bacterial-size ones; pass is a plunger that holds; bubbles show only inverted; "
        "dry spots give a false fail; re-prime after (TA, TF)", PLAUSIBLE, closed_by="")
c.cited("S29", "With the socket plug out and the socket under water, dirty water bypasses the membrane at more than the filtered flow, and the user cannot tell",
        "Physics", "Fluid mechanics", "Orifice flow through the 2 mm socket passage at 10 kPa", f"About {R['socket_bypass_mLmin']:.0f} mL/min, 2.8 to 4.6 "
        "times the membrane flow; controls: socket 43 mm above the dip line, tethered plug, dip-line pictogram; a self-closing socket proposed (D12)",
        WITHIN, closed_by="PR-028; HWA-DEC-001 D12")
c.cited("S21", "Freezing when wet can crack fibres and potting without changing flow, so the straw is not freeze tolerant and says so",
        "Physics", "Thermodynamics", "Water expands about 9 % on freezing", "No freeze claim; on-product warning; a straw that may have frozen is replaced, "
        "since the air check finds gross defects only (S20)", WITHIN, closed_by="PR-016")
# --- Hygiene and materials ----------------------------------------------------------------------------------------
c.cited("S22", "Bacteria can grow on the carbon and in the clean header during wet storage and reach the user directly, since the carbon sits after the barrier and "
        "removes any chlorine residual", "Biology", "Microbiology", "Heterotrophic growth on GAC is well known; Rev A section 05",
        "Design: drainable, capped, carbon replaced by volume; saliva and blow-back reach the carbon from the mouth side (D9); regrowth after wet storage "
        "to measure (TG)", PLAUSIBLE, closed_by="")
c.cited("S23", "Every wetted material, the membrane and potting included, is available in a grade listed for drinking-water contact",
        "Chemistry", "Materials and polymer chemistry", "NSF/ANSI/CAN 61 (extraction); 372 for lead in metal parts only (HWP-REG-001 W7)",
        "PP, EPDM, silicone, 316L and GAC grades exist; the membrane (PES or PVDF with PVP and a glycerine wetting agent, residual solvent) and the "
        "potting (polyurethane or epoxy) need the module maker's listing; a first-flush volume before first use (F11); printed prototypes see known "
        "potable test water only and nobody drinks from them", PLAUSIBLE, closed_by="")
c.cited("S32", "The carbon fines pad wets and passes water at the sip pressure", "Chemistry", "Physical chemistry",
        "Young-Laplace water entry pressure 4 gamma cos(theta) / d for a 20 um pore", "Untreated non-woven PP (contact angle about 100 deg) needs about 2.5 kPa "
        "to wet, a quarter of the sip; fixed: hydrophilic-treated pad (F6); its permeability is still assumed (C6)", WITHIN, closed_by="HWA-DEC-001 F6")
# --- Human factors, envelope and mass ---------------------------------------------------------------------------
c.claim("S24", "The straw is under 25 cm long and 3 cm across (kit compatible)", "Engineering and technology", "Standards practice",
        "Concept validation questions, item 39", round(R["across_port_mm"], 1), 30.0, "mm across",
        closed_by=f"{CAL} section 9 (length {R['length_mm']:.0f} mm; 0.4 mm margin across the plug)")
c.claim("S25", "The straw weighs under 100 g dry", "Mathematics", "Units and dimensional analysis", "Model volumes x densities (cad_parts.MATERIALS)",
        round(R["mass_g"], 1), 100.0, "g", closed_by=f"{CAL} section 9 (full of water about {R['mass_full_g']:.0f} g)")
c.order_of_magnitude("S26", f"About {P['N_FIBRES']} fibres of 0.8 mm fill a 17.2 mm bundle at about 48 % packing", "Mathematics", "Orders of magnitude",
                     claimed=P["N_FIBRES"], estimate=0.48 * (P["BUNDLE_D"] / P["FIBRE_OD"]) ** 2, unit="fibres",
                     law="Fibre count = packing x (bundle / fibre diameter)^2", closed_by=f"{CAL} section 2")

# --- Dropped options -------------------------------------------------------------------------------------------
x = Check(ROOT / "docs/04-calcs/stem_results_dropped.csv")
x.order_of_magnitude("X1", "A2: a sintered ceramic tube 17 mm x 106 mm gives 200 mL/min at 10 kPa", "Physics", "Fluid mechanics", claimed=200.0,
                     estimate=R["A2_flow_mLmin"], unit="mL/min",
                     law=f"Radial Darcy flow; ceramic permeability from pot filters (1 to 3 L/h, Akvopedia; {R['Lp_pot_LMHbar']:.0f} L/(m2 h bar) at 15 mm); "
                         f"best case thin 0.2 um layer {R['A2_flow_best_mLmin']:.0f} mL/min")
x.cited("X2", "A2: a 0.2 to 1 um ceramic retains cysts and reduces bacteria", "Biology", "Microbiology", "Size exclusion; pot filters reduce bacteria "
        "by about 2 log with silver (Akvopedia)", "A 1 um rating does not retain 0.3 to 0.5 um bacteria; holds only as reduction, and the option is dropped on X1", WITHIN)
x.order_of_magnitude("X3", "A3: copper in the straw inactivates bacteria during a sip", "Biology", "Microbiology", claimed=R["A3_contact_s"],
                     estimate=R["A3_needed_s"], unit="s", law="Copper pots reduced bacteria over 16 h storage (Sudha et al. 2012); wet copper contact "
                     "killing takes minutes to hours (Grass et al. 2011)")
x.cited("X4", "A3: charcoal removes bacteria and protozoa", "Biology", "Microbiology", "Granular carbon is an adsorbent, not a size barrier: water passes "
        "between 0.4 to 1.7 mm granules", "Gaps between granules are 100 times a bacterium; carbon can also grow bacteria", FAILS)
x.cited("X5", "A3: copper and charcoal address Cryptosporidium", "Biology", "Microbiology", "Cryptosporidium oocysts resist chemical disinfectants "
        "(chlorine; HWP-CLM-001)", "No mechanism in seconds", FAILS)
x.cited("X6", "A3: copper released in a sip stays below the 1.3 mg/L action level", "Chemistry", "Environmental and atmospheric chemistry",
        "EPA Lead and Copper Rule action level (Rev A R2)", "Likely low in a flowing sip; the first draw after wet storage (about 9 dm2 of copper in "
        "17 mL) may exceed it, release rate to assess; not the reason the option fails", PLAUSIBLE)


def table(rows, dropped=False):
    out = ["| # | Claim (number and unit) | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda r: int(r["id"][1:])):
        v = r["verdict"] + (" (option dropped)" if dropped and r["verdict"] == FAILS else "")
        out.append(f"| {r['id']} | {r['claim']} | {r['field']} | {r['branch']} | {r['law']} | {r['check']} | {v} | {r['closed_by'] or 'Open'} |")
    return "\n".join(out)


def inject(doc, tag, text):
    s = doc.read_text(encoding="utf-8")
    a, b = f"<!-- {tag} -->", f"<!-- /{tag} -->"
    if a in s and b in s:
        i, j = s.index(a) + len(a), s.index(b)
        doc.write_text(s[:i] + "\n" + text + "\n" + s[j:], encoding="utf-8")


if __name__ == "__main__":
    state = c.write()
    x.write()
    doc = ROOT / "docs/01b-stem-check.md"
    if doc.exists():
        inject(doc, "STM_TABLE", table(c.rows))
        inject(doc, "STM_DROPPED", table(x.rows, dropped=True))
        print("refreshed tables in docs/01b-stem-check.md")
    print("A1 state:", state)
