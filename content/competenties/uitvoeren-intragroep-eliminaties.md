---
title: Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/uitvoeren-intragroep-eliminaties.yaml
gegenereerd_op: '2026-05-17'
---
# Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden

**⚖️ 80% · 🤖 20%**

> De eliminatieplichten en de berekening van het aandeel van derden zijn wettelijk vastgelegd (KB WVV art. 3:134-3:140). De materialiteitsbeoordeling (verwaarloosbare bedragen, art. 3:139) is een praktijkoordeel.

## Aanbevolen werkwijze

### 1. Identificeren van onderlinge vorderingen en schulden

Lijst alle wederzijdse vorderingen en schulden tussen groepsvennootschappen op.

**Waarom?** Onderlinge posities moeten worden geschrapt om dubbeltelling in de geconsolideerde balans te vermijden.

**📥 Input**:
- Geconsolideerde proefbalansen van moeder en dochters → **Vorderingen en schulden tegenover groepsvennootschappen** _(boekhoudkundig-bedrag)_
- Intercompany-reconciliaties → **Saldi per tegenpartij** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eliminaties → **Lijst onderlinge posities per tegenpartij** _(document)_

**🛠️ Hoe**:

1. Open de proefbalans van Aurelia Holding NV en zoek de subrubrieken 'Vorderingen op groepsvennootschappen' en 'Schulden aan groepsvennootschappen'.
2. Open de proefbalans van Brugse Brouwerij BV en doe hetzelfde.
3. Voer een intercompany-reconciliatie uit: voor elk paar (Aurelia ↔ Brugse) moet vordering bij A = schuld bij B (en omgekeerd).
4. Verschillen tussen vordering en schuld? → vraag uitsplitsing aan beide vennootschappen. Vaak veroorzaakt door valuta-omrekening of timing-verschillen.
5. Documenteer de geverifieerde saldi voor eliminatie in stap 2.


**Grondslag**: [[intragroep-eliminaties]] §identificatie, KB WVV art. 3:134

### 2. Elimineren van onderlinge vorderingen en schulden

Schrap wederzijdse vorderingen en schulden tussen groepsvennootschappen uit de geconsolideerde balans.

**Waarom?** Het beeld 'alsof het geheel één onderneming was' vereist dat interne posities verdwijnen.

**📥 Input**:
- Werkpapier eliminaties stap 1 → **Geverifieerde onderlinge posities** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Vorderingen + schulden op groepsvennootschappen** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Boek voor elk paar een eliminatie: debiteer 'Schulden aan groepsvennootschappen' bij dochter, crediteer 'Vorderingen op groepsvennootschappen' bij moeder, voor hetzelfde bedrag.
2. Verifieer dat na alle eliminaties enkel posities tegenover entiteiten buiten de consolidatiekring overblijven.
3. Controleer dat de geconsolideerde balans nog steeds in evenwicht is.
4. Documenteer in werkpapier eliminaties: welke bedragen geschrapt, welke restposten over.


> [!example]- Voorbeeld: Aurelia Holding NV heeft een vordering van € 250.000 op Brugse Brouwerij BV. Brugse heeft een overeenkomstige schuld van…
> Aurelia Holding NV heeft een vordering van € 250.000 op Brugse Brouwerij BV. Brugse heeft een overeenkomstige schuld van € 250.000 aan Aurelia.
>
> 1. **Eliminatie-boeking** 📝
>
>    Debiteer: Schulden aan groepsvennootschappen (Brugse)     € 250.000
>    Crediteer: Vorderingen op groepsvennootschappen (Aurelia)  € 250.000
>    
>
> 2. **Effect op geconsolideerde balans** 📊
>
>    | Vóór eliminatie                                  | Aurelia (€) | Brugse (€) |
>    |--------------------------------------------------|------------:|-----------:|
>    | Vorderingen op groepsvennootschappen (Brugse)    |     250.000 |          — |
>    | Schulden aan groepsvennootschappen (Aurelia)     |           — |    250.000 |
>    
>    | Na eliminatie in geconsolideerde balans          | Bedrag (€) |
>    |--------------------------------------------------|-----------:|
>    | Vorderingen op groepsvennootschappen             |          0 |
>    | Schulden aan groepsvennootschappen               |          0 |
>    
>

**Grondslag**: [[intragroep-eliminaties]] §boeking-eliminatie, KB WVV art. 3:134

### 3. Elimineren van in activa begrepen onderlinge winsten

Schrap de winstmarge die de groep aan zichzelf heeft toegerekend en die nog in voorraden of vaste activa zit.

**Waarom?** Winsten op interne transacties zijn economisch niet gerealiseerd zolang het actief de groep niet verlaten heeft.

**📥 Input**:
- Voorraadbestanden bij elke groepsvennootschap → **Restvoorraad afkomstig van interne aankoop** _(boekhoudkundig-bedrag)_
- Brutomarge intra-groepsverkopen → **Percentage marge** _(percentage)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Voorraad en intra-groepswinst** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Vraag aan elke kopende groepsvennootschap (bv. Brugse): hoeveel voorraad afkomstig van interne aankoop (van Aurelia) staat nog op de balans?
2. Vraag aan de verkopende vennootschap (Aurelia) de brutomarge die op de interne verkoop is toegepast.
3. Bereken de niet-gerealiseerde winst: brutomarge × restvoorraad.
4. Boek de eliminatie: voorraad bij de kopende vennootschap wordt teruggebracht naar de waarde voor de groep (zonder marge); resultaat wordt verminderd met dezelfde brutomarge.
5. Idem voor vaste activa die intern zijn verkocht: schrap de niet-gerealiseerde winst en herzie de afschrijvingsbasis.


> [!example]- Voorbeeld: Aurelia Holding NV heeft aan Brugse Brouwerij BV voorraad verkocht met een brutomarge van 25 %
> Aurelia Holding NV heeft aan Brugse Brouwerij BV voorraad verkocht met een brutomarge van 25 %. Op balansdatum staat bij Brugse nog € 200.000 van die voorraad.
>
> 1. **Berekening niet-gerealiseerde winst** 🧮
>
>    niet-gerealiseerde winst = brutomarge × restvoorraad
>                            = 25 % × € 200.000
>                            = **€ 50.000**
>    
>
> 2. **Eliminatie-boeking** 📝
>
>    Debiteer: Resultaat (eliminatie intra-groepswinst)    € 50.000
>    Crediteer: Voorraad bij Brugse                        € 50.000
>    → Voorraad wordt teruggebracht naar de waarde voor de groep (€ 150.000 i.p.v. € 200.000).
>    
>

**Grondslag**: [[intragroep-eliminaties]] §niet-gerealiseerde-winsten, KB WVV art. 3:134 lid 2

> [!warning]- Schrap ook intra-groepswinsten in voorraad of vaste activa, niet alleen vorderingen en schulden.
>
> _Vaak fout gedaan_: Aannemen dat alleen vorderingen en schulden moeten worden geëlimineerd.
>
> _Grondslag_: [[intragroep-eliminaties]] §winsten-in-activa

### 4. Elimineren van onderlinge opbrengsten en kosten

Schrap interne verkopen, beheersvergoedingen, intresten en huur uit de geconsolideerde resultatenrekening.

**Waarom?** Dezelfde transactie mag niet dubbel verschijnen in de groepscijfers.

**📥 Input**:
- Resultatenrekeningen van groepsvennootschappen → **Interne verkopen, beheersvergoedingen, intresten, huur** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde resultatenrekening → **Onderlinge opbrengsten en kosten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak een matrix van interne transacties tussen Aurelia Holding NV en Brugse Brouwerij BV: verkopen, beheersvergoedingen, intresten op interne leningen, huur van interne gebouwen.
2. Voor elke transactie: schrap de omzet bij de verkopende vennootschap én de aankoopkost (of huurkost, intrestkost) bij de kopende vennootschap, voor exact hetzelfde bedrag.
3. Verifieer dat het geconsolideerde resultaat per saldo niet verandert (eliminatie raakt zowel opbrengst als kost).
4. Documenteer in werkpapier eliminaties: welke transacties geschrapt en bedragen.


**Grondslag**: [[intragroep-eliminaties]] §resultaat-eliminaties, KB WVV art. 3:136

### 5. Aanpassen van eliminaties voor evenredig geconsolideerde dochters

Beperk de eliminaties bij gemeenschappelijke dochters tot het pro-rata deel.

**Waarom?** Bij evenredige consolidatie wordt slechts het pro-rata deel opgenomen; eliminatie moet daarbij aansluiten.

**📥 Input**:
- Lijst gemeenschappelijke dochters → **Belangenpercentage per gemeenschappelijke dochter** _(percentage)_

**📤 Output**:
- Werkpapier eliminaties → **Aangepaste eliminatiebedragen pro-rata** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Identificeer de gemeenschappelijke dochters die evenredig zijn geconsolideerd (bv. Filmstudio Florence BV voor 50 %).
2. Voor elke eliminatie tussen moeder en gemeenschappelijke dochter: pas niet 100 % maar het belangenpercentage toe (KB WVV art. 3:140 a).
3. Bv. Cardinal Group NV ↔ Filmstudio Florence BV: eliminatie van intra-groepswinst van € 50.000 wordt 50 % × € 50.000 = € 25.000.
4. Documenteer apart waarom de pro-rata behandeling is gekozen.


**Grondslag**: [[intragroep-eliminaties]] §evenredige-consolidatie-pro-rata, KB WVV art. 3:140

### 6. Beoordelen van materialiteit

Beslis welke eliminaties achterwege mogen blijven omdat ze van te verwaarlozen betekenis zijn.

**Waarom?** De wet staat een proportionaliteitsoordeel toe; rituele eliminatie van triviale bedragen is niet vereist.

**📥 Input**:
- Bedragen van geïdentificeerde eliminaties → **Bedragen** _(boekhoudkundig-bedrag)_
- Geconsolideerd balanstotaal + resultaat → **Referentiebedragen voor materialiteit** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eliminaties → **Lijst eliminaties die achterwege blijven met motivering** _(conclusie)_

**🛠️ Hoe**:

1. Bepaal de materialiteitsdrempel voor de geconsolideerde jaarrekening (typisch een percentage van balanstotaal of resultaat).
2. Toets per eliminatie of het bedrag onder de drempel valt EN of weglating geen vertekening van het getrouw beeld geeft.
3. Eliminaties bedoeld in KB WVV art. 3:134, 3:136 1°/2° en 3:138 mogen weggelaten worden als het bedrag verwaarloosbaar is (KB WVV art. 3:139).
4. Documenteer de gekozen materialiteit en welke eliminaties achterwege blijven.


**Grondslag**: [[intragroep-eliminaties]] §materialiteit, KB WVV art. 3:139

### 7. Berekenen van het aandeel van derden

Bereken het deel van eigen vermogen en resultaat van de dochter dat toebehoort aan minderheidsaandeelhouders.

**Waarom?** Bij integrale consolidatie wordt 100 % opgenomen; het deel toebehorend aan derden moet afzonderlijk worden gepresenteerd.

**📥 Input**:
- Eigen vermogen dochter op afsluitingsdatum → **Bedrag** _(boekhoudkundig-bedrag)_
- Resultaat dochter boekjaar → **Winst of verlies** _(boekhoudkundig-bedrag)_
- Belangenpercentage moeder → **Percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde balans (passiefzijde) → **Belangen van derden** _(nieuwe-balanspost)_
- Geconsolideerde resultatenrekening → **Aandeel van derden in het resultaat** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Neem het eigen vermogen totaal van Brugse Brouwerij BV op afsluitingsdatum (bv. € 2.000.000).
2. Bereken het derden-percentage: 1 − belangenpercentage moeder (bv. 1 − 0,90 = 0,10).
3. Belangen van derden in EV = derden-percentage × eigen vermogen dochter = 0,10 × € 2.000.000 = € 200.000. Boek aan passiefzijde.
4. Resultaat dochter boekjaar (bv. € 500.000): aandeel van derden in resultaat = 0,10 × € 500.000 = € 50.000. Boek onderaan de geconsolideerde resultatenrekening.
5. Verifieer dat het netto-resultaat voor de moeder dan = 0,90 × € 500.000 = € 450.000.


> [!example]- Voorbeeld: Aurelia Holding NV bezit 90 % in Brugse Brouwerij BV. Eigen vermogen Brugse op afsluitingsdatum = € 2.000.000
> Aurelia Holding NV bezit 90 % in Brugse Brouwerij BV. Eigen vermogen Brugse op afsluitingsdatum = € 2.000.000. Resultaat boekjaar Brugse = € 500.000.
>
> 1. **Berekening belangen van derden in eigen vermogen** 🧮
>
>    belangen van derden in EV = (1 − belangenpercentage) × eigen vermogen dochter
>                              = (1 − 0,90) × € 2.000.000
>                              = 0,10 × € 2.000.000
>                              = **€ 200.000**
>    
>
> 2. **Berekening aandeel van derden in resultaat** 🧮
>
>    aandeel van derden in resultaat = (1 − 0,90) × € 500.000 = **€ 50.000**
>    
>
> 3. **Presentatie in geconsolideerde jaarrekening** 📊
>
>    | Geconsolideerde balans (passiefzijde, uittreksel) |     Bedrag (€) |
>    |---------------------------------------------------|---------------:|
>    | Eigen vermogen toebehorend aan Aurelia            |              x |
>    | **Belangen van derden**                           |    **200.000** |
>    
>    | Geconsolideerde resultatenrekening (uittreksel)   |     Bedrag (€) |
>    |---------------------------------------------------|---------------:|
>    | Resultaat boekjaar (totaal)                       |        500.000 |
>    | waarvan: **Aandeel van derden in resultaat**      |     **50.000** |
>    | waarvan: aandeel Aurelia in resultaat             |        450.000 |
>    
>

**Grondslag**: [[minderheidsbelangen]] §berekening, KB WVV art. 3:137

> [!warning]- Boek alleen 'Belangen van derden' bij integrale consolidatie, nooit bij evenredige consolidatie.
>
> _Vaak fout gedaan_: Bij evenredige consolidatie alsnog een aandeel van derden boeken voor het deel buiten de groep.
>
> _Grondslag_: [[minderheidsbelangen]] §uitsluitend-bij-integrale-consolidatie

### 8. Aanpassen van de toelichting

Verwijder weggelaten rechten en verplichtingen uit de toelichting bij de geconsolideerde jaarrekening.

**Waarom?** Wat geëlimineerd is in cijfers moet ook in de toelichting consistent verdwijnen.

**📥 Input**:
- Toelichting bij enkelvoudige jaarrekeningen → **Rechten en verplichtingen tegenover groepsvennootschappen** _(document)_

**📤 Output**:
- Toelichting bij geconsolideerde jaarrekening → **Wederzijdse rechten/verplichtingen verwijderd** _(document)_

**🛠️ Hoe**:

1. Open de toelichting bij de enkelvoudige jaarrekeningen van Aurelia en Brugse.
2. Identificeer toelichtings-onderdelen die rechten of verplichtingen tussen Aurelia en Brugse vermelden (garanties, borgstellingen, verhuurde activa).
3. Schrap deze items uit de geconsolideerde toelichting (KB WVV art. 3:138).
4. Verifieer consistentie: wat geëlimineerd is in cijfers, moet ook uit de tekstuele toelichting verdwijnen.


**Grondslag**: [[intragroep-eliminaties]] §toelichting-consistentie, KB WVV art. 3:138


## Voorbeelden

> [!example]- Aurelia Holding NV bezit 90 % in Brugse Brouwerij BV. Aurelia heeft aan Brugse voorraad verkocht met een brutomarge van…
> **Conclusie**: Te elimineren intra-groepswinst in voorraad = 25 % × € 200.000 = € 50.000 (voorraad terug naar € 150.000 — de waarde voor de groep). Belangen van derden op balans = (1 − 0,90) × € 2.000.000 = € 200.000. Aandeel van derden in resultaat = (1 − 0,90) × € 500.000 = € 50.000.
>
> **Grondslag**: [[intragroep-eliminaties]] §eliminatie-voorraad; [[minderheidsbelangen]] §berekening
>
> **Redenering**: Intra-groepswinst in voorraad wordt teruggedraaid omdat het actief de groep nog niet heeft verlaten. Het complementaire belang van 10 % wordt afgezonderd voor derden bij integrale consolidatie.


## Gebaseerd op concepten

[[intragroep-eliminaties]] · [[minderheidsbelangen]] · [[integrale-consolidatie]] · [[evenredige-consolidatie]] · [[belangenpercentage]]
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.D, 1.4.I.B, 1.4.I.F
