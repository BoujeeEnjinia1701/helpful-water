---
doc_id: HWB-PRB-001
title: "Helpful Water B: bottle cartridge problem statement"
project: "Helpful Water B: bottle cartridge"
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
    change: "First problem statement for solution B, citing the program problem HWP-PRB-001 (kit 1.9.1-he)"
---

# Helpful Water B: bottle cartridge problem statement

Families, schools and camps that drink from untreated or recontaminated sources need a personal filter that costs little, works with the bottles they already have, lasts 6 to 12 months and needs no power, tools or straw. Solution B is a screw-on cartridge for a standard PET bottle that is designed to reduce bacteria and protozoa; it is one of four Helpful Water solutions that share the program evidence in HWP-PRB-001. Design with, not for: these needs are a desk draft from the Helpful Engineering source pack and must be reviewed with users through a field partner before any build.

> **Release limitation.** Nothing in this folder is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The problem for solution B

- **Scale and harm** are stated once for the program: 2.1 billion people lack safely managed drinking water and about 505,000 diarrhoeal deaths a year are attributed to contaminated drinking water (HWP-PRB-001, citing WHO and UNICEF 2025 and the WHO fact sheet).
- **Why a bottle cartridge.** A straw (solution A) protects only the person sipping and cannot fill a cup for a child or for cooking (HWP-PRB-001, Ali Raza's review). A cartridge on a bottle can be squeezed into a cup, shared without a shared mouthpiece, and uses a container people already own. The viability shortlist scored it 40 of 50, the joint top score: "modular screw-on cartridge that turns any plastic bottle" into a long-life filter, squeeze or gravity, hollow fibre plus activated carbon, reusable 6 to 12 months with replaceable carbon, about 100 g, backflushing needed, under USD 8 at scale and under USD 10 per user per year (Project Viability Shortlist Analysis, item 9).
- **The gap.** Commercial squeeze filters exist (Sawyer Squeeze about USD 46, Sawyer Mini USD 17 to 29, Membrane Solutions straw USD 19.99; HWB-MKT-001), but their price, closed designs and proprietary threads limit regional manufacture and resupply. None is published as open hardware with its calculations.
- **What it must not do.** Imply virus protection, chemical removal or safety. The membrane is not a virus barrier; where viruses are a risk the water is also treated with chlorine (solution D or a WHO-recommended tablet; Amish, 2026-11-11: no virus claim, co-treat).

## Users and context

Table 1. Users and needs for solution B (personas from HWP-PRB-001 Table 1).

| User type | Goals and needs | Typical use scenario | Pain points and challenges |
| --- | --- | --- | --- |
| Child (8 to 12) | Fill a cup or drink with a squeeze a child can give | School, home, camp | Grip of about 12 to 22 kg at age 10 to 11; impatience |
| Elderly user | Low effort; a no-squeeze option | Home, camp | Grip of about 15 to 25 kg (women 70+), arthritis |
| User with limited dexterity | Screw on, open the valve, change the carbon without small loose parts | Home | Threads, small seals, syringe backflush |
| Household carer | Treated water into cups for children, without passing a mouthpiece around | Rural home, camp shelter | A straw cannot serve others; bottle squeeze is tiring for litres |
| Crisis or disaster recipient | Use at once with pictograms | Flood or displacement | No time; any PET bottle to hand |
| Field worker or NGO distributor | Fits the bottles in the local supply; carbon resupply | Distribution point | Bottle neck variety; consumable logistics |
| Traveller or outdoor user | Light and compact; fits a bottle | Trekking | Compares with Sawyer and others |
| High-turbidity user | Usable flow from muddy water after settling | Monsoon | Fast fouling; backflush often |
| Immunocompromised user | Higher margin; knows the device's limits | High-HIV-prevalence regions | Viruses and silent failure matter more |

### Stakeholders

Table 2. Stakeholders who are not day-to-day users (program list in HWP-PRB-001 Table 2; additions for B).

| Stakeholder group | Role or interest | Engagement needed |
| --- | --- | --- |
| Helpful Engineering and Design Molecule Labs | Co-owners of the program | Design review of the B options and the open decisions |
| NGO and WASH cluster buyers | Procurement, cost per litre, resupply | Review the carbon consumable and the no-virus pairing |
| Bottled-water and beverage bottlers (neck finish owners) | The PCO 1881, PCO 1810 and 38 mm finishes on local bottles | Survey of local finishes before the adapter range is fixed |
| Membrane module makers | Pre-potted modules with data sheets | Request for quotation (HWB-DEC-001 C1 to C3) |
| Accredited water microbiology laboratories | Challenge testing at TRL 4 | Protocols per HWP-VER-001 |
| Regional moulders and makerspaces | Make the housings | Open drawings under CERN-OHL-P-2.0 |

## Constraints

- Program constraints of HWP-PRB-001: zero power, zero setup, open hardware, no claim beyond evidence, TRL 3 and stage P3.
- Fits standard PET bottles: 28 mm PCO 1881 and PCO 1810 directly; 38 mm wide-mouth finishes through an adapter (HWB-CAL-001 section 2).
- Value-engineering target USD 20 for prototype parts; under USD 8 at scale and under USD 10 per user per year from the shortlist (targets, not limits; STANDARDS section 18).
- Source classes: SC1, SC2 and SC5 suitable; SC3 and SC4 conditional (settle turbid water first; well water only after analysis); SC6 and SC7 excluded (HWP-SRC-001).

## Out of scope

Viruses without co-treatment, dissolved chemicals (arsenic, nitrate, fluoride, lead, PFAS, pesticides), salt, radiological and unknown industrial contaminants; desalination; electrical treatment; certification and distribution (HWP-PRB-001).

## Kill criteria

Those of the program (HWP-PRB-001, HWP-PLN-001), applied to B: stop or pause if the cartridge cannot show consistent bacteria and protozoa reduction; if flow at a child's or elderly user's squeeze is unusable or is not recovered by backflush; if the header seal or membrane integrity cannot be kept through drops, freezing warnings and carbon changes; if cost per user per year cannot approach USD 10; or if partners decline on safety, liability or usability grounds.

## Open questions

- Which neck finishes dominate in the first partner's region (PCO 1881, PCO 1810, 38 mm, others)?
- Is a squeeze effort acceptable for children and elderly users, or is the gravity mode (option B2) the household default?
- Who resupplies carbon capsules, or can users refill them with locally bought granular carbon?
- Is a bottle made for single use acceptable for months of reuse with this cartridge (cleaning, cracking, leaching; HWB-REG-001)?

## User research and co-design

- [ ] Field partner through Helpful Engineering (HWP-PLN-001)
- [ ] Neck finish survey of local bottles
- [ ] Persona squeeze trials with known potable test water only (child, elderly, low dexterity)
- [ ] Revise these needs and the requirements from findings before any build

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
