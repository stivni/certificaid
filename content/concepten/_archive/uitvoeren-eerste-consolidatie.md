---
title: Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde
  onderneming
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.D
- 1.4.I.E
- 1.4.I.G
- 1.4.II.D
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/uitvoeren-eerste-consolidatie.json
gegenereerd_op: '2026-05-21'
---
# Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming 🔗

Een toepassingscompetentie binnen het Belgische boekhoudrecht-consolidatieregime (KB WVV Boek 3, Titel 2) — gericht op het boekjaar van eerste opname. De stagiair waardeert de overgenomen netto-activa, bepaalt het consolidatieverschil (goodwill of negatief verschil) en boekt het in conform de toepasselijke techniek.



## Stappen

### 1. Vaststellen van de aanschaffingswaarde van de deelneming

Bepaal de prijs die de moeder voor de aandelen heeft betaald.

**Waarom?** De aanschaffingswaarde is één van de twee termen in de compensatie van de eerste consolidatie.

**📥 Input**:
- Aandelenkoopovereenkomst → **Aanschaffingsprijs op verwervingsdatum** _(boekhoudkundig-bedrag)_
- Betalingsbewijzen en addenda → **Earn-outs, vendor loans, aanpassingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eerste consolidatie → **Aanschaffingswaarde op verwervingsdatum** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de aandelenkoopovereenkomst van 1 januari 20X1 waarmee Aurelia Holding NV 80 % van Brugse Brouwerij BV verwerft.
2. Lees de overeengekomen prijs (bv. € 1.600.000).
3. Tel alle aanpassingen op: earn-outs, vendor loans, transactiekosten — maar enkel als ze tot de aanschaffingswaarde behoren volgens [[eerste-consolidatie]] §aanschaffingswaarde.
4. Noteer het eindresultaat als 'Aanschaffingswaarde deelneming Brugse Brouwerij BV = € 1.600.000'.


**Grondslag**: [[eerste-consolidatie]] §aanschaffingswaarde, KB WVV art. 3:127

### 2. Bepalen van het eigen vermogen van de dochter op verwervingsdatum

Bereken het eigen vermogen van de dochter op de datum dat de moeder controle verwerft.

**Waarom?** Het pro-rata aandeel van de moeder in dit eigen vermogen vormt de tweede term van de compensatie.

**📥 Input**:
- Balans van Brugse Brouwerij BV op of nabij verwervingsdatum → **Kapitaal + reserves + overgedragen resultaat** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eerste consolidatie → **Eigen vermogen dochter op verwervingsdatum** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Vraag aan Brugse Brouwerij BV de tussentijdse balans op verwervingsdatum (1 januari 20X1), of de balans op de meest nabije datum die binnen het toegelaten venster van KB WVV art. 3:129 valt.
2. Tel op: kapitaal + uitgiftepremies + reserves + overgedragen resultaat.
3. Bij Brugse: kapitaal € 1.000.000 + reserves € 500.000 = eigen vermogen € 1.500.000.
4. Documenteer ook welke datum gebruikt werd en waarom (KB WVV art. 3:129 b laat ook aanvangsdatum boekjaar toe in eerste-consolidatie-uitzondering).


**Grondslag**: [[eerste-consolidatie]] §eigen-vermogen-op-verwervingsdatum, KB WVV art. 3:129

### 3. Toerekenen van het verschil aan onder- of overgewaardeerde activa en passiva

Bereken het verschil tussen aanschaffingswaarde en pro-rata eigen vermogen, en reken het zoveel mogelijk toe aan posten waarvan de werkelijke waarde afwijkt van de boekwaarde.

**Waarom?** KB WVV art. 3:128 vereist dat het verschil eerst aan stille meer- of minderwaarden wordt toegerekend vóór het residu als consolidatieverschil wordt geboekt.

**📥 Input**:
- Aanschaffingswaarde + belangenpercentage uit stap 1 → **Bedrag + percentage** _(boekhoudkundig-bedrag)_
- Eigen vermogen dochter uit stap 2 → **Bedrag** _(boekhoudkundig-bedrag)_
- Inventaris stille meer- of minderwaarden → **Per actief- en passiefpost: werkelijke waarde versus boekwaarde** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eerste consolidatie → **Toerekening verschil per post** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bereken het pro-rata aandeel: belangenpercentage × eigen vermogen dochter op verwervingsdatum. Voor Aurelia/Brugse: 80 % × € 1.500.000 = € 1.200.000.
2. Bereken het totale verschil: aanschaffingswaarde − pro-rata aandeel. Voor Aurelia/Brugse: € 1.600.000 − € 1.200.000 = € 400.000.
3. Inventariseer stille meer- of minderwaarden bij Brugse Brouwerij BV: vastgoed dat boekhoudkundig lager staat dan de werkelijke waarde, voorraden, voorzieningen, ...
4. Reken het verschil zoveel mogelijk toe aan die posten: opwaardering bij meerwaarde, afwaardering bij minderwaarde. Per post: bedrag pro-rata aan belangenpercentage.
5. Wat overblijft, is het residuele consolidatieverschil voor stap 4.
6. Aandachtspunt: bij Brugse Brouwerij worden in ons scenario ondergewaardeerde terreinen geïdentificeerd voor € 250.000; het residu van € 150.000 gaat door naar stap 4 als consolidatieverschil.


> [!example]- Voorbeeld: Aurelia Holding NV verwerft op 1 januari 20X1 een belang van 80 % in Brugse Brouwerij BV voor € 1.600.000
> Aurelia Holding NV verwerft op 1 januari 20X1 een belang van 80 % in Brugse Brouwerij BV voor € 1.600.000. Eigen vermogen (EV) Brugse op die datum: € 1.500.000. Ondergewaardeerde terreinen geïdentificeerd voor € 250.000.
>
> 1. **Berekening pro-rata aandeel** 🧮
>
>    pro-rata aandeel Aurelia in EV Brugse = belangenpercentage × eigen vermogen dochter
>                                          = 80 % × € 1.500.000
>                                          = **€ 1.200.000**
>    
>
> 2. **Berekening totaal verschil** 🧮
>
>    totaal verschil = aanschaffingswaarde − pro-rata aandeel
>                    = € 1.600.000 − € 1.200.000
>                    = **€ 400.000** (positief verschil)
>    
>
> 3. **Toerekening aan posten** 💬
>
>    Ondergewaardeerde terreinen bij Brugse: toerekening € 250.000.
>    Residu = € 400.000 − € 250.000 = **€ 150.000** gaat door naar stap 4 als residueel consolidatieverschil.
>    
>

**Grondslag**: [[consolidatieverschil]] §toerekening, KB WVV art. 3:128 en 3:130

> [!warning]- Eerst toerekenen aan onder- of overgewaardeerde posten, dan pas residu als consolidatieverschil boeken.
>
> _Vaak fout gedaan_: Het volledige verschil tussen aanschaffingswaarde en boekwaarde van pro-rata EV rechtstreeks als consolidatieverschil boeken.
>
> _Grondslag_: [[consolidatieverschil]] §toerekening

### 4. Berekenen en boeken van het residuele consolidatieverschil

Boek het resterende verschil als 'Consolidatieverschillen' (actief- of passiefzijde).

**Waarom?** Het overblijvende verschil weerspiegelt goodwill (positief — synergieën, marktpositie) of badwill (negatief — verwachte verliezen).

**📥 Input**:
- Residueel verschil uit stap 3 → **Bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Consolidatieverschillen (actief- of passiefzijde)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem het residueel verschil over uit stap 3 (bv. € 150.000 positief voor Aurelia/Brugse).
2. Positief verschil? → 'Positieve consolidatieverschillen' aan actiefzijde van de geconsolideerde balans.
3. Negatief verschil? → 'Negatieve consolidatieverschillen' aan passiefzijde.
4. Belangrijke regel: positieve en negatieve consolidatieverschillen van verschillende dochters mag je NIET compenseren. Binnen dezelfde dochter MOET je wel compenseren.
5. Pas het afschrijvingsplan van stap 5 toe op een positief consolidatieverschil.


> [!example]- Voorbeeld: Aurelia/Brugse: residueel verschil = € 150.000 (positief, na toerekening van € 250.000 aan ondergewaardeerde terreinen)
> Aurelia/Brugse: residueel verschil = € 150.000 (positief, na toerekening van € 250.000 aan ondergewaardeerde terreinen).
>
> 1. **Boeking in de geconsolideerde balans** 📝
>
>    Debiteer: Positieve consolidatieverschillen (actiefzijde)    € 150.000
>    Crediteer: Compensatie deelneming (afsluiting stap 2)         € 150.000
>    
>
> 2. **Schematische impact op balans** 📊
>
>    | Geconsolideerde balans Aurelia — Activa     |     Bedrag (€) |
>    |---------------------------------------------|---------------:|
>    | Vaste activa (incl. opwaardering terreinen) |      8.000.000 |
>    | **Positieve consolidatieverschillen**       |    **150.000** |
>    | Vlottende activa                            |      5.000.000 |
>    | **Totaal**                                  | **13.150.000** |
>    
>

**Grondslag**: [[consolidatieverschil]] §boeking-residu, KB WVV art. 3:130

> [!warning]- Compensatie van positieve en negatieve consolidatieverschillen is verboden, tenzij ze dezelfde dochter betreffen.
>
> _Vaak fout gedaan_: Positieve en negatieve consolidatieverschillen van verschillende dochters tegen elkaar wegstrepen.
>
> _Grondslag_: [[consolidatieverschil]] §compensatie-verbod

### 5. Vastleggen van het afschrijvingsplan voor positief consolidatieverschil

Bepaal de afschrijvingsduur die de werkelijke economische gebruiksduur van de goodwill weerspiegelt.

**Waarom?** Positieve consolidatieverschillen moeten worden afgeschreven over de vermoedelijke gebruiksduur (KB WVV art. 3:131).

**📥 Input**:
- Inschatting economische voordelen onderliggend aan goodwill → **Synergieën, marktpositie, merken, klantenbasis** _(document)_

**📤 Output**:
- Werkpapier afschrijvingsplan → **Afschrijvingsduur + jaarlijkse afschrijving** _(document)_

**🛠️ Hoe**:

1. Beoordeel waaruit de goodwill van € 150.000 bij Brugse Brouwerij BV bestaat: synergieën met Aurelia? Marktaandeel? Merken?
2. Schat de vermoedelijke gebruiksduur (bv. 5 of 10 jaar). Documenteer de motivering.
3. Bereken de jaarlijkse afschrijving: residueel consolidatieverschil / gebruiksduur. Bv. € 150.000 / 5 = € 30.000 per jaar.
4. Plan de afschrijving over de volgende boekjaren (telkens als kost in de geconsolideerde resultatenrekening).
5. Toelichting verplicht voor afschrijvingsduren > 5 jaar — motiveer in de toelichting.


**Grondslag**: [[consolidatieverschil]] §afschrijving, KB WVV art. 3:131

### 6. Integreren van de cijfers van de dochter in de geconsolideerde jaarrekening

Voer de gekozen consolidatietechniek uit op de geherwaardeerde cijfers van de dochter.

**Waarom?** De keuze van techniek (integraal, evenredig, vermogensmutatie) bepaalt hoe de cijfers verschijnen in de geconsolideerde jaarrekening.

**📥 Input**:
- Geherwaardeerde activa en passiva van dochter → **Per post: bedrag na toerekening** _(boekhoudkundig-bedrag)_
- Keuze techniek uit [[kiezen-consolidatiemethode]] → **Integraal / evenredig / vermogensmutatie** _(conclusie)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Posten van dochter geïntegreerd** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bij integrale consolidatie: volg [[integrale-consolidatie]] §uitvoering. Neem 100 % activa/passiva op. Boek 'Belangen van derden' = (1 − belangenpercentage) × eigen vermogen dochter op afsluitingsdatum.
2. Bij evenredige consolidatie: neem activa/passiva pro-rata op (belangenpercentage × bedrag). Geen aandeel van derden.
3. Bij vermogensmutatie: boek één post 'Vennootschappen waarop vermogensmutatie is toegepast' = belangenpercentage × eigen vermogen dochter + consolidatieverschil.
4. Stuur intragroep-eliminaties door naar [[uitvoeren-intragroep-eliminaties]].


> [!example]- Voorbeeld: Aurelia/Brugse: integrale consolidatie
> Aurelia/Brugse: integrale consolidatie. Belangenpercentage = 80 %. Eigen vermogen Brugse op afsluitingsdatum 20X1 = € 2.000.000 (waarvan resultaat boekjaar € 500.000).
>
> 1. **Berekening aandeel van derden in eigen vermogen** 🧮
>
>    aandeel van derden in EV = (1 − belangenpercentage) × eigen vermogen dochter
>                            = (1 − 80 %) × € 2.000.000
>                            = 20 % × € 2.000.000
>                            = **€ 400.000**
>    
>
> 2. **Berekening aandeel van derden in resultaat** 🧮
>
>    aandeel van derden in resultaat = (1 − 80 %) × € 500.000 = **€ 100.000**
>    
>
> 3. **Geconsolideerde balans (uittreksel)** 📊
>
>    | Geconsolideerde balans Aurelia (uittreksel)  |     Bedrag (€) |
>    |----------------------------------------------|---------------:|
>    | Activa van Aurelia + Brugse (100 %)          |              x |
>    | Positieve consolidatieverschillen            |        150.000 |
>    | ...                                          |            ... |
>    | Belangen van derden (passief)                |        400.000 |
>    
>

**Grondslag**: [[integrale-consolidatie]] §100-procent-opname, KB WVV art. 3:124 en 3:137


## Voorbeelden



