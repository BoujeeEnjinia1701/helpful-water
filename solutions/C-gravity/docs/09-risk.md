---
doc_id: HWC-RSK-001
title: "Helpful Water C: household gravity filter risk register"
project: "Helpful Water C: household gravity filter"
doc_type: Risk register
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Project risks, preliminary hazard analysis and first-pass design FMEA for C1 at P3"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Decisions recorded as Amish's (all pending decisions settled on their recommendations, 2026-11-11)

---

# Helpful Water C: household gravity filter risk register

The largest risks for C are silent failure (a broken fibre or a frozen module that still flows), false reassurance against hazards C does not address (viruses without D, dissolved chemicals), and a tall loaded stand in a home with children. The design answers with an air hold test, a no-virus label and the D interface, and wider feet with a wall strap (HWC-DEC-001 D4); the rest waits on accredited tests. Likelihood and impact are scored 1 to 5; the design FMEA uses severity, occurrence and detection 1 to 10 and RPN = S x O x D.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## Project risks

Table 1. Project risk register.

| # | Risk | Cause | Effect | L | I | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Module flux below the assumed value | Permeability assumed at 1,000 L/(m2 h bar) | Daily filtering over 3 h | 3 | 3 | Membrane engineer | Supplier data at 5 kPa (HWC-DEC-001 C1); larger module or lower shelf as fallback |
| P2 | No supplier offers a suitable pre-potted gravity module | Niche geometry | Custom potting, which the Rev A specification advises against | 2 | 4 | Program lead | Request for quotation to several makers; accept a standard inline module and adapt the clips |
| P3 | Accredited tests fail the reduction targets | Seal, potting or fibre defects | Kill criterion | 2 | 5 | Microbiologist | Supplier integrity data first (TA); test before any field step |
| P4 | Households stop using it | Fill height, slow batches, chlorine taste | Low sustained use (the Kenya warning) | 3 | 4 | Human-factors lead | Persona trials (TH); D5 shelf height; adoption KPI at 3, 6, 12 months |
| P5 | Module not resupplied after about two years | Logistics in dispersed populations | Use past rated life | 3 | 4 | NGO liaison | Tally card retirement trigger (PR-012); resupply in the partner plan |
| P6 | D interface not agreed | Two solutions designed in parallel | Port mismatch | 2 | 2 | Program lead | Agree the 60 mm port with the D team (HWC-DEC-001 D7) |
| P7 | Cost over the value-engineering target | Stand, module, buckets | Higher unit cost | 4 | 2 | Design lead | Value-engineering list in HWC-DEC-001 |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity (1 to 5) | Likelihood (1 to 5) | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Pathogens pass a damaged membrane | Broken fibre, freezing, potting defect | Diarrhoeal disease, worst in infants and immunocompromised users | 5 | 2 | Integrity-tested module; air hold test; retire after freezing; release limitation | Medium until tested |
| H2 | Viruses pass the filter | Membrane is 0.1 um | Viral disease | 5 | 3 without D | No-virus label and pictogram; D dosing port and 30 minute hold | Medium; low with D |
| H3 | Dissolved chemicals not removed | Arsenic, fluoride, nitrate, lead, pesticides in the source | Chronic poisoning with false reassurance | 4 | 2 | Exclusions on the label; source screening (HWP-SRC-001) | Medium |
| H4 | Recontamination in storage | Dipping, open lid, dirty tap | Disease | 4 | 2 | Closed lid, screened vent, tap; weekly chlorine rinse; D residual | Low |
| H5 | Stand tips over | Child pulls or climbs; uneven floor | Crush injury from 18 kg falling from about 1.2 m | 4 | 2 | 560 mm feet; wall strap proposed (D4); level floor | Low with strap |
| H6 | Contaminated clean side during service | Dirty hands or raw water used for backflush | Disease | 4 | 2 | Backflush water only from the clean tap; pinch clamp; colour coding | Low |
| H7 | Leaching from containers or fittings | Non-food-grade bucket, PVC hose, brass | Chemical exposure | 3 | 2 | Food-grade new parts; silicone hose; PP valve; certificates | Low |
| H8 | Chlorine overdose from D | Dosing error | Taste rejection; exposure above 5 mg/L | 3 | 2 | D's dose design; C's port does not set the dose | Owned by D |
| H9 | Back strain while filling | Lifting a full bucket | Injury | 2 | 3 | Fill in place from 5 L jugs (PR-027) | Low |

## Design FMEA (first pass, P3)

Table 3. Design FMEA for C1. RPN = severity x occurrence x detection.

| Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hollow-fibre module | Remove bacteria and cysts | Broken fibre | Pathogens pass; flow unchanged | Freezing, knock, ageing | 10 | 3 | 5 | 150 | Air hold test monthly (F5); retire after freezing; supplier integrity test (TI) |
| Hollow-fibre module | Pass enough water | Fouling | Slow batches; users give up | Turbid water, clay | 5 | 6 | 2 | 60 | Settle 1 to 1.5 h; cloth; backflush; retirement trigger |
| Potting and header | Separate dirty from clean | Potting leak | Bypass | Process defect | 10 | 2 | 6 | 120 | Buy integrity-tested modules; lot certificates (TA) |
| Raw outlet bulkhead | Seal the wall | Leak | Water on the stand; no contamination of the clean side | Loose nut, gasket | 3 | 3 | 2 | 18 | Hand tight plus a quarter turn; first check 2 |
| Strainer | Keep grit out of valve and module | Clogged | Slow batch | Sediment | 3 | 4 | 3 | 36 | Rinse when the bucket is washed |
| Ball valve | Hold the raw batch for contact time | Opened early | Short chlorine contact | User error | 6 | 4 | 5 | 120 | Valve tag (F4); pictogram; D's own timer if any |
| Raw hose | Carry raw water to the module | High loop traps air | Reduced flow | Routing | 4 | 3 | 3 | 36 | Hose falls all the way; bleed screw (F2) |
| Tee and check valve | Allow backflush and air test | Cap or valve lost | Port open to dirt on the clean side | Handling | 8 | 3 | 4 | 96 | Cap tethered (to add at TRL 4); clean before use |
| Clean hose and inlet | Carry permeate to storage | Hose pulled off barb | Treated water spilled; port exposed | Knock | 6 | 2 | 2 | 24 | Barb with ridges; hose routed inside the stand |
| Clean bucket and lid | Keep treated water closed | Lid left off; dipping | Recontamination | Behaviour | 7 | 4 | 4 | 112 | Tap only; label; weekly rinse; D residual |
| Clean bucket | Hold one batch | Overflow | Spill | Batch started too early | 3 | 3 | 2 | 18 | 2.5 L refill line (F3) |
| Stand | Hold 18 kg at 0.9 m | Tips over | Injury | Child pull | 8 | 2 | 6 | 96 | Feet (F1); wall strap (D4) |
| Labels | Tell users the limits | Faded or misunderstood | Misuse; false reassurance | Sun, literacy | 7 | 3 | 5 | 105 | Pictograms; comprehension trials (TH) |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
