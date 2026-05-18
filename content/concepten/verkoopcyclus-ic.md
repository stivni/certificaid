---
title: Verkoopcyclus en interne controle
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.IX.C
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verkoopcyclus-ic.json
gegenereerd_op: '2026-05-18'
---
# Verkoopcyclus en interne controle 🤖

De verkoopcyclus is de keten van order tot inning van klantvorderingen. Interne controle focust op vermijden van fictieve omzet, niet-gefactureerde leveringen, oneigenlijke kortingen en oninbare vorderingen. Cut-off rond balansdatum is kritisch voor de juistheid van de resultatenrekening. Stagiairs komen dit tegen bij walkthroughs van het sales-proces en bij analytische review van DSO-evolutie.

> [!summary] Korte inhoud
> Interne controle in de verkoopcyclus is het geheel van maatregelen die de stadia order → kredietacceptatie → levering → facturatie → inning beheersen, met als doel fictieve omzet, niet-gefactureerde leveringen, cut-off-fouten en oninbare vorderingen te voorkomen of te detecteren.

> [!info] Behoort tot: [[cyclus-analyse-ic]]

Interne controle in de verkoopcyclus is het geheel van maatregelen die de stadia order → kredietacceptatie → levering → facturatie → inning beheersen, met als doel fictieve omzet, niet-gefactureerde leveringen, cut-off-fouten en oninbare vorderingen te voorkomen of te detecteren.


## Bouwstenen

### Kredietacceptatie en kredietlimiet 🤖

De kredietwaardigheid van een klant wordt vooraf getoetst en vertaald in een kredietlimiet die het ERP-systeem afdwingt.

**Waarom?** Leveren zonder kredietcheck vergroot het risico op oninbare vorderingen; de limiet werkt als preventieve controle.


**In de praktijk**: Bij een nieuwe klant raadpleegt de salesverantwoordelijke de KBO en de jaarrekening; bij grote bedragen wordt een kredietverzekeraar geconsulteerd. Het ERP-systeem blokkeert automatisch leveringen aan klanten in over-limit of in mora.


_Grondslag: Audit-cyclus-doctrine + boekhoudkundige voorzichtigheid_

### Order-levering-facturatie-match 🤖

Order, levering en factuur worden tegen elkaar afgezet — een spiegel van de three-way match aan de aankoopzijde.

**Waarom?** Detecteert leveringen zonder factuur, facturen zonder levering en cut-off-fouten rond balansdatum.


**In de praktijk**: Het ERP genereert maandelijks een lijst van delivery notes zonder bijhorende factuur; cut-off rond 31 december wordt apart gecontroleerd.


_Grondslag: Audit-doctrine + WBTW factureringsverplichting_

### Functiescheiding sales-levering-facturatie-inning 🤖

De rollen verkoper, magazijnier, facturator en inner worden door verschillende personen ingevuld.

**Waarom?** Wie verkoopt én factureert kan kortingen toekennen aan zichzelf bevriende klanten; wie factureert én int kan ontvangen bedragen onderscheppen.




_Grondslag: [[functiescheiding]] §toepassing-verkoop_

### Aged-receivables-opvolging 🤖

Wekelijkse rapportering van uitstaande klantenvorderingen per ouderdomsbucket triggert herinneringen, ingebrekestellingen en voorzieningen.

**Waarom?** Vorderingen zonder follow-up worden oninbaar; cijferanalyse via DSO detecteert sluipende problemen.



Bij Yperse Werkplaats BV stuurt boekhouder Cindy Demeyer op dag 31 een herinnering, op dag 61 een ingebrekestelling, en op dag 91 wordt de vordering doorgegeven aan de juridische dienst van Helena Devos en wordt een voorziening voor dubieuze debiteuren geboekt. _(Yperse Werkplaats BV, Cindy Demeyer, Helena Devos)_ 🤖

_Grondslag: Boekhoudkundige voorzichtigheid (KB 21.10.2018)_


## Berekening

### Procesgang verkoopcyclus — stappen + IC-haakpunten

### 1. Klantenacceptatie en krediettoekenning

Toets vooraf de kredietwaardigheid van de klant; ken een kredietlimiet toe.

**Waarom?** Levering zonder kredietcheck verhoogt het risico op oninbare vordering.

**📥 Input**:
- Klantvoorstel → **KBO-data, jaarrekening** _(due-diligence)_

**📤 Output**:
- Klantmaster → **kredietlimiet** _(ERP-masterdata)_

**🛠️ Hoe**:

1. Nieuwe klant: doe due-diligence (KBO, jaarrekening, kredietverzekeraar).
2. Bepaal kredietlimiet op basis van solvabiliteit en sector.
3. ERP blokkeert leveringen aan klanten in over-limit of in mora.

**Grondslag**: Audit-cyclus-doctrine

### 2. Order en leveringsautorisatie

Order aanvaarden en magazijn-uitlevering autoriseren.

**Waarom?** Levering zonder geldige order leidt tot leveringen op naam van fictieve klanten of leveringen die later worden 'vergeten' te factureren.

**📥 Input**:
- Order → **klant, artikel, hoeveelheid, prijs** _(ERP-record)_

**📤 Output**:
- Delivery note → **ondertekening sales** _(ERP-record)_

**🛠️ Hoe**:

1. Sales tekent order; ERP creëert delivery note.
2. Magazijn levert uit op basis van delivery note (geen mondelinge instructie).

**Grondslag**: [[functiescheiding]] §sales-levering

### 3. Levering en facturatie

Goederen leveren tegen ondertekende leveringsbon; factuur uitschrijven binnen 15 dagen (btw-vereiste).

**Waarom?** Time-gap tussen levering en factuur is fraude-risico (cut-off): omzet niet boeken in juiste periode.

**📥 Input**:
- Delivery note → **ondertekening klant** _(ERP-record)_

**📤 Output**:
- Verkoopfactuur → **btw-conform** _(boeking)_

**🛠️ Hoe**:

1. Klant tekent leveringsbon bij ontvangst.
2. ERP genereert automatisch factuur uit delivery note.
3. Maandelijks: alle delivery notes zonder factuur onderzoeken.

**Grondslag**: WBTW + cut-off-doctrine

### 4. Inning en opvolging

Klant betaalt; bij niet-tijdige betaling herinnering, ingebrekestelling en eventueel juridische actie.

**Waarom?** Vorderingen zonder follow-up worden oninbaar; cijferanalyse (DSO) detecteert problemen.

**📥 Input**:
- Aged-receivables-rapport → **ouderdom per klant** _(ERP-rapport)_

**📤 Output**:
- Voorziening dubieuze debiteuren → **bedrag, klant** _(boeking)_

**🛠️ Hoe**:

1. Wekelijks: aged-receivables-rapport.
2. > 30 dagen: herinnering.
3. > 60 dagen: ingebrekestelling.
4. > 90 dagen: juridische actie + voorziening voor dubieuze debiteuren.

**Grondslag**: Boekhoudkundige voorzichtigheid


## Valkuilen

> [!warning]- Cut-off rond balansdatum is een klassiek frauderisico: leveringen van december worden in januari gefactureerd om omzet te verschuiven
> ⚠️ Cut-off rond balansdatum is een klassiek frauderisico: leveringen van december worden in januari gefactureerd om omzet te verschuiven. Substantieve test: zoek delivery notes van laatste week december tegen factuurdatum. 🤖


> [!warning]- Kortingen en creditnota's zijn typische manipulatie-vectoren
> ⚠️ Kortingen en creditnota's zijn typische manipulatie-vectoren. Eis voor elke creditnota: aparte goedkeuring, traceerbare reden, geen link aan dezelfde persoon die de oorspronkelijke factuur boekte. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]
- **Vereist kennis van**: [[beheersactiviteiten]]

## Voorbeelden

### Cut-off-manipulatie en oneigenlijke creditnota's bij Rotex Roeselare NV

_Personages: Rotex Roeselare NV, Robert Vandenberghe, Sofie Janssens_

Rotex Roeselare NV is een grote NV (volledig schema). Salesdirecteur Robert Vandenberghe wil zijn jaardoel halen en factureert in week 52 voor € 850.000 aan leveringen die pas in week 2 van het nieuwe jaar effectief vertrekken. Tegelijk reikt hij in januari voor € 320.000 creditnota's uit aan dezelfde klanten — zonder retourbewijzen. Externe auditor Sofie Janssens detecteert de cut-off-breuk en de niet-gegronde creditnota's bij haar substantieve testen rond balansdatum.

1. Cut-off-test: Sofie vergelijkt de datums op leveringsbons (van het magazijnsysteem) met factuurdatums voor de laatste 10 dagen van december en de eerste 10 dagen van januari. Resultaat: 14 facturen met factuurdatum ≤ 31/12 maar leveringsbon ≥ 02/01.
2. Creditnota-test: Sofie filtert alle creditnota's > € 10.000 in januari. Voor 9 van de 11 ontbreekt een retourbewijs of een goedgekeurde commerciële geste-aanvraag.
3. IC-zwakte: bouwsteen 'Functiescheiding sales-levering-facturatie-inning' niet hard genoeg — Robert kan zelf creditnota's autoriseren tot € 50.000. Bouwsteen 'Order-levering-facturatie-match' wordt niet automatisch afgedwongen voor cut-off rond balansdatum.
4. Audit-conclusie: omzet 20X1 wordt met € 850.000 verminderd, oninbare creditnota's worden teruggedraaid. Vermoeden van bewuste resultaatmanipulatie → ISA 240-respons (fraude in financiële verslaggeving).
#### Correctieboeking cut-off — omzet terug naar 20X2
| Rekening | Debet | Credit |
|---|---:|---:|
| 700 — Verkopen _(Storno fictieve omzet december)_ | 850000 |  |
| 451 — Verschuldigde btw | 178500 |  |
| 400 — Handelsvorderingen |  | 1028500 |

🤖



