"""Tests voor `tools/examen/normalize_vraagteksten.py`."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.examen.normalize_vraagteksten import (
    bouw_rapport,
    detecteer_broken_table,
    detecteer_flags_voor_vraagtekst,
    detecteer_loose_caps,
    detecteer_open_antwoord_prompt,
    detecteer_trailing_ellipses,
    main,
    scan_examen_data,
)


# ---------------------------------------------------------------------------
# trailing_ellipses
# ---------------------------------------------------------------------------

def test_trailing_ellipses_legitiem_punten_format_niet_geflagged() -> None:
    """`Vraag 4 … / 3 punten` is standaard ITAA-format en mag niet flaggen."""
    tekst = "Vraag 4 … / 3 punten Vennootschap Export heeft op 5 februari 2014..."
    assert detecteer_trailing_ellipses(tekst) == []


def test_trailing_ellipses_na_antwoord_middenin_wel_geflagged() -> None:
    tekst = (
        "Vraag 3 … / 8 punten lange uitleg over een octrooi en daarna "
        "d) wat zou er moeten gebeuren? Antwoord …/ 2 punten dan volgt opties"
    )
    flags = detecteer_trailing_ellipses(tekst)
    assert len(flags) >= 1


def test_trailing_ellipses_tussen_cijfers_geflagged() -> None:
    tekst = "Vraag 1 / 2 punten Het bedrag bedraagt 1000 … 2000 EUR per jaar."
    flags = detecteer_trailing_ellipses(tekst)
    assert len(flags) >= 1


# ---------------------------------------------------------------------------
# broken_table
# ---------------------------------------------------------------------------

def test_broken_table_kapotte_tabel_geflagged() -> None:
    tekst = "Vul de tabel aan. M 70 % 30 % 60 % 20 % A B C Antwoord"
    flags = detecteer_broken_table(tekst)
    assert len(flags) == 1
    assert "70 %" in flags[0]


def test_broken_table_pipe_table_niet_geflagged() -> None:
    tekst = "| M | 70 % | 30 % | 60 % |\n| A | B | C | D |"
    assert detecteer_broken_table(tekst) == []


def test_broken_table_twee_percents_op_regel_niet_geflagged() -> None:
    tekst = "De groei was 5 % vorig jaar en 7 % dit jaar."
    assert detecteer_broken_table(tekst) == []


# ---------------------------------------------------------------------------
# loose_caps
# ---------------------------------------------------------------------------

def test_loose_caps_whitelist_ifrs_niet_geflagged() -> None:
    tekst = "Volgens IFRS moet de onderneming dit boeken."
    assert detecteer_loose_caps(tekst) == []


def test_loose_caps_whitelist_btw_niet_geflagged() -> None:
    tekst = "De BTW wordt later afgedragen."
    assert detecteer_loose_caps(tekst) == []


def test_loose_caps_maatschapkring_wel_geflagged() -> None:
    tekst = "De MaatschapKring is een speciale vorm."
    flags = detecteer_loose_caps(tekst)
    assert "MaatschapKring" in flags


def test_loose_caps_meerdere_woorden_geflagged() -> None:
    tekst = "De boekhouderHeeft de boekHouding gevoerd."
    flags = detecteer_loose_caps(tekst)
    # boekhouderHeeft, boekHouding
    assert len(flags) == 2


# ---------------------------------------------------------------------------
# open_antwoord_prompt
# ---------------------------------------------------------------------------

def test_open_antwoord_prompt_na_vraagteken_niet_geflagged() -> None:
    tekst = "Wat is het bedrag? Antwoord  5.000 EUR  10.000 EUR"
    assert detecteer_open_antwoord_prompt(tekst) == []


def test_open_antwoord_prompt_op_einde_niet_geflagged() -> None:
    tekst = "Vul de tabel in. Antwoord"
    assert detecteer_open_antwoord_prompt(tekst) == []


def test_open_antwoord_prompt_middenin_zonder_vraagteken_geflagged() -> None:
    tekst = (
        "Vraag 4 / 3 punten Bereken het bedrag dat in de omzet wordt opgenomen "
        "Antwoord  5.000.000 EUR  5.600.000 EUR  4.400.000 EUR"
    )
    flags = detecteer_open_antwoord_prompt(tekst)
    assert len(flags) >= 1


def test_open_antwoord_prompt_na_dubbelepunt_niet_geflagged() -> None:
    tekst = "De opties zijn als volgt: Antwoord 1 of 2 of 3."
    assert detecteer_open_antwoord_prompt(tekst) == []


# ---------------------------------------------------------------------------
# combinator + dataclass
# ---------------------------------------------------------------------------

def test_detecteer_flags_combineert_alle_detectors() -> None:
    tekst = "Vul tabel. M 70 % 30 % 60 % 20 % A B C. De boekHouder boekt."
    flags = detecteer_flags_voor_vraagtekst(
        tekst, examen_file="fake.json", vraag_id="vrX", subvraag_label=None
    )
    detectors = {f.detector for f in flags}
    assert "broken_table" in detectors
    assert "loose_caps" in detectors


def test_detecteer_flags_lege_tekst_geen_flags() -> None:
    flags = detecteer_flags_voor_vraagtekst(
        "", examen_file="fake.json", vraag_id="vrX", subvraag_label=None
    )
    assert flags == []


def test_flag_ernst_niveaus() -> None:
    flags = detecteer_flags_voor_vraagtekst(
        "M 70 % 30 % 60 % 20 % A B",
        examen_file="fake.json",
        vraag_id="vr1",
        subvraag_label=None,
    )
    assert all(f.ernst == "hoog" for f in flags if f.detector == "broken_table")


# ---------------------------------------------------------------------------
# end-to-end op mini-corpus
# ---------------------------------------------------------------------------

@pytest.fixture
def mini_corpus(tmp_path: Path) -> Path:
    """Bouw 3 fake examen-vragen-files + 1 metadata-file + 1 labels-file."""
    examen_dir = tmp_path / "examen_vragen"
    examen_dir.mkdir()

    # Echte file 1: bevat broken_table + open_antwoord_prompt
    (examen_dir / "2099-1.json").write_text(
        json.dumps(
            {
                "examen_id": "2099-1",
                "vragen": [
                    {
                        "id": "2099-1-vr1",
                        "vraagtekst": (
                            "Vraag 1 … / 2 punten Vul de tabel aan. "
                            "M 70 % 30 % 60 % 20 % A B C Antwoord"
                        ),
                        "subvragen": [],
                    },
                    {
                        "id": "2099-1-vr2",
                        "vraagtekst": "Wat is X? Antwoord  optie1  optie2",
                        "subvragen": [
                            {
                                "label": "a)",
                                "tekst": "Bereken Y zonder vraagteken Antwoord  1  2  3",
                            }
                        ],
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    # Echte file 2: schoon
    (examen_dir / "2099-2.json").write_text(
        json.dumps(
            {
                "examen_id": "2099-2",
                "vragen": [
                    {
                        "id": "2099-2-vr1",
                        "vraagtekst": "Vraag 1 / 2 punten Volgens IFRS is dit correct.",
                        "subvragen": [],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    # Echte file 3: loose_caps
    (examen_dir / "2099-3.json").write_text(
        json.dumps(
            {
                "examen_id": "2099-3",
                "vragen": [
                    {
                        "id": "2099-3-vr1",
                        "vraagtekst": "De MaatschapKring is een entiteit.",
                        "subvragen": [],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    # Skip: underscore-metadata
    (examen_dir / "_metadata.json").write_text("{}", encoding="utf-8")
    # Skip: labels
    (examen_dir / "2099-1-labels.json").write_text("{}", encoding="utf-8")

    return examen_dir


def test_end_to_end_op_mini_corpus(mini_corpus: Path) -> None:
    """End-to-end: scan 3 files, verwacht flags op file 1 + file 3, file 2 schoon."""
    from tools.examen import normalize_vraagteksten as mod

    alle_flags = []
    totaal_vragen = 0
    totaal_subvragen = 0
    for pad in mod.itereer_examen_files(mini_corpus, examen_filter=None):
        with pad.open(encoding="utf-8") as f:
            data = json.load(f)
        flags, n_v, n_s = scan_examen_data(data, pad.name)
        alle_flags.extend(flags)
        totaal_vragen += n_v
        totaal_subvragen += n_s

    assert totaal_vragen == 4
    assert totaal_subvragen == 1

    bestanden_met_flags = {f.examen_file for f in alle_flags}
    assert "2099-1.json" in bestanden_met_flags
    assert "2099-3.json" in bestanden_met_flags
    assert "2099-2.json" not in bestanden_met_flags
    # underscore + labels mogen niet gescand worden
    assert "_metadata.json" not in bestanden_met_flags
    assert "2099-1-labels.json" not in bestanden_met_flags

    rapport = bouw_rapport(alle_flags, totaal_vragen, totaal_subvragen)
    assert rapport["totaal_vragen"] == 4
    assert rapport["totaal_subvragen"] == 1
    assert rapport["totaal_geflagged"] >= 2


def test_main_summary_modus_schrijft_geen_file(
    monkeypatch: pytest.MonkeyPatch, mini_corpus: Path, tmp_path: Path
) -> None:
    """`--summary` mag geen rapport-file schrijven."""
    from tools.examen import normalize_vraagteksten as mod

    qa_pad = tmp_path / "vraagtekst_qa.json"
    monkeypatch.setattr(mod, "EXAMEN_VRAGEN_DIR", mini_corpus)
    monkeypatch.setattr(mod, "QA_RAPPORT_PAD", qa_pad)

    exit_code = main(["--summary"])
    assert exit_code == 0
    assert not qa_pad.exists()


def test_main_strict_modus_exit_1_bij_hoog(
    monkeypatch: pytest.MonkeyPatch, mini_corpus: Path, tmp_path: Path
) -> None:
    from tools.examen import normalize_vraagteksten as mod

    qa_pad = tmp_path / "vraagtekst_qa.json"
    monkeypatch.setattr(mod, "EXAMEN_VRAGEN_DIR", mini_corpus)
    monkeypatch.setattr(mod, "QA_RAPPORT_PAD", qa_pad)

    exit_code = main(["--strict", "--summary"])
    # mini_corpus heeft een broken_table = hoog
    assert exit_code == 1


def test_main_schrijft_rapport(
    monkeypatch: pytest.MonkeyPatch, mini_corpus: Path, tmp_path: Path
) -> None:
    from tools.examen import normalize_vraagteksten as mod

    qa_pad = tmp_path / "vraagtekst_qa.json"
    monkeypatch.setattr(mod, "EXAMEN_VRAGEN_DIR", mini_corpus)
    monkeypatch.setattr(mod, "QA_RAPPORT_PAD", qa_pad)

    exit_code = main([])
    assert exit_code == 0
    assert qa_pad.exists()

    rapport = json.loads(qa_pad.read_text(encoding="utf-8"))
    assert "gegenereerd_op" in rapport
    assert "flags" in rapport
    assert rapport["totaal_vragen"] == 4


def test_main_examen_filter(
    monkeypatch: pytest.MonkeyPatch, mini_corpus: Path, tmp_path: Path
) -> None:
    from tools.examen import normalize_vraagteksten as mod

    qa_pad = tmp_path / "vraagtekst_qa.json"
    monkeypatch.setattr(mod, "EXAMEN_VRAGEN_DIR", mini_corpus)
    monkeypatch.setattr(mod, "QA_RAPPORT_PAD", qa_pad)

    exit_code = main(["--examen", "2099-2"])
    assert exit_code == 0
    rapport = json.loads(qa_pad.read_text(encoding="utf-8"))
    # 2099-2 is schoon
    assert rapport["totaal_vragen"] == 1
    assert rapport["totaal_geflagged"] == 0
