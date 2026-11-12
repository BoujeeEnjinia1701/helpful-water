---
doc_id: HWD-DEC-001
title: "Helpful Water D: chlorine co-treatment add-on design decisions register"
project: "Helpful Water D: chlorine co-treatment add-on"
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
    change: First register; open decisions D1 to D6, items to confirm C1 to C4, fixes F1 to F6 under the standing instruction of 2026-10-23
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Independent STEM review run (D2 closed); fixes F7 to F12 under the standing instruction (HWD-DDR-004); F4 and F6 revised by F11; new proposed decision D7 (field chlorine check); D3 and D4 updated with the review findings; item C5 added
  - version: "0.3"
    date: 2026-11-11
    author: Amish Chadha
    change: All pending decisions settled on their recommendations by Amish (instruction of 2026-11-11); no decision open

---

# Helpful Water D: chlorine co-treatment add-on design decisions register

Every design decision for this solution, in one place. Each is argued in its decision record under `docs/decisions/`. On 2026-11-11 Amish instructed that every pending decision be settled on its recommendation; the decisions below are recorded as his, and no decision is open. The STEM fixes were made under his standing instruction of 2026-10-23. Items under "To confirm when parts are bought" are supplier facts to collect, not decisions.

## Decisions taken on 2026-11-11

| ID | To decide | Options | Recommendation | Affects in the build | Record |
| --- | --- | --- | --- | --- | --- |
| D1 | Concept to carry | D1 tablet dose cap (174 of 215); D2 metered liquid doser (143); D3 erosion feeder (dropped) | D1 tablet dose cap with ball timer; D2's timer is offered as a clip where SWS liquid is distributed. Decided by Amish, 2026-11-11 (recommendation adopted). | Everything; D1 is drawn, priced and planned | HWD-OPT-001, HWD-DDR-001 |
| D2 | Independent STEM review | Closed 2026-11-11: run as a separate process; 20 holds, 18 weak, 5 refuted of 43 rows; findings fixed (F7 to F12) or sent here (D3, D4, D7) | Closed (independent review run 2026-11-11). Decided by Amish, 2026-11-11 (recommendation adopted). | Fixes F7 to F12 | HWD-STM-001, HWD-DDR-004 |
| D3 | Residual after the filter | (a) Accept no residual and rely on C's closed tap container and A and B's immediate drinking; (b) a second small dose in C's clean container after the filter (taste, by-products); (c) no carbon in C, or carbon before the wait in C; (d) a residual-preserving order for C only | (a) for A and B; (c) for C: C has no carbon stage (HWC-DEC-001 D3), so the residual protects its stored water. Decided by Amish, 2026-11-11 (recommendation adopted). | Label wording; C's design | HWD-STM-001 S16, PR-013 |
| D4 | Interface with C | A 28 mm PCO 1881 port in C's raw-bucket lid, and C's outlet closed (tap or hose clip) for the full wait; or tablets dropped straight into the bucket with a separate timer | A 28 mm port with the orange insert in C's lid and a closed outlet during the wait, with pour-through and a 30 s stir (F7). Dropping the tablet into the empty bucket before filling, with the cap kept as the timer, is printed on the label as the fallback method. Decided by Amish, 2026-11-11 (recommendation adopted). | Orange insert; C's lid; the bucket steps on the label | PR-014, HWD-STM-001 S41 |
| D5 | Main route: 1 L or 20 L | Personal bottles (USD 12.74 per person a year at humanitarian prices); household 20 L bucket (USD 5.72 per household a year) | Household 20 L as the main route; 1 L for personal and field use. Decided by Amish, 2026-11-11 (recommendation adopted). | Which insert and tablets ship in each kit | HWD-CAL-001 section 10 |
| D7 | Field check of the residual | (a) No check: rely on the matched tablet, the clear plug and the timer; (b) free chlorine test strips (DPD type) in each kit, used after the wait on every new source and every tenth batch, target at least 0.5 mg/L; (c) a colour comparator for programme staff only | (b) free chlorine test strips in the household kit; (c) a colour comparator for partners. The strip cost is to assess. Decided by Amish, 2026-11-11 (recommendation adopted). | Kit contents, cost per household, label | HWD-STM-001 S43 |
| D6 | Timer type | Ball timer (no watch needed, needs fluid tuning); hand-set dial (cheaper, needs a clock); none (pictogram only) | Ball timer; the hand-set dial is the fall-back if the fall time cannot be held within 10 %. Decided by Amish, 2026-11-11 (recommendation adopted). | Timer parts | HWD-CAL-001 section 5 |

## To confirm when parts are bought

Table 2. Items to confirm.

| ID | Item | Why | Affects |
| --- | --- | --- | --- |
| C1 | Diameter and thickness of the 3.5 mg and 67 mg tablets in the partner's kits | The keyed bores (9.5 and 14.5 mm) and free heights (8.0 and 11.0 mm) assume 8 x 3.5 mm and 13 x 5.0 mm | Inserts, plug stop |
| C2 | Silicone fluid grade for a fall of at least 30 minutes at 25 C | The Faxen wall factor at d/D = 0.5 is approximate | Timer fluid |
| C3 | Chlorine tolerance of the A to C hollow-fibre modules, from their suppliers | Pre-chlorinated water reaches the membranes | A to C module choice |
| C4 | Dissolution time of each tablet in the well when shaken, at 5 and 30 C | Sets the shake instruction | Pictogram |
| C5 | Expansion allowance for the timer capsule: a floating top cap or a compliant FKM end, set with the fluid trials | The sealed 0.19 mL of fluid changes volume 3.4 % (6 uL) between a 25 C fill and -10 or 60 C | Timer end caps, build step 1 |

## Value engineering

Value-engineering target: USD 10. Estimated cost of the constructable design: USD 9.15 (USD 0.85 under the target). Main cost drivers: the printed cap body (USD 2.11) and the twenty test tablets at retail (USD 3.20). Savings worth trying: buy test tablets at humanitarian prices through a partner (about USD 0.01 each); print the inserts, hub and end caps in one job; a moulded scale version is estimated at USD 1.40.

## Decisions made

Table 3. Decisions made.

| Date | Decision | Amish's words where recorded | Record |
| --- | --- | --- | --- |
| 2026-11-11 | Program shape: one repo, lettered solutions A to D; Helpful Engineering licences; no archive; credits list | As set for the program | HWP-PLN-001 |
| 2026-11-11 | No virus claim for A to C; D is the co-treatment | "No virus claim, co-treat" | HWP-CLM-001 |
| 2026-10-23 | Standing STEM fix rule | Standing instruction (STANDARDS section 20) | STANDARDS |
| 2026-11-11 | F1: settle-first and two-tablet rule for 5 to 50 NTU, do-not-use above 50 NTU, well sized for two tablets | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S6 |
| 2026-11-11 | F2: colour-keyed inserts, blue 9.5 mm (1 L) and orange 14.5 mm (20 L) | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S20 |
| 2026-11-11 | F3: plug stop spigot leaves room for two tablets, not three | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S21 |
| 2026-11-11 | F4: cold-water run count (one, two, four) on the timer label | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S24 |
| 2026-11-11 | F5: insert O-ring groove root 17.8 mm (19 % squeeze) | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S26 |
| 2026-11-11 | F6: timer nominal set to 34 minutes so the low end of the fluid tolerance still reads 30 (superseded by F11) | Decided under the standing instruction of 2026-10-23 | HWD-DDR-003, STM S23 |
| 2026-11-11 | F7: 20 L bucket method: plug off, pour raw water through the well until the tablet has gone, stir 30 s, then start the timer | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S41 |
| 2026-11-11 | F8: blue 1 L insert labelled for bottles of 1 to 1.5 L (two tablets in 0.5 L give 8 mg/L) | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S42 |
| 2026-11-11 | F9: D2 dropper orifice 2.0 mm and five drops per litre (three drops from 1.2 mm gave 0.6 to 0.7 mg/L) | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S36 |
| 2026-11-11 | F10: insert O-ring groove root 17.9 mm with bore +/-0.05 and groove +/-0.03 mm (15 to 28 % squeeze; 17.8 mm fell to 8 % at print tolerance) | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S26 |
| 2026-11-11 | F11: timer nominal 45 minutes so it reads at least 30 minutes up to 40 C (34 minutes read 23 at 40 C); run count one, two, three (revises F4 and F6) | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S23, S24 |
| 2026-11-11 | F12: clear well plug in PETG or clarified PP, not PC (the well holds up to 22 g/L chlorine while a tablet dissolves) | Decided under the standing instruction of 2026-10-23, after the independent review | HWD-DDR-004, STM S28 |
| 2026-11-11 | D1: D1 tablet dose cap with ball timer; D2's timer is offered as a clip where SWS liquid is distributed. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D2: Closed (independent review run 2026-11-11). | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D3: (a) for A and B; (c) for C: C has no carbon stage (HWC-DEC-001 D3), so the residual protects its stored water. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D4: A 28 mm port with the orange insert in C's lid and a closed outlet during the wait, with pour-through and a 30 s stir (F7). Dropping the tablet into the empty bucket before filling, with the cap kept as the timer, is printed on the label as the fallback method. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D5: Household 20 L as the main route; 1 L for personal and field use. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D6: Ball timer; the hand-set dial is the fall-back if the fall time cannot be held within 10 %. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |
| 2026-11-11 | D7: (b) free chlorine test strips in the household kit; (c) a colour comparator for partners. The strip cost is to assess. | Amish (recommendation adopted, instruction of 2026-11-11) | This register |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
