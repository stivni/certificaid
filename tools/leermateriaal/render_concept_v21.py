"""Schema 2.1 concept-fiche render — v1 minimal voor inspectie.

Doel: alle 396 schema 2.1-records snel naar Quartz-markdown krijgen zodat de
gebruiker visueel kan inspecteren wat er in zit. Niet productie-perfect:

- Confidence-iconen per claim
- Seed-banner bovenaan zolang `claims_checken` niet in operaties_uitgevoerd staat
- Elementen-recursie zonder collapsibles (max 4 niveaus)
- Stub-records (lege `inhoud`) krijgen een placeholder-fiche
- Relaties als platte sectie onderaan
- Geen specialised weergave-rendering (boeking/balans/formule worden als JSON-dump getoond)

Usage:
    python3 -m tools.leermateriaal.render_concept_v21               # render alle 396
    python3 -m tools.leermateriaal.render_concept_v21 --slug=kapitaalvermindering
    python3 -m tools.leermateriaal.render_concept_v21 --limit=5
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
    "methode": "Methode",
    "kader": "Kader",
    "principe": "Principe",
    "actor": "Actor",
}

INHOUD_LABEL = {
    "definitie": "Definitie",
    "substantie": "Economische substantie",
    "rationale": "Rationale",
    "voorkennis_leespad": "Voorkennis & leespad",
    "gebruikscontext": "Gebruikscontext",
    "elementen": "Inhoud",
    "voorbeelden": "Voorbeelden",
    "rollen_per_perspectief": "Rollen per perspectief",
    "keuzekader": "Keuzekader",
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


def naam_str(naam: dict | None) -> str:
    if not naam:
        return ""
    return naam.get("primair", "")


def confidence_icon(grondslag: dict | None) -> str:
    if not grondslag:
        return ""
    conf = grondslag.get("confidence", "")
    icon = CONFIDENCE_ICON.get(conf, "")
    if conf == "verondersteld" and any(
        b.get("type") == "mens" for b in grondslag.get("bronnen", [])
    ):
        icon = "🧠"
    return icon


def render_bronnen(grondslag: dict | None) -> str:
    if not grondslag:
        return ""
    bronnen = grondslag.get("bronnen", [])
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


def render_tekstblok(blok: dict | None, inline_icon: bool = True) -> str:
    if not blok:
        return ""
    text = blok.get("text", "").strip()
    if not text:
        return ""
    grondslag = blok.get("grondslag", {})
    icon = confidence_icon(grondslag)
    bronnen = render_bronnen(grondslag)
    out = text
    if inline_icon and icon:
        out = f"{icon} {out}"
    if bronnen:
        out += f"\n\n<small>📚 {bronnen}</small>"
    weerlegging = grondslag.get("weerlegging")
    if weerlegging:
        out += f"\n\n> ❌ **Weerlegd**: {weerlegging}"
    return out


def render_contextitem(item: dict) -> str:
    text = item.get("text", "").strip()
    icon = confidence_icon(item.get("grondslag"))
    rationale = item.get("rationale")
    rel = item.get("relateert_naar")
    parts = []
    if icon:
        parts.append(icon)
    parts.append(text)
    if rel:
        parts.append(f"→ [[{rel}]]")
    line = " ".join(parts)
    if rationale:
        line += f" _{rationale}_"
    bronnen = render_bronnen(item.get("grondslag"))
    if bronnen:
        line += f" <small>📚 {bronnen}</small>"
    return line


def render_gebruikscontext(ctx: dict) -> str:
    if not ctx:
        return ""
    lines = []
    # array-velden
    for key in ["voor", "niet_voor", "voorwaarden", "uitsluitingen", "indicaties", "contra_indicaties"]:
        items = ctx.get(key)
        if items:
            lines.append(f"\n**{GEBRUIK_LABEL.get(key, key)}**")
            for item in items:
                lines.append(f"- {render_contextitem(item)}")
    # single-item velden — schema zegt single, maar records leveren soms een lijst
    for key in ["trigger_start", "trigger_einde", "voordeel", "risico"]:
        item = ctx.get(key)
        if not item:
            continue
        items = item if isinstance(item, list) else [item]
        for it in items:
            if isinstance(it, dict):
                lines.append(f"\n**{GEBRUIK_LABEL.get(key, key)}**: {render_contextitem(it)}")
    return "\n".join(lines)


def render_voorkennis(vk: dict) -> str:
    if not vk:
        return ""
    lines = []
    if vk.get("kader"):
        lines.append(f"**Kader**: [[{vk['kader']}]]")
    if vk.get("voorvereisten"):
        lines.append(f"**Voorvereisten**: " + " · ".join(f"[[{x}]]" for x in vk["voorvereisten"]))
    if vk.get("naast_relevant"):
        lines.append(f"**Naast relevant**: " + " · ".join(f"[[{x}]]" for x in vk["naast_relevant"]))
    if vk.get("volgkennis"):
        lines.append(f"**Volgkennis**: " + " · ".join(f"[[{x}]]" for x in vk["volgkennis"]))
    return "\n".join(lines)


def render_weergave(w: dict, depth: int = 3) -> str:
    """Type-specifieke weergaven worden voorlopig als JSON-blok getoond."""
    wtype = w.get("type", "?")
    payload = {k: v for k, v in w.items() if k not in ("type", "grondslag")}
    icon = confidence_icon(w.get("grondslag"))
    header = f"{'#' * depth} Weergave · `{wtype}` {icon}".rstrip()
    if not payload:
        return header
    return f"{header}\n\n```json\n{json.dumps(payload, indent=2, ensure_ascii=False)}\n```"


def render_voorbeeld_inline(v: dict, depth: int = 4) -> str:
    naam = naam_str(v.get("naam"))
    icon = confidence_icon(v.get("grondslag"))
    out = [f"{'#' * depth} 💡 {naam} {icon}".rstrip()]
    if v.get("context"):
        out.append(f"_{v['context']}_")
    for w in v.get("weergaven", []) or []:
        out.append(render_weergave(w, depth=depth + 1))
    for el in v.get("elementen", []) or []:
        out.append(render_element(el, depth=depth + 1))
    bronnen = render_bronnen(v.get("grondslag"))
    if bronnen:
        out.append(f"<small>📚 {bronnen}</small>")
    return "\n\n".join(p for p in out if p)


def render_element(el: dict, depth: int = 3) -> str:
    naam = naam_str(el.get("naam"))
    inhoud_type = el.get("inhoud_type", "")
    icon = confidence_icon(el.get("grondslag"))
    out = [f"{'#' * min(depth, 6)} {naam} {icon}".rstrip() + f"  \n_`{inhoud_type}`_"]

    if el.get("beschrijving"):
        out.append(el["beschrijving"])
    if el.get("definitie"):
        out.append(render_tekstblok(el["definitie"]))
    if el.get("substantie"):
        out.append("**Substantie**: " + render_tekstblok(el["substantie"]))
    if el.get("rationale"):
        out.append("**Rationale**: " + render_tekstblok(el["rationale"]))

    if el.get("verwijst_naar"):
        out.append("**Verwijst naar**: " + " · ".join(f"[[{r}]]" for r in el["verwijst_naar"]))

    for w in el.get("weergaven", []) or []:
        out.append(render_weergave(w, depth=depth + 1))

    for sub in el.get("elementen", []) or []:
        out.append(render_element(sub, depth=depth + 1))

    for v in el.get("voorbeelden", []) or []:
        out.append(render_voorbeeld_inline(v, depth=depth + 1))

    bronnen = render_bronnen(el.get("grondslag"))
    if bronnen:
        out.append(f"<small>📚 {bronnen}</small>")

    return "\n\n".join(p for p in out if p)


def render_voorbeelden_top(vt) -> str:
    if not vt:
        return ""
    # Soms geleverd als platte lijst i.p.v. {cases: [...]}
    if isinstance(vt, list):
        vt = {"cases": vt}
    lines = []
    if vt.get("intro"):
        lines.append(vt["intro"])
    for case in vt.get("cases", []) or []:
        naam = naam_str(case.get("naam"))
        icon = confidence_icon(case.get("grondslag"))
        lines.append(f"### 💡 {naam} {icon}".rstrip())
        if case.get("context"):
            lines.append(f"_{case['context']}_")
        for el in case.get("elementen", []) or []:
            lines.append(render_element(el, depth=4))
        bronnen = render_bronnen(case.get("grondslag"))
        if bronnen:
            lines.append(f"<small>📚 {bronnen}</small>")
    return "\n\n".join(lines)


def render_rollen_perspectief(rp: dict) -> str:
    if not rp:
        return ""
    lines = []
    if rp.get("intro"):
        lines.append(rp["intro"])
    for p in rp.get("perspectieven", []) or []:
        pnaam = naam_str(p.get("naam"))
        lines.append(f"### Perspectief: {pnaam}")
        for r in p.get("rollen", []) or []:
            lines.append(f"#### Rol: `{r.get('rol', '?')}`")
            for el in r.get("elementen", []) or []:
                lines.append(render_element(el, depth=5))
    return "\n\n".join(lines)


def render_keuzekader(kk: dict) -> str:
    if not kk:
        return ""
    lines = []
    if kk.get("intro"):
        lines.append(kk["intro"])
    for ax in kk.get("assen", []) or []:
        lines.append(f"### {ax.get('vraag', '?')}")
        for r in ax.get("richtingen", []) or []:
            lines.append(f"- **{r.get('richting', '?')}** → [[{r.get('leidt_naar', '?')}]]")
    vt = kk.get("vergelijkingstabel")
    if vt:
        kolommen = vt.get("kolommen", [])
        rijen = vt.get("rijen", [])
        if kolommen and rijen:
            lines.append("\n### Vergelijkingstabel\n")
            lines.append("| " + " | ".join(kolommen) + " |")
            lines.append("| " + " | ".join("---" for _ in kolommen) + " |")
            for row in rijen:
                lines.append("| " + " | ".join(row) + " |")
    return "\n\n".join(lines)


def render_relaties(relaties: list) -> str:
    if not relaties:
        return ""
    lines = []
    by_type: dict[str, list] = {}
    for r in relaties:
        by_type.setdefault(r.get("type", "?"), []).append(r)
    # vergelijkbaar_met krijgt rijke rendering
    for rtype, items in by_type.items():
        lines.append(f"### `{rtype}`")
        for r in items:
            target = r.get("target", "?")
            icon = confidence_icon(r.get("grondslag"))
            line = f"- [[{target}]] {icon}".rstrip()
            toel = r.get("toelichting")
            if isinstance(toel, dict):
                toel = toel.get("text", "")
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


def render_metadata_strip(meta: dict) -> str:
    """Korte info-strip onder de titel: PO · anchors · provenance."""
    bits = []
    if meta.get("primary_po"):
        bits.append(f"PO **{meta['primary_po']}**")
    if meta.get("linked_anchors"):
        bits.append("Anchors: " + " · ".join(f"`{a}`" for a in meta["linked_anchors"]))
    if meta.get("dekt_tdks"):
        bits.append("TDK: " + " · ".join(f"`{t}`" for t in meta["dekt_tdks"]))
    prov = meta.get("provenance", {})
    if prov.get("model"):
        bits.append(f"Model: `{prov['model']}`")
    if prov.get("wave_id"):
        bits.append(f"Wave: `{prov['wave_id']}`")
    return " · ".join(bits)


def render_seed_banner(meta: dict) -> str:
    ops = meta.get("operaties_uitgevoerd") or {}
    status = meta.get("status", "seed")
    if "claims_checken" in ops:
        return ""
    if not ops and status == "seed":
        return (
            "> [!warning] ⚠️ Seed-fiche — claims niet gevalideerd\n"
            "> Deze fiche is automatisch gegenereerd uit één extractie-pas (`beschrijven`) "
            "zonder bron-validatie. Claims zijn overwegend `🤖 verondersteld` en kunnen "
            "hallucinaties bevatten. Gebruik **niet** voor examenvoorbereiding zolang "
            "`claims_checken` niet is uitgevoerd."
        )
    operatie_list = ", ".join(f"`{op}`" for op in ops.keys())
    return (
        f"> [!info] Operaties uitgevoerd: {operatie_list}\n"
        f"> Status: `{status}` — claims nog niet door `claims_checken` heen."
    )


def render_stub(rec: dict) -> str:
    """Placeholder voor records met lege inhoud."""
    naam = naam_str(rec.get("naam"))
    ctype = rec.get("concept_type", "?")
    meta = rec.get("metadata", {})
    return f"""# {naam}

> [!warning] 🌱 Stub-fiche — nog niet beschreven
> Dit concept staat in de kandidatenlijst (`{ctype}`) maar is nog niet via een
> `beschrijven`-operatie ingevuld. Alleen metadata en linked_anchors zijn aanwezig.

{render_metadata_strip(meta)}
"""


def render_record(rec: dict) -> str:
    inhoud = rec.get("inhoud") or {}
    if not inhoud:
        return render_stub(rec)

    naam = naam_str(rec.get("naam"))
    ctype = rec.get("concept_type", "?")
    type_label = CONCEPT_TYPE_LABEL.get(ctype, ctype)
    meta = rec.get("metadata", {})

    parts = [f"# {naam}", f"_{type_label}_", render_metadata_strip(meta)]

    banner = render_seed_banner(meta)
    if banner:
        parts.append(banner)

    if naam_dict := rec.get("naam"):
        synoniemen = naam_dict.get("synoniemen") or []
        afkorting = naam_dict.get("afkorting")
        andere = naam_dict.get("andere_talen") or {}
        bits = []
        if afkorting:
            bits.append(f"**Afk.**: {afkorting}")
        if synoniemen:
            bits.append("**Synoniemen**: " + " · ".join(synoniemen))
        if andere:
            bits.append("**Vertalingen**: " + " · ".join(f"{k}: {v}" for k, v in andere.items()))
        if bits:
            parts.append(" — ".join(bits))

    # Top-level inhoud-secties in vaste volgorde
    SECTIE_VOLGORDE = [
        ("definitie", lambda v: render_tekstblok(v)),
        ("substantie", lambda v: render_tekstblok(v)),
        ("rationale", lambda v: render_tekstblok(v)),
        ("voorkennis_leespad", render_voorkennis),
        ("gebruikscontext", render_gebruikscontext),
        ("elementen", lambda v: "\n\n".join(render_element(el, depth=3) for el in v)),
        ("voorbeelden", render_voorbeelden_top),
        ("rollen_per_perspectief", render_rollen_perspectief),
        ("keuzekader", render_keuzekader),
    ]
    for key, fn in SECTIE_VOLGORDE:
        v = inhoud.get(key)
        if not v:
            continue
        body = fn(v)
        if not body:
            continue
        parts.append(f"## {INHOUD_LABEL[key]}\n\n{body}")

    relaties = rec.get("relaties") or []
    if relaties:
        parts.append(f"## Relaties\n\n{render_relaties(relaties)}")

    return "\n\n".join(parts) + "\n"


def render_frontmatter(rec: dict) -> str:
    meta = rec.get("metadata") or {}
    inhoud = rec.get("inhoud") or {}
    ops = meta.get("operaties_uitgevoerd") or {}
    is_stub = not inhoud
    has_check = "claims_checken" in ops
    fm = {
        "title": naam_str(rec.get("naam")),
        "concept_type": rec.get("concept_type", ""),
        "schema_version": meta.get("schema_version", ""),
        "status": meta.get("status", ""),
        "primary_po": meta.get("primary_po", ""),
        "linked_anchors": meta.get("linked_anchors", []),
        "tags": ["concept", "schema-2.1"]
        + ([f"po-{meta['primary_po'].replace('.', '-')}"] if meta.get("primary_po") else [])
        + (["stub"] if is_stub else [])
        + (["geverifieerd"] if has_check else ["ongeverifieerd"]),
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
            if v == "":
                continue
            lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", help="Render één record (id zonder .json)")
    p.add_argument("--limit", type=int, help="Maximaal N records renderen")
    p.add_argument("--filled-only", action="store_true", help="Skip stubs (lege inhoud)")
    args = p.parse_args()

    if args.slug:
        files = [RECORDS_DIR / f"{args.slug}.json"]
    else:
        files = sorted(RECORDS_DIR.glob("*.json"))

    if args.limit:
        files = files[: args.limit]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    rendered, skipped, failed = 0, 0, 0
    for f in files:
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"PARSE-FAIL {f.name}: {e}", file=sys.stderr)
            failed += 1
            continue
        if args.filled_only and not rec.get("inhoud"):
            skipped += 1
            continue
        try:
            fm = render_frontmatter(rec)
            body = render_record(rec)
        except Exception as e:
            print(f"RENDER-FAIL {f.name}: {type(e).__name__}: {e}", file=sys.stderr)
            failed += 1
            # schrijf placeholder zodat de fiche toch in Quartz verschijnt met de fout
            naam = naam_str(rec.get("naam"))
            body = (
                f"# {naam}\n\n> [!error] Render-fout in v1\n> `{type(e).__name__}: {e}`\n\n"
                f"```json\n{json.dumps(rec, indent=2, ensure_ascii=False)[:3000]}\n```\n"
            )
            fm = render_frontmatter(rec)
        out_path = OUT_DIR / f"{rec['id']}.md"
        out_path.write_text(f"{fm}\n\n{body}", encoding="utf-8")
        rendered += 1

    print(f"Rendered: {rendered}, skipped: {skipped}, failed: {failed} → {OUT_DIR}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
