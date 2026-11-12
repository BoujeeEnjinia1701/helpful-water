---
doc_id: HWB-FEA-001
title: "Helpful Water B: bottle cartridge feasibility assessment"
project: "Helpful Water B: bottle cartridge"
doc_type: Feasibility assessment
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Feasibility closed for P3 on paper; supply of a matching pre-potted module is the main uncertainty"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review recorded: weak-child flow 160 mL/min, fixes F5 to F9, D8 and D9"
---

# Helpful Water B: bottle cartridge feasibility assessment

Overall verdict: feasible on paper with known parts and processes; the main uncertainty is buying a pre-potted hollow-fibre module of this geometry with a published flux, and the main performance risk is flow at a weak child's squeeze once the module fouls. Method: STANDARDS section 23.

Table 1. Feasibility by aspect.

| Aspect | Assessment | Rating | Risks and notes | Evidence |
| --- | --- | --- | --- | --- |
| Design | Every claim within known science or plausible; nine detail fixes made; D3 model passes the fidelity check | High | Flow rests on assumed permeability and 20 C water (D9); independent STEM review run 2026-11-11, five more fixes (F5 to F9), end wall at a blocked backflush proposed (D8) | HWB-STM-001, HWB-CAL-001, `cad/fidelity.json` |
| Materials | PP, EPDM or silicone, 316L, PVDF or PES fibres, coconut GAC: all available in drinking-water grades | Medium | Printed PP filament certificates; potting extractables; PET bottle reuse (HWB-REG-001 B11) | HWB-REG-001 |
| Manufacturing and assembly | Seven printed parts, no glue, no in-house potting, hand assembly in nine steps; injection moulding at scale with thread cores | High | Printed threads and the 37 mm bore finish need care | HWB-BLD-001 |
| Power and controls | None | High | Not applicable | |
| Supply of parts | Seals, mesh, carbon, syringe and duckbill are catalogue items; the module needs a request for quotation | Medium | No module chosen; header geometry may need to follow the supplier's (C1 to C3) | `bom/bom.csv`, HWB-DEC-001 |
| Performance | 465 mL/min adult, 160 weak child (clean, estimates); half that fouled | Medium | PR-005 and PR-006 at risk fouled | HWB-CAL-001 section 3 |
| Cost | USD 18.35 prototype; USD 7.05 at scale; USD 10.8 per user per year (9 months) | Medium | Over the per-year target unless the life is 12 months or the capsule lasts longer | HWB-CAL-001 section 7 |

Ratings: High, Medium, Low.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
