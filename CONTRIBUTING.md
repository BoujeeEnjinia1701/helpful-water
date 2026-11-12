# Contributing to Helpful Water

Thank you for helping. Helpful Water is open hardware, developed by Design Molecule Labs with Helpful Engineering.

## Licences

Contributions are licensed under the Helpful Engineering licensing guide (https://helpfulengineering.org/licensing-guide/):

- Hardware, CAD, drawings, BOM, build plans, firmware and test software: CERN-OHL-P-2.0 (`LICENSE-HARDWARE.txt`).
- Software not needed for the hardware to work: Apache-2.0 (`LICENSE-SOFTWARE.txt`).
- Documentation, guides, pictures and videos: CC-BY-4.0 (`LICENSE-DOCUMENTATION.txt`).

## Contributor warranty

By contributing you confirm that your employment contract (or any other agreement you are bound by) allows you to volunteer and to contribute to open hardware and software through Helpful Engineering, and that your contribution may be made freely available to everyone under the licences above.

## How the work is done

- Read `CLAUDE.md` and `.kit/STANDARDS.md` (section 25 for this joint profile).
- Program documents live in `docs/`; each lettered solution is a full kit project in `solutions/`. Run the kit tools from the solution folder: `cd solutions/A-straw && python .kit/render.py --check`.
- Follow the water claims rule (HWP-CLM-001): describe risk reduction, never safety, and state the exclusions.
- No prototype may be used to treat water for drinking until it has been validated by a qualified laboratory.
- Chicago Manual of Style; no em dashes; SI units.
