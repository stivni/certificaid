---
title: Begeleiden van de inbreng in geld en in natura bij oprichting
tags:
- concept
- competentie
- po-1-7
- po-3-0
linked_anchors:
- 3.0.taak.1
- 3.0.I
- 1.7.taak.1
programmaonderdelen:
- '1.7'
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/begeleiden-inbreng-bij-oprichting.json
gegenereerd_op: '2026-05-21'
---
# Begeleiden van de inbreng in geld en in natura bij oprichting 🔗

Operationele competentie: de oprichter begeleiden bij het correct uitvoeren van de inbreng — voor geld via deponering op een geblokkeerde rekening vóór de notariële akte, voor natura via revisorenverslag en oprichtersverslag. Doel: vermijden van nietigheid van de akte en van oprichtersaansprakelijkheid voor kennelijke overwaardering.



## In de praktijk

- Inbreng in geld is administratief licht (1 storting + attest) maar moet vóór de akte gebeuren — niet erna.
- Inbreng in natura vraagt 2-6 weken voorbereiding voor het revisorenverslag — plan dit vroeg in het oprichtings-tijdspad.
- Voor een eenvoudige BV met enkel cash-inbreng en € 18.600 vennootschapsbelasting-drempel: vergeet de boekhouding-impact niet — eerste storting wordt geboekt als 100 — kapitaal of inbreng + 55 — bank, niet andersom.

## Stappen

### 1. Identificeren van het inbreng-type per oprichter

Klassificeer per oprichter wat wordt ingebracht: geld, lichamelijk roerend goed, onroerend goed, IP-rechten, schuldvorderingen, of een bestaand handelsfonds.

**Waarom?** Het inbreng-type bepaalt de procedure: geld = geblokkeerde rekening, natura = bedrijfsrevisor-verslag + oprichtersverslag, nijverheid bij BV/CV = mogelijk maar in apart regime.

**📥 Input**:
- Intentieverklaringen oprichters → **Bedrag + aard per oprichter** _(vrije-tekst)_

**📤 Output**:
- Inbreng-mapping-tabel → **Per oprichter: type + waarde + procedure** _(tabel)_

**🛠️ Hoe**:

1. Lijst per oprichter wat hij inbrengt — bedrag en aard.
2. Klassificeer per inbreng: (a) geld — art. 5:9 BV / 7:9 NV; (b) natura — art. 5:7 BV / 7:7 NV; (c) nijverheid — alleen BV/CV (niet NV) via art. 5:8/6:11.
3. Bij mengsel (cash + machine): splits in twee aparte inbrengen, elke met eigen procedure.
4. Verwijs naar [[inbreng-vennootschap]] voor algemene classificatie.

**Grondslag**: [[inbreng-vennootschap]]; WVV art. 5:7-5:9, 7:7-7:9

### 2. Begeleiden van de inbreng in geld

Voor inbreng in geld: laat oprichter het bedrag deponeren op een bijzondere rekening (geblokkeerd) op naam van 'vennootschap in oprichting' bij een EER-kredietinstelling vóór het verlijden van de akte, met overhandiging van het deponeringsbewijs aan de notaris.

**Waarom?** Geblokkeerde-rekening-procedure beschermt de inbreng tegen onttrekking vóór de oprichting — pas bij verkrijging rechtspersoonlijkheid wordt het geld vrijgegeven aan de vennootschap.

**📥 Input**:
- Bedragen inbreng in geld per oprichter → **Cash-bedragen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Deponeringsbewijs van EER-kredietinstelling → **Voor notaris** _(wettelijk-document)_

**🛠️ Hoe**:

1. Open bij een Belgische of EER-gevestigde kredietinstelling een bijzondere rekening 'NAAM BV in oprichting'.
2. Oprichter(s) storten hun cash-inbreng op die rekening (vóór de akte).
3. Vraag bij de bank een attest van deponering — kan elektronisch.
4. Overhandig dit attest aan de notaris vóór het verlijden van de akte.
5. De rekening is geblokkeerd totdat de notaris bevestigt dat de vennootschap rechtspersoonlijkheid heeft verkregen.

> [!example]- Voorbeeld: Oprichtingen Oostende BV — inbreng in geld € 25.000
> Oprichtingen Oostende BV — inbreng in geld € 25.000.
>
> 1. **Bankprocedure** 💬
>
>    Pieter Vermeulen opent op 12 maart bij KBC een rekening 'Oprichtingen Oostende BV in oprichting'. Hij stort € 25.000 op 14 maart. De bank levert hetzelfde attest af. Notaris verlijdt akte op 18 maart; deponering is dan reeds 4 dagen ouder.
>    
>

**Grondslag**: WVV art. 5:9 (BV), 7:9 (NV), 6:12 (CV)

### 3. Voorbereiden van de inbreng in natura — revisorenverslag

Voor inbreng in natura: laat een bedrijfsrevisor (of in BV optioneel een gecertificeerd accountant volgens recente herzieningen) een verslag opstellen over de beschrijving + de gebruikte waarderingsmethoden + de waarde van de inbreng vóór de notariële akte.

**Waarom?** Het revisoren-/accountantsverslag is de objectivering die overwaardering moet voorkomen — kennelijke overwaardering activeert hoofdelijke oprichtersaansprakelijkheid.

**📥 Input**:
- Beschrijving van het inbreng-goed → **Goedbeschrijving + voorgestelde waardering** _(vrije-tekst)_
- Onderliggende waarderingsdocumenten → **Schattingsverslag, facturen, marktwaarderingen** _(wettelijk-document)_

**📤 Output**:
- Revisorenverslag inbreng in natura → **Conform [[inbreng-in-natura-verslag]]** _(wettelijk-document)_

**🛠️ Hoe**:

1. Stel een schrijven op aan een bedrijfsrevisor (extern) met opdracht: 'Beoordeel waardering inbreng in natura voor oprichting BV X.'
2. Lever de revisor: (a) beschrijving van het goed, (b) waarderingsdossier, (c) ontwerp-statuten.
3. Revisor stelt verslag op met: beschrijving inbreng, gebruikte waarderingsmethoden, conclusie of de inbreng-waarde minstens overeenstemt met aantal en pari-waarde van uit te geven aandelen.
4. De oprichters stellen daarnaast een oprichtersverslag op met motivering van de waardebepaling — verplicht naast het revisorenverslag.
5. Beide verslagen worden vóór de akte aan de notaris overhandigd. Zie [[inbreng-in-natura-verslag]] voor detail.

**Grondslag**: [[inbreng-in-natura-verslag]]; WVV art. 5:7 (BV), 7:7 (NV)

### 4. Voorbereiden van mogelijke quasi-inbreng

Wanneer de vennootschap binnen twee jaar na oprichting een goed verwerft van een oprichter, aandeelhouder of bestuurder voor minstens 1/10e van het kapitaal/eigen vermogen — bereid een quasi-inbrengverslag voor (art. 5:99 BV / 7:8 NV).

**Waarom?** De quasi-inbreng-regels voorkomen ontduiking van de inbreng-in-natura-procedure door eerst geld in te brengen en het goed later 'gewoon' aan de vennootschap te verkopen.

**📥 Input**:
- Aankoop-intentie van de oprichter → **Goed + prijs + tijdstip** _(vrije-tekst)_

**📤 Output**:
- Quasi-inbrengverslag → **Indien drempel + tijdsvenster overschreden** _(wettelijk-document)_

**🛠️ Hoe**:

1. Detecteer tijdens de eerste 2 jaar elke transactie tussen vennootschap en oprichter/aandeelhouder/bestuurder.
2. Toets per transactie: bedrag ≥ 10% van het kapitaal (NV) of eigen vermogen (BV)?
3. Zo ja: bedrijfsrevisorverslag + bestuursverslag verplicht — analoog aan inbreng in natura.
4. Algemene vergadering moet de verrichting goedkeuren.
5. Zie [[quasi-inbreng-verslag]] voor detail.

**Grondslag**: [[quasi-inbreng-verslag]]; WVV art. 5:99 (BV), 7:8 (NV)

### 5. Reviewen aansprakelijkheidsrisico's en cliënt informeren

Vóór ondertekening van de akte: informeer oprichter over de aansprakelijkheid voor kennelijke overwaardering van inbreng in natura en voor onjuiste vermeldingen in de akte.

**Waarom?** Oprichter moet weten dat hij hoofdelijk aansprakelijk blijft voor schade aan derden in geval van overwaardering — zelfs te goeder trouw. Dit verandert de stevigheid waarmee hij de waardering wil bevestigen.

**📥 Input**:
- Concept-akte + revisorenverslag → **Voorgestelde inbrengwaardes** _(wettelijk-document)_

**📤 Output**:
- Risico-briefing oprichter → **Schriftelijke informatie + bevestiging gelezen** _(tekst-document)_

**🛠️ Hoe**:

1. Lijst per inbreng in natura de waardering + bron + risico-niveau (laag voor goed-onderbouwde marktwaarde, hoger voor IP/handelsfonds).
2. Verwijs naar [[oprichtersaansprakelijkheid]] §kennelijke-overwaardering en art. 5:16 1° / 7:18 1°.
3. Vraag oprichter te bevestigen dat hij de inbrengwaarden heeft gereviewed en dat ze conservatief zijn.
4. Documenteer in cliëntdossier — beschermt de accountant bij latere discussie.

**Grondslag**: [[oprichtersaansprakelijkheid]]; WVV art. 5:16 1°, 7:18 1°

> [!warning]- Een 'positief' revisorenverslag beschermt de oprichter niet absoluut — een rechter kan nog steeds 'kennelijke' overwaardering vaststellen als bv. een marktwaarde-schatting frauduleus was.
>
> _Vaak fout gedaan_: Oprichter denkt dat revisorenverslag = volledige indemnisering. Niet juist: het is een waarderings-validatie, geen aansprakelijkheidsoverdracht.


## Voorbeelden



