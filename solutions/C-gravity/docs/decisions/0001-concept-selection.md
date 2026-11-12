---
doc_id: HWC-DDR-001
title: "Helpful Water C: concept selection"
project: "Helpful Water C: household gravity filter"
doc_type: Decision record
version: "0.1"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: "Concept selection argued; C1 recommended; Proposed, awaiting Amish"
---

# Helpful Water C: concept selection

**Status: Decided by Amish on 2026-11-11 (recommendation adopted).** C1 (two-bucket hollow-fibre filter) scored 286 of 345 in HWC-OPT-001, C2 (ceramic candles) 234 and C3 (plastic biosand) 227. C1 leads the runner-up by 22 %, outside the 10 % band of STANDARDS section 21, so the recommendation is C1.

## Context

The brief asked for a household gravity filter for five people, built from locally available containers, with a settling or prefilter step for turbid water, a closed safe-storage container with a tap, and an interface for solution D. It named three principles to consider: a hollow-fibre module fed by gravity, ceramic candles, and a biosand or slow sand filter. All three pass the STEM check (HWC-STM-001); none fails outright, so none is dropped.

## Options

1. **C1 two-bucket hollow fibre.** 45 L in 1.6 to 2.8 h of filtering; works the first day; chlorine from D can be dosed before the membrane, which then removes *Cryptosporidium*, and the residual passes into storage; USD 86.40 of prototype parts; weak points: the assumed membrane permeability, the 1.27 m fill rim and a bought module that must be resupplied after about two years.
2. **C2 ceramic candles.** Simple, stackable, no stand; about 19 h of filtering for 45 L with four candles; brittle and silent when cracked; silver needs biocide registration.
3. **C3 plastic biosand.** No consumable, regional materials; up to 30 days to ripen with low and silent removal; about 1 to 1.8 log bacteria in the cited data, below the WHO two-star target; 124 kg of media; chlorine only after the filter.

## Recommendation

C1, for the reasons in HWC-OPT-001: it is the only option that delivers the household day in a few hours from the first day and the only one in which the D co-treatment and the filter cover each other's gap in one pass. Grafts: C2's stacked arrangement as a fallback where no stand can be built; C3's practice of chlorinating stored water while performance is in doubt.

## Consequences

The drawings (HWC-DWG-001, 002, 101 to 113), BOM and build plan (HWC-BLD-001) describe C1. If Amish picks C2 or C3, their D3 models in `cad/src/model.py` are the starting point and the drawing, BOM and build plan are redone.

Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
