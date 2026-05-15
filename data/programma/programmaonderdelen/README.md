# Programmaonderdelen — werkcontext

De inhoud van het ITAA-examenprogramma 04/2022 (`resources/raw/andere/programma.pdf`) leeft sinds 2026-05-10 in **één globaal bestand**: [`data/programma.json`](../programma.json).

Per-PO ankerlijsten in [`data/extractie/<po>/anchors/<po>-anchors.json`](../extractie/) zijn afgeleid en regenereerbaar via:

```bash
python3 -m tools.extractie.flatten_anchors
```

Deze map bevat alleen nog **per-PO scope-yamls** (legacy, zolang `match_bronnen.py` per-PO matching ondersteunt; verdwijnt zodra de matcher globaal werkt).

## Mapping examenprogramma-letter ↔ programmaonderdeel-nummer

Het examenprogramma 04/2022 nummert de hoofdstukken alfabetisch (A-T). De projectinterne nummering (1.1 t/m 4.0) volgt de oude vakindeling van vóór de 2022-hervorming. De volgorde komt niet overeen.

| Letter | Nummer | Titel (kort) |
|---|---|---|
| A | — | Methodologie (geen programmaonderdeel) |
| B | 1.1 | Algemene boekhouding |
| C | 1.2 | Boekhoudrecht en jaarrekeningenrecht |
| D | 1.3 | Analyse en kritische beoordeling van de jaarrekening |
| E | 1.4 | Geconsolideerde jaarrekening |
| F | 1.9 | Financiële analyse en fundamentele principes |
| G | 1.8 | Analytische boekhouding en management accounting |
| H | 1.6 | Externe controle |
| I | 1.7 | Interne controle |
| J | 1.5 | Beginselen van de Europese wetgeving en internationale boekhoudkundige normen |
| K | 3.0 | Vennootschaps- en verenigingsrecht en insolventiewetgeving (zie *3.1/3.2-splitsing* hieronder) |
| L | 2.1 | Algemene beginselen van fiscaal recht |
| M | 2.8 | Europees en internationaal fiscaal recht |
| N | 2.6 | Registratie- en successierechten |
| O | 2.7 | Regionale en lokale belastingen |
| P | 2.2 | Personenbelasting |
| Q | 2.3 | Vennootschapsbelasting |
| R | 2.5 | Fiscale procedure |
| S | 2.4 | Belasting over de toegevoegde waarde |
| T | 4.0 | Deontologische beginselen + antiwitwaswetgeving |

## Algemene werkafspraken

### Pre-2022 examens hebben een andere vaknummering

De hervorming van 2022 heeft de vaknummering gewijzigd. Voorbeeldexamens van vóór 2022 (`resources/raw/voorbeeldexamens/2013-1.pdf`, `2013-2.pdf`, `2014-1.pdf`, `2015_1_*.pdf`) gebruiken de **oude** nummering. Bij koppeling van examenvragen aan programmaonderdelen of kenniselementen: vertaal de oude nummering eerst, of gebruik een titel-match.

Voorbeeldexamen ITAA 2024 (`resources/raw/voorbeeldexamens/Vragen schriftelijk bekwaamheidsexamen ITAA 2024.pdf`) gebruikt de huidige nummering — geen vertaling nodig.

### 3.1/3.2-splitsing tijdens het examen

Het examenprogramma 04/2022 heeft één hoofdstuk K = *"Vennootschaps- en verenigingsrecht en insolventiewetgeving"*. Tijdens het echte examen wordt dit gesplitst in:
- **3.1 Vennootschapsrecht**
- **3.2 Bijzondere mandaten**

Voor extractie volgen we de programma-structuur (één `code: "3.0"` PO in `programma.json`). Examenvragen kunnen extra labels krijgen (`onderdeel: "3.1"` / `"3.2"`) wanneer dat duidelijk is uit de vraag.

## Code-conventie voor ankers (in `programma.json`)

Globaal uniek; hiërarchie afleidbaar uit het pad:

- `<po>.taak.<n>` — hoofd-taak (bv. `1.6.taak.1`)
- `<po>.taak.<n>.<a/b/c/...>` — subtaak
- `<po>.taak.<n>.doel.<m>` — doelstelling onder een taak
- `<po>.taak.<n>.doel.<m>.<a/b/...>` — subdoelstelling
- `<po>.<I/II/...>` — kenniselement-hoofdgroep (Romeins)
- `<po>.<I>.<A/B/...>` — kenniselement-subgroep (Latijn)
- Diepere nesting: `<po>.<I>.<A>.<1>.<a>` (max 4-5 levels in praktijk)
