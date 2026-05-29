"""Schema 2.2 concept-fiche render — eerste versie.

Doel: 359 schema-2.2-records naar Quartz-markdown brengen zodat de
gebruiker visueel kan inspecteren wat er in zit.

Schema 2.2 shape:
- `inhoud.kern.{definitie,substantie,rationale}` (wrapper)
- `inhoud.subconcepten[]` recursief (zelfde inhoud-shape, geen metadata/scope)
- `inhoud.bouwstenen[]` flat met `bouwsteen_type`
- `inhoud.voorbeelden[]`, `valkuilen[]`, `speelruimtes[]`, `syntheses[]`
- `accountant_perspectieven[]` TOP-level (was rollen_per_perspectief in v2.1)
- `inhoud.gebruikscontext.geldigheid` (status: in-voege/uitdovend/afgeschaft/...)
- `metadata.categorieen[]` K/E/G/R
- `metadata.scope.{in,out}` (out heeft {topic,richting,ref})

Usage:
    python3 -m tools.leermateriaal.render_concept_v22                 # render alle records
    python3 -m tools.leermateriaal.render_concept_v22 --slug btw-aftrek
    python3 -m tools.leermateriaal.render_concept_v22 --limit 5
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO / "data" / "concepten" / "records"
OUT_DIR = REPO / "content" / "concepten"

# Globaal: alle slugs van bestaande v2.2-records (gevuld in main()).
EXISTING_SLUGS: set[str] = set()


def safe_link(target: str, label: str | None = None) -> str:
    """Wikilink alleen indien target bestaat als v2.2-record; anders ⏳ tekst."""
    target = (target or "").strip()
    if not target:
        return ""
    slug = target.split("#")[0]
    if slug in EXISTING_SLUGS:
        return f"[[{target}|{label}]]" if label else f"[[{target}]]"
    # niet-bestaand record → niet-aanklikbaar
    display = label or slug
    return f"⏳ {display}"

CONFIDENCE_ICON = {
    "geciteerd": "📖",
    "afgeleid": "🔗",
    "verondersteld": "🤖",
    "betwijfeld": "❓",
    "weerlegd": "❌",
}

CONCEPT_TYPE_LABEL = {
    "instrument": "Instrument",
    "verrichting": "Verrichting",
    "procedure": "Procedure",
    "balanspost": "Balanspost",
    "ratio": "Ratio",
    "regime": "Regime",
    "kader": "Kader",
    "principe": "Principe",
    "actor": "Actor",
}

BOUWSTEEN_ICON = {
    "begrip": "💡",
    "stap": "👣",
    "drempel": "📏",
    "regel": "📜",
    "uitzondering": "↪️",
    "vuistregel": "🧭",
    "mechanisme": "⚙️",
    "risico": "⚠️",
    "formule": "🧮",
    "principe": "✴️",
    "beperking": "🚧",
}

GELDIGHEID_BANNER = {
    "in-voege": None,  # default — geen banner
    "uitdovend": "> [!warning] **Uitdovend regime** — wordt afgebouwd; check sinds-/tot-data.",
    "afgeschaft": "> [!danger] **Afgeschaft** — niet meer van toepassing voor nieuwe gevallen.",
    "historisch": "> [!note] **Historisch** — alleen relevant voor historische dossiers.",
    "ontwerp": "> [!note] **Ontwerp** — wet/regelgeving nog niet in voege.",
}

GEBRUIK_LABEL = {
    "voor": "✅ Voor",
    "niet_voor": "🚫 Niet voor",
    "voorwaarden": "📋 Voorwaarden",
    "uitsluitingen": "⛔ Uitsluitingen",
    "indicaties": "🟢 Indicaties",
    "contra_indicaties": "🔴 Contra-indicaties",
    "trigger_start": "▶️ Trigger start",
    "trigger_einde": "⏹ Trigger einde",
    "voordeel": "👍 Voordeel",
    "risico": "⚠️ Risico",
}

ROL_LABEL = {
    "boekhouder": "📒 Boekhouder",
    "auditor": "🔍 Auditor",
    "fiscaal": "💰 Fiscaal adviseur",
    "adviseur": "🧭 Adviseur",
    "begeleider": "👥 Begeleider",
}

RICHTING_PREFIX = {
    "moet-verwijzen": "→",
    "mag-verwijzen": "↪",
    "niet-verwijzen": "✂",
}


# ─── helpers ──────────────────────────────────────────────────────────


def naam_str(naam: dict | None) -> str:
    if not naam:
        return ""
    return naam.get("primair", "")


def confidence_icon(grondslag: dict | None) -> str:
    if not grondslag:
        return ""
    return CONFIDENCE_ICON.get(grondslag.get("confidence", ""), "")


def render_bronnen(grondslag: dict | None) -> str:
    if not grondslag:
        return ""
    bronnen = grondslag.get("bronnen") or []
    if not bronnen:
        return ""
    parts = []
    for b in bronnen:
        bits = []
        if b.get("naam"):
            bits.append(b["naam"])
        if b.get("ref"):
            bits.append(b["ref"])
        if b.get("type"):
            bits.append(f"_{b['type']}_")
        if b.get("datum"):
            bits.append(f"({b['datum']})")
        parts.append(" — ".join(bits) if bits else b.get("type", "?"))
    return " · ".join(parts)


def render_tekst(blok: dict | None, prefix: str = "") -> str:
    """Universele {tekst, grondslag, ...}-blok render.

    Confidence-icon (🔗/📖/🤖/…) staat NIET meer voor de tekst, maar als prefix
    van de <small>-bronvermelding. Houdt de lopende tekst leesbaar; vertrouwen
    blijft zichtbaar bij de bron.
    """
    if not blok:
        return ""
    text = (blok.get("tekst") or "").strip()
    if not text:
        return ""
    grondslag = blok.get("grondslag") or {}
    icon = confidence_icon(grondslag)
    out = text
    if prefix:
        out = f"{prefix} {out}"
    bronnen = render_bronnen(grondslag)
    if bronnen:
        marker = icon or "📚"
        out += f"\n\n<small>{marker} {bronnen}</small>"
    elif icon:
        # geen bron maar wel confidence-label → alleen icon als marker
        out += f"\n\n<small>{icon}</small>"
    rationale = blok.get("rationale")
    if rationale:
        out += f"\n\n_Waarom: {rationale}_"
    for w in blok.get("weergaven") or []:
        out += "\n\n" + render_weergave(w)
    return out


def _fmt_bedrag(v) -> str:
    """EUR-bedrag — int/float/None → string ('' voor None)."""
    if v is None or v == "":
        return ""
    if isinstance(v, (int, float)):
        if float(v).is_integer():
            return f"{int(v):,}".replace(",", ".")
        return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return str(v)


def _render_boekingsregels(rijen: list) -> str:
    """Render lijst boekingsregels als debet|credit-tabel."""
    if not rijen:
        return ""
    heeft_oms = any((r or {}).get("omschrijving") for r in rijen)
    if heeft_oms:
        head = ["Rekening", "Debet", "Credit", "Omschrijving"]
    else:
        head = ["Rekening", "Debet", "Credit"]
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    for r in rijen:
        r = r or {}
        # zijde-shape (legacy): {zijde: debet/credit, bedrag, rekening, omschrijving}
        if r.get("zijde") and "bedrag" in r:
            d = _fmt_bedrag(r["bedrag"]) if r["zijde"] == "debet" else ""
            c = _fmt_bedrag(r["bedrag"]) if r["zijde"] == "credit" else ""
        else:
            d = _fmt_bedrag(r.get("debet"))
            c = _fmt_bedrag(r.get("credit"))
        rek = r.get("rekening", "?")
        cells = [rek, d, c]
        if heeft_oms:
            cells.append(r.get("omschrijving", ""))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def render_weergave(w: dict) -> str:
    wtype = w.get("type", "?")

    if wtype == "proza":
        return (w.get("tekst") or "").strip()

    if wtype == "berekening":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**🧮 {titel}**")
        else:
            parts.append("**Berekening:**")
        if tekst := w.get("tekst"):
            parts.append(tekst.strip())
        if stappen := w.get("stappen"):
            parts.append("\n".join(f"- {s}" for s in stappen))
        if r := w.get("resultaat"):
            parts.append(f"→ **Resultaat**: {r}")
        return "\n\n".join(parts)

    if wtype == "boeking":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**📒 {titel}**")
        if ctx := w.get("context"):
            parts.append(f"_{ctx}_")
        if tekst := w.get("tekst"):
            parts.append(tekst.strip())
        # variant 1: top-level rijen / regels
        rijen = w.get("rijen") or w.get("regels")
        if rijen:
            tbl = _render_boekingsregels(rijen)
            if tbl:
                parts.append(tbl)
        # variant 2: top-level debet/credit (één regel)
        elif w.get("debet") is not None or w.get("credit") is not None:
            tbl = _render_boekingsregels([{
                "rekening": w.get("rekening", "?"),
                "debet": w.get("debet"),
                "credit": w.get("credit"),
                "omschrijving": w.get("omschrijving", ""),
            }])
            parts.append(tbl)
        # variant 3: geneste boekingen[]
        if boekingen := w.get("boekingen"):
            for sub in boekingen:
                if not isinstance(sub, dict):
                    continue
                if t := sub.get("titel"):
                    parts.append(f"_{t}_")
                sub_rijen = sub.get("rijen") or sub.get("regels")
                if sub_rijen:
                    parts.append(_render_boekingsregels(sub_rijen))
        # variant 4: lijnen + scenario (meerdere scenario's naast elkaar)
        if lijnen := w.get("lijnen"):
            parts.append(_render_boekingsregels(lijnen))
        if scenario := w.get("scenario"):
            parts.append(f"_Scenario: {scenario}_")
        if toel := w.get("toelichting"):
            parts.append(f"_{toel}_")
        return "\n\n".join(p for p in parts if p)

    if wtype == "tabel":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**📋 {titel}**")
        if tekst := w.get("tekst"):
            return f"{parts[0]}\n\n{tekst.strip()}" if parts else tekst.strip()
        kolommen = w.get("kolommen") or w.get("kopjes") or []
        rijen = w.get("rijen") or []
        if kolommen and rijen:
            parts.append("| " + " | ".join(str(k) for k in kolommen) + " |")
            parts.append("| " + " | ".join("---" for _ in kolommen) + " |")
            for row in rijen:
                if isinstance(row, list):
                    cells = [str(c) for c in row]
                else:
                    cells = [str(row.get(k, "")) for k in kolommen]
                parts.append("| " + " | ".join(cells) + " |")
        elif rijen:
            # rijen zonder kolommen — render als bullet-lijst
            for row in rijen:
                parts.append(f"- {row}")
        if interp := w.get("interpretatie"):
            parts.append(f"_{interp}_")
        if conc := w.get("conclusie"):
            parts.append(f"→ **{conc}**")
        if toel := w.get("toelichting"):
            parts.append(f"_{toel}_")
        return "\n\n".join(p for p in parts if p)

    if wtype == "formule" or wtype == "formule_expressie":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**🧮 {titel}**")
        formule = w.get("formule") or w.get("uitdrukking") or w.get("expressie") or w.get("tekst")
        if formule:
            if "\n" in str(formule):
                parts.append(f"```\n{formule}\n```")
            else:
                parts.append(f"`{formule}`")
        if toel := w.get("toelichting"):
            parts.append(toel)
        return "\n\n".join(p for p in parts if p)

    if wtype == "stappenlijst":
        parts = []
        if titel := w.get("titel") or w.get("label"):
            parts.append(f"**👣 {titel}**")
        if tekst := w.get("tekst"):
            parts.append(tekst.strip())
        if stappen := w.get("stappen"):
            parts.append("\n".join(f"{i+1}. {s}" for i, s in enumerate(stappen)))
        if r := w.get("resultaat"):
            parts.append(f"→ **Resultaat**: {r}")
        return "\n\n".join(p for p in parts if p)

    if wtype == "vergelijkingstabel":
        # zelfde shape als tabel — delegeer
        return render_weergave({**w, "type": "tabel"})

    if wtype == "tijdslijn":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**⏱ {titel}**")
        if intro := w.get("intro"):
            parts.append(intro)
        if tekst := w.get("tekst"):
            parts.append(tekst.strip())
        inhoud = w.get("inhoud") or {}
        mijlpalen = inhoud.get("mijlpalen") or w.get("stappen") or []
        for m in mijlpalen:
            if isinstance(m, dict):
                moment = m.get("moment", "")
                actie = m.get("actie") or m.get("tekst") or ""
                parts.append(f"- **{moment}** — {actie}" if moment else f"- {actie}")
            else:
                parts.append(f"- {m}")
        return "\n".join(parts) if all("\n" not in p for p in parts) else "\n\n".join(parts)

    if wtype == "beslisboom":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**🌳 {titel}**")
        if intro := w.get("intro"):
            parts.append(intro)
        if tekst := w.get("tekst"):
            parts.append(tekst.strip())
        if code := w.get("code"):
            # waarschijnlijk mermaid
            parts.append(f"```mermaid\n{code}\n```")
        inhoud = w.get("inhoud") or {}
        if vragen := inhoud.get("vragen"):
            parts.append("**Vragen:**\n" + "\n".join(f"- {v}" for v in vragen))
        if paden := inhoud.get("antwoord_per_pad") or inhoud.get("paden"):
            parts.append("**Uitkomsten per pad:**\n" + "\n".join(f"- {p}" for p in paden))
        if stappen := w.get("stappen"):
            parts.append("\n".join(f"- {s}" for s in stappen))
        return "\n\n".join(p for p in parts if p)

    if wtype == "balans_snapshot":
        parts = []
        if titel := w.get("titel"):
            parts.append(f"**📊 {titel}**")
        if toel := w.get("toelichting"):
            parts.append(f"_{toel}_")
        # zonder dedicated balans-renderer: payload als JSON tonen
        payload = {k: v for k, v in w.items() if k not in ("type", "grondslag", "titel", "toelichting")}
        if payload:
            parts.append(f"```json\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n```")
        return "\n\n".join(p for p in parts if p)

    # onbekend type — zichtbare placeholder (niet stilte). Per regel 9: maak fail
    # zichtbaar zodat we 'm kunnen toevoegen, geen JSON-dump in productie.
    return f"_⚠️ weergave-type `{wtype}` nog niet ondersteund_"


def render_kern(kern: dict | None, depth: int = 2) -> str:
    """Render kern.{definitie,substantie,rationale}."""
    if not kern:
        return ""
    parts = []
    if defi := kern.get("definitie"):
        parts.append(f"{'#' * depth} Definitie\n\n{render_tekst(defi)}")
    if sub := kern.get("substantie"):
        parts.append(f"{'#' * depth} Substantie\n\n{render_tekst(sub)}")
    if rat := kern.get("rationale"):
        parts.append(f"{'#' * depth} Rationale\n\n{render_tekst(rat)}")
    return "\n\n".join(parts)


def render_gebruikscontext(ctx: dict | None) -> str:
    if not ctx:
        return ""
    lines = []
    # geldigheid eerst
    g = ctx.get("geldigheid")
    if g:
        status = g.get("status", "")
        bits = [f"**Status**: `{status}`"]
        if g.get("sinds"):
            bits.append(f"sinds **{g['sinds']}**")
        if g.get("tot"):
            bits.append(f"tot **{g['tot']}**")
        if g.get("wettelijke_basis"):
            bits.append(f"basis: {g['wettelijke_basis']}")
        lines.append(" · ".join(bits))
        if g.get("toelichting"):
            lines.append(f"\n{g['toelichting']}")
    # arrays voor/niet_voor/voorwaarden/uitsluitingen/...
    for key in ["voor", "niet_voor", "voorwaarden", "uitsluitingen", "indicaties", "contra_indicaties", "trigger_start", "trigger_einde", "voordeel", "risico"]:
        items = ctx.get(key)
        if not items:
            continue
        items = items if isinstance(items, list) else [items]
        lines.append(f"\n**{GEBRUIK_LABEL.get(key, key)}**")
        for item in items:
            if isinstance(item, dict):
                t = (item.get("tekst") or "").strip()
                icon = confidence_icon(item.get("grondslag"))
                line = f"- {icon} {t}".rstrip()
                if item.get("relateert_naar"):
                    line += f" → {safe_link(item['relateert_naar'])}"
                lines.append(line)
            else:
                lines.append(f"- {item}")
    return "\n".join(lines)


def render_bouwsteen(b: dict, depth: int = 3) -> str:
    naam = naam_str(b.get("naam"))
    btype = b.get("bouwsteen_type", "")
    icon = BOUWSTEEN_ICON.get(btype, "•")
    # icon draagt de bouwsteen-typering; type-label als losse tag toegevoegd
    # niets meer voor de leesbaarheid.
    parts = [f"{'#' * depth} {icon} {naam}"]
    if k := b.get("kern"):
        # bouwsteen.kern is hetzelfde shape als concept.kern (definitie/substantie/rationale)
        if defi := k.get("definitie"):
            parts.append(render_tekst(defi))
        if sub := k.get("substantie"):
            parts.append("**Substantie**: " + render_tekst(sub))
        if rat := k.get("rationale"):
            parts.append("**Rationale**: " + render_tekst(rat))
    return "\n\n".join(parts)


def render_subconcept(sc: dict, depth: int = 3) -> str:
    naam = naam_str(sc.get("naam"))
    parts = [f"{'#' * depth} 📦 {naam}"]
    inhoud = sc.get("inhoud") or {}
    if inhoud.get("kern"):
        parts.append(render_kern(inhoud["kern"], depth=depth + 1))
    for b in inhoud.get("bouwstenen") or []:
        parts.append(render_bouwsteen(b, depth=depth + 1))
    for sub in inhoud.get("subconcepten") or []:
        parts.append(render_subconcept(sub, depth=depth + 1))
    for v in inhoud.get("voorbeelden") or []:
        parts.append(render_voorbeeld(v, depth=depth + 1))
    for vk in inhoud.get("valkuilen") or []:
        parts.append(render_valkuil(vk, depth=depth + 1))
    if gc := inhoud.get("gebruikscontext"):
        parts.append(render_gebruikscontext(gc))
    return "\n\n".join(p for p in parts if p)


def _as_callout(callout_type: str, titel: str, body_parts: list[str], collapsed: bool = True) -> str:
    """Wrap body-parts in een Obsidian-style callout. `-` na type = collapsed-by-default."""
    body = "\n\n".join(p for p in body_parts if p)
    marker = "-" if collapsed else ""
    lines = [f"> [!{callout_type}]{marker} {titel}"]
    for line in body.split("\n"):
        lines.append(f"> {line}" if line else ">")
    return "\n".join(lines)


def render_voorbeeld(v: dict, depth: int = 3) -> str:
    # depth wordt genegeerd — voorbeeld zit in collapsed callout, niet meer als heading.
    titel = v.get("titel") or naam_str(v.get("naam")) or "Voorbeeld"
    body = []
    if v.get("context"):
        body.append(f"_{v['context']}_")
    for w in v.get("weergaven") or []:
        body.append(render_weergave(w))
    bronnen = render_bronnen(v.get("grondslag"))
    icon = confidence_icon(v.get("grondslag"))
    if bronnen:
        marker = icon or "📚"
        body.append(f"<small>{marker} {bronnen}</small>")
    # Geen emoji-prefix in titel — Quartz' callout-renderer toont al een icon
    # op basis van het callout-type.
    return _as_callout("example", titel, body, collapsed=True)


def render_valkuil(vk: dict, depth: int = 3) -> str:
    titel = vk.get("titel") or "Valkuil"
    body = []
    if vk.get("verkeerde_assumptie"):
        body.append(f"**Verkeerde assumptie**: {vk['verkeerde_assumptie']}")
    if vk.get("kernpunt"):
        body.append(f"**Kernpunt**: {vk['kernpunt']}")
    if vk.get("toelichting"):
        body.append(vk["toelichting"])
    bronnen = render_bronnen(vk.get("grondslag"))
    icon = confidence_icon(vk.get("grondslag"))
    if bronnen:
        marker = icon or "📚"
        body.append(f"<small>{marker} {bronnen}</small>")
    return _as_callout("warning", titel, body, collapsed=True)


def render_speelruimte(sr: dict, depth: int = 3) -> str:
    titel = sr.get("titel") or "Speelruimte"
    parts = [f"{'#' * depth} 🎚️ {titel}"]
    if sr.get("keuze"):
        parts.append(f"**Keuze**: {sr['keuze']}")
    if sr.get("criteria"):
        if isinstance(sr["criteria"], list):
            parts.append("**Criteria**:")
            for c in sr["criteria"]:
                parts.append(f"- {c}")
        else:
            parts.append(f"**Criteria**: {sr['criteria']}")
    if sr.get("toelichting"):
        parts.append(sr["toelichting"])
    return "\n\n".join(parts)


def render_synthese(s: dict, depth: int = 3) -> str:
    """Schema 2.2 synthese: {type, intro, inhoud:{...}}.
    inhoud-shapes (gezien in corpus):
      - kolommen+rijen        — matrix
      - assen+rijen           — 2-zijdige matrix met as|links|rechts
      - mermaid               — mermaid-blok
      - mijlpalen             — tijdslijn ({moment, actie})
      - stappen / fasen / rangorde — geordende lijst
      - vragen+antwoord_per_pad   — beslisboom-lijst
      - diagram               — onbekend, alleen intro tonen
    """
    stype = s.get("type", "synthese")
    type_label = {
        "matrix": "Matrix", "vergelijkingstabel": "Vergelijking",
        "beslisboom": "Beslisboom", "tijdslijn": "Tijdslijn",
        "stappenlijst": "Stappenlijst", "rangorde": "Rangorde",
    }.get(stype, "Synthese")
    parts = [f"{'#' * depth} 🧩 {type_label}"]
    if intro := s.get("intro"):
        parts.append(intro)

    inhoud = s.get("inhoud") or {}

    # matrix: kolommen+rijen — bouw tabel als één string (markdown-tabel mag
    # GEEN blanco regels tussen rijen hebben, dus niet als losse parts join'en).
    if inhoud.get("kolommen") and inhoud.get("rijen"):
        kol = inhoud["kolommen"]
        tbl = ["| " + " | ".join(str(k) for k in kol) + " |",
               "| " + " | ".join("---" for _ in kol) + " |"]
        for row in inhoud["rijen"]:
            if isinstance(row, list):
                cells = [str(c) for c in row]
            else:
                cells = [str(row.get(k, "")) for k in kol]
            tbl.append("| " + " | ".join(cells) + " |")
        parts.append("\n".join(tbl))

    # assen+rijen: 2-zijdige vergelijking (as | links | rechts)
    elif inhoud.get("assen") and inhoud.get("rijen"):
        assen = inhoud["assen"]  # [links_label, rechts_label]
        l_label = assen[0] if len(assen) > 0 else "Links"
        r_label = assen[1] if len(assen) > 1 else "Rechts"
        tbl = [f"| As | {l_label} | {r_label} |", "| --- | --- | --- |"]
        for row in inhoud["rijen"]:
            tbl.append(f"| **{row.get('as','')}** | {row.get('links','')} | {row.get('rechts','')} |")
        parts.append("\n".join(tbl))

    # mermaid
    if mm := inhoud.get("mermaid"):
        parts.append(f"```mermaid\n{mm}\n```")

    # mijlpalen — tijdslijn
    if mijlpalen := inhoud.get("mijlpalen"):
        for m in mijlpalen:
            if isinstance(m, dict):
                moment = m.get("moment", "")
                actie = m.get("actie") or m.get("tekst") or ""
                parts.append(f"- **{moment}** — {actie}" if moment else f"- {actie}")
            else:
                parts.append(f"- {m}")

    # stappen / fasen / rangorde — geordende lijst
    for lijst_key in ("stappen", "fasen", "rangorde"):
        if items := inhoud.get(lijst_key):
            for i, item in enumerate(items, 1):
                if isinstance(item, dict):
                    titel_i = item.get("titel") or item.get("naam") or ""
                    body_i = item.get("tekst") or item.get("toelichting") or ""
                    if titel_i and body_i:
                        parts.append(f"{i}. **{titel_i}** — {body_i}")
                    else:
                        parts.append(f"{i}. {titel_i or body_i}")
                else:
                    parts.append(f"{i}. {item}")

    # vragen + antwoord_per_pad — beslisboom
    if vragen := inhoud.get("vragen"):
        parts.append("**Vragen:**\n" + "\n".join(f"- {v}" for v in vragen))
    if paden := inhoud.get("antwoord_per_pad"):
        parts.append("**Uitkomsten per pad:**\n" + "\n".join(f"- {p}" for p in paden))

    if conc := inhoud.get("conclusie"):
        parts.append(f"→ **{conc}**")
    if toel := inhoud.get("toelichting"):
        parts.append(f"_{toel}_")

    return "\n\n".join(parts)


def render_perspectief(p: dict, depth: int = 3) -> str:
    naam = naam_str(p.get("naam"))
    parts = [f"{'#' * depth} {naam}"]
    if p.get("intro"):
        parts.append(f"_{p['intro']}_")
    for rol in p.get("rollen") or []:
        rol_naam = rol.get("rol", "?")
        parts.append(f"{'#' * (depth + 1)} {ROL_LABEL.get(rol_naam, rol_naam)}")
        for el in rol.get("elementen") or []:
            # el is a bouwsteen-shape
            parts.append(render_bouwsteen(el, depth=depth + 2))
    return "\n\n".join(parts)


def render_relaties(relaties: list) -> str:
    if not relaties:
        return ""
    by_type: dict[str, list] = {}
    for r in relaties:
        by_type.setdefault(r.get("type", "?"), []).append(r)
    lines = []
    for rtype, items in by_type.items():
        lines.append(f"### `{rtype}`")
        for r in items:
            target = r.get("target", "?")
            line = f"- {safe_link(target)}"
            toel = r.get("toelichting")
            if isinstance(toel, dict):
                toel = toel.get("tekst") or toel.get("text", "")
            if toel:
                line += f" — {toel}"
            lines.append(line)
            if rtype == "vergelijkbaar_met":
                if r.get("gelijkenissen"):
                    lines.append("    - **Gelijkenissen**:")
                    for g in r["gelijkenissen"]:
                        lines.append(f"        - {g}")
                if r.get("verschillen"):
                    lines.append("    - **Verschillen**:")
                    for v in r["verschillen"]:
                        lines.append(f"        - {v}")
                if r.get("verwarring_risico"):
                    lines.append(f"    - ⚠️ **Verwarringsrisico**: {r['verwarring_risico']}")
    return "\n".join(lines)


def render_scope_out(scope_out: list) -> str:
    if not scope_out:
        return ""
    lines = []
    for item in scope_out:
        if isinstance(item, str):
            lines.append(f"- ✂ {item}")
            continue
        topic = item.get("topic", "")
        richting = item.get("richting", "")
        ref = item.get("ref", "")
        prefix = RICHTING_PREFIX.get(richting, "·")
        line = f"- {prefix} {topic}"
        if ref:
            line += f" → {safe_link(ref)}"
        if richting and richting != "niet-verwijzen":
            line += f" _({richting})_"
        lines.append(line)
    return "\n".join(lines)


def render_status_banner(meta: dict, geldigheid: dict | None) -> str:
    # Concept-/skeleton-status komt uit frontmatter-tag (status-concept / status-skeleton);
    # geen prominente banner meer in body. Wettelijke geldigheid blijft wél als banner.
    banners = []
    if geldigheid:
        gbanner = GELDIGHEID_BANNER.get(geldigheid.get("status", ""))
        if gbanner:
            banners.append(gbanner)
    return "\n\n".join(banners)


def render_frontmatter(rec: dict) -> str:
    meta = rec.get("metadata") or {}
    fm = {
        "title": naam_str(rec.get("naam")),
        "concept_type": rec.get("concept_type", ""),
        "schema_version": meta.get("schema_version", ""),
        "status": meta.get("status", ""),
        "categorieen": meta.get("categorieen") or [],
        "ankers": meta.get("ankers") or [],
        "tags": ["concept", "schema-2.2", f"type-{rec.get('concept_type', 'onbekend')}"]
        + [f"cat-{c}" for c in (meta.get("categorieen") or [])]
        + [f"status-{meta.get('status', 'concept')}"],
        "gegenereerd_uit": f"data/concepten/records/{rec['id']}.json",
    }
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            if not v:
                continue
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            if v in ("", None):
                continue
            lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def render_record(rec: dict) -> str:
    naam = naam_str(rec.get("naam"))
    ctype = rec.get("concept_type", "?")
    type_label = CONCEPT_TYPE_LABEL.get(ctype, ctype)
    meta = rec.get("metadata") or {}
    inhoud = rec.get("inhoud") or {}
    gc = inhoud.get("gebruikscontext") or {}
    geldigheid = gc.get("geldigheid")

    # H1 wordt door Quartz (ArticleTitle) uit frontmatter.title gerenderd.
    # Type-indicator + afkorting + synoniemen op één compacte regel,
    # zodat de definitie meteen boven de fold zichtbaar is.
    # Vertalingen tijdelijk weggelaten — pas tonen als records een 'common'-flag
    # per vertaling krijgen (alleen ingeburgerde FR/EN-termen renderen).
    intro_bits = [f"_{type_label}_"]
    if naam_dict := rec.get("naam"):
        if afk := naam_dict.get("afkorting"):
            intro_bits.append(f"afk: **{afk}**")
        if syn := naam_dict.get("synoniemen"):
            intro_bits.append("ook: " + " · ".join(syn))
    parts = [" · ".join(intro_bits)]

    banner = render_status_banner(meta, geldigheid)
    if banner:
        parts.append(banner)

    # kern
    if k := inhoud.get("kern"):
        parts.append(render_kern(k, depth=2))

    # gebruikscontext
    if gc:
        body = render_gebruikscontext(gc)
        if body:
            parts.append(f"## Gebruikscontext\n\n{body}")

    # subconcepten
    if subs := inhoud.get("subconcepten"):
        parts.append("## Sub-concepten")
        for sc in subs:
            parts.append(render_subconcept(sc, depth=3))

    # bouwstenen
    if bs := inhoud.get("bouwstenen"):
        parts.append("## Bouwstenen")
        for b in bs:
            parts.append(render_bouwsteen(b, depth=3))

    # voorbeelden
    if vb := inhoud.get("voorbeelden"):
        parts.append("## Voorbeelden")
        for v in vb:
            parts.append(render_voorbeeld(v, depth=3))

    # valkuilen
    if vk := inhoud.get("valkuilen"):
        parts.append("## Valkuilen")
        for v in vk:
            parts.append(render_valkuil(v, depth=3))

    # speelruimtes
    if sr := inhoud.get("speelruimtes"):
        parts.append("## Speelruimtes")
        for s in sr:
            parts.append(render_speelruimte(s, depth=3))

    # syntheses
    if sy := inhoud.get("syntheses"):
        parts.append("## Syntheses")
        for s in sy:
            parts.append(render_synthese(s, depth=3))

    # accountant_perspectieven (top-level in schema 2.2)
    if persp := rec.get("accountant_perspectieven"):
        parts.append("## Accountant-perspectieven")
        for p in persp:
            parts.append(render_perspectief(p, depth=3))

    # scope.out (cross-links)
    scope = meta.get("scope") or {}
    if so := scope.get("out"):
        body = render_scope_out(so)
        if body:
            parts.append(f"## Verder lezen (scope-out)\n\n{body}")

    # relaties
    if rels := rec.get("relaties"):
        parts.append(f"## Relaties\n\n{render_relaties(rels)}")

    return "\n\n".join(p for p in parts if p) + "\n"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", help="Render één record (id zonder .json)")
    p.add_argument("--limit", type=int, help="Maximaal N records renderen")
    p.add_argument("--out-dir", default=str(OUT_DIR))
    args = p.parse_args()

    if args.slug:
        files = [RECORDS_DIR / f"{args.slug}.json"]
    else:
        files = sorted(RECORDS_DIR.glob("*.json"))

    if args.limit:
        files = files[: args.limit]

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Vul EXISTING_SLUGS voor safe_link()
    global EXISTING_SLUGS
    for fp in RECORDS_DIR.glob("*.json"):
        try:
            r = json.loads(fp.read_text())
        except Exception:
            continue
        if (r.get("metadata") or {}).get("schema_version") == "2.2":
            EXISTING_SLUGS.add(r["id"])

    rendered, failed = 0, 0
    for f in files:
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"PARSE-FAIL {f.name}: {e}", file=sys.stderr)
            failed += 1
            continue
        # alleen schema 2.2 verwerken
        if (rec.get("metadata") or {}).get("schema_version") != "2.2":
            continue
        try:
            fm = render_frontmatter(rec)
            body = render_record(rec)
            (out_dir / f"{rec['id']}.md").write_text(f"{fm}\n\n{body}", encoding="utf-8")
            rendered += 1
        except Exception as e:
            print(f"RENDER-FAIL {f.name}: {type(e).__name__}: {e}", file=sys.stderr)
            failed += 1

    print(f"Rendered: {rendered}, failed: {failed} → {out_dir}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
