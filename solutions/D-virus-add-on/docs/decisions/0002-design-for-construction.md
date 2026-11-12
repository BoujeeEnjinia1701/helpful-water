---
doc_id: HWD-DDR-002
title: "Helpful Water D: design for construction"
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
    change: Changes made so every D1 part can be made and fitted
---

# Helpful Water D: design for construction

**Status:** changes made to the model so that every D1 part can be printed, cut or bought and fitted (STANDARDS section 18; Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). None changes what the product does, its pitch or its safety case.

## Changes

1. **Timer pivot.** A through pin at the capsule's centre would cross the tube bore and stop the ball. The hub now carries two moulded 2 mm trunnions that run in a 2.2 mm hole in the slot wall and one in the window.
2. **Capsule length.** At 23 mm the capsule's corners swept a radius larger than the slot's half height and it could not turn over. The tube is 18 mm with 1.5 mm caps (21 mm overall, corner radius 10.9 mm against 11.25 mm).
3. **Timer outside the water space.** The timer sits in its own side slot behind a screwed window, so no seal is needed around it and the fluid never meets the water.
4. **Crown coring.** The crown was 10 mm thick; a 4 mm coring groove 12 mm deep, kept clear of the timer boss and the plug O-ring, gives even walls for printing and moulding.
5. **Insert floor.** The 1 L insert's floor became 7.5 mm thick when the plug stop was added; it is hollowed from below, leaving a central boss that carries the four slots.
6. **Drawing and STEP.** Each made part is drawable on its own (HWD-DWG-101 to 107) and exported as STEP in `cad/step/D1/`.

## Checks

`python .kit/cad_check.py --export` passes at D3 for all three options with no interference beyond the listed seal and fluid contacts (`cad/fidelity.json`).

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
