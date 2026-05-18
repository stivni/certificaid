---
title: Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.G
- 1.4.II.D
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verwerken-wijziging-consolidatiekring.json
gegenereerd_op: '2026-05-18'
---
# Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition) 🤖


## Stappen

### 1. Identificeren van de aard van de wijziging

Bepaal welk type wijziging zich tussen twee boekjaren heeft voorgedaan in de groep.

**Waarom?** De aard van de wijziging bepaalt welk specifiek verwerkingsregime van toepassing is.

**📥 Input**:
- Wijzigingsoverzicht groep boekjaar t versus t-1 → **Verwervingen, vervreemdingen, liquidaties, belang-aanpassingen** _(document)_

**📤 Output**:
- Werkpapier wijziging consolidatiekring → **Type wijziging per entiteit** _(conclusie)_

**🛠️ Hoe**:

1. Maak een verschillenanalyse tussen de consolidatiekring van vorig boekjaar en die van het huidig boekjaar.
2. Identificeer per entiteit het type wijziging:
   (a) Nieuwe dochter (eerste consolidatie).
   (b) Uittrede dochter (de-consolidatie).
   (c) Step acquisition met kwalificatiewijziging (bv. Antwerpse Investments NV verhoogt belang in Drukkerij Dendermonde BV van 25 % naar 60 %).
   (d) Wijziging tussen gezamenlijke en exclusieve controle.
   (e) Transactie onder gemeenschappelijke leiding (interne herstructurering).
3. Documenteer per wijziging: aard, datum, betrokken percentages.


**Grondslag**: [[wijziging-consolidatiekring]] §typologie

### 2. Toetsen kwalificatiewijziging bij belangsverhoging

Ga na of een belangsverhoging de kwalificatie wijzigt (van geen invloed naar invloed van betekenis, van invloed naar controle, ...).

**Waarom?** Een kwalificatiewijziging triggert een wijziging van consolidatietechniek met waarderingsgevolgen.

**📥 Input**:
- Belangenpercentage en controlepercentage voor en na transactie → **Percentages** _(percentage)_
- Aandeelhoudersovereenkomsten → **Wijziging van controle-rechten** _(document)_

**📤 Output**:
- Werkpapier kwalificatiewijziging → **Per trap: wijzigt kwalificatie ja/nee + nieuwe kwalificatie** _(conclusie)_

**🛠️ Hoe**:

1. Voor elke trap (bv. Antwerpse Investments NV verhoogt van 25 % naar 60 % in Drukkerij Dendermonde BV): noteer belangenpercentage en controlepercentage voor en na.
2. Volg [[kwalificeren-relatie-deelneming]] §toetsing-controle voor de nieuwe kwalificatie.
3. Bepaal of de kwalificatie wijzigt:
   - Van geen invloed naar invloed van betekenis (drempel ≥ 20 %)?
   - Van invloed van betekenis naar controle (drempel > 50 %)?
   - Verhoging binnen dezelfde categorie?
4. Wijziging bevestigd → ga naar stap 4 (kantelpunt-procedure).


**Grondslag**: [[step-acquisition]] §kwalificatiewijziging

### 3. Verwerken eerste consolidatie bij opname van een nieuwe entiteit

Voer een eerste consolidatie uit voor elke nieuw opgenomen dochter of geassocieerde.

**Waarom?** Elke nieuwe opname in de kring vereist een eerste consolidatie met berekening van consolidatieverschil.

**📥 Input**:
- Aandelenkoopovereenkomst, balans dochter op verwervingsdatum → **Aanschaffingswaarde, eigen vermogen, stille meer- of minderwaarden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eerste consolidatie → **Compensatie, toerekening, residueel verschil, afschrijvingsplan** _(boekingsregel)_

**🛠️ Hoe**:

1. Volg de procedure uit [[uitvoeren-eerste-consolidatie]] §stappen-1-tot-5 voor de nieuwe entiteit.
2. Sluit aan op de gekozen techniek (integrale, evenredige of vermogensmutatie — uit [[kiezen-consolidatiemethode]]).
3. Documenteer in werkpapier: aanschaffingswaarde, pro-rata aandeel, toerekening aan posten, residueel consolidatieverschil, afschrijvingsplan.


**Grondslag**: [[eerste-consolidatie]] §procedure, KB WVV art. 3:127-3:131

### 4. Verwerken kantelpunt vermogensmutatie naar integrale of evenredige consolidatie

Bij overschrijding van de controlegrens: verlaat de vermogensmutatie en start integrale (of evenredige) consolidatie.

**Waarom?** Bij overgang naar controle volstaat vermogensmutatie niet meer; de techniek kantelt en het consolidatieverschil moet worden herberekend.

**📥 Input**:
- Boekwaarde deelneming voor de nieuwe trap → **Post 'Vennootschappen waarop vermogensmutatie is toegepast' + bestaand consolidatieverschil** _(boekhoudkundig-bedrag)_
- Aandelenkoopovereenkomst nieuwe trap → **Aanvullende aanschaffingswaarde** _(boekhoudkundig-bedrag)_
- Balans dochter op datum van nieuwe trap → **Eigen vermogen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans + werkpapier → **Volledige opname activa/passiva + nieuw consolidatieverschil + aandeel van derden** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Verlaat de vermogensmutatie: de post 'Vennootschappen waarop vermogensmutatie is toegepast' wordt afgeboekt.
2. Herwaardeer het bestaande consolidatieverschil op datum van de nieuwe trap.
3. Voer een nieuwe eerste consolidatie uit: tel beide aanschaffingswaarden samen (oude trap + nieuwe trap), trek het pro-rata aandeel in eigen vermogen op datum van nieuwe trap af.
4. Reken het verschil toe aan onder- of overgewaardeerde posten; boek het residu als nieuw consolidatieverschil.
5. Vanaf nu: integrale (of evenredige) consolidatie met afzondering van aandeel van derden voor het deel dat aan andere aandeelhouders toebehoort.


> [!example]- Voorbeeld: Antwerpse Investments NV bezat sinds 20X0 een belang van 25 % in Drukkerij Dendermonde BV (geassocieerde, vermogensmutat…
> Antwerpse Investments NV bezat sinds 20X0 een belang van 25 % in Drukkerij Dendermonde BV (geassocieerde, vermogensmutatie). Op 1 juli 20X1 koopt Antwerpse extra aandelen tot 60 %. Op die datum: eigen vermogen (EV) Drukkerij Dendermonde = € 1.250.000.
>
> 1. **Berekening pro-rata aandeel op datum van trap 2** 🧮
>
>    pro-rata aandeel Antwerpse na trap 2 = belangenpercentage × eigen vermogen Drukkerij Dendermonde
>                                          = 60 % × € 1.250.000
>                                          = **€ 750.000**
>    
>
> 2. **Toewijzing nieuwe techniek** 💬
>
>    Kwalificatiewijziging: invloed van betekenis (25 %) → exclusieve controle (60 %).
>    Vermogensmutatie wordt verlaten. Integrale consolidatie start vanaf 1 juli 20X1.
>    
>
> 3. **Aandeel van derden bij integrale consolidatie** 🧮
>
>    aandeel van derden in EV Drukkerij Dendermonde = (1 − 60 %) × € 1.250.000
>                                                    = 40 % × € 1.250.000
>                                                    = **€ 500.000** (passiefzijde)
>    
>
> 4. **Effect op consolidatieverschil** 💬
>
>    Het bestaande consolidatieverschil uit de eerste trap (25 %, vermogensmutatie) wordt geherwaardeerd. Een nieuw consolidatieverschil wordt berekend op basis van de gecombineerde aanschaffingswaarde en het pro-rata aandeel op datum van de nieuwe trap.
>    
>

**Grondslag**: [[step-acquisition]] §kanteling-techniek, KB WVV art. 3:127 (analogische toepassing)

> [!warning]- Bij kanteling van techniek: het bestaande consolidatieverschil wordt geherwaardeerd, niet behouden.
>
> _Vaak fout gedaan_: Aannemen dat bij overgang van vermogensmutatie naar integrale consolidatie het oude consolidatieverschil ongewijzigd blijft.
>
> _Grondslag_: [[step-acquisition]] §herwaardering-consolidatieverschil

### 5. Verwerken gehele of gedeeltelijke realisatie van aandelen

Bij verkoop van aandelen: boek het overblijvende consolidatieverschil af naar verhouding van de gerealiseerde aandelen.

**Waarom?** Bij realisatie verdwijnt de economische binding (geheel of gedeeltelijk). Het consolidatieverschil moet pro-rata worden afgeboekt.

**📥 Input**:
- Verkoopovereenkomst → **Aantal verkochte aandelen + verkoopprijs** _(boekhoudkundig-bedrag)_
- Oorspronkelijk consolidatieverschil → **Bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Afboeking consolidatieverschil + eventuele meer- of minderwaarde** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal het percentage gerealiseerde aandelen ten opzichte van het oorspronkelijke belang (bv. Aurelia Holding NV verkoopt 30 % van haar 100 %-deelneming in Brugse Brouwerij BV).
2. Boek pro-rata afboeking van het oorspronkelijke consolidatieverschil: bv. 30 % × oorspronkelijk verschil.
3. Vergelijk de verkoopprijs met de boekwaarde van het verkochte deel (deelneming + pro-rata consolidatieverschil) → meer- of minderwaarde op de realisatie.
4. Indien Aurelia controle behoudt (bv. blijft op 70 %): Brugse blijft in de kring, maar voor 30 % wordt nu een aandeel van derden geboekt.
5. Indien Aurelia alle controle verliest: volledige de-consolidatie volgens [[wijziging-consolidatiekring]] §de-consolidatie.


> [!example]- Voorbeeld: Aurelia Holding NV verkoopt 30 % van haar 100 %-dochter Brugse Brouwerij BV buiten de groep
> Aurelia Holding NV verkoopt 30 % van haar 100 %-dochter Brugse Brouwerij BV buiten de groep. Aurelia behoudt 70 %. Oorspronkelijk consolidatieverschil (residu na toerekening) = € 150.000.
>
> 1. **Pro-rata afboeking consolidatieverschil** 🧮
>
>    afboeking = % gerealiseerde aandelen × oorspronkelijk consolidatieverschil
>              = 30 % × € 150.000
>              = **€ 45.000**
>    
>
> 2. **Resterend consolidatieverschil + nieuw aandeel van derden** 💬
>
>    Resterend consolidatieverschil = € 150.000 − € 45.000 = € 105.000.
>    Brugse blijft in de kring (Aurelia 70 % > 50 %, exclusieve controle behouden).
>    Nieuw aandeel van derden = 30 % × eigen vermogen Brugse op afsluitingsdatum (30 % × € 2.000.000 = € 600.000).
>    
>

**Grondslag**: [[wijziging-consolidatiekring]] §realisatie-aandelen, KB WVV art. 3:132

### 6. Verwerken van transacties onder gemeenschappelijke leiding

Bij interne herstructurering waarbij de economische controle ongewijzigd blijft: behoud historische cijfers; genereer geen nieuwe goodwill.

**Waarom?** Interne herstructureringen mogen het groepsbeeld niet kunstmatig wijzigen.

**📥 Input**:
- Beschrijving herstructurering → **Overdracht van dochter binnen de groep** _(document)_

**📤 Output**:
- Werkpapier herstructurering → **Behoud historische cijfers, geen nieuwe goodwill** _(conclusie)_

**🛠️ Hoe**:

1. Identificeer of de transactie plaatsvindt onder gemeenschappelijke leiding (bv. Aurelia Holding NV verkoopt Brugse Brouwerij BV aan een andere 100 %-dochter binnen de groep).
2. Toets aan CBN-doctrine over 'common control transactions': de uiteindelijke economische controle is ongewijzigd.
3. Behoud de historische cijfers van Brugse in de geconsolideerde jaarrekening — geen herwaardering, geen nieuwe goodwill.
4. Boek alleen reclassificatie tussen de betrokken interne entiteiten, geen impact op de geconsolideerde cijfers.


**Grondslag**: [[wijziging-consolidatiekring]] §common-control, CBN-advies common-control transactions


## Voorbeelden




