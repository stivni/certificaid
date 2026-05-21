"""Merge per-vraag artefacten naar één `<examen>.json` schema 4.0 (ADR-024 §6).

Deterministisch, idempotent, fail-loud. Geen LLM, geen netwerk.

Input:
    data/programma/examen_vragen/_poc_subset.json             (selectie)
    data/programma/examen_vragen/_interpretaties/<examen>/<vraag>.json
    data/programma/examen_vragen/_antwoorden/<examen>/<vraag>.json
    data/programma/examen_vragen/_segmenten/<examen>/<vraag>/meta.json

Output:
    data/programma/examen_vragen/_merged/<examen>.json

CLI:
    python3 -m tools.examen.merge_examen_artefacten            # alle examens met
                                                                # POC-artefacten
    python3 -m tools.examen.merge_examen_artefacten --examen 2024-1
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXAMEN_VRAGEN_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen"
SUBSET_PATH = EXAMEN_VRAGEN_DIR / "_poc_subset.json"
INTERPRETATIES_DIR = EXAMEN_VRAGEN_DIR / "_interpretaties"
ANTWOORDEN_DIR = EXAMEN_VRAGEN_DIR / "_antwoorden"
SEGMENTEN_DIR = EXAMEN_VRAGEN_DIR / "_segmenten"
MERGED_DIR = EXAMEN_VRAGEN_DIR / "_merged"

SCHEMA_VERSIE = "4.0"
TOOL_NAAM = "merge-examen-artefacten"


class MergerError(RuntimeError):
    """Wordt opgeworpen bij ontbrekende artefacten of inconsistente input."""


def _laad_subset() -> list[dict[str, Any]]:
    if not SUBSET_PATH.is_file():
        raise MergerError(f"POC-subset ontbreekt: {SUBSET_PATH}")
    return json.loads(SUBSET_PATH.read_text(encoding="utf-8"))["selectie"]


def _discover_alle_interpretaties() -> list[dict[str, Any]]:
    """Bouw entry-lijst uit alle interpretatie-bestanden onder `_interpretaties/`.

    Geeft `[{examen_id, vraag_id}, ...]` terug — alle vragen die effectief
    een interpretatie hebben. Schema-compatibel met `_laad_subset()`-output,
    extra subset-velden (karakter, rationale) ontbreken hier maar zijn
    optioneel.
    """
    if not INTERPRETATIES_DIR.exists():
        raise MergerError(
            f"Interpretaties-map ontbreekt: {INTERPRETATIES_DIR}"
        )
    entries: list[dict[str, Any]] = []
    for examen_dir in sorted(INTERPRETATIES_DIR.iterdir()):
        if not examen_dir.is_dir():
            continue
        examen_id = examen_dir.name
        for pad in sorted(examen_dir.glob("*.json")):
            entries.append({"examen_id": examen_id, "vraag_id": pad.stem})
    if not entries:
        raise MergerError(
            f"Geen interpretaties gevonden onder {INTERPRETATIES_DIR}"
        )
    return entries


def _groepeer_per_examen(
    selectie: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    per_examen: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in selectie:
        per_examen[entry["examen_id"]].append(entry)
    # deterministische volgorde per vraag-id
    for examen_id, entries in per_examen.items():
        entries.sort(key=lambda e: e["vraag_id"])
    return dict(per_examen)


def _lees_json(pad: Path) -> dict[str, Any]:
    return json.loads(pad.read_text(encoding="utf-8"))


def _bouw_examen_payload(
    examen_id: str,
    entries: list[dict[str, Any]],
    antwoord_optioneel: bool = False,
) -> dict[str, Any]:
    """Bouwt de payload (zonder `merge_datum`) voor één examen.

    Faalt fail-loud op de eerste ontbrekende interpretatie / meta. Bij
    `antwoord_optioneel=True` wordt een ontbrekend antwoord-bestand niet
    als fout behandeld — `antwoord` wordt dan `None` in de output.
    """
    vragen: list[dict[str, Any]] = []
    bron_pdf: str | None = None

    for entry in entries:
        vraag_id = entry["vraag_id"]

        interp_pad = INTERPRETATIES_DIR / examen_id / f"{vraag_id}.json"
        antwoord_pad = ANTWOORDEN_DIR / examen_id / f"{vraag_id}.json"
        meta_pad = SEGMENTEN_DIR / examen_id / vraag_id / "meta.json"

        if not interp_pad.is_file():
            raise MergerError(
                f"interpretatie ontbreekt voor {vraag_id}: {interp_pad}"
            )
        if not meta_pad.is_file():
            raise MergerError(
                f"segment-meta ontbreekt voor {vraag_id}: {meta_pad}"
            )

        antwoord: dict[str, Any] | None
        if antwoord_pad.is_file():
            antwoord = _lees_json(antwoord_pad)
        elif antwoord_optioneel:
            antwoord = None
        else:
            raise MergerError(
                f"antwoord ontbreekt voor {vraag_id}: {antwoord_pad}"
            )

        interpretatie = _lees_json(interp_pad)
        segment_meta = _lees_json(meta_pad)

        # sanity-check: vraag_id moet matchen in elk aanwezig artefact
        for naam, data in [
            ("interpretatie", interpretatie),
            ("antwoord", antwoord),
            ("segment_meta", segment_meta),
        ]:
            if data is None:
                continue
            if data.get("vraag_id") != vraag_id:
                raise MergerError(
                    f"vraag_id-mismatch in {naam} voor {vraag_id}: "
                    f"file zegt {data.get('vraag_id')!r}"
                )

        if bron_pdf is None:
            bron_pdf = segment_meta.get("pdf_bestand")
        elif segment_meta.get("pdf_bestand") != bron_pdf:
            raise MergerError(
                f"pdf_bestand-mismatch binnen examen {examen_id}: "
                f"{bron_pdf!r} vs {segment_meta.get('pdf_bestand')!r}"
            )

        vragen.append(
            {
                "vraag_id": vraag_id,
                "interpretatie": interpretatie,
                "antwoord": antwoord,
                "segment_meta": segment_meta,
            }
        )

    if bron_pdf is None:
        raise MergerError(f"kon bron_pdf niet bepalen voor examen {examen_id}")

    return {
        "schema_versie": SCHEMA_VERSIE,
        "examen_id": examen_id,
        "tool": TOOL_NAAM,
        "bron_pdf": bron_pdf,
        "vragen": vragen,
    }


def _serialiseer(payload: dict[str, Any]) -> str:
    """Deterministische JSON-serializatie. `merge_datum` blijft aanwezig
    op de positie waar de caller hem gezet heeft."""
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _gelijk_modulo_merge_datum(
    nieuwe_payload: dict[str, Any], bestaande_tekst: str
) -> bool:
    """Vergelijk content modulo het `merge_datum`-veld.

    Zo blijft de file byte-identiek wanneer alleen het timestamp zou wijzigen.
    """
    try:
        bestaand = json.loads(bestaande_tekst)
    except json.JSONDecodeError:
        return False
    a = {k: v for k, v in nieuwe_payload.items() if k != "merge_datum"}
    b = {k: v for k, v in bestaand.items() if k != "merge_datum"}
    return a == b


def _schrijf_atomair(pad: Path, tekst: str) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    tmp = pad.with_suffix(pad.suffix + ".tmp")
    tmp.write_text(tekst, encoding="utf-8")
    tmp.replace(pad)


def merge_examen(
    examen_id: str,
    entries: list[dict[str, Any]],
    antwoord_optioneel: bool = False,
) -> Path:
    """Merge één examen. Geeft het pad naar de geschreven (of ongewijzigde) file."""
    payload = _bouw_examen_payload(examen_id, entries, antwoord_optioneel)
    out_pad = MERGED_DIR / f"{examen_id}.json"

    if out_pad.is_file():
        bestaand = out_pad.read_text(encoding="utf-8")
        if _gelijk_modulo_merge_datum(payload, bestaand):
            # niets te doen — preserveer bestaand timestamp + byte-state
            return out_pad
        # content gewijzigd → nieuw timestamp
        payload["merge_datum"] = datetime.now(tz=timezone.utc).isoformat(
            timespec="seconds"
        )
    else:
        payload["merge_datum"] = datetime.now(tz=timezone.utc).isoformat(
            timespec="seconds"
        )

    _schrijf_atomair(out_pad, _serialiseer(payload))
    return out_pad


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--examen",
        help="Beperk tot één examen-id (bv. 2024-1).",
    )
    parser.add_argument(
        "--alle",
        action="store_true",
        help="Gebruik alle interpretaties onder _interpretaties/ (auto-discovery) "
        "i.p.v. _poc_subset.json. Default: POC-subset.",
    )
    args = parser.parse_args(argv)

    try:
        if args.alle:
            selectie = _discover_alle_interpretaties()
        else:
            selectie = _laad_subset()
        per_examen = _groepeer_per_examen(selectie)

        if args.examen:
            if args.examen not in per_examen:
                bron = "interpretaties-folder" if args.alle else "POC-subset"
                raise MergerError(
                    f"examen {args.examen!r} niet in {bron}; "
                    f"beschikbaar: {sorted(per_examen)}"
                )
            doel = {args.examen: per_examen[args.examen]}
        else:
            doel = per_examen

        # In --alle-modus zijn antwoorden optioneel (uitrolfase: alleen
        # interpretaties zijn voltooid, antwoorden volgen later na RAG).
        antwoord_optioneel = bool(args.alle)

        for examen_id in sorted(doel):
            pad = merge_examen(examen_id, doel[examen_id], antwoord_optioneel)
            print(f"[merge] {examen_id} -> {pad.relative_to(REPO_ROOT)}")
    except MergerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
