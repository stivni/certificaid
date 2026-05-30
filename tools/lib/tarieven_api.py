"""
Centrale tarieven-API voor Certificaid tarief-records (ADR-026).

Enige toegestane interface voor mutaties aan data/tarieven/records/*.json.
Schrijft atomair naar disk + rendert content/tarieven/<id>.md.

In tegenstelling tot records_api (concepten) is er GEEN RAG-parity: de
certificaid-tarieven MCP-server leest direct van disk en gebruikt text-match.
Geen daemon-afhankelijkheid, geen embedding-stap.

Operaties:
  save_record(record_dict, trusted=False)
    Valideert tegen schema, schrijft JSON, rendert markdown.
  mark_trusted(record_id, trusted_by=None)
    Vlagt record als trusted (verified door verify-pass).
  audit_parity()
    Sanity-check: matchen disk-records met rendered content-fiches?
  load_record(record_id)
    Read-helper (zonder mutatie).

CLI:
  python3 -m tools.lib.tarieven_api audit
  python3 -m tools.lib.tarieven_api render-all
  python3 -m tools.lib.tarieven_api list
  python3 -m tools.lib.tarieven_api show <record_id>
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import date
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "tarieven" / "records"
CONTENT_DIR = ROOT / "content" / "tarieven"
SCHEMA_PATH = ROOT / "data" / "tarieven" / "schema.json"

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


# ---------------------------------------------------------------------------
# Uitzonderingen
# ---------------------------------------------------------------------------

class TariefValidationError(ValueError):
    """Record voldoet niet aan schema of slug-conventie."""


class TariefRecordNotFoundError(KeyError):
    """Record bestaat niet op disk."""


# ---------------------------------------------------------------------------
# Schema-validatie (lightweight — vermijd jsonschema-dep als die ontbreekt)
# ---------------------------------------------------------------------------

def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _valideer(record: dict) -> None:
    """Lightweight valideren — checkt verplichte velden, slug, categorie, confidence.

    Volledige JSON-schema-validatie kan via `jsonschema` package; bewust niet
    geforceerd als dep zodat de API in minimal-env werkt. Strict-mode kan later
    achter een flag.
    """
    if not isinstance(record, dict):
        raise TariefValidationError("Record moet een dict zijn")

    schema = _load_schema()
    required = schema["required"]
    missing = [k for k in required if k not in record]
    if missing:
        raise TariefValidationError(f"Verplichte velden ontbreken: {missing}")

    record_id = record["id"]
    if not isinstance(record_id, str) or not SLUG_RE.match(record_id):
        raise TariefValidationError(
            f"Ongeldige id '{record_id}' — moet kebab-case zijn (a-z0-9-)"
        )

    if record["schema_version"] != "1.0":
        raise TariefValidationError(
            f"schema_version moet '1.0' zijn, kreeg '{record['schema_version']}'"
        )

    cats = schema["properties"]["categorie"]["enum"]
    if record["categorie"] not in cats:
        raise TariefValidationError(
            f"categorie '{record['categorie']}' niet in {cats}"
        )

    conf = schema["properties"]["confidence"]["enum"]
    if record["confidence"] not in conf:
        raise TariefValidationError(
            f"confidence '{record['confidence']}' niet in {conf}"
        )

    wetsbasis = record["wetsbasis"]
    if not isinstance(wetsbasis, list) or not wetsbasis:
        raise TariefValidationError("wetsbasis moet niet-lege lijst zijn")
    for entry in wetsbasis:
        if not isinstance(entry, dict) or "bron" not in entry or "artikel" not in entry:
            raise TariefValidationError(
                f"Elke wetsbasis-entry moet {{bron, artikel}} zijn, kreeg {entry}"
            )

    criteria = record["criteria"]
    if not isinstance(criteria, list) or not criteria:
        raise TariefValidationError("criteria moet niet-lege lijst zijn")
    for c in criteria:
        if "naam" not in c:
            raise TariefValidationError(f"criterium mist 'naam': {c}")


# ---------------------------------------------------------------------------
# IO-helpers
# ---------------------------------------------------------------------------

def _record_pad(record_id: str) -> Path:
    return RECORDS_DIR / f"{record_id}.json"


def _content_pad(record_id: str) -> Path:
    return CONTENT_DIR / f"{record_id}.md"


def load_record(record_id: str) -> dict:
    pad = _record_pad(record_id)
    if not pad.exists():
        raise TariefRecordNotFoundError(record_id)
    return json.loads(pad.read_text(encoding="utf-8"))


def lijst_record_ids() -> list[str]:
    if not RECORDS_DIR.exists():
        return []
    return sorted(p.stem for p in RECORDS_DIR.glob("*.json"))


# ---------------------------------------------------------------------------
# Render — JSON → Quartz-markdown
# ---------------------------------------------------------------------------

def _format_bedrag(waarde, eenheid: str | None) -> str:
    """Formatteer een numerieke waarde + eenheid leesbaar."""
    if waarde is None:
        return "—"
    if isinstance(waarde, str):
        return waarde
    if isinstance(waarde, (int, float)):
        if eenheid == "EUR":
            return f"€ {waarde:,.0f}".replace(",", ".")
        if eenheid == "%":
            return f"{waarde}%"
        if eenheid == "personen":
            return f"{waarde:,}".replace(",", ".")
        return f"{waarde:,}".replace(",", ".")
    return str(waarde)


def render_markdown(record: dict) -> str:
    """Render record als Quartz-markdown."""
    titel = record["titel"]
    samenvatting = record["samenvatting"]
    tags = ["tarief-record"] + list(record.get("tags", []))
    categorie = record["categorie"]

    geldigheid = record.get("geldigheidsperiode") or {}
    vanaf = geldigheid.get("vanaf_boekjaar")
    tot = geldigheid.get("tot_boekjaar")
    wijziging = geldigheid.get("wijziging_door")
    if vanaf and tot:
        periode = f"Boekjaar {vanaf} t.e.m. {tot}"
    elif vanaf:
        periode = f"Vanaf boekjaar {vanaf}"
    else:
        periode = ""

    wetsbasis_str = ", ".join(
        f"{w['bron']} art. {w['artikel']}" for w in record["wetsbasis"]
    )

    bron = record["bron"]
    confidence = record["confidence"]
    metadata = record.get("metadata", {})
    trusted = metadata.get("trusted", False)
    trusted_str = "✓ trusted" if trusted else "draft"

    # Criteria-tabel
    crit_lines = ["| Criterium | Waarde |", "|---|---|"]
    for c in record["criteria"]:
        naam = c["naam"]
        if "tarief_pct" in c and c.get("tarief_pct") is not None:
            extra = []
            if c.get("ondergrens") is not None or c.get("bovengrens") is not None:
                og = _format_bedrag(c.get("ondergrens"), "EUR")
                bg = _format_bedrag(c.get("bovengrens"), "EUR") if c.get("bovengrens") is not None else "—"
                extra.append(f"{og} – {bg}")
            extra.append(f"tarief **{c['tarief_pct']}%**")
            waarde_str = " · ".join(extra)
        else:
            waarde_str = _format_bedrag(c.get("waarde"), c.get("eenheid"))
            if c.get("eenheid") and not isinstance(c.get("waarde"), str):
                pass  # eenheid al in format
        if c.get("toelichting"):
            waarde_str += f" — {c['toelichting']}"
        crit_lines.append(f"| {naam} | {waarde_str} |")
    crit_tabel = "\n".join(crit_lines)

    drempel_regel = record.get("drempel_regel", "")

    # Context-tabellen wikilinks
    context_links = ""
    if record.get("context_tabellen"):
        items = "\n".join(f"- [[tarieven/{cid}]]" for cid in record["context_tabellen"])
        context_links = f"\n## Verwante tabellen\n\n{items}\n"

    # Bron-blok
    bron_lines = [f"- **Primaire bron**: {bron['primair']}"]
    if bron.get("wettekst"):
        bron_lines.append(f"- **Wettekst**: {bron['wettekst']}")
    if bron.get("cijferzakboekje_pagina") is not None:
        bron_lines.append(f"- **Cijferzakboekje 2026**: p{bron['cijferzakboekje_pagina']}")
    if bron.get("verified_via"):
        bron_lines.append(f"- **Geverifieerd via**: {bron['verified_via']}")
    bron_blok = "\n".join(bron_lines)

    tags_yaml = "\n".join(f"  - {t}" for t in tags)

    frontmatter = (
        f"---\n"
        f"title: \"{titel}\"\n"
        f"description: \"{samenvatting}\"\n"
        f"tags:\n{tags_yaml}\n"
        f"---\n"
    )

    body = f"""
> **Tarief-record** — `{record['id']}` · {confidence} · {trusted_str}

{samenvatting}

## Cijfers

{crit_tabel}
"""
    if drempel_regel:
        body += f"\n**Toepassingsregel**: {drempel_regel}\n"

    body += f"""
## Wettelijke basis

{wetsbasis_str}
"""
    if periode:
        body += f"\n**Geldigheid**: {periode}"
        if wijziging:
            body += f" · gewijzigd door {wijziging}"
        body += "\n"

    body += f"""
## Bron

{bron_blok}
{context_links}
---

*Tarief-record schema 1.0 ([ADR-026](../../docs/adr/ADR-026-tarief-extractie-pijplijn.md)). Categorie: {categorie}.*
"""

    return frontmatter + body


# ---------------------------------------------------------------------------
# Schrijf-operaties
# ---------------------------------------------------------------------------

def save_record(record: dict, *, trusted: bool = False, trusted_by: Optional[str] = None) -> Path:
    """
    Valideer + schrijf record naar disk + render markdown.

    Atomisch contract:
      1. Validate schema
      2. Set metadata.created_at / updated_at + optioneel trusted-flag
      3. Write JSON (atomic via tmpfile rename)
      4. Render markdown

    Render-fout logt WARNING maar raiset niet (markdown is afgeleid).
    """
    _valideer(record)
    record_id = record["id"]
    pad = _record_pad(record_id)
    pad.parent.mkdir(parents=True, exist_ok=True)

    metadata = record.setdefault("metadata", {})
    today = date.today().isoformat()
    metadata.setdefault("created_at", today)
    if pad.exists():
        metadata["updated_at"] = today
    if trusted:
        metadata["trusted"] = True
        metadata["trusted_at"] = today
        if trusted_by:
            metadata["trusted_by"] = trusted_by

    # Atomic write
    tmp = pad.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(pad)
    logger.info("Wrote %s", pad)

    try:
        _render_to_disk(record)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Render-fout voor %s: %s — markdown niet bijgewerkt", record_id, exc)

    return pad


def _render_to_disk(record: dict) -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    md = render_markdown(record)
    pad = _content_pad(record["id"])
    pad.write_text(md, encoding="utf-8")


def mark_trusted(record_id: str, trusted_by: Optional[str] = None) -> Path:
    record = load_record(record_id)
    record.setdefault("metadata", {})
    record["metadata"]["trusted"] = True
    record["metadata"]["trusted_at"] = date.today().isoformat()
    if trusted_by:
        record["metadata"]["trusted_by"] = trusted_by
    return save_record(record)


def audit_parity() -> dict:
    """
    Disk-vs-content parity check.

    Returns: dict met:
      records: lijst van record-ids op disk
      content_present: ids met markdown
      content_ontbreekt: ids zonder markdown
      content_overbodig: markdown zonder bijhorend record
    """
    disk_ids = set(lijst_record_ids())
    content_ids = (
        {p.stem for p in CONTENT_DIR.glob("*.md")} if CONTENT_DIR.exists() else set()
    )
    return {
        "records_totaal": len(disk_ids),
        "content_aanwezig": sorted(disk_ids & content_ids),
        "content_ontbreekt": sorted(disk_ids - content_ids),
        "content_overbodig": sorted(content_ids - disk_ids),
    }


def render_all() -> int:
    """Rendert alle records opnieuw. Voor migraties of render-template-wijzigingen."""
    n = 0
    for rid in lijst_record_ids():
        record = load_record(rid)
        _render_to_disk(record)
        n += 1
    return n


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli() -> int:
    parser = argparse.ArgumentParser(description="Tarieven-API CLI (ADR-026)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("audit", help="Disk-content parity check")
    sub.add_parser("render-all", help="Render alle records opnieuw")
    sub.add_parser("list", help="Lijst alle record-ids")
    s_show = sub.add_parser("show", help="Toon één record")
    s_show.add_argument("record_id")
    s_save = sub.add_parser("save", help="Schrijf record uit JSON-bestand")
    s_save.add_argument("json_path")
    s_save.add_argument("--trusted", action="store_true")
    s_trust = sub.add_parser("trust", help="Mark trusted")
    s_trust.add_argument("record_id")
    s_trust.add_argument("--by", default=None)

    args = parser.parse_args()
    if args.cmd == "audit":
        print(json.dumps(audit_parity(), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "render-all":
        n = render_all()
        print(f"Re-rendered {n} records")
        return 0
    if args.cmd == "list":
        for rid in lijst_record_ids():
            print(rid)
        return 0
    if args.cmd == "show":
        print(json.dumps(load_record(args.record_id), indent=2, ensure_ascii=False))
        return 0
    if args.cmd == "save":
        data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
        pad = save_record(data, trusted=args.trusted)
        print(f"Saved {pad}")
        return 0
    if args.cmd == "trust":
        pad = mark_trusted(args.record_id, trusted_by=args.by)
        print(f"Marked trusted: {pad}")
        return 0
    return 1


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.exit(_cli())
