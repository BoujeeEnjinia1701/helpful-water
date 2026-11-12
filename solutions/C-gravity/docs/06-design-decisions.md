---
doc_id: HWC-DEC-001
title: "Helpful Water C: household gravity filter design decisions register"
project: "Helpful Water C: household gravity filter"
doc_type: Design decisions register
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Register opened at TRL 3: concept choice and design questions proposed, awaiting Amish; STEM fixes F1 to F5 recorded under the standing instruction of 2026-10-23"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: All pending decisions settled on their recommendations by Amish (instruction of 2026-11-11); no decision open

---

# Helpful Water C: household gravity filter design decisions register

Every design decision for this solution, in one place. Each is argued in its decision record under `docs/decisions/`. On 2026-11-11 Amish instructed that every pending decision be settled on its recommendation; the decisions below are recorded as his, and no decision is open. The STEM fixes were made under his standing instruction of 2026-10-23. Items under "To confirm when parts are bought" are supplier facts to collect, not decisions.

## Decisions taken on 2026-11-11

| # | Decision needed | Options | Decision (Amish, 2026-11-11) | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| D1 | Concept for solution C | C1 two-bucket hollow fibre (286 of 345); C2 ceramic candles (234); C3 biosand (227) | C1 two-bucket hollow-fibre filter. Decided by Amish, 2026-11-11 (recommendation adopted). | Everything: the drawings, BOM and build plan describe C1 | HWC-OPT-001, HWC-DDR-001 |
| D2 | Membrane class of the bought module | 0.1 um microfiltration (as designed); 0.02 um ultrafiltration (a physical virus barrier in some products, lower flux, more area) | 0.1 um microfiltration with solution D, in line with "no virus claim, co-treat"; suppliers quote both classes so a UF module can be tested at TRL 4. Decided by Amish, 2026-11-11 (recommendation adopted). | Module line of the BOM; area and flow | HWC-STM-001 S9, S10 |
| D3 | Carbon stage | None (as designed); a carbon cup at the tap; carbon only where D is not used | No carbon stage; chlorine taste is accepted and tested (consistent with HWD-DEC-001 D3). Decided by Amish, 2026-11-11 (recommendation adopted). | Taste (PR-021 at risk) | HWC-STM-001 S14 |
| D4 | Wall strap for the stand | No strap (18.7 deg tip angle, 78 N at 1 m); a webbing strap and screw eye to the wall | Wall strap fitted wherever children are about. Decided by Amish, 2026-11-11 (recommendation adopted). | One strap and a screw eye; safety instructions | HWC-STM-001 S18, independent review |
| D5 | Height of the top shelf | 900 mm (rim 1.27 m, head 0.42 to 0.66 m); 750 mm (rim 1.12 m, about 30 % less head, needs about 40 % more fibre area) | 900 mm top shelf for the prototype, tested with the household carer persona. Decided by Amish, 2026-11-11 (recommendation adopted). | Leg length, module size | PR-027 at risk |
| D6 | Colour coding | Blue raw bucket and lid, white clean bucket | Blue raw side, white clean side, with pictograms. Decided by Amish, 2026-11-11 (recommendation adopted). | Bucket purchase | HWC-BLD-001 |
| D7 | Solution D interface | 60 mm dosing port in the raw lid with a screw cap (as designed); another size from D | The HWD-DEC-001 D4 interface: a 28 mm PCO 1881 port with the orange insert in the raw-bucket lid, and the outlet closed for the full wait. Decided by Amish, 2026-11-11 (recommendation adopted). | Raw lid and dosing collar | HWC-STM-001 S11, S21 |
| D8 | Batch tally for retirement | A tick card on the label; a printed counter ring on the fill cover | Tick card for the prototype. Decided by Amish, 2026-11-11 (recommendation adopted). | Label artwork | PR-012 |

## To confirm when parts are bought

Table 2. Items to confirm.

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| C1 | The module's clean-water flux at about 5 kPa and 20 degC | Every flow figure rests on an assumed 1,000 L/(m2 h bar) | HWC-CAL-001 section 1 |
| C2 | The module's maximum backwash pressure, burst rating of the shell, caps and potting, and lifetime chlorine exposure (ppm h) | Backflush instruction; chlorine from D | HWC-STM-001 S13, S26, S27 |
| C3 | Inside sizes of the local 20 L buckets (top, base, height, wall) | Fill line, batch volume, tap and outlet heights | `cad/src/params.py` |
| C4 | Food-contact certificates for the buckets, tap, valve, bulkhead, tee, check valve and hose | NSF/ANSI/CAN 61 and 372 design rule | PR-016 |
| C5 | Bulkhead thread and the valve thread match (1/2 in BSP or NPT) | Leak-free outlet | HWC-BLD-001 section 3.12 |
| C6 | A bleed screw on the module's top cap (design request) | Priming | HWC-STM-001 S19 |
| C7 | Cracking pressure of the luer check valve | Backflush and air test | HWC-STM-001 S22 |

## Value engineering

Value-engineering target: USD 60 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 86.40 (USD 26.40 over the target). Main cost drivers: the bought module (USD 15), the timber stand and its fasteners (USD 18.30), the two buckets with lids (USD 15.10), the tap (USD 5.90) and the valve, bulkhead and strainer (USD 10). Savings worth trying: a wall bracket or an existing table and a brick plinth in place of the stand (saves up to USD 18 but loses the fixed head and the stability margin); one jerrycan with a tap as the clean container if it is cheaper locally; printing the tee and strainer only once food-contact filament is confirmed; moulded fittings at scale (an estimated USD 29 at scale is a planning figure).

## Decisions made

Table 3. Decisions made.

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-11-11 | Program shape: one repo, lettered solutions A to D; solution C is the household gravity filter | Amish Chadha | HWP-PLN-001 |
| 2026-11-11 | Licences: CERN-OHL-P-2.0 hardware, Apache-2.0 software, CC-BY-4.0 documentation; no archive, no DOI | Amish Chadha | STANDARDS section 25 |
| 2026-11-11 | Credits: Amish Chadha, Ali Raza, Suraksha Bhat, Lillian Fernandes, Raksha Thammaiah, James Butler | Amish Chadha | README |
| 2026-11-11 | "No virus claim, co-treat": C makes no virus claim and pairs with chlorine (solution D) | Amish Chadha | HWP-CLM-001 |
| 2026-11-11 | F1: 560 mm cross feet under the stand (the 420 mm frame tipped at 14.2 deg loaded) | Decided under Amish's standing instruction of 2026-10-23 (STEM fix rule) | HWC-DDR-003 |
| 2026-11-11 | F2: module upright with its raw inlet on top and a bleed screw on the top cap | Decided under the standing instruction of 2026-10-23 | HWC-DDR-003 |
| 2026-11-11 | F3: 17 L fill line on the raw bucket and a 2.5 L refill line on the clean bucket | Decided under the standing instruction of 2026-10-23 | HWC-DDR-003 |
| 2026-11-11 | F4: dosing port in the raw lid and a "shut 30 minutes after dosing" valve tag | Decided under the standing instruction of 2026-10-23 | HWC-DDR-003 |
| 2026-11-11 | F5: luer check valve on the backflush port for the several-stroke air test | Decided under the standing instruction of 2026-10-23 | HWC-DDR-003 |

Amish can reverse any decision taken under the standing instruction.
| 2026-11-11 | D1: C1 two-bucket hollow-fibre filter. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D2: 0.1 um microfiltration with solution D, in line with "no virus claim, co-treat"; suppliers quote both classes so a UF module can be tested at TRL 4. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D3: No carbon stage; chlorine taste is accepted and tested (consistent with HWD-DEC-001 D3). | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D4: Wall strap fitted wherever children are about. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D5: 900 mm top shelf for the prototype, tested with the household carer persona. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D6: Blue raw side, white clean side, with pictograms. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D7: The HWD-DEC-001 D4 interface: a 28 mm PCO 1881 port with the orange insert in the raw-bucket lid, and the outlet closed for the full wait. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D8: Tick card for the prototype. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
