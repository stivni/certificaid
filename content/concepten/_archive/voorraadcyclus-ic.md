---
title: Voorraadcyclus en interne controle
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.IX.E
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voorraadcyclus-ic.json
gegenereerd_op: '2026-05-21'
---
# Voorraadcyclus en interne controle 🔗

Voorraadbeheer combineert administratieve controles (perpetuele registraties, bin cards) met fysieke controles (afgesloten magazijnen, toegangsbeheer, tellingen). Verschillen tussen administratieve en fysieke voorraad triggeren onderzoek en boekingen. Stagiairs komen dit tegen bij bijwoning van jaareinde-inventarisaties (ISA 501) en bij audits met hoog fysiek-risicoprofiel.

> [!summary] Korte inhoud
> Interne controle in de voorraadcyclus is het geheel van fysieke en administratieve maatregelen die de stadia ingang, bewaring, uitgang en telling beheersen, met als doel diefstal, verkeerde waardering en telmiss te voorkomen of te detecteren.

> [!info] Behoort tot: [[cyclus-analyse-ic]]

Interne controle in de voorraadcyclus is het geheel van fysieke en administratieve maatregelen die de stadia ingang, bewaring, uitgang en telling beheersen, met als doel diefstal, verkeerde waardering en telmiss te voorkomen of te detecteren.



## Bouwstenen

### Fysieke beveiliging van het magazijn 🤖

Het magazijn is afgesloten; toegang is beperkt tot magazijnpersoneel via badge; camerabewaking dekt ingang en hoge-waarde-zones.

**Waarom?** Een open magazijn maakt directe diefstal mogelijk voor elke medewerker.


**In de praktijk**: Badge-toegang met log per persoon per uur; camera bij ingang en op zones met dure artikelen; buiten kantooruren is het magazijn verzegeld.


_Grondslag: Fysieke-beveiliging-doctrine_

### Permanente voorraad in het ERP 🤖

Elke ingang en uitgang wordt direct geboekt; het ERP toont saldo per artikel en locatie in real-time.

**Waarom?** Zonder permanente voorraad worden verschillen pas bij de jaarlijkse telling ontdekt, vaak te laat om de oorzaak te traceren.




_Grondslag: Voorraadbeheer-doctrine_

### Periodieke en jaarlijkse inventaris met scheiding teller-bewaarder ⚖️

Cycle counts (steekproef) lopen maandelijks; een volledige inventaris gebeurt jaarlijks; de teller is altijd iemand anders dan de magazijnier.

**Waarom?** Tellen door de magazijnier laat niemand toe zijn fouten of diefstal te ontdekken; onafhankelijkheid is essentieel.


**In de praktijk**: Maandelijks 10 procent van artikelen wisselend; jaarlijks een volledige telling met externe persoon, bijvoorbeeld een medewerker boekhouding.

Bij Yperse Werkplaats BV telt boekhouder Cindy Demeyer eind december de magazijnvoorraad samen met externe auditor Sofie Janssens; magazijnier Bart Vandenberghe begeleidt maar telt zelf niet. Verschillen van meer dan 500 euro per artikel worden onderzocht en geboekt. _(Yperse Werkplaats BV, Cindy Demeyer, Sofie Janssens, Bart Vandenberghe)_ 🤖

_Grondslag: KB 21.10.2018 + ISA 501 par. 4 (waarneming voorraadopname)_


## Berekening

### Procesgang voorraadcyclus — stappen + IC-haakpunten

### 1. Fysieke bewaking en toegangscontrole

Magazijn op slot; toegang beperkt tot magazijnpersoneel via badge; camerabewaking bij waardevolle voorraad.

**Waarom?** Open magazijn is een directe diefstal-mogelijkheid voor elke medewerker.

**📥 Input**:
- Toegangsbeleid → **rollen** _(interne-richtlijn)_

**📤 Output**:
- Toegangslog → **wie wanneer** _(logbestand)_

**🛠️ Hoe**:

1. Badge-toegang met log per persoon per uur.
2. Camerabewaking ingang en hoge-waarde-zones.
3. Verzegeling buiten kantooruren.

**Grondslag**: Fysieke-beveiliging-doctrine

### 2. Permanente voorraad in ERP

Elke ingang en uitgang van voorraad direct boeken; saldo zichtbaar in real-time.

**Waarom?** Zonder permanente voorraad worden verschillen pas bij jaarlijkse telling ontdekt.

**📥 Input**:
- Ingang/uitgang-event → **scan** _(ERP-event)_

**📤 Output**:
- Voorraadsaldo → **per artikel-locatie** _(ERP-saldo)_

**🛠️ Hoe**:

1. Magazijnier scant elke beweging.
2. ERP houdt saldo per artikel en locatie.
3. Discrepantie tussen sticker en saldo: direct opvolgen.

**Grondslag**: Voorraadbeheer-doctrine

### 3. Periodieke en jaarlijkse inventaris

Cycle counts maandelijks; volledige inventaris jaarlijks; telling door iemand anders dan magazijnier.

**Waarom?** Tellen door magazijnier laat niemand toe zijn fouten of diefstal te ontdekken.

**📥 Input**:
- Voorraadsaldo ERP → **te tellen artikelen** _(ERP-rapport)_

**📤 Output**:
- Inventaris-rapport + boekingen → **verschillen** _(boeking)_

**🛠️ Hoe**:

1. Maandelijks: 10 procent van artikelen wisselend tellen.
2. Jaarlijks: volledige telling met externe persoon.
3. Verschillen boven drempel: onderzoeken + boeking + actieplan.

**Grondslag**: KB 21.10.2018 + ISA 501 par. 4


## Valkuilen

> [!warning]- Magazijnier die zelf telt is geen onafhankelijke controle
> ⚠️ Magazijnier die zelf telt is geen onafhankelijke controle. Vereiste: tweede persoon, idealiter uit andere afdeling of een externe partij. 🤖


> [!warning]- Bestellingen in uitvoering (rekening 37) hebben een eigen waarderingsproblematiek volgens CBN 132/7 - niet zomaar als voorraad behandelen
> ⚠️ Bestellingen in uitvoering (rekening 37) hebben een eigen waarderingsproblematiek volgens CBN 132/7 - niet zomaar als voorraad behandelen. ⚖️
>
> _Bron: CBN 132/7_


> [!warning]- Slow-movers en obsolete voorraad worden vaak niet afgewaardeerd: voorraadinventaris bevestigt alleen aanwezigheid, niet realiseerbare waarde
> ⚠️ Slow-movers en obsolete voorraad worden vaak niet afgewaardeerd: voorraadinventaris bevestigt alleen aanwezigheid, niet realiseerbare waarde. Vereiste: afzonderlijke obsolete-analyse op basis van laatste mutatiedatum. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[productiecyclus-ic]]
- **Wordt voorondersteld in** (1): [[productiecyclus-ic]]
## Voorbeelden

### Voorraadtelling met onafhankelijke teller bij Verffabriek Veurne BV

_Personages: Verffabriek Veurne BV, Pieter Vermeulen, Sofie Janssens_

Verffabriek Veurne BV is in vereffening en moet op 31/12 een formele voorraadopname doen vóór de balans. Magazijnier Pieter Vermeulen mag niet zelf tellen — de auditrichtlijn vereist een onafhankelijke teller. Auditor Sofie Janssens woont de telling bij (ISA 501 §4). De ERP-permanente-voorraad toont 4.200 vaten verf van type 'Marine-blauw', de fysieke telling levert 3.870 vaten op — een verschil van 330 vaten × € 47 = € 15.510.

1. Vooraf: Sofie kiest 30 hoge-waarde-artikelen voor onafhankelijke recount (substantieve test); Pieter weet niet welke vooraf.
2. Tijdens telling: cycle-count-blad per zone, teller en hertel-er parafereren elk blad — bouwsteen 'Periodieke en jaarlijkse inventaris met scheiding teller-bewaarder'.
3. Verschillen-analyse: 200 vaten blijken legitiem (lekkage tijdens transport, niet geboekt — bouwsteen 'Permanente voorraad in het ERP' niet correct gevoed); 130 vaten ontbreken zonder traceerbare reden.
4. Boekhoudkundige verwerking: voorraad-aanpassing € 9.400 (legitieme lekkage) als bijzondere kost; € 6.110 als geheim verlies hangende inbraakaangifte.
5. Vereffeningsimpact: voorraad op vereffeningsbalans bedraagt na correctie 3.870 vaten × € 47 = € 181.890 in plaats van € 197.400.
#### Voorraad-correctie op vereffeningsbalans

#### Correctieboeking voor de twee verschilcomponenten
| Rekening | Debet | Credit |
|---|---:|---:|
| 6300 — Bijzondere kosten — voorraadverliezen _(Lekkage transport — legitiem)_ | 9400 |  |
| 6420 — Andere bedrijfskosten _(Ongeboekt verlies — aangifte)_ | 6110 |  |
| 33 — Voorraad gereed product |  | 15510 |

🔗



## Bronnen

[^1]: `ISA-501__sec_vereisten`
[^2]: `CBN-132-7-voorraden-en-bestellingen-in-uitvoering__sec_begrip`
