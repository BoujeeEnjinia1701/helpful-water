---
doc_id: HWB-RSK-001
title: "Helpful Water B: bottle cartridge risk register and hazard analysis"
project: "Helpful Water B: bottle cartridge"
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
    change: "Project risks, preliminary hazard analysis and first-pass design FMEA (P3) for the B1 cartridge"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review: H3 chlorine order (F7) and H5 lumen hold-up with first flush (F6)"
---

# Helpful Water B: bottle cartridge risk register and hazard analysis

The top hazard is silent failure: a cracked fibre, a leaking header O-ring or a frozen module passes untreated water while the flow and taste seem normal, and good taste from the carbon builds false confidence. The second is misuse beyond the claims: drinking virus-risk or chemically contaminated water without co-treatment. The top project risks are an unknown membrane flux and a module that cannot be bought in this geometry. Method: STANDARDS section 23. Likelihood, impact, severity and occurrence are scored 1 (low) to 5 (high); detection 1 (sure to be found) to 5 (not found).

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Real module flux far below the assumed 1,000 L/(m2 h bar) | Assumption, no supplier data | Flow targets missed, mainly for children | 3 | 4 | Membrane engineer | Request flux at 10 kPa from two or three makers (C1); enlarge the module or move households to the gravity mode |
| R2 | No module of this geometry for sale | Most modules are proprietary to filter brands | Redesign around a bought header | 3 | 3 | Mechanical engineer | Draw the housing around the supplier's header (C3); keep the model parametric |
| R3 | Squeeze too hard for children and elderly users | Weak grip; fouled module halves flow | Low use; abandonment | 3 | 4 | Human-factors lead | Persona trials (TH); gravity mode (D1) |
| R4 | Neck finishes in the field differ | Many bottlers and regions | Collar does not fit | 3 | 3 | Field partner | Neck survey; adapters (D3) |
| R5 | Cost per user per year above USD 10 | Short carbon life; module life unknown | Weaker case to NGO buyers | 3 | 3 | Program lead | Measure capsule breakthrough; quotations at volume |
| R6 | Patent exposure | Squeeze and bottle filter patents not yet searched | Cannot distribute | 2 | 4 | Legal adviser | Desk search before P4; attorney opinion before distribution (D5) |
| R7 | No field partner | Not yet named | Requirements stay a desk draft | 3 | 4 | Amish with Helpful Engineering | Partner search (HWP-PLN-001) |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Pathogens pass a damaged membrane unnoticed | Freezing, a drop, over-pressure backflush, manufacturing defect | Diarrhoeal illness | 5 | 2 | Module maker's integrity test; field air check (shows openings above 17 um); retire after freezing or a hard drop; gentle backflush rule; accredited testing before any use (TB, TF) | 3 |
| H2 | Bypass at the header seal | O-ring damaged, missing or rolled; housing bore scored | Illness | 5 | 2 | Single seal line with two O-rings; capsule change never opens it; air check | 2 |
| H3 | Viral infection | Membrane is not a virus barrier | Illness | 5 | 3 | No virus claim; on-product warning and pictogram; pair with chlorine (solution D), dosed and left for its full contact time before filtering because the carbon removes the residual (F7) | 3 |
| H4 | Chemical exposure | Arsenic, nitrate, fluoride, fuel in the source | Chronic or acute harm | 5 | 2 | Exclusions on the product; source classes (HWP-SRC-001); SC6 and SC7 excluded | 3 |
| H5 | Regrowth on the clean side | Wet storage in heat; mouth or hand contact | Illness | 4 | 3 | Carbon moved to the dirty side (F1); 5.7 mL downstream of the potting drains but 15.2 mL stays wet in the lumens, so a 50 mL first flush after storage (F6); dust cover; grow-through and storage testing (TE, TG) | 2 |
| H6 | Leaching from parts | Uncertified plastics, potting or carbon; heat | Chemical exposure | 4 | 2 | NSF/ANSI/CAN 61 grades only (PR-013); extractables testing (TG) | 2 |
| H7 | Carbon fines or grains in the water | Damaged pads | Grit; no direct harm known | 2 | 2 | Membrane downstream of the carbon holds fines | 1 |
| H8 | Spray in the face during backflush | Hard syringe push, about 180 kPa | Eye contact with dirty water | 2 | 2 | Point away from the face; gentle push | 1 |
| H9 | Dirty water on hands at the duckbill | Valve leaks under squeeze | Recontamination of the outlet by hand | 3 | 2 | Duckbill closes under squeeze; leak check (PR-027) | 2 |

## Design FMEA (first pass, P3)

Table 3. Failure modes. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Fibre bundle | Size barrier | Broken or split fibre | Bypass of pathogens | Freezing, drop, over-pressure | 5 | 2 | 3 | 30 | Air check after any suspected damage; retire rule; supplier backwash limit (C2) |
| F2 | Fibre bundle | Size barrier | Pinhole defect under 17 um | Small bypass not seen by the air check | Manufacturing | 5 | 2 | 5 | 50 | 100 % supplier integrity test (TI); accredited challenge (TB) |
| F3 | Header O-rings | Dirty-to-clean seal | Rolled or cut at assembly | Bypass | Insertion over a rough bore | 5 | 2 | 3 | 30 | Smooth bore finish; lead-in chamfer; air check after assembly |
| F4 | Potting | Seal fibres to header | Void or debond | Bypass | Supplier process | 5 | 1 | 4 | 20 | Bought tested modules only |
| F5 | Fibre bundle | Flow | Fouling | Flow below targets | Turbid water | 3 | 4 | 1 | 12 | Backflush; settle turbid water; mesh upstream |
| F6 | Carbon capsule | Taste | Exhausted carbon | Taste returns; trust drops | Use beyond capsule life | 2 | 4 | 3 | 24 | Capsule life from breakthrough (TG); date or volume marker |
| F7 | Carbon capsule | Taste | Clogged with silt | Higher pressure drop | Turbid water | 2 | 3 | 2 | 12 | Mesh upstream; rinse or replace |
| F8 | Collar gasket | Neck seal | Leak at the neck | Water on hands; lost pressure | Unfamiliar neck, worn gasket | 3 | 3 | 1 | 9 | Neck survey; spare gaskets |
| F9 | Duckbill | Air return | Stuck shut | Bottle stays crushed | Dirt, low springback | 2 | 3 | 1 | 6 | Rinse; cracking pressure from the supplier (C5) |
| F10 | Duckbill | Seal under squeeze | Leaks outward | Dirty water on hands | Wrong orientation, damage | 3 | 2 | 2 | 12 | Assembly check (PR-027) |
| F11 | Push-pull valve | Open and shut | Leaks shut | Drips; clean outlet wetted | Worn O-ring | 2 | 3 | 1 | 6 | Spare O-ring |
| F12 | Housing | Contain pressure | Cracks at a layer line | Leak; possible bypass if at the header | Print defect, impact | 4 | 2 | 2 | 16 | Four perimeters; factor 6; moulded at scale |
| F13 | Collar thread | Hold on the neck | Strips | Cartridge comes off | Over-tightening a printed thread | 2 | 2 | 1 | 4 | Hand tight; seal on the gasket |
| F14 | Clean side | Hygiene | Biofilm in the spout | Contamination | Wet storage, mouth contact | 4 | 3 | 4 | 48 | Drain and dry; dust cover; cup filling; storage tests (TE, TG) |

Highest RPN: F2 (50), F14 (48), F1 and F3 (30). All are controlled by laboratory work at TRL 4 and none can be closed on paper.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
