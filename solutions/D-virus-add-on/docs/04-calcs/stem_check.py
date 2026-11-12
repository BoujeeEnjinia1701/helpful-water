#!/usr/bin/env python3
"""HWD-STM-001 STEM check for Helpful Water D (chlorine co-treatment add-on). Run from the solution folder after sizing.py:

    python docs/04-calcs/sizing.py && python docs/04-calcs/stem_check.py && python docs/04-calcs/stm_table.py

Every physical, chemical and biological claim of the idea and of options D1, D2 and D3, with the water checks of
STANDARDS section 25.6 (disinfection dose, CT, residual and by-products in full; hydraulics and separation where they
apply to an add-on). Numbers come from docs/04-calcs/sizing_results.json (HWD-CAL-001). Rows closed by a fix made under
Amish's standing instruction of 2026-10-23 name the decision (HWD-DEC-001 F1 to F12) in "closed_by". Rows of the
dropped option D3 go to stem_results_dropped.csv.

Licence: Apache-2.0 (Helpful Engineering licensing guide). Design Molecule Labs with Helpful Engineering.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
from stem_check import Check, WITHIN, PLAUSIBLE, FIX, FAILS  # noqa: E402,F401

J = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
r, C = J["results"], J["cited"]
sc, d = r["scenarios"], r["dose_mg_l"]
c = Check(ROOT / "docs/04-calcs/stem_results.csv")

# ---- dose arithmetic (chemistry, mathematics) ------------------------------------------------------------------
# Rows revised after the independent review of 2026-11-11 (HWD-STM-001, Independent review); fixes F7 to F12 and
# decision D7 are recorded in HWD-DEC-001 and HWD-DDR-004.
P_DROPS, P_ORIF = r["drop_ml"]["drops_1L"], r["drop_ml"]["orifice_mm"]
tm, od, sq, br = r["timer"], r["overdose"], r["oring_squeeze_pct"], r["bottle_range"]
c.cited("S1", f"A 3.5 mg NaDCC tablet carries 2.0 mg of available chlorine ({r['tablet_cl_share']['1L']:.0%} of its mass, anhydrous basis)",
        "Chemistry", "Inorganic", "Stoichiometry: two N-Cl per NaDCC, each counted as one Cl2; IFRC catalogue WASDCHLA01 (2 mg per 3.5 mg tablet)",
        f"Theory {r['nadcc_available_cl']['dihydrate']:.1%} (dihydrate) to {r['nadcc_available_cl']['anhydrous']:.1%} (anhydrous); catalogue tablets "
        f"{min(r['tablet_cl_share'].values()):.0%} to {max(r['tablet_cl_share'].values()):.0%}, so the tablets are anhydrous NaDCC with binder", WITHIN)
c.claim("S2", "D1: one matched tablet gives about 2 mg/L free chlorine (1 L tablet in 1 L, or 20 L tablet in 20 L; 1.6 mg/L in 25 L)",
        "Mathematics", "Units and dimensional analysis", "Dose = available chlorine / volume; household tablet doses (IFRC tablet-choice note: 67 mg per 20 to 25 L)",
        d["D1_20L_one_25L"], 1.0, "mg/L", rule="above")
c.claim("S3", "The double dose for settled turbid water (two tablets, 4.0 mg/L) stays at or below the WHO chlorine guideline value of 5 mg/L in the containers on the label (1 to 1.5 L, 20 L)",
        "Chemistry", "Environmental and atmospheric chemistry", "WHO guideline value 5 mg/L (WHO chlorine fact sheet 2022); IFRC: double dose if visibly turbid; bottle range from S42",
        d["D1_20L_two"], C["WHO_GV"], "mg/L", rule="below")
c.cited("S4", f"Free chlorine after 30 minutes stays at or above the WHO 0.5 mg/L for clear water (under 5 NTU) at the single dose ({sc['clear']['c30']:.1f} mg/L)",
        "Chemistry", "Physical chemistry", "WHO GDWQ: at least 0.5 mg/L after 30 min at pH under 8 (via WEDC Mobile Note 7); residual model with assumed demand 0.3 mg/L",
        f"Passes while the 30 minute demand is under 1.5 mg/L; demand is assumed, and Wu and Dorea (2020) measured up to 4 mg/L over 24 h in jerrycans, so real demand is measured (HWP-VER-001 TJ)", PLAUSIBLE)
c.cited("S5", f"A residual remains for a day of storage before filtering: {sc['clear']['c24h']:.2f} mg/L (clear) and {sc['turbid_double']['c24h']:.2f} mg/L (turbid, double dose) at 24 h",
        "Chemistry", "Physical chemistry", "CDC Safe Water System: above 0.2 mg/L at 24 h (Lantagne 2006); first-order decay after the 30 min demand, k assumed 0.035 and 0.07 per hour",
        f"24 h consumption {sc['clear']['consumed_24h']:.1f} and {sc['turbid_double']['consumed_24h']:.1f} mg/L, inside the 0.5 to 4 mg/L measured in 20 L jerrycans (Wu and Dorea 2020); at the top of that range the single dose leaves none; the residual matters only until the water is filtered (S16); real demand to measure (HWP-VER-001 TJ, TD)",
        PLAUSIBLE)
c.cited("S6", f"A single dose in turbid water keeps a residual for 24 h (it falls to {sc['turbid_single']['c24h']:.2f} mg/L)",
        "Chemistry", "Physical chemistry", "Same model with turbid demand 1.0 mg/L in 30 min; CDC 0.2 mg/L at 24 h; IFRC: under 5 NTU for proper disinfection, above 50 NTU do not chlorinate",
        f"Failed as briefed (one tablet for all water). Fixed (F1): settle first and use two tablets for 5 to 50 NTU, do not use above 50 NTU; the double dose leaves {sc['turbid_double']['c24h']:.2f} mg/L at 24 h on an assumed 1.0 mg/L demand; demand at 10, 25 and 50 NTU to measure (TJ)",
        PLAUSIBLE, closed_by="HWD-DEC-001 F1")
c.cited("S7", f"Water dosed for 30 minutes stays under the CDC 2.0 mg/L acceptability limit at 1 h when clear ({sc['clear']['c60']:.2f} mg/L), but not at the turbid double dose ({sc['turbid_double']['c60']:.2f} mg/L)",
        "Biology", "Human physiology and biomechanics", f"CDC SWS 2.0 mg/L at 1 h; median taste detection {C['TASTE']['detect_nadcc']} and acceptability {C['TASTE']['accept_nadcc']} mg/L for NaDCC (Crider et al. 2018)",
        "Most users will taste chlorine before filtering; the carbon stages of A to C are intended to remove it, so water is drunk only after the filter; taste after the filter is measured (TG, TH)", PLAUSIBLE)
# ---- CT and inactivation (biology) -----------------------------------------------------------------------------
c.claim("S8", f"In 30 minutes clear water at the single dose reaches the CT for 4-log virus inactivation at 5 C (CT {sc['clear']['ct30_epa']:.0f} against 8 mg min/L)",
        "Biology", "Microbiology", "US EPA CT table for 4-log virus inactivation by free chlorine, pH 6 to 9 (Hepatitis A data with a safety factor of 3); CT = residual at the end of contact x time (EPA definition; the integral gives 53)",
        sc["clear"]["ct30_epa"], 8.0, "mg min/L", rule="above")
c.cited("S9", f"No 4-log virus credit is taken above 5 NTU: the misuse case (turbid water, single dose) reaches CT {sc['turbid_single']['ct30_epa']:.0f} in 30 minutes, but the EPA table assumes low-turbidity water",
        "Biology", "Microbiology", "As S8, demand 1.0 mg/L in 30 min; particle-associated viruses are shielded from chlorine, so the CT table is not applied to 5 to 50 NTU water (IFRC: under 5 NTU for proper disinfection)",
        "The misuse case is not credited; settled turbid water at the double dose is credited only after the TB challenge at 10 and 50 NTU (HWP-VER-001 TB)", WITHIN)
c.cited("S10", "No quantified norovirus claim is made; free chlorine at the household dose is expected to act on human norovirus, but the data are not drinking-water infectivity data",
        "Biology", "Microbiology", "Dunkin et al. 2017: 2-log molecular (RT-qPCR) reduction of norovirus GII at CT 7.5 to 13 in produce wash water; no 4-log infectivity data for human norovirus in drinking water",
        f"CT {sc['clear']['ct30_epa']:.0f} is {r['ct_margin']['norovirus_gii_2log_at_30min']:.1f} times the 2-log molecular figure, which is a different measure from infectivity; virus reduction for the combined system is measured, never assumed (HWP-VER-001 TB)", PLAUSIBLE)
c.cited("S11", "Cold water gets a longer wait: 30 min above 18 C, 60 min at 10 to 18 C, 120 min below 10 C",
        "Biology", "Microbiology", "US EPA CT rises from 3 (20 C) to 12 mg min/L (0.5 C); WHO and WEDC TN 11: 30 minutes at 18 C and above; the 60 and 120 minute tiers are practice guidance (Akvopedia NaDCC page, revision of the page)",
        f"Already at 30 min the CT is {r['ct_margin']['virus_4log_0c_at_30min']:.1f} times the 0.5 C requirement, so the longer cold waits are a conservative margin, not the basis of the virus check; at 120 min the CT is {sc['clear']['ct120_epa']:.0f}, {r['ct_margin']['virus_4log_0c_at_120min']:.0f} times", WITHIN)
c.cited("S12", f"Disinfection weakens as pH rises (HOCl share {r['hocl_share']['7.5']:.0%} at pH 7.5, {r['hocl_share']['8.0']:.0%} at 8.0 at 20 C; {r['hocl_share_5c']['8.5']:.0%} at pH 8.5 and 5 C); pH above 8 takes 60 minutes and pH above 9 is excluded",
        "Chemistry", "Physical chemistry", f"HOCl pKa by temperature (Morris 1966): {r['pka_hocl']['25']} at 25 C, {r['pka_hocl']['20']} at 20 C, {r['pka_hocl']['5']} at 5 C; EPA CT table applies to pH 6 to 9 and jumps from 8 to 60 at pH 10; Akvopedia: unreliable above pH 9",
        f"The check uses the EPA table directly (CT {sc['clear']['ct30_epa']:.0f} against 8 at pH 6 to 9); HOCl weighting is not applied on top because the table already covers pH; the 60 minute rule above pH 8 is extra margin; field pH to record (TD), source suitability by class (HWP-SRC-001)", WITHIN)
c.cited("S13", f"Chlorine does not inactivate Cryptosporidium at household doses, so the filter (A to C) is still needed",
        "Biology", "Microbiology", "CDC chlorine timetable: about 15,300 min at 1 mg/L, pH 7.5, 25 C; Akvopedia; HWP-CLM-001",
        f"At {sc['clear']['c30']:.1f} mg/L the CT would take about {sc['clear']['days_ct_crypto']:.0f} days; D makes no claim against Cryptosporidium", WITHIN)
c.cited("S14", "Giardia is not claimed from chlorine at 30 minutes; the filter is the barrier for cysts",
        "Biology", "Microbiology", "CDC timetable: Giardia about 45 min at 1 mg/L, pH 7.5, 25 C",
        f"CT {sc['clear']['ct30_epa']:.0f} against 45: margin {r['ct_margin']['giardia_at_30min']:.2f} at 25 C, and the cold-water Giardia CT is several times higher, so no claim is made", WITHIN)
c.cited("S15", "Chlorination is only for water under 50 NTU, and settled water does best (under 5 NTU)",
        "Chemistry", "Environmental and atmospheric chemistry", "IFRC tablet-choice note: 0 to 5 NTU low, 5 to 50 NTU high, above 50 NTU do not chlorinate; particles shield microbes and add demand",
        "Pictogram: cloudy water, let it settle and pour off, use two tablets; muddy water, do not use D alone (HWP-SRC-001 SC3, SC6); users cannot measure NTU, so the pictogram's see-through test is checked by persona (TH)", WITHIN)
# ---- interfaces with A to C -----------------------------------------------------------------------------------
c.cited("S16", "Where the household stores filtered water (solution C), a chlorine residual remains to protect it, because C has no carbon stage; A and B are drunk at once",
        "Chemistry", "Physical chemistry", "CDC SWS: residual above 0.2 mg/L at 24 h is for protection in storage; granular carbon removes free chlorine fast (HWP-CLM-001 sequence: chlorinate, wait, filter, carbon removes taste)",
        "Fixed: C is carbon-free (HWC-DEC-001 D3), so the residual reaches C's closed clean bucket; A and B keep their carbon and no residual is claimed for them (on-product wording, HWP-CLM-001). The residual at 24 h in C is confirmed in test TJ at TRL 4",
        WITHIN, closed_by="Fix: HWD-DEC-001 D3 and HWC-DEC-001 D3 (Amish, 2026-11-11)")
c.cited("S17", "A few mg/L of free chlorine ahead of the filter does not harm the hollow-fibre modules of A to C",
        "Chemistry", "Materials and polymer chemistry", "PVDF and PES hollow fibres are commonly cleaned with hypochlorite; tolerance is given by makers as a chlorine exposure in mg h/L, commonly 1e5 to 1e6",
        f"Even with the fibres soaked in dosed water all year the exposure is about {r['membrane_exposure_mg_h_l_year']:,.0f} mg h/L; the bought module's limit and flux on chlorinated feed are confirmed with the supplier and over 100 L (HWD-DEC-001 C3)", PLAUSIBLE)
c.cited("S18", "The carbon stages of A to C remove the dosed chlorine taste over their life (B: about 7 g of carbon against about 1.7 mg/L x 150 L = 0.26 g of chlorine)",
        "Chemistry", "Physical chemistry", "Carbon reduces free chlorine by surface reaction; NSF/ANSI 42 chlorine reduction is the reference test",
        "Total capacity is not the limit: 7 g is about 15 mL of bed, a contact time of a few seconds at B's flow, so breakthrough at the real flow and over the module's life in litres is measured (HWP-VER-001 TG)", PLAUSIBLE)
# ---- by-products and overdose ------------------------------------------------------------------------------------
c.cited("S19", f"By-products stay low: cyanuric acid from NaDCC at the double dose is about {od['cya_at_4mgl']:.1f} mg/L against the WHO 40 mg/L; THMs from household chlorination have been found below WHO guideline values",
        "Chemistry", "Environmental and atmospheric chemistry", "WHO NaDCC fact sheet (NaDCC 50 mg/L, cyanuric acid 40 mg/L); Lantagne et al. 2008 as summarised by Akvopedia; WHO GDWQ THM guideline values",
        "Cyanuric acid holds by arithmetic; THMs at the double dose in organic-rich settled water are the case the field data do not cover, so THMs are measured (TG)", PLAUSIBLE)
c.cited("S20", f"A 20 L tablet cannot enter the blue 1 L well (13 mm tablet against a 9.5 mm bore); it would give {od['wrong_tablet_20L_in_1L_cl']:.0f} mg/L chlorine and {od['wrong_tablet_20L_in_1L_nadcc']:.0f} mg/L NaDCC in a bottle",
        "Engineering and technology", "Manufacturing tolerances", "WHO guideline values 5 mg/L chlorine and 50 mg/L NaDCC; keyed well bores 9.5 mm (1 L) and 14.5 mm (20 L) against assumed tablet sizes 8 and 13 mm",
        "Fixed as briefed (F2, colour-keyed inserts); the key blocks the well only, so a 20 L tablet dropped straight into an open bottle neck is a misuse the cap cannot stop: the 20 L tablets ship only in the household kit, strips are matched to the insert colours where the supplier allows, and the label warns (HWD-RSK-001); tablet sizes are measured before the bores are frozen (C1)",
        PLAUSIBLE, closed_by="HWD-DEC-001 F2, C1")
c.cited("S21", f"No more than two tablets fit in the well, so the dose cannot pass the 5 mg/L guideline value (three 1 L tablets would give 6 mg/L)",
        "Engineering and technology", "Manufacturing tolerances", "Free height under the plug stop 8.0 mm (1 L) and 11.0 mm (20 L) against tablets 3.5 and 5.0 mm thick (assumed)",
        f"Two fit (7.0 under 8.0 mm); three are stopped only while each tablet is thicker than {od['three_fit_if_t_below_mm']['1L']} mm (1 L) or {od['three_fit_if_t_below_mm']['20L']} mm (20 L); the minimum thickness is measured (C1) and the plug stop set from it; broken tablets are a misuse on the label",
        PLAUSIBLE, closed_by="HWD-DEC-001 F3, C1")
# ---- timer (physics) ---------------------------------------------------------------------------------------------
c.claim("S22", f"The ball timer works in the Stokes regime: a 2 mm steel ball in about {tm['cst']:,.0f} cSt silicone falls 13 mm in about {tm['t_nominal_min']:.0f} min at 25 C",
        "Physics", "Fluid mechanics", f"Stokes drag with the Haberman-Sayre wall factor {tm['wall_haberman_sayre']} at d/D = 0.5 (Faxen, {tm['faxen']}, is not valid there); fluid {tm['mu_pa_s']:.0f} Pa s; PMX-200 type grades exist to 600,000 cSt",
        tm["reynolds"], 0.1, "Reynolds number", rule="below")
c.claim("S23", f"The timer never reads less than 30 minutes up to 40 C air temperature (nominal {tm['t_nominal_min']:.0f} min at 25 C; {tm['t_40c_low_min']:.1f} min at 40 C and -10 % viscosity)",
        "Engineering and technology", "Manufacturing tolerances", f"Fall time scales with viscosity; viscosity tolerance assumed 10 %; activation energy 15 kJ/mol; the briefed 34 min nominal read {tm['t_briefed_34_40c_low_min']:.0f} min at 40 C",
        tm["t_40c_low_min"], 30.0, "min", rule="above", closed_by="HWD-DEC-001 F11")
c.cited("S24", f"In cold water the user runs the timer twice (10 to 18 C) or three times (under 10 C); the timer itself slows about {tm['cold_ratio']} times at 10 C",
        "Physics", "Thermodynamics", f"Silicone viscosity-temperature coefficient {C['PDMS_VTC']} (Dow PMX-200), which back-calculates to the assumed 15 kJ/mol; contact times as S11",
        f"Low-tolerance totals at the warm end of each band: {tm['runs_total_min']['10-18 C']:.0f} min (two runs at 18 C, need 60) and {tm['runs_total_min']['<10 C']:.0f} min (three runs at 10 C, need 120). Failed as briefed (one run for all water); fixed by the run count on the label (F4, revised to one, two, three by F11). The user judges water temperature by feel; that is checked by persona (TH)",
        WITHIN, closed_by="HWD-DEC-001 F4, F11")
# ---- integrity, human factors, materials --------------------------------------------------------------------------
c.cited("S25", "The 1 L tablet dissolves fully in the well when the bottle is turned over and shaken, and the clear plug shows it has gone",
        "Chemistry", "Physical chemistry", "NaDCC household tablets are effervescent; floor slots let raw water flood the well when inverted; the CO2 vents through the slots",
        "Dissolution time in the well at 5 and 30 C to measure (TJ); the pictogram says shake until the tablet has gone, then start the timer; the 20 L route cannot be inverted and is S41", PLAUSIBLE)
c.cited("S26", f"The well insert O-ring is squeezed within the static-seal range in the 20.4 mm bore over the stated tolerances ({sq['min']} to {sq['max']} %, nominal {sq['nominal']} %)",
        "Engineering and technology", "Manufacturing tolerances", "Static radial gland: squeeze 15 to 30 %; groove root 17.9 mm; bore +/-0.05 mm, groove +/-0.03 mm, section 1.6 +/-0.08 mm (ISO 3601 class); stretch 4.1 %",
        f"Failed as briefed twice: root 17.2 gave 0 %, and root 17.8 at print tolerance (+/-0.1 mm) gave {sq['briefed_17_8_print_tol_min']} % at the low end. Fixed (F5, F10): root 17.9 mm, the bore and groove held to the stated tolerances (moulded at scale; the prototype insert is measured and reprinted to the gauge)",
        WITHIN if 15.0 <= sq["min"] and sq["max"] <= 30.0 else FAILS, closed_by="HWD-DEC-001 F5, F10")
c.cited("S27", "The cap screws onto the same 28 mm PCO 1881 neck as the B cartridge and onto the 28 mm port proposed for C's raw-bucket lid",
        "Engineering and technology", "Standards practice", "PCO 1881 neck data (Kapy CAD), as used in HWB-CAL-001; C's lid port is a proposal to solution C",
        "The bottle neck interface follows HWB; the C port is not yet agreed, so the row stays open until the interface is agreed (HWD-DEC-001 D4)", PLAUSIBLE)
c.cited("S28", "Every wetted material resists dilute chlorine and the tablet concentrate in the well, and is available in a drinking-water listed grade (PP, silicone, EPDM, PETG)",
        "Chemistry", "Materials and polymer chemistry", "NSF/ANSI/CAN 61 (HWP-REG-001 W7); polyolefins and EPDM resist dilute hypochlorite; PC is prone to stress cracking in alkaline hypochlorite",
        f"While a tablet dissolves the well briefly holds about {od['well_conc_g_l']['1L']} g/L (1 L) to {od['well_conc_g_l']['20L']} g/L (20 L) of chlorine; the clear plug is PETG or clarified PP, not PC (F12); printed prototype grades are not listed, so prototypes see known potable test water only; concentrate soak and leachables to test (TG)", PLAUSIBLE)
c.cited("S29", "Tablets keep 3 to 5 years in their strips; the cap stores no tablets loose",
        "Chemistry", "Inorganic", "Akvopedia: strips 5 years, tubs 3 years; humidity degrades NaDCC once the foil is open",
        "One tablet is taken from the strip per use; spare strips ride in the kit, not in the cap", WITHIN)
c.cited("S30", "Freezing and heat do not damage the tablets or the timer, and a frozen bottle is thawed before dosing",
        "Physics", "Thermodynamics", f"Water expands about 9 % on freezing; PDMS stays liquid far below 0 C and expands {C['PDMS_EXPANSION_PER_K']:.1e} per K (Dow PMX-200)",
        f"Water left in the well could crack the clear plug if frozen: empty the cap in freezing weather. The sealed timer holds {tm['fluid_ml']} mL; from a 25 C fill its fluid changes by {tm['expansion_ul'][0]} to +{tm['expansion_ul'][1]} uL over -10 to 60 C ({tm['expansion_share']:.1%}), enough to load the end caps or open a bubble; an expansion allowance is to be detailed and a freeze-thaw and 60 C fall-time test run (C5, TI)", PLAUSIBLE)
c.cited("S31", "A child or an older user can open a foil strip, drop a tablet in, turn the plug (3.5 turns) and flip the timer the counted number of times",
        "Biology", "Ergonomics", "Low-dexterity users struggle with small parts and caps (HWP-PRB-001 personas)",
        "To observe by persona (HWP-VER-001 TH) with pass criteria: dose done in under 2 minutes, no tablet dropped, the right run count chosen; a strip with a tear notch and a 27 mm knurled plug are specified", PLAUSIBLE)
c.claim("S32", f"D1 weighs under 60 g without the bottle ({r['mass_g']['D1']:.0f} g, model volumes)",
        "Mathematics", "Units and dimensional analysis", "Model volumes x densities (cad_parts.MATERIALS), per part in cad/fidelity.json", r["mass_g"]["D1"], 60.0, "g", rule="below")
c.order_of_magnitude("S33", "CDC SWS arithmetic: 3 mL of 1.25 % hypochlorite in 20 L is about 1.9 mg/L",
        "Mathematics", "Units and dimensional analysis", claimed=1.875, estimate=12.5 * 3.0 / 20.0, unit="mg/L",
        law="1.25 % = 12.5 g/L = 12.5 mg/mL; 3 mL x 12.5 mg/mL / 20 L")
c.claim("S34", f"D1 prototype parts and test tablets cost under the USD 10 value-engineering target (USD {r['cost']['bom_usd']:.2f})",
        "Engineering and technology", "Standards practice", "BOM sum (bom/bom.csv); estimates, not quotes", r["cost"]["bom_usd"], 10.0, "USD", rule="below")
# ---- D2 metered liquid -------------------------------------------------------------------------------------------
c.claim("S35", f"D2: the metering chamber holds {r['chamber_ml']:.2f} mL below the standpipe top, within 5 % of the CDC 3.0 mL dose for 20 L",
        "Mathematics", "Units and dimensional analysis", "Annulus area (18 mm chamber, 5 mm standpipe) x 12.8 mm standpipe height; tilt and wall film are not modelled and the dose is weighed at TRL 4",
        abs(r["chamber_ml"] - 3.0), 0.15, "mL from 3.0", rule="below")
c.cited("S36", f"D2: {P_DROPS} drops from a {P_ORIF} mm orifice treat 1 L at {d['D2_1L_drops_low']:.1f} to {d['D2_1L_drops_high']:.1f} mg/L",
        "Physics", "Fluid mechanics", f"Tate's law with the Harkins-Brown factor 0.60 to 0.72; LDPE does not wet, so the drop pins at the orifice: {r['drop_ml']['range'][0]} to {r['drop_ml']['range'][1]} mL per drop",
        f"Failed as briefed: three drops from a 1.2 mm orifice give {d['D2_1L_3_drops_1_2mm_low']:.2f} to {d['D2_1L_3_drops_1_2mm_high']:.2f} mg/L, under 1. Fixed (F9): 2.0 mm orifice and five drops; drops weighed gravimetrically at TRL 4; a squeezed stream is the misuse on the label",
        PLAUSIBLE, closed_by="HWD-DEC-001 F9")
c.cited("S37", f"D2: the liquid loses strength over its shelf life (a warm-storage bound gives {r['d2_decay']['warm_3mo_share']:.0%} after 3 months, so one cap gives {r['d2_decay']['dose_20L_warm_3mo']:.1f} mg/L, and {r['d2_decay']['dose_20L_warm_6mo']:.2f} mg/L at 6 months)",
        "Chemistry", "Physical chemistry", "WEDC: half strength in a year when cool and dark; E4C WaterGuard: 13 % to 8 % in 75 days at 27 C (a bound for 1.25 %); Akvopedia: use within 3 months",
        "Under-dosing as the liquid ages is a silent failure the user cannot see; D2 would need a date stamp, a 3 month use-by and a two-cap rule after 2 months (scored in HWD-OPT-001)", PLAUSIBLE)
c.claim("S38", f"D2: a gentle squeeze lifts the liquid into the chamber (about {r['effort']['d2_squeeze_kpa_needed']:.1f} kPa) well within a weak child's grip",
        "Biology", "Human physiology and biomechanics", "Hydrostatic lift of 134 mm plus 0.5 kPa entry loss; grip 124 N weak child (Camry norms, as HWB-CAL-001); squeeze force assumed 10 N",
        r["effort"]["d2_squeeze_n_assumed"], r["effort"]["grip_n"]["child_10_11_weak"] * 0.4, "N", rule="below")
c.cited("S39", "D2: 1.25 % hypochlorite is an irritant, not a corrosive at that strength, and is kept behind a child-resistant flip cap",
        "Biology", "Toxicology", "CDC SWS uses 1.25 % for household distribution; under CLP generic limits 1 to 5 % of a Skin Corr. 1B substance classes as Skin Irrit. 2 and Eye Irrit. 2",
        "Hazard handled in HWD-RSK-001 (eye splash at pH about 12, child access); D1 tablets carry a do-not-swallow warning on the strip (IFRC)", WITHIN)
# ---- rows added by the independent review (2026-11-11) ----------------------------------------------------------------
c.cited("S40", f"A 1 L tablet put in the orange 20 L well by mistake is noticed (it would give {od['wrong_tablet_1L_in_20L_cl']} mg/L, two give {od['two_1L_in_20L_cl']} mg/L)",
        "Engineering and technology", "Manufacturing tolerances", "An 8 mm tablet passes a 14.5 mm bore; the key works one way only; WHO 0.5 mg/L after 30 min",
        "A silent under-dose: mitigated by actual-size tablet circles on the label next to each insert, the clear plug, and 20 L tablets packed only with the household kit; a free chlorine check after the wait would catch it (D7); misuse trial (TH)", PLAUSIBLE)
c.cited("S41", "On C's bucket port the 20 L tablet dissolves and mixes through the 20 L without turning the bucket over",
        "Physics", "Fluid mechanics", "A 20 kg bucket cannot be inverted and shaken; a dissolved dose entering at the surface mixes slowly without stirring",
        "Failed as briefed (the inversion method was written for bottles). Fixed (F7): on the bucket the plug is taken off and raw water is poured through the well from a cup until the tablet has gone, then the bucket is stirred for 30 s with a clean stick before the timer starts; free chlorine at top and bottom after 1 and 5 minutes within 20 % of the mean (TJ); the simpler drop-in-before-filling method is put to Amish under D4",
        PLAUSIBLE, closed_by="HWD-DEC-001 F7, D4")
c.claim("S42", f"The 1 L tablet is used only in bottles of 1 to 1.5 L, so a clear single dose gives at least 1.33 mg/L and a double dose at most 4.0 mg/L",
        "Mathematics", "Units and dimensional analysis", f"Dose = 2 mg / volume: 0.5 L gives {br['0.5']['one']} and {br['0.5']['two']} mg/L (double over 5); 2 L gives {br['2.0']['one']} mg/L; range printed on the blue insert label (F8)",
        br["1.0"]["two"], C["WHO_GV"], "mg/L", rule="below", closed_by="HWD-DEC-001 F8")
c.cited("S43", "A wrong, missing, weak or undissolved dose is made visible by a free chlorine check after the wait (test strips in the household kit, a comparator for partners)",
        "Engineering and technology", "Sensing resolution", "Free chlorine is invisible; the clear plug shows only that the tablet has gone; DPD test strips or a comparator read 0.2 mg/L and above",
        "Fixed: DPD free chlorine strips in each household kit, used after the wait on every new source and every tenth batch (target at least 0.5 mg/L); a comparator for programme staff. The strip cost is to assess",
        WITHIN, closed_by="Fix: HWD-DEC-001 D7 (Amish, 2026-11-11)")
c.write()

# ---- dropped option D3: erosion feeder ----------------------------------------------------------------------------
x = Check(ROOT / "docs/04-calcs/stem_results_dropped.csv")
d3 = r["d3"]
x.claim("X1", "D3: an erosion feeder in the raw bucket holds the dose between 1 and 5 mg/L for standing times of 30 minutes to a day",
        "Chemistry", "Physical chemistry", "A release set by contact time gives dose proportional to standing time (TAMU tablet chlorination guide: dissolution depends on contact amount and time)",
        d3["stand_ratio"], d3["allowed_ratio"], "ratio of longest to shortest standing time", rule="below")
x.cited("X2", f"D3: left overnight at a rate that gives 2 mg/L in 30 min the bucket reaches about {d3['dose_at_24h_if_2mgl_at_30min']:.0f} mg/L",
        "Chemistry", "Environmental and atmospheric chemistry", "Dose = rate x time / volume; WHO guideline value 5 mg/L",
        f"Set instead for 5 mg/L at 24 h, the 30 minute dose is {d3['dose_at_30min_if_5mgl_at_24h']:.2f} mg/L, far below 0.5", FAILS)
x.cited("X3", "D3: TCCA pool tablets release chlorine slowly and safely in a wetted feeder",
        "Chemistry", "Inorganic", "TAMU: TCCA not approved for tablet chlorinators, too slow, and repeated wetting can form explosive nitrogen trichloride; never mix with calcium hypochlorite",
        "Hazard as well as range; calcium hypochlorite erosion feeders work only in flowing water", FAILS)
x.cited("X4", "D3: the household can see when the feeder is spent or over-dosing",
        "Engineering and technology", "Sensing resolution", "No dose indication without a chlorine test",
        "Fails: no dose indication without a chlorine test, so under- or over-dose is silent; the option is dropped on X1", FAILS)
x.write()
