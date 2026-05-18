---
title: Beheersactiviteiten (COSO-component 3)
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VIII.D
- 1.7.VIII
- 1.7.X.D
- 1.7.III.A
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/beheersactiviteiten.json
gegenereerd_op: '2026-05-18'
---
# Beheersactiviteiten (COSO-component 3) ⚖️

Beheersactiviteiten zijn COSO-component 3 — de concrete laag waar abstract risico wordt vertaald naar dagelijkse handelingen die het IC-systeem maken werken. In ISA 315 (herzien-2019) genoemd als één van de vijf componenten die de auditor moet begrijpen vóór risk assessment. Voor de stagiair een centraal begrip: examen-vragen testen of hij beheersactiviteiten kan typeren (preventief vs detectief, manueel vs geautomatiseerd, vier categorieën) en aan concrete risico's koppelen.

> [!summary] Korte inhoud
> Beheersactiviteiten zijn de concrete procedures en handelingen die de onderneming inzet om de geïdentificeerde risico's te beheersen.

> [!info] Behoort tot: [[interne-controle]]

Beheersactiviteiten zijn de concrete procedures en handelingen die de onderneming inzet om de geïdentificeerde risico's te beheersen. Ze omvatten zowel preventieve (vóór de transactie) als detectieve (na de transactie) maatregelen, en kunnen manueel of geautomatiseerd zijn. Vormen samen COSO-component 3 — de uitvoerende laag van het IC-systeem.

_Bron: ISA 315 (herzien-2019) §A86 + COSO 2013 component 3_


## Bouwstenen

### Vier hoofdcategorieën 🤖

(1) Autorisaties + goedkeuringen (wie mag wat tot welk bedrag). (2) Verificaties + afstemmingen (kruiscontrole tussen registers, bank-grootboek). (3) Functiescheiding (zie [[functiescheiding]]). (4) Fysieke controles (toegangsbeperking magazijn, sleutels, alarm).

**Waarom?** Een goed IC-systeem combineert minstens uit elke categorie — geen enkele aanpak dekt alles af.



Bij Yperse Werkplaats BV: toegangsbadge magazijn (fysiek) + dubbele handtekening boven drempel (autorisatie) + maandelijkse stockcount door extern (verificatie) + scheiding aankoop/ontvangst/betaling (segregation).

_Grondslag: COSO-doctrine_

### Preventief versus detectief 🤖

Preventief = ontwerpt fouten/fraude weg vóór ze gebeuren (autorisaties, functiescheiding). Detectief = ontdekt fouten/fraude nadat ze gebeurd zijn (afstemmingen, inventaris, analyse). Een sluitend systeem gebruikt beide.

**Waarom?** Preventief alleen verzwakt door management override; detectief alleen laat fouten doorlopen tot de detectie — soms te laat.




_Grondslag: COSO-doctrine_

### Manuele versus geautomatiseerde controls ⚖️

Manueel = een mens beslist en tekent af (handtekening op factuur, paraaf op reconciliatie, oog-check op voorraad). Geautomatiseerd = het systeem dwingt zelf af (ERP blokkeert input buiten range, drie-weg-match-validatie, audit trail). Geautomatiseerd is consistenter; manueel is flexibeler bij uitzondering.

**Waarom?** Bij een audit op IT-zware processen (zie ISA 315 §A87 schaalbaarheid) zijn geautomatiseerde controls vaak betrouwbaarder mits de general IT controls (toegang, change management) ook werken. Bij KMO's met beperkte IT-volwassenheid blijven manuele controls dominant.


**In de praktijk**: Bij Yperse Werkplaats BV: drie-weg-match in ERP (geautomatiseerd, > € 0) + dubbele handtekening boven € 25.000 (manueel) + maandelijkse reconciliatie door externe accountant (manueel + extern).


_Grondslag: ISA 315 (herzien-2019) §13 + §A86_


## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

## Voorbeelden

Bij Yperse Werkplaats BV: (preventief) facturen > € 25.000 vereisen handtekening van CFO David; (detectief) maandelijkse afstemming bank-grootboek door iemand anders dan de boeker; (geautomatiseerd) ERP weigert input van prijs > 20% afwijking van laatste aankoopprijs zonder override.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3`
[^2]: `ISA-315-herzien-2019__sec_schaalbaarheid_13_part3`
