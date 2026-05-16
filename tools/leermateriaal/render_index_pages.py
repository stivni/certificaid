"""
Genereer Quartz-landingspagina's (index.md) voor de catalogus-mappen.

Maakt deze index-pagina's aan:
- content/index.md  — site-landing met overzicht van alle PO's + ingangen
- content/studiemateriaal/index.md  — lijst van alle PO-minicursussen
- content/concepten/index.md  — alfabetisch overzicht + filter per PO
- content/competenties/index.md  — alfabetisch overzicht + filter per PO

Voor elke PO die een minicursus heeft als index.md (in studiemateriaal/<slug>/),
wordt geen extra index aangemaakt — die staat al via render_minicursus.py.

Geen Opus-LLM; volledig deterministisch.

Gebruik:
  python3 -m tools.leermateriaal.render_index_pages
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
COMPETENTIES_DIR = ROOT / "data" / "concepten" / "competenties"
LEERPADEN_DIR = ROOT / "data" / "concepten" / "leerpaden"
STUDIEMATERIAAL_DIR = ROOT / "content" / "studiemateriaal"
CONCEPTEN_DIR = ROOT / "content" / "concepten"
COMPETENTIES_OUT_DIR = ROOT / "content" / "competenties"
PROGRAMMA_FILE = ROOT / "data" / "programma" / "programma.json"


def _po_titels() -> dict[str, str]:
    """Map PO-code naar titel."""
    if not PROGRAMMA_FILE.exists():
        return {}
    data = json.loads(PROGRAMMA_FILE.read_text(encoding="utf-8"))
    return {
        str(po["code"]): po.get("titel", "")
        for po in data.get("programmaonderdelen", [])
        if po.get("code")
    }


def _records_per_po() -> dict[str, list[dict]]:
    """Groepeer concept-records per PO."""
    per_po: dict[str, list[dict]] = defaultdict(list)
    for p in sorted(RECORDS_DIR.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        pos = set()
        for a in r.get("linked_anchors", []):
            pos.add(".".join(a.split(".")[:2]))
        for po in pos:
            per_po[po].append(r)
    return per_po


def _competenties_per_po() -> dict[str, list[dict]]:
    """Groepeer competentie-yamls per PO."""
    per_po: dict[str, list[dict]] = defaultdict(list)
    for p in sorted(COMPETENTIES_DIR.glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        try:
            c = yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        for po in c.get("programmaonderdelen", []) or []:
            per_po[str(po)].append(c)
    return per_po


def _studiemateriaal_folders() -> list[tuple[str, str, Path]]:
    """Lijst van (po_code, slug, path) voor elke minicursus.

    Plat: minicursussen zijn `.md`-bestanden direct onder
    `content/studiemateriaal/`. Slug-conventie: '1-4-geconsolideerde-
    jaarrekening' (dashes i.p.v. dots — serve-handler-compat). PO-code
    wordt teruggevormd door leidende numerieke segmenten met '.' samen
    te voegen ('1-4' → '1.4').
    """
    folders = []
    if not STUDIEMATERIAAL_DIR.exists():
        return folders
    for f in sorted(STUDIEMATERIAAL_DIR.iterdir()):
        # Skip index.md zelf + niet-md
        if not f.is_file() or f.suffix != ".md" or f.name == "index.md":
            continue
        slug = f.stem
        tokens = slug.split("-")
        leading_num: list[str] = []
        for t in tokens:
            if t.isdigit():
                leading_num.append(t)
            else:
                break
        po_code = ".".join(leading_num) if leading_num else slug
        folders.append((po_code, slug, f))
    return folders


def _frontmatter(title: str, *, tags: list[str] | None = None) -> str:
    lines = ["---", f"title: {json.dumps(title, ensure_ascii=False)}"]
    if tags:
        lines.append("tags:")
        for t in tags:
            lines.append(f"  - {t}")
    lines.append(f"gegenereerd_op: '{datetime.now(timezone.utc).date().isoformat()}'")
    lines.append("---")
    return "\n".join(lines) + "\n"


def render_site_landing(po_titels: dict[str, str], studiemateriaal: list) -> str:
    """`content/index.md` — site-landing."""
    out = [_frontmatter("Certificaid")]
    out.append("# Certificaid\n")
    out.append("Kennisbank voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant.\n")
    out.append("## Studiemateriaal\n")
    out.append("<div class=\"two-column-list\">\n")
    aanwezige_pos = sorted({po for po, _, _ in studiemateriaal})
    for po in aanwezige_pos:
        titel = po_titels.get(po, "")
        slug = next((s for p, s, _ in studiemateriaal if p == po), "")
        if slug:
            out.append(f"- [[studiemateriaal/{slug}|{po} {titel}]]")
    out.append("\n</div>\n")
    out.append("## Catalogi\n")
    out.append("- [[concepten/index|Alle concepten]]")
    out.append("- [[competenties/index|Alle competenties]]\n")
    return "\n".join(out)


def render_studiemateriaal_index(po_titels: dict[str, str], studiemateriaal: list) -> str:
    """`content/studiemateriaal/index.md`."""
    out = [_frontmatter("Studiemateriaal")]
    out.append("# Studiemateriaal\n")
    out.append("<div class=\"two-column-list\">\n")
    for po, slug, _ in sorted(studiemateriaal):
        titel = po_titels.get(po, "")
        out.append(f"- [[studiemateriaal/{slug}|{po} {titel}]]")
    out.append("\n</div>\n")
    return "\n".join(out)


def render_concepten_index(records_per_po: dict[str, list[dict]], po_titels: dict[str, str]) -> str:
    """`content/concepten/index.md` — alfabetisch overzicht + per-PO sectie."""
    out = [_frontmatter("Concept-index", tags=["catalogus"])]
    out.append("# Concept-index\n")
    out.append("Alle concept-records, gegroepeerd per programmaonderdeel. Een concept kan in meerdere PO's voorkomen via `linked_anchors`.\n")

    # Verzamel unieke records
    alle_records: dict[str, dict] = {}
    for recs in records_per_po.values():
        for r in recs:
            rid = r.get("id", "")
            if rid:
                alle_records[rid] = r

    out.append(f"**Totaal**: {len(alle_records)} concept-records over {len(records_per_po)} programmaonderdelen.\n")

    # Per PO sectie
    for po in sorted(records_per_po.keys()):
        titel = po_titels.get(po, "")
        records = sorted(records_per_po[po], key=lambda r: r.get("naam", ""))
        out.append(f"## {po} {titel} ({len(records)} records)\n")
        out.append("<div class=\"two-column-list\">\n")
        for r in records:
            out.append(f"- [[{r.get('id', '')}|{r.get('naam', r.get('id', ''))}]] · `{r.get('node_type', '?')}`")
        out.append("\n</div>\n")

    return "\n".join(out)


def render_competenties_index(competenties_per_po: dict[str, list[dict]], po_titels: dict[str, str]) -> str:
    """`content/competenties/index.md` — overzicht per PO."""
    out = [_frontmatter("Competentie-index", tags=["catalogus"])]
    out.append("# Competentie-index\n")
    out.append("Werkstap-procedures die je als stagiair moet kunnen uitvoeren, gegroepeerd per programmaonderdeel.\n")

    alle_comp: dict[str, dict] = {}
    for comps in competenties_per_po.values():
        for c in comps:
            cid = c.get("id", "")
            if cid:
                alle_comp[cid] = c

    out.append(f"**Totaal**: {len(alle_comp)} competentie-yamls over {len(competenties_per_po)} programmaonderdelen.\n")

    for po in sorted(competenties_per_po.keys()):
        titel = po_titels.get(po, "")
        comps = sorted(competenties_per_po[po], key=lambda c: c.get("titel", ""))
        out.append(f"## {po} {titel} ({len(comps)} competenties)\n")
        out.append("<div class=\"two-column-list\">\n")
        for c in comps:
            badge = ""
            grondslag = c.get("procedure_grondslag", {}) or {}
            wpct = grondslag.get("wettelijk_pct", 0)
            ppct = grondslag.get("praktijk_pct", 0)
            if wpct or ppct:
                badge = f" · ⚖️ {wpct}% · 🤖 {ppct}%"
            out.append(f"- [[competenties/{c.get('id', '')}|{c.get('titel', '')}]]{badge}")
        out.append("\n</div>\n")

    return "\n".join(out)


def main() -> None:
    po_titels = _po_titels()
    records_per_po = _records_per_po()
    competenties_per_po = _competenties_per_po()
    studiemateriaal = _studiemateriaal_folders()

    # Landing
    landing_md = render_site_landing(po_titels, studiemateriaal)
    (ROOT / "content" / "index.md").write_text(landing_md, encoding="utf-8")
    print(f"[index] content/index.md ({len(landing_md)} bytes)")

    # Studiemateriaal-folder index
    sm_index = render_studiemateriaal_index(po_titels, studiemateriaal)
    (STUDIEMATERIAAL_DIR / "index.md").write_text(sm_index, encoding="utf-8")
    print(f"[index] content/studiemateriaal/index.md ({len(sm_index)} bytes)")

    # Concepten-folder index
    CONCEPTEN_DIR.mkdir(parents=True, exist_ok=True)
    cp_index = render_concepten_index(records_per_po, po_titels)
    (CONCEPTEN_DIR / "index.md").write_text(cp_index, encoding="utf-8")
    print(f"[index] content/concepten/index.md ({len(cp_index)} bytes)")

    # Competenties-folder index
    COMPETENTIES_OUT_DIR.mkdir(parents=True, exist_ok=True)
    comp_index = render_competenties_index(competenties_per_po, po_titels)
    (COMPETENTIES_OUT_DIR / "index.md").write_text(comp_index, encoding="utf-8")
    print(f"[index] content/competenties/index.md ({len(comp_index)} bytes)")


if __name__ == "__main__":
    main()
