---
doc_id: HWA-PRS-001
title: "Helpful Water A: filter straw product requirements and specifications"
project: "Helpful Water A: filter straw"
doc_type: Product requirements and specifications
version: "0.3"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First product requirements for option A1 (recommended), each traced to HWA-URS-001, with the Rev A flow target reconciled against the 400 mL/min user threshold
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "After the independent STEM review: flows at 20 C; PR-002 and PR-003 not met on paper; PR-001 absolute rating and B. diminuta challenge; PR-004 note; PR-012 plunger-hold check; PR-027 dry mass"
  - version: "0.3"
    date: 2026-11-11
    author: Amish Chadha
    change: PR-002 target set to 150 mL/min at 10 kPa as an upper bound (HWA-DEC-001 D3, Amish 2026-11-11)

---

# Helpful Water A: filter straw product requirements and specifications

What the straw (option A1) must do, each requirement traced to a user need. Targets are proposals for review with Helpful Engineering and a field partner. "Met on paper" means met by HWA-CAL-001 or the model; nothing is measured at TRL 3. Planned tests cite the test families of HWP-VER-001 (TA to TJ) and happen at TRL 4. Method: STANDARDS section 22.

**Flow targets reconciled.** The Rev A target (at least 200 mL/min at 10 kPa or less, clean water at 20 C) is kept as PR-002. The 400 mL/min below which straw users report dissatisfaction needs 21 to 33 kPa through this membrane area, beyond a comfortable sip, so it is carried as a known shortfall rather than a target (PR-002 note; HWA-DEC-001 D3). After the independent review the Rev A target itself is not met on paper: 110 to 179 mL/min at 10 kPa, clean water, shell primed (HWA-STM-001 S2, S3). Kit compatibility (under 25 cm and 3 cm) is PR-019.

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Bacteria reduction | The membrane module shall carry an absolute rating validated by a *Brevundimonas diminuta* retention challenge and a supplier challenge report, and reach the target log reduction of a bacterial surrogate at the worst-case flow and temperature, at the start and end of life; thin bacteria such as Leptospira are excluded unless tested | 6 | min | log10 | Test, HWP-VER-001 TA and TB, TRL 4 | To verify at TRL 4 |
| PR-002 | UR-004 | Performance | Flow at 10 kPa | The assembled straw shall deliver the target flow of clean water at 20 C with 10 kPa of suction, the straw upright and primed, stated as an upper bound (400 mL/min is not reachable: 21 to 33 kPa; HWA-DEC-001 D3) | 150 | min | mL/min | Analysis HWA-CAL-001 section 4, TRL 3; test TC, TRL 4 | Met on paper with the 0.2 um grade (179); not met with the 0.1 um grade (110), which is used only under HWA-DEC-001 D2 |
| PR-003 | UR-004 | Performance | Flow for a child | The straw shall deliver the target flow at 5 kPa of suction, upright | 80 | min | mL/min | Analysis HWA-CAL-001 section 4; test TC and TH with known potable test water, TRL 4 | Not met on paper (45 to 74) |
| PR-004 | UR-004 | Materials | Membrane permeability | The membrane shall have a clean-water permeability, normalised to 25 C as the datasheets state it, of at least the target, the floor for usable flow (1,600 at 20 C; HWA-DEC-001 F3); PR-002 needs about 3,420 at 20 C | 1800 | min | L/(m2 h bar) | Inspection of the supplier certificate, TA, TRL 4 | Met by design (specification) |
| PR-005 | UR-004 | Physical architecture | Membrane area | The module shall have at least the target outer membrane area in the 22 mm bore (HWA-DEC-001 F2) | 0.050 | min | m2 | Analysis HWA-CAL-001 section 2 (0.056) | Met on paper |
| PR-006 | UR-002 | Performance | Cyst reduction | The straw shall reach the target log reduction of a protozoan cyst surrogate (*Cryptosporidium* size) | 3 | min | log10 | Test TB, TRL 4 | To verify at TRL 4 |
| PR-007 | UR-001, UR-002, UR-009 | Safety | No bypass | Every clean/dirty boundary shall be a factory potting or two O-rings in series; zero detectable bypass at the challenge and after drops | 0 | max | detectable bypass | Inspection of the model; test TF, TRL 4 | Met by design |
| PR-008 | UR-003 | Safety | Virus warning | The straw shall carry the HWP-CLM-001 warning in words and as a pictogram (virus crossed out, tablet beside it) | 1 | min | warning on the body | Inspection, TRL 4 | Met by design |
| PR-009 | UR-005 | Usability | Ready to use | The straw shall be usable from the pack with no tools: remove two caps, wet for no more than the target time | 3 | max | min | Demonstration TH, TRL 4 | To verify at TRL 4 |
| PR-010 | UR-006 | Usability | Pictograms | Use, backflush, the air-hold check and end of life shall each be shown in three pictogram steps or fewer | 3 | max | steps per task | Test TH (comprehension), TRL 4 | To verify at TRL 4 |
| PR-011 | UR-007 | Maintenance | Daily upkeep | A daily backflush (three 20 mL syringe strokes) shall take under the target time | 2 | max | min | Analysis HWA-CAL-001 section 7 (about 1 min); test TH | Met on paper |
| PR-012 | UR-008 | Safety | Integrity check | The user shall be able to check for gross defects (broken fibre, failed collar seal) with the supplied syringe at the target air pressure through the backflush socket: push to the 6 mL mark and hold 10 s (HWA-DEC-001 D4, F7) | 50 | +- 10 | kPa | Analysis HWA-CAL-001 section 7; test TA and TF, TRL 4 | At risk (supplier reverse-pressure rating to confirm) |
| PR-013 | UR-019 | Maintenance | Rinseable mesh | A 316L mesh of the target aperture shall be captive in the removable intake cap | 250 | 150 to 350 (DOE) | um | Inspection of the model; test TE | Met by design |
| PR-014 | UR-101, UR-009 | Maintenance | Backflush route | Backflush water shall enter the clean header and leave through the fibres and intake without passing the carbon (HWA-DEC-001 F4) | 0 | max | mL through the carbon | Analysis HWA-STM-001 S18; test TE (no downstream contamination) | Met by design |
| PR-015 | UR-018, UR-015 | Performance | Carbon bed | The carbon bed shall hold the target mass of drinking-water-grade 12 x 40 coconut GAC (16 x 20 mm, 4.0 mL), replaced at a volume set from a measured breakthrough | 2.0 | 1.9 to 2.1 | g | Analysis HWA-CAL-001 section 5; test TG | Met on paper |
| PR-016 | UR-017 | Environment and durability | Freezing and drops | The straw shall carry a "do not freeze when wet" warning and keep integrity after the TF drop test | 1.5 | min | m drop height (proposed) | Test TF, TRL 4 | To verify at TRL 4 |
| PR-017 | UR-010 | Safety | Drain and dry | Every wetted space shall drain with the caps off and the straw hung mouthpiece up; heterotrophic regrowth after wet storage shall stay within the laboratory's acceptance limit | 1 | min | drain path per space | Inspection of the model; test TG | At risk (regrowth to measure) |
| PR-018 | UR-011 | Materials | Wetted materials | Every wetted material shall be a grade listed to NSF/ANSI/CAN 61 (and 372 for lead content) or equivalent | 100 | min | % of wetted parts | Inspection of certificates; test TG | To verify at TRL 4 (printed prototype parts are not listed) |
| PR-019 | UR-012 | Physical architecture | Kit compatible | The straw shall fit within the target length and width | 250 x 30 | max | mm | Analysis HWA-CAL-001 section 9 (205 x 29.6) | Met on paper |
| PR-020 | UR-014 | Cost | Cost per litre | Cost per litre over the life, consumables included, shall stay below NaDCC tablets (about USD 0.02 a litre) | 0.02 | max | USD/L | Analysis HWA-CAL-001 section 10 (0.011 prototype, about 0.002 at scale) | Met on paper |
| PR-021 | UR-014 | Cost | Prototype parts | Prototype parts cost against the value-engineering target | 25 | target | USD | Analysis, BOM | Met on paper (USD 17.46) |
| PR-022 | UR-016 | Environment and durability | Shelf life | The dry-packed straw shall keep its integrity and flow after the module maker's shelf-life and heat ageing conditions | 3 | min | years (proposed) | Test TF (ageing), TRL 4 | To verify at TRL 4 |
| PR-023 | UR-020 | Safety | Mouthpiece hygiene | The mouthpiece shall be capped between uses and replaceable per person (HWA-DEC-001 D6) | 1 | min | mouthpiece per user | Inspection | At risk (D6 open) |
| PR-024 | UR-021 | Environment and durability | End of life | Made parts shall be polypropylene and separable by hand from the module, metal and carbon | 1 | max | polymer families in made parts | Inspection of the BOM | Met by design |
| PR-025 | UR-022 | Deployment and assembly | Regional manufacture | Every made part shall be printable or mouldable regionally; only the module, mesh, O-rings and carbon are bought | 0 | max | specialist made parts | Inspection, HWA-BLD-001 | Met by design |
| PR-026 | UR-101 | Maintenance | Backflush recovery | Three standard backflush cycles shall restore at least the target share of the initial flow at fixed suction | 80 | min | % | Test TE, TRL 4 | To verify at TRL 4 |
| PR-027 | UR-102 | Physical architecture | Mass | The straw with caps and lanyard shall weigh no more than the target, dry (about 106 g full of water) | 100 | max | g | Analysis HWA-CAL-001 section 9 (66 g dry) | Met on paper |
| PR-028 | UR-008, UR-009 | Safety | Dip line | A dip line shall mark the deepest immersion, below the header, socket and mouthpiece joint | 110 | max | mm from the intake face | Inspection of the model | Met by design |
| PR-029 | UR-018 | Performance | Chlorine taste | The carbon stage shall reduce free chlorine under NSF/ANSI 42 conditions at the PR-002 flow before any taste claim | 50 | min | % reduction (NSF/ANSI 42 target) | Test TG, TRL 4 | To verify at TRL 4 |

Categories: physical architecture, performance, materials, usability, packaging and transport, safety, electrical, software. Status: met on paper, met by design, at risk, not met, over target, withdrawn, to verify at TRL 4.

## Assumptions

- Persona suction: child 5 kPa, elderly 7 kPa, adult 15 kPa (HWA-CAL-001 A2); to replace with measured values (TH).
- Membrane permeability per area of a 0.8/0.5 mm straw fibre equals the datasheet value for the 1.0 mm lumen fibres (A1).
- Membrane life 2,000 L and carbon life 500 L for the cost per litre (A11, A12); both to replace with measured values.


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
