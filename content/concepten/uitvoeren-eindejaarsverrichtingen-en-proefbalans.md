---
title: Uitvoeren van eindejaarsverrichtingen en opmaken van proefbalans
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II
- 1.1.I.A
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/uitvoeren-eindejaarsverrichtingen-en-proefbalans.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van eindejaarsverrichtingen en opmaken van proefbalans 🤖

De brug-competentie tussen de dagelijkse boekhouding en de jaarrekening: inventaris, afschrijvingen, waardeverminderingen, voorzieningen, overlopende rekeningen worden samen in één eindjaars-cyclus afgewerkt. Voor een stagiair-GA: de proefbalans vóór en na eindjaarsverrichtingen is een vast examen-artefact dat de volledigheid en juistheid van de cyclus toetst.


## Stappen

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





