---
title: "Omrekening buitenlandse dochter"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.4.I.D
  - 1.4.II.C
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/omrekening-buitenlandse-dochter.json"
---

_Verrichting_ · ook: foreign currency translation · valuta-omrekening · currency translation

## Definitie

Omrekening van een buitenlandse dochter is het proces waarbij de jaarrekening van een dochter die wordt gevoerd in een andere munt dan de presentatie-munt van de groep, wordt omgerekend naar die presentatie-munt vóór ze in de consolidatie wordt opgenomen. IAS 21 schrijft daarbij twee methodes voor, afhankelijk van de functionele munt: (1) de current-rate-methode (alle activa en passiva tegen slotkoers, opbrengsten en kosten tegen gemiddelde koers van de periode); (2) de temporal-methode (monetaire posten tegen slotkoers; niet-monetaire posten gewaardeerd tegen historische kostprijs blijven tegen historische koers). Het omrekeningsverschil wordt afhankelijk van de methode in eigen vermogen (CTA) of in de resultatenrekening geboekt.

<small>📖 Verordening (EU) 2023/1803 — IAS 21 — _wettekst_ · CBN-advies — 152/1 — _cbn_ · CBN-advies — 172/1 — _cbn_</small>

## Substantie

Twee koersen worden onderscheiden: de slotkoers (closing rate, koers op balansdatum) en de historische koers (koers op transactiedatum). Het kernidee: een buitenlandse dochter die economisch onafhankelijk opereert (eigen valuta is haar 'functionele munt') wordt vertaald via current-rate-methode — alsof de hele balans als één pakket wordt geconverteerd op balansdatum. Een dochter die feitelijk een verlengstuk van de moeder is (operaties zo geïntegreerd dat de moedermunt de facto haar werkmunt is) wordt vertaald via temporal-methode — niet-monetaire activa (vaste activa, voorraden) blijven tegen de historische koers omdat ze 'eigenlijk' al in moedermunt waren aangekocht. Het verschil tussen oude en nieuwe slotkoers genereert omrekeningsverschillen: bij current-rate-methode komen die in een aparte EV-rubriek (Cumulative Translation Adjustment — CTA), niet in resultaat. Bij temporal-methode komen ze direct in de RR.

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 39-46 — _wettekst_ · CBN-advies — 152/1 — _cbn_</small>

## Rationale

Ratio: koerswijzigingen kunnen het geconsolideerde resultaat sterk vertekenen als ze rechtstreeks in de RR vallen. Voor zelfstandige dochters is het netto-investering-concept toepasselijk: de moeder houdt een EV-belang in een buitenlandse entiteit; de koerswijziging is een 'translation effect' op die investering, geen operationeel resultaat. Daarom wordt CTA in EV geparkeerd — pas bij verkoop of vereffening van de dochter wordt het cumulatief saldo via recycling naar resultaat overgeboekt (IAS 21 alinea 48-49). Voor temporal-methode geldt het inverse: niet-monetaire activa zijn 'als waren ze al in moedermunt aangekocht' → koersverschillen op monetaire posten zijn echte 'transactional' winsten/verliezen → direct in RR.

<small>🔗 Verordening (EU) 2023/1803 — IAS 21 alinea 32, 48-49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: IAS 21 (Verordening (EU) 2023/1803) — IFRS-context. Onder BE-GAAP: CBN-adviezen 152/1, 172/1 + nieuwere adviezen 2022/15 en 2024/02 voor bijkantoren.

**✅ Voor**
- 📖 Toepasselijk telkens wanneer een geconsolideerde groep een dochter of buitenlands bijkantoor heeft met een functionele munt die verschilt van de presentatie-munt van de geconsolideerde jaarrekening. Typisch: Belgische groep met dochters in USD, GBP, CHF, of buiten de eurozone.

**📋 Voorwaarden**
- 📖 Eerste stap: bepaling van de functionele munt van de dochter (IAS 21 alinea 9-12). Criteria: in welke munt worden verkoopprijzen, materiaal/arbeid betaald, financiering aangetrokken, kasstromen aangehouden? Vaak is dat de lokale munt; soms (bv. integrale buitenlandse bijkantoor met intercompany-financiering) is dat de munt van de moeder.

## Sub-concepten

### 📦 Current-rate-methode (slotkoers-methode)

#### Definitie

Alle activa en passiva van de buitenlandse dochter worden omgerekend tegen de slotkoers op balansdatum. Opbrengsten en kosten worden omgerekend tegen de wisselkoers op de transactiedatum — in de praktijk vaak benaderd door de gemiddelde koers van de periode. EV-posten blijven tegen historische koers (koers op transactiedatum — typisch koers bij verkrijging dochter of bij latere kapitaalverhoging). Het ontstane verschil komt in een EV-rubriek 'Omrekeningsverschillen' (CTA).

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 39 — _wettekst_</small>

#### 📜 Wanneer current-rate?

Toepasselijk wanneer de functionele munt van de buitenlandse activiteit verschilt van de presentatie-munt van de moeder/groep. Dat is de standaard voor economisch zelfstandige dochters in het buitenland (eigen klantenkring, eigen financiering, eigen prijsbeleid).

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 38-39 — _wettekst_</small>

### 📦 Temporal-methode (historische-koers-methode)

#### Definitie

Monetaire posten (kas, vorderingen, schulden) worden omgerekend tegen de slotkoers. Niet-monetaire posten gewaardeerd tegen historische kostprijs (vaste activa, voorraden in kostprijs) blijven tegen de historische koers van de aanschaffingsdatum. Niet-monetaire posten op reële-waarde-basis worden omgerekend tegen de koers op de waarderingsdatum. Opbrengsten en kosten tegen transactiekoers (gemiddeld). Omrekeningsverschillen lopen door de resultatenrekening, niet via EV.

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 21-26 — _wettekst_</small>

#### 📜 Wanneer temporal?

Toepasselijk wanneer de functionele munt van de buitenlandse activiteit dezelfde is als die van de moeder — bv. een bijkantoor dat exclusief in de presentatiemunt verkoopt, materialen aankoopt en gefinancierd wordt. De buitenlandse boekhouding wordt dan vertaald 'alsof' de transacties altijd al in moedermunt waren.

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 9-12, 21 — _wettekst_ · CBN-advies — 172/1 — _cbn_</small>

## Bouwstenen

### 💡 Cumulative Translation Adjustment (CTA)

CTA = cumulatieve som van omrekeningsverschillen die ontstaan bij de current-rate-methode, samengebracht in een aparte EV-rubriek (typisch 'Cumulatieve omrekeningsreserve' of 'Foreign currency translation reserve'). Wordt jaarlijks bewogen met de translation gain/loss van het lopende jaar. Komt niet door de RR — wel via Other Comprehensive Income (OCI) onder IFRS. Bij geheel of gedeeltelijke verkoop, vereffening of verlies-van-controle van de buitenlandse dochter wordt het cumulatief saldo gerecycleerd naar de RR (IAS 21 alinea 48).

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 32, 48 — _wettekst_</small>

### ⚙️ Recyclage CTA bij verkoop dochter

Bij volledige verkoop of vereffening van een buitenlandse dochter wordt het volledige cumulatieve saldo van de CTA toegerekend aan die dochter overgeboekt naar de winst-en-verliesrekening, als deel van de gerealiseerde meerwaarde of minderwaarde. Bij gedeeltelijke verkoop zonder verlies van controle: geen recyclage (alleen herallocatie binnen NCI in EV). Bij gedeeltelijke verkoop mét verlies van controle: volledige recyclage van CTA, en het overblijvend belang wordt geherwaardeerd tegen reële waarde (IFRS 10 + IAS 21 alinea 48A-B).

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 48-48B — _wettekst_</small>

## Voorbeelden

> [!example]- Bijkantoor in vreemde valuta — CBN-advies 172/1
> _Een Belgische zetel heeft een bijkantoor in de UK. Eind periode x+1: balans bijkantoor in GBP wordt omgerekend naar EUR. Vaste activa: omrekening tegen historische koers; voorraden: historische koers per aanschaffing; vorderingen/schulden: slotkoers._
>
> **📊 Balans zetel na opneming bijkantoor in EUR (periode x+1) — temporal-methode**
>
> ```json
> {
>   "tekst": "Activa: Vaste activa 6.600.000 (historische koers) - Afschrijvingen (110.000) - Voorraden 550.000 (historische) - Handelsvorderingen 4.440.000 (slotkoers). Passiva: Kapitaal 7.720.000 - Overgedragen resultaat 55.000 - Financiële schulden 2.065.000 - Handelsschulden 600.000 - Overige + overlopend 1.040.000. Resultaat zetel beïnvloed door verschillende koersen op afschrijvingen + onttrekkingen voorraad."
> }
> ```
>
> <small>📖 CBN-advies — 172/1 — _cbn_</small>

## Valkuilen

> [!warning]- Niet-monetair zien als monetair (omgekeerd ook)
> **Verkeerde assumptie**: Studenten zien een 'voorraad' als geld → behandelen tegen slotkoers.
>
> **Kernpunt**: Voorraden zijn niet-monetair. Bij temporal-methode worden ze tegen de historische koers van de aankoop omgerekend. Verwarrend punt: 'monetair' betekent 'in geld of vaste contractbedragen' (kas, vorderingen, schulden, leningen). Voorraden/vaste activa/IVA = niet-monetair.
>
> <small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 8 (definitie monetaire posten) — _wettekst_</small>

> [!warning]- CTA niet recycleren bij verkoop
> **Verkeerde assumptie**: CTA blijft in EV staan ook na verkoop dochter.
>
> **Kernpunt**: Bij volledige verkoop of verlies van controle moet het cumulatief saldo CTA via een EV-naar-RR-boeking gerecycleerd worden (IAS 21 alinea 48). Vergeten → onjuiste meerwaarde/minderwaarde, controlepunt bij audit.
>
> <small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 48 — _wettekst_</small>

> [!warning]- Functionele munt = lokale munt (automatisch)
> **Verkeerde assumptie**: Dochter zit in Zwitserland → functionele munt CHF.
>
> **Kernpunt**: Niet automatisch. De functionele munt = de munt van de primaire economische omgeving (alinea 9 IAS 21). Een Zwitserse vehicle die exclusief in EUR verkoopt aan Belgische groepsklanten, in EUR financiert en in EUR rapporteert → functionele munt EUR, niet CHF. Bepaling vereist analyse — geen reflex.
>
> <small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 9-12 — _wettekst_ · CBN-advies — 2022/15 — _cbn_</small>

## Accountant-perspectieven

### Groepsmoedervennootschap met buitenlandse dochters

_De consolidatieverantwoordelijke die jaarlijks buitenlandse dochterbalansen omrekent._

#### 📒 Boekhouder

##### 👣 Bepalen functionele munt per dochter

Voor elke buitenlandse dochter: analyse van (1) munt waarin verkoopprijzen voornamelijk worden uitgedrukt en betaald, (2) munt van het land dat verkoopprijzen + kosten reguleert, (3) munt waarin operationele financiering wordt aangetrokken, (4) munt waarin verkopen-ontvangsten worden aangehouden. Documenteer de keuze — wijziging van functionele munt heeft prospectieve effecten (alinea 36 IAS 21).

<small>📖 Verordening (EU) 2023/1803 — IAS 21 alinea 9-12, 36 — _wettekst_</small>

##### 👣 Toepassen koersen per balansrubriek

Bij current-rate: alle activa + passiva tegen slotkoers; opbrengsten + kosten tegen periode-gemiddelde; EV-componenten tegen historische koers. Reconcilieer het omrekeningsverschil tot CTA. Bij temporal: monetair tegen slotkoers, niet-monetair tegen historische koers; resultatenverschil direct in RR. Bewaar koers-archief: historische koersen per aanschaffing van vaste activa zijn na 20 jaar nog relevant voor temporal-methode.

<small>🔗 Verordening (EU) 2023/1803 — IAS 21 alinea 21-26, 39 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Audit-werkzaamheden omrekening

Toets (1) functionele-munt-bepaling per dochter (geschikt vermogen + documentatie); (2) gebruikte koersen (slotkoers ECB of NBB; gemiddelde koers consistent toegepast); (3) CTA-saldo-aansluiting met vorige periode + huidige translation gain/loss; (4) bij verkoop dochter: correcte recyclage CTA naar RR. ISA 600: groepsauditor controleert consolidatie-aanpassingen (waaronder omrekening) als kritisch onderdeel van het consolidatieproces.

<small>📖 ISA 600 — Bijlage 2 — _norm_ · Verordening (EU) 2023/1803 — IAS 21 — _wettekst_</small>

## Verder lezen (scope-out)

- → Opmaak-procedure → [[opmaak-geconsolideerde-jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS Σ (IAS 21-context) → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[geconsolideerde-jaarrekening]]
### `vereist`
- [[integrale-consolidatie]] — Omrekening is enkel een issue bij integrale of evenredige consolidatie van een buitenlandse dochter.
### `vergelijkbaar_met`
- [[uniforme-waarderingsregels-consolidatie]] — Beide zijn pre-consolidatie-aanpassingen op de dochter-jaarrekening vóór integrale opname.
