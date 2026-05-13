"""
Transformer-laag voor de Certificaid ETL-pipeline (ADR-005 §4).

Elke transformer is een pure functie:
    (body: str, frontmatter: dict) -> tuple[str, dict]

TRANSFORMERS is de centrale registry: {"naam": callable}.
apply_chain() voert een geordende lijst transformers in volgorde uit.
"""
from __future__ import annotations

from tools.etl.transformers.base import TransformerFn
from tools.etl.transformers.cleanup_basics import cleanup_basics
from tools.etl.transformers.inject_headings_wettekst import inject_headings_wettekst
from tools.etl.transformers.inject_headings_narratief import inject_headings_narratief
from tools.etl.transformers.organize_headings import organize_headings
from tools.etl.transformers.emit_frontmatter import emit_frontmatter
from tools.etl.transformers.strip_fisconet_artefacts import strip_fisconet_artefacts
from tools.etl.transformers.fix_stuck_art_number import fix_stuck_art_number
from tools.etl.transformers.split_merged_headings import split_merged_headings
from tools.etl.transformers.strip_amendment_overview import strip_amendment_overview
from tools.etl.transformers.strip_compilatie_appendix import strip_compilatie_appendix
from tools.etl.transformers.unindent_pdftotext_margin import unindent_pdftotext_margin
from tools.etl.transformers.strip_pdf_page_noise import strip_pdf_page_noise
from tools.etl.transformers.merge_pdf_paragraph_breaks import merge_pdf_paragraph_breaks
from tools.etl.transformers.merge_broken_sentences import merge_broken_sentences
from tools.etl.transformers.fix_italic_spacing import fix_italic_spacing
from tools.etl.transformers.normalize_bullet_glyphs import normalize_bullet_glyphs
from tools.etl.transformers.fix_bold_italic_mixing import fix_bold_italic_mixing
from tools.etl.transformers.strip_itaa_norm_footers import strip_itaa_norm_footers
from tools.etl.transformers.promote_norm_section_labels import promote_norm_section_labels
from tools.etl.transformers.strip_running_page_headers import strip_running_page_headers

TRANSFORMERS: dict[str, TransformerFn] = {
    "cleanup_basics": cleanup_basics,
    "inject_headings_wettekst": inject_headings_wettekst,
    "inject_headings_narratief": inject_headings_narratief,
    "organize_headings": organize_headings,
    "emit_frontmatter": emit_frontmatter,
    "strip_fisconet_artefacts": strip_fisconet_artefacts,
    "fix_stuck_art_number": fix_stuck_art_number,
    "split_merged_headings": split_merged_headings,
    "strip_amendment_overview": strip_amendment_overview,
    "strip_compilatie_appendix": strip_compilatie_appendix,
    "unindent_pdftotext_margin": unindent_pdftotext_margin,
    "strip_pdf_page_noise": strip_pdf_page_noise,
    "merge_pdf_paragraph_breaks": merge_pdf_paragraph_breaks,
    "merge_broken_sentences": merge_broken_sentences,
    "fix_italic_spacing": fix_italic_spacing,
    "normalize_bullet_glyphs": normalize_bullet_glyphs,
    "fix_bold_italic_mixing": fix_bold_italic_mixing,
    "strip_itaa_norm_footers": strip_itaa_norm_footers,
    "promote_norm_section_labels": promote_norm_section_labels,
    "strip_running_page_headers": strip_running_page_headers,
}


def apply_chain(
    body: str,
    frontmatter: dict,
    chain: list[str],
) -> tuple[str, dict]:
    """Voer een chain van transformers in volgorde uit.

    Args:
        body: markdown-body (zonder frontmatter-blok).
        frontmatter: huidige frontmatter als plain dict (wordt doorgegeven
            en kan door elke transformer worden gewijzigd).
        chain: geordende lijst van transformer-namen (sleutels in TRANSFORMERS).

    Returns:
        (body, frontmatter) na alle transformers toegepast.

    Raises:
        ValueError: als een chain-naam niet in TRANSFORMERS staat.
    """
    for name in chain:
        fn = TRANSFORMERS.get(name)
        if fn is None:
            raise ValueError(
                f"Onbekende transformer: {name!r}. "
                f"Beschikbaar: {sorted(TRANSFORMERS)}"
            )
        body, frontmatter = fn(body, frontmatter)
    return body, frontmatter
