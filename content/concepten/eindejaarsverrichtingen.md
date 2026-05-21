---
title: Eindejaarsverrichtingen (jaarafsluiting)
tags:
- concept
- procedure
- po-1-2
linked_anchors:
- 1.2.taak.1
- 1.2.III.D
- 1.2.V
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: procedure
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/eindejaarsverrichtingen.json
gegenereerd_op: '2026-05-21'
---
# Eindejaarsverrichtingen (jaarafsluiting) 🔗

De eindejaarsverrichtingen (afsluitingsboekingen) zijn de boekingen die de boekhoudkundige cijfers tot **economische waarheid** brengen op balansdatum: afschrijvingen, waardeverminderingen, voorzieningen, overlopende rekeningen, periodisering. Voor de stagiair-GA is dit het meest praktische thema van PO 1.2 — examen-cases vertrekken vaak vanuit één missing eindejaarsverrichting.

> [!summary] Korte inhoud
> Voor het opstellen van de jaarrekening moeten de eindejaarsverrichtingen (ook 'inventarisboekingen' of 'afsluitingsboekingen') worden uitgevoerd.

Voor het opstellen van de jaarrekening moeten de eindejaarsverrichtingen (ook 'inventarisboekingen' of 'afsluitingsboekingen') worden uitgevoerd. Dit zijn boekingen die de boekhouding aanvullen om de positie op balansdatum correct weer te geven: afschrijvingen, waardeverminderingen, voorzieningen, overlopende rekeningen, herwaarderingen, eindvoorraad en herklasseringen.



## In de praktijk

<h3 id="volgorde-matters">Volgorde matters</h3>

> [!tip]- Volgorde matters
> Beste praktijk: eerst inventariseren, dan afschrijvingen, dan waardeverminderingen, dan voorzieningen, dan overlopende rekeningen, dan eindvoorraad. Zo bouw je systematisch het correcte beeld op. 🔗

> [!tip]- Herkennen op het examen
> Examen-scenario 'voer eindejaarsverrichtingen uit' → ga deze volgorde af, niet random.


## Tijdlijn

| Stap | Termijn | Actor | Actie |
|---|---|---|---|
| Inventarisatie | op of vlak na balansdatum | onderneming | Fysieke telling + bevestigingen + lijsten |
| Inventaris-boekingen | binnen 6 maanden na balansdatum | onderneming + accountant | Afschrijvingen, waardeverminderingen, voorzieningen, overlopende rekeningen |
| Definitieve proef-en-saldibalans | vóór jaarrekening-opstelling | accountant | Controle debet = credit; basis voor balans + RR |

## Stappen

### 1. Inventaris opmaken

Eens per jaar (op balansdatum) opnemen, verifiëren en waarderen van alle bezittingen, vorderingen, schulden en verplichtingen. Resultaat: inventarislijst.

**Waarom?** Zonder inventaris kun je niet beoordelen wat werkelijk in de boeken hoort te staan.

**📥 Input**:
- Magazijn → **Fysieke voorraad** _(telling)_
- Bankrekeningen → **Saldo per 31/12** _(bevestiging-bank)_
- Klantenlijst → **Openstaande facturen** _(lijst)_

**📤 Output**:
- Inventarisboek → **Alle bezittingen/vorderingen/schulden** _(boekhoudkundig-overzicht)_

**🛠️ Hoe**:

1. Tel fysiek de voorraad (telkens met twee personen onafhankelijk). 2. Vraag bankbevestigingen op (saldobrief). 3. Maak lijst klantenvorderingen en leveranciersschulden. 4. Maak lijst lopende contracten en verbintenissen. 5. Schrijf alles over in het inventarisboek.

**Grondslag**: WER art. III.85

### 2. Boek afschrijvingen op vaste activa

Voor elke vaste actief met beperkte levensduur de jaarlijkse afschrijving boeken volgens de gekozen methode (lineair/degressief).

**Waarom?** Matching-beginsel: kost spreiden over levensduur waarin actief bijdraagt.

**🛠️ Hoe**:

1. Lijst alle vaste activa met aanschaffingsdatum en methode. 2. Bereken afschrijving voor het boekjaar (pro rata bij aankoop in lopend boekjaar). 3. Boek: 6300 'Afschrijvingen' (debet) tegen 22.X9 'Afschrijvingen vaste activa' (credit).

> [!example]- Voorbeeld: Naaiatelier Ninove BV bezit machine aangekocht 1/3/2024 voor € 80.000, lineair 10 jaar
> Naaiatelier Ninove BV bezit machine aangekocht 1/3/2024 voor € 80.000, lineair 10 jaar.
>
> 1. **Berekening pro rata 2024** 🧮
>
>    Jaarafschrijving = € 80.000 / 10 = € 8.000
>    Pro rata 2024 (maart-december = 10 maanden) = € 8.000 × 10/12 = **€ 6.667**
>
> 2. **Boeking 31/12/2024** 📝
>
>    | Rekening                          | Debet     | Credit    |
>    |-----------------------------------|----------:|----------:|
>    | 6300 Afschrijvingen MVA           | € 6.667   |           |
>    | 23.X9 Geboekte afschr. MVA        |           | € 6.667   |
>

**Grondslag**: KB-WVV art. 3:39

### 3. Boek waardeverminderingen

Bij waardeverlies (vooral op vorderingen, voorraden, geldbeleggingen) een waardevermindering boeken. Voorzichtigheidsbeginsel: bij ernstige twijfel boeken, niet wachten.

**Waarom?** Maakt de balans actueel — toont schade aan waarde op het moment dat ze ontstaat.

**🛠️ Hoe**:

1. Beoordeel elke vordering op recupereerbaarheid. 2. Voor twijfelachtige debiteuren (faillissement, lange achterstand): waardevermindering 25-100%. 3. Boek: 6340/6360 (debet) tegen 40.9/29.9 (credit).

> [!example]- Voorbeeld: Klant van Meubelzaak Mertens BV failliet — vordering € 12.000
> Klant van Meubelzaak Mertens BV failliet — vordering € 12.000.
>
> 1. **Boeking waardevermindering 100%** 📝
>
>    | Rekening                                        | Debet      | Credit     |
>    |-------------------------------------------------|-----------:|-----------:|
>    | 6340 Waardeverminderingen handelsvorderingen    | € 12.000   |            |
>    | 40.9 Geboekte waardeverminderingen klanten      |            | € 12.000   |
>

**Grondslag**: KB-WVV art. 3:66

### 4. Boek voorzieningen

Voor toekomstige verplichtingen die op balansdatum waarschijnlijk maar nog niet zeker zijn (rechtsgeschil, garantie-verplichtingen, herstructurering): voorziening aanleggen.

**Waarom?** Voorzichtigheidsbeginsel: erkennen wat waarschijnlijk gaat kosten, zelfs als bedrag onzeker is.

**🛠️ Hoe**:

1. Identificeer waarschijnlijke verplichtingen. 2. Schat beste raming. 3. Boek: 6.X (debet) tegen 16.X 'Voorzieningen' (credit).

> [!example]- Voorbeeld: Rotex Roeselare NV verwacht € 150.000 herstructureringskosten in 2025
> Rotex Roeselare NV verwacht € 150.000 herstructureringskosten in 2025.
>
> 1. **Boeking voorziening** 📝
>
>    | Rekening                                        | Debet       | Credit      |
>    |-------------------------------------------------|------------:|------------:|
>    | 6350 Voorz. risico's herstructurering           | € 150.000   |             |
>    | 162 Voorzieningen herstructurering              |             | € 150.000   |
>

**Grondslag**: KB-WVV art. 3:54-3:55

### 5. Boek overlopende rekeningen

Toerekenen van kosten en opbrengsten aan het juiste boekjaar (matching-beginsel). Verleden boekjaar betaald maar betreft volgend jaar → 'over te dragen kosten' op activa. Nog niet betaald maar betreft afgelopen jaar → 'toe te rekenen kosten' op passiva.

**Waarom?** Het resultaat van een boekjaar moet alleen kosten en opbrengsten van dat boekjaar bevatten.

**🛠️ Hoe**:

1. Identificeer betalingen die meerdere boekjaren bestrijken (huur, verzekering, abonnementen). 2. Splits in deel-vorig-jaar en deel-volgend-jaar. 3. Boek 490/491 'Overlopende rekeningen' op de balans.

> [!example]- Voorbeeld: Meubelzaak Mertens BV betaalt op 1/10/2024 een verzekeringspremie € 12.000 die loopt van 1/10/2024 tot 30/9/2025
> Meubelzaak Mertens BV betaalt op 1/10/2024 een verzekeringspremie € 12.000 die loopt van 1/10/2024 tot 30/9/2025.
>
> 1. **Berekening over te dragen kost** 🧮
>
>    Periode 1/10/2024 - 31/12/2024 = 3 maanden = € 12.000 × 3/12 = € 3.000 (boekjaar 2024)
>    Periode 1/1/2025 - 30/9/2025 = 9 maanden = € 12.000 × 9/12 = € 9.000 (boekjaar 2025) → **over te dragen**
>
> 2. **Boeking** 📝
>
>    | Rekening                                | Debet    | Credit   |
>    |-----------------------------------------|---------:|---------:|
>    | 490 Over te dragen kosten               | € 9.000  |          |
>    | 6.X Verzekeringskosten                  |          | € 9.000  |
>

**Grondslag**: KB-WVV art. 3:56-3:57; matching-beginsel

### 6. Voorraad-waardering en herklassering

Op balansdatum de eindvoorraad waarderen volgens de gekozen methode (FIFO, gewogen gemiddelde, individuele identificatie). Resultaat: aanpassen van rekening 6000 'Voorraadwijziging' tegenover voorraadrekening 30/31/32.

**Waarom?** Voorraadwaarde op balans correct krijgen — directe impact op resultaat (waarde stijgt → kost daalt → resultaat hoger).

**🛠️ Hoe**:

1. Tel fysiek de voorraad. 2. Waardeer aan eenheidsprijs volgens gekozen methode. 3. Vergelijk met openingsvoorraad. 4. Boek voorraadwijziging.

**Grondslag**: KB-WVV art. 3:44; voorraadmethodes

### 7. Resultaatverwerking en afsluiting

Sluit alle resultaatrekeningen (klasse 6 en 7) af tegen rekening 14 'Overgedragen resultaat'. Definitieve proef- en saldibalans → vertrekpunt voor balans en RR.

**Waarom?** Boekjaar 'sluiten' — saldi van klasse 6 en 7 worden 0; alleen klasse 1-5 (balansposten) blijven actief voor het volgende boekjaar.

**🛠️ Hoe**:

1. Som alle 6-rekeningen → debet 14 'Resultaatverwerking'. 2. Som alle 7-rekeningen → credit 14. 3. Verschil = winst (credit op 14) of verlies (debet op 14).

**Grondslag**: WER art. III.84; KB-WVV


## Valkuilen

> [!warning]- Vergeet niet de niet-balansrechten en -verplichtingen in de toelichting op te nemen — geen aparte boeking, wel verplichte vermelding (klasse…
> ⚠️ Vergeet niet de niet-balansrechten en -verplichtingen in de toelichting op te nemen — geen aparte boeking, wel verplichte vermelding (klasse 0 + toelichting rubriek IX). ⚖️
>
> _Bron: KB-WVV art. 3:14_


> [!warning]- Het matching-beginsel werkt twee kanten op
> ⚠️ Het matching-beginsel werkt twee kanten op. Niet alleen kosten van volgend jaar overdragen (490) maar ook **opbrengsten** die nog niet ontvangen zijn maar wel het boekjaar betreffen → toe te rekenen opbrengsten (491). ⚖️
>
> _Bron: KB-WVV art. 3:56-3:57_



## Zie ook

- **Vereist kennis van**: [[inventaris]]
- **Vereist kennis van**: [[waarderingsregels-jaarrekening]]
- **Getriggerd door**: [[proef-en-saldibalans]]
- **Wordt voorondersteld in** (1): [[samenstelling-statutaire-jaarrekening]]- **Triggert** (6): [[balans]] · [[inventaris]] · [[jaarrekening]] · [[overlopende-rekeningen]] · [[resultaatverwerking]] · [[resultatenrekening]]
## Bronnen

[^1]: `CBN-0007-04-opmaken-van-de-inventaris__sec_inleiding`
[^2]: `KB-WVV-2019__art_3_57`
[^3]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_in-een-dagboek`
[^4]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_inleiding`
[^5]: `KB-WVV-2019__art_3_55`
