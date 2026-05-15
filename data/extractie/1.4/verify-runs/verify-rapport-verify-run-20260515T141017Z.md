# VERIFY-rapport — verify-run-20260515T141017Z

**Programmaonderdeel**: 1.4 (Consolidatie)
**Gegenereerd op**: 2026-05-15T14:30:00+00:00
**Scope**: 30 records / 13 anchors

## Samenvatting

| Bron | aantal gaps |
|---|---|
| Bestaand (mechanisch) | 1 |
| Nieuw (deze run)      | 8 |
| **Totaal in gaps.json** | **9** |

### Per check
- **Check A** (examenvraag-simulatie, 6 representatieve consolidatievragen uit 2013-1 / 2013-2 / 2014-1 / 2015-1): **2 gaps**
- **Check B** (minicursus-haalbaarheid + uniforme rijkheid): **2 gaps**
- **Check C1** (mechanisch): 1 reeds bestaand, **0 nieuwe**
- **Check C2** (LLM-oordeel: vrije tekst + overlap): **4 gaps** (1 overlap + 3 vrije-tekst-niet-gespiegeld)

### Per prio
- **hoog**: 2
- **midden**: 6
- **laag**: 1 (bestaand)

---

## Top-5 zwaarste gaps

1. **geconsolideerde-jaarrekening → `drempelwaarden.ontbreekt`** (hoog)
   Examenvragen 2013-1 vr7 en 2014-1 vr7 vragen de maximale afwijking qua afsluitingsdatum (KB WVV art. 3:109, tweede lid: 3 maanden). De bouwsteen "Afsluitingsdatum" in het record vermeldt enkel "mits motivering in de toelichting" zonder de drie-maanden-drempel — vraag onbeantwoordbaar uit record alleen.

2. **consolidatieverschil → `definitie.onvolledig`** (hoog)
   Examenvragen 2013-2 vr8 en 2015-1 vr11 vragen expliciet de **vier** voornaamste oorzaken van **positieve** consolidatieverschillen (8 / 4 punten). Het record `oorzaken[]` bevat 3 entries waarvan één over negatieve verschillen. Een vierde positieve oorzaak (typisch: immateriële activa / klantenbestand / merken als afzonderlijke verklaring naast goodwill voor synergie) ontbreekt.

3. **groep-van-beperkte-omvang → `records.overlappend-fenomeen`** (midden)
   Sterke inhoudelijke overlap met `groottecriteria-consolidatie` (zelfde bron WVV art. 1:26, § 1; beide records beschrijven de twee berekeningsmethoden — geconsolideerd en geaggregeerd +20 %). Eén van beide records herorganiseren of samenvoegen voorkomt redundantie.

4. **geconsolideerd-jaarverslag → `in_praktijk.ontbreekt`** (midden)
   Slechts 1 in_praktijk-entry, 1 valkuil, 1 vergelijkingspaar — dunst van alle 30 records terwijl het concept centraal staat in WVV art. 3:32 / 3:35 (inhoudsvereisten, risico's, niet-financiële verklaring, beschrijving van deelnemingen). Te dun voor een coherente minicursus-paragraaf.

5. **exclusieve-controle → `in_praktijk.ontbreekt`** (midden)
   Slechts 1 in_praktijk-entry voor een concept dat de keuze tussen integrale consolidatie en de andere methoden bepaalt. Voorbeeld van controle in feite (bestuurdersbenoeming op de twee laatste AV's) en het onderscheid tussen de onweerlegbare vermoedens (> 50 % stemrechten / bestuurdersbenoeming / stemovereenkomst) ontbreekt.

---

## Geconstateerde gaps Check A — examenvraag-simulatie

Gesimuleerde vragen (6 stuks):

| Vraag | Onderwerp | Beantwoordbaar uit records? |
|---|---|---|
| 2013-1 #vr6 | post in geconsolideerde resultatenrekening voor aandeel derden | ja — `minderheidsbelangen.definitie` noemt expliciet "Aandeel van derden in het resultaat" |
| 2013-1 #vr7 | max afwijking afsluitingsdatum | **nee** — drempel 3 maanden ontbreekt → gap (hoog) |
| 2013-2 #vr8 | + en 4 voornaamste oorzaken positief consolidatieverschil | **deels** — definitie OK, oorzaken[] telt slechts 3 (1 negatief) → gap (hoog) |
| 2014-1 #vr7 | max afwijking afsluitingsdatum | idem 2013-1 vr7 — zelfde gap |
| 2014-1 #vr8 | tabel controle%/belang%/consolidatiemethode | ja — `controlepercentage.in_praktijk` + `belangenpercentage.in_praktijk` geven expliciete rekenregels en herkenningspunten |
| 2015-1 #vr11 | + en 4 voornaamste oorzaken positief consolidatieverschil | idem 2013-2 vr8 — zelfde gap |

## Geconstateerde gaps Check B — minicursus

- `geconsolideerd-jaarverslag` te dun (1+1+1 in praktijk/valkuilen/vp).
- `exclusieve-controle` te dun aan in_praktijk (1) voor centraal concept dat consolidatiekeuze stuurt.
- Niet gelogd maar opgemerkt: `controle` heeft kortste definitie (369 tekens) maar wordt grotendeels gecompenseerd door 2 bouwstenen (in rechte / in feite) en 4 vergelijkingsparen — voldoende voor minicursus.

## Geconstateerde gaps Check C — semantische coherentie

### C1 mechanisch (al gelogd in run-start, hier ter completeness)
- `consolidatieverplichting → groottecriteria` — target moet `groottecriteria-consolidatie` zijn (typo). Status open, prio laag.

### C2 LLM-oordeel
- `groep-van-beperkte-omvang ↔ groottecriteria-consolidatie` — `records.overlappend-fenomeen`.
- `consolidatieverschil` — definitie noemt "dochter- en geassocieerde onderneming" als bereik, maar deze records staan niet als VP/edge.
- `evenredige-consolidatie` — definitie verwijst naar gezamenlijke controle / gemeenschappelijke dochter / minderheidsbelangen, niet gespiegeld als VP.
- `vermogensmutatiemethode` — asymmetrische VP: `invloed-van-betekenis` en `consolidatieverschil` wijzen wel naar `vermogensmutatiemethode`, maar omgekeerd niet.

## Algeheel oordeel

**`needs-enrich`** — geen extract-rerun nodig.

Rationale: de records dekken het programmaonderdeel inhoudelijk goed (alle 13 anchors hebben minstens één goed gevuld record, methode/procedure/begrip-records zijn uniform in rijkheid, examenvragen zijn voor 4 van de 6 unieke vraagstellingen volledig beantwoordbaar). De twee Check-A-strandpunten zijn precies de soort puntuele aanvullingen die `enrich_records.py` kan toevoegen (één numerieke drempel toevoegen aan een bestaand bouwsteen + één extra `oorzaken[]`-entry uitschrijven), niet een schaarsteprobleem in de extractiestap zelf.
