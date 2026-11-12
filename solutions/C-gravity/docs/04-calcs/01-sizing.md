---
doc_id: HWC-CAL-001
title: "Helpful Water C: household gravity filter sizing"
project: "Helpful Water C: household gravity filter"
doc_type: Calculation note
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First sizing of C1 (and first-order numbers for C2 and C3) from cad/src/params.py by docs/04-calcs/sizing.py"
---

# Helpful Water C: household gravity filter sizing

On paper, C1 treats a household of five's 45 L day in 1.6 h of filtering with a clean module and 2.8 h when the module is due for a backflush, on a gravity head of 0.42 to 0.66 m, from an assumed membrane permeability of 1,000 L/(m2 h bar) that the module maker must confirm (HWC-DEC-001 C1). The membrane takes 87 % of the head; every other stage together takes under 0.7 kPa. All numbers come from `docs/04-calcs/sizing.py`, which reads `cad/src/params.py` (the same dimensions the CAD model uses) and writes `sizing_results.json`. These are first-order estimates, not measurements.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## 1. Assumptions

Table 1. Assumptions (each marked assumed until a supplier or a TRL 4 test replaces it).

| Assumption | Value | Basis |
| --- | --- | --- |
| Clean-water permeability of the module | 1,000 L/(m2 h bar), assumed | Same design value as solutions A and B; a 0.1 um bucket kit gives about 50 L/h at a similar head (CAWST), consistent within a factor of two |
| Permeability when a backflush is due | 50 % of clean, assumed | Program assumption (A, B) |
| Module life | 30,000 L, assumed | LifeStraw Family 2.0 is rated 30,000 L (Engineering for Change, checked 2026-11-11); supplier to state |
| Bucket | 300 mm top, 262 mm base, 370 mm tall, 2.3 mm wall, assumed typical | To measure from local 20 L food-grade pails (HWC-DEC-001 C3) |
| Fittings loss | K sum 7.7 at the 7 mm barb bore | Typical handbook values for entry, strainer, open ball valve, barbs and tee, exit |
| Tip criterion | 15 deg, assumed | As solution B |
| Water | 20 degC, 998 kg/m3, 1.0 mPa s | Standard values |

## 2. Household demand

Sphere gives 2.5 to 3 L for drinking and food and 3 to 6 L for basic cooking per person per day ([Sphere, water supply standard 1](https://sphereprototype.conted.ox.ac.uk/standards/watersupply/accessAndWaterQuantity.html), checked 2026-11-11), so five people need 27.5 to 45 L a day. C is sized for **45 L a day** (requirement PR-005), in about three batches.

## 3. Containers, levels and head

Table 2. Levels (heights above the floor).

| Quantity | Value |
| --- | --- |
| Upper shelf top (raw bucket foot) | 900 mm |
| Raw outlet centre (50 mm above the raw floor) | 953 mm |
| Fill line (17 L, 291 mm deep) | 1,194 mm |
| Raw bucket rim | 1,270 mm |
| Clean discharge (inlet fitting top on the clean lid) | 536 mm |
| Settling zone below the outlet | 2.65 L |
| Usable batch above the outlet | 14.35 L |
| Clean bucket free volume above the 2.5 L refill line | 19.6 L |
| Worst batch: raw bucket filled to the brim | 19.4 L |
| Head, outlet to discharge and fill line to discharge | 0.42 to 0.66 m (4.1 to 6.4 kPa), mean 5.3 kPa (PR-030) |

Even a brim-full raw bucket fits in the clean bucket when the user starts below the 2.5 L refill line, which sits just above the tap (PR-025). The full system weighs about 49 kg.

## 4. Flow and daily filtering time

The module has 600 looped fibres, 0.8 mm outside and 0.5 mm inside diameter, with 220 mm legs: 0.664 m2 of outside area. Flow solves head = membrane loss (flux = permeability x transmembrane pressure) + lumen loss (Hagen-Poiseuille, half the full-leg loss because permeate collects along the leg) + hose loss (Hagen-Poiseuille, 0.81 m of 9.5 mm bore) + fittings loss (K x v2/2). A batch drains in 10 s steps as the raw level falls.

Table 3. Flow and time (estimates).

| Quantity | Clean module | Due for a backflush |
| --- | --- | --- |
| Flow at the fill line / at the outlet | 36.7 / 23.6 L/h | 19.9 / 12.7 L/h |
| Mean flow | 30.2 L/h (about 500 mL/min) | 16.3 L/h |
| One 14.1 L batch | 28 min | 52 min |
| 45 L day, filtering | 1.6 h | 2.8 h (PR-005) |
| 45 L day, elapsed with 1 h settling and 30 min contact per batch | 6.3 h | 7.6 h |

Table 4. Pressure taken by each stage at the mean head, clean module.

| Stage | Pressure |
| --- | --- |
| Fibre walls (outside-in) | 4.55 kPa |
| Lumens and potting | 0.50 kPa |
| Hoses | 0.03 kPa |
| Strainer, valve, barbs, tee, entry and exit | 0.18 kPa |
| Total | 5.26 kPa |

Cross-check: 1,000 L/(m2 h bar) x 0.66 m2 x 0.053 bar is 35 L/h before the other stages (STEM row S5), and a commercial 0.1 um bucket kit gives 46.5 to 54 L/h with a 0.3 m hose under a bucket ([CAWST](https://washplusblog.fhi360.org/drinkingwaterupdates/wp-content/uploads/2014/03/cawst-sawyer.pdf), checked 2026-11-11).

## 5. Separation, settling, integrity and hygiene

- **Settling.** Stokes velocity for quartz silt: 13 mm/h at 2 um, 81 mm/h at 5 um, 324 mm/h at 10 um, 1.3 m/h at 20 um. 10 um silt falls the 241 mm column above the outlet in 0.74 h at 20 degC and 1.13 h at 5 degC (viscosity 1.52 mPa s), so the instruction is 1 h, or 1.5 h below 10 degC; clay and colloids stay suspended and load the module, so turbid water (SC3) needs more backflushes (PR-026). The cloth (eight layers, about 20 um effective pore; Colwell et al. 2003) takes the coarse load at filling.
- **Air hold test.** Young-Laplace 4 gamma / d: at 100 kPa (a firm 56 N push on the 26.7 mm bore) any opening above 2.9 um passes air and shows as bubbles in the clear raw hose, while real 0.1 um fibres hold air to hundreds of kPa (PR-011). The lumens hold 52 mL of water, which the first strokes push out through the fibre walls; Boyle's law then needs several more strokes, so a luer check valve sits on the backflush port (HWC-DEC-001 F5). A gross check, never a proof of performance.
- **Clean-side pressure.** The module outlet (360 mm) sits 176 mm below the clean discharge, so the clean side is at +1.7 kPa while filtering: a leaking clean fitting drips out (PR-013).
- **Hold-up.** About 83 mL stands on the clean side between batches: 52 mL in the lumens, the rest in the tee and clean hose (PR-015).
- **Chlorine (with D).** 30 min at an assumed 0.5 mg/L residual gives CT 15 mg min/L, above the 8 mg min/L for 4 log virus inactivation at 5 degC ([California Water Boards, EPA CT table](https://www.waterboards.ca.gov/drinking_water/programs/districts/docs/sonoma/120_4_log_virus_inactivation_through_cl2_disinfection.pdf), checked 2026-11-11). *Cryptosporidium* needs CT 15,300 mg min/L ([CDC guidance via NJ DOH](https://nj.gov/health/ceohs/documents/phss/hyperchlorination-to-kill-crypto-when-chlorine-stabilizer-is-not-in-the-water.pdf), checked 2026-11-11), 136 h at 1.875 mg/L, so the membrane is the barrier for oocysts. Three years of 3.75 mg/L contact is 98,550 ppm h, 3.3 % of a PVDF membrane's 3,000,000 ppm h lifetime tolerance ([LG Water Solutions](https://www.lgwatersolutions.com/wp-content/uploads/2024/12/QuantumFlux_Pressurized-UF-Membrane_Design-and-Operating-Parameters_F-1.pdf), checked 2026-11-11).

## 6. People and the stand

- **Tap.** An 8 mm tap bore at 0.05 to 0.26 m of head gives 1.75 to 4.1 L/min: a 250 mL cup in 8.6 s with 5 L in the bucket (PR-006).
- **Backflush.** 30 N on the syringe gives 54 kPa; 100 N gives 179 kPa (PR-007); the module's backwash limit is to confirm (HWC-DEC-001 C2).
- **Filling.** The raw bucket is filled in place from 5 L jugs at a 1.27 m rim (PR-027).
- **Stability.** With the raw bucket full and the clean bucket empty the centre of gravity is 0.83 m up. The 420 mm frame alone tips at 14.2 deg (58 N at 1 m), under the 15 deg criterion; the 560 mm feet raise it to 18.7 deg (78 N) (PR-028, HWC-DEC-001 F1).

## 7. Cost

Value-engineering target: USD 60. Estimated cost of the constructable design: **USD 86.40** (USD 26.40 over the target; `bom/bom.csv`). Over the assumed 30,000 L module life (1.8 years at 45 L a day) that is USD 0.003 a litre and USD 9.44 per person per year, before any chlorine from D (PR-017). An estimated USD 29 at scale (moulded parts, module at volume, local stand) is a planning figure, not a quote.

## 8. Options C2 and C3 (first order)

- **C2 ceramic candles.** Four candles at about 1 L/h each (British Berkefeld data) give 4 L/h full; a 16 L batch takes about 6.7 h and the 45 L day about 19 h of filtering. Four candles at 10,000 L each give 40,000 L.
- **C3 biosand.** A 392 mm bore (0.12 m2) at the 0.4 L/min CAWST maximum loads 199 L/(h m2), under the 600 limit; an 18 L batch takes about an hour, 2.5 batches a day, each followed by a pause of 1 to 48 h; 124 kg of sand and gravel; up to 30 days to ripen.

## Requirements checked here

PR-005, PR-006, PR-007, PR-011, PR-013, PR-015, PR-017, PR-025, PR-026, PR-027, PR-028 and PR-030 are evaluated in this note; PR-004 and PR-021 rest on section 5.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
