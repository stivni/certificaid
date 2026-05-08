#!/usr/bin/env python3
"""
Verwijder een bron én analyseer de volledige downstream impact.

De verwijderketen werkt in drie lagen — elke laag vereist menselijke/agent-review
vóór de volgende:

  Laag 1 — Bron zelf (dit script voert dit uit):
    a. ChromaDB-chunks  → verwijdert alle chunks waarvan 'bestand' == filename
    b. MD-bestand       → git rm (of gewone rm als niet getrackt)
    c. Raw-bronbestand  → rm van raw PDF/HTML (alleen met --ook-raw, alleen als uniek)
    d. source_config    → verwijdert de entry als die bron expliciet vermeld staat

  Laag 2 — Vermoedens (NIET automatisch — vereist agent-review):
    De retrieval-bestanden in data/extractie/*/retrieval/*.json bevatten
    vermoedens die gegrond zijn op chunks van deze bron. Dit script toont
    welke vermoedens getroffen worden, maar past ze NIET aan.
    → Review met: Claude Code Task + qa_subagent_prompt.md
    → Daarna: vermoedens herschrijven of alternatieve bron aanwijzen

  Laag 3 — Content-fiches (NIET automatisch — na Laag 2):
    Materie-/competentie-fiches die leunen op de getroffen vermoedens moeten
    herzien worden NADAT de vermoedens zijn bijgewerkt.
    Dit script toont welke content-pagina's mogelijk geraakt zijn (via
    de bron-referentie in /content/bronnen/), maar verwijdert ze NIET.
    → Handmatige review na Laag 2

Waarom niet automatisch?
  Stel bron X wordt verwijderd. Vermoeden V leunde op chunk X§3.
  Als er een alternatieve bron Y beschikbaar is die hetzelfde dekt, kan V
  gewoon herschreven worden met Y als grondslag. Als er geen alternatief is,
  moet V als 'onvoldoende gedekt' gemarkeerd worden of verwijderd worden.
  Dat onderscheid kan alleen een agent (of mens) maken.

Veiligheid:
  - --dry-run (default): toont de volledige impact zonder iets aan te raken.
  - Expliciet --execute vereist om Laag 1 daadwerkelijk uit te voeren.
  - Stopt met fout als trust-status 'trusted' is (gebruik --force).

Voorbeelden:

  # Impact-analyse (default dry-run):
  python tools/etl/remove_bron.py --bron ITAA-norm-X.md

  # Uitvoeren Laag 1 (bron + chunks):
  python tools/etl/remove_bron.py --bron ITAA-norm-X.md --execute [--ook-raw]

  # Legacy-bestand (rejected, geen chunks, geen vermoedens):
  python tools/etl/remove_bron.py --bron oud-bestand.md --force --execute
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}
CHROMA_PATH = ROOT / "data" / "chroma_db"
SOURCE_CONFIG = ROOT / "resources" / "source_config.yaml"
EXTRACTIE_DIR = ROOT / "data" / "extractie"
CONTENT_DIR = ROOT / "content"


# ─── Frontmatter-lezer ───────────────────────────────────────────────────────

_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _read_frontmatter_raw(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        return {}
    result: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


# ─── Bron-pad resolver ────────────────────────────────────────────────────────

def resolve_bron_path(arg: str) -> Path:
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


# ─── Laag 1: ChromaDB ────────────────────────────────────────────────────────

def _chroma_chunk_ids(bestandsnaam: str) -> list[str]:
    try:
        import chromadb  # type: ignore
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("bronnen")
        results = col.get(where={"bestand": bestandsnaam}, include=[])
        return results.get("ids", [])
    except Exception:
        return []


def _chroma_delete(ids: list[str]) -> int:
    try:
        import chromadb  # type: ignore
        client = chromadb.PersistentClient(path=str(CHROMA_PATH))
        col = client.get_collection("bronnen")
        col.delete(ids=ids)
        return len(ids)
    except Exception as exc:
        print(f"    WARN ChromaDB: {exc}")
        return 0


# ─── Laag 1: Raw-bestand ─────────────────────────────────────────────────────

def _raw_paths_for_bron(fm: dict[str, str]) -> list[Path]:
    paths: list[Path] = []
    for key in ("bron-pdf", "raw"):
        val = fm.get(key, "")
        if val and not val.startswith("http"):
            c = ROOT / val
            if c.exists():
                paths.append(c)
    return paths


def _raw_used_by_others(raw_path: Path, exclude: str) -> list[str]:
    rel = str(raw_path.relative_to(ROOT))
    users: list[str] = []
    for d in BRON_DIRS.values():
        for md in d.glob("*.md"):
            if md.name == exclude:
                continue
            if rel in md.read_text(encoding="utf-8") or raw_path.name in md.read_text():
                users.append(str(md.relative_to(ROOT)))
    return users


# ─── Laag 1: source_config ───────────────────────────────────────────────────

def _source_config_entry(bestandsnaam: str) -> bool:
    stem = Path(bestandsnaam).stem
    text = SOURCE_CONFIG.read_text(encoding="utf-8")
    return "output: resources/bronnen" in text and stem in text


# ─── Laag 1: git rm ──────────────────────────────────────────────────────────

def _git_rm(path: Path) -> str:
    result = subprocess.run(
        ["git", "rm", "-f", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    if result.returncode == 0:
        return "git rm OK"
    if path.exists():
        path.unlink()
        return "rm OK (niet getrackt)"
    return "FOUT: bestand niet gevonden"


# ─── Laag 2: Vermoedens-impact ───────────────────────────────────────────────

def _find_affected_vermoedens(bron_stem: str) -> list[dict]:
    """
    Doorzoek alle retrieval-JSON's op verwijzingen naar deze bron.
    Geeft een lijst van {taakblok, vermoeden_naam, n_chunks, chunk_ids}.
    """
    affected: list[dict] = []
    if not EXTRACTIE_DIR.exists():
        return affected

    for retrieval_file in sorted(EXTRACTIE_DIR.rglob("retrieval/*.json")):
        try:
            data = json.loads(retrieval_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        taakblok = data.get("taakblok", retrieval_file.stem)
        for v in data.get("vermoedens", []):
            naam = v.get("naam", "?")
            hits = [
                c["chunk_id"]
                for c in v.get("chunks", [])
                if c.get("bron", "") == bron_stem
                or c.get("chunk_id", "").startswith(bron_stem + "__")
            ]
            if hits:
                affected.append({
                    "taakblok": taakblok,
                    "vermoeden": naam,
                    "n_chunks": len(hits),
                    "chunk_ids": hits,
                    "retrieval_file": str(retrieval_file.relative_to(ROOT)),
                })
    return affected


# ─── Laag 3: Content-pagina's ────────────────────────────────────────────────

def _find_content_pages(bron_path: Path) -> list[Path]:
    """
    Zoek content-pagina's die direct naar deze bron verwijzen.
    Kijkt in content/bronnen/ naar een gelijknamige pagina.
    Zoekt NIET in materie-/competentie-fiches (die zijn via vermoedens gelinkt,
    niet direct — die horen in Laag 2).
    """
    pages: list[Path] = []
    stem = bron_path.stem
    for sub in ("wetteksten", "normen", "adviezen"):
        c = CONTENT_DIR / "bronnen" / sub / f"{stem}.md"
        if c.exists():
            pages.append(c)
    return pages


# ─── Hoofd-analyse ───────────────────────────────────────────────────────────

def analyse_one(path: Path) -> dict:
    """Volledige impact-analyse voor één bron. Raakt niets aan."""
    bestandsnaam = path.name
    bron_stem = path.stem
    fm = _read_frontmatter_raw(path)

    try:
        from tools.lib.provenance import read_trust  # noqa
        trust_status = read_trust(path).status
    except Exception:
        trust_status = fm.get("trust", {}) or "onbekend"

    chunk_ids = _chroma_chunk_ids(bestandsnaam)
    raw_paths = _raw_paths_for_bron(fm)
    vermoedens = _find_affected_vermoedens(bron_stem)
    content_pages = _find_content_pages(path)

    return {
        "bestand": str(path.relative_to(ROOT)),
        "bron_stem": bron_stem,
        "trust_status": trust_status,
        "fm": fm,
        # Laag 1
        "chunk_ids": chunk_ids,
        "raw_paths": raw_paths,
        "source_config_entry": _source_config_entry(bestandsnaam),
        # Laag 2
        "affected_vermoedens": vermoedens,
        # Laag 3
        "content_pages": content_pages,
    }


def execute_laag1(analyse: dict, *, ook_raw: bool, dry_run: bool) -> list[str]:
    """Voer Laag 1 uit: chunks + raw + MD. Geeft actielog terug."""
    log: list[str] = []
    bestandsnaam = Path(analyse["bestand"]).name

    # ChromaDB
    ids = analyse["chunk_ids"]
    if ids:
        log.append(f"ChromaDB: {len(ids)} chunk(s) verwijderen")
        if not dry_run:
            n = _chroma_delete(ids)
            log[-1] += f" → {n} verwijderd"
    else:
        log.append("ChromaDB: 0 chunks")

    # Raw-bestand
    for raw_path in analyse["raw_paths"]:
        others = _raw_used_by_others(raw_path, bestandsnaam)
        if others:
            log.append(f"Raw {raw_path.name}: ook gebruikt door {others} → overgeslagen")
        elif ook_raw:
            log.append(f"Raw {raw_path.name}: verwijderen")
            if not dry_run:
                raw_path.unlink(missing_ok=True)
                log[-1] += " → gedaan"
        else:
            log.append(f"Raw {raw_path.name}: gebruik --ook-raw om te verwijderen")

    # source_config
    if analyse["source_config_entry"]:
        log.append("source_config.yaml: entry aanwezig → handmatig verwijderen vereist")
    else:
        log.append("source_config.yaml: geen expliciete entry")

    # MD-bestand
    md_path = ROOT / analyse["bestand"]
    log.append(f"MD-bestand: {analyse['bestand']}")
    if not dry_run:
        resultaat = _git_rm(md_path)
        log[-1] += f" → {resultaat}"

    return log


# ─── Rapportering ─────────────────────────────────────────────────────────────

def print_rapport(analyse: dict, *, actielog: list[str], dry_run: bool) -> None:
    trust = analyse["trust_status"]
    print(f"\n{'─'*60}")
    print(f"  {Path(analyse['bestand']).name}  [trust: {trust}]")
    print(f"{'─'*60}")

    # Laag 1 — uitgevoerd of gepland
    print("\n  LAAG 1 — bron verwijderen (dit script):")
    prefix = "    [dry]" if dry_run else "    [✓]  "
    for actie in actielog:
        print(f"{prefix} {actie}")

    # Laag 2 — vermoedens (NOOIT automatisch)
    vermoedens = analyse["affected_vermoedens"]
    if vermoedens:
        print(f"\n  LAAG 2 — ⚠️  {len(vermoedens)} vermoeden(s) vereisen review:")
        print("    (NIET automatisch — run een agent-review vóór content aan te passen)")
        for v in vermoedens:
            print(f"    • [{v['taakblok']}] {v['vermoeden']}")
            print(f"        {v['n_chunks']} chunk(s): {', '.join(v['chunk_ids'][:2])}"
                  + ("..." if len(v['chunk_ids']) > 2 else ""))
            print(f"        in: {v['retrieval_file']}")
    else:
        print("\n  LAAG 2 — vermoedens: geen getroffen (0 retrieval-verwijzingen)")

    # Laag 3 — content-pagina's
    pages = analyse["content_pages"]
    if pages:
        print(f"\n  LAAG 3 — content-pagina's (pas aanpassen NA Laag 2-review):")
        for pg in pages:
            print(f"    • {pg.relative_to(ROOT)}")
    else:
        print("\n  LAAG 3 — content-pagina's: geen directe Quartz-bronpagina gevonden")


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--bron", nargs="+", required=True,
                   help="Één of meer bron-MD's (pad, relatief-to-root, of bestandsnaam)")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True,
                      help="Toon impact-analyse zonder iets aan te raken (default)")
    mode.add_argument("--execute", action="store_true",
                      help="Voer Laag 1 daadwerkelijk uit (chunks + MD verwijderen)")
    p.add_argument("--ook-raw", action="store_true",
                   help="(met --execute) verwijder ook het raw-bronbestand als het uniek is")
    p.add_argument("--force", action="store_true",
                   help="Sta verwijdering toe ook als trust-status 'trusted' is")
    args = p.parse_args()

    dry_run = not args.execute

    print(f"=== remove_bron {'(DRY-RUN)' if dry_run else '(EXECUTE — Laag 1)'} ===")
    if dry_run:
        print("   Toont impact-analyse. Gebruik --execute voor daadwerkelijke verwijdering.\n")

    blocked: list[str] = []

    for bron_arg in args.bron:
        try:
            path = resolve_bron_path(bron_arg)
        except SystemExit as exc:
            print(f"\n[SKIP] {bron_arg}: {exc}")
            continue

        analyse = analyse_one(path)

        # Veiligheidscheck
        if analyse["trust_status"] == "trusted" and not args.force:
            blocked.append(path.name)
            print(f"\n  ⛔ {path.name}: trust-status 'trusted' — gebruik --force")
            continue

        # Laag 1 uitvoeren (of dry-run)
        actielog = execute_laag1(analyse, ook_raw=args.ook_raw, dry_run=dry_run)
        print_rapport(analyse, actielog=actielog, dry_run=dry_run)

    # Afsluiting
    print(f"\n{'═'*60}")
    if blocked:
        print(f"⛔ Geblokkeerd (trusted, gebruik --force): {blocked}")

    if dry_run:
        print("→ Gebruik --execute om Laag 1 daadwerkelijk uit te voeren.")

    if not dry_run:
        print("\nVolgende stap — Laag 2:")
        print("  Als er vermoedens getroffen zijn: run een agent-review op de")
        print("  betrokken retrieval-bestanden vóór content aan te passen.")
        print("  Zie tools/etl/qa_subagent_prompt.md voor de review-instructies.")


if __name__ == "__main__":
    main()
