# ITAA Normen — Semantische index

Gebruik deze index om te bepalen welke norm relevant is voor een onderwerp.
Grep daarna in het volledige bestand: `grep -n "zoekterm" content/bronnen/normen/NAAM.md`

**Werkwijze zoeken op thema:**
```
grep -rl "  - [thema]" content/bronnen/normen/
```

Laatste update: 2026-05-02

---

| Bestand | Naam | Datum | Thema's |
|---|---|---|---|
| `ITAA-norm-algemene-controlenorm.md` | Algemene Controlenorm | 1991-09-30 | controle, accountancy, rapportering, verslag |
| `ITAA-norm-kmo-controlenorm.md` | KMO-Controlenorm | 2019 | controle, KMO, assurance, gedeelde voorbehouden opdrachten |
| `ITAA-norm-aww-reglement.md` | AWW-Reglement (IAB/ITAA) | 2020-03-31 | antiwitwas, cliëntenonderzoek, UBO, AMLCO, risicoanalyse, meldingsplicht |
| `ITAA-norm-aww-procedurereglement.md` | Procedurereglement Tuchtkamer AWW (art. 118 AWW) | — | antiwitwas, tucht, tuchtkamer, procedure, sanctie |
| `ITAA-norm-opdrachtbrief.md` | Nota Opdrachtbrief | — | opdrachtbrief, opdrachtenrecht, aanvang opdracht |
| `ITAA-norm-permanente-vorming.md` | Norm Permanente Vorming | 2020-12-01 | permanente vorming, stage, opleiding, uren, sanctie |
| `ITAA-norm-gedragslijnen-relaties-IBR.md` | Gedragslijnen betrekkingen IBR | — | samenwerking, IBR, bedrijfsrevisor, gedeelde opdrachten |
| `ITAA-norm-omzetting-vennootschap.md` | Norm Verslag bij Omzetting Vennootschap | — | vennootschapsrecht, omzetting, verslag, WVV |
| `ITAA-norm-ontbinding-vereffening.md` | Norm Opdracht Ontbinding en Vereffening | — | vennootschapsrecht, ontbinding, vereffening, verslag, WVV |
| `ITAA-norm-domiciliering.md` | Norm Domiciliëring | 2024-09-02 | domiciliëring, maatschappelijke zetel, cliëntenrelatie |
| `ISA-570-herzien.md` | ISA 570 (herzien) — Continuïteit | 2023 | continuïteitsrisico, going concern, ISA, assurance, controle |

| `ITAA-norm-aww-richtlijn-bibf.md` | AWW-Richtlijn (BIBF) | 2020-03-31 | antiwitwas, cliëntenonderzoek, UBO, AMLCO, BIBF |
| `ITAA-norm-aww-geconsolideerd.md` | Geconsolideerde AWW-norm (IAB + BIBF gecombineerd) | 2022-04-26 | antiwitwas, cliëntenonderzoek, UBO, AMLCO, geconsolideerd |
| `ITAA-norm-fusie-splitsing.md` | Norm Controle Fusie- en Splitsingsverrichtingen | 2013-12-13 | fusie, splitsing, vennootschapsrecht, verslag, ruilverhouding, WVV |
| `ITAA-norm-samenstellingsopdrachten-isrs4410.md` | Norm Samenstellingsopdrachten (ISRS 4410) | 2025-05-09 | samenstellingsopdrachten, ISRS 4410, assurance, jaarrekening |
| `ITAA-norm-intern-kwaliteitsmanagement.md` | Norm Algemene Vereisten Intern Kwaliteitsmanagement | 2025-09-03 | kwaliteitsmanagement, intern kwaliteitssysteem, kantoororganisatie |
| `ITAA-norm-effectennorm.md` | Effectennorm *(nog niet in werking)* | 2026-03-31 | effectennorm, beoordeling, financiële gegevens, assurance |

## Herdownloaden / bijwerken

Alle normen zijn lokaal beschikbaar. Om een norm te vernieuwen na een update op BeExcellent:

1. Log in op het ITAA-portaal via de browser
2. Voer `python3 tools/download_beexcellent_normen.py` uit — het script haalt verse presigned URLs op en converteert de bestanden opnieuw

**BeExcellent artikel-IDs** (voor handmatige toegang):
- AWW BIBF richtlijn: artikel 4 | AWW geconsolideerd: artikel 416
- Fusie/splitsing: artikelen 56–60 | ISRS 4410: artikel 2091
- Kwaliteitsmanagement: artikel 2640 | Effectennorm: artikel 2692
