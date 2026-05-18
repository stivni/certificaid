---
title: Functiescheiding (segregation of duties)
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VII
- 1.7.VIII.B
- 1.7.X.C
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/functiescheiding.json
gegenereerd_op: '2026-05-18'
---
# Functiescheiding (segregation of duties) 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


Functiescheiding is het verdelen van vier kritische taken — autoriseren, uitvoeren, bewaren en registreren — over verschillende personen zodat geen enkele individu een transactie van begin tot einde kan controleren. Doel: fouten ontdekken door natuurlijke kruiscontrole en fraude bemoeilijken door samenspanning nodig te maken.

> [!info] Behoort tot: [[interne-controle]]


## Bouwstenen

### Vier kritische functies 🤖

(1) Autoriseren: beslissing nemen of een transactie mag plaatsvinden (bv. inkoop goedkeuren). (2) Uitvoeren: de fysieke handeling doen (bestelling plaatsen, betaling uitvoeren). (3) Bewaren: bezit nemen van activa (magazijn, kas). (4) Registreren: boekhoudkundig vastleggen.

**Waarom?** Wie alle vier doet, kan elke transactie en zijn boekhoudkundige sporen manipuleren zonder controle.



Bij Meubelzaak Mertens BV deed één werknemer kasontvangsten + bankreconciliatie + boekhouding. Detectie van € 15.000 verduistering kwam pas na 2 jaar — gemiste functiescheiding.

_Grondslag: Internationaal audit-doctrine (COSO, ISA 315)_

### Incompatibele combinaties 🤖

Combinaties die nooit bij één persoon mogen liggen: (a) kasontvangst + bankboekingen, (b) voorraadbeheer + voorraadtelling, (c) HR-aanmeldingen + loonberekening + uitbetaling, (d) goederontvangst + factuurgoedkeuring.

**Waarom?** Elke combinatie geeft één persoon de macht om een fictieve transactie te creëren en de boekhoudkundige bewijzen te wissen.



Combinatie 'HR-aanmelding + loonbetaling' = risico op fictieve werknemer ('ghost employee'). Bij Yperse Werkplaats BV maakt HR de loonberekening; CFO David tekent het bestand digitaal vóór upload naar de bank.

_Grondslag: Internationaal audit-doctrine_

### KMO-uitdaging ⚖️

Bij kleine ondernemingen is volledige vier-functies-scheiding onmogelijk — er zijn niet genoeg mensen. Compensatie: meer betrokkenheid van de zaakvoerder (review van bankuittreksels, periodieke spot-checks) en externe revisie (boekhouder, accountant).

**Waarom?** Geen scheiding zonder compensatie = open deur voor fouten en fraude. De ITAA-norm-kmo-controlenorm erkent deze specifieke context.



Bij Praktijk Persenaire (eenmanszaak vrij beroep) doet de zaakvoerder alles zelf. Compensatie: de externe accountant doet maandelijks een kasreconciliatie en bekijkt de bankafschriften.

_Grondslag: ITAA-norm-kmo-controlenorm §96_


## In de praktijk

<h3 id="functiescheiding-in-it-omgeving-1-7-x-c">Functiescheiding in IT-omgeving (1.7.X.C)</h3>

> [!tip]- Functiescheiding in IT-omgeving (1.7.X.C)
> Bij geautomatiseerde systemen vertaalt functiescheiding zich in: (1) gebruikersprofielen met verschillende rechten, (2) audit trails die elke actie logmatig vastleggen, (3) developer-rechten gescheiden van productie-rechten. IT-administrators krijgen vaak alle rechten — beperkt en gemonitord houden. 🤖

<h3 id="examen-herkenningspunt">Examen-herkenningspunt</h3>

> [!tip]- Examen-herkenningspunt
> Bij elke casus: teken een matrix [persoon × functie]. Markeer waar één persoon meer dan één van de vier functies heeft. Elke combinatie is potentieel zwakke IC. 🤖


## Valkuilen

> [!warning]- Functiescheiding op papier is niet hetzelfde als in werking
> ⚠️ Functiescheiding op papier is niet hetzelfde als in werking. Test altijd of de scheiding daadwerkelijk wordt nageleefd — soms tekent één persoon namens 'iemand anders' bij afwezigheid, en dan valt het systeem. 🤖


> [!warning]- Management override doorbreekt functiescheiding altijd
> ⚠️ Management override doorbreekt functiescheiding altijd. Specifieke detectie: ongebruikelijke journaalposten, periode-einde-aanpassingen, transacties met geliëerde partijen. 🤖



## Zie ook

- **Wordt voorondersteld in** (8): [[aankoopcyclus-ic]] · [[fraude]] · [[geinformatiseerde-omgeving-ic]] · [[interne-controle]] · [[productiecyclus-ic]] · [[taakverdeling-ic]] · [[verkoopcyclus-ic]] · [[voorraadcyclus-ic]]
## Voorbeelden

Bij Yperse Werkplaats BV is een aankoop verdeeld over vier personen: (1) inkoper Anna autoriseert de bestelling, (2) magazijnier Bart neemt goederen in ontvangst, (3) boekhouder Cindy registreert de factuur, (4) financieel verantwoordelijke David tekent de betaling. Als één van hen iets verdraait, ontdekt iemand anders het in zijn kruiscontrole. Fraude vereist samenspanning van minstens twee — exponentieel moeilijker.

## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
