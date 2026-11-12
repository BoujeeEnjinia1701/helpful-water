# Helpful Water review notes

## Session 2026-11-11: program repo created and four solutions taken to TRL 3 (kit 1.9.1-he)

Amish, 2026-11-11: "open up a new repo on the Design Molecule Github called Helpful Water. Do not apply for Zoho and DOI notation. But apply everything else in the kit. Perhaps first provide an alternate kit approach. This one should focus on projects that will be a joint effort between Design Molecule and Helpful Engineering. Follow the licensing guidelines as per Helpful Engineering." Answers the same day: solutions A, B and C plus a D virus add-on; one repo with solution folders; "No virus claim, co-treat"; credits Amish Chadha, Ali Raza, Suraksha Bhat, Lillian Fernandes, Raksha Thammaiah and James Butler. Later: "make sure we are covering everything Design Molecule covers plus the additional as per the Helpful Engineering documentation."

### What was done

- Kit 1.9.1-he (`.kit/`, STANDARDS section 25, CLAUDE.md section 8): Helpful Engineering licences (CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0) with root `.txt` licence files and a licence line enforced at the foot of every controlled document; archiving and DOI off (`archive: false`); joint brand line on PDFs, title blocks and cards; program repos with lettered solutions; water claims rule enforced by `render.py --check`; water STEM checks; new document types CLM, VER, FTO, SRC, PGM; release gate and storefront checks that find licence, CITATION and issue files at the repository top; `trace.py` writes the documentation licence and licence line.
- Program documents (`docs/`): HWP-PRB-001, HWP-SRC-001, HWP-URS-001 (UR-001 to UR-022 and personas), HWP-REG-001, HWP-MKT-001, HWP-PLN-001 (kill criteria, targets and KPIs, minimum team, 60 to 90 day plan, support needed), HWP-CLM-001 v0.2, HWP-VER-001 (families TA to TJ), HWP-FTO-001 (US 8,852,439 B2).
- Solutions A to D (`solutions/`), each a full kit project at stage P3, TRL 3, design constructable: STEM check with an independent reviewer (separate process) and fixes under the standing instruction; two or three options at CAD D3; URS, PRS and generated RTM; sizing; priced BOM; drawings; build plan with pictures; DEC and DDRs; REG, FEA, RSK with FMEA, MKT, PLN; concept media; solution README with every Design Molecule section plus "Claims and limits" and "Helpful Engineering".
- Root files: README, project.yaml (program), CITATION.cff, CONTRIBUTORS.md, CONTRIBUTING.md (Helpful Engineering contributor warranty), REUSE.toml, licence files, workflows (document check per solution), issue templates.

### Key results

| Solution | Options (score) | Decision (Amish, 2026-11-11) | BOM against target | Not met or at risk |
| --- | --- | --- | --- | --- |
| A filter straw | A1 164, A2 135, A3 125 of 215 | A1 | USD 17.46 against 25 | PR-002 (150 mL/min at 10 kPa) met on paper with the 0.2 um grade (179), not with 0.1 um (110); PR-003 child flow not met on paper (45 to 74 against 80); integrity check and carbon regrowth at risk |
| B bottle cartridge | B1 246, B2 222, B3 209 of 310 | B1 (B2 within 10 %; its stand is a possible later accessory) | USD 18.35 against 20 | PR-014 met at the B-specific 50 mm width; cost per user per year over at 9 months; fouled flow and backflush pressure at risk |
| C household gravity | C1 286, C2 234, C3 227 of 345 | C1 | USD 86.40 against 60 (over) | Cost over; chlorine taste (no carbon) and 1.27 m fill rim at risk; all flows rest on an assumed membrane permeability |
| D chlorine co-treatment add-on | D1 174, D2 143, D3 85 of 215 | D1 | USD 9.15 against 10 | Residual kept only in C (carbon-free); A and B claim none; strip cost to assess |

### Decisions made by Amish on 2026-11-11

Amish, 2026-11-11: "for any pending decisions go with a recommendation. Don't leave any pending decisions in the file for Amish to make at this time." Every pending decision was settled on its recommendation and is recorded as his in each register; no decision is open. Where a recommendation offered a fork, the branch that keeps the current CAD, BOM and build plan valid was taken.

- Concepts: A1, B1, C1, D1. For B, B1 and B2 were within 10 %; B1 was taken as the higher score and the design already carried to the drawings.
- A (HWA-DEC-001): both membrane grades prototyped in the same housing and selected on laboratory log reductions with an absolute rating; PR-002 set to 150 mL/min at 10 kPa as an upper bound, with the 245 mm body held as the TRL 4 revision; plunger-hold air check (conditional on the supplier reverse rating); supplied syringe; carbon and no-carbon variants from one housing; 250 um mesh; no mouthpiece valve; backflush relief valve if the module's reverse rating is under 200 kPa; tethered socket plug for the prototype.
- B (HWB-DEC-001): PCO 1881 neck; no 38 mm adapter until the neck survey shows it is needed; B-specific 50 mm width (PR-014 met); squeeze-filter patent desk search before P4 and an attorney opinion before distribution; cost per user per year reported at 9 and 12 months; end wall thickened at the next geometry revision; flows rated at 20 C with 10 C figures beside them.
- C (HWC-DEC-001): 0.1 um module with D (quotes for both classes); no carbon stage; wall strap; 900 mm top shelf; blue and white colour coding; D's 28 mm lid port; tick card.
- D (HWD-DEC-001): residual accepted as none for A and B, kept in C by C staying carbon-free; 28 mm lid port with the orange insert, with drop-in-before-filling printed as the fallback; household 20 L as the main route; ball timer; free chlorine test strips in the household kit and a comparator for partners. The solution title is now "chlorine co-treatment add-on", so the name makes no virus claim.
- Program: the value-engineering targets in each solution and the service-level targets in HWP-PLN-001 Table 2 adopted as working targets; licences stay CERN-OHL-P-2.0, Apache-2.0 and CC-BY-4.0, with no switch to a "Helpful Copyleft Licence".

### Safety concerns

- No prototype may be used for drinking water before accredited testing (release limitation in every document).
- Silent membrane failure after freezing or a drop; open backflush socket under water (A); chlorine dosing errors and tablets near children (D).

### Final checks (2026-11-11)

- Blender Cycles renders are done on the Mac: 13 options panels and 12 product views, captioned into each solution's `media/`, plus `media/card.png` and `media/social-preview.png` per solution and `media/program-hero.png` at the root. `image_qc.py` passes in every solution (21 images, 0 problems).
- `render.py --check` passes at the root and in all four solutions; `reuse lint` passes (940 of 940 files).
- `release_gate.py` now has a program mode (STANDARDS section 25.4): at the root it runs each solution's gate and checks the program hero. It fails on one item per solution, `stem_check: open`, which the kit sets while any Plausible row still needs TRL 4 evidence (laboratory tests, supplier data). No decision is open and no STEM row fails. Amish authorised a public repo on 2026-11-11; no release is tagged.

### Recommended next step

Amish, 2026-11-11: "you can make the repo public". `create_helpful_water.sh` creates BoujeeEnjinia1701/helpful-water as a public repo. The release gate passes except `stem_check: open` in each solution, which stays open until TRL 4 laboratory and supplier evidence closes the Plausible rows; the release limitation and claims rule in every document cover this. TRL 4 (prototypes and accredited laboratory testing, HWP-VER-001) stays closed until Amish opens it with Helpful Engineering.
