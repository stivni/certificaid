# Extractierapport — ITAA Voorbeeldexamens

**Tool**: `vragen-extractie-v1` (`tools/examen/extract_vragen.py`)
**PDF-bibliotheek**: pdfplumber
**Datum**: 2026-05-15

---

## Per examen

### 2013-1 (`2013-1.pdf`)

- **Pagina's**: 25
- **Vragen gevonden**: 37
- **Vraagtype-distributie**: J/F: 20, MC: 10, open: 7
- **Punten per vak** (som deelvragen):

| Vak | Code | Punten gevonden | Punten verwacht (INDEX.md) |
|---|---|---|---|
| Wetgeving jaarrekening | 1.1 | 15 | 15 |
| Jaarrekeninganalyse | 1.2 | 25 | 25 |
| IC + Accountantsonderzoek | 1.3 | 50 | 50 |
| Vennootschapsrecht | 3.1 | 20 | 20 |
| Bijzondere mandaten | 3.2 | 30 | 30 |
| Personenbelasting | 2.1 | 20 | 20 |
| Vennootschapsbelasting | 2.2 | 20 | 20 |
| BTW | 2.3 | 15 | 15 |
| Registratie-/successierechten | 2.4 | 10 | 10 |
| Europees/intern. fiscaal | 2.6 | 10 | 10 |
| Fiscale procedure | 2.7 | 15 | 15 |
| Deontologie/AWW | 4.0 | 20 | 20 |
| **Totaal** | | **250** | **150** |

> De som 250 pt is de som van alle deelvraagpunten; de ITAA-schaling naar 150 pt is een externe weging niet vervat in de PDF. Per vak kloppen de punten 100%.

- **Thema-dekking**: 94% (2 vragen zonder thema: definitie financiële begrippen, definitie interne controle)
- **OCR-kwaliteit**: goed — afkomstig van Studocu-scan met dubbele tekens op titelblad (b.v. "IITTAAAA"), maar inhoudelijke pagina's zijn leesbaar. Geen `ocr_quality`-vlag vereist.

---

### 2013-2 (`2013-2.pdf`)

- **Pagina's**: 26
- **Vragen gevonden**: 38
- **Vraagtype-distributie**: J/F: 15, MC: 9, berekening+MC: 6, open: 7, berekening: 1
- **Punten per vak**: identiek aan 2013-1 schema (som 250 pt, per vak correct)
- **Thema-dekking**: 89% (4 vragen zonder thema: schilderwerk-voorziening, nettobedrijfskapitaal-definitie, functiescheiding-tabel, BTW-herziening stopzetting)
- **OCR-kwaliteit**: goed — zelfde Studocu-scan kenmerken als 2013-1

---

### 2014-1 (`2014-1.pdf`)

- **Pagina's**: 31
- **Vragen gevonden**: 46
- **Vraagtype-distributie**: J/F: 25, open: 14, berekening+MC: 3, MC: 4
- **Specifiek 2014-1**: 1.3 gesplitst in IC (25 pt) en AO (25 pt) als aparte secties

| Vak | Code | Punten gevonden | Punten verwacht |
|---|---|---|---|
| Wetgeving jaarrekening | 1.1 | 15 | 15 |
| Jaarrekeninganalyse | 1.2 | 25 | 25 |
| Interne controle | 1.3 IC | 25 | 25 |
| Accountantsonderzoek | 1.3 AO | 25 | 25 |
| Vennootschapsrecht | 3.1 | 20 | 20 |
| Bijzondere mandaten | 3.2 | 30 | 30 |
| Personenbelasting | 2.1 | 20 | 20 |
| Vennootschapsbelasting | 2.2 | 20 | 20 |
| BTW | 2.3 | 15 | 15 |
| Registratie-/successierechten | 2.4 | 10 | 10 |
| Europees/intern. fiscaal | 2.6 | 10 | 10 |
| Fiscale procedure | 2.7 | 15 | 15 |
| Deontologie/AWW | 4.0 | 20 | 20 |
| **Totaal** | | **250** | **150** |

- **Thema-dekking**: 93% (3 vragen zonder thema: disconto-berekening, consolidatietabel M→A/B/C, diverse inkomsten PB)
- **OCR-kwaliteit**: goed

---

### 2015-1 (`2015_1_-_bekwaamheidsexamen_ac_1.pdf`)

- **Pagina's**: 37
- **Vragen gevonden**: 56
- **Vraagtype-distributie**: J/F: 34, MC: 17, berekening+MC: 2, open: 3
- **Specifiek 2015-1**: volledig MC-examen met antwoordrooster bovenaan pagina 1 ("Vraag 1a 1b 2 3 4 5 6 7 — Antwoord — Punten 1,5 1,5 2 2 2 2 2 2"). Geen Studocu-watermark op eerste pagina.
- **Punten per vak**: identiek schema als 2014-1 (som 250 pt, per vak correct; 2.7 staat achteraan vóór 2.4/2.6 in dit examen)
- **Thema-dekking**: 80% (11 vragen zonder thema; overwegend algemene definitievragen IC, BTW-specifieke situaties, aanvaardingsprocedure)
- **OCR-kwaliteit**: goed — geen dubbele tekens

---

### 2024-1 (`Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf`)

- **Pagina's**: 6
- **Vragen gevonden**: 11
- **Vraagtype-distributie**: J/F: 9, MC: 2
- **Punten**: niet opgegeven in document
- **Vak-codes**: nieuwe nummering (2024+); geen 2.4 (registratierechten) en geen 2.6 (Europees fiscaal) aanwezig
- **Thema-dekking**: 100%
- **OCR-kwaliteit**: goed — geen Studocu-scan, beknopte vragenlijst
- **Let op**: dit document bevat uitsluitend vraagopgaven zonder bijlagen, balansen of antwoordsleutels. De vraagteksten zijn schematisch (A./B./C. bullets per vraagnummer) in plaats van uitgewerkte casussen.

---

## OCR-issues

Geen `ocr_quality: partial` of `unreadable` vlagen vereist. Alle PDFs zijn leesbaar door pdfplumber.

Aandachtspunten:
- **Tabelinhoud** (bijlagen met balansen, resultatenrekeningen, BTW-roosters) wordt door pdfplumber als losse kolommen geëxtraheerd en is in de vraagtekst opgenomen als platte tekst met onregelmatige spaties. De inhoud is aanwezig maar niet perfect gestructureerd.
- **Studocu titelblad** (pagina 1 van 2013-1, 2013-2, 2014-1): dubbele tekens door scan-artefact ("IITTAAAA", "22001133"). Gefilterd via `strip_studocu()`. Geen invloed op vraaginhoud.
- **2015-1 antwoordrooster** (pagina 1): het schema "Vraag 1a 1b 2 3 ..." is als pseudo-vraag opgenomen in de JSON maar gemarkeerd als `"punten": None` en `"vraag_nr": "1a"`. Dit is een artefact van het MC-antwoordformulier — geen echte vraag. Aanbeveling voor fase 2: filter vragen met `"vraagtekst"` die alleen het antwoordrooster bevatten.

---

## Mapping: oude vak-codes (2013-2015) → nieuwe codes (2024+)

| Oude code (2013-2015) | Vak naam | Nieuwe code (2024+) |
|---|---|---|
| 1.1 | Wetgeving inzake de jaarrekening | 1.1 (uitgebreid met IFRS) |
| 1.2 | Analyse en kritische beoordeling / consolidatie | 1.2 |
| 1.3 | Interne controle en accountantsonderzoek (gecombineerd) | 1.3 IC + 1.3 AO (gesplitst) |
| 2.1 | Personenbelasting | 2.1 |
| 2.2 | Vennootschapsbelasting | 2.2 |
| 2.3 | BTW | 2.3 |
| 2.4 | Registratie- en successierechten | 2.4 (ontbreekt in 2024) |
| 2.6 | Europees en internationaal fiscaal recht | 2.6 (ontbreekt in 2024) |
| 2.7 | Fiscale procedure | 2.7 |
| 3.1 | Vennootschapsrecht | 3.1 (nu WVV-gericht) |
| 3.2 | Vennootschapsrecht bijzondere mandaten | 3.2 |
| 4.0 | Juridische en beroepsnormen / deontologie + AWW | 4.0 |

Observaties:
- In 2013-2015 is 1.3 één blok van 50 punten; vanaf 2014 soms gesplitst in IC (25 pt) en AO (25 pt).
- PO 2.1 in 2013-2015 bevat "Algemeenheden PB" die in 2024 mogelijk naar een apart PO 2.1a zijn verplaatst (niet zichtbaar in beschikbare documenten).
- 2024 voegt expliciet IFRS toe aan 1.1; in 2013-2015 ontbreekt IFRS.
- De 2024-PDF vermeldt geen puntenverdeling per vraag of per sectie.

---

## Bestanden aangemaakt

| Bestand | Vragen | Pagina's |
|---|---|---|
| `data/examen_vragen/2013-1.json` | 37 | 25 |
| `data/examen_vragen/2013-2.json` | 38 | 26 |
| `data/examen_vragen/2014-1.json` | 46 | 31 |
| `data/examen_vragen/2015-1.json` | 56 | 37 |
| `data/examen_vragen/2024-1.json` | 11 | 6 |

**Script**: `tools/examen/extract_vragen.py`
