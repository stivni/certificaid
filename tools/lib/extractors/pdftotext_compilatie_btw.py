"""Extractor voor `pdftotext_compilatie_btw` — 1-op-N split-extractie.

Een compilatie-PDF (bv. WBTW-KB-compilatie.pdf of WBTW-MB-compilatie.pdf)
bevat meerdere KBs of MBs. Deze extractor levert per gevraagde split de
body-tekst, geïndexeerd op het gewenste output-pad.

De ``params.kind`` parameter (``"kb"`` of ``"mb"``, default ``"kb"``)
bepaalt welk type besluit-headers wordt herkend. Beide types delen
dezelfde extractie- en cleanup-pipeline.

Pipeline:
  1. PDF → tekst via pdftotext (zelfde aanpak als pdftotext_ejustice).
  2. Body-cleanup per split:
       a. FOD page-headers, page-numbers, bijwerkings-marginalia
          (analoog aan tools/etl/split-kb-compilatie.py).
       b. Inhoudstafel-strip (Inhoudstafel + dotted-leader-pagina-refs)
          — voorkomt dat TOC-AFDELINGen body-structuur lijken voor
          tools/lib/headings.detect_hierarchy.
       c. AFDELING-normalisatie:
            - "EERSTE AFDELING"  → "AFDELING I"
            - "TWEEDE AFDELING"  → "AFDELING II"
            - "AFDELING. III." → "AFDELING III"
       d. "Artikel N" → "Art. N" zodat tools/lib/headings._ART_RE
          (`Art\\.|Par\\.`) ze als artikel herkent en process_wettekst
          ze later naar het juiste markdown-niveau injecteert.
  3. Splits-detectie via tools/lib/compilatie_split.split_btw_compilatie
     met de SplitConfig-list opgebouwd uit cfg["splits"].

Het resultaat is determistisch: dezelfde raw PDF + dezelfde split-config
levert exact dezelfde staging-bodies. Heading-injectie (markdown-niveau-
toekenning) gebeurt nadien centraal in tools/lib/headings.process_wettekst.

Returntype: dict[output_path, body_str] — de orchestrator herkent dict
en schrijft N bestanden i.p.v. één.

Frontmatter-bouw is NIET hier — dat doet de orchestrator centraal (op basis
van de bijhorende SplitConfig-velden ``wet`` en ``extra_metadata``).
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from tools.lib.compilatie_split import SplitConfig, split_btw_compilatie
from tools.lib.inhoudstafel import strip_inhoudstafel

ROOT = Path(__file__).resolve().parents[3]


# Cleanup-patronen voor body — uit split-kb-compilatie.py overgenomen.
# Patronen dekken zowel KB- als MB-compilaties: "Btw KB", "Btw MB",
# bijwerkings-marginalia en page-footers in beide stijlen.
_BODY_NOISE = [
    re.compile(r'^FOD Financi.n.+?(?:Btw|BTW)\s+(?:KB|MB).+', re.I),
    re.compile(r'^Btw\s+(?:KB|MB)\s+nr\.\s+\d+\s+-\s+bijw.+', re.I),
    re.compile(r'^\s*-\s*\d+\s*-\s*$'),
    re.compile(r'^(?:KB|MB)\d+\w*\s+pg\..+', re.I),
    re.compile(r'^-\s*(?:KB|MB)\d+\w*\s+pg\..+', re.I),
    # Page-footer in MB-compilatie: "- MB nr. 1 / 1 -" of "- MB 28.10.2009 / 3 -".
    re.compile(
        r'^-\s*MB\s+(?:nr\.\s+\d+\w*|\d{2}[\.\-/]\d{2}[\.\-/]\d{4})'
        r'\s*/\s*\d+\s*-$',
        re.I,
    ),
    re.compile(r'^-\s*Recente wijzigingen\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^-\s*Bijlage\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^Recente wijzigingen\s+www\.fisconetplus.+', re.I),
    re.compile(r'^Lijst van de bijwerkingen\b.+', re.I),
    re.compile(r'^www\.fisconetplus\.be\b'),
    # Lijst-van-MB's pagina (TOC-footer in MB-compilatie).
    re.compile(r'^-\s*Lijst van de MB.s\s*/\s*\d+\s*-\s*$'),
    # Catch-all running header met fisconetplus URL ergens in de regel,
    # gevolgd door page-nummer-info (`pg. I/1`, `KBxx pg. yy`). Dekt
    # patronen zoals:
    #   "Tarieven                       www.fisconetplus.be          KB20   pg. I/1"
    #   "T. A - Goederen 6 pct.         www.fisconetplus.be          KB20   pg. II/1"
    # Vereist dat 'fisconetplus' ergens in de regel staat samen met `pg.\s*`
    # of `KB\d+`-marker, zodat we body-paragrafen die fisconet citeren niet
    # per ongeluk strippen.
    re.compile(
        r'^.*?\bwww\.fisconetplus\b.*?\b(?:pg\.|KB\d+|MB\d+).*$',
        re.I,
    ),
]


# ─── Heading-normalisatie patronen (per-split body-cleanup) ────────────────

_AFDELING_WORDS = {
    "EERSTE": "I", "TWEEDE": "II", "DERDE": "III", "VIERDE": "IV",
    "VIJFDE": "V", "ZESDE": "VI", "ZEVENDE": "VII", "ACHTSTE": "VIII",
    "NEGENDE": "IX", "TIENDE": "X", "ELFDE": "XI", "TWAALFDE": "XII",
}
_ART_BIS_SUFFIX = (
    r"(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|"
    r"undecies|duodecies|terdecies|quaterdecies)"
)
_ARTIKEL_PLAIN_RE = re.compile(
    rf"^[ \t]+Artikel\s+(\d+(?:{_ART_BIS_SUFFIX})?(?:/\d+)?)\s*\.?\s*$"
)
_EERSTE_AFD_RE = re.compile(
    r"^[ \t]+(" + "|".join(_AFDELING_WORDS) + r")\s+AFDELING\s*\.?\s*$"
)
_AFDELING_RE = re.compile(
    r"^(?:#{1,4}\s+)?AFDELING\.?\s+([IVXLCDM]+)\b\.?\s*(.*)$"
)

# TOC-suffix-detectoren (voor `_is_toc_line`-fallback in `_normalize_afdeling_and_artikel`).
_TOC_LINE_HINTS = (
    re.compile(r"\(art\.\s+\d+\w*\s*[\-–]\s*art\.\s+\d+\w*\)"),
    re.compile(r"\(art\.\s+\d+[^)]{0,40}\)"),
    re.compile(r"\.{3,}\s*\d+\s*$"),
    re.compile(r"\s{3,}\d+\s*$"),
)

_BIJWERKING_RE = re.compile(
    r"^\([^)]*(?:Inwerkingtreding|gewijzigd|vervangen|ingevoegd|opgeheven)"
    r"[^)]*\)\s*$",
    re.I,
)


def _is_toc_line(ln: str) -> bool:
    if not ln.strip():
        return False
    return any(p.search(ln) for p in _TOC_LINE_HINTS)


def _normalize_afdeling_and_artikel(body: str) -> str:
    """Normaliseer AFDELING- en Artikel-regels naar process_wettekst-vriendelijke vorm.

    Body-niveau-conversies (geen markdown-headings hier; die zet
    process_wettekst later op basis van detected hierarchy):
      "EERSTE AFDELING"  → "AFDELING I"
      "  AFDELING. III." → "AFDELING III"
      "  Artikel 21bis"  → "Art. 21bis"
    """
    out: list[str] = []
    for ln in body.splitlines():
        m_word = _EERSTE_AFD_RE.match(ln)
        if m_word:
            roman = _AFDELING_WORDS[m_word.group(1).upper()]
            out.append(f"AFDELING {roman}")
            continue
        m_afd = _AFDELING_RE.match(ln)
        if m_afd and not _is_toc_line(ln):
            roman = m_afd.group(1)
            tail = m_afd.group(2).strip().rstrip(".").strip()
            out.append(f"AFDELING {roman}" + (f" — {tail}" if tail else ""))
            continue
        m_art = _ARTIKEL_PLAIN_RE.match(ln)
        if m_art:
            out.append(f"Art. {m_art.group(1)}")
            continue
        out.append(ln)
    return "\n".join(out)


def _strip_bijwerking_marginalia(body: str) -> str:
    out: list[str] = []
    for ln in body.splitlines():
        if _BIJWERKING_RE.match(ln.strip()):
            continue
        out.append(ln)
    return "\n".join(out)


def _collapse_blanks(body: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", body)


def _pdftotext_layout(pdf_path: str) -> str:
    """Run pdftotext -layout op de hele PDF."""
    result = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {result.stderr}")
    return result.stdout


def _clean_body(body: str) -> str:
    """Schrap page-headers/footers + Inhoudstafel + normaliseer AFDELING/Artikel.

    Pipeline:
      1. Lijn-voor-lijn: schrap FOD/page-noise (`_BODY_NOISE`).
      2. Strip Inhoudstafel-blok (TOC met dotted-leaders + paginanummers).
      3. Normaliseer "EERSTE AFDELING" → "AFDELING I" en
         "Artikel N" → "Art. N" zodat tools/lib/headings die als
         structuurlabel resp. artikel detecteert.
      4. Strip bijwerkings-marginalia (1-line "(... gewijzigd met ...)").
      5. Collapseer 3+ opeenvolgende blanke regels.
    """
    # Stap 1: line-noise-filter
    out_lines: list[str] = []
    prev_blank = False
    for ln in body.splitlines():
        stripped = ln.strip()
        if any(p.match(stripped) for p in _BODY_NOISE):
            continue
        if not stripped:
            if prev_blank:
                continue
            prev_blank = True
        else:
            prev_blank = False
        out_lines.append(ln)
    body = "\n".join(out_lines)

    # Stap 2-5: structuur-cleanup
    body = strip_inhoudstafel(body)
    body = _normalize_afdeling_and_artikel(body)
    body = _strip_bijwerking_marginalia(body)
    body = _collapse_blanks(body)
    return body.strip() + "\n"


def _build_splits(cfg: dict) -> list[SplitConfig]:
    """Converteer cfg['splits'] (lijst van dicts) → list[SplitConfig]."""
    raw_splits = cfg.get("splits") or []
    splits: list[SplitConfig] = []
    for s in raw_splits:
        kb_id = str(s["kb_id"])
        output = s["output"]
        wet = s.get("wet", "")
        extra = s.get("extra_metadata") or {}
        # Hoist extra top-level metadata (tags, itaa_sectie, bijgewerkt, ...)
        # die soms direct op de split-entry staan i.p.v. onder extra_metadata.
        for k in ("tags", "itaa_sectie", "bijgewerkt", "titel"):
            if k in s and k not in extra:
                extra[k] = s[k]
        splits.append(SplitConfig(
            kb_id=kb_id, output=output, wet=wet, extra_metadata=extra,
        ))
    return splits


def extract_compilatie(cfg: dict, source_name: str) -> dict[str, str]:
    """Compilatie-PDF → {output_path: body_text} voor N splits.

    cfg moet bevatten:
        raw     : pad naar de compilatie-PDF (relatief aan repo-root)
        splits  : list van split-dicts met velden kb_id, output, wet, ...
        extract.params.kind : optioneel, ``"kb"`` (default) of ``"mb"`` —
            bepaalt welk type besluit-headers de splitter herkent.

    Returnt een mapping output-pad → body-tekst (zonder frontmatter,
    zonder heading-injectie). De orchestrator zorgt voor frontmatter,
    heading-injectie en wegschrijven naar staging.
    """
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"raw-pad ontbreekt voor {source_name}")
    raw_path = ROOT / raw
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw PDF niet gevonden: {raw_path}")

    extract_cfg = cfg.get("extract") or {}
    params = extract_cfg.get("params") or {}
    kind = str(params.get("kind", "kb")).lower()
    if kind not in ("kb", "mb"):
        raise ValueError(
            f"{source_name}: extract.params.kind moet 'kb' of 'mb' zijn, "
            f"kreeg {kind!r}"
        )

    splits = _build_splits(cfg)
    if not splits:
        raise ValueError(
            f"{source_name}: geen 'splits:' veld of leeg — "
            "compilatie-extractor verwacht minstens 1 SplitConfig"
        )

    # Belangrijk: eerst splitsen, dán cleanen. De FOD page-headers zijn de
    # boundary-markers — die moeten dus zichtbaar zijn voor split_btw_compilatie.
    # `_clean_body` schrapt ze achteraf per split.
    text = _pdftotext_layout(str(raw_path))
    raw_splits = split_btw_compilatie(text, splits, kind=kind)
    return {out: _clean_body(body) if body else "" for out, body in raw_splits.items()}


# Alias voor consistente naming met andere extractors.
extract = extract_compilatie
