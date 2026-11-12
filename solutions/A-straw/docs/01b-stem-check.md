---
doc_id: HWA-STM-001
title: "Helpful Water A: filter straw STEM check"
project: "Helpful Water A: filter straw"
doc_type: STEM check
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First STEM check with the water checks of STANDARDS 25.6; five detail failures fixed under the standing instruction (HWA-DEC-001 F1 to F5); options A2 and A3 dropped
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Independent review recorded (13 hold, 10 weak, 4 refuted of 27 rows; 13 missed claims); permeability converted from 25 C to 20 C; S2 and S5 now fail with a fix proposed; rows S27 to S32 added; fixes F6 to F11 under the standing instruction; D10 to D12 proposed
---

# Helpful Water A: filter straw STEM check

Verdict: the hollow-fibre straw (option A1) sits within known science once its Rev A details are fixed, but it does not reach the Rev A flow target on paper. The supplier permeabilities are stated at 25 C; converted to 20 C, the full-bore bundle (about 220 fibres, 0.056 m2) gives **110 mL/min at 10 kPa with a 0.1 um fibre and 179 mL/min with a 0.2 um fibre**, upright with a shallow dip and a primed shell. 200 mL/min at 10 kPa needs a permeability of about 3,420 L/(m2 h bar) at 20 C, above the listed minimum of either grade, so S2 and S3 fail with fixes proposed to Amish (grade, a 245 mm body, or a lower target). The 400 mL/min users want needs 21 to 33 kPa (S5, a known shortfall). A child at 5 kPa draws 45 to 74 mL/min, so 1.5 L takes 20 to 33 minutes of sipping. These are clean-water upper bounds: turbid water fouls the fibres (S27), and air trapped in the dirty shell cuts the working area (S28). Of 32 rows for A1, 20 are within known science (eight of them closed by fixes), 9 are plausible and wait for TRL 4 evidence, and 3 fail with a fix that needs Amish. Options A2 (ceramic tube: about 10 mL/min) and A3 (copper and charcoal: seconds of contact where hours are needed) fail on their working principle and are dropped. An independent reviewer attacked every verdict on 2026-11-11; its findings and the changes are recorded below. `stem_check: open`. Method: STANDARDS sections 20 and 25.6; calculations in `docs/04-calcs/stem_check.py` and `docs/04-calcs/sizing.py` (HWA-CAL-001).

## Claims checked: option A1

Table 1. Claims, governing science and verdicts for the recommended option A1 (generated from `docs/04-calcs/stem_results.csv`). "Plausible, to confirm at TRL 3" is the kit's label; for this straw these rows can only be closed by the laboratory families of HWP-VER-001 at TRL 4, and stay open.

<!-- STM_TABLE -->
| # | Claim (number and unit) | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Rev A's 40 to 80 fibres (0.011 to 0.022 m2) cannot give 200 mL/min at 10 kPa with any listed grade; filling the bore with about 220 fibres raises the area 2.5 times | Physics | Fluid mechanics | Darcy flux J = Lp x TMP over the outer fibre area; SepraPor minima at 25 C converted to 20 C | 80 fibres x 110 mm: 46 mL/min (0.1 um) to 78 mL/min (0.2 um); 40 x 90 mm: 19 mL/min. Fixed by a full-bore bundle (0.056 m2, packing 48%, no central tube); the fix is necessary, not sufficient: the flow target then rests on the grade (S2, S3) | Within known science | HWA-DEC-001 F2; HWA-CAL-001 section 4 |
| S2 | Full-bore bundle with a 0.2 um MF fibre gives 200 mL/min at 10 kPa, clean water, 20 C, straw upright | Physics | Fluid mechanics | Stage sum: lift, intake, membrane, lumen and potting (Hagen-Poiseuille), grids, carbon (Ergun), pad (Darcy), mouth | 179 mL/min at 10 kPa; 200 mL/min needs 11.0 kPa, or Lp 3,419 L/(m2 h bar) at 20 C, above the grade's listed minimum (2,930). Dipped to the dip line and primed: 191; 245 mm body: 213. Uncertainties (pad, carbon, area basis) run mostly downward (independent review 2026-11-11) | Fails, fix proposed | Proposed, awaiting Amish (HWA-DEC-001 D2, D3) |
| S3 | With a 0.1 um MF fibre the straw meets the Rev A target of 200 mL/min at 10 kPa | Physics | Fluid mechanics | Same stage sum | 110 mL/min at 10 kPa; 200 mL/min needs 17.1 kPa. Fix options: 0.2 um grade, a 245 mm body, or a lower target; the grade is a safety trade-off | Fails, fix proposed | Proposed, awaiting Amish (HWA-DEC-001 D2, D3) |
| S4 | A true ultrafiltration fibre (100 kDa) cannot give usable flow at suction in this envelope, so the membrane must be a microfiltration grade | Physics | Fluid mechanics | SepraPor UF 100 kDa 215 to 550 L/(m2 h bar) at 25 C | 15 to 37 mL/min at 10 kPa. Fixed: PR-004 floor 1,800 L/(m2 h bar) at 25 C (1,600 at 20 C), the floor for usable flow (110 mL/min); PR-002 itself needs 3,419 at 20 C, which no listed grade guarantees (S2) | Within known science | HWA-DEC-001 F3 |
| S5 | At a comfortable 10 kPa sip the straw reaches the 400 mL/min below which straw users report dissatisfaction | Physics | Fluid mechanics | Stage sum; 400 mL/min threshold from the concept validation questions | 110 to 179 mL/min, under half; 400 mL/min needs 21 to 33 kPa. Not reachable in this envelope; carried as a known shortfall | Fails, fix proposed | Proposed, awaiting Amish (HWA-DEC-001 D3) |
| S6 | A child at 5 kPa draws 45 to 74 mL/min and an elderly user at 7 kPa 71 to 116 mL/min; 1.5 L takes a child 20 to 33 min of sipping | Biology | Human physiology and biomechanics | Persona suction assumed 5 and 7 kPa (STANDARDS 25.6 range 5 to 15 kPa); sustained sip suction of children and older adults is to assess (Wertsen and Stenberg 2017 measured adult lip force only) | Stage sum; at 5 C the child needs 31 to 50 min per 1.5 L; tilting to 50 mm lift gives 58 to 96 mL/min; fatigue and lip seal on the 10 mm tip to test (TH) | Plausible, to confirm at TRL 3 | Open |
| S7 | At 200 mL/min the carbon bed costs about 1 kPa of suction | Physics | Fluid mechanics | Ergun, 12 x 40 GAC, sphericity 0.75, voidage 0.42 (assumed); range 0.5 to 2.0 kPa for 0.6 to 0.84 mm and voidage 0.38 to 0.45 | claimed 1 kPa, estimate 0.689 kPa (ratio 1.45) | Within known science | HWA-CAL-001 section 4 (membrane 7.3, lift 1.5, pad 0.9, lumen 0.6 kPa) |
| S8 | Lumen and potting pressure drop is small beside the membrane (single open end, 0.5 mm lumen, 102 mm active, 10 mm potting) | Physics | Fluid mechanics | Hagen-Poiseuille with flow rising along the fibre, full flow through the potting | 0.604 kPa <= 1 kPa | Within known science | HWA-CAL-001 section 4 |
| S9 | Upright with a shallow dip (water surface at 50 mm) the 155 mm lift to the mouth costs 1.5 kPa; at the dip line 0.9 kPa | Physics | Fluid mechanics | Hydrostatics rho g h; the flow cases assume a primed shell (S28) | 1.52 kPa <= 1.6 kPa | Within known science | HWA-CAL-001 section 4 |
| S10 | Water at 5 C flows about a third slower than at 20 C | Physics | Fluid mechanics | Viscosity 1.52 against 1.00 mPa s; flux falls as 1/viscosity, lift does not | claimed 0.66 ratio, estimate 0.667 ratio (ratio 0.99) | Within known science | HWA-CAL-001 section 4 |
| S11 | A microfiltration fibre with a supplier-validated absolute rating is designed to retain most bacteria and protozoan cysts; removal is claimed only from laboratory log reductions, and thin bacteria such as Leptospira are not claimed | Biology | Microbiology | Size exclusion; STANDARDS 25.6 organism sizes; bacterial retention challenge with Brevundimonas diminuta (0.3 to 0.4 um, ASTM F838 method); Leptospira about 0.1 um across passes 0.2 um membranes (Standard Methods 9260 I) | Most bacteria 0.5 to 5 um, cysts 3 to 15 um; but the smallest relevant bacteria are 0.1 to 0.4 um, below a 0.2 um nominal label. Fixed: PR-001 asks for an absolute rating with a B. diminuta challenge report; Leptospira added to the exclusions unless tested (TA, TB) | Within known science | HWA-DEC-001 F10; PR-001, PR-006 |
| S12 | Viruses (0.02 to 0.3 um) are not reliably retained, so no virus claim is made and the product says so | Biology | Microbiology | Size exclusion; HWP-CLM-001 | Enteric viruses 0.027 to 0.09 um, below the 0.1 to 0.2 um rating | Within known science | HWP-CLM-001; PR-008 |
| S13 | The 250 um mesh stops grit and debris only, not silt, microbes or chemicals | Physics | Fluid mechanics | Sieving; Rev A item 2 | Silt 2 to 63 um and clay under 2 um pass a 250 um aperture; the membrane is the fouling point (S27) | Within known science | PR-013 |
| S14 | The 16 x 20 mm carbon bed holds about 2 g, not 5 g | Chemistry | Physical chemistry | Bed volume 4.0 mL x apparent density 0.48 to 0.50 g/mL (12 x 40 coconut GAC sheet) | claimed 2 g, estimate 1.93 g (ratio 1.04) | Within known science | HWA-CAL-001 section 5 |
| S15 | With an empty-bed contact time of 1.2 s at 200 mL/min the carbon is intended to reduce free chlorine taste only | Chemistry | Physical chemistry | Chlorine reduction on GAC is fast; straws with a few grams of carbon are sold as NSF/ANSI 42 for chlorine (retailer listing, not verified against the NSF database); organics and odours need minutes | EBCT 0.6 to 2.4 s across 100 to 400 mL/min at about 60 m/h superficial velocity through a 20 mm bed, fast and shallow even for dechlorination; claim limited to chlorine taste, measured under NSF/ANSI 42 before any claim | Plausible, to confirm at TRL 3 | Open |
| S16 | Carbon life is set by a measured breakthrough curve, not assumed | Chemistry | Analytical chemistry | Rev A section 07 (carbon life) | Replacement interval to be set from HWP-VER-001 TG; 500 L is a planning assumption only | Within known science | PR-015 |
| S17 | AS568-018 O-rings (18.77 x 1.78 mm) in male glands with a 19.3 mm floor seal a 22.0 mm bore | Engineering and technology | Manufacturing tolerances | Static radial gland practice: squeeze 15 to 30 %, stretch under 5 %, fill under 85 % | Nominal squeeze 24%, stretch 2.8%, fill 77%, radial gap 0.10 mm. Tolerance stack as printed (+-0.1 mm) 15% to 33%, outside the range; fixed: bores and gland floors reamed or turned to +-0.05 mm, 18% to 30%. The Rev A 20 x 2 mm ring (outside 24 mm) cannot enter a 22 mm bore | Within known science | HWA-DEC-001 F1, F9 |
| S18 | Backflush water enters the clean header and leaves through the fibre walls and the intake without passing the carbon | Physics | Fluid mechanics | Continuity: with the mouthpiece cap plugging the 5 mm bore the carbon branch is dead-ended | Socket on the header at 153 mm, below the carbon cartridge; the cap plug must be fitted first (instruction and pictogram); with the cap off the flush runs out of the mouthpiece instead and the fibres are not cleaned | Within known science | HWA-DEC-001 F4 |
| S19 | A 20 mL syringe at 50 kPa backflushes at about 556 to 741 mL/min with a 16 N thumb force | Physics | Fluid mechanics | Membrane resistance in reverse plus the luer tip and 2 mm passage (1.5 velocity heads each); force = pressure x plunger area (20 mm bore, assumed) | 20 mL in about 1.6 to 2.2 s; 20 mL is about 0.35 L/m2, so the number of strokes is set in TE; the syringe is filled with water already treated, never from the source (F11) | Plausible, to confirm at TRL 3 | Open |
| S20 | A plunger-hold air check through the backflush socket shows a broken fibre or a failed collar seal (gross defects only) | Physics | Fluid mechanics | Young-Laplace: a wetted 0.2 um pore holds air to hundreds of kPa; an open 0.5 mm lumen passes air above 0.6 kPa; isothermal compression of the syringe, header and lumen gas | The water in the lumens (4.8 mL) and header (2.3 mL) leaves first, so 51 kPa is reached at the 6 mL mark (fix F7, not 13.3 mL); it opens defects of 5.6 um and larger, not bacterial-size ones; pass is a plunger that holds; bubbles show only inverted; dry spots give a false fail; re-prime after (TA, TF) | Plausible, to confirm at TRL 3 | Open |
| S21 | Freezing when wet can crack fibres and potting without changing flow, so the straw is not freeze tolerant and says so | Physics | Thermodynamics | Water expands about 9 % on freezing | No freeze claim; on-product warning; a straw that may have frozen is replaced, since the air check finds gross defects only (S20) | Within known science | PR-016 |
| S22 | Bacteria can grow on the carbon and in the clean header during wet storage and reach the user directly, since the carbon sits after the barrier and removes any chlorine residual | Biology | Microbiology | Heterotrophic growth on GAC is well known; Rev A section 05 | Design: drainable, capped, carbon replaced by volume; saliva and blow-back reach the carbon from the mouth side (D9); regrowth after wet storage to measure (TG) | Plausible, to confirm at TRL 3 | Open |
| S23 | Every wetted material, the membrane and potting included, is available in a grade listed for drinking-water contact | Chemistry | Materials and polymer chemistry | NSF/ANSI/CAN 61 (extraction); 372 for lead in metal parts only (HWP-REG-001 W7) | PP, EPDM, silicone, 316L and GAC grades exist; the membrane (PES or PVDF with PVP and a glycerine wetting agent, residual solvent) and the potting (polyurethane or epoxy) need the module maker's listing; a first-flush volume before first use (F11); printed prototypes see known potable test water only and nobody drinks from them | Plausible, to confirm at TRL 3 | Open |
| S24 | The straw is under 25 cm long and 3 cm across (kit compatible) | Engineering and technology | Standards practice | Concept validation questions, item 39 | 29.6 mm across <= 30 mm across | Within known science | HWA-CAL-001 section 9 (length 205 mm; 0.4 mm margin across the plug) |
| S25 | The straw weighs under 100 g dry | Mathematics | Units and dimensional analysis | Model volumes x densities (cad_parts.MATERIALS) | 66.2 g <= 100 g | Within known science | HWA-CAL-001 section 9 (full of water about 107 g) |
| S26 | About 220 fibres of 0.8 mm fill a 17.2 mm bundle at about 48 % packing | Mathematics | Orders of magnitude | Fibre count = packing x (bundle / fibre diameter)^2 | claimed 220 fibres, estimate 222 fibres (ratio 0.99) | Within known science | HWA-CAL-001 section 2 |
| S27 | Clean-water flows are upper bounds: turbid water builds a cake on the fibres and the flow falls between backflushes | Physics | Fluid mechanics | Cake filtration R = Rm + alpha m / A; design flux 213 L/(m2 h) against tens of L/(m2 h) sustained in surface-water plants; 50 mg/L solids, alpha 1e13 to 1e14 m/kg (assumed A13) | 0.2 um at 10 kPa after 1, 5 and 20 L: 169, 140, 85 to 116, 48, 15 mL/min. Settle or cloth-strain cloudy water; backflush interval in litres from TE | Plausible, to confirm at TRL 3 | Open |
| S28 | Once primed, the dirty shell stays full of water while the intake is under water; air trapped in it cuts the working membrane area | Physics | Fluid mechanics | The shell is closed at the top by the potting and wetted fibres hold air to their bubble point, so trapped air sits above the outside water level (hydrostatics; Young-Laplace) | At the dip line, primed 117 to 191 mL/min; with the shell drained above the outside level (71% wetted) 86 to 144; shallow dip unprimed 15 to 26. Dry fibres prime on first use; between uses the intake cover keeps the shell full; a re-prime method or vent to test (TC, D10). Degassing under suction may add bubbles | Plausible, to confirm at TRL 3 | Open |
| S29 | With the socket plug out and the socket under water, dirty water bypasses the membrane at more than the filtered flow, and the user cannot tell | Physics | Fluid mechanics | Orifice flow through the 2 mm socket passage at 10 kPa | About 506 mL/min, 2.8 to 4.6 times the membrane flow; controls: socket 43 mm above the dip line, tethered plug, dip-line pictogram; a self-closing socket proposed (D12) | Within known science | PR-028; HWA-DEC-001 D12 |
| S30 | A firm push on the syringe stays within the membrane's reverse-pressure rating | Physics | Fluid mechanics | Pressure = force / plunger area; SepraPor lists a maximum TMP of 1.0 bar (0.2 um) and 1.4 bar (0.1 um) and gives no backflush rating | 60 N on a 20 mm plunger gives 191 kPa static, about twice the 0.2 um rating; the module's reverse rating is to confirm (C2) and a pressure limit is proposed (D11) | Plausible, to confirm at TRL 3 | Open |
| S31 | The straw does no disinfection; with a chlorine co-treatment the contact time is completed in the container before sipping, and the carbon then removes the residual | Chemistry | Physical chemistry | Free chlorine passes MF membranes; GAC removes it in about a second (S15); CT needs minutes (HWP-CLM-001) | EBCT 1.2 s against a contact time of 30 min; instruction: dose, wait, then drink through the straw; the membrane's free-chlorine tolerance (ppm h) to confirm (C2) | Within known science | HWP-CLM-001; HWA-DEC-001 F11 |
| S32 | The carbon fines pad wets and passes water at the sip pressure | Chemistry | Physical chemistry | Young-Laplace water entry pressure 4 gamma cos(theta) / d for a 20 um pore | Untreated non-woven PP (contact angle about 100 deg) needs about 2.5 kPa to wet, a quarter of the sip; fixed: hydrophilic-treated pad (F6); its permeability is still assumed (C6) | Within known science | HWA-DEC-001 F6 |
<!-- /STM_TABLE -->

## Water checks of STANDARDS 25.6

| Check | Where | Result |
| --- | --- | --- |
| Membrane flux against the pressure available | S1 to S4, S27 | Flux decides the design: at 200 mL/min the membrane takes 7.3 kPa with a 0.2 um fibre and 13.3 kPa with a 0.1 um fibre, at permeabilities converted from 25 C to 20 C. Design flux 213 L/(m2 h) clean; on turbid water the flow falls between backflushes (S27) |
| Pressure drop per stage | S7 to S9, CAL section 4 | At 200 mL/min: lift 1.5 (0.9 at the dip line), membrane 7.3 to 13.3, pad 0.9 (assumed), carbon 0.7 (0.5 to 2.0), lumens and potting 0.6; grids, screen, mesh and mouth bore under 0.1 kPa together |
| Flow at the persona efforts | S5, S6 | Child (5 kPa) 45 to 74 mL/min; elderly (7 kPa) 71 to 116; 10 kPa 110 to 179; adult 15 kPa 174 to 281 mL/min; a third less at 5 C; 1.5 L takes a child 20 to 33 min (31 to 50 min at 5 C) |
| Pore or MWCO against organism size | S11, S12 | Most bacteria 0.5 to 5 um and cysts 3 to 15 um, but thin bacteria (Leptospira, about 0.1 um across) pass 0.2 um membranes and are not claimed; absolute rating with a *B. diminuta* challenge required; viruses 0.027 to 0.3 um not claimed |
| Carbon contact time and bed mass | S14 to S16 | 4.0 mL bed, 1.9 to 2.0 g; EBCT 1.2 s at 200 mL/min; claim limited to chlorine taste after measurement |
| Disinfection dose and CT | S31 | The straw does no disinfection; a chlorine co-treatment (solution D or a tablet) completes its contact time in the container before the water is drunk through the straw, whose carbon removes the residual |
| Integrity and silent failure | S17, S18, S20, S29, S21 | Two O-rings in series at the only clean/dirty seal, reamed glands; plunger-hold air check finds gross defects (5.6 um and larger) only; an open socket under water bypasses at about 506 mL/min (dip line, tethered plug; D12); freezing warned |
| Biofilm downstream of the membrane | S22 | Carbon and header sit after the barrier with no residual; drain, dry, cap, replace carbon by volume; saliva and blow-back reach the carbon; regrowth to measure (TG) |
| Materials leaching | S23 | Listed grades exist for PP, EPDM, silicone, 316L and GAC; membrane and potting need the maker's listing; first flush before first use; printed prototypes see known potable test water only |
| Freezing | S21 | Not freeze tolerant; warning on the product; a straw that may have frozen is replaced |
| Priming and air (added) | S28, S32 | Trapped shell air leaves only the fibre length below the outside water working (71 % at the dip line); hydrophilic fines pad, since untreated PP needs 2.5 kPa to wet |

## Fields not relevant

Every field has at least one row. Within Physics, electromagnetism, optics and nuclear branches are not relevant (no power, light or radiation source). Within Chemistry, electrochemistry is not relevant (no cells, no electrolytic treatment). Disinfection chemistry is not relevant to A1 (no disinfectant).

## Concept options

- **A1 hollow-fibre straw with backflush:** no Fails row; three failed details (S2 and S3, the flow target against the membrane grade; S5, the 400 mL/min users want) await Amish. Carried forward as the recommendation.
- **A2 ceramic tube straw:** **Fails** on flow (X1): a ceramic tube that fits the bore passes about 10 mL/min at 10 kPa, one twentieth of the target, even with a thin 0.2 um layer. Dropped.
- **A3 copper and charcoal straw:** **Fails** on its working principle (X3 to X5): a sip gives copper about 5 s of contact where copper pots need about 16 h, charcoal is not a size barrier, and neither touches *Cryptosporidium*. Dropped, as the Rev A specification had already removed copper.

Table 2. Dropped options (generated from `docs/04-calcs/stem_results_dropped.csv`).

<!-- STM_DROPPED -->
| # | Claim (number and unit) | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X1 | A2: a sintered ceramic tube 17 mm x 106 mm gives 200 mL/min at 10 kPa | Physics | Fluid mechanics | Radial Darcy flow; ceramic permeability from pot filters (1 to 3 L/h, Akvopedia; 556 L/(m2 h bar) at 15 mm); best case thin 0.2 um layer 10 mL/min | claimed 200 mL/min, estimate 10.2 mL/min (ratio 19.69) | Fails (option dropped) | Open |
| X2 | A2: a 0.2 to 1 um ceramic retains cysts and reduces bacteria | Biology | Microbiology | Size exclusion; pot filters reduce bacteria by about 2 log with silver (Akvopedia) | A 1 um rating does not retain 0.3 to 0.5 um bacteria; holds only as reduction, and the option is dropped on X1 | Within known science | Open |
| X3 | A3: copper in the straw inactivates bacteria during a sip | Biology | Microbiology | Copper pots reduced bacteria over 16 h storage (Sudha et al. 2012); wet copper contact killing takes minutes to hours (Grass et al. 2011) | claimed 5.13179 s, estimate 5.76e+04 s (ratio 0.00) | Fails (option dropped) | Open |
| X4 | A3: charcoal removes bacteria and protozoa | Biology | Microbiology | Granular carbon is an adsorbent, not a size barrier: water passes between 0.4 to 1.7 mm granules | Gaps between granules are 100 times a bacterium; carbon can also grow bacteria | Fails (option dropped) | Open |
| X5 | A3: copper and charcoal address Cryptosporidium | Biology | Microbiology | Cryptosporidium oocysts resist chemical disinfectants (chlorine; HWP-CLM-001) | No mechanism in seconds | Fails (option dropped) | Open |
| X6 | A3: copper released in a sip stays below the 1.3 mg/L action level | Chemistry | Environmental and atmospheric chemistry | EPA Lead and Copper Rule action level (Rev A R2) | Likely low in a flowing sip; the first draw after wet storage (about 9 dm2 of copper in 17 mL) may exceed it, release rate to assess; not the reason the option fails | Plausible, to confirm at TRL 3 | Open |
<!-- /STM_DROPPED -->

## Fixes made under the standing instruction (2026-10-23)

Each fix keeps the working principle (outside-in hollow fibre, carbon polish, backflush) and is recorded in HWA-DEC-001 and HWA-DDR-003.

- **F1 O-rings.** Rev A's 20 x 2 mm rings have a 24 mm outside diameter and cannot enter a 22 mm bore. Fixed: AS568-018 (18.77 x 1.78 mm) EPDM in male glands with a 19.3 mm floor and 2.4 mm width: 24 % squeeze, 2.8 % stretch, 77 % fill (S17).
- **F2 Fibre count and termination.** Rev A's 40 to 80 fibres give 0.011 to 0.022 m2. Fixed: the bundle fills the bore, about 220 fibres in a 17.2 mm bundle (48 % packing, 0.056 m2), single-ended: far ends closed in the bottom potting, lumens open into a clean header above the top potting. The central permeate tube is dropped, since it took bore area and a two-ended header adds a second potting seal (S1).
- **F3 Membrane permeability.** A 100 kDa ultrafiltration fibre gives 17 to 42 mL/min at 10 kPa. Fixed: PR-004 sets a clean-water permeability of at least 1,800 L/(m2 h bar) at 20 C, which is a microfiltration grade (S4). Which grade, 0.1 or 0.2 um, is a safety trade-off for Amish (D2).
- **F4 Backflush routing.** Fixed: the socket enters the clean header below the carbon; the mouthpiece cap carries a plug that dead-ends the carbon during backflush, so backflush water never passes the carbon (S18).
- **F5 Carbon mass.** Rev A's "5 g" cannot fit a 16 x 20 mm bed. Fixed in the BOM and PRS: 1.9 to 2.0 g of 12 x 40 coconut-shell GAC from its apparent density (S14).

Fixes F6 to F11 follow the independent review below; each keeps the working principle.

- **F6 Hydrophilic fines pad.** Untreated non-woven polypropylene needs about 2.5 kPa to wet through 20 um pores. Fixed: BOM 10 is a permanently hydrophilic-treated pad (S32).
- **F7 Air check restated.** The 7.1 mL of water in the lumens and header must leave before air reaches the fibre walls, so 51 kPa is reached at the 6 mL plunger mark, not 13.3 mL. The check is now a plunger-hold test (push to the 6 mL mark, hold 10 s; a plunger that keeps moving fails), described as a gross-defect check (5.6 um and larger) with a re-prime afterwards (S20, PR-012).
- **F8 Priming and immersion stated.** Flow figures now say primed or not; the instruction keeps the intake cover on between uses so the shell stays full, and the flow at the dip line is given (S28). A vent or re-prime method is D10.
- **F9 Gland tolerance.** As printed (+-0.1 mm) the squeeze runs 15 to 33 %; bores and gland floors are reamed or turned to +-0.05 mm, giving 18 to 30 % (S17).
- **F10 Organism size and rating.** PR-001 asks for an absolute rating validated by a *Brevundimonas diminuta* retention challenge; Leptospira and other thin bacteria join the stated exclusions unless tested (S11).
- **F11 Clean water for the syringe, first flush and co-treatment order.** The syringe is filled only with water already treated (boiled, tablet-treated or bottled), never from the source; the first 3 x 40 mL through a new straw are discarded; with a chlorine co-treatment the contact time is completed in the container first (S19, S23, S31).

## Independent review

**Method.** On 2026-11-11 a second agent (Claude, run as a separate `claude -p` process with no access to this document's prose, the decisions or the review note) was given only the claims table (`docs/04-calcs/stem_results.csv`), `stem_check.py`, `sizing.py` with its results, the PARAMS in `cad/src/model.py`, `bom/bom.csv` and the cited sources. It was asked to refute every "Within known science" and "Plausible" verdict, defaulting to refuted or weak when unsure, to recompute every number and unit, and to look for claims the check missed against the water checks of STANDARDS 25.6. The author then checked each finding with numbers before acting; the reviewer's report is model output, not evidence.

**Result.** Of the 27 rows then marked Within or Plausible (S1 to S26 less S3, and X2, X6), **13 hold, 10 are weak and 4 are refuted** (S2, S5, S11, X6). It also found **13 missed claims** (M1 to M13). It reproduced every stage drop in `sizing.py` to within 1 Pa and found the formulas sound; the errors were in inputs, scenarios and framing. On checking, the author agrees with every finding except X6, which is weak rather than refuted (the copper release rate it used is assumed and the option is already dropped). The previous author pass had changed S5, the lift and the pad; that pass is superseded by this review.

Table 3. Independent review findings and changes.

| Row | Finding (verified) | Change made |
| --- | --- | --- |
| All flow rows | Weak: the SepraPor permeabilities are normalised to 25 C, not 20 C (Meissner datasheet, checked 2026-11-11); at 20 C they are 0.888 times lower | `sizing.py` converts them; flow at 10 kPa 110 to 179 mL/min (was 122 to 197); every document updated |
| S2 | Refuted: 179 mL/min at 10 kPa, below 200; 200 needs 11.0 kPa or a permeability of 3,420 at 20 C, above the 0.2 um minimum (2,930); the uncertainties run mostly downward | Verdict "Fails, fix proposed"; to Amish with S3 (D2, D3) |
| S5 | Refuted: a "stays below 400 mL/min" rule passed trivially while the design reaches under half of it | Reworded as the claim the users want; "Fails, fix proposed"; a known shortfall for Amish (D3) |
| S11 | Refuted: the smallest relevant bacteria are 0.1 to 0.4 um (Leptospira about 0.1 um across passes 0.2 um membranes; *B. diminuta* 0.3 to 0.4 um), not 0.5 um | F10: absolute rating with a *B. diminuta* challenge in PR-001; Leptospira in the exclusions |
| S1, S4 | Weak: the area fix and the 1,800 floor are necessary but do not deliver 200 mL/min | Reworded: the floor is for usable flow; PR-002 needs 3,420 at 20 C (PR-004 note; D2) |
| S6 | Weak: persona suctions are assumptions; the cited paper measured adult lip force only; sip time and cold water missing (M8) | Source marked "to assess"; minutes per 1.5 L and the 5 C figure added |
| S9 | Weak: the 155 mm lift sits the water 12 mm above the bottom potting; with air in the shell only 12 % of the fibre would work (M2) | Lift tied to immersion; new row S28 and fix F8; D10 for a vent |
| S15 | Weak: the NSF/ANSI 42 straw listing is a retailer page, not verified; the bed is fast and shallow (60 m/h) | Source qualified; claim stays open |
| S19 | Weak: the luer tip and 2 mm passage were left out; grades mixed; 20 mL is only 0.35 L/m2 | 556 to 741 mL/min with port losses; strokes set in TE; clean syringe water (F11) |
| S20 | Weak: lumen and header water (7.1 mL) leaves first, so 51 kPa is at the 6 mL mark; bubbles rise into the shell, not to the intake; 51 kPa finds defects of 5.6 um and larger only; dry spots false-fail | F7: plunger-hold check to the 6 mL mark, gross-defect wording, re-prime after; PR-012 and the build plan updated |
| S22 | Weak: the mechanism was wrong (chlorine passes MF membranes; the carbon removes it); mouth back-contamination missing (M6) | Reworded |
| S23 | Weak: membrane (PVP, glycerine, solvent) and potting omitted; NSF/ANSI 372 is for lead in metal parts | Row widened; first flush (F11); C5 extended |
| X2 | Weak: a 1 um ceramic reduces bacteria by about 2 log; it does not retain them | Reworded (option dropped) |
| X6 | Refuted by the reviewer for a stagnant first draw; the author judges it weak (assumed release rate) | Reworded (option dropped) |
| S7, S8, S17, S18, S21, S24, S25 | Hold, with notes: carbon range 0.5 to 2.0 kPa; 10 mm potting adds 0.1 kPa; O-ring tolerance stack 15 to 33 %; cap forgotten in backflush; frozen straw replaced; 0.4 mm margin across; 106 g full of water | Notes added; F9 reamed glands; lumen drop now 0.6 kPa; S25 states dry mass |
| S10, S12, S13, S14, S16, S26 | Hold | Unchanged apart from figures |
| M1 | Missed: clean-water flux at 213 L/(m2 h) ignores fouling | New row S27 (cake model, assumption A13); TE sets the backflush interval |
| M2, M12 | Missed: air trapped in the shell, and degassing under suction | New row S28; F8; D10 |
| M3 | Missed: nominal against absolute rating | Into S11 (F10) |
| M4 | Missed: open socket under water bypasses at about 506 mL/min, silently; syringe filled from the source inoculates the clean side | New row S29; F11; D12 self-closing socket |
| M5 | Missed: a missing collar O-ring passes about 228 mL/min | Already two in series (PR-007); the assembly air check catches it; noted in S20 |
| M6, M7 | Missed: back-contamination; membrane and potting leaching | Into S22 and S23 |
| M8 | Missed: persona fatigue and sip time | Into S6 |
| M9 | Missed: hydrophobic fines pad | New row S32; F6 |
| M10 | Missed: chlorine CT and order of use | New row S31; F11 |
| M11 | Missed: a 60 N push gives 191 kPa, about twice the 0.2 um TMP rating | New row S30; C2 extended; D11 pressure limit |
| M13 | Missed: full of water the straw weighs about 106 g | S25 states the dry and full masses; PR-027 is dry |

**What changed in numbers.** Flow at 10 kPa, upright, primed: 110 to 179 mL/min (was 122 to 197); at the dip line, primed: 117 to 191. Child at 5 kPa: 45 to 74 (was 50 to 82). Suction for 200 mL/min: 11.0 to 17.1 kPa; for 400 mL/min: 21 to 33 kPa. Backflush: 556 to 741 mL/min at 50 kPa. Air check: plunger to the 6 mL mark. BOM total unchanged at USD 17.46 (specification changes only).

## Sources

All checked 2026-11-11 unless stated.

- Meissner. "SepraPor hollow fiber microfiltration and ultrafiltration membranes" (clean water flux by pore rating, normalised to 25 C; maximum TMP 1.0 bar for 0.2 um and 1.4 bar for 0.1 um; area basis not stated). https://www.meissner.com/wp-content/uploads/Seprapor_green_doc_2026.pdf.
- Meissner. "SepraPor hollow fiber filter cartridges." https://www.meissner.com/wp-content/uploads/seprapor-hollow-fiber-filter-cartridges.pdf.
- Standard Methods 9260 I, *Leptospira* (NEMI summary). https://nemi.gov/methods/method_summary/9670.
- Leptospira passage through 0.22 um filters (PMC273532). https://pmc.ncbi.nlm.nih.gov/articles/PMC273532.
- Prepol. "O-ring sizes AS 568." https://www.prepol.com/documents/o-ring-sizes-as-568.
- Envirosupply. "12 x 40 coconut shell activated carbon specification sheet." https://cdn.shopify.com/s/files/1/0018/8193/1811/files/12x40CoconutShell_SpecSheet.pdf.
- Wertsén, M., and M. Stenberg. "Measuring Lip Force by Oral Screens. Part 2: The Importance of Screen Design, Instruction and Suction." *Clinical and Experimental Dental Research* 3, no. 5 (2017): 191 to 197. https://research.chalmers.se/publication/253532/file/253532_Fulltext.pdf.
- Akvopedia. "Ceramic pot filter." https://akvopedia.org/wiki/Ceramic_filter.
- Sudha, V. B. P., et al. "Storing Drinking-Water in Copper Pots Kills Contaminating Diarrhoeagenic Bacteria." *Journal of Health, Population and Nutrition* 30, no. 1 (2012). https://pubmed.ncbi.nlm.nih.gov/22524115/.
- Grass, G., C. Rensing, and M. Solioz. "Metallic Copper as an Antimicrobial Surface." *Applied and Environmental Microbiology* 77, no. 5 (2011). https://pmc.ncbi.nlm.nih.gov/articles/PMC3067274.
- Google Patents. "US8852439B2, Drinking straw with hollow fibre liquid filter." https://patents.google.com/patent/US8852439B2/en.
- Membrane Solutions S2 straw listing (NSF/ANSI 42 and 372). https://www.desertcart.uy/products/246879908-membrane-solutions-water-filter-straw-s2-nsf-ansi-42-372.md.
- Helpful Engineering. Portable Freshwater Filter Straw: Component Specifications, Rev A, 2026-10-14 (internal), with its references R1 to R13; Concept Validation Questions, 2026 (internal); Project Viability Shortlist Analysis (internal).
- Program documents HWP-PRB-001, HWP-SRC-001, HWP-CLM-001, HWP-REG-001, HWP-VER-001, HWP-FTO-001.


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
