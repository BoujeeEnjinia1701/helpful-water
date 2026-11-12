---
doc_id: HWD-DDR-004
title: "Helpful Water D: fixes after the independent STEM review"
project: "Helpful Water D: chlorine add-on for viruses"
doc_type: Design decision record
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: Fixes F7 to F12 made under the standing instruction of 2026-10-23 after the independent review recorded in HWD-STM-001; D7 proposed
---

# Helpful Water D: fixes after the independent STEM review

**Status:** decided under Amish's standing instruction of 2026-10-23 (STANDARDS section 20 fix rule); Amish can reverse any of them. Each keeps the working principle (a matched tablet dose, a mechanical wait indicator, filter after). One finding that changes the kit and its cost (a field chlorine check) goes to Amish as HWD-DEC-001 D7. Numbers are from HWD-CAL-001 (`docs/04-calcs/sizing.py`).

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## Context

A second agent, run as a separate process that saw only the claims table, the two calculation scripts, the dimensions and the sources, tried to refute every verdict on 2026-11-11 (HWD-STM-001, Independent review). Each finding below was recomputed before it was acted on.

Table 1. Fixes.

| Fix | Row | Failure found | Options weighed | Fix made | Cost |
| --- | --- | --- | --- | --- | --- |
| F7 | S25, S41 | A 20 kg bucket cannot be turned over, so the orange well never floods and the dose does not mix | A stirring rod in the kit; drop the tablet into the empty bucket before filling (changes the C interface, so it stays under D4); pour through the well and stir | Bucket steps on the label: plug off, pour raw water through the well from a cup until the tablet has gone, stir 30 s with a clean stick, then flip the timer; mixing measured (TJ) | None |
| F8 | S3, S42 | The 1881 neck also fits 0.5 L bottles, where two 1 L tablets give 8 mg/L, above 5 | A smaller tablet for small bottles (another consumable); a label range | Blue insert labelled for bottles of 1 to 1.5 L (1.33 to 4.0 mg/L) | None |
| F9 | S36 | Tate's law for a non-wetting 1.2 mm LDPE orifice gives 0.017 to 0.020 mL drops, so three drops give 0.6 to 0.7 mg/L | More drops from the same tip (seven or more, error-prone); a wider orifice | D2 orifice 2.0 mm (0.028 to 0.033 mL per drop) and five drops per litre: 1.7 to 2.1 mg/L; drops weighed at TRL 4 | None |
| F10 | S26 | The 17.8 mm groove gave 19 % squeeze at nominal but 8 % at print tolerance (+/-0.1 mm) | A larger section (new O-ring); a deeper or shallower groove alone | Groove root 17.9 mm; bore +/-0.05 mm (reamed) and groove +/-0.03 mm (moulded at scale; the prototype insert is measured and reprinted to the gauge): 15.1 to 28.0 %, nominal 21.9 %, stretch 4.1 % | None |
| F11 | S23, S24 | The timer runs at air temperature: the 34 minute nominal read 23 minutes at 40 C at the low end of the tolerance | A claim of "at least 25 minutes" (disinfection would still hold, but the 30 minute rule would not); a longer nominal | 45 minute nominal at 25 C (fluid about 548,000 cSt by the Haberman-Sayre wall factor), at least 30.3 minutes at 40 C; run count one, two, three (94 and 167 minutes against 60 and 120 at the low tolerance), one flip fewer in cold water | Fluid grade only |
| F12 | S28 | While a tablet dissolves the well holds up to 3.5 g/L (1 L) and 22 g/L (20 L) of chlorine; polycarbonate is prone to stress cracking in hypochlorite | Keep PC and test; change the plug material | Clear plug in PETG for the prototype and clarified PP at scale; PC is not used; concentrate soak in TG | None |

## Calculation corrections (no design change)

- CT is now the residual at the end of the wait multiplied by the time (US EPA definition): 51 mg min/L in clear water at 30 minutes, against 53 by the integral used in version 0.1. The 4-log virus margin at 5 C is 6.4.
- No virus credit is taken above 5 NTU, since the CT tables assume low-turbidity water (S9).
- HOCl pKa is taken by temperature (Morris 1966: 7.75 at 5 C, 7.58 at 20 C, 7.54 at 25 C), and the EPA table is used directly over pH 6 to 9 rather than weighted again by the HOCl share (S12).
- Rows whose numbers rest on assumed demand, decay or tablet sizes were made Plausible: S4, S6, S19, S20, S21, S27. Dropped option row X4 is now Fails.

## Consequences

- BOM: no cost change (USD 9.15); the fluid, plug, label and pictogram specifications changed.
- CAD: only the insert O-ring groove root changed (17.8 to 17.9 mm) and the D2 tip name; `cad/fidelity.json` passes; drawings HWD-DWG-001, 002, 101 to 103 and the concept media were regenerated.
- Open: the timer capsule's expansion allowance (HWD-DEC-001 C5), and the field chlorine check (D7, awaiting Amish).

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
