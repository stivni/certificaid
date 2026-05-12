"""
Type-definities en helpers gedeeld door alle transformers (ADR-005 §4).

Een transformer is een pure functie:
    (body: str, frontmatter: dict) -> tuple[str, dict]

`body` is de markdown-tekst (zonder frontmatter-blok).
`frontmatter` is een plain Python-dict met de huidige frontmatter-state.

Transformers mogen zowel body als frontmatter wijzigen; ze zijn idempotent
waar dat mogelijk is.
"""
from __future__ import annotations

from typing import Callable

# Type-alias voor een transformer-functie.
TransformerFn = Callable[[str, dict], tuple[str, dict]]
