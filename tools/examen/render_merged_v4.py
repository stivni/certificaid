"""Render _merged/<examen>.json (schema 4.0) naar Quartz-markdown, gegroepeerd per programmaonderdeel.

Output:
    content/voorbeeldexamens/po-<code>.md  — één pagina per programmaonderdeel (bv. po-1.1.md)
    content/voorbeeldexamens/index.md      — overzicht met links + telling per PO

Vragen worden gegroepeerd op `interpretatie.programmaonderdeel_ids[]`. Een
vraag met twee PO-codes verschijnt in beide PO-pagina's. PO-codes en titels
worden gelezen uit `data/programma/programma.json`.

CLI::

    python3 -m tools.examen.render_merged_v4          # alle PO-pagina's + index
    python3 -m tools.examen.render_merged_v4 --po 1.1
    python3 -m tools.examen.render_merged_v4 --po 2.4

Schema 4.0 structuur per vraag:
    {
      "vraag_id": "...",
      "interpretatie": { schema 1.2, incl. programmaonderdeel_ids[] },
      "antwoord": { schema 1.1 } | null,
      "segment_meta": { ... }
    }

Templates in tools/examen/templates/ (Jinja2).
Deterministisch, idempotent.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parents[2]
MERGED_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_merged"
CLUSTERS_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_clusters"
PROGRAMMA_JSON = REPO_ROOT / "data" / "programma" / "programma.json"
OUTPUT_DIR = REPO_ROOT / "content" / "voorbeeldexamens"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

# Examens die als "nieuw toegevoegd" worden gerenderd: badge in herkomst-regel
# + aparte kolom in de index. Verwijder een examen-id zodra zijn nieuwigheid
# in de UI is afgekoeld (bv. na een paar weken).
NEW_EXAMENS: set[str] = {"2010-2"}

# Cluster-cache: laadt _clusters/<po>.json on demand
_CLUSTER_CACHE: dict[str, dict[str, Any] | None] = {}

_CONFIDENCE_ICOON: dict[str, str] = {
    # Schema 2.1 v1.5 confidence-tokens (canoniek)
    "geciteerd": "📖",
    "afgeleid": "🔗",
    "verondersteld": "🤖",
    "betwijfeld": "❓",
    "weerlegd": "❌",
    # Schema 1.1 backward-compat (examenvraag-antwoorden)
    "grounded": "📖",   # gemapt naar geciteerd
    "inferred": "🔗",   # gemapt naar afgeleid (logische conclusie uit bronnen)
}

# Alle iconen om dubbele markers te detecteren (agent zet vaak per-claim
# iconen in `tekst`; renderer mag dan geen blok-niveau icoon meer toevoegen).
_ALLE_ICONEN: set[str] = set(_CONFIDENCE_ICOON.values()) | {"⚖️", "🤖"}

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


def _bold_vraag_zin(tekst: str) -> str:
    """Bold de laatste zin als die met `?` eindigt — markeert de 'echte vraag'.

    Werkt consistent voor zowel mc_keuze `vraagstelling` (typisch één zin
    eindigend op `?`) als voor casus_context (typisch lange casus + vraag-zin
    aan het eind). J/F-stellingen eindigen op `.` en blijven plain.
    """
    tekst = tekst.strip()
    if not tekst.endswith("?"):
        return tekst
    match = re.match(r"(.*?)([^.!?\n]+\?)\s*$", tekst, re.DOTALL)
    if not match:
        return f"**{tekst}**"
    prefix, vraag_zin = match.group(1).strip(), match.group(2).strip()
    if prefix:
        return f"{prefix}\n\n**{vraag_zin}**"
    return f"**{vraag_zin}**"


def _callout(soort: str, titel: str, body: str, *, collapsed: bool = False) -> str:
    """Bouw een Quartz-callout block.

    collapsed=True voegt '-' toe na het type, waardoor de callout
    standaard ingeklapt is.
    """
    suffix = "-" if collapsed else ""
    kop = f"> [!{soort}]{suffix} {titel}"
    if not body.strip():
        return kop
    # Blank quoted regel tussen kop en body. Voorkomt dat de Quartz/Obsidian
    # callout-parser de eerste body-regel als deel van de titel interpreteert
    # — vooral relevant bij geneste callouts of wanneer body met een
    # cursief-marker (`_` of `*`) begint.
    body_geprefixt = _prefix_regels(body, "> ")
    return f"{kop}\n>\n{body_geprefixt}"


def _confidence_icoon(blok: dict[str, Any]) -> str:
    """Blok-niveau confidence-icoon (met leading space).

    Skip als de tekst van het blok al eindigt op een confidence-icoon —
    dat betekent dat de agent per-claim markers in de tekst zet en het
    blok-niveau icoon zou een dubbele zijn.
    """
    c = blok.get("confidence", "")
    if c not in _CONFIDENCE_ICOON:
        return ""
    tekst = (blok.get("tekst") or "").rstrip()
    for marker in _ALLE_ICONEN:
        if tekst.endswith(marker):
            return ""
    return f" {_CONFIDENCE_ICOON[c]}"


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
        # Bold de laatste zin als die met `?` eindigt (= de "echte vraag" die
        # vaak na een casus staat). Consistent met _render_deelvraag_data
        # waar mc_keuze + open vraagstellingen ook bold krijgen als ze met `?`
        # eindigen — zodat de "echte vraag" altijd visueel onderscheidbaar is.
        return _bold_vraag_zin(tekst)

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

    if blok_type == "groepsschema":
        # Render als Mermaid diagram (Quartz heeft mermaid=True default in OFM).
        knopen = blok.get("knopen", [])
        relaties = blok.get("relaties", [])
        kop = blok.get("kop", "")
        beschrijving = (blok.get("beschrijving") or "").strip()
        if not relaties:
            # Geen typed relaties — fallback op beschrijving
            return f"*{kop}*: {beschrijving}" if kop else beschrijving
        regels = ["```mermaid", "graph TD"]
        # Declareer knopen expliciet zodat ook losse knopen verschijnen
        for n in knopen:
            regels.append(f"    {n}[{n}]")
        for r in relaties:
            van = r.get("van", "")
            naar = r.get("naar", "")
            pct = str(r.get("percentage", "")).replace("%", "%").strip()
            label = f"|{pct}|" if pct else ""
            regels.append(f"    {van} -->{label} {naar}")
        regels.append("```")
        delen = []
        if kop:
            delen.append(f"**{kop}**")
            delen.append("")
        delen.append("\n".join(regels))
        if beschrijving:
            delen.append("")
            delen.append(f"_{beschrijving}_")
        return "\n".join(delen)

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
        # Geen wrap — bron-tekst bevat typisch al `**bold**` markers voor de
        # belangrijkste delen. Een extra `**_..._**` wrap zou de inline-bold
        # mixen met de outer-bold (`**_**foo** bar_**` = parser-mess).
        tekst = (blok.get("tekst") or "").strip()
        return f"{tekst}{conf}"

    if blok_type == "grondslag":
        # Geen cursief-wrap meer — bron-tekst kan zelf `**bold**` of `*italic*`
        # markers bevatten die met de outer-wrap conflicteren. Plain tekst +
        # "Bron"-suffix op nieuwe regel.
        tekst = (blok.get("tekst") or "").strip()
        wetsref = blok.get("wetsref", "")
        bron_zin = f"  \n*Bron: {wetsref}*" if wetsref else ""
        return f"{tekst}{conf}{bron_zin}"

    if blok_type == "definitie":
        lemma = blok.get("lemma", "")
        uitleg = (blok.get("uitleg") or "").strip()
        if not lemma and not uitleg:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
        return f"**{lemma}**: {uitleg}{conf}"

    if blok_type == "boeking":
        regels = blok.get("regels", [])
        toelichting = blok.get("toelichting", "")
        if not regels:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
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
        if not formule and not stappen:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
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
        if not stappen:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
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
        if not rows:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
        return _markdown_tabel(headers, rows) + conf

    if blok_type == "opsomming":
        items = blok.get("items", [])
        if not items:
            tekst = (blok.get("tekst") or "").strip()
            if tekst:
                return f"{tekst}{conf}"
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


def _antwoord_callout_titel(deelvraag: dict[str, Any]) -> str:
    """Type-bewuste callout-titel met consistent suffix "(klik om te openen)".

    Voor juist_fout geen type-hint in titel — de badge boven de stelling zegt
    al "Juist of fout?", redundantie vermijden. Voor mc_keuze wel "Welke
    optie(s)?" als type-hint (meerdere antwoorden mogelijk). Open is generic.
    """
    vraagtype = deelvraag.get("vraagtype", "open")
    if vraagtype == "mc_keuze":
        return "Welke optie(s)? (klik om te openen)"
    return "Antwoord (klik om te openen)"


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
        return _callout("success", _antwoord_callout_titel(deelvraag), body, collapsed=True)

    status = vraag_antwoord.get("antwoord_status", "")

    if status == "wacht_op_vraag_generatie":
        body = _PLACEHOLDER_WACHT
        return _callout("success", _antwoord_callout_titel(deelvraag), body, collapsed=True)

    if status == "hard_blocked":
        gap = vraag_antwoord.get("record_gap_report") or {}
        beschrijving = gap.get("beschrijving", "")
        body = f"_Antwoord blokkeert op ontbrekend record._ {beschrijving}"
        return _callout("success", _antwoord_callout_titel(deelvraag), body, collapsed=True)

    # Render zodra blokken[] aanwezig zijn — accepteert alle status-varianten
    # ("beantwoord", "beantwoord_zonder_cijfers", "betwijfeld", "niet_beantwoordbaar",
    # "topic_only_kader", etc.). Agents kunnen genuanceerde statussen leveren;
    # placeholder enkel wanneer er écht geen inhoud is.
    blokken = vraag_antwoord.get("blokken", [])
    if blokken:
        vraagtype = deelvraag.get("vraagtype", "open")
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

        # Status-flag tonen bij niet-standaard status
        if status and status != "beantwoord":
            label_map = {
                "beantwoord_zonder_cijfers": "_Antwoord zonder concrete cijfers (bijlage ontbreekt)._",
                "betwijfeld": "_Antwoord onder voorbehoud._",
                "niet_beantwoordbaar": "_Vraag niet volledig beantwoordbaar; framework geleverd._",
                "topic_only_kader": "_Topic-only herinnering; framework geleverd._",
                "topic_only": "_Topic-only herinnering; framework geleverd._",
            }
            label = label_map.get(status, f"_Status: {status}._")
            delen.append(label)

        # Typed blokken (motivering bij mc/jf, of volledig antwoord bij open)
        blokken_md = _render_antwoord_blokken(blokken)
        if blokken_md.strip():
            delen.append(blokken_md)

        body = "\n\n".join(d for d in delen if d.strip())
        if not body.strip():
            body = "_Antwoord aangemerkt als beantwoord (geen verdere toelichting)._"
        return _callout("success", _antwoord_callout_titel(deelvraag), body, collapsed=True)

    if status == "beantwoord":
        body = "_Antwoord aangemerkt als beantwoord (geen verdere toelichting)._"
        return _callout("success", _antwoord_callout_titel(deelvraag), body, collapsed=True)

    # Status zonder blokken (en niet wacht/hard_blocked) → placeholder
    body = _PLACEHOLDER_GEEN_ANTWOORD
    return _callout("success", "Antwoord (klik om te openen)", body, collapsed=True)


# ---------------------------------------------------------------------------
# Deelvraag-rendering
# ---------------------------------------------------------------------------


def _is_placeholder_antwoord(vraag_antwoord: dict[str, Any] | None) -> bool:
    """True als het antwoord een lege placeholder is (geen echte inhoud).

    Statussen die ECHTE inhoud opleveren: 'beantwoord' (heeft blokken /
    gekozen_optie_id / oordeel) en 'hard_blocked' (heeft gap-report met
    beschrijving). Andere statussen + None geven alleen een placeholder-tekst
    en zijn visueel ruis als ze per-deelvraag worden gerepliceerd.
    """
    if vraag_antwoord is None:
        return True
    status = vraag_antwoord.get("antwoord_status", "")
    return status not in ("beantwoord", "hard_blocked")


def _render_deelvraag_data(
    deelvraag: dict[str, Any],
    vraag_antwoord: dict[str, Any] | None,
    env: Environment,
) -> str:
    """Bereid deelvraag-data voor en delegeer naar _deelvraag.md.j2.

    juist_fout-deelvragen krijgen een inline badge "Juist of fout" als
    visuele marker, zodat ze duidelijk onderscheiden zijn van vraag-context
    en mengbaar zijn met andere typen binnen één vraag-eenheid. CSS-styling
    via `.jf-badge` in `quartz-custom/styles/custom.scss`.
    """
    volledigheid = deelvraag.get("volledigheid", "volledig")
    vraagtype = deelvraag.get("vraagtype", "open")
    vraagstelling_raw = (deelvraag.get("vraagstelling") or "").strip() or None

    # Vraagstelling-styling per type:
    # - juist_fout: inline J/F-badge + stelling via expliciete spans (CSS
    #   Grid hanging-indent). De stelling eindigt typisch op `.`, geen bold.
    # - mc_keuze + open: bold-vraag-rule via _bold_vraag_zin — bold de zin
    #   die met `?` eindigt. Consistent met casus_context-rendering, zodat
    #   de "echte vraag" overal visueel onderscheidbaar is.
    if (
        vraagtype == "juist_fout"
        and vraagstelling_raw
        and volledigheid in ("volledig", "fragment")
    ):
        vraagstelling = (
            f'<span class="jf-badge">Juist of fout?</span>'
            f'<span class="jf-stelling">{vraagstelling_raw}</span>'
        )
    elif vraagstelling_raw:
        vraagstelling = _bold_vraag_zin(vraagstelling_raw)
    else:
        vraagstelling = vraagstelling_raw

    # MC-opties: normaliseer naar list[dict] met id en tekst (id behouden — MC-opties wél gelabeld)
    opties_raw = deelvraag.get("opties", []) or []
    opties = [
        {"id": o.get("id", "?"), "tekst": (o.get("tekst") or "").strip()}
        for o in opties_raw
    ]

    topic_only_onderwerp = deelvraag.get("topic_only_onderwerp", "") or ""

    # Geen antwoord-callout voor topic_only deelvragen — er is geen vraag,
    # dus een "wacht op antwoord"-placeholder zou misleidend zijn.
    if volledigheid == "topic_only":
        antwoord_callout_md = ""
    else:
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


def _formatteer_herkomst(
    examen_id: str,
    vraag_herkomst: str,
    programmaonderdeel_ids: list[str] | None = None,
) -> str:
    """Formatteer een kleine italic-notitie over examen-herkomst + PO('s).

    PRUTS: pas de notitie-string hier aan.

    Voorbeelden:
      ("2013-1", "officieel", ["1.7"])
        → "Examen 2013-1 · PO 1.7"
      ("2024-1", "herinnering", ["3.0"])
        → "Examen 2024-1 (uit herinnering gereconstrueerd) · PO 3.0"
      ("2013-2", "officieel", ["1.6", "3.0"])
        → "Examen 2013-2 · PO 1.6 + 3.0"
    """
    if vraag_herkomst == "herinnering":
        basis = f"Examen {examen_id} (uit herinnering gereconstrueerd)"
    elif vraag_herkomst == "hybride":
        basis = f"Examen {examen_id} (hybride bron)"
    else:
        basis = f"Examen {examen_id}"
    # NB: 🆕-marker zit niet hier — die staat in de callout-titel (zie
    # _is_nieuwe_vraag()). Hier blijft de italic-herkomst plain.
    if programmaonderdeel_ids:
        po_str = " + ".join(programmaonderdeel_ids)
        return f"{basis} · PO {po_str}"
    return basis


def _is_nieuwe_vraag(
    examen_id: str,
    cluster_leden: list[dict[str, Any]] | None = None,
) -> bool:
    """Bepaal of een vraag (canonical of een cluster-lid) uit een NEW_EXAMENS-examen komt."""
    if examen_id in NEW_EXAMENS:
        return True
    for lid in cluster_leden or []:
        li = lid.get("interpretatie", {}) or {}
        if li.get("examen_id", "") in NEW_EXAMENS:
            return True
    return False


def _groepeer_per_cluster(
    vragen: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    """Groepeer cluster-leden naar één canonieke render-entry.

    De **echte canonical** wordt opgehaald uit `_clusters/<po>.json` (waar
    apply_cluster_review.py de alphabetic-first cluster-canonical heeft
    vastgelegd). Dat is de vraag-id waar het antwoord op staat. Eerdere
    versie nam "first-encountered" als canonical, wat tot rendering-fouten
    leidde wanneer render-volgorde ≠ alphabetic-volgorde (cluster-lid
    zonder antwoord werd ten onrechte als canonical gerenderd).

    Returns:
        (render_vragen, leden_per_canonical_vraag_id)
        - render_vragen: gefilterde lijst — alleen de canonical per cluster
          komt in render, op de positie van de eerst-encountered lid (om
          natuurlijke volgorde van het examen te behouden).
        - leden_per_canonical_vraag_id: dict van canonical_vraag_id → ALLE
          leden (incl. canonical) in input-volgorde.
    """
    # Bouw een lookup: cluster_id → canonical vraag_id, geladen uit
    # cluster-files via _laad_cluster_file (gecached).
    def _canonical_voor_cluster(cid: str, po_codes: list[str]) -> str | None:
        for po in po_codes:
            cl_file = _laad_cluster_file(po)
            if not cl_file:
                continue
            for c in cl_file.get("clusters", []):
                if c.get("cluster_id") == cid:
                    voork = c.get("voorkomens", [])
                    if voork:
                        # Alphabetic first → matcht apply_cluster_review.py
                        return sorted(v["vraag_id"] for v in voork)[0]
        return None

    seen_clusters: set[str] = set()
    leden_per_cluster: dict[str, list[dict[str, Any]]] = {}
    canonical_per_cluster: dict[str, str] = {}
    positie_per_cluster: dict[str, int] = {}  # positie eerst-encountered lid

    # Eerste pass: verzamel alle leden per cluster, bepaal canonical
    for idx, v in enumerate(vragen):
        interp = v.get("interpretatie", {}) or {}
        cid = interp.get("cluster_id")
        if not cid:
            continue
        leden_per_cluster.setdefault(cid, []).append(v)
        if cid not in seen_clusters:
            seen_clusters.add(cid)
            positie_per_cluster[cid] = idx
            # Echte canonical uit cluster-file
            po_codes = interp.get("programmaonderdeel_ids") or []
            real_canonical = _canonical_voor_cluster(cid, po_codes)
            canonical_per_cluster[cid] = real_canonical or v["vraag_id"]

    # Tweede pass: bouw render_vragen
    # - Singletons in natuurlijke volgorde
    # - Per cluster: gebruik canonical-vraag op positie van eerst-encountered lid
    render_vragen: list[dict[str, Any]] = []
    clusters_geplaatst: set[str] = set()
    # Maak een dict van vraag_id → vraag voor snelle canonical-lookup
    vraag_by_id = {v["vraag_id"]: v for v in vragen}

    for idx, v in enumerate(vragen):
        interp = v.get("interpretatie", {}) or {}
        cid = interp.get("cluster_id")
        if cid:
            if cid in clusters_geplaatst:
                continue
            clusters_geplaatst.add(cid)
            canonical_vid = canonical_per_cluster.get(cid)
            canonical_vraag = vraag_by_id.get(canonical_vid) if canonical_vid else None
            # Fallback: als canonical niet in deze vragen-lijst zit (zou raar zijn),
            # gebruik eerst-encountered
            render_vragen.append(canonical_vraag if canonical_vraag else v)
        else:
            render_vragen.append(v)

    # Mappen leden → canonical_vraag_id voor render-tijd lookup
    leden_per_canonical: dict[str, list[dict[str, Any]]] = {}
    for cid, leden in leden_per_cluster.items():
        canonical_vid = canonical_per_cluster.get(cid)
        if canonical_vid:
            leden_per_canonical[canonical_vid] = leden

    return render_vragen, leden_per_canonical


def _laad_cluster_file(po_code: str) -> dict[str, Any] | None:
    """Cached loader voor `_clusters/<po>.json`. None als file ontbreekt."""
    if po_code in _CLUSTER_CACHE:
        return _CLUSTER_CACHE[po_code]
    pad = CLUSTERS_DIR / f"{po_code}.json"
    if not pad.is_file():
        _CLUSTER_CACHE[po_code] = None
        return None
    _CLUSTER_CACHE[po_code] = json.loads(pad.read_text(encoding="utf-8"))
    return _CLUSTER_CACHE[po_code]


def _cluster_badge_regel(
    cluster_id: str,
    cluster_verdict: str,
    huidige_vraag_id: str,
    po_codes: list[str],
) -> str:
    """Bouw een callout-body-regel met cluster-info (zonder `> `-prefix).

    Voorbeeld output:
        🔁 **2× bevraagd** (echt duplicaat) — ook in [[#2014-1-vr7]]
    """
    for po in po_codes:
        cluster_file = _laad_cluster_file(po)
        if not cluster_file:
            continue
        for cluster in cluster_file.get("clusters", []):
            if cluster.get("cluster_id") != cluster_id:
                continue
            voorkomens = cluster.get("voorkomens", [])
            n = len(voorkomens)
            anderen = [v["vraag_id"] for v in voorkomens if v["vraag_id"] != huidige_vraag_id]
            if not anderen:
                return ""
            verdict_label = {
                "echt_duplicaat": "echt duplicaat",
                "varianten": "varianten",
            }.get(cluster_verdict, cluster_verdict)
            anderen_links = ", ".join(f"[[#{v}|{v}]]" for v in anderen)
            return f"🔁 **{n}× bevraagd** ({verdict_label}) — ook in {anderen_links}"
    return ""


def _render_vraag_eenheid(
    vraag: dict[str, Any],
    env: Environment | None = None,
    cluster_leden: list[dict[str, Any]] | None = None,
) -> str:
    """Bereid vraag-eenheid-data voor en delegeer naar _vraag_eenheid.md.j2.

    Args:
        vraag: de canonical vraag (volgt examen-merge-volgorde).
        env: Jinja-env, anders default.
        cluster_leden: indien gegeven, alle leden (incl. canonical) van een
            cluster. De herkomst-regel toont alle examens, en alle leden
            krijgen een eigen anchor bovenaan. De vraag-body komt van de
            canonical; varianten worden NIET separately gerenderd (MVP).
    """
    if env is None:
        env = _get_env()

    vraag_id = vraag["vraag_id"]
    interpretatie = vraag.get("interpretatie", {})
    antwoord = vraag.get("antwoord")

    onderwerp = interpretatie.get("vraag_onderwerp", "")
    examen_id = interpretatie.get("examen_id", "")
    vraag_herkomst = interpretatie.get("vraag_herkomst", "officieel")
    programmaonderdeel_ids = interpretatie.get("programmaonderdeel_ids") or []
    context_blokken = interpretatie.get("context_blokken", [])
    deelvragen = interpretatie.get("vragen", [])

    antwoorden_index = _bouw_antwoorden_index(antwoord)

    # Complexe context-blokken blijven in Python
    context_md = _render_context_blokken(context_blokken)

    # Herkomst-regel: bij cluster combineer alle examens, anders enkel canonical
    if cluster_leden and len(cluster_leden) > 1:
        examen_items: list[str] = []
        for lid in cluster_leden:
            li = lid.get("interpretatie", {}) or {}
            e_id = li.get("examen_id", "")
            l_vid = lid["vraag_id"]
            l_herkomst = li.get("vraag_herkomst", "officieel")
            suffix = ""
            if l_herkomst == "herinnering":
                suffix = " (herinnering)"
            elif l_herkomst == "hybride":
                suffix = " (hybride)"
            examen_items.append(f"{e_id} ({l_vid}){suffix}")
        po_str = " + ".join(programmaonderdeel_ids) if programmaonderdeel_ids else ""
        herkomst_regel = (
            f"Examens {' & '.join(examen_items)}"
            + (f" · PO {po_str}" if po_str else "")
        )
    else:
        herkomst_regel = (
            _formatteer_herkomst(examen_id, vraag_herkomst, programmaonderdeel_ids)
            if examen_id
            else ""
        )

    # Per deelvraag: eigen antwoord-callout. Verschillende typen binnen één
    # vraag-eenheid worden ondersteund — bv. 3 juist_fout + 1 open vraag.
    # Type-specifieke markering (J/F-badge, callout-titel) zit in
    # _render_deelvraag_data + _render_antwoord_callout.
    deelvragen_md = [
        _render_deelvraag_data(dv, antwoorden_index.get(dv.get("id", "?")), env)
        for dv in deelvragen
    ]

    # De vraag wordt in een collapsible question-callout gewrapt (ADR-032).
    # Elke regel van de body krijgt '> '-prefix (Obsidian/Quartz callout-
    # blockquote-syntax). Geneste callouts (antwoord-callouts in deelvragen)
    # krijgen daardoor automatisch '> > '.
    #
    # Geen Jinja-template hier: trim_blocks=True maakt block-tag-newlines
    # onbetrouwbaar voor een nested-callout-layout die strict '> '-prefixen
    # vereist. Pure-Python is voorspelbaarder.
    titel = onderwerp or "Vraag"
    # 🆕-marker vóór de titel zodra de vraag (canonical of een cluster-lid)
    # uit een examen in NEW_EXAMENS komt. Zo valt het op in zowel het ingeklapt
    # als uitgeklapt callout-overzicht en blijft de herkomst-italic plain.
    if _is_nieuwe_vraag(examen_id, cluster_leden):
        titel = f"🆕 {titel}"
    # Outer callout-type wordt `topic` (i.p.v. `question`) wanneer ALLE
    # deelvragen topic_only zijn — visueel grijzer in CSS, signaal aan de
    # student dat er hier geen echt antwoord-werk is (geen vraagstelling).
    alle_topic_only = (
        len(deelvragen) > 0
        and all(dv.get("volledigheid") == "topic_only" for dv in deelvragen)
    )
    outer_callout_type = "topic" if alle_topic_only else "question"
    # Anchors: bij cluster alle leden, anders alleen canonical
    if cluster_leden and len(cluster_leden) > 1:
        anchor_ids = [lid["vraag_id"] for lid in cluster_leden]
    else:
        anchor_ids = [vraag_id]
    regels: list[str] = [f'<a id="{aid}"></a>' for aid in anchor_ids]
    regels.append("")
    regels.append(f"> [!{outer_callout_type}]- {titel}")
    if herkomst_regel:
        regels.append(f"> *{herkomst_regel}*")
        regels.append(">")

    # Cluster-badge: vraag is onderdeel van een gereviewde cluster
    cluster_id = interpretatie.get("cluster_id")
    if cluster_id:
        if cluster_leden and len(cluster_leden) > 1:
            # Multi-lid: herkomst-regel toont al alle examens; korte badge
            verdict = interpretatie.get("cluster_verdict", "")
            verdict_label = {
                "echt_duplicaat": "echt duplicaat",
                "varianten": "varianten",
            }.get(verdict, verdict)
            n = len(cluster_leden)
            regels.append(f"> 🔁 **{n}× bevraagd** ({verdict_label})")
            regels.append(">")
        else:
            # Single-lid fallback (cluster info aanwezig maar leden niet doorgegeven)
            badge = _cluster_badge_regel(
                cluster_id=cluster_id,
                cluster_verdict=interpretatie.get("cluster_verdict", ""),
                huidige_vraag_id=vraag_id,
                po_codes=programmaonderdeel_ids,
            )
            if badge:
                regels.append(f"> {badge}")
                regels.append(">")

    if context_md.strip():
        regels.append(_prefix_regels(context_md.strip(), "> "))
        regels.append(">")
    for i, dv in enumerate(deelvragen_md):
        regels.append(_prefix_regels(dv, "> "))
        if i < len(deelvragen_md) - 1:
            regels.append(">")
    # Geen hr-divider tussen vraag-eenheden — de collapsible callout-border
    # geeft al de visuele scheiding. ADR-032 §6 + custom.scss styling.
    return "\n".join(regels)


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
# Data-voorbereiding: groepering per programmaonderdeel
# ---------------------------------------------------------------------------


def _laad_po_catalogus() -> dict[str, str]:
    """Lees code → titel mapping uit programma.json."""
    data = json.loads(PROGRAMMA_JSON.read_text(encoding="utf-8"))
    return {po["code"]: po["titel"] for po in data["programmaonderdelen"]}


def _natural_sort_key(s: str) -> list:
    """Natural-sort: 'vr2A' < 'vr10A' (zie ook merge_examen_artefacten._natural_sort_key)."""
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", s)]


def _groepeer_per_po(
    examen_data_list: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    """Verzamel vragen per programmaonderdeel-code.

    Een vraag verschijnt onder elk PO uit `interpretatie.programmaonderdeel_ids`.
    Multi-PO vragen verschijnen dus in meerdere PO-pagina's. Sortering binnen
    PO: chronologisch op examen_id, dan natural-sort op vraag_id.
    """
    per_po: dict[str, list[dict[str, Any]]] = {}
    for examen in examen_data_list:
        examen_id = examen.get("examen_id", "?")
        for vraag in examen.get("vragen", []):
            interp = vraag.get("interpretatie") or {}
            po_ids = interp.get("programmaonderdeel_ids") or []
            # Vraag krijgt examen_id-context mee via _bron_examen-veld (niet
            # persistent, alleen voor sortering en filtering tijdens render).
            vraag_met_context = dict(vraag)
            vraag_met_context["_bron_examen"] = examen_id
            for po in po_ids:
                per_po.setdefault(po, []).append(vraag_met_context)

    # Sortering: recenter examen eerst (aflopend op examen_id), maar binnen
    # examen oplopend op vraag_id. Python's sort is stable → twee-pass.
    for po, vragen in per_po.items():
        vragen.sort(key=lambda v: _natural_sort_key(v.get("vraag_id", "")))
        vragen.sort(key=lambda v: v["_bron_examen"], reverse=True)
    return per_po


# ---------------------------------------------------------------------------
# PO-pagina rendering
# ---------------------------------------------------------------------------


def _po_slug(po_code: str) -> str:
    """Frontmatter-tag-vriendelijke slug: '1.1' → '1-1'."""
    return po_code.replace(".", "-")


def _render_po_pagina(
    po_code: str,
    po_titel: str,
    vragen: list[dict[str, Any]],
) -> str:
    """Render één PO-pagina via Jinja2-template."""
    env = _get_env()
    tmpl = env.get_template("po_pagina.md.j2")

    vandaag = date.today().isoformat()
    # Groepeer cluster-leden: canonical houdt de positie, andere leden worden
    # samengenest in de combined-herkomst-regel + multi-anchor.
    render_vragen, leden_per_canonical = _groepeer_per_cluster(vragen)
    vraag_eenheden_md = [
        _render_vraag_eenheid(
            v, env,
            cluster_leden=leden_per_canonical.get(v["vraag_id"]),
        )
        for v in render_vragen
    ]

    examens = sorted({v["_bron_examen"] for v in vragen})
    totaal_voorkomens = len(vragen)
    totaal = len(render_vragen)  # na cluster-dedup
    met_antwoord = sum(1 for v in render_vragen if v.get("antwoord") is not None)
    n_clusters = sum(1 for v in render_vragen if leden_per_canonical.get(v["vraag_id"]))

    inhoud = tmpl.render(
        po_code=po_code,
        po_titel=po_titel,
        po_slug=_po_slug(po_code),
        vragen=vragen,
        vraag_eenheden_md=vraag_eenheden_md,
        examens=examens,
        totaal=totaal,
        totaal_voorkomens=totaal_voorkomens,
        n_clusters=n_clusters,
        met_antwoord=met_antwoord,
        vandaag=vandaag,
    )
    return inhoud.rstrip() + "\n"


# ---------------------------------------------------------------------------
# Index-pagina rendering
# ---------------------------------------------------------------------------


def _render_index_pagina(
    per_po: dict[str, list[dict[str, Any]]],
    po_catalogus: dict[str, str],
) -> str:
    """Render de index met overzichtstabel + lijst onbezette PO's."""
    env = _get_env()
    tmpl = env.get_template("index_pagina.md.j2")
    vandaag = date.today().isoformat()

    sorteer_key = lambda code: _natural_sort_key(code)

    po_overzicht = []
    totaal_vragen = 0
    totaal_nieuw = 0
    for code in sorted(per_po.keys(), key=sorteer_key):
        vragen = per_po[code]
        met_antwoord = sum(1 for v in vragen if v.get("antwoord") is not None)
        # Een vraag is "nieuw" als canonical of een cluster-lid tot NEW_EXAMENS behoort.
        nieuw_count = 0
        for v in vragen:
            interp = v.get("interpretatie", {}) or {}
            examens_in_vraag = {interp.get("examen_id", "")}
            for lid in v.get("cluster_leden", []) or []:
                li = lid.get("interpretatie", {}) or {}
                examens_in_vraag.add(li.get("examen_id", ""))
            if examens_in_vraag & NEW_EXAMENS:
                nieuw_count += 1
        po_overzicht.append({
            "code": code,
            "titel": po_catalogus.get(code, "?"),
            "slug": _po_slug(code),
            "totaal": len(vragen),
            "met_antwoord": met_antwoord,
            "nieuw": nieuw_count,
        })
        totaal_vragen += len(vragen)
        totaal_nieuw += nieuw_count

    onbezette_pos = [
        {"code": code, "titel": titel}
        for code, titel in sorted(po_catalogus.items(), key=lambda kv: sorteer_key(kv[0]))
        if code not in per_po
    ]

    inhoud = tmpl.render(
        po_overzicht=po_overzicht,
        totaal_vragen=totaal_vragen,
        totaal_nieuw=totaal_nieuw,
        nieuw_examens=sorted(NEW_EXAMENS),
        onbezette_pos=onbezette_pos,
        vandaag=vandaag,
    )
    return inhoud.rstrip() + "\n"


def _render_nieuw_pagina(
    per_po: dict[str, list[dict[str, Any]]],
    po_catalogus: dict[str, str],
) -> str:
    """Render aparte index van vraag-eenheden uit recent toegevoegde examens.

    Geeft lege string terug als er geen vragen uit `NEW_EXAMENS` zijn — caller
    verwijdert dan de file (auto-cleanup als examen uit NEW_EXAMENS gehaald).
    """
    if not NEW_EXAMENS:
        return ""

    vandaag = date.today().isoformat()
    nieuw_examens = sorted(NEW_EXAMENS)

    # Verzamel per PO de vragen waarvan canonical of cluster-lid in NEW_EXAMENS zit.
    items_per_po: dict[str, list[dict[str, Any]]] = {}
    totaal_nieuw = 0
    for po_code in sorted(per_po.keys(), key=_natural_sort_key):
        po_titel = po_catalogus.get(po_code, "?")
        for v in per_po[po_code]:
            interp = v.get("interpretatie", {}) or {}
            examen_id = interp.get("examen_id", "")
            cluster_leden = v.get("cluster_leden") or []
            betrokken: set[str] = {examen_id}
            for lid in cluster_leden:
                li = lid.get("interpretatie", {}) or {}
                betrokken.add(li.get("examen_id", ""))
            nieuw_ids = betrokken & NEW_EXAMENS
            if not nieuw_ids:
                continue
            vraag_id = v.get("vraag_id", "")
            onderwerp = interp.get("vraag_onderwerp") or "(geen onderwerp)"
            anker_slug = vraag_id.lower().replace(".", "-")
            items_per_po.setdefault(po_code, []).append({
                "vraag_id": vraag_id,
                "examen_id": examen_id,
                "onderwerp": onderwerp,
                "po_code": po_code,
                "po_titel": po_titel,
                "anker": anker_slug,
                "examens_nieuw": sorted(nieuw_ids),
                "is_cluster": len(cluster_leden) > 1,
            })
            totaal_nieuw += 1

    if totaal_nieuw == 0:
        return ""

    regels: list[str] = []
    regels.append("---")
    regels.append("title: 🆕 Recent toegevoegde voorbeeldexamens")
    regels.append(
        "description: Aparte index van voorbeeldexamen-vragen uit recent toegevoegde examens, "
        "gegroepeerd per programmaonderdeel."
    )
    regels.append("tags: [examen, voorbeeldvragen, nieuw]")
    regels.append("gegenereerd_uit: tools/examen/render_merged_v4.py")
    regels.append(f"gegenereerd_op: {vandaag}")
    regels.append("---")
    regels.append("")
    regels.append("# 🆕 Recent toegevoegde voorbeeldexamens")
    regels.append("")
    examens_label = ", ".join(nieuw_examens)
    eenheid_woord = "vraag-eenheid" if totaal_nieuw == 1 else "vraag-eenheden"
    regels.append(
        f"Vragen uit recent toegevoegd{'e examens' if len(nieuw_examens) > 1 else ' examen'} "
        f"**{examens_label}**, gegroepeerd per programmaonderdeel. "
        f"Totaal: **{totaal_nieuw}** {eenheid_woord}."
    )
    regels.append("")
    regels.append(
        "_De vragen zijn ook geïntegreerd in de gewone PO-pagina's (zie [[index|hoofdoverzicht]]). "
        "Deze pagina is een snelle filter zolang het examen als 'nieuw' is gemarkeerd._"
    )
    regels.append("")

    for po_code in sorted(items_per_po.keys(), key=_natural_sort_key):
        po_items = items_per_po[po_code]
        po_titel = po_catalogus.get(po_code, "?")
        regels.append(f"## PO {po_code} — {po_titel}")
        regels.append("")
        regels.append(f"_{len(po_items)} {'vraag-eenheid' if len(po_items) == 1 else 'vraag-eenheden'} · [[po-{po_code}|volledig overzicht PO {po_code}]]_")
        regels.append("")
        for item in po_items:
            link = f"[[po-{item['po_code']}#{item['anker']}|{item['vraag_id']}]]"
            cluster_suffix = " · (geclusterd met eerder examen)" if item["is_cluster"] else ""
            regels.append(f"- {link} — {item['onderwerp']}{cluster_suffix}")
        regels.append("")

    return "\n".join(regels).rstrip() + "\n"


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


def _laad_alle_merged() -> list[dict[str, Any]]:
    """Lees alle _merged/<examen>.json bestanden."""
    return [
        json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(MERGED_DIR.glob("*.json"))
    ]


def render_po(po_code: str) -> bool:
    """Render één PO-pagina. Geeft True als het bestand (her)geschreven is."""
    po_catalogus = _laad_po_catalogus()
    if po_code not in po_catalogus:
        raise ValueError(
            f"Onbekende PO-code {po_code!r}. Geldige codes: "
            f"{sorted(po_catalogus.keys(), key=_natural_sort_key)}"
        )
    per_po = _groepeer_per_po(_laad_alle_merged())
    vragen = per_po.get(po_code, [])
    if not vragen:
        print(
            f"[warn] PO {po_code} ({po_catalogus[po_code]}) heeft geen "
            f"vragen — geen pagina geschreven."
        )
        return False
    inhoud = _render_po_pagina(po_code, po_catalogus[po_code], vragen)
    uitvoer = OUTPUT_DIR / f"po-{po_code}.md"
    return _schrijf_indien_gewijzigd(uitvoer, inhoud)


def render_alle() -> dict[str, bool]:
    """Render alle PO-pagina's + index.md.

    Geeft dict naam → True als (her)geschreven. Naam-conventie:
    'po-1.1' voor PO-pagina's, 'index' voor de overzichtspagina.
    """
    po_catalogus = _laad_po_catalogus()
    per_po = _groepeer_per_po(_laad_alle_merged())
    resultaten: dict[str, bool] = {}

    for po_code in sorted(per_po.keys(), key=_natural_sort_key):
        inhoud = _render_po_pagina(po_code, po_catalogus.get(po_code, "?"), per_po[po_code])
        uitvoer = OUTPUT_DIR / f"po-{po_code}.md"
        resultaten[f"po-{po_code}"] = _schrijf_indien_gewijzigd(uitvoer, inhoud)

    # Onbekende PO's in interpretaties (niet in programma.json) zouden hier
    # opvallen — fail-loud zou kunnen maar voor nu: warning.
    onbekende = sorted(set(per_po.keys()) - set(po_catalogus.keys()), key=_natural_sort_key)
    if onbekende:
        print(
            f"[warn] PO-codes in interpretaties maar niet in programma.json: "
            f"{onbekende}"
        )

    index_inhoud = _render_index_pagina(per_po, po_catalogus)
    index_pad = OUTPUT_DIR / "index.md"
    resultaten["index"] = _schrijf_indien_gewijzigd(index_pad, index_inhoud)

    # Aparte index van recent toegevoegde examens — pas schrijven als er iets te tonen valt.
    nieuw_inhoud = _render_nieuw_pagina(per_po, po_catalogus)
    nieuw_pad = OUTPUT_DIR / "nieuw.md"
    if nieuw_inhoud:
        resultaten["nieuw"] = _schrijf_indien_gewijzigd(nieuw_pad, nieuw_inhoud)
    elif nieuw_pad.exists():
        nieuw_pad.unlink()
        resultaten["nieuw"] = True

    return resultaten


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Render examen-vragen per programmaonderdeel naar Quartz-markdown."
        )
    )
    parser.add_argument(
        "--po",
        help="Render enkel deze PO-code (bv. '1.1'). Zonder dit argument: alle PO's + index.",
    )
    args = parser.parse_args()

    if args.po:
        geschreven = render_po(args.po)
        status = "geschreven" if geschreven else "ongewijzigd (idempotent of leeg)"
        print(f"po-{args.po}: {status}")
        return 0

    resultaten = render_alle()
    for naam, geschreven in sorted(resultaten.items(), key=lambda kv: _natural_sort_key(kv[0])):
        status = "geschreven" if geschreven else "ongewijzigd"
        print(f"  {naam}: {status}")
    totaal = sum(1 for v in resultaten.values() if v)
    print(f"\n{totaal}/{len(resultaten)} bestanden (her)geschreven.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
