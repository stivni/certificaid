"""OCR-normalisatie-gate voor voorbeeldexamenvragen (ADR-020 §6).

Scant `data/programma/examen_vragen/*.json` op typische OCR-fouten in
`vraagtekst`-velden (kapotte tabellen, verdachte ellipsen, weggevallen
letters, weggevallen vraagtekens). Detecteert; corrigeert niet.

Output: `data/extractie/vraagtekst_qa.json` met flag-rapport voor
handmatige review.

CLI:
    python3 -m tools.examen.normalize_vraagteksten
    python3 -m tools.examen.normalize_vraagteksten --examen 2014-1
    python3 -m tools.examen.normalize_vraagteksten --summary
    python3 -m tools.examen.normalize_vraagteksten --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXAMEN_VRAGEN_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen"
QA_RAPPORT_PAD = REPO_ROOT / "data" / "extractie" / "vraagtekst_qa.json"

# Bekende afkortingen die `loose_caps` niet mag flaggen
HOOFDLETTER_WHITELIST = {
    "IFRS",
    "BEGAAP",
    "BTW",
    "WVV",
    "KB",
    "CBN",
    "ITAA",
    "BIBF",
    "NV",
    "BV",
    "IC",
    "EV",
    "RR",
    "BVBA",
    "BVBAS",
    "VZW",
    "EBIT",
    "EBITDA",
    "EUR",
    "MC",
    "BCE",
    "KBO",
    "IPCF",
    "PCMN",
    "MAR",
    "ISA",
    "ISAE",
    "ISRS",
    "ADR",
    "PDF",
    "OCR",
    "JF",
}

# Regex: woord met intern een kleine-letter→hoofdletter overgang.
# Pakt zowel `boekHouder` (begin lowercase) als `MaatschapKring`
# (begin uppercase). De `[A-Za-z]*` aan het begin laat het woord starten
# met een hoofdletter; de kern eist een interne `[a-z][A-Z]`-overgang.
LOOSE_CAPS_PATTERN = re.compile(r"\b([A-Za-z]*[a-z][A-Z][a-z]+)\b")

# Regex: percent-tekens losstaand
PERCENT_PATTERN = re.compile(r"\b\d+\s*%")


@dataclass
class Flag:
    """Eén OCR-vermoeden op één vraag of subvraag."""

    examen_file: str
    vraag_id: str
    subvraag_label: str | None
    detector: str
    snippet: str
    ernst: str


def _snippet_rond_match(tekst: str, start: int, end: int, marge: int = 40) -> str:
    """Geef een korte context-snippet rond een match-positie."""
    begin = max(0, start - marge)
    eind = min(len(tekst), end + marge)
    snippet = tekst[begin:eind].strip()
    if begin > 0:
        snippet = "..." + snippet
    if eind < len(tekst):
        snippet = snippet + "..."
    return snippet


def detecteer_trailing_ellipses(tekst: str) -> list[str]:
    """Vind ellipsen op verdachte plekken.

    Legitiem: "Vraag N … / X punten" aan begin van vraagtekst — ITAA-format.
    Verdacht: ellipsen middenin een zin, na een cijfer, of binnen een tabel-rij.
    """
    vermoedens: list[str] = []
    # Iterate over elke ellipsis
    for match in re.finditer(r"…", tekst):
        pos = match.start()
        # Skip de standaard "Vraag N … / X punten"-opener (eerste 80 tekens)
        if pos < 80:
            voor = tekst[:pos]
            # Match patroon "Vraag <nr> " of "Vraag <letter>) "
            if re.search(r"Vraag\s+\S+\s*$", voor):
                continue

        # Verdacht: ellipsis voorafgegaan door cijfer of binnen een woord
        voor_2 = tekst[max(0, pos - 2):pos]
        na_2 = tekst[pos + 1:pos + 3]

        # "Antwoord …/ N punten" middenin = verdacht (open_antwoord_prompt
        # pakt dit ook, maar trailing_ellipses geeft hier signaal)
        if "Antwoord" in tekst[max(0, pos - 15):pos]:
            vermoedens.append(_snippet_rond_match(tekst, pos, pos + 1))
            continue

        # Ellipsis tussen cijfers/percents — verdacht
        if re.search(r"\d\s*$", voor_2) or re.search(r"^\s*\d", na_2):
            vermoedens.append(_snippet_rond_match(tekst, pos, pos + 1))
            continue

        # Ellipsis middenin een woord
        if re.search(r"[a-zA-Z]\s*$", voor_2) and re.search(r"^\s*[a-zA-Z]", na_2):
            vermoedens.append(_snippet_rond_match(tekst, pos, pos + 1))
    return vermoedens


def detecteer_broken_table(tekst: str) -> list[str]:
    """Vind tabel-fragmenten die als platte tekst-stroom uitgevallen zijn.

    Heuristiek: ≥3 percent-tekens op één regel zonder kolom-separator
    (geen `|`, geen newlines tussen waardes).
    """
    vermoedens: list[str] = []
    for regel in tekst.split("\n"):
        if "|" in regel:
            continue
        percents = PERCENT_PATTERN.findall(regel)
        if len(percents) >= 3:
            vermoedens.append(regel.strip()[:200])
    return vermoedens


def detecteer_loose_caps(tekst: str) -> list[str]:
    """Vind hoofdletter midden in een woord (mogelijk weggevallen spatie)."""
    vermoedens: list[str] = []
    for match in LOOSE_CAPS_PATTERN.finditer(tekst):
        woord = match.group(1)
        # Whitelist: bekende afkortingen vergeleken case-insensitive op
        # uppercase-versie
        if woord.upper() in HOOFDLETTER_WHITELIST:
            continue
        vermoedens.append(woord)
    return vermoedens


def detecteer_open_antwoord_prompt(tekst: str) -> list[str]:
    """Vind `Antwoord` middenin tekst zonder voorafgaand vraagteken.

    Wijst op weggevallen vraagteken of weggevallen optie-tekst.
    Een `Antwoord` aan het eind van de vraagtekst is OK.
    """
    vermoedens: list[str] = []
    for match in re.finditer(r"\bAntwoord\b", tekst):
        pos = match.start()
        # Skip als deze Antwoord-marker op het eind staat (laatste 30 tekens)
        if pos >= len(tekst) - len("Antwoord") - 5:
            continue
        # Kijk terug: tot waar het laatste `?` zit, of begin
        voor = tekst[max(0, pos - 300):pos]
        # Vind laatste niet-whitespace teken vóór Antwoord
        voor_strip = voor.rstrip()
        if not voor_strip:
            continue
        laatste_teken = voor_strip[-1]
        # OK: vraagteken, dubbelpunt, of nieuwe paragraph
        if laatste_teken in {"?", ":"}:
            continue
        # Niet-OK: cijfer, letter, punt, komma — wijst op weggevallen `?`
        vermoedens.append(_snippet_rond_match(tekst, pos, pos + len("Antwoord")))
    return vermoedens


def detecteer_flags_voor_vraagtekst(
    tekst: str,
    examen_file: str,
    vraag_id: str,
    subvraag_label: str | None,
) -> list[Flag]:
    """Run alle vier detectors op één vraagtekst en geef flags terug."""
    flags: list[Flag] = []
    if not tekst:
        return flags

    for snippet in detecteer_broken_table(tekst):
        flags.append(
            Flag(
                examen_file=examen_file,
                vraag_id=vraag_id,
                subvraag_label=subvraag_label,
                detector="broken_table",
                snippet=snippet,
                ernst="hoog",
            )
        )
    for snippet in detecteer_open_antwoord_prompt(tekst):
        flags.append(
            Flag(
                examen_file=examen_file,
                vraag_id=vraag_id,
                subvraag_label=subvraag_label,
                detector="open_antwoord_prompt",
                snippet=snippet,
                ernst="hoog",
            )
        )
    for snippet in detecteer_trailing_ellipses(tekst):
        flags.append(
            Flag(
                examen_file=examen_file,
                vraag_id=vraag_id,
                subvraag_label=subvraag_label,
                detector="trailing_ellipses",
                snippet=snippet,
                ernst="middel",
            )
        )
    for snippet in detecteer_loose_caps(tekst):
        flags.append(
            Flag(
                examen_file=examen_file,
                vraag_id=vraag_id,
                subvraag_label=subvraag_label,
                detector="loose_caps",
                snippet=snippet,
                ernst="laag",
            )
        )
    return flags


def itereer_examen_files(examen_dir: Path, examen_filter: str | None) -> Iterator[Path]:
    """Yield examen-vragen-files, met optionele filter op examen_id."""
    for pad in sorted(examen_dir.glob("*.json")):
        if pad.name.startswith("_"):
            continue
        if pad.name.endswith("-labels.json"):
            continue
        if examen_filter and pad.stem != examen_filter:
            continue
        yield pad


def scan_examen_data(
    examen_data: dict, examen_file: str
) -> tuple[list[Flag], int, int]:
    """Scan de vragen + subvragen in één examen-dict.

    Returns:
        (flags, aantal_vragen, aantal_subvragen)
    """
    flags: list[Flag] = []
    aantal_vragen = 0
    aantal_subvragen = 0

    for vraag in examen_data.get("vragen", []):
        aantal_vragen += 1
        vraag_id = vraag.get("id", "?")
        vraagtekst = vraag.get("vraagtekst", "") or ""
        flags.extend(
            detecteer_flags_voor_vraagtekst(
                vraagtekst, examen_file, vraag_id, subvraag_label=None
            )
        )
        for subvraag in vraag.get("subvragen", []) or []:
            aantal_subvragen += 1
            sub_tekst = subvraag.get("tekst", "") or ""
            sub_label = subvraag.get("label")
            flags.extend(
                detecteer_flags_voor_vraagtekst(
                    sub_tekst, examen_file, vraag_id, subvraag_label=sub_label
                )
            )
    return flags, aantal_vragen, aantal_subvragen


def bouw_rapport(
    flags: list[Flag], totaal_vragen: int, totaal_subvragen: int
) -> dict:
    """Bouw het JSON-rapport-object."""
    geflagged_ids = {(f.examen_file, f.vraag_id, f.subvraag_label) for f in flags}
    return {
        "gegenereerd_op": datetime.now(timezone.utc).isoformat(),
        "totaal_vragen": totaal_vragen,
        "totaal_subvragen": totaal_subvragen,
        "totaal_geflagged": len(geflagged_ids),
        "flags": [asdict(f) for f in flags],
    }


def print_samenvatting(rapport: dict) -> None:
    """Print compacte samenvatting naar stdout."""
    flags = rapport["flags"]
    print(f"Vragen gescand:      {rapport['totaal_vragen']}")
    print(f"Subvragen gescand:   {rapport['totaal_subvragen']}")
    print(f"Items geflagged:     {rapport['totaal_geflagged']}")
    print(f"Totaal flags:        {len(flags)}")
    per_detector: dict[str, int] = {}
    per_ernst: dict[str, int] = {}
    for f in flags:
        per_detector[f["detector"]] = per_detector.get(f["detector"], 0) + 1
        per_ernst[f["ernst"]] = per_ernst.get(f["ernst"], 0) + 1
    print("Per detector:")
    for detector, n in sorted(per_detector.items()):
        print(f"  {detector:<25} {n}")
    print("Per ernst:")
    for ernst in ("hoog", "middel", "laag"):
        if ernst in per_ernst:
            print(f"  {ernst:<25} {per_ernst[ernst]}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--examen",
        type=str,
        default=None,
        help="Targeting één examen-stem (bv. 2014-1)",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Alleen counts naar stdout, geen JSON-rapport schrijven",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit-code 1 als er ernst=hoog flags zijn",
    )
    args = parser.parse_args(argv)

    alle_flags: list[Flag] = []
    totaal_vragen = 0
    totaal_subvragen = 0

    files = list(itereer_examen_files(EXAMEN_VRAGEN_DIR, args.examen))
    if not files:
        print(f"Geen examen-vragen-files gevonden in {EXAMEN_VRAGEN_DIR}", file=sys.stderr)
        return 2

    for pad in files:
        with pad.open(encoding="utf-8") as f:
            examen_data = json.load(f)
        flags, n_vragen, n_sub = scan_examen_data(examen_data, pad.name)
        alle_flags.extend(flags)
        totaal_vragen += n_vragen
        totaal_subvragen += n_sub

    rapport = bouw_rapport(alle_flags, totaal_vragen, totaal_subvragen)

    if not args.summary:
        QA_RAPPORT_PAD.parent.mkdir(parents=True, exist_ok=True)
        with QA_RAPPORT_PAD.open("w", encoding="utf-8") as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        try:
            print(f"Rapport geschreven: {QA_RAPPORT_PAD.relative_to(REPO_ROOT)}")
        except ValueError:
            print(f"Rapport geschreven: {QA_RAPPORT_PAD}")

    print_samenvatting(rapport)

    if args.strict and any(f.ernst == "hoog" for f in alle_flags):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
