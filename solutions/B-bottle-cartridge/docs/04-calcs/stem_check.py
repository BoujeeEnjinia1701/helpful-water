#!/usr/bin/env python3
"""HWB-STM-001 STEM check for Helpful Water B (bottle cartridge). Run from the solution folder after sizing.py:

    python docs/04-calcs/sizing.py && python docs/04-calcs/stem_check.py

Every physical, chemical and biological claim of the idea and of options B1, B2 and B3, with the water checks of
STANDARDS section 25.6. Numbers come from docs/04-calcs/sizing_results.json (HWB-CAL-001). Rows closed by a fix made
under Amish's standing instruction of 2026-10-23 name the decision (HWB-DEC-001 F1 to F9) in "closed_by". Rows S28 to
S33 and the rewording of S1 to S27 follow the independent review of 2026-11-11 (HWB-STM-001, Independent review).

Licence: Apache-2.0 (Helpful Engineering licensing guide). Design Molecule Labs with Helpful Engineering.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
from stem_check import Check, WITHIN, PLAUSIBLE, FIX, FAILS  # noqa: E402,F401

r = json.loads((ROOT / "docs/04-calcs/sizing_results.json").read_text())
b1, sq, c10 = r["b1"], r["squeeze_kpa"], r["b1_10c"]
c = Check(ROOT / "docs/04-calcs/stem_results.csv")
LP = "assumed clean-water permeability 1,000 L/(m2 h bar), a quarter of the 0.1 um PVDF example in US 8,708,161 B2"

# ---- hydraulics (25.6) -------------------------------------------------------------------------------------------
c.claim("S1", f"B1 gives at least 400 mL/min at a comfortable adult squeeze ({sq['adult']:.0f} kPa) with a clean module in 20 C water",
        "Physics", "Fluid mechanics", f"Darcy flux J = Lp x TMP over {r['area_m2']['B1']:.3f} m2 of outside fibre area, {LP}; Ergun bed, Hagen-Poiseuille lumens and outlet in series (CAL section 3); fouled {b1['adult']['fouled']['q_ml_min']:.0f}, at 10 C {c10['adult']['clean']['q_ml_min']:.0f} mL/min (S31)",
        round(b1["adult"]["clean"]["q_ml_min"]), 400, "mL/min", rule="above", margin=0.25, closed_by="")
c.claim("S2", f"B1 gives at least 150 mL/min at a weak child's squeeze ({sq['child_10_11_weak']:.1f} kPa, girls' boundary 11.8 kg) and an elderly woman's ({sq['elderly_f_weak']:.1f} kPa) with a clean module in 20 C water",
        "Physics", "Fluid mechanics", f"As S1 at the persona pressures; {LP}; fouled {b1['child_10_11_weak']['fouled']['q_ml_min']:.0f}, at 10 C {c10['child_10_11_weak']['clean']['q_ml_min']:.0f} mL/min (S31)",
        round(min(b1["child_10_11_weak"]["clean"]["q_ml_min"], b1["elderly_f_weak"]["clean"]["q_ml_min"])), 150, "mL/min", rule="above", margin=0.25)
c.cited("S3", f"A hand squeeze on a 1 L PET bottle gives about {sq['child_10_11_weak']:.0f} to {sq['adult']:.0f} kPa held and about {sq['adult_max']:.0f} kPa at full grip",
        "Biology", "Human physiology and biomechanics", "Grip norms (Camry dynamometer, 10 to 11 years and 70 to 99 years) x 40 % held x 0.8 wall loss over an 80 x 80 mm contact; STANDARDS 25.6 range 10 to 30 kPa",
        "Model only: the dynamometer grip is not the grip on an 80 mm cylinder (a diameter factor of about 0.6 would give 10 kPa for the adult) and a child's hand does not wrap 80 mm; two-handed squeezing is the design case; bottle pressure to measure with a gauge (HWP-VER-001 TH)", PLAUSIBLE)
c.claim("S4", "Mesh, carbon bed, lumens and outlet together take under a fifth of the squeeze pressure, so the membrane sets the flow",
        "Physics", "Fluid mechanics", "Pressure drop per stage at the adult squeeze: Ergun bed (12 x 40 GAC, void 0.40), lumens, nipple, nozzle and valve ports; clean bed only, silt loading is S32",
        round(b1["adult"]["clean"]["bed_kpa"] + b1["adult"]["clean"]["lumen_kpa"] + b1["adult"]["clean"]["outlet_kpa"] + b1["adult"]["clean"]["mesh_kpa"], 2),
        round(0.2 * sq["adult"], 2), "kPa", rule="below")
c.order_of_magnitude("S5", "Flux arithmetic: 1,000 L/(m2 h bar) x 0.174 m2 at 10 kPa is about 290 mL/min before the other stages",
        "Mathematics", "Units and dimensional analysis", claimed=1000 * r["area_m2"]["B1"] * 0.1 / 60 * 1000, estimate=r["b1_at_10kpa"]["clean"]["q_ml_min"], unit="mL/min",
        law="L/(m2 h bar) x m2 x bar = L/h; / 60 x 1000 = mL/min")
c.cited("S6", f"B2 gravity drip treats 1 L in under 15 minutes with a clean module in 20 C water (heads {r['b2']['clean']['head_empty_kpa']:.1f} to {r['b2']['clean']['head_full_kpa']:.1f} kPa)",
        "Physics", "Fluid mechanics", f"Falling-head drain of an inverted 1 L bottle through {r['area_m2']['B2']:.3f} m2; {LP}",
        f"{r['b2']['clean']['minutes_per_litre']:.1f} min per litre clean, {r['b2']['fouled']['minutes_per_litre']:.1f} min fouled, against 15 min; at 10 C {r['b2_10c']['clean']['minutes_per_litre']:.1f} and {r['b2_10c']['fouled']['minutes_per_litre']:.1f} min; rests on the assumed permeability (supplier flux data, HWB-DEC-001 C1)", PLAUSIBLE)
c.cited("S7", f"B3 press reaches {r['b3']['elderly_or_child']['clean']['press_kpa']:.0f} kPa with 80 N of arm or body weight and gives at least 300 mL/min with a clean module",
        "Physics", "Mechanics and statics", "p = (F - lip seal friction 10 N, assumed; 30 N would give 13 kPa) / cup bore area (70 mm); flow as S1",
        f"{r['b3']['elderly_or_child']['clean']['q_ml_min']:.0f} mL/min clean, {r['b3']['elderly_or_child']['fouled']['q_ml_min']:.0f} fouled, against 300; rests on the assumed permeability", PLAUSIBLE)
c.claim("S8", "B3 press tube holds the 350 mL fill line of treated water above and around the cartridge",
        "Mathematics", "Orders of magnitude", "Press tube volume less the cartridge housing volume", round(r["b3_volumes"]["clean_ml"]), 350, "mL", rule="above")
# ---- separation (25.6) -------------------------------------------------------------------------------------------
c.cited("S9", "A 0.1 um hollow-fibre membrane is a size barrier for protozoan cysts (about 3 to 15 um) and is designed to reduce most bacteria; no removal is claimed from the pore label",
        "Biology", "Microbiology", "Size exclusion: Cryptosporidium oocysts 4 to 6 um, Giardia cysts 8 to 12 um (40 to 120 x the 0.1 um pore); most bacteria are 0.3 um or more across, but thin forms such as Leptospira (about 0.1 um) reach the nominal pore; CDC: microfiltration very high effectiveness for protozoa, moderate for bacteria",
        "Sieving ratio about 1 for the thinnest bacteria and 3 for Brevundimonas diminuta (0.3 um), so the pore label is not a bacteria barrier; the supplier's absolute rating (C1) and an accredited log reduction (HWP-VER-001 TA, TB) decide", PLAUSIBLE)
c.cited("S10", "The membrane is not a virus barrier, so the product carries the no-virus warning and pairs with chlorine (solution D) where viruses are a risk",
        "Biology", "Microbiology", "Viruses about 0.02 to 0.3 um overlap and pass a 0.1 um pore (sieving ratio 0.2 to 3); CDC: microfiltration not effective for viruses",
        "No virus claim (Amish, 2026-11-11: no virus claim, co-treat); HWP-CLM-001 warning on the product", WITHIN)
# ---- adsorption (25.6) -------------------------------------------------------------------------------------------
c.order_of_magnitude("S11", "The carbon capsule holds about 7 g of 12 x 40 coconut GAC",
        "Chemistry", "Physical chemistry", claimed=7.0, estimate=r["carbon"]["mass_g"], unit="g",
        law="Bed 29.8 mm x 20 mm = 13.9 mL x bulk density 0.48 to 0.50 g/cm3 (Newterra 5DCAW 1240 data sheet)")
c.cited("S12", f"Carbon intended to reduce chlorine taste at an empty-bed contact time of {r['carbon']['ebct_s']['adult']:.1f} to {r['carbon']['ebct_s']['child_10_11_weak']:.1f} s (B1) and about {r['carbon']['ebct_b2_s']:.0f} s (B2)",
        "Chemistry", "Physical chemistry", "EBCT = bed volume / flow; the true residence time is about 0.4 x EBCT (void 0.40); seconds of contact are short for granular carbon (concept validation questions, item 19); free chlorine reacts fast at carbon surfaces, organics and odours much more slowly",
        "Chlorine taste reduction is a target only, no odour or organics claim, to measure with an NSF/ANSI 42 style test and a breakthrough curve that sets the capsule life (HWP-VER-001 TG); 150 L capsule life is assumed", PLAUSIBLE)
# ---- integrity and silent failure (25.6) -------------------------------------------------------------------------
c.claim("S13", "Squeezing air through the wetted cartridge (empty bottle) shows a broken fibre as a stream of bubbles, while an intact 0.1 um membrane holds air",
        "Physics", "Fluid mechanics", "Young-Laplace bubble point dP = 4 gamma / d: 0.1 um pore about 2,900 kPa ideal (real membranes lower, still far above 17 kPa); open 0.5 mm lumen 0.6 kPa; adult squeeze 17 kPa with the outlet in a cup of water reveals any opening above about 17 um",
        round(r["bubble_kpa"]["broken_lumen_500um"], 2), round(sq["adult"], 1), "kPa", rule="below")
c.cited("S14", "The air test, done with an adult squeeze, does not find round defects under about 17 um (slits under about 9 um), so it is a check for gross damage, not proof of pathogen performance",
        "Engineering and technology", "Sensing resolution", "Bubble point at the available squeeze: d = 4 gamma / dP = 17 um at 17 kPa (slit width 2 gamma / dP = 8.5 um); a weak user's 6 kPa finds only openings above about 50 um; cysts are 4 to 15 um, bacteria 0.1 to 5 um",
        "User guidance says 'stop using if bubbles stream'; never 'safe if no bubbles'. Production integrity test by the module maker (TI)", WITHIN)
c.cited("S15", "Wet fibres can be damaged by freezing without any change in flow, so the product carries a do-not-freeze-wet warning and a retire-after-freezing rule",
        "Physics", "Thermodynamics", "Water expands about 9 % on freezing; competitors report freezing as the main silent-failure cause (concept validation questions, item 17)",
        "No freeze claim; warning and pictogram; air test after suspected freezing; retire if frozen wet (HWP-VER-001 TF)", WITHIN)
c.cited("S16", "The housing stays far below the strength of printed polypropylene at the highest squeeze and a hard backflush",
        "Physics", "Strength of materials", "Hoop p r / t and the flat 4 mm end wall as a circular plate (1.24 p a2 / t2, simply supported); printed PP taken at 10 MPa (assumed, a third of moulded PP yield; layer strength lower)",
        f"Full squeeze: end wall {r['end_wall_mpa']['squeeze_max_ss']:.2f} MPa, factor 9. Backflush as instructed (collar end open): shell near 0 kPa. If the collar end were blocked at 179 kPa: hoop {r['hoop_mpa']['backflush_hard']:.2f} MPa but end wall {r['end_wall_mpa']['blocked_backflush_ss']:.1f} MPa, factor 2.1 against PR-028's 5 ({r['end_wall_t_for_factor5_mm']:.1f} mm wall needed; HWB-DEC-001 D8); burst test at TRL 4", PLAUSIBLE)
c.cited("S17", f"A 60 mL syringe backflush ({r['backflush_kpa']['gentle']:.0f} kPa gentle to {r['backflush_kpa']['hard']:.0f} kPa hard) stays inside the module's backwash limit",
        "Engineering and technology", "Standards practice", "p = F / syringe bore area (26.7 mm); the module maker's maximum backwash pressure is not yet known",
        f"To confirm from the supplier (HWB-DEC-001 C2), with the potting bond rated for {r['potting_push_n']:.0f} N at 179 kPa; the instruction is a gentle push; backflush runs with the carbon capsule removed so no fines or carbon are flushed into the fibres", PLAUSIBLE)
# ---- fixes under the standing instruction --------------------------------------------------------------------------
c.cited("S18", "Wet carbon downstream of the membrane (the briefed B1 layout) would grow bacteria on the clean side in warm storage and need a backflush bypass",
        "Biology", "Microbiology", "Carbon after the membrane can harbour microorganisms (Rev A specification section 05); wet carbon supports regrowth (concept validation questions, item 21)",
        "Failed as briefed, fixed: carbon moved to a dirty-side capsule upstream of the membrane, so the membrane is the last barrier and backflush never passes carbon", WITHIN, closed_by="HWB-DEC-001 F1")
c.cited("S19", "On release the squeezed bottle refills with air without unscrewing",
        "Physics", "Fluid mechanics", f"A wetted 0.1 um membrane blocks air up to its bubble point (about 2,900 kPa, S13), so air cannot return through the outlet; a dirty-side duckbill valve opens inward at about 0.5 kPa (assumed) and closes under squeeze; tipped, it sits under the bottle's water and needs about {r['duckbill_open_kpa']['tipped_full']:.1f} kPa of vacuum",
        "Failed as briefed (no air path), fixed with a duckbill valve in the collar (F2); the bottle is turned upright on release so the valve is in air and opens at about 0.5 kPa (F5); springback of a thin still-water bottle to confirm by test (TH)", PLAUSIBLE, closed_by="HWB-DEC-001 F2, F5")
c.claim("S20", "The B2 stand does not tip over when the full bottle hangs in it",
        "Physics", "Mechanics and statics", f"Tip angle atan(base radius / centre of gravity height) for the continuous base ring (not leg feet) with a full 1 L bottle; criterion 15 deg (assumed); base radius 65 mm gave 9.9 deg (failed), widened to 115 mm; a {r['b2_stability']['tip_force_n']:.1f} N side push at the centre of gravity still tips it, so the stand goes on a table away from children's reach",
        round(r["b2_stability"]["tip_deg"], 1), 15.0, "deg", rule="above", closed_by="HWB-DEC-001 F3")
c.cited("S21", "The inverted bottle of B2 drains without collapsing or locking",
        "Physics", "Fluid mechanics", f"Air must replace the water leaving the bottle; the wetted membrane blocks air (S13). The 4 x 0.8 vent tube has a 2.4 mm bore (Bond number {r['b2_vent']['bond']:.2f}, below 3.37), so water it takes in on filling stays as a plug that the bottle must purge",
        f"Failed as briefed, fixed with the vent tube (F4); the first purge needs about {r['b2_vent']['purge_kpa']:.1f} kPa of bottle vacuum against a {r['b2']['clean']['head_full_kpa']:.1f} kPa full head, so it works on paper with a slow first minute; to confirm by test (TH)", PLAUSIBLE, closed_by="HWB-DEC-001 F4")
# ---- hygiene, materials, fit, human factors ------------------------------------------------------------------------
c.cited("S22", f"With carbon on the dirty side, the clean side holds about {r['clean_wet_ml']:.0f} mL: {r['hold_up_clean_ml']:.1f} mL in the header, nipple and spout, which drains, and {r['lumen_ml']:.1f} mL in the lumens, which stays wet; a first flush after storage clears it",
        "Biology", "Microbiology", f"Biofilm grows where water stands on wetted surfaces; capillary rise in a 0.5 mm lumen is about {r['lumen_capillary_rise_mm']:.0f} mm, so the lumens never drain; bacteria can grow through 0.1 to 0.2 um membranes over days of wet storage; the outlet can be recontaminated by the mouth or hands",
        f"Refuted as first stated ('drains and dries', 5.7 mL), fixed: discard the first {r['first_flush_ml']:.0f} mL after any storage (F6); grow-through and regrowth to measure in storage cycles (HWP-VER-001 TE, TG); dust cover, pour into a cup for shared use", PLAUSIBLE, closed_by="HWB-DEC-001 F6")
c.cited("S23", "Every wetted material is from a family available in NSF/ANSI/CAN 61 grades: PP, EPDM or silicone, 316L, PVDF or PES fibres, polyurethane or epoxy potting, coconut GAC",
        "Chemistry", "Materials and polymer chemistry", "NSF/ANSI/CAN 61 and 372 set the contact-material references; printed prototype parts are not certified",
        "Extractables and leachables of the actual grades, potting (residual isocyanate or amine) and carbon fines and ash (TG); the first flush (F6) also clears fines; prototypes are used with known potable test water only", PLAUSIBLE)
c.claim("S24", "One collar fits both 28 mm PCO 1881 and PCO 1810 necks: the skirt clears the support ring of the shorter 1881 neck",
        "Engineering and technology", "Manufacturing tolerances", "Same thread diameter and pitch (about 27.4 mm, 2.7 mm); neck height about 17 mm (1881) and 21 mm (1810); skirt 15.5 mm below the lip with the compressed 1.5 mm gasket included (Kapy CAD, approximate); thread starts and tolerances from the ISBT drawings (C7)",
        round(r["neck"]["clear_1881"], 1), 1.0, "mm", rule="above")
c.cited("S25", "A printed adapter fits the collar to 38 mm two-start necks used on wide-mouth juice and dairy bottles",
        "Engineering and technology", "Manufacturing tolerances", "38 mm two-start finishes exist in several variants (Bericap 38 mm HF two-start; Petainer 38 mm two-start)",
        "Dimensions of the exact 38 mm finish to obtain from its drawing before the adapter is drawn (HWB-DEC-001 C4)", PLAUSIBLE)
c.order_of_magnitude("S26", f"The B1 cartridge weighs about 120 g dry and about {r['mass_b1_wet_g']:.0f} g wet",
        "Mathematics", "Orders of magnitude", claimed=120.0, estimate=r["mass_b1_dry_g"], unit="g",
        law="Model volumes x densities (PP 905, EPDM 1,150, 316L 7,950 kg/m3, fibres 30 % solid PVDF, GAC 490 kg/m3)")
c.cited("S27", f"A weak child can fill a 250 mL cup in about {250 / b1['child_10_11_weak']['clean']['q_ml_min'] * 60:.0f} s of squeezing with a clean module, in short squeezes",
        "Biology", "Ergonomics", f"Held grip of 40 % of maximum is assumed for 10 to 20 s at a time; the fouled module halves the flow ({250 / b1['child_10_11_weak']['fouled']['q_ml_min'] * 60:.0f} s); a litre takes a weak child {1000 / b1['child_10_11_weak']['clean']['q_ml_min']:.0f} min clean; household volumes are B2's job",
        "Persona trials with known potable water only (HWP-VER-001 TH); if children cannot sustain it, B2 gravity is the household mode", PLAUSIBLE)
# ---- rows added after the independent review of 2026-11-11 ----------------------------------------------------------
c.cited("S28", "Chlorine co-treatment works with the cartridge only if the water is dosed and left for solution D's full contact time before it is filtered; the filtered water then carries no residual",
        "Chemistry", "Physical chemistry", "Granular carbon removes free chlorine within seconds (S12), so the CT stops at the carbon; WHO and solution D set the dose and contact time (about 30 min) in the bottle; nothing downstream protects stored water",
        "Fixed: dose, wait, then filter; drink or use the filtered water the same day and do not store it (F7); the pictogram shows the order (PR-003)", WITHIN, closed_by="HWB-DEC-001 F7")
c.cited("S29", "The only dirty-to-clean routes, the header O-rings and the potting, are free of bypass at 53 % fibre packing",
        "Engineering and technology", "Manufacturing tolerances", f"Packing {r['packing'] * 100:.0f} % of the header bore (800 fibre ends of 0.8 mm in 31 mm); above about 50 % potting may not penetrate fully and leave voids; a gap under 17 um (slit 8.5 um) passes cysts and bacteria and is not seen by the air test (S14)",
        "Supplier to confirm packing, potting penetration and a production integrity test of every module (C1, F9); assembled-cartridge challenge (HWP-VER-001 TA, TB); about 300 U fibres (0.13 m2, flows about 25 % lower) if the maker asks for less", PLAUSIBLE)
c.cited("S30", "The bought fibres pass water at a few kPa",
        "Chemistry", "Materials and polymer chemistry", "Plain PVDF is hydrophobic: water enters a 0.1 um pore only far above 17 kPa; hydrophilised PVDF or PES passes water but can dewet if it dries out",
        "Fixed in the module request: hydrophilic PVDF or PES, shipped wet or with a wetting agent (F9); first-use priming and a backflush if first flow is low (F8)", PLAUSIBLE, closed_by="HWB-DEC-001 F8, F9")
c.cited("S31", "Every flow figure is for 20 C water; cold water gives about a quarter less",
        "Physics", "Fluid mechanics", "Flux and laminar losses scale with 1 / viscosity: 1.00 mPa s at 20 C, 1.31 at 10 C (0.77 x)",
        f"At 10 C: adult {c10['adult']['clean']['q_ml_min']:.0f} mL/min clean (under PR-004's 400), weak child {c10['child_10_11_weak']['clean']['q_ml_min']:.0f} and elderly woman {c10['elderly_f_weak']['clean']['q_ml_min']:.0f} (PR-005's 150); B2 {r['b2_10c']['fouled']['minutes_per_litre']:.1f} min per litre fouled. Rating temperature is HWB-DEC-001 D9", WITHIN)
c.cited("S32", "The upstream carbon bed keeps its flow in turbid water",
        "Physics", "Fluid mechanics", "The 150 um mesh passes silt, so the carbon bed works as a depth filter and cannot be backflushed (capsule out); Ergun viscous loss rises about 3.4 x as bed voids fall from 0.40 to 0.30",
        "Settle or cloth-filter turbid water first (HWP-SRC-001); replace the capsule when a backflush does not restore the flow (instructions, PR-016); clog rate to measure (HWP-VER-001 TE)", PLAUSIBLE)
c.cited("S33", "Air left on the dirty side does not blind the fibres",
        "Physics", "Fluid mechanics", "Air in the shell cannot cross the wetted membrane (S13) and rises against the flow through a wet 12 x 40 bed only above a capillary entry of about 1 to 2 kPa; at B2's 2.5 to 5 kPa head it may stay and cover fibres",
        "Fixed: prime at first use and after drying by a syringe backflush with the capsule out, which fills the shell from the fibres outward and pushes the air out of the open collar end (F8); to confirm by test (TC)", PLAUSIBLE, closed_by="HWB-DEC-001 F8")
state = c.write()
print("stem_check:", state)
