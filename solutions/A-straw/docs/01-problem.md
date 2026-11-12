---
doc_id: HWA-PRB-001
title: "Helpful Water A: filter straw problem statement"
project: "Helpful Water A: filter straw"
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
    change: First problem statement for solution A, citing the program statement HWP-PRB-001
---

# Helpful Water A: filter straw problem statement

A person drinking straight from a stream, a lake, a stored container or a distrusted tap needs a personal barrier that reduces bacteria and protozoa at the suction a child or an elderly person can give, that can be cleaned in the field, and that never fails without the user knowing. Solution A is that personal barrier: the filter straw of the Helpful Engineering Rev A component specification (2026-10-14), taken to a constructable design on paper. The program problem, its scale and its evidence are in HWP-PRB-001 and are not repeated here.

> **Release limitation.** Nothing in this folder is a validated water treatment product. No prototype is used to treat water for drinking until its pathogen performance, materials safety, integrity, source suitability and claims are validated by qualified laboratories (HWP-CLM-001).

## The problem for a personal straw

- **Per-sip protection only.** A straw protects the person sipping, at the moment of drinking. It does not treat water for cooking, for a stored supply or for an infant (HWP-PRB-001, "Why several solutions"); those needs belong to solutions B and C.
- **Flow against effort.** Hollow-fibre straws on the market flow at about 0.5 to 1 L/min in clean water, and users report dissatisfaction below about 400 mL/min (concept validation questions, item 12). The Rev A specification asks for at least 200 mL/min at 10 kPa or less. A child or an elderly person sucks less hard than an adult, so the flow they get is what decides whether the straw is used.
- **Silent failure.** The highest-risk failure across hollow-fibre filters is a cracked fibre or a leaking seal after freezing or a drop: water still flows normally while pathogens pass (concept validation questions, items 17 and 42).
- **Cleaning without contamination.** Backflushing restores flow, but if the cleaning water passes through the carbon, or dirty water reaches the clean side, cleaning makes the straw less safe (Rev A sections 02 and 05).
- **Viruses.** A microfiltration or ultrafiltration straw does not reliably remove viruses. The program position, decided by Amish on 2026-11-11, is "No virus claim, co-treat": solution A carries the on-product virus warning and points to solution D or a WHO-recommended tablet.

## Users and context

The personas come from HWP-PRB-001 Table 1; this table keeps the ones a straw serves and states what each needs from it.

Table 1. Users and needs for the filter straw.

| User type | Goals and needs | Typical use scenario | Pain points and challenges |
| --- | --- | --- | --- |
| Child (8 to 12) | Enough flow at low suction; a mouthpiece that fits a small mouth | School, home, camp | Low suction (assumed about 5 kPa, HWA-CAL-001), impatience |
| Elderly user | Low effort; acceptable taste; caps that need little grip | Home, camp | Low suction, arthritis, sensitivity to taste |
| User with limited dexterity | Use and clean without small loose parts or tools | Home | Bayonets, plugs and the backflush syringe |
| Crisis or disaster recipient | Reduced risk at once with almost no training | Flood or displacement | Stress; no time for upkeep |
| Humanitarian field worker | Fast demonstration, predictable operation | Distribution points | Training many people quickly; carbon resupply |
| Traveller or outdoor user | Light, pocketable, compares with LifeStraw and Sawyer | Trekking, travel | Flow and size against commercial straws |
| High-turbidity user | Usable flow from muddy water | Monsoon, floods | Fast clogging; needs pre-settling (HWP-SRC-001 SC3 conditional) |
| Immunocompromised user | Higher margin; to know when the straw has failed | High-HIV-prevalence regions | Viruses and *Cryptosporidium*; silent failure |

### Stakeholders

Table 2. Stakeholders specific to solution A (the program list is HWP-PRB-001 Table 2).

| Stakeholder group | Role or interest | Engagement needed |
| --- | --- | --- |
| Helpful Engineering Helpful Water team | Rev A owners; design review of this solution | Review of HWA-DEC-001 open decisions |
| Hollow-fibre module makers | Pre-potted outside-in modules, permeability and integrity data | Requests for quotation at P3 to P4 (HWA-DEC-001 C1) |
| Accredited water microbiology laboratory | Challenge testing (HWP-VER-001 TB) | Protocol before TRL 4 |
| NGO and WASH buyers | Cost per litre, resupply of carbon, claims | Review before any pilot |
| Patent attorney (pro bono) | Freedom to operate against US 8,852,439 B2 (HWP-FTO-001) | Opinion before any product is made for distribution |

## Source classes

Solution A is designed for HWP-SRC-001 classes SC1 (treated tap, taste), SC2 (clear stream or lake) and SC5 (stored household water); SC3 (moderately turbid river) only after pre-settling and SC4 (private well) only after certified analysis; SC6 (flood or urban runoff) and SC7 (brackish, sea, industrial or mining water) are excluded.

## Constraints

- Envelope from Rev A: 205 mm long, 26 mm across the body, 22 mm bore, 2 mm wall; kit compatible under 25 cm and 3 cm (concept validation questions, item 39).
- Zero power and no setup beyond removing the caps.
- Value-engineering target: USD 25 for prototype parts; the program target at mass production is about USD 1 to 5 a unit (HWP-PLN-001).
- Bought, qualified, pre-potted membrane modules; no in-house membrane spinning or potting (Rev A, build-versus-buy).
- Licences: CERN-OHL-P-2.0 hardware, Apache-2.0 software, CC-BY-4.0 documentation.
- Claims follow HWP-CLM-001: designed to reduce bacteria and protozoa in clear freshwater; no virus claim; exclusions stated on the product.

## Exclusions shown on the product

Viruses (co-treat with chlorine: solution D or a WHO-recommended tablet), salt, arsenic, nitrate, fluoride, lead, PFAS, pesticides, cyanotoxins, fuel and industrial chemicals, radiological contaminants. Do not freeze when wet.

## User research and co-design

- [ ] Persona flow trials with known potable test water only (child, elderly, low dexterity), HWP-VER-001 TH
- [ ] Confirm the acceptable flow: 200 mL/min at 10 kPa or 400 mL/min (HWA-DEC-001 D3)
- [ ] Ask a field partner who would resupply carbon cartridges, or whether a no-carbon variant is preferred
- [ ] Test pictogram comprehension for use, backflush, the air-hold check and end of life


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
