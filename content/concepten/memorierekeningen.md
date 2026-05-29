---
title: "Memorierekeningen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.R
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/memorierekeningen.json"
---

_Balanspost_ · ook: niet in de balans opgenomen rechten en verplichtingen · klasse 0 · off-balance-rekeningen

## Definitie

**Memorierekeningen** zijn rekeningen van de **MAR-klasse 0** waarop rechten en verplichtingen worden bijgehouden die het vermogen, de financiële positie of het resultaat van de onderneming **aanmerkelijk kunnen beïnvloeden** maar die **niet in de balans** worden opgenomen omdat ze (nog) geen actuele activa of passiva vormen. Voorbeelden: gestelde of ontvangen garanties, persoonlijke en zakelijke zekerheden, niet-uitgeoefende aankoopopties bij operationele leasing, eventuele restschulden, niet-opgenomen kredietlijnen, retro-cessies. Klasse 0 functioneert als **memorie** of geheugen — daadwerkelijke vermogensverschuiving leidt tot reguliere boeking op klassen 1-9.

<small>📖 KB 21-10-2018 — Bijlage 1 MAR — Klasse 0 (29) (30) — _kb_ · CBN-advies 2017/07 — Boeking van rechten en verplichtingen onder klasse 0 — _cbn_</small>

## Substantie

De **klasse 0** is **dubbelzijdig**: elke memoriële boeking wordt op **twee tegengestelde 0-rekeningen** opgenomen — debet 09x recht/verbintenis · credit 09y tegenboeking, of omgekeerd. Sub-categorieën:

- **00** Zekerheden door derden gesteld voor rekening van de onderneming
- **01** Persoonlijke zekerheden door de onderneming gesteld voor derden
- **02** Zakelijke zekerheden door de onderneming gesteld op haar eigen activa
- **03** Goederen en waarden van derden in bewaring/consignatie/bewerking
- **04** Verleende kredietopeningen niet opgenomen
- **05** Verkregen kredietopeningen niet opgenomen
- **06** Verbintenissen wegens termijnverrichtingen op aandelen/effecten
- **07** Diverse rechten en verplichtingen
- **09** Restcategorie (diverse rechten en verplichtingen — niet uitputbaar via 00-07)

Deze rekeningen verschijnen in de **toelichting bij de jaarrekening** (staat XVII/VIII *Aard en zakelijk doel van buitenbalans-regelingen*) — niet op de balans zelf.

<small>📖 KB 21-10-2018 — Bijlage 1 MAR — Klasse 0 — _kb_ · CBN-advies 2017/07 — Rekening 09 — _cbn_</small>

## Rationale

Klasse 0 lost een spanning op in het boekhoudrecht: de **balanslogica** vereist dat een passief alleen wordt opgenomen wanneer het een **actuele verplichting** vertegenwoordigt (geen voorwaardelijke of toekomstige), maar de **getrouw-beeld-norm** vereist dat **belangrijke risico's en rechten** zichtbaar blijven voor lezers van de jaarrekening. Klasse 0 + toelichtingsstaten brengen deze beide vereisten samen: het cijfer staat niet in de balans (waar het misleidend zou zijn), maar wel in de toelichting met aard, omvang en doel — zodat banken, leveranciers en investeerders het integrale risicoprofiel kennen.

<small>🔗 CBN-advies 2017/07 — Algemeen + boekingsregels — _cbn_</small>

## Sub-concepten

### 📦 Rechten (ontvangen garanties + verkregen verbintenissen)

#### Definitie

**Rechten** in klasse 0 zijn de **voordelen** die de onderneming heeft ontvangen van derden: ontvangen borgtochten, bankgaranties die haar zijn verleend, niet-opgenomen kredietlijnen, beloofde overheidssubsidies waarvan de toekenning nog niet zeker is. Ze worden geboekt aan debet-zijde (van de tegenrekeningparen) en signaleren toekomstige inkomende geldstromen of zekerheden waar de onderneming op kan rekenen.

<small>📖 KB 21-10-2018 MAR — Klasse 0 — rechten — _kb_</small>

### 📦 Verplichtingen (gestelde zekerheden + gegeven verbintenissen)

#### Definitie

**Verplichtingen** in klasse 0 zijn de **risico's** die de onderneming op zich heeft genomen tegenover derden: gestelde borgtochten, hypotheken op eigen activa, garanties aan dochterondernemingen, verkregen termijnverrichtingen die nog moeten worden afgewikkeld. Ze worden geboekt aan credit-zijde (van de tegenrekeningparen) en signaleren mogelijke toekomstige uitstromen of vermogensverhinderingen.

<small>📖 KB 21-10-2018 MAR — Klasse 0 — verplichtingen — _kb_</small>

## Bouwstenen

### ⚙️ Boeking gestelde zekerheid

Wanneer de onderneming aan een derde (bv. een bank, een verhuurder) een **zakelijke zekerheid** stelt — bv. een pand op een onroerend goed, een handelszekerheid op de bedrijfsactiva — wordt dit geboekt in klasse 0:

```
020 Onroerende goederen bezwaard met hypotheek    D 500.000
   021 Crediteuren wegens gestelde zakelijke zekerheid C 500.000
```
(De waarde = nominale waarde van het bezwaarde goed of het maximum-bedrag van de hypothecaire inschrijving.)

Bij **vrijgave** (bv. lening volledig terugbetaald): omgekeerde boeking.

<small>📖 CBN-advies 2017/07 — Boeking gestelde zekerheid — _cbn_</small>

### ⚙️ Boeking operationele leasing — aankoopoptie + niet-vervallen huur

Onder **B-GAAP** wordt operationele leasing **niet** op de balans opgenomen (huur als kost in klasse 61). De aankoopoptie en het saldo van toekomstige huurbedragen worden wel in **klasse 0** geboekt als off-balance verplichting:

```
051 Verbintenissen wegens niet-opgenomen huurleasingen   D 36.000
   050 Crediteuren leasingverbintenissen                  C 36.000
```
(Voor een leasing met 3 jaar restduur × 12.000 EUR jaarhuur)

De aankoopoptie wordt apart vermeld (typisch 5-10 % van aanschaffingsprijs).

**Belangrijk verschil IFRS 16**: onder IFRS gaat dezelfde lease wél op de balans (right-of-use-actief + lease-verplichting). Dit is een van de grootste B-GAAP/IFRS-verschillen.

<small>📖 CBN-advies 2015/04 — Leasing — informatieverschaffing toelichting — _cbn_ · IFRS 16 — IFRS 16 — _richtlijn_</small>

## Valkuilen

> [!warning]- Klasse 0 vergeten bij commissaris-controle
> **Verkeerde assumptie**: Klasse 0 is informatief — geen impact op balans/resultaat, dus geen controle nodig.
>
> **Kernpunt**: Klasse 0 is **onderdeel van de jaarrekening** (toelichting staat XVII/VIII) en moet door de commissaris worden gecontroleerd. Een belangrijke off-balance verplichting (bv. een hypothecaire inschrijving van 2 miljoen EUR op het bedrijfsvastgoed) niet vermelden, is een **materieel verzuim** dat het getrouw beeld aantast.
>
> <small>🔗 CBN-advies 2017/07 — Algemeen — _cbn_</small>

> [!warning]- Operationele leasing onder IFRS off-balance houden
> **Verkeerde assumptie**: Voor IFRS-rapportering kan de operationele leasing in klasse 0 blijven zoals onder B-GAAP.
>
> **Kernpunt**: **IFRS 16** schrapt het onderscheid tussen operationele en financiële leasing voor de lessee: **alle** leasecontracten met looptijd > 12 maanden en bedrag > low-value-drempel komen op de balans (right-of-use-actief + lease-verplichting). De klasse 0-presentatie geldt **alleen** voor B-GAAP-rapportering.
>
> <small>📖 IFRS 16 — IFRS 16 — _richtlijn_</small>

## Verder lezen (scope-out)

- → Schulden op balans (klasse 17 + 42-48) → [[schulden-op-korte-termijn]] _(moet-verwijzen)_
- ↪ IFRS-leasing — on-balance presentatie (IFRS 16) → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vergelijkbaar_met`
- [[schulden-op-korte-termijn]]
    - **Gelijkenissen**:
        - Beide signaleren een toekomstige verplichting tot uitstroom van middelen
    - **Verschillen**:
        - Schulden: actuele verplichting + zeker bedrag → op de balans (klasse 42-48)
        - Memorierekeningen: voorwaardelijk of onzeker actueel statuut → buiten de balans (klasse 0)
    - ⚠️ **Verwarringsrisico**: Een aankoopoptie bij operationele lease op de balans boeken (verkeerd onder B-GAAP) of een verschuldigde factuur op klasse 0 boeken (idem).
