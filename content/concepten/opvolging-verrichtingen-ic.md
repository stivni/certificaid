---
title: Opvolging van verrichtingen
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VIII.C
- 1.7.VIII
programmaonderdelen:
- '1.7'
confidence: inferred-from-aggregation
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/opvolging-verrichtingen-ic.json
gegenereerd_op: '2026-05-18'
---
# Opvolging van verrichtingen 🤖

Opvolging van verrichtingen is de praktische uitwerking van detectieve IC: structureel nakijken of geboekte transacties echt hebben plaatsgevonden, juist zijn geregistreerd en in de juiste periode. Het is een werkpaard van monitoring (COSO-component 5) en levert tegelijk evidence waarop de externe auditor kan steunen (ISA 330 §4(a)). Voor de stagiair gaat het om de concrete technieken — bank-grootboek-afstemming, debiteurenbevestiging, voorraadtelling, cijferanalyses — en de organisatorische conditie: uitvoerder ≠ reviewer (functiescheiding op IC-zelf). Bij KMO neemt de externe accountant deze rol vaak gedeeltelijk over (ITAA-norm-kmo-controlenorm §97).

> [!summary] Korte inhoud
> Opvolging van verrichtingen is het systematisch nakijken of geboekte transacties echt hebben plaatsgevonden, juist zijn geregistreerd en in de juiste periode geboekt.

> [!info] Behoort tot: [[monitoring-interne-controle]]

Opvolging van verrichtingen is het systematisch nakijken of geboekte transacties echt hebben plaatsgevonden, juist zijn geregistreerd en in de juiste periode geboekt. Het is detectieve IC — fouten en fraude ontdekken na de feiten. Concrete technieken: bank-grootboek-afstemming, debiteuren/crediteuren-leeftijdsanalyse en bevestiging, voorraadtelling, cijferanalyses (trends, ratio's, uitzonderingsoverzichten). Vormt onderdeel van COSO-component 5 (monitoring) en levert evidence waarop ISA 330 §4(a) leunt.


## Bouwstenen

### Bank-grootboek-afstemming ⚖️

Periodieke (typisch maandelijkse) reconciliatie tussen het bankuittreksel-saldo en het bankrekening-saldo in de boekhouding. Verschillen worden lijn per lijn verklaard (timing, openstaande cheques, fouten).

**Waarom?** De bank is een externe, onafhankelijke bron — discrepanties signaleren ofwel verkeerde boekingen ofwel ontbrekende boekingen ofwel verduistering. Eenvoudigste sluitstuk-controle.


**In de praktijk**: Bij Yperse Werkplaats BV: boekhouder Cindy maakt de reconciliatie, externe accountant David van Xenon Expertise BV reviewt en tekent maandelijks. Uitvoerder ≠ reviewer = functiescheiding op IC zelf.

Reconciliatie maand juni 20X1 toont € 4.250 verschil. Cindy verklaart: € 4.000 cheque uitgegeven 30/06, geïnd door begunstigde 02/07 (timing) + € 250 bankkosten geboekt door bank maar nog niet door boekhouding (correctie nodig).

_Grondslag: ITAA-norm-kmo-controlenorm §97 + CBN-advies 174/1 (volledigheid)_

### Openstaande-postenlijsten (debiteuren + crediteuren) ⚖️

Periodiek overzicht van openstaande facturen per ouderdomscategorie (0-30, 31-60, 61-90, > 90 dagen). Voor debiteuren én crediteuren. Optioneel: directe bevestiging vragen aan klant/leverancier (saldo-confirmatie).

**Waarom?** Oude openstaande posten signaleren ofwel slechte invordering, ofwel fictieve facturatie (omzet-inflatie), ofwel onverwerkte betalingen. Crediteurenkant: vertraagde betalingen kunnen IC-zwakte zijn of liquiditeitsstress.


**In de praktijk**: Bij Yperse Werkplaats BV: leeftijdslijst debiteuren elke maand naar CFO David; alle vorderingen > 90 dagen vergen schriftelijke uitleg + provisie-voorstel.

Leeftijdslijst toont € 12.500 vordering op klant Brugse Brouwerij BV uit 20X0. Onderzoek toont kredietnota niet geboekt — correctie + functiescheiding-vraag waarom de verkoper de kredietnota niet doorgaf.

_Grondslag: ISA 505 (externe bevestigingen) + ITAA-norm-kmo-controlenorm §97_

### Voorraadtelling en spot-checks ⚖️

Periodieke fysieke telling van voorraad-items (compleet of selectie) en vergelijking met de voorraadadministratie. Verschillen worden onderzocht en gecorrigeerd; persistent grote verschillen wijzen op IC-zwakte (diefstal, registratiefout, breuk).

**Waarom?** Voorraad is bij uitstek vatbaar voor verduistering en registratiefouten. Fysieke telling is het enige onafhankelijke bewijs van het werkelijk aanwezig zijn van activa (ISA 501 §A1).


**In de praktijk**: Bij Yperse Werkplaats BV: jaarlijkse complete telling op 31/12 (verplicht voor balansopstelling) + maandelijkse spot-check op 20 random items door magazijnier Bart en boekhouder Cindy samen.


_Grondslag: ISA 501 (specifieke aspecten — voorraden) + ITAA-norm-kmo-controlenorm §97_

### Cijferanalyses en uitzonderingsoverzichten ⚖️

Vergelijking van actuele cijfers met budget, vorige periode, sector-ratio's. Plus geautomatiseerde uitzonderingsrapporten: transacties boven drempel, na kantooruren, met afwijkende prijs, met handmatige overrides. Doel: afwijkingen vroeg zichtbaar maken.

**Waarom?** Ratio-analyse vangt 'plausibel ogende maar inhoudelijk verkeerde' boekingen die individuele controles missen — typisch ISA 520-werkpaard. Exception reports leggen IT-omzeilingen bloot.


**In de praktijk**: Bij Yperse Werkplaats BV: bruto-marge per kostencentrum maandelijks vergeleken met voorgaand jaar; ERP exporteert wekelijks 'override-rapport' (alle handmatige correcties > € 1.000) voor review door CFO David.

Bruto-marge productie-divisie daalt van 28% naar 19% in Q2 zonder uitleg. Onderzoek toont fictieve omzet bij één klant — boekhouder boekte vooruit zonder leveringsbon. Cijferanalyse trok de fraude aan het licht.

_Grondslag: ISA 520 (cijferanalyses) + ISA 240 §32-§33 (journaalpost-testing)_


## In de praktijk

<h3 id="frequentie-hangt-af-van-risico">Frequentie hangt af van risico</h3>

> [!tip]- Frequentie hangt af van risico
> Hoog-risico-stromen (kas, bank, materiaalvoorraad): maandelijks of zelfs wekelijks. Middel-risico (debiteuren, crediteuren): maandelijks. Laag-risico (immateriële activa): kwartaal of jaarlijks. Frequentie documenteren in IC-handboek. 🤖

<h3 id="functiescheiding-op-de-opvolging-zelf">Functiescheiding op de opvolging zelf</h3>

> [!tip]- Functiescheiding op de opvolging zelf
> De persoon die de opvolging doet mag niet dezelfde zijn als degene die de transactie boekte of het bezit beheert. Anders dekt hij eigen fouten of fraude toe. Bij KMO: externe accountant of zaakvoerder neemt vaak de reviewer-rol. 🤖


## Valkuilen

> [!warning]- Een afstemming die altijd 'klopt' is verdacht: ofwel wordt het verschil systematisch verstopt in een 'diverse'-rubriek, ofwel doet de uitvoe…
> ⚠️ Een afstemming die altijd 'klopt' is verdacht: ofwel wordt het verschil systematisch verstopt in een 'diverse'-rubriek, ofwel doet de uitvoerder de telling met de administratie naast zich (gestuurde controle). Test door zelf de telling te herhalen. 🤖


> [!warning]- Cijferanalyse vergelijken met eigen vorige periode mist trends die zich al jaren voordoen — vergelijken met sector-benchmarks of budget vang…
> ⚠️ Cijferanalyse vergelijken met eigen vorige periode mist trends die zich al jaren voordoen — vergelijken met sector-benchmarks of budget vangt structurele afwijkingen beter. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[beheersactiviteiten]]

## Voorbeelden

Bij Yperse Werkplaats BV doet boekhouder Cindy elke maand: (1) bank ↔ grootboek-afstemming (saldo's gelijk?), (2) debiteurenlijst per leeftijd (welke vorderingen > 60 dagen?), (3) voorraad spot-check (10 willekeurige artikelen), (4) cijferanalyse omzet/marge per kostencentrum. Afwijkingen meldt ze aan CFO David, die ze valideert en het rapport tekent.

## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_toetsingen-van-interne-beheersingsmaatregelen`
[^2]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_boeking-van-verrichtingen`
[^3]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
