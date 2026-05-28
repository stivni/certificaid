---
title: "Fiscale procedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 2.5.I
  - 2.5.II
  - 2.5.III
  - 2.5.IV
  - 2.5.V
  - 2.5.VI
  - 2.5.VII
  - 2.5.VIII
  - 2.5.taak.1
  - 2.5.taak.2
  - 2.5.taak.3
  - 2.5.taak.4
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-procedure.json"
---

# Fiscale procedure

_Procedure_

🏛️ Kader · Anchors: `2.5.I` · `2.5.II` · `2.5.III` · `2.5.IV` · `2.5.V` · `2.5.VI` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: fiscale rechtsgang · fiscale rechtspleging — **Vertalingen**: fr: procédure fiscale

## Definitie

🔗 De fiscale procedure is het geheel van wettelijk geregelde stappen waarmee de inkomstenbelasting wordt vastgesteld, betwist en ingevorderd. Ze loopt van de aangifte door de belastingplichtige, via de controle en taxatie door de fiscus, de inkohiering en betekening van het aanslagbiljet, het administratief bezwaar (en eventueel bemiddeling), tot en met de gerechtelijke fase en — indien nodig — de gedwongen invordering. Voor inkomstenbelastingen is dit federaal geregeld in WIB92 (vestiging) en het Wetboek van de minnelijke en gedwongen invordering (inning); gewest- en gemeentebelastingen hebben hun eigen procedures.

<small>📚 WIB92 — art. 305 e.v. (aangifte) + Titel VII (vestiging, bezwaar) + art. 376quinquies (bemiddeling) — _wettekst_ · Wetboek minnelijke en gedwongen invordering — art. 15 e.v. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 In de praktijk is de fiscale procedure de 'as' waarrond elke dossier van een gecertificeerd accountant draait: tijdige aangifte voorkomt sancties, een goed onderbouwde controle-respons voorkomt rechtzettingen, een tijdig en gemotiveerd bezwaar voorkomt onnodige procedures, en kennis van invordering voorkomt verrassende beslag-aankondigingen. Elke fase heeft eigen termijnen, vormvereisten en bewijsregels — een gemiste termijn maakt de aanslag in beginsel definitief.

<small>📚 ITAA-norm algemene controlenorm — §3 — uitvoering opdracht — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De cascade-structuur (administratief → bemiddeling → rechter) komt voort uit het beginsel van behoorlijk bestuur en de scheiding der machten: de fiscus is rechter-in-eigen-zaak in eerste lijn (taxatie + bezwaar), maar de onafhankelijke rechter heeft het laatste woord. Het bezwaar is een verplichte voorportaal — wie de bezwaartermijn laat lopen, kan in beginsel niet meer naar de rechtbank. Dat dwingt belastingplichtigen en hun adviseurs tot tijdige en gestructureerde betwisting.

<small>📚 WIB92 — art. 366 + 1385decies Ger.W. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 Titel VII + Wetboek minnelijke en gedwongen invordering (2019)

De vestigingsprocedure (WIB92) is stabiel sinds 1992 met regelmatige aanpassingen van termijnen; de invordering werd in 2019 gehergroepeerd in een nieuw Wetboek (vervangt het oude KB/Inv W.).

**▶️ Trigger start**
- 📖 Verzending van het aangifteformulier door de fiscus (of de digitale beschikbaarstelling via Tax-on-web/Biztax) start de aangifteplicht en daarmee de hele cyclus.

**⏹ Trigger einde**
- 🔗 Definitieve betaling van de belasting (of definitieve ontheffing/teruggave), nadat alle bezwaar- en beroepsmogelijkheden zijn uitgeput of niet binnen de termijn werden gebruikt.

## Bouwstenen

### 👣 Stap 1 — Aangifte  
_`stap`_

📖 De belastingplichtige dient binnen de wettelijke termijn een aangifte in (PB via Tax-on-web; VenB via Biztax). De aangifte is de eerste declaratie van inkomsten en kosten en bindt de belastingplichtige tenzij hij ze tijdig rechtzet. Niet of laattijdig aangeven leidt tot ambtshalve aanslag (art. 351 WIB92) en/of belastingverhoging.

<small>📚 WIB92 — art. 305-308 + art. 351 — _wettekst_</small>

### 👣 Stap 2 — Controle  
_`stap`_

📖 De fiscus controleert de aangifte (bureel-onderzoek, controle ter plaatse of BBI-onderzoek). Tijdens de onderzoekstermijn (standaard 3 jaar; 10 jaar bij fraude) mag hij vragen om inlichtingen stellen, boeken inkijken en bankgegevens opvragen. De controle eindigt met aanvaarding, een bericht van wijziging of een proces-verbaal.

<small>📚 WIB92 — art. 315-323 + art. 354 (onderzoekstermijnen) — _wettekst_</small>

### 👣 Stap 3 — Taxatie  
_`stap`_

📖 Op basis van de aangifte en eventuele rechtzettingen vestigt de fiscus de aanslag. Wijkt de fiscus af van de aangifte → bericht van wijziging (BvW, art. 346 WIB92) met antwoordtermijn van 1 maand; geeft de belastingplichtige niet of geen geldige aangifte → ambtshalve aanslag (art. 351 WIB92).

<small>📚 WIB92 — art. 346 + art. 351-352 — _wettekst_</small>

### 👣 Stap 4 — Aanslag en inkohiering  
_`stap`_

📖 De aanslag wordt ingekohierd en betekend via een aanslagbiljet. Dit start de betalingstermijn (2 maanden na verzending) én de bezwaartermijn (zie volgende stap).

<small>📚 WIB92 — art. 297 + art. 366 — _wettekst_</small>

### 👣 Stap 5 — Administratief bezwaar  
_`stap`_

📖 Binnen 6 maanden (vanaf 1e dag van de 3e maand na verzending van het aanslagbiljet) kan de belastingplichtige bezwaar indienen bij de adviseur-generaal van de bevoegde gewestelijke directie. De directeur beslist op het bezwaar — zonder beslistermijn (in praktijk 6-18 maanden). Detail → bezwaarprocedure.

<small>📚 WIB92 — art. 366-376 — _wettekst_</small>

### 👣 Stap 6 — Fiscale bemiddeling (optioneel)  
_`stap`_

📖 Tijdens een lopend bezwaar kan de belastingplichtige de federale Fiscale Bemiddelingsdienst (FBD) inschakelen — vrijwillig en gratis. De bemiddeling schorst de beroepstermijn naar de rechtbank tot het bemiddelingsverslag wordt afgeleverd. Detail → fiscale-bemiddelingsprocedure.

<small>📚 WIB92 — art. 376quinquies — _wettekst_</small>

### 👣 Stap 7 — Gerechtelijke fase  
_`stap`_

📖 Na (afwijzende) directeursbeslissing — of na 6 maanden stilzitten — kan de belastingplichtige binnen 3 maanden naar de rechtbank van eerste aanleg (fiscale kamer). Hoger beroep bij het hof van beroep; cassatieberoep bij het Hof van Cassatie. Géén beroep bij de Raad van State voor inkomstenbelasting (volle rechtsmacht ligt bij de gewone rechter). Detail → gerechtelijke-fase-belasting.

<small>📚 Ger.W. — art. 1385decies-undecies + art. 569 16° — _wettekst_</small>

### 👣 Stap 8 — Invordering  
_`stap`_

📖 Wanneer de belasting niet vrijwillig wordt betaald, gaat de ontvanger over tot gedwongen invordering: dwangbevel, bewarend of uitvoerend beslag op activa, verkoop van goederen. Bezwaar schorst de invordering niet automatisch (uitzondering: 'onbetwist verschuldigd gedeelte' moet wel direct worden betaald). Detail → invorderingsprocedure.

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 15 e.v. — _wettekst_</small>

### ⚙️ Bewijslast-verdeling per fase  
_`mechanisme`_

📖 Algemeen gemeen-rechtelijk uitgangspunt (art. 8.4 BW): wie iets beweert, moet bewijzen. In fiscale context: (1) de fiscus moet bewijzen dat een inkomst belastbaar is en het juiste bedrag heeft; (2) de belastingplichtige moet bewijzen dat een kost aftrekbaar is, dat een vrijstelling van toepassing is, of dat een bezwaarmiddel gegrond is. Bij ambtshalve aanslag (art. 351) keert de bewijslast om: de belastingplichtige moet aantonen dat de aanslag overdreven is.

<small>📚 Oud BW — art. 8.4 (bewijslast) — _wettekst_ · WIB92 — art. 339-352 + art. 351 (ambtshalve aanslag) — _wettekst_</small>

## Valkuilen

### ⚠️ Bezwaartermijn = niet vanaf datum aanslagbiljet

**Verkeerde assumptie**: De 6 maanden bezwaartermijn begint te lopen op de datum van het aanslagbiljet.

**Kernpunt**: De termijn begint op de 1e dag van de derde maand die volgt op de verzending van het aanslagbiljet (art. 371 WIB92) — dus een aanslagbiljet verzonden op 15 april 2026 geeft een bezwaartermijn die loopt vanaf 1 juli 2026 en eindigt eind december 2026.

<small>📚 WIB92 — art. 371 — _wettekst_</small>

### ⚠️ Geen Raad van State voor inkomstenbelasting

**Verkeerde assumptie**: Als de directeur het bezwaar afwijst kun je naar de Raad van State.

**Kernpunt**: Voor inkomstenbelastingen is de gewone rechter exclusief bevoegd (Ger.W. art. 569 16°) — de Raad van State is voor andere administratieve geschillen. Beroep gaat naar de rechtbank van eerste aanleg.

<small>📚 Ger.W. — art. 569 16° — _wettekst_</small>

### ⚠️ Bezwaar schorst niet automatisch de invordering

**Verkeerde assumptie**: Zolang het bezwaar loopt moet je niets betalen.

**Kernpunt**: Het 'onbetwist verschuldigd gedeelte' blijft onmiddellijk opeisbaar. Voor het betwiste deel kan de ontvanger bewarend beslag leggen. Praktijk: wie wil voorkomen dat de fiscus invordert, moet betalen onder voorbehoud en in het bezwaar de teruggave vorderen.

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 409-410 WIB92 + art. 11 Wb.Inv. — _wettekst_</small>

## Syntheses

### 🧩 Synthese  
_`tijdslijn`_

End-to-end cascade van de fiscale procedure (federale inkomstenbelasting).

## Accountant-perspectieven

### Cliënt vertegenwoordigen in de fiscale procedure

_De gecertificeerd accountant kan de cliënt in alle administratieve fasen vertegenwoordigen (aangifte, controle, bezwaar, bemiddeling). In de gerechtelijke fase is hij beperkt tot dossiervoorbereiding — pleiten is voorbehouden aan de advocaat._

#### 💰 Fiscaal adviseur

##### 👣 Correcte en tijdige aangifte indienen  
_`stap`_

📖 Verzamel jaarstukken + fiscale stukken (lonen, bankuittreksels, fiscale fiches). Stem de aangifte af op de boekhouding. Onderteken (gecertificeerd accountants kunnen handtekening niet delegeren — ITAA-norm opdrachtbrief §3).

<small>📚 ITAA-norm opdrachtbrief — §3 — _norm_</small>

##### 👣 Cliënt bijstaan bij controle  
_`stap`_

🔗 Bij een controle ter plaatse: cliënt wijzen op zijn rechten (recht op bijstand, recht op stilte), zelf aanwezig zijn, vragen en antwoorden documenteren. Bij vraag om inlichtingen: tijdige (1 maand) en gemotiveerde respons. Geen documenten meegeven zonder kopie.

<small>📚 WIB92 — art. 315-323 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Bezwaar opstellen en indienen  
_`stap`_

📖 Bezwaar schriftelijk, gemotiveerd, ondertekend door de belastingplichtige (of door de accountant met volmacht). Adviseur-generaal van de bevoegde gewestelijke directie. Per aangetekende brief of via MyMinfin/Bizfin. Termijn: 6 maanden vanaf 1e dag derde maand na verzending aanslagbiljet.

<small>📚 WIB92 — art. 366-371 — _wettekst_</small>

#### 🧭 Adviseur

##### 👣 Bemiddeling overwegen vóór gerechtelijke procedure  
_`stap`_

🔗 Wanneer het bezwaar dreigt vast te lopen of de directeur niet beslist: overweeg een aanvraag fiscale bemiddeling (FBD). Vrijwillig, gratis, schorst de beroepstermijn naar de rechtbank. Vooral nuttig bij feitelijke betwistingen (waardering, kost-en-aftrek), minder bij zuivere rechtsvragen.

<small>📚 WIB92 — art. 376quinquies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Aanslagcyclus-detail → [[aanslag-cyclus]] _(moet-verwijzen)_
- → Bezwaar-stappen-detail → [[bezwaarprocedure]] _(moet-verwijzen)_
- → Sancties bij niet-naleving → [[fiscale-sancties]] _(moet-verwijzen)_
- → Gewestelijke procedure (Vlaamse Codex Fiscaliteit) → [[gewestelijke-fiscale-procedure]] _(moet-verwijzen)_
- ↪ Algemene fiscale beginselen → [[fiscale-beginselen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscaal-recht]]
### `bevat`
- [[taxatieprocedure]]
- [[aanslag-cyclus]]
- [[fiscale-controle]]
- [[fiscale-bewijsmiddelen]]
- [[bezwaarprocedure]]
- [[fiscale-bemiddelingsprocedure]]
- [[gerechtelijke-fase-belasting]]
- [[invorderingsprocedure]]
- [[fiscale-sancties]]
### `vergelijkbaar_met`
- [[gewestelijke-fiscale-procedure]]
