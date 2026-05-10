"""
Anchor-builder — bouwt `data/anchors.json` uit `data/programma.json`.

Per `anchor_role: "anchor"`-node een record met:
  - `embedding_text`: gestructureerde concatenatie van tekst + verbose + synoniemen
    + ingevouwen `context`-descendants + (indien parent een `intro_template` heeft)
    template-prefix.
  - `references[]`: alle `anchor_role: "reference"`-descendants met hun
    `source_files` en `scope`. Worden in de concept-extractie bundle van dit
    anker verplicht meegenomen, ongeacht similarity.
  - `vector`: null (wordt ingevuld door `embed_anchors.py`).

Eén globale anchors-set, geen per-PO files.

Gebruik:
  python3 -m tools.extractie.build_anchors
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROGRAMMA = ROOT / "data" / "programma.json"
ANCHORS = ROOT / "data" / "anchors.json"


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def _children_keys(node: dict) -> list[str]:
    """Iterable van keys waarin children kunnen zitten."""
    return ["subitems", "subtaken", "doelstellingen", "subdoelen"]


def _iter_children(node: dict):
    for key in _children_keys(node):
        for c in node.get(key, []) or []:
            yield c


def _collect_context(node: dict, accumulator: list[str]) -> None:
    """Vouw alle `context`-descendants van een anchor in: voeg hun tekst + verbose
    toe aan accumulator (synoniemen niet — die geven veel ruis als alle children
    samen worden geconcat)."""
    for c in _iter_children(node):
        role = c.get("anchor_role")
        if role == "context":
            tekst = c.get("tekst", "").strip()
            if tekst:
                accumulator.append(tekst)
            verbose = c.get("verbose", "")
            if verbose:
                accumulator.append(verbose)
            # Recurseer: de context-children van deze context worden ook gevouwen
            _collect_context(c, accumulator)
        # anchor- en reference-children stoppen het vouw-pad voor hun subtree
        # (die hebben hun eigen anker / worden via references[] geattacheerd).


def _collect_references(node: dict, accumulator: list[dict]) -> None:
    """Verzamel alle `reference`-descendants. Stop NIET bij context-nodes
    (een reference kan onder een context-knoop hangen)."""
    for c in _iter_children(node):
        role = c.get("anchor_role")
        if role == "reference":
            accumulator.append({
                "code": c["code"],
                "tekst": c.get("tekst", ""),
                "source_files": c.get("source_files", []),
                "scope": c.get("scope", "geheel"),
            })
            # Reference-leaves hebben zelden children, maar voor de zekerheid:
            _collect_references(c, accumulator)
        elif role == "context":
            _collect_references(c, accumulator)
        # anchor-children stoppen de walk (die zijn een eigen anker met eigen refs).


def _build_embedding_text(
    node: dict,
    *,
    parent_template: list[str] | None,
) -> str:
    """Bouw de geconcateneerde embedding-tekst voor één anchor."""
    parts: list[str] = []

    if parent_template:
        parts.append("Aspecten: " + " / ".join(parent_template))

    tekst = node.get("tekst", "").strip()
    if tekst:
        parts.append(tekst)

    verbose = node.get("verbose", "").strip() if node.get("verbose") else ""
    if verbose:
        parts.append(verbose)

    syns = node.get("synoniemen") or []
    if syns:
        parts.append("Synoniemen: " + ", ".join(syns))

    # Eigen intro_template (voor anchors die zelf templates dragen) als sub-aspecten
    own_template = node.get("intro_template") or []
    if own_template:
        parts.append("Sub-aspecten: " + " / ".join(own_template))

    # Vouw context-descendants in
    ctx_acc: list[str] = []
    _collect_context(node, ctx_acc)
    if ctx_acc:
        parts.append("Context: " + " · ".join(ctx_acc))

    return "\n\n".join(parts).strip()


def _walk_for_anchors(
    node: dict,
    *,
    po: str,
    po_titel: str,
    parent_template: list[str] | None,
    anchors_out: list[dict],
) -> None:
    """Recursie die anchor-nodes uitspuwt en bij anchor-nodes stopt met de subtree
    (subtree is dan ofwel context-vouw of een eigen anchor opnieuw)."""
    role = node.get("anchor_role")

    if role == "anchor":
        emb_text = _build_embedding_text(node, parent_template=parent_template)
        refs: list[dict] = []
        _collect_references(node, refs)
        anchors_out.append({
            "anchor_id": node["code"],
            "po": po,
            "po_titel": po_titel,
            "tekst": node.get("tekst", ""),
            "verbose": node.get("verbose", ""),
            "synoniemen": node.get("synoniemen", []),
            "embedding_text": emb_text,
            "embedding_text_sha": _sha(emb_text),
            "vector": None,
            "references": refs,
        })

        # Voor diepere anchor-children van deze anchor: recurseer met zijn
        # eigen template als parent_template (indien gezet).
        own_template = node.get("intro_template")
        for c in _iter_children(node):
            if c.get("anchor_role") == "anchor":
                _walk_for_anchors(c, po=po, po_titel=po_titel,
                                  parent_template=own_template, anchors_out=anchors_out)
        return

    # context- en reference-nodes worden niet als anker uitgespuwd.
    # Maar: ze kunnen dieper liggende anchor-children bevatten — recurseer.
    own_template = node.get("intro_template")
    next_template = own_template if own_template else parent_template
    for c in _iter_children(node):
        _walk_for_anchors(c, po=po, po_titel=po_titel,
                          parent_template=next_template, anchors_out=anchors_out)


def build() -> dict:
    data = json.loads(PROGRAMMA.read_text())
    anchors: list[dict] = []

    for po in data["programmaonderdelen"]:
        po_code = po["code"]
        po_titel = po.get("titel", "")
        for t in po.get("taken", []):
            _walk_for_anchors(t, po=po_code, po_titel=po_titel,
                              parent_template=None, anchors_out=anchors)
        for ke in po.get("kenniselementen", []):
            _walk_for_anchors(ke, po=po_code, po_titel=po_titel,
                              parent_template=None, anchors_out=anchors)

    return {
        "version": "1",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "data/programma.json",
        "n_anchors": len(anchors),
        "anchors": anchors,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="alleen tellen, niet schrijven")
    args = parser.parse_args()

    payload = build()
    n = payload["n_anchors"]

    # Stats
    n_with_refs = sum(1 for a in payload["anchors"] if a["references"])
    total_refs = sum(len(a["references"]) for a in payload["anchors"])
    avg_emb_len = (
        sum(len(a["embedding_text"]) for a in payload["anchors"]) // max(n, 1)
    )
    by_po: dict[str, int] = {}
    for a in payload["anchors"]:
        by_po[a["po"]] = by_po.get(a["po"], 0) + 1

    print(f"  {n} anchors gebouwd")
    print(f"  {n_with_refs} anchors hebben references ({total_refs} totaal)")
    print(f"  gemiddelde embedding_text-lengte: {avg_emb_len} chars")
    print(f"  per PO: {dict(sorted(by_po.items()))}")

    if not args.dry_run:
        ANCHORS.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        print(f"  → {ANCHORS.relative_to(ROOT)}")
    else:
        print("  (dry-run — geen bestand geschreven)")


if __name__ == "__main__":
    main()
