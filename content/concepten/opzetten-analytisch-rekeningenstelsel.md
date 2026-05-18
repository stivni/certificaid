---
title: Opzetten van een analytisch rekeningenstelsel met kostencentra en kostendragers
tags:
- concept
- competentie
- po-1-8
linked_anchors:
- 1.8.taak.1
- 1.8.I
- 1.8.I.A
- 1.8.IV
- 1.8.IV.A
- 1.8.IV.B
- 1.8.IV.C
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opzetten-analytisch-rekeningenstelsel.json
gegenereerd_op: '2026-05-18'
---
# Opzetten van een analytisch rekeningenstelsel met kostencentra en kostendragers 🤖


## Stappen

### 1. Bepalen van de informatiebehoeften en doelstellingen

Identificeer welke beslissingen het analytisch stelsel moet ondersteunen (prijszetting, voorraadwaardering, budgetcontrole, performantie per centrum).

**Waarom?** Het ontwerp van het stelsel volgt de informatievraag — anders riskeer je een fijnmazige indeling die niemand gebruikt.

**📥 Input**:
- Bedrijfsplan + organogram → **Productlijnen, afdelingen, sturingsritme** _(document)_
- Gesprekken met directie/controlling → **Welke vragen moet de boekhouding maandelijks beantwoorden** _(document)_

**📤 Output**:
- Lijst informatie-objecten → **Producten, klanten, opdrachten, afdelingen** _(conclusie)_

**🛠️ Hoe**:

1. Lees de vier klassieke doelen volgens [[doelstellingen-analytische-boekhouding]]:
   voorraadwaardering, prijszetting, beslissingen, prestatiebeoordeling.
2. Inventariseer welke doelen voor de cliënt prioritair zijn — niet elke onderneming
   heeft alle vier even sterk nodig.
3. Vertaal elk doel naar concrete informatie-objecten:
   voorraadwaardering → kost per product; performantie → kost per kostencentrum;
   beslissingen → kost per order of klant.
4. Documenteer keuzes in een ontwerpnota; vraag bevestiging van directie.


**Grondslag**: [[doelstellingen-analytische-boekhouding]] §vier-doelen, [[analytische-boekhouding]] §scope

### 2. Definiëren van kostensoorten, kostencentra en kostendragers

Bouw de drie dimensies van de analytische registratie op: kostensoorten (klasse 6 spiegel), kostencentra (waar wordt verbruikt), kostendragers (waaraan wordt toegerekend).

**Waarom?** Zonder duidelijke afbakening loopt kost-informatie door elkaar en wordt geen enkele dimensie betrouwbaar.

**📥 Input**:
- Lijst informatie-objecten uit stap 1 → **Producten + afdelingen + opdrachten** _(document)_
- MAR-klasse 9 (Bijlage 1 KB 21.10.2018) → **Vrije nummering binnen klasse 9** _(document)_

**📤 Output**:
- Drie rekening-lijsten → **Kostensoorten, kostencentra, kostendragers met code + omschrijving** _(document)_

**🛠️ Hoe**:

1. Lijst de kostensoorten op volgens [[kostensoort]] — vaak een spiegel van klasse 6
   (60 grondstoffen, 61 diensten, 62 personeel, 63 afschrijvingen, 64 andere).
2. Lijst de kostencentra op volgens [[kostencentrum]] §afbakening: hulp-centra
   (bv. onderhoud) tegenover hoofd-centra (productie-afdelingen).
   Voor Yperse Werkplaats BV: Spinnerij, Weverij, Confectie.
3. Lijst de kostendragers op volgens [[kostendrager]] §scope: producten, productgroepen,
   opdrachten of klanten.
4. Vermijd verwarring tussen centra (waar) en dragers (waarop) — zie examen-valkuilen.
5. Wijs codes toe binnen klasse 9 (vrij): bv. 90 kostensoorten, 91 centra, 92 dragers.


> [!example]- Voorbeeld: Yperse Werkplaats BV — productie van wollen tapijten met drie kostencentra (Spinnerij, Weverij, Confectie) en productlij…
> Yperse Werkplaats BV — productie van wollen tapijten met drie kostencentra (Spinnerij, Weverij, Confectie) en productlijnen (tapijt-standaard / tapijt-luxe / kleed-handgeknoopt).
>
> 1. **Kostensoorten (klasse 90)** 📊
>
>    | Code  | Kostensoort                    |
>    |-------|--------------------------------|
>    | 9000  | Grondstoffen (wol, garen)      |
>    | 9001  | Hulpstoffen (kleurstoffen)     |
>    | 9020  | Directe arbeid                 |
>    | 9021  | Indirecte arbeid               |
>    | 9030  | Afschrijvingen productiemachines |
>    | 9040  | Energiekosten                  |
>    | 9050  | Onderhoud                      |
>    
>
> 2. **Kostencentra (klasse 91)** 📊
>
>    | Code  | Kostencentrum  | Type        |
>    |-------|----------------|-------------|
>    | 9100  | Onderhoud      | Hulp-centrum |
>    | 9101  | Stroomvoorziening | Hulp-centrum |
>    | 9110  | Spinnerij      | Hoofd-centrum |
>    | 9120  | Weverij        | Hoofd-centrum |
>    | 9130  | Confectie      | Hoofd-centrum |
>    | 9140  | Administratie  | Algemeen     |
>    
>
> 3. **Kostendragers (klasse 92)** 📊
>
>    | Code  | Kostendrager           |
>    |-------|------------------------|
>    | 9200  | Tapijt-standaard       |
>    | 9201  | Tapijt-luxe            |
>    | 9202  | Kleed-handgeknoopt     |
>    
>

**Grondslag**: [[kostensoort]] §klassen-9, [[kostencentrum]] §afbakening, [[kostendrager]] §scope, [[rekeningenstelsel-analytisch]] §MAR-bijlage-1, KB 21.10.2018 art. MAR

> [!warning]- Houd kostencentrum (plaats van verbruik) en kostendrager (object van toerekening) consequent gescheiden.
>
> _Vaak fout gedaan_: Een afdeling als drager registreren of een product als centrum — leidt tot onbruikbare rapporten.
>
> _Grondslag_: [[kostencentrum]] §verschil-met-drager, [[kostendrager]] §scope

### 3. Kiezen van verdeelsleutels voor indirecte kosten

Stel per indirecte-kosten-categorie een verdeelsleutel vast die de oorzakelijkheid tussen het verbruik en de drager benadert.

**Waarom?** De verdeelsleutel bepaalt de toegerekende kost — een verkeerde sleutel vertekent zowel voorraadwaardering als prijszetting.

**📥 Input**:
- Lijst indirecte kostensoorten → **Onderhoud, energie, leiding, etc.** _(document)_
- Historische data + kennis productieproces → **Drijvers van verbruik** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Sleutelmatrix → **Per indirecte kost een toewijzingsbasis (uren, m², kWh, ...)** _(document)_

**🛠️ Hoe**:

1. Volg [[verdeelsleutel]] §oorzakelijkheidsprincipe: kies een grootheid die het
   werkelijk verbruik weerspiegelt (machine-uren voor energie, m² voor huur).
2. Onderscheid primaire verdeling (kost → centrum) van secundaire verdeling
   (hulp-centra → hoofd-centra) volgens [[verdeelsleutel]] §primair-secundair.
3. Test plausibiliteit: pas de sleutel toe op een historische maand en kijk
   of de toerekening realistisch is.
4. Documenteer keuzes (waarom deze sleutel) — onmisbaar voor consistentie en audit.
5. Voor toewijzing aan dragers: gebruik bij voorkeur cost-drivers zoals in
   [[abc-methode]] §activiteit-drivers; alleen bij beperkte complexiteit volstaat
   één globale opslag.


**Grondslag**: [[verdeelsleutel]] §oorzakelijkheidsprincipe, [[abc-methode]] §activiteit-drivers

### 4. Kiezen van het registratiesysteem (koppeling met algemene boekhouding)

Beslis hoe analytische klasse-9-rekeningen gekoppeld worden aan de algemene boekhouding (eenvoudige spiegel, proportionele integratie, of waarderingsneutrale variant).

**Waarom?** De koppeling bepaalt hoe en wanneer reconciliatie tussen klasse 6 en klasse 9 gebeurt en of analytische cijfers kunnen afwijken van algemene.

**📥 Input**:
- Vereisten uit stap 1 → **Sturingsritme + audit-traceerbaarheid** _(document)_

**📤 Output**:
- Geselecteerd registratiesysteem → **Type + reconciliatie-procedure** _(conclusie)_

**🛠️ Hoe**:

1. Vergelijk de drie systemen:
   - [[registratiesysteem-eenvoudige-integratie]]: klasse-9 spiegelt klasse-6
     één-op-één, zelfde waardering, geen reconciliatie nodig.
   - [[registratiesysteem-proportionele-integratie]]: vaste verdeelsleutel-koppeling,
     geschikt voor stabiele productieprocessen.
   - [[registratiesysteem-waarderingsneutraal]]: analytische waardering mag afwijken
     (bv. opportuniteitskost) mits expliciet verklaard — conform CBN 3/3 §principe.
2. Voor Yperse Werkplaats BV: eenvoudige integratie volstaat voor de jaarrekening;
   maandelijkse rapportering werkt waarderingsneutraal voor management-besluiten.
3. Documenteer reconciliatie-procedure: hoe vaak, door wie, welke verschillen mogen
   voorkomen en hoe ze worden verklaard.


**Grondslag**: [[registratiesysteem-eenvoudige-integratie]], [[registratiesysteem-proportionele-integratie]], [[registratiesysteem-waarderingsneutraal]] §CBN-3-3

> [!warning]- Sluit aan op bestaande IT-systemen en analytische rapporteringsroutines vóór je kiest.
>
> _Vaak fout gedaan_: Een theoretisch zuiver systeem kiezen dat in de praktijk niet onderhouden wordt.
>
> _Grondslag_: [[registratiesysteem-waarderingsneutraal]] §praktijk

### 5. Testen, documenteren en uitrollen

Test het stelsel op een proefmaand, documenteer alle keuzes in een analytisch handboek en train de gebruikers.

**Waarom?** Zonder testrun blijven inconsistenties verborgen; zonder documentatie verwatert het stelsel binnen een jaar.

**📥 Input**:
- Reeël boekhoud-maand → **Werkelijke aankoop-, verbruik- en personeelsdata** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Analytisch handboek + opleiding → **Rekeningenkader, sleutels, procedures** _(document)_

**🛠️ Hoe**:

1. Boek één maand parallel in algemene én analytische boekhouding.
2. Vergelijk klasse-6-totalen met klasse-9-totalen — verschil moet verklaarbaar zijn.
3. Stel een schriftelijke procedure op: wie boekt wat in klasse 9, wanneer worden
   hulp-centra naar hoofd-centra verdeeld, wie reconcilieert.
4. Geef opleiding aan boekhouding én aan de afdelingsverantwoordelijken die de
   analytische rapporten gaan lezen.
5. Plan een eerste-jaars-evaluatie: zijn de informatie-objecten uit stap 1 werkelijk
   gehaald? Stel bij waar nodig.


**Grondslag**: [[analytische-boekhouding]] §implementatie


## Voorbeelden



