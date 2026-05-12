"""
Transformer: emit_frontmatter (ADR-005 §4).

Verantwoordelijk voor het serialiseren van de frontmatter naar YAML en het
combineren ervan met de body. Dit is altijd de LAATSTE transformer in de chain.

Leest de huidige frontmatter-dict en serialiseert die als YAML-frontmatter-blok
dat voor de body geplaatst wordt.

Intern gebruik van frontmatter-sleutels die door eerder transformers zijn
gezet:
  - `_chunk_level`: int — van inject_headings_wettekst (of default 2)
  - `_chunk_type`:  str — van inject_headings_wettekst (of default "##")
  - `_sub_strategy`: str|None — van inject_headings_wettekst
  - `_chunk_info`:  dict — logging-info (wordt niet naar output geschreven)

Alle `_`-prefixed sleutels zijn interne orchestrator-velden en worden
verwijderd vóór serialisatie.

Na de transformer bevat de body de volledige tekst: YAML-frontmatter + body.
De frontmatter-dict is daarna leeg (alles is geserialiseerd in de body).

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.lib.headings import update_frontmatter_chunk  # noqa: E402


def _format_tags(tags) -> str:
    """Render tags-lijst als geldige YAML flow-list met dubbele quotes."""
    if isinstance(tags, list):
        return "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    return str(tags)


def _safe(value) -> str:
    """Escape dubbele quotes binnen YAML-strings."""
    if value is None:
        return ""
    return str(value).replace('"', '\\"')


def _build_yaml_only_block(frontmatter: dict) -> str:
    """Bouw alleen het YAML-frontmatter-blok (eindigt op '\\n---\\n').

    Bevat geen intro-content (# titel, *Bijgewerkt...*). Wordt gebruikt door
    emit_frontmatter zodat update_frontmatter_chunk het chunk-blok kan invoegen
    vóórdat de intro-content wordt toegevoegd.

    Returns het frontmatter-blok inclusief `---` delimiters, eindigend op `\\n---\\n`.
    """
    tags = frontmatter.get("tags", [])
    tags_str = _format_tags(tags)
    itaa = _safe(frontmatter.get("itaa_sectie", ""))
    wet_full = frontmatter.get("wet", "")
    bijgewerkt = _safe(frontmatter.get("bijgewerkt", ""))
    bron_rol = frontmatter.get("bron_rol")
    bron_label = frontmatter.get("bron", "onbekend")

    fm_lines = [
        "---",
        f"tags: {tags_str}",
        f'itaa-lex-sectie: "{itaa}"',
        f'wet: "{_safe(wet_full)}"',
    ]
    if bron_rol:
        fm_lines.append(f'bron_rol: "{_safe(bron_rol)}"')
    fm_lines.extend([
        'status: "beschikbaar"',
        f'bijgewerkt: "{bijgewerkt}"',
        f'bron: "{bron_label}"',
        "---",
        "",
    ])
    return "\n".join(fm_lines)


def _build_intro_block(frontmatter: dict) -> str:
    """Bouw de intro-sectie (# titel + *Bijgewerkt...*) die na de frontmatter komt."""
    wet_full = frontmatter.get("wet", "")
    bijgewerkt = _safe(frontmatter.get("bijgewerkt", ""))
    titel = frontmatter.get("titel") or wet_full

    intro_lines = [
        f"# {titel}",
        "",
        f"*Bijgewerkt tot en met {bijgewerkt} — gecoördineerde versie.*",
        "",
        "",
    ]
    return "\n".join(intro_lines)


def emit_frontmatter(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Serialiseer frontmatter naar YAML en voeg chunk-blok toe.

    Verwijdert alle interne `_`-prefixed sleutels uit frontmatter vóór
    serialisatie. Het chunk-blok wordt ingevoegd via update_frontmatter_chunk
    op basis van `_chunk_level`, `_chunk_type` en `_sub_strategy`.

    Na afloop bevat `body` de volledige tekst (frontmatter-YAML + body-markdown).
    De geretourneerde frontmatter-dict is leeg (alles geserialiseerd).
    """
    # Haal interne velden op en verwijder ze
    chunk_level = frontmatter.pop("_chunk_level", 2)
    chunk_type = frontmatter.pop("_chunk_type", "Art.")
    sub_strategy = frontmatter.pop("_sub_strategy", None)
    frontmatter.pop("_chunk_info", None)  # logging-info, niet serialiseren

    # Bouw het pure YAML-blok (eindigt op \n---\n) zodat update_frontmatter_chunk
    # het chunk-blok correct kan invoegen vóór de intro-content.
    yaml_block = _build_yaml_only_block(frontmatter)

    # Voeg chunk-blok toe via de bestaande helper
    yaml_block_with_chunk = update_frontmatter_chunk(
        yaml_block, chunk_level, chunk_type=chunk_type, sub_strategy=sub_strategy,
    )

    # Bouw intro-content (# titel + *Bijgewerkt...*)
    intro = _build_intro_block(frontmatter)

    # Combineer frontmatter + intro + body.
    # yaml_block_with_chunk eindigt op '\n---\n'; de originele build_initial_frontmatter
    # plaatst een extra lege regel tussen frontmatter-sluiter en # H1, dus we voegen
    # '\n' toe zodat het resultaat '\n---\n\n# titel' wordt (identiek aan origineel).
    full_text = yaml_block_with_chunk + "\n" + intro + body.lstrip("\n")

    return full_text, {}
