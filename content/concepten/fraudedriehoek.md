---
title: Fraude-driehoek (motief – gelegenheid – rationalisatie)
tags:
- concept
- begrip
- po-1-6
- po-1-7
linked_anchors:
- 1.7.VI
- 1.7.VI.B
- 1.6.II.B
programmaonderdelen:
- '1.6'
- '1.7'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/fraudedriehoek.json
gegenereerd_op: '2026-05-18'
---
# Fraude-driehoek (motief – gelegenheid – rationalisatie) ⚖️

De fraude-driehoek (Donald Cressey, 1953) is het diagnostische kader dat ISA 240 §A1 hanteert om te beschrijven onder welke omstandigheden fraude ontstaat. Voor de stagiair is dit een centraal denkkader: het verklaart waarom IC primair op één element kan aangrijpen — gelegenheid — terwijl de andere twee buiten de greep van de onderneming liggen. Bij elke fraude-risico-inschatting (verplicht onder ISA 240) toetst de auditor of de drie elementen aanwezig zijn.

> [!summary] Korte inhoud
> De fraude-driehoek beschrijft drie voorwaarden die samen aanwezig zijn wanneer fraude wordt gepleegd: (1) een stimulans of druk om te frauderen (motief), (2) een waargenomen gelegenheid om de interne beheersing te doorbreken, en (3) een rechtvaardiging waarmee de pleger de handel….

> [!info] Behoort tot: [[fraude]]

De fraude-driehoek beschrijft drie voorwaarden die samen aanwezig zijn wanneer fraude wordt gepleegd: (1) een stimulans of druk om te frauderen (motief), (2) een waargenomen gelegenheid om de interne beheersing te doorbreken, en (3) een rechtvaardiging waarmee de pleger de handeling voor zichzelf aanvaardbaar maakt. Het wegnemen van één element verkleint significant het fraude-risico — en daarom mikt sterke IC vooral op het verkleinen van gelegenheid.

_Bron: ISA 240 §A1_


## Bouwstenen

### Motief — stimulans of druk ⚖️

De druk of stimulans die de pleger ertoe brengt fraude te overwegen. Kan persoonlijk zijn (financiële stress, gokverslaving, levensstijl-druk) of organisationeel (winstdoelstellingen, bonus-targets, dreiging van ontslag).

**Waarom?** Zonder druk is er geen aanleiding tot fraude. Bij management-druk om winst te halen wordt frauduleuze financiële verslaggeving waarschijnlijker; bij persoonlijke druk eerder oneigenlijke toeëigening van activa.


**In de praktijk**: De auditor herkent dit aan: agressieve targets, stockoptie-plannen met cliff-dates, debiteur-leveringen vlak vóór jaareinde, persoonlijke financiële stress bij sleutel-personen (publiek bekend of geruchten).


_Grondslag: ISA 240 §A1 + Cressey (1953)_

### Gelegenheid — doorbreking van IC mogelijk ⚖️

De pleger meent dat de interne beheersing kan worden omzeild: zwakke functiescheiding, geen onafhankelijke review, vertrouwenspositie zonder controle, of een management-override-cultuur.

**Waarom?** Dit is het ENIGE element dat de onderneming direct via IC kan verkleinen — daarom de hefboom voor preventief IC-ontwerp.


**In de praktijk**: Concrete gelegenheids-indicatoren: één persoon doet aankoop + goedkeuring + betaling, geen periodieke rotatie van functies, niemand reviewt de hoogste-niveau-handtekeningen, ERP-superuser zonder log.


_Grondslag: ISA 240 §A1 + COSO 2013 component 3 (beheersactiviteiten)_

### Rationalisatie — argumenten om de handeling te rechtvaardigen ⚖️

De interne narratief waarmee de pleger zijn handeling voor zichzelf aanvaardbaar maakt: 'ik leen het maar', 'iedereen doet het', 'ze betalen me te weinig', 'het bedrijf merkt het toch niet', 'ik geef het later terug'.

**Waarom?** Zelfs eerlijke personen kunnen fraude plegen wanneer de omgevingsdruk groot genoeg is en een rationalisatie zich aanbiedt (ISA 240 §A1). Tone-at-the-top en gedragscode verkleinen rationalisatie-ruimte.


**In de praktijk**: Detectie indirect: cultuur-onderzoek, exit-interviews, klokkenluiderkanaal als signaalmechanisme. Sterke ethische cultuur + voorbeeldgedrag van leidinggevenden vermindert het rationalisatie-element.


_Grondslag: ISA 240 §A1 + Cressey (1953)_


## In de praktijk

<h3 id="diagnostisch-gebruik-door-auditor">Diagnostisch gebruik door auditor</h3>

> [!tip]- Diagnostisch gebruik door auditor
> Bij elke audit-engagement-bespreking (ISA 240 §16) toetsen de teamleden waar in de entiteit alle drie elementen samenkomen. Dat is de prioritaire fraude-risk-locatie. Het is geen bewijs — wel een waarschuwingssignaal dat extra controlewerkzaamheden noodzakelijk maakt. ⚖️

<h3 id="ic-ontwerp-implicatie">IC-ontwerp-implicatie</h3>

> [!tip]- IC-ontwerp-implicatie
> Een goed IC-systeem verkleint primair de 'gelegenheid' via functiescheiding, controle-instrumenten en monitoring. Motief en rationalisatie worden indirect verkleind via tone-at-the-top, gedragscode, transparante remuneratie, eerlijke targets. 🤖


## Valkuilen

> [!warning]- Eén element zien betekent NIET dat fraude is gepleegd — het is een waarschuwing dat de gelegenheid bestaat of de druk hoog is
> ⚠️ Eén element zien betekent NIET dat fraude is gepleegd — het is een waarschuwing dat de gelegenheid bestaat of de druk hoog is. Bewijs van opzet blijft vereist alvorens 'fraude' te kwalificeren. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[controle-omgeving]]

## Voorbeelden

### De drie elementen bij Yperse Werkplaats BV

_Personages: Yperse Werkplaats BV, Tom Lefèvre_

Aankoopdirecteur Tom Lefèvre van Yperse Werkplaats BV bouwt over een jaar een schaduw-leveranciersfraude op van € 280.000.

Motief: persoonlijke gokschulden + recente echtscheiding (extern bekend bij collega's, niet bij management).
Gelegenheid: Tom mag zowel leveranciers goedkeuren als facturen tekenen voor betaling onder € 50.000 — functiescheiding ontbreekt voor 'mid-range' transacties (alleen ingericht > € 50.000).
Rationalisatie: 'ik werk al 15 jaar onderbetaald hier, dit is wat ik verdien' (gemeld in klokkenluider-melding nà ontslag).
Conclusie: alle drie elementen aanwezig → fraude. IC-respons: drie-weg-match verplicht voor alle nieuwe leveranciers; functiescheiding aankoop/betaling ook onder € 50.000.


## Bronnen

[^1]: `ISA-240__sec_toepassingsgerichte-en-overige-verklarende-teksten_2_part2`
[^2]: `ISA-240__sec_toepassingsgerichte-en-overige-verklarende-teksten`
