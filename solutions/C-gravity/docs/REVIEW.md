# Review note: Helpful Water C, household gravity filter (TRL 1 to TRL 3, 2026-11-11)

## Session 2026-11-11 (decisions): every pending decision settled

Amish, 2026-11-11: "for any pending decisions go with a recommendation. Don't leave any pending decisions in the file for Amish to make at this time." Each pending decision in HWC-DEC-001 was settled on its recommendation and is recorded as his; no decision is open. Later sections of this note are kept as the record of what was proposed at the time.

- D1: C1 two-bucket hollow-fibre filter.
- D2: 0.1 um microfiltration with solution D, in line with "no virus claim, co-treat"; suppliers quote both classes so a UF module can be tested at TRL 4.
- D3: No carbon stage; chlorine taste is accepted and tested (consistent with HWD-DEC-001 D3).
- D4: Wall strap fitted wherever children are about.
- D5: 900 mm top shelf for the prototype, tested with the household carer persona.
- D6: Blue raw side, white clean side, with pictograms.
- D7: The HWD-DEC-001 D4 interface: a 28 mm PCO 1881 port with the orange insert in the raw-bucket lid, and the outlet closed for the full wait.
- D8: Tick card for the prototype.

The cost remains over the value-engineering target (USD 86.40 against 60). `stem_check` stays `open` only because Plausible rows need TRL 4 evidence (laboratory tests, supplier data); no row fails. The options picture now shows the chosen option, and `docs/03b-traceability.md` was regenerated.

Recommended next step: create the program repo as public (Amish, 2026-11-11); TRL 4 (prototype and accredited testing under HWP-VER-001) opens only when Amish opens it with Helpful Engineering.

Session run under the common brief and the solution C brief (kit 1.9.1-he), `/to-trl3` path: STEM check first, concept options, D3 CAD of every option, calculations, drawings, priced BOM, build plan, pipeline documents. Nothing was built or tested; no git command was run. Stage P3, `trl: 3`, `design_state: constructable`, `stem_check: open`, `concept_chosen: "C1"`.

## What was done

- STEM check first: `docs/01b-stem-check.md` (HWC-STM-001), `docs/04-calcs/stem_check.py`, `stem_results.csv`, table from `stm_table.py`. Independent review by a second agent (a separate Claude process given only the claims table and sources) recorded in the STM, Table 3.
- Concept options C1 two-bucket hollow fibre, C2 ceramic candles, C3 plastic biosand: `docs/02a-concept-options.md` (HWC-OPT-001), with the comparison against claim 1 of US 8,852,439 B2.
- CAD at D3 for all three options: `cad/src/params.py`, `cad/src/model.py`, `cad/src/c_parts.py`; `python .kit/cad_check.py --export` passes (C1 86 parts and 35 fasteners, C2 29 and 4, C3 26 and 2; bare share 4 %, the two flat labels); STEP in `cad/step/C1/` and `cad/step/C1-assembly.step`, `C2-assembly.step`, `C3-assembly.step` (largest about 9 MB); STL of the seven printed parts in `cad/stl/`.
- Calculations: `docs/04-calcs/sizing.py`, `sizing_results.json`, note `docs/04-calcs/01-sizing.md` (HWC-CAL-001).
- Drawings: `cad/drawings/HWC-DWG-001` (general arrangement), `HWC-DWG-002` (section through the water path), `HWC-DWG-101` to `113` (making sketches); `cad/src/sheets.py`, `cad/src/build_plan_media.py`.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (1.75 m person for scale), `cutaway.png`, `exploded.png` (BOM numbers), `flow.png`, `concept-blueprint.png/.pdf/.svg`, `model.glb`, `viewer.html`.
- Build plan `docs/05-build-plan.md` (HWC-BLD-001) with `docs/05-build-plan/overview.png`, seven joint close-ups and twelve step pictures.
- `bom/bom.csv` (32 lines, every row priced), `project.yaml`, `README.md`, `cad/src/product_model.py`.
- Documents: PRB, PRC, URS, PRS, RTM (generated, 0 gaps), DEC, DDR-001 to 003, REG, FEA, RSK (PHA and design FMEA), MKT, PLN.
- Render queue for Amish's Mac: `/home/claude/hw/renderq/C-gravity/` (option scenes and jobs file) and `/home/claude/hw/renderq/C-gravity/views/` (hero, studio, exploded product views).

## TRL 2 section: concept

- Household day: 45 L for five people (Sphere: drinking and food 2.5 to 3 L, cooking 3 to 6 L per person).
- STEM: 36 claims; 25 within known science, 11 plausible and open, none fails. Five detail failures fixed under the standing instruction of 2026-10-23 (HWC-DDR-003): F1 560 mm feet (the 420 mm frame tipped at 14.2 deg loaded; now 18.7 deg); F2 module upright, inlet on top, bleed screw (shell air); F3 17 L fill line and 2.5 L refill line (overflow, even from a brim-full raw bucket); F4 dosing port and a 30 minute valve tag (chlorine contact before filtering); F5 luer check valve on the backflush port (found by the independent review: one syringe stroke cannot reach the air-test pressure).
- Independent review: 28 "within" rows attacked; 14 hold, 12 weakened, 2 refuted (the air test as first written, and a mass total that double-counted water). All changes are listed in HWC-STM-001 Table 3.
- Options: C1 286, C2 234, C3 227 of 345. C1 leads by 22 %; recommended, Decided by Amish on 2026-11-11.

## TRL 3 section: results (estimates; assumed membrane permeability 1,000 L/(m2 h bar))

| Quantity | C1 |
| --- | --- |
| Gravity head | 0.42 to 0.66 m (4.1 to 6.4 kPa) |
| Flow, clean and due for backflush | 30.2 and 16.3 L/h (mean over a batch) |
| Pressure per stage at the mean head | fibre walls 4.55 kPa; lumens 0.50; hoses 0.03; fittings 0.18 |
| One 14.4 L batch | 28 min clean, 52 min fouled |
| 45 L day | 1.6 h of filtering clean, 2.8 h fouled; 6.3 to 7.6 h elapsed with 1 h settling and 30 min contact per batch |
| Persona efforts | Gravity sets the flow for all users; 250 mL cup from the tap in 8.6 s; 30 N syringe push gives 54 kPa in the barrel |
| Settling | 10 um silt in 0.74 h at 20 degC, 1.13 h at 5 degC (instruction 1 h, 1.5 h below 10 degC) |
| With D | CT 15 mg min/L in 30 min against 12 for 4 log viruses at 0.5 degC; *Cryptosporidium* left to the membrane |
| Air test | Openings above about 3 um at 100 kPa (56 N push) |
| Clean-side hold-up | 83 mL (52 mL in the lumens) |
| Stability | 18.7 deg, 78 N at 1 m |
| Life (assumed) | 30,000 L, about 1.8 years |
| Size and mass | 520 x 560 x 1,300 mm; 15 kg empty, about 49 kg full |
| BOM against the target | USD 86.40 against a USD 60 value-engineering target (USD 26.40 over) |
| Cost over life | USD 0.003 a litre; USD 9.44 per person per year (before D's chlorine) |

C2: about 4 L/h, about 19 h of filtering for the 45 L day. C3: up to 0.4 L/min, 2.5 batches with pauses, 124 kg of media, up to 30 days to ripen, about 1 to 1.8 log bacteria in the cited data.

### Requirements not met or at risk

- PR-017 cost: over the value-engineering target (USD 86.40 against USD 60).
- PR-021 taste with chlorine: at risk; there is no carbon stage by design (HWC-DEC-001 D3).
- PR-027 fill height: at risk; the raw rim is at 1.27 m, a carer task (D5).
- Every flow figure (PR-005, PR-030) rests on the assumed permeability; to confirm from the supplier (C1).
- Seven requirements wait on TRL 4 tests (PR-001, 002, 009, 012, 016, 019, 026).

### Build plan findings (design for construction, HWC-DDR-002)

Stand designed as bolted timber with notched lower shelf on rails; clean bucket moved 75 mm forward so its tap overhangs; module moved beside the leg so the P-clip screws land on the leg's centre line (the first model had them 1.5 mm from its edge); foot coach screws shortened to 80 mm (they reached the rail bolts); labels tilted to the bucket taper; check valve cap spaced off the valve.

## Decisions proposed at the time (all settled by Amish on 2026-11-11; see the top section)

D1 concept choice (C1 recommended); D2 membrane class (0.1 um with D; quote 0.02 um UF too); D3 no carbon stage; D4 wall strap for the stand (recommended where children are about); D5 top shelf height (900 mm, test filling); D6 blue and white colour coding; D7 the solution D dosing interface (60 mm port, to agree with D); D8 batch tally card. Items to confirm when parts are bought: C1 to C7 in HWC-DEC-001.

## Safety concerns

- Silent failure of the membrane (broken fibre, freezing): air test and retire-after-freezing rule; the module maker's integrity test is the real proof.
- Viruses without D, and dissolved chemicals: label exclusions and the no-virus pictogram.
- A tall loaded stand in a home: wider feet now, wall strap proposed.
- Recontamination in storage: closed lid, screened vent, tap only, weekly chlorine rinse.
- Release limitation: nothing is drunk from any prototype before accredited testing.

## Checks

- `python .kit/cad_check.py --export`: PASS at D3.
- `python .kit/trace.py`: matrix written, 0 gaps.
- `python .kit/render.py --check`: every controlled document passes (front matter, claims rule, licence lines); the only failure is `media/options.png` missing, which needs Blender. Warnings: storefront items (render-hero, card, social preview, issue templates, CITATION.cff), which belong to the release step and need Blender renders first.
- Blender-only media not in this folder: `media/options.png`, `media/render-hero.png` and the other photoreal views, then `media/card.png` and `media/social-preview.png` from `.kit/cards.py`.

## Suggestions (not in the repo)

- Ask module makers for a gravity module with a top-cap bleed port and a stated flux at 5 kPa; quote both 0.1 um and 0.02 um.
- Consider a tethered cap on the backflush check valve at TRL 4 (FMEA RPN 96).

## Recommended next step

Amish decided D1 to D8 on 2026-11-11; then render the options picture and product views from the render queue on the Mac and run `python .kit/cards.py .`. The design is ready to be built and tested at TRL 4 once Amish opens P4: two prototypes to HWC-BLD-001, a flux map with known potable test water, and module quotations.
