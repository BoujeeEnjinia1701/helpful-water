---
doc_id: HWC-DDR-002
title: "Helpful Water C: design for construction"
project: "Helpful Water C: household gravity filter"
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
    change: "Changes made to make C1 constructable (STANDARDS section 18; Amish, 2026-09-30)"
---

# Helpful Water C: design for construction

**Status: made under the build-plan rule (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"); Amish can reverse any of it.** None of these changes alters what C1 does, its pitch or its safety case.

Table 1. Changes made to make C1 buildable.

| # | Concept as briefed | Constructable design | Reason |
| --- | --- | --- | --- |
| 1 | Raw bucket "above" the clean container | Bolted timber stand: four 45 x 45 legs on two feet, two lower rails, plywood shelves at 900 and 138 mm, two diagonal braces | Sets the head (0.42 to 0.66 m) and keeps the tap at cup height; every joint is a coach screw, a bolt set or a wood screw |
| 2 | Lower shelf on the floor or feet | Lower shelf notched round the legs and resting on rails at 120 mm | The feet sit under the legs, so a shelf on them would clash; the rails carry the shelf clear of the floor |
| 3 | Clean bucket centred | Clean bucket 75 mm forward of centre | Its tap must overhang the shelf so a cup fits under it |
| 4 | Module clipped "on the leg" | Module beside the front right leg, P-clip tabs screwed to the leg's front face on its centre line | A screw at the leg's edge (1.5 mm from it, in the first model) would split the timber |
| 5 | Foot screws 100 mm | All coach screws 80 mm | The 100 mm screws reached the rail bolts inside the legs |
| 6 | Hose, valve and fittings unspecified | 1/2 in polypropylene bulkhead with two gaskets, ball valve, 3/8 in barbs, silicone hose, tee with luer port, pinch clamp | Standard bought fittings; no glue or potting; silicone avoids plasticiser leaching |
| 7 | Lid openings unspecified | Printed cloth clamp ring, fill cover, dosing collar and cap; printed clean inlet fitting and screened vent cap | Seven small printed parts make every opening closable and cleanable |
| 8 | Labels flat | Labels tilted 3 deg to the bucket taper | They sat inside the tapered wall in the first model |

Every change is checked by `python .kit/cad_check.py` (no part overlaps another by more than 5 mm3 except the listed seals, hoses and media) and shown in HWC-BLD-001 section 2.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
