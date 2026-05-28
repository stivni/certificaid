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

CATEGORIE_LABEL = {
    "kader": "🏛️ Kader",
    "entiteit": "🏢 Entiteit",
    "gebeurtenis": "📅 Gebeurtenis",
    "regeling": "📋 Regeling",
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
    """Universele {tekst, grondslag, ...}-blok render."""
    if not blok:
        return ""
    text = (blok.get("tekst") or "").strip()
    if not text:
        return ""
    grondslag = blok.get("grondslag") or {}
    icon = confidence_icon(grondslag)
    out = text
    if icon:
        out = f"{icon} {out}"
    if prefix:
        out = f"{prefix} {out}"
    bronnen = render_bronnen(grondslag)
    if bronnen:
        out += f"\n\n<small>📚 {bronnen}</small>"
    rationale = blok.get("rationale")
    if rationale:
        out += f"\n\n_Waarom: {rationale}_"
    # weergaven (inline JSON-blokken)
    for w in blok.get("weergaven") or []:
        out += "\n\n" + render_weergave(w)
    return out


def render_weergave(w: dict) -> str:
    wtype = w.get("type", "?")
    if wtype == "proza":
        return (w.get("tekst") or "").strip()
    if wtype == "berekening":
        lines = ["**Berekening:**"]
        for s in w.get("stappen", []) or []:
            lines.append(f"- {s}")
        if w.get("resultaat"):
            lines.append(f"\n→ **Resultaat**: {w['resultaat']}")
        return "\n".join(lines)
    if wtype == "boeking":
        lines = ["**Boeking:**", ""]
        for line in w.get("regels", []) or []:
            d = "D" if line.get("zijde") == "debet" else "C"
            rek = line.get("rekening", "?")
            bedrag = line.get("bedrag", "")
            oms = line.get("omschrijving", "")
            lines.append(f"- {d} `{rek}` {bedrag} — {oms}")
        if w.get("toelichting"):
            lines.append(f"\n_{w['toelichting']}_")
        return "\n".join(lines)
    if wtype == "tabel":
        kolommen = w.get("kolommen", [])
        rijen = w.get("rijen", [])
        if not kolommen or not rijen:
            return ""
        lines = ["| " + " | ".join(kolommen) + " |", "| " + " | ".join("---" for _ in kolommen) + " |"]
        for row in rijen:
            cells = [str(c) for c in row]
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines)
    if wtype == "balans_snapshot":
        return f"**Balans-snapshot**: `{w.get('toelichting','')}`\n\n```json\n{json.dumps({k:v for k,v in w.items() if k!='type'}, indent=2, ensure_ascii=False)}\n```"
    # fallback: JSON-dump
    payload = {k: v for k, v in w.items() if k not in ("type", "grondslag")}
    return f"**Weergave** `{wtype}`:\n\n```json\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n```"


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
                    line += f" → [[{item['relateert_naar']}]]"
                lines.append(line)
            else:
                lines.append(f"- {item}")
    return "\n".join(lines)


def render_bouwsteen(b: dict, depth: int = 3) -> str:
    naam = naam_str(b.get("naam"))
    btype = b.get("bouwsteen_type", "")
    icon = BOUWSTEEN_ICON.get(btype, "•")
    parts = [f"{'#' * depth} {icon} {naam}  \n_`{btype}`_"]
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
    ctype = sc.get("concept_type", "")
    parts = [f"{'#' * depth} 📦 {naam}  \n_`{ctype}` (subconcept)_"]
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


def render_voorbeeld(v: dict, depth: int = 3) -> str:
    titel = v.get("titel") or naam_str(v.get("naam")) or "Voorbeeld"
    icon = confidence_icon(v.get("grondslag"))
    parts = [f"{'#' * depth} 💡 {titel} {icon}".rstrip()]
    if v.get("context"):
        parts.append(f"_{v['context']}_")
    for w in v.get("weergaven") or []:
        parts.append(render_weergave(w))
    bronnen = render_bronnen(v.get("grondslag"))
    if bronnen:
        parts.append(f"<small>📚 {bronnen}</small>")
    return "\n\n".join(parts)


def render_valkuil(vk: dict, depth: int = 3) -> str:
    titel = vk.get("titel") or "Valkuil"
    parts = [f"{'#' * depth} ⚠️ {titel}"]
    if vk.get("verkeerde_assumptie"):
        parts.append(f"**Verkeerde assumptie**: {vk['verkeerde_assumptie']}")
    if vk.get("kernpunt"):
        parts.append(f"**Kernpunt**: {vk['kernpunt']}")
    if vk.get("toelichting"):
        parts.append(vk["toelichting"])
    bronnen = render_bronnen(vk.get("grondslag"))
    if bronnen:
        parts.append(f"<small>📚 {bronnen}</small>")
    return "\n\n".join(parts)


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
    titel = s.get("titel") or "Synthese"
    stype = s.get("type", "")
    parts = [f"{'#' * depth} 🧩 {titel}  \n_`{stype}`_"]
    if s.get("intro"):
        parts.append(s["intro"])
    # matrix
    if s.get("kolommen") and s.get("rijen"):
        kol = s["kolommen"]
        parts.append("| " + " | ".join(kol) + " |")
        parts.append("| " + " | ".join("---" for _ in kol) + " |")
        for row in s["rijen"]:
            cells = [str(c) for c in row] if isinstance(row, list) else [str(row.get(k, "")) for k in kol]
            parts.append("| " + " | ".join(cells) + " |")
    # beslisboom in mermaid
    if s.get("mermaid"):
        parts.append("```mermaid\n" + s["mermaid"] + "\n```")
    if s.get("toelichting"):
        parts.append(s["toelichting"])
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
            line = f"- [[{target}]]"
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
            line += f" → [[{ref}]]"
        if richting and richting != "niet-verwijzen":
            line += f" _({richting})_"
        lines.append(line)
    return "\n".join(lines)


def render_metadata_strip(meta: dict) -> str:
    bits = []
    if cats := meta.get("categorieen"):
        bits.append(" · ".join(CATEGORIE_LABEL.get(c, c) for c in cats))
    if ankers := meta.get("ankers"):
        bits.append("Anchors: " + " · ".join(f"`{a}`" for a in ankers[:6]))
    prov = meta.get("provenance") or {}
    if prov.get("wave_id"):
        bits.append(f"Wave: `{prov['wave_id']}`")
    return " · ".join(bits)


def render_status_banner(meta: dict, geldigheid: dict | None) -> str:
    status = meta.get("status", "")
    banners = []
    if status == "skeleton":
        banners.append("> [!warning] 🌱 **Skeleton** — alleen structuur + scope; geen content (nog).")
    elif status == "concept":
        banners.append("> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.")
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

    parts = [f"# {naam}", f"_{type_label}_", render_metadata_strip(meta)]

    banner = render_status_banner(meta, geldigheid)
    if banner:
        parts.append(banner)

    # synoniemen + afkorting
    if naam_dict := rec.get("naam"):
        bits = []
        if afk := naam_dict.get("afkorting"):
            bits.append(f"**Afk.**: {afk}")
        if syn := naam_dict.get("synoniemen"):
            bits.append("**Synoniemen**: " + " · ".join(syn))
        if vert := naam_dict.get("vertaling"):
            bits.append("**Vertalingen**: " + " · ".join(f"{k}: {v}" for k, v in vert.items()))
        if bits:
            parts.append(" — ".join(bits))

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
