#!/usr/bin/env python3
"""Write Tables 1 and 3 of HWD-STM-001 from docs/04-calcs/stem_results.csv and stem_results_dropped.csv between the
STM_TABLE and STM_DROPPED markers. Run from the solution folder after stem_check.py.
Licence: Apache-2.0. Design Molecule Labs with Helpful Engineering."""
import csv, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
HEAD = ["| # | Claim | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |"]


def rows(name, dropped=False):
    out = list(HEAD)
    for r in csv.DictReader((ROOT / "docs/04-calcs" / name).open()):
        v = r["verdict"] + (" (option dropped)" if dropped and r["verdict"] == "Fails" else "")
        cb = r["closed_by"] or ("HWD-CAL-001" if r["verdict"].startswith("Within") else ("Option dropped" if dropped else "Open"))
        out.append("| " + " | ".join([r["id"], r["claim"], r["field"], r["branch"], r["law"], r["check"], v, cb]) + " |")
    return out


doc = ROOT / "docs/01b-stem-check.md"
t = doc.read_text()
t = re.sub(r"<!-- STM_TABLE -->.*?<!-- /STM_TABLE -->", "<!-- STM_TABLE -->\n" + "\n".join(rows("stem_results.csv")) + "\n<!-- /STM_TABLE -->", t, flags=re.S)
t = re.sub(r"<!-- STM_DROPPED -->.*?<!-- /STM_DROPPED -->", "<!-- STM_DROPPED -->\n" + "\n".join(rows("stem_results_dropped.csv", True)) + "\n<!-- /STM_DROPPED -->", t, flags=re.S)
doc.write_text(t)
print("tables written")
