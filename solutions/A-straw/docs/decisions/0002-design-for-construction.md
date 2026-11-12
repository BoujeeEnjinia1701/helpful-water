---
doc_id: HWA-DDR-002
title: "Helpful Water A: filter straw design for construction"
project: "Helpful Water A: filter straw"
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
    change: Rev A made constructable (STANDARDS section 18)
---

# 0002: Design for construction

- **Date:** 2026-11-11
- **Status:** made for construction (STANDARDS section 18, Amish 2026-09-30: "fix the design assumptions to match and be physically feasible"); nothing here changes what the straw does, its pitch or its safety case

## Context

The Rev A specification stacks its modules axially (15 + 10 + 125 + 30 + 25 mm) and leaves joints, fixings and the backflush routing open. A part that cannot be made, fitted or fixed as drawn is changed to the simplest sound design.

## Changes

| Component | Rev A had | The constructable design has | Why |
| --- | --- | --- | --- |
| End joints | Not defined | Quarter-turn bayonets: two lugs on each spigot in a groove ring with two entry slots inside the bore | A thread on a 2 mm wall leaves under 1.1 mm at the root, or pushes the outside past 30 mm; internal bayonets keep 26 mm |
| Module stop | Not defined | Seat ring inside the housing, 17 mm bore, 22 to 24 mm from the intake face; the module cage has feet | The module needs a stop that leaves the mesh bay open |
| Mesh | Disc "nominal 22 mm" | 17 mm disc captive in the intake cap under a press-fit retaining ring | Rinse the mesh with the cap off without losing it (UR-019) |
| Header | Not dimensioned | 6 mm space above the top potting, held open by three legs under the carbon cartridge | The legs stand on the module collar, so the cartridge cannot close the lumens |
| Backflush port | "Captive-sealed port, luer or barb to choose" | Luer-slip taper socket (4.3 to 3.9 mm, 5 mm deep) in an 8 mm boss on the header, closed by a tethered silicone plug | A luer-lock socket stands 8 mm proud and makes the straw 32 mm across; the shortened slip socket keeps it at 29.6 mm |
| Mouthpiece cap | "Hygienic protective cap" | Snap cap with a 4.9 mm plug in the bore and a lanyard eye | The plug dead-ends the carbon during backflush (F4) |
| Dip line | Not defined | Groove round the housing at 110 mm | The header, socket and mouthpiece joint must stay above the water, so dirty water cannot reach a clean-side seal |
| Carbon fines screen | "Pore, area and binder to qualify" | 150 um 316L disc under the bed, a non-woven PP pad over it | Bought stock; the pad permeability is to confirm (C6) |

## Consequences

Twenty-six parts at D3, every made part printable in polypropylene for the prototype and mouldable at scale; the bought module is the only part that must come from a specialist. The build plan (HWA-BLD-001) follows this design.


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
