"""Helpful Water C: household gravity filter. Main dimensions (mm unless named otherwise) shared by the CAD model
(cad/src/model.py) and the calculations (docs/04-calcs/sizing.py, HWC-CAL-001; docs/04-calcs/stem_check.py).
Kept apart from model.py so the calculations run without the CAD kernel. CONCEPT, NOT FOR FABRICATION.

Bucket sizes are assumed typical values for a 5 US gal (about 20 L) food-grade HDPE pail and are measured from the
local buckets before any part is drawn to them (HWC-DEC-001 C3).

Licence: CERN-OHL-P-2.0 (hardware design files, Helpful Engineering licensing guide).
"""

PARAMS = {
    # ---- household demand (HWC-CAL-001 section 2) -----------------------------------------------------------
    "PERSONS": 5,
    "L_PER_PERSON_DAY": 9.0,        # Sphere: drinking and food 2.5 to 3 L, basic cooking 3 to 6 L (upper end used)
    "FILTER_HOURS_TARGET": 3.0,     # "a few hours" of filtering a day, with a module due for backflush
    # ---- 20 L food-grade HDPE bucket (assumed typical, measure locally) ---------------------------------------
    "BKT_TOP_OD": 300.0, "BKT_BOT_OD": 262.0, "BKT_H": 370.0, "BKT_WALL": 2.3, "BKT_FLOOR": 3.0,
    "BKT_RIM": (306.0, 8.0),        # rim bead outside diameter and height
    "LID_T": 3.0, "LID_SKIRT": 14.0,
    # ---- C1 stand (timber, bolted) --------------------------------------------------------------------------
    "TIMBER": 45.0,                 # 45 x 45 mm planed softwood
    "LEG_C": 187.5,                 # leg centre from the stand axis in X and Y (420 mm outer frame)
    "FOOT_L": 560.0,                # cross feet along Y; widened from 420 for stability (HWC-DEC-001 F1)
    "TOP_Z": 900.0,                 # top of the upper shelf (raw bucket sits here)
    "SHELF_T": 18.0,                # exterior plywood
    "LOW_Z": 120.0,                 # top of the lower rails; the lower shelf sits on them
    "CLEAN_Y": -75.0,               # clean bucket centre moved forward so its tap clears the front rail
    # ---- C1 raw side --------------------------------------------------------------------------------------
    "OUTLET_H": 50.0,               # raw outlet centre above the raw bucket floor: the settling zone below it
    "FILL_L": 17.0,                 # raw fill line, litres (marked on the bucket)
    "STRAINER_UM": 250,             # stainless strainer on the raw outlet (protects valve and module from grit)
    "CLOTH_FOLDS": 4,               # cotton cloth folded to 8 layers in the fill ring (Colwell et al. 2003)
    "D_PORT_D": 60.0,               # solution D dosing port in the raw lid (interface, to agree with D)
    "FILL_D": 160.0,                # fill opening in the raw lid, covered by the cloth ring
    # ---- C1 hollow-fibre module (bought, pre-potted; the dimensions are the design request to the supplier) --
    "FIBRE_OD": 0.80, "FIBRE_ID": 0.50, "U_FIBRES": 600, "LEG_LEN": 220.0, "PORE_UM": 0.1,
    "MOD_OD": 50.0, "MOD_ID": 46.0, "MOD_L": 290.0, "POTTING_H": 15.0, "BUNDLE_D": 41.0,
    "MOD_TOP_Z": 650.0,             # module top (raw inlet) height in the stand
    # ---- hoses and fittings ---------------------------------------------------------------------------------
    "HOSE_ID": 9.5, "HOSE_OD": 14.0,           # 3/8 in silicone tube
    "HOSE_RAW_L": 0.44, "HOSE_CLEAN_L": 0.37,  # m, lengths of the swept hoses in model.py
    "BULKHEAD_BORE": 12.0, "VALVE_BORE": 12.0, "BARB_BORE": 7.0,
    "CLEAN_INLET_TOP": 25.0,        # clean inlet fitting height above the clean lid
    "TAP_BORE": 8.0, "TAP_H": 45.0,  # clean tap: effective bore and centre height above the clean bucket floor
    "REFILL_L": 2.5,                # "start a batch only below this line" mark on the clean bucket (HWC-DEC-001 F3)
    # ---- backflush and integrity --------------------------------------------------------------------------
    "SYRINGE_ML": 60.0, "SYRINGE_BORE_MM": 26.7,
    # ---- C2 ceramic candles ---------------------------------------------------------------------------------
    "CANDLES": 4, "CANDLE_OD": 50.0, "CANDLE_L": 178.0, "CANDLE_R": 68.0,   # 7 in x 2 in candles on a 136 mm circle
    "STOOL_H": 300.0,
    # ---- C3 biosand (plastic body, CAWST version 10 layer depths) --------------------------------------------
    "BSF_OD": 400.0, "BSF_ID": 392.0, "BSF_H": 900.0,
    "BSF_LAYERS": {"drainage_gravel": 50.0, "separating_gravel": 50.0, "fine_sand": 540.0},
    "BSF_STANDING": 50.0, "BLOCK_H": 150.0,
}
