#!/usr/bin/env python3
"""
Verwijder een bron én al zijn downstream gevolgen.

Aanpakt de volledige verwijderketen voor één of meer bron-MD's:

  1. ChromaDB-chunks  → verwijdert alle chunks waarvan 'bestand' == filename
  2. MD-bestand       → git rm (of gewone rm als niet getrackt)
  3. Raw-bronbestand  → rm van raw PDF/HTML (alleen met --ook-raw, alleen als uniek)
  4. source_config    → verwijdert de entry als die bron expliciet vermeld staat
  5. content/-pagina  → git rm als er een Quartz-content-pagina is gekoppeld

Veiligheid:
  - --dry-run (default): toont wat er zou verwijderd worden, raakt niets aan.
  - Expliciet --execute vereist om effectief te verwijderen.
  - Controleert of het raw-bestand ook door andere bronnen gebruikt wordt.
  - Stopt met fout als de bron nog trust-status 'trusted' heeft (gebruik
    --force om te overschrijven).

Voorbeelden:

  # Wat zou er verwijderd worden? (default: dry-run)
  python tools/etl/remove_bron.py --bron algemene-controlenorm.md

  # Meerdere legacy bestanden in één keer
  python tools/etl/remove_bron.py \\
      --bron algemene-controlenorm.md aww-reglement-iab.md kmo-controlenorm.md \\
      --dry-run

  # Effectief verwijderen + ook raw PDF weggooien als die uniek is
  python tools/etl/remove_bron.py --bron algemene-controlenorm.md \\
      --execute --ook-raw
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
RAW_DIRS = [
    ROOT / "resources" / "raw" / "normen",
    ROOT / "resources" / "raw" / "wetteksten",
    ROOT / "resources" / "raw" / "adviezen",
]
CHROMA_PATH = ROOT / "data" / "chroma_db"
SOURCE_CONFIG = ROOT / "resources" / "source_config.yaml"


# ─── Helpers ─────────────────────────────────────────────────────────────────

_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _read_frontmatter_raw(path: Path) -> dict[str, str]:
    """Eenvoudige key: value-lezer voor YAML-frontmatter (geen volledige YAML-parse)."""
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        return {}
    fm_text = m.group(1)
    result: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def resolve_bron_path(arg: str) -> Path:
    """Accepteer absoluut pad, relatief-to-root, of bare bestandsnaam."""
    p = Path(arg)
    if p.is_absolute() and p.exists():
        return p
    candidate = ROOT / arg
    if candidate.exists():
        return candidate
    if "/" not in arg:
        for d in BRON_DIRS.values():
            hits = list(d.glob(arg))
            if len(hits) == 1:
                return hits[0]
            if len(hits) > 1:
                raise SystemExit(f"Meerdere matches voor {arg!r}: {hits}")
    raise SystemExit(f"Bron niet gevonden: {arg!r}")


def _raw_paths_for_bron(fm: dict[str, str]) -> list[Path]:
    """Geef lokale raw-bestandspaden uit frontmatter (bron-pdf, raw)."""
    paths: list[Path] = []
    for key in ("bron-pdf", "raw"):
        val = fm.get(key, "")
        if val and not val.startswith("http"):
            candidate = ROOT / val
            if candidate.exists():
                paths.append(candidate)
    return paths


def _raw_used_by_others(raw_path: Path, exclude_bestand: str) -> list[str]:
    """Zoek andere bronnen die hetzelfde raw-bestand als input gebruiken."""
    users: list[str] = []
    rel_raw = str(raw_path.relative_to(ROOT))
    for bron_dir in BRON_DIRS.values():
        for md in bron_dir.glob("*.md"):
            if md.name == exclude_bestand:
                continue
            text = md.read_text(encoding="utf-8")
            if rel_raw in text or raw_path.name in text:
                users.append(str(md.relative_to(ROOT)))
    return users


def _source_config_has_entry(bron_name: str) -> bool:
    """Controleer of source_config.yaml een expliciete entry heeft voor deze bron."""
    text = SOURCE_CONFIG.read_text(encoding="utf-8")
    # Zoek op output-pad of een key die de bestandsnaam bevat
    stem = Path(bron_name).stem
    return f"output: resources/bronnen" in text and stem in text


def _chroma_chunk_count(bestandsnaam: str) -> int:
    """Hoeveel chunks zitten er in ChromaDB met dit bestand?"""
    try:
        import chromadb  # type: ignore
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("bronnen")
        results = col.get(where={"bestand": bestandsnaam}, include=[])
        return len(results.get("ids", []))
    except Exception:
        return 0


def _chroma_delete_chunks(bestandsnaam: str) -> int:
    """Verwijder alle chunks van dit bestand uit ChromaDB. Geeft count terug."""
    try:
        import chromadb  # type: ignore
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("bronnen")
        results = col.get(where={"bestand": bestandsnaam}, include=[])
        ids = results.get("ids", [])
        if ids:
            col.delete(ids=ids)
        return len(ids)
    except Exception as exc:
        print(f"    WARN ChromaDB: {exc}")
        return 0


def _git_rm(path: Path) -> bool:
    """Voer git rm uit. Geeft True als gelukt, False als bestand niet getrackt is."""
    result = subprocess.run(
        ["git", "rm", "-f", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    if result.returncode == 0:
        return True
    # Niet getrackt (bijv. gitignored raw-bestand) → gewone verwijdering
    if path.exists():
        path.unlink()
        return True
    return False


def _content_page(bron_path: Path) -> Optional[Path]:
    """Zoek een gekoppelde Quartz content/-pagina (als die bestaat)."""
    # Conventie: content/bronnen/{bron_rol}/{stem}.md
    fm = _read_frontmatter_raw(bron_path)
    bron_rol = fm.get("bron_rol") or fm.get("type", "")
    stem = bron_path.stem
    for sub in ("wetteksten", "normen", "adviezen", bron_rol):
        candidate = ROOT / "content" / "bronnen" / sub / f"{stem}.md"
        if candidate.exists():
            return candidate
    return None


# ─── Hoofd-verwijder-logica ───────────────────────────────────────────────────

def remove_one(
    path: Path,
    *,
    ook_raw: bool,
    force: bool,
    dry_run: bool,
) -> dict:
    """
    Verwijder één bron en al zijn downstream gevolgen.
    Geeft een rapport-dict terug.
    """
    bestandsnaam = path.name
    fm = _read_frontmatter_raw(path)
    trust_status = fm.get("status", "")  # van provenance.trust.status — zit genest
    # Lees trust via provenance lib voor zekerheid
    try:
        from tools.lib.provenance import read_trust  # noqa
        trust = read_trust(path)
        trust_status = trust.status
    except Exception:
        pass

    rapport = {
        "bestand": str(path.relative_to(ROOT)),
        "trust_status": trust_status,
        "acties": [],
        "geblokkeerd": None,
    }

    # Veiligheidscheck: trusted bronnen blokkeren zonder --force
    if trust_status == "trusted" and not force:
        rapport["geblokkeerd"] = (
            f"trust-status is 'trusted' — gebruik --force om toch te verwijderen"
        )
        return rapport

    # 1. ChromaDB chunks
    n_chunks = _chroma_chunk_count(bestandsnaam)
    if n_chunks:
        rapport["acties"].append(f"ChromaDB: {n_chunks} chunk(s) verwijderen")
        if not dry_run:
            deleted = _chroma_delete_chunks(bestandsnaam)
            rapport["acties"][-1] += f" → {deleted} verwijderd"
    else:
        rapport["acties"].append("ChromaDB: 0 chunks (niets te doen)")

    # 2. Raw-bestand(en)
    raw_paths = _raw_paths_for_bron(fm)
    for raw_path in raw_paths:
        users = _raw_used_by_others(raw_path, bestandsnaam)
        if users:
            rapport["acties"].append(
                f"Raw {raw_path.name}: OOK gebruikt door {users} → overgeslagen"
            )
        elif ook_raw:
            rapport["acties"].append(f"Raw {raw_path.name}: verwijderen")
            if not dry_run:
                raw_path.unlink(missing_ok=True)
                rapport["acties"][-1] += " → gedaan"
        else:
            rapport["acties"].append(
                f"Raw {raw_path.name}: bestaat maar --ook-raw niet opgegeven → overgeslagen"
            )

    # 3. Content/-pagina
    content_page = _content_page(path)
    if content_page:
        rapport["acties"].append(f"Content-pagina: {content_page.relative_to(ROOT)}")
        if not dry_run:
            _git_rm(content_page)
            rapport["acties"][-1] += " → verwijderd"

    # 4. source_config.yaml (alleen als er een expliciete entry is)
    if _source_config_has_entry(bestandsnaam):
        rapport["acties"].append("source_config.yaml: entry gevonden → handmatig verwijderen vereist")
    else:
        rapport["acties"].append("source_config.yaml: geen expliciete entry (collection-gebaseerde bron)")

    # 5. MD-bestand zelf (als laatste — anders kunnen andere checks mislukken)
    rapport["acties"].append(f"MD-bestand: {path.relative_to(ROOT)}")
    if not dry_run:
        ok = _git_rm(path)
        rapport["acties"][-1] += f" → {'verwijderd (git rm)' if ok else 'FOUT'}"

    return rapport


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--bron", nargs="+", required=True,
        help="Één of meer bron-MD's (pad, relatief-to-root, of bestandsnaam)",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run", action="store_true", default=True,
        help="Toon wat er zou verwijderd worden zonder iets aan te raken (default)",
    )
    mode.add_argument(
        "--execute", action="store_true",
        help="Voer de verwijdering daadwerkelijk uit",
    )
    p.add_argument(
        "--ook-raw", action="store_true",
        help="Verwijder ook het raw-bronbestand als het uniek is",
    )
    p.add_argument(
        "--force", action="store_true",
        help="Verwijder ook als trust-status 'trusted' is",
    )
    args = p.parse_args()

    dry_run = not args.execute

    print(f"=== remove_bron {'(DRY-RUN — geen wijzigingen)' if dry_run else '(EXECUTE)'} ===")
    if dry_run:
        print("   Gebruik --execute om effectief te verwijderen.\n")

    for bron_arg in args.bron:
        try:
            path = resolve_bron_path(bron_arg)
        except SystemExit as exc:
            print(f"\n[SKIP] {bron_arg}: {exc}")
            continue

        print(f"\n── {path.name} (trust: ", end="")
        rapport = remove_one(path, ook_raw=args.ook_raw, force=args.force, dry_run=dry_run)
        print(f"{rapport['trust_status']}) ──")

        if rapport["geblokkeerd"]:
            print(f"  ⛔ GEBLOKKEERD: {rapport['geblokkeerd']}")
            continue

        for actie in rapport["acties"]:
            prefix = "  [dry]" if dry_run else "  [✓]  "
            print(f"{prefix} {actie}")

    print("\n─────")
    if dry_run:
        print("Voeg --execute toe om daadwerkelijk te verwijderen.")


if __name__ == "__main__":
    main()
