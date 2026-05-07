"""
Concept-extractor voor de Certificaid kennisbank (ADR-008).

Drie sub-commando's:

  vermoedensruimte
    Stap A: LLM genereert 8–25 concept-kandidaten per taakblok.
    Geen retrieval. Output: data/extractie/<po>/vermoedens/<taakblok>.json

  seed
    Stap B+C: multi-level retrieval + LLM-synthese → seed-records.
    Input: vermoedens-JSON van stap A.
    Output: data/concept_records/<id>.json (status: seed)

  verdiep
    Stap D: verdieping van een bestaand seed/partieel concept.
    Queries vanuit bestaande velden (naam, main_rule, edges).
    Output: bijgewerkt data/concept_records/<id>.json (status: partieel)

Gebruik:
  python tools/extractie/concept_extractor.py vermoedensruimte \\
      --programmaonderdeel data/programmaonderdelen/4.0-deontologie.json \\
      [--taakblok 4.0.D1.1]   # default: alle kern-taakblokken

  python tools/extractie/concept_extractor.py seed \\
      --vermoedens data/extractie/4.0/vermoedens/4.0.D1.1.json \\
      --programmaonderdeel data/programmaonderdelen/4.0-deontologie.json \\
      [--chroma data/chroma_db_4.0]   # default: data/chroma_db

  python tools/extractie/concept_extractor.py verdiep \\
      --concept beroepsgeheim-gecertificeerd-accountant \\
      [--chroma data/chroma_db_4.0]

  Voeg --dry-run toe om LLM-output te printen zonder op te slaan.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Laad .env als ANTHROPIC_API_KEY nog niet in de omgeving zit
def _laad_dotenv():
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    if env_path.exists() and not os.environ.get("ANTHROPIC_API_KEY"):
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

_laad_dotenv()

import anthropic

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from lib.retrieval import (
    build_retrieval_stack,
    open_collections,
    multi_query_retrieve,
    BRONNEN_COLS,
)

CLAUDE_MODEL   = "claude-sonnet-4-6"
CONCEPT_DIR    = ROOT / "data" / "concept_records"
EXTRACTIE_DIR  = ROOT / "data" / "extractie"
PROMPTS_DIR    = ROOT / "prompts"
SCHEMA_VERSION = "1.0"


# ---------------------------------------------------------------------------
# Helpers: programmaonderdeel-JSON lezen
# ---------------------------------------------------------------------------

def laad_programmaonderdeel(path: Path) -> dict:
    return json.loads(path.read_text())


def verzamel_kenniselementen(data: dict, alleen_deel1: bool = True) -> list[dict]:
    """Verzamel alle kenniselementen (incl. subitems) als platte lijst."""
    result = []
    for ke in data.get("kenniselementen", []):
        if alleen_deel1 and ke.get("deel") != 1:
            continue
        if "subitems" in ke:
            for sub in ke["subitems"]:
                result.append({"code": sub["code"], "tekst": sub["tekst"], "parent": ke["code"]})
        else:
            result.append({"code": ke["code"], "tekst": ke["tekst"], "parent": None})
    return result


def get_taakblok(data: dict, code: str) -> dict | None:
    for tb in data.get("taakblokken", []):
        if tb.get("code") == code:
            return tb
    return None


def kern_taakblokken(data: dict) -> list[str]:
    return data.get("scope", {}).get("kern_taakblokken", [])


def bestaande_concepten() -> list[str]:
    """Geef namen van bestaande concept-records (voor anti-duplicatie)."""
    if not CONCEPT_DIR.exists():
        return []
    namen = []
    for f in CONCEPT_DIR.glob("*.json"):
        try:
            rec = json.loads(f.read_text())
            if not rec.get("_provenance", {}).get("stale", False):
                namen.append(rec.get("naam", f.stem))
        except Exception:
            pass
    return namen


# ---------------------------------------------------------------------------
# Helpers: LLM-client
# ---------------------------------------------------------------------------

def llm_client() -> anthropic.Anthropic:
    return anthropic.Anthropic()


def llm_call(client: anthropic.Anthropic, system: str, user: str) -> str:
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return msg.content[0].text


def parse_json_response(text: str) -> dict | list:
    """Extraheer JSON uit LLM-response (ook als er proza omheen staat)."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"```(?:json)?\s*(\{[\s\S]*?\}|\[[\s\S]*?\])\s*```", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    raise ValueError(f"Kon geen JSON parsen uit LLM-response:\n{text[:500]}")


# ---------------------------------------------------------------------------
# Helpers: provenance
# ---------------------------------------------------------------------------

def _pipeline_version() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode().strip()
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode().strip()
        return sha + ("-dirty" if dirty else "")
    except Exception:
        return "unknown"


def maak_provenance(pipeline: str, inputs: list[dict] | None = None,
                    prompt_version: str = "v1") -> dict:
    return {
        "inputs": inputs or [],
        "tooling": {
            "pipeline": pipeline,
            "pipeline_version": _pipeline_version(),
            "model": CLAUDE_MODEL,
            "prompt_version": prompt_version,
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stale": False,
        "stale_reason": None,
    }


# ---------------------------------------------------------------------------
# SUB-COMMANDO A: vermoedensruimte
# ---------------------------------------------------------------------------

def _system_vermoedensruimte() -> str:
    p = PROMPTS_DIR / "vermoedensruimte-v1.md"
    return p.read_text() if p.exists() else "Genereer concept-kandidaten als JSON."


def build_vermoedensruimte_prompt(
    po_data: dict,
    taakblok: dict,
    kenniselementen: list[dict],
    bestaande: list[str],
) -> str:
    po_titel = po_data.get("titel", "")
    po_nr    = po_data.get("programmaonderdeel", "")

    taken_tekst = "\n".join(f"- {t['tekst']}" for t in taakblok.get("taken", []))
    doel_tekst  = "\n".join(f"- {d['tekst']}" for d in taakblok.get("doelstellingen", []))
    ke_tekst    = "\n".join(f"- [{ke['code']}] {ke['tekst']}" for ke in kenniselementen)
    bestaande_tekst = (
        "\n".join(f"- {n}" for n in bestaande[:40])
        if bestaande else "(nog geen concepten aangemaakt)"
    )

    return f"""## Programmaonderdeel {po_nr}: {po_titel}

## Taakblok {taakblok['code']}

### Taken
{taken_tekst}

### Doelstellingen
{doel_tekst}

### Relevante kenniselementen
{ke_tekst}

### Bestaande concepten (vermijd duplicaten)
{bestaande_tekst}

---

Genereer de vermoedensruimte voor dit taakblok als JSON."""


def cmd_vermoedensruimte(args):
    po_path = Path(args.programmaonderdeel)
    po_data = laad_programmaonderdeel(po_path)
    po_nr   = po_data.get("programmaonderdeel", po_path.stem)

    taakblok_codes = [args.taakblok] if args.taakblok else kern_taakblokken(po_data)
    if not taakblok_codes:
        print("Geen kern_taakblokken gevonden. Gebruik --taakblok.")
        sys.exit(1)

    kenniselementen = verzamel_kenniselementen(po_data, alleen_deel1=True)
    bestaande = bestaande_concepten()
    client = llm_client()
    system = _system_vermoedensruimte()

    output_dir = EXTRACTIE_DIR / po_nr / "vermoedens"
    output_dir.mkdir(parents=True, exist_ok=True)

    for code in taakblok_codes:
        tb = get_taakblok(po_data, code)
        if tb is None:
            print(f"  Taakblok {code} niet gevonden — overgeslagen")
            continue

        print(f"\n→ Vermoedensruimte voor {code} …")
        prompt = build_vermoedensruimte_prompt(po_data, tb, kenniselementen, bestaande)

        if args.dry_run:
            print("=== SYSTEEM-PROMPT (fragment) ===")
            print(system[:300])
            print("\n=== USER-PROMPT ===")
            print(prompt)
            print("=== (dry-run, geen LLM-call) ===")
            continue

        response = llm_call(client, system, prompt)

        try:
            parsed = parse_json_response(response)
        except ValueError as e:
            print(f"  Fout bij parsen: {e}")
            print("  Raw response:", response[:300])
            continue

        if isinstance(parsed, list):
            parsed = {"taakblok": code, "vermoedens": parsed}
        parsed.setdefault("taakblok", code)
        parsed["_provenance"] = maak_provenance(
            "concept_extractor/vermoedensruimte", prompt_version="vermoedensruimte-v1"
        )

        out_path = output_dir / f"{code}.json"
        out_path.write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
        n = len(parsed.get("vermoedens", []))
        print(f"  {n} vermoedens → {out_path.relative_to(ROOT)}")

        bestaande += [v["naam"] for v in parsed.get("vermoedens", [])]


# ---------------------------------------------------------------------------
# SUB-COMMANDO B+C: seed
# ---------------------------------------------------------------------------

SYSTEM_SEED = """Je bent een expert in het ITAA-bekwaamheidsexamen voor gecertificeerde accountants.
Je helpt een kennisbank opbouwen door op basis van bronteksten een seed-concept-record te schrijven.

## Taak

Schrijf één JSON-concept-record voor het opgegeven vermoeden. Gebruik ALLEEN informatie uit de
aangeleverde bronteksten. Laat velden leeg als de bronteksten onvoldoende informatie geven.

## Schema

```json
{
  "id": "<slug: kleine letters, koppeltekens>",
  "naam": "<volledige naam, simpele taal>",
  "node_type": "<begrip | regel | beginsel | procedure | methode | drempel | actor | afwegingskader | skill | casus | fenomeen>",
  "status": "seed",
  "schema_version": "1.0",
  "main_rule": {
    "text": "<kernregel in simpele taal — paraphrase, geen letterlijke wetstekst>",
    "confidence": "grounded",
    "source": {"short": "<bv. AWW art. 5>", "citation": "<optioneel verbatim quote ≤30 woorden>"}
  },
  "exceptions": [
    {"text": "<uitzondering>", "confidence": "grounded", "source": {"short": "<ref>"}}
  ],
  "scope": {"applies_to": "<wie/wat>", "excludes": "<wie/wat uitgesloten>"},
  "edges": [
    {"type": "<edge-type>", "target": "<concept-id of naam>", "_dangling": true, "notitie": "<optioneel>"}
  ],
  "pitfalls": [],
  "voorbeeld_inline": []
}
```

## Schrijfregels

- Simpele taal, geen wetgeeftaal (paraphrase in hoofdtekst; verbatim enkel in source.citation)
- Afkortingen voluit eerste keer: "Cel voor Financiële Informatieverwerking (CFI)"
- confidence "grounded": alleen als je een concrete bron kunt aanwijzen
- confidence "inferred": als je iets afleidt dat niet letterlijk in de bron staat
- Lege velden weglaten of null — sparse is de norm
- Geen emoji in de JSON

Geef alleen geldig JSON terug, geen proza erbuiten."""


def chunks_naar_context(chunks) -> str:
    parts = []
    for i, chunk in enumerate(chunks, 1):
        bron    = chunk.meta.get("bron", "")
        artikel = chunk.artikel or ""
        header  = f"[Bron {i}: {bron} — {artikel}]" if artikel else f"[Bron {i}: {bron}]"
        parts.append(f"{header}\n{chunk.text[:2000]}")
    return "\n\n---\n\n".join(parts)


def build_seed_prompt(vermoeden: dict, po_context: str, chunks_context: str) -> str:
    return f"""## Context

{po_context}

## Te extraheren concept

Naam: {vermoeden['naam']}
Node-type (vermoeden): {vermoeden.get('node_type', '?')}
Rationale: {vermoeden.get('rationale', '')}
Gekoppeld aan: {vermoeden.get('gekoppeld_aan', '')}

## Bronteksten

{chunks_context}

---

Schrijf het seed-concept-record als JSON."""


def cmd_seed(args):
    vermoedens_path = Path(args.vermoedens)
    po_path         = Path(args.programmaonderdeel)
    chroma_path     = Path(args.chroma) if args.chroma else ROOT / "data" / "chroma_db"

    vermoedens_data = json.loads(vermoedens_path.read_text())
    po_data         = laad_programmaonderdeel(po_path)
    po_nr           = po_data.get("programmaonderdeel", "")
    vermoedens      = vermoedens_data.get("vermoedens", [])

    if not vermoedens:
        print("Geen vermoedens gevonden.")
        sys.exit(1)

    print("→ Retrieval-stack laden …")
    client_chroma, ef, reranker = build_retrieval_stack(chroma_path)
    cols = open_collections(client_chroma, ef, BRONNEN_COLS)
    if not cols:
        print(f"  Geen collections in {chroma_path}. Bouw de index eerst.")
        sys.exit(1)

    llm = llm_client()
    CONCEPT_DIR.mkdir(parents=True, exist_ok=True)

    po_context = (
        f"Programmaonderdeel {po_nr}: {po_data.get('titel', '')}\n"
        f"Taakblok: {vermoedens_data.get('taakblok', '')}"
    )

    for vermoeden in vermoedens:
        naam = vermoeden["naam"]
        print(f"\n→ Seed: {naam} …")

        # Multi-level retrieval queries (ADR-008 §2.B)
        sub_queries = [naam, f"{po_data.get('titel', '')} {naam}"]
        if vermoeden.get("rationale"):
            sub_queries.append(vermoeden["rationale"])

        # Voeg doelstellingen van het gekoppelde taakblok toe
        tb_code = ".".join(vermoeden.get("gekoppeld_aan", "").split(".")[:3])
        if tb_code:
            tb = get_taakblok(po_data, tb_code)
            if tb:
                sub_queries += [d["tekst"] for d in tb.get("doelstellingen", [])[:3]]

        chunks = multi_query_retrieve(
            sub_queries, cols, BRONNEN_COLS, reranker,
            bi_top_n=50,
            rerank_threshold=0.40,
            max_per_query=15,
            expand_context=True,
        )

        if not chunks:
            print("  Geen relevante chunks — overgeslagen")
            continue

        print(f"  {len(chunks)} chunks (rerank ≥ 0.40)")

        if args.dry_run:
            for c in chunks[:5]:
                print(f"    [{c.rerank_score:.3f}] {c.bron} — {c.artikel}")
            print("  (dry-run, geen LLM-call)")
            continue

        prompt   = build_seed_prompt(vermoeden, po_context, chunks_naar_context(chunks[:20]))
        response = llm_call(llm, SYSTEM_SEED, prompt)

        try:
            record = parse_json_response(response)
        except ValueError as e:
            print(f"  Parse-fout: {e}")
            continue

        if not isinstance(record, dict):
            print(f"  Onverwacht type: {type(record)}")
            continue

        record.setdefault("status", "seed")
        record.setdefault("schema_version", SCHEMA_VERSION)
        record.setdefault("node_type", vermoeden.get("node_type", "fenomeen"))
        if not record.get("id"):
            slug = re.sub(r"[^a-z0-9]+", "-", record.get("naam", naam).lower()).strip("-")
            record["id"] = slug[:60]

        chunk_inputs = [
            {"id": c.chunk_id, "sha256": None, "version": "rag-v1"}
            for c in chunks[:20]
        ]
        record["_provenance"] = maak_provenance(
            "concept_extractor/seed", inputs=chunk_inputs, prompt_version="seed-v1"
        )

        out_path = CONCEPT_DIR / f"{record['id']}.json"
        out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False))
        print(f"  → {out_path.relative_to(ROOT)}")

        dangling = [e["target"] for e in record.get("edges", []) if e.get("_dangling")]
        if dangling:
            print(f"  Dangling edges: {dangling}")


# ---------------------------------------------------------------------------
# SUB-COMMANDO D: verdiep
# ---------------------------------------------------------------------------

SYSTEM_VERDIEP = """Je bent een expert in het ITAA-bekwaamheidsexamen voor gecertificeerde accountants.
Je helpt een concept-record verdiepen op basis van aanvullende bronteksten.

Gegeven een bestaand seed-concept en nieuwe bronteksten: vul ontbrekende velden aan en verrijk
bestaande. Schrijf alleen velden die je kunt onderbouwen. Zet status op "partieel".
Dezelfde schrijfregels als bij seed (simpele taal, geen emoji, confidence-labels).

Geef het VOLLEDIGE bijgewerkte record als JSON."""


def cmd_verdiep(args):
    concept_id  = args.concept
    chroma_path = Path(args.chroma) if args.chroma else ROOT / "data" / "chroma_db"
    record_path = CONCEPT_DIR / f"{concept_id}.json"

    if not record_path.exists():
        print(f"Concept-record niet gevonden: {record_path}")
        sys.exit(1)

    record = json.loads(record_path.read_text())
    naam   = record.get("naam", concept_id)
    print(f"→ Verdiep: {naam}")

    sub_queries = [naam]
    if record.get("main_rule", {}).get("text"):
        sub_queries.append(record["main_rule"]["text"][:200])
    for edge in record.get("edges", [])[:5]:
        if edge.get("target"):
            sub_queries.append(edge["target"])

    client_chroma, ef, reranker = build_retrieval_stack(chroma_path)
    cols   = open_collections(client_chroma, ef, BRONNEN_COLS)
    chunks = multi_query_retrieve(
        sub_queries, cols, BRONNEN_COLS, reranker,
        bi_top_n=80, rerank_threshold=0.45, max_per_query=20, expand_context=True,
    )

    if not chunks:
        print("  Geen aanvullende chunks gevonden.")
        return

    print(f"  {len(chunks)} chunks")

    if args.dry_run:
        for c in chunks[:5]:
            print(f"  [{c.rerank_score:.3f}] {c.bron} — {c.artikel}")
        return

    llm = llm_client()
    prompt = f"""## Bestaand concept-record

```json
{json.dumps(record, indent=2, ensure_ascii=False)[:3000]}
```

## Aanvullende bronteksten

{chunks_naar_context(chunks[:20])}

---

Verdiep het record. Status → "partieel". Geef het volledige record als JSON."""

    response = llm_call(llm, SYSTEM_VERDIEP, prompt)

    try:
        updated = parse_json_response(response)
    except ValueError as e:
        print(f"  Parse-fout: {e}")
        return

    updated.setdefault("status", "partieel")
    updated["schema_version"] = SCHEMA_VERSION

    # Provenance: unie van bestaande + nieuwe inputs
    existing_prov   = record.get("_provenance", {})
    existing_inputs = existing_prov.get("inputs", [])
    known_ids       = {i["id"] for i in existing_inputs}
    new_inputs      = [
        {"id": c.chunk_id, "sha256": None, "version": "rag-v1"}
        for c in chunks[:20] if c.chunk_id not in known_ids
    ]
    updated["_provenance"] = {
        **existing_prov,
        "inputs": existing_inputs + new_inputs,
        "tooling": maak_provenance("concept_extractor/verdiep", prompt_version="verdiep-v1")["tooling"],
        "stale": False,
        "stale_reason": None,
    }

    record_path.write_text(json.dumps(updated, indent=2, ensure_ascii=False))
    print(f"  → {record_path.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Concept-extractor (ADR-008): vermoedensruimte / seed / verdiep"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_v = sub.add_parser("vermoedensruimte", help="Stap A: concept-kandidaten per taakblok")
    p_v.add_argument("--programmaonderdeel", required=True)
    p_v.add_argument("--taakblok", help="Specifieke code (default: alle kern-taakblokken)")
    p_v.add_argument("--dry-run", action="store_true")

    p_s = sub.add_parser("seed", help="Stap B+C: retrieval + LLM → seed-records")
    p_s.add_argument("--vermoedens", required=True)
    p_s.add_argument("--programmaonderdeel", required=True)
    p_s.add_argument("--chroma", help="ChromaDB-pad (default: data/chroma_db)")
    p_s.add_argument("--dry-run", action="store_true")

    p_d = sub.add_parser("verdiep", help="Stap D: verdiep een bestaand concept")
    p_d.add_argument("--concept", required=True, help="Concept-id (zonder .json)")
    p_d.add_argument("--chroma", help="ChromaDB-pad (default: data/chroma_db)")
    p_d.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()
    {
        "vermoedensruimte": cmd_vermoedensruimte,
        "seed": cmd_seed,
        "verdiep": cmd_verdiep,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
