# Helpful Water A: filter straw review note

## Session 2026-11-11 (decisions): every pending decision settled

Amish, 2026-11-11: "for any pending decisions go with a recommendation. Don't leave any pending decisions in the file for Amish to make at this time." Each pending decision in HWA-DEC-001 was settled on its recommendation and is recorded as his; no decision is open. Later sections of this note are kept as the record of what was proposed at the time.

- D1: A1 hollow-fibre straw with backflush.
- D2: Prototype both (a) 0.1 um and (b) 0.2 um in the same housing. The grade is then selected on the laboratory log reductions (HWP-VER-001 TA, TB) at the flow each gives, and only a grade with an absolute rating, a *B. diminuta* retention challenge and a supplier challenge report for at least 6 log bacteria is accepted. This is a selection rule, not an open decision.
- D3: (d): PR-002 becomes 150 mL/min at 10 kPa on clean water at 20 C, upright and primed, stated as an upper bound. It is met on paper with the 0.2 um grade (179) and not met with the 0.1 um grade (110). The 205 mm body stays; the 245 mm body of (c) is kept as the TRL 4 revision if persona trials ask for more flow. The child target (PR-003, 80 mL/min at 5 kPa) stays and is reported as not met on paper (45 to 74).
- D4: (a), the 50 kPa plunger-hold air check, provided the module supplier rates the membrane for 60 kPa reverse pressure and the laboratory shows a cut fibre and a missing collar O-ring (TA, TF); if either condition fails, (b).
- D5: (a): a 20 mL luer-slip syringe in the kit (BOM 17).
- D6: (a) for the prototype as modelled; (b), one replaceable top per user, for the next revision after the persona trials.
- D7: Both, from the same housing: carbon cartridge as standard, a spacer in its place for the no-carbon variant; the field partner chooses per deployment.
- D8: 250 um baseline; 150 and 350 um only in the fouling tests (TE).
- D9: (a): no mouthpiece valve; revisit only if blow-back fouls the carbon in trials.
- D10: (a) now; (b) tested in TC; (c) only if (a) and (b) both fail in trials, with its own integrity test.
- D11: Set by the module reverse rating (C2): (a) if the rating is 200 kPa or more; (b), a luer pressure relief in the syringe line, if it is under 200 kPa.
- D12: (a) for the prototype; (b) is asked of makers and (c) is studied with D6 for the next revision.

PR-002 is now 150 mL/min at 10 kPa (upper bound): met on paper with the 0.2 um grade (179), not with 0.1 um (110). PR-003 (child, 80 mL/min at 5 kPa) stays not met on paper (45 to 74). STEM rows S2, S3 and S5 are closed by D2 and D3. `stem_check` stays `open` only because Plausible rows need TRL 4 evidence (laboratory tests, supplier data); no row fails. The options picture now shows the chosen option, and `docs/03b-traceability.md` was regenerated.

Recommended next step: create the program repo as public (Amish, 2026-11-11); TRL 4 (prototype and accredited testing under HWP-VER-001) opens only when Amish opens it with Helpful Engineering.

## Session 2026-11-11 (second): independent STEM review and fixes

Brief: run an independent STEM reviewer on HWA-STM-001, verify its findings, apply the fix rule, and record the review. Nothing has been built or tested; everything below is on paper.

### What was done

- Independent reviewer: a separate `claude -p` process (Opus) given only `docs/04-calcs/stem_results.csv`, `stem_check.py`, `sizing.py` with its results, the PARAMS in `cad/src/model.py`, `bom/bom.csv` and the sources; asked to refute every Within and Plausible verdict and to find missed claims against the STANDARDS 25.6 water checks. Its report was kept outside the repo; every finding was recomputed before acting.
- Result: of 27 rows, **13 hold, 10 weak, 4 refuted** (S2, S5, S11, X6; the author judges X6 weak); **13 missed claims**. Recorded in `docs/01b-stem-check.md` (HWA-STM-001 v0.2, section "Independent review", Table 3).
- Calculation correction: the SepraPor permeabilities are normalised to 25 C (Meissner datasheet, checked 2026-11-11), not 20 C; `docs/04-calcs/sizing.py` now converts them (x 0.888) and adds the potting drop, immersion and priming, a fouling estimate (assumption A13), persona minutes, port losses in backflush, the air-check plunger mark, overpressure, the seal tolerance stack, socket bypass and wet mass.
- `docs/04-calcs/stem_check.py`: rows rewritten and S27 to S32 added (fouling, priming, socket bypass, backflush overpressure, chlorine co-treatment order, hydrophilic pad); table sorted by row.
- Fixes F6 to F11 under Amish's standing instruction of 2026-10-23 (`docs/06-design-decisions.md` v0.2, `docs/decisions/0003-stem-fixes.md` v0.2): hydrophilic fines pad; plunger-hold air check to the 6 mL mark (gross defects only); flows stated primed and unprimed, intake cover on between uses; bores and gland floors to +-0.05 mm; absolute rating with a *B. diminuta* challenge and Leptospira excluded; treated water in the syringe, first flush, chlorine contact time before drinking. None changes geometry, so `cad_check.py --export` was not rerun.
- Updated: `bom/bom.csv` (specifications of items 1, 4, 7, 10, 11, 17; no cost change), `docs/03-requirements.md` (PR-001, 002, 003, 004, 012, 027), `docs/04-calcs/01-sizing.md` (HWA-CAL-001 v0.2, new sections 4.1 to 4.3), `docs/05-build-plan.md`, `docs/09-risk.md` (FMEA F11 to F13), `docs/02-concept.md`, `docs/02a-concept-options.md`, `docs/08-feasibility.md`, `docs/11-plan.md`, `docs/decisions/0001-concept-selection.md`, `README.md` (STEM check, safety, exclusions), `project.yaml`.
- Regenerated: HWA-DWG-001 and 002 (rev P2), making sketches HWA-DWG-101, 102, 104, 105, `media/flow.png`, `media/concept-blueprint.*` (rev P2); `docs/03b-traceability.md` by `trace.py`.

### Key results now (HWA-CAL-001 v0.2)

| Quantity | Result |
| --- | --- |
| Flow at 10 kPa, clean, 20 C, upright, primed | 110 (0.1 um) to 179 (0.2 um) mL/min (was 122 to 197) |
| At the dip line: primed / air in the shell | 117 to 191 / 86 to 144 mL/min |
| Child at 5 kPa / elderly at 7 kPa | 45 to 74 / 71 to 116 mL/min; 1.5 L takes a child 20 to 33 min |
| Suction for 200 / 400 mL/min | 11.0 to 17.1 / 21 to 33 kPa; 200 needs a permeability of 3,420 at 20 C |
| Turbid water (50 mg/L, assumed cake) | 0.2 um after 20 L: 15 to 85 mL/min before backflush |
| Backflush at 50 kPa | 556 to 741 mL/min with port losses; a 60 N push gives 191 kPa |
| Air check | 51 kPa at the 6 mL mark; finds defects of 5.6 um and larger |
| Seals | Squeeze 15 to 33 % as printed, 18 to 30 % reamed |
| Mass | 66 g dry, about 106 g full |
| Cost | USD 17.46 (unchanged) |

### Requirements not met or at risk

- PR-002, 200 mL/min at 10 kPa: **not met on paper** (110 to 179). PR-003, 80 mL/min for a child: **not met on paper** (45 to 74). Only a 245 mm body with the 0.2 um grade reaches 200 (213) on paper.
- The 400 mL/min user threshold is not met by any arrangement in this envelope.
- PR-012 air check: at risk (supplier reverse rating; gross defects only). PR-017 regrowth, PR-023 mouthpiece per person: at risk.

### STEM check

A1: 32 rows; 20 within known science (8 closed by fixes), 9 plausible and open for TRL 4 evidence, 3 "Fails, fix proposed" (closed by Amish\'s decisions of 2026-11-11) (S2, S3, S5: the flow target against the grade). A2 and A3: Fails, dropped. `stem_check: open`. The open item "independent review not run" is closed.

### Decisions proposed at the time (all settled by Amish on 2026-11-11; see the top section)

D2 and D3 updated with the new numbers (and a new option D3 (d), a lower clean-water target). New: **D10** air trapped in the shell (instructions now; re-prime step or a hydrophobic vent, the vent being a safety trade-off); **D11** backflush pressure limit; **D12** socket bypass (tethered plug as now, a self-closing socket, or the backflush entry moved into the mouthpiece cap). New confirm items C7 (absolute rating with *B. diminuta* report) and wider C2, C3, C5, C6.

### Safety concerns

Silent bypass through an open socket under water (about 506 mL/min); backflush overpressure on the fibres and potting; a syringe filled from the source; thin bacteria such as Leptospira passing a 0.2 um fibre; the air check misses bacterial-size flaws. Prototypes are never drunk from.

### Notes for the program

- The program claims register HWP-CLM-001 (outside this folder) may want *Leptospira* added to the exclusions for every membrane solution; only this solution's README was changed.
- `python .kit/render.py --check`: every document passes; the only failure is `media/options.png` (needs Blender), with the known storefront warnings. `cad/fidelity.json` refreshed (`cad_check.py`, PASS D3) because the BOM text changed. `trace.py`: 0 gaps.

### Recommended next step

Amish reviews D2, D3 and D10 to D12. Then ask straw-core makers for the permeability basis (temperature and area), reverse rating and *B. diminuta* report (C2, C3, C7) before any P4 work.

## Session 2026-11-11: P0 to P3 (TRL 3) under kit 1.9.1-he

Brief: take solution A from P0 to P3 (TRL 3) under the common brief and the solution A brief. Nothing has been built or tested; everything below is on paper.

### What was done

- `project.yaml`: stage P3, TRL 3, `stem_check: open`, `concept_options: [A1, A2, A3]`, `concept_chosen: "A1"`, `design_state: constructable`, `budget_usd: 25` (value-engineering target), `trl_evidence`.
- STEM check first: `docs/01b-stem-check.md` (HWA-STM-001) with `docs/04-calcs/stem_check.py`, `stem_results.csv` (A1) and `stem_results_dropped.csv` (A2, A3), with the water checks of STANDARDS 25.6.
- Controlled documents: HWA-PRB-001, HWA-STM-001, HWA-PRC-001, HWA-OPT-001, HWA-URS-001, HWA-PRS-001, HWA-RTM-001 (generated), HWA-CAL-001 (`docs/04-calcs/01-sizing.md`, `sizing.py`, `sizing_results.json`), HWA-BLD-001 with pictures, HWA-DEC-001, HWA-DDR-001 to 003, HWA-REG-001, HWA-FEA-001, HWA-RSK-001 (PHA and design FMEA), HWA-MKT-001, HWA-PLN-001.
- CAD at D3 for all three options: `cad/src/model.py` with `cad/src/straw_parts.py`; `cad/fidelity.json` passes (A1 26 parts, A2 25, A3 20; bare share 0 %; one fastener each, the lanyard split ring). STEP per part in `cad/step/A1/` and an assembly STEP per option (about 12 MB in total). STL in `cad/stl/`.
- Drawings: HWA-DWG-001 (general arrangement), HWA-DWG-002 (half section), HWA-DWG-101 to 108 (making sketches), HWA-DWG-010 (concept blueprint, `media/concept-blueprint.*`).
- Concept media: `media/hero.png` (with an adult hand), `cutaway.png`, `exploded.png` (BOM numbers), `flow.png`, `model.glb` and `viewer.html`.
- Build plan pictures: `docs/05-build-plan/overview.png`, `joint-01` to `04`, `step-01` to `08`.
- `bom/bom.csv`: 17 lines, every one priced (estimates, with sources where listed).
- `README.md` with every Design Molecule section plus "Claims and limits" and "Helpful Engineering".
- Blender scenes exported for Amish's Mac: `/home/claude/hw/renderq/A-straw/` (options: `A-straw__options_jobs.json`, `opt-A1/A2/A3.npz`; product views: `views/A-straw__jobs.json` with hero, studio, cutaway and exploded).

### Key results (HWA-CAL-001)

| Quantity | Result |
| --- | --- |
| Flow at 10 kPa, clean, 20 C | 122 mL/min (0.1 um fibre) to 197 mL/min (0.2 um) |
| Child at 5 kPa / elderly at 7 kPa | 50 to 82 / 79 to 128 mL/min; a third less at 5 C |
| Suction for 400 mL/min | 19 to 30 kPa (not reachable at a comfortable sip) |
| Pressure budget at 200 mL/min (0.2 um) | Membrane 6.4, lift 1.5, pad 0.9 (assumed), carbon 0.7, lumens 0.5, rest under 0.1 kPa |
| Membrane | About 220 fibres, 0.056 m2 (Rev A: 0.011 to 0.022 m2) |
| Carbon | 4.0 mL, 1.9 to 2.0 g, 1.2 s contact at 200 mL/min |
| Seals | AS568-018 in 19.3 mm glands: squeeze 24 %, stretch 2.8 %, fill 77 % |
| Backflush | 846 mL/min at 50 kPa; 16 N thumb force |
| Size, mass | 205 mm x 26 mm (29.6 mm across the plug); 66 g |
| Cost | USD 17.46 prototype parts against the USD 25 target (USD 7.54 under); USD 0.011 a litre prototype, about 0.002 at scale |

### Requirements not met or at risk

- PR-002 flow 200 mL/min at 10 kPa: **at risk** (122 with 0.1 um, 197 with 0.2 um).
- PR-003 child flow 80 mL/min at 5 kPa: **at risk** (50 to 82).
- The 400 mL/min user threshold is **not met** by any arrangement in this envelope; carried as a known shortfall (D3).
- PR-012 air-hold check: at risk until the supplier's reverse-pressure rating is known.
- PR-017 regrowth, PR-023 mouthpiece per person: at risk.
- Every pathogen, materials, integrity and taste requirement is "to verify at TRL 4".

### STEM check

A1: 26 rows; 18 within known science (4 closed by fixes F1 to F4; F5 closes S14), 7 plausible and open for TRL 4 evidence (S2, S6, S15, S19, S20, S22, S23), 1 "Fails, fix proposed" (closed by Amish\'s decisions of 2026-11-11) (S3, membrane grade against the flow target). A2 and A3: Fails, dropped. `stem_check: open`. The independent reviewer pass was not run in this first session; it was run later the same day (see the second session above).

### Decisions proposed at the time (all settled by Amish on 2026-11-11; see the top section) (HWA-DEC-001)

D1 concept (A1); D2 membrane grade 0.1 or 0.2 um (safety trade-off); D3 flow target and a possible 245 mm body; D4 user air-hold check; D5 supplied syringe; D6 carbon and mouthpiece as one replaceable top; D7 a no-carbon variant; D8 mesh aperture; D9 no mouthpiece valve. Fixes F1 to F5 were made under the standing instruction of 2026-10-23 and can be reversed.

### Build plan findings (design for construction, HWA-DDR-002)

Internal quarter-turn bayonets instead of threads; a seat ring for the module; mesh captive in the intake cap; header held open by three cartridge legs; shortened luer-slip socket and tethered plug to stay under 30 mm; a bore plug in the mouthpiece cap; a dip line at 110 mm; 150 um screen and fines pad as bought stock.

### Safety concerns

Silent fibre damage (FMEA RPN 60), carbon biofilm (RPN 60), users assuming virus or chemical protection, clean-side contamination during a carbon change, a shared mouthpiece. Prototypes are never drunk from.

### Appearance model

`cad/src/product_model.py` uses every part of `components("A1")` unchanged and adds only the hand and a half-cut copy for the cutaway render; no appearance deviation to propose.

### Checks that do not pass, and kit notes

- `python .kit/render.py --check` fails only on `media/options.png`, which needs Blender (scenes exported; compose with `python .kit/options.py --compose=<dir>` after rendering). It warns about storefront items (`media/render-hero.png`, `card.png`, `social-preview.png`, which need Blender renders, and `.github` issue templates and `CITATION.cff`, which sit at the program root).
- `python .kit/trace.py --check`: passes, 0 gaps. The kit gap reported here (trace.py licence and licence line) was fixed in the kit (kit 1.9.1-he trace.py) on 2026-11-11 and the workaround script removed.
- The README links to the program README `../../README.md`, which does not exist yet at the program root.
- Renders still needed on Blender: `media/options.png`, `media/render-hero.png` (and the other product views), then `python .kit/cards.py .` for `card.png` and `social-preview.png`.

### Recommended next step

Amish reviews D1 to D3. Then: run the independent STEM review, render the Blender media, and send the module drawing (BOM 5) to straw-core makers for quotes. The design looks ready for TRL 4 prototypes of both membrane grades once P4 is opened.
