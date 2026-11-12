---
doc_id: HWD-PRS-001
title: "Helpful Water D: chlorine add-on for viruses product requirements and specifications"
project: "Helpful Water D: chlorine add-on for viruses"
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
    change: First product requirements for the D1 tablet dose cap carried to the TRL 3 documents, statuses from HWD-CAL-001
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: PR-008 now at least 30 minutes up to 40 C; PR-009 run count one, two, three (F11)
---

# Helpful Water D: chlorine add-on for viruses product requirements and specifications

What the dose cap must do, each requirement traced to a user need in HWD-URS-001 (links in HWD-RTM-001). The requirements describe option D1, the tablet dose cap carried to the drawings, BOM and build plan; the concept choice is Amish's (HWD-DEC-001 D1). Of 24 requirements, 17 are met on paper or by design, 5 are to verify at TRL 4 and 2 are at risk; none is over the value-engineering target. Planned tests cite the HWP-VER-001 families (TA to TJ); none is run at TRL 3. Targets remain proposals for review with a co-design partner.

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-003 | Performance | Household dose | One matched tablet shall give a free chlorine dose of 2.0 mg/L in its rated volume (1 L or 20 L) | 2.0 | 1.5 to 2.5 | mg/L | Analysis (HWD-CAL-001 section 1), TRL 3; dose test (TJ), TRL 4 | Met on paper (2.0; 1.6 in 25 L) |
| PR-002 | UR-003 | Performance | Residual at 30 minutes | In clear water (under 5 NTU, pH under 8) the free chlorine 30 minutes after dosing shall be at least 0.5 mg/L | 0.5 | min | mg/L | Analysis (HWD-CAL-001 section 2), TRL 3; DPD residual at 30 and 60 min (TJ), TRL 4 | Met on paper (1.7, assumed demand) |
| PR-003 | UR-003 | Performance | CT for viruses | Within the stated contact time the CT shall reach the US EPA 4-log virus value for the water temperature (8 mg min/L at 5 C, 12 at 0.5 C) | 8 | min | mg min/L | Analysis (HWD-CAL-001 section 3), TRL 3; virus protocol for the combined system (TB), TRL 4 | Met on paper (53 in 30 min) |
| PR-004 | UR-003 | Regulatory | Claim wording | Product, pack and documents shall use only the HWP-CLM-001 wording for D and state that chlorine does not inactivate *Cryptosporidium* and that the water must be filtered after the wait | 1 | none | wording | Inspection of the artwork and documents, TRL 3 | Met by design |
| PR-005 | UR-011 | Safety | Maximum dose | No allowed use shall exceed the WHO guideline value of 5 mg/L free chlorine | 5.0 | max | mg/L | Analysis (HWD-CAL-001 section 6), TRL 3; TJ, TRL 4 | Met on paper (4.0 at two tablets) |
| PR-006 | UR-101 | Safety | Wrong tablet rejected | The 1 L well shall not accept a 20 L tablet; wells shall be colour-keyed (blue 1 L, orange 20 L) | 1 | none | rejection | Inspection with bought tablets (HWD-DEC-001 C1), TRL 4; human factors (TH), TRL 4 | Met by design (tablet sizes assumed) |
| PR-007 | UR-101 | Safety | Two-tablet limit | The free height under the plug stop shall hold two tablets and not three | 2 | max | tablets | Inspection of the model (HWD-DWG-002), TRL 3; TH, TRL 4 | Met by design (8.0 and 11.0 mm) |
| PR-008 | UR-102 | Usability | Timer run | The ball timer shall run at least 30 minutes at air temperatures up to 40 C at the low end of the fluid tolerance | 30 | min | min | Analysis (HWD-CAL-001 section 5), TRL 3; fall-time check per fluid batch at 25 and 40 C (TH, TI), TRL 4 | To verify at TRL 4 (30.3 on paper) |
| PR-009 | UR-102 | Usability | Cold-water rule | The timer label shall show the run count: one above 18 C, two at 10 to 18 C, three below 10 C | 1 | none | label | Inspection of the artwork, TRL 3; comprehension (TH), TRL 4 | Met by design |
| PR-010 | UR-104 | Usability | Turbid-water rule | The pictograms shall show settle-and-pour then two tablets for cloudy water, and do-not-use for muddy water (over 50 NTU) | 1 | none | label | Inspection, TRL 3; comprehension (TH), TRL 4 | Met by design |
| PR-011 | UR-008 | Safety | See the tablet dissolve | The well plug shall be clear so the user can see whether the tablet has fully dissolved | 1 | none | window | Inspection of the model, TRL 3; dissolution time in the well (TJ), TRL 4 | Met by design |
| PR-012 | UR-103 | Usability | Bottle neck fit | The cap shall screw onto a 28 mm PCO 1881 neck (the B interface) and seal on its liner upside down | 1 | none | fit | Inspection against HWB-CAL-001 neck data, TRL 3; leak test inverted (TF), TRL 4 | Met by design |
| PR-013 | UR-103 | Usability | Order of use and residual | Instructions shall put dose, wait, then filter; the water drunk or stored after A to C shall keep a protective free residual where storage requires it | 0.2 | min | mg/L at 24 h | Analysis (HWD-STM-001 S16), TRL 3 | At risk (no residual after carbon; HWD-DEC-001 D3) |
| PR-014 | UR-103 | Usability | C bucket interface | A 28 mm PCO 1881 port on C's raw-bucket lid and the orange 20 L insert shall dose 20 L, with C's outlet closed during the wait | 1 | none | interface | Interface agreement with C (HWD-DEC-001 D4), TRL 3 | At risk (C design in progress) |
| PR-015 | UR-005 | Usability | Ready to use | The cap shall come assembled and need no tool, power or measuring | 0 | max | tools | Inspection, TRL 3; TH, TRL 4 | Met by design |
| PR-016 | UR-006 | Usability | Pictograms | Dose, shake, wait and filter shall be shown in pictograms of three steps or fewer, ISO 7010 style | 3 | max | steps per task | Inspection, TRL 3; comprehension (TH), TRL 4 | To verify at TRL 4 |
| PR-017 | UR-011 | Materials | Wetted materials | Every wetted part shall be made from a grade certified to NSF/ANSI/CAN 61 (or an equal national scheme) and resistant to dilute chlorine | 100 | min | % of wetted parts | Supplier certificates, TRL 4; extractables (TG), TRL 4 | To verify at TRL 4 |
| PR-018 | UR-011 | Safety | By-products | Cyanuric acid at the highest allowed dose shall stay below the WHO 40 mg/L; THMs shall be measured at worst-case organics | 40 | max | mg/L | Analysis (HWD-CAL-001 section 6), TRL 3; TG, TRL 4 | Met on paper (4.1) |
| PR-019 | UR-014 | Cost | Cost | Prototype parts and test tablets shall be reported against the USD 10 value-engineering target, with cost per litre and per person per year over life | 10 | max | USD | Analysis (HWD-CAL-001 section 10, BOM), TRL 3 | Met on paper (USD 9.15) |
| PR-020 | UR-015 | Logistics | Standard consumable | The cap shall take standard household NaDCC tablets (3.5 mg and 67 mg) from humanitarian catalogues, with no proprietary refill | 1 | none | consumable | Inspection of the BOM, TRL 3; partner kit check (C1), TRL 4 | Met by design |
| PR-021 | UR-016 | Environment and durability | Storage | Tablets shall stay in foil strips until use; the cap shall survive 50 C storage and transit without distortion of the thread or seals | 50 | max | C | Analysis of materials, TRL 3; ageing (TF), TRL 4 | To verify at TRL 4 |
| PR-022 | UR-018 | Usability | Taste after the filter | Water dosed at 2 mg/L and filtered through A, B or C shall be below the median NaDCC taste acceptability (1.26 mg/L) at the cup | 1.26 | max | mg/L | Measurement after each filter (TG, TH), TRL 4 | To verify at TRL 4 |
| PR-023 | UR-021 | Environment and durability | End of life | No batteries or electronics; plastic parts marked by resin type | 0 | max | batteries | Inspection, TRL 3 | Met by design |
| PR-024 | UR-022 | Deployment and assembly | Regional manufacture | Made parts shall be printable (prototype) and mouldable (scale) with open drawings; the timer fluid and balls bought | 1 | none | route | Inspection of the BOM and build plan, TRL 3 | Met by design |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
