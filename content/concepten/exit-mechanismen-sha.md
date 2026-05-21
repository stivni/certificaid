---
title: Exit- en deadlock-mechanismen in aandeelhoudersovereenkomsten
tags:
- concept
- cluster
- po-3-0
linked_anchors:
- 3.0.VI
- 3.0.VI.A
- 3.0.VI.D
programmaonderdelen:
- '3.0'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/exit-mechanismen-sha.json
gegenereerd_op: '2026-05-21'
---
# Exit- en deadlock-mechanismen in aandeelhoudersovereenkomsten ⚖️

Een aandeelhoudersovereenkomst is doorgaans voor lange duur (10 jaar of meer). Aandeelhouders willen weten **hoe ze eruit kunnen** wanneer de samenwerking eindigt, een aandeelhouder uitvalt, of partijen elkaar blokkeren. **Exit-mechanismen** geven vooraf overeengekomen routes om **uit elkaar te gaan** — zonder rechterlijke procedure.

> [!summary] Korte inhoud
> Verzamelterm voor **contractuele clausules** die de **uitstap** van een aandeelhouder of de **ontbinding van een patstelling** (deadlock) regelen: **put- en callopties**, **Russian roulette**, **Texas shoot-out**, **good/bad leaver-regelingen** en **deadlock-resolutie**.

> [!info] Behoort tot: [[aandeelhoudersovereenkomst]]

Verzamelterm voor **contractuele clausules** die de **uitstap** van een aandeelhouder of de **ontbinding van een patstelling** (deadlock) regelen: **put- en callopties**, **Russian roulette**, **Texas shoot-out**, **good/bad leaver-regelingen** en **deadlock-resolutie**. Doel: een onderhandelde, voorspelbare uitstap mogelijk maken zonder te moeten teruggrijpen naar een **gerechtelijke uittreding** (art. 2:60 WVV voor de BV; ook ontbinding wegens gegronde redenen).

_Bron: IBA SHA-Guide 2024 §8, §11, §13_



## Bouwstenen

### Putoptie ⚖️

Recht — niet verplichting — voor de **begunstigde** om een bepaald aantal aandelen **te verkopen** tegen een vooraf bepaalde prijs of formule, binnen een vastgesteld tijdvenster. Typisch gebruikt door een **minderheid** of **co-investeerder** als exit-garantie.

**Waarom?** Geeft de minderheid **zekerheid van liquiditeit** — een 'put' op de meerderheid betekent dat de meerderheid bij uitoefening **moet kopen**.




_Grondslag: IBA SHA-Guide 2024 §8_

### Calloptie ⚖️

Recht — niet verplichting — voor de **begunstigde** om een bepaald aantal aandelen **te kopen** tegen een vooraf bepaalde prijs of formule, binnen een vastgesteld tijdvenster. Typisch gebruikt door de **meerderheid** om bij bv. een **bad leaver** de aandelen van de uitvaller op te nemen.

**Waarom?** Voorkomt dat een **uitvaller** (ex-bestuurder, ex-werknemer-aandeelhouder, …) passief aandeelhouder blijft zonder bijdrage aan de vennootschap.




_Grondslag: IBA SHA-Guide 2024 §8_

### Good leaver / bad leaver ⚖️

Regelt het **vertrek van een aandeelhouder-medewerker** met onderscheid in **waardering**: een **good leaver** (overlijden, ziekte, pensioen, niet-verwijtbaar einde van mandaat) krijgt de aandelen aan **fair value** of **marktwaarde**; een **bad leaver** (fraude, schending non-concurrence, ontslag om dringende reden) krijgt slechts **boekwaarde** of een sterk gediscounteerde waarde.

**Waarom?** Maakt het mogelijk om **management** aandeelhouder te maken zonder het risico dat de vennootschap belast blijft met een toxische ex-medewerker als aandeelhouder.


**In de praktijk**: Cruciaal in **management buy-out** en **stock-option plannen** — vaak de meest onderhandelde clausule in SHA's.


_Grondslag: IBA SHA-Guide 2024 §8_

### Russian roulette ⚖️

Patstelling-mechanisme tussen **twee partijen**: aandeelhouder A biedt een **prijs per aandeel** aan. B moet kiezen: **kopen** aan die prijs of **verkopen** aan dezelfde prijs. Wie het bod doet weet niet wie er uiteindelijk eigenaar blijft.

**Waarom?** Dwingt A om een **eerlijke prijs** voor te stellen — als hij te laag biedt, verliest hij zelf zijn aandelen aan die prijs.


**In de praktijk**: Werkt vooral bij **50/50-partners** met **gelijkwaardige financiële slagkracht**. Werkt minder goed wanneer één partij veel rijker is — die kan dan altijd kopen.


_Grondslag: IBA SHA-Guide 2024 §13 (exit clausules bij patstelling)_

### Texas shoot-out ⚖️

Variant op Russian roulette: bij deadlock dienen **beide partijen** een **verzegeld bod** in (sealed bid) op de aandelen van de andere. Het **hoogste bod** wint — die partij wordt enige aandeelhouder en koopt de andere uit aan zijn bod-prijs.

**Waarom?** Brengt **maximale prijs-onthulling** — beide partijen tonen wat ze écht willen betalen voor 100% controle.




_Grondslag: IBA SHA-Guide 2024 §13_

### Deadlock-resolutie via mediation/arbitrage ⚖️

Niet alle deadlocks vereisen een **exit**. Vaak voorziet de SHA eerst een **escalatieladder**: (1) **interne escalatie** naar CEO's of voorzitters; (2) **mediation** door een onafhankelijke derde; (3) **bindende arbitrage**; (4) pas als laatste redmiddel: uitkoop via Russian roulette / Texas shoot-out / gerechtelijke uittreding.

**Waarom?** Een **exit** is destructief voor de vennootschap (verlies van expertise, kapitaal); een onderhandelde oplossing behoudt de going concern.




_Grondslag: IBA SHA-Guide 2024 §13_


## In de praktijk

<h3 id="waardering-bij-exit">Waardering bij exit</h3>

> [!tip]- Waardering bij exit
> De **prijs** bij exit-uitoefening is het meest betwiste element. Vaste formules (boekwaarde, EBITDA-multiple, DCF) bieden **rechtszekerheid** maar zijn rigide; **onafhankelijke deskundige** biedt flexibiliteit maar opent risico op betwisting. Vaak combineert de SHA beide: **formule als startpunt**, deskundige bij geschil. ⚖️

<h3 id="verhouding-tot-gerechtelijke-uittreding">Verhouding tot gerechtelijke uittreding</h3>

> [!tip]- Verhouding tot gerechtelijke uittreding
> Naast contractuele exits bestaat altijd de **gerechtelijke uittreding** (art. 2:60 WVV — uitsluiting; art. 2:63 — uittreding wegens gegronde redenen). Maar dat is **traag, openbaar en duur**. Een goed ontworpen SHA-exit voorkomt die route. ⚖️


## Valkuilen

> [!warning]- Een **Russian roulette** in een SHA tussen twee partijen met **zeer ongelijke financiële slagkracht** geeft de rijke partij een **structureel voordeel**: zij kan altijd het 'fair' bod doen en kopen, terwijl de armere partij niet kan kopen en dus verplicht verkoopt. Bij dergelijke onbalans → kies eerder voor onafhankelijke deskundige + put/call.
> ⚠️  🔗


> [!warning]- Definieer good/bad-leaver-events **uitputtend en objectief**. Vage termen als 'ernstig disfunctioneren' leiden tot **eindeloze betwistingen** op het moment dat de waardering moet vastgesteld worden.
> ⚠️  🔗



## Zie ook

- **Triggert** (1): [[deadlock-vennootschap]]
> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IBA-SHA-Belgium-2024-NL__sec_8-welke-mechanismen-staan-het-belgische-recht-toe-voor-de-re`
[^2]: `IBA-SHA-Belgium-2024-NL__sec_11-welke-inhoud-bevatten-aandeelhoudersovereenkomsten-in-be`
