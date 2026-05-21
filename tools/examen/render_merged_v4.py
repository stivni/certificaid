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

Geen Jinja, geen Claude API. Pure deterministisch, idempotent.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
MERGED_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_merged"
OUTPUT_DIR = REPO_ROOT / "content" / "voorbeeldexamens"

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


def _render_deelvraag(
    deelvraag: dict[str, Any],
    vraag_antwoord: dict[str, Any] | None,
) -> str:
    """Render één deelvraag (H3 + vraagstelling + mc-opties + antwoord-callout)."""
    label = deelvraag.get("label_in_pdf") or deelvraag.get("id", "?")
    motivatie_verwacht = deelvraag.get("motivatie_verwacht", False)
    volledigheid = deelvraag.get("volledigheid", "volledig")
    vraagtype = deelvraag.get("vraagtype", "open")

    motivatie_hint = " *(motivering vereist)*" if motivatie_verwacht else ""
    header = f"### Vraag {label}{motivatie_hint}"

    delen: list[str] = [header, ""]

    # Vraagstelling: skip bij topic_only of als None
    if volledigheid != "topic_only":
        vraagstelling = (deelvraag.get("vraagstelling") or "").strip()
        if vraagstelling:
            delen.append(vraagstelling)
            delen.append("")

    # MC-opties als bullet-lijst
    if vraagtype == "mc_keuze":
        opties = deelvraag.get("opties", [])
        for optie in opties:
            optie_id = optie.get("id", "?")
            optie_tekst = (optie.get("tekst") or "").strip()
            delen.append(f"- **{optie_id}**: {optie_tekst}")
        if opties:
            delen.append("")

    # Topic-only warning callout (geen collapsed)
    if volledigheid == "topic_only":
        topic_onderwerp = deelvraag.get("topic_only_onderwerp", "")
        warning_body = topic_onderwerp
        delen.append(_callout("warning", "Topic only", warning_body))
        delen.append("")

    # Antwoord-callout (altijd aanwezig, collapsed)
    delen.append(_render_antwoord_callout(deelvraag, vraag_antwoord))
    delen.append("")

    return "\n".join(delen).rstrip()


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


def _render_vraag_eenheid(vraag: dict[str, Any]) -> str:
    """Render één vraag-eenheid (H2 + context + deelvragen)."""
    vraag_id = vraag["vraag_id"]
    interpretatie = vraag.get("interpretatie", {})
    antwoord = vraag.get("antwoord")

    onderwerp = interpretatie.get("vraag_onderwerp", "")
    themas = interpretatie.get("themas", [])
    context_blokken = interpretatie.get("context_blokken", [])
    deelvragen = interpretatie.get("vragen", [])

    antwoorden_index = _bouw_antwoorden_index(antwoord)

    delen: list[str] = []

    # H2 anchor
    delen.append(f"## {vraag_id}")
    delen.append("")

    # Onderwerp
    if onderwerp:
        delen.append(f"**{onderwerp}**")
        delen.append("")

    # Themas als tags (inline)
    if themas:
        tags_str = " · ".join(f"`{t}`" for t in themas)
        delen.append(f"*Thema's*: {tags_str}")
        delen.append("")

    # Context-blokken
    context_md = _render_context_blokken(context_blokken)
    if context_md.strip():
        delen.append(context_md)
        delen.append("")

    # Deelvragen
    for deelvraag in deelvragen:
        deelvraag_id = deelvraag.get("id", "?")
        vraag_antwoord = antwoorden_index.get(deelvraag_id)
        delen.append(_render_deelvraag(deelvraag, vraag_antwoord))
        delen.append("")

    delen.append("---")
    return "\n".join(delen)


# ---------------------------------------------------------------------------
# Examen-pagina rendering
# ---------------------------------------------------------------------------


def _render_examen_pagina(data: dict[str, Any]) -> str:
    """Render één examen naar een volledige markdown-pagina."""
    examen_id = data.get("examen_id", "?")
    bron_pdf = data.get("bron_pdf", "")
    vragen = data.get("vragen", [])
    vandaag = date.today().isoformat()

    delen: list[str] = []

    # Frontmatter
    delen.append("---")
    delen.append(f"title: Voorbeeldexamen {examen_id}")
    delen.append(f"description: Examenvragen {examen_id} — schema 4.0 render.")
    delen.append("tags: [examen, voorbeeldvragen]")
    delen.append("gegenereerd_uit: tools/examen/render_merged_v4.py")
    delen.append(f"gegenereerd_op: {vandaag}")
    delen.append("---")
    delen.append("")

    # H1 titel
    delen.append(f"# Voorbeeldexamen {examen_id}")
    delen.append("")

    if bron_pdf:
        delen.append(f"*Bron*: {bron_pdf}")
        delen.append("")

    # Statistieken
    totaal = len(vragen)
    met_antwoord = sum(1 for v in vragen if v.get("antwoord") is not None)
    delen.append(f"**{totaal} vraag-eenheden** — {met_antwoord} met antwoord")
    delen.append("")

    # Vraag-eenheden
    for vraag in vragen:
        delen.append(_render_vraag_eenheid(vraag))
        delen.append("")

    return "\n".join(delen).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Index-pagina rendering
# ---------------------------------------------------------------------------


def _render_index_pagina(examen_data_list: list[dict[str, Any]]) -> str:
    """Render de index-pagina met overzichtstabel."""
    vandaag = date.today().isoformat()

    delen: list[str] = []

    delen.append("---")
    delen.append("title: Voorbeeldexamens")
    delen.append(
        "description: Overzicht van alle voorbeeldexamens met examenvragen "
        "(schema 4.0, ADR-024)."
    )
    delen.append("tags: [examen, voorbeeldvragen, overzicht]")
    delen.append("gegenereerd_uit: tools/examen/render_merged_v4.py")
    delen.append(f"gegenereerd_op: {vandaag}")
    delen.append("---")
    delen.append("")

    delen.append("# Voorbeeldexamens")
    delen.append("")
    delen.append(
        "Overzicht van alle beschikbare voorbeeldexamens. "
        "Elke pagina toont de vraag-eenheden met context-blokken, "
        "deelvragen en (waar beschikbaar) uitgewerkte antwoorden. "
        "Antwoord-callouts zijn standaard ingeklapt — klik om te openen."
    )
    delen.append("")

    # Tabel
    delen.append("| Examen | Vraag-eenheden | Herkomst | Pagina |")
    delen.append("| --- | ---: | --- | --- |")

    for data in sorted(examen_data_list, key=lambda d: d.get("examen_id", "")):
        examen_id = data.get("examen_id", "?")
        vragen = data.get("vragen", [])
        totaal = len(vragen)
        # Herkomst: meest voorkomende
        herkomsten = [
            v.get("interpretatie", {}).get("vraag_herkomst", "")
            for v in vragen
            if v.get("interpretatie")
        ]
        herkomst = herkomsten[0] if herkomsten else "?"
        if len(set(herkomsten)) > 1:
            herkomst = "hybride"
        link = f"[[{examen_id}]]"
        delen.append(f"| {examen_id} | {totaal} | {herkomst} | {link} |")

    delen.append("")

    return "\n".join(delen).rstrip() + "\n"


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
