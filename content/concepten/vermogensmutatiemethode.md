---
title: "Vermogensmutatiemethode"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 1.4.I.D
  - 1.4.I.E
  - 1.4.II.C
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/vermogensmutatiemethode.json"
---

_Verrichting_ · afk: **VMM** · ook: equity method · vermogensmutatie · equivalentiemethode

## Definitie

De vermogensmutatiemethode (VMM, equity method) is een consolidatietechniek waarbij de deelneming in een andere vennootschap wordt opgenomen op één enkele balanslijn ('deelnemingen verwerkt volgens VMM'), waarvan de boekwaarde geleidelijk wordt aangepast aan de evolutie van het eigen vermogen van de geconsolideerde vennootschap. Bij eerste opname: aanschaffingsprijs (of, voor een vroegere participatie, herwaardering naar reële waarde). Daarna jaarlijks: + aandeel in winst (of - aandeel in verlies) → één regel in de groeps-RR ('aandeel in resultaat van entiteiten verwerkt volgens VMM'); - uitgekeerde dividenden → vermindering deelnemingswaarde. Toepasselijk op geassocieerde ondernemingen (notabele invloed, art. 1:20 WVV / IAS 28) en, sinds IFRS 11, op joint ventures.

<small>📖 KB WVV — art. 3:143 — _kb_ · Verordening (EU) 2023/1803 — IAS 28 alinea 10-11 — _wettekst_</small>

## Substantie

Concept: 'één-regel-consolidatie'. In tegenstelling tot integrale of evenredige consolidatie worden de activa en passiva van de deelneming NIET regel-per-regel opgenomen — alleen het netto-economisch-belang van de moeder verschijnt. Dat is consistent met het feit dat de moeder geen controle heeft over de deelneming (alleen invloed of gezamenlijke controle bij JV) — ze kan niet beschikken over de individuele activa, dus presenteert ze die niet als haar eigen. De deelnemingswaarde 'beweegt mee' met het EV van de deelneming: groeit de deelneming, dan groeit ook de deelnemingsregel. Tussen-de-regels gedrag: uitgekeerde dividenden zijn een 'realisatie' van een deel van het EV-belang → verminderen de deelnemingswaarde (niet als opbrengst in RR opnemen onder VMM — anders dubbele telling met aandeel in resultaat).

<small>📖 KB WVV — art. 3:143 — _kb_ · Verordening (EU) 2023/1803 — IAS 28 alinea 10-11 — _wettekst_ · CBN-advies — 2022/11 — _cbn_</small>

## Rationale

Ratio: bij notabele invloed (typisch 20-50 % stemrechten) of gezamenlijke controle heeft de moeder geen volledige zeggenschap over de activa en schulden van de deelneming. Het zou misleidend zijn die volledig of pro rata op te nemen alsof het haar eigen waren. Tegelijk is een 30%-deelneming meer dan een gewone belegging — de moeder beïnvloedt het beleid, deelt in de winst en draagt de risico's pro rata. De VMM is het compromis: één-regel-opname die het netto-belang weerspiegelt, zonder over-presentatie. Het is ook fiscaal verbonden: meerwaarden via VMM zijn verworpen uitgaven, dividenden ervan profiteren van de DBI-vrijstelling (art. 186 WIB92 — kapitaalvermindering vergelijkbaar mechanisme).

<small>🔗 Verordening (EU) 2023/1803 — IAS 28 alinea 11 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB WVV art. 3:143; IAS 28 (Verordening (EU) 2023/1803)

VMM is sinds IFRS 11 (2013) de verplichte methode voor joint ventures onder IFRS — vóór 2013 was evenredige consolidatie een keuze-alternatief. Voor associates is VMM altijd de methode geweest. Onder BE-GAAP: art. 3:143 KB WVV voor geassocieerde ondernemingen; gemeenschappelijke dochters worden evenredig geconsolideerd (art. 3:140).

**✅ Voor**
- 📖 (IFRS) Verplicht voor: (a) associates — entiteiten waarin de groep notabele invloed heeft (typisch 20-50 % stemrechten of bewijsbare invloed bij <20 %); (b) joint ventures (gezamenlijke controle waarbij rechten op netto-activa van een afgescheiden vehicle). (BE-GAAP) Voor associates (art. 1:20 + 3:143 KB WVV).

**🚫 Niet voor**
- 📖 Niet voor dochters (exclusieve controle → integrale consolidatie). Niet voor gewone beleggingen zonder invloed (< 20 % stemrechten en geen invloed → IFRS 9 fair-value-waardering). Onder BE-GAAP niet voor gemeenschappelijke dochters (gezamenlijke controle → evenredige consolidatie volgens art. 3:140).

**⛔ Uitsluitingen**
- 📖 Vrijstelling onder IAS 28 alinea 17-19: een entiteit hoeft VMM niet toe te passen indien zij zelf een dochter is, haar moeder een geconsolideerde jaarrekening publiceert die voldoet aan IFRS, en de andere aandeelhouders geen bezwaar hebben.

## Bouwstenen

### 🧮 Formule evolutie deelnemingswaarde

DW(t) = DW(t-1) + (%belang × resultaat deelneming jaar t) - (%belang × dividend deelneming jaar t) ± (%belang × andere EV-bewegingen jaar t) - (impairment-correcties). Bij eerste opname (t=0): DW(0) = aanschaffingsprijs. Verschil tussen aanschaffingsprijs en %belang × EV-deelneming op verkrijgingsdatum = impliciete goodwill (binnen DW, niet apart gepresenteerd onder VMM).

<small>📖 KB WVV — art. 3:143 — _kb_ · Verordening (EU) 2023/1803 — IAS 28 alinea 10-11 — _wettekst_ · CBN-advies — 2022/11 — _cbn_</small>

### 📜 Eliminatie van intercompany-winsten bij VMM

Niet-gerealiseerde winsten/verliezen uit transacties tussen de groep en de VMM-deelneming (upstream + downstream sales) worden gedeeltelijk geëlimineerd ten belope van het % belang van de groep (IAS 28 alinea 28). Bv. een groep verkoopt voorraad voor 100 winst aan een 30 %-associate; de associate heeft de voorraad nog niet doorverkocht → 30 % van 100 = 30 winst moet geëlimineerd worden tegen de deelnemingswaarde.

<small>📖 Verordening (EU) 2023/1803 — IAS 28 alinea 28 — _wettekst_ · CBN-advies — 2022/11 — _cbn_</small>

### 👣 Impairment-test op VMM-belang

Bij indicatie van bijzondere waardevermindering (IAS 36-indicatoren toepasselijk) → test of recoverable amount (max van fair value less costs of disposal en value in use) lager is dan de boekwaarde van de VMM-deelneming. Indien lager: impairment-verlies in RR + verlaging deelnemingswaarde. Onder BE-GAAP (art. 3:48 e.v. KB WVV): waardevermindering wanneer 'duurzame ontwaarding' vaststaat.

<small>📖 Verordening (EU) 2023/1803 — IAS 28 alinea 40-43, IAS 36 — _wettekst_ · KB WVV — art. 3:48 — _kb_</small>

### 👣 Herberekening bij stapsgewijze controleverwerving

Wanneer een eerder VMM-belang (associate) wordt opgevoerd tot controle (dochter) door een additionele aankoop: het VMM-belang wordt geherwaardeerd naar fair value bij controleverwerving, het verschil komt in RR (fair-value-stap-up). Daarna integrale consolidatie. CBN-advies 2022/11 behandelt de herberekening van de deelnemingswaarde bij verschillende scenario's: van VMM naar integrale, of omgekeerd bij verlies van controle.

<small>📖 CBN-advies — 2022/11 — _cbn_ · Verordening (EU) 2023/1803 — IFRS 3 alinea 41-42 — _wettekst_</small>

## Voorbeelden

> [!example]- Jaarlijkse update VMM-belang in 30 %-associate
> _Groep G heeft op 1/1/2024 30 % aandelen in associate A gekocht voor 600. EV A op die datum = 1.800 (G's aandeel = 540). Impliciete goodwill = 60 (binnen DW). In 2024 maakt A 200 winst en betaalt 80 dividend._
>
> **🧮 DW-evolutie 2024**
>
> - Stap 1 — Opening DW (1/1/2024) = aanschaffingsprijs = 600
> - Stap 2 — Aandeel G in resultaat A (2024) = 30 % × 200 = +60
> - Stap 3 — Aandeel G in dividend A (2024) = 30 % × 80 = -24
> - Stap 4 — DW eind 2024 = 600 + 60 - 24 = 636
> - Stap 5 — In groeps-RR komt 'Aandeel in resultaat van VMM-deelnemingen' = +60
> - Stap 6 — De 24 dividend cash-ontvangen wordt NIET als opbrengst in RR geboekt — alleen DW verlaagd (anders dubbele opname)
>
> → **Resultaat**: Eindbalans: deelneming 636 EUR (één regel); RR-impact: aandeel resultaat +60.
>
> <small>🔗 KB WVV — art. 3:143 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Dividend van VMM-deelneming in RR boeken
> **Verkeerde assumptie**: Het ontvangen dividend van een associate = financieel resultaat → in RR opnemen.
>
> **Kernpunt**: Bij VMM wordt dividend afgetrokken van de deelnemingswaarde, niet als opbrengst geboekt. Reden: het resultaat is al volledig opgenomen via 'aandeel in resultaat van VMM-deelnemingen' (= 30 % × 200 in het voorbeeld); het dividend is een verdeling van dat reeds opgenomen resultaat → opname in RR zou een dubbele telling zijn. In de statutaire jaarrekening van de moeder gebeurt dit anders (dividend wel in RR — kostprijsmethode).
>
> <small>📖 Verordening (EU) 2023/1803 — IAS 28 alinea 10 — _wettekst_ · KB WVV — art. 3:143 — _kb_</small>

> [!warning]- VMM en evenredige consolidatie verwarren
> **Verkeerde assumptie**: Een 30 %-belang in een associate → 30 % van activa/passiva opnemen (zoals evenredige consolidatie).
>
> **Kernpunt**: VMM is één-regel-consolidatie — alleen de deelnemingswaarde verschijnt, niet 30 % van activa + 30 % van passiva. Evenredige consolidatie (art. 3:140 KB WVV) opneemt wél pro-rata activa en passiva regel-per-regel; alleen voor gemeenschappelijke dochters (gezamenlijke controle).
>
> <small>📖 KB WVV — art. 3:140 — _kb_ · KB WVV — art. 3:143 — _kb_</small>

> [!warning]- Notabele invloed automatisch bij ≥ 20 %
> **Verkeerde assumptie**: 20 %-drempel = notabele invloed = automatische VMM.
>
> **Kernpunt**: 20 % is een weerlegbaar vermoeden (IAS 28 alinea 5). De feiten kunnen tegenbewijs leveren: bv. 25 %-belang zonder vertegenwoordiging in bestuursorgaan, geen materiële intercompany-transacties, geen interchange-relaties → geen notabele invloed. Omgekeerd kan bij <20 % notabele invloed bestaan door bestuursvertegenwoordiging of beleidsbeïnvloeding.
>
> <small>📖 Verordening (EU) 2023/1803 — IAS 28 alinea 5-6 — _wettekst_</small>

## Speelruimtes

### 🎚️ BE-GAAP — keuze tussen vermogensmutatiemethode en kostprijsmethode voor 'deelnemingen' in statutaire jaarrekening

## Accountant-perspectieven

### Groep met VMM-deelnemingen (associates + JV's)

_De accountant die jaarlijks de VMM-deelnemingen aanpast._

#### 📒 Boekhouder

##### 👣 Jaarlijkse update deelnemingswaarde

Per VMM-deelneming: (1) verkrijg jaarrekening associate/JV (afgesloten op groepsdatum of binnen 3 maanden, art. 3:121 KB WVV); (2) herwaardeer naar groepswaarderingsregels (uniformiteit, art. 3:117); (3) bereken aandeel in resultaat = %belang × netto-resultaat; (4) elimineer intercompany-winsten pro rata (alinea 28 IAS 28); (5) boek beweging: DW + aandeel resultaat - dividend - impairment; (6) bevestig DW-saldo met associate/JV op cross-check.

<small>📖 KB WVV — art. 3:117 — _kb_ · KB WVV — art. 3:121 — _kb_ · KB WVV — art. 3:143 — _kb_ · Verordening (EU) 2023/1803 — IAS 28 alinea 28 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale behandeling VMM-resultaat

Het 'aandeel in resultaat van VMM-deelnemingen' is louter een boekhoudkundige opboeking — fiscaal komt het pas in beeld bij effectieve uitkering van dividend (DBI-aftrek art. 202 e.v. WIB92) of bij realisatie via verkoop (meerwaarde art. 192 WIB92). De jaarlijkse VMM-aanpassing is dus een verworpen uitgave / verworpen opbrengst voor de aangifte VenB.

<small>📖 WIB92 — art. 186 — _wettekst_ · WIB92 — art. 192 — _wettekst_ · WIB92 — art. 202 — _wettekst_</small>

#### 🔍 Auditor

##### 👣 Audit VMM-deelneming

Toets (1) bestaan + correcte aansluiting jaarrekening associate; (2) berekening % belang + resultaat-aandeel; (3) eliminatie intercompany-winsten (vooral bij significante intra-groep-omzet); (4) impairment-indicatoren (substantieel verlies van marktwaarde, financiële moeilijkheden bij deelneming, technologische obsolescentie); (5) toelichting in geconsolideerde toelichting (IFRS 12-vereisten voor materiële associates/JV's).

<small>📖 Verordening (EU) 2023/1803 — IAS 28 alinea 40-43, IFRS 12 alinea 20-23 — _wettekst_ · ISA 600 — Bijlage 2 — _norm_</small>

## Verder lezen (scope-out)

- → Consolidatiemethoden Σ-keuze-kader → [[consolidatiemethoden]] _(moet-verwijzen)_
- ↪ Andere methoden (vergelijking) → [[consolidatiemethoden]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[consolidatiemethoden]]
### `vereist`
- ⏳ controle-vennootschap — Vereist notabele invloed (associate) of gezamenlijke controle (JV onder IFRS 11) — geen exclusieve controle, anders integrale consolidatie.
### `vergelijkbaar_met`
- [[integrale-consolidatie]]
    - **Gelijkenissen**:
        - Beide elimineren de oorspronkelijke deelnemingsregel uit de moederbalans
        - Beide weerspiegelen het belang van de moeder in de geconsolideerde entiteit
    - **Verschillen**:
        - Integraal: 100 % activa + passiva regel-per-regel, minderheidsbelang afzonderlijk
        - VMM: één regel deelneming + één regel resultaat-aandeel
        - Integraal bij controle; VMM bij invloed of gezamenlijke controle
    - ⚠️ **Verwarringsrisico**: Studenten zien VMM als 'mini-versie van integrale consolidatie' — terwijl het conceptueel anders is: VMM behandelt deelneming als één economisch belang, niet als bezit van individuele activa.
- [[evenredige-consolidatie]]
    - **Gelijkenissen**:
        - Beide gebruikt voor entiteiten zonder exclusieve controle
    - **Verschillen**:
        - Evenredig: pro-rata activa + passiva regel-per-regel (alleen gemeenschappelijke dochters BE-GAAP)
        - VMM: één regel deelneming (associates + JV's IFRS)
        - Onder IFRS 11 geen evenredige consolidatie meer voor JV's — verplicht VMM
