"""Render alle voorbeeldexamenvragen naar één Quartz-renderbare markdown-pagina.

Doel: visuele verificatie van vraag-extractie (ADR-021 v2 + ADR-022
herinterpretatie), modelantwoorden (ADR-020) en gap-rapporten over alle 7
examenbundels (~253 vragen, alle programmaonderdelen).

Output: ``content/voorbeeldexamens/alle-vragen.md`` — één pagina met TOC per
programmaonderdeel en H3-secties per vraag (incl. subvragen, herinterpretatie,
MC-opties, modelantwoord, motivering, bronnen, provenance, gap-rapport).

Gebruik::

    python3 -m tools.examen.render_alle_vragen

Geen argumenten; idempotent. Pure deterministische rendering, geen Claude API.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXAMEN_VRAGEN_DIRECTORY = REPOSITORY_ROOT / "data" / "programma" / "examen_vragen"
KLASSIFICATIE_BESTAND = (
    EXAMEN_VRAGEN_DIRECTORY / "_programmaonderdeel_classificatie.json"
)
OUTPUT_BESTAND = (
    REPOSITORY_ROOT / "content" / "voorbeeldexamens" / "alle-vragen.md"
)

PROGRAMMAONDERDEEL_ONBEKEND = "onbekend"


# ---------------------------------------------------------------------------
# Inlezen
# ---------------------------------------------------------------------------


def laad_examen_bestanden() -> list[dict[str, Any]]:
    """Laad alle examen-JSON's (skip _* metadata-bestanden)."""
    bestanden = sorted(EXAMEN_VRAGEN_DIRECTORY.glob("2*.json"))
    examens: list[dict[str, Any]] = []
    for bestand in bestanden:
        if bestand.name.startswith("_"):
            continue
        if "-labels" in bestand.name:
            continue
        examens.append(json.loads(bestand.read_text(encoding="utf-8")))
    return examens


def laad_klassificatie() -> dict[str, dict[str, Any]]:
    """Map vraag_id → klassificatie-record."""
    return json.loads(KLASSIFICATIE_BESTAND.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def prefix_regels(tekst: str, prefix: str) -> str:
    """Plaats ``prefix`` voor elke regel van ``tekst`` (voor callout-bodies)."""
    if not tekst:
        return prefix.rstrip()
    return "\n".join(prefix + regel for regel in tekst.splitlines())


def anker_voor_programmaonderdeel(programmaonderdeel: str) -> str:
    """Quartz auto-slug van de H2-titel.

    Quartz/github-slugger lowercased en strip punctuatie + vervangt spaties
    door koppels. Voor ``titel_voor_programmaonderdeel`` betekent dat:
    "PO 1.1" → "po-11" (punt weg, spatie naar koppel) en
    "Programmaonderdeel onbekend" → "programmaonderdeel-onbekend".
    """
    titel = titel_voor_programmaonderdeel(programmaonderdeel)
    slug = titel.lower().replace(".", "")
    slug = slug.replace(" ", "-")
    return slug


def titel_voor_programmaonderdeel(programmaonderdeel: str) -> str:
    if programmaonderdeel == PROGRAMMAONDERDEEL_ONBEKEND:
        return "Programmaonderdeel onbekend"
    return f"PO {programmaonderdeel}"


# ---------------------------------------------------------------------------
# Blok-rendering (vraagtekst_blokken[])
# ---------------------------------------------------------------------------


def _formatteer_bedrag(waarde: Any) -> str:
    """Formatteer bedrag als Belgisch '7.000,00 EUR' (best-effort)."""
    try:
        f = float(waarde)
    except (TypeError, ValueError):
        return str(waarde) if waarde is not None else ""
    # Belgisch: punt = thousands, komma = decimaal
    geheel = f"{f:,.2f}"  # bv. "7,000.00"
    # vlip komma en punt
    geheel = geheel.replace(",", "X").replace(".", ",").replace("X", ".")
    return geheel


def _render_regels_tabel(
    regels: list[dict[str, Any]],
    kolommen: list[tuple[str, str]],
    bedrag_eenheid: str = "EUR",
) -> str:
    """Render dict-regels als markdown-tabel.

    `kolommen` is [(label, dict-key), ...]. Bedrag-keys met "bedrag" worden
    Belgisch-geformatteerd.
    """
    if not regels:
        return "_(geen regels)_"
    headers = [k[0] for k in kolommen]
    body_rijen = []
    for r in regels:
        cellen = []
        for label, key in kolommen:
            v = r.get(key, "")
            if "bedrag" in key.lower():
                cellen.append(_formatteer_bedrag(v))
            else:
                cellen.append(str(v) if v is not None else "")
        body_rijen.append(cellen)
    sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    regels_md = [
        "| " + " | ".join(headers) + " |",
        sep,
    ]
    for rij in body_rijen:
        regels_md.append("| " + " | ".join(rij) + " |")
    return "\n".join(regels_md)


def render_vraagtekst_blokken(blokken: list[dict[str, Any]]) -> str:
    """Render typed blokken naar markdown (v2 + v3 blok-types)."""
    delen: list[str] = []
    # Verzamel MC-opties contiguous als één lijst
    huidige_mc: list[dict[str, Any]] = []

    def flush_mc():
        if not huidige_mc:
            return
        regels = []
        for opt in huidige_mc:
            label = opt.get("label", "?")
            tekst = (opt.get("tekst") or "").strip()
            regels.append(f"- **{label}.** {tekst}")
        delen.append("\n".join(regels))
        huidige_mc.clear()

    for blok in blokken:
        blok_type = blok.get("type")
        if blok_type != "mc_optie" and huidige_mc:
            flush_mc()
        if blok_type == "tekst":
            inhoud = (blok.get("inhoud") or "").strip()
            if inhoud:
                delen.append(inhoud)
        elif blok_type == "tabel":
            delen.append(render_tabel_blok(blok))
        elif blok_type == "formule":
            inhoud = blok.get("inhoud") or ""
            notatie = blok.get("notatie", "plain")
            if notatie == "latex":
                delen.append(f"$$\n{inhoud}\n$$")
            else:
                delen.append(f"```\n{inhoud}\n```")
        elif blok_type == "figuur":
            caption = blok.get("caption", "(figuur)")
            bron_pdf = blok.get("bron_pdf", "?")
            pagina = blok.get("page", "?")
            delen.append(f"_Figuur ({caption}) — bron: {bron_pdf} p.{pagina}_")
        # ---- v3-blok-types ----
        elif blok_type == "casus_context":
            inhoud = (blok.get("inhoud") or "").strip()
            if inhoud:
                # Quote-blok: prefix elke regel met "> "
                prefixed = "\n".join("> " + r for r in inhoud.splitlines())
                delen.append(prefixed)
        elif blok_type == "vraag_instructie":
            inhoud = (blok.get("inhoud") or "").strip()
            if inhoud:
                delen.append(f"**{inhoud}**")
        elif blok_type == "bijlage_verwijzing":
            beschrijving = (blok.get("beschrijving") or "").strip()
            delen.append(f"_{beschrijving}_")
        elif blok_type == "proef_saldibalans":
            kop = "**Proef- en saldibalans**"
            tabel = _render_regels_tabel(
                blok.get("regels", []),
                [("Rekening", "rekening"), ("Naam", "naam"), ("Zijde", "zijde"), ("Bedrag", "bedrag")],
            )
            delen.append(kop + "\n\n" + tabel)
        elif blok_type == "rekeningstaat":
            kop = "**Rekeningstaat**"
            tabel = _render_regels_tabel(
                blok.get("regels", []),
                [("Rekening", "rekening"), ("Naam", "naam"), ("Bedrag", "bedrag")],
            )
            delen.append(kop + "\n\n" + tabel)
        elif blok_type == "inventaris":
            kop = "**Inventaris**"
            regels = blok.get("regels", []) or []
            lijst = "\n".join(
                f"- {r.get('post', '')}: {_formatteer_bedrag(r.get('bedrag'))} EUR"
                for r in regels
            )
            delen.append(kop + "\n" + lijst)
        elif blok_type == "balans":
            kop = "**Balans**"
            sub: list[str] = []
            if blok.get("activa"):
                sub.append("*Activa*")
                for r in blok["activa"]:
                    sub.append(
                        f"- {r.get('rubriek', '')}: "
                        f"{_formatteer_bedrag(r.get('bedrag'))} EUR"
                    )
            if blok.get("passiva"):
                sub.append("*Passiva*")
                for r in blok["passiva"]:
                    sub.append(
                        f"- {r.get('rubriek', '')}: "
                        f"{_formatteer_bedrag(r.get('bedrag'))} EUR"
                    )
            delen.append(kop + "\n" + "\n".join(sub))
        elif blok_type == "resultatenrekening":
            kop = "**Resultatenrekening**"
            tabel = _render_regels_tabel(
                blok.get("regels", []),
                [("Code", "code"), ("Post", "post"), ("Bedrag", "bedrag")],
            )
            delen.append(kop + "\n\n" + tabel)
        elif blok_type == "marktwaarde":
            post = blok.get("post") or "post"
            bedrag = _formatteer_bedrag(blok.get("bedrag"))
            delen.append(f"_Marktwaarde {post}: **{bedrag} EUR**_")
        elif blok_type == "aanpassing":
            subtype = blok.get("subtype", "aanpassing")
            bedrag = _formatteer_bedrag(blok.get("bedrag"))
            delen.append(f"_Aanpassing ({subtype}): **{bedrag} EUR**_")
        elif blok_type == "mc_optie":
            huidige_mc.append(blok)
        elif blok_type == "berekening_gegeven":
            formule = blok.get("formule") or ""
            delen.append(f"```\n{formule}\n```")
        else:
            # Onbekend type → debug-fallback
            inhoud_dump = json.dumps(blok, ensure_ascii=False)
            delen.append(
                f"```\n[onbekend blok-type: {blok_type}]\n{inhoud_dump}\n```"
            )
    flush_mc()
    return "\n\n".join(delen)


def render_tabel_blok(blok: dict[str, Any]) -> str:
    """Render een tabel-blok als markdown-tabel."""
    headers = blok.get("headers") or []
    rows = blok.get("rows") or []
    if not rows:
        return "_(lege tabel)_"

    # Aantal kolommen bepalen vanuit headers + breedste rij
    aantal_kolommen = max(
        [len(headers)] + [len(rij) for rij in rows] + [1]
    )

    def normaliseer_cel(cel: Any) -> str:
        tekst = "" if cel is None else str(cel)
        # Newlines in cellen breken markdown-tabellen; <br> houdt structuur
        tekst = tekst.replace("|", "\\|")
        tekst = tekst.replace("\n", " <br> ")
        return tekst.strip() or " "

    def pad_rij(rij: list[Any]) -> list[str]:
        gevuld = list(rij) + [""] * (aantal_kolommen - len(rij))
        return [normaliseer_cel(cel) for cel in gevuld]

    if headers:
        header_rij = pad_rij(headers)
    else:
        header_rij = [" "] * aantal_kolommen

    regels = [
        "| " + " | ".join(header_rij) + " |",
        "| " + " | ".join(["---"] * aantal_kolommen) + " |",
    ]
    for rij in rows:
        regels.append("| " + " | ".join(pad_rij(rij)) + " |")
    return "\n".join(regels)


def vraagtekst_markdown(vraag: dict[str, Any]) -> str:
    """Kies blokken-rendering indien beschikbaar, anders platte fallback."""
    blokken = vraag.get("vraagtekst_blokken")
    if blokken:
        gerendererd = render_vraagtekst_blokken(blokken)
        if gerendererd.strip():
            return gerendererd
    platte_tekst = (vraag.get("vraagtekst") or "").strip()
    if platte_tekst:
        return platte_tekst
    return "_(geen vraagtekst beschikbaar)_"


# ---------------------------------------------------------------------------
# Callouts
# ---------------------------------------------------------------------------


def callout(
    soort: str,
    titel: str,
    body: str,
    *,
    inklapbaar: bool = False,
) -> str:
    """Bouw een Quartz-callout. ``inklapbaar=True`` voegt ``-`` toe."""
    suffix = "-" if inklapbaar else ""
    kop = f"> [!{soort}]{suffix} {titel}".rstrip()
    if not body.strip():
        return kop
    body_geprefixt = prefix_regels(body, "> ")
    return f"{kop}\n{body_geprefixt}"


# ---------------------------------------------------------------------------
# Vraag-rendering
# ---------------------------------------------------------------------------


def render_herinterpretatie(vraag: dict[str, Any]) -> str:
    """Render herinterpretatie-callout (ADR-022). Geeft '' als niet aanwezig."""
    herinterpretatie = vraag.get("vraag_herinterpreteerd")
    if not herinterpretatie:
        return ""
    tekst = herinterpretatie.get("tekst_geherinterpreteerd", "").strip()
    motivering = herinterpretatie.get("interpretatie_motivering", "").strip()
    confidence = herinterpretatie.get("confidence", "?")
    datum = herinterpretatie.get("datum", "?")
    body_delen = [tekst, "", f"_Motivering_: {motivering}"]
    body_delen.append(f"_Confidence_: {confidence} · _Datum_: {datum}")
    return callout(
        "note",
        "Geherinterpreteerde vraagtekst (ADR-022)",
        "\n".join(body_delen),
        inklapbaar=True,
    )


def render_antwoord_hint(vraag: dict[str, Any]) -> str:
    """Render antwoord-hint-callout (ADR-022). '' als afwezig."""
    hint = vraag.get("antwoord_hint_in_vraag")
    if not hint:
        return ""
    if not hint.get("aanwezig"):
        return ""
    tekst = hint.get("tekst", "").strip()
    interpretatie = hint.get("interpretatie", "").strip()
    body_delen = [tekst]
    if interpretatie:
        body_delen.append("")
        body_delen.append(f"_Interpretatie_: {interpretatie}")
    return callout(
        "tip",
        "Antwoord-hint in originele vraagtekst",
        "\n".join(body_delen),
        inklapbaar=True,
    )


def render_mc_opties_gestructureerd(vraag: dict[str, Any]) -> str:
    """Render typed MC-opties (ADR-022) als markdown-tabel in callout."""
    opties = vraag.get("mc_opties_gestructureerd")
    if not opties:
        return ""
    regels = [
        "| Label | Tekst | Juistheid | Motivering |",
        "| --- | --- | --- | --- |",
    ]
    for optie in opties:
        label = (optie.get("label") or "").strip()
        tekst = (optie.get("tekst") or "").strip().replace("|", "\\|").replace(
            "\n", " <br> "
        )
        juistheid = (optie.get("juistheid") or "onbekend").strip()
        motivering = (
            (optie.get("motivering") or "")
            .strip()
            .replace("|", "\\|")
            .replace("\n", " <br> ")
        )
        regels.append(f"| {label} | {tekst} | {juistheid} | {motivering} |")
    return callout(
        "example",
        "MC-opties (gestructureerd)",
        "\n".join(regels),
        inklapbaar=True,
    )


_CONFIDENCE_MARKER = {"grounded": "⚖️", "inferred": "🤖"}


def _render_confidence(blok: dict[str, Any]) -> str:
    c = blok.get("confidence")
    if c in _CONFIDENCE_MARKER:
        return f" {_CONFIDENCE_MARKER[c]}"
    return ""


def render_antwoord_blok(blok: dict[str, Any]) -> str:
    """Render één typed `correct_antwoord_blokken[]`-element (ADR-023)."""
    btype = blok.get("type")
    conf = _render_confidence(blok)
    if btype == "motivatie":
        inh = (blok.get("inhoud") or "").strip()
        kop = blok.get("kop")
        if kop:
            return f"**{kop}**{conf}\n\n{inh}"
        return f"{inh}{conf}".rstrip()
    if btype == "definitie":
        lemma = blok.get("lemma", "")
        zin = blok.get("definitie_zin", "")
        kerneig = blok.get("kerneigenschappen") or []
        regels = [f"**{lemma}**{conf}", "", zin]
        if kerneig:
            regels.append("")
            regels.append("_Kerneigenschappen:_")
            for k in kerneig:
                eig = k.get("eigenschap", "") if isinstance(k, dict) else str(k)
                k_conf = _render_confidence(k) if isinstance(k, dict) else ""
                regels.append(f"- {eig}{k_conf}")
        return "\n".join(regels)
    if btype == "boeking":
        regels = blok.get("regels") or []
        eenheid = blok.get("eenheid") or "EUR"
        context = blok.get("context")
        lijn_kop = ["| D/C | Rekening | Naam | Bedrag |", "|:-:|:-:|:--|---:|"]
        for r in regels:
            zijde = r.get("zijde", "?")
            rek = r.get("rekening", "?")
            naam = (r.get("naam") or "").replace("|", "\\|")
            bedrag = r.get("bedrag")
            bedrag_s = f"{bedrag:,.2f}".replace(",", " ").replace(".", ",").replace(" ", ".") if isinstance(bedrag, (int, float)) else ""
            lijn_kop.append(f"| **{zijde}** | {rek} | {naam} | {bedrag_s} {eenheid} |")
        prefix = f"**Boeking — {context}**{conf}\n\n" if context else f"**Boeking**{conf}\n\n"
        return prefix + "\n".join(lijn_kop)
    if btype == "berekening":
        formule = blok.get("formule")
        comp = blok.get("componenten") or []
        tussen = blok.get("tussenstappen") or []
        result = blok.get("resultaat")
        eenheid = blok.get("eenheid") or ""
        interpretatie = blok.get("interpretatie")
        regels: list[str] = [f"**Berekening**{conf}"]
        if formule:
            regels.append("")
            regels.append(f"```\n{formule}\n```")
        if comp:
            regels.append("")
            for c in comp:
                naam = c.get("naam", "?")
                bedrag = c.get("bedrag", "")
                regels.append(f"- {naam}: {bedrag}")
        if tussen:
            regels.append("")
            for t in tussen:
                regels.append(f"- {t}")
        if result is not None:
            regels.append("")
            regels.append(f"**Resultaat**: {result} {eenheid}".rstrip())
        if interpretatie:
            regels.append("")
            regels.append(f"_{interpretatie}_")
        return "\n".join(regels)
    if btype == "opsomming":
        items = blok.get("items") or []
        kop = blok.get("kop")
        regels: list[str] = []
        if kop:
            regels.append(f"**{kop}**{conf}")
            regels.append("")
        for i, it in enumerate(items, 1):
            lemma = it.get("lemma", "")
            toel = it.get("toelichting", "")
            it_conf = _render_confidence(it)
            tail = f" — {toel}" if toel else ""
            regels.append(f"{i}. **{lemma}**{tail}{it_conf}")
        return "\n".join(regels)
    if btype == "procedure":
        stappen = blok.get("stappen") or []
        kop = blok.get("kop")
        regels: list[str] = []
        if kop:
            regels.append(f"**{kop}**{conf}")
            regels.append("")
        for s in stappen:
            nummer = s.get("nummer", "?")
            besch = s.get("beschrijving", "")
            s_conf = _render_confidence(s)
            regels.append(f"{nummer}. {besch}{s_conf}")
        return "\n".join(regels)
    if btype == "tabel":
        headers = blok.get("headers") or []
        rows = blok.get("rows") or []
        kop = blok.get("kop")
        lijnen: list[str] = []
        if kop:
            lijnen.append(f"**{kop}**{conf}")
            lijnen.append("")
        if headers:
            lijnen.append("| " + " | ".join(headers) + " |")
            lijnen.append("|" + "|".join(["---"] * len(headers)) + "|")
        for r in rows:
            lijnen.append("| " + " | ".join(r) + " |")
        return "\n".join(lijnen)
    if btype == "conclusie":
        inh = blok.get("inhoud", "")
        label = blok.get("gekozen_mc_label")
        prefix = f"**Conclusie**: {inh}{conf}"
        if label:
            return prefix + f"\n\n> [!check] Gekozen: **{label}**"
        return prefix
    if btype == "grondslag":
        bronnen = blok.get("bronnen") or []
        return f"_Grondslag: {'; '.join(bronnen)}._{conf}".rstrip()
    return ""


def render_antwoord_blokken(blokken: list[dict[str, Any]]) -> str:
    """Render volledige list[blok] als één markdown-string."""
    if not blokken:
        return ""
    return "\n\n".join(render_antwoord_blok(b) for b in blokken if b)


def render_modelantwoord_blok(vraag_of_subvraag: dict[str, Any]) -> str:
    """Render modelantwoord + motivering + bronnen + provenance.

    Werkt voor zowel vragen als subvragen — beide hebben dezelfde antwoord-
    velden volgens ADR-020 §8.

    ADR-023: gebruikt bij voorkeur `correct_antwoord_blokken[]` (typed)
    voor het motivering-blok wanneer aanwezig; fallback naar de platte
    `antwoord_motivering`-string.
    """
    correct = (vraag_of_subvraag.get("correct_antwoord") or "").strip()
    if not correct:
        return ""

    delen: list[str] = []
    delen.append("#### Modelantwoord")
    delen.append("")
    delen.append(correct)

    # ADR-023: typed antwoord-blokken bij voorkeur
    typed_blokken = vraag_of_subvraag.get("correct_antwoord_blokken")
    motivering = (vraag_of_subvraag.get("antwoord_motivering") or "").strip()
    if isinstance(typed_blokken, list) and typed_blokken:
        body = render_antwoord_blokken(typed_blokken)
        if body:
            delen.append("")
            delen.append(
                callout("success", "Motivering (typed)", body, inklapbaar=True)
            )
    elif motivering:
        delen.append("")
        delen.append(
            callout("success", "Motivering", motivering, inklapbaar=True)
        )

    bronnen_ruw = vraag_of_subvraag.get("antwoord_bron")
    bronnen_regels: list[str] = []
    bronnen_aantal = 0
    if isinstance(bronnen_ruw, str) and bronnen_ruw.strip():
        bronnen_regels.append(f"- _{bronnen_ruw.strip()}_")
        bronnen_aantal = 1
    elif isinstance(bronnen_ruw, list):
        for bron in bronnen_ruw:
            if isinstance(bron, dict):
                record = bron.get("record", "?")
                sectie = bron.get("sectie", "?")
                ondersteunt = bron.get("ondersteunt", "?")
                record_naam = Path(record).stem if record else "?"
                bronnen_regels.append(
                    f"- [[{record_naam}|{record}]] · {sectie} → "
                    f"ondersteunt: {ondersteunt}"
                )
            elif isinstance(bron, str) and bron.strip():
                bronnen_regels.append(f"- _{bron.strip()}_")
            bronnen_aantal += 1
    if bronnen_regels:
        delen.append("")
        delen.append(
            callout(
                "info",
                f"Bronnen ({bronnen_aantal})",
                "\n".join(bronnen_regels),
                inklapbaar=True,
            )
        )

    provenance = vraag_of_subvraag.get("antwoord_provenance") or {}
    if provenance:
        prov_regels = []
        generator = provenance.get("generator")
        datum = provenance.get("datum")
        checklist = provenance.get("checklist_versie")
        gates = provenance.get("gates_gepasseerd") or []
        opmerking = provenance.get("opmerking")
        antwoord_type_prov = provenance.get("antwoord_type")
        policy = provenance.get("policy_versie_wet")
        verify = provenance.get("verify_passed")
        if generator:
            prov_regels.append(f"- Generator: {generator}")
        if datum:
            prov_regels.append(f"- Datum: {datum}")
        if antwoord_type_prov:
            prov_regels.append(f"- Antwoord-type: {antwoord_type_prov}")
        if checklist:
            prov_regels.append(f"- Checklist-versie: {checklist}")
        if gates:
            prov_regels.append(f"- Gates gepasseerd: {', '.join(gates)}")
        if verify is not None:
            prov_regels.append(f"- Verify gepasseerd: {verify}")
        if policy:
            prov_regels.append(f"- Wetsversie-policy: {policy}")
        if opmerking:
            prov_regels.append(f"- Opmerking: {opmerking}")
        if prov_regels:
            delen.append("")
            delen.append(
                callout(
                    "info",
                    "Provenance",
                    "\n".join(prov_regels),
                    inklapbaar=True,
                )
            )

    return "\n".join(delen)


def render_gap_rapport(vraag_of_subvraag: dict[str, Any]) -> str:
    """Render record_gap_report-callout. '' als geen gap."""
    gap = vraag_of_subvraag.get("record_gap_report")
    if not gap:
        return ""
    niveau = gap.get("niveau", "?")
    gap_type = gap.get("type", "?")
    sub_type = gap.get("sub_type")
    beschrijving = (gap.get("beschrijving") or "").strip()
    ontbrekende_velden = gap.get("ontbrekende_velden") or []
    betrokken_records = gap.get("betrokken_records") or []
    gedetecteerd_op = gap.get("gedetecteerd_op")

    titel_delen = [f"Gap niveau **{niveau}** — type **{gap_type}**"]
    if sub_type:
        titel_delen.append(f"sub-type **{sub_type}**")
    titel = " · ".join(titel_delen)

    body_delen = [beschrijving] if beschrijving else []
    if ontbrekende_velden:
        body_delen.append("")
        body_delen.append(
            "Ontbrekende velden: " + ", ".join(ontbrekende_velden)
        )
    if betrokken_records:
        body_delen.append("")
        body_delen.append("Betrokken records: " + ", ".join(betrokken_records))
    if gedetecteerd_op:
        body_delen.append("")
        body_delen.append(f"_Gedetecteerd op_: {gedetecteerd_op}")

    return callout("warning", titel, "\n".join(body_delen))


def render_subvragen(vraag: dict[str, Any]) -> str:
    """Render subvragen-blok. '' als geen subvragen of allemaal leeg."""
    subvragen = vraag.get("subvragen") or []
    if not subvragen:
        return ""
    delen: list[str] = []
    for sub in subvragen:
        if not isinstance(sub, dict):
            continue
        label = (sub.get("label") or "?").strip()
        tekst = (sub.get("tekst") or "").strip()
        delen.append(f"#### Subvraag {label}")
        delen.append("")
        if tekst:
            delen.append(tekst)
        else:
            delen.append("_(geen vraagtekst voor subvraag)_")

        antwoord_type_sub = sub.get("antwoord_type")
        antwoord_confidence_sub = sub.get("antwoord_confidence")
        meta_delen = []
        if antwoord_type_sub:
            meta_delen.append(f"**Antwoord-type**: {antwoord_type_sub}")
        if antwoord_confidence_sub:
            meta_delen.append(f"**Confidence**: {antwoord_confidence_sub}")

        modelantwoord_blok = render_modelantwoord_blok(sub)
        if modelantwoord_blok:
            if meta_delen:
                delen.append("")
                delen.append(" · ".join(meta_delen))
            delen.append("")
            delen.append(modelantwoord_blok)

        gap_blok = render_gap_rapport(sub)
        if gap_blok:
            delen.append("")
            delen.append(gap_blok)

        delen.append("")
    return "\n".join(delen).rstrip()


def render_herinnering_waarschuwing(vraag: dict[str, Any]) -> str:
    """ADR-022: waarschuwing als vraag een herinnering-reconstructie is."""
    herkomst = vraag.get("vraag_herkomst")
    if not herkomst or herkomst == "officieel":
        return ""
    volledigheid = vraag.get("vraag_volledigheid", "onbekend")
    body = (
        f"Deze vraag is een **{herkomst}**-reconstructie "
        f"(volledigheid: {volledigheid}) — geen officiële ITAA-bundel. "
        "Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022)."
    )
    return callout(
        "warning",
        f"Herinnering-reconstructie ({volledigheid})",
        body,
    )


def render_vraag(
    vraag: dict[str, Any],
    examen_id: str,
    extra_programmaonderdelen: list[str],
) -> str:
    """Render één vraag als markdown-blok."""
    vraag_id = vraag.get("id", "?")
    punten = vraag.get("punten")
    punten_tekst = f" · {punten} pt" if punten not in (None, "") else ""
    vraagtype = vraag.get("vraagtype", "?")
    antwoord_type = vraag.get("antwoord_type") or "—"
    antwoord_confidence = vraag.get("antwoord_confidence") or "—"

    delen: list[str] = []
    delen.append(f"### {vraag_id} · {examen_id}{punten_tekst}")
    delen.append("")

    if extra_programmaonderdelen:
        delen.append(
            "_Ook geklassificeerd onder_: "
            + ", ".join(extra_programmaonderdelen)
        )
        delen.append("")

    herinnering_callout = render_herinnering_waarschuwing(vraag)
    if herinnering_callout:
        delen.append(herinnering_callout)
        delen.append("")

    delen.append(
        f"**Vraagformaat**: {vraagtype} · **Antwoord-type**: "
        f"{antwoord_type} · **Confidence**: {antwoord_confidence}"
    )
    delen.append("")

    delen.append("#### Vraagtekst")
    delen.append("")
    delen.append(vraagtekst_markdown(vraag))
    delen.append("")

    herinterpretatie_callout = render_herinterpretatie(vraag)
    if herinterpretatie_callout:
        delen.append(herinterpretatie_callout)
        delen.append("")

    antwoord_hint_callout = render_antwoord_hint(vraag)
    if antwoord_hint_callout:
        delen.append(antwoord_hint_callout)
        delen.append("")

    mc_opties_callout = render_mc_opties_gestructureerd(vraag)
    if mc_opties_callout:
        delen.append(mc_opties_callout)
        delen.append("")

    modelantwoord = render_modelantwoord_blok(vraag)
    if modelantwoord:
        delen.append(modelantwoord)
        delen.append("")
    elif not vraag.get("record_gap_report"):
        # Geen antwoord en geen gap → expliciete melding
        delen.append("_Nog niet beantwoord (modelantwoord ontbreekt)._")
        delen.append("")

    gap_callout = render_gap_rapport(vraag)
    if gap_callout:
        delen.append(gap_callout)
        delen.append("")

    subvragen_blok = render_subvragen(vraag)
    if subvragen_blok:
        delen.append(subvragen_blok)
        delen.append("")

    delen.append("---")
    return "\n".join(delen)


# ---------------------------------------------------------------------------
# Groepering per programmaonderdeel
# ---------------------------------------------------------------------------


def bepaal_programmaonderdeel(
    vraag_id: str,
    klassificatie: dict[str, dict[str, Any]],
) -> tuple[str, list[str]]:
    """Geeft (primair_programmaonderdeel, extra_programmaonderdelen).

    Primair = eerste in ``programmaonderdelen``-lijst. Extra = de rest.
    Wanneer klassificatie ontbreekt → (PROGRAMMAONDERDEEL_ONBEKEND, []).
    """
    record = klassificatie.get(vraag_id)
    if not record:
        return PROGRAMMAONDERDEEL_ONBEKEND, []
    programmaonderdelen = record.get("programmaonderdelen") or []
    if not programmaonderdelen:
        return PROGRAMMAONDERDEEL_ONBEKEND, []
    return programmaonderdelen[0], list(programmaonderdelen[1:])


def groepeer_vragen_per_programmaonderdeel(
    examens: list[dict[str, Any]],
    klassificatie: dict[str, dict[str, Any]],
) -> dict[str, list[tuple[str, dict[str, Any], list[str]]]]:
    """Map programmaonderdeel → list[(examen_id, vraag, extra_pos)].

    Items zijn gesorteerd op (examen_id, vraag_nr-numeriek-waar-mogelijk).
    """
    groepen: dict[str, list[tuple[str, dict[str, Any], list[str]]]] = {}
    for examen in examens:
        examen_id = examen.get("examen_id", "?")
        for vraag in examen.get("vragen", []):
            vraag_id = vraag.get("id", "?")
            primair, extra = bepaal_programmaonderdeel(vraag_id, klassificatie)
            groepen.setdefault(primair, []).append((examen_id, vraag, extra))

    def sorteersleutel(item: tuple[str, dict[str, Any], list[str]]) -> tuple:
        examen_id, vraag, _ = item
        nr_ruwer = str(vraag.get("vraag_nr") or "")
        # Splits in numeriek + suffix om "vr10" na "vr9" te sorteren
        numeriek = ""
        suffix = ""
        for teken in nr_ruwer:
            if teken.isdigit() and not suffix:
                numeriek += teken
            else:
                suffix += teken
        nr_int = int(numeriek) if numeriek else 0
        return (examen_id, nr_int, suffix, vraag.get("id", ""))

    for sleutel in groepen:
        groepen[sleutel].sort(key=sorteersleutel)
    return groepen


def sorteer_programmaonderdelen(sleutels: list[str]) -> list[str]:
    """Sorteer programmaonderdelen logisch (1.1 < 1.2 < … < 2.0 < onbekend)."""

    def sleutel_functie(programmaonderdeel: str) -> tuple:
        if programmaonderdeel == PROGRAMMAONDERDEEL_ONBEKEND:
            return (9, 9, programmaonderdeel)
        delen = programmaonderdeel.split(".")
        try:
            hoofd = int(delen[0])
            sub = int(delen[1]) if len(delen) > 1 else 0
        except ValueError:
            return (8, 8, programmaonderdeel)
        return (hoofd, sub, programmaonderdeel)

    return sorted(sleutels, key=sleutel_functie)


# ---------------------------------------------------------------------------
# Statistieken voor TOC
# ---------------------------------------------------------------------------


def tel_statistieken(
    vragen_items: list[tuple[str, dict[str, Any], list[str]]],
) -> dict[str, int]:
    """Aantal vragen, met antwoord, met gap voor een PO-groep."""
    totaal = len(vragen_items)
    met_antwoord = 0
    met_gap = 0
    for _, vraag, _ in vragen_items:
        if vraag.get("correct_antwoord"):
            met_antwoord += 1
        # subvragen met antwoord tellen ook
        elif any(
            (sub.get("correct_antwoord") or "").strip()
            for sub in (vraag.get("subvragen") or [])
            if isinstance(sub, dict)
        ):
            met_antwoord += 1
        if vraag.get("record_gap_report"):
            met_gap += 1
        else:
            for sub in vraag.get("subvragen") or []:
                if isinstance(sub, dict) and sub.get("record_gap_report"):
                    met_gap += 1
                    break
    return {
        "totaal": totaal,
        "met_antwoord": met_antwoord,
        "met_gap": met_gap,
    }


# ---------------------------------------------------------------------------
# Pagina-rendering
# ---------------------------------------------------------------------------


def render_inhoudsopgave(
    groepen: dict[str, list[tuple[str, dict[str, Any], list[str]]]],
) -> str:
    """Bouw inhoudsopgave met deep-links + statistieken per PO."""
    delen = ["## Inhoudsopgave", ""]
    delen.append("| Programmaonderdeel | Totaal | Met modelantwoord | Met gap |")
    delen.append("| --- | ---: | ---: | ---: |")
    for programmaonderdeel in sorteer_programmaonderdelen(list(groepen.keys())):
        stats = tel_statistieken(groepen[programmaonderdeel])
        titel = titel_voor_programmaonderdeel(programmaonderdeel)
        anker = anker_voor_programmaonderdeel(programmaonderdeel)
        delen.append(
            f"| [{titel}](#{anker}) "
            f"| {stats['totaal']} "
            f"| {stats['met_antwoord']} "
            f"| {stats['met_gap']} |"
        )
    return "\n".join(delen)


def render_pagina(
    examens: list[dict[str, Any]],
    klassificatie: dict[str, dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    """Bouw de volledige markdown-pagina + statistieken-rapport."""
    groepen = groepeer_vragen_per_programmaonderdeel(examens, klassificatie)

    totaal_vragen = sum(len(v) for v in groepen.values())
    totaal_met_antwoord = 0
    totaal_met_gap = 0
    voor_rapport_per_po: dict[str, dict[str, int]] = {}
    for programmaonderdeel, vragen_items in groepen.items():
        stats = tel_statistieken(vragen_items)
        voor_rapport_per_po[programmaonderdeel] = stats
        totaal_met_antwoord += stats["met_antwoord"]
        totaal_met_gap += stats["met_gap"]

    vandaag = date.today().isoformat()

    delen: list[str] = []
    delen.append("---")
    delen.append("title: Alle voorbeeldexamenvragen")
    delen.append(
        "description: Visuele verificatie van vraag-extractie, "
        "modelantwoorden en gap-rapporten over alle PO 1.x en PO 2.x/3.x/4.x "
        "vragen."
    )
    delen.append("tags: [examen, voorbeeldvragen, verificatie]")
    delen.append("gegenereerd_uit: tools/examen/render_alle_vragen.py")
    delen.append(f"gegenereerd_op: {vandaag}")
    delen.append("---")
    delen.append("")
    delen.append("# Alle voorbeeldexamenvragen")
    delen.append("")
    delen.append(
        "Deze pagina toont alle voorbeeldexamenvragen uit "
        "`data/programma/examen_vragen/` — gegroepeerd per "
        "programmaonderdeel. Doel: visuele verificatie van vraag-extractie "
        "(ADR-021 v2), modelantwoorden (ADR-020) en herinterpretatie "
        "(ADR-022). Auto-gegenereerd, niet handmatig bewerken."
    )
    delen.append("")
    delen.append(
        f"**Totaal**: {totaal_vragen} vragen — {totaal_met_antwoord} met "
        f"modelantwoord — {totaal_met_gap} met gap-rapport."
    )
    delen.append("")

    delen.append(render_inhoudsopgave(groepen))
    delen.append("")

    for programmaonderdeel in sorteer_programmaonderdelen(list(groepen.keys())):
        vragen_items = groepen[programmaonderdeel]
        stats = voor_rapport_per_po[programmaonderdeel]
        titel = titel_voor_programmaonderdeel(programmaonderdeel)
        # Geen expliciete {#anker}: Quartz slugt automatisch het H2-heading
        # (bv. "PO 1.1" → "po-11"); zelfde slug-functie als
        # ``anker_voor_programmaonderdeel`` (lowercase, punt weg).
        delen.append(f"## {titel}")
        delen.append("")
        delen.append(
            f"_{stats['totaal']} vragen — {stats['met_antwoord']} met "
            f"modelantwoord — {stats['met_gap']} met gap-rapport._"
        )
        delen.append("")
        for examen_id, vraag, extra_programmaonderdelen in vragen_items:
            delen.append(
                render_vraag(vraag, examen_id, extra_programmaonderdelen)
            )
            delen.append("")

    rapport = {
        "totaal_vragen": totaal_vragen,
        "totaal_met_antwoord": totaal_met_antwoord,
        "totaal_met_gap": totaal_met_gap,
        "per_programmaonderdeel": voor_rapport_per_po,
    }
    return "\n".join(delen).rstrip() + "\n", rapport


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    examens = laad_examen_bestanden()
    klassificatie = laad_klassificatie()
    pagina, rapport = render_pagina(examens, klassificatie)

    OUTPUT_BESTAND.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_BESTAND.write_text(pagina, encoding="utf-8")

    print(f"Geschreven naar: {OUTPUT_BESTAND.relative_to(REPOSITORY_ROOT)}")
    print(f"Totaal vragen: {rapport['totaal_vragen']}")
    print(f"Met modelantwoord: {rapport['totaal_met_antwoord']}")
    print(f"Met gap-rapport: {rapport['totaal_met_gap']}")
    print("Per programmaonderdeel:")
    for programmaonderdeel in sorteer_programmaonderdelen(
        list(rapport["per_programmaonderdeel"].keys())
    ):
        stats = rapport["per_programmaonderdeel"][programmaonderdeel]
        titel = titel_voor_programmaonderdeel(programmaonderdeel)
        print(
            f"  {titel}: {stats['totaal']} vragen "
            f"({stats['met_antwoord']} met antwoord, "
            f"{stats['met_gap']} met gap)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
