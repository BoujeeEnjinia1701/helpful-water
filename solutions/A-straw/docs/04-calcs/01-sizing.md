---
doc_id: HWA-CAL-001
title: "Helpful Water A: filter straw sizing and first-principles checks"
project: "Helpful Water A: filter straw"
doc_type: Calculation note
version: "0.3"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First TRL 3 calculation note for option A1 (recommended, awaiting Amish), with checks of options A2 and A3
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: After the independent STEM review, permeabilities converted from 25 C to 20 C; potting drop, immersion and priming, fouling, persona minutes, port losses in backflush, air-check plunger mark, overpressure, seal tolerance stack, socket bypass and wet mass added (assumption A13)
  - version: "0.3"
    date: 2026-11-11
    author: Amish Chadha
    change: Decisions recorded as Amish's (all pending decisions settled on their recommendations, 2026-11-11)

---

# Helpful Water A: filter straw sizing and first-principles checks

The membrane decides the straw. The datasheet permeabilities are normalised to 25 C; at 20 C they are 0.89 times lower. At 200 mL/min the fibre walls then take 7.3 kPa of suction with a 0.2 um microfiltration fibre and 13.3 kPa with a 0.1 um fibre, against 1.5 kPa to lift the water to the mouth and about 2.3 kPa for everything else together. With the bundle filling the bore (about 220 fibres, 0.056 m2) the straw delivers **110 to 179 mL/min at 10 kPa**, **45 to 74 mL/min for a child at 5 kPa** and 71 to 116 mL/min for an elderly user at 7 kPa, all a third lower in water at 5 C; a child needs 20 to 33 minutes of sipping for 1.5 L. 200 mL/min at 10 kPa needs a permeability of about 3,420 L/(m2 h bar) at 20 C, more than either grade's listed minimum. The 400 mL/min that straw users want needs 21 to 33 kPa. These are clean-water figures with the dirty shell primed: turbid water fouls the fibres (section 4.3) and air trapped in the shell cuts the working area (section 4.2). The carbon bed holds 1.9 to 2.0 g with a 1.2 s contact time at 200 mL/min. The straw is 205 mm long, 29.6 mm across at the backflush plug and 66 g dry (about 106 g full of water); prototype parts cost USD 17.46 against the USD 25 value-engineering target, and the cost per litre over its life is about USD 0.011 as a prototype and USD 0.002 at scale, against USD 0.02 for chlorine tablets. Everything is a paper estimate: nothing has been built or measured. Script: `docs/04-calcs/sizing.py` (writes `sizing_results.json`).

## 1. Assumptions

| # | Assumption | Basis | Effect if wrong |
| --- | --- | --- | --- |
| A1 | A 0.8/0.5 mm straw fibre has the clean-water permeability per area of the datasheet fibres: 0.2 um at least 3,300, 0.1 um at least 1,800, 100 kDa 215 to 550 L/(m2 h bar), normalised to 25 C and converted to 20 C by the viscosity ratio (0.888); per outer area | Meissner SepraPor datasheet (minimum values for MF; area basis not stated), checked 2026-11-11 | Flow scales almost in proportion (C3); if the datasheet is per lumen area the outer-area value could be lower |
| A2 | Persona suction for a sustained sip: child 5 kPa, elderly 7 kPa, Rev A test point 10 kPa, adult 15 kPa | STANDARDS 25.6 range 5 to 15 kPa; to assess: the only source found (Wertsén and Stenberg 2017) measured adult lip force on oral screens, not sustained sip suction of children or older adults | Persona flows; to measure (TH) |
| A3 | Straw upright, mouth 155 mm above the water surface (shallow dip, shell primed); 95 mm at the dip line; 50 mm when tilted to drink from a cup | Geometry | 1.5 kPa against 0.9 and 0.5 kPa; an unprimed shell is section 4.2 |
| A4 | Mesh 35 % open, screens 30 % open; orifice coefficient 0.6 | Typical woven mesh | Negligible |
| A5 | Carbon: 12 x 40 mesh (0.42 to 1.68 mm, mean 0.84 mm), sphericity 0.75, bed voidage 0.42 | Envirosupply sheet; typical GAC | Ergun drop scales with the square of 1/size |
| A6 | Fines pad Darcy permeability 3 x 10^-11 m2, 1.6 mm thick, hydrophilic-treated (HWA-DEC-001 F6) | Assumed for a 20 um non-woven; to measure (C6) | 0.9 kPa at 200 mL/min; could be 0.3 to 3 kPa; untreated PP would need 2.5 kPa to wet |
| A7 | Clean water, no fouling; viscosity 1.00 mPa s at 20 C, 1.52 mPa s at 5 C | Water properties | Real water fouls: flow falls with volume (TE) |
| A8 | 20 mL syringe with a 20 mm plunger bore | Typical | Thumb force |
| A9 | Ceramic pot filter: 2 L/h through about 0.31 m2 at a mean head of 0.12 m and a 15 mm wall | Akvopedia (1 to 3 L/h; pot about 30 cm by 25 cm) | Option A2 only |
| A10 | Best-case ceramic: a thin 0.2 um alumina layer at 1,500 L/(m2 h bar) | Typical of ceramic microfiltration membranes | Option A2 only |
| A11 | Membrane life 2,000 L before replacement | Planning value, half of LifeStraw Personal's 4,000 L rating (HWP-PRB-001) | Cost per litre |
| A12 | Carbon cartridge life 500 L | Lower end of 500 to 1,000 L (concept validation questions, item 41) | Cost per litre; replacement set from TG |
| A13 | Turbid water: 50 mg/L suspended solids, specific cake resistance 1 x 10^13 to 1 x 10^14 m/kg | Assumed range for a natural silt and organic cake; to measure (TE) | Flow decline between backflushes (section 4.3) |

## 2. Geometry

Envelope from Rev A: 205 mm long, 26 mm OD, 22 mm bore, 2 mm wall. Axial stations (mm from the intake face): intake cap 0 to 22 (head 0 to 12), seat ring 22 to 24 (17 mm bore), mesh bay 24 to 30, module 24 to 150 (bottom potting 30 to 38, active fibres 38 to 140, top potting 140 to 150 inside the collar 135 to 150), clean header 150 to 156 (backflush socket at 153), carbon cartridge 156 to 180 (bed 158.4 to 178.4), mouthpiece 180 to 205. Fibres: about 220 of 0.8 mm OD and 0.5 mm ID in a 17.2 mm bundle, packing 48 %, active length 102 mm, outer area **0.0564 m2**. The Rev A range of 40 to 80 fibres at 90 to 110 mm gives 0.011 to 0.022 m2 (PR-005).

## 3. Membrane permeability cases

Clean-water permeability (assumption A1), at 25 C as listed and at 20 C as used: 0.2 um MF 3,300 and 2,931; 0.1 um MF 1,800 and 1,599; 100 kDa UF 550 and 489 (high), 215 and 191 (low) L/(m2 h bar). PR-004 sets a floor of 1,800 at 25 C, the floor for usable flow (HWA-DEC-001 F3). PR-002 (200 mL/min at 10 kPa) needs about **3,420 at 20 C** upright and 3,120 at the dip line, primed, which neither grade's listed minimum guarantees (HWA-DEC-001 D2, D3).

## 4. Pressure budget and flow at the persona efforts

Each stage is summed in series: lift (rho g h), intake slots and mesh (orifice), membrane (flux over area), lumens (Hagen-Poiseuille with flow rising along a fibre that is open at one end, factor one half, plus the full flow through the 10 mm top potting), carbon grid and mouthpiece grid (orifice), inlet screen (orifice), carbon bed (Ergun), fines pad (Darcy) and mouthpiece bore (Hagen-Poiseuille and exit velocity head). Flow at a given suction is found by bisection.

Table 1. Pressure drop by stage at 200 mL/min, clean water at 20 C (kPa).

| Stage | 0.2 um fibre | 0.1 um fibre |
| --- | --- | --- |
| Lift to the mouth (upright, shallow dip) | 1.52 | 1.52 |
| Intake slots and mesh | 0.003 | 0.003 |
| Membrane walls | 7.26 | 13.31 |
| Fibre lumens and top potting | 0.60 | 0.60 |
| Grids, screen, mouth bore | 0.08 | 0.08 |
| Carbon bed (0.5 to 2.0 across grading and voidage) | 0.69 | 0.69 |
| Fines pad (assumed A6) | 0.89 | 0.89 |
| **Total** | **11.04** | **17.08** |

Table 2. Flow at the persona efforts (mL/min, clean water, upright, shell primed).

| Suction | 0.2 um at 20 C | 0.1 um at 20 C | 0.2 um at 5 C | 0.1 um at 5 C | UF 100 kDa at 20 C |
| --- | --- | --- | --- | --- | --- |
| Child, 5 kPa | 74 | 45 | 49 | 30 | 6 to 15 |
| Elderly, 7 kPa | 116 | 71 | 77 | 47 | 10 to 24 |
| Rev A, 10 kPa | 179 | 110 | 119 | 73 | 15 to 37 |
| Adult, 15 kPa | 281 | 174 | 188 | 115 | 24 to 59 |

Tilted to drink from a cup (50 mm lift) the child's flow rises to 58 to 96 mL/min. The Rev A geometry (80 fibres at 110 mm) gives 46 (0.1 um) to 78 (0.2 um) mL/min at 10 kPa and 40 fibres at 90 mm gives 19 mL/min. To reach 200 mL/min takes 11.0 kPa (0.2 um) or 17.1 kPa (0.1 um); 400 mL/min takes 20.9 or 33.0 kPa. A 245 mm body with a 145 mm active length (HWA-DEC-001 D3) gives 138 to 213 mL/min at 10 kPa and 53 to 83 mL/min for a child, a small gain because the extra length also adds lift. A child at 45 mL/min takes about 4.4 minutes to drink 200 mL.

### 4.1 Persona effort

Minutes of sipping for 1.5 L, upright, primed, 20 C: child 20 (0.2 um) to 33 (0.1 um), elderly 13 to 21, at 10 kPa 8 to 14, adult 5 to 9; a child in 5 C water needs 31 to 50 minutes. Fatigue, lip seal on the 10 mm tip and holding the straw at a source are for the persona trials (TH).

### 4.2 Immersion and priming

The dirty shell around the fibres is closed at the top by the potting, and wetted fibres do not pass air below their bubble point. Air that gets into the shell (the straw lifted out and drained, or after the air check) therefore stays above the outside water level, and only the fibre length below that level filters. Dry fibres pass air, so a new straw primes itself on the first sips. Table 3 gives the effect; the intake cover keeps the shell full between uses (HWA-DEC-001 F8) and a vent or re-prime step is D10. Suction also lets dissolved air come out of solution (up to about 10 % of it at 10 kPa), which may collect under the carbon and pad; to observe in TC.

Table 3. Flow at 10 kPa by immersion (mL/min, clean, 20 C).

| Case | 0.2 um | 0.1 um |
| --- | --- | --- |
| Shallow dip (water at 50 mm), primed | 179 | 110 |
| Dipped to the 110 mm dip line, primed (lift 0.9 kPa) | 191 | 117 |
| Dip line, shell drained above the water (71 % of the fibre wetted) | 144 | 86 |
| Shallow dip, shell drained (12 % wetted) | 26 | 15 |

### 4.3 Fouling on turbid water

The design flux at 200 mL/min is 213 L/(m2 h), well above what membrane plants sustain on surface water. With a cake model (R = Rm + alpha m / A, assumption A13) and 50 mg/L of suspended solids, flow at 10 kPa through the 0.2 um fibre falls from 179 mL/min clean to 169, 140 and 85 mL/min after 1, 5 and 20 L with a loose cake (1 x 10^13 m/kg) and to 116, 48 and 15 mL/min with a tight one (1 x 10^14 m/kg); the 0.1 um fibre falls from 110 to 106, 94 and 65 or to 82, 41 and 14 mL/min. Clean-water flows are therefore upper bounds: cloudy water should be settled or strained through cloth first, and the backflush interval in litres comes from TE (PR-026).

Results against PR-002, PR-003, PR-004 and PR-005 are in section 11.

## 5. Carbon bed

Bed 16 mm across and 20 mm deep: 4.02 mL; at 0.48 to 0.50 g/mL that is **1.93 to 2.01 g**, not the 5 g first quoted (HWA-DEC-001 F5; PR-015). Empty-bed contact time: 2.4 s at 100, 1.2 s at 200 and 0.6 s at 400 mL/min. That is enough time for free chlorine, which GAC reduces fast, and too short for organic tastes and odours, which need minutes; the carbon claim is limited to chlorine taste, and only after an NSF/ANSI 42 measurement (PR-029). Carbon life is a measured breakthrough, not an assumption (PR-015).

## 6. Seals

AS568-018 EPDM rings (18.77 mm ID x 1.78 mm) on male glands with a 19.3 mm floor and 2.4 mm width in the 22.0 mm bore: gland depth 1.35 mm, **squeeze 24 %**, **stretch 2.8 %**, **fill 77 %**, radial gap 0.10 mm between the 21.8 mm spigots and the bore. These sit within usual static radial practice (squeeze 15 to 30 %, stretch under 5 %, fill under 85 %). With the ring cross-section at 1.78 +- 0.08 mm and printed bores and gland floors at +- 0.1 mm the squeeze spans 15 to 33 %, outside that range; reamed or turned to +- 0.05 mm it spans **18 to 30 %** (HWA-DEC-001 F9). A missing collar ring would leave a 0.10 mm annular gap passing about 230 mL/min of unfiltered water at 10 kPa, which is why there are two in series and an air check at assembly. The Rev A 20 x 2 mm rings have a 24 mm outside diameter and would not enter the bore (HWA-DEC-001 F1). Two rings in series at the only clean/dirty seal that is not a factory potting (PR-007).

## 7. Backflush and the air-hold check

- Backflush at 50 kPa passes about **556 mL/min** (0.1 um) to **741 mL/min** (0.2 um) once the luer tip and the 2 mm socket passage are counted (1.5 velocity heads each), so 20 mL goes through in about 1.6 to 2.2 s; three strokes, with refilling, take about a minute (PR-011, PR-014). 20 mL is only about 0.35 L per m2 of membrane, so the number of strokes is set in TE. The syringe is filled only with water already treated (boiled, tablet-treated or bottled), never from the source, which would put raw water on the clean side (HWA-DEC-001 F11). Thumb force on a 20 mm plunger at 50 kPa is about **16 N**; a firm 60 N push gives about **191 kPa**, about twice the SepraPor forward TMP rating of 1.0 bar for 0.2 um. The module's rated reverse pressure is to confirm (C2) and a pressure limit is D11.
- Air check (PR-012, HWA-DEC-001 F7): 20 mL of air compressed to 13.3 mL of gas is at 51 kPa, but the 4.8 mL of water in the lumens and the 2.3 mL in the header must leave through the fibre walls first, so 51 kPa is reached at about the **6 mL plunger mark**. A wetted, intact 0.2 um wall holds air well above that (ideal Young-Laplace limit 720 kPa for a 0.4 um largest pore; real bubble points lower, to measure); an open, broken 0.5 mm lumen passes air above 0.6 kPa. The check is a plunger hold: push to the 6 mL mark and hold for 10 s; a plunger that keeps moving fails. At 51 kPa it opens only defects of **5.6 um and larger**, so it finds broken fibres and failed collar seals, not bacterial-size flaws. Upright, escaping air rises into the shell and does not reach the intake, so bubbles show only with the straw inverted; dry spots pass air and give a false fail; the shell must be re-primed afterwards (section 4.2). Telling diffusion from a defect is for TA and TF.
- Socket left open under water: through the 2 mm passage at 10 kPa about **506 mL/min** of raw water would bypass the membrane, 2.8 to 4.6 times the filtered flow, and the sip would feel easier, not harder. The socket sits 43 mm above the dip line and its plug is tethered (PR-028); a self-closing socket is D12.

## 8. Options A2 and A3

- **A2 ceramic tube.** From the pot filter (A9) the ceramic's specific permeability is about 2.3 x 10^-14 m2 (556 L/(m2 h bar) at 15 mm). A 17 mm tube with a 4 mm wall and 106 mm of active length, at the 7 kPa left after lift and carbon, passes about **10 mL/min**; a best-case thin 0.2 um layer (A10) also gives about 10 mL/min because the outer area is only 0.006 m2. Both are a twentieth of the target.
- **A3 copper and charcoal.** A copper roll 60 mm long in the 22 mm bore, 75 % open, holds about 17 mL, so at 200 mL/min water spends about **5 s** in it, against the 16 h storage in which copper pots reduced bacteria (Sudha et al. 2012).

## 9. Envelope and mass

From the model: 205 mm long without caps (216 mm with the mouthpiece cap and lanyard eye), 26 mm body, **29.6 mm across** at the backflush plug and tether band, under the 25 cm and 3 cm kit limit (PR-019). Mass **66 g** dry with caps and lanyard (62 g without), under 100 g (PR-027). The straw holds about 40 mL of water when wet (estimate), so it weighs about 106 g full.

## 10. Cost and cost per litre

Prototype parts from `bom/bom.csv`: **USD 17.46** (value-engineering target USD 25, USD 7.54 under; PR-021). A replacement carbon cartridge (body, screen, carbon, pad and O-ring) costs about USD 1.21. Over a 2,000 L membrane life (A11) with a cartridge every 500 L (A12), three replacements: **USD 0.011 a litre** as a prototype. At a mass-production unit cost of USD 3 (mid-range of HWP-PLN-001) with USD 0.15 refills (assumed): about **USD 0.002 a litre**, against about USD 0.02 a litre for NaDCC tablets (HWP-MKT-001) (PR-020). The straw serves one drinker; a tablet treats a household's water and covers viruses.

## 11. Results against the requirements

Table 3. Results by product requirement.

| PR | What | Result on paper | Status |
| --- | --- | --- | --- |
| PR-001 | Bacteria 6 log | Not computable; size exclusion only, absolute rating with a *B. diminuta* challenge required (STM S11) | To verify at TRL 4 (TA, TB) |
| PR-002 | 150 mL/min at 10 kPa, upper bound (HWA-DEC-001 D3) | 110 (0.1 um) to 179 (0.2 um), clean, primed | Met on paper with the 0.2 um grade; not met with 0.1 um (used only under D2) |
| PR-003 | 80 mL/min at 5 kPa | 45 to 74 | Not met on paper |
| PR-004 | Permeability at least 1,800 at 25 C | Specified; PR-002 needs 3,420 at 20 C | Met by design |
| PR-005 | Area at least 0.050 m2 | 0.056 m2 | Met on paper |
| PR-006 | Cysts 3 log | Size exclusion only | To verify at TRL 4 |
| PR-007 | No bypass | Potting plus two O-rings in series (section 6) | Met by design |
| PR-008 | Virus warning | On the drawing | Met by design |
| PR-009 | Ready in 3 min | Wetting time to measure | To verify at TRL 4 |
| PR-010 | Pictograms | Not computable | To verify at TRL 4 |
| PR-011 | Upkeep under 2 min | About 1 min | Met on paper |
| PR-012 | Air check at 50 kPa | 51 kPa at the 6 mL plunger mark; gross defects only | At risk (C2) |
| PR-013 | 250 um mesh, captive | In the model | Met by design |
| PR-014 | Backflush avoids carbon | Carbon dead-ended (STM S18) | Met by design |
| PR-015 | 2.0 g carbon | 1.93 to 2.01 g | Met on paper |
| PR-016 | Freeze warning, drop | Warning on the drawing | To verify at TRL 4 |
| PR-017 | Drain and dry | Drain paths in the model; regrowth unknown | At risk |
| PR-018 | Listed wetted materials | Grades exist | To verify at TRL 4 |
| PR-019 | 250 x 30 mm | 205 x 29.6 mm | Met on paper |
| PR-020 | Below USD 0.02 a litre | 0.011 (prototype), about 0.002 (scale) | Met on paper |
| PR-021 | Parts against USD 25 | USD 17.46 | Met on paper |
| PR-022 | Shelf life | Supplier data | To verify at TRL 4 |
| PR-023 | Mouthpiece per person | Cap fitted; D6 open | At risk |
| PR-024 | One polymer family | PP made parts | Met by design |
| PR-025 | Regional manufacture | Printed or moulded | Met by design |
| PR-026 | 80 % backflush recovery | Not computable | To verify at TRL 4 |
| PR-027 | 100 g dry | 66 g (106 g full) | Met on paper |
| PR-028 | Dip line at 110 mm | In the model | Met by design |
| PR-029 | Chlorine reduction | EBCT 1.2 s | To verify at TRL 4 |


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
