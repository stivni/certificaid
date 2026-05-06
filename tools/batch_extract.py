"""
Batch concept extractor: verwerkt alle concepten van één of meer PO's.

Leest de TDKs uit de PO-fiches en roept concept_extractor aan per concept.
Slaat voortgang op zodat je kunt hervatten bij onderbreking.

Gebruik:
  python tools/batch_extract.py --po 4.0
  python tools/batch_extract.py --po 2.4 --resume      # hervat na onderbreking
  python tools/batch_extract.py --po 2.4 --dry-run     # toon wat er geëxtraheerd zou worden
  python tools/batch_extract.py --po all               # alle PO's
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime

import frontmatter

ROOT = Path(__file__).parent.parent
PO_DIR = ROOT / "content" / "programmaonderdelen"
OUTPUT_DIR = ROOT / "data" / "concept_records"
PROGRESS_DIR = ROOT / "data"

sys.path.insert(0, str(ROOT / "tools"))
from concept_extractor import extract_concept, save_record


# ---------------------------------------------------------------------------
# TDK-parsing uit PO-fiches
# ---------------------------------------------------------------------------

def parse_tdk_concepts(po_path: Path) -> list[dict]:
    """
    Extraheer kandidaat-concepten uit een PO-fiche.
    Zoekt naar:
    1. Wikilinks in Kenniselementen: [[concept-naam|Beschrijving]]
    2. Items gemarkeerd als ⚠️ materie aan te maken
    3. Alle ## en ### headings in de Kenniselementen-sectie
    """
    try:
        post = frontmatter.load(str(po_path))
    except Exception as e:
        print(f"  ⚠️  Kon {po_path.name} niet laden: {e}")
        return []

    fm = post.metadata
    po_tags = fm.get("tags", [])
    po_nr = next((t for t in po_tags if re.match(r"\d+\.\d+", str(t))), po_path.stem)

    content = post.content
    concepts = []
    seen = set()

    # --- Methode 1: wikilinks in de content ---
    # Patroon: [[concept-naam|Beschrijving]] of [[concept-naam]]
    wikilink_re = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?\|?([^\]]*)\]\]")
    for m in wikilink_re.finditer(content):
        slug = m.group(1).strip()
        label = m.group(2).strip() or slug
        # Enkel materie-fiches (geen competenties, geen wetteksten)
        if any(skip in slug for skip in ["wetteksten/", "bronnen/", "competentie"]):
            continue
        if slug in seen:
            continue
        seen.add(slug)
        concepts.append({
            "id": slug,
            "naam": label or slug,
            "tdk_tekst": label,
            "po_nr": str(po_nr),
        })

    # --- Methode 2: kenniselement-teksten (items zonder link) ---
    ke_section = _extract_section(content, "Kenniselementen")
    if ke_section:
        # Regels van de stijl: "- I.A — Naam concept" of "- I.A — [[link|Naam]]"
        ke_item_re = re.compile(r"^[-*]\s+(?:[IVX]+\.[A-Z0-9]+\s*—\s*)?(.+)$", re.MULTILINE)
        for m in ke_item_re.finditer(ke_section):
            tekst = m.group(1).strip()
            # Verwijder markdown opmaak
            tekst_clean = re.sub(r"\[!\w+\].*", "", tekst)
            tekst_clean = re.sub(r"\[\[.*?\]\]", "", tekst_clean).strip()
            tekst_clean = re.sub(r"\*(⚠️.*?)\*", "", tekst_clean).strip()
            if len(tekst_clean) < 5 or "⚠️" in tekst_clean:
                continue
            # Geen duplicaten op basis van eerste woorden
            key = tekst_clean[:30].lower()
            if key in seen:
                continue
            seen.add(key)
            concepts.append({
                "id": _slugify(tekst_clean),
                "naam": tekst_clean[:60],
                "tdk_tekst": tekst_clean,
                "po_nr": str(po_nr),
            })

    return concepts


def _extract_section(content: str, section_name: str) -> str | None:
    """Extraheer de inhoud van een ## sectie op naam."""
    pattern = re.compile(
        rf"^#{{{1,3}}}\s+{re.escape(section_name)}.*?$(.+?)(?=^#{{{1,3}}}\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(content)
    return m.group(1) if m else None


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60]


# ---------------------------------------------------------------------------
# Voortgang bijhouden
# ---------------------------------------------------------------------------

def load_progress(po_nr: str) -> dict:
    path = PROGRESS_DIR / f"batch-progress-{po_nr}.json"
    if path.exists():
        return json.loads(path.read_text())
    return {"done": [], "failed": []}


def save_progress(po_nr: str, progress: dict):
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    path = PROGRESS_DIR / f"batch-progress-{po_nr}.json"
    progress["updated"] = datetime.now().isoformat()
    path.write_text(json.dumps(progress, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# Batch runner
# ---------------------------------------------------------------------------

def get_po_files(po_nr: str) -> list[Path]:
    if po_nr == "all":
        return sorted(PO_DIR.glob("*.md"))
    # Zoek bestand dat begint met PO-nummer
    matches = list(PO_DIR.glob(f"{po_nr}*.md")) or list(PO_DIR.glob(f"*{po_nr}*.md"))
    if not matches:
        print(f"❌ Geen PO-fiche gevonden voor '{po_nr}' in {PO_DIR}")
        sys.exit(1)
    return matches


def run_batch(po_nr: str, resume: bool = False, dry_run: bool = False,
              max_concepts: int | None = None):
    po_files = get_po_files(po_nr)
    print(f"PO-fiches: {[f.name for f in po_files]}")

    # Verzamel alle concepten
    all_concepts = []
    for po_file in po_files:
        concepts = parse_tdk_concepts(po_file)
        all_concepts.extend(concepts)
        print(f"  {po_file.name}: {len(concepts)} kandidaat-concepten")

    if not all_concepts:
        print("Geen concepten gevonden.")
        return

    # Dedupliceer op id
    seen_ids = set()
    unique_concepts = []
    for c in all_concepts:
        if c["id"] not in seen_ids:
            seen_ids.add(c["id"])
            unique_concepts.append(c)

    print(f"\nTotaal: {len(unique_concepts)} unieke concepten")

    if dry_run:
        print("\nDRY RUN — te extraheren concepten:")
        for i, c in enumerate(unique_concepts, 1):
            exists = (OUTPUT_DIR / f"{c['id']}.json").exists()
            mark = "✓" if exists else " "
            print(f"  [{mark}] {i:3d}. {c['id']} ({c['po_nr']})")
            print(f"       TDK: {c['tdk_tekst'][:70]}")
        return

    # Laad voortgang
    progress = load_progress(po_nr) if resume else {"done": [], "failed": []}

    if max_concepts:
        unique_concepts = unique_concepts[:max_concepts]

    for i, concept in enumerate(unique_concepts, 1):
        cid = concept["id"]

        if resume and cid in progress["done"]:
            print(f"  [{i}/{len(unique_concepts)}] Overgeslagen (al gedaan): {cid}")
            continue

        if (OUTPUT_DIR / f"{cid}.json").exists() and not resume:
            print(f"  [{i}/{len(unique_concepts)}] Overgeslagen (bestand bestaat): {cid}")
            continue

        print(f"\n  [{i}/{len(unique_concepts)}] Verwerk: {cid}")
        try:
            record = extract_concept(
                concept_naam=cid,
                po_nr=concept["po_nr"],
                tdk_tekst=concept["tdk_tekst"],
                dry_run=False,
            )
            if record:
                save_record(record, OUTPUT_DIR)
                progress["done"].append(cid)
            else:
                progress["failed"].append(cid)
        except KeyboardInterrupt:
            print("\n⚠️  Onderbroken. Voortgang opgeslagen.")
            save_progress(po_nr, progress)
            sys.exit(0)
        except Exception as e:
            print(f"  ❌ Fout bij {cid}: {e}")
            progress["failed"].append(cid)

        save_progress(po_nr, progress)

    print(f"\n✓ Batch klaar: {len(progress['done'])} gedaan, {len(progress['failed'])} mislukt")
    if progress["failed"]:
        print(f"  Mislukt: {progress['failed']}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch concept extractie per PO")
    parser.add_argument("--po", required=True,
                        help="PO-nummer (bv. '4.0', '2.4', of 'all')")
    parser.add_argument("--resume", action="store_true",
                        help="Hervat na onderbreking (sla al gedane concepten over)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Toon welke concepten geëxtraheerd zouden worden")
    parser.add_argument("--max", type=int, default=None,
                        help="Maximaal N concepten verwerken (voor testen)")
    args = parser.parse_args()

    run_batch(args.po, resume=args.resume, dry_run=args.dry_run, max_concepts=args.max)


if __name__ == "__main__":
    main()
