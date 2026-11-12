---
doc_id: HWA-RSK-001
title: "Helpful Water A: filter straw risk register and hazard analysis"
project: "Helpful Water A: filter straw"
doc_type: Risk register and hazard analysis
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: Project risks, preliminary hazard analysis and first-pass design FMEA for option A1
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "After the independent STEM review: FMEA rows F11 to F13 (reverse pressure, shell air, syringe water); air check wording"
---

# Helpful Water A: filter straw risk register and hazard analysis

The top risks are a fibre or seal that fails silently, users believing the straw covers viruses or chemicals, and a flow too low for children, so the straw is abandoned. Method: STANDARDS section 23. Likelihood, impact, severity and occurrence are scored 1 (low) to 5 (high); detection 1 (sure to be found) to 5 (not found). Kill criteria are in HWA-PLN-001.

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Flow too low at the grade that gives the log reductions | Membrane permeability (HWA-CAL-001 section 4) | Users stop using it; kill criterion | 4 | 5 | Membrane engineer | Test 0.1 and 0.2 um grades side by side (D2); persona trials (TH) |
| R2 | No supplier for a module to the drawing | Niche geometry | Delay; redesign round a stock core | 3 | 4 | Mechanical engineer | RFQ to several straw-core makers (C1); housing parametric |
| R3 | Patent exposure | US 8,852,439 B2 family until about 2029-12-18 | Cannot distribute | 2 | 5 | Program lead | Attorney opinion (C4) |
| R4 | Carbon resupply fails in the field | Displaced populations | Carbon spent; taste returns; growth | 3 | 3 | NGO liaison | No-carbon variant (D7); replacement by volume |
| R5 | Laboratory testing cost | USD 50,000 to 150,000 (HWP-PLN-001) | Gate P4 slips | 3 | 4 | Program lead | Share test campaigns across A to C |
| R6 | Users misread the claims | Straws are marketed as making water safe | Harm; liability | 3 | 5 | Industrial designer | On-product warning and pictograms (PR-008) |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Pathogens pass a broken fibre | Freezing, drop, ageing | Waterborne infection | 5 | 3 | Warning; air check (D4, gross defects only); replace after a hard drop or suspected freeze | Medium until the check is validated |
| H2 | Dirty water bypasses the membrane | O-ring damage, misassembly, immersion past the dip line | Infection | 5 | 2 | Two O-rings in series; dip line; plug and cap seals; factory assembly of the module | Low to medium |
| H3 | Viral infection | User assumes virus protection | Infection | 5 | 3 | No virus claim; warning; co-treatment (solution D) | Medium (behaviour) |
| H4 | Chemical exposure | Arsenic, nitrate, fuel in the source | Chronic or acute poisoning | 5 | 2 | Source classes (HWP-SRC-001); exclusions on the product | Medium (behaviour) |
| H5 | Bacterial growth in the carbon or header | Wet storage in heat, no chlorine residual | Infection, taste | 4 | 3 | Drain and dry, caps, replacement by volume; regrowth test (TG) | Medium |
| H6 | Clean side contaminated during service | Carbon change, dirty syringe, mouth backflush | Infection | 4 | 3 | Socket on the header; syringe only; clean-hands instruction; D6 combined top | Medium |
| H7 | Leachables | Potting, printed plastics, rubber | Chemical exposure | 3 | 2 | Listed grades; prototypes not drunk from | Low |
| H8 | Mouth-to-mouth transmission | Shared mouthpiece | Infection | 3 | 3 | Cap; one mouthpiece per person (D6) | Medium |
| H9 | Choking on a small part | Plug or cap detaches | Choking (child) | 4 | 1 | Tethered plug; cap with lanyard; parts above 10 mm except the plug, which is tethered | Low |

## Design FMEA (first pass, P3)

Table 3. Failure modes. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Hollow fibres | Pathogen barrier | Fibre cracks | Silent pass of pathogens | Freezing, drop | 5 | 3 | 4 | 60 | Air check to the 6 mL mark (D4, F7); laboratory validation (TA, TF); warning |
| F2 | Module collar O-rings | Clean/dirty seal | Ring nicked or rolled | Bypass | Insertion past the bore edge | 5 | 2 | 3 | 30 | Reamed band; hold point in BLD step 1; a lead-in chamfer at the housing top proposed for the next model revision |
| F3 | Top potting | Clean/dirty seal | Delamination | Bypass | Freeze-thaw, ageing | 5 | 2 | 4 | 40 | Supplier qualification (TI); air-hold check |
| F4 | Fibre lumens and membrane | Flow | Fouling | Flow falls; user gives up | Turbid water | 3 | 4 | 1 | 12 | Mesh; backflush; source classes; TE |
| F5 | Carbon bed | Taste | Exhausted | Taste returns; growth | Volume past breakthrough | 2 | 4 | 4 | 32 | Replacement by volume; tally on pictogram; D7 |
| F6 | Carbon bed | No new hazard | Biofilm | Bacteria in the water | Wet storage | 4 | 3 | 5 | 60 | Drain and dry; TG regrowth test; D6 |
| F7 | Mouthpiece cap plug | Dead-ends carbon in backflush | Leaks | Backflush through carbon, fines to the mouth | Worn plug | 2 | 3 | 2 | 12 | Plug check in BLD 3.6; test TE |
| F8 | Backflush plug | Seals the header | Missing or loose | Dirty water or air drawn into the clean header | Plug left out | 5 | 2 | 3 | 30 | Tether; socket above the dip line; pictogram |
| F9 | Bayonets | Hold the ends | Turn loose | Parts separate | Wear, children | 2 | 2 | 1 | 4 | Detent in the groove at P4 |
| F10 | Mesh | Stop grit | Torn | Faster membrane fouling | Rinsing with a brush | 2 | 2 | 2 | 8 | 316L; rinse only |
| F11 | Fibres and potting | Pathogen barrier | Damaged by reverse pressure | Silent pass of pathogens | A firm push on the syringe (about 190 kPa at 60 N) | 5 | 3 | 4 | 60 | Supplier reverse rating (C2); pressure limit (D11); "push gently" pictogram |
| F12 | Dirty shell | Feed the whole fibre length | Air pocket | Flow falls by a quarter or more; user gives up | Straw lifted out and drained; after the air check | 3 | 4 | 2 | 24 | Intake cover between uses (F8); re-prime or vent (D10); TC |
| F13 | Backflush syringe | Clean water for backflush | Filled from the source | Raw water on the clean side | User error | 5 | 3 | 4 | 60 | Instruction and pictogram: treated water only (F11); TH comprehension |

Highest RPN: F1 fibre cracking and F6 carbon biofilm (60 each), then F3 potting (40).


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
