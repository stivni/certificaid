"""Extractor voor `custom_wetboek` — Fisconet/JUSTEL wetboek-PDFs.

Gekopieerd uit `tools/etl/convert-wetboek.py` (functies extract_nl_text,
clean_and_structure, clean_and_structure_eu, met de YAML-leeskant verwijderd —
wij krijgen `cfg` direct).

Voor entries met `extract.params.script` (bv. Oud-BW met een eigen converter):
fallback naar subprocess en lees daarna het resultaat. De orchestrator gooit
de subprocess-output door dezelfde cleanup heen — dat is dubbel werk maar
veiliger dan het complete script in-process kopiëren voor één bron.

Modi (zoals in source_config.yaml):
  - "nl"           → pdftotext -layout, één kolom
  - "bilingual"    → rechterkolom (NL) per pagina via -x/-W
  - "eu_richtlijn" → pdftotext zonder -layout (EU Official Journal)
  - None / overig  → fallback naar `extract.params.script` als gespecifieerd
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import (  # noqa: E402
    fix_broken_words,
    merge_heading_continuations,
    merge_wrapped_lines,
)


# ─── PDF-extractie ────────────────────────────────────────────────────────────

def _extract_nl_text(pdf: str, mode: str, start_page: int | None = None,
                     col_x: int | None = None,
                     col_w: int | None = None,
                     page_w: int = 595, page_h: int = 842) -> str:
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    pages_match = re.search(r"Pages:\s+(\d+)", info)
    total_pages = int(pages_match.group(1)) if pages_match else 300

    if mode == "eu_richtlijn":
        r = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True)
        return r.stdout
    if mode == "nl":
        r = subprocess.run(
            ["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True,
        )
        return r.stdout

    # Bilingual: extraheer NL-kolom per pagina.
    # NB: in de Fisconet/JUSTEL-PDFs voor BE-wetboeken staat NL standaard *links*
    # (col_x=0..297). De vorige default (col_x=300) sloeg de FR-kolom uit;
    # daarom is de default nu 0. Belangrijk: gebruik `is None`-checks i.p.v.
    # truthy-fallbacks, anders valt `col_x: 0` per ongeluk terug op de default.
    if col_x is None:
        col_x = 0
    if col_w is None:
        # Net iets breder dan halve A4-breedte: pakt het laatste woord van de
        # NL-zin mee zonder FR-fragmenten binnen te halen (empirisch ~305 op
        # de Fisconet-PDFs). Wanneer col_x>0 (NL rechts) gebruiken we de rest
        # van de pagina-breedte.
        col_w = 310 if col_x == 0 else max(1, page_w - col_x)
    parts: list[str] = []
    sp = start_page or 1
    for p in range(sp, total_pages + 1):
        r = subprocess.run(
            ["pdftotext", "-layout", "-f", str(p), "-l", str(p),
             "-x", str(col_x), "-y", "0", "-W", str(col_w), "-H", str(page_h),
             pdf, "-"],
            capture_output=True, text=True,
        )
        parts.append(r.stdout)
    return "\n".join(parts)


# ─── Structuur en cleanup ─────────────────────────────────────────────────────

def _clean_and_structure(text: str, wet_naam: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    prev_empty = False
    in_toc = False
    seen_toc = False
    in_wijzigingsnota = False

    noise_patterns = [
        r"^(FOD Financiën|www\.fisconet|W\.Btw|W\.Reg|Federale|Overheidsdienst|Beleidsexpertise)",
        r"^BELASTING OVER DE$|^TOEGEVOEGDE WAARDE$|^WETBOEK VAN DE BTW$",
        r"^WETBOEK DER REGISTRATIE",
        r"^VLAAMSE CODEX FISCALITEIT$",
        r"^bijgewerkt tot|^BIJGEWERKT TOT",
        r"^WWW\.",
        r"^JUSTEL - Geconsolideerde wetgeving",
        r"^http://www\.ejustice",
        r"^Dossiernummer\s*:",
        r"^Situatie\s*:",
        r"^Bron\s*: (BRUSSELS|WAALSE|BRUSSEL|FOD|JUSTITIE)",
        r"^Publicatie\s*:",
        r"^Inwerkingtreding\s*:",
        r"^Nota.*:$",
        r"^Copyright Belgisch",
        r"^Pagina \d+ van \d+",
        r"^Art\.\s+[\d][\d]*[-–,/]",
        r"^[-–—=]{3,}$",
        r"^\d+$",
        r"^[IVX]+/\d+\s*-?\s*$",
        r"^-\s*[IVX]+/\d+\s*-$",
    ]

    for line in lines:
        stripped = line.strip()

        if in_wijzigingsnota:
            if not stripped:
                in_wijzigingsnota = False
                if not prev_empty:
                    out.append("")
                    prev_empty = True
            continue

        if in_toc:
            if re.match(r"^Tekst$", stripped):
                in_toc = False
                continue
            if re.match(
                r"^HOOFDSTUK\s+[IVXLC]+(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?$",
                stripped,
            ):
                in_toc = False
            elif (re.match(r"^(?:BOEK|HOOFDSTUK)\s+[IVXLC]+\w*\s+-\s+\S", stripped)
                  and not re.search(r"\.{2,}", stripped)):
                in_toc = False
            else:
                continue

        if not stripped:
            if not prev_empty:
                out.append("")
            prev_empty = True
            continue

        if not seen_toc and re.match(r"^Inhoudstafel$", stripped, re.I):
            in_toc = True
            seen_toc = True
            continue

        if (re.match(r"^Art\.\s+\d+\w*\s*,", stripped)
                and re.search(r"\b(werd|wordt|met ingang|B\.S\.|Numac)\b", stripped)):
            in_wijzigingsnota = True
            continue

        if any(re.match(p, stripped, re.I) for p in noise_patterns):
            continue
        if re.match(r"^net\w*plus\.be", stripped, re.I):
            continue

        if re.match(r"^TITEL\s+[IVXLC]+", stripped):
            if not prev_empty:
                out.append("")
            out.append(f"### {stripped}")
            out.append("")
            prev_empty = True
            continue

        if re.match(r"^HOOFDSTUK\s+", stripped):
            if not prev_empty:
                out.append("")
            out.append(f"#### {stripped}")
            out.append("")
            prev_empty = True
            continue

        if re.match(r"^(Afdeling|Onderafdeling)\s+", stripped):
            if not prev_empty:
                out.append("")
            out.append(f"##### {stripped}")
            out.append("")
            prev_empty = True
            continue

        art_match = re.match(r"^(?:Artikel|Art\.)\s+([\d][\d./\w]*)\s*\.?\s*$", stripped)
        if art_match:
            art_num = art_match.group(1).rstrip(".")
            if not prev_empty:
                out.append("")
            out.append(f"## Art. {art_num}")
            out.append("")
            prev_empty = True
            continue

        art_inline = re.match(r"^(?:Artikel|Art\.)\s+([\d][\d./\w]*\.?)\s+(.+)$", stripped)
        if art_inline:
            art_num = art_inline.group(1).rstrip(".")
            if not prev_empty:
                out.append("")
            out.append(f"## Art. {art_num}")
            out.append("")
            out.append(art_inline.group(2))
            prev_empty = False
            continue

        out.append(stripped)
        prev_empty = False

    text_out = "\n".join(out)
    text_out = fix_broken_words(text_out)
    text_out = re.sub(r"\n{3,}", "\n\n", text_out)
    text_out = merge_wrapped_lines(text_out)
    text_out = merge_heading_continuations(text_out)
    return text_out.strip()


def _clean_and_structure_eu(text: str) -> str:
    """Structureert EU Official Journal richtlijntekst naar markdown."""
    lines = text.split("\n")
    out: list[str] = []
    prev_empty = False

    eu_noise = [
        r"^L\s+\d+/\d+\s*$",
        r"^NL\s*$",
        r"^Publicatieblad van de Europese Unie",
        r"^\d{1,2}\.\d{1,2}\.\d{4}\s*$",
        r"^\(\d+\)\s*$",
        r"^C\d+/\d+\s*$",
    ]

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if not prev_empty:
                out.append("")
            prev_empty = True
            continue

        if any(re.match(p, stripped) for p in eu_noise):
            continue

        if re.match(r"^Artikel\s+\d+\s*$", stripped):
            num = re.match(r"^Artikel\s+(\d+)", stripped).group(1)
            if not prev_empty:
                out.append("")
            out.append(f"## Artikel {num}")
            out.append("")
            prev_empty = True
            continue

        if re.match(r"^BIJLAGE", stripped):
            if not prev_empty:
                out.append("")
            out.append(f"## {stripped}")
            out.append("")
            prev_empty = True
            continue

        out.append(stripped)
        prev_empty = False

    text_out = "\n".join(out)
    text_out = fix_broken_words(text_out)
    text_out = re.sub(r"\n{3,}", "\n\n", text_out)
    text_out = merge_wrapped_lines(text_out)
    text_out = merge_heading_continuations(text_out)
    return text_out.strip()


# ─── Subprocess-fallback voor `extract.params.script` ─────────────────────────

_FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


def _strip_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    if m:
        return text[m.end():]
    return text


def _run_subprocess_script(script_rel: str, source_name: str,
                           output_path: Path) -> str:
    """Roep een legacy converter-script aan en lees het resultaat (zonder frontmatter)."""
    script = ROOT / script_rel
    if not script.exists():
        raise FileNotFoundError(f"Subprocess-script niet gevonden: {script}")
    cmd = ["python3", str(script)]
    # Sommige scripts (convert-wetboek.py) accepteren een argument; andere niet.
    # We proberen eerst zonder argument te draaien — convert-oud-bw.py heeft géén
    # argumenten en convert-wetboek.py-style scripts bestaan niet voor deze tak.
    # Voor zekerheid testen we of het script de naam als arg accepteert:
    #   - convert-oud-bw.py negeert argumenten en schrijft een vaste output.
    # We voegen `source_name` toe wanneer het pad expliciet "wetboek" matcht.
    if "convert-wetboek" in script_rel:
        cmd.append(source_name)
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        raise RuntimeError(
            f"Subprocess-script faalde ({script.name}): {result.stderr[:500]}"
        )
    if not output_path.exists():
        raise FileNotFoundError(
            f"Subprocess voltooid maar output ontbreekt: {output_path}"
        )
    return _strip_frontmatter(output_path.read_text(encoding="utf-8"))


# ─── Publieke handler ─────────────────────────────────────────────────────────

def extract(cfg: dict, source_name: str) -> str:
    """Extract custom_wetboek-bron → gestructureerde markdown body."""
    extract_cfg = cfg.get("extract") or {}
    params = extract_cfg.get("params") or {}
    script_rel = params.get("script")

    if script_rel:
        # Legacy custom-script per bron (bv. Oud-BW). Subprocess + body-uitlees.
        output_rel = cfg.get("output")
        if not output_rel:
            raise ValueError(
                f"`extract.params.script` zonder `output` voor {source_name}"
            )
        return _run_subprocess_script(script_rel, source_name, ROOT / output_rel)

    raw_rel = cfg.get("raw")
    if not raw_rel:
        raise ValueError(f"raw-pad ontbreekt voor {source_name}")
    pdf_path = ROOT / raw_rel
    if not pdf_path.exists():
        raise FileNotFoundError(f"Raw PDF niet gevonden: {pdf_path}")

    # Parameters mogen zowel top-level (legacy) als onder `extract.params` staan.
    # `extract.params` heeft voorrang wanneer beide gezet zijn.
    def _pick(key: str):
        if key in params:
            return params[key]
        return cfg.get(key)

    mode = _pick("mode") or "nl"
    start_page = _pick("start_page")
    # Belangrijk: `0` is een geldige col_x-waarde (NL-kolom links). Gebruik dus
    # geen `or`-fallback (truthy-bug); test expliciet op None.
    col_x = _pick("col_x")
    col_w = _pick("col_w")

    raw_text = _extract_nl_text(
        str(pdf_path), mode, start_page=start_page, col_x=col_x, col_w=col_w,
    )

    if mode == "eu_richtlijn":
        return _clean_and_structure_eu(raw_text)

    wet_naam = cfg.get("wet", source_name)
    return _clean_and_structure(raw_text, wet_naam)
