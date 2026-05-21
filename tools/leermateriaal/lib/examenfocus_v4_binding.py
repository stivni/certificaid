"""Examenfocus v4-binding voor minicursus-render.

Laadt vragen uit _merged/<examen>.json (schema 4.0) en rendert ze als
nested collapsible callouts voor Quartz.

Geen LLM-calls. Deterministisch en idempotent.

ADR-024 §3 (schema 1.2) + §5 (antwoord-schema) + §6 (merger).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

# Hergebruik render-helpers uit render_merged_v4 (geen aanpassingen aan die module)
from tools.examen.render_merged_v4 import (
    _bouw_antwoorden_index,
    _formatteer_herkomst,
    _render_antwoord_callout,
    _render_context_blokken,
    _render_deelvraag_data,
)

ROOT = Path(__file__).resolve().parent.parent.parent.parent
MERGED_DIR = ROOT / "data" / "programma" / "examen_vragen" / "_merged"


# ---------------------------------------------------------------------------
# Laad + filter vragen
# ---------------------------------------------------------------------------


def laad_vragen_voor_po(programmaonderdeel_code: str) -> list[dict]:
    """Scan alle _merged/<examen>.json en filter vragen op programmaonderdeel_code.

    Filter: vraag.interpretatie.programmaonderdeel_ids bevat programmaonderdeel_code.
    Sorteer op (examen_id, vraag_id) voor determinisme.

    Return-vorm: lijst van dicts met velden:
        vraag_id, examen_id, onderwerp, herkomst_label,
        context_blokken, deelvragen, antwoord

    Geen LLM-calls.
    """
    if not MERGED_DIR.exists():
        return []

    resultaat: list[dict] = []
    for bestand in sorted(MERGED_DIR.glob("*.json")):
        try:
            data = json.loads(bestand.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        for vraag in data.get("vragen", []):
            interpretatie = vraag.get("interpretatie") or {}
            po_ids = interpretatie.get("programmaonderdeel_ids") or []
            if programmaonderdeel_code not in po_ids:
                continue

            examen_id = interpretatie.get("examen_id", data.get("examen_id", ""))
            vraag_herkomst = interpretatie.get("vraag_herkomst", "officieel")
            herkomst_label = _formatteer_herkomst(examen_id, vraag_herkomst, po_ids)

            resultaat.append({
                "vraag_id": vraag.get("vraag_id", ""),
                "examen_id": examen_id,
                "onderwerp": interpretatie.get("vraag_onderwerp", ""),
                "herkomst_label": herkomst_label,
                "context_blokken": interpretatie.get("context_blokken", []),
                "deelvragen": interpretatie.get("vragen", []),
                "antwoord": vraag.get("antwoord"),
            })

    resultaat.sort(key=lambda v: (v["examen_id"], v["vraag_id"]))
    return resultaat


# ---------------------------------------------------------------------------
# Render-helper: één vraag → nested collapsible callout
# ---------------------------------------------------------------------------


def _prefix_callout(content_md: str, soort: str, titel: str, *, collapsed: bool = True) -> str:
    """Wrap content_md in een Quartz-callout.

    Elke regel van content_md wordt geprefixed met '> ' zodat hij deel wordt
    van de callout-body. De callout-header wordt er bovenop gezet.

    collapsed=True → [!soort]- titel (standaard ingeklapt).
    """
    suffix = "-" if collapsed else ""
    header = f"> [!{soort}]{suffix} {titel}"
    if not content_md.strip():
        return header
    regels = content_md.splitlines()
    body_regels = [f"> {regel}" if regel.strip() else ">" for regel in regels]
    return header + "\n" + "\n".join(body_regels)


def render_vraag_callout(vraag: dict[str, Any]) -> str:
    """Render één vraag-dict naar een nested collapsed callout voor Quartz.

    Structuur:
        > [!question]- {onderwerp}
        > *{herkomst_label}*
        > {context_blokken}
        > {deelvraag 1 vraagstelling}
        > {deelvraag 1 mc-opties}
        > > [!success]- Antwoord (klik om te openen)
        > > {antwoord-inhoud}
        > {deelvraag 2 ...}

    Geneste callouts werken in Quartz via '> > '-prefixes voor de inner-callout.
    """
    from tools.examen.render_merged_v4 import _get_env
    env = _get_env()

    onderwerp = vraag.get("onderwerp", "")
    herkomst_label = vraag.get("herkomst_label", "")
    context_blokken = vraag.get("context_blokken", [])
    deelvragen = vraag.get("deelvragen", [])
    antwoord = vraag.get("antwoord")

    antwoorden_index = _bouw_antwoorden_index(antwoord)

    # --- Bouw body-inhoud (wordt geprefixed met '> ') ---
    body_delen: list[str] = []

    # Herkomst-regel (italic)
    if herkomst_label:
        body_delen.append(f"*{herkomst_label}*")

    # Context-blokken (volledig, niet ingekort)
    context_md = _render_context_blokken(context_blokken).strip()
    if context_md:
        body_delen.append(context_md)

    # Deelvragen: vraagstelling + mc-opties + antwoord-callout
    for deelvraag in deelvragen:
        vraag_antwoord = antwoorden_index.get(deelvraag.get("id", "?"))

        # Render deelvraag-data via bestaande subtemplate (_deelvraag.md.j2)
        # render_deelvraag_data produceert: vraagstelling + opties + antwoord_callout
        deelvraag_md = _render_deelvraag_data(deelvraag, vraag_antwoord, env).strip()

        if deelvraag_md:
            # De antwoord-callout binnenin de deelvraag is een collapsed '> [!success]-'
            # Dit moet genest worden: elke '> ' regel wordt '> > ' in de outer context.
            # render_deelvraag_data produceert de antwoord_callout als vlakke string
            # (begint met '> [!success]-'). We moeten dit correct nesten.
            # Strategie: splits deelvraag_md in pre-callout en callout-deel,
            # prefix alles met '> ' (de outer-prefix doet de nesting).
            body_delen.append(deelvraag_md)

    # Combineer body
    body = "\n\n".join(d for d in body_delen if d.strip())

    # Nest inner antwoord-callouts: elke regel die begint met '> [!success]'
    # of '> > ' in de deelvraag-output moet genest worden onder de outer '> '-prefix.
    # Dit gebeurt automatisch omdat _prefix_callout elke body-regel prefixeert
    # met '> ', waardoor bestaande '> [!success]-' regels '> > [!success]-' worden.

    return _prefix_callout(body, "question", onderwerp, collapsed=True)
