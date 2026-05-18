---
title: Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.C
- 1.4.I.B
- 1.4.I.G
- 1.4.II.D
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/afbakenen-consolidatiekring.json
gegenereerd_op: '2026-05-18'
---
# Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden 🤖


## Stappen

### 1. Identificeren van de consoliderende vennootschap

Bepaal welke vennootschap de geconsolideerde jaarrekening opmaakt.

**Waarom?** Zonder startpunt kun je de kring niet opbouwen.

**📥 Input**:
- Conclusie uit [[bepalen-consolidatieverplichting]] → **Moeder of consortium-leden** _(conclusie)_

**📤 Output**:
- Werkpapier consolidatiekring → **Lijst van consoliderende vennootschappen** _(document)_

**🛠️ Hoe**:

1. Neem de eindconclusie van [[bepalen-consolidatieverplichting]] §eindkwalificatie over.
2. Bij een verticale groep: Aurelia Holding NV is de consoliderende vennootschap.
3. Bij een consortium: Industria Antwerpen NV en Jachthaven Jezus-Eik NV zijn samen de consoliderende vennootschappen.
4. Noteer dit als startpunt van het werkpapier "Consolidatiekring".


**Grondslag**: [[consolidatiekring]] §startpunt

### 2. Inventariseren van alle dochterondernemingen

Lijst alle entiteiten op waarover de moeder controlebevoegdheid heeft.

**Waarom?** Alle dochters behoren in beginsel tot de kring (KB WVV art. 3:96).

**📥 Input**:
- Aandeelhoudersregister van Aurelia Holding NV → **Deelnemingen per entiteit** _(document)_
- Statuten en aandeelhoudersovereenkomsten → **Controle-aanwijzingen** _(document)_

**📤 Output**:
- Werkpapier consolidatiekring → **Lijst kandidaat-dochters met aard van controle** _(document)_

**🛠️ Hoe**:

1. Open het aandeelhoudersregister van Aurelia Holding NV en zoek alle deelnemingen.
2. Volg per deelneming de procedure uit [[kwalificeren-relatie-deelneming]] om controle vast te stellen.
3. Vergeet niet de ruime definitie uit WVV art. 3:22: ook verenigingen, stichtingen en buitenlandse instellingen met een commerciële, financiële of industriële activiteit kunnen dochter zijn.
4. Maak een tabel met per entiteit: naam, juridische vorm, belang Aurelia, controle-aard.


**Grondslag**: [[dochteronderneming]] §definitie, WVV art. 3:22

> [!warning]- Inventariseer ook verenigingen, stichtingen en buitenlandse instellingen.
>
> _Vaak fout gedaan_: Alleen klassieke handelsvennootschappen meetellen in de kring.
>
> _Grondslag_: [[dochteronderneming]] §ruime-definitie

### 3. Beoordelen of een dochter buiten de kring mag worden gelaten

Toets per dochter aan de vier wettelijke weglatingsgronden van KB WVV art. 3:97.

**Waarom?** De wet laat vier weglatingsgronden toe; misbruik schendt het getrouw beeld.

**📥 Input**:
- Werkpapier per dochter → **Materialiteit, controlebeperkingen, kostprijs gegevens, verkoopvoornemen** _(document)_

**📤 Output**:
- Werkpapier consolidatiekring → **Per dochter: opname óf weglating met motivering** _(conclusie)_

**🛠️ Hoe**:

1. Toets per dochter aan de vier gronden van KB WVV art. 3:97:
   (a) te verwaarlozen betekenis (bv. Gent Garantie BV met enkele duizenden EUR omzet);
   (b) duurzame controlebeperking (bv. Logistics Lille SAS in een land met deviezenrestricties);
   (c) onevenredige kosten of vertraging;
   (d) bestemd om te worden verkocht.
2. Bij controle in feite: pas KB WVV art. 3:98 toe als opname het getrouw beeld zou schaden.
3. Documenteer voor elke weggelaten dochter de motivering — deze komt in de toelichting bij de geconsolideerde jaarrekening.
4. Hou in gedachte: weglating is uitzondering, opname is regel.


> [!example]- Voorbeeld: Aurelia Holding NV heeft drie dochters: Brugse Brouwerij BV (volledig gecontroleerd, materieel), Logistics Lille SAS (pr…
> Aurelia Holding NV heeft drie dochters: Brugse Brouwerij BV (volledig gecontroleerd, materieel), Logistics Lille SAS (productie-eenheid in een land met deviezenrestricties), Gent Garantie BV (omzet 8.000 EUR).
>
> 1. **Toets per dochter** 🧮
>
>    | Dochter                | Grond                              | Wettelijk artikel | Beslissing      |
>    |------------------------|------------------------------------|-------------------|-----------------|
>    | Brugse Brouwerij BV    | Geen weglatingsgrond               | —                 | Opname in kring |
>    | Logistics Lille SAS    | Duurzame controlebeperking         | KB WVV art. 3:97  | Weglaten        |
>    | Gent Garantie BV       | Te verwaarlozen betekenis          | KB WVV art. 3:97  | Weglaten        |
>    
>
> 2. **Werkpapier consolidatiekring** 💬
>
>    Logistics Lille SAS en Gent Garantie BV worden vermeld in de toelichting met motivering. Zij worden alsnog opgenomen via vermogensmutatie (zie stap 4).
>    
>

**Grondslag**: [[consolidatiekring]] §uitsluitingsgronden, KB WVV art. 3:97 en 3:98

> [!warning]- Weglating vereist altijd één van de vier wettelijke gronden.
>
> _Vaak fout gedaan_: Een dochter weglaten omdat consolideren administratief lastig is.
>
> _Grondslag_: [[consolidatiekring]] §wettelijke-weglatingsgronden

### 4. Verwerken van weggelaten dochters via vermogensmutatie

Neem dochters die zijn weggelaten op grond van art. 3:98 of 3:99 alsnog op via vermogensmutatie.

**Waarom?** KB WVV laat deze dochters niet zomaar verdwijnen — ze moeten via vermogensmutatie zichtbaar blijven voor het getrouw beeld.

**📥 Input**:
- Lijst weggelaten dochters → **Gronden art. 3:98 of 3:99** _(document)_

**📤 Output**:
- Werkpapier consolidatietechnieken → **Beslissing vermogensmutatie per weggelaten dochter** _(conclusie)_

**🛠️ Hoe**:

1. Maak een lijst van dochters die zijn uitgesloten op grond van KB WVV art. 3:98 (controle in feite indruisend tegen getrouw beeld) of art. 3:99 (geen going concern).
2. Voor elk: noteer dat de boekhoudkundige verwerking gebeurt via [[vermogensmutatiemethode]] §toepassing-weggelaten-dochter.
3. Geef dit door aan stap 5 voor verdere keuze van consolidatietechnieken.


**Grondslag**: [[consolidatiekring]] §verwerking-uitgesloten-dochters

### 5. Identificeren van geassocieerde en gemeenschappelijke dochters

Lijst de geassocieerde ondernemingen (invloed van betekenis) en de gemeenschappelijke dochters (gezamenlijke controle) op.

**Waarom?** Geassocieerde en gemeenschappelijke dochters zijn geen klassieke dochters, maar moeten wel in de geconsolideerde jaarrekening verschijnen.

**📥 Input**:
- Deelnemingen-lijst Aurelia Holding NV → **Stemrechtpercentage per deelneming** _(percentage)_
- Aandeelhoudersovereenkomsten → **Afspraken over gezamenlijke controle** _(document)_

**📤 Output**:
- Werkpapier consolidatiekring → **Lijst geassocieerden + gemeenschappelijke dochters** _(document)_

**🛠️ Hoe**:

1. Open de deelnemingen-lijst. Voor elke deelneming zonder controle: volg [[kwalificeren-relatie-deelneming]] §invloed-van-betekenis.
2. Stemrechtpercentage ≥ 20 % zonder controle? → vermoeden geassocieerde onderneming (bv. Drukkerij Dendermonde BV).
3. Aandeelhoudersovereenkomst dat alle beleidsbeslissingen samen worden genomen? → gemeenschappelijke dochter (bv. Filmstudio Florence BV, 50/50 met Cardinal Group NV).
4. Geef de lijst door aan [[kiezen-consolidatiemethode]] voor toewijzing van techniek (vermogensmutatie / evenredige consolidatie).


**Grondslag**: [[geassocieerde-onderneming]] §kwalificatie, [[gemeenschappelijke-dochteronderneming]] §kwalificatie


## Voorbeelden




