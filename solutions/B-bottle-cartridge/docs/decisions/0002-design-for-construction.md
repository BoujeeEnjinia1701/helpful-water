---
doc_id: HWB-DDR-002
title: "Helpful Water B: design for construction"
project: "Helpful Water B: bottle cartridge"
doc_type: Decision record
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Changes that make the B1 cartridge constructable (STANDARDS section 18), checked with the D3 model"
---

# Helpful Water B: design for construction

**Status: Made under STANDARDS section 18** (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). None changes what the cartridge does, its pitch or its safety case. Each was checked in `cad/src/model.py` with `python .kit/cad_check.py` (no two parts overlap by more than 5 mm3 except seals at their compressed fit, media in their seats and threads at half a pitch).

Table 1. Changes from the concept to the constructable design.

| Component | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| Neck interface | "Screw-on cartridge" | A collar with a 28 mm PCO 1881 female thread in a 15.5 mm skirt and a flat EPDM gasket on the neck lip | Seals on the lip, so the same collar fits the taller PCO 1810 neck |
| Housing joint | One body | Collar and housing joined by a 40 x 3 mm thread with a 33.4 x 2 O-ring on a seal land | The capsule and mesh must be reachable by hand (UR-019); the O-ring keeps bottle water in |
| Module retention | Module "in the housing" | The header shoulders against a 4 mm end wall; its nipple passes a 10.4 mm bore; two O-rings in 2.4 mm grooves seal in a 37 mm bore | Fixes the module axially and makes the header the only dirty-to-clean seal |
| Potting | Potting depth 8 to 12 mm (Rev A) | 10 mm in a 31 mm header; 800 fibre ends at 53 % packing; fibre count cut from 450 to 400 | At 60 % packing potting becomes hard to fill without voids |
| Carbon capsule | A carbon bay | A printed cup with a 29.8 mm plug into the collar bore, a holed floor, two nonwoven pads and a press-in lid with finger notches | Tool-free change; the lid was first drawn with a pull tab that hit the module foot and was replaced by notches |
| Spout and valve | "Drink valve" | Spout on a 20 x 2 mm thread with a flat gasket; nozzle with an O-ring groove and side ports; push-pull sleeve with a sealing plug | Opens and closes by hand; parts printable |
| Dust cover | Not in the concept | Cap on two cheeks with a 1.5 x 9 mm stainless pin through a spout lug | Keeps hands and dust off the clean outlet (UR-010) |
| Housing wall | 2.5 mm (first model, 72 g) | 2 mm (41 mm outside), grip band 44 mm with 16 ribs | Mass; factor of 6 on printed PP at a hard backflush (HWB-CAL-001 section 6) |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
