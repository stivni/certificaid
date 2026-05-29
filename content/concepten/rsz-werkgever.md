---
title: "RSZ-werkgever"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/rsz-werkgever.json"
---

_Regime_ · ook: sociale zekerheidsbijdragen werkgever · patronale RSZ · werkgeversbijdragen

## Definitie

De RSZ-werkgeversbijdrage is de patronale sociale-zekerheidsbijdrage die de werkgever bovenop het brutoloon van zijn werknemer aan de Rijksdienst voor Sociale Zekerheid (RSZ) stort. Het is een wettelijke werkgeverskost — niet ingehouden op het loon van de werknemer maar als aparte kost gedragen door de werkgever. De basisbijdrage bedraagt ongeveer 25 % van het brutoloon (cijfer 2026), met sectorvariatie via aanvullende bijdragen (vakantiegeld arbeiders, fonds voor bestaanszekerheid, beroepsziekten, arbeidsongevallen, ...). Op die basis worden verminderingen toegepast: structurele (lage lonen, ondernemingsstart) en doelgroep-gerichte (oudere werknemers, eerste aanwervingen, langdurig werkzoekenden).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28) · CBN-advies 2018/13 — _advies_</small>

## Substantie

Economisch betekent de RSZ-werkgeversbijdrage dat de totale loonkost voor de werkgever aanzienlijk hoger ligt dan het brutoloon van de werknemer. Een werknemer met 3.000 EUR brutoloon kost de werkgever ongeveer 3.750 EUR (3.000 × 1,25) — vóór maaltijdcheques, GSM, verzekeringen en andere voordelen. Boekhoudkundig wordt de bijdrage geboekt op rekeningklasse 62 (bezoldigingen, sociale lasten en pensioenen) — meer bepaald in subrekening 621 (Werkgeversbijdragen voor sociale verzekeringen) — tegenover een schuld op klasse 454 (RSZ). De RSZ-verminderingen die de werkgever krijgt (lettercodes per werknemer in de DMFA-aangifte) verminderen die kost — die financiële voordelen worden in de sociale balans afzonderlijk gerapporteerd.

<small>🔗 CBN-advies S100 — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De RSZ-werkgeversbijdrage financiert de Belgische sociale zekerheid (werkloosheid, pensioenen, ziekteverzekering, kinderbijslag, arbeidsongevallen, beroepsziekten). De keuze om die financiering deels via een werkgeverslast te organiseren (en niet uitsluitend via inhouding op het loon) maakt de bruto-netto-spreiding minder pijnlijk voor de werknemer en spreidt het financieringseffort. De verminderingen sturen tewerkstellingsbeleid bij: lage lonen blijven aantrekkelijk om aan te werven (structurele vermindering), specifieke doelgroepen (oudere werknemers, jongeren) worden geholpen tegen langdurige werkloosheid.

<small>🤖 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2026-01-01**

Basisbijdrage en verminderingen blijven structureel ~25 % voor 2026. Tarieven en plafonds van verminderingen jaarlijks geïndexeerd — exacte bedragen via RSZ-instructies en Cijferzakboekje.

**✅ Voor**
- 📖 Elke werkgever die werknemers tewerkstelt met een arbeidsovereenkomst onderworpen aan de Belgische sociale zekerheid (DIMONA-aangifte bij de RSZ).

**🚫 Niet voor**
- 🔗 Bestuurders en zaakvoerders zonder dienstverband — die zijn zelfstandigen (RSZ-zelfstandigen, ander stelsel). Uitzendkrachten worden door het uitzendkantoor afgedragen, niet door de gebruiker.

**👍 Voordeel**
- 🔗 Verminderingen verlagen de effectieve loonkost — structurele vermindering voor lage lonen kan oplopen tot enkele honderden EUR per kwartaal per werknemer; doelgroep-verminderingen (eerste aanwerving, oudere werknemers, jongeren) zijn nog substantiëler en kunnen jarenlang lopen.

**⚠️ Risico**
- 🔗 Vergeten RSZ-bijdragen op extra-legale voordelen die toch onderworpen zijn (bv. bonus, eindejaarspremie). De RSZ controleert via DMFA-aangiften en kan met terugwerkende kracht navorderen plus bijdrageopslag opleggen. Boekhoudkundig: een verschil tussen de geboekte 621-kost en de werkelijk afgedragen RSZ-bedragen wijst op een fout in de loonadministratie.

## Bouwstenen

### 📏 Basisbijdrage ~25 %

Op het volledige brutoloon van de werknemer betaalt de werkgever een patronale basisbijdrage van ongeveer 25 % (cijfer 2026, sector-afhankelijk). Het percentage omvat de patronale sociale-zekerheidsbijdrage stricto sensu (~19,88 %) plus loonmatigingsbijdrage en aanvullende bijdragen — exacte sectorpercentages via paritair comité.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Structurele vermindering lage lonen

Werkgevers krijgen een forfaitaire vermindering van werkgeversbijdragen voor werknemers met een laag of middelmatig refertekwartaalloon. De vermindering wordt automatisch berekend per kwartaal in functie van het kwartaalloon (S) — onder een onderste drempel: een vast forfaitair bedrag; tussen de drempels: een degressieve formule; boven de bovenste drempel: geen vermindering meer. Bestaat sinds de 'structurele vermindering' van 2004 en wordt regelmatig hervormd.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Doelgroep-verminderingen

Naast de structurele vermindering bestaan doelgroep-verminderingen: oudere werknemers (vanaf bepaalde leeftijdsgrens, vaak vanaf 58 of 60 jaar — gewest-afhankelijk sinds bevoegdheidsoverdracht in 2014), jongeren (laaggeschoolde jongeren <26 jaar), langdurig werkzoekenden, eerste aanwervingen (KMO — voor de eerste vijf werknemers verminderde bijdragen, vooral voor de eerste werknemer kan dit volledig vrijstelling zijn voor onbeperkte duur). Sinds de zesde staatshervorming zijn deze maatregelen sterk regio-afhankelijk: Vlaanderen, Wallonië en Brussel hebben eigen accenten.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Bijzondere bijdrage betaald verlof (arbeiders)

Voor arbeiders betaalt de werkgever het vakantiegeld niet rechtstreeks, maar via een bijzondere RSZ-bijdrage (~10,27 % bovenop het loon, plus ~5,57 % als jaarbijdrage in december) die wordt doorgestort aan de Rijksdienst voor Jaarlijkse Vakantie (RJV). Die instantie betaalt vervolgens vakantiegeld aan de arbeider. Voor bedienden geldt dit niet: hun werkgever betaalt vakantiegeld zelf en boekt provisie 456 'Vakantiegeld' op balansdatum voor reeds opgebouwde aanspraken.

<small>🔗 CBN-advies 2018/13 — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Formule loonkost werkgever

Loonkost = Brutoloon × (1 + p_basis) − verminderingen + aanvullende bijdragen. Waarbij p_basis ≈ 25 %; verminderingen = structureel + doelgroep; aanvullende bijdragen = sectorbijdragen (bedrijfsziekten, arbeidsongevallen-premie via private verzekeraar, fonds bestaanszekerheid, vakantiebijdrage arbeiders).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Boekhoudkundige verwerking

De werkgeversbijdrage wordt geboekt als kost op subrekening 621 'Werkgeversbijdragen voor sociale verzekeringen' tegenover schuld 454 'Rijksdienst voor Sociale Zekerheid'. Bij betaling: debiteer 454, crediteer 55 (bank). Verminderingen worden in mindering geboekt op 621 (per kwartaal in de DMFA-saldo), niet als opbrengst. De maandelijkse provisie volgt het matchingsprincipe — kosten aan het boekjaar waarin de prestaties zijn verricht (art. 33 KB WVV uitvoering).

<small>🔗 CBN-advies 2018/13 — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Loonkost bediende met brutoloon 3.000 EUR/maand
> _Zelena Bio NV heeft één bediende, Jonas. Brutoloon: 3.000 EUR/maand. Geen doelgroep-vermindering van toepassing. Structurele vermindering verwaarloosbaar (loon > middelmatig)._
>
> **Berekening:**
>
> - Stap 1 — Brutoloon Jonas = 3.000 EUR
> - Stap 2 — RSZ-werkgever = 3.000 × 25 % = 750 EUR
> - Stap 3 — Maandkost RSZ = 750 EUR; jaarlijks ~9.000 EUR (excl. vakantiegeld, eindejaar)
> - Stap 4 — Voor de werkgever totale loonkost vóór andere voordelen = 3.000 + 750 = 3.750 EUR/maand
>
> → **Resultaat**: Jonas kost zijn werkgever ongeveer 25 % méér dan zijn brutoloon — vóór vakantiegeld, eindejaarspremie en extralegale voordelen.
>
> **📒 Maandelijkse boeking loon Jonas (vereenvoudigd)**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 620 — Bezoldigingen en rechtstreekse sociale voordelen | 3.000 |  |
> | 621 — Werkgeversbijdragen sociale verzekeringen | 750 |  |
> | 454 — RSZ |  | 750 |
> | 455 — Bezoldigingen |  | 2.608 |
> | 453 — Ingehouden voorheffingen |  | 392 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- RSZ-vermindering boeken als opbrengst
> **Verkeerde assumptie**: Studenten boeken de structurele RSZ-vermindering soms als opbrengst (klasse 74).
>
> **Kernpunt**: RSZ-verminderingen verlagen de werkgeversbijdrage zelf — ze worden in mindering geboekt op rekening 621, niet als opbrengst. Dit is consistent met de sociale-balans-rapportering waar de vermindering als 'financieel voordeel' verschijnt — niet als opbrengst-post.
>
> <small>🔗 CBN-advies S100 — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Exact 25 % vasthouden in een berekening
> **Verkeerde assumptie**: Het percentage 25 % als 'het' RSZ-werkgeverstarief gebruiken in alle berekeningen.
>
> **Kernpunt**: 25 % is een vuistregel — het effectief percentage hangt af van sector (arbeiders/bedienden), grootte van de onderneming (loonmatigingsbijdrage), structurele vermindering en doelgroep-verminderingen. Bij het examen: het Cijferzakboekje raadplegen voor het werkbare basispercentage en checken welke verminderingen van toepassing kunnen zijn.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vakantiegeld arbeiders en bedienden gelijk behandelen
> **Verkeerde assumptie**: Voor zowel arbeiders als bedienden 'gewoon' een provisie 456 boeken op balansdatum.
>
> **Kernpunt**: Voor bedienden in vast dienstverband: ja, provisie 456 voor opgebouwd vakantiegeld (CBN 2018/13). Voor arbeiders: NEE — de werkgever betaalt geen rechtstreeks vakantiegeld maar bijzondere RSZ-bijdrage aan de RJV; geen provisie 456, want de RJV betaalt vakantiegeld. De bijzondere bijdrage is al in 621 verwerkt op het moment dat het loon werd betaald.
>
> <small>🔗 CBN-advies 2018/13 — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever-onderneming (KMO of grote werkgever)

_De accountant die de payroll en boekhouding van een werkgever-cliënt verzorgt._

#### 📒 Boekhouder

##### 👣 Maandelijkse RSZ-boekingen + kwartaalsaldo

Per maand: 621 (D) tegenover 454 (C) voor de berekende werkgeversbijdrage. Per kwartaal afpunten met de DMFA-aangifte: de RSZ-applicatie levert het kwartaalsaldo inclusief verminderingen — controleer dat 454 overeenstemt met dat saldo. Bij verschillen: nakijken of structurele vermindering correct mee is berekend, of een doelgroep-vermindering die ondertussen is afgelopen toch nog in de boeking zat.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Jaarafsluit — sociale balans + provisie vakantiegeld

Op balansdatum: (1) provisie vakantiegeld bedienden op rekening 456 voor opgebouwde aanspraken die in volgend jaar uitbetaald worden (CBN 2018/13); (2) sociale balans invullen met DIMONA-werknemers per categorie + financieel voordeel = totaal RSZ-verminderingen per maatregel.

<small>📖 CBN-advies 2018/13 — _advies_ · CBN-advies S100 — _advies_ · KB WVV uitvoering — art. 5:4 — _kb_</small>

#### 🧭 Adviseur

##### 🧭 Doelgroep-vermindering-scan bij aanwerving

Bij elke nieuwe aanwerving van een cliënt: checken of een doelgroep-vermindering van toepassing is (eerste aanwerving KMO — voor de eerste werknemer is vaak een ruime vrijstelling beschikbaar; jonge werknemer; oudere werknemer; langdurig werkzoekende uit een gewestelijk programma). De besparing kan oplopen tot vele duizenden EUR per jaar — een gemiste vermindering is een directe vermogensschade voor de cliënt.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Sociaal passief eenheidsstatuut (VenB-vrijstelling)

Bij werknemers die minstens 5 dienstjaren na 1-1-2014 in dienst zijn: in VenB-aangifte vrijstelling sociaal passief opnemen (art. 67quater WIB92, code 1607). Drie weken bezoldiging vrij te stellen per werknemer vanaf het 6de tot het 20ste dienstjaar; één week vanaf het 21ste. Maximum bezoldigingsbasis = 100 % op 0–1.500 EUR + 30 % op 1.500–2.600 EUR. Gespreid over 5 boekjaren (20 % per jaar). Verplichte nominatieve lijst via Belcotax-on-Web.

<small>📖 WIB92 — art. 67quater — _wettekst_ · KB/WIB92 — art. 46ter — _kb_ · KB/WIB92 — art. 46quater — _kb_ · aangifte-VenB-2025-afzonderlijke-aanslagen — _aangifte_</small>

## Verder lezen (scope-out)

- → Loon-en-payroll K-techniek (cascade-context) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Werknemers-vergoedingen Σ (alternatieven) → [[werknemers-vergoedingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[loon-en-payroll]]
### `vergelijkbaar_met`
- [[rsz-werknemer]]
    - **Gelijkenissen**:
        - Beide zijn sociale-zekerheidsbijdragen op het brutoloon
        - Beide worden afgedragen aan de RSZ via DMFA-aangifte
        - Beide financieren de Belgische sociale zekerheid
    - **Verschillen**:
        - Werkgeversbijdrage (~25 %) is een werkgeverskost — boven op het brutoloon — niet ingehouden
        - Werknemersbijdrage (13,07 %) is ingehouden op het brutoloon — verlaagt het netto-loon
        - Werkgeverskant kent ruime verminderingen (structureel + doelgroep); werknemerskant alleen werkbonus voor lage lonen
    - ⚠️ **Verwarringsrisico**: Studenten verwarren beide soms, vooral bij berekening van de totale loonkost — pas op: 'RSZ' op een loonfiche kan zowel werknemers- als werkgeversaandeel betekenen.
### `triggert`
- [[werkbonus]] — Lage lonen activeren naast de RSZ-werkgeverskant ook de werkbonus aan werknemerskant.
