---
title: "Ontbinding en vereffening"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.IX
  - 3.0.IX.B
  - 3.0.X
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/ontbinding-en-vereffening.json"
---

# Ontbinding en vereffening

_Procedure_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.IX` · `3.0.IX.B` · `3.0.X` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: liquidatie van een vennootschap · dissolution et liquidation

## Definitie

📖 Ontbinding is de juridische beslissing om een vennootschap te beëindigen; vereffening is de daaropvolgende feitelijke afwikkeling waarbij de activa worden verkocht, de schulden voldaan en het saldo onder de aandeelhouders verdeeld. Ontbinding zonder vereffening bestaat niet — beide vormen één procedure in twee fases. Het Wetboek van vennootschappen en verenigingen (WVV, boek 2 titel 8 — art. 2:70 tot 2:119) regelt de vrijwillige variant. De gerechtelijke vereffening (door rechter bevolen wegens grove tekortkomingen of langdurige inactiviteit) valt onder boek XX van het Wetboek van Economisch Recht (WER). Een faillissement leidt eveneens tot ontbinding van de rechtspersoon bij sluiting.

<small>📚 WVV — art. 2:70 e.v. — _wettekst_ · WVV — art. 2:71 (ontbindingsgronden) — _wettekst_ · WVV — art. 2:79 (afsluiting + doorhaling) — _wettekst_</small>

## Substantie

🔗 Voor de stagiair is het kernonderscheid: gaat het om een **gezonde** vennootschap (activa > schulden — vereffening levert een uitkering aan aandeelhouders op) of een **deficitaire** vennootschap (schulden > activa — vereffening eindigt zonder uitkering en kan kantelen in faillissement)? Bij de gezonde variant is er ruimte voor de 'turbo-vereffening' (onmiddellijke sluiting in één AV-akte, art. 2:80) als er geen openstaande schulden meer zijn. Bij de deficitaire variant moet de vereffenaar de schuldeisers raadplegen en, bij staking van betaling + geschokte krediet, het faillissement aanvragen — anders riskeert hij persoonlijke aansprakelijkheid.

<small>📚 WVV — art. 2:80 (onmiddellijke sluiting) — _wettekst_ · CBN-advies 2022/06 — Verslaggeving bij onmiddellijke sluiting van de vereffening van een vennootschap — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 Het systeem van ontbinding + vereffening bestaat om bij beëindiging van een rechtspersoon de rechten van schuldeisers veilig te stellen — zij moeten eerst worden voldaan, vóór aandeelhouders enig saldo ontvangen. Tegelijk biedt het een gestructureerde manier om gezonde vennootschappen 'opgeruimd' af te sluiten (bv. na overname van de activiteit door een nieuwe entiteit, of na pensionering van de zaakvoerder). De rol van de gecertificeerd accountant is wettelijk verankerd: bij elke vrijwillige ontbinding moet hij/zij een 'staat van activa en passiva' opmaken en de continuïteitsevaluatie uitvoeren (WVV art. 2:71 § 2 + ITAA-norm).

<small>📚 WVV — art. 2:71 § 2 — _wettekst_ · ITAA-norm ontbinding-vereffening — § II.2 — Staat van A/P in continuïteit — _norm_</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2020-01-01** · basis: WVV boek 2 titel 8 (W 23-03-2019); aansluitende CBN-adviezen 2022/05, 2022/06, 2022/07, 2024/09

**✅ Voor**
- 📖 Vrijwillige ontbinding: vennootschap heeft haar doel bereikt of opgegeven; aandeelhouders willen actief de stekker eruit trekken. Gerechtelijke vereffening: rechter beveelt einde wegens wettige redenen (langdurige inactiviteit, grove tekortkomingen, niet-neerleggen jaarrekeningen 3 opeenvolgende jaren).

**▶️ Trigger start**
- 📖 Vrijwillig: bijzondere algemene vergadering (statutenwijzigingsmeerderheid) beslist tot ontbinding op verslag van bestuursorgaan + accountant. Gerechtelijk: dagvaarding door belanghebbende of openbaar ministerie → rechterlijk vonnis dat de vennootschap ontbindt + vereffenaar aanstelt.

**⏹ Trigger einde**
- 📖 Vereffening eindigt door een AV-besluit dat de eindrekening goedkeurt, waarna de vereffenaar de afsluiting laat publiceren en de rechtspersoon wordt doorgehaald in de Kruispuntbank van Ondernemingen (art. 2:79).

## Sub-concepten

### 📦 Vrijwillige ontbinding (WVV)  
_`procedure` (subconcept)_

#### Definitie

📖 Beslissing van de algemene vergadering om de vennootschap te ontbinden, genomen met de meerderheid vereist voor statutenwijziging (NV: 75%; BV: 75%). Voorafgaand zijn drie documenten nodig (art. 2:71 § 2): (1) een verslag van het bestuursorgaan met motivering; (2) een staat van activa en passiva niet ouder dan 3 maanden; (3) een controleverslag van een commissaris, bedrijfsrevisor of externe accountant op die staat. Zonder die drie documenten is het AV-besluit nietig.

<small>📚 WVV — art. 2:71 § 2 — _wettekst_ · WVV — art. 5:147 (BV) / art. 7:181 (NV) — quorum-meerderheid — _wettekst_</small>

#### Rationale

🔗 De wet wil voorkomen dat aandeelhouders een vennootschap laten verdwijnen zonder de schuldeisers in te lichten. De staat van A/P + controleverslag is hét waarborg-instrument: het toont objectief of er voldoende activa zijn om alle schulden te dekken, of niet.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Gerechtelijke vereffening  
_`procedure` (subconcept)_

#### Definitie

📖 De ondernemingsrechtbank kan op vordering van een belanghebbende of het openbaar ministerie de ontbinding bevelen wanneer de vennootschap (art. 2:74-75 WVV): drie opeenvolgende boekjaren geen jaarrekening heeft neergelegd; gedurende lange tijd inactief blijft zonder publieke opmerkingen; of zware tekortkomingen in haar werking vertoont. De rechter stelt zelf een vereffenaar aan, vaak een advocaat. Deze procedure valt formeel onder WVV maar leeft in symbiose met boek XX WER wanneer er ook insolventie speelt.

<small>📚 WVV — art. 2:74-75 — _wettekst_</small>

### 📦 Vereffenaar — aanstelling en mandaat  
_`actor` (subconcept)_

#### Definitie

📖 De vereffenaar wordt aangesteld door (a) de statuten, (b) de algemene vergadering bij ontbindingsbesluit, of (c) de rechtbank (bij gerechtelijke vereffening of indien AV in gebreke blijft, art. 2:75). Diens benoeming moet — opmerkelijk! — worden bevestigd of homologeerd door de ondernemingsrechtbank (art. 2:75) vóór de vereffening rechtsgeldig verder kan, tenzij de venn vereenvoudigde voorwaarden vervult. Het mandaat omvat: realiseren van activa, betalen van schulden, vertegenwoordigen vennootschap in rechte, uitkeren saldo aan aandeelhouders.

<small>📚 WVV — art. 2:75 (aanstelling + homologatie) — _wettekst_ · WVV — art. 2:91 (bevoegdheden vereffenaar) — _wettekst_</small>

#### Substantie

🔗 Belangrijk voor de stagiair: niet iedereen kan vereffenaar zijn. Verboden o.a. wie strafrechtelijk veroordeeld is voor faillissementsmisdrijven of wie een beroepsverbod heeft. Bij homologatieverzoek moet de vereffenaar uittreksels strafregister voorleggen + verklaring CKO ('geen verbod').

<small>📚 WVV — art. 2:75 § 2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Procedure-stappen in chronologie  
_`procedure` (subconcept)_

#### Definitie

📖 **Stap 1 — Voorbereiding**: bestuursorgaan stelt staat van A/P + verslag op; accountant maakt controleverslag. **Stap 2 — Ontbindings-AV**: notariële akte → ontbinding + vereffenaar aanduiding → bekendmaking BS. **Stap 3 — Homologatie**: vereffenaar laat zijn benoeming homologeren door ondernemingsrechtbank (art. 2:75). **Stap 4 — Vereffening**: realisatie activa, betaling schulden, jaarlijkse staat van vereffening (art. 2:99). **Stap 5 — Verdelingsplan**: bij meer dan één schuldeiser of complexe situatie — verdelingsplan ter goedkeuring rechter (art. 2:97 § 2). **Stap 6 — Eindrekening**: opmaak + AV-goedkeuring. **Stap 7 — Sluitings-AV + doorhaling**: bekendmaking sluiting, vennootschap stopt te bestaan, doorhaling KBO.

<small>📚 WVV — art. 2:75 t/m art. 2:79 — _wettekst_ · WVV — art. 2:91-99 (vereffening) — _wettekst_</small>

### 📦 Onmiddellijke sluiting ('turbo-vereffening')  
_`regime` (subconcept)_

#### Definitie

📖 Wanneer de vennootschap (a) geen schuldeisers meer heeft of (b) alle bekende schuldeisers schriftelijk hun akkoord geven, kan de AV in één enkele akte ontbinden + vereffenen + sluiten (art. 2:80). Geen vereffenaar nodig, geen aparte sluitings-AV. De staat van A/P + accountantsverslag + bestuursverslag blijven verplicht. Dit is verreweg de gebruikelijkste vorm voor kleine vennootschappen zonder schulden.

<small>📚 WVV — art. 2:80 — _wettekst_ · CBN-advies 2022/06 — Toepassingsvoorwaarden + Voorbeeld — _cbn_</small>

#### Rationale

🔗 De turbo-route bespaart kosten en tijd. Voor een familie-BV die haar activiteit jaren geleden heeft gestopt, met enkel een banksaldo en geen schulden meer, is dit één notariële akte van een paar duizend EUR — versus een volledige vereffening die maanden duurt en meer kost.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Boekenstaat (staat van activa en passiva) bij ontbinding  
_`instrument` (subconcept)_

#### Definitie

📖 Dit is de wettelijk verplichte staat van activa en passiva niet ouder dan 3 maanden die het bestuursorgaan moet opmaken vóór de ontbindings-AV (WVV art. 2:71 § 2). Hij wordt opgesteld in 'continuïteit' — d.w.z. volgens de gebruikelijke jaarrekening-regels (CBN), niet in liquidatie-waarde. De accountant geeft op deze staat een **controleverslag** uit. Centrale vraag: zijn alle activa correct gewaardeerd? zijn alle schulden volledig opgenomen? is de informatie up-to-date en compleet? De ITAA-norm 'opdrachten met betrekking tot ontbinding en vereffening' geeft de praktische werkpapieren mee.

<small>📚 WVV — art. 2:71 § 2, 2°-3° — _wettekst_ · ITAA-norm ontbinding-vereffening — § II.2 — Staat A/P in continuïteit — _norm_</small>

#### Substantie

🔗 Voor de accountant: deze opdracht is een 'bijzonder mandaat' uit het Wetboek (vergelijkbaar met inbreng in natura). Hij staat 'in continuïteit' — dus geen herwaardering, geen liquidatiekosten in de staat verwerken. Wel: een continuïteitsverslag in het algemeen, dat aangeeft of er een continuïteitsprobleem bestaat. Bij ontbinding na faillissementsdreiging is dat continuïteitsoordeel manifest negatief en de staat moet dat reflecteren.

<small>📚 ITAA-norm ontbinding-vereffening — § II.2 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Heropening van de vereffening (vergeten actief of passief)  
_`procedure` (subconcept)_

#### Definitie

📖 Zelfs na sluiting kan blijken dat een actief (bv. teruggevonden vordering) of een passief (bv. opgelegde fiscale rectificatie) onbekend was. De vereffening kan dan **heropend** worden op verzoek van een belanghebbende. De heropende vereffening krijgt zelfs een aparte boekhouding en eigen jaarrekening (CBN-advies 2024/09). Dit kan tot 5 jaar na de sluitings-publicatie.

<small>📚 CBN-advies 2024/09 — Verslaggeving bij heropening van de vereffening — _cbn_ · WVV — art. 2:79 § 4 (vergeten activa/passiva) — _wettekst_</small>

### 📦 Vereffenaarsaansprakelijkheid  
_`regime` (subconcept)_

#### Definitie

📖 De vereffenaar is persoonlijk aansprakelijk voor fouten in de uitoefening van zijn mandaat (art. 2:96 WVV). Drie veel-voorkomende fouten: (a) **selectieve betaling** — eerst aandeelhouders uitbetalen terwijl er schuldeisers openstaan; (b) **niet-naleving verdelingsplan** — bij meerdere niet-bevoorrechte schuldeisers de gelijkheid schenden; (c) **niet-aangifte faillissement** — bij vaststelling staking betaling + geschokte krediet moet hij faillissement aanvragen, niet de vereffening doorzetten. Bij gerechtelijke vereffening die deficitair blijkt, geldt boek XX WER en kan aansprakelijkheid voor netto-passief volgen (art. XX.225-226).

<small>📚 WVV — art. 2:96 — _wettekst_ · WER — art. XX.225-226 — _wettekst_</small>

## Bouwstenen

### 📜 Drie verplichte documenten bij vrijwillige ontbinding  
_`regel`_

📖 Vóór de ontbindings-AV moeten klaarliggen: (1) bestuursverslag met verantwoording; (2) staat van A/P niet ouder dan 3 maanden; (3) controleverslag van commissaris, bedrijfsrevisor of (externe) accountant. Het bestuursverslag MOET ingaan op de gevolgen voor schuldeisers; het controleverslag MOET een verklaring bevatten of de staat een getrouw beeld geeft. Ontbreken van één van de drie → nietigheid AV-besluit.

<small>📚 WVV — art. 2:71 § 2 — _wettekst_</small>

### ✴️ Saldo voor aandeelhouders pas na schuldeisers  
_`principe`_

🔗 Aandeelhouders hebben slechts recht op het saldo na betaling (of provisionering voor toekomstige betaling) van alle schuldeisers. Vereffenaar die deze volgorde schendt is persoonlijk aansprakelijk. Bij twijfel over een schuld: provisioneren, niet uitkeren.

<small>📚 WVV — art. 2:97-98 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Turbo-vereffening van een 'slapende' BV — Aurelia Beheer BV 🔗

_Aurelia Beheer BV (familie-vennootschap, 1 aandeelhouder = mevrouw Aurelia) is sinds 2 jaar inactief, heeft enkel een banksaldo van 45.000 EUR en geen schulden behalve een gehonoreerde lening._

**Weergave** `stappenlijst`:

```json
{
  "tekst": "Week 1: Accountant maakt tussentijdse balans + staat A/P. Geen schulden meer (lening afgelost).\nWeek 2: Bestuur stelt verslag op + accountant controleverslag.\nWeek 3: Notariële akte — ontbinding + onmiddellijke sluiting in één AV (art. 2:80).\nWeek 4: Bekendmaking Belgisch Staatsblad + doorhaling KBO.\nWeek 4: Banksaldo 45.000 EUR uitgekeerd aan mevr. Aurelia (verminderd met liquidatiebonus 30% in PB sinds 2018 ofwel onder voorwaarden VVPRbis-tarief)."
}
```

<small>📚 CBN-advies 2022/06 — Voorbeeld — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Ontbinding ≠ stop zonder formaliteiten

**Verkeerde assumptie**: Een inactieve vennootschap stopt automatisch te bestaan als ze haar jaarrekening niet meer neerlegt.

**Kernpunt**: Een vennootschap blijft bestaan tot ze formeel ontbonden + vereffend + doorgehaald is. Niet-neerleggen leidt na 3 jaar tot mogelijke gerechtelijke ontbinding (art. 2:74) — maar tot dan blijven jaarrekening- en aangifteverplichtingen lopen, met bijhorende boetes.

<small>📚 WVV — art. 2:74 — _wettekst_</small>

### ⚠️ Turbo-vereffening bij dubieuze schuldeiser

**Verkeerde assumptie**: Onmiddellijke sluiting werkt zolang de aandeelhouder beweert dat er geen schulden meer zijn.

**Kernpunt**: Art. 2:80 vereist OF geen schuldeisers, OF schriftelijk akkoord van élke bekende schuldeiser. Vergeten van één schuldeiser (bv. een lopende fiscale controle, een potentiële garantieverplichting) kan de turbo-sluiting nietig maken en leiden tot vereffenaarsaansprakelijkheid voor het saldo dat al werd uitgekeerd.

<small>📚 WVV — art. 2:80 — _wettekst_</small>

### ⚠️ Staat in continuïteit = ook in liquidatie

**Verkeerde assumptie**: Bij ontbinding moet de staat van A/P meteen in liquidatiewaarde worden opgesteld.

**Kernpunt**: De WVV en de ITAA-norm zijn duidelijk: de staat is opgesteld 'in continuïteit' (dezelfde waarderingsregels als de laatste jaarrekening). De **eerste vereffenings-jaarrekening** is wel in liquidatie. De staat is een momentopname vóór de ontbinding, niet erna.

<small>📚 ITAA-norm ontbinding-vereffening — § II.2 — _norm_</small>

## Accountant-perspectieven

### Accountant levert staat A/P + controleverslag bij ontbinding

#### 🔍 Auditor

##### 👣 Controleverslag op staat van activa en passiva  
_`stap`_

📖 Werk volgens ITAA-norm 'ontbinding-vereffening': (1) plan de opdracht, identificeer de risico's (volledigheid passiva, juistheid activa); (2) verzamel bewijs door inspectie van boekhouding + bevestigingen schuldeisers; (3) toets continuïteit — kan de vennootschap, mocht ze niet ontbinden, twaalf maanden voortgaan? (4) formuleer een verklaring: zonder voorbehoud, met voorbehoud, of weigering. Verslag binnen 3 maanden na staat-datum.

<small>📚 ITAA-norm ontbinding-vereffening — § II.2 + § 2 Verantwoordelijkheden — _norm_</small>

#### 📒 Boekhouder

##### 👣 Eerste vereffenings-jaarrekening — overgang naar liquidatie-grondslag  
_`stap`_

📖 Bij het opmaken van de eerste jaarrekening **na** de ontbinding: stap af van continuïteits-grondslag. Concreet: hervorm immateriële vaste activa en goodwill naar nul, voorraden naar netto-realiseerbare waarde, materiële vaste activa naar marktwaarde of liquidatiewaarde, en voorzien voor liquidatiekosten (vereffenaars-erelonen, notariskosten, eventuele ontslagvergoedingen). CBN-advies 2022/06 geeft concrete schema's.

<small>📚 CBN-advies 2022/06 — Jaarrekeningrechtelijke gevolgen — _cbn_</small>

## Verder lezen (scope-out)

- → Parent kader — WER boek XX (voor gerechtelijke vereffening) → [[insolventierecht-wer-boek-xx]] _(moet-verwijzen)_
- → Faillissement als alternatieve route bij insolventie → [[faillissement]] _(moet-verwijzen)_
- → AV-besluit als trigger-mechanisme → [[algemene-vergadering]] _(moet-verwijzen)_
- → Bijzondere mandaten — boekenstaat bij ontbinding als type → [[bijzondere-mandaten]] _(moet-verwijzen)_
- ↪ Rehabilitatie + beroepsverbod (cross natuurlijk persoon) → [[rehabilitatie-en-beroepsverbod]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsrecht]]
### `vergelijkbaar_met`
- [[faillissement]]
    - **Gelijkenissen**:
        - Beide leiden tot einde van de rechtspersoon
        - Beide vereisen schuldeisers eerst te voldoen
    - **Verschillen**:
        - Vereffening typisch bij solvabele venn — faillissement bij insolvabele
        - Vereffening = aandeelhouders kiezen einde; faillissement = ondernemingsrechter dwingt
        - Vereffenaar handelt onder controle aandeelhouders; curator onder rechter-commissaris
### `vereist`
- [[algemene-vergadering]]
### `triggert`
- [[bijzondere-mandaten]]
