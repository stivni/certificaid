---
title: Identificeren van fouten, fraude en verspilling in een organisatie
tags:
- competentie
- po-1-7
programmaonderdelen:
- '1.7'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/identificeren-fouten-fraude-verspilling.json
gegenereerd_op: '2026-05-18'
---
# Identificeren van fouten, fraude en verspilling in een organisatie

**⚖️ 30% · 🤖 70%**

> De rechtsfiguur fraude wordt strafrechtelijk omkaderd (Strafwetboek 2024 Boek 2 art. 479 oplichting, art. 488 informaticabedrog). De Wet 28 november 2022 klokkenluiderregeling verplicht meldkanalen bij middelgrote en grote ondernemingen. De detectie- en preventiemethodologie zelf (fraudedriehoek Cressey, ACFE-typologie, red flags) is vakdoctrine.

## Aanbevolen werkwijze

### 1. Onderscheid maken tussen fout, fraude en verspilling — definities toepassen

Classificeer elke vastgestelde onregelmatigheid als fout (onopzettelijk), fraude (opzettelijk + bedrog) of verspilling (legaal maar inefficiënt). De juridische en operationele gevolgen verschillen fundamenteel.

**Waarom?** Fout, fraude en verspilling vragen verschillende reacties: foutcorrectie (fout), onderzoek + sanctie + melding (fraude), procesoptimalisatie (verspilling).

**📥 Input**:
- Bevindingen-rapport (uit reconciliatie, audit of klokkenluiderkanaal) → **Onregelmatigheden + context** _(document)_

**📤 Output**:
- Geclassificeerd bevindingen-rapport → **Per item: type (fout/fraude/verspilling) + onderbouwing** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[fouten-en-fraude]] §typologie: onopzettelijk + correctie-mogelijk = fout; opzettelijk + bedrog/bevoordeling = fraude; legaal + suboptimaal = verspilling.
2. Voor fouten — gebruik [[fouten-ic]] §types: oordeelsfouten (verkeerde inschatting), uitvoeringsfouten (mens of systeem maakt fout), datafouten (foute invoer).
3. Voor fraude — toets aan [[fraude]] §driehoek: druk + gelegenheid + rationalisatie. Geen driehoek = geen fraude (waarschijnlijk fout).
4. Voor verspilling — categoriseer volgens [[verspilling]]: tijd, materiaal, kapitaal, informatie. Geen wetsovertreding, wel value destruction.


**Grondslag**: [[fouten-en-fraude]] §typologie, [[fraude]] §driehoek, [[verspilling]] §types

> [!warning]- Documenteer altijd de intentie-analyse — bij ontbreken van bewijs van opzet classificeer als fout, niet als fraude.
>
> _Vaak fout gedaan_: Een onregelmatigheid voortijdig 'fraude' noemen zonder bewijs van opzet — heeft reputatie- en juridische gevolgen voor de beschuldigde.
>
> _Grondslag_: [[fraude]] §opzet-vereist

### 2. Fraude-red-flags monitoren in transactiestromen en HR

Bouw indicatoren in de organisatie die typische fraude-red-flags signaleren: ongewone leveranciers, ronde bedragen, weekend-transacties, levensstijl-discrepantie.

**Waarom?** Fraude wordt zelden ontdekt door geplande audit (~4%) maar door tips en red-flag-monitoring. Vroege detectie verkleint schade.

**📥 Input**:
- Transactiedata + HR-data → **ERP-export, payroll, expense-claims** _(document)_

**📤 Output**:
- Red-flag-dashboard → **Periodieke lijst van afwijkingen voor onderzoek** _(document)_

**🛠️ Hoe**:

1. Bouw transactie-red-flags: nieuwe leveranciers met directe grote orders, betalingen aan privé-adressen, leveranciers zonder KBO, ronde bedragen vlak onder autorisatiedrempels (€ 4.999 bij drempel € 5.000), facturen zonder onderliggende bestelling.
2. Bouw HR-red-flags: medewerker neemt geen vakantie, weekend-werk in financiële systemen, levensstijl-discrepantie versus salaris, klachten van leveranciers/klanten over een medewerker.
3. Volg [[fraude]] §ACFE-typologie: corruption (omkoping, conflict of interest), asset misappropriation (verduistering, skimming, payroll fraud), financial statement fraud (omzet-padding, cost-shifting).
4. Documenteer red-flag-onderzoeken vertrouwelijk — onschuldvermoeden + AVG-bescherming van de betrokkene.


**Grondslag**: [[fraude]] §ACFE-typologie, [[opvolging-verrichtingen-ic]] §afwijkingen, ACFE Report to the Nations

### 3. Klokkenluiderkanaal inrichten en beheren conform Wet 28 november 2022

Implementeer een intern meldkanaal (telefonisch, online platform of postbus) dat anoniem of vertrouwelijk meldingen accepteert, behandeld door een onafhankelijke meldfunctionaris.

**Waarom?** Wet 28 november 2022 verplicht een meldkanaal bij ondernemingen met ≥ 50 werknemers. Klokkenluiders zorgen voor ~40% van fraude-ontdekkingen (ACFE).

**📥 Input**:
- Werknemersaantal + sectorale verplichtingen → **Toepasselijkheid Wet 2022** _(document)_

**📤 Output**:
- Klokkenluiderbeleid + meldkanaal → **Procedure + technische tool + register meldingen** _(document)_

**🛠️ Hoe**:

1. Volg [[klokkenluiderregeling]] §verplichtingen: ondernemingen ≥ 50 werknemers moeten intern kanaal hebben; ≥ 250 sinds 17/12/2021, 50-249 sinds 17/12/2023.
2. Stel een meldfunctionaris aan — onafhankelijk van management, met directe toegang tot bestuursorgaan of auditcomité.
3. Bouw drie kanalen aan: (a) intern meldkanaal (telefoon, e-mail, online platform), (b) extern naar Federaal Coördinator (FOD), (c) publiekelijk in uitzonderlijke gevallen.
4. Garandeer bescherming: anonieme melding mogelijk, vergeldingsverbod, omkering bewijslast bij arbeidsmaatregel. Behandel binnen 3 maanden (ontvangstbevestiging binnen 7 dagen, feedback < 3 maanden).


**Grondslag**: [[klokkenluiderregeling]] §verplichtingen, Wet 28 november 2022

> [!warning]- Stel een onafhankelijke meldfunctionaris aan — niet de HR-directeur of een lid van het uitvoerend management.
>
> _Vaak fout gedaan_: Meldkanaal toewijzen aan HR — afhankelijkheid leidt tot wantrouwen + lagere meldingen. Doet het beoogde effect teniet.
>
> _Grondslag_: [[klokkenluiderregeling]] §onafhankelijkheid

### 4. Vermoeden van fraude onderzoeken en escaleren

Bij concreet vermoeden: voer een fact-finding-onderzoek uit, betrek juridische en (indien nodig) gerechtelijke instanties, en documenteer chain-of-custody van bewijsmateriaal.

**Waarom?** Fout onderzoek kan bewijs vernietigen, de betrokkene tippen, of nietigheid van eventuele sanctie veroorzaken.

**📥 Input**:
- Concrete red-flag of melding → **Aanwijzing + onderbouwing** _(document)_

**📤 Output**:
- Onderzoeksdossier → **Feiten, bewijs, conclusies, beslissingen, gevolgen** _(document)_

**🛠️ Hoe**:

1. Stel een onderzoeksteam samen — discreet, met externe forensisch accountant indien complex (verwijs naar [[interne-audit]] §forensic).
2. Beveilig bewijs: blokkeer ERP-toegang van verdachte medewerker, kopieer hard drives (chain-of-custody), exporteer transactielogs, bevries betalingsworkflows.
3. Hoor de verdachte volgens recht op verdediging — bij voorkeur in aanwezigheid van HR + jurist. Geen confrontatie zonder dossier-voorbereiding.
4. Beslis: arbeidsrechtelijk (sanctie tot ontslag om dringende reden), civielrechtelijk (terugvordering schade), strafrechtelijk (aangifte bij parket — verplicht bij significante fraude). Meld witwasvermoedens aan CFI (Cel Financiële Informatieverwerking) via art. 47 antiwitwaswet.


> [!example]- Voorbeeld: Bij Yperse Werkplaats BV detecteert de maandelijkse cijferanalyse dat aankopen van Leverancier X € 280.000 zijn (vorig j…
> Bij Yperse Werkplaats BV detecteert de maandelijkse cijferanalyse dat aankopen van Leverancier X € 280.000 zijn (vorig jaar € 35.000), met factuurnummers die niet sequentieel lopen. Aankoopdirecteur Tom Lefèvre is bevoegd. Sofie Janssens (externe IC-adviseur) wordt geconsulteerd.
>
> 1. **Voor-analyse (zonder Tom Lefèvre te alarmeren)** 💬
>
>    - Achtergrondcheck Leverancier X via KBO/Graydon: opgericht 6 maanden geleden, geen webpresence, één actieve zaakvoerder.
>    - Cross-check leveringen vs ontvangstbonnen: 14 facturen zonder bijhorende ontvangst.
>    - Betalingsdetail: alle betalingen naar één bankrekening BE-NL combinatie.
>    - Adres Leverancier X = zelfde postcode als woonadres Tom Lefèvre.
>    
>
> 2. **Conclusie + escalatie** 💬
>
>    Fraude-driehoek aanwezig: druk (privé-schulden vermoed), gelegenheid (Tom Lefèvre tekent leveranciersgoedkeuring én factuur goed = SOD-conflict niet eerder gedetecteerd!), rationalisatie nog te bevestigen.
>    Escalatie: Pieter Vermeulen (zaakvoerder) geïnformeerd; externe jurist betrokken; ERP-toegang Tom geschorst; back-up e-mailaccount; aangifte parket + CFI-melding voorbereid.
>    
>
> 3. **Vervolgacties IC-systeem** 💬
>
>    - SOD-conflict in aankoop-flow oplossen: aankoopgoedkeuring losgekoppeld van leveranciersacceptatie.
>    - Nieuwe leverancier > € 25.000 vereist KBO-check + tweede goedkeuring CFO.
>    - Whistleblower-platform werd niet gebruikt — interne communicatie heropfrissen.
>    
>

**Grondslag**: [[fraude]] §onderzoek, Strafwetboek 2024 art. 479 + art. 488, Antiwitwaswet art. 47

> [!warning]- Betrek vroeg een jurist + behoud chain-of-custody van bewijsmateriaal — anders is bewijs in rechtszaak onbruikbaar.
>
> _Vaak fout gedaan_: Verdachte direct confronteren in een vergadering 'om het uit te praten' — verdachte vernietigt sporen en collega's worden gewaarschuwd.
>
> _Grondslag_: [[fraude]] §onderzoek, Strafwetboek art. 479-488


## Voorbeelden

> [!example]- Meubelzaak Mertens BV: de zaakvoerder ontdekt dat een werknemer al 3 jaar geen vakantie heeft genomen
> **Conclusie**: Ja — klassieke fraude-red-flag uit ACFE-typologie. Geen vakantie betekent dat de medewerker bang is dat in zijn afwezigheid een collega zijn werk bekijkt en fraude ontdekt. Actie: forceer minimaal 2 aaneensluitende weken vakantie waarin een collega zijn taken overneemt + spot-check uitvoert. Documenteer professioneel — geen beschuldiging, wel preventieve maatregel.
>
> **Grondslag**: [[fraude]] §red-flags-HR, ACFE Report to the Nations
>
> **Redenering**: Vakantie-vermijding is een vroege indicator zonder zelf bewijs van fraude. De passende reactie is preventief (verplichte vakantie + cross-review) — niet beschuldigend.

> [!example]- Praktijk Persenaire (eenmanszaak, 1 werknemer) — moet er een klokkenluiderkanaal opgezet worden
> **Conclusie**: Niet wettelijk verplicht onder Wet 2022 (< 50 werknemers). Wel: documenteer een eenvoudige meldroute via externe accountant Sofie Janssens als 'klacht- en meldfunctie'. Verzeker dat de werknemer weet dat dit kanaal bestaat — voorkomt onzichtbaarheid van misstanden.
>
> **Grondslag**: [[klokkenluiderregeling]] §toepassingsgebied
>
> **Redenering**: Wettelijke ondergrens 50 werknemers; daaronder geen verplichting maar best practice — toont integriteitscultuur.


## Gebaseerd op concepten

[[fouten-en-fraude]] · [[fouten-ic]] · [[fraude]] · [[verspilling]] · [[klokkenluiderregeling]] · [[opvolging-verrichtingen-ic]]
## Voortkomend uit

- **Taken**: 1.7.taak.1
- **Kenniselementen**: 1.7.VI, 1.7.VI.A, 1.7.VI.B, 1.7.VI.C, 1.7.XII.A, 1.7.XII.H
