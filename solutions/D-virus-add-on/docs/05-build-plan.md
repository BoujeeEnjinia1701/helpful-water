---
doc_id: HWD-BLD-001
title: "Helpful Water D: chlorine add-on for viruses prototype build plan"
project: "Helpful Water D: chlorine add-on for viruses"
doc_type: Build plan
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First prototype build plan for the D1 tablet dose cap, with pictures generated from the model
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Timer check at 45 minutes and expansion note (F11, C5); groove root 17.9 mm with tolerances (F10); plug not PC (F12)
---

# Helpful Water D: chlorine add-on for viruses prototype build plan

**Plan, not yet built.** This plan tells a capable maker how to build the first proof-of-concept D1 dose cap, part by part, and how to check it with known potable test water only. Building and testing to it is TRL 4 work and has not started. Open decisions and items to confirm are kept in the design decisions register (HWD-DEC-001), not here.

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## 1. What you are building

![D1 components in build order](05-build-plan/overview.png)

Figure 1. Every component of the D1 dose cap, pulled apart and numbered in build order.

A cap that screws onto a 1 L PET bottle in place of its own cap. Inside it, a blue well holds one chlorine tablet behind a clear screw plug; on its side, a clear tube with a small steel ball in thick silicone fluid turns end over end and takes about 45 minutes to empty its fall (at least 30 minutes up to 40 C). Seven parts are printed, one is cut from tube, one from clear sheet; the rest are bought O-rings, a liner, a ball, the fluid, two screws and labels. The parts cost about USD 6, and twenty test tablets about USD 3.

## 2. What changed to make it buildable

Table 1. Changes from the concept (HWD-DDR-002, HWD-DDR-003).

| Concept had | Constructable design has | Why |
| --- | --- | --- |
| A through pin as the timer pivot | Two short trunnions moulded on the timer hub, running in a hole in the cap and a hole in the window | A pin across the tube would block the ball's path |
| A solid crown 10 mm thick | A coring groove from the top, 4 mm wide and 12 mm deep, away from the timer boss | Even walls that print and mould without sinking |
| One holder for every tablet size | Two colour-keyed inserts: blue 9.5 mm bore (1 L), orange 14.5 mm bore (20 L) | A 20 L tablet must not fit a 1 L bottle |
| An open well 12 mm deep | A stop spigot under the plug that leaves room for two tablets, not three | Keeps the dose under 5 mg/L |
| An insert O-ring groove with no squeeze | Groove root 17.9 mm (22 % squeeze in the 20.4 mm bore; 15 to 28 % over a bore of +/-0.05 mm and a groove of +/-0.03 mm) | The ring held nothing at 17.2 mm, and 17.8 mm fell to 8 % at print tolerance (F5, F10) |
| A thick insert floor | Floor hollowed from below, leaving a central boss with four slots | Even walls; water still reaches the slots |
| A timer capsule 23 mm long | 21 mm long, so its corners clear the 22.5 mm slot as it turns | It jammed half way round |

## 3. Making the components

### 3.1 Dose cap body

![Making sketch HWD-DWG-101](../cad/drawings/HWD-DWG-101.png)

Figure 2. Making sketch of the cap body (HWD-DWG-101).

What it is: the main part, printed in food-contact polypropylene. How to make it:

1. Print skirt-down at 0.15 mm layers, 100 % infill, so the thread inside the skirt and the plug thread at the top are dense.
2. Clean the 28 mm bottle thread with a bottle: screw a 1 L bottle on and off five times.
3. Ream the 20.4 mm well bore and the 2.2 mm bearing hole in the side slot; open the two 1.6 mm pilot holes for the window screws.
4. Clear any strings from the 7.5 mm side slot so the timer can turn.

How it fits: the bottle's neck lip presses on the silicone liner under the 4 mm deck; the blue insert sits on the top of the deck inside the 20.4 mm bore; the plug screws into the 22.4 mm thread at the top. Check before moving on: a bottle screws on fully by hand; the slot is clear end to end.

![Joint: cap on the bottle neck](05-build-plan/joint-01.png)

Figure 3. The cap on the bottle neck, cut open: thread, liner and deck.

### 3.2 Tablet well inserts (blue 1 L, orange 20 L)

![Making sketch HWD-DWG-102](../cad/drawings/HWD-DWG-102.png)

Figure 4. Making sketch of the 1 L insert (HWD-DWG-102).

What it is: a 20 mm plug-in cup that holds the tablet. The blue one has a 9.5 mm bore and one key notch; the orange one, for C's bucket port, has a 14.5 mm bore, a lower floor and two key notches. How to make it: print floor-down in coloured polypropylene, 100 % infill; open the four 1.5 mm floor slots and the 1.6 mm centre hole with a drill held in the fingers. How it fits: an O-ring on its side grips the 20.4 mm bore; the floor sits on the deck; the plug's stop spigot comes down to 8 mm above the floor (blue) or 11 mm (orange). Check: a 20 L tablet does not enter the blue bore; two 1 L tablets fit under the plug, a third does not.

![Joint: tablet well](05-build-plan/joint-02.png)

Figure 5. The well cut open: insert, its O-ring, the tablet and the plug stop.

### 3.3 Well plug

![Making sketch HWD-DWG-103](../cad/drawings/HWD-DWG-103.png)

Figure 6. Making sketch of the well plug (HWD-DWG-103).

What it is: a clear screw plug with a knurled 27 mm head, so the tablet can be seen. How to make it: print head-down in clear PETG at 0.1 mm layers, then polish the head top with fine abrasive and a drop of oil so it is see-through. How it fits: 3.5 turns into the cap; its face O-ring seals on the crown top; its 9 mm spigot limits the tablets. Check: with the plug home, a bottle of test water held upside down for a minute does not drip.

### 3.4 Tether

![Making sketch HWD-DWG-104](../cad/drawings/HWD-DWG-104.png)

Figure 7. Making sketch of the tether (HWD-DWG-104).

A soft band and strap printed in TPU 95A. The band rolls over the crown into place 2 mm below its top; the strap end loops through the lug on the plug head. Check: the plug lifts off and turns without the strap pulling tight.

### 3.5 Timer capsule: tube, end caps and hub

![Making sketch HWD-DWG-105](../cad/drawings/HWD-DWG-105.png)

Figure 8. Making sketch of the timer hub (HWD-DWG-105).

![Making sketch HWD-DWG-106](../cad/drawings/HWD-DWG-106.png)

Figure 9. Making sketch of a timer end cap (HWD-DWG-106).

What it is: an 18 mm length of clear polycarbonate tube (6 mm outside, 4 mm bore) closed by two printed end caps with tiny O-rings, holding a 2 mm stainless ball in about 0.2 mL of very thick silicone fluid, with a printed hub clamped round its middle. How to make it: cut the tube square with a fine saw and chamfer both ends; press the bottom cap in; warm the silicone fluid to about 40 C so it pours, fill the tube to 1.5 mm below the top, drop the ball in, push the top cap in and seal both caps with a drop of UV-cure adhesive; slide the hub to the middle and fix it with a drop of adhesive. How it fits: the hub's two 2 mm trunnions run in the bearing hole in the cap slot and in the window. Check: held upright at 25 C, the ball takes about 45 minutes (at least 40.5) to fall from the top mark to the bottom mark, so it still reads 30 minutes at 40 C; if it is faster, use a thicker fluid grade. The fluid changes volume by about 3.4 % (6 uL) between the fill and -10 or 60 C; the expansion allowance is detailed with the fluid trials (HWD-DEC-001 C5), so leave the top cap unbonded on the first capsules.

### 3.6 Timer window

![Making sketch HWD-DWG-107](../cad/drawings/HWD-DWG-107.png)

Figure 10. Making sketch of the timer window (HWD-DWG-107).

A 1.5 mm clear polycarbonate plate cut to 9 x 35 x 24.5 mm with three holes: a 2.2 mm bearing for the outer trunnion and two 2.2 mm screw holes. Check: it lies flat over the slot and the capsule turns behind it.

![Joint: ball timer](05-build-plan/joint-03.png)

Figure 11. The ball timer cut open: capsule on its trunnions in the slot, window and screws.

### 3.7 Bought components

- Neck liner: food-grade silicone, 27.6 mm outside, 20.5 mm inside, 1.5 mm thick, cut from sheet.
- O-rings: 17.2 x 1.6 mm (two, one per insert), 22.6 x 1.6 mm (plug) and 3.0 x 0.5 mm (two, timer), drinking-water grade and chlorine resistant; timer rings compatible with silicone fluid.
- Stainless ball, 2.0 mm; silicone fluid of about 400,000 to 500,000 cSt; two stainless pan-head screws for plastic, 2.2 x 6.5 mm.
- Labels: printed polyester timer scale (START band, 30 minute mark, cold-water run count) and crown pictogram (dose, shake, wait, filter; tablet key).
- Household NaDCC tablets in foil strips: 3.5 mg for 1 L and 67 mg for 20 L. Measure their diameter and thickness before printing the inserts.

## 4. Putting it together

### Step 1: build the timer capsule

![Step 1](05-build-plan/step-01.png)

Figure 12. Bottom cap, fluid and ball, top cap, hub to the middle. Hold point: let the fluid settle for an hour so no bubble sits under the ball.

### Step 2: put the capsule in the slot

![Step 2](05-build-plan/step-02.png)

Figure 13. Tilt the capsule into the side slot and push the inner trunnion into its bearing hole.

### Step 3: fit the window

![Step 3](05-build-plan/step-03.png)

Figure 14. Lay the window over the slot with the outer trunnion through its hole, then drive the two screws until snug. Do not overtighten: the capsule must still turn with a light flick.

### Step 4: labels

![Step 4](05-build-plan/step-04.png)

Figure 15. Stick the scale label on the window with its clear strip over the tube, and the pictogram label round the crown, opposite the timer.

### Step 5: neck liner

![Step 5](05-build-plan/step-05.png)

Figure 16. Press the silicone liner up into the skirt until it sits flat against the underside of the deck.

### Step 6: well insert

![Step 6](05-build-plan/step-06.png)

Figure 17. Roll the O-ring into the blue insert's groove and press the insert, slots down, into the well until it sits on the deck.

### Step 7: tether and plug

![Step 7](05-build-plan/step-07.png)

Figure 18. Roll the tether band onto the crown, fit the face O-ring under the plug head, loop the strap through the lug and screw the plug home, 3.5 turns.

### Step 8: on a bottle

![Step 8](05-build-plan/step-08.png)

Figure 19. Screw the finished cap onto a 1 L PET bottle filled with known potable test water. No tablet is used until the first checks below call for one.

## 5. First checks

The plan lists them; a TRL 4 test report records them. Use known potable test water only, and pour all chlorinated test water away; nobody drinks it.

Table 2. First checks.

| Check | Requirement | Method | Pass |
| --- | --- | --- | --- |
| Neck seal upside down | PR-012 | Cap on a full bottle, held upside down for 5 minutes over a dry tissue | No drop |
| Plug seal | PR-012 | As above with the plug unscrewed and refitted 10 times | No drop |
| Wrong tablet rejected | PR-006 | Try a 20 L tablet in the blue well | It does not enter |
| Two-tablet limit | PR-007 | Two 1 L tablets in the well, plug home; then three | Two fit; three stop the plug |
| Tablet dissolves and is seen | PR-011 | One 1 L tablet, bottle turned over and shaken | Tablet gone in a few minutes, visible through the plug |
| Timer run | PR-008 | Flip the timer five times at 25 C and time the ball from mark to mark | Every run at least 30 minutes |
| Dose and residual | PR-001, PR-002 | DPD free chlorine test (pool or field kit) at 30 and 60 minutes in known potable test water | 1.5 to 2.5 mg/L at 30 min; record the drop by 60 min |
| No overdose | PR-005 | Two tablets in 1 L, DPD at 30 min | Under 5 mg/L |
| Pictograms | PR-016 | Three people who did not build it follow the label with test water | Correct order unaided |

## 6. Safety stops

- **Before opening any tablets:** gloves and eye protection on, strips away from children, a clean area with no acids or other chemicals near; read the tablet maker's safety data sheet.
- **Before the first dose check:** the cap has passed both seal checks with plain test water.
- **Before anyone handles chlorinated water:** label the bottle "test water, do not drink"; pour it away after the check.
- **Stop if:** a tablet sticks undissolved, the timer runs under 30 minutes, the free chlorine reads above 5 mg/L, or any part cracks; fix the cause before going on.

> **Safety:** NaDCC releases chlorine; do not mix it with acids, ammonia or other chlorine products, and do not use pool tablets. Wash hands after handling tablets.

## 7. Tools, skills and workspace

An FDM printer that prints polypropylene, PETG and TPU (or a print service); a fine saw, a deburring tool, hand drills of 1.5, 1.6 and 2.2 mm; a small screwdriver; a hot-water bath at about 40 C; UV-cure adhesive and a small UV lamp; a stopwatch; a DPD free chlorine test kit; gloves and safety glasses. Skills: careful printing and small-part assembly. A clean bench with a sink.

## 8. Where the numbers come from

- `cad/src/model.py` (all sizes, option D1), `cad/fidelity.json`, `cad/step/D1/`
- `cad/drawings/HWD-DWG-001` (general arrangement), `HWD-DWG-002` (section), `HWD-DWG-101` to `107` (making sketches)
- `docs/04-calcs/01-sizing.md` and `sizing.py` (HWD-CAL-001)
- `bom/bom.csv`
- `cad/src/build_plan_media.py` (these pictures)

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
