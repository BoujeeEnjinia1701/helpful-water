---
doc_id: HWD-DDR-003
title: "Helpful Water D: STEM fixes"
project: "Helpful Water D: chlorine co-treatment add-on"
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
    change: Fixes F1 to F6 made under the standing instruction of 2026-10-23
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Note that the independent review revised F4 and F6 (by F11) and F5 (by F10); see HWD-DDR-004
---

# Helpful Water D: STEM fixes

**Status:** decided under Amish's standing instruction of 2026-10-23 (STANDARDS section 20 fix rule); Amish can reverse any of them. Each keeps the working principle (a matched tablet dose, a mechanical wait indicator, filter after).

| Fix | Row | Failure as briefed | Options weighed | Fix made | Cost |
| --- | --- | --- | --- | --- | --- |
| F1 | S6 | One tablet in turbid water leaves 0.19 mg/L at 24 h | A larger tablet for all water (overdoses clear water); a turbidity test strip (cost, a step); a settle-first and two-tablet rule | Pictogram rule: settle and pour for cloudy water, two tablets; do not use D above 50 NTU; the well holds two tablets | None |
| F2 | S20 | One holder for 1 L and 20 L lets a 20 L tablet into a bottle (40 mg/L) | Separate caps; a printed warning only; keyed inserts | Blue 9.5 mm and orange 14.5 mm inserts, colour and notch keyed | USD 0.62 for the orange insert |
| F3 | S21 | Three 1 L tablets fit (6 mg/L) | A shallower insert (leaves a gap above it); a stop on the plug | A 9 mm stop spigot under the plug leaves 8.0 mm (1 L) or 11.0 mm (20 L) | None |
| F4 | S24 | One timer run is short of the 60 and 120 minute cold-water times | A temperature-compensated fluid (not available at this precision); a longer timer (too long in warm water); a run count | Run count on the label: one above 18 C, two at 10 to 18 C, four below 10 C | None |
| F5 | S26 | Insert O-ring groove root 17.2 mm gave 0 % squeeze | A larger cross-section; a shallower groove | Groove root 17.8 mm: 19 % squeeze, 3.5 % stretch | None |
| F6 | S23 | A 30 minute nominal reads 27 minutes at -10 % viscosity | Tighter fluid tolerance (cost); a longer nominal | 34 minute nominal (30.6 at the low end) | None |

The STEM check was rerun after the fixes (`docs/04-calcs/stem_check.py`). The independent review of 2026-11-11 then revised three of them, recorded in HWD-DDR-004: F4 and F6 by F11 (a 45 minute nominal that reads at least 30 minutes up to 40 C, and a run count of one, two, three) and F5 by F10 (groove root 17.9 mm with stated tolerances). F1 rests on an assumed turbid demand, so S6 is now Plausible until the TJ tests.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
