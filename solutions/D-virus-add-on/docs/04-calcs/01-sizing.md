---
doc_id: HWD-CAL-001
title: "Helpful Water D: chlorine add-on for viruses sizing calculations"
project: "Helpful Water D: chlorine add-on for viruses"
doc_type: Calculation note
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First sizing of dose, residual, CT, pH and temperature effects, ball timer, overdose, liquid decay, erosion feeder range, mass and cost
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: CT by the EPA definition (51); Morris pKa; Haberman-Sayre wall factor and a 45 minute timer that reads 30 minutes at 40 C; D2 drops by Tate's law; bottle range, wrong-tablet, squeeze tolerance and timer expansion figures (independent review, HWD-DDR-004)
---

# Helpful Water D: chlorine add-on for viruses sizing calculations

At the household rate of about 2 mg/L in clear water, the free chlorine left after 30 minutes is estimated at 1.7 mg/L and the CT at 51 mg min/L (residual at the end of the wait x time, the EPA definition), about six times the US EPA value for 4-log virus inactivation at 5 C, so the dose and wait of D1 have margin for viruses in clear, near-neutral water; they have none for *Cryptosporidium*. The figures are first-order estimates from `docs/04-calcs/sizing.py`, which reads `cad/src/model.py` PARAMS and writes `sizing_results.json`; every assumption is marked "assumed". Nothing here is measured. Option D1 is described; D2 and D3 are sized only as far as the options comparison needs (HWD-OPT-001).

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## 1. Dose arithmetic (PR-001, PR-005, PR-020)

NaDCC carries two N-Cl groups, each releasing one hypochlorous acid, counted as one Cl2 of available chlorine: 2 x 70.906 / 219.95 = 64.5 % for the anhydrous salt and 55.4 % for the dihydrate. Catalogue household tablets carry 57 to 61 % (2 mg in 3.5 mg, 40 mg in 67 mg; IFRC catalogue WASDCHLA01, checked 2026-11-11), inside that range.

Table 1. Doses (mg/L free chlorine before demand).

| Case | Dose | Note |
| --- | --- | --- |
| D1, one 3.5 mg tablet in 1 L | 2.0 | Household rate |
| D1, two 3.5 mg tablets in 1 L | 4.0 | Settled turbid water; below 5 mg/L |
| D1, one 67 mg tablet in 20 L | 2.0 | C's raw bucket |
| D1, one 67 mg tablet in 25 L | 1.6 | Full 25 L container |
| D1, one 1 L tablet in 1.5 L | 1.3 | Larger bottle: one tablet per litre or part |
| D2, 3.0 mL of 1.25 % in 20 L | 1.9 | CDC SWS one cap (Lantagne 2006) |
| D2, five drops in 1 L | 1.7 to 2.1 | Drop 0.028 to 0.033 mL from a 2.0 mm orifice (Tate's law, Harkins-Brown 0.60 to 0.72; F9) |
| D2, three drops from a 1.2 mm orifice (as briefed) | 0.6 to 0.7 | Under 1 mg/L, so the orifice and count were changed (F9) |
| D1, one 1 L tablet in 0.5 L (two tablets) | 4.0 (8.0) | Two tablets in a small bottle pass 5 mg/L, so the blue insert is labelled for 1 to 1.5 L bottles (F8) |
| D1, one 1 L tablet in the 20 L well by mistake | 0.1 | Silent under-dose (S40); actual-size tablet circles on the label; field check proposed (D7) |

Units check (S33): 1.25 % = 12.5 g/L = 12.5 mg/mL; 3 mL x 12.5 mg/mL / 20 L = 1.875 mg/L. D2's metering chamber holds the annulus between an 18 mm bore and a 5 mm standpipe, 12.8 mm deep: 3.01 mL. A 150 mL bottle therefore treats 1,000 L.

## 2. Residual model (PR-002, PR-013)

Free chlorine C(t) is modelled as a fast demand d30 used over the first 30 minutes (time constant 6 min, assumed), then first-order decay with rate k. Demands and rates are assumed, chosen inside the 0.5 to 4 mg/L of 24 h consumption measured in 20 L jerrycans by Wu and Dorea (2020).

Table 2. Residual scenarios (assumed demand and decay).

| Scenario | Dose | d30 | k (per h) | At 30 min | At 1 h | At 24 h | Used in 24 h |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Clear, under 5 NTU | 2.0 | 0.3 | 0.035 | 1.70 | 1.67 | 0.75 | 1.25 |
| Settled turbid, 5 to 50 NTU, two tablets | 4.0 | 1.0 | 0.070 | 3.00 | 2.90 | 0.58 | 3.42 |
| Turbid, one tablet (misuse) | 2.0 | 1.0 | 0.070 | 1.00 | 0.97 | 0.19 | 1.81 |

Against the targets: at least 0.5 mg/L at 30 minutes (WHO GDWQ via WEDC Mobile Note 7) is met in all three; below 2.0 mg/L at 1 h (CDC acceptability) is met for clear water and missed at the turbid double dose; at least 0.2 mg/L at 24 h (CDC protection in storage) is met for clear and double-dosed water and missed by the misuse case, which is why the turbid rule (fix F1) exists. The residual is removed by the carbon of A to C, so none survives in the filtered water (PR-013, HWD-STM-001 S16).

## 3. CT against inactivation data (PR-003)

CT is the residual at the end of the contact time multiplied by the time, as the US EPA defines it for a batch; the integral of the residual over time, used in version 0.1, is a little higher (53 against 51 in clear water) and is kept only as a cross-check. The CT tables assume low-turbidity water, so no virus credit is taken above 5 NTU (S9).

Table 3. CT reached and the time needed for each target, clear water at 2 mg/L.

| Target | CT needed (mg min/L) | Source | CT in 30 min | Margin | Time to reach it |
| --- | --- | --- | --- | --- | --- |
| 4-log virus, 5 C, pH 6 to 9 | 8 | US EPA table | 51 | 6.4 | 4.2 min |
| 4-log virus, 0.5 C, pH 6 to 9 | 12 | US EPA table | 51 (194 in 120 min) | 4.3 (16.1) | 6.4 min |
| 4-log virus, 5 C, pH 10 | 60 | US EPA table | 51 (194 in 120 min) | 0.85 (3.2) | 34 min |
| Hepatitis A, 1 mg/L, pH 7.5, 25 C | 16 | CDC timetable | 51 | 3.2 | 8.6 min |
| Human norovirus GII, 2-log (molecular) | 13 | Dunkin et al. 2017 | 51 | 3.9 | No quantified claim (S10) |
| Giardia, 1 mg/L, pH 7.5, 25 C | 45 | CDC timetable | 51 | 1.1 | 25.5 min; not relied on |
| *Cryptosporidium* | 15,300 | CDC timetable | 51 | 0.003 | About 6 days; not addressed |

The misuse case (turbid water, one tablet) reaches CT 30 in 30 minutes, but the CT tables are built for low-turbidity water and particle-associated viruses are shielded, so this case is not credited; that is the reason for the settle-first rule, and settled turbid water at the double dose is credited only after the TB challenge at 10 and 50 NTU.

## 4. pH and temperature (PR-009, PR-010)

The HOCl share of free chlorine is 1 / (1 + 10^(pH - pKa)), with the pKa taken by temperature from Morris (1966): 7.54 at 25 C, 7.58 at 20 C and 7.75 at 5 C. At 20 C the share is 79 % at pH 7, 52 % at 7.5, 28 % at 8 and 11 % at 8.5; at 5 C it is 85 %, 64 %, 36 % and 15 %. HOCl is 80 to 100 times more effective than OCl- (operator study guide, checked 2026-11-11). The US EPA CT table already covers pH 6 to 9, so the check uses it directly; weighting it by the HOCl share as well, as version 0.1 did, counts pH twice. The label keeps 60 minutes above pH 8 as extra margin and excludes pH above 9, where the EPA value jumps to 60. Cold water: at 30 minutes the CT is already 4.3 times the 0.5 C value, so the longer waits of practice guidance (30 minutes above 18 C, 60 at 10 to 18 C, 120 below 10 C; Akvopedia, WHO and WEDC TN 11 for 18 C and above) are a conservative margin; the label run count (one, two, three) implements them (fixes F4 and F11).

## 5. Ball timer (PR-008, PR-009)

A 2.0 mm stainless ball (7,900 kg/m3) falls 13.0 mm through silicone fluid (975 kg/m3) in a 4.0 mm bore. The Faxen series used in version 0.1 is valid only to d/D of about 0.3; the Haberman-Sayre wall factor for d/D = 0.5 (0.170) gives the viscosity for a 45 minute nominal fall at 25 C: 534 Pa s, about 548,000 cSt, inside the 600,000 cSt grade sold (Dow PMX-200 listing), blended down as the fall-time check requires. Reynolds number 2 x 10^-8, far inside the Stokes regime. The timer sits at air temperature. With an assumed activation energy of 15 kJ/mol (the data-sheet viscosity-temperature coefficient of 0.61 back-calculates to 14.8 kJ/mol) and a viscosity tolerance of 10 % (assumed), the 34 minute nominal of version 0.1 read only 23 minutes at 40 C, so the nominal is now 45 minutes, the shortest that still reads 30.3 minutes at 40 C at the low end of the tolerance (fix F11, replacing F6). It runs 37 minutes at 35 C and 62 minutes at 10 C. The run count on the label is the smallest that meets the cold-water wait at the warm end of each band at the low tolerance: one above 18 C, two at 10 to 18 C (94 minutes against 60) and three below 10 C (167 minutes against 120). The sealed 0.19 mL of fluid changes volume by about 6 uL (3.4 %) between a 25 C fill and -10 or 60 C, so the capsule needs an expansion allowance, to be detailed with the fluid trials (HWD-DEC-001 C5). End effects over the short 13 mm fall are ignored; the fluid grade is tuned by a fall-time check per batch (C2).

## 6. Overdose and by-products (PR-005, PR-006, PR-007, PR-018)

A 67 mg tablet in a 1 L bottle would give 40 mg/L chlorine and 67 mg/L NaDCC (WHO values 5 and 50 mg/L). The keyed wells stop it: the 1 L bore is 9.5 mm against an assumed 13 mm 20 L tablet; the 20 L bore is 14.5 mm (fix F2; sizes measured when bought, C1). The key works one way only: a 1 L tablet fits the 20 L well and gives 0.1 mg/L, a silent under-dose (S40), and a 20 L tablet dropped straight into an open bottle neck bypasses the key (S20). Three 1 L tablets would give 6 mg/L; the free height under the plug stop (8.0 mm for 1 L, 11.0 mm for 20 L) holds two tablets of 3.5 and 5.0 mm but not three (fix F3), as long as each tablet is thicker than 2.67 mm (1 L) or 3.67 mm (20 L), which C1 confirms. Cyanuric acid from NaDCC is 129.07 / 219.95 = 0.587 of the NaDCC mass: 4.1 mg/L at the two-tablet dose, against the WHO 40 mg/L. THMs from household chlorination have been found below the WHO guideline values (Lantagne et al. 2008, as summarised by Akvopedia); organic-rich water forms more, so settling helps and TG measures them.

## 7. Liquid strength over shelf life (option D2)

WEDC: hypochlorite stored sealed, cool and dark can lose half its strength in a year, which leaves 84 % after 3 months. E4C reports a 13 % product falling to 8 % in 75 days at 27 C, a half-life of about 107 days; applied to 1.25 % as a warm bound, 55 % remains at 3 months and one cap gives 1.0 mg/L in 20 L (0.6 at 6 months). Dilute hypochlorite decays more slowly than the concentrate, so the real figure lies between, to measure (TJ). This silent under-dose is D2's main weakness.

## 8. Erosion feeder range (option D3)

A release set by contact gives a dose proportional to standing time t. In a household raw bucket t runs from 0.5 to 24 h (assumed), a ratio of 48, while the 1 to 5 mg/L band allows 5 and the 2 to 4 mg/L target band 2. Sized for 2 mg/L at 30 minutes the bucket reaches about 96 mg/L at 24 h; sized for 5 mg/L at 24 h it gives 0.1 mg/L at 30 minutes. The principle fails in a batch container (HWD-STM-001 X1, X2).

## 9. Effort, mass and size (PR-012, PR-015, PR-021)

D1 is 52 x 41 x 52 mm with the timer boss and about 45 g without the bottle (model volumes and densities). The plug needs 3.5 turns; the cap closes at an assumed 1.0 N m on the PCO 1881 thread, the same as a bottle cap. D2's squeeze lifts the liquid 134 mm into the chamber (about 1.8 kPa with entry loss); a 10 N squeeze (assumed) is under half of a weak child's 124 N grip (Camry norms, as HWB-CAL-001). PCO 1881 neck data are those of HWB-CAL-001.

## 10. Cost and cost per litre (PR-019, PR-020)

Value-engineering target: USD 10 of prototype parts. Estimated cost of the constructable design: USD 9.15 (USD 0.85 under the target), of which USD 5.95 is the cap and USD 3.20 the twenty test tablets. Scale cost of the cap is estimated at USD 1.40 (moulded parts 0.45, seals 0.10, timer 0.35, labels 0.10, assembly and pack 0.40; estimates, not quotes). Over an assumed two-year life:

Table 4. Cost per litre and per year (humanitarian tablet price CHF 0.01, about USD 0.011, IFRC pre-budget figure).

| Use | Litres over life | Cost per litre | Cost per year |
| --- | --- | --- | --- |
| Personal, 1 L tablets, 3 L a day | 2,190 | USD 0.012 | USD 12.74 per person |
| Household of five, 20 L tablets, 5 L per person a day for drinking and cooking (assumed) | 18,250 | USD 0.0006 | USD 5.72 per household (456 tablets) |
| Personal, 1 L tablets at retail (USD 0.22 each, CampSaver) | 2,190 | USD 0.22 | Not viable as the main route |
| D2, 1.25 % liquid (USD 0.33 per 150 mL, E4C) | 1,000 per bottle | USD 0.0003 | Liquid only |

Dosing in the 20 L bucket is about twenty times cheaper per litre than dosing bottle by bottle, which is a decision for Amish (HWD-DEC-001 D5).

## 11. Results against requirements

Table 5. Results against the product requirements of HWD-PRS-001.

| Requirement | Result | Section |
| --- | --- | --- |
| PR-001 household dose | 2.0 mg/L (1.6 in 25 L) | 1 |
| PR-002 residual at 30 min | 1.7 mg/L, assumed demand | 2 |
| PR-003 CT for viruses | 53 against 8 mg min/L at 5 C | 3 |
| PR-004 claim wording | HWP-CLM-001 wording only | Precis, README |
| PR-005 maximum dose | 4.0 mg/L at two tablets | 1, 6 |
| PR-006 wrong tablet rejected | 9.5 mm bore against 13 mm (assumed) | 6 |
| PR-007 two-tablet limit | 8.0 and 11.0 mm free height | 6 |
| PR-008 timer run | 30.6 min at the low end | 5 |
| PR-009 cold-water rule | Run count on the label | 4, 5 |
| PR-010 turbid-water rule | Settle, two tablets, not above 50 NTU | 2, 4 |
| PR-011 see the tablet dissolve | Clear plug | Precis |
| PR-012 bottle neck fit | PCO 1881, as HWB-CAL-001 | 9 |
| PR-013 order and residual | No residual after carbon: at risk | 2 |
| PR-014 C bucket interface | Proposed 28 mm port: at risk | 1 |
| PR-015 ready to use | No tools | 9 |
| PR-016 pictograms | To verify (TH) | Precis |
| PR-017 wetted materials | To verify (TG) | STM S28 |
| PR-018 by-products | Cyanuric acid 4.1 against 40 mg/L | 6 |
| PR-019 cost | USD 9.15 against USD 10 | 10 |
| PR-020 standard consumable | 3.5 mg and 67 mg household tablets | 1, 10 |
| PR-021 storage | To verify (TF) | 9 |
| PR-022 taste after the filter | To verify (TG, TH) | 2 |
| PR-023 end of life | No batteries | Precis |
| PR-024 regional manufacture | Printed and moulded parts | 10 |

## Sources

As listed in HWD-STM-001, in particular: IFRC catalogue WASDCHLA01 and the IFRC tablet-choice note; Lantagne (2006), CDC SWS; WEDC Mobile Note 7 quoting WHO GDWQ; WHO chlorine and NaDCC fact sheets; the US EPA 4-log virus CT table (California Water Boards copy); the CDC chlorine timetable; Dunkin et al. (2017); Crider et al. (2018); Wu and Dorea (2020); Akvopedia NaDCC; E4C WaterGuard; Dow PMX-200; CampSaver Aquatabs listing (https://www.campsaver.com/aquatabs-water-purification-tablets.html, checked 2026-11-11); Topend Sports grip norms (as HWB-CAL-001). All checked 2026-11-11.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
