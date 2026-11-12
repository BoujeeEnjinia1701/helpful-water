---
doc_id: HWP-PRB-001
title: Helpful Water program problem statement
project: Helpful Water
doc_type: Problem statement
version: '0.1'
status: Draft
date: '2026-11-11'
author: Amish Chadha
license: CC-BY-4.0
revisions:
- version: '0.1'
  date: '2026-11-11'
  author: Amish Chadha
  change: First draft from the Helpful Water source pack (2026-11-11)
---

# Helpful Water program problem statement

Hundreds of millions of people drink from unsafe sources and get preventable waterborne infections, and the options they have are too expensive, too hard to run or not made for their setting. Helpful Water is a joint program of Design Molecule Labs and Helpful Engineering that develops a family of open, unpowered point-of-use water treatment products, from a personal straw to a household gravity filter, each taken to a constructable design on paper (TRL 3) before any prototype is built. Design with, not for: requirements come from the people who will use these products, through partners in the field.

> **Release limitation.** Nothing in this repository is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The problem

- **Scale.** 2.1 billion people, one in four, still lack safely managed drinking water, and 106 million drink untreated surface water ([WHO and UNICEF, 2025](https://www.who.int/news/item/26-08-2025-1-in-4-people-globally-still-lack-access-to-safe-drinking-water---who--unicef), checked 2026-11-11). At least 1.7 billion people used a drinking water source contaminated with faeces in 2022 ([WHO drinking-water fact sheet](https://www.who.int/news-room/fact-sheets/detail/drinking-water), checked 2026-11-11).
- **Harm.** Microbiologically contaminated drinking water is estimated to cause about 505,000 diarrhoeal deaths a year, and about 395,000 deaths of children under five could be avoided if unsafe water, sanitation and hygiene were addressed (same fact sheet).
- **Inequality.** Coverage of safely managed drinking water is 38 percentage points lower in fragile contexts than elsewhere, and people in the least developed countries are more than twice as likely to lack basic drinking water ([WHO and UNICEF, 2025](https://www.who.int/news/item/26-08-2025-1-in-4-people-globally-still-lack-access-to-safe-drinking-water---who--unicef)).
- **Gap.** Current options in target markets are costly, need upkeep, are hard to carry or are not available at the point of use (Helpful Water update, 2026-02-26). Chemical tablets cost about USD 0.02 a litre but do not inactivate *Cryptosporidium* ([Akvopedia, NaDCC](https://akvopedia.org/wiki/Chlorine_(NaDCC)), checked 2026-11-11); hollow-fibre straws remove bacteria and protozoa but not viruses, and protect only the person sipping.

## Why several solutions

A personal straw protects only the person drinking from it. It does not treat water for cooking or for a stored household supply, and it cannot be used by an infant, while diarrhoeal deaths concentrate in children under five (Ali Raza, concept validation review, 2026). The program therefore carries four lettered solutions that share one evidence base:

| Solution | Folder | What it is | Main users |
| --- | --- | --- | --- |
| A | `solutions/A-straw` | Personal filter straw: steel mesh, hollow-fibre membrane, carbon polish, backflush port (Rev A specification) | Individuals, field workers, disaster response |
| B | `solutions/B-bottle-cartridge` | Screw-on cartridge that turns a standard PET bottle into a squeeze or gravity filter | Individuals and families, schools, camps |
| C | `solutions/C-gravity` | Household gravity filter for drinking and cooking water, usable for children and infants' water | Households, clinics, camps |
| D | `solutions/D-virus-add-on` | Chlorine co-treatment add-on that pairs with A, B or C to cover viruses | All, where viral disease is a risk |

## Users and context

Table 1. Users and needs (personas from the concept validation questions, 2026).

| User type | Goals and needs | Typical use scenario | Pain points and challenges |
| --- | --- | --- | --- |
| Child (8 to 12) | Drink without help; enough flow at low suction | School, home, camp | Low suction, small mouth, impatience |
| Elderly user | Low effort; acceptable taste | Home, camp | Low suction, arthritis, sensitivity to taste |
| User with limited dexterity or disability | Use and clean without small parts or tools | Home | Caps, cartridge changes and backflush steps |
| Crisis or disaster recipient | Safer water at once with almost no training | Flood or displacement | Stress, no time, low tolerance for maintenance |
| Humanitarian field worker or NGO distributor | Fast onboarding, predictable operation, easy demonstration | Distribution points, outreach | Training many people quickly; resupply |
| Traveller or outdoor user | Portability and convenience | Trekking, travel | Compares with commercial products |
| High-turbidity user | Usable flow from muddy river or flood water | Monsoon, floods | Fast clogging, worst-case loading |
| Household carer (infants and cooking) | Treated water for the whole household, including infant feeds | Rural home, camp shelter | A straw cannot serve infants or cooking |
| Immunocompromised user | Higher protection margin | High-HIV-prevalence regions | Higher stakes from viruses, *Cryptosporidium* and silent failure |

### Stakeholders

Table 2. Stakeholders who are not day-to-day users.

| Stakeholder group | Role or interest | Engagement needed |
| --- | --- | --- |
| Helpful Engineering (Infectious Disease Challenge, Helpful Water team) | Co-owner of the program; volunteer engineers, testers and partners | Joint design reviews; lab and partner introductions |
| Design Molecule Labs | Co-owner; design kit, CAD, documentation | Runs the design pipeline to TRL 3 |
| NGO and WASH cluster buyers (for example UNHCR, MSF, Red Cross and Red Crescent) | Procurement, distribution, training | Review claims, cost per litre and resupply before any pilot |
| Ministries of health in target countries | Longer, higher-volume procurement path | Later, after independent testing |
| University and accredited water microbiology laboratories | Pathogen challenge testing, flow and turbidity benchmarking | Protocols before TRL 4 (HWP-VER-001) |
| Membrane, carbon and moulding suppliers | Qualified parts and data sheets | Requests for quotation at P3 to P4 |
| Certification bodies (NSF and others) | Materials and performance certification | Scope at P4 |
| Legal advisers (pro bono) | Claims, disclaimers, freedom to operate | Before any distribution (HWP-FTO-001) |
| Households and communities served | Drinking-water safety and adoption | Through partners only; no contact by the project at TRL 3 |

## Constraints

- Zero power, zero setup: every solution works without electricity and arrives ready to use.
- Humanitarian cost: cost per person per year and cost per litre over the device life are the comparison metrics, not unit price alone.
- Open hardware under the Helpful Engineering licensing guide (CERN-OHL-P-2.0, Apache-2.0, CC-BY-4.0).
- No claim beyond evidence (HWP-CLM-001): bacteria and protozoa reduction is the design intent of A to C; viruses are addressed only by the D co-treatment; dissolved chemicals, salt and heavy metals are excluded.
- Program at TRL 3 and stage P3 at most (`.kit/PHASE.yaml`); every solution reaches a constructable design with a build plan.

## Out of scope

- Desalination, reverse osmosis at the point of use (pressures of 50 to 800 psi are far beyond suction or squeeze; Helpful Water open questions, 2026), and removal of arsenic, fluoride, nitrate, lead, PFAS, pesticides, cyanotoxins or radiological contaminants.
- Copper as a disinfecting stage: removed from the Rev A design because of unverified contact efficacy, leaching and taste (component specification, 2026-10-14).
- Electrical treatment (UV lamps, electrochlorination).
- Certification and field distribution, which follow accredited testing beyond TRL 3.

## Prior work

- **LifeStraw Personal:** 0.2 um hollow fibre, 4,000 L rated life, 65 g, does not remove viruses ([MEC listing](https://www.mec.ca/en/product/6018-750/Personal-Water-Filter-Straw), checked 2026-11-11). Patent US 8,852,439 B2 covers a straw with one hollow-fibre bundle potted with closed ends toward the outlet (HWP-FTO-001).
- **Sawyer Mini:** 0.1 um hollow fibre, about USD 29, about 0.5 L/min squeezed, does not treat viruses ([OutdoorGearLab](https://www.outdoorgearlab.com/reviews/camping-and-hiking/backpacking-water-filter/sawyer-mini), checked 2026-11-11).
- **NaDCC tablets:** about USD 0.02 a litre, 30 minutes contact time, effective against bacteria and viruses, not *Cryptosporidium* ([Akvopedia](https://akvopedia.org/wiki/Chlorine_(NaDCC))).
- **Deployment evidence:** in a large household-filter deployment in Kenya, 24 % of households were not using the filters at 12 months and only 56 % used them correctly ([Stanford Social Innovation Review](https://ssir.org/articles/entry/thirty_million_dollars_a_little_bit_of_carbon_and_a_lot_of_hot_air), cited in the concept validation questions).

## Kill criteria (Helpful Water update, 2026-02-26)

Pause or stop a solution if it cannot show consistent bacteria and protozoa reduction under realistic conditions; if flow becomes unusable or is not recovered by backflush; if seal or membrane integrity cannot be kept in field handling; if total cost or complexity is not viable at humanitarian scale; or if partners decline because of safety, liability or usability concerns. These criteria are carried into each solution's plan and into HWP-PLN-001.

## Open questions

- Which target source classes come first for each solution (HWP-SRC-001)?
- What is the typical pH, turbidity and conductivity of the first partner's sources? Copper is no longer in the design, so the alkaline-water-and-copper question in the open questions no longer applies.
- What flow is acceptable: 200 mL/min at 10 kPa (Rev A target) or the roughly 400 mL/min below which straw users report dissatisfaction?
- Which components are disposable, and who resupplies carbon and chlorine in a displaced population?
- Which first partner: a WASH cluster member, a university laboratory or a Helpful Engineering field network? Left open under the portfolio rule.

## User research and co-design

- [ ] Confirm a field partner through Helpful Engineering
- [ ] Persona trials with known potable water only (child, elderly, low dexterity)
- [ ] Source-water characterisation for the first region (HWP-SRC-001)
- [ ] Revise the shared and solution requirements from findings before freezing any design


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
