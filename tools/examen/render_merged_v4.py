"""Render _merged/<examen>.json (schema 4.0) naar Quartz-markdown.

Output:
    content/voorbeeldexamens/<examen>.md  — per examen één pagina
    content/voorbeeldexamens/index.md     — overzicht met links

CLI::

    python3 -m tools.examen.render_merged_v4          # alle examens
    python3 -m tools.examen.render_merged_v4 --examen 2024-1

Schema 4.0 structuur per vraag:
    {
      "vraag_id": "...",
      "interpretatie": { schema 1.1 },
      "antwoord": { schema 1.1 } | null,
      "segment_meta": { ... }
    }

Templates in tools/examen/templates/ (Jinja2).
Deterministisch, idempotent.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parents[2]
MERGED_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_merged"
OUTPUT_DIR = REPO_ROOT / "content" / "voorbeeldexamens"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

_CONFIDENCE_ICOON: dict[str, str] = {
    "grounded": "⚖️",
    "inferred": "🤖",
}

_PLACEHOLDER_GEEN_ANTWOORD = "_Antwoord wacht op concept-laag._"
_PLACEHOLDER_WACHT = (
    "_Vraag-inhoud niet gereconstrueerd (topic-only). "
    "Wacht op vraag-generatie._"
)


# ---------------------------------------------------------------------------
# Kleine hulpfuncties
# ---------------------------------------------------------------------------


def _prefix_regels(tekst: str, prefix: str) -> str:
    """Plaats prefix voor elke regel van tekst (voor callout-bodies)."""
    if not tekst.strip():
        return prefix.rstrip()
    return "\n".join(prefix + regel for regel in tekst.splitlines())


def _callout(soort: str, titel: str, body: str, *, collapsed: bool = False) -> str:
    """Bouw een Quartz-callout block.

    collapsed=True voegt '-' toe na het type, waardoor de callout
    standaard ingeklapt is.
    """
    suffix = "-" if collapsed else ""
    kop = f"> [!{soort}]{suffix} {titel}"
    if not body.strip():
        return kop
    body_geprefixt = _prefix_regels(body, "> ")
    return f"{kop}\n{body_geprefixt}"


def _confidence_icoon(blok: dict[str, Any]) -> str:
    c = blok.get("confidence", "")
    return f" {_CONFIDENCE_ICOON[c]}" if c in _CONFIDENCE_ICOON else ""


def _formatteer_bedrag(waarde: Any) -> str:
    """Formatteer getal met punt als duizend-scheidingsteken."""
    if waarde is None:
        return ""
    try:
        f = float(waarde)
    except (TypeError, ValueError):
        return str(waarde)
    if f == int(f):
        return f"{int(f):,}".replace(",", ".")
    return f"{f:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _normaliseer_cel(cel: Any) -> str:
    tekst = "" if cel is None else str(cel)
    tekst = tekst.replace("|", "\\|")
    tekst = tekst.replace("\n", " <br> ")
    return tekst.strip() or " "


def _markdown_tabel(headers: list[str], rows: list[list[Any]]) -> str:
    """Bouw een markdown-tabel vanuit headers + rows."""
    n = max(len(headers), max((len(r) for r in rows), default=0), 1)
    headers_genorm = [_normaliseer_cel(h) for h in headers] + [" "] * (n - len(headers))

    def pad_rij(rij: list[Any]) -> list[str]:
        gevuld = list(rij) + [""] * (n - len(rij))
        return [_normaliseer_cel(c) for c in gevuld]

    lijnen = [
        "| " + " | ".join(headers_genorm) + " |",
        "| " + " | ".join(["---"] * n) + " |",
    ]
    for rij in rows:
        lijnen.append("| " + " | ".join(pad_rij(rij)) + " |")
    return "\n".join(lijnen)


# ---------------------------------------------------------------------------
# Context-blokken rendering
# ---------------------------------------------------------------------------


def _render_context_blok(blok: dict[str, Any]) -> str:
    """Render één context-blok naar markdown."""
    blok_type = blok.get("type", "")

    if blok_type == "casus_context":
        tekst = (blok.get("tekst") or "").strip()
        if not tekst:
            return ""
        return "\n".join(f"> {regel}" for regel in tekst.splitlines())

    if blok_type == "balans":
        delen: list[str] = ["**Balans**", ""]
        actief = blok.get("actief", {})
        passief = blok.get("passief", {})
        if actief:
            delen.append("**Actief**")
            delen.append("")
            headers = actief.get("headers", [])
            rows = actief.get("rows", [])
            delen.append(_markdown_tabel(headers, rows))
            delen.append("")
        if passief:
            delen.append("**Passief**")
            delen.append("")
            headers = passief.get("headers", [])
            rows = passief.get("rows", [])
            delen.append(_markdown_tabel(headers, rows))
        return "\n".join(delen).rstrip()

    if blok_type in ("resultatenrekening", "proef_saldibalans", "rekeningstaat", "inventaris", "tabel"):
        kop_map = {
            "resultatenrekening": "**Resultatenrekening**",
            "proef_saldibalans": "**Proef- en saldibalans**",
            "rekeningstaat": "**Rekeningstaat**",
            "inventaris": "**Inventaris**",
            "tabel": None,
        }
        kop = kop_map.get(blok_type)
        headers = blok.get("headers", [])
        rows = blok.get("rows", [])
        if not rows and not headers:
            return f"_{blok_type}_"
        tabel = _markdown_tabel(headers, rows)
        if kop:
            return f"{kop}\n\n{tabel}"
        return tabel

    if blok_type == "gegevens_tabel":
        titel = blok.get("titel", "")
        rijen = blok.get("rijen", [])
        kop = f"**{titel}**" if titel else "**Gegevens**"
        if not rijen:
            return kop
        tabel_rijen = []
        for rij in rijen:
            label = str(rij.get("label", ""))
            bedrag = rij.get("bedrag")
            bedrag_str = _formatteer_bedrag(bedrag) if bedrag is not None else ""
            tabel_rijen.append([label, bedrag_str])
        tabel = _markdown_tabel(["Label", "Bedrag"], tabel_rijen)
        return f"{kop}\n\n{tabel}"

    if blok_type == "tekst":
        return (blok.get("tekst") or "").strip()

    # Fallback: cursief type-prefix + beschikbare tekst-velden
    tekst_velden = []
    for sleutel in ("tekst", "beschrijving", "inhoud", "formule", "notitie"):
        waarde = blok.get(sleutel)
        if waarde:
            tekst_velden.append(str(waarde))
    extra = " ".join(tekst_velden)
    return f"*[{blok_type}]* {extra}".strip()


def _render_context_blokken(blokken: list[dict[str, Any]]) -> str:
    """Render alle context-blokken; skip lege resultaten."""
    delen = [_render_context_blok(b) for b in blokken]
    return "\n\n".join(d for d in delen if d.strip())


# ---------------------------------------------------------------------------
# Antwoord-blokken rendering (blokken[] binnen vraag_antwoorden[])
# ---------------------------------------------------------------------------


def _render_antwoord_blok(blok: dict[str, Any]) -> str:
    """Render één typed antwoord-blok naar markdown."""
    blok_type = blok.get("type", "")
    conf = _confidence_icoon(blok)

    if blok_type == "motivatie":
        tekst = (blok.get("tekst") or "").strip()
        return f"{tekst}{conf}"

    if blok_type == "conclusie":
        tekst = (blok.get("tekst") or "").strip()
        return f"**_{tekst}_**{conf}"

    if blok_type == "grondslag":
        tekst = (blok.get("tekst") or "").strip()
        wetsref = blok.get("wetsref", "")
        bron_zin = f"\n*Bron: {wetsref}*" if wetsref else ""
        return f"> {tekst}{conf}{bron_zin}"

    if blok_type == "definitie":
        lemma = blok.get("lemma", "")
        uitleg = (blok.get("uitleg") or "").strip()
        return f"**{lemma}**: {uitleg}{conf}"

    if blok_type == "boeking":
        regels = blok.get("regels", [])
        toelichting = blok.get("toelichting", "")
        tabel_rijen = []
        for r in regels:
            zijde = str(r.get("zijde", ""))
            rekening = str(r.get("rekening", ""))
            naam = str(r.get("naam", ""))
            bedrag = r.get("bedrag")
            bedrag_str = _formatteer_bedrag(bedrag) if bedrag is not None else ""
            tabel_rijen.append([zijde, rekening, naam, bedrag_str])
        tabel = _markdown_tabel(["Zijde", "Rekening", "Naam", "Bedrag"], tabel_rijen)
        toel_zin = f"\n\n{toelichting}" if toelichting else ""
        return f"{tabel}{conf}{toel_zin}"

    if blok_type == "berekening":
        formule = blok.get("formule", "")
        stappen = blok.get("stappen", [])
        delen: list[str] = [f"**Berekening**{conf}"]
        if formule:
            delen.append(f"`{formule}`")
        if stappen:
            for i, stap in enumerate(stappen, 1):
                stap_tekst = str(stap) if not isinstance(stap, dict) else stap.get("beschrijving", str(stap))
                delen.append(f"{i}. {stap_tekst}")
        return "\n".join(delen)

    if blok_type == "procedure":
        stappen = blok.get("stappen", [])
        conf_zin = conf
        regel_delen: list[str] = []
        for stap in stappen:
            if isinstance(stap, dict):
                nr = stap.get("nummer", "")
                besch = stap.get("beschrijving", "")
                regel_delen.append(f"{nr}. {besch}")
            else:
                regel_delen.append(f"- {stap}")
        return "\n".join(regel_delen) + conf_zin

    if blok_type == "tabel":
        headers = blok.get("headers", [])
        rows = blok.get("rows", [])
        return _markdown_tabel(headers, rows) + conf

    if blok_type == "opsomming":
        items = blok.get("items", [])
        conf_zin = conf
        regels = [f"- {item}" for item in items]
        return "\n".join(regels) + conf_zin

    # Fallback
    return f"*[{blok_type}]* {blok.get('tekst', '')}{conf}".strip()


def _render_antwoord_blokken(blokken: list[dict[str, Any]]) -> str:
    """Render alle typed antwoord-blokken."""
    if not blokken:
        return ""
    return "\n\n".join(
        _render_antwoord_blok(b) for b in blokken if b
    )


# ---------------------------------------------------------------------------
# Antwoord-callout (per deelvraag)
# ---------------------------------------------------------------------------


def _render_antwoord_callout(
    deelvraag: dict[str, Any],
    vraag_antwoord: dict[str, Any] | None,
) -> str:
    """Render de collapsed success-callout voor één deelvraag.

    vraag_antwoord is het item uit antwoord.vraag_antwoorden[] voor deze
    deelvraag-id, of None als er geen antwoord-bestand is.
    """
    if vraag_antwoord is None:
        # antwoord=null op vraag-niveau → geen antwoord-bestand
        body = _PLACEHOLDER_GEEN_ANTWOORD
        return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)

    status = vraag_antwoord.get("antwoord_status", "")

    if status == "wacht_op_vraag_generatie":
        body = _PLACEHOLDER_WACHT
        return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)

    if status == "hard_blocked":
        gap = vraag_antwoord.get("record_gap_report") or {}
        beschrijving = gap.get("beschrijving", "")
        body = f"_Antwoord blokkeert op ontbrekend record._ {beschrijving}"
        return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)

    if status == "beantwoord":
        vraagtype = deelvraag.get("vraagtype", "open")
        blokken = vraag_antwoord.get("blokken", [])
        delen: list[str] = []

        if vraagtype == "mc_keuze":
            gekozen = vraag_antwoord.get("gekozen_optie_id", "?")
            delen.append(f"**Antwoord: {gekozen}**")
        elif vraagtype == "juist_fout":
            oordeel = vraag_antwoord.get("oordeel")
            if oordeel is True:
                delen.append("**Antwoord: Juist**")
            elif oordeel is False:
                delen.append("**Antwoord: Fout**")

        # Typed blokken (motivering bij mc/jf, of volledig antwoord bij open)
        blokken_md = _render_antwoord_blokken(blokken)
        if blokken_md.strip():
            delen.append(blokken_md)

        body = "\n\n".join(d for d in delen if d.strip())
        if not body.strip():
            body = "_Antwoord aangemerkt als beantwoord (geen verdere toelichting)._"
        return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)

    # Onbekende status → placeholder
    body = _PLACEHOLDER_GEEN_ANTWOORD
    return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)


# ---------------------------------------------------------------------------
# Deelvraag-rendering
# ---------------------------------------------------------------------------


def _render_deelvraag_data(
    deelvraag: dict[str, Any],
    vraag_antwoord: dict[str, Any] | None,
    env: Environment,
) -> str:
    """Bereid deelvraag-data voor en delegeer naar _deelvraag.md.j2.

    Geen labels of nummering meer in output — vraagstelling staat verbatim.
    """
    volledigheid = deelvraag.get("volledigheid", "volledig")
    vraagtype = deelvraag.get("vraagtype", "open")
    vraagstelling = (deelvraag.get("vraagstelling") or "").strip() or None

    # MC-opties: normaliseer naar list[dict] met id en tekst (id behouden — MC-opties wél gelabeld)
    opties_raw = deelvraag.get("opties", []) or []
    opties = [
        {"id": o.get("id", "?"), "tekst": (o.get("tekst") or "").strip()}
        for o in opties_raw
    ]

    topic_only_onderwerp = deelvraag.get("topic_only_onderwerp", "") or ""

    # Complexe antwoord-callout blijft in Python
    antwoord_callout_md = _render_antwoord_callout(deelvraag, vraag_antwoord)

    tmpl = env.get_template("_deelvraag.md.j2")
    uitvoer = tmpl.render(
        volledigheid=volledigheid,
        vraagtype=vraagtype,
        vraagstelling=vraagstelling,
        opties=opties,
        topic_only_onderwerp=topic_only_onderwerp,
        antwoord_callout_md=antwoord_callout_md,
    )
    return uitvoer.rstrip()


# ---------------------------------------------------------------------------
# Vraag-eenheid rendering (H2)
# ---------------------------------------------------------------------------


def _bouw_antwoorden_index(antwoord: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    """Map deelvraag-id → antwoord-record vanuit antwoord.vraag_antwoorden[]."""
    if antwoord is None:
        return {}
    return {
        a["id"]: a
        for a in antwoord.get("vraag_antwoorden", [])
        if isinstance(a, dict) and "id" in a
    }


def _formatteer_herkomst(examen_id: str, vraag_herkomst: str) -> str:
    """Formatteer een kleine italic-notitie over de herkomst van de vraag.

    PRUTS: pas de notitie-string hier aan (bv. wikilink i.p.v. plain text,
    andere herkomst-labels, fallback-tekst).

    Voorbeelden:
      ("2013-1", "officieel")    → "Examen 2013-1"
      ("2024-1", "herinnering")  → "Examen 2024-1 (uit herinnering gereconstrueerd)"
      ("2014-1", "hybride")      → "Examen 2014-1 (hybride bron)"
    """
    if vraag_herkomst == "herinnering":
        return f"Examen {examen_id} (uit herinnering gereconstrueerd)"
    if vraag_herkomst == "hybride":
        return f"Examen {examen_id} (hybride bron)"
    return f"Examen {examen_id}"


def _render_vraag_eenheid(vraag: dict[str, Any], env: Environment | None = None) -> str:
    """Bereid vraag-eenheid-data voor en delegeer naar _vraag_eenheid.md.j2."""
    if env is None:
        env = _get_env()

    vraag_id = vraag["vraag_id"]
    interpretatie = vraag.get("interpretatie", {})
    antwoord = vraag.get("antwoord")

    onderwerp = interpretatie.get("vraag_onderwerp", "")
    examen_id = interpretatie.get("examen_id", "")
    vraag_herkomst = interpretatie.get("vraag_herkomst", "officieel")
    context_blokken = interpretatie.get("context_blokken", [])
    deelvragen = interpretatie.get("vragen", [])

    antwoorden_index = _bouw_antwoorden_index(antwoord)

    # Complexe context-blokken blijven in Python
    context_md = _render_context_blokken(context_blokken)

    # Herkomst-regel (PRUTS-punt zit in _formatteer_herkomst)
    herkomst_regel = _formatteer_herkomst(examen_id, vraag_herkomst) if examen_id else ""

    # Deelvragen pre-renderen via subtemplate
    deelvragen_md = [
        _render_deelvraag_data(dv, antwoorden_index.get(dv.get("id", "?")), env)
        for dv in deelvragen
    ]

    tmpl = env.get_template("_vraag_eenheid.md.j2")
    return tmpl.render(
        vraag_id=vraag_id,
        onderwerp=onderwerp,
        herkomst_regel=herkomst_regel,
        context_md=context_md.strip(),
        deelvragen_md=deelvragen_md,
    ).rstrip()


# ---------------------------------------------------------------------------
# Jinja2 Environment
# ---------------------------------------------------------------------------


def _get_env() -> Environment:
    """Maak Jinja2-environment met FileSystemLoader op templates-map."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


# ---------------------------------------------------------------------------
# Data-voorbereiding voor index-pagina
# ---------------------------------------------------------------------------


def _bereken_herkomst(vragen: list[dict[str, Any]]) -> str:
    """Bepaal meest-voorkomende herkomst; 'hybride' bij mix."""
    herkomsten = [
        v.get("interpretatie", {}).get("vraag_herkomst", "")
        for v in vragen
        if v.get("interpretatie")
    ]
    if not herkomsten:
        return "?"
    if len(set(herkomsten)) > 1:
        return "hybride"
    return herkomsten[0]


# ---------------------------------------------------------------------------
# Examen-pagina rendering
# ---------------------------------------------------------------------------


def _render_examen_pagina(data: dict[str, Any]) -> str:
    """Render één examen naar een volledige markdown-pagina via Jinja2-template."""
    env = _get_env()
    tmpl = env.get_template("examen_pagina.md.j2")

    examen_id = data.get("examen_id", "?")
    vragen = data.get("vragen", [])
    vandaag = date.today().isoformat()

    # Render vraag-eenheden via subtemplate (complex blokken blijven in Python)
    vraag_eenheden_md = [_render_vraag_eenheid(v, env) for v in vragen]

    totaal = len(vragen)
    met_antwoord = sum(1 for v in vragen if v.get("antwoord") is not None)

    inhoud = tmpl.render(
        examen_id=examen_id,
        bron_pdf=data.get("bron_pdf", ""),
        vragen=vragen,
        vandaag=vandaag,
        totaal=totaal,
        met_antwoord=met_antwoord,
        vraag_eenheden_md=vraag_eenheden_md,
    )
    return inhoud.rstrip() + "\n"


# ---------------------------------------------------------------------------
# Index-pagina rendering
# ---------------------------------------------------------------------------


def _render_index_pagina(examen_data_list: list[dict[str, Any]]) -> str:
    """Render de index-pagina met overzichtstabel via Jinja2-template."""
    env = _get_env()
    tmpl = env.get_template("index_pagina.md.j2")

    vandaag = date.today().isoformat()

    examen_meta = []
    for data in sorted(examen_data_list, key=lambda d: d.get("examen_id", "")):
        vragen = data.get("vragen", [])
        examen_meta.append({
            "examen_id": data.get("examen_id", "?"),
            "totaal": len(vragen),
            "herkomst": _bereken_herkomst(vragen),
        })

    inhoud = tmpl.render(
        examen_meta=examen_meta,
        vandaag=vandaag,
    )
    return inhoud.rstrip() + "\n"


# ---------------------------------------------------------------------------
# Schrijf-met-idempotentie
# ---------------------------------------------------------------------------


def _schrijf_indien_gewijzigd(pad: Path, inhoud: str) -> bool:
    """Schrijf inhoud naar pad, maar sla over als content identiek is.

    Geeft True als er daadwerkelijk geschreven is.
    """
    if pad.exists():
        bestaand = pad.read_text(encoding="utf-8")
        if bestaand == inhoud:
            return False
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(inhoud, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Publieke API
# ---------------------------------------------------------------------------


def render_examen(examen_id: str) -> bool:
    """Render één examen. Geeft True als het bestand (her)geschreven is."""
    pad = MERGED_DIR / f"{examen_id}.json"
    if not pad.exists():
        raise FileNotFoundError(f"Geen merged-bestand gevonden: {pad}")
    data = json.loads(pad.read_text(encoding="utf-8"))
    inhoud = _render_examen_pagina(data)
    uitvoer = OUTPUT_DIR / f"{examen_id}.md"
    return _schrijf_indien_gewijzigd(uitvoer, inhoud)


def render_alle() -> dict[str, bool]:
    """Render alle _merged/*.json bestanden + index.md.

    Geeft dict examen_id → True als (her)geschreven.
    """
    bestanden = sorted(MERGED_DIR.glob("*.json"))
    resultaten: dict[str, bool] = {}
    alle_data: list[dict[str, Any]] = []

    for bestand in bestanden:
        data = json.loads(bestand.read_text(encoding="utf-8"))
        alle_data.append(data)
        examen_id = data.get("examen_id", bestand.stem)
        inhoud = _render_examen_pagina(data)
        uitvoer = OUTPUT_DIR / f"{examen_id}.md"
        resultaten[examen_id] = _schrijf_indien_gewijzigd(uitvoer, inhoud)

    # Index
    index_inhoud = _render_index_pagina(alle_data)
    index_pad = OUTPUT_DIR / "index.md"
    resultaten["index"] = _schrijf_indien_gewijzigd(index_pad, index_inhoud)

    return resultaten


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render _merged/<examen>.json naar Quartz-markdown."
    )
    parser.add_argument(
        "--examen",
        help="Render enkel dit examen (bv. '2024-1'). Zonder dit argument: alle.",
    )
    args = parser.parse_args()

    if args.examen:
        geschreven = render_examen(args.examen)
        status = "geschreven" if geschreven else "ongewijzigd (idempotent)"
        print(f"{args.examen}: {status}")
        return 0

    resultaten = render_alle()
    for naam, geschreven in sorted(resultaten.items()):
        status = "geschreven" if geschreven else "ongewijzigd"
        print(f"  {naam}: {status}")
    totaal = sum(1 for v in resultaten.values() if v)
    print(f"\n{totaal}/{len(resultaten)} bestanden (her)geschreven.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
