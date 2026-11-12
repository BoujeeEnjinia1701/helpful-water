"""Release gate (STANDARDS sections 14, 16 and 17). Run from the repo root before a repository is made public
or a release is tagged:

    python .kit/release_gate.py

Prints ok / warn / FAIL lines and exits non-zero if any check fails. Warnings need a human look
but do not block. Optional tools are used when installed: gitleaks (secret scan of the whole
history), cffconvert (CITATION.cff schema), reuse (REUSE lint) and gh (visibility of linked sibling
repositories).
"""
import re, shutil, subprocess, sys
from pathlib import Path
import yaml

ROOT = Path.cwd()
KIT = Path(__file__).resolve().parent
TEXT = {".md", ".yaml", ".yml", ".cff", ".py", ".txt", ".csv", ".json", ".html"}
SOFT = ["research and educational prototype", "not a medical device"]
fails, warns = [], []


def ok(msg): print(f"ok   {msg}")
def warn(msg): warns.append(msg); print(f"warn {msg}")
def fail(msg): fails.append(msg); print(f"FAIL {msg}")
def run(*cmd): return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


pm = yaml.safe_load((ROOT / "project.yaml").read_text()) or {}
try:   # program repos (STANDARDS section 25.4): licences, REUSE and CITATION live at the repository top
    TOP = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=ROOT, text=True).strip())
except Exception:
    TOP = ROOT
owner, _, name = str(pm.get("repo", "")).partition("/")
readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""

# 1. Document control, TRL cap and concept media
r = run(sys.executable, str(KIT / "render.py"), "--check")
(ok if r.returncode == 0 else fail)("render.py --check" + ("" if r.returncode == 0 else ": " + " ".join(
    l.strip() for l in r.stdout.splitlines() if l.startswith(("FAIL", "     -")))[:400]))

# 1b. Program repos (STANDARDS section 25.4): each solution carries its own pipeline and storefront
program = bool(pm.get("program"))
if program:
    for sol in pm.get("solutions") or []:
        sd = ROOT / "solutions" / str(sol.get("folder", ""))
        g = subprocess.run([sys.executable, str(sd / ".kit" / "release_gate.py")], cwd=sd, capture_output=True, text=True)
        (ok if g.returncode == 0 else fail)(f"solution {sol.get('folder')}: release gate" + ("" if g.returncode == 0 else ": " + " ".join(
            l[5:] for l in g.stdout.splitlines() if l.startswith("FAIL"))[:300]))
        for l in g.stdout.splitlines():
            if l.startswith("warn"):
                warns.append(f"{sol.get('folder')}: {l[5:]}")
# 1c. The pipeline (sections 19 to 23)
if program:
    pass
elif "stage" in pm:
    stem = str(pm.get("stem_check", "")).lower()
    (ok if stem == "pass" else fail)(f"STEM check: {stem or 'missing'}" + ("" if stem == "pass" else " (STANDARDS section 20)"))
    n = len(pm.get("concept_options") or [])
    (ok if n >= 2 else fail)(f"{n} concept options" + ("" if n >= 2 else "; at least two are required (STANDARDS section 21)"))
    if pm.get("concept_chosen"):
        ok(f"concept chosen: {pm['concept_chosen']}")
    else:
        warn("no concept_chosen in project.yaml; the concept selection is still awaiting Amish")
    t = run(sys.executable, str(KIT / "trace.py"), "--check")
    (ok if t.returncode == 0 else fail)("traceability matrix" + (" current" if t.returncode == 0 else ": " + " ".join(l[5:] for l in t.stdout.splitlines() if l.startswith("FAIL"))[:300]))
else:
    warn("repo not yet on kit 1.8 pipeline documents (no 'stage' in project.yaml); run /upgrade-1.8")

# 2. Storefront (section 13)
if program:
    hero = ROOT / "media/program-hero.png"
    (ok if hero.exists() else fail)("media/program-hero.png" + (" present" if hero.exists() else " missing"))
    if "media/program-hero.png" not in readme:
        fail("README does not lead with media/program-hero.png")
for f in ([] if program else ["media/render-hero.png", "media/card.png", "media/social-preview.png"]):
    (ok if (ROOT / f).exists() else fail)(f + (" present" if (ROOT / f).exists() else " missing (python .kit/cards.py .)" if "render" not in f else " missing"))
sp = ROOT / "media/social-preview.png"
if sp.exists() and sp.stat().st_size >= 1_000_000:
    fail("media/social-preview.png is 1 MB or more; GitHub will refuse it")
if not program and not re.search(r"media/render-hero\.png", readme):
    fail("README does not lead with media/render-hero.png")
sys.path.insert(0, str(KIT))
import image_qc  # noqa: E402
qfails, qn = image_qc.run(ROOT)
for q in qfails:
    fail("image quality: " + q)
if not qfails:
    ok(f"image quality: {qn} images, text clear and readable, renders sharp")
tpl = ROOT / ".github/ISSUE_TEMPLATE" if (ROOT / ".github/ISSUE_TEMPLATE").exists() else TOP / ".github/ISSUE_TEMPLATE"
need = {"question.md", "build-report.md", "design-suggestion.md"}
have = {p.name for p in tpl.glob("*.md")} if tpl.exists() else set()
(ok if need <= have else fail)("issue templates " + ("present" if need <= have else "missing: " + ", ".join(sorted(need - have))))

# 3. Authorship (section 15)
cff = TOP / "CITATION.cff"
if not cff.exists():
    fail("CITATION.cff missing")
else:
    c = yaml.safe_load(cff.read_text()) or {}
    authors = c.get("authors") or []
    if not any(a.get("orcid") for a in authors if isinstance(a, dict)):
        fail("CITATION.cff has no author with an ORCID")
    else:
        ok("CITATION.cff names an author with an ORCID")
    try:
        import cffconvert  # noqa: F401
        has_cff = True
    except ImportError:
        has_cff = bool(shutil.which("cffconvert"))
    if has_cff:
        v = subprocess.run([sys.executable, "-c", "import sys; from cffconvert.cli.cli import cli; sys.argv = ['cffconvert', '--validate']; cli()"], cwd=TOP, capture_output=True, text=True)
        (ok if v.returncode == 0 else fail)("CITATION.cff schema" + ("" if v.returncode == 0 else ": " + v.stderr.strip()[-200:]))
    else:
        warn("cffconvert not installed; CITATION.cff schema not validated")

# 4. Licenses
lic = pm.get("licenses") or {}
helpful = pm.get("partner") == "Helpful Engineering"
if helpful:
    # Helpful Engineering licensing guide: one licence .txt per content type at the repo root (STANDARDS section 25.1)
    need = {"hardware": "LICENSE-HARDWARE.txt", "software": "LICENSE-SOFTWARE.txt", "documentation": "LICENSE-DOCUMENTATION.txt"}
    miss = [f for k, f in need.items() if lic.get(k) and not (TOP / f).exists()]
    (fail if miss else ok)("Helpful Engineering licence files present" if not miss else "licence .txt files missing: " + ", ".join(miss))
    want = {"hardware": "CERN-OHL-P-2.0", "software": "Apache-2.0", "documentation": "CC-BY-4.0"}
    wrong = [f"{k}: {lic.get(k)} (guide: {v})" for k, v in want.items() if lic.get(k) != v]
    (warn if wrong else ok)("licences match the Helpful Engineering guide" if not wrong else "licences differ from the Helpful Engineering guide: " + "; ".join(wrong))
elif not (ROOT / "LICENSE").exists():
    fail("LICENSE missing")
elif lic.get("hardware") and lic.get("software") and not (ROOT / "LICENSE-SOFTWARE").exists():
    fail("project.yaml names a software license but LICENSE-SOFTWARE is missing")
else:
    ok("license files present")

# 4b. Licensing metadata (section 16) and archiving (section 17)
miss = [f for f in ("REUSE.toml", "LICENSES", ".github/workflows/reuse.yml") if not (TOP / f).exists()]
if miss:
    fail("REUSE files missing: " + ", ".join(miss) + " (python .kit/archive.py reuse)")
else:
    try:
        import reuse  # noqa: F401
        rl = subprocess.run([sys.executable, "-m", "reuse", "--root", str(TOP), "lint", "-q"], capture_output=True, text=True)
        (ok if rl.returncode == 0 else fail)("reuse lint" + ("" if rl.returncode == 0 else " fails; run `reuse lint` and fix REUSE.toml"))
    except ImportError:
        warn("reuse not installed; REUSE compliance not checked (pip install reuse)")
if cff.exists():
    c = yaml.safe_load(cff.read_text()) or {}
    if not isinstance(c.get("license"), str):
        fail("CITATION.cff must name one license, not a list; Zenodo rejects a list (python .kit/archive.py zenodo)")
    else:
        ok(f"CITATION.cff names one license ({c['license']})")
    if not c.get("doi") and pm.get("archive", True):
        warn("CITATION.cff has no DOI yet; after the first Zenodo archive run python .kit/archive.py zenodo --doi <concept DOI>")
badges = (("zenodo.org/badge", "Zenodo DOI"), ("reuse.yml/badge.svg", "REUSE"), ("softwareheritage.org/badge", "Software Heritage"))
if pm.get("archive", True) is False:   # archiving switched off (Helpful Engineering profile, STANDARDS section 25.2)
    badges = (("reuse.yml/badge.svg", "REUSE"),)
for key, label in badges:
    if key not in readme:
        warn(f"README has no {label} badge (python .kit/archive.py reuse / zenodo)")

# 5. Writing rules: no em dashes anywhere in the repo's own text
tracked = run("git", "ls-files").stdout.split()
dash = [f for f in tracked if not f.startswith((".kit/", "LICENSES/")) and "/.kit/" not in f and Path(f).suffix in TEXT and (ROOT / f).exists()
        and "\u2014" in (ROOT / f).read_text(encoding="utf-8", errors="ignore")]
(ok if not dash else fail)("no em dashes" if not dash else "em dashes in: " + ", ".join(dash[:10]))

# 6. Wording and safety
if owner == "enjinia1929" or pm.get("area") == "BioMedical":
    miss = [s for s in SOFT if s not in readme.lower()]
    (ok if not miss else fail)("soft, non-clinical wording" if not miss else "README must say: " + "; ".join(miss))
if "not for fabrication" not in readme.lower():
    warn("README does not say the design is not for fabrication")
if not re.search(r"^##+ .*safety", readme, re.I | re.M):
    warn("README has no Safety heading; confirm hazards are covered (mains, pressure, heat, lithium, hydrogen, machinery)")

# 7. Secrets
if shutil.which("gitleaks"):
    g = run("gitleaks", "git", ".", "--no-banner", "--redact")
    (ok if g.returncode == 0 else fail)("gitleaks: no secrets in history" if g.returncode == 0 else "gitleaks found possible secrets; review before release")
else:
    warn("gitleaks not installed; history not scanned for secrets")

# 8. Links to sibling repositories must not point at private repos
links = sorted(set(re.findall(r"github\.com/([A-Za-z0-9-]+)/([A-Za-z0-9_.-]+?)(?:[/)#\s\"']|\.git|$)",
                              " ".join((ROOT / f).read_text(errors="ignore") for f in tracked
                                       if f.endswith((".md", ".yaml", ".cff")) and not f.startswith(".kit/")))))
others = [f"{o}/{n}" for o, n in links if f"{o}/{n}".lower() != str(pm.get("repo", "")).lower()]
if others and shutil.which("gh"):
    private = [o for o in others if run("gh", "repo", "view", o, "--json", "visibility", "-q", ".visibility").stdout.strip() != "PUBLIC"]
    (ok if not private else fail)("sibling links all public" if not private else "links to repos that are not public: " + ", ".join(private))
elif others:
    warn("links to sibling repos, check they are public: " + ", ".join(others))

print(f"\n{'FAIL' if fails else 'PASS'}: {len(fails)} failed, {len(warns)} warnings")
sys.exit(1 if fails else 0)
