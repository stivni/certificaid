---
title: Bedrijfsresultaat (bedrijfskosten en bedrijfsopbrengsten)
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.M
- 1.1.II.N
- 1.1.II.S
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/bedrijfsresultaat.json
gegenereerd_op: '2026-05-21'
---
# Bedrijfsresultaat (bedrijfskosten en bedrijfsopbrengsten) ⚖️

Het bedrijfsresultaat is de **operationele kern** van de resultatenrekening — de klassieke vraag 'verdient de onderneming geld uit haar gewone activiteit?'. Voor een stagiair-GA is dit het eerste analyse-niveau: alvorens financiële kosten of niet-recurrente posten in beeld komen, moet de bedrijfsmarge zelf gezond zijn. Categorisatie-fouten tussen klasse 6/7 (bedrijf), 65/75 (financieel) en 66/76 (niet-recurrent) vervormen direct dit cijfer.

> [!summary] Korte inhoud
> Het verschil tussen **bedrijfsopbrengsten** (klasse 7, hoofdzakelijk omzet en voorraadwijzigingen) en **bedrijfskosten** (klasse 6, hoofdzakelijk handelsgoederen/grond- en hulpstoffen, diensten en diverse goederen, bezoldigingen + sociale lasten, afschrijvingen, waardeverminderin….

> [!info] Behoort tot: [[resultatenrekening]]

Het verschil tussen **bedrijfsopbrengsten** (klasse 7, hoofdzakelijk omzet en voorraadwijzigingen) en **bedrijfskosten** (klasse 6, hoofdzakelijk handelsgoederen/grond- en hulpstoffen, diensten en diverse goederen, bezoldigingen + sociale lasten, afschrijvingen, waardeverminderingen, voorzieningen, andere bedrijfskosten). Geeft weer wat de onderneming presteert in haar **kernactiviteit** — vóór financiële en niet-recurrente posten.

_Bron: MAR klasse 6 + 7_



## Bouwstenen

### Klasse 70 — Omzet ⚖️

De **verkoop van goederen en levering van diensten aan derden** in het kader van de gewone bedrijfsuitoefening, onder aftrek van kortingen, rabatten en ristorno's. **Geen** BTW of andere directe verkoopbelasting. Voor natuurlijke personen-koopman: ook onttrekkingen in natura die niet aan het bedrijf ten goede komen.

**Waarom?** Omzet is de centrale meeteenheid van bedrijfsprestatie. Heldere definitie voorkomt manipulatie van groei-percentages of fiscale gunstregimes.



Meubelzaak Mertens BV verkoopt 245 stoelen × € 280 + 87 tafels × € 1.250 = € 68.600 + € 108.750 = € 177.350; geeft 3 % volumekorting = € 5.320 → omzet € 172.030 op rekening 700.

_Grondslag: MAR rubriek 70 (zie MAR-noot 55)_

### Klasse 60 — Handelsgoederen, grond- en hulpstoffen ⚖️

Aankopen van grondstoffen en handelsgoederen, gecorrigeerd door voorraadwijzigingen (klasse 609 'Voorraadwijziging' kan in- of uitwerken).

**Waarom?** Boekhoudkundig moet de kost van wat verkocht is matchen met de opbrengst. Voorraadwijziging corrigeert de aankopen naar 'gebruikte/verkochte voorraad'.



Naaiatelier Ninove BV: aankoop grondstoffen 20X1 € 480.000; beginvoorraad € 60.000, eindvoorraad € 90.000 → voorraadwijziging +€ 30.000. Verbruikte grondstoffen = € 480.000 − € 30.000 = € 450.000.

_Grondslag: MAR klasse 60_

### Klasse 62 — Bezoldigingen + sociale lasten ⚖️

Lonen en salarissen (620, 621), werkgeversbijdragen sociale zekerheid (621, 622), pensioenen en overige sociale lasten (623, 624), andere personeelskosten (verzekeringen, vergoedingen).

**Waarom?** Personeelskosten zijn vaak de grootste kostenpost; aparte rubricering laat de gebruiker toe loonintensiviteit te beoordelen.



Naaiatelier Ninove BV 20X1: brutolonen € 280.000 (620), werkgevers-RSZ € 84.000 (621), groepsverzekering € 12.000 (623), maaltijdcheques € 4.000 (624). Totaal € 380.000 onder rubriek 62.

_Grondslag: MAR klasse 62_

### Klasse 63-64-65 — Niet-kaskosten en andere ⚖️

Rubriek 63 = afschrijvingen + waardeverminderingen + voorzieningen — toevoegingen (de zogenoemde 'niet-kaskosten' die het bedrijfsresultaat aanpassen zonder cashuitgang). Rubriek 64 = andere bedrijfskosten (bv. bedrijfsbelastingen op de exploitatie). Rubriek 65 = financiële kosten (apart van het bedrijfsresultaat).

**Waarom?** De financiële analyst onderscheidt graag operationele cashflow van boekhoudkundig resultaat. De niet-kasrubrieken (klasse 63) zijn essentieel voor die brug.



Naaiatelier Ninove BV: afschrijvingen MVA € 85.000 (6302) + IVA € 5.000 (6301) + waardeverminderingen voorraden € 4.500 (6340) + toevoeging voorziening garantie € 25.000 (6371) → klasse 63 totaal € 119.500.

_Grondslag: MAR klasse 63 + 64_


## In de praktijk

<h3 id="brutomarge-en-ebitda-als-afgeleide-ratio-s">Brutomarge en EBITDA als afgeleide ratio's</h3>

> [!tip]- Brutomarge en EBITDA als afgeleide ratio's
> Brutomarge = omzet − klasse 60 (aankopen) − voorraadwijziging. EBITDA = bedrijfsresultaat + afschrijvingen + waardeverminderingen + voorzieningen — toevoegingen. Twee veelgebruikte indicatoren bij ratio-analyse en kredietbeoordeling. 🔗

> [!tip]- Herkennen op het examen
> Examen: EBITDA = klasse 70+71+72+74 − 60 − 61 − 62 − 64 (zonder klasse 63 niet-kas).


> [!info]- Niet verwarren met [[financiele-verrichtingen]]
> Bedrijfsresultaat: klasse 60-64 vs 70-74, gewone bedrijfsuitoefening. Financiële verrichtingen: klasse 65 vs 75, rente + financiële kosten/opbrengsten. Strikt gescheiden in de resultatenrekening voor analytische helderheid.
>
> _Trigger_: Examen: 'intrest op leveranciersschuld te laat betaald' — financiële kost (klasse 65), NIET bedrijfskost. 'huurkost van magazijn' — bedrijfskost (klasse 61).


## Valkuilen

> [!warning]- Voorraadwijziging is een onderdeel van de bedrijfsopbrengsten (rekening 71) bij stijging van voorraad gereed product/goederen in bewerking,…
> ⚠️ Voorraadwijziging is een onderdeel van de bedrijfsopbrengsten (rekening 71) bij stijging van voorraad gereed product/goederen in bewerking, MAAR een correctie op de aankopen (rekening 609) bij voorraadwijziging grondstoffen. Onderscheid is essentieel voor correct bedrijfsresultaat. 🔗
>
> _Bron: MAR klasse 60 + 71_


> [!warning]- Bezoldigingen incl. werkgeversbijdragen en alle aanvullende kosten — niet alleen het brutoloon
> ⚠️ Bezoldigingen incl. werkgeversbijdragen en alle aanvullende kosten — niet alleen het brutoloon. Voor matching met fiscale aangifte: arbeiders/bedienden/zelfstandige bestuurders apart. ⚖️
>
> _Bron: MAR klasse 62_



## Zie ook

- **Vereist kennis van**: [[voorraden]]

## Voorbeelden

Naaiatelier Ninove BV 20X1: omzet € 1.250.000 (rekening 70), voorraadwijziging gereed product +€ 22.300 (71), totaal bedrijfsopbrengsten € 1.272.300. Bedrijfskosten: aankopen grondstoffen € 450.000 (60), diensten en diverse goederen € 185.000 (61), bezoldigingen + sociale lasten € 380.000 (62), afschrijvingen € 95.000 (630), waardeverminderingen € 8.500 (634), andere bedrijfskosten € 18.000 (64) → totaal € 1.136.500. Bedrijfsresultaat = € 1.272.300 − € 1.136.500 = € 135.800.

## Bronnen

[^1]: `MAR-ondernemingen__art_7`
[^2]: `MAR-ondernemingen__art_6`
[^3]: `MAR-ondernemingen__art_0__sub_2deg_part2`
