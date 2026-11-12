---
doc_id: HWA-DDR-003
title: "Helpful Water A: filter straw STEM check fixes"
project: "Helpful Water A: filter straw"
doc_type: Design decision record
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: Fixes F1 to F5 made under Amish's standing instruction of 2026-10-23
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Fixes F6 to F11 after the independent STEM review; F3 restated at the 25 C datasheet basis
---

# 0003: STEM check fixes F1 to F11

- **Date:** 2026-11-11
- **Status:** made under Amish's standing instruction of 2026-10-23 (STANDARDS section 20, fix rule); Amish can reverse any of them

## Context

HWA-STM-001 found five details of the Rev A specification, and its independent review of 2026-11-11 six more, that fail known science or arithmetic while the working principle (outside-in hollow fibre, carbon polish, isolated backflush) holds.

## Options considered and decision

| Fix | Failing detail | Options weighed | Made | Cost effect |
| --- | --- | --- | --- | --- |
| F1 | 20 x 2 mm O-rings (24 mm outside) in a 22 mm bore | 1.5 mm metric rings (thin gland walls); AS568-018 1.78 mm rings in male glands | AS568-018, gland floor 19.3 mm, 2.4 mm wide: squeeze 24 %, stretch 2.8 %, fill 77 % | About USD 0.25 a ring |
| F2 | 40 to 80 fibres, 0.011 to 0.022 m2: 22 to 51 mL/min at 10 kPa | Two-ended header with the central tube (second potting seal, less area); U-looped fibres; single-ended full-bore bundle | Single-ended, about 220 fibres in 17.2 mm (0.056 m2); far ends closed in the bottom potting; central tube dropped | Module price to quote (C1) |
| F3 | A 100 kDa ultrafiltration fibre gives 17 to 42 mL/min at 10 kPa | Longer body only (not enough); a permeability floor | PR-004: at least 1,800 L/(m2 h bar) at 25 C (1,600 at 20 C), the floor for usable flow (110 mL/min at 10 kPa); the 0.1 or 0.2 um grade goes to Amish (D2) | None on paper |
| F4 | Backflush route not defined; a route through the carbon would push fines and growth into the lumens | Valve or switch in the outlet; socket on the header with the outlet plugged | Socket on the clean header; mouthpiece cap plug dead-ends the carbon | Plug on the existing cap |
| F5 | "5 g" of carbon in a 4.0 mL bed | Larger bed (more pressure drop, length); correct the mass | 1.9 to 2.0 g of 12 x 40 coconut GAC at 0.48 to 0.50 g/mL | Less carbon |
| F6 | Untreated non-woven PP fines pad needs about 2.5 kPa to wet (20 um pores, contact angle about 100 deg) | Drop the pad (fines reach the mouth); a hydrophilic-treated pad | Permanently hydrophilic-treated PP pad, no leachable surfactant (BOM 10) | Small; to quote |
| F7 | The air check reached 51 kPa at 13.3 mL only if no water had to leave first; bubbles cannot reach the intake upright | Larger syringe; plunger-hold criterion | Push to the 6 mL mark and hold 10 s; a plunger that keeps moving fails; a gross-defect check (5.6 um and larger); re-prime after | None |
| F8 | Flow figures assumed a full shell; trapped air leaves only the length below the outside water working | Vent (D10); state and instruct | Flows stated primed and unprimed; intake cover kept on between uses; dip to the dip line | None |
| F9 | Printed bore and gland floor at +-0.1 mm give 15 to 33 % squeeze | Larger cross-section ring (no room); tighter tolerance | Bores and gland floors reamed or turned to +-0.05 mm: 18 to 30 % | A reaming step in the build |
| F10 | "Smallest bacterium 0.5 um" was wrong; thin bacteria are 0.1 to 0.4 um | Claim nothing from the label (kept); require a validated absolute rating | PR-001: absolute rating with a *B. diminuta* retention challenge; Leptospira in the exclusions unless tested | Supplier report |
| F11 | Backflush water from the source would inoculate the clean side; leaching on first use; chlorine CT cannot happen in a 1.2 s carbon bed | Instructions | Syringe filled with treated water only; first 3 x 40 mL discarded; any chlorine contact time completed in the container before drinking | None |

## Consequences

STEM rows S1, S4, S11, S14, S17, S18, S31 and S32 close; S2, S3 and S5 stay open until Amish decides D2 and D3, and D10 to D12 are proposed for what instructions alone cannot close. The model, drawings, CAL, BOM, build plan and PRS carry the fixes; F6 to F11 change specifications and instructions only, not geometry.


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
