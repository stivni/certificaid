---
title: "Fouten en fraude (in context van interne controle)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.7.VI
  - 1.7.VI.A
  - 1.7.VI.B
  - 1.7.VI.C
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/fouten-en-fraude.json"
---

# Fouten en fraude (in context van interne controle)

_Kader_

🏛️ Kader · Anchors: `1.7.VI` · `1.7.VI.A` · `1.7.VI.B` · `1.7.VI.C` · Wave: `cluster-extract-controle-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: errors and fraud · anomalies · irregularities · intentional vs unintentional misstatements · fouten verspilling fraude — **Vertalingen**: fr: erreurs et fraudes

## Definitie

📖 In de context van interne controle worden afwijkingen onderverdeeld in drie categorieen langs de as bedoelen en gevolgen: (1) fouten zijn onbedoelde afwijkingen door menselijke vergissingen, onachtzaamheid of kennistekort; (2) fraude is bewust handelen voor onrechtmatig financieel voordeel - hetzij door valse financiele verslaggeving, hetzij door oneigenlijke toe-eigening van activa; (3) verspilling is een onnodig of inefficient gebruik van middelen, zonder per se intentie tot bedrog, maar wel een aandachtspunt voor interne controle die operationele doelmatigheid nastreeft. Elke categorie vraagt een andere mitigatie-strategie.

<small>📚 ISA 240 — par. 2-3 - definities fraude (intentioneel) versus fouten (onintentioneel) — _norm_</small>

## Substantie

🔗 Het kernverschil tussen fouten en fraude is intentie - en intentie is in audit-context moeilijk te bewijzen. Voor de externe auditor (ISA 240) en voor interne controle is het pragmatisch onderscheid dit: fouten worden mitigeerbaar door betere procedures, training, IT-validaties; fraude wordt mitigeerbaar door functiescheiding, controle door onafhankelijken, monitoring en een sterk ethisch klimaat (tone at the top). De fraudedriehoek van criminoloog Donald Cressey (1953) - druk, gelegenheid, rationalisatie - is het standaardmodel om frauderisico te begrijpen en te bestrijden door telkens een van de drie hoeken weg te nemen.

<small>📚 ISA 240 — Bijlage 1 - frauderisicofactoren langs de drie hoeken van de fraudedriehoek — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio voor expliciete categorisering is dat verschillende interventies nodig zijn. Een fout-mitigatie (extra checklist, opleiding, geautomatiseerde herrekening) werkt niet tegen fraude - want de fraudeur kent de checklist en omzeilt ze bewust. Omgekeerd voorkomt functiescheiding fouten beperkt - een aandachtige medewerker maakt nog steeds vergissingen. Verspilling vraagt budget-discipline en KPI-monitoring, geen detectieve controles. Wie alle afwijkingen op dezelfde hoop gooit, mist het onderscheid en kiest de verkeerde mitigatie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege`

Universeel kader, geldt in elke audit-context (ISA 240 verplicht voor elke jaarrekening-audit) en in elk interne-controle-ontwerp.

**✅ Voor**
- 📖 Bij ontwerp van interne controle (stap 2: risico-identificatie), bij externe controle (ISA 240-verplichting tot specifieke aandacht voor fraude), bij interne audit (frauderisico-audits), bij incident response na een vastgestelde onregelmatigheid.

## Sub-concepten

### 📦 Fouten (onbedoelde afwijkingen)  
_`kader` (subconcept)_

#### Definitie

📖 Fouten zijn afwijkingen zonder intentie van bedrog: vergissingen bij invoer, foutieve berekeningen, verkeerde toepassing van een boekhoudregel door kennistekort, vergeten boekingen, dubbele inboeking. Komen veel vaker voor dan fraude maar zijn doorgaans makkelijker te detecteren (geen verhulling) en goedkoper te remediëren.

<small>📚 ISA 240 — par. 2 - fouten vs fraude — _norm_</small>

#### ⚙️ Mitigatie van fouten  
_`mechanisme`_

🔗 (1) Heldere procedures en checklists; (2) opleiding en awareness; (3) geautomatiseerde validaties (mandatory fields, herrekening, dropdown-keuzes, dubbele-invoer-preventie); (4) vier-ogen-principe op kritieke handelingen; (5) detectie via aansluitingen en uitzonderingsrapporten. Volledige eliminatie is onmogelijk - geen procedure maakt mensen feilloos.

<small>📚 ISA 315 (herzien-2019) — par. 20 interne beheersingsactiviteiten — _norm_</small>

### 📦 Fraude (intentioneel bedrog voor voordeel)  
_`kader` (subconcept)_

#### Definitie

📖 Fraude vereist intentie tot bedrog voor onrechtmatig voordeel. ISA 240 onderscheidt twee hoofdtypes: (a) frauduleuze financiele verslaggeving - vervalsen van rekeningen om de financiele toestand mooier voor te stellen (typisch door of met medeplichtigheid van het management); (b) oneigenlijke toe-eigening van activa - diefstal van kasmiddelen, voorraad, intellectuele eigendom (typisch door medewerkers). Tipping-off-fraude richting derden via valse facturen of CEO-fraud richting medewerkers zijn varianten die de externe wereld involveren.

<small>📚 ISA 240 — par. 3 - frauduleuze financiele verslaggeving + oneigenlijke toe-eigening — _norm_</small>

#### ⚙️ Fraudedriehoek (Cressey)  
_`mechanisme`_

📖 Fraude vereist gelijktijdig drie elementen: (1) Druk of stimulans - persoonlijke financiele nood, target-druk om winsten te halen, schulden, gokverslaving; (2) Gelegenheid - zwakke interne controle, geen functiescheiding, vertrouwde positie zonder oversight, complexe transactiestructuren die verhulling mogelijk maken; (3) Rationalisatie - de fraudeur overtuigt zichzelf dat zijn gedrag aanvaardbaar is ('ik leen maar even', 'ze betalen me te weinig', 'iedereen doet het'). ISA 240 Bijlage 1 lijst gedetailleerde risicofactoren langs deze drie assen. Mitigatie: weg een van de drie hoeken (druk reduceren is moeilijk; gelegenheid reduceren via interne controle is de hefboom; rationalisatie reduceren via ethisch klimaat en tone at the top).

<small>📚 ISA 240 — Bijlage 1 - drie omstandigheden die typisch aanwezig zijn bij fraude — _norm_</small>

#### ⚙️ Mitigatie van fraude  
_`mechanisme`_

📖 (1) Functiescheiding (ACR-IH): voorkomt dat een persoon alleen een hele transactie kan voltooien; (2) onafhankelijke controles door interne audit of externe accountant; (3) ethisch klimaat - duidelijke gedragscode, klokkenluider-kanaal, voorbeeldgedrag van bestuur; (4) verplichte vakantie en jobrotatie in sleutelfuncties (vervanger detecteert afwijkingen tijdens afwezigheid); (5) monitoring via SIEM, anomalie-detectie, uitzonderingsrapporten; (6) achtergrond-screening van personeel in vertrouwensposities; (7) fraude-hotline.

<small>📚 ISA 240 — Bijlage 1 - mitigatie via verkleinen gelegenheid — _norm_</small>

### 📦 Verspilling (waste)  
_`kader` (subconcept)_

#### Definitie

🔗 Verspilling is onnodig of inefficient gebruik van middelen zonder bedrog-intentie: te dure inkoop omdat geen prijsvergelijk gedaan wordt, overuren door slechte planning, voorraadverliezen door slecht magazijnbeheer, dubbel werk door slechte communicatie tussen afdelingen. Het is geen primaire focus van financiele audit (geen impact op getrouw beeld als de werkelijke kosten correct geboekt zijn) maar wel een element van interne controle - doelstelling 3: doeltreffendheid en doelmatigheid.

<small>📚 ISA 315 (herzien-2019) — par. A91 doelstellingen IC inclusief doeltreffendheid — _norm_</small>

#### ⚙️ Mitigatie van verspilling  
_`mechanisme`_

🔗 Budgetdiscipline (afwijkingen-analyse), efficiency-KPI's (kost per eenheid, voorraadrotatie, productiviteit), procurement-procedures met verplichte prijsvergelijk boven een grens, kosten-budgetten per afdeling met maandelijkse rapportering. Eerder een management-control-aangelegenheid dan een interne-controle-aangelegenheid in enge zin.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 📜 Afwijkingen accumuleren tijdens controle (ISA 450)  
_`regel`_

📖 ISA 450 vereist dat de externe auditor tijdens de controle alle geidentificeerde afwijkingen accumuleert (uitgezonderd duidelijk triviale). Aan het einde van de controle worden niet-gecorrigeerde afwijkingen geevalueerd op materialiteit en aan het management voorgelegd voor correctie. De auditor maakt onderscheid tussen fouten (mogelijk een isolated incident) en aanwijzingen voor fraude (vraagt verdere overweging volgens ISA 240).

<small>📚 ISA 450 — par. 5-8 accumuleren en evalueren afwijkingen — _norm_</small>

### ⚠️ Indicatoren van fraude (red flags)  
_`risico`_

📖 ISA 240 Bijlage 1 lijst frauderisicofactoren: ongebruikelijke transacties net voor jaareinde, transacties met verbonden partijen onder ongebruikelijke condities, ineffectieve monitoring door management, hoog personeelsverloop in sleutelposities, druk op management om financiele targets te halen, geen verplichte vakantie in sleutelfuncties, klachten van klanten over factureringsfouten, anonieme tips, ongebruikelijk levensstandaard van medewerker in vertrouwenspositie. Geen enkel signaal alleen bewijst fraude - patroon en context bepalen.

<small>📚 ISA 240 — Bijlage 1 — _norm_</small>

### ✴️ Professioneel-kritische instelling tegenover fraude  
_`principe`_

📖 ISA 240 par. 12 verplicht de auditor om gedurende de hele controle een professioneel-kritische instelling aan te houden, en de mogelijkheid van fraude te erkennen, ondanks eerdere ervaring met de eerlijkheid en integriteit van het management. Dit betekent: niet automatisch geloven wat het management zegt, alert blijven voor inconsistenties, voldoende skepsis tegenover schriftelijke bevestigingen.

<small>📚 ISA 240 — par. 12-14 — _norm_</small>

### 📜 Rapportering van fraude  
_`regel`_

📖 Bij vermoeden van fraude door management: rapportering aan met governance belaste personen (auditcomite). Bij vermoeden van fraude door deze laatste zelf: direct rapport aan toezichthouder waar passend. In Belgie: CFI-melding verplicht voor witwas-vermoeden (AWW), aangifte bij parket voor strafrechtelijke feiten. Voor externe auditor bovendien overweging om de opdracht te beeindigen indien de cliente weigert te remedieren (ISA 240 par. 38).

<small>📚 ISA 240 — par. 38-43 rapportering — _norm_</small>

## Voorbeelden

### 💡 Drie scenario's bij Zelena Bio NV - fout, fraude of verspilling 🔗

_De boekhouder van Zelena Bio NV doet zijn dagelijkse werk. Drie observaties in dezelfde week. Hoe categoriseert de auditor ze?_

| Observatie | Categorisatie | Mitigatie |
| --- | --- | --- |
| Boekhouder tikt 4.500 in plaats van 45.000 EUR voor een leveranciersfactuur (komma-positie) | Fout | Geautomatiseerde tolerantietest tov inkooporder + vier-ogen-controle |
| Aankoopverantwoordelijke creëert fictieve leverancier en betaalt naar eigen rekening 12.500 EUR | Fraude (oneigenlijke toe-eigening) | Functiescheiding aankoop/betaling + onafhankelijke validatie nieuwe leveranciers + monitoring atypische betalingen |
| Marketing bestelt 3.000 promo-tassen voor een beurs waar uiteindelijk slechts 500 bezoekers komen | Verspilling | Budget-discipline + post-event ROI-analyse + procurement-procedure |

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Alle afwijkingen als fouten benaderen

**Verkeerde assumptie**: Als ik geen bewijs heb van intentie kan ik er geen fraude van maken.

**Kernpunt**: ISA 240 vereist alertness voor fraude doorheen de hele controle. Bij twijfel: verdere overweging volgens ISA 240, niet automatisch wegklasseren als fout. Patronen van schijnbaar onbeduidende fouten (altijd in eenzelfde richting, altijd bij dezelfde medewerker) kunnen een fraude-patroon zijn.

<small>📚 ISA 240 — par. 12-14 professioneel-kritische instelling — _norm_</small>

### ⚠️ Vertrouwen op een controle die wel functiescheiding heeft maar geen monitoring

**Verkeerde assumptie**: Functiescheiding voorkomt fraude.

**Kernpunt**: Functiescheiding voorkomt enkelvoudige fraude. Bij collusie (twee personen samen) of management override doorbreekt fraude functiescheiding. Daarom altijd combineren met onafhankelijke monitoring, verplichte vakantie en rotatie - die de collusie-trajecten doorkruisen.

<small>📚 ISA 240 — Bijlage 1 - collusie en management override als grondbeperkingen — _norm_</small>

### ⚠️ Tone at the top onderschatten

**Verkeerde assumptie**: Goede procedures op papier volstaan.

**Kernpunt**: Onderzoek (ACFE Report to the Nations) toont dat ethisch klimaat - voorbeeldgedrag van bestuur, gedragscode, klokkenluider-mechanisme, sanctionering van overtredingen - de sterkste preventieve maatregel tegen fraude is. Een 'do what I say not what I do'-bestuur sloopt elke procedurele controle. Cultuur is hier minstens zo belangrijk als techniek.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Externe auditor en fraude (ISA 240)

_De externe auditor moet specifiek inspelen op frauderisico - ISA 240 bovenop ISA 315._

#### 🔍 Auditor

##### 👣 Brainstorm frauderisico in opdrachtteam  
_`stap`_

📖 ISA 240 par. 15 verplicht een specifieke discussie binnen het opdrachtteam over hoe de financiele overzichten van de cliente vatbaar zouden kunnen zijn voor afwijkingen door fraude. Aandacht voor revenue recognition (verplichte focus, par. 26), management override van controles (verplichte focus, par. 32-33), en specifieke risicofactoren uit de cliente-context.

<small>📚 ISA 240 — par. 15-16 + 26 + 32-33 — _norm_</small>

##### 👣 Specifieke werkzaamheden tegen management override  
_`stap`_

📖 ISA 240 par. 32-33 vereist: (1) testing van journaalboekingen en andere aanpassingen op moment van rapportering - met focus op ongebruikelijke entries; (2) review van schattingen op tendentie bij management; (3) evaluatie van bedrijfsmatige rationaliteit van significante transacties buiten normaal verloop. Deze werkzaamheden zijn verplicht ongeacht of de auditor specifiek frauderisico inschat.

<small>📚 ISA 240 — par. 32-33 — _norm_</small>

### Advies aan cliente: fraude-preventie

_De accountant in adviesopdracht voor het opzetten van een fraude-preventie-programma._

#### 🧭 Adviseur

##### 👣 Fraude-risico-inventarisatie per cyclus  
_`stap`_

🔗 Doorloop met de cliente de transactionele cycli (aankoop, verkoop, voorraad, treasury, personeel) en identificeer per cyclus de specifieke fraude-scenario's, gecombineerd met de drie hoeken van de fraudedriehoek. Resultaat: een fraude-risico-matrix met per scenario de huidige mitigatie en eventuele leemtes. Trigger voor remediering: functiescheiding-conflicten, ontbrekende verplichte vakantie, generieke admin-accounts, geen klokkenluider-kanaal.

<small>📚 ISA 240 — Bijlage 1 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Interne controle als mitigatie-context → [[interne-controle]] _(moet-verwijzen)_
- → Functiescheiding als preventieve mitigatie → [[functiescheiding]] _(moet-verwijzen)_
- → Detectie via IC-evaluatie → [[evaluatie-interne-controle]] _(moet-verwijzen)_
- → Antiwitwas-cross (fraude raakt witwas) → [[antiwitwaspreventie]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]]
### `vereist`
- [[functiescheiding]] — Functiescheiding is de primaire preventieve mitigatie tegen oneigenlijke toe-eigening van activa.
### `triggert`
- [[antiwitwaspreventie]] — Vermoeden van fraude met geldstromen kan een meldingsplicht bij de Cel voor Financiele Informatieverwerking (CFI) triggeren onder de antiwitwaswet.
