#!/usr/bin/env python3
"""Write Table 1 of HWB-STM-001 from docs/04-calcs/stem_results.csv between the STM_TABLE markers.
Run from the solution folder after stem_check.py. Licence: Apache-2.0. Design Molecule Labs with Helpful Engineering."""
import csv, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader((ROOT / "docs/04-calcs/stem_results.csv").open()))
out = ["| # | Claim | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in rows:
    cb = r["closed_by"] or ("HWB-CAL-001" if r["verdict"].startswith("Within") else "Open")
    out.append("| " + " | ".join([r["id"], r["claim"], r["field"], r["branch"], r["law"], r["check"], r["verdict"], cb]) + " |")
doc = ROOT / "docs/01b-stem-check.md"
t = doc.read_text()
t = re.sub(r"<!-- STM_TABLE -->.*?<!-- /STM_TABLE -->", "<!-- STM_TABLE -->\n" + "\n".join(out) + "\n<!-- /STM_TABLE -->", t, flags=re.S)
doc.write_text(t)
print("table rows:", len(rows))
