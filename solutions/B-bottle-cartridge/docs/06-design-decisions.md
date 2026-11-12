---
doc_id: HWB-DEC-001
title: "Helpful Water B: bottle cartridge design decisions register"
project: "Helpful Water B: bottle cartridge"
doc_type: Design decisions register
version: "0.3"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First register: F1 to F4 decided under the standing instruction; D1 to D7 proposed; items to confirm C1 to C7; value engineering"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review run (HWB-STM-001): D6 closed; F5 to F9 decided under the standing instruction; D8 and D9 proposed; C1, C2 and C7 extended"
  - version: "0.3"
    date: 2026-11-11
    author: Amish Chadha
    change: All pending decisions settled on their recommendations by Amish (instruction of 2026-11-11); no decision open

---

# Helpful Water B: bottle cartridge design decisions register

Every design decision for this solution, in one place. Each is argued in its decision record under `docs/decisions/`. On 2026-11-11 Amish instructed that every pending decision be settled on its recommendation; the decisions below are recorded as his, and no decision is open. The STEM fixes were made under his standing instruction of 2026-10-23. Items under "To confirm when parts are bought" are supplier facts to collect, not decisions.

## Decisions taken on 2026-11-11

| # | Decision needed | Options | Decision (Amish, 2026-11-11) | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| D1 | Concept: B1 squeeze cartridge or B2 gravity drip stand (within 10 %, 246 against 222) | B1; B2; B1 with B2's stand as an accessory | B1 squeeze cartridge (246, the higher score, already carried to the drawings, BOM and build plan). B2's drip stand is recorded as a possible later accessory, outside the current scope. Decided by Amish, 2026-11-11 (recommendation adopted). | The drawings, BOM and plan describe B1; B2 needs its own stand parts and plan | HWB-OPT-001, HWB-DDR-001 |
| D2 | Neck finish the prototype is drawn to | PCO 1881 (collar also fits 1810); PCO 1810 | PCO 1881. Decided by Amish, 2026-11-11 (recommendation adopted). | Collar thread | HWB-CAL-001 section 2 |
| D3 | 38 mm wide-mouth adapter in the first prototype | Draw it now; after the neck survey | No adapter in the first prototype; a 38 mm adapter is added after the neck survey only if the local 38 mm finish is common. Decided by Amish, 2026-11-11 (recommendation adopted). | One more printed part | HWB-STM-001 S25 |
| D4 | Size target for B (UR-012 gives 30 mm across for personal devices) | Keep 30 mm (not met); set 50 mm for bottle-mounted devices | A B-specific size target of 250 mm long and 50 mm across, since the bottle is 80 mm across; PR-014 is met (46 mm). Decided by Amish, 2026-11-11 (recommendation adopted). | None | HWB-PRS-001 PR-014 |
| D5 | Freedom-to-operate search for squeeze and bottle filters | Search now; at P4 | Desk search of squeeze-filter patents before P4 opens; patent attorney opinion before any distribution. Decided by Amish, 2026-11-11 (recommendation adopted). | None | HWB-OPT-001, HWP-FTO-001 |
| D8 | Housing end wall at a blocked backflush (PR-028) | (a) Keep 4 mm and rely on the procedure (collar end open, shell near 0 kPa; factor 9 at a full squeeze); (b) thicken the end wall to 6.5 mm (factor 5 even if the collar end were blocked; housing 2.5 mm longer, about 3 g more, drawings and build media to regenerate); (c) restate PR-028 at the shell pressure the procedure allows | (a) until the next geometry revision, then (b). Decided by Amish, 2026-11-11 (recommendation adopted). | Housing, HWB-DWG-001 and -002, build plan media | HWB-STM-001 S16, HWB-CAL-001 section 6 |
| D9 | Water temperature for the flow requirements (PR-004 to PR-006, PR-025) | Keep 20 C; rate at 10 C (PR-004 360 and PR-005 123 mL/min, both not met on paper) | 20 C for the paper design, with the 10 C figures stated beside it; the rating temperature is reset once the co-design partners give source temperatures. Decided by Amish, 2026-11-11 (recommendation adopted). | Possibly membrane area (longer legs) | HWB-STM-001 S31 |
| D7 | Design life used for the cost per user per year | 9 months (USD 10.8); 12 months (USD 8.5) | Report both design lives until the fouling tests set the module life. Decided by Amish, 2026-11-11 (recommendation adopted). | None | HWB-CAL-001 section 7 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| C1 | The module's clean-water flux at 10 kPa and 20 C, area, fibre size, absolute or nominal rating, hydrophilic fibre, packing limit (design 53 %), potting penetration and production integrity test | Every flow figure assumes 1,000 L/(m2 h bar); potting voids are a silent bypass | HWB-CAL-001 section 3, HWB-STM-001 S29, S30 |
| C2 | The module's maximum backwash pressure and potting rating | A hard syringe push reaches 179 kPa and 135 N on the potting face | HWB-STM-001 S17, PR-029 |
| C3 | Header outside diameter, groove sizes and nipple, or a header drawn to this design | The housing bore and O-rings are sized for a 36.6 mm header | HWB-DWG-002 |
| C4 | The exact 38 mm finish of local wide-mouth bottles | Needed before the adapter is drawn | HWB-CAL-001 section 2 |
| C5 | Duckbill cracking pressure and size | Springback of the bottle must open it | HWB-STM-001 S19 |
| C6 | Food-contact certificates for the PP filament, EPDM or silicone, carbon and potting | PR-013 | HWB-REG-001 |
| C7 | Real PCO 1881 and 1810 neck dimensions from local bottles (calipers) and the ISBT drawings, including the number of thread starts and tolerances | Thread data are approximate; the collar thread is drawn single-start | HWB-CAL-001 section 2, HWB-STM-001 S24 |

## Value engineering

Value-engineering target: USD 20 for prototype parts (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 18.35 (USD 1.65 under the target). At scale: about USD 7.05 against the shortlist's under USD 8. Main cost drivers: the bought membrane module (USD 6.00 estimate, a third of the total), the printed housing (USD 4.70) and the syringe (USD 1.00). Savings worth trying: quotations from two or three module makers at 100 and 1,000 units; printing the housing with a 1.5 mm wall; one syringe per household rather than per cartridge; a bought sports-cap valve in place of the printed valve and cover.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-11-11 | Program shape: one repo, lettered solutions A to D; licences CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0; no archive; credits list | Amish | HWP-PLN-001, project.yaml |
| 2026-11-11 | No virus claim; co-treat with chlorine where viruses are a risk | Amish ("No virus claim, co-treat") | HWP-CLM-001 |
| 2026-11-11 | F1: carbon moved upstream of the membrane, to a dirty-side capsule | Under Amish's standing instruction of 2026-10-23 | HWB-DDR-003 |
| 2026-11-11 | F2: duckbill air valve in the collar | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F3: B2 base widened to 230 mm | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F4: B2 vent tube into the inverted bottle | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F5: bottle turned upright on release so the duckbill refills in air | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F6: 50 mL first flush after storage (lumens stay wet) | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F7: chlorine co-treatment dosed and left for its full contact time before filtering; filtered water not stored | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F8: prime by syringe backflush (capsule out, collar end open) when first flow is low or after drying | Under the standing instruction | HWB-DDR-003 |
| 2026-11-11 | F9: module request names hydrophilic fibres shipped wet, potting rating, packing limit and production integrity test | Under the standing instruction | HWB-DDR-003, bom/bom.csv item 8 |
| 2026-11-11 | D6 closed: independent STEM review run (separate process, claims, calculations and sources only) | Brief of 2026-11-11 (STANDARDS section 20) | HWB-STM-001 |
| 2026-11-11 | Design-for-construction changes | STANDARDS section 18 (Amish, 2026-09-30) | HWB-DDR-002 |
| 2026-11-11 | D1: B1 squeeze cartridge (246, the higher score, already carried to the drawings, BOM and build plan). B2's drip stand is recorded as a possible later accessory, outside the current scope. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D2: PCO 1881. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D3: No adapter in the first prototype; a 38 mm adapter is added after the neck survey only if the local 38 mm finish is common. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D4: A B-specific size target of 250 mm long and 50 mm across, since the bottle is 80 mm across; PR-014 is met (46 mm). | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D5: Desk search of squeeze-filter patents before P4 opens; patent attorney opinion before any distribution. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D7: Report both design lives until the fouling tests set the module life. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D8: (a) until the next geometry revision, then (b). | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D9: 20 C for the paper design, with the 10 C figures stated beside it; the rating temperature is reset once the co-design partners give source temperatures. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
