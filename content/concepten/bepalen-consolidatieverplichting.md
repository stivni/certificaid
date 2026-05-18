---
title: Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.C
- 1.4.I.B
- 1.4.II.B
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/bepalen-consolidatieverplichting.json
gegenereerd_op: '2026-05-18'
---
# Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen 🤖


## Stappen

### 1. Vaststellen of de entiteit als vennootschap kwalificeert

Ga na of de entiteit rechtspersoonlijkheid heeft en als vennootschap kwalificeert.

**Waarom?** Alleen vennootschappen met rechtspersoonlijkheid kunnen moedervennootschap zijn.

**📥 Input**:
- Statuten van de entiteit → **Juridische vorm** _(document)_
- KBO-uittreksel → **Rechtsvorm** _(document)_

**📤 Output**:
- Notitie aan dossier → **Bevestiging vennootschapsstatus** _(conclusie)_

**🛠️ Hoe**:

1. Open de statuten van de entiteit (bv. Aurelia Holding NV).
2. Lees de juridische vorm (NV, BV, CV, maatschap zonder rechtspersoonlijkheid, ...).
3. Vergelijk met de definitie van moedervennootschap in [[moedervennootschap]] §definitie.
4. Conclusie: vennootschap met rechtspersoonlijkheid → ga naar stap 2. Geen rechtspersoonlijkheid of natuurlijk persoon → geen consolidatieplicht op deze entiteit (mogelijk wel via consortium-lid).


**Grondslag**: [[moedervennootschap]] §definitie, WVV art. 1:15

> [!warning]- Een natuurlijke persoon is nooit zelf moedervennootschap.
>
> _Vaak fout gedaan_: Aannemen dat Pieter Vermeulen die meerderheidsstemrechten heeft in meerdere vennootschappen, zelf consolidatieplichtig is.
>
> _Grondslag_: [[consolidatieverplichting]] §natuurlijke personen

> [!warning]- Een maatschap zonder rechtspersoonlijkheid is geen moeder.
>
> _Vaak fout gedaan_: Een maatschap zonder rechtspersoonlijkheid behandelen als moedervennootschap.
>
> _Grondslag_: [[consolidatieverplichting]] §rechtspersoonlijkheid

### 2. Vaststellen of er controle bestaat over een of meer dochters

Ga na of de vennootschap controle uitoefent over een of meer andere vennootschappen.

**Waarom?** Zonder controle is de vennootschap geen moeder en hoeft zij niet te consolideren.

**📥 Input**:
- Aandelenregister → **Stemrechten per aandeelhouder** _(percentage)_
- Aandeelhoudersovereenkomsten → **Afspraken over benoemingen, vetorechten** _(document)_
- Notulen van laatste twee algemene vergaderingen → **Aanstelling bestuurders met effectieve stemrechten** _(document)_

**📤 Output**:
- Lijst van gecontroleerde vennootschappen → **Aard van controle (in rechte, in feite, exclusief, gezamenlijk)** _(conclusie)_

**🛠️ Hoe**:

1. Open het aandelenregister van Aurelia Holding NV en zoek per deelneming het stemrechtpercentage.
2. Bij meer dan 50 % stemrechten: onweerlegbaar vermoeden van controle in rechte (zie [[exclusieve-controle]] §controle-in-rechte).
3. Bij precies 50 % of minder: open de aandeelhoudersovereenkomsten en check op vetorechten of benoemingsrechten.
4. Open de notulen van de laatste twee algemene vergaderingen (AV) van de doelvennootschap. Heeft Aurelia de meerderheid van bestuurders aangesteld met haar effectieve stemrechten? Dan is er controle in feite (zie [[exclusieve-controle]] §controle-in-feite).
5. Maak een lijst van alle gecontroleerde vennootschappen met de aard van controle.


**Grondslag**: [[controle]] §soorten controle, WVV art. 1:14 tot 1:19

> [!warning]- Tel ook controle-in-feite mee, niet alleen het aandelenpercentage.
>
> _Vaak fout gedaan_: Aannemen dat controle altijd meer dan 50 % stemrechten vereist.
>
> _Grondslag_: [[controle]] §controle-in-feite

### 3. Onderzoeken of er een consortium is

Ga na of meerdere vennootschappen onder centrale leiding staan zonder onderlinge moeder-dochter-relatie.

**Waarom?** Bij een consortium ontbreekt een verticale moeder en rust de plicht gezamenlijk op de leden (WVV art. 3:24).

**📥 Input**:
- Aandeelhoudersstructuur van de betrokken vennootschappen → **Wie controleert wie?** _(document)_
- Aandeelhoudersovereenkomsten of beleidsdocumenten → **Aanwijzingen voor centrale leiding** _(document)_

**📤 Output**:
- Conclusie over groep-structuur → **Verticale groep met moeder OF horizontale groep (consortium)** _(conclusie)_

**🛠️ Hoe**:

1. Teken de aandeelhoudersstructuur uit: wie bezit aandelen in wie?
2. Is er één rechtspersoon die de andere(n) controleert? → verticale groep, ga naar stap 4 met die moeder.
3. Staan meerdere vennootschappen onder gemeenschappelijke leiding (vaak natuurlijke persoon zoals Pieter Vermeulen) zonder dat zij elkaar controleren? → consortium.
4. Bij consortium: de plicht rust gezamenlijk bij Industria Antwerpen NV en Jachthaven Jezus-Eik NV (zie [[consortium]] §gezamenlijke-plicht).


**Grondslag**: [[consortium]] §definitie, WVV art. 1:19 en 3:24

### 4. Toetsen aan de vrijstelling 'groep van beperkte omvang'

Bereken de geconsolideerde of geaggregeerde cijfers en toets aan de drempelwaarden.

**Waarom?** Een kleine groep is in beginsel vrijgesteld van consolidatie (WVV art. 1:26 §1).

**📥 Input**:
- Enkelvoudige jaarrekeningen van alle groepsvennootschappen → **Omzet, balanstotaal, jaargemiddelde werknemers** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toets-conclusie → **Vrijgesteld of niet** _(conclusie)_

**🛠️ Hoe**:

1. Verzamel de enkelvoudige jaarrekeningen van Aurelia Holding NV en al haar dochters.
2. Bereken op geaggregeerde basis (som van enkelvoudige cijfers, vóór eliminaties): jaaromzet, balanstotaal en jaargemiddelde werknemers.
3. Vergelijk met de drempelwaarden uit [[groottecriteria-consolidatie]] §drempels (cijferzakboekje).
4. Overschreden de groep meer dan één criterium gedurende twee opeenvolgende boekjaren? → vrijstelling vervalt, ga naar stap 5.
5. Overschreden ten hoogste één criterium? → groep van beperkte omvang, vrijgesteld (tenzij beursnotering, zie [[groep-van-beperkte-omvang]] §uitzondering-notering).


> [!example]- Voorbeeld: Aurelia Holding NV consolideert met haar dochter Gent Garantie BV. Geaggregeerde cijfers: omzet 20 mln EUR, balanstotaal…
> Aurelia Holding NV consolideert met haar dochter Gent Garantie BV. Geaggregeerde cijfers: omzet 20 mln EUR, balanstotaal 12 mln EUR, jaargemiddelde werknemers 180.
>
> 1. **Toets aan drempels groep van beperkte omvang** 🧮
>
>    | Criterium                     | Geaggregeerd | Drempel (cijferzakboekje) | Overschreden? |
>    |-------------------------------|-------------:|--------------------------:|:--------------|
>    | Jaaromzet                     | 20 mln EUR   | 34 mln EUR                | Nee           |
>    | Balanstotaal                  | 12 mln EUR   | 17 mln EUR                | Nee           |
>    | Jaargemiddelde werknemers     | 180          | 250                       | Nee           |
>    
>
> 2. **Conclusie** 💬
>
>    Geen enkel criterium overschreden → groep van beperkte omvang.
>    Vrijgesteld van consolidatie (mits geen notering op gereglementeerde markt).
>    
>

**Grondslag**: [[groep-van-beperkte-omvang]] §drempels, WVV art. 1:26

> [!warning]- 'Geaggregeerde basis' is enkel een berekeningswijze, geen vooraf bestaande consolidatie.
>
> _Vaak fout gedaan_: Aannemen dat 'op geconsolideerde basis' betekent dat er al een geconsolideerde jaarrekening moet bestaan vóór de toets.
>
> _Grondslag_: [[groottecriteria-consolidatie]] §toetswijze

### 5. Toetsen aan de vrijstelling van subconsolidatie

Ga na of een hogere moeder al een gelijkwaardige geconsolideerde jaarrekening opstelt.

**Waarom?** Subconsolidatie wordt vermeden als hogerop al wordt geconsolideerd, tenzij er beursnotering is.

**📥 Input**:
- Aandeelhoudersstructuur op hoger niveau → **Bestaat er een hogere moeder?** _(document)_
- Geconsolideerde jaarrekening van de hogere moeder → **Wettelijke gelijkwaardigheid, controle, openbaarheid** _(document)_

**📤 Output**:
- Vrijstellings-conclusie → **Submoeder is wel of niet vrijgesteld** _(conclusie)_

**🛠️ Hoe**:

1. Identificeer de hogere moeder boven Aurelia Holding NV (bv. Kappers Köln GmbH met 95 % in Aurelia).
2. Vraag de geconsolideerde jaarrekening van Kappers Köln GmbH op.
3. Toets aan de drie voorwaarden uit [[vrijstelling-subconsolidatie]] §voorwaarden: gelijkwaardigheid (EU-richtlijn 2013/34 of equivalent), wettelijke controle door commissaris, openbaarmaking.
4. Check of geen enkel lid van de subconsolidatiekring (Aurelia + Brugse Brouwerij BV + andere dochters) genoteerd is op een gereglementeerde markt.
5. Alle voorwaarden vervuld? → Aurelia is vrijgesteld van subconsolidatie. Een voorwaarde niet vervuld? → wel consolideren.


**Grondslag**: [[vrijstelling-subconsolidatie]] §voorwaarden, WVV art. 3:26

> [!warning]- Bij beursnotering vervalt de vrijstelling altijd.
>
> _Vaak fout gedaan_: Aannemen dat de vrijstelling geldt ongeacht of een dochter genoteerd is.
>
> _Grondslag_: [[vrijstelling-subconsolidatie]] §uitzondering-notering

### 6. Formuleren van de eindconclusie

Stel de eindconclusie op voor de cliënt op basis van stappen 1 tot 5.

**Waarom?** De cliënt heeft een ondubbelzinnig antwoord nodig over zijn consolidatieplicht.

**📥 Input**:
- Werkpapieren stappen 1-5 → **Per toets een ja/nee-conclusie** _(conclusie)_

**📤 Output**:
- Conclusienota voor cliënt → **Eindkwalificatie van consolidatieplicht** _(document)_

**🛠️ Hoe**:

1. Vat de conclusies van stappen 1 tot 5 samen in één tabel.
2. Combineer tot één eindconclusie:
   - Geen rechtspersoonlijkheid of geen controle → niet consolidatieplichtig.
   - Groep van beperkte omvang (zonder notering) → vrijgesteld.
   - Subconsolidatie-vrijstelling van toepassing → vrijgesteld.
   - Anders → consolidatieplichtig als moeder of als consortium-lid samen met andere leden.
3. Documenteer de gronden voor de conclusie in het cliëntdossier.


**Grondslag**: [[consolidatieverplichting]] §eindkwalificatie (praktijk-synthese)


## Voorbeelden




