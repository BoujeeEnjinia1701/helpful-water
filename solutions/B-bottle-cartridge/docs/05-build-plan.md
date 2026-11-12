---
doc_id: HWB-BLD-001
title: "Helpful Water B: bottle cartridge prototype build plan"
project: "Helpful Water B: bottle cartridge"
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
    change: "First prototype build plan for the B1 squeeze cartridge (STANDARDS section 18); design made constructable (HWB-DDR-002)"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Independent STEM review: priming, upright refill, open collar end in backflush, lumen hold-up and first flush, chlorine order (HWB-DEC-001 F5 to F9)"
---

# Helpful Water B: bottle cartridge prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept B1 squeeze cartridge, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Release limitation.** The prototype is for fit, flow and leak checks with known potable test water only. It is not used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## 1. What you are building

![Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

A cartridge about 217 mm long and 46 mm across its grip ribs that screws onto a 1 L PET bottle with a 28 mm PCO 1881 neck. It has 18 components: seven printed polypropylene parts (collar, carbon capsule body and lid, housing, spout, drink valve, dust cover) and eleven bought items (a pre-potted hollow-fibre membrane module, granular carbon, two retention pads, a steel mesh disc, O-rings, two cut gaskets, a duckbill valve, a hinge pin and a 60 mL syringe). Nothing is glued or potted by the maker: the module arrives potted and tested. Parts cost about USD 18 (estimate).

## 2. What changed to make it buildable

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Carbon | Carbon after the membrane | A carbon capsule before the membrane, on the dirty side | Wet carbon after the membrane can grow bacteria on the clean side; backflush no longer passes the carbon |
| Air return | Nothing | A small silicone duckbill valve in the side of the collar | A wet membrane does not let air back in, so a squeezed bottle would stay crushed |
| Neck seal | "Screws on" | A flat rubber gasket on the neck lip inside a 28 mm thread | One collar fits both the shorter and the taller 28 mm necks |
| Module hold | Not shown | The module's header stops against the housing's end wall; two O-rings seal it in the bore | One seal line between dirty and clean water |
| Capsule lid | A pull tab | Two finger notches in the lid rim | The tab hit the foot of the module |
| Fibre count | 450 looped fibres | 400 looped fibres | Leaves room for the potting to fill between fibre ends |
| Housing wall | 2.5 mm | 2 mm with a ribbed grip band | Lighter; still six times stronger than needed at a hard backflush |

## 3. Making the components

### 3.1 Neck collar

![Making sketch](../cad/drawings/HWB-DWG-101.png)

**What it is and what it is made from.** The part that screws onto the bottle and carries the inlet, the mesh, the air valve and the thread for the housing. Polypropylene (food-contact grade), printed; PETG is an acceptable stand-in for fit checks only.

**How to make it.**

1. Print skirt-down at 0.15 mm layers, 100 % infill, so the 28 mm inside thread prints without support.
2. Ream the 18 mm inlet bore and the 6 mm counterbore for the air valve; clear the 3 mm side air bore with a drill.
3. Remove any stringing from both threads and the O-ring groove; the groove is 2.4 mm wide in the 36.6 mm seal land.

**How it fits the parts next to it.**

![Collar on the bottle neck, cut open](05-build-plan/joint-01.png)

The flat gasket sits in the top of the skirt and seals on the bottle's neck lip; the thread only holds it there, so it is screwed hand tight. The duckbill pushes into the counterbore with its lips pointing inward. The mesh disc lies on the deck, rim down.

**Check before moving on.** It screws onto a 1 L water bottle and a taller-neck soft-drink bottle by hand, and stops on the gasket before the skirt touches the support ring.

### 3.2 Carbon capsule body and lid

![Making sketch, capsule body](../cad/drawings/HWB-DWG-102.png)

![Making sketch, capsule lid](../cad/drawings/HWB-DWG-103.png)

**What it is and what it is made from.** A cup 34 mm across and 37 mm tall that holds a 20 mm bed of carbon between two pads, with a press-in lid. Polypropylene, printed in black.

**How to make it.**

1. Print the body floor-down and the lid flange-down, 100 % infill.
2. Clear the seven 3 mm holes in the floor and the seven holes in the lid.
3. Rinse the carbon in known potable test water until the rinse runs clear, and let it drain.
4. Put in the lower pad, pour in about 6.8 g (14 mL) of the drained carbon, tap it level, add the upper pad and press the lid in until its flange sits on the rim.

**How it fits.** The capsule's 29.8 mm plug drops into the collar's 30 mm bore and rests on the mesh side of the deck; the housing above holds it down. Water passing round the capsule only loses some taste benefit; it never reaches the clean side.

**Check before moving on.** Shaken over white paper, no carbon grains come out of the holes.

### 3.3 Housing

![Making sketch](../cad/drawings/HWB-DWG-104.png)

**What it is and what it is made from.** The tube that holds the membrane module, 41 mm across and 165 mm long, with a 40 mm inside thread at the bottom for the collar and a 20 mm thread spigot at the top for the spout. Polypropylene, printed upright with four perimeters.

**How to make it.**

1. Print upright, bottom thread down, 0.15 mm layers.
2. Smooth the 37 mm bore where the module's O-rings will run; it must be free of layer ridges over the top 25 mm.
3. Clear the 10.4 mm bore in the end wall.

**How it fits.**

![Module header in the housing, cut open](05-build-plan/joint-03.png)

The module goes in from below, header first; its two O-rings seal in the 37 mm bore and its shoulder stops against the end wall, with the outlet nipple through the 10.4 mm bore. These two O-rings are the only seal between dirty and clean water.

![Housing on the collar, cut open](05-build-plan/joint-02.png)

The housing screws onto the collar's 40 mm thread until the grip band meets the collar; the collar's O-ring seals in the housing bore above the thread.

**Check before moving on.** With the module fitted, the O-rings slide in with light hand force and the module cannot fall out when the housing is turned over.

### 3.4 Spout, drink valve and dust cover

![Making sketch, spout](../cad/drawings/HWB-DWG-105.png)

![Making sketch, drink valve](../cad/drawings/HWB-DWG-106.png)

![Making sketch, dust cover](../cad/drawings/HWB-DWG-107.png)

**What they are and what they are made from.** The spout screws onto the top of the housing and carries the 12 mm nozzle; the push-pull valve slides on the nozzle; the dust cover clips over the valve on a hinge. All polypropylene, printed; a bought sports-cap valve of the same bore may replace the valve.

**How to make them.**

1. Print the spout plate-down, the valve top-down and the cover top-down.
2. Clear the four 2 mm side ports in the nozzle, the four 2 mm holes in the valve top and the 1.6 mm hinge holes.

**How they fit.**

![Spout, valve and dust cover, cut open](05-build-plan/joint-04.png)

A flat gasket goes on the housing's top spigot before the spout is screwed down. The 10 x 1.2 O-ring sits in the nozzle groove and seals inside the valve sleeve. Pushed down, the valve's plug closes the nozzle bore; pulled up 4 mm, water leaves through the side ports and out of the valve top. The cover's two cheeks straddle the spout lug and the stainless pin is pressed through all three.

**Check before moving on.** The valve slides with a firm push and pull; the cover flips open and shut.

### 3.5 Bought parts

- **Hollow-fibre membrane module:** pre-potted and integrity-tested by its maker; looped fibres about 0.8 mm across, 0.1 um rating or finer, potted 10 mm deep in a 36.6 mm header with two O-ring grooves and a 10 mm outlet nipple; with a data sheet giving clean-water flux, maximum backwash pressure and test data. Fit two 33.4 x 2 mm O-rings. Do nothing else to it.
- **Granular carbon:** coconut-shell, 12 x 40 mesh, certified for drinking-water contact. Rinse before use.
- **Mesh disc:** 316L stainless, about 150 um aperture, cut to 29.6 mm and the edge pressed over.
- **Seals:** drinking-water grade EPDM or silicone O-rings; cut the two flat gaskets from 1.5 mm and 1.2 mm sheet with hole punches.
- **Duckbill valve:** silicone, 6 mm flange, low cracking pressure.
- **Hinge pin:** stainless, 1.5 mm x 9 mm.
- **Syringe:** 60 mL slip tip, for backflushing.

## 4. Putting it together

### Step 1: fit the module into the housing

![Step 1](05-build-plan/step-01.png)

Wet the two header O-rings with clean water and push the module up into the housing from the bottom, header first, until it stops. Hold point: the nipple shows through the top bore.

### Step 2: fit the collar's small parts

![Step 2](05-build-plan/step-02.png)

Press the duckbill into its counterbore, lips inward. Lay the gasket in the skirt and the mesh disc on the deck. Roll the collar O-ring into its groove.

### Step 3: fill the carbon capsule

![Step 3](05-build-plan/step-03.png)

Lower pad, drained carbon, upper pad, lid (section 3.2).

### Step 4: drop the capsule into the collar

![Step 4](05-build-plan/step-04.png)

Plug first, until it sits on the deck.

### Step 5: screw the housing onto the collar

![Step 5](05-build-plan/step-05.png)

Hand tight, until the grip band meets the collar. Hold point: no gap between grip band and collar.

### Step 6: fit the spout

![Step 6](05-build-plan/step-06.png)

Spout gasket on the top spigot, then screw the spout down hand tight.

### Step 7: fit the drink valve

![Step 7](05-build-plan/step-07.png)

O-ring into the nozzle groove, then push the valve on.

### Step 8: hang the dust cover

![Step 8](05-build-plan/step-08.png)

Cheeks over the lug, pin pressed through.

### Step 9: put it on a bottle

![Step 9](05-build-plan/step-09.png)

Fill a 1 L PET bottle with known potable test water only, screw the cartridge on hand tight and prime it with two squeezes into a sink.

## 5. First checks

These checks are listed here and recorded in a TRL 4 test report; none has been done. Use known potable test water only.

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Neck fit | PR-024 | Screw onto a PCO 1881 bottle and a PCO 1810 bottle | Seals on the gasket by hand; no drip when squeezed upside down |
| No leaks at a hard squeeze | PR-011, PR-027 | Full bottle, valve shut, squeeze hard for 10 s | No water at the collar, grip band, spout or duckbill |
| Flow at an adult squeeze | PR-004, PR-006 | Measure mL in 30 s with a pressure gauge on a bottle fitting | At least 400 mL/min at 17 kPa and 200 mL/min at 10 kPa |
| Flow at a weak squeeze | PR-005, PR-025 | As above at 6 to 7 kPa | At least 150 mL/min |
| Air return | PR-027 | Release after a squeeze with the bottle turned upright (duckbill in air) | The bottle springs back without unscrewing |
| Priming | PR-007 | First use: two squeezes of a full bottle; if the first flow is low, a syringe backflush with the capsule out, collar end open | Water flows; no air pocket stays in the shell |
| Air check | PR-010, PR-018 | Wet the cartridge, empty the bottle, squeeze air through into a cup of water with an adult squeeze | No stream of bubbles from the outlet |
| Backflush | PR-009, PR-029 | Cartridge off the bottle, capsule out, collar end open, two 60 mL syringe strokes of treated water at a gentle push | Water leaves through the open collar end; under 2 minutes |
| Capsule change | PR-011, PR-016 | Unscrew the housing, lift out and refill the capsule | The clean side (header, spout) stays closed |
| Hold-up and drain | PR-012 | Weigh before and after upending, then run a 50 mL first flush | About 6 g drains from the header, nipple and spout (under 10 g); about 15 g stays in the lumens by design |
| Size and mass | PR-014 | Measure and weigh | About 217 mm and 118 g dry |
| Instructions and cup fill | PR-003, PR-007, PR-008, PR-020, PR-021 | Untrained user with the pictogram card | Fills a cup without mouth contact; warning seen |
| Parts and materials | PR-013, PR-022, PR-023 | Check every part against the BOM and certificates | All wetted grades certified; PP parts separable |
| Shelf, drop, taste, life | PR-001, PR-002, PR-015, PR-017, PR-019, PR-026, PR-028 | Laboratory and fouling tests of HWP-VER-001 (TA, TB, TE, TF, TG) | As the requirement states; done by an accredited laboratory |

## 6. Safety stops

- **Before first water:** stop unless every printed part is in polypropylene or another certified food-contact grade and the carbon has been rinsed. Fit checks in PETG use tap water only and the parts are then discarded.
- **Before any drinking:** stop. No prototype is used for drinking until accredited laboratories have validated it (release limitation).
- **Before backflushing:** stop unless the backflush water is treated water and the capsule is out; never backflush by mouth or through the carbon. Point the cartridge away from the face.
- **After a drop, a freeze or a stream of bubbles:** stop and retire the cartridge.
- **After any storage:** discard the first 50 mL; the lumens stay wet between uses (HWB-DEC-001 F6).
- **With chlorinated water (solution D):** dose in the bottle and wait the full contact time before filtering; the carbon removes the residual, so filtered water is used the same day and not stored (HWB-DEC-001 F7).
- **Before using a source other than known potable test water:** stop; that is TRL 4 laboratory work.

## 7. Tools, skills and workspace

A desktop FDM printer able to print polypropylene (or a print service), a 30 mm and an 18 mm reamer or a fine round file, 3 mm and 1.5 mm drills, hole punches for the gaskets, a kitchen scale to 0.1 g, a measuring jug, a 0 to 50 kPa gauge with a bottle fitting for the flow checks, and a clean bench and sink. Skills: 3D printing in PP, careful deburring. About half a day after printing.

## 8. Where the numbers come from

- Model: `cad/src/model.py` (option B1) and the STEP files in `cad/step/B1/`.
- Drawings: `cad/drawings/HWB-DWG-001` (general arrangement), `HWB-DWG-002` (section), `HWB-DWG-101` to `107` (making sketches).
- Calculations: `docs/04-calcs/01-sizing.md` (HWB-CAL-001) and `docs/04-calcs/sizing.py`.
- Parts and costs: `bom/bom.csv`.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
