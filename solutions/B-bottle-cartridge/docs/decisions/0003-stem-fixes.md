---
doc_id: HWB-DDR-003
title: "Helpful Water B: STEM check fixes F1 to F9"
project: "Helpful Water B: bottle cartridge"
doc_type: Decision record
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Four detail failures found by the first STEM check fixed under Amish's standing instruction of 2026-10-23"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "F5 to F9 added after the independent STEM review of 2026-11-11, under the same instruction"
---

# Helpful Water B: STEM check fixes F1 to F9

**Status: Decided under Amish's standing instruction of 2026-10-23** (STANDARDS section 20, fix rule). Each fix keeps the working principle of its option; Amish can reverse any of them. The STEM check was rerun after the fixes (HWB-STM-001).

## F1: carbon upstream of the membrane (B1, B2, B3; row S18)

**Failure.** The brief placed the carbon downstream of the membrane. Wet carbon after the membrane can harbour microorganisms on the clean side in warm storage (Rev A specification section 05; concept validation questions, item 21), and the backflush would need a separate path around the carbon.
**Options weighed.** (a) Keep it downstream and add silver-impregnated carbon: adds a biocide claim and registration (HWP-REG-001 W9) and silver leaching. (b) Keep it downstream with a bypass valve for backflush: more parts and a second clean-side seal. (c) Move it to a dirty-side capsule upstream of the membrane: the membrane becomes the last barrier; fines and any regrowth in the bed are held by the membrane; backflush runs with the capsule out.
**Chosen.** (c). Cost: none extra. Trade-off: the carbon sees turbid water and may clog faster, so the mesh sits upstream of it and settling is advised for turbid sources; any chlorine co-treatment (solution D) is done in the bottle before filtering, so its contact time is not shortened.

## F2: duckbill air valve (B1; row S19)

**Failure.** A wetted 0.1 um membrane holds air to about 2,900 kPa, so after a squeeze no air can return through the outlet and the bottle stays crushed.
**Options weighed.** (a) Unscrew to let air in: breaks the seal each time and wets hands with dirty water. (b) A vent hole: leaks dirty water under squeeze. (c) A one-way silicone duckbill in the collar, opening inward at about 0.5 kPa (assumed) and closing under squeeze.
**Chosen.** (c). Cost about USD 0.40. Open: springback of a 1 L bottle against the cracking pressure, to test (TH).

## F3: wider stand base (B2; row S20)

**Failure.** With a 130 mm base ring the full stand tips at about 9.9 deg (centre of gravity 372 mm up).
**Chosen.** An outer base ring of 230 mm on three spokes: 17.2 deg, against a 15 deg criterion (assumed). Cost: about 60 g more printed PP.

## F4: vent tube for the inverted bottle (B2; row S21)

**Failure.** The inverted bottle cannot take in air through the wetted membrane, so it goes to a partial vacuum and the drip stops.
**Chosen.** A 4 x 0.8 mm silicone tube from the collar's duckbill up into the bottle's air space, so the air pocket stays near atmospheric pressure (Mariotte principle); the duckbill stops dirty water leaving through the tube. Cost about USD 0.60 (estimate).

## F5: upright refill (B1; row S19)

**Failure found by the independent review.** Tipped for drinking, the duckbill sits under up to about 240 mm of water and needs about 2.9 kPa of bottle vacuum to open, more than a thin still-water bottle may give on springback.
**Chosen.** The bottle is turned upright on release, so the valve is in the air space and opens at about 0.5 kPa. Cost: none; one pictogram. Keeps the duckbill (F2).

## F6: first flush after storage (B1, B2, B3; row S22)

**Failure found by the independent review.** The stated 5.7 mL clean side that "drains and dries" left out the 15.2 mL in the 800 lumens, which capillary rise (about 60 mm in a 0.5 mm bore) keeps wet; bacteria can grow through a 0.1 um membrane over days of wet storage.
**Chosen.** Discard the first 50 mL (more than twice the 21 mL wet clean side) after any storage; grow-through tested in storage cycles (TE, TG). Cost: none.

## F7: chlorine before filtering, with its full contact time (all options; row S28)

**Failure found by the independent review.** The carbon upstream of the membrane removes free chlorine within seconds, so chlorine dosed just before filtering would get almost no contact time and no virus inactivation.
**Chosen.** The instruction and pictogram give the order: dose in the bottle, wait solution D's full contact time, then filter; the filtered water has no residual and is used the same day. Cost: none.

## F8: priming by backflush (B1, B2, B3; rows S30, S33)

**Failure found by the independent review.** Air left in the dirty-side shell cannot cross the wetted membrane or rise through the wet bed at a gravity head, so it can cover fibres; dried fibres can dewet.
**Chosen.** If the first flow is low, or after the cartridge has dried, prime it with a syringe backflush (capsule out, collar end open), which fills the shell from the fibres outward and pushes the air out. PR-007's two-squeeze priming stays the normal case. Cost: none; the syringe is already supplied.

## F9: module request (all options; rows S29, S30, S17)

**Failure found by the independent review.** The module request did not name a hydrophilic fibre (plain PVDF passes no water at a few kPa), the potting load at a hard backflush (135 N), the 53 % packing or a production integrity test of each module.
**Chosen.** BOM item 8 and HWB-DEC-001 C1 and C2 now ask for all four. Cost: none at TRL 3.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
