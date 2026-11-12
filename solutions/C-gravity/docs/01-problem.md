---
doc_id: HWC-PRB-001
title: "Helpful Water C: household gravity filter problem statement"
project: "Helpful Water C: household gravity filter"
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
    change: "First problem statement for solution C, from HWP-PRB-001 and the Helpful Water source pack (kit 1.9.1-he)"
---

# Helpful Water C: household gravity filter problem statement

A household that treats its water one sip at a time cannot cook with it, store it or give it to an infant, and diarrhoeal deaths concentrate in children under five, so the program needs a household unit as well as a personal one (Ali Raza, concept validation review, 2026; HWP-PRB-001). Solution C is that unit: an unpowered gravity filter, built from containers families already know, that treats a day's drinking and cooking water for five people in a few hours and keeps it in a closed container with a tap. It is designed to reduce bacteria and protozoa; it does not remove viruses, so it is paired with chlorine (solution D) where viral disease is a risk.

> **Release limitation.** No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The problem for households

- **The program problem.** 2.1 billion people lack safely managed drinking water and microbiologically contaminated water causes about 505,000 diarrhoeal deaths a year (WHO and UNICEF, 2025, and the WHO fact sheet, both cited in HWP-PRB-001).
- **The straw gap.** A straw protects only the person drinking from it; it serves no cooking, no stored supply and no infant feed (HWP-PRB-001, "Why several solutions").
- **Household volume.** The Sphere Handbook puts survival water intake at 2.5 to 3 L and basic cooking at 3 to 6 L per person per day ([Sphere Project, water supply standard 1](https://sphereprototype.conted.ox.ac.uk/standards/watersupply/accessAndWaterQuantity.html), checked 2026-11-11). A household of five therefore needs 27.5 to 45 L a day; C is sized for the upper figure, 45 L (HWC-CAL-001).
- **Recontamination in storage.** In camps and homes, water from a good source is recontaminated in handling and storage (HWP-SRC-001 SC5; HWP-URS-001 use case 3). A filter that delivers into an open pot loses much of its value.
- **Turbid water.** Monsoon and river water of 10 to 100 NTU (SC3) clogs filters fast; the unit needs a settling or prefilter step.
- **Chlorine and cysts.** Chlorine tablets cost about USD 0.02 a litre and address viruses and bacteria but do not inactivate *Cryptosporidium* (HWP-PRB-001); a membrane after chlorination covers that gap, and the chlorine residual can protect the stored water.

## Users and context

Table 1. Users and needs for solution C (from HWP-PRB-001 Table 1; the household rows lead).

| User type | Goals and needs | Typical use scenario | Pain points and challenges |
| --- | --- | --- | --- |
| Household carer (infants and cooking) | Treated water for the whole household, including cooking and infant feeds | Rural home, camp shelter | Lifting and pouring 5 to 20 L; time; knowing the filter still works |
| Child (8 to 12) | Draw a cup without help | Home, school | Cannot lift a bucket; should only open a tap |
| Elderly user | Low effort; acceptable taste | Home | Weak grip; reaching a high rim; chlorine taste |
| User with limited dexterity | Use and clean without small parts or tools | Home | Hose clamps, caps, syringe steps |
| Crisis or disaster recipient | Treated water at once with almost no training | Flood, displacement | No time to ripen a biological filter; no tools |
| High-turbidity user | Usable flow from muddy river water | Monsoon, floods | Fast clogging; settling takes time |
| Immunocompromised user | Higher protection margin | High-HIV-prevalence regions | Viruses and *Cryptosporidium*; silent failure |
| Clinic or camp water point (secondary) | Several households from one unit | Clinic, school | Volume; shared handling |

### Stakeholders

Table 2. Stakeholders who are not day-to-day users (from HWP-PRB-001 Table 2, with what C needs from each).

| Stakeholder group | Role or interest | Engagement needed for C |
| --- | --- | --- |
| Helpful Engineering (Helpful Water team) | Co-owner; volunteer engineers and testers | Design review of C; field partner introduction |
| Design Molecule Labs | Co-owner; kit, CAD, documents | Runs C to TRL 3 |
| NGO and WASH cluster buyers | Procurement, distribution, training | Cost per litre, resupply of the module, comparison with ceramic pots, biosand and tablets |
| Solution D team (chlorine add-on) | Co-treatment for viruses | Agree the dosing port, dose and contact time in the raw bucket |
| Accredited water microbiology laboratory | Challenge testing | Household-unit protocol, including WHO scheme testing at the stated flow |
| Membrane module suppliers | Pre-potted gravity modules with data | Flux at 5 kPa, backwash limit, chlorine tolerance, LRV, NSF/ANSI/CAN 61 status |
| Local bucket, timber and print suppliers | Containers, stand, printed parts | Food-grade buckets with certificates; local timber |
| Households and communities | Users | Through partners only; no contact by the project at TRL 3 |

## Constraints

- Zero power; gravity only; usable by a household without tools once set up.
- Locally available containers (20 L food-grade buckets, jerrycans) wherever possible.
- Source classes (HWP-SRC-001): SC1, SC2, SC3 (with the settling stage) and SC5 suitable; SC4 conditional on certified analysis; SC6 not as a sole barrier; SC7 excluded.
- No claim beyond evidence (HWP-CLM-001): "designed to reduce bacteria and protozoa in household water for drinking and cooking"; no infant-use claim until tested at the infant-use volume and paired with D.
- Value-engineering target: USD 60 of prototype parts (a control target, not a limit).

## Out of scope

Viruses without D, arsenic, fluoride, nitrate, lead, PFAS, pesticides, cyanotoxins, salt, fuel and industrial chemicals; flood and runoff water as a sole barrier; electrical treatment; certification and distribution, which follow accredited testing.

## Prior work

- **0.1 um bucket hollow-fibre kits** (Sawyer PointONE): 46.5 to 54 L/h under a 19 L bucket with a 0.3 m hose, above 7 log *Klebsiella* and 5 log *Cryptosporidium* and *Giardia* in the laboratory, no virus removal, about USD 60 retail ([CAWST fact sheet](https://washplusblog.fhi360.org/drinkingwaterupdates/wp-content/uploads/2014/03/cawst-sawyer.pdf), checked 2026-11-11).
- **LifeStraw Family 2.0**: 20 nm ultrafiltration, over 12 L/h, 30,000 L life, 5 L storage, listed as meeting the WHO "highly protective" level, about USD 67 ([Engineering for Change](https://www.engineeringforchange.org/solutions/product/lifestraw-family-2-0/), checked 2026-11-11).
- **Ceramic candle filters** (British Berkefeld): about 1 L/h per candle, 2 to 4 candles in stacked chambers, silver-impregnated ([data sheet](https://cdn.shopify.com/s/files/1/2522/0950/files/British_Berkefeld_SS_Gravity_-_Data_Sheet.pdf), checked 2026-11-11).
- **Biosand filters** (CAWST version 10): 0.4 L/min maximum, 12 to 18 L batches, up to 30 days to ripen, 87.9 to 98.5 % bacteria reduction in the field ([CAWST 2009 fact sheet](https://sswm.info/sites/default/files/reference_attachments/CAWST%202009%20Biosand%20Filter%20Fact%20Sheet%20academic_1.pdf), checked 2026-11-11).
- **CDC Safe Water System**: chlorine dose of 3.75 %-mL per 20 L for clear water (twice that for turbid water), 30 minutes before drinking, residual above 0.2 mg/L at 24 h ([National Academies, 2006](https://www.nationalacademies.org/read/11577/chapter/8), checked 2026-11-11).
- **Deployment warning**: 24 % non-use and 56 % correct use at 12 months in a large Kenyan household-filter deployment (HWP-PRB-001).

## Kill criteria

Carried from HWP-PRB-001 and HWP-PLN-001, applied to C: stop or pause if C cannot show consistent bacteria and protozoa reduction under realistic household conditions; if flow becomes unusable for the 45 L day or is not recovered by backflush; if seal or membrane integrity cannot be kept in household handling; if cost per litre or complexity is not viable at humanitarian scale; or if partners decline for safety, liability or usability reasons.

## Open questions

- Which household sizes and volumes does the first partner see (the 45 L design day is the Sphere upper figure)?
- Will households fill a raw bucket at 1.27 m from 5 L jugs, or does the stand need a lower top shelf and a larger module?
- Is chlorine taste in stored water acceptable where D is used, given C has no carbon stage?
- Who resupplies the module after about two years, and how is end of life signalled?

## User research and co-design

- [ ] Confirm a household field partner through Helpful Engineering
- [ ] Persona trials with known potable test water only: filling, tap use, backflush, air test (child, elderly, low dexterity)
- [ ] Measure local bucket sizes, timber sections and household water use
- [ ] Revise HWC-URS-001 from findings before freezing the design

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
