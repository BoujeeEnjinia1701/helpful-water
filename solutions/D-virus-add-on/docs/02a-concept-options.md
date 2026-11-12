---
doc_id: HWD-OPT-001
title: "Helpful Water D: chlorine add-on for viruses concept options"
project: "Helpful Water D: chlorine add-on for viruses"
doc_type: Concept options
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: Three options with different working principles, modelled to D3, scored against HWD-URS-001; D3 dropped on the STEM check
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Timer and D2 dropper figures updated after the independent review (F9, F11); STEM summary updated
---

# Helpful Water D: chlorine add-on for viruses concept options

Recommendation: option D1, the tablet dose cap with a ball timer, scores 174 of 215 against 143 for the metered liquid doser (D2) and 85 for the erosion feeder (D3), more than 10 % ahead of D2; D3 also fails the STEM check on its working principle and is dropped. The choice is **Proposed, awaiting Amish** (HWD-DEC-001 D1, HWD-DDR-001). Method: STANDARDS section 21. All three options are modelled to detail level D3 in `cad/src/model.py`; the side-by-side options picture is rendered in Blender on Amish's Mac from the scenes in the render queue (`media/options.png` is not yet made).

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The options

### Option D1: tablet dose cap with ball timer

Working principle: one NaDCC tablet matched to the container (3.5 mg for 1 L, 67 mg for 20 L) sits in a colour-keyed well in a cap that screws onto the 28 mm PCO 1881 bottle neck or a 28 mm port on C's raw bucket lid; turning the container over and shaking floods the well through floor slots and dissolves the tablet to about 2 mg/L; a flip-over ball timer (a 2 mm steel ball falling 13 mm through sealed silicone fluid) shows about 45 minutes (at least 30 up to 40 C). First-order numbers: 52 x 41 x 52 mm, 45 g, 21 parts, USD 9.15 of prototype parts and test tablets. STEM check: no Fails row; six details fixed (F1 to F6) and six more after the independent review (F7 to F12). Key risks: the tablet sizes are assumed until measured; the ball timer needs its fluid grade tuned; no residual survives carbon after filtering (S16). Needs from a partner: the tablet sizes in their kits; a water chemist and a laboratory for the TJ family.

### Option D2: metered liquid doser with ball timer

Working principle: a 150 mL bottle of 1.25 % sodium hypochlorite (the CDC Safe Water System strength) carries a head whose squeeze-to-fill chamber holds 3.0 mL below a standpipe, the dose for 20 L; a 2.0 mm dropper orifice gives five drops (about 0.15 mL, Tate's law) for 1 L; the same ball timer sits on the head. First-order numbers: 50 x 150 mm, 58 g with the bottle (empty), 24 parts. STEM check: no Fails row; open on drop size (S36) and on liquid strength, which falls with age and heat to about 55 % in 3 months on a warm bound (S37), an under-dose the user cannot see. Key risks: the 3 month use-by, spills, child access. Needs from a partner: a local SWS hypochlorite producer.

### Option D3: erosion feeder in the raw bucket (dropped)

Working principle: three calcium hypochlorite tablets in a perforated PVC tube hung in C's 20 L raw bucket from a rim hook dissolve slowly; a rotating sleeve sets how many of the 12 holes are open. First-order numbers: 119 g, 21 parts. STEM check: **Fails** (X1, X2): in a still bucket the dose grows with standing time, which runs from 30 minutes to a day (a ratio of 48 against the 5 that the 1 to 5 mg/L band allows), so it either reaches about 96 mg/L overnight or gives 0.1 mg/L at 30 minutes. TCCA pool tablets add a nitrogen trichloride hazard (X3). Erosion feeders work in flowing water, not in a batch bucket. Dropped.

## First-order numbers

Table 1. First-order numbers (HWD-CAL-001).

| Quantity | D1 tablet dose cap | D2 liquid doser | D3 erosion feeder |
| --- | --- | --- | --- |
| Dose per container | 2.0 mg/L (1 L or 20 L), 4.0 turbid | 1.9 mg/L (3 mL per 20 L or 5 drops per 1 L), 3.75 turbid | Not controllable (X1) |
| Dose spread | Tablet tolerance (to measure) | 1.3 to 2.4 mg/L by drop size; falls with liquid age | 0.1 to 96 mg/L |
| Contact indicator | Ball timer, about 34 min | Same | None defined |
| Consumable shelf life | Strips 5 years | About 3 months (use within) | To assess |
| Parts | 21 | 24 | 21 |
| Mass | 45 g | 58 g (bottle empty) | 119 g |
| Cost per litre (consumable) | USD 0.0006 (20 L tablets) to 0.011 (1 L), humanitarian price | USD 0.0003 (USD 0.33 per 1,000 L bottle) | To assess |
| Containers served | 1 L bottles (A, B), C bucket port | Any container | C bucket only |

## Scoring

Criteria are the user requirements of HWD-URS-001 weighted by priority (High 3, Medium 2, Low 1), plus buildability (2), safety (3) and maintenance (1). Each option scores 1 to 5 with a one-line reason.

Table 2. Weighted scoring.

| Criterion | UR | Weight | D1 | D2 | D3 | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Viruses addressed | UR-003 | 3 | 4 | 3 | 1 | Fixed tablet dose; liquid drifts with age; feeder uncontrolled |
| Right dose, no overdose | UR-101 | 3 | 5 | 3 | 1 | Keyed wells and two-tablet stop; drops and streams vary; dose follows time |
| Knows the contact time | UR-102 | 3 | 4 | 4 | 2 | Both carry the timer; continuous dosing has no start |
| Ready to use, no tools | UR-005 | 3 | 4 | 4 | 3 | All tool-free; the feeder needs setting |
| Simple instructions | UR-006 | 3 | 4 | 3 | 3 | One tablet, shake, wait; two dose modes for D2 |
| Knows when it fails | UR-008 | 3 | 4 | 2 | 1 | Tablet seen dissolving; aged liquid invisible; no indication |
| Safe materials and chemistry | UR-011 | 3 | 4 | 3 | 1 | Solid tablets; liquid spills and child access; overdose and NCl3 |
| Affordable | UR-014 | 3 | 4 | 5 | 3 | Tablets cheap per 20 L; liquid cheapest per litre |
| Works with A, B and C in order | UR-103 | 3 | 4 | 4 | 2 | Neck and port; any container; C only |
| Resupply | UR-015 | 2 | 4 | 3 | 2 | NaDCC in humanitarian catalogues; SWS liquid where produced; less standard tablets |
| Shelf life and transit | UR-016 | 2 | 5 | 2 | 3 | 5 year strips; 3 month liquid |
| Taste | UR-018 | 2 | 3 | 3 | 1 | Both about 2 mg/L before carbon; overdose taste |
| Cloudy and cold water | UR-104 | 2 | 4 | 4 | 1 | Two-tablet and run-count rules; same; none |
| End of life | UR-021 | 1 | 3 | 3 | 3 | Plastics and foil |
| Regional manufacture | UR-022 | 1 | 4 | 4 | 4 | Printed or moulded parts |
| Buildability with local skills | | 2 | 4 | 3 | 4 | Seven printed parts; metering head tolerances; simple tube |
| Safety | | 3 | 4 | 3 | 1 | Solid dose; corrosive liquid near children; overdose |
| Maintenance | | 1 | 4 | 4 | 2 | Rinse; rinse; refill and re-set |
| **Weighted total (of 215)** | | | **174** | **143** | **85** | |

D2 is 17.8 % behind D1, outside the 10 % band, so a single recommendation is made.

## Recommendation

Carry D1, the tablet dose cap with ball timer (**Proposed, awaiting Amish**, HWD-DEC-001 D1). Runner-up's best idea to graft on: D2's metering chamber and dropper are the right tool where a partner already distributes SWS liquid; the shared ball timer can be offered as a stand-alone clip for those households, without the cap.

## Patent comparison: claim 1 of US 8,852,439 B2 (HWP-FTO-001)

None of the options is a hollow-fibre straw or bottle filter, so claim 1 of US 8,852,439 B2 (a method of drinking through a straw with one bundle of hydrophilic hollow fibres, inside-out flow, closed ends toward the outlet) does not read on D.

Table 3. Elements of claim 1 against the options.

| Element of claim 1 (as summarised in HWP-FTO-001) | D1 | D2 | D3 |
| --- | --- | --- | --- |
| Drinking straw with a hollow-fibre bundle | No; a bottle or bucket cap | No; a dosing bottle | No; a bucket feeder |
| Hydrophilic fibres potted with closed ends toward the outlet | No fibres | No fibres | No fibres |
| Water enters the lumens and passes outward through the walls | No; chemical dosing | No | No |

Dosing caps, tablet dispensers, liquid dose chambers and timers are to search at P1 (HWP-FTO-001 row 3); the design uses long-established public principles (a tablet in a container, a measuring chamber, a falling-ball timer). Not legal advice; an attorney confirms.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
