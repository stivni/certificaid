---
title: Uitvoeren van eindejaarsverrichtingen en opmaken van proefbalans
tags:
- competentie
- po-1-1
programmaonderdelen:
- '1.1'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-eindejaarsverrichtingen-en-proefbalans.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van eindejaarsverrichtingen en opmaken van proefbalans

**⚖️ 70% · 🤖 30%**

> De inventarisplicht (WER art. III.84) en de eindejaarsverrichtingen volgen uit het boekhoudrecht. Het opmaken van de proefbalans en de volgorde van verrichtingen zijn beroepspraktijk — best practices uit ITAA-normen.

## Aanbevolen werkwijze

### 1. Maak een eindejaars-checklist op

Stel een gestructureerde lijst op van alle posten die op balansdatum gecontroleerd of aangepast moeten worden.

**Waarom?** Een checklist verzekert dat geen relevante verrichting wordt vergeten — sluitend bewijsstuk bij audit en controle.

**📥 Input**:
- Vorige jaarrekening + balansrubriek-overzicht → **Alle openstaande rubrieken** _(document)_

**📤 Output**:
- Eindejaars-checklist → **Per rubriek: vereiste actie + verantwoordelijke + deadline** _(document)_

**🛠️ Hoe**:

1. Loop alle balansrubrieken af en noteer welke actie nodig is:
   - Klasse 2: afschrijvingsdotaties, eventuele waardeverminderingen, herwaarderingen
   - Klasse 3 (voorraden): fysieke inventaris + waardering + waardeverminderingen
   - Klasse 4 (vorderingen/schulden): leveranciersafstemming, klanten-ouderdomsanalyse, btw-aansluiting
   - Klasse 5 (banken/kas): bankreconciliatie, kasstaat
   - Klasse 6/7: overlopende posten, voorzieningen, resultatenrekeningen
2. Documenteer in cliëntdossier.


**Grondslag**: [[regelmatige-boekhouding]] §eindejaars-procedure

### 2. Voer fysieke inventaris uit (klasse 3 + andere activa)

Tel en waardeer alle voorraden, controleer aanwezigheid en staat van vaste activa.

**Waarom?** Inventarisplicht is wettelijk; verschillen met boekhoudkundige stand wijzen op fouten of diefstal.

**📥 Input**:
- Inventaris-formulieren + magazijnplan → **Lokaal-overzicht, artikel-lijst** _(document)_

**📤 Output**:
- Inventarisstaat → **Werkelijke aantal × waardering = voorraad-waarde** _(balans)_

**🛠️ Hoe**:

1. Volg [[inventaris]] §opmaak — fysieke telling per lokaal/magazijn, bevestigingsbrieven aan klanten/leveranciers, bankbevestiging.
2. Waardeer voorraad volgens vastgelegde regels (FIFO of GGP) — zie competentie [[waarderen-en-boeken-voorraden-fifo-ggp]].
3. Vergelijk met boekhoudkundige stand op 31/12; boek inventarisverschillen via 60X of 70X.
4. Voor Meubelzaak Mertens BV — inventaris 30/12/2026, fysieke telling levert € 156.000 voorraad; boekhoudkundige stand € 159.500 → tekort € 3.500: D 609 Voorraadwijziging € 3.500; C 34 Handelsgoederen € 3.500.
5. Documenteer inventaris-rapport.


**Grondslag**: [[inventaris]] §opmaak, WER art. III.84

### 3. Boek alle resultaatsmatigingen (afschrijvingen, waardeverminderingen, voorzieningen, overlopende posten)

Voer de eindejaarsboekingen uit die het resultaat aanpassen aan economisch verbruik en risico's.

**Waarom?** Zonder deze boekingen geeft het resultaat geen getrouw beeld — kostencomponenten ontbreken of zijn niet correct toegerekend.

**📥 Input**:
- Eindejaars-checklist stap 1 + inventaris stap 2 → **Te boeken bedragen per categorie** _(berekening)_

**📤 Output**:
- Pakket eindejaarsboekingen → **Set journaalposten** _(boekingsregel)_

**🛠️ Hoe**:

1. Afschrijvingen — volg afschrijvingstabel; boek per categorie. Zie competentie [[opstellen-afschrijvingsplan-vaste-activa]].
2. Waardeverminderingen — toets dubieuze klanten en incourante voorraden. Zie competentie [[boeken-waardeverminderingen-op-vorderingen-en-voorraden]].
3. Voorzieningen — toets nieuwe risico's + aanpassing bestaande. Zie competentie [[boeken-voorzieningen-voor-risicos-en-kosten]].
4. Overlopende rekeningen — toepassing matching-principe. Zie competentie [[verwerken-overlopende-rekeningen-matching]].
5. Btw-eindafsaldering — saldeer 411 en 451; boek 4500 te betalen of 4110 terug te vorderen.
6. Bezoldigingen, vakantiegeld, eindejaarspremie — toets aansluiting met sociaal secretariaat.
7. Belastingschattingen — boek voorlopige belastingschuld op 6700 / 4500.


**Grondslag**: [[afschrijvingen]] §dotatie, [[waardeverminderingen]] §boeking-vorderingen, [[voorzieningen]] §boeking, [[overlopende-rekeningen]] §boeking

### 4. Stel de proefbalans en saldibalans op

Bereken alle rekening-saldi en toets de gelijkheid debet=credit.

**Waarom?** De proefbalans bewijst dat het dubbel-boekhoudsysteem mathematisch sluit; saldibalans is basis voor jaarrekening.

**📥 Input**:
- Centralisaties grootboek → **Per rekening: bewegingen + saldo** _(balans)_

**📤 Output**:
- Proef- en saldibalans → **Rekening | debet-totaal | credit-totaal | saldo** _(balans)_

**🛠️ Hoe**:

1. Voor elke rekening: bereken ∑ debet en ∑ credit; netto saldo = ∑ debet - ∑ credit (positief = debetsaldo, negatief = creditsaldo).
2. Som alle debet-totalen en credit-totalen — moet gelijk zijn (controle door balans).
3. Bij ongelijkheid: foutopsporing — meest voorkomende oorzaken: dubbele boeking, fout tegenrekening, btw-fout, overdracht-fout.
4. Documenteer proefbalans als bewijs van sluitende boekhouding.


**Grondslag**: [[regelmatige-boekhouding]] §proefbalans

### 5. Genereer voorlopige jaarrekening en bestemming resultaat

Stel op basis van saldibalans de balans en resultatenrekening op + bereken resultaat van het boekjaar.

**Waarom?** Jaarrekening is wettelijk vereist als afsluiting boekjaar; bestemming resultaat moet door algemene vergadering goedgekeurd worden.

**📥 Input**:
- Saldibalans stap 4 → **Saldi per rekening** _(balans)_

**📤 Output**:
- Voorlopige balans + resultatenrekening → **Schema KB-WVV** _(balans)_

**🛠️ Hoe**:

1. Klasseer saldi: klasse 1-2 op actief (uitzondering: gecumuleerde afschr. negatief presenteren), klasse 1-4-5 op passief/actief volgens debet- of creditsaldo, klasse 6 als kost in resultaat, klasse 7 als opbrengst.
2. Bereken resultaat = ∑ opbrengsten (klasse 7) - ∑ kosten (klasse 6).
3. Bij Mertens BV — voorbeeld: opbrengsten € 1.250.000 - kosten € 1.183.000 = winst € 67.000. Boek: D 692 Te bestemmen winst € 67.000; C 14 Overgedragen resultaat € 67.000 (voorlopig).
4. Bereid voorstel resultaatbestemming voor algemene vergadering — zie competentie [[boeken-resultaatverwerking-en-bestemming]].
5. Verlies-jaar: omgekeerde boeking via 691.


**Grondslag**: [[jaarrekening]] §opmaak, [[regelmatige-boekhouding]] §resultaatberekening, KB-WVV art. 3:1


## Voorbeelden

> [!example]- Meubelzaak Mertens BV op 31/12/2026 — eindejaar
> **Conclusie**: Sequentie: (1) checklist opmaken; (2) fysieke inventaris 30/12 — verschil € 3.500 in min op voorraad; (3) afschrijvingen € 35.000 totaal + waardeverminderingen klant Wegener € 3.512; (4) voorzieningen geen nieuwe + overlopende rekeningen € 9.000 op 490; (5) proefbalans opstellen, debet=credit € 4.518.500; (6) resultaat € 67.000 winst → voorlopig op 14 Overgedragen resultaat.
>
> **Grondslag**: [[regelmatige-boekhouding]] §eindejaar; [[inventaris]] §opmaak
>
> **Redenering**: Sequentie respecteert afhankelijkheden: inventaris vóór waardevermindering voorraad, afschrijving vóór resultaat. Verschil voorraad direct via 609.

> [!example]- Naaiatelier Ninove BV — proefbalans 31/12/2026 toont debet-totaal € 2.345.500 en credit-totaal € 2.349.000
> **Conclusie**: NIET overgaan tot jaarrekening — fout opsporen. Verschil € 3.500 wijst vaak op een rekening die enkel gedebiteerd is zonder tegenpost (of omgekeerd). Volg systematiek: btw-aansluiting (411/451), klanten-leveranciers reconciliaties, dagboek-controlebalans.
>
> **Grondslag**: [[regelmatige-boekhouding]] §controle-door-de-balans
>
> **Redenering**: Onsluitende boekhouding maakt jaarrekening ongeldig. Foutopsporing eerst — pas dan kunnen eindejaars-verrichtingen voltooid worden.

> [!example]- Praktijk Persenaire (vereenvoudigde boekhouding eenmanszaak) moet ook een inventaris opmaken
> **Conclusie**: Ja — inventarisplicht (WER art. III.84) geldt ook voor vereenvoudigde boekhouding. Vereenvoudigde inventaris volstaat: lijst van openstaande vorderingen/schulden, voorraad bij benadering, vaste activa volgens fiscale afschrijvingstabel.
>
> **Grondslag**: [[inventaris]] §toepassingsgebied; WER art. III.84
>
> **Redenering**: Inventaris is universele plicht; alleen de complexiteit van waardering kan vereenvoudigd zijn — niet de plicht zelf.


## Gebaseerd op concepten

[[inventaris]] · [[afschrijvingen]] · [[waardeverminderingen]] · [[voorzieningen]] · [[overlopende-rekeningen]] · [[regelmatige-boekhouding]] · [[jaarrekening]]
## Voortkomend uit

- **Taken**: 1.1.taak.1
- **Kenniselementen**: 1.1.II, 1.1.I.A
