---
title: Boeken van een aankoop en verkoop met btw en betaling
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.D
- 1.1.II.F
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/boeken-aankoop-verkoop-met-btw.json
gegenereerd_op: '2026-05-18'
---
# Boeken van een aankoop en verkoop met btw en betaling 🤖


## Stappen

### 1. Verifieer de factuur op vorm en inhoud

Controleer of de factuur voldoet aan alle btw-vormvereisten vóór boeking.

**Waarom?** Een onregelmatige factuur geeft geen recht op btw-aftrek en kan leiden tot verwerping bij controle.

**📥 Input**:
- Inkomende of uitgaande factuur → **Datum, partijen, btw-nummers, bedragen, btw-tarief** _(document)_

**📤 Output**:
- Verificatie-stempel of -notitie → **OK voor boeking + grondslag tarief** _(conclusie)_

**🛠️ Hoe**:

1. Toets de vormvereisten: factuurdatum, opeenvolgend nummer, identiteit beide partijen, btw-nummer leverancier en (indien afgenomen) afnemer, prijs excl. btw, btw-tarief, btw-bedrag, totaal.
2. Toets het btw-tarief: 21% standaard, 6% voor specifieke categorieën (zoals voeding, boeken), 12% voor bepaalde diensten — toetsen aan KB nr. 20.
3. Bij gemengde activiteit (Praktijk Persenaire heeft 50% btw-vrijgesteld): bepaal het pro-rata aftrekrecht.
4. Bij twijfel: vraag rechtzetting bij tegenpartij vóór boeking — niet eerst boeken en dan corrigeren.


**Grondslag**: [[dagboek]] §factuurvereisten, btw-wetboek art. 5

> [!warning]- Verifieer btw-nummer leverancier in VIES vóór aftrek — een ongeldig nummer maakt de btw niet aftrekbaar.
>
> _Vaak fout gedaan_: Btw aftrekken op een factuur met ontbrekend of foutief btw-nummer.
>
> _Grondslag_: [[bedrijfsvorderingen]] §btw-aftrekvoorwaarden

### 2. Boek de aankoop in het aankoopdagboek

Splits de factuur in kost, aftrekbare btw en schuld aan leverancier.

**Waarom?** De drie-rekening-boeking maakt btw-aangifte en periodieke schuldenstaat mogelijk.

**📥 Input**:
- Geverifieerde aankoopfactuur stap 1 → **Bedrag excl. btw, btw-bedrag, totaal incl. btw** _(berekening)_

**📤 Output**:
- Journaalpost in aankoopdagboek → **Drie regels (kost, btw, schuld) — debet = credit** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal de kost-rekening volgens MAR — zie [[minimum-algemeen-rekeningenstelsel]] §klasse-6.
2. Voorbeeld bij Meubelzaak Mertens BV — aankoopfactuur Houthandel Hove € 2.500 grondstoffen + 21% btw:
3. Debet: 600 Grondstoffen € 2.500; Debet: 411 Aftrekbare btw € 525; Credit: 4400 Leveranciers — Houthandel Hove € 3.025.
4. Voor diensten: gebruik klasse 61 (61X bv. 6112 Lonen door uitzendkantoor, 6131 Bezoldigingen bestuurders) of 615 (onderhoud).
5. Voor investeringen: gebruik klasse 22-24 (zie [[materiele-vaste-activa]]) niet klasse 6.


> [!example]- Voorbeeld: Naaiatelier Ninove BV ontvangt aankoopfactuur 27/02/2026 van Garenfabriek Gent voor textielgaren: € 4.200 excl. btw + 21…
> Naaiatelier Ninove BV ontvangt aankoopfactuur 27/02/2026 van Garenfabriek Gent voor textielgaren: € 4.200 excl. btw + 21% btw = € 5.082 totaal.
>
> 1. **Boeking in aankoopdagboek** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 27/02/2026 | 600 Grondstoffen — garen | aankoop AF nr. 220 | € 4.200,00 | |
>    | 27/02/2026 | 411 Aftrekbare btw 21% | btw aankoop | € 882,00 | |
>    | 27/02/2026 | 4400 Leveranciers — Garenfabriek Gent | te betalen 60 dagen | | € 5.082,00 |
>    
>

**Grondslag**: [[dagboek]] §aankoop, [[schulden]] §handelsschulden

### 3. Boek de verkoop in het verkoopdagboek

Boek de uitgaande factuur als opbrengst, verschuldigde btw en vordering op klant.

**Waarom?** Het opbrengstgedeelte voedt het bedrijfsresultaat; het btw-gedeelte voedt de btw-aangifte; het vorderings-gedeelte voedt de balans.

**📥 Input**:
- Uitgaande factuur → **Bedrag excl. btw, btw, totaal incl. btw, klant-identificatie** _(berekening)_

**📤 Output**:
- Journaalpost in verkoopdagboek → **Vordering / opbrengst / verschuldigde btw** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal opbrengst-rekening — klasse 70 voor omzet eigen activiteit; 74 voor andere bedrijfsopbrengsten.
2. Voorbeeld bij Meubelzaak Mertens BV: verkoop tafelreeks aan winkel Wevelgem € 6.500 + 21% btw = € 7.865.
3. Debet: 4000 Handelsvorderingen — Wevelgem € 7.865; Credit: 7000 Verkopen meubelen € 6.500; Credit: 451 Verschuldigde btw € 1.365.
4. Verstuur factuur binnen 15 dagen volgens btw-wetgeving (KB nr. 1, art. 4).


> [!example]- Voorbeeld: Meubelzaak Mertens BV verkoopt een keukenset aan klant winkel Wevelgem, factuur 12/03/2026: € 6.500 + 21% btw = € 7.865,…
> Meubelzaak Mertens BV verkoopt een keukenset aan klant winkel Wevelgem, factuur 12/03/2026: € 6.500 + 21% btw = € 7.865, betaling op 30 dagen.
>
> 1. **Boeking in verkoopdagboek** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 12/03/2026 | 4000 Handelsvorderingen — Wevelgem | uitg. factuur 026/2026 | € 7.865,00 | |
>    | 12/03/2026 | 7000 Verkopen meubelen | omzet | | € 6.500,00 |
>    | 12/03/2026 | 451 Verschuldigde btw 21% | btw verkoop | | € 1.365,00 |
>    
>

**Grondslag**: [[dagboek]] §verkoop, [[bedrijfsvorderingen]] §registratie

### 4. Boek de betaling (in- of uitgaand) in het financieel dagboek

Boek de betaling met aanzuivering van vordering of schuld.

**Waarom?** Vorderings-/schulden-saldi moeten gevoed worden tot ze nul zijn, anders blijft de balans verkeerd.

**📥 Input**:
- Bankuittreksel / kasstuk → **Datum, bedrag, tegenpartij, referentie factuur** _(document)_

**📤 Output**:
- Journaalpost in financieel dagboek → **Bank/kas tegen klant/leverancier** _(boekingsregel)_

**🛠️ Hoe**:

1. Identificeer de factuur waarop de betaling slaat (referentie of bedrag-matching).
2. Boek bij betaling leverancier: Debet 4400 Leveranciers; Credit 5500 Bank.
3. Boek bij ontvangst klant: Debet 5500 Bank; Credit 4000 Handelsvorderingen.
4. Bij betaling in cash (zeldzaam, max € 3.000 wettelijke beperking): via 5700 Kas i.p.v. 5500 Bank.
5. Bij gedeeltelijke betaling: vorderings-/schuldsaldi blijven openstaand voor het verschil — zie [[bedrijfsvorderingen]] §saldo.


> [!example]- Voorbeeld: Wevelgem betaalt op 11/04/2026 de factuur van € 7.865 volledig op de KBC-rekening van Meubelzaak Mertens BV.
> Wevelgem betaalt op 11/04/2026 de factuur van € 7.865 volledig op de KBC-rekening van Meubelzaak Mertens BV.
>
> 1. **Boeking ontvangst** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 11/04/2026 | 5500 Bank — KBC | ontvangst Wevelgem | € 7.865,00 | |
>    | 11/04/2026 | 4000 Handelsvorderingen — Wevelgem | aanzuivering F 026/2026 | | € 7.865,00 |
>    
>

**Grondslag**: [[dagboek]] §financieel-dagboek, [[dubbel-boekhouden]] §saldo-aanzuivering

### 5. Saldeer btw-rekeningen op btw-aangiftedatum

Saldeer de aftrekbare btw (411) en verschuldigde btw (451) tegen elkaar en boek het verschil als te betalen of terug te vorderen.

**Waarom?** De btw-aangifte (maand- of kwartaal) vereist een netto-saldo dat als schuld of vordering aan de fiscus blijft staan.

**📥 Input**:
- Proefbalans btw-rekeningen → **Saldi 411 en 451** _(balans)_

**📤 Output**:
- Journaalpost btw-saldering → **Saldering naar 4500 Btw te betalen of 4110 Btw te ontvangen** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal periode (maand of kwartaal volgens omvang cliënt).
2. Bereken: Verschuldigde btw 451 - Aftrekbare btw 411 = te betalen (indien positief) of terug te vorderen (indien negatief).
3. Voorbeeld bij Mertens BV — Q1/2026: 451 € 15.000 - 411 € 10.500 = € 4.500 te betalen.
4. Boek: Debet 451 € 15.000; Credit 411 € 10.500; Credit 4500 Te betalen btw € 4.500.
5. Boek bij betaling aan fiscus op 20e van de volgende maand: Debet 4500; Credit 5500.


**Grondslag**: [[schulden]] §btw-schuld, btw-wetboek art. 53


## Voorbeelden




