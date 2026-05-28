---
title: "Levensverzekering als successieplanningsinstrument"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.6.VI.D
  - 2.6.VI.E
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/levensverzekering-successieplanning.json"
---

# Levensverzekering als successieplanningsinstrument

_Instrument_

📋 Regeling · Anchors: `2.6.VI.D` · `2.6.VI.E` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: levensverzekering-planning · AB-BC-verzekering — **Vertalingen**: fr: assurance-vie planification successorale

## Definitie

📖 Een levensverzekering met successieplanning-oogmerk is een verzekeringscontract waarbij een persoon (verzekeringnemer) een premie betaalt aan een verzekeraar, en bij overlijden van een verzekerde een uitkering ontvangt door een vooraf aangewezen begunstigde. Drie partijen in het contract — de A-B-C-trio (verzekeringnemer A · verzekerde B · begunstigde C) — kunnen wel of niet samenvallen. De fiscale behandeling bij erfbelasting hangt af van die configuratie (art. 8 W.Succ. / VCF art. 2.7.1.0.6). Het instrument wordt gebruikt om: (a) een gegarandeerd kapitaal aan een specifieke begunstigde te bezorgen los van het erfrecht; (b) liquiditeit te creëren bij overlijden om de erfbelasting te betalen; (c) niet-erfgenamen (vriend, partner zonder huwelijk) een vermogensvoordeel toe te kennen.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.1.0.6 — _wettekst_</small>

## Substantie

🔗 Praktisch werkt het instrument zoals volgt: een ouder (verzekeringnemer + verzekerde A=B) sluit een verzekering die bij zijn overlijden 200.000 EUR uitkeert aan zijn kind C. Civielrechtelijk is dit geen erfenis (de uitkering komt rechtstreeks van de verzekeraar, niet uit de nalatenschap) — wat het kind buiten de erfreserve-discussie tussen alle kinderen kan houden indien gewenst. Fiscaal echter: art. 8 W.Succ. herwaardeert de uitkering ALS legaat voor de erfbelasting — het kind betaalt erfbelasting volgens de tarieftabel rechte lijn. De configuratie A≠B is interessant voor planning: ouder verzekeringnemer + kind verzekerde + ander kind begunstigde leidt bij overlijden van het verzekerde kind tot een afkoop-clause zonder erfbelasting (art. 8 grijpt enkel op overlijden van de verzekeringnemer). Branche 21 (gegarandeerd rendement) vs branche 23 (beleggingsverzekering) vs branche 26 (kapitalisatieovereenkomst zonder verzekerd risico) hebben verschillende fiscale + civielrechtelijke gevolgen.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Art. 8 W.Succ. (federaal) + VCF art. 2.7.1.0.6 (Vlaanderen); Wet 4 april 2014 verzekeringen

Stabiel regime. Vlaanderen heeft sinds decreet 2017 de fictie verfijnd om bepaalde planning-configuraties (huwelijksgemeenschap-verzekeringen) anders te behandelen. Een gunstige Vlaamse hervorming sinds 2022 maakt bepaalde overdracht-tussen-echtgenoten-verzekeringen flexibeler.

**✅ Voor**
- 🔗 Cliënten met (a) een complexe gezinssituatie (kinderen uit verschillende huwelijken, niet-gehuwde partner, vriend), (b) liquiditeitsbehoefte bij overlijden (bedrijfsleider met grote illiquide aandelen), of (c) wens om reserveregels van het erfrecht te omzeilen voor een specifieke vermogensbeschikking.

**⚠️ Risico**
- 🔗 (a) Reserve-bescherming: civielrechtelijk kunnen reservataire erfgenamen onder bepaalde voorwaarden inkorting eisen indien de premies disproportioneel waren ten opzichte van het patrimonium. (b) Fiscale herwaardering: art. 8 W.Succ. is een fictiebepaling — de verzekeraar deelt automatisch aan de fiscus. (c) Bij branche 23: kapitaal niet gegarandeerd, prestatie kan lager uitvallen dan ingelegd. (d) Anti-misbruik: een 'sterfbed-verzekering' (premie kort vóór overlijden, hoge uitkering) kan door VLABEL als simulatie worden geherkwalificeerd.

## Bouwstenen

### 📜 Fictiebepaling art. 8 W.Succ.  
_`regel`_

📖 Een som die naar aanleiding van het overlijden van een verzekerde wordt uitgekeerd aan een derde-begunstigde op grond van een levensverzekeringscontract waarin de overledene als verzekeringnemer fungeerde, wordt geacht als legaat door de overledene aan de begunstigde te zijn verkregen. Gevolg: de uitkering valt onder de erfbelasting, met tarief volgens de verwantschap tussen verzekeringnemer (de overledene) en begunstigde. Vlaamse equivalent: VCF art. 2.7.1.0.6 met enkele verfijningen voor huwelijksgemeenschap-verzekeringen.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.1.0.6 — _wettekst_</small>

### ⚙️ A-B-C-configuraties + fiscale gevolgen  
_`mechanisme`_

🔗 Drie rollen (A = verzekeringnemer, B = verzekerde, C = begunstigde) leiden tot verschillende uitkomsten: (i) A=B≠C — typisch (ouder verzekert eigen leven voor kind): bij overlijden uitkering aan C, fictie art. 8 grijpt, erfbelasting verschuldigd door C. (ii) A≠B=C — bij overlijden van B krijgt C zichzelf (= B) niets, geen erfbelasting. (iii) A=C≠B — bij overlijden van B krijgt A zichzelf de uitkering, geen erfbelasting (A betaalde de premie, A krijgt terug). (iv) A≠B≠C — ouder A verzekert echtgenoot B voor kind C: bij overlijden B betaalt A premies door en bij overlijden A wordt C de nieuwe verzekeringnemer; vraagstuk wordt complex bij dubbel overlijden.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Branche 21 vs 23 vs 26  
_`mechanisme`_

🔗 Branche 21 — verzekering met gegarandeerd rendement; kapitaalbescherming + interest. Branche 23 — beleggingsverzekering gekoppeld aan fondsen (geen kapitaalgarantie, hoger rendementspotentieel). Branche 26 — kapitalisatieovereenkomst zonder verzekerd risico (puur belegging). Fiscaal voor successie: alle drie vallen onder art. 8 W.Succ. zodra er overlijden + uitkering aan begunstigde plaatsvindt. Verschillen vooral in PB (roerende voorheffing 30% op vermogenswinst bij afkoop branche 23; vrijstelling bij branche 21 na 8 jaar onder voorwaarden; branche 26 = roerend inkomen bij afkoop).

<small>📚 WIB92 — art. 21 §1 9° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ AB-BC-techniek voor partnerverzekering  
_`mechanisme`_

🔗 Klassieke planning voor echtgenoten: 'AB-BC'-configuratie. Beide echtgenoten zijn elk verzekeringnemer + verzekerde + begunstigde van elkaar — twee kruisende contracten: contract 1 (A=verzn, A=verz, B=beg) + contract 2 (B=verzn, B=verz, A=beg). Bij overlijden van A: B krijgt uitkering; art. 8 grijpt → erfbelasting tussen partners (3% Vl). Bij overlijden van B vóór A: A krijgt uitkering uit contract 2 (eigen verzekering); art. 8 grijpt evenzeer → erfbelasting. Wat de techniek wel oplost: liquiditeit + zekerheid van uitkering los van het erfrecht. Wat niet: de erfbelasting wordt niet vermeden tenzij echt het kapitaal aan partner gelegateerd wordt en gezinswoning-vrijstelling wordt geclaimd.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Levensverzekering = 'belastingvrij' voor begunstigde

**Verkeerde assumptie**: Studenten denken vaak dat een levensverzekering een belastingvrije manier is om vermogen aan iemand te bezorgen — buiten de erfbelasting om.

**Kernpunt**: Art. 8 W.Succ. behandelt de uitkering ALS legaat — erfbelasting volgens de tarieftabel tussen verzekeringnemer en begunstigde. Voor een vriend (geen verwantschap) komt dat in Vlaanderen neer op 25-55%. Het instrument is dus geen belastingvermijding maar een planningstool voor LIQUIDITEIT + GERICHTHEID van overdracht.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_</small>

### ⚠️ Configuratie A=C≠B verwarren met de standaard

**Verkeerde assumptie**: Alle levensverzekering-uitkeringen vallen automatisch onder art. 8.

**Kernpunt**: Wanneer de verzekeringnemer A tegelijk de begunstigde is (A=C) en iemand anders is verzekerde (B), valt de uitkering bij overlijden B aan A NIET onder art. 8 — A krijgt zijn eigen kapitaal terug. Dit is een vaak gebruikte techniek bij kruislingse partnerverzekeringen om sommige uitkomsten te optimaliseren.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Levensverzekering in planningsdossier

_De accountant die samen met verzekeringsmakelaar + notaris een successieplanning uitwerkt._

#### 🧭 Adviseur

##### 👣 ABC-configuratie doorrekenen  
_`stap`_

🔗 Voor elk planningsdossier: maak een ABC-matrix met alle bestaande verzekeringen en bereken voor elk scenario (overlijden A, overlijden B) de erfbelasting voor de begunstigde. Vergelijk met alternatieven (handgift, schenking met voorbehoud, FBO-gunstregime). Vermijd verzekeringen die fiscaal nadeliger zijn dan een gewone erfenis.

<small>📚 Wetboek der Successierechten — art. 8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Fictiebepaling erfbelasting → [[erfbelasting]] _(moet-verwijzen)_
- → Successieplanning kader → [[successieplanning]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[successieplanning]]
### `triggert`
- [[erfbelasting]] — Fictiebepaling art. 8 W.Succ. — uitkering aan derde-begunstigde wordt belast als legaat.
