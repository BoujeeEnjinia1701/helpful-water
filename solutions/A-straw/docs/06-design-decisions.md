---
doc_id: HWA-DEC-001
title: "Helpful Water A: filter straw design decisions register"
project: "Helpful Water A: filter straw"
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
    change: Register opened at TRL 3; fixes F1 to F5 made under the standing instruction of 2026-10-23; D1 to D9 proposed, awaiting Amish
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Independent STEM review run and recorded (open item closed); fixes F6 to F11 made under the standing instruction; flows at 20 C corrected; D2, D3 updated; D10 to D12 proposed; C2, C3, C5, C6 extended, C7 added
---

# Helpful Water A: filter straw design decisions register

Every design decision still to be made, and every decision made, in one place. Each is argued in its decision record under `docs/decisions/`; this register is the index Amish works from. Nothing here is recorded as Amish's decision unless he made it: the concept choice and every design choice below are **Proposed, awaiting Amish**. The STEM fixes F1 to F11 were made under Amish's standing instruction of 2026-10-23 (STANDARDS section 20) and he can reverse any of them; F6 to F11 follow the independent review of 2026-11-11 (HWA-STM-001).

## Open decisions

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| D1 | Concept choice | A1 hollow-fibre straw with backflush (164); A2 ceramic tube (135, fails flow); A3 copper and charcoal (125, fails efficacy) | A1. Proposed, awaiting Amish | Everything | HWA-OPT-001, HWA-DDR-001 |
| D2 | Membrane grade (a safety trade-off) | (a) 0.1 um microfiltration, at least 1,800 L/(m2 h bar) at 25 C (1,600 at 20 C): 110 mL/min at 10 kPa; better margin on thin bacteria such as Leptospira (about 0.1 um across); (b) 0.2 um microfiltration, at least 3,300 at 25 C (2,930 at 20 C): 179 mL/min; Leptospira passes 0.2 um membranes; (c) 100 kDa ultrafiltration: 15 to 37 mL/min, fails flow. Neither grade's listed minimum reaches the 3,420 at 20 C that 200 mL/min needs | Prototype both (a) and (b) with the same housing; choose on the laboratory log reductions (HWP-VER-001 TA, TB) at the flow each gives, and only a grade with an absolute rating, a *B. diminuta* retention challenge and a supplier challenge report for at least 6 log bacteria. Proposed, awaiting Amish | Module specification (BOM 5); PR-001, PR-002 | HWA-STM-001 S2 to S4, HWA-CAL-001 section 4 |
| D3 | Flow target for PR-002 and PR-003 | (a) Rev A: 200 mL/min at 10 kPa, not met on paper by either grade (110 to 179 upright; 117 to 191 at the dip line, primed); (b) 400 mL/min, which users want: needs 21 to 33 kPa, not reachable at a comfortable sip; (c) (a) plus a 245 mm body (UR-012 allows under 250 mm): 138 to 213 mL/min at 10 kPa; (d) a lower target, such as 150 mL/min at 10 kPa on clean water, stated as an upper bound | (c) with the 0.2 um grade is the only arrangement that reaches 200 on paper; otherwise (d). Keep the child target of 80 mL/min at 5 kPa as at risk (45 to 74). Decide after the persona trials. Proposed, awaiting Amish | Length of housing and module | Concept validation questions item 12; HWA-CAL-001 section 4 |
| D4 | User integrity check | (a) 50 kPa plunger-hold air check with the supplied syringe through the backflush socket (push to the 6 mL mark, hold 10 s; finds gross defects of 5.6 um and larger, F7); (b) flow decline and replacement by volume only | (a), if the module supplier rates the membrane for 60 kPa of reverse pressure and the laboratory confirms that a cut fibre and a missing collar O-ring show (TA, TF). Proposed, awaiting Amish | Instructions and pictograms; syringe | HWA-STM-001 S20 |
| D5 | Backflush tool | (a) supply a 20 mL luer-slip syringe (BOM 17); (b) mouth-to-socket backflush; (c) squeeze bulb | (a). Rev A forbids reverse flushing by mouth; a syringe also gives the air-hold check. Proposed, awaiting Amish | BOM 17; instructions | Rev A item 10 |
| D6 | Carbon cartridge and mouthpiece | (a) separate cartridge behind a removable mouthpiece (as modelled); (b) one replaceable top that carries both, so the clean header is opened only by a factory-sealed new top, and each household member can have their own top | (b) for the next revision, after persona trials. Proposed, awaiting Amish | Mouthpiece and cartridge bodies | HWA-OPT-001 runner-up idea; UR-020 |
| D7 | Carbon at all | (a) carbon stage (taste, resupply needed); (b) a variant without carbon, where taste is not a barrier to use and resupply cannot be assured | Offer both from the same housing (a spacer replaces the cartridge); ask the field partner. Proposed, awaiting Amish | Carbon cartridge or spacer | Concept validation review (who resupplies the carbon) |
| D8 | Mesh aperture | 150, 250 or 350 um | 250 um baseline; the other two for the fouling tests (TE). Proposed, awaiting Amish | BOM 2 | Rev A item 2 |
| D9 | Mouthpiece check valve | (a) none (as modelled); (b) umbrella valve against blow-back | (a): Rev A advises against valves that obstruct drinking or cleaning; revisit if blow-back fouls the carbon in trials. Proposed, awaiting Amish | Mouthpiece | Rev A item 9 |
| D10 | Air trapped in the dirty shell (HWA-STM-001 S28) | (a) instructions only: keep the intake cover on between uses, dip to the dip line, flow stated primed and unprimed (F8, as now); (b) a re-prime step (hold the straw intake up under water and tap) if trials show it vents the shell through the wetted 250 um mesh; (c) a hydrophobic air vent from the top of the shell into the clean header that primes the shell on every sip, which adds a clean/dirty boundary that can wet out (a safety trade-off) | (a) now, test (b) in TC; (c) only if (a) and (b) fail in trials, with its own integrity test. Proposed, awaiting Amish | Instructions; possibly the module collar | Independent review M2 |
| D11 | Backflush pressure limit (HWA-STM-001 S30) | (a) instruction and pictogram only; (b) a luer pressure-relief or a calibrated spring in the syringe line; (c) a larger-bore syringe, which lowers the pressure per newton but makes the air check harder | Set by the module's reverse rating (C2); if it is under 200 kPa, (b). Proposed, awaiting Amish | BOM 17; socket | Independent review M11 |
| D12 | Socket bypass when the plug is out and the socket is under water (S29: about 506 mL/min, silent) | (a) tethered plug, socket 43 mm above the dip line and pictogram (as now); (b) a self-closing luer-activated socket, if one fits the 30 mm envelope (0.4 mm margin now); (c) move the backflush entry into the mouthpiece cap so the socket only exists while the cap is on | (a) for the prototype; ask makers about (b); study (c) with D6. Proposed, awaiting Amish | Housing boss, plug, mouthpiece cap | Independent review M4 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| C1 | A pre-potted outside-in module to the BOM 5 drawing: collar 21.8 mm with two glands (or one we can groove), bundle 17.2 mm, about 102 mm active, far ends closed | The housing, seals and header are drawn round it | HWA-BLD-001 section 3 |
| C2 | The module's maximum reverse (backflush) pressure, bubble point, integrity method and free-chlorine tolerance (ppm h) | Backflush at 50 kPa, a 60 N push (191 kPa), the air check and chlorine co-treatment depend on it; SepraPor lists 1.0 to 1.4 bar forward TMP and no backflush rating | HWA-STM-001 S19, S20, S30, S31 |
| C3 | Clean-water permeability at 20 C on the supplier's certificate, its temperature normalisation and its area basis (lumen or outer) | Flow depends on it more than on any other part; the datasheet values are at 25 C and do not state the area basis | HWA-CAL-001 assumption A1 |
| C4 | Freedom to operate against US 8,852,439 B2 by a patent attorney | Desk reading only so far | HWA-OPT-001, HWP-FTO-001 |
| C5 | EPDM O-ring compound, membrane (with its wetting agent and residual solvent), potting and GAC with drinking-water material listings; the first-flush volume | Leaching (UR-011) | HWP-REG-001 W7, HWA-STM-001 S23 |
| C6 | Fines pad permeability and its permanent hydrophilic treatment | Third largest pressure loss, assumed; untreated PP needs 2.5 kPa to wet | HWA-CAL-001 assumption A6, HWA-STM-001 S32 |
| C7 | An absolute rating with a *Brevundimonas diminuta* retention challenge report for the chosen grade | Thin bacteria (0.1 to 0.4 um) sit below a nominal 0.2 um label | HWA-STM-001 S11 |

## Value engineering

Value-engineering target: USD 25 for prototype parts (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 17.46 (USD 7.54 under the target). The program target at mass production is about USD 1 to 5 a unit (HWP-PLN-001). Main cost drivers: the bought hollow-fibre module (USD 8.00, 46 %), the printed housing (USD 2.50) and six O-rings (USD 1.50). Savings worth trying: a module bought by the hundred to the program's own drawing; one moulded housing with the intake cap captive; dropping the intake cover; a mouthpiece and carbon top in one moulding (D6).

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-11-11 | Program shape (one repo, lettered solutions A to D), licences (CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0), no archive, credits list | Amish | Program `project.yaml`, STANDARDS 25 |
| 2026-11-11 | "No virus claim, co-treat": solution A makes no virus claim and carries the on-product warning pointing to solution D or a WHO-recommended tablet | Amish | HWP-CLM-001 |
| 2026-11-11 | F1: AS568-018 EPDM O-rings in 19.3 mm male glands replace the Rev A 20 x 2 mm rings | Under Amish's standing instruction of 2026-10-23 | HWA-DDR-003 |
| 2026-11-11 | F2: full-bore single-ended bundle, about 220 fibres, lumens open into a clean header; central permeate tube dropped | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F3: membrane clean-water permeability at least 1,800 L/(m2 h bar) at 20 C (PR-004) | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F4: backflush socket on the clean header, carbon dead-ended by the mouthpiece cap plug | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F5: carbon bed 1.9 to 2.0 g, not 5 g | Under the standing instruction | HWA-DDR-003 |

| 2026-11-11 | Independent STEM review run (open item "independent review not run" closed): a separate agent attacked 27 rows; 13 hold, 10 weak, 4 refuted; 13 missed claims | Under STANDARDS section 20 (method); the findings are recorded, not decided | HWA-STM-001 Independent review |
| 2026-11-11 | Correction: SepraPor permeabilities converted from their 25 C basis to 20 C (flows 0.89 times lower) | Calculation correction | HWA-CAL-001 section 3 |
| 2026-11-11 | F6: hydrophilic-treated fines pad (BOM 10) | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F7: air check restated as a plunger-hold test to the 6 mL mark, gross defects only, re-prime after | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F8: priming and immersion stated in every flow figure; intake cover kept on between uses | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F9: bores and gland floors reamed or turned to +-0.05 mm (squeeze 18 to 30 %) | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F10: PR-001 absolute rating with a *B. diminuta* challenge; Leptospira in the exclusions | Under the standing instruction | HWA-DDR-003 |
| 2026-11-11 | F11: syringe filled with treated water only; first flush of 3 x 40 mL; chlorine contact time completed before drinking | Under the standing instruction | HWA-DDR-003 |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
