"""Extractor voor `pdftotext_compilatie_btw` — 1-op-N split-extractie.

Een compilatie-PDF (bv. WBTW-KB-compilatie.pdf) bevat meerdere KBs. Deze
extractor levert per gevraagde split de body-tekst, geïndexeerd op het
gewenste output-pad.

Pipeline:
  1. PDF → tekst via pdftotext (zelfde aanpak als pdftotext_ejustice).
  2. Body-cleanup: schrap FOD page-headers, page-numbers en bijwerkings-
     marginalia (analoog aan tools/etl/split-kb-compilatie.py).
  3. Splits-detectie via tools/lib/compilatie_split.split_btw_compilatie
     met de SplitConfig-list opgebouwd uit cfg["splits"].

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

ROOT = Path(__file__).resolve().parents[3]


# Cleanup-patronen voor body — uit split-kb-compilatie.py overgenomen.
_BODY_NOISE = [
    re.compile(r'^FOD Financi.n.+?(?:Btw|BTW)\s+KB.+', re.I),
    re.compile(r'^Btw KB nr\.\s+\d+\s+-\s+bijw.+', re.I),
    re.compile(r'^\s*-\s*\d+\s*-\s*$'),
    re.compile(r'^KB\d+\w*\s+pg\..+', re.I),
    re.compile(r'^-\s*KB\d+\w*\s+pg\..+', re.I),
    re.compile(r'^-\s*Recente wijzigingen\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^-\s*Bijlage\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^Recente wijzigingen\s+www\.fisconetplus.+', re.I),
    re.compile(r'^Lijst van de bijwerkingen\b.+', re.I),
    re.compile(r'^www\.fisconetplus\.be\b'),
]


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
    """Schrap page-headers/footers en collapseer dubbele blanke regels."""
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
    return "\n".join(out_lines).strip() + "\n"


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
    raw_splits = split_btw_compilatie(text, splits)
    return {out: _clean_body(body) if body else "" for out, body in raw_splits.items()}


# Alias voor consistente naming met andere extractors.
extract = extract_compilatie
