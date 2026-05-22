---
title: Functiescheiding
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
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/functiescheiding.json
gegenereerd_op: '2026-05-21'
---
# Functiescheiding 🔗

Functiescheiding is binnen het examenprogramma 1.7.VII het hoeksteen-principe van preventieve IC: door autoriseren, uitvoeren, bewaren en registreren te splitsen ontstaat natuurlijke kruiscontrole en wordt fraude alleen mogelijk via samenspanning. De ISA-norm en de ITAA KMO-controlenorm erkennen het principe expliciet, maar erkennen ook dat een KMO niet altijd volledige scheiding kan realiseren — dan zijn compenserende controles (review door bovenliggende laag, externe accountant, IT-afdwinging) verplicht.

> [!info] Behoort tot: [[interne-controle]]



## Bouwstenen

### Vier kritische functies ⚖️

Het audit-doctrinaire model verdeelt vier handelingen rond elke transactie over verschillende personen: (1) autoriseren — beslissen of een transactie mag plaatsvinden (bv. inkoop goedkeuren); (2) uitvoeren — de fysieke handeling doen (bestelling plaatsen, betaling initiëren); (3) bewaren — bezit van activa nemen (kas, magazijn, betaalmiddel); (4) registreren — boekhoudkundig vastleggen. ISA 315 Bijlage 3 §20 erkent autoriseren, vastleggen en bewaren expliciet; uitvoeren versus registreren is in de bredere doctrine als afzonderlijke functies losgemaakt.

**Waarom?** Als één persoon alle vier doet, kan hij fictieve transacties creëren én de boekhoudkundige sporen wissen zonder dat iemand het in de normale werking ziet.



Bij Meubelzaak Mertens BV deed één werknemer kasontvangsten + bankreconciliatie + boekhouding. Detectie van € 15.000 verduistering kwam pas na 2 jaar — gemiste functiescheiding.

_Grondslag: ISA 315 (herzien-2019) Bijlage 3 §20_

### Incompatibele combinaties ⚖️

Combinaties die nooit bij één persoon mogen liggen: (a) kasontvangst + bankboekingen, (b) voorraadbeheer + voorraadtelling, (c) HR-aanmeldingen + loonberekening + uitbetaling, (d) goederontvangst + factuurgoedkeuring.

**Waarom?** Elke combinatie geeft één persoon de macht om een fictieve transactie te creëren en de boekhoudkundige bewijzen te wissen.



Combinatie 'HR-aanmelding + loonbetaling' = risico op fictieve werknemer ('ghost employee'). Bij Yperse Werkplaats BV maakt HR de loonberekening; CFO David tekent het bestand digitaal vóór upload naar de bank.

_Grondslag: ISA 315 (herzien-2019) Bijlage 3 §20 (illustraties van verboden combinaties)_

### KMO-uitdaging ⚖️

Bij kleine ondernemingen is volledige vier-functies-scheiding onmogelijk — er zijn niet genoeg mensen. Compensatie: meer betrokkenheid van de zaakvoerder (review van bankuittreksels, periodieke spot-checks) en externe revisie (boekhouder, accountant).

**Waarom?** Geen scheiding zonder compensatie = open deur voor fouten en fraude. De ITAA-norm-kmo-controlenorm erkent deze specifieke context.



Bij Praktijk Persenaire (eenmanszaak vrij beroep) doet de zaakvoerder alles zelf. Compensatie: de externe accountant doet maandelijks een kasreconciliatie en bekijkt de bankafschriften.

_Grondslag: ITAA-norm-kmo-controlenorm §96_

### Functiescheiding in IT-omgeving — RBAC en admin-uitzondering ⚖️

Bij geautomatiseerde systemen wordt functiescheiding gerealiseerd via (1) Role-Based Access Control (RBAC): gebruikers krijgen rechten op basis van hun functie, niet ad hoc per persoon; (2) een SoD-matrix die alle combinaties van rollen toetst op incompatibiliteiten; (3) audit-trail-logging die elke transactie aan een gebruikersaccount koppelt; (4) scheiding tussen developer-rechten (test/dev-omgeving) en productie-rechten. De grote uitzondering: IT-administrators hebben technische rechten over alle rollen — daarvoor zijn aparte compenserende controles nodig (review van admin-acties door security officer, vier-ogen-principe op kritische admin-handelingen).

**Waarom?** ISA 315 (herzien-2019) Bijlage 6 §toegangsprivileges noemt expliciet 'controles over de toegang van beheerders of krachtige gebruikers' als apart aandachtspunt. Zonder RBAC-discipline ontstaan rechten-creep (cumulerende rechten over tijd) en gedeelde accounts (toegang aan onbekend identificeerbare persoon) — beide elimineren functiescheiding effectief.


**In de praktijk**: Concrete inrichting: (a) jaarlijkse user-access-review per applicatie waar elke gebruiker tegen zijn functiebeschrijving wordt gematcht; (b) joiner-mover-leaver-proces dat rechten meebeweegt met functie-wijzigingen; (c) SoD-matrix als configureerbare check in het ERP (bv. SAP GRC, Oracle Risk Cloud) die conflicterende rol-toekenningen blokkeert; (d) admin-acties op kritische tabellen worden gelogd naar een write-once-storage waar de admin zelf geen toegang toe heeft.

Bij Yperse Werkplaats BV heeft inkoper Tom de rol 'Inkoop_Aanvragen' (bestelling indienen, niet goedkeuren); CFO David heeft 'Finance_Approval' (goedkeuren > € 5.000). RBAC sluit uit dat één persoon beide rollen heeft. Maandelijkse SoD-audit-script meldt elke rol-combinatie buiten de SoD-matrix aan compliance officer Helena. 🤖
### Scenario

Bij Rotex Roeselare NV bleek tijdens een ITGC-audit dat sysadmin Maarten DBA-rechten + financiële module-rechten + log-rotatie-beheer had — drie incompatibele admin-functies. Compenserende controle ontbrak. Remediatie: log-rotatie naar aparte rol bij security officer, DBA-acties geforceerd via change-ticket met dubbele goedkeuring.
🤖



_Grondslag: ISA 315 (herzien-2019) Bijlage 6 §toegangsprivileges + functiescheiding-doctrine_


## In de praktijk

<h3 id="examen-herkenningspunt">Examen-herkenningspunt</h3>

> [!tip]- Examen-herkenningspunt
> Bij elke casus: teken een matrix [persoon × functie]. Markeer waar één persoon meer dan één van de vier functies heeft. Elke combinatie is potentieel zwakke IC. 🤖


## Valkuilen

> [!warning]- Functiescheiding op papier is niet hetzelfde als in werking
> ⚠️ Functiescheiding op papier is niet hetzelfde als in werking. Test altijd of de scheiding daadwerkelijk wordt nageleefd — soms tekent één persoon namens 'iemand anders' bij afwezigheid, en dan valt het systeem. 🤖


> [!warning]- Management override doorbreekt functiescheiding altijd
> ⚠️ Management override doorbreekt functiescheiding altijd. Specifieke detectie: ongebruikelijke journaalposten, periode-einde-aanpassingen, transacties met geliëerde partijen. 🤖



## Zie ook

- **Wordt voorondersteld in** (18): [[aankoopcyclus-ic]] · [[beheersactiviteiten]] · [[controlemiddelen-ic]] · [[cyclus-analyse-ic]] · [[fraude]] · [[fraudedriehoek]] · [[geinformatiseerde-omgeving-ic]] · [[hr-cyclus-ic]] · [[implementeren-functiescheiding-transactiecycli]] · [[interne-controle]] · [[it-general-controls]] · [[opvolging-verrichtingen-ic]] · [[preventief-versus-detecterende-controle]] · [[productiecyclus-ic]] · [[taakverdeling-ic]] · [[uitvoering-interne-controle]] · [[verkoopcyclus-ic]] · [[voorraadcyclus-ic]]
## Voorbeelden

Bij Yperse Werkplaats BV is een aankoop verdeeld over vier personen: (1) inkoper Anna autoriseert de bestelling, (2) magazijnier Bart neemt goederen in ontvangst, (3) boekhouder Cindy registreert de factuur, (4) financieel verantwoordelijke David tekent de betaling. Als één van hen iets verdraait, ontdekt iemand anders het in zijn kruiscontrole. Fraude vereist samenspanning van minstens twee — exponentieel moeilijker.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3_part5`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
[^3]: `ISA-315-herzien-2019__sec_bijlage-6-overwegingen-voor-het-verwerven-van-inzicht-in-gen`
