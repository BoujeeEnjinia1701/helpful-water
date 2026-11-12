---
doc_id: HWD-RSK-001
title: "Helpful Water D: chlorine add-on for viruses risk register and hazard analysis"
project: "Helpful Water D: chlorine add-on for viruses"
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
    change: Project risks, preliminary hazard analysis and first-pass design FMEA for option D1
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Four FMEA rows and two hazard rows updated from the independent review (F7, F8, F11, C5, D7)
---

# Helpful Water D: chlorine add-on for viruses risk register and hazard analysis

The highest risks are a user drinking water before the wait or without the filter, and a false sense that D makes any water safe; the design answers them with the timer, the clear plug, the sequence pictograms and the HWP-CLM-001 wording, but only human-factors trials (TH) can show they work. The highest design FMEA items are a wrong-size tablet that the key does not stop (until tablet sizes are measured) and a timer that runs fast. Likelihood, impact, severity, occurrence and detection are scored 1 to 5 (detection 5 = hard to detect).

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## Project risk register

Table 1. Project risks.

| Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- |
| No residual after the filter | Carbon in A to C removes chlorine | Stored filtered water can be recontaminated | 5 | 4 | Program lead | Decision D3; C team to address |
| Tablet sizes differ from the assumed | Several makers and strengths | Keyed bores reject the right tablet or accept a wrong one | 3 | 4 | Mechanical engineer | Measure before freezing the bores (C1) |
| Timer fluid grade | Wall factor and end effects approximate | Runs short or long | 3 | 3 | Mechanical engineer | Fall-time check per batch (C2) |
| Registration of a disinfection claim | Biocide or pesticide law | Delay or reworded claims | 3 | 3 | Regulatory specialist | Use registered bought tablets; HWP-CLM-001 wording (HWD-REG-001 W9) |
| Interface with C not agreed | C designed in parallel | No port, outlet open during the wait | 3 | 3 | Program lead | Decision D4 |
| Consumable cost for personal 1 L use | 1 L tablets cost per litre twenty times the 20 L ones | Buyers reject the personal route | 3 | 2 | Program lead | Decision D5 |
| Partner declines on chemical safety | Liability for chemicals | Program stops for D | 2 | 4 | Program lead | Kill criteria (HWD-PLN-001) |

## Preliminary hazard analysis

Table 2. Hazards.

| Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- |
| Viral infection | Water drunk before the wait, or in cold water after one run | Illness | 4 | 3 | Ball timer; run count; sequence pictogram | 2 |
| *Cryptosporidium* infection | Water drunk chlorinated but unfiltered | Illness, severe for the immunocompromised | 5 | 3 | "Filter after" on the cap and in all wording; PR-004 | 3 |
| Over-chlorination | Wrong tablet or extra tablets; a 20 L tablet dropped straight into an open bottle; two tablets in a small bottle | Taste, irritation; above WHO values (40 mg/L chlorine, 67 mg/L NaDCC for a 20 L tablet in 1 L) | 3 | 2 | Keyed inserts, two-tablet stop (F2, F3); 20 L tablets only in the household kit; bottle range on the label (F8) | 1 |
| Under-dosing | Tablet left undissolved, larger container, very turbid water, a 1 L tablet in the 20 L well, a bucket not stirred | Viruses not addressed | 4 | 3 | Clear plug; one tablet per litre or part; turbid rule (F1); pour-and-stir on the bucket (F7); field check proposed (D7) | 2 |
| Swallowed tablet or child access | Tablets loose or in an open strip | Chemical injury | 4 | 2 | Tablets stay in strips; do-not-swallow warning; kit storage | 2 |
| Chlorine gas | Tablets mixed with acids or other products | Respiratory harm | 4 | 1 | Warning; no pool tablets; D3 (TCCA) dropped | 1 |
| False confidence | User believes D makes any water safe | Use on unsuitable sources | 4 | 3 | HWP-CLM-001 wording; exclusions; not above 50 NTU | 2 |
| By-products | Chlorinating organic-rich water | Long-term exposure to THMs | 2 | 2 | Settle first; TG measures THMs | 1 |
| Leaching from prototype parts | Printed grades not listed | Contaminated test water | 2 | 2 | Test water only, poured away | 1 |

## Design FMEA (first pass, P3)

Table 3. Design FMEA for D1. RPN = severity x occurrence x detection.

| Item | Function | Failure mode | Effect | Cause | Severity | Occurrence | Detection | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Keyed insert | Reject a wrong tablet | Wrong tablet fits | Overdose or under-dose | Tablet sizes differ from assumed | 4 | 3 | 3 | 36 | Measure tablets (C1); colour and notch key; label |
| Ball timer | Show 30 minutes | Runs fast | Short contact | Fluid grade or temperature | 4 | 2 | 4 | 32 | 45 min nominal, at least 30 min up to 40 C (F11); fall-time check per batch |
| Ball timer | Reset | Flipped part way through | Short contact | User habit | 4 | 3 | 3 | 36 | START band on the label; instruction "ball at the bottom before you start" (TH) |
| Tablet well | Dissolve the tablet | Tablet stays undissolved | Under-dose | Not shaken enough | 4 | 2 | 2 | 16 | Clear plug; shake until gone |
| Plug stop | Limit to two tablets | Third tablet fits | Dose above 5 mg/L | Thin tablets | 3 | 2 | 3 | 18 | Free height from measured tablets (C1) |
| Neck liner | Seal the bottle inverted | Leak | Dose lost; wet hands with chlorinated water | Liner missing or worn | 2 | 2 | 2 | 8 | Seal check; spare liner |
| Plug O-ring | Seal the well | Leak | As above | O-ring missing | 2 | 2 | 2 | 8 | Seal check |
| Timer capsule | Hold the fluid | Fluid leaks | Timer stops working | Cap seal fails | 3 | 2 | 2 | 12 | O-rings and adhesive; visible through window |
| Label | Instruct | Faded or misunderstood | Wrong use | Sun, literacy | 4 | 3 | 3 | 36 | ISO 7010 style pictograms; comprehension trial (TH) |
| Orange insert | Take only a 20 L tablet | 1 L tablet in the 20 L well | 0.1 mg/L, silent under-dose | Key works one way only | 4 | 2 | 4 | 32 | Actual-size tablet circles on the label; 20 L tablets only in the household kit; field chlorine check proposed (D7) |
| 20 L bucket dosing | Mix the dose through 20 L | Dose stays near the surface | Under-dose low in the bucket | Bucket cannot be inverted | 4 | 3 | 4 | 48 | Pour through the well and stir 30 s (F7); mixing test (TJ); method under D4 |
| Blue insert | Dose a bottle | Used on a 0.5 L bottle with two tablets | 8 mg/L, above 5 | Small bottles share the 1881 neck | 3 | 2 | 3 | 18 | Label: 1 to 1.5 L bottles only (F8) |
| Timer capsule | Keep a bubble-free fluid | Fluid expands or shrinks 3.4 % | End cap pushed out, or a bubble in the ball path | -10 to 60 C storage | 3 | 3 | 2 | 18 | Expansion allowance (C5); freeze-thaw and 60 C fall test (TI) |
| Cap thread | Fit B's neck and C's port | Does not fit a 1810 or other neck | Cannot dose | Neck variety | 2 | 3 | 1 | 6 | Fits 1881; 1810 to check; adapter if needed |

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
