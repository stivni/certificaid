---
title: Opzetten van controle-activiteiten en monitoringsmechanismen
tags:
- concept
- competentie
- po-1-7
linked_anchors:
- 1.7.taak.1
- 1.7.VIII
- 1.7.VIII.A
- 1.7.VIII.C
- 1.7.VIII.D
- 1.7.VIII.F
- 1.7.X.D
- 1.7.XI
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opzetten-controleactiviteiten-en-monitoring.json
gegenereerd_op: '2026-05-18'
---
# Opzetten van controle-activiteiten en monitoringsmechanismen 🤖


## Stappen

### 1. Per risico het type controle kiezen — preventief versus detectief

Wijs aan elk risico boven appetite minstens één preventieve én één detectieve controle toe, op het juiste niveau (transactie, periode, of jaar).

**Waarom?** Preventief alleen mist falen op uitvoering; detectief alleen ontdekt fouten te laat. Combinatie verhoogt zekerheid en faciliteert tijdige correctie.

**📥 Input**:
- Risico-register met risk-respons-keuze → **Per risico: gekozen verminderen-respons** _(document)_

**📤 Output**:
- Control-design-tabel → **Per risico: preventieve control + detectieve control + frequentie** _(document)_

**🛠️ Hoe**:

1. Volg [[beheersactiviteiten]] §preventief-detectief: preventief stopt de fout (autorisatie, validatie, drie-weg-match); detectief vindt de fout achteraf (reconciliatie, review, cijferanalyse).
2. Categorieën uit [[beheersactiviteiten]] §vier-categorieen: autorisaties/goedkeuringen, verificaties, functiescheiding, fysieke beveiliging.
3. Kies de frequentie: bij elke transactie (online controls), dagelijks (reconciliaties), wekelijks (rapporten), maandelijks (bankafstemming), kwartaal (managementrapport), jaarlijks (inventaris, review).
4. Onderscheid manuele controls (mens controleert) van geautomatiseerde controls (systeem blokkeert) — geautomatiseerd is robuuster en consistenter.


**Grondslag**: [[beheersactiviteiten]] §types, [[controlemiddelen-ic]] §preventief-detectief

### 2. Controlemiddelen kiezen — handtekening, paraaf, formulier, IT-control

Bepaal per control welk concreet middel zekerheid geeft: ondertekend formulier, ERP-veld, dubbel-paraaf, screenshot, reconciliatieblad.

**Waarom?** Een control zonder evidence is niet auditbaar. Een control zonder middel is niet uitvoerbaar.

**📥 Input**:
- Control-design-tabel stap 1 → **Controle-acties zonder middel** _(document)_

**📤 Output**:
- Evidence-matrix → **Per control: middel + bewaarplaats + bewaartermijn** _(document)_

**🛠️ Hoe**:

1. Volg [[controlemiddelen-ic]] §middelen: handtekening op originele documenten, paraaf op werkpapieren, ondertekende formulieren, ERP-flags, screenshots van rapporten.
2. Onderscheid harde evidence (ondertekend papier, ERP-log) van zachte evidence (e-mail, mondelinge bevestiging) — bij hoog-risico-controls altijd harde evidence.
3. Voor IT-controls: zorg dat het systeem zelf de control afdwingt en logt — bv. ERP-veld vereist dat factuurnummer ingevuld is + audit-trail bewaart de input-gebruiker.
4. Bewaartermijn alignen met boekhoudkundige bewaarplicht (7 jaar boekhoudkundige stukken; 10 jaar bij commissaris-mandaat — zie ook [[documenteren-auditdossier]]).


**Grondslag**: [[controlemiddelen-ic]] §evidence, [[geinformatiseerde-omgeving-ic]] §audit-trail

### 3. Opvolging-verrichtingen — dagelijkse en periodieke afstemmingen inrichten

Implementeer reguliere afstemmingen die discrepanties tussen verschillende informatiebronnen detecteren (bv. bank vs grootboek, voorraad vs ERP, klant-saldo vs verkoopdagboek).

**Waarom?** Reconciliaties vinden vroeg afwijkingen — voorkomt foute jaarrekening en is laagdrempelige fraudedetectie.

**📥 Input**:
- Lijst informatiebronnen per cyclus → **Bron A versus bron B per cyclus** _(document)_

**📤 Output**:
- Afstemmings-kalender → **Per afstemming: bronnen, frequentie, uitvoerder, reviewer** _(document)_

**🛠️ Hoe**:

1. Volg [[opvolging-verrichtingen-ic]] §reconciliaties: bankreconciliatie (dagelijks of wekelijks), btw-controle (maandelijks), voorraadrotatie-cycle-counts (continu of kwartaal), klantbalans-aging (maandelijks).
2. Voor elke reconciliatie: documenteer wie uitvoert (uitvoerder), wie reviewt (reviewer ≠ uitvoerder — functiescheiding!), evidence (afstemmingsblad met paraffen).
3. Definieer verschillen-tolerantie: < € 100 = afsluiten met opmerking; € 100-€ 1.000 = onderzoek + correctie binnen 2 weken; > € 1.000 = escalatie naar CFO.
4. Combineer met cijferanalyses ([[cijferanalyses-audit]] aangepast aan interne context): maandelijkse marge-analyse per productlijn, debiteurenrotatie, voorraadrotatie.


**Grondslag**: [[opvolging-verrichtingen-ic]] §reconciliaties, [[beheersactiviteiten]] §verificaties

> [!warning]- Scheid uitvoerder en reviewer van elke reconciliatie — automatische SOD-toepassing op IC zelf.
>
> _Vaak fout gedaan_: Boekhouder doet reconciliatie én tekent ze zelf af — geen tweede paar ogen, fraude makkelijk te verbergen.
>
> _Grondslag_: [[opvolging-verrichtingen-ic]] §reviewer

### 4. Doorlopende monitoring en periodieke evaluatie opzetten

Bouw monitoring op twee niveaus: doorlopend (ingebed in dagelijkse processen) en periodiek (formele review door interne audit of externe adviseur).

**Waarom?** Controles verzwakken in de tijd door personeelswissel, regelgevingsverandering en proceswijziging. Monitoring is component 5 van COSO.

**📥 Input**:
- Volledig IC-systeem (componenten 1-4) → **Documentatie + beheersmatrices** _(document)_

**📤 Output**:
- Monitoring-plan en KPI-dashboard → **Doorlopende KPI's + periodieke audit-plan** _(document)_

**🛠️ Hoe**:

1. Volg [[monitoring-interne-controle]] §twee-niveaus.
   a. Doorlopend: bouw KPI's in dashboards (% afgekeurde facturen, dagen tot reconciliatie, % toegangsrechten herbevestigd) die proceseigenaren zien.
   b. Periodiek: plan jaarlijkse evaluatie van design én operating effectiveness — zie [[beoordelen-effectiviteit-ic-via-interne-audit]].
2. Definieer escalatie-protocol: bij rode KPI (afwijking > drempel) automatische melding aan CFO en risico-eigenaar binnen 5 werkdagen.
3. Gebruik [[evaluatiecriteria-ic]] §design-operating om in elke periodieke evaluatie beide dimensies te toetsen.
4. Rapporteer maandelijks aan zaakvoerder, kwartaal aan bestuursorgaan, jaarlijks aan auditcomité (indien aanwezig) of algemene vergadering.


> [!example]- Voorbeeld: Yperse Werkplaats BV (€ 8,5M omzet, productie-KMO) implementeert haar eerste formele monitoring-laag, begeleid door Xeno…
> Yperse Werkplaats BV (€ 8,5M omzet, productie-KMO) implementeert haar eerste formele monitoring-laag, begeleid door Xenon Expertise BV.
>
> 1. **KPI-dashboard maandelijks** 💬
>
>    - Bankreconciliatie tijdig (binnen 5 dagen na maandeinde): target 100%, drempel < 90%
>    - % facturen drie-weg-match niet succesvol: target < 2%, drempel > 5%
>    - Voorraadtelling-variantie: target < 1%, drempel > 3%
>    - Aging klantvorderingen > 60 dagen: target < € 50.000, drempel > € 100.000
>    - Aantal SOD-violations open: target = 0, drempel > 3
>    
>
> 2. **Periodieke audit-cycle** 💬
>
>    Q1: review aankoopcyclus (8 dagen)
>    Q2: review verkoopcyclus + AVG-compliance (8 dagen)
>    Q3: review HR + payroll-cyclus (5 dagen)
>    Q4: IT-general-controls + cyberrisico (10 dagen)
>    Jaarlijks: management self-assessment IC + commissaris-debrief
>    
>
> 3. **Rapportering-kalender** 💬
>
>    - Wekelijks: dashboard naar CFO
>    - Maandelijks: KPI-rapport naar zaakvoerder + bestuur
>    - Kwartaal: status risico-respons + audit-bevindingen naar auditcomité
>    - Jaarlijks: IC-jaarrapport + bevestigingsbrief management aan externe auditor
>    
>

**Grondslag**: [[monitoring-interne-controle]] §twee-niveaus, [[evaluatiecriteria-ic]] §design-operating, COSO 2013 component 5


## Voorbeelden




