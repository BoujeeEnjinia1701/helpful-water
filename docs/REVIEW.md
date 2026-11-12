# Helpful Water review notes

## Session 2026-11-11: program repo created and four solutions taken to TRL 3 (kit 1.9.1-he)

Amish, 2026-11-11: "open up a new repo on the Design Molecule Github called Helpful Water. Do not apply for Zoho and DOI notation. But apply everything else in the kit. Perhaps first provide an alternate kit approach. This one should focus on projects that will be a joint effort between Design Molecule and Helpful Engineering. Follow the licensing guidelines as per Helpful Engineering." Answers the same day: solutions A, B and C plus a D virus add-on; one repo with solution folders; "No virus claim, co-treat"; credits Amish Chadha, Ali Raza, Suraksha Bhat, Lillian Fernandes, Raksha Thammaiah and James Butler. Later: "make sure we are covering everything Design Molecule covers plus the additional as per the Helpful Engineering documentation."

### What was done

- Kit 1.9.1-he (`.kit/`, STANDARDS section 25, CLAUDE.md section 8): Helpful Engineering licences (CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0) with root `.txt` licence files and a licence line enforced at the foot of every controlled document; archiving and DOI off (`archive: false`); joint brand line on PDFs, title blocks and cards; program repos with lettered solutions; water claims rule enforced by `render.py --check`; water STEM checks; new document types CLM, VER, FTO, SRC, PGM; release gate and storefront checks that find licence, CITATION and issue files at the repository top; `trace.py` writes the documentation licence and licence line.
- Program documents (`docs/`): HWP-PRB-001, HWP-SRC-001, HWP-URS-001 (UR-001 to UR-022 and personas), HWP-REG-001, HWP-MKT-001, HWP-PLN-001 (kill criteria, targets and KPIs, minimum team, 60 to 90 day plan, support needed), HWP-CLM-001 v0.2, HWP-VER-001 (families TA to TJ), HWP-FTO-001 (US 8,852,439 B2).
- Solutions A to D (`solutions/`), each a full kit project at stage P3, TRL 3, design constructable: STEM check with an independent reviewer (separate process) and fixes under the standing instruction; two or three options at CAD D3; URS, PRS and generated RTM; sizing; priced BOM; drawings; build plan with pictures; DEC and DDRs; REG, FEA, RSK with FMEA, MKT, PLN; concept media; solution README with every Design Molecule section plus "Claims and limits" and "Helpful Engineering".
- Root files: README, project.yaml (program), CITATION.cff, CONTRIBUTORS.md, CONTRIBUTING.md (Helpful Engineering contributor warranty), REUSE.toml, licence files, workflows (document check per solution), issue templates.

### Key results

| Solution | Options (score) | Recommendation | BOM against target | Not met or at risk |
| --- | --- | --- | --- | --- |
| A filter straw | A1 164, A2 135, A3 125 of 215 | A1, awaiting Amish | USD 17.46 against 25 | PR-002 and PR-003 not met on paper (110 to 179 mL/min at 10 kPa against 200); 400 mL/min unreachable in the envelope; integrity check and carbon regrowth at risk |
| B bottle cartridge | B1 246, B2 222, B3 209 of 310 | B1 or B2 (within 10 %), no pick | USD 18.35 against 20 | PR-014 width (46 mm against 30 mm) not met; cost per user per year over at 9 months; fouled flow and backflush pressure at risk |
| C household gravity | C1 286, C2 234, C3 227 of 345 | C1, awaiting Amish | USD 86.40 against 60 (over) | Cost over; chlorine taste (no carbon) and 1.27 m fill rim at risk; all flows rest on an assumed membrane permeability |
| D chlorine add-on | D1 174, D2 143, D3 85 of 215 | D1, awaiting Amish | USD 9.15 against 10 | No residual after carbon in A to C (PR-013); C interface not agreed (PR-014) |

### Proposed, awaiting Amish

- Concept choice in each solution (A1, B1 or B2, C1, D1).
- A: membrane grade (0.1 or 0.2 um, a safety trade-off), the flow target and a 245 mm body, air in the shell, backflush pressure limit, open socket under water, and the other items in HWA-DEC-001.
- B: neck finish, wide-mouth adapter, a 50 mm width target, end wall thickness, rating temperature and the others in HWB-DEC-001.
- C: membrane grade with a 0.02 um quote, no carbon stage, wall strap, colour coding, dosing interface with D, tally card (HWC-DEC-001).
- D: residual after carbon (accept for A and B; for C, which stores water, keep C carbon-free), the port in C's lid, household or bottle dosing as the main route, the ball timer, free chlorine test strips (HWD-DEC-001).
- Program: the value-engineering targets in each solution and the program targets in HWP-PLN-001 Table 2; a "Helpful Copyleft Licence" when Helpful Engineering releases it.

### Safety concerns

- No prototype may be used for drinking water before accredited testing (release limitation in every document).
- Silent membrane failure after freezing or a drop; open backflush socket under water (A); chlorine dosing errors and tablets near children (D).

### Final checks (2026-11-11)

- Blender Cycles renders are done on the Mac: 13 options panels and 12 product views, captioned into each solution's `media/`, plus `media/card.png` and `media/social-preview.png` per solution and `media/program-hero.png` at the root. `image_qc.py` passes in every solution (21 images, 0 problems).
- `render.py --check` passes at the root and in all four solutions; `reuse lint` passes (940 of 940 files).
- `release_gate.py` now has a program mode (STANDARDS section 25.4): at the root it runs each solution's gate and checks the program hero. It fails, as intended, on one item per solution: `stem_check: open`, because STEM findings and fixes in each solution await Amish's decision. This is not a release, and nothing is public.

### Recommended next step

Amish decides the concepts; then the repo is created private under BoujeeEnjinia1701. TRL 4 (prototypes and accredited laboratory testing, HWP-VER-001) stays closed until Amish opens it with Helpful Engineering.
