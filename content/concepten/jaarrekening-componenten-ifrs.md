---
title: Componenten van een IFRS-jaarrekening
tags:
- concept
- begrip
- po-1-5
linked_anchors:
- 1.5.IV.B
- 1.5.IV
- 1.5.taak.1
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/jaarrekening-componenten-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Componenten van een IFRS-jaarrekening ⚖️

> [!summary] Korte inhoud
> Onder IAS 1 — Presentatie van de jaarrekening bestaat een volledige IFRS-jaarrekening uit **vijf vaste componenten**: (1) een overzicht van de financiële positie aan het eind van de periode (de 'IFRS-balans'); (2) een overzicht van het totaalresultaat over de periode (winst of ve….

> [!info] Bestaat uit (5): [[balans-presentatie-ifrs]] · [[mutatieoverzicht-eigen-vermogen-ifrs]] · [[presentatiebeginselen-jaarrekening-ifrs]] · [[toelichtingsvereisten-jaarrekening-ifrs]] · [[totaalresultaat-ifrs]]

Onder IAS 1 — Presentatie van de jaarrekening bestaat een volledige IFRS-jaarrekening uit **vijf vaste componenten**: (1) een overzicht van de financiële positie aan het eind van de periode (de 'IFRS-balans'); (2) een overzicht van het totaalresultaat over de periode (winst of verlies + overige onderdelen van het totaalresultaat, samen of in twee afzonderlijke overzichten); (3) een mutatieoverzicht van het eigen vermogen; (4) een kasstroomoverzicht (vereisten in IAS 7); en (5) de toelichting met grondslagen voor financiële verslaggeving en andere materiële informatie. Daarbij hoort verplicht vergelijkende informatie over de voorgaande periode, en in specifieke gevallen (eerste IFRS-toepassing, retroactieve aanpassing, herclassificatie) ook een derde balans (openingsbalans van de vergelijkende periode). De entiteit mag andere namen gebruiken voor de overzichten — bv. 'overzicht van gerealiseerde en niet-gerealiseerde resultaten' in plaats van 'overzicht van het totaalresultaat'.

_Bron: IAS 1 alinea 10_


## Bouwstenen

### Overzicht financiële positie (IFRS-balans) ⚖️

De IFRS-balans toont activa, verplichtingen en eigen vermogen op één tijdstip. Activa en verplichtingen worden gesplitst in **vlottend** (current — gebruikt of vereffend binnen 12 maanden of bedrijfscyclus) en **niet-vlottend** (non-current). Een entiteit mag van deze splitsing afwijken naar een **liquiditeitsvolgorde** indien dat een betrouwbaarder en relevanter beeld geeft (bv. financiële instellingen).

**Waarom?** De vlottend/niet-vlottend-splitsing geeft gebruikers meteen inzicht in liquiditeitsrisico en kapitaalstructuur. Voor banken is die splitsing weinig zinvol — vandaar de afwijking.



Zelena Bio NV (productiebedrijf) volgt de vlottend/niet-vlottend-splitsing. Een buitenlandse bankdochter binnen de Zelena Bio Groep zou de liquiditeitsvolgorde aanhouden in haar lokale rapportering.

_Grondslag: IAS 1 alinea 54 + 60_

### Overzicht totaalresultaat ⚖️

Twee onderdelen: **winst of verlies** (de klassieke W&V-rekening) + **overige onderdelen van het totaalresultaat** (Other Comprehensive Income, OCI). OCI omvat zaken die IFRS bewust buiten het resultaat houdt: herwaarderingsreserves (IAS 16, IAS 38), actuariële herwaarderingen pensioenen (IAS 19), wisselkoersverschillen uit omrekening buitenlandse activiteit (IAS 21), reële-waardewijzigingen voor eigen-vermogensinstrumenten (IFRS 9), kasstroom-hedge-effectieve deel (IFRS 9), etc. De entiteit mag één enkel overzicht presenteren of twee afzonderlijke (eerst W&V, daarna totaalresultaat).

**Waarom?** Sommige waarde-mutaties hebben niets met de gewone bedrijfsuitoefening te maken (herwaardering vastgoed; wisselkoersverschil op buitenlandse dochter). Ze meteen in winst of verlies opnemen zou het resultaat onvergelijkbaar maken. OCI parkeert ze tot ze definitief gerealiseerd of geherclassificeerd worden.



Zelena Bio NV behaalt in 2026 een winst van € 35.000.000 (uit verkoop biofarmaceutische producten). Daarnaast OCI: herwaardering productieterrein +€ 4.500.000 (Zelena past het herwaarderingsmodel toe op terreinen — IAS 16 alinea 31). Totaalresultaat = € 39.500.000.

_Grondslag: IAS 1 alinea 10A + 81A + 82A_

### Mutatieoverzicht eigen vermogen ⚖️

Verzoeningsschema: beginsaldo per categorie eigen vermogen (kapitaal, agio, herwaarderingsreserve, hedge-reserve, ingehouden winsten, ...) → totaalresultaat → transacties met eigenaars (dividenden, kapitaalverhoging, terugkoop eigen aandelen) → eindsaldo.

**Waarom?** Eigen vermogen is geen monoliet. Gebruikers willen zien hoeveel van de verandering komt uit operationele winst, hoeveel uit OCI, hoeveel uit dividenden of kapitaaltransacties.



Zelena Bio NV: ingehouden winsten 1 januari 2026 € 95.000.000 + winst 2026 € 35.000.000 − dividend 2026 −€ 15.000.000 = € 115.000.000 ingehouden winsten 31 december 2026. Apart kolom voor herwaarderingsreserve toont de OCI-toevoeging € 4.500.000.

_Grondslag: IAS 1 alinea 106_

### Kasstroomoverzicht (IAS 7) ⚖️

Splitsing van geldstromen in drie categorieën: **operationeel** (uit bedrijfsuitoefening, direct of indirect gepresenteerd), **investeringsactiviteiten** (verwerving/vervreemding activa) en **financieringsactiviteiten** (kapitaal, schulden). De vereisten zelf staan in IAS 7, niet in IAS 1.

**Waarom?** De W&V-rekening werkt op toerekeningsbasis (accruals), dus weerspiegelt niet de cash-realiteit. Het kasstroomoverzicht voegt de cash-laag toe.



Zelena Bio NV: operationele cashflow 2026 = € 42.000.000 (winst € 35M + afschrijvingen € 12M − werkkapitaalstijging −€ 5M); investeringscashflow = −€ 28.000.000 (CAPEX in nieuwe productielijn); financieringscashflow = −€ 8.000.000 (dividend + aflossing obligaties).

_Grondslag: IAS 1 alinea 10(d) + IAS 7_

### Toelichting ⚖️

Bevat de grondslagen voor financiële verslaggeving (welke IFRS-keuzes — kostprijsmodel vs. herwaarderingsmodel, FIFO vs. gewogen gemiddelde, ...) plus alle door specifieke IFRS-en vereiste toelichtingsnota's (segmentinformatie onder IFRS 8, financiële-instrumentenrisico onder IFRS 7, leasing onder IFRS 16, opbrengsten-uitsplitsing onder IFRS 15, etc.).

**Waarom?** Cijfers krijgen pas betekenis met context. IFRS bevat veel keuze-momenten; gebruikers moeten weten welke keuze de entiteit maakte om vergelijkingen te kunnen maken.



Zelena Bio's toelichting vermeldt: 'Materiële vaste activa: kostprijsmodel (IAS 16 alinea 30), behalve terreinen die volgens het herwaarderingsmodel worden gewaardeerd (IAS 16 alinea 31).' Een lezer weet meteen waarom de terreinen schommelen in waarde.

_Grondslag: IAS 1 alinea 7 + 117_


## In de praktijk

<h3 id="drie-balansen-bij-eerste-ifrs-toepassing-of-retroactieve-aanpassing">Drie balansen bij eerste IFRS-toepassing of retroactieve aanpassing</h3>

> [!tip]- Drie balansen bij eerste IFRS-toepassing of retroactieve aanpassing
> Een entiteit moet drie balansen presenteren (huidig jaareinde + vorig jaareinde + begin vorig jaar) wanneer: (a) zij voor het eerst IFRS toepast (IFRS 1); of (b) zij een grondslag retroactief wijzigt of een fout corrigeert met materieel effect (IAS 1 alinea 40A). In gewone jaren volstaan twee balansen. ⚖️

> [!tip]- Herkennen op het examen
> Bij eerste IFRS-jaarrekening van Zelena Bio voor boekjaar 2027: balans 31 december 2027 + 31 december 2026 + **1 januari 2026** (openingsdatum vergelijkende periode).

<h3 id="geen-voorgeschreven-vorm-wel-verplichte-minimumposten">Geen voorgeschreven vorm — wel verplichte minimumposten</h3>

> [!tip]- Geen voorgeschreven vorm — wel verplichte minimumposten
> IAS 1 schrijft geen vast jaarrekeningmodel voor zoals KB WVV doet. Wél een lijst minimum-posten die op de balans (alinea 54) en in het overzicht totaalresultaat (alinea 82) moeten verschijnen. De volgorde, naam en groepering staan vrij — mits getrouw beeld. ⚖️


> [!info]- Niet verwarren met [[samenstelling-statutaire-jaarrekening]]
> Belgische statutaire jaarrekening (KB WVV) heeft een **vast voorgeschreven schema** met letter-cijfer-codes (II.A, II.B, ...). IFRS-jaarrekening volgens IAS 1 heeft geen vast schema — wel een minimumlijst posten (alinea 54 en 82). IFRS verplicht expliciet vijf componenten; KB WVV vereist standaard drie (balans + W&V + toelichting).
>
> _Trigger_: Bij vraag 'Welke vorm heeft de jaarrekening van een beursgenoteerde NV?': onderscheid maken tussen enkelvoudige (BE-GAAP-schema) en geconsolideerde (IAS 1).


## Valkuilen

> [!warning]- Het mutatieoverzicht eigen vermogen is geen optie maar een **verplichte** component (alinea 10(c))
> ⚠️ Het mutatieoverzicht eigen vermogen is geen optie maar een **verplichte** component (alinea 10(c)). Stagiairs vergeten dit vaak omdat KB WVV geen vergelijkbare verplichting kent voor de enkelvoudige jaarrekening. ⚖️
>
> _Bron: IAS 1 alinea 10(c)_


> [!warning]- OCI ≠ winst of verlies
> ⚠️ OCI ≠ winst of verlies. Een entiteit mag **niet** OCI-posten als opbrengsten of kosten in winst of verlies opnemen — dat zou dubbeltelling zijn. Hereclassificatie naar W&V gebeurt enkel bij specifieke gebeurtenissen (bv. realisatie hedge, vervreemding buitenlandse activiteit). ⚖️
>
> _Bron: IAS 1 alinea 7 (definitie OCI)_



## Zie ook

- **Wordt voorondersteld in** (1): [[ifrs-eerste-toepassing]]
## Voorbeelden

De geconsolideerde IFRS-jaarrekening 2027 van Zelena Bio NV (eerste IFRS-jaar) bevat: (1) overzicht financiële positie per 31 december 2027 + per 31 december 2026; (2) overzicht totaalresultaat 2027 + 2026; (3) mutatieoverzicht eigen vermogen 2027 + 2026; (4) kasstroomoverzicht 2027 + 2026; (5) toelichting met grondslagen, segment-informatie, leasing-uitsplitsing, etc. Omdat 2027 het eerste IFRS-jaar is, hoort er ook een derde balans bij — de openingsbalans per 1 januari 2026 (overgangsdatum, IFRS 1).

## Bronnen

[^1]: `IAS-1-presentatie-van-de-jaarrekening__sec_jaarrekening`
[^2]: `IAS-1-presentatie-van-de-jaarrekening__sec_10a`
[^3]: `IAS-1-presentatie-van-de-jaarrekening__sec_definities`
[^4]: `IAS-1-presentatie-van-de-jaarrekening__sec_40a`
