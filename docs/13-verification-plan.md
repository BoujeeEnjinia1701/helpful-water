---
doc_id: HWP-VER-001
title: Helpful Water verification plan
project: Helpful Water
doc_type: Verification plan
version: '0.1'
status: Draft
date: '2026-11-11'
author: Amish Chadha
license: CC-BY-4.0
revisions:
- version: '0.1'
  date: '2026-11-11'
  author: Amish Chadha
  change: First draft from the Helpful Water source pack (2026-11-11)
---

# Helpful Water verification plan

The verification that P4 will run, planned on paper so that requirements carry a verification method from the start. Nothing here is run at TRL 3, and no human study uses anything but known potable water. Families A to I come from the Rev A component specification (2026-10-14); family J is added for the chlorine add-on. Test families are lettered with a "T" prefix to keep them apart from the solution letters.

Table 1. Test families.

| Family | Method and observations | Evidence needed for the gate | Solutions |
| --- | --- | --- | --- |
| TA Membrane qualification | Supplier challenge reports; absolute or nominal rating; bubble point or the supplier's nondestructive integrity test | Certificate of analysis and lot traceability; never the pore label alone | A B C |
| TB Pathogen reduction | Independent laboratory challenge at beginning and end of life with bacteria and protozoa surrogates; virus protocol for the combined system with D | Log reduction by class at worst-case flow and temperature and after repeated use | A B C D |
| TC Hydraulics | Pressure and flow map for each stage alone and the full assembly | Pressure budget per stage; measured user effort | A B C |
| TD Field water variability | pH, turbidity, suspended solids, natural organic matter, temperature, salinity within the chosen source classes | Documented fit and no-fit conditions (HWP-SRC-001) | A B C D |
| TE Fouling and backflush | Repeated loading, service cycling, rinse inspection; volume before 50 % flow loss at 1, 10, 50 and 100 NTU | Sustained flow; at least 80 % recovery after 3 standard backflush cycles; no downstream contamination | A B C |
| TF Structural and bypass | Drops, torque, cap and cartridge cycles, O-ring cycling, temperature ageing, freezing where relevant | Integrity kept; clear retirement triggers | A B C D |
| TG Carbon and contact materials | Taste and odour marker; carbon fines; extractables and leachables of every wetted part; silver if used | Laboratory report tied to the materials and the cartridge life | A B C D |
| TH Human factors | Untrained setup, drinking comfort, one-hand use, cap and cartridge change, backflush, by persona | Failure counts by persona; comprehension; maintenance burden | A B C D |
| TI Manufacturing verification | Critical dimensions, membrane area, potting bond, lot tracking, yield | Work instructions, incoming quality control, 100 % integrity strategy | A B C D |
| TJ Chlorine dosing | Free chlorine residual after 30 and 60 minutes at pH 6 to 8.5, 5 to 30 degC, 1 to 50 NTU; dose stability over shelf life | Residual between the WHO-recommended household range and the 5 mg/L guideline value; dose drift | D |


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
