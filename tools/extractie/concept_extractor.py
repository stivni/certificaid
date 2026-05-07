"""
Deterministische helpers voor concept-extractie (ADR-008).

Dit module bevat GEEN LLM-aanroepen — alle Anthropic API-calls zijn verwijderd.
Orkestratie (retrieval → LLM-synthese → record-schrijven) loopt via de
extractie-subagent (Claude Code Opus) die deze helpers importeert of aanroept
via Bash-commando's.

Wat dit module biedt:
  - Programmaonderdeel-JSON laden en doorzoeken
  - Prompt-bouwfuncties (deterministische string-operaties)
  - Provenance-helpers
  - JSON-parsing (robuust tegen proza rondom de JSON)
  - Record-schrijven (CONCEPT_DIR / <id>.json)

Gebruik (vanuit subagent of ander script):
  from tools.extractie.concept_extractor import (
      laad_programmaonderdeel,
      verzamel_kenniselementen,
      get_taakblok,
      kern_taakblokken,
      bestaande_concepten,
      chunks_naar_context,
      build_seed_prompt,
      maak_provenance,
      parse_json_response,
      schrijf_record,
      CONCEPT_DIR,
      SCHEMA_VERSION,
  )
"""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT           = Path(__file__).resolve().parent.parent.parent
CONCEPT_DIR    = ROOT / "data" / "concept_records"
EXTRACTIE_DIR  = ROOT / "data" / "extractie"
PROMPTS_DIR    = ROOT / "prompts"
SCHEMA_VERSION = "1.0"


# ---------------------------------------------------------------------------
# Programmaonderdeel-JSON lezen
# ---------------------------------------------------------------------------

def laad_programmaonderdeel(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


def verzamel_kenniselementen(data: dict, alleen_deel1: bool = True) -> list[dict]:
    """Verzamel alle kenniselementen (incl. subitems) als platte lijst."""
    result = []
    for ke in data.get("kenniselementen", []):
        if alleen_deel1 and ke.get("deel") != 1:
            continue
        if "subitems" in ke:
            for sub in ke["subitems"]:
                result.append({
                    "code":   sub["code"],
                    "tekst":  sub["tekst"],
                    "parent": ke["code"],
                })
        else:
            result.append({
                "code":   ke["code"],
                "tekst":  ke["tekst"],
                "parent": None,
            })
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
            rec = json.loads(f.read_text(encoding="utf-8"))
            if not rec.get("_provenance", {}).get("stale", False):
                namen.append(rec.get("naam", f.stem))
        except Exception:
            pass
    return namen


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------

def _pipeline_version() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, stderr=subprocess.DEVNULL,
        ).decode().strip()
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=ROOT, stderr=subprocess.DEVNULL,
        ).decode().strip()
        return sha + ("-dirty" if dirty else "")
    except Exception:
        return "unknown"


def maak_provenance(
    pipeline: str,
    inputs: list[dict] | None = None,
    prompt_version: str = "v1",
    model: str = "",
) -> dict:
    return {
        "inputs": inputs or [],
        "tooling": {
            "pipeline":         pipeline,
            "pipeline_version": _pipeline_version(),
            "model":            model,
            "prompt_version":   prompt_version,
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stale":        False,
        "stale_reason": None,
    }


# ---------------------------------------------------------------------------
# JSON-parsing
# ---------------------------------------------------------------------------

def parse_json_response(text: str) -> dict | list:
    """Extraheer JSON uit een LLM-response (ook als er proza omheen staat)."""
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
    raise ValueError(f"Kon geen JSON parsen:\n{text[:500]}")


# ---------------------------------------------------------------------------
# Prompt-bouwfuncties (deterministische string-operaties, geen LLM)
# ---------------------------------------------------------------------------

def chunks_naar_context(chunks) -> str:
    """
    Zet een lijst van RetrievalResult-objecten om naar een geformateerde
    brontekst-string voor gebruik in een LLM-prompt.
    """
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
Kenniselementen: {', '.join(vermoeden.get('kenniselementen', [])) or '—'}

## Bronteksten

{chunks_context}

---

Schrijf het seed-concept-record als JSON."""


def build_vermoedensruimte_prompt(
    po_data: dict,
    taakblok: dict,
    kenniselementen: list[dict],
    bestaande: list[str],
) -> str:
    po_titel = po_data.get("titel", "")
    po_nr    = po_data.get("programmaonderdeel", "")

    taken_tekst    = "\n".join(f"- {t['tekst']}" for t in taakblok.get("taken", []))
    doel_tekst     = "\n".join(f"- {d['tekst']}" for d in taakblok.get("doelstellingen", []))
    ke_tekst       = "\n".join(f"- [{ke['code']}] {ke['tekst']}" for ke in kenniselementen)
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


# ---------------------------------------------------------------------------
# Record-schrijven
# ---------------------------------------------------------------------------

def schrijf_record(record: dict, *, overschrijf: bool = False) -> Path:
    """
    Schrijf een concept-record naar CONCEPT_DIR/<id>.json.
    Raises FileExistsError als het record al bestaat en overschrijf=False.
    """
    CONCEPT_DIR.mkdir(parents=True, exist_ok=True)
    record_id = record.get("id")
    if not record_id:
        slug = re.sub(r"[^a-z0-9]+", "-", record.get("naam", "concept").lower()).strip("-")
        record_id = slug[:60]
        record["id"] = record_id

    pad = CONCEPT_DIR / f"{record_id}.json"
    if pad.exists() and not overschrijf:
        raise FileExistsError(f"Record bestaat al: {pad}. Gebruik overschrijf=True.")

    pad.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    return pad
