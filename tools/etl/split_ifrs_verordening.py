"""
Split de EU-Verordening 2023/1803 (geconsolideerde IFRS) per standaard naar
individuele markdown-bestanden.

Output: resources/bronnen/wetteksten/IAS-<n>-<slug>.md (+ IFRS + IFRIC)

Elke output-MD krijgt YAML-frontmatter met:
- title, bron_type, bron_rol, bron_categorie
- standaard_nummer, standaard_type (IAS/IFRS/IFRIC)
- bron_pdf, bron_pdf_sha256, bron_pdf_bladzijdes (pages_from-to)
- trust_status: unreviewed (QA-pass volgt later)

Het script registreert ook elke geproduceerde markdown in source_config.yaml
als individuele bron-entry.

Eenmalig draaien:
  python3 -m tools.etl.split_ifrs_verordening
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

import pymupdf
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
PDF_PATH = ROOT / "resources" / "raw" / "wetteksten" / "EU-Verordening-2023-1803-IFRS-Geconsolideerd.pdf"
OUT_DIR = ROOT / "resources" / "bronnen" / "wetteksten"
SOURCE_CONFIG = ROOT / "resources" / "source_config.yaml"

VERORDENING = "Verordening (EU) 2023/1803 — geconsolideerde IFRS"
VERORDENING_DATUM = "13.08.2023"


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[àáâäåã]", "a", s)
    s = re.sub(r"[èéêë]", "e", s)
    s = re.sub(r"[ìíîï]", "i", s)
    s = re.sub(r"[òóôöõ]", "o", s)
    s = re.sub(r"[ùúûü]", "u", s)
    s = re.sub(r"[ñ]", "n", s)
    s = re.sub(r"[ç]", "c", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def detect_standards(doc: pymupdf.Document) -> list[dict]:
    """Detecteer alle IAS/IFRS/IFRIC-standaarden met start-pagina en titel.

    Returns: list of dicts with keys: type, nummer, titel, start_page (1-indexed)
    """
    standards: list[dict] = []
    seen: set[tuple[str, str]] = set()

    # Headers staan boven elke standaard, typisch op een eigen pagina-top
    # IAS: "INTERNATIONAL ACCOUNTING STANDARD <N>"
    # IFRS: "INTERNATIONAL FINANCIAL REPORTING STANDARD <N>"
    # IFRIC: "IFRIC-INTERPRETATIE <N>" of "IFRIC INTERPRETATIE <N>"
    pat_ias = re.compile(r"INTERNATIONAL\s+ACCOUNTING\s+STANDARD\s+(\d+)\b", re.IGNORECASE)
    pat_ifrs = re.compile(r"INTERNATIONAL\s+FINANCIAL\s+REPORTING\s+STANDARD\s+(\d+)\b", re.IGNORECASE)
    pat_ifric = re.compile(r"IFRIC[‑\- ]?INTERPRETATIE\s+(\d+)\b", re.IGNORECASE)

    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        lines = text.split("\n")
        # Scan eerste 8 niet-lege regels (page-header zone)
        first_lines = [l for l in lines[:12] if l.strip()][:6]
        first_blob = "\n".join(first_lines)

        for pat, kind in [(pat_ias, "IAS"), (pat_ifrs, "IFRS"), (pat_ifric, "IFRIC")]:
            m = pat.search(first_blob)
            if not m:
                continue
            nummer = m.group(1)
            key = (kind, nummer)
            if key in seen:
                continue
            seen.add(key)
            # Titel is meestal de volgende non-empty regel
            titel = ""
            idx_in_lines = None
            for i, line in enumerate(lines):
                if pat.search(line):
                    idx_in_lines = i
                    break
            if idx_in_lines is not None:
                # Zoek eerstvolgende niet-lege niet-numerieke regel
                for j in range(idx_in_lines + 1, min(idx_in_lines + 6, len(lines))):
                    cand = lines[j].strip()
                    if cand and not cand.isdigit() and len(cand) > 3:
                        titel = cand
                        break
            standards.append({
                "type": kind,
                "nummer": nummer,
                "titel": titel,
                "start_page": page_num,
            })

    # Sort by page
    standards.sort(key=lambda s: s["start_page"])
    return standards


def page_text(doc: pymupdf.Document, page_num: int) -> str:
    """Tekst van pagina N (1-indexed) met header/footer-strip."""
    page = doc[page_num - 1]
    text = page.get_text()
    # Strip page-headers (eerste 3 regels die EU-publicatieblad-formaat hebben)
    lines = text.split("\n")
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^L\s+\d+/\d+\s*$", stripped):  # bv. "L 237/35"
            continue
        if re.match(r"^\d{1,2}\.\d{1,2}\.\d{4}\s*$", stripped):  # datum bv. "26.9.2023"
            continue
        if stripped == "NL":  # taal-marker
            continue
        if re.match(r"^Publicatieblad van de Europese Unie\s*$", stripped):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_standard_text(doc: pymupdf.Document, start: int, end: int) -> str:
    """Tekst van pagina-range [start, end) (1-indexed, end exclusive)."""
    parts: list[str] = []
    for p in range(start, end):
        parts.append(page_text(doc, p))
    return "\n\n".join(parts)


def normalize_text(raw: str) -> str:
    """Tekst-normalisatie: hyphenated-merge + paragraph-flow.

    PDF-extract levert één `\\n` per gerenderde lijn op. Paragrafen zijn
    gescheiden door blank-line (`\\n\\n`). Binnen een paragraaf: single `\\n`
    → spatie zodat zinnen doorlopen. Hyphenated breaks worden gemerged.
    """
    raw = raw.replace("\x0c", "\n")
    raw = raw.replace("\xad", "")
    # Hyphenated word over linebreak: "boekhoud-\nkundig" → "boekhoudkundig"
    raw = re.sub(r"(\w)-\n(\w)", r"\1\2", raw)
    # Triple-blanks → double-blanks (paragraph-break)
    raw = re.sub(r"\n{3,}", "\n\n", raw)

    # Split in paragrafen op blank-line, join single \n binnen paragraaf
    paragraphs = raw.split("\n\n")
    normalized: list[str] = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # Skip joining op kennelijke lijst-items + headings
        # Lijst-items beginnen met "(a) " of "(i) " of "- " of "1." of "2." enz.
        lines = para.split("\n")
        if len(lines) == 1:
            normalized.append(lines[0])
            continue
        out_lines: list[str] = []
        buffer = lines[0].rstrip()
        for line in lines[1:]:
            stripped = line.strip()
            # Lijst-item-start? Flush buffer + start nieuwe regel
            if re.match(r"^\(?(?:[a-zA-Z]|[ivxIVX]+|\d+)\)[\s.]", stripped) or stripped.startswith("- "):
                out_lines.append(buffer)
                buffer = stripped
            # Continuation: join met spatie
            else:
                buffer = buffer + " " + stripped
        out_lines.append(buffer)
        normalized.append("\n".join(out_lines))
    return "\n\n".join(normalized).strip()


SECTION_KEYWORDS = {
    "DOEL", "TOEPASSINGSGEBIED", "DEFINITIES", "INLEIDING",
    "ALGEMENE OVERWEGINGEN", "OPNAME", "WAARDERING", "PRESENTATIE",
    "INFORMATIEVERSCHAFFING", "OVERGANGSBEPALINGEN", "INGANGSDATUM",
    "INTREKKING VAN ANDERE UITSPRAKEN", "REFERENTIES", "ACHTERGROND",
    "CONSENSUS", "INGANGSDATUM EN OVERGANG", "TOELICHTING",
    "GRONDSLAGEN VOOR HET OPSTELLEN VAN CONCLUSIES",
    "RICHTLIJNEN VOOR DE TOEPASSING",
    "ILLUSTRATIEVE VOORBEELDEN",
    "OPNAME ALS LAST", "WAARDERING VAN VOORRADEN",
}


def mark_headings(raw: str) -> str:
    """Markeer all-caps regels die headings zijn met placeholder.

    Placeholder format: `\\n\\n@@HEADING@@<text>@@\\n\\n` zodat ze de paragraph-
    merge overleven. Worden later vervangen door `## <Title>`.
    """
    lines = raw.split("\n")
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out.append("")
            continue
        upper = stripped.upper() == stripped
        short = 3 <= len(stripped) <= 80
        has_alpha = any(c.isalpha() for c in stripped)
        no_dash = "—" not in stripped and "-" not in stripped
        is_keyword = stripped.upper() in SECTION_KEYWORDS
        # All-caps + short + alfabetisch + no em-dash → vermoedelijk heading
        if is_keyword or (upper and short and has_alpha and no_dash and not stripped.endswith(".")):
            out.append("")
            out.append(f"@@HEADING@@{stripped.title()}@@")
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def to_markdown(raw_text: str, std: dict) -> str:
    """Markdown-conversion met heading-bescherming.

    Stappen:
    1. Markeer heading-lijnen met placeholder vóór paragraph-merge
    2. Normalize (paragraph-merge + hyphen-merge)
    3. Vervang placeholders door `## <heading>`
    """
    marked = mark_headings(raw_text)
    normalized = normalize_text(marked)
    # Vervang placeholders door echte heading
    normalized = re.sub(r"@@HEADING@@(.+?)@@", r"\n\n## \1\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def build_frontmatter(std: dict, end_page: int, pdf_sha: str) -> dict:
    """Frontmatter conform bestaande wetteksten-conventie (provenance.trust.status)."""
    code = f"{std['type']}-{std['nummer']}"
    titel = f"{code} — {std['titel']}" if std["titel"] else code
    iso_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "title": titel,
        "tags": ["1.5", "ifrs", std["type"].lower()],
        "itaa-lex-sectie": "",
        "wet": VERORDENING,
        "bron_rol": "normatief",
        "bron_categorie": "ifrs",
        "standaard_type": std["type"],
        "standaard_nummer": std["nummer"],
        "status": "beschikbaar",
        "bijgewerkt": VERORDENING_DATUM,
        "bron": "EUR-Lex CELEX 32023R1803",
        "chunk": {
            "level": 2,
            "type": "Sectie",
            "sub_strategy": None,
        },
        "provenance": {
            "inputs": [
                {
                    "id": str(PDF_PATH.relative_to(ROOT)),
                    "sha256": pdf_sha,
                    "version": VERORDENING_DATUM,
                    "pages": f"{std['start_page']}-{end_page - 1}",
                }
            ],
            "tooling": {
                "pipeline": "tools/etl/split_ifrs_verordening.py",
                "pipeline_version": "1.0",
                "model": None,
                "prompt_version": None,
            },
            "generated_at": iso_now,
            "stale": False,
            "stale_reason": None,
            "trust": {
                "status": "unreviewed",
                "confirmed_at": None,
                "confirmed_by": None,
                "rationale": (
                    "ETL-output: pymupdf-extractie + heading-detectie (DOEL/TOEPASSINGSGEBIED/"
                    "DEFINITIES etc.) + paragraph-merge. QA-pass nodig om heading-correctheid en "
                    "incidentele woord-splits (zoals 'op brengstwaarde', erfgenaam van PDF-kolom-"
                    "wrap) te valideren. EU-publicatieblad CELEX 32023R1803 = primary law."
                ),
            },
        },
    }


def write_standard(std: dict, body_md: str, frontmatter: dict, dry_run: bool = False) -> Path:
    slug = slugify(std["titel"]) if std["titel"] else f"standaard-{std['nummer']}"
    filename = f"{std['type']}-{std['nummer']}-{slug}.md"
    out_path = OUT_DIR / filename
    if dry_run:
        return out_path
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fm_yaml = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    content = f"---\n{fm_yaml}---\n\n{body_md}\n"
    out_path.write_text(content, encoding="utf-8")
    return out_path


def main() -> None:
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF niet gevonden: {PDF_PATH}")

    print(f"[ifrs-split] Open {PDF_PATH.name}")
    pdf_bytes = PDF_PATH.read_bytes()
    pdf_sha = hashlib.sha256(pdf_bytes).hexdigest()
    doc = pymupdf.open(PDF_PATH)
    total_pages = len(doc)
    print(f"[ifrs-split] {total_pages} pagina's, sha256={pdf_sha[:16]}...")

    standards = detect_standards(doc)
    print(f"[ifrs-split] {len(standards)} standaarden gevonden")
    for s in standards:
        print(f"  p{s['start_page']:3d}  {s['type']:5s} {s['nummer']:3s}  {s['titel']}")

    written: list[tuple[str, Path]] = []
    for i, std in enumerate(standards):
        start = std["start_page"]
        end = standards[i + 1]["start_page"] if i + 1 < len(standards) else total_pages + 1
        raw = extract_standard_text(doc, start, end)
        md = to_markdown(raw, std)
        fm = build_frontmatter(std, end, pdf_sha)
        out_path = write_standard(std, md, fm)
        written.append((f"{std['type']}-{std['nummer']}", out_path))
        print(f"[ifrs-split] wrote {out_path.relative_to(ROOT)} ({len(md):,} chars)")

    doc.close()
    print(f"\n[ifrs-split] {len(written)} bestanden geschreven naar {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
