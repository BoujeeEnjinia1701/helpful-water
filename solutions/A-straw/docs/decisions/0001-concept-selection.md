---
doc_id: HWA-DDR-001
title: "Helpful Water A: filter straw concept selection"
project: "Helpful Water A: filter straw"
doc_type: Design decision record
version: "0.2"
status: Draft
date: 2026-11-11
author: Amish Chadha
license: CC-BY-4.0
revisions:
  - version: "0.1"
    date: 2026-11-11
    author: Amish Chadha
    change: Concept selection proposed (A1), awaiting Amish
  - version: "0.2"
    date: 2026-11-11
    author: Amish Chadha
    change: "Figures updated after the independent STEM review (HWA-STM-001 v0.2): permeabilities at 20 C, flows 110 to 179 mL/min at 10 kPa"
---

# 0001: Concept selection

- **Date:** 2026-11-11
- **Status:** proposed, awaiting Amish (HWA-DEC-001 D1)

## Context

The solution brief asks for at least two working principles: the Rev A hollow-fibre straw, a different pathogen barrier (a ceramic tube) and the copper and charcoal straw of the viability shortlist. All three are modelled at detail level D3 in `cad/src/model.py` and checked in HWA-STM-001.

## Options considered

- **A1 hollow-fibre straw with backflush:** 164 of 215; no Fails row; flow tight (110 to 179 mL/min at 10 kPa).
- **A2 ceramic tube straw:** 135; fails on flow (about 10 mL/min at 10 kPa).
- **A3 copper and charcoal straw:** 125; fails on efficacy (seconds of copper contact; charcoal is not a barrier).

## Decision

Proposed: carry A1 to the drawing, BOM and build plan, as this folder already does so that TRL 3 evidence exists for Amish to review. A2 and A3 stay in the model, marked dropped. Not within 10 %, so a single recommendation is made.

## Consequences

If Amish chooses A1, D2 (membrane grade) and D3 (flow target) become the first decisions of P4. If he asks for a different barrier, A2's flow failure means a new principle is needed rather than a revised ceramic tube.


Licence: this document is licensed under CC-BY-4.0 (Creative Commons Attribution 4.0 International), following the Helpful Engineering licensing guide. Design Molecule Labs with Helpful Engineering.
