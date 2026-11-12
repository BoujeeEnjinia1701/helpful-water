---
doc_id: HWD-PRB-001
title: "Helpful Water D: chlorine co-treatment add-on problem statement"
project: "Helpful Water D: chlorine co-treatment add-on"
doc_type: Problem statement
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: First problem statement for solution D, citing HWP-PRB-001
---

# Helpful Water D: chlorine co-treatment add-on problem statement

The filters of solutions A to C are designed to reduce bacteria and protozoa, not viruses, so wherever viral disease is a risk they need a second barrier, and a chlorine tablet is the cheapest one in the world's humanitarian supply chains. People already have the tablets; what fails in practice is the dose (wrong tablet for the container, guessed amounts, under-dosing to avoid the taste), the wait (water drunk before the contact time is up, or the same 30 minutes used in cold water) and the order (chlorinate first, wait, then filter). Solution D is a small, tool-free add-on that gets those three right with the bottles and buckets the other solutions use. It follows Amish's decision of 2026-11-11, "No virus claim, co-treat": A to C carry no virus claim and D is the co-treatment that pairs with any of them, under the same claims rule (HWP-CLM-001). The program problem is set out in HWP-PRB-001 and is not repeated here.

> **Release limitation.** Nothing here is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The problem for solution D

- **Viruses pass the filters.** Hollow-fibre membranes of about 0.1 um do not reliably retain viruses of 0.02 to 0.3 um, so A, B and C each carry the no-virus warning (HWP-CLM-001). Hepatitis A, norovirus and rotavirus are common where faecal contamination is (concept validation questions, item 45).
- **Chlorine is the established co-treatment, with its own limits.** NaDCC tablets cost about USD 0.02 a litre (as listed), need at least 30 minutes of contact (longer when cold or alkaline) and do not inactivate *Cryptosporidium* ([Akvopedia, NaDCC](https://akvopedia.org/wiki/Chlorine_(NaDCC)), checked 2026-11-11). Chlorine and the filter therefore cover each other's gaps: chlorine for viruses, the filter for cysts.
- **Dose errors are the common failure.** Household tablets come in several sizes for 1, 5, 10 and 20 to 25 L, and emergency tablets carry about twice the chlorine of household ones ([IFRC, Chlorine Tablet Choice in Emergencies](https://wash.ifrc.org/wp-content/uploads/2025/06/Chlorine-Tablet-Choice-in-Emergencies.pdf), checked 2026-11-11). A 20 L tablet in a 1 L bottle gives about 40 mg/L, eight times the WHO guideline value of 5 mg/L (HWD-CAL-001 section 6). Users also dose below the recommendation (Akvopedia).
- **Taste drives under-use.** Median taste detection of free chlorine in a Dhaka study was 0.73 mg/L for NaDCC and the median acceptability limit 1.26 mg/L (Crider et al. 2018), below the residuals that household dosing leaves; the carbon stages of A to C are intended to remove that taste after the wait.
- **Turbid water needs more chlorine, very turbid water should not be chlorinated alone.** Water under 5 NTU is properly disinfected; 5 to 50 NTU needs settling and a double dose; above 50 NTU it should not be chlorinated (IFRC note above).

## Users and context

Table 1. Users and needs for solution D (personas from HWP-PRB-001 Table 1).

| User type | Goals and needs | Typical use scenario | Pain points and challenges |
| --- | --- | --- | --- |
| Household carer (infants and cooking) | Dose a 20 L raw-water bucket before it goes through C | Rural home, camp shelter | Which tablet, how long to wait, taste for children |
| Child (8 to 12) | Dose a 1 L bottle before using A or B, without help | School, home | Small foil strips, waiting 30 minutes |
| Elderly user | Low effort; acceptable taste | Home, camp | Arthritis on caps and strips; dislikes chlorine taste |
| User with limited dexterity | No small loose parts | Home | Picking up a 1 L tablet, turning caps |
| Crisis or disaster recipient | Correct dose at once with almost no training | Flood, displacement | Mixed tablet sizes in relief kits; cold water in winter |
| Humanitarian field worker or NGO distributor | Easy demonstration; predictable resupply | Distribution points | Training many people; tablets and liquid of different strengths |
| Immunocompromised user | Higher protection margin against viruses | High-HIV-prevalence regions | Higher stakes from viruses, *Cryptosporidium* and silent failure |
| High-turbidity user | Knows when water is too muddy to chlorinate | Monsoon, floods | Chlorine demand, shielding by particles |

### Stakeholders

Table 2. Stakeholders who are not day-to-day users (adds to HWP-PRB-001 Table 2).

| Stakeholder group | Role or interest | Engagement needed |
| --- | --- | --- |
| Solutions A, B and C teams | Interfaces: B's 28 mm bottle neck, A's straw in a cup, C's 20 L raw bucket and outlet | Agree the 28 mm port on C's raw-bucket lid and the closed outlet during the wait (HWD-DEC-001 D4) |
| Water chemist (HWP-PLN-001 Table 4) | Dose, residual, CT and by-products | Owns HWD-CAL-001 and the TJ test family (HWP-VER-001) |
| Chlorine tablet and hypochlorite suppliers | Tablet sizes, strip packs, shelf life, registration | Data sheets and tablet dimensions (HWD-DEC-001 C1) |
| Regulators for disinfectant products | Biocide or pesticide registration of chlorine products and their claims | Before any distribution (HWP-REG-001 W9) |
| NGO and WASH buyers | Already distribute NaDCC and hypochlorite | Confirm the tablet sizes in their kits and the resupply route |

## Constraints

- Co-treatment only: chlorinate the raw water, wait the full contact time, then filter with A, B or C (Amish, 2026-11-11: "No virus claim, co-treat"; HWP-CLM-001).
- Dose at the household rate used by WHO-referenced programmes (about 2 mg/L, double for settled turbid water), never above the WHO guideline value of 5 mg/L; a free residual of at least 0.5 mg/L after 30 minutes at pH under 8 (WHO GDWQ, via WEDC Mobile Note 7).
- Use the consumables already in humanitarian supply (NaDCC tablets, 1.25 % sodium hypochlorite), no proprietary refill.
- Zero power and zero tools; value-engineering target USD 10 of prototype parts.
- Open hardware under CERN-OHL-P-2.0, Apache-2.0 and CC-BY-4.0 (Helpful Engineering licensing guide).

## Out of scope

- Any claim against *Cryptosporidium* from chlorine, any "purifier" claim for D alone, and chlorination of water above 50 NTU or of flood and urban runoff (HWP-SRC-001 SC6).
- Chlorine dioxide and iodine, electrochlorination, and dosing of piped or community supplies.
- Removal of dissolved chemicals, salt or metals (the exclusions of HWP-CLM-001 apply).

## Kill criteria

From HWP-PRB-001 and HWP-PLN-001, applied to D: stop or pause if the dose cannot be held between the WHO-referenced household rate and the 5 mg/L guideline value in realistic use, if users cannot tell when the contact time is complete, if the consumable cannot be resupplied where the device is used, or if partners decline because of chemical safety, registration or liability concerns.

## Open questions

- Which tablet sizes do the first partner's relief kits carry, and are they household or emergency strength?
- What pH, temperature and turbidity do the first sources show (HWP-SRC-001, HWP-VER-001 TD)?
- Should the household dose be done in the 20 L bucket (cheapest per litre) or per bottle (simplest for one person)?
- Where in C should a protective residual survive, given that carbon removes it (HWD-DEC-001 D3)?

## User research and co-design

- [ ] Confirm the tablet sizes and liquid strengths in the partner's supply
- [ ] Persona trials of the dose cap with known potable test water and placebo tablets only (child, elderly, low dexterity)
- [ ] Comprehension test of the pictograms: dose, shake, wait, cold-water rule, then filter
- [ ] Revise the requirements from findings before freezing the design

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
