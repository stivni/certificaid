---
title: Controlemiddelen — concrete instrumenten
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VIII.D
- 1.7.VIII
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: inferred-from-aggregation
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/controlemiddelen-ic.json
gegenereerd_op: '2026-05-21'
---
# Controlemiddelen — concrete instrumenten 🔗

Controlemiddelen zijn de fysieke + digitale infrastructuur die beheersactiviteiten daadwerkelijk afdwingt — wat ISA 315 (herzien-2019) onderbrengt onder 'controle-instrumenten' van COSO-component 3. Voor de stagiair belangrijk om te begrijpen dat een control zonder middel niet uitvoerbaar én niet auditbaar is: zonder ondertekend formulier, ERP-flag, of audit-trail is er geen evidence en kan de auditor er niet op steunen (ISA 500 + ISA 330). Het examenprogramma 1.7.VIII.D vraagt de stagiair om concrete instrumenten te kunnen koppelen aan controle-doelen.

> [!summary] Korte inhoud
> Controlemiddelen zijn de concrete instrumenten — documenten, fysieke beveiligingen, IT-functies, procedurele artefacten — waarmee beheersactiviteiten daadwerkelijk worden uitgevoerd.

> [!info] Behoort tot: [[beheersactiviteiten]]

Controlemiddelen zijn de concrete instrumenten — documenten, fysieke beveiligingen, IT-functies, procedurele artefacten — waarmee beheersactiviteiten daadwerkelijk worden uitgevoerd. Het is de tastbare laag onder COSO-component 3: zonder middel kan een controle niet plaatsvinden én niet bewezen worden. Een sluitend IC-systeem combineert middelen uit alle vier categorieën (documenten, fysiek, IT, procedureel).



## Bouwstenen

### Documenten en formulieren ⚖️

Gestandaardiseerde papieren of digitale dragers met vaste velden, doorlopende nummering en verplichte goedkeuringsslots: bestelbon, ontvangstbon, factuur, kasstaat, urenstaat, reisnota. Het document is tegelijk middel én bewijs.

**Waarom?** Standaardvelden dwingen volledigheid af; doorlopende nummering maakt ontbrekende transacties zichtbaar; verplichte goedkeuringsslots realiseren autorisatie zonder extra handeling.


**In de praktijk**: Bij Yperse Werkplaats BV: bestelbon (5-cijferig opvolgnummer, paraaf inkoper, handtekening boven € 5.000), ontvangstbon (gekoppeld aan bestelbon-nummer), driewegmatch met factuur vóór betaling.

Een ontbrekend bestelbon-nummer in de reeks (bv. 1234 → 1236) signaleert ofwel een geannuleerde transactie ofwel een verwijderd document — beide vragen onderzoek.

_Grondslag: ISA 500 §A1-A3 (controle-informatie), CBN-advies 174/1 (volledigheid van boekingen)_

### Fysieke beveiligingen ⚖️

Toegangsbeperkingen die directe beschikking over activa regelen: sleutels, badges, kluizen, magazijnsloten, kassa-sloten, camerabewaking, alarmering, sloten op IT-rekken.

**Waarom?** Activa die fysiek niet bereikbaar zijn zonder identificatie en autorisatie genereren een ingebouwde scheiding tussen 'bewaring' en 'gebruik'. Spreekt direct met de vier-functies-doctrine (bewaring).


**In de praktijk**: Bij Yperse Werkplaats BV: magazijn alleen toegankelijk met badge gekoppeld aan rolprofiel; bestelmuntje voor goederenontvangst getekend door magazijnier; nachtcamera met cloud-opslag van 30 dagen.


_Grondslag: ISA 315 (herzien-2019) Bijlage 3 §20 (physical controls + segregation)_

### IT-instrumenten ⚖️

Geautomatiseerde controlemechanismen in software: rollenbeheer + wachtwoorden + multi-factor authenticatie, audit trails met user-id + timestamp, geautomatiseerde validaties (range-checks, drie-weg-match, mandatory fields), geautomatiseerde blokkades (kredietlimiet, betalingsdrempel), digitale handtekeningen, encryptie.

**Waarom?** IT-controls zijn consistenter dan menselijke (geen vermoeidheid, geen sociale druk), maar werken alleen als de general IT controls (toegang, change management) zelf werken — anders zijn ze omzeilbaar.


**In de praktijk**: Bij Yperse Werkplaats BV: ERP weigert inkoopfactuur zonder gekoppelde ontvangstbon; bank-platform vraagt digitale handtekening + SMS-code boven € 25.000; audit trail logt elke prijswijziging met user + datum + oude/nieuwe waarde.

Bij een audit van Rotex Roeselare NV trekt de auditor de audit trail-export op alle journaalposten van december (uniform reeks). Drie posten geboekt door super-user buiten kantooruren — onderzoek toont legitieme jaarafsluiting-correcties met getekende motivering. Audit trail = controlemiddel + evidence.

_Grondslag: ISA 315 (herzien-2019) §A86 (geautomatiseerde controles) + ISA 230 (controledocumentatie)_

### Procedurele instrumenten ⚖️

Geformaliseerde werkwijzen die menselijke uitvoering structureren: checklists, walkthroughs, observation-rondes, periodieke afstemmingen, KPI-dashboards, control self-assessments. Geen fysiek of digitaal middel, wel een herhaalbaar proces.

**Waarom?** Procedures geven uitvoerders een steiger zonder het systeem digitaal te moeten dichten — vooral nuttig voor KMO's met beperkte IT-volwassenheid.


**In de praktijk**: Bij Praktijk Persenaire (eenmanszaak): maandelijkse kasstaat-checklist (zes vragen: kasbeginsaldo, ontvangsten, uitgaven, eindsaldo, fysieke telling, verschil). Zonder ERP-validatie maar wel reproduceerbaar.


_Grondslag: ITAA-norm-kmo-controlenorm §96-§97 (proportionele aanpak bij KMO)_


## In de praktijk

<h3 id="mix-afhankelijk-van-risico-en-aard-proces">Mix afhankelijk van risico en aard proces</h3>

> [!tip]- Mix afhankelijk van risico en aard proces
> Geen one-size-fits-all: een kasontvangst-proces vraagt fysieke beveiligingen + dubbele telling (procedureel) + dagboek-registratie (documentair). Een online-aankoop vraagt vooral IT-instrumenten (drie-weg-match, krediet-check) + documenten (bestelbon-bewijs). Aanvullende procedurele controle als sluitstuk. 🔗

<h3 id="middel-beheersactiviteit">Middel ≠ beheersactiviteit</h3>

> [!tip]- Middel ≠ beheersactiviteit
> Een handtekening (middel) is nog geen autorisatie (beheersactiviteit) tot er ook een norm bestaat wie tekent vanaf welk bedrag. Stagiair krijgt soms 'controle-instrumenten' vraag — vertaal eerst naar welke beheersactiviteit ze realiseren. 🔗


## Valkuilen

> [!warning]- Middelen verzamelen zonder de onderliggende beheersactiviteit te benoemen — leidt tot 'controle-theater': stempel-en-paraaf-cultuur waarbij…
> ⚠️ Middelen verzamelen zonder de onderliggende beheersactiviteit te benoemen — leidt tot 'controle-theater': stempel-en-paraaf-cultuur waarbij niemand inhoudelijk kijkt. 🤖


> [!warning]- IT-instrumenten vertrouwen zonder ITGC te testen — als toegangsbeheer faalt, valt de hele geautomatiseerde controlelaag
> ⚠️ IT-instrumenten vertrouwen zonder ITGC te testen — als toegangsbeheer faalt, valt de hele geautomatiseerde controlelaag. 🤖



## Zie ook

- **Vereist kennis van**: [[geinformatiseerde-omgeving-ic]]
- **Vereist kennis van**: [[functiescheiding]]
- **Wordt voorondersteld in** (2): [[confirmatiebrieven]] · [[uitvoering-interne-controle]]
## Voorbeelden

### Controlemiddelen-mix bij Yperse Werkplaats BV (KMO)

_Personages: Yperse Werkplaats BV_

Voor het inkoop-tot-betalingsproces zet Yperse Werkplaats BV de volgende mix in:

1. Documentair: bestelbon (doorlopend genummerd) + ontvangstbon + leveranciersfactuur — drie-weg-match.
2. Fysiek: magazijnbadge per medewerker, camera bij ontvangstdok.
3. IT: ERP-validatie weigert facturen zonder gekoppelde ontvangstbon; betaling vraagt digitale handtekening + SMS-code boven € 25.000; audit trail logt elke prijswijziging.
4. Procedureel: maandelijkse bank-grootboek-afstemming door externe accountant (Xenon Expertise BV); kwartaalrapport openstaande crediteuren > 60 dagen.
Resultaat: één persoon kan geen fictieve transactie creëren zonder dat een ander middel haar zichtbaar maakt.


## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-3`
[^2]: `ISA-230__sec_definities`
[^3]: `ISA-500__sec_vereisten`
[^4]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_boeking-van-verrichtingen`
[^5]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
