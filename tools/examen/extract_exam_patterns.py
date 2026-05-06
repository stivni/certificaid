"""
Extraheer examenpatronen uit ITAA voorbeeldexamen PDFs.

Gebruik:
  python tools/examen/extract_exam_patterns.py                    # alle examens
  python tools/examen/extract_exam_patterns.py --exam 2013-1.pdf  # één examen
  python tools/examen/extract_exam_patterns.py --merge-only       # herconsolideer bestaande patronen
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import anthropic
import pdfplumber

ROOT = Path(__file__).resolve().parent.parent.parent
EXAMS_DIR = ROOT / "resources" / "voorbeeldexamens"
PATTERNS_DIR = ROOT / "data" / "exam_patterns"
INDEX_PATH = ROOT / "resources" / "voorbeeldexamens" / "INDEX.md"

# Laad .env
_env = ROOT / ".env"
if _env.exists():
    for _line in _env.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ[_k.strip()] = _v.strip()

TODAY = date.today().strftime("%Y%m%d")


# ---------------------------------------------------------------------------
# PDF → tekst
# ---------------------------------------------------------------------------

def extract_pdf_text(pdf_path: Path) -> str:
    """Extraheer alle tekst uit een PDF via pdfplumber."""
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append(f"[pagina {i}]\n{text}")
    return "\n\n".join(pages)


# ---------------------------------------------------------------------------
# Patroon-extractie via Claude
# ---------------------------------------------------------------------------

EXTRACTION_PROMPT = """\
Je analyseert een ITAA-bekwaamheidsexamen voor Gecertificeerde Accountants.

Jouw taak: identificeer alle **examenpatronen** in dit examen. Een examenpatroon is een terugkerende manier waarop het ITAA-examen kennis toetst — onafhankelijk van het specifieke onderwerp.

## Definitie van een patroon

Een patroon beschrijft:
- De **vraagvorm** (J/F, MC, open, berekening, tabel)
- De **cognitieve laag** (weten-en-inzien / toepassen / integratie)
- Wat de student echt moet kunnen om de vraag goed te beantwoorden
- De typische **valkuil** — wat gaat een onvoldoende-student fout denken?
- De **typische formulering** — exacte of parafrasen van examenzinnen

## Herken deze terugkerende patronen (en voeg toe wat je nog ziet)

- **uitzondering-in-reeks**: reeks uitspraken, sommige fout door randgeval/uitzondering
- **bereken-en-motiveer**: getal berekenen + wettelijke grondslag opgeven
- **grensgeval-herkenning**: situatie lijkt duidelijk maar triggert een specifieke uitzondering
- **procedure-stappen**: welke stappen, in welke volgorde, door wie
- **rol-en-bevoegdheid**: wie mag/moet wat doen in een gegeven situatie
- **vergelijk-behandeling**: twee situaties die lijken op elkaar maar anders behandeld worden
- **identificeer-de-fout**: beschreven handelwijze bevat een conceptuele fout
- **adviseer-en-onderbouw**: integratievraag, meerdere concepten combineren tot advies

## Output

Geef een JSON-array van patroonobjecten. Elk object heeft dit formaat:

```json
{
  "id": "patroon:[kebab-case-naam]",
  "naam": "Leesbare naam",
  "versie": "VERSIEDATUM.1",
  "bijgewerkt": "DATUM",
  "beschrijving": "Wat dit patroon inhoudt in 2-3 zinnen.",
  "vraagtypen": ["J/F"],
  "cognitieve_laag": "toepassen",
  "wat_getoetst_wordt": "Wat de student echt moet kennen/kunnen.",
  "typische_formulering": ["Exacte of geparafraseerde examenzin 1", "..."],
  "valkuil": "Wat gaat een onvoldoende-student fout denken of doen.",
  "pos_geobserveerd": ["2.1", "4.0"],
  "typische_themas": ["meldingsplicht", "btw-vrijstellingen"],
  "typische_concepten": [],
  "echte_voorbeelden": [
    {
      "examen": "EXAMEN_ID",
      "po": "X.X",
      "vraag_samenvatting": "Korte samenvatting van de vraag (1-2 zinnen).",
      "patroon_manifestatie": "Waarom dit een voorbeeld is van het patroon."
    }
  ]
}
```

Gebruik versie "VERSIEDATUM.1" en bijgewerkt "DATUM".
Gebruik examen-ID "EXAMEN_ID" in echte_voorbeelden.

Geef ALLEEN de JSON-array terug, geen uitleg errond.
"""


def extract_patterns_from_exam(pdf_path: Path, client: anthropic.Anthropic) -> list[dict]:
    """Extraheer patronen uit één exam PDF via Claude."""
    examen_id = pdf_path.stem
    # Normaliseer examen_id
    examen_id = re.sub(r"[^a-z0-9-]", "-", examen_id.lower()).strip("-")

    print(f"  → Lees PDF: {pdf_path.name}")
    text = extract_pdf_text(pdf_path)
    if len(text) < 200:
        print(f"  ⚠️  Te weinig tekst in {pdf_path.name}, overgeslagen")
        return []

    # Beperk tot max ~80k tekens om context te respecteren
    text = text[:80000]

    prompt = (
        EXTRACTION_PROMPT
        .replace("VERSIEDATUM", TODAY)
        .replace("DATUM", date.today().isoformat())
        .replace("EXAMEN_ID", examen_id)
    )

    print(f"  → Claude extraheert patronen...")
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n---\n\n## EXAMENTEKST\n\n{text}"
            }
        ]
    )

    raw = message.content[0].text.strip()

    # Extraheer JSON uit de response (soms omgeven door ```json ... ```)
    json_match = re.search(r"```json\s*(.*?)\s*```", raw, re.DOTALL)
    if json_match:
        raw = json_match.group(1)
    elif raw.startswith("["):
        pass  # al JSON
    else:
        # Probeer eerste [ ... ] te vinden
        start = raw.find("[")
        end = raw.rfind("]")
        if start != -1 and end != -1:
            raw = raw[start:end+1]

    try:
        patterns = json.loads(raw)
        print(f"  ✓ {len(patterns)} patronen geëxtraheerd")
        return patterns
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON-parsefout: {e}")
        print(f"  Raw output (eerste 500 chars): {raw[:500]}")
        return []


# ---------------------------------------------------------------------------
# Samenvoegen: meerdere examens → geconsolideerde patroonbibliotheek
# ---------------------------------------------------------------------------

MERGE_PROMPT = """\
Je consolideert examenpatronen die geëxtraheerd zijn uit meerdere ITAA-examens.

Hieronder staan alle geëxtraheerde patronen (met duplicaten). Jouw taak:
1. Groepeer patronen die hetzelfde patroon beschrijven (ook al hebben ze een andere naam).
2. Maak voor elke groep één geconsolideerd patroonobject met:
   - De beste beschrijving, typische_formulering en valkuil (kies of combineer)
   - Alle unieke echte_voorbeelden samengevoegd
   - Alle pos_geobserveerd en typische_themas samengevoegd en gededupliceerd
3. Houd patronen apart als ze echt een verschillende cognitieve operatie beschrijven.

Output: JSON-array van geconsolideerde patroonobjecten in exact hetzelfde schema als de input.
Gebruik versie "VERSIEDATUM.1" en bijgewerkt "DATUM".
Geef ALLEEN de JSON-array terug.
"""


def merge_patterns(all_patterns: list[dict], client: anthropic.Anthropic) -> list[dict]:
    """Consolideer patronen uit meerdere examens via Claude."""
    if not all_patterns:
        return []

    print(f"\n  → Consolideer {len(all_patterns)} patronen uit alle examens...")

    prompt = (
        MERGE_PROMPT
        .replace("VERSIEDATUM", TODAY)
        .replace("DATUM", date.today().isoformat())
    )

    raw_input = json.dumps(all_patterns, ensure_ascii=False, indent=2)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=12000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\n---\n\n{raw_input}"
            }
        ]
    )

    raw = message.content[0].text.strip()
    json_match = re.search(r"```json\s*(.*?)\s*```", raw, re.DOTALL)
    if json_match:
        raw = json_match.group(1)
    elif not raw.startswith("["):
        start = raw.find("[")
        end = raw.rfind("]")
        if start != -1 and end != -1:
            raw = raw[start:end+1]

    try:
        merged = json.loads(raw)
        print(f"  ✓ {len(merged)} geconsolideerde patronen")
        return merged
    except json.JSONDecodeError as e:
        print(f"  ❌ Merge JSON-parsefout: {e}")
        return all_patterns


# ---------------------------------------------------------------------------
# Opslaan
# ---------------------------------------------------------------------------

def save_pattern(pattern: dict):
    """Sla één patroon op als JSON-bestand."""
    pid = pattern.get("id", "patroon:onbekend")
    slug = pid.replace("patroon:", "")
    path = PATTERNS_DIR / f"{slug}.json"
    path.write_text(json.dumps(pattern, ensure_ascii=False, indent=2))
    return path


def load_existing_patterns() -> list[dict]:
    """Laad alle bestaande patroon-JSON-bestanden."""
    patterns = []
    for f in sorted(PATTERNS_DIR.glob("*.json")):
        try:
            patterns.append(json.loads(f.read_text()))
        except Exception as e:
            print(f"  ⚠️  Fout bij laden {f.name}: {e}")
    return patterns


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Extraheer ITAA-examenpatronen")
    parser.add_argument("--exam", help="Specifieke PDF-bestandsnaam (bv. 2013-1.pdf)")
    parser.add_argument("--merge-only", action="store_true",
                        help="Herconsolideer bestaande patronen zonder nieuwe PDFs te lezen")
    parser.add_argument("--no-merge", action="store_true",
                        help="Sla per-examen resultaten op zonder consolidatie")
    args = parser.parse_args()

    client = anthropic.Anthropic()
    PATTERNS_DIR.mkdir(parents=True, exist_ok=True)

    if args.merge_only:
        existing = load_existing_patterns()
        if not existing:
            print("Geen bestaande patronen gevonden.")
            return
        merged = merge_patterns(existing, client)
        # Wis oude bestanden
        for f in PATTERNS_DIR.glob("*.json"):
            f.unlink()
        for p in merged:
            path = save_pattern(p)
            print(f"  ✓ {path.name}")
        print(f"\n✓ {len(merged)} patronen geconsolideerd.")
        return

    # Selecteer PDFs
    if args.exam:
        pdfs = [EXAMS_DIR / args.exam]
        if not pdfs[0].exists():
            print(f"❌ Bestand niet gevonden: {pdfs[0]}")
            sys.exit(1)
    else:
        pdfs = sorted(EXAMS_DIR.glob("*.pdf"))

    if not pdfs:
        print("Geen PDF's gevonden in", EXAMS_DIR)
        sys.exit(1)

    # Extraheer per examen
    all_patterns = []
    for pdf in pdfs:
        print(f"\n{'='*60}")
        print(f"Examen: {pdf.name}")
        patterns = extract_patterns_from_exam(pdf, client)
        all_patterns.extend(patterns)

        if args.no_merge:
            for p in patterns:
                # Voeg examen-suffix toe aan ID om conflicten te vermijden
                exam_slug = re.sub(r"[^a-z0-9]", "-", pdf.stem.lower()).strip("-")
                p["id"] = p["id"] + f"--{exam_slug}"
                path = save_pattern(p)
                print(f"  → {path.name}")

    if args.no_merge:
        print(f"\n✓ Klaar — {len(all_patterns)} patronen (niet geconsolideerd).")
        return

    # Consolideer
    if len(pdfs) > 1 or load_existing_patterns():
        # Voeg bestaande patronen toe voor volledige consolidatie
        existing = load_existing_patterns()
        existing_ids = {p.get("id") for p in existing}
        new_only = [p for p in all_patterns if p.get("id") not in existing_ids]
        to_merge = existing + new_only if existing else all_patterns
        merged = merge_patterns(to_merge, client)
    else:
        merged = all_patterns

    # Wis oude bestanden en schrijf nieuw
    for f in PATTERNS_DIR.glob("*.json"):
        f.unlink()
    for p in merged:
        path = save_pattern(p)
        print(f"  ✓ {path.name}")

    print(f"\n✓ Klaar — {len(merged)} geconsolideerde patronen in {PATTERNS_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
