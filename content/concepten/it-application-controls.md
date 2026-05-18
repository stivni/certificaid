---
title: IT application controls
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.X
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/it-application-controls.json
gegenereerd_op: '2026-05-18'
---
# IT application controls ⚖️

Application controls (toepassings-controles) zijn de geautomatiseerde of handmatige controles binnen een specifieke IT-applicatie die de volledigheid, juistheid en autorisatie van transacties bewaken. Ze werken op transactie-niveau, in tegenstelling tot ITGC die op omgevings-niveau werken. Stagiairs herkennen ze als input checks, geprogrammeerde validaties en three-way matches in ERP-systemen.

> [!summary] Korte inhoud
> IT application controls zijn de geautomatiseerde of handmatige controles ingebouwd in een specifieke IT-applicatie die toezien op invoer, verwerking en uitvoer van transacties, met als doel volledigheid, juistheid en autorisatie te waarborgen.

> [!info] Behoort tot: [[geinformatiseerde-omgeving-ic]]

IT application controls zijn de geautomatiseerde of handmatige controles ingebouwd in een specifieke IT-applicatie die toezien op invoer, verwerking en uitvoer van transacties, met als doel volledigheid, juistheid en autorisatie te waarborgen.

_Bron: ISA 315 (herzien-2019) Bijlage 5_


## Bouwstenen

### Input controls ⚖️

Validaties bij invoer: verplichte velden, formaat-checks, range-checks, dubbele invoer voor kritische velden zoals IBAN, key-validaties tegen masterdata.

**Waarom?** Fouten die aan de invoerzijde glippen zijn duur te corrigeren en kunnen tot materiële afwijkingen leiden.


**In de praktijk**: Een ERP weigert een verkoopfactuur zonder klant uit het klantmaster; het IBAN-veld wordt op modulus-11 gecheckt; een datum mag niet in de toekomst staan voor een leveringsbon.


_Grondslag: ISA 315 Bijlage 5 par. 1 + audit-doctrine_

### Processing controls ⚖️

Controles binnen de verwerking: geautomatiseerde berekeningen, accumulatie-controles, sequentiële nummering, geautomatiseerde three-way match en cut-off-routines.

**Waarom?** ISA 315 noemt geautomatiseerde controles betrouwbaarder dan handmatige bij grote volumes terugkerende transacties.


**In de praktijk**: Btw-berekening op factuur is automatisch op basis van btw-code; sequentiële nummering van verkoopfacturen verhindert het schrappen van transacties; een rapport van delivery notes zonder factuur draait elke maand.


_Grondslag: ISA 315 Bijlage 5 par. 2_

### Output controls ⚖️

Controles op uitvoer: reconciliaties tussen systemen, automatische rapportering, exception-rapporten en goedkeuring van kritische output.

**Waarom?** Uitvoer is wat het management en externe gebruikers gebruiken; een fout in een geautomatiseerd rapport plant zich voort in beslissingen en in de jaarrekening.


**In de praktijk**: Maandelijkse reconciliatie tussen ERP-omzet en btw-aangifte; exception-rapport van facturen boven een drempel zonder goedkeuring; goedgekeurd loonbestand vóór upload naar de bank.


_Grondslag: ISA 315 Bijlage 5 par. 3_


## In de praktijk

<h3 id="application-controls-zonder-itgc-zijn-niet-betrouwbaar">Application controls zonder ITGC zijn niet betrouwbaar</h3>

> [!tip]- Application controls zonder ITGC zijn niet betrouwbaar
> Application controls vooronderstellen dat de onderliggende IT-omgeving (toegang, change management, operations) integer is. Als ITGC tekortschieten, kan een ontwikkelaar een geprogrammeerde validatie omzeilen of uitschakelen — en dan zegt de geautomatiseerde controle niets meer over de werking ervan. ⚖️


> [!info]- Niet verwarren met [[]]
> Application controls werken op transactie-niveau binnen één specifieke applicatie (drempel-check, three-way match, btw-berekening). ITGC werken op omgevings-niveau over alle applicaties (toegang, change, operations) en ondersteunen de werking van application controls. Application controls zonder ITGC zijn niet betrouwbaar te testen.
>
> _Trigger_: Examenvraag: 'classificeer deze controle' — beslis op basis van scope (binnen één applicatie versus over de IT-omgeving).


## Valkuilen

> [!warning]- Een geautomatiseerde controle is niet hetzelfde als een effectieve controle
> ⚠️ Een geautomatiseerde controle is niet hetzelfde als een effectieve controle. Audit-stap: toets de configuratie (welke regels zijn actief), de toleranties (handmatige overrides), en het exceptie-proces (wie keurt afwijkingen goed). 🤖


> [!warning]- Application controls in commerciële software (zoals een ERP) zijn vaak configureerbaar — wijzigingen aan parameters kunnen ze effectief uits…
> ⚠️ Application controls in commerciële software (zoals een ERP) zijn vaak configureerbaar — wijzigingen aan parameters kunnen ze effectief uitschakelen. Een ITGC over change management op deze configuratie is daarom essentieel. ⚖️
>
> _Bron: ISA 315 Bijlage 5 par. 6_



## Zie ook

- **Vereist kennis van**: [[it-general-controls]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-5_part2`
[^2]: `ISA-315-herzien-2019__sec_bijlage-5_part3`
