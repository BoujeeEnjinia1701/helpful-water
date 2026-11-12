# Review note: Helpful Water D, chlorine co-treatment add-on (TRL 1 to TRL 3, 2026-11-11)

## Session 2026-11-11 (decisions): every pending decision settled

Amish, 2026-11-11: "for any pending decisions go with a recommendation. Don't leave any pending decisions in the file for Amish to make at this time." Each pending decision in HWD-DEC-001 was settled on its recommendation and is recorded as his; no decision is open. Later sections of this note are kept as the record of what was proposed at the time.

- D1: D1 tablet dose cap with ball timer; D2's timer is offered as a clip where SWS liquid is distributed.
- D2: Closed (independent review run 2026-11-11).
- D3: (a) for A and B; (c) for C: C has no carbon stage (HWC-DEC-001 D3), so the residual protects its stored water.
- D4: A 28 mm port with the orange insert in C's lid and a closed outlet during the wait, with pour-through and a 30 s stir (F7). Dropping the tablet into the empty bucket before filling, with the cap kept as the timer, is printed on the label as the fallback method.
- D5: Household 20 L as the main route; 1 L for personal and field use.
- D6: Ball timer; the hand-set dial is the fall-back if the fall time cannot be held within 10 %.
- D7: (b) free chlorine test strips in the household kit; (c) a colour comparator for partners. The strip cost is to assess.

STEM rows S16 and S43 are closed by D3 and D7. The solution is renamed "chlorine co-treatment add-on" so its name makes no virus claim. `stem_check` stays `open` only because Plausible rows need TRL 4 evidence (laboratory tests, supplier data); no row fails. The options picture now shows the chosen option, and `docs/03b-traceability.md` was regenerated.

Recommended next step: create the program repo as public (Amish, 2026-11-11); TRL 4 (prototype and accredited testing under HWP-VER-001) opens only when Amish opens it with Helpful Engineering.

Solution D was taken from a scaffold (TRL 1, P0) to a constructable design on paper (TRL 3, P3) under kit 1.9.1-he, following the briefs for the Helpful Water program. No prototype exists; nothing was built or tested.

## What was done

- STEM check first: `docs/01b-stem-check.md` (HWD-STM-001), `docs/04-calcs/stem_check.py`, `stem_results.csv`, `stem_results_dropped.csv`, `stm_table.py`.
- Calculations: `docs/04-calcs/sizing.py`, `sizing_results.json`, `docs/04-calcs/01-sizing.md` (HWD-CAL-001): dose, residual model, CT, pH and temperature, ball timer, overdose and by-products, liquid decay, erosion feeder range, mass, cost per litre.
- Three concept options modelled to D3 and scored: `docs/02a-concept-options.md` (HWD-OPT-001), `cad/src/model.py`, `cad/src/hw_parts.py`.
- Documents: PRB, PRC, URS, PRS, RTM (generated), CAL, BLD, DEC, three DDRs, REG, FEA, RSK (PHA and design FMEA), MKT, PLN, README.
- CAD and media: `cad/fidelity.json` (PASS at D3, all options), `cad/step/` (D1 per-part STEP and three assembly STEPs, 6 MB in all), `cad/stl/`, `cad/drawings/HWD-DWG-001`, `002` (GA, section) and `101` to `107` (making sketches), `media/hero.png`, `concept-blueprint.png/.pdf`, `model.glb`, `viewer.html`, `cutaway.png`, `exploded.png`, `flow.png`, build plan pictures in `docs/05-build-plan/`.
- Blender queue: `python .kit/options.py --export=/home/claude/hw/renderq/D-virus-add-on` (three option scenes) and `python .kit/export_views.py /home/claude/hw/renderq/D-virus-add-on/views` (hero, studio, exploded).

## TRL 2 section: concept

- Options: D1 tablet dose cap with ball timer 174 of 215; D2 metered liquid doser 143; D3 erosion feeder 85 and dropped on the STEM check (a contact-time release gives a dose proportional to standing time: about 96 mg/L overnight if set for 2 mg/L at 30 minutes). D1 is 17.8 % ahead of D2, so one recommendation is made: D1, **decided by Amish on 2026-11-11**.
- STEM verdicts (D1 and D2), after the independent review: 22 Within known science, 19 Plausible, 2 Fails, fix proposed (S16 and S43, sent to Amish), 0 Fails, over 43 rows (S1 to S43). Dropped D3: 4 Fails. `stem_check: open`.
- Fixes under the standing instruction of 2026-10-23 (HWD-DDR-003): F1 turbid-water rule and a two-tablet well; F2 colour-keyed 1 L and 20 L inserts; F3 a plug stop that leaves room for two tablets, not three; F4 a cold-water run count on the timer; F5 an O-ring groove that had no squeeze; F6 a 34 minute timer nominal for tolerance.
- Independent second-agent STEM review: run on 2026-11-11 (see the section below); HWD-DEC-001 D2 is closed.

## TRL 3 section: results (estimates)

| Quantity | Result |
| --- | --- |
| Dose | 2.0 mg/L per matched tablet (1.6 in 25 L); 4.0 at two tablets for settled turbid water |
| Free chlorine, clear water | 1.7 mg/L at 30 min, 0.75 mg/L at 24 h (assumed demand and decay) |
| CT in 30 min | 51 mg min/L (US EPA definition) against 8 (4-log virus, 5 C) and 12 (0.5 C); 1.1 times Giardia; 0.003 of *Cryptosporidium*; no virus credit above 5 NTU |
| Ball timer | 2 mm ball, 13 mm fall, about 548,000 cSt fluid (Haberman-Sayre), 45 min nominal at 25 C, 30.3 min at 40 C and -10 % viscosity; runs one, two, three by water temperature |
| Size, mass, parts | 52 x 41 x 52 mm, about 45 g, 21 parts |
| BOM | USD 9.15 against the USD 10 value-engineering target (USD 5.95 cap, USD 3.20 test tablets) |
| Cost per litre over two years | USD 0.0006 (20 L tablets, household) to USD 0.012 (1 L tablets, personal); scale cap about USD 1.40 |
| Persona efforts | No flow; plug 3.5 turns; up to three timer flips; pour and 30 s stir on the bucket; D2 squeeze about 10 N against a weak child's 124 N grip |
| D2 dropper | 2.0 mm orifice, five drops per litre, 1.7 to 2.1 mg/L (Tate's law) |

### Requirements not met or at risk (HWD-PRS-001)

- PR-013 order and residual: **at risk**. Carbon in A to C removes the chlorine, so no protective residual reaches stored filtered water (HWD-DEC-001 D3).
- PR-014 C bucket interface: **at risk**. Needs C's lid port and a closed outlet during the wait (D4).
- To verify at TRL 4: PR-008 timer run, PR-016 pictograms, PR-017 materials, PR-021 storage, PR-022 taste after the filter.

### Build plan findings (HWD-DDR-002)

Timer pivot changed from a through pin (it would block the ball) to moulded trunnions; capsule shortened so it can turn in its slot; crown cored; insert floor hollowed; timer kept outside the water space behind a screwed window.

## Independent STEM review (2026-11-11)

- Method: `claude -p` run as a separate process in its own folder with only the claims tables, `stem_check.py`, `sizing.py`, `sizing_results.json`, the PARAMS block and the sources; asked to refute every Within and Plausible verdict and to look for missed water checks. Output kept outside the repo; findings recorded in HWD-STM-001 Table 4.
- Counts over 43 rows: 20 hold, 18 weak, 5 refuted (S20, S23, S25, S36, X4). Every finding was recomputed before acting; one suggested correction (a 17.6 mm groove root) went the wrong way and was not used.
- Fixes under the standing instruction (HWD-DDR-004): F7 pour-through and stir on the 20 L bucket; F8 bottle range 1 to 1.5 L on the label; F9 D2 orifice 2.0 mm, five drops; F10 groove root 17.9 mm with tolerances (15 to 28 % squeeze); F11 timer nominal 45 min, at least 30 min up to 40 C, run count one, two, three; F12 no PC in the well plug. Calculation corrections: EPA CT definition, Morris pKa, Haberman-Sayre wall factor; six rows moved to Plausible.
- Files changed: `cad/src/model.py`, `docs/04-calcs/sizing.py`, `stem_check.py`, `stem_results*.csv`, `sizing_results.json`, `bom/bom.csv` (specs only, total unchanged at USD 9.15), `docs/01b-stem-check.md`, `01-sizing.md`, `02-concept.md`, `02a-concept-options.md`, `03-requirements.md`, `05-build-plan.md`, `06-design-decisions.md`, `09-risk.md`, `decisions/0003-stem-fixes.md`, new `decisions/0004-independent-review-fixes.md`, README; regenerated `cad/fidelity.json`, STEP and STL, HWD-DWG-001, 002, 101 to 103, `media/cutaway.png`, `flow.png`, `concept-blueprint`, `model.glb`, and the traceability matrix.

## Decisions proposed at the time (all settled by Amish on 2026-11-11; see the top section) (HWD-DEC-001)

D1 concept (recommend D1); D3 residual after the filter (recommend accepting no residual for A and B, and asking C to drop or move its carbon since C stores water); D4 C interface (28 mm port and closed outlet; the review showed the bucket needs a pour-and-stir step, and dropping the tablet into the empty bucket before filling is the simpler alternative to weigh); D5 main route (household 20 L tablets are about twenty times cheaper per litre than 1 L tablets); D6 timer type (ball timer, dial as fall-back); D7 field check of the residual (new: free chlorine test strips in the household kit, cost to assess; recommended, since a wrong, weak or missing dose is otherwise silent).

## Safety concerns

- The largest hazards are behavioural: drinking before the wait or without the filter (*Cryptosporidium*), and over-trust in D. Controls are the timer, the clear plug, the pictograms and the HWP-CLM-001 wording; only TH trials can confirm them.
- Tablet keying rests on assumed tablet sizes until the partner's tablets are measured (C1), and works one way only: a 1 L tablet in the 20 L well gives 0.1 mg/L, and a 20 L tablet dropped straight into an open bottle gives 40 mg/L.
- The sealed timer fluid changes volume by 3.4 % over -10 to 60 C; the expansion allowance is open (C5).
- Tablets are a chemical: child access, swallowing and mixing with acids or other products are on the label and in HWD-RSK-001.

## Checks

- `python .kit/cad_check.py --export`: PASS at D3 (D1 21 parts, D2 24, D3 21; no interference outside the listed seal and fluid contacts).
- `python .kit/trace.py`: matrix written, 0 gaps.
- `python .kit/render.py --check`: every controlled document passes (front matter, licence lines, claims rule, no em dashes). It fails only on `media/options.png`, which needs Blender (rendered on Amish's Mac from the render queue). Storefront warnings (render-hero, card, social preview, issue templates, CITATION.cff) are Blender or release items outside this brief.
- Media needing Blender: `media/options.png` (compose with `python .kit/options.py --compose=<dir>` after rendering), `media/render-hero.png` and the studio and exploded renders, then `python .kit/cards.py .`.

## Notes for Amish

- The C team designs the raw bucket in parallel; D proposes a 28 mm PCO 1881 port in its lid so the same cap and an orange insert dose 20 L, and asks that C's outlet stays closed during the wait.
- The program sequence (chlorinate, wait, filter, carbon removes the taste) is sound for viruses and taste, but it removes the residual that the CDC Safe Water System relies on to protect stored water. This matters most for C.

## Recommended next step

(D1, D4 and D7 were decided on 2026-11-11.) Measure the partner's tablets. After that the design looks ready for a TRL 4 bench build with known potable test water; that is a recommendation only, and P4 stays closed until Amish opens it.
