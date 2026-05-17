---
title: Onveranderlijkheid van de boekingen
tags:
- concept
- beginsel
- po-1-1
- po-1-2
linked_anchors:
- 1.1.I
- 1.1.I.A
- 1.1.I.B
- 1.2.III
- 1.2.III.D
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: beginsel
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/onveranderlijkheid-boekingen.json
gegenereerd_op: '2026-05-17'
---
# Onveranderlijkheid van de boekingen ⚖️

> [!summary] Korte inhoud
> Een boeking mag **na inschrijving niet onzichtbaar gewijzigd, weggelaten of toegevoegd** worden.

> [!info] Behoort tot: [[boekhoudbeginselen-overzicht]] · [[regelmatige-boekhouding]]

Een boeking mag **na inschrijving niet onzichtbaar gewijzigd, weggelaten of toegevoegd** worden. Wijzigingen zijn wel toegelaten, maar moeten **duidelijk leesbaar blijven** — het oorspronkelijke geschrevene én de correctie moeten allebei zichtbaar zijn. Hetzelfde geldt voor jaarrekening- en inventarisgegevens (WER art. III.84 jo. CBN 174/1).

_Bron: WER art. III.84_


## Bouwstenen

### Geen verborgen wijziging ⚖️

Wijzigingen aan een eerdere boeking mogen niet 'onzichtbaar' worden aangebracht: niet overschrijven, niet uitvegen, niet schrappen zonder zichtbaar spoor.

**Waarom?** Onzichtbare wijzigingen vernietigen de controleerbaarheid: niemand kan dan nog vaststellen wat oorspronkelijk geboekt was.

**Voorbeeld**: Een papieren dagboek met een uitgeveegde regel waar nu een ander bedrag staat = schending van onveranderlijkheid. In een softwarepakket: een 'edit'-knop die het origineel overschrijft zonder log = idem schending.

_Grondslag: WER art. III.84; CBN 174/1_

### Correctie wel toegelaten — maar zichtbaar ⚖️

Fouten of vergetelheden mogen worden rechtgezet, op voorwaarde dat zowel het origineel als de correctie volledig leesbaar blijven. Typisch via een tegenboeking op huidige datum.

**Waarom?** De wet wil geen bevriezing van fouten, maar transparantie over correcties. Beide perspectieven (wat eerst stond, wat nu staat) blijven beschikbaar voor controle.

**Voorbeeld**: Naaiatelier Ninove BV ontdekt op 15 april dat een afschrijving van januari met € 1.200 te hoog werd geboekt. Correctie op 15 april: tegenboeking € 1.200 (Debet 22 / Credit 630), verwijzing 'corr. boeking nr. 22 d.d. 31/1, fout afschrijvingsbasis'.

_Grondslag: WER art. III.84; CBN 174/1_

### Geldt ook voor jaarrekening en inventaris ⚖️

Niet alleen dagboekboekingen vallen onder het beginsel; ook de jaarrekening en de inventarisgegevens mogen niet stilzwijgend worden gewijzigd na vaststelling.

**Waarom?** De jaarrekening is het kernartefact dat met derden wordt gedeeld (NBB-neerlegging). Achteraf 'aanpassen' zou de derde misleiden.

**Voorbeeld**: Indien Rotex Roeselare NV na neerlegging een fout in de balans 20X1 ontdekt: NIET stilzwijgend de neergelegde versie vervangen, wel via een formele rechtzettings-procedure (en gecorrigeerde versie expliciet als zodanig vermelden).

_Grondslag: CBN 174/1_


## In de praktijk

<h3 id="software-implementatie">Software-implementatie</h3>

> [!tip]- Software-implementatie
> Boekhoudsoftware moet wijzigingen aan reeds geboekte verrichtingen onmogelijk maken — of zichtbaar maken via een audit trail. Een 'update'-functie die overschrijft zonder log is in strijd met het beginsel. 🤖

> [!tip]- Herkennen op het examen
> Examen / fiscaal: vraag over de bewijskracht van een digitale boekhouding waar bedragen geretroactief zijn aangepast → onveranderlijkheid geschonden, bewijskracht aangetast.


## Valkuilen

> [!warning]- Onveranderlijkheid betekent NIET 'fouten mogen niet gecorrigeerd worden'
> ⚠️ Onveranderlijkheid betekent NIET 'fouten mogen niet gecorrigeerd worden'. Wel: de correctie moet expliciet en zichtbaar gebeuren — via tegenboeking, niet via overschrijving. ⚖️
>
> _Bron: CBN 174/1_


> [!warning]- Onveranderlijkheid is één van meerdere regelmatigheidsbeginselen; ze volstaat NIET op zich om de boekhouding bewijskrachtig te maken
> ⚠️ Onveranderlijkheid is één van meerdere regelmatigheidsbeginselen; ze volstaat NIET op zich om de boekhouding bewijskrachtig te maken. CBN 174/1 benadrukt: volledigheid is minstens even belangrijk. ⚖️
>
> _Bron: CBN 174/1_



## Bronnen

[^1]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_draagwijdte-van-het-beginsel-van-de-onveranderlijkheid-van-d`
[^2]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_boekhoudrechtelijke-invalshoek`
