---
title: Stromen in de onderneming
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.II.C
- 1.7.II
- 1.7.II.B
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/stromen-onderneming.json
gegenereerd_op: '2026-05-18'
---
# Stromen in de onderneming 🤖

Het stromen-begrip is in PO 1.7 cruciaal omdat IC-ontwerp begint bij stroom-analyse: waar ontstaat een transactie, langs welke handen passeert ze, waar wordt ze geregistreerd? Voor de stagiair is dit de brug naar cyclusanalyse (PO 1.6 audit): elke aankoop-, verkoop-, voorraad- of personeels-cyclus volgt een stroom. Examen-vragen vragen vaak om controles aan stroompunten te koppelen ('waar in deze stroom zou je een vier-ogen-controle inbouwen?').

> [!summary] Korte inhoud
> Stromen zijn de bewegingen van goederen, geld of informatie door de onderneming.

> [!info] Behoort tot: [[informatiesysteem-onderneming]]

Stromen zijn de bewegingen van goederen, geld of informatie door de onderneming. Voor IC kritisch omdat elke stroom potentiële uitlek-, verlies- of manipulatiepunten heeft. Drie hoofdstromen: (1) fysieke (goederen, voorraad), (2) financiële (geld, vorderingen, schulden), (3) informatie (documenten, data). De drie moeten onderling afgestemd zijn — bij elke fysieke beweging hoort een informatie- en typisch ook financiële tegenpost.


## Bouwstenen

### Drie hoofdstromen — fysiek, financieel, informatie 🤖

Fysieke stroom = goederen en personen (productieflow, voorraad, magazijn). Financiële stroom = geld (vorderingen, schulden, kas, bank). Informatiestroom = documenten en data (bestelbonnen, facturen, boekhoudgegevens).

**Waarom?** De drie zijn gekoppeld: bij elke fysieke beweging hoort een informatie-tegenpost en typisch ook een financieel gevolg. IC ontwerpt controles aan de aansluitingspunten.




_Grondslag: Bedrijfsvoerings-doctrine + ISA 315 cyclus-aanpak_

### Aansluitingspunten als IC-hot-spots 🤖

Waar twee stromen elkaar kruisen (bv. goederenontvangst ↔ inboeking factuur, betaling ↔ bankafschrift) is het natuurlijke punt voor controle. Aansluitingsbreuken (bv. ontvangst zonder bon, betaling zonder factuur) zijn de meest voorkomende foutbron.

**Waarom?** IC-effectiviteit hangt af van of aansluitingscontroles werken — niet of er veel controles bestaan.


**In de praktijk**: Vraag op IC-review: kun je voor één willekeurige aankoop het volledige spoor reconstrueren? Zo niet → ontwerpfout.


_Grondslag: Cyclus-doctrine_

### Stromen mappen op cycli (aankoop / verkoop / voorraad / HR) 🤖

In de IC-praktijk worden stromen niet apart bekeken, maar per bedrijfscyclus geïntegreerd: aankoopcyclus = bestelstroom + ontvangstreglement + factuurverwerking + betalingsstroom; verkoopcyclus = orderstroom + leveringsstroom + facturatiestroom + ontvangststroom; voorraadcyclus = mutatiestroom + telstroom + waarderingsstroom. Elke cyclus stelt eigen risico's en eigen controles.

**Waarom?** Cyclus-aanpak is de operationele entrée voor ISA 315 risk assessment: per cyclus identificeert de auditor de relevante beweringen (completeness, accuracy, cut-off, valuation) en de controles die ze afdekken.


**In de praktijk**: Bij IC-walkthrough: kies één transactie per cyclus en volg hem letterlijk door de drie stromen. Aansluiting-issues (fysieke levering zonder boeking, betaling zonder factuur) verschijnen meteen.


_Grondslag: ISA 315 cyclus-aanpak + IC-doctrine_


## In de praktijk

<h3 id="cycli-mappen-op-stromen">Cycli mappen op stromen</h3>

> [!tip]- Cycli mappen op stromen
> Elke cyclus (aankoop, verkoop, productie, HR, voorraad) heeft een typische combinatie van fysieke + financiële + informatiestromen. IC-analyse start met het mappen van die stromen — wie initieert, wie volgt op, wie registreert. 🤖


## Valkuilen

> [!warning]- Stromen alleen denken als 'goederenstromen' (productie-bias)
> ⚠️ Stromen alleen denken als 'goederenstromen' (productie-bias). In diensten-bedrijven dragen vooral informatie- en financiële stromen het IC-ontwerp. 🤖



## Zie ook

- **Vereist kennis van**: [[cyclus-analyse-ic]]

## Voorbeelden

Bij Yperse Werkplaats BV: een aankoop van staalplaten start met bestelbon (informatie), gevolgd door levering (fysiek), goederenontvangstbon (informatie), factuur (informatie), betaling via bank (financieel). Magazijnier Bart Maes tekent de goederenontvangstbon; boekhouder Karen De Backer matcht bestelbon-ontvangstbon-factuur (vier-ogen-aansluitingspunt) vóór betaling.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3`
