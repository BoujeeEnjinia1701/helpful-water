# Review note: Helpful Water B, bottle cartridge (TRL 1 to TRL 3, 2026-11-11)

Session run under the common brief and the solution B brief (kit 1.9.1-he), `/to-trl3` path: STEM check first, concept options, D3 CAD of every option, calculations, drawings, priced BOM, build plan, pipeline documents. Nothing was built or tested; no git command was run. Stage P3, `trl: 3`, `design_state: constructable`, `stem_check: open`.

## What was done

- STEM check first: `docs/01b-stem-check.md` (HWB-STM-001), `docs/04-calcs/stem_check.py`, `stem_results.csv`, table from `stm_table.py`.
- Concept options B1 squeeze cartridge, B2 gravity drip stand, B3 press cup: `docs/02a-concept-options.md` (HWB-OPT-001), with the comparison against claim 1 of US 8,852,439 B2.
- CAD at D3 for all three options: `cad/src/model.py`, `cad/src/hw_parts.py`; `python .kit/cad_check.py --export` passes (B1 24 parts, B2 32, B3 24; bare share 0 %; fasteners in each); STEP in `cad/step/B1/` (23 files) and `cad/step/B1-assembly.step`, `B2-assembly.step`, `B3-assembly.step` (largest 5.2 MB); STL in `cad/stl/`.
- Calculations: `docs/04-calcs/sizing.py`, `sizing_results.json`, note `docs/04-calcs/01-sizing.md` (HWB-CAL-001).
- Drawings: `cad/drawings/HWB-DWG-001` (general arrangement), `HWB-DWG-002` (half section), `HWB-DWG-101` to `107` (making sketches); `cad/src/sheets.py`, `cad/src/build_plan_media.py`.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (hand and 1 L PET bottle for scale), `cutaway.png`, `exploded.png` (BOM numbers), `flow.png`, `concept-blueprint.png/.pdf/.svg`, `model.glb`, `viewer.html`.
- Build plan `docs/05-build-plan.md` (HWB-BLD-001) with `docs/05-build-plan/overview.png`, four joint close-ups and nine step pictures.
- `bom/bom.csv` (18 lines, every row priced), `project.yaml`, `README.md`.
- Documents: PRB, PRC, URS, PRS, RTM (generated), DEC, DDR-001 to 003, REG, FEA, RSK (PHA and design FMEA), MKT, PLN.
- Render queue for Amish's Mac: `/home/claude/hw/renderq/B-bottle-cartridge/` (three option scenes and `B-bottle-cartridge__options_jobs.json`) and `/home/claude/hw/renderq/B-bottle-cartridge/views/` (hero, studio, exploded product views from `cad/src/product_model.py`).

## TRL 2 section: concept

- STEM (first pass): 27 claims; the script gave 16 within known science and 11 plausible (the first summary said 18 and 9 in error), none fails. After the independent review: 33 claims, 14 within, 19 plausible, none fails. Four detail failures were found and fixed under the standing instruction of 2026-10-23 (HWB-DDR-003): F1 carbon moved upstream of the membrane (the briefed downstream carbon would grow bacteria on the clean side); F2 duckbill air valve (a wet membrane blocks air, so the squeezed bottle would stay crushed); F3 B2 base widened to 230 mm (tipped at 9.9 deg, now 17.2 deg); F4 B2 vent tube (the inverted bottle would vacuum-lock).
- Options: B1 246, B2 222, B3 209 of 310. B1 and B2 are within 10 % (9.8 %), so both go to Amish without a pick.
- Independent STEM review: **run on 2026-11-11** (see "Independent STEM review" below); D6 closed.

## TRL 3 section: results (estimates; assumed membrane permeability 1,000 L/(m2 h bar))

| Quantity | B1 |
| --- | --- |
| Flow, held adult squeeze 17 kPa | 465 mL/min clean, 242 fouled |
| Flow, weak child 5.8 kPa; weak elderly woman 7.2 kPa | 160 and 198 clean; 82 and 102 fouled |
| Flow at 10 kPa | 274 clean, 141 fouled |
| Stage pressure drops at 17 kPa | mesh 0.004, carbon 0.47, lumens 0.25, outlet 0.41, fibre walls 16.0 kPa |
| Membrane | 400 looped fibres 0.8/0.5 mm, 0.174 m2, potting 53 % packed |
| Carbon | 13.9 mL, 6.8 g; contact 1.8 to 5.2 s |
| Air check | shows openings above 17 um |
| Size, mass | 217 x 46 mm, about 118 g dry (claim now about 120 g), about 182 g wet |
| Clean-side hold-up | 5.7 mL downstream of the potting (drains) plus 15.2 mL in the lumens (stays wet) |
| Housing stress | hoop factor 6 at 179 kPa; flat end wall factor 9 at a full squeeze, 2.1 if the collar end were blocked in a backflush (D8) |
| Flow in 10 C water | 360 adult, 123 weak child, 152 weak elderly woman (clean) |
| Prototype parts | USD 18.35 against the USD 20 target (USD 1.65 under) |
| Scale cost; life cost | USD 7.05; USD 0.015 a litre; USD 10.8 per user per year at 9 months (USD 0.8 over the USD 10 target), USD 8.5 at 12 months |

B2: about 6.2 minutes per litre clean (11.9 fouled), heads 2.5 to 5.2 kPa. B3: 500 to 990 mL/min at 80 to 150 N.

### Requirements not met or at risk (HWB-PRS-001)

- **Not met:** PR-014 width (46 mm against UR-012's 30 mm for personal devices; B-specific 50 mm proposed, D4).
- **Over target:** PR-015 cost per user per year (USD 10.8 at 9 months).
- **At risk:** PR-005 child and elderly flow and PR-006 flow at 10 kPa once the module fouls; PR-028 housing end wall if the collar end were blocked in a backflush (D8); PR-029 backflush pressure until the module's backwash limit is known.
- Every flow requirement rests on the assumed permeability (C1) and 20 C water; at 10 C PR-004 (360) and PR-005 (123) would not be met (D9).
- Nine requirements wait for TRL 4 tests (pathogen reduction, materials, shelf life, drops, life, air return, pictograms).

### Build plan findings (HWB-DDR-002)

Collar seals on the neck lip so one collar fits PCO 1881 and 1810; collar and housing threaded with an O-ring so the mesh and capsule are reachable; module held by the end wall with two header O-rings as the single dirty-to-clean seal; fibre count cut from 450 to 400 for potting room; capsule pull tab replaced by finger notches (it hit the module); housing wall 2 mm; dust cover on a stainless pin added.

## Decisions proposed and awaiting Amish (HWB-DEC-001)

D1 concept (B1, B2, or B1 with B2's stand as an accessory; no pick, within 10 %); D2 prototype neck finish PCO 1881; D3 38 mm adapter after a neck survey; D4 B-specific width target of 50 mm; D5 squeeze-filter patent search before P4; D7 report the cost per user per year at both 9 and 12 months; D8 housing end wall at a blocked backflush (recommend 6.5 mm at the next geometry revision, procedure until then); D9 rating temperature for flow (recommend 20 C with the 10 C figures stated). D6 (independent STEM review) is closed: the review was run on 2026-11-11. `concept_chosen` reads "proposed: B1 or B2 (within 10 %), awaiting Amish".

## Independent STEM review (2026-11-11)

- Method: `claude -p --model claude-opus-5-5` as a separate process in this folder, read, shell and web tools only, given `stem_results.csv`, `stem_check.py`, `sizing.py` with the PARAMS input values, `sizing_results.json` and the cited sources; asked to refute every verdict and to look for missed 25.6 water checks. Output kept outside the repo (`/tmp/claude-0/review-B-bottle-cartridge.md`).
- Counts on the 27 rows: 10 hold, 16 weak, 1 refuted (S22); 11 missed checks (1 refuted, 9 weak, 1 holds). Two findings were checked and rejected: S20 (the stand tips about a continuous ring, not leg feet) and S24 (the skirt depth already includes the compressed gasket).
- Fixes under the standing instruction (HWB-DDR-003 v0.2): F5 upright refill; F6 50 mL first flush after storage; F7 chlorine dosed and left for its full contact time before filtering, filtered water not stored; F8 priming by syringe backflush when the first flow is low; F9 module request names hydrophilic fibres shipped wet, the 135 N potting load, the 53 % packing and a production integrity test (`bom/bom.csv` item 8).
- Corrections: weak child at the girls' 11.8 kg grip boundary (5.8 kPa, 160 mL/min, PR-005 restated); 10 C flows; S3, S9, S16, S21 made Plausible; S12 limited to chlorine taste; S26 now about 120 g; new rows S28 to S33. Files: `docs/04-calcs/sizing.py`, `stem_check.py`, `01-sizing.md` v0.2, `docs/01b-stem-check.md` v0.2, `docs/03-requirements.md` v0.2, `docs/05-build-plan.md` v0.2, `docs/06-design-decisions.md` v0.2, `docs/09-risk.md` v0.2, `docs/decisions/0003-stem-fixes.md` v0.2. No geometry changed, so CAD, drawings and media were not regenerated; BOM total unchanged at USD 18.35.

## Safety concerns

- Silent failure (broken fibre, rolled header O-ring, freezing) is the top hazard; the air check finds only openings above about 17 um. Design FMEA highest RPNs: pinhole defects (50) and clean-side biofilm in the spout (48).
- The carbon strips chlorine in seconds, so chlorine co-treatment gives virus inactivation only if the water stands for solution D's full contact time before filtering (F7); filtered water carries no residual.
- The lumens stay wet between uses (15.2 mL); grow-through in warm storage is untested, so the first 50 mL after storage is discarded (F6).
- Good taste from the carbon can build false confidence; the no-virus warning and exclusions must be on the product.
- Printed prototypes in uncertified filament must not touch drinking water; prototypes are for known potable test water only.

## Checks

- `python .kit/render.py --check`: every controlled document passes; the run fails only on `media/options.png`, which needs Blender (scenes exported to the render queue; not faked). Storefront items (`render-hero.png`, `card.png`, `social-preview.png`, issue templates, CITATION.cff in this folder) are warnings; the renders need Blender and the others live at the program root.
- `python .kit/trace.py --check`: passes, 0 gaps. The kit gap reported here (trace.py licence and licence line) was fixed in the kit (kit 1.9.1-he trace.py) on 2026-11-11 and the workaround script removed.
- `python .kit/cad_check.py --export`: PASS at D3.
- After the independent review (2026-11-11): `sizing.py`, `stem_check.py` (open: 14 within, 19 plausible, 0 fail), `stm_table.py`, `.kit/trace.py` (0 gaps), `.kit/cad_check.py` (PASS at D3; rerun because the BOM text changed, no geometry change) and `.kit/render.py --check` (fails only on `media/options.png`, which needs Blender).

## Notes for Amish

- The program README (`../../README.md`) does not exist yet; the solution README links to it.
- The kit's drawing title blocks print the hardware licence (CERN-OHL-P-2.0) on the concept blueprint, which is documentation under the guide; a kit change, not done here.
- The hand context part has a fixed grip size, so in the hero its fingers sink into the 80 mm bottle; acceptable for scale, worth a proper grip pose in a later kit.

## Recommended next step

Decide D1. Then run the independent STEM review, render the queued options picture and product views on the Mac, and, when P4 opens, request module quotations with flux at 10 kPa and the backwash limit (C1 to C3). The design is ready for TRL 4 prototyping on paper once a module is chosen; that is Amish's call.
