---
title: Rechten en verplichtingen buiten balans
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.R
- 1.1.I.A
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/rechten-verplichtingen-buiten-balans.json
gegenereerd_op: '2026-05-18'
---
# Rechten en verplichtingen buiten balans ⚖️

> [!summary] Korte inhoud
> **Rechten en verplichtingen** die op balansdatum bestaan maar GEEN actief- of passiefbestanddeel vormen in de zin van het KB WVV (geen vermogensbestanddeel met onmiddellijke balansimpact).

> [!info] Behoort tot: [[regelmatige-boekhouding]]

**Rechten en verplichtingen** die op balansdatum bestaan maar GEEN actief- of passiefbestanddeel vormen in de zin van het KB WVV (geen vermogensbestanddeel met onmiddellijke balansimpact). Bv. zekerheden gesteld door of voor derden, persoonlijke borgstellingen, ontvangen of gegeven garanties, termijnovereenkomsten, lopende rechtsgedingen waarvan de uitkomst nog onzeker is, optieovereenkomsten. **MAR klasse 0** voorziet aparte rekeningen; ze verschijnen niet in de balans maar moeten WEL in de toelichting worden vermeld voor de volledigheid van de jaarrekening.

_Bron: MAR klasse 0; KB WVV_


## Bouwstenen

### Klasse 0 — Categorieën ⚖️

(00) Zekerheden door derden gesteld voor rekening van de onderneming, (01) Persoonlijke zekerheden gesteld voor rekening van derden, (02) Zakelijke zekerheden op eigen activa, (03) Ontvangen zekerheden, (04) Goederen en waarden gehouden door derden ten bate van de onderneming, (05) Verplichtingen tot aan- en verkoop van vaste activa, (06) Termijnovereenkomsten, (07) Goederen van derden gehouden door de onderneming, (09) Diverse rechten en verplichtingen.

**Waarom?** Een gestructureerde 'spiegel' van alle waarschijnlijke verplichtingen die ooit de balans kunnen raken. Zonder deze opname zou de jaarrekening misleidend onvolledig zijn.



Transport Tongeren BV heeft een retentierecht ontvangen van haar leasinggever op haar vrachtwagens (waarborg € 45.000) → boeking rekening 03 'Ontvangen zekerheden' € 45.000. Tegelijk heeft de NV haar vrachtwagens als zakelijke zekerheid bij eigen lening → rekening 02 'Zakelijke zekerheden op eigen activa' € 380.000.

_Grondslag: MAR klasse 0_

### Toelichting verplicht ⚖️

Hoewel rekeningen klasse 0 niet in de balans verschijnen, MOETEN de bedragen en aard van rechten/verplichtingen buiten balans verplicht in de **toelichting** bij de jaarrekening worden vermeld (rubriek 13 toelichting van het volledige schema).

**Waarom?** Het volledigheidsbeginsel vereist dat de gebruiker alle relevante verplichtingen ziet — ook als ze nu nog niet op balans staan. Een persoonlijke borg van € 850.000 is een groot signaal voor schuldeisers, ook al staat het 'naast' de balans.



Toelichting Aurelia Holding NV: 'Persoonlijke borgstelling € 850.000 gesteld voor bankkrediet van Brugse Brouwerij BV (verbonden onderneming), looptijd 7 jaar.'

_Grondslag: KB WVV jaarrekeningschema + toelichtingsvereisten_

### Boeking via tegenrekeningen klasse 0 ⚖️

Voor elk recht/verplichting buiten balans worden TWEE rekeningen in klasse 0 gebruikt: één voor het recht/verplichting zelf, één voor de tegenpost. Bv. rekening 010 'Persoonlijke zekerheden voor derden' tegen rekening 011 'Crediteuren'. De saldi compenseren elkaar; klasse 0 staat altijd in evenwicht.

**Waarom?** Symmetrische registratie — hetzelfde principe als dubbel boekhouden — geeft een interne consistentiecheck.



Aurelia Holding NV borgstelling € 850.000: Debet 010 Persoonlijke zekerheden voor rekening van derden € 850.000 / Credit 011 Crediteuren van persoonlijke zekerheden € 850.000.

_Grondslag: MAR klasse 0_

### Migratie naar balans bij realisatie 🤖

Wanneer een recht/verplichting concretiseert (borgsteller wordt aangesproken, optie wordt uitgeoefend, geschil leidt tot vonnis), wordt het bedrag uit klasse 0 verwijderd en als een echte boeking op de balans of in RR opgenomen.

**Waarom?** Klasse 0 is een 'waakkamer'; bij activering moet de transactie volledig in de gewone boekhouding doorlopen.



Brugse Brouwerij BV (dochter van Aurelia) defaultoptreedt; bank roept persoonlijke borg op. Aurelia betaalt € 850.000. Boeking: (a) afboeking klasse 0: Debet 011 / Credit 010 € 850.000. (b) Werkelijke boeking: Debet 416 Vordering op verbonden ondernemingen € 850.000 / Credit 550 Bank € 850.000.

_Grondslag: MAR + algemene boekhoudkundige verwerking_


## In de praktijk

<h3 id="typische-voorbeelden-bij-kmo">Typische voorbeelden bij KMO</h3>

> [!tip]- Typische voorbeelden bij KMO
> Frequent voorkomende posten klasse 0: persoonlijke borgstelling bestuurder voor bedrijfslening, hypothecaire inschrijving op pand voor bankkrediet, ontvangen pand op verkochte goederen, leasingovereenkomsten zonder activering, lopende rechtsgedingen, niet-opgenomen kapitaalverbintenissen (capital commitments). ⚖️

> [!tip]- Herkennen op het examen
> Examen: een bestuurder borg voor 100 % van de lening van zijn BV → onmiddellijk klasse 0 zelfs als boekhoudkundig niet 'gevoeld' tot default.


> [!info]- Niet verwarren met [[voorzieningen]]
> Voorzieningen = passief op de balans (rubriek 16) voor waarschijnlijke verplichting. Klasse 0 = mogelijk recht/verplichting buiten balans, met enkel toelichting. Bij toenemende waarschijnlijkheid + raamebaar bedrag verschuift klasse 0 → voorziening.
>
> _Trigger_: Examen: 'lopende rechtsgeding met 30 % verlieskans, schadebedrag onbekend' → klasse 0 (te onzeker voor voorziening). 'lopende rechtsgeding met 70 % verlieskans, schadebedrag € 75.000' → voorziening 16.


## Valkuilen

> [!warning]- Het feit dat een recht/verplichting niet in de balans staat, betekent NIET dat het irrelevant is
> ⚠️ Het feit dat een recht/verplichting niet in de balans staat, betekent NIET dat het irrelevant is. Een grote persoonlijke borg of een hangend geschil kan economisch significant zijn — toelichtingsplicht voorkomt dat gebruiker misleid wordt. ⚖️
>
> _Bron: CBN 0003/02_


> [!warning]- Onderscheid met voorzieningen (klasse 16): voorziening = waarschijnlijke verplichting die de balans WEL raakt; klasse 0 = recht/verplichting…
> ⚠️ Onderscheid met voorzieningen (klasse 16): voorziening = waarschijnlijke verplichting die de balans WEL raakt; klasse 0 = recht/verplichting die de balans (nog) NIET raakt. Bij stijgende waarschijnlijkheid kantelt klasse 0 → voorziening. 🤖
>
> _Bron: CBN 0003/02 + CBN 2018/25_



## Voorbeelden

Aurelia Holding NV heeft op 31/12 een persoonlijke borgstelling gegeven voor een bankkrediet van € 850.000 verleend aan dochter Brugse Brouwerij BV. Geen balanspost — dochter blijft hoofdschuldenaar — MAAR opname op rekening 010 'Persoonlijke zekerheden gesteld voor rekening van derden' € 850.000. In toelichting: aard, ontvanger, bedrag, looptijd. Bij niet-betaling door dochter: omzetting in werkelijke verplichting en boeking op rekening 49 + klasse 65.

## Bronnen

[^1]: `MAR-ondernemingen__art_0_part1`
[^2]: `CBN-0003-02-niet-in-de-balans-opgenomen-rechten-en-verplichtingen__sec_top_part1`
