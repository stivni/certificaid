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
from tools.etl.transformers.strip_kb_bijwerkingen import strip_kb_bijwerkingen
from tools.etl.transformers.strip_empty_trailing_headings import strip_empty_trailing_headings
from tools.etl.transformers.merge_article_reference_wraps import merge_article_reference_wraps
from tools.etl.transformers.strip_mb_compilatie_cover import strip_mb_compilatie_cover
from tools.etl.transformers.fix_pdftotext_glue_bugs import fix_pdftotext_glue_bugs
from tools.etl.transformers.promote_wettekst_section_labels import promote_wettekst_section_labels
from tools.etl.transformers.normalize_artikel_to_art import normalize_artikel_to_art
from tools.etl.transformers.strip_leading_toc_heading_block import strip_leading_toc_heading_block
from tools.etl.transformers.fix_pdf_slash_loss_in_article_headings import fix_pdf_slash_loss_in_article_headings
from tools.etl.transformers.strip_french_bilingue_bleed import strip_french_bilingue_bleed
from tools.etl.transformers.strip_norm_column_bleed import strip_norm_column_bleed
from tools.etl.transformers.strip_norm_toc_residue import strip_norm_toc_residue
from tools.etl.transformers.strip_opgeheven_kb_appendix import strip_opgeheven_kb_appendix
from tools.etl.transformers.merge_wrapped_headings import merge_wrapped_headings
from tools.etl.transformers.strip_toc_headings_with_art_range import strip_toc_headings_with_art_range
from tools.etl.transformers.strip_inline_footnote_block import strip_inline_footnote_block
from tools.etl.transformers.strip_concord_table_headings import strip_concord_table_headings
from tools.etl.transformers.strip_duplicate_toc_headings import strip_duplicate_toc_headings
from tools.etl.transformers.promote_roman_rubrieken import promote_roman_rubrieken
from tools.etl.transformers.reorder_heading_cluster import reorder_heading_cluster
from tools.etl.transformers.split_long_art_heading import split_long_art_heading
from tools.etl.transformers.strip_isa_page_footers import strip_isa_page_footers
from tools.etl.transformers.inject_headings_isa import inject_headings_isa
# Pre-existing breakage: commit 0c77206e (2026-05-19) voegde deze 4 imports toe maar de
# bronfiles zijn nooit meegecommit. Tijdelijk uitgecommentarieerd om pytest-collectie te
# laten slagen. ETL-laag herstel is een separate werkstroom.
# from tools.etl.transformers.merge_eu_reflow_word_splits import merge_eu_reflow_word_splits
# from tools.etl.transformers.promote_eu_structural_labels import promote_eu_structural_labels
# from tools.etl.transformers.strip_letter_spaced_page_headers import strip_letter_spaced_page_headers
# from tools.etl.transformers.strip_trailing_french_section import strip_trailing_french_section

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
    "strip_kb_bijwerkingen": strip_kb_bijwerkingen,
    "strip_empty_trailing_headings": strip_empty_trailing_headings,
    "merge_article_reference_wraps": merge_article_reference_wraps,
    "strip_mb_compilatie_cover": strip_mb_compilatie_cover,
    "fix_pdftotext_glue_bugs": fix_pdftotext_glue_bugs,
    "promote_wettekst_section_labels": promote_wettekst_section_labels,
    "normalize_artikel_to_art": normalize_artikel_to_art,
    "strip_leading_toc_heading_block": strip_leading_toc_heading_block,
    "fix_pdf_slash_loss_in_article_headings": fix_pdf_slash_loss_in_article_headings,
    "strip_french_bilingue_bleed": strip_french_bilingue_bleed,
    "strip_norm_column_bleed": strip_norm_column_bleed,
    "strip_norm_toc_residue": strip_norm_toc_residue,
    "strip_opgeheven_kb_appendix": strip_opgeheven_kb_appendix,
    "merge_wrapped_headings": merge_wrapped_headings,
    "strip_toc_headings_with_art_range": strip_toc_headings_with_art_range,
    "strip_inline_footnote_block": strip_inline_footnote_block,
    "strip_concord_table_headings": strip_concord_table_headings,
    "strip_duplicate_toc_headings": strip_duplicate_toc_headings,
    "promote_roman_rubrieken": promote_roman_rubrieken,
    "reorder_heading_cluster": reorder_heading_cluster,
    "split_long_art_heading": split_long_art_heading,
    "strip_isa_page_footers": strip_isa_page_footers,
    "inject_headings_isa": inject_headings_isa,
    # Zie commentaar bovenaan; 4 entries uitgecommentarieerd tot bronfiles landen.
    # "merge_eu_reflow_word_splits": merge_eu_reflow_word_splits,
    # "promote_eu_structural_labels": promote_eu_structural_labels,
    # "strip_letter_spaced_page_headers": strip_letter_spaced_page_headers,
    # "strip_trailing_french_section": strip_trailing_french_section,
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
