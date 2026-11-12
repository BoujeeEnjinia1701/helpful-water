---
doc_id: HWC-PLN-001
title: "Helpful Water C: household gravity filter project plan"
project: "Helpful Water C: household gravity filter"
doc_type: Project plan
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "First plan for solution C at P3, carrying the kill criteria and the parts of HWP-PLN-001 that apply"
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: Decisions recorded as Amish's (all pending decisions settled on their recommendations, 2026-11-11)

---

# Helpful Water C: household gravity filter project plan

Purpose: give households a way to treat a day's drinking and cooking water for five people, without power, in a few hours, and keep it closed, as the household member of the Helpful Water family (HWP-PLN-001). Solution C is at TRL 3 and stage P3 (the portfolio cap): a constructable design on paper with a build plan. Amish decided the concept (C1) and D2 to D8 on 2026-11-11 (HWC-DEC-001); no decision is open. P4 (prototype and accredited testing) stays closed until Amish opens it with Helpful Engineering.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## Kill criteria

Carried from HWP-PLN-001 and applied to C: stop or pause if C cannot show consistent bacteria and protozoa reduction under realistic household conditions; if flow becomes unusable for the 45 L day or is not recovered by backflush; if seal or membrane integrity cannot be kept in household handling (knocks, freezing, repeated hose and cap handling); if cost per litre or complexity is not viable at humanitarian scale; or if partners decline for safety, liability or usability reasons.

## Workstreams

Table 1. Workstreams.

| Workstream | Owner (role) | Deliverable | Status |
| --- | --- | --- | --- |
| Problem, users, requirements | Program lead | HWC-PRB-001, HWC-URS-001, HWC-PRS-001, HWC-RTM-001 | Drafted |
| STEM check and options | Design lead | HWC-STM-001 (with independent review), HWC-OPT-001 | Drafted; stem_check open |
| CAD, drawings, BOM | Mechanical and design-for-manufacture engineer | `cad/`, HWC-DWG-001, 002, 101 to 113, `bom/bom.csv` | D3 passed |
| Build plan and decisions | Mechanical engineer | HWC-BLD-001, HWC-DEC-001, DDR-001 to 003 | Drafted |
| Regulatory, risk, market | Regulatory specialist | HWC-REG-001, HWC-RSK-001, HWC-MKT-001 | Drafted |
| D interface | Water chemist with the D team | Dosing port, dose and contact time in the raw bucket | Open (HWC-DEC-001 D7) |
| Module supply | Membrane engineer | Quotations with flux at 5 kPa, backwash, burst, chlorine, LRV, NSF/ANSI/CAN 61 | Not started (P4 preparation) |
| Photoreal renders and options picture | Amish (Mac with Blender) | `media/options.png`, product renders | Scenes exported to the render queue |

## Targets and key performance indicators

Table 2. Targets that apply to C (from HWP-PLN-001 Table 2: set by Amish on 2026-11-11).

| Category | Target for C | Basis |
| --- | --- | --- |
| Bacteria and protozoa | At least 3 log as a first gate, toward the WHO three-star 4 log | HWP-PLN-001; HWP-CLM-001 Table 2 |
| Daily volume | 45 L in no more than 3 h of filtering, module due for backflush | Sphere; HWC-PRS-001 PR-005 |
| Durability | At least 90 days of daily use before the first lab life test ends | HWP-PLN-001 |
| Backflush recovery | At least 80 % of flow after 3 backflushes | HWP-VER-001 TE |
| User testing | 90 % follow the fill, settle, dose and filter sequence unassisted | HWP-PLN-001 |
| Cost | Report against USD 60; USD 10 per person per year or less | Value-engineering target; HWP-MKT-001 |

KPIs follow HWP-PLN-001 Table 3; for C the adoption KPI also records whether the clean bucket lid stays on and whether water is drawn only by the tap.

## Minimum viable team for C

Mechanical and design-for-manufacture engineer (stand, fittings, prints); membrane and water filtration engineer (module selection, flux, backflush); water microbiologist with an accredited laboratory (household-unit protocol, WHO scheme testing); water chemist (D interface, residual in storage); WASH specialist (source classes, household use); human-factors lead (filling, tap, pictograms); NGO liaison and field tester. Specialists may be part time (HWP-PLN-001 Table 4).

## Support needed from Helpful Engineering and partners

- A household field partner to review the requirements and the 45 L design day.
- An accredited laboratory for the household protocol (HWP-VER-001 TA, TB, TE).
- Introductions to membrane module makers that supply gravity modules with data sheets.
- The solution D team, to agree the dosing interface.

## Resources needed

Table 3. Resources (P4 onwards; on hold).

| Resource | Deliverable | Effort | Estimated cost (USD) |
| --- | --- | --- | --- |
| Prototype parts | Two C1 prototypes | From the BOM | About 175 (2 x USD 86.40) |
| Module samples | Three suppliers' modules for flux mapping | Weeks | To assess |
| Accredited testing | Household-unit challenge and life tests | Months | Share of the program's 50,000 to 150,000 |
| Human-factors trials | Persona trials with known potable test water only | Weeks | To assess |

## Stage gates

Table 4. Stages for C.

| Stage | Gate criteria | Status |
| --- | --- | --- |
| P0 to P2 | Problem, STEM check, options, requirements, calculations, traceability | Done on paper |
| P3 | Constructable model (D3), drawings, priced BOM, build plan, decisions register, design FMEA | Reached (this release) |
| P4 | Prototypes; flux map (TC); fouling and backflush (TE); structural and bypass (TF); materials (TG); human factors (TH); accredited pathogen tests (TA, TB) | On hold (stage cap) |
| P5 | Field trial with a partner, with D where viruses are a risk | On hold |
| P6 | Release and certification | On hold |

## 60 to 90 day plan once P4 opens

Table 5. Gated plan (from HWP-PLN-001 Table 7, for C).

| Window | Outputs and decision |
| --- | --- |
| Days 0 to 15 | Confirm the design day and sources with the partner; module quotations; D interface agreed |
| Days 16 to 35 | Build two prototypes to HWC-BLD-001; first checks; flux and head map with known potable test water |
| Days 36 to 60 | Fouling at 1, 10, 50, 100 NTU; backflush recovery; air test with seeded defects; tip tests; begin accredited pathogen testing; persona trials |
| Days 61 to 90 | Review results and costs; update BOM, risk register and requirements; go, pivot or stop recommendation |

## References

- Program documents: HWP-PRB-001, HWP-SRC-001, HWP-URS-001, HWP-CLM-001, HWP-REG-001, HWP-MKT-001, HWP-PLN-001, HWP-VER-001, HWP-FTO-001.
- Sphere Project. "Water Supply Standard 1: Access and Water Quantity." https://sphereprototype.conted.ox.ac.uk/standards/watersupply/accessAndWaterQuantity.html (checked 2026-11-11).
- CAWST. "Sawyer PointONE Biological Filter" fact sheet. https://washplusblog.fhi360.org/drinkingwaterupdates/wp-content/uploads/2014/03/cawst-sawyer.pdf (checked 2026-11-11).
- CAWST. "Biosand Filter" fact sheet, 2009. https://sswm.info/sites/default/files/reference_attachments/CAWST%202009%20Biosand%20Filter%20Fact%20Sheet%20academic_1.pdf (checked 2026-11-11).
- Engineering for Change. "LifeStraw Family 2.0." https://www.engineeringforchange.org/solutions/product/lifestraw-family-2-0/ (checked 2026-11-11); "British Berkefeld Household Filter Kit." https://www.engineeringforchange.org/solutions/product/british-berkefeld-household-filter-kit/ (checked 2026-11-11).
- British Berkefeld. "SS Gravity Data Sheet." https://cdn.shopify.com/s/files/1/2522/0950/files/British_Berkefeld_SS_Gravity_-_Data_Sheet.pdf (checked 2026-11-11).
- California State Water Resources Control Board. "4-Log Virus Inactivation through Chlorine Disinfection." https://www.waterboards.ca.gov/drinking_water/programs/districts/docs/sonoma/120_4_log_virus_inactivation_through_cl2_disinfection.pdf (checked 2026-11-11).
- New Jersey Department of Health. "Hyperchlorination to Kill Crypto When Chlorine Stabilizer Is Not in the Water." https://nj.gov/health/ceohs/documents/phss/hyperchlorination-to-kill-crypto-when-chlorine-stabilizer-is-not-in-the-water.pdf (checked 2026-11-11).
- Lantagne, Daniele, et al. "Engineering Inputs to the CDC Safe Water System Program." National Academies Press, 2006. https://www.nationalacademies.org/read/11577/chapter/8 (checked 2026-11-11).
- LG Water Solutions. "QuantumFlux Pressurized UF Membrane: Design and Operating Parameters." https://www.lgwatersolutions.com/wp-content/uploads/2024/12/QuantumFlux_Pressurized-UF-Membrane_Design-and-Operating-Parameters_F-1.pdf (checked 2026-11-11).
- Colwell, Rita R., et al. "Reduction of Cholera in Bangladeshi Villages by Simple Filtration." *PNAS* 100, no. 3 (2003): 1051 to 1055. https://pmc.ncbi.nlm.nih.gov/articles/PMC298724 (checked 2026-11-11).
- ePackageSupply. "White 5 Gallon 90 Mil Food Grade Bucket." https://epackagesupply.com/products/white-5-gallon-90-mil-food-grade-bucket-with-plastic-handle-1-count (checked 2026-11-11).
- Arco. "3/4 in Plastic Drum Spigot." https://arconow.com/products/3-4-plastic-drum-spigot (checked 2026-11-11).
- Helpful Engineering internal source pack: Helpful Water update (2026-02-26), Rev A component specification (2026-10-14), concept validation questions with Ali Raza's review (2026), viability shortlist, open questions.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
