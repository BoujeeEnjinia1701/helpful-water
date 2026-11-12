---
doc_id: HWB-PRS-001
title: "Helpful Water B: bottle cartridge product requirements and specifications"
project: "Helpful Water B: bottle cartridge"
doc_type: Product requirements
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First product requirements for the B1 squeeze cartridge carried to the TRL 3 documents, statuses from HWB-CAL-001"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review (HWB-STM-001): weak child at the girls' grip boundary (5.8 kPa, PR-005); PR-012 status names the 15.2 mL lumens that stay wet; PR-028 at risk on the end wall; 10 C flows noted (HWB-DEC-001 D9)"
---

# Helpful Water B: bottle cartridge product requirements and specifications

What the cartridge must do, each requirement traced to a user need in HWB-URS-001 (links in HWB-RTM-001). The requirements describe option B1, the squeeze cartridge carried to the drawings, BOM and build plan; the concept choice between B1 and B2 is Amish's (HWB-DEC-001 D1). Of 29 requirements, 14 are met on paper or by design, 9 are to verify at TRL 4, 4 are at risk, 1 is not met and 1 is over target. **Not met:** PR-014 diameter (46 mm against the 30 mm that UR-012 gives for personal devices; the bottle sets the width in any case, and a B-specific target is proposed, HWB-DEC-001 D4). **At risk:** PR-005 and PR-006 with a fouled module (82 and 141 mL/min), PR-028 if the collar end were blocked during a backflush (end wall factor 2.1, HWB-DEC-001 D8), and PR-029 until the module's backwash limit is known. All flows are rated in 20 C water; at 10 C they are about 23 % lower, so PR-004 (360 mL/min) and PR-005 (123 mL/min for the weak child) would not be met if the rating temperature became 10 C (HWB-DEC-001 D9). **Over target:** PR-015 cost per user per year (USD 10.8 at a 9-month life; USD 8.5 at 12 months). Every flow figure rests on an assumed membrane permeability of 1,000 L/(m2 h bar) that the module maker must confirm (HWB-DEC-001 C1). Verification families TA to TJ are those of HWP-VER-001; nothing is tested at TRL 3. Targets are proposals for review with a co-design partner.

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Bacteria reduction | The bought module shall carry a supplier-stated absolute or nominal rating of 0.1 um or finer and, assembled, shall target a bacteria log reduction of at least 3 (first gate) toward 6 | 3 | min | log10 | Supplier certificate (TA) and accredited challenge at beginning and end of life (TB), TRL 4 | To verify at TRL 4 |
| PR-002 | UR-002 | Performance | Protozoa reduction | The assembled cartridge shall target a cyst-surrogate log reduction of at least 3 | 3 | min | log10 | Accredited challenge (TB), TRL 4 | To verify at TRL 4 |
| PR-003 | UR-003 | Safety | No-virus warning | The cartridge and pack shall carry the HWP-CLM-001 warning and pictogram (virus crossed out, tablet beside it) and the instructions shall pair it with chlorine (solution D) where viruses are a risk | 1 | none | warning | Inspection of the artwork, TRL 3; comprehension trial (TH), TRL 4 | Met by design |
| PR-004 | UR-004 | Performance | Adult flow | With a clean module the cartridge shall deliver at least 400 mL/min at a held adult squeeze of 17 kPa | 400 | min | mL/min | Analysis (HWB-CAL-001 section 3), TRL 3; pressure-flow map (TC), TRL 4 | Met on paper (465 at 20 C, assumed permeability; 360 at 10 C, D9) |
| PR-005 | UR-004 | Performance | Child and elderly flow | With a clean module the cartridge shall deliver at least 150 mL/min at 5.8 kPa (weak child) and 7.2 kPa (weak elderly woman) | 150 | min | mL/min | Analysis (HWB-CAL-001 section 3), TRL 3; persona trials (TH) and TC, TRL 4 | At risk (160 and 198 clean; 82 and 102 fouled) |
| PR-006 | UR-004 | Performance | Flow at 10 kPa | The cartridge shall deliver at least 200 mL/min at 10 kPa (Rev A goal), clean module, 20 C | 200 | min | mL/min | Analysis (HWB-CAL-001), TRL 3; TC, TRL 4 | At risk (274 clean, 141 fouled) |
| PR-007 | UR-005 | Usability | Ready to use | The cartridge shall be supplied assembled with its carbon capsule fitted and shall be primed by two squeezes of a full bottle, with no tool | 2 | max | min to first use | Demonstration (TH), TRL 4 | To verify at TRL 4 |
| PR-008 | UR-006 | Usability | Pictogram instructions | Use, backflush, limits and retirement shall be shown in pictograms of three steps or fewer each, with ISO 7010 style symbols | 3 | max | steps per task | Inspection, TRL 3; comprehension trial (TH), TRL 4 | To verify at TRL 4 |
| PR-009 | UR-007 | Maintenance | Daily upkeep | A backflush (two 60 mL syringe strokes with treated water, capsule out) and a drain shall take under 2 minutes with the supplied syringe and no other tool | 2 | max | min | Analysis of the procedure (HWB-BLD-001 section 5), TRL 3; TH, TRL 4 | Met on paper |
| PR-010 | UR-008 | Safety | Field integrity check | Squeezing air from an empty bottle through the wetted cartridge into a cup of water shall show a stream of bubbles from any opening larger than 20 um | 20 | max | um | Analysis (HWB-CAL-001 section 5), TRL 3; defect-seeded test (TF, TI), TRL 4 | Met on paper (17 um at 17 kPa); not a proof of performance |
| PR-011 | UR-009 | Safety | One dirty-to-clean seal | The only dirty-to-clean boundary shall be the potting and the two header O-rings; changing the carbon capsule shall not open the clean side | 1 | none | seal line | Inspection of the model (HWB-DWG-002), TRL 3; bypass tests (TF), TRL 4 | Met by design |
| PR-012 | UR-010 | Safety | Small clean-side hold-up | The clean side downstream of the potting shall hold no more than 10 mL and drain when the cartridge is upended | 10 | max | mL | Analysis (HWB-CAL-001), TRL 3; storage regrowth (TE, TG), TRL 4 | Met on paper (5.7 mL downstream of the potting; the 15.2 mL in the lumens stays wet, so a 50 mL first flush follows storage, HWB-DEC-001 F6); regrowth and grow-through to verify |
| PR-013 | UR-011 | Materials | Wetted materials | Every wetted part shall be made from a grade certified to NSF/ANSI/CAN 61 (or an equal national scheme), lead-free to NSF/ANSI/CAN 372 | 100 | min | % of wetted parts | Supplier certificates, TRL 4; extractables (TG), TRL 4 | To verify at TRL 4 |
| PR-014 | UR-012 | Physical architecture | Size | The cartridge shall be no longer than 250 mm and no wider than 30 mm | 250 x 30 | max | mm | Inspection of the model, TRL 3 | Not met (217 mm long, 46 mm across; B-specific target proposed, HWB-DEC-001 D4) |
| PR-015 | UR-014 | Cost | Cost | Prototype parts shall be reported against the USD 20 value-engineering target; at scale the unit shall approach USD 8 and the cost per user per year USD 10 | 10 | max | USD per user per year | Analysis (HWB-CAL-001 section 7, BOM), TRL 3 | Over target (USD 10.8 at 9 months; prototype USD 18.35, scale USD 7.05) |
| PR-016 | UR-015 | Logistics | Refillable carbon | The carbon capsule shall open by hand and accept any NSF/ANSI/CAN 61 granular carbon of 12 x 40 mesh | 1 | none | capsule | Inspection, TRL 3; refill trial (TH), TRL 4 | Met by design |
| PR-017 | UR-016 | Environment | Shelf life | The packed cartridge shall keep its integrity and flow after 2 years at 40 C storage | 2 | min | years | Ageing test (TF), TRL 4; module maker's shelf-life data | To verify at TRL 4 |
| PR-018 | UR-017 | Environment | Drops and freezing | The cartridge on a full 1 L bottle shall pass the air check after a 1.5 m drop onto concrete; the product shall carry a do-not-freeze-wet warning and a retire-after-freezing rule | 1.5 | min | m | Drop test and air check (TF), TRL 4; warning by inspection | To verify at TRL 4 |
| PR-019 | UR-018 | Performance | Taste contact time | The carbon bed shall give at least 1.5 s of empty-bed contact at the adult flow; taste and chlorine reduction shall be measured, not assumed | 1.5 | min | s | Analysis (HWB-CAL-001 section 4), TRL 3; NSF/ANSI 42 style test (TG), TRL 4 | Met on paper (1.8 s); taste to verify |
| PR-020 | UR-019 | Maintenance | Rinseable mesh | The mesh disc shall be reachable by unscrewing the housing by hand and rinsed in place | 1 | none | step | Inspection, TRL 3 | Met by design |
| PR-021 | UR-020 | Usability | Cup filling | The push-pull valve shall fill a cup with the outlet held clear of the mouth, so one cartridge can serve a household without a shared mouthpiece | 1 | none | mode | Inspection, TRL 3; TH, TRL 4 | Met by design |
| PR-022 | UR-021 | Environment | End of life | Housing, collar, capsule and spout shall be polypropylene, separable by hand from the module, seals and carbon | 4 | min | PP parts | Inspection of the BOM, TRL 3 | Met by design |
| PR-023 | UR-022 | Manufacturing | Regional make | Every made part shall be printable on a desktop FDM printer for the prototype and mouldable without side actions beyond thread cores | 7 | min | made parts | Inspection (HWB-BLD-001), TRL 3 | Met by design |
| PR-024 | UR-101 | Physical architecture | Neck fit | The collar shall screw onto 28 mm PCO 1881 and PCO 1810 necks by hand and seal on the neck lip; a printed adapter shall fit 38 mm two-start necks | 2 | min | finishes direct | Analysis (HWB-CAL-001 section 2), TRL 3; fit test (TF), TRL 4 | Met on paper (1881 and 1810); 38 mm adapter to draw |
| PR-025 | UR-102 | Usability | No-squeeze mode | A user with weak hands shall get at least 150 mL/min at a weak elderly squeeze, and a gravity mode (B2 stand) shall be offered for no squeeze at all | 150 | min | mL/min | Analysis (HWB-CAL-001 section 3), TRL 3; TH, TRL 4 | Met on paper (198 clean); gravity mode depends on D1 |
| PR-026 | UR-103 | Maintenance | Membrane life | The module shall treat at least 550 L (9 months at 2 L a day) and recover at least 80 % of its flow after three standard backflushes | 550 | min | L | Fouling and backflush (TE), TRL 4 | To verify at TRL 4 |
| PR-027 | UR-004 | Usability | Air return | After each squeeze the bottle shall refill with air through the duckbill valve without unscrewing, and the valve shall not leak at a full squeeze | 0.5 | max | kPa cracking | Analysis (HWB-STM-001 S19), TRL 3; TH and TF, TRL 4 | To verify at TRL 4 |
| PR-028 | UR-011 | Safety | Housing strength | The housing shall keep a safety factor of at least 5 on printed polypropylene strength at a hard backflush (179 kPa) | 5 | min | factor | Analysis (HWB-CAL-001 section 6), TRL 3; burst test (TF), TRL 4 | At risk (hoop factor 6; flat end wall factor 2.1 if the collar end were blocked; the procedure keeps it open, HWB-DEC-001 D8) |
| PR-029 | UR-008 | Safety | Backflush pressure | The backflush procedure shall stay below the module maker's maximum backwash pressure | 1 | max | share of limit | Supplier data (HWB-DEC-001 C2), TRL 4 | At risk (limit not yet known; a gentle push gives 54 kPa) |

Categories: physical architecture, performance, materials, usability, packaging and transport, safety, electrical, software. Status: met on paper, met by design, at risk, not met, over target, withdrawn, to verify at TRL 4.

## Assumptions

- Membrane clean-water permeability 1,000 L/(m2 h bar), halved just before a backflush is due (HWB-CAL-001 section 3).
- Squeeze pressure from grip norms, 40 % of maximum held, 80 % reaching the water through the PET wall, over an 80 x 80 mm contact (HWB-CAL-001 section 3).
- 2 L a day per user; carbon capsule life 150 L until a breakthrough curve sets it.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
