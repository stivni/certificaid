---
title: Opstellen van een analytische balans voor een vennootschap
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.I.C
- 1.3.II.B
- 1.3.II.C.1
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/opstellen-analytische-balans.json
gegenereerd_op: '2026-05-21'
---
# Opstellen van een analytische balans voor een vennootschap 🔗

Competentie om de officiële balans te herklasseren tot analytische balans: activa naar liquiditeitsgraad geordend, passiva naar opeisbaarheid. Deze herklassering is de basis voor élke ratioberekening — de officiële balans dient als juridisch document, de analytische balans als analyse-instrument.



## Stappen

### 1. Sorteren van de activa volgens liquiditeit

Orden de activa van minst naar meest liquide en groepeer ze in drie analyse-blokken.

**Waarom?** Pas door deze ordening zie je hoeveel kapitaal duurzaam vastligt en hoeveel snel kan worden gemobiliseerd.

**📥 Input**:
- Officiële balans uit de jaarrekening → **Activa-zijde, post per post** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Analytische activa-tabel → **Drie blokken (vast, voorraden, vlottend zeer liquide)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de officiële balans van Rotex Roeselare NV en kopieer de activa-zijde naar je werkbestand.
2. Groepeer de posten in drie blokken volgens [[analytische-balans]] §activa-naar-liquiditeit:
   - **Vast** (minst liquide): oprichtingskosten, immateriële + materiële + financiële vaste activa, vorderingen > 1 jaar.
   - **Voorraden** (medium): voorraden + bestellingen in uitvoering.
   - **Vlottend zeer liquide**: vorderingen ≤ 1 jaar, geldbeleggingen, liquide middelen, overlopende rekeningen.
3. Bereken het subtotaal per blok.
4. Controleer dat de som van de drie blokken = balanstotaal-actief.


> [!example]- Voorbeeld: Rotex Roeselare NV (grote NV, volledig schema) — balanstotaal € 25.800.000
> Rotex Roeselare NV (grote NV, volledig schema) — balanstotaal € 25.800.000.
>
> 1. **Activa-blokken na herwerking** 📊
>
>    | Blok                       | Posten                                              | Bedrag        |
>    |----------------------------|-----------------------------------------------------|--------------:|
>    | Vast (minst liquide)       | Oprichting + Imm + Mat + Fin VA + Vord. > 1j        | € 18.000.000  |
>    | Voorraden (medium)         | Voorraden + bestellingen in uitvoering              | € 2.500.000   |
>    | Vlottend zeer liquide      | Vord. ≤ 1j + geldbeleggingen + liquide + overl.     | € 5.300.000   |
>    | **Totaal**                 |                                                     | **€ 25.800.000** |
>    
>

**Grondslag**: [[analytische-balans]] §activa-naar-liquiditeit, KB WVV balansschema

### 2. Sorteren van de passiva volgens opeisbaarheid

Orden de passiva van niet-opeisbaar naar zeer kort opeisbaar in vier analyse-blokken.

**Waarom?** Zo zie je hoeveel financiering structureel is (permanent kapitaal) versus hoeveel binnenkort moet worden vergoed.

**📥 Input**:
- Officiële balans uit de jaarrekening → **Passiva-zijde, post per post** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Analytische passiva-tabel → **Vier blokken (EV, voorzieningen, lange schulden, korte schulden)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Kopieer de passiva-zijde van Rotex naar je werkbestand.
2. Groepeer in vier blokken volgens [[analytische-balans]] §passiva-naar-opeisbaarheid:
   - **Eigen vermogen** (niet opeisbaar): kapitaal + reserves + overgedragen resultaat + herwaarderingsmeerwaarden + kapitaalsubsidies.
   - **Voorzieningen + uitgestelde belastingen**: opeisbaar bij realisatie van het risico.
   - **Schulden > 1 jaar** (lange termijn).
   - **Schulden ≤ 1 jaar + overlopende rekeningen** (korte termijn).
3. Bereken subtotaal per blok en het permanent kapitaal = EV + voorzieningen + schulden > 1 jaar.
4. Controleer dat de som = balanstotaal-passief = balanstotaal-actief uit stap 1.


> [!example]- Voorbeeld: Rotex Roeselare NV — passiva-zijde
> Rotex Roeselare NV — passiva-zijde.
>
> 1. **Passiva-blokken na herwerking** 📊
>
>    | Blok                            | Posten                                  | Bedrag        |
>    |---------------------------------|-----------------------------------------|--------------:|
>    | Eigen vermogen                  | Kapitaal + reserves + overgedr. result. | € 12.000.000  |
>    | Voorzieningen                   | Voorzieningen risico's en kosten        | € 1.000.000   |
>    | Schulden > 1 jaar               | Bank LT + obligaties + leasing LT       | € 8.000.000   |
>    | Schulden ≤ 1 jaar + overl. rek. | Leveranciers + bank KT + sociaal + fisc.| € 4.800.000   |
>    | **Totaal**                      |                                         | **€ 25.800.000** |
>    |                                 | **Permanent kapitaal** = € 12M + € 1M + € 8M = € 21.000.000 |          |
>    
>

**Grondslag**: [[analytische-balans]] §passiva-naar-opeisbaarheid

### 3. Doorvoeren van noodzakelijke herklassificaties

Pas economisch verantwoorde correcties toe op de boekhoudkundige balans.

**Waarom?** De wettelijke balans verzoent meerdere doelen (juridisch, fiscaal). Voor analyse wil je een zuiver-economisch beeld.

**📥 Input**:
- Toelichting bij de jaarrekening → **Uitgestelde belastingen, verbonden partijen, gemengde posten** _(document)_
- Analytische tabellen uit stap 1 en 2 → **Per-blok-totalen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geherklasseerde analytische balans → **Aangepaste blokken met motivering per herklassificatie** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de toelichting en zoek naar posten die analytisch in een ander blok thuishoren.
2. **Vorderingen > 1 jaar**: laat staan in "vast", of verplaats naar "overig" als ze een specifieke financieringsrol hebben.
3. **Uitgestelde belastingen**: splits het deel dat binnen 5 jaar realiseerbaar is (schuldachtig) van het permanent deel (toevoegen aan EV).
4. **Onuitkeerbare reserves**: maak zichtbaar als aparte regel binnen het EV.
5. **Niet in de balans opgenomen verplichtingen** uit [[niet-in-balans-opgenomen-rechten-verplichtingen]] §subsidiariteit: noteer ze in een memo onder de balans (niet vermengen met balanscijfers — vakdoctrine vraagt transparantie).
6. Documenteer elke herklassificatie in een aparte kolom "Aanpassing + motivering" zodat de analyse reproduceerbaar is.


> [!example]- Voorbeeld: Rotex Roeselare NV — toelichting vermeldt € 500.000 uitgestelde belastingen waarvan € 350.000 realisatie binnen 5 jaar
> Rotex Roeselare NV — toelichting vermeldt € 500.000 uitgestelde belastingen waarvan € 350.000 realisatie binnen 5 jaar.
>
> 1. **Splitsing uitgestelde belastingen** 🧮
>
>    - Boekwaarde uitgestelde belastingen: € 500.000
>    - Schuldachtig (≤ 5 jaar): € 350.000 → blijft bij "Voorzieningen + uitgestelde belastingen"
>    - Permanent karakter: € 150.000 → toegevoegd aan **Eigen vermogen**
>    
>
> 2. **Analytisch EV na aanpassing** 📊
>
>    | Post                              | Wettelijk     | Aanpassing    | Analytisch    |
>    |-----------------------------------|--------------:|--------------:|--------------:|
>    | Eigen vermogen                    | € 12.000.000  | + € 150.000   | € 12.150.000  |
>    | Voorzieningen + uitgest. belast.  | € 1.000.000   | – € 150.000   | € 850.000     |
>    
>

**Grondslag**: [[analytische-balans]] §herklassificaties-voor-analyse

> [!warning]- Documenteer elke herklassificatie expliciet in een aparte kolom.
>
> _Vaak fout gedaan_: Een analyse maken die afwijkt van de wettelijke balans zonder dat de afwijking traceerbaar is — niet reproduceerbaar en niet vergelijkbaar.
>
> _Grondslag_: [[analytische-balans]] §documenteer-herklassificaties

### 4. Berekenen van het werkkapitaal en het netto-bedrijfskapitaal

Bereken werkkapitaal en netto-bedrijfskapitaal op basis van de analytische balans.

**Waarom?** Werkkapitaal is de eerste indicator van financieel evenwicht tussen lange financiering en duurzame investering.

**📥 Input**:
- Analytische balans uit stap 1-3 → **Blokken activa en passiva** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkkapitaal-tabel → **Werkkapitaal in € en als signaal positief/negatief** _(conclusie)_

**🛠️ Hoe**:

1. Bereken het **werkkapitaal** op twee manieren conform [[werkkapitaal]] §absolute-tegenhanger:
   - Vlottende activa – schulden ≤ 1 jaar
   - Permanent kapitaal – vaste activa
2. Beide moeten hetzelfde getal opleveren — verschil betekent rekenfout of vergeten post.
3. Interpreteer het teken: positief = comfortzone, vaste activa zijn met lange financiering gedekt; negatief = kwetsbaarheid, korte schulden financieren deels duurzaam actief.
4. Vergelijk met sectormediaan via [[sectorvergelijking-financiele-analyse]] §sectorgrenzen.


> [!example]- Voorbeeld: Rotex Roeselare NV — werkkapitaal-berekening na herwerking
> Rotex Roeselare NV — werkkapitaal-berekening na herwerking.
>
> 1. **Werkkapitaal beide methodes** 🧮
>
>    | Methode                                   | Berekening                          | Bedrag       |
>    |-------------------------------------------|-------------------------------------|-------------:|
>    | Vlottende activa – schulden ≤ 1 jaar      | (€ 2.500.000 + € 5.300.000) – € 4.800.000 | € 3.000.000 |
>    | Permanent kapitaal – vaste activa         | € 21.000.000 – € 18.000.000         | € 3.000.000  |
>    
>
> 2. **Interpretatie** 💬
>
>    Werkkapitaal € 3.000.000 — positief. Permanent kapitaal dekt vaste activa
>    ruimschoots; € 3M veiligheidsmarge financiert deel van voorraden en
>    vorderingen. Comfortzone bevestigd.
>    
>

**Grondslag**: [[werkkapitaal]] §positief-werkkapitaal, [[analytische-balans]] §herwerking


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.II.A`
