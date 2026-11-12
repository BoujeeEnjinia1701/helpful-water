---
doc_id: HWC-BLD-001
title: "Helpful Water C: household gravity filter prototype build plan"
project: "Helpful Water C: household gravity filter"
doc_type: Build plan
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First build plan for the C1 proof-of-concept prototype (STANDARDS section 18); plan, not yet built"
---

# Helpful Water C: household gravity filter prototype build plan

**Plan, not yet built.** This plan tells a capable maker how to build the first C1 prototype, a two-bucket hollow-fibre filter on a timber stand, component by component and in pictures. Building and testing to it is TRL 4 work. Anything still to be decided is in the design decisions register (HWC-DEC-001), not here.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001). Every check in this plan uses known potable test water only.

## 1. What you are building

![Every component of the C1 prototype, numbered in build order](05-build-plan/overview.png)

Figure 1. The C1 prototype pulled apart, numbered in build order.

A timber stand 520 mm wide, 560 mm deep and 900 mm high carries a blue 20 L raw bucket on its top shelf and a white 20 L clean bucket on its lower shelf. Raw water falls from a strainer outlet near the bottom of the raw bucket, through a ball valve and a clear silicone hose, into the top of a bought hollow-fibre module clipped upright to the front right leg; filtered water leaves the bottom of the module through a tee with a backflush port and rises through a second hose into the closed clean bucket, which has a tap. The parts cost about USD 86 (bill of materials).

## 2. What changed to make it buildable

Table 1. Changes from the briefed concept.

| The concept had | The constructable design has | Why |
| --- | --- | --- |
| A raw bucket "above" a clean container, height not set | A bolted timber stand, top shelf at 900 mm, lower shelf at 138 mm | Gives 0.42 to 0.66 m of head while the tap stays at cup height |
| A 420 mm square frame | 560 mm cross feet under the legs | The loaded frame tipped at 14 deg; the feet raise it to 18.7 deg |
| A module "on the hose" | The module upright beside the front right leg in two P-clips whose tabs screw to the leg's front face, inlet on top | Air in the module rises back to the bucket instead of blocking fibre area; the screws land on the leg's centre line, not its edge |
| An outlet at the bucket floor | An outlet 50 mm up behind a strainer | Sediment settles below the outlet |
| A syringe straight into the port | A luer check valve on the backflush port | The air test needs several strokes to reach 100 kPa |
| A plain module top | A bleed screw on the module's top cap | Lets shell air out at the first fill |
| Two 20 L containers | A 17 L fill line on the raw bucket and a 2.5 L refill line, just above the tap, on the clean bucket | Even a brim-full batch fits; no overflow |
| A chlorine step not tied to the filter | A dosing port in the raw lid and a "shut 30 minutes" tag on the valve | Chlorine gets its contact time before water reaches the module |
| Open clean container | Lid with an inlet fitting and a screened vent; tap 45 mm above the floor, bucket set forward so the tap overhangs | Water is never dipped; a cup fits under the tap |
| Lower shelf on the feet | Lower shelf on two bolted rails, notched round the legs | Lifts the clean bucket and its tap clear of the floor |

The reasons are argued in decision records HWC-DDR-002 and HWC-DDR-003.

## 3. Making the components

Made parts are sawn timber and plywood for the stand and seven small printed parts. Bought parts are fitted as they come, with holes drilled where the plan says.

### 3.1 Feet (two)

![Foot making sketch](../cad/drawings/HWC-DWG-102.png)

Figure 2. Foot, sketch HWC-DWG-102.

Planed softwood 45 x 45 mm, 560 mm long.

1. Cut two lengths of 560 mm, ends square.
2. Mark the middle; drill two 8.4 mm holes through, 187.5 mm either side of it (375 mm apart).
3. Counterbore each hole from below, 16 mm across and 6 mm deep, so the screw heads sit below the surface.
4. Round every edge by about 2 mm and oil with a food-safe oil.

Fit: each foot carries a pair of legs, joined by an M8 x 80 coach screw driven up from below into the leg end. Check: both feet lie flat, parallel and 375 mm apart.

### 3.2 Legs (four)

![Leg making sketch](../cad/drawings/HWC-DWG-101.png)

Figure 3. Leg, sketch HWC-DWG-101.

Planed softwood 45 x 45 mm, 837 mm long.

1. Cut four lengths of 837 mm, ends square.
2. Drill an 8.4 mm pilot hole 80 mm deep into the centre of each end.
3. Drill a 9 mm hole across each leg, side to side, 52.5 mm above the bottom end (97.5 mm above the floor), for the rail bolt.
4. Front right leg only: drill two 4.6 mm pilot holes in the front face, on its centre line, 385 mm and 535 mm above the bottom end (430 mm and 580 mm above the floor), for the P-clip screws.
5. Round the edges and oil.

Check: the legs stand on a flat floor without rocking.

### 3.3 Lower rails (two)

![Lower rail making sketch](../cad/drawings/HWC-DWG-103.png)

Figure 4. Lower rail, sketch HWC-DWG-103.

Planed softwood 45 x 45 mm, 420 mm long. Drill two 9 mm holes across, 375 mm apart and 22.5 mm below the top face, to line up with the leg holes; drill two 4.6 mm pilot holes in the top face, 300 mm apart, for the shelf screws. Fit: each rail is bolted to the outside of the left or right pair of legs with an M8 x 105 bolt, two washers and a nut through each leg. Check: the top faces are level, 120 mm above the floor.

### 3.4 Upper shelf

![Upper shelf making sketch](../cad/drawings/HWC-DWG-104.png)

Figure 5. Upper shelf, sketch HWC-DWG-104.

Exterior plywood 18 mm, 420 x 420 mm. Drill four 9 mm holes 187.5 mm from the centre each way and countersink them for the coach screw heads; round the corners and seal the edges with oil. Fit: four M8 x 80 coach screws down into the leg tops. Check: the shelf sits flat and the raw valve will clear its right edge.

### 3.5 Lower shelf

![Lower shelf making sketch](../cad/drawings/HWC-DWG-105.png)

Figure 6. Lower shelf, sketch HWC-DWG-105.

Exterior plywood 18 mm, 510 x 420 mm, with a 46 x 46 mm notch at each corner round the legs. Drill four 5 mm holes over the rails. Fit: it drops over the legs onto the rails and is held by four 5 x 30 wood screws. Check: the top face is 138 mm above the floor.

### 3.6 Diagonal braces (two)

![Diagonal brace making sketch](../cad/drawings/HWC-DWG-106.png)

Figure 7. Diagonal brace, sketch HWC-DWG-106.

Planed softwood 70 x 20 mm, about 900 mm long, ends cut to the brace angle (about 59 deg to the floor). Each runs on the outside of the left or right legs from 180 mm up at the front leg to 820 mm up at the back leg, held by one 5 x 30 wood screw into each leg. Check: the frame no longer racks when pushed at the top shelf.

### 3.7 Cloth clamp ring

![Cloth clamp ring making sketch](../cad/drawings/HWC-DWG-107.png)

Figure 8. Cloth clamp ring, sketch HWC-DWG-107.

Polypropylene (or PETG), printed flange-down at 0.2 mm layers. A 190 mm flange 4 mm thick with four grip lugs, and a 22 mm spigot 137 mm across. Fit: the folded cloth lies over the 160 mm fill hole and the spigot pushes it into the hole, where it is held by the pinch between spigot and hole. Check: it presses in by hand over eight layers of cloth and lifts out for washing.

![Raw lid joint: cloth, clamp ring, cover and dosing port](05-build-plan/joint-02.png)

Figure 9. The raw lid, cut open.

### 3.8 Fill cover

![Fill cover making sketch](../cad/drawings/HWC-DWG-108.png)

Figure 10. Fill cover, sketch HWC-DWG-108.

Polypropylene, printed top-down: a 198 mm disc 3 mm thick with a 5 mm skirt and a handle with a finger slot. It sits over the clamp ring. Check: it does not rock.

### 3.9 Dosing port collar and cap

![Dosing port collar making sketch](../cad/drawings/HWC-DWG-109.png)

Figure 11. Dosing port collar, sketch HWC-DWG-109.

![Dosing port cap making sketch](../cad/drawings/HWC-DWG-110.png)

Figure 12. Dosing port cap, sketch HWC-DWG-110.

Polypropylene. The collar has a 76 mm flange, a 59.4 mm spigot that passes the 60 mm lid hole and a 3 mm pitch thread for the 70 mm cap. It is the place where a solution D doser will sit; its size is agreed with solution D. Check: the cap turns on and off with wet hands.

### 3.10 Clean inlet fitting and vent cap

![Clean inlet fitting making sketch](../cad/drawings/HWC-DWG-111.png)

Figure 13. Clean inlet fitting, sketch HWC-DWG-111.

![Vent cap making sketch](../cad/drawings/HWC-DWG-112.png)

Figure 14. Vent cap, sketch HWC-DWG-112.

Polypropylene, printed at 100 % infill. The inlet fitting has a 40 mm flange on the lid, a 21.4 mm spigot through a 22 mm hole with a retaining collar under the lid and a 3/8 in barb on top. The vent cap has six 4 mm side ports under a closed top, a 15.4 mm spigot through a 16 mm hole and a stainless screen disc of about 0.5 mm mesh pressed inside. Check: the hose stays on the barb with a firm pull, and there is no straight line of sight into the bucket through the vent.

![Clean lid joint: inlet fitting and vent](05-build-plan/joint-05.png)

Figure 15. The clean lid, close-up.

### 3.11 Valve tag

![Valve tag making sketch](../cad/drawings/HWC-DWG-113.png)

Figure 16. Valve tag, sketch HWC-DWG-113.

Yellow polypropylene, 30 x 40 x 2 mm, with a 5 mm hole and the pictogram: tablet, clock, 30, valve shut. It hangs on the valve lever on a cable tie.

### 3.12 Bought parts and what to do to them

- **Raw bucket (blue) and lid.** A new food-grade 20 L HDPE pail with its food-contact statement; never a pail that held anything but food. Drill a 32 mm hole on one side with its centre 53 mm above the inside floor (50 mm above the floor face) using a step drill, and deburr. Mark the 17 L fill line (291 mm above the inside floor). In the lid cut a 160 mm fill hole and a 60 mm dosing hole where the sketches show.
- **Raw outlet.** A 1/2 in polypropylene bulkhead fitting with two EPDM gaskets: the flange and one gasket inside, the other gasket and the nut outside, nut hand tight plus a quarter turn. The 250 um stainless strainer pushes over the inner end; the ball valve screws onto the outer thread with PTFE tape; the 3/8 in barb screws into the valve.

![Raw outlet joint](05-build-plan/joint-01.png)

Figure 17. The raw outlet, cut open: gaskets either side of the wall, strainer inside, valve and barb outside.

- **Hollow-fibre module.** Buy a pre-potted, integrity-tested outside-in module to the BOM specification; do not pot fibres yourself. Do nothing to it but rinse it with known potable test water as its maker says.
- **Clean bucket (white) and lid.** As the raw bucket, translucent, so the level shows. Drill a 25.4 mm hole at the front with its centre 45 mm above the inside floor for the tap; mark the 2.5 L refill line, just above the tap. In the lid drill the 22 mm inlet and 16 mm vent holes.
- **Drum tap.** Gasket outside, nut inside, hand tight plus a quarter turn.

![Tap joint](05-build-plan/joint-06.png)

Figure 18. The tap, cut open.

- **Hoses, tee, check valve, pinch clamp, P-clips, syringe.** Cut the silicone hose to 0.45 m (raw) and 0.40 m (clean). The tee push-fits onto the module's outlet nipple; the luer check valve screws onto its backflush port, and the cap onto the valve. Nothing else is altered.

## 4. Putting it together

### Step 1: legs on the feet

![Step 1](05-build-plan/step-01.png)

Figure 19. Stand the four legs on the feet and drive the M8 x 80 coach screws up from below. Hold: the legs are square to the feet.

### Step 2: lower rails

![Step 2](05-build-plan/step-02.png)

Figure 20. Bolt a rail to the outside of each side pair of legs, 75 to 120 mm above the floor, with an M8 x 105 bolt set through each leg.

![Stand joint: rail bolt, shelf screw, foot screw](05-build-plan/joint-07.png)

Figure 21. The stand joint at the front right foot.

### Step 3: shelves

![Step 3](05-build-plan/step-03.png)

Figure 22. Screw the upper shelf onto the leg tops (four coach screws) and the lower shelf onto the rails (four wood screws).

### Step 4: braces

![Step 4](05-build-plan/step-04.png)

Figure 23. Screw the two diagonal braces to the outside of the side legs. Hold: the frame does not rack.

### Step 5: raw bucket outlet

![Step 5](05-build-plan/step-05.png)

Figure 24. Fit the bulkhead with a gasket each side of the wall, the strainer inside, then the valve (shut), the tag and the barb.

### Step 6: raw lid

![Step 6](05-build-plan/step-06.png)

Figure 25. Lay the folded cloth over the fill hole, press the clamp ring in, place the cover, fit the dosing collar and its cap.

### Step 7: raw bucket on the stand

![Step 7](05-build-plan/step-07.png)

Figure 26. Stand the empty raw bucket in the middle of the upper shelf with its valve to the right and snap the lid on.

### Step 8: module

![Step 8](05-build-plan/step-08.png)

Figure 27. Clip the module upright just right of the front right leg, inlet on top, and screw the two P-clip tabs to the leg's front face.

![Module joint](05-build-plan/joint-03.png)

Figure 28. The module in its P-clips on the leg.

### Step 9: raw hose

![Step 9](05-build-plan/step-09.png)

Figure 29. Push the raw hose over the valve barb and the module inlet. Hold: the hose falls all the way from valve to module, with no high loop.

### Step 10: clean bucket

![Step 10](05-build-plan/step-10.png)

Figure 30. Fit the tap, the inlet fitting and the vent cap with its screen to the clean bucket and lid.

### Step 11: clean bucket on the stand

![Step 11](05-build-plan/step-11.png)

Figure 31. Stand the clean bucket on the lower shelf, 75 mm forward of centre, tap to the front.

### Step 12: clean side

![Step 12](05-build-plan/step-12.png)

Figure 32. Push the tee onto the module outlet, screw the luer check valve and its cap onto the backflush port, run the clean hose from the tee to the lid inlet and fit the pinch clamp on it, open.

![Clean-side joint](05-build-plan/joint-04.png)

Figure 33. The tee, backflush port and pinch clamp.

## 5. First checks

All with known potable test water. The plan lists the checks; a TRL 4 test report records them.

Table 2. First checks.

| # | Check | Requirement | Pass criterion |
| --- | --- | --- | --- |
| 1 | Stand loaded with 17 L in the raw bucket, clean bucket empty: tilt by hand and push at 1 m | PR-028 | Needs more than 70 N and does not walk |
| 2 | Fill to the 17 L line, valve shut, 1 h: look for drips at the bulkhead | PR-013 | No drip |
| 3 | Open the bleed screw on the module top, open the valve, close the screw when water shows | PR-029 | Clear water reaches the clean bucket within 2 min; no air pocket in the shell |
| 4 | Time one batch from the fill line to the outlet | PR-005, PR-030 | Under 40 min with a new module |
| 5 | Clean side: look for drips at the tee and inlet while filtering | PR-013, PR-014 | Any leak drips outward; none seen |
| 6 | Fill the raw bucket to the brim and start a batch with the clean bucket at the 2.5 L refill line | PR-025 | No overflow at the vent |
| 7 | Draw a 250 mL cup with 5 L in the clean bucket | PR-006 | Under 15 s |
| 8 | Backflush: pinch clamp shut, raw valve open, three gentle syringe strokes of water from the tap through the check valve | PR-007, PR-010 | Under 2 min; push under 50 N |
| 9 | Air hold: clamp shut, raw valve open with a little water in the raw bucket; pump air strokes through the check valve until a firm push of about 5 kg (56 N) holds; watch the clear raw hose | PR-011 | No streaming bubbles from a new module |
| 10 | Labels and tag readable from the front | PR-003, PR-009, PR-012, PR-020 | All present |
| 11 | Cloth ring out, rinse, dry, refit without tools | PR-022 | Under 2 min |
| 12 | Fill height: carer fills from a 5 L jug | PR-027 | Rim at no more than 1.3 m; no spill |
| 13 | Materials record: certificates for every wetted part | PR-016, PR-001 | On file before any water test |

The remaining requirements (PR-002, PR-004, PR-008, PR-015, PR-017, PR-018, PR-019, PR-021, PR-023, PR-024, PR-026) are verified by analysis, inspection or the laboratory tests of HWP-VER-001.

## 6. Safety stops

- **Before the first fill:** the stand is on a level floor, every screw and bolt is tight, and check 1 has been done with water, not with people leaning on it. Where children are about, tie the stand to a wall.
- **Before any water touches the filter:** every wetted part is new, food grade and on the materials record; the buckets have never held chemicals.
- **Before backflushing or the air test:** the pinch clamp is shut, the check valve is on the port, the syringe holds water from the clean tap (or clean air), and the push is gentle; never point the port at a face.
- **Stop and retire the module** if bubbles stream in the air test, after any freezing, or if a batch takes more than 2 h after three backflushes. After a hard knock, run the air test before the next batch.
- **No drinking.** Nothing from the prototype is drunk until accredited testing is done (release limitation).

## 7. Tools, skills and workspace

A saw, a drill with 4.6, 8.4 and 9 mm bits, a 16 mm flat bit, a 32 mm step drill or hole saw, a 25 mm hole saw, a countersink, a 13 mm spanner or socket, a screwdriver, a tape measure and square, PTFE tape, a craft knife and a jigsaw or hole saw for the 160 mm lid hole. Basic woodworking skills; access to an FDM printer for seven small parts. A level floor about 1 m square; a sink or bucket of known potable test water.

## 8. Where the numbers come from

`cad/src/model.py` and `cad/src/params.py` (the model), `cad/drawings/HWC-DWG-001` and `HWC-DWG-002` (general arrangement and section), `cad/drawings/HWC-DWG-101` to `113` (making sketches), `docs/04-calcs/01-sizing.md` (HWC-CAL-001) and `bom/bom.csv`.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
