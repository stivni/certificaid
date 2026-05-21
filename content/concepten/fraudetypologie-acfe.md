---
title: Fraudetypologie ACFE (drie hoofdtypen)
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
confidence: inferred-from-aggregation
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/fraudetypologie-acfe.json
gegenereerd_op: '2026-05-21'
---
# Fraudetypologie ACFE (drie hoofdtypen) 🔗

De Association of Certified Fraud Examiners (ACFE) onderscheidt drie wezenlijk verschillende fraude-types — elk met eigen modus operandi, eigen red flags en eigen detectie-methodes. ISA 240 §A2 benoemt expliciet de eerste twee (frauduleuze financiële verslaggeving + oneigenlijke toeëigening van activa). Voor de stagiair is dit dé taxonomie om bij een gemeld fraudegeval het type te identificeren en de gepaste auditor- of IC-respons te kiezen.

> [!summary] Korte inhoud
> De ACFE-fraudetypologie verdeelt fraude in drie wezenlijk verschillende categorieën: (1) frauduleuze financiële verslaggeving — manipulatie van jaarrekening om beeld te verbeteren; (2) oneigenlijke toeëigening van activa (asset misappropriation) — verduistering van geld, voorraad….

> [!info] Behoort tot: [[fraude]]

De ACFE-fraudetypologie verdeelt fraude in drie wezenlijk verschillende categorieën: (1) frauduleuze financiële verslaggeving — manipulatie van jaarrekening om beeld te verbeteren; (2) oneigenlijke toeëigening van activa (asset misappropriation) — verduistering van geld, voorraad, immaterieel; (3) corruption — omkoping, belangenconflicten, kickbacks. Elk type vraagt eigen preventie + detectie.



## Bouwstenen

### Frauduleuze financiële verslaggeving ⚖️

Opzettelijke afwijkingen in de jaarrekening (inclusief weglatingen) om gebruikers te misleiden over prestaties of financiële positie. Typische schema's: omzet padding (vervroegd boeken, fictieve verkopen), kosten uitstellen, voorraad overwaarderen, schulden verbergen, off-balance-sheet-entiteiten.

**Waarom?** Wordt typisch gepleegd door of met medeweten van het management — dus moeilijk te detecteren met routine-controles. Auditor moet professioneel-kritisch zijn bij subjectieve waarderingen en periode-grensjes.


**In de praktijk**: Detectie via: cijferanalyses op trends (omzetgroei vs. cash-flow-groei), cut-off-tests op grens financiële periode, journaalboeking-analyse (ISA 240 §32(a) verplicht), substantieve werkzaamheden op subjectieve schattingen.

Bij Rotex Roeselare NV verschuift het management work-in-progress van € 200.000 naar 'klaar product' om omzet vroeger te kunnen erkennen — boekjaar haalt zo de bank-covenant. Geen verkoop, wel boeking.

_Grondslag: ISA 240 §A2 + ACFE Report to the Nations_

### Oneigenlijke toeëigening van activa (asset misappropriation) ⚖️

Verduistering van middelen door werknemers of management: kasgeld, voorraad, vaste activa, intellectuele eigendom. Typische schema's: skimming (cash voor registratie), larceny (na registratie), ghost employees (fictieve werknemers in payroll), expense-fraud, voorraad-diefstal.

**Waarom?** Meest voorkomende fraudetype in KMO's — typisch lage bedragen per voorval, hoge frequentie. Treft het bedrijf direct in resultaat én kas.


**In de praktijk**: Detectie via: bank- en kas-reconciliaties (skimming-detectie), periodieke fysieke voorraadtellingen, payroll-analyse (HR-data ↔ payroll), expense-claim-audits, surprise cash counts.

Bij Meubelzaak Mertens BV neemt een magazijnier maandelijks afgekeurde meubels mee voor privé-verkoop. Detectie pas na 14 maanden via voorraadtelling-discrepantie + tip van collega.

_Grondslag: ISA 240 §A2 + ACFE Report to the Nations_

### Corruption (omkoping, kickbacks, belangenconflicten) ⚖️

Misbruik van bedrijfspositie voor persoonlijk voordeel via externe partijen: kickbacks van leveranciers, omkoping van inkopers, ondoorzichtige consultancy-vergoedingen, belangenconflicten zonder disclosure. Vaak ondergewaardeerd in fraude-cijfers omdat het in twee organisaties tegelijk speelt.

**Waarom?** Raakt rechtstreeks de beslissingsketen van inkopen + contracten — kan grote bedragen omvatten zonder dat de jaarrekening direct fout is (de leverancier is wel duur, niet fictief).


**In de praktijk**: Detectie via: leverancier-due-diligence, periodieke benchmark van inkoopprijzen, klokkenluider-kanaal, levensstijl-analyse sleutelmedewerkers, third-party-relationship-disclosures.

Aankoper bij Yperse Werkplaats BV krijgt 5% kickback van een leverancier op orders > € 100.000. Leverancier is bestaand en levert echt — jaarrekening is technisch correct, maar de onderneming betaalt structureel 10% te veel.

_Grondslag: ISA 240 §A6 + ACFE Report to the Nations_


## In de praktijk

<h3 id="type-bepaalt-detectiestrategie">Type bepaalt detectiestrategie</h3>

> [!tip]- Type bepaalt detectiestrategie
> Elk type wordt op een andere plek detecteerd: financiële vervalsing in de jaarrekening-analyse (cijfertests, cut-off); asset misappropriation in kasprocessen + voorraad; corruption in leveranciers-due-diligence + klokkenluiders. Een fraude-detectie-strategie die alle drie negeert, mist het meeste. 🔗


## Valkuilen

> [!warning]- Een corruption-geval kan een 'cleane' jaarrekening hebben — een externe auditor die alleen rekent en niet vraagt naar leverancier-relaties z…
> ⚠️ Een corruption-geval kan een 'cleane' jaarrekening hebben — een externe auditor die alleen rekent en niet vraagt naar leverancier-relaties zal het niet vinden. Audit-procedures moeten alle drie types adresseren. 🔗



## Zie ook

- **Vereist kennis van**: [[klokkenluiderregeling]]
- **Wordt voorondersteld in** (2): [[fraude]] · [[fraude-versus-fout]]
## Bronnen

[^1]: `ISA-240__sec_toepassingsgerichte-en-overige-verklarende-teksten_2_part2`
