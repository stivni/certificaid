"""
Genereer chunk-level semantische keywords voor wetteksten (ADR-004).

Per artikel-chunk worden 5–10 Nederlandstalige juridische keywords gegenereerd
via Claude en opgeslagen in resources/bronnen/wetteksten/keywords/NAAM.json.
Tijdens indexering (rag_index.py) worden deze keywords aan de chunk-tekst prepended
zodat de bge-m3 embedding de semantische context meeneemt.

Gebruik:
  python tools/generate_keywords.py                        # alle wetteksten
  python tools/generate_keywords.py --source Antiwitwaswet-2017
  python tools/generate_keywords.py --priority             # AWW, WIB92, WBTW, WVV, Wet-ITAA, WER
  python tools/generate_keywords.py --dry-run              # toon zonder API-calls
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import frontmatter

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "tools"))

KEYWORDS_DIR = ROOT / "resources" / "bronnen" / "wetteksten" / "keywords"
WETTEKSTEN_DIR = ROOT / "resources" / "bronnen" / "wetteksten"

# Wetteksten die het meest bevraagd worden op het examen — eerst genereren
PRIORITY_SOURCES = [
    "Antiwitwaswet-2017",
    "WIB92",
    "WBTW",
    "WVV",
    "Wet-ITAA-2019",
    "WER",
    "KB-WVV-2019",
    "KB-21-10-2018",
    "Wetboek-Invordering",
    "WDRT",
]

SYSTEM_PROMPT = """Je bent een juridische taxonomie-expert voor Belgisch recht en accountancy.
Genereer voor elk wetsartikel een compacte lijst van 5–10 Nederlandstalige keywords.

Regels:
- Keywords zijn juridische en boekhoudkundige termen die studenten gebruiken om dit artikel op te zoeken
- Gebruik termen uit de tekst zelf + synoniemen + gerelateerde concepten
- Geen volledige zinnen, alleen losse termen of korte woordgroepen (max 3 woorden)
- Schrijf in het Nederlands (geen Engels tenzij de wet zelf Engels gebruikt)
- Vermeld ook de naam van de wet als keyword als die niet duidelijk is uit de context

Formaat: JSON-object met als key de artikel-heading en als value een array van strings.
Voorbeeld:
{
  "Art. 47": ["meldingsplicht", "CFI", "vermoeden witwassen", "antiwitwaswetgeving", "melding", "onderworpen entiteit", "terrorismefinanciering"],
  "Art. 48": ["tipping-off verbod", "mededeling", "meldingsplicht", "witwassen", "geheimhouding"]
}"""


def _chunk_wettekst(path: Path) -> list[dict]:
    """Splits een wettekst-bestand in artikel-chunks (zelfde logica als rag_index.py)."""
    import re

    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        print(f"  ⚠️  Kon {path.name} niet laden: {e}")
        return []

    content = post.content
    chunks = []
    current_heading = ""
    current_lines = []

    for line in content.split("\n"):
        if re.match(r"^#{1,4} ", line):
            if current_lines and current_heading:
                body = "\n".join(current_lines).strip()
                if len(body) >= 80:
                    chunks.append({"heading": current_heading, "body": body[:600]})
            stripped = line.lstrip("#").strip()
            # Sla structurele headings over (BOEK/TITEL/etc.)
            if re.match(r"^(HOOFDSTUK|AFDELING|TITEL|DEEL|BOEK|SECTIE)", stripped, re.I):
                current_heading = ""
            else:
                current_heading = stripped
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines and current_heading:
        body = "\n".join(current_lines).strip()
        if len(body) >= 80:
            chunks.append({"heading": current_heading, "body": body[:600]})

    return chunks


def generate_keywords_for_file(
    path: Path,
    client,
    dry_run: bool = False,
    batch_size: int = 15,
) -> dict:
    """Genereer keywords voor alle chunks in één wettekst-bestand."""
    chunks = _chunk_wettekst(path)
    if not chunks:
        print(f"  Geen chunks gevonden in {path.name}")
        return {}

    print(f"  {len(chunks)} chunks → {(len(chunks) + batch_size - 1) // batch_size} API-calls")

    if dry_run:
        return {c["heading"]: [f"[dry-run] {c['heading'][:20]}"] for c in chunks}

    keywords_map = {}
    batches = [chunks[i:i+batch_size] for i in range(0, len(chunks), batch_size)]

    for batch_idx, batch in enumerate(batches):
        # Bouw prompt op voor deze batch
        batch_text = "\n\n".join(
            f"Heading: {c['heading']}\nTekst: {c['body']}"
            for c in batch
        )
        prompt = f"""Genereer keywords voor de volgende {len(batch)} wetsartikelen uit '{path.stem}'.
Geef een JSON-object terug met als keys de headings en als values arrays van keywords.

{batch_text}

JSON:"""

        try:
            response = client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=1500,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            raw = response.content[0].text.strip()

            # Extraheer JSON uit de response
            import re
            json_match = re.search(r"\{.*\}", raw, re.DOTALL)
            if json_match:
                batch_keywords = json.loads(json_match.group())
                keywords_map.update(batch_keywords)
            else:
                print(f"  ⚠️  Geen JSON gevonden in batch {batch_idx+1}")

        except Exception as e:
            print(f"  ⚠️  API-fout batch {batch_idx+1}: {e}")

        # Rate limiting: korte pauze tussen batches
        if batch_idx < len(batches) - 1:
            time.sleep(0.5)

    return keywords_map


def save_keywords(stem: str, keywords_map: dict) -> Path:
    """Sla keywords op als JSON in de keywords-map."""
    KEYWORDS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = KEYWORDS_DIR / f"{stem}.json"
    out_path.write_text(json.dumps(keywords_map, ensure_ascii=False, indent=2))
    return out_path


def load_existing(stem: str) -> dict:
    """Laad bestaand keywords-bestand als dat er al is."""
    path = KEYWORDS_DIR / f"{stem}.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}


def main():
    parser = argparse.ArgumentParser(description="Genereer chunk-level keywords voor wetteksten")
    parser.add_argument("--source", help="Naam van één wettekst (stem, zonder .md)")
    parser.add_argument("--priority", action="store_true", help="Verwerk alleen prioritaire wetteksten")
    parser.add_argument("--force", action="store_true", help="Overschrijf bestaande keywords-bestanden")
    parser.add_argument("--dry-run", action="store_true", help="Geen API-calls, toon alleen chunk-aantallen")
    parser.add_argument("--batch-size", type=int, default=15, help="Aantal chunks per API-call (default: 15)")
    args = parser.parse_args()

    # Bepaal welke bestanden verwerkt worden
    if args.source:
        files = [WETTEKSTEN_DIR / f"{args.source}.md"]
        if not files[0].exists():
            print(f"❌ {files[0]} niet gevonden")
            sys.exit(1)
    elif args.priority:
        files = [WETTEKSTEN_DIR / f"{s}.md" for s in PRIORITY_SOURCES
                 if (WETTEKSTEN_DIR / f"{s}.md").exists()]
    else:
        files = sorted(f for f in WETTEKSTEN_DIR.glob("*.md")
                      if "INDEX" not in f.name and "compilatie" not in f.name.lower())

    # Filter al-verwerkte bestanden (tenzij --force)
    if not args.force and not args.dry_run:
        to_process = [f for f in files if not (KEYWORDS_DIR / f"{f.stem}.json").exists()]
        skipped = len(files) - len(to_process)
        if skipped:
            print(f"  {skipped} bestanden al verwerkt (gebruik --force om te overschrijven)")
        files = to_process

    if not files:
        print("✓ Alle bestanden al verwerkt.")
        return

    print(f"Te verwerken: {len(files)} wetteksten\n")

    # Laad Claude client (niet nodig bij dry-run)
    client = None
    if not args.dry_run:
        try:
            import anthropic
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                # Probeer .env te laden
                env_file = ROOT / ".env"
                if env_file.exists():
                    for line in env_file.read_text().splitlines():
                        if line.strip() and not line.startswith("#") and "=" in line:
                            k, v = line.split("=", 1)
                            os.environ[k.strip()] = v.strip()
                api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                print("❌ ANTHROPIC_API_KEY niet ingesteld.")
                sys.exit(1)
            client = anthropic.Anthropic(api_key=api_key)
        except ImportError:
            print("❌ anthropic package niet geïnstalleerd: pip3 install anthropic")
            sys.exit(1)

    # Verwerk bestanden
    total_chunks = 0
    for path in files:
        print(f"\n{'='*55}")
        print(f"Verwerk: {path.stem}")
        kw = generate_keywords_for_file(path, client, args.dry_run, args.batch_size)
        if kw:
            out = save_keywords(path.stem, kw)
            total_chunks += len(kw)
            print(f"  ✓ {len(kw)} artikel-keywords → {out.relative_to(ROOT)}")

    print(f"\n✓ Klaar — {total_chunks} artikel-keywords gegenereerd voor {len(files)} wetteksten.")
    print(f"  Keywords worden automatisch gebruikt bij de volgende rag_index.py run.")


if __name__ == "__main__":
    main()
