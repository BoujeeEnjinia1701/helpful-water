---
doc_id: HWB-CAL-001
title: "Helpful Water B: bottle cartridge sizing calculations"
project: "Helpful Water B: bottle cartridge"
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
    change: "First TRL 3 sizing of options B1 to B3 from the D3 model (python docs/04-calcs/sizing.py)"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review (HWB-STM-001): weak child at the girls' grip boundary (11.8 kg); 10 C flows; lumen hold-up, first flush and wet mass; end wall, potting and thread checks; duckbill and vent tube checks"
  - version: "0.3"
    date: 2026-11-11
    author: Amish Chadha
    change: Decisions recorded as Amish's (all pending decisions settled on their recommendations, 2026-11-11)

---

# Helpful Water B: bottle cartridge sizing calculations

Result: on paper the B1 squeeze cartridge delivers about 465 mL/min at a held adult squeeze of 17 kPa and 160 mL/min at a weak child's 5.8 kPa with a clean module in 20 C water, about half of each just before a backflush is due and about 23 % less in 10 C water; the membrane takes over 90 % of the pressure. The prototype parts cost USD 18.35 against the USD 20 value-engineering target (USD 1.65 under it), the dry cartridge weighs about 118 g, and the cost per user per year is about USD 10.8 at a 9-month life (over the USD 10 target by USD 0.8) or USD 8.5 at 12 months. All of this rests on an **assumed** clean-water permeability of 1,000 L/(m2 h bar) for the bought module; the module maker's flux data (HWB-DEC-001 C1) can move every flow figure by a factor of 2 or more. Script: `docs/04-calcs/sizing.py`, which reads `cad/src/model.py` PARAMS and writes `docs/04-calcs/sizing_results.json`. Estimates only; nothing here was measured.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## 1. Basis

Table 1. Inputs.

| Input | Value | Basis |
| --- | --- | --- |
| Fibres | 400 looped (800 legs), 0.8 mm outside, 0.5 mm inside, 86.5 mm legs (B1, B3), 146.5 mm (B2) | Design request to the module maker; Rev A illustrative fibre 0.8 / 0.5 mm |
| Membrane area (outside) | 0.174 m2 (B1, B3), 0.295 m2 (B2) | n x pi x outside diameter x 2 x leg |
| Potting packing | 53 % of the 31 mm header bore | Fibre ends over potting area; above about 55 % potting becomes difficult (to confirm with the maker) |
| Clean-water permeability | 1,000 L/(m2 h bar), **assumed** | A quarter of the 0.1 um PVDF example in US 8,708,161 B2 (108 m3/(m2 day 100 kPa), about 4,500 L/(m2 h bar)) |
| Fouled permeability | 50 % of clean, **assumed** | Point at which a backflush is due |
| Water | 998 kg/m3, 1.0 mPa s, 0.0728 N/m (20 C) | Standard values |
| Carbon | 12 x 40 coconut GAC, 0.49 g/cm3, void 0.40, 0.9 mm mean, sphericity 0.75 | Newterra 5DCAW 1240 data sheet (density); void and shape assumed |
| Grip | Child 10 to 11 weak 11.8 kg (girls; boys 12.6), mid 17.5; women 70 to 99 weak 14.7; men 70 to 99 weak 21.3; adult 35 kg (**assumed**) | Topend Sports norms (Camry dynamometer) |
| Squeeze model | 40 % of maximum grip held, 80 % reaching the water, over an 80 x 80 mm contact on an 80 mm bottle, **assumed** | p = F / (D x contact height); STANDARDS 25.6 gives 10 to 30 kPa for a squeeze bottle |

## 2. Neck fit (PR-024)

The collar's female thread matches the 28 mm PCO 1881 and PCO 1810 finishes, which share a thread diameter of about 27.4 mm and a pitch of about 2.7 mm; the 1881 neck is about 17 mm from lip to support ring and the 1810 about 21 mm (Kapy CAD, approximate). The skirt reaches 15.5 mm below the lip, clearing the 1881 support ring by 1.5 mm and the 1810 ring by 5.5 mm, and the cartridge seals on the neck lip through a flat gasket, so both necks fit one collar. The prototype is drawn for PCO 1881. Wide-mouth juice and dairy bottles often use 38 mm two-start finishes (Bericap 38 mm HF two-start, Petainer 38 mm two-start); a printed adapter with a 38 mm female thread below and a 28 mm PCO 1881 male neck above covers them, to be drawn once the exact 38 mm finish drawing is obtained (HWB-DEC-001 C4). Thread data must be checked against the ISBT drawings before any tooling.

## 3. Hydraulics (PR-004, PR-005, PR-006, PR-025)

Flow is found by solving p = (membrane) + (carbon bed) + (lumens) + (outlet) + (mesh) for Q: Darcy flux through the fibre walls, the Ergun equation through the bed, Hagen-Poiseuille in the lumens with uniform permeation (mean drop one third of the full-flow drop over a leg, plus the potting length), Hagen-Poiseuille and one velocity head per contraction in the nipple and nozzle, and K = 1.5 at the four 2 mm valve ports.

Table 2. Squeeze pressure by persona (estimates).

| Persona | Grip (kg) | Held squeeze (kPa) |
| --- | --- | --- |
| Child 10 to 11, weak | 12.6 | 6.2 |
| Child 10 to 11, mid | 17.5 | 8.6 |
| Woman 70+, weak | 14.7 | 7.2 |
| Man 70+, weak | 21.3 | 10.4 |
| Adult, held | 35 (assumed) | 17.2 |
| Adult, full grip | 35 (assumed) | 42.9 |

Table 3. B1 flow by persona (estimates; clean and fouled module).

| Persona | Clean (mL/min) | Fouled (mL/min) | Membrane share of pressure (clean) |
| --- | --- | --- | --- |
| Child 10 to 11, weak (5.8 kPa) | 160 | 82 | 95 % |
| Child 10 to 11, mid (8.6 kPa) | 236 | 121 | 94 % |
| Woman 70+, weak (7.2 kPa) | 198 | 102 | 95 % |
| Man 70+, weak (10.4 kPa) | 286 | 148 | 95 % |
| Adult, held (17.2 kPa) | 465 | 242 | 93 % |
| Adult, full grip (42.9 kPa) | 1,119 | 598 | 90 % |
| Fixed 10 kPa (Rev A goal) | 274 | 141 | 94 % |

At the adult squeeze the stages take: mesh 0.004 kPa, carbon bed 0.47 kPa, lumens 0.25 kPa, nipple, nozzle and valve 0.41 kPa, fibre walls 16.0 kPa. Sensitivity: at the patent's 0.1 um example permeability the flow at 10 kPa would be about 906 mL/min, so the assumed value is deliberately low. Cross-check: the Sawyer Squeeze, a commercial 0.1 um squeeze filter of unpublished area, gave 0.58 L/min by gravity and 2.41 L/min at a maximum squeeze when new (Backpacking Light, 2021), the same order as B1's 1.1 L/min at full grip.

**Cold water.** Flux and the laminar losses scale with 1 / viscosity (1.31 mPa s at 10 C against 1.00 at 20 C). At 10 C B1 gives 360 mL/min at the adult squeeze (186 fouled), 123 for the weak child and 152 for the weak elderly woman (63 and 78 fouled), and B2 takes 8.1 minutes per litre clean and 15.6 fouled. Every requirement is rated at 20 C; whether to rate at 10 C is HWB-DEC-001 D9.

**Squeeze model caveat.** The dynamometer measures grip on a handle about 50 mm across; grip on an 80 mm bottle is lower, and a child's hand does not wrap 80 mm. A diameter factor of about 0.6 (to assess) would put the adult held squeeze near 10 kPa and the adult flow near 275 mL/min. Two-handed squeezing is the design case, and the pressure in a squeezed bottle is to measure with a gauge (HWP-VER-001 TH).

**B2 gravity drip (PR-025 gravity mode).** The inverted bottle drains through 0.295 m2 with a head of 5.2 kPa full and 2.5 kPa near empty, less 0.5 kPa to crack the vent duckbill (assumed): about 6.2 minutes per litre clean and 11.9 minutes fouled, about 160 and 84 mL/min on average. The vent tube (4 x 0.8 mm, 2.4 mm bore) has a Bond number of 0.77, below the 3.37 at which a bubble can rise in a tube, so water it takes in during filling stays as a plug; the first purge needs about 2.9 kPa of bottle vacuum (230 mm of water, meniscus and duckbill) against the 5.2 kPa full head, so the drip slows for the first minute and then runs (to confirm, TH). The base is a continuous 230 mm ring, so it tips at 17.2 deg, but a side push of 4.4 N at the centre of gravity tips it: the stand goes on a table out of children's reach.

**B3 press.** 80 N of arm or body weight on the 70 mm cup gives 18 kPa after 10 N of lip-seal friction (assumed), about 500 mL/min clean and 257 fouled; 150 N gives 36 kPa and about 990 mL/min. The press tube holds 559 mL around the cartridge against a 350 mL fill line.

## 4. Carbon (PR-016, PR-019)

The capsule bed is 29.8 mm across and 20 mm deep: 13.9 mL, or about 6.8 g at 0.49 g/cm3, close to the Rev A finding that a 4 mL straw bed holds about 2 g, not 5 g. Empty-bed contact time is 1.8 s at the adult flow and 5.2 s at a weak child's, about 5 s in B2; the true residence time is about 0.4 times these. These are short contact times for granular carbon, so chlorine taste reduction is a target only (no odour or organics claim), to measure with an NSF/ANSI 42 style test and a breakthrough curve (HWP-VER-001 TG); the 150 L capsule life used for costs is assumed. The bed takes 0.47 kPa at the adult flow, so a deeper bed is affordable hydraulically if tests ask for more contact time. The capsule sits on the dirty side, upstream of the membrane (HWB-DEC-001 F1), so carbon fines and any bacteria that grow in the bed meet the membrane before the outlet. Two consequences follow. Free chlorine is removed in the bed within seconds, so chlorine co-treatment (solution D) must be dosed in the bottle and left for its full contact time before the water is filtered, and the filtered water carries no residual and is not stored (HWB-DEC-001 F7). Turbid water loads the bed with silt that a backflush cannot reach (the capsule is out), and the bed's viscous loss rises about 3.4 times as its voids fall from 0.40 to 0.30, so turbid water is settled or cloth-filtered first and the capsule is replaced when a backflush does not restore the flow.

## 5. Integrity and hygiene (PR-010, PR-011, PR-012, PR-018, PR-029)

A wetted 0.1 um pore holds air to about 2,900 kPa (Young-Laplace, 4 gamma / d), an open 0.5 mm lumen only to 0.6 kPa, so squeezing air from an empty bottle through the wetted cartridge into a cup of water shows a stream of bubbles from any opening larger than about 17 um at 17 kPa. That finds broken or cut fibres and leaking O-rings; it does not find small defects that cysts (4 to 15 um) or bacteria could pass, so the user rule is "stop if bubbles stream", never "safe if there are none" (PR-010). The test is done with an adult squeeze: at a weak user's 6 kPa it finds only openings above about 50 um, and slits are found from about 8.5 um (2 gamma / w). The only dirty-to-clean boundary is the potting and the two header O-rings (PR-011); at 53 % packing the potting's penetration and the module's production integrity test are for the maker to confirm (HWB-DEC-001 C1, F9). Downstream of the potting the clean side holds 5.7 mL in the header plenum, nipple and spout, which drains when upended (PR-012), but the 800 lumens hold another 15.2 mL that never drains (capillary rise in a 0.5 mm bore is about 60 mm), so about 21 mL of clean side stays wet and bacteria can grow through a 0.1 um membrane over days of wet storage. After any storage the first 50 mL is discarded (HWB-DEC-001 F6), and grow-through is tested in storage cycles (TE, TG). The fibres must be hydrophilic PVDF or PES, shipped wet or with a wetting agent, because plain PVDF passes no water at a few kPa; at first use and after drying the cartridge is primed by a syringe backflush with the capsule out, which also pushes air out of the dirty-side shell where it would cover fibres (HWB-DEC-001 F8, F9). Water expands about 9 % on freezing, which can split fibres with no change in flow, so there is no freeze claim and a frozen cartridge is retired (PR-018). A 60 mL syringe (26.7 mm bore) gives 54 kPa at a gentle 30 N push and 179 kPa at a hard 100 N push; the module maker's maximum backwash pressure is not yet known (PR-029, HWB-DEC-001 C2). At 179 kPa the clean side pushes 135 N on the potting face, which the maker must rate. On release after a squeeze the duckbill opens at about 0.5 kPa when the bottle is upright, but tipped it sits under the water and needs about 2.9 kPa of vacuum, so the bottle is turned upright to refill (HWB-DEC-001 F5).

## 6. Strength and mass (PR-014, PR-028)

The housing wall (41 mm outside, 37 mm bore, 2 mm) carries a hoop stress of 1.65 MPa at a hard backflush and 0.4 MPa at a full squeeze, a factor of 6 on 10 MPa taken for printed polypropylene (a third of moulded yield, assumed). The flat 4 mm end wall governs: as a simply supported circular plate (1.24 p a2 / t2) it carries 1.14 MPa at a full squeeze (factor 9), and in the backflush as instructed the collar end is open, so the shell is near atmospheric pressure. If the collar end were blocked at 179 kPa the end wall would reach 4.7 MPa (2.9 MPa clamped), a factor of 2.1 against PR-028's 5; a 6.2 mm wall would meet it (HWB-DEC-001 D8; PR-028 at risk). The housing thread carries 192 N in that case at 0.33 MPa of shear. From the model's volumes and real densities the dry cartridge weighs about 118 g: housing 49 g, collar 17 g, module about 35 g (fibres 11 g at 30 % solid wall), capsule and carbon 16 g, the rest 1 to 3 g each. That is above the shortlist's "about 100 g", so the claim is now about 120 g; wet, with the clean side, the shell water and the carbon's water, it is about 182 g. A moulded 1.5 mm housing wall would save about 12 g. The cartridge is 217 mm long and 46 mm across the collar thread, inside UR-012's 250 mm length but wider than its 30 mm for personal devices (PR-014 not met).

## 7. Cost and life (PR-015, PR-026)

Prototype parts from `bom/bom.csv`: USD 18.35 (value-engineering target USD 20; USD 1.65 under). Scale estimate (not quotes): module USD 3.20, moulded parts USD 1.40, carbon capsule USD 0.35, seals, mesh and valve USD 0.60, assembly, quality checks and pack USD 1.50, total USD 7.05 against the shortlist's under USD 8. Over a 9-month life at 2 L a day (547 L, PR-026) a user needs three extra capsules: USD 8.10, or USD 0.015 a litre and USD 10.8 per user per year, over the USD 10 target by USD 0.8 (PR-015). At a 12-month life the cost is about USD 8.5 per user per year. The module life itself is unknown until fouling and backflush tests (TE).

## 8. Results against requirements

Table 4. Results.

| Requirement | Result | Status |
| --- | --- | --- |
| PR-001, PR-002 | Pore 0.1 um against bacteria (5 to 50 times larger) and cysts (40 to 120 times); a log reduction exists only once measured | To verify at TRL 4 |
| PR-003 | Warning and pictogram in the artwork and instructions | Met by design |
| PR-004 | 465 mL/min at 17 kPa, clean, 20 C (360 at 10 C) | Met on paper |
| PR-005 | 160 (child) and 198 (elderly) mL/min clean; 82 and 102 fouled | At risk |
| PR-006 | 274 mL/min clean, 141 fouled, at 10 kPa | At risk |
| PR-007, PR-008 | Shipped assembled; pictograms to design | To verify at TRL 4 |
| PR-009 | Two 60 mL syringe strokes and a drain, about 1 minute | Met on paper |
| PR-010 | Air test shows openings above 17 um | Met on paper |
| PR-011 | One seal line: potting and two header O-rings | Met by design |
| PR-012 | 5.7 mL downstream of the potting; 15.2 mL in the lumens stays wet (first flush) | Met on paper |
| PR-013 | Material families listable; grades to certify | To verify at TRL 4 |
| PR-014 | 217 mm long, 46 mm across against 250 x 50 (HWB-DEC-001 D4) | Met |
| PR-015 | USD 18.35 prototype, USD 7.05 at scale, USD 10.8 per user per year | Over target |
| PR-016 | Capsule opens by hand; refills with 12 x 40 GAC | Met by design |
| PR-017, PR-018 | Shelf life and drop to test; freeze warning by design | To verify at TRL 4 |
| PR-019 | 1.8 s contact at the adult flow | Met on paper |
| PR-020 to PR-023 | Mesh reachable, cup filling, PP parts separable, printable parts | Met by design |
| PR-024 | Fits PCO 1881 and 1810; 38 mm adapter to draw | Met on paper |
| PR-025 | 198 mL/min at a weak elderly squeeze; B2 gravity mode 6.2 min per litre | Met on paper |
| PR-026 | 547 L over 9 months needed; module life to test | To verify at TRL 4 |
| PR-027 | Duckbill cracking about 0.5 kPa (assumed) | To verify at TRL 4 |
| PR-028 | Hoop factor 6; end wall factor 2.1 if the collar end were blocked | At risk |
| PR-029 | 54 to 179 kPa against an unknown module limit | At risk |

## Sources

As HWB-STM-001, plus FreshWaterSystems, "SilCarbon Activated Carbon Coconut Shell 12 x 40 Mesh, 1 Cubic Foot," USD 108.93, https://www.freshwatersystems.com/products/silcarbon-activated-carbon-coconut-shell-12-x-40-mesh-1-cubic-foot (checked 2026-11-11).

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
