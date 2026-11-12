---
doc_id: HWC-PRS-001
title: "Helpful Water C: household gravity filter product requirements and specifications"
project: "Helpful Water C: household gravity filter"
doc_type: Product requirements
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First product requirements for option C1 carried to the TRL 3 documents, statuses from HWC-CAL-001"
---

# Helpful Water C: household gravity filter product requirements and specifications

What the C1 filter must do, each requirement traced to a user need in HWC-URS-001 (links in HWC-RTM-001). The requirements describe option C1, the two-bucket hollow-fibre filter carried to the drawings, BOM and build plan; the concept choice is Amish's (HWC-DEC-001 D1). Of 30 requirements, 20 are met on paper or by design, 7 are to verify at TRL 4, 2 are at risk and 1 is over the value-engineering target. Every flow figure rests on an assumed membrane permeability that the module maker must confirm (HWC-DEC-001 C1). Targets are proposals for review with a co-design partner. Planned tests cite the HWP-VER-001 families TA to TJ; none is run at TRL 3.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Bacteria reduction | The bought module shall carry a supplier-stated absolute or nominal rating of 0.1 um or finer and, assembled, shall target a bacteria log reduction of at least 3 (first gate) toward the WHO three-star 4 log | 3 | min | log10 | Supplier certificate (TA) and accredited challenge at beginning and end of life (TB), TRL 4 | To verify at TRL 4 |
| PR-002 | UR-002 | Performance | Protozoa reduction | The assembled filter shall target a cyst-surrogate log reduction of at least 3 toward the WHO three-star 4 log | 3 | min | log10 | Accredited challenge (TB), TRL 4 | To verify at TRL 4 |
| PR-003 | UR-003, UR-006 | Safety | Chlorine interface and no-virus warning | The raw lid shall carry a 60 mm dosing port for solution D, the valve a "shut 30 minutes after dosing" tag, and the raw bucket the HWP-CLM-001 warning and pictogram | 1 | none | interface | Inspection of the model (HWC-DWG-001), TRL 3; comprehension (TH) and dosing with D (TJ), TRL 4 | Met by design |
| PR-004 | UR-003, UR-101 | Performance | Residual reaches storage | No stage downstream of the dosing point shall remove free chlorine (no carbon), so a residual reaches the clean bucket | 0.2 | min | mg/L free chlorine at 24 h with D | Residual at 1 and 24 h with D (TJ), TRL 4 | Met by design; residual to verify |
| PR-005 | UR-013 | Performance | Daily volume | The filter shall treat 45 L in no more than 3 h of filtering with the module at half its clean permeability (settling and contact time come on top: about 6 to 8 h elapsed for three batches) | 3 | max | h of filtering per day | Analysis (HWC-CAL-001 section 4), TRL 3; pressure-flow map (TC), TRL 4 | Met on paper (1.6 h clean, 2.8 h fouled; assumed permeability) |
| PR-006 | UR-004 | Usability | Tap draw | Drawing a 250 mL cup from the tap shall take no more than 15 s with 5 L in the clean bucket, with no force beyond opening the tap | 15 | max | s | Analysis (HWC-CAL-001 section 6), TRL 3; persona trials (TH), TRL 4 | Met on paper (8.6 s) |
| PR-007 | UR-004, UR-007 | Usability | Backflush effort | A backflush shall need no more than a 50 N push on the 60 mL syringe | 50 | max | N | Analysis (HWC-CAL-001 section 6), TRL 3; TH, TRL 4 | Met on paper (30 N gives 54 kPa) |
| PR-008 | UR-005 | Usability | Ready on day one | Once the stand is built, the filter shall need no ripening and no tool before the first batch | 0 | max | days of ripening | Inspection of the procedure (HWC-BLD-001), TRL 3; TH, TRL 4 | Met by design |
| PR-009 | UR-006 | Usability | Pictogram instructions | Filling, dosing, filtering, backflush, the air test and retirement shall each be shown in three pictogram steps or fewer | 3 | max | steps per task | Inspection of the label artwork, TRL 3; comprehension trial (TH), TRL 4 | To verify at TRL 4 |
| PR-010 | UR-007 | Maintenance | Daily upkeep | A backflush (three 60 mL strokes of water from the clean tap) and a cloth rinse shall take under 2 minutes with no tool | 2 | max | min | Analysis of the procedure (HWC-BLD-001 section 5), TRL 3; TH, TRL 4 | Met on paper |
| PR-011 | UR-008 | Safety | Air hold test | An air hold at 100 kPa, pumped by the syringe through a luer check valve until a firm 56 N push holds, shall show bubbles in the clear raw hose from any opening larger than 5 um | 5 | max | um | Analysis (HWC-CAL-001 section 5), TRL 3; defect-seeded test (TF, TI), TRL 4 | Met on paper (2.9 um); not a proof of performance |
| PR-012 | UR-008 | Safety | Retirement signal | The label shall give two retirement triggers: a batch taking more than 2 h after three backflushes, and the batch tally reaching the module's rated volume (30,000 L assumed) | 2 | max | h per batch | Inspection, TRL 3; fouling and life test (TE), TRL 4 | To verify at TRL 4 |
| PR-013 | UR-009 | Safety | One dirty-to-clean boundary | The only dirty-to-clean boundary shall be the module potting; the clean side shall run above atmospheric pressure while filtering; backflush water shall come from the clean tap | 1 | none | boundary | Inspection of the model (HWC-DWG-002), TRL 3; bypass tests (TF), TRL 4 | Met by design (1.7 kPa clean-side pressure) |
| PR-014 | UR-010, UR-101 | Safety | Closed clean bucket | The clean bucket shall be closed by a lid with the inlet fitting and a screened vent (0.5 mm), and emptied only through the tap | 0.5 | max | mm opening | Inspection, TRL 3; storage recontamination test (TE), TRL 4 | Met by design |
| PR-015 | UR-010 | Safety | Clean-side hold-up | Water standing on the clean side between batches (lumens, tee, clean hose) shall be no more than 100 mL | 100 | max | mL | Analysis (HWC-CAL-001 section 5), TRL 3; regrowth (TE, TG), TRL 4 | Met on paper (83 mL, 52 mL of it in the lumens); regrowth to verify |
| PR-016 | UR-011 | Materials | Wetted materials | Every wetted part shall be a grade certified to NSF/ANSI/CAN 61 (or an equal scheme), lead-free to NSF/ANSI/CAN 372; no plasticised PVC hose, no brass | 100 | min | % of wetted parts | Supplier certificates and extractables (TG), TRL 4 | To verify at TRL 4 |
| PR-017 | UR-014 | Cost | Cost | Prototype parts shall be reported against the USD 60 value-engineering target, with the cost per litre and per person per year over the module life | 60 | target | USD | Analysis (BOM, HWC-CAL-001 section 7), TRL 3 | Over target (USD 86.40; USD 0.003 a litre; USD 9.44 per person per year) |
| PR-018 | UR-015 | Logistics | No routine consumable | The only replaced parts shall be the module (at its rated life, about two years) and the cotton cloth | 2 | max | replaced parts | Inspection of the BOM, TRL 3; life test (TE), TRL 4 | Met by design (module life assumed) |
| PR-019 | UR-016 | Environment and durability | Shelf life | The kit shall be packed dry with the module sealed and shall state a storage range from the module maker | 1 | none | stated range | Supplier data (TA), shelf-life ageing (TF), TRL 4 | To verify at TRL 4 |
| PR-020 | UR-017 | Environment and durability | Freezing and knocks | The label shall carry a do-not-freeze pictogram and a retire-after-freezing or hard-knock rule followed by the air test | 1 | none | warning | Inspection, TRL 3; freeze and drop tests (TF), TRL 4 | Met by design |
| PR-021 | UR-018 | Usability | Taste with chlorine | With D, free chlorine in the clean bucket shall be under 2 mg/L at 1 h (CDC acceptability limit) | 2 | max | mg/L | Taste panel and residual (TG, TJ), TRL 4 | At risk (no carbon stage; HWC-DEC-001 D3) |
| PR-022 | UR-019 | Maintenance | Cleanable prefilter | The cloth shall lift out with the clamp ring by hand, be rinsed and dried, with a spare in rotation | 1 | none | tool-free | Inspection of the model, TRL 3; TH, TRL 4 | Met by design |
| PR-023 | UR-021 | Environment and durability | End of life | Every part shall separate by hand or screwdriver into HDPE or PP, timber, stainless and the module | 4 | max | material streams | Inspection of the BOM, TRL 3 | Met by design |
| PR-024 | UR-022 | Deployment and assembly | Regional manufacture | Buckets, timber, plywood, printed parts and fasteners shall be obtainable regionally; only the module and small fittings imported | 2 | max | imported line items | Inspection of the BOM, TRL 3 | Met by design (module, tee) |
| PR-025 | UR-101, UR-013 | Performance | No overflow | Even a raw bucket filled to the brim shall fit in the clean bucket when the batch is started below the 2.5 L refill line | 19.6 | min | L free in the clean bucket | Analysis (HWC-CAL-001 section 3), TRL 3; TH, TRL 4 | Met on paper (19.4 L worst batch, 19.6 L free) |
| PR-026 | UR-102 | Performance | Settling and turbid water | The raw outlet shall sit 50 mm above the raw floor (2.6 L settling zone) behind a 250 um strainer; at 100 NTU after 1 h of settling (1.5 h below 10 degC) the module shall treat at least 40 L between backflushes | 40 | min | L between backflushes at 100 NTU | Analysis (HWC-CAL-001 section 5), TRL 3; fouling test at 1, 10, 50 and 100 NTU (TE, TD), TRL 4 | To verify at TRL 4 |
| PR-027 | UR-103 | Usability | Fill in place | The raw bucket shall be filled in place from containers of 5 L or less, with its rim no higher than 1.3 m | 1.3 | max | m | Inspection of the model (HWC-DWG-001), TRL 3; persona trials (TH), TRL 4 | At risk (1.27 m: chest height of a 1.75 m adult; a carer task, not a child's) |
| PR-028 | UR-104 | Safety | Stability | The loaded stand (raw bucket full, clean bucket empty) shall need at least 15 deg of tilt and 70 N at 1 m to tip | 15 | min | deg | Analysis (HWC-CAL-001 section 6), TRL 3; tip test with water (TF), TRL 4 | Met on paper (18.7 deg, 78 N) |
| PR-029 | UR-005, UR-013 | Performance | Priming | The module shall stand upright with its raw inlet on top, the raw hose falling all the way, and a bleed screw on the top cap opened at first fill until water shows | 1 | none | arrangement | Inspection of the model, TRL 3; first-fill observation (TC), TRL 4 | Met by design |
| PR-030 | UR-013 | Performance | Gravity head | The head from the raw outlet and fill line to the clean discharge shall be 0.4 to 0.7 m | 0.4 to 0.7 | range | m | Analysis (HWC-CAL-001 section 3), TRL 3 | Met on paper (0.42 to 0.66 m) |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
