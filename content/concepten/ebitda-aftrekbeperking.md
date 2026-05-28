---
title: "EBITDA-aftrekbeperking"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.3.II.D
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/ebitda-aftrekbeperking.json"
---

# EBITDA-aftrekbeperking

_Regime_

📋 Regeling · Anchors: `2.3.II.D` · Wave: `skeleton-pb-venb-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: interestaftrekbeperking ATAD · 30%-EBITDA-regel · financieringskostensurplus-beperking — **Vertalingen**: fr: limitation EBITDA / surplus de coûts d'emprunt

## Definitie

📖 De EBITDA-aftrekbeperking (art. 198/1 WIB92) is een Belgische implementatie van de ATAD-richtlijn (EU 2016/1164 art. 4) sinds AJ 2020. Ze beperkt de aftrekbaarheid van het FINANCIERINGSKOSTENSURPLUS — d.w.z. het positieve verschil tussen interestkosten en interestopbrengsten — tot het GRENSBEDRAG. Het grensbedrag is het hoogste van: (a) 30% van de fiscale EBITDA van de vennootschap, OF (b) een safe-harbor van 3.000.000 EUR. Surplus boven dat grensbedrag is niet-aftrekbaar in het lopende boekjaar (toevoeging code 1262 in vak Verworpen uitgaven) maar kan ONBEPERKT worden overgedragen naar volgende boekjaren (art. 194sexies). Een groepsmechanisme (interestaftrek-overeenkomst, art. 198/1 §4) laat toe niet-benutte capaciteit binnen de groep over te dragen.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · WIB92 — art. 194sexies — _wettekst_ · ATAD-richtlijn EU 2016/1164 — art. 4 — _richtlijn_</small>

## Substantie

📖 Economisch effect: vennootschappen met zware schuldfinanciering (vooral private equity, vastgoedstructuren, holdings) verliezen een deel van hun renteaftrek. Een vennootschap met 8 mio EUR netto-interestkosten en 20 mio EUR fiscale EBITDA: grensbedrag = 30% × 20 mio = 6 mio (≥ 3 mio safe-harbor). Surplus 8-6 = 2 mio EUR niet-aftrekbaar dit jaar → +500.000 EUR VenB (25%). De 2 mio EUR is overdraagbaar — in een latere goed jaar met EBITDA-ruimte kan het alsnog aftrekbaar zijn. Effect: cash-impact in slechte jaren, niet noodzakelijk permanente fiscale verlies. De 3 mio EUR safe-harbor beschermt KMO-vennootschappen — onder dat plafond geen beperking. Cumulatief met thin-cap-regime: meest-beperkende geldt.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Voorbeeld vennootschap X met EBITDA 30M en interest 20M — _cbn_</small>

## Rationale

🔗 Ratio legis: implementatie van OESO-BEPS-actie 4 + ATAD-richtlijn (EU 2016/1164) — anti-erosie van belastinggrondslag door overmatige schuldfinanciering. Logica: vennootschappen die >30% van hun economische winstcapaciteit (EBITDA) als rente betalen, zijn typisch overgekapitaliseerd via vreemd vermogen — soms gestuurd door fiscale optimalisatie (renteaftrek > dividendenfinanciering). De 30%-grens dwingt tot een evenwichtiger schuld-eigen-vermogensstructuur. Safe-harbor 3 mio EUR zorgt dat normale KMO-financiering buiten schot blijft. Onbeperkte overdracht (art. 194sexies) erkent dat de beperking 'timing'-effect heeft, niet 'definitief': een verlieslatend jaar mag niet structureel een vennootschap haar renteaftrek doen verliezen.

<small>📚 ATAD-richtlijn EU 2016/1164 — Considerans + art. 4 — _richtlijn_ · WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **AJ 2020 (inkomstenjaar 2019)** · basis: WIB92 art. 198/1 + art. 194sexies (overdracht) — ATAD-implementatie Wet 2 mei 2019

Geleidelijke verfijning via Circulaires (laatste 2023/C/8 van 12/01/2023). Voor multinationale groepen onder Pijler 2-regime: cumulatie met minimumbelasting nog te verfijnen.

**✅ Voor**
- 📖 Belgische vennootschappen met financieringskostensurplus boven 3.000.000 EUR safe-harbor — typisch holdings, private-equity-investeringsvennootschappen, vastgoedvennootschappen met hypothecaire schulden, en buitenlandse dochters van internationale groepen met intercompany-leningen.

**📋 Voorwaarden**
- 📖 Toepassings-stappen: (1) bereken netto-financieringskostensurplus = interestkosten - interestopbrengsten (per groep van vennootschappen op geconsolideerde basis, niet enkel statutair); (2) bereken fiscale EBITDA = belastbaar resultaat + financieringskostensurplus + afschrijvingen + waardeverminderingen + niet-aftrekbare elementen; (3) bepaal grensbedrag = MAX(30% × fiscale EBITDA ; 3.000.000 EUR); (4) is financieringskostensurplus > grensbedrag? Zo ja: surplus is niet-aftrekbaar (code 1262); (5) optioneel: interestaftrek-overeenkomst met groepslid (formulier 275 CDI bij aangifte).

**⛔ Uitsluitingen**
- 📖 Niet van toepassing op (art. 198/1 §6): (a) financiële ondernemingen (banken, verzekeraars, ICBE's); (b) alleenstaande vennootschap zonder verbonden ondernemingen (mits voldoet aan voorwaarden); (c) bepaalde grandfathered leningen aangegaan vóór 17/6/2016 — uitfasering tot 2024; (d) leningen aangegaan voor langetermijn-publieke-infrastructuurprojecten (specifieke uitsluiting).

**👍 Voordeel**
- 📖 Onbeperkte overdracht van niet-aftrekbaar surplus naar volgende jaren (art. 194sexies) → fiscale verlies is niet definitief. Interestaftrek-overeenkomst (art. 198/1 §4) laat groepen toe binnen-groep-optimalisatie. Safe-harbor van 3 mio EUR beschermt KMO's en middelgrote ondernemingen.

**⚠️ Risico**
- 🔗 Cash-impact in jaren met negatieve of lage EBITDA: zelfs als safe-harbor 3 mio bescherming biedt voor klein-segment, kunnen vastgoedvennootschappen of holdings ineens veel surplus krijgen. · Vergeten 275 CDI-formulier in te dienen bij gebruik interestaftrek-overeenkomst → overeenkomst niet geldig → groepsoptimalisatie verloren. · Cumulatie met thin-cap (art. 198 §1, 11°/1): meest-beperkende regel telt — beide kunnen tegelijk gelden voor verschillende delen.

## Bouwstenen

### 💡 Definitie financieringskostensurplus (art. 198/1 §2)  
_`begrip`_

📖 Financieringskostensurplus = positief verschil tussen interestkosten (rek 650 + economisch gelijkwaardige financiële kosten) en interestopbrengsten (rek 751 + financiële opbrengsten op vreemde valuta-derivaten gerelateerd aan financiering). Belangrijk: 'economisch gelijkwaardig' omvat ook impliciete rente in financial leases, factoring-kosten, financiële swap-componenten, etc. Voor groepen van vennootschappen: berekening gebeurt OP NIVEAU VAN DE BELGISCHE GROEP (alle groepsleden samen) — niet per individuele vennootschap. Een groep van vennootschappen die samen <3 mio EUR netto-interest hebben → safe-harbor — alle leden vol-aftrekbaar.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Definitie netto-interestkosten — _cbn_</small>

### 🧮 Fiscale EBITDA — eigen berekeningsformule  
_`formule`_

📖 Fiscale EBITDA ≠ boekhoudkundige EBITDA. Berekening:

Fiscale EBITDA = belastbaar resultaat (vóór art. 198/1-toepassing)
+ financieringskostensurplus (de te beperken last)
+ afschrijvingen + waardeverminderingen op materiële + immateriële vaste activa
+ andere niet-aftrekbare elementen (geheel of gedeeltelijk verworpen uitgaven, code 1240)

Het doel: maken dat de EBITDA-base voldoende groot is om reële economische winstcapaciteit te weerspiegelen, los van fiscale optimalisatie via aftrekken (DBI, innovatie, transfer-pricing). Belastbaar resultaat = na DBI + innovatie-aftrek + risicokapitaal — maar VÓÓR het EBITDA-mechanisme zelf (cirkelvermijding).

<small>📚 WIB92 — art. 198/1 — _wettekst_</small>

### 📏 Grensbedrag (art. 198/1 §3)  
_`drempel`_

📖 Grensbedrag = MAX( 30% × fiscale EBITDA ; 3.000.000 EUR safe-harbor ). Voor een vennootschap met fiscale EBITDA = 5 mio EUR: 30% × 5 mio = 1,5 mio → safe-harbor 3 mio is groter → grensbedrag = 3 mio. Voor vennootschap met EBITDA 20 mio: 30% × 20 = 6 mio > 3 mio → grensbedrag = 6 mio. Voor een verlieslatende vennootschap (negatieve EBITDA): 30% × negatief = negatief → safe-harbor 3 mio is hoger → grensbedrag = 3 mio.

<small>📚 WIB92 — art. 198/1 — _wettekst_</small>

### ⚙️ Interestaftrek-overeenkomst groepsleden (art. 198/1 §4)  
_`mechanisme`_

📖 Wanneer een groepslid X niet-aftrekbaar surplus heeft EN een ander groepslid Y onbenutte aftrekcapaciteit heeft (grensbedrag > financieringskostensurplus), kunnen X en Y een interestaftrek-overeenkomst sluiten waarbij Y een deel van zijn grensbedrag aan X overdraagt. Effect: X kan dat extra aftrekcapaciteit gebruiken om meer rente af te trekken; Y verliest evenredig zijn marge. De overeenkomst MOET vóór afsluiting boekjaar gesloten zijn EN het formulier 275 CDI moet bij de aangifte worden gevoegd. Optioneel: Y kan vergoeding eisen van X (boekhoudkundig + fiscaal verwerkt — zie CBN 2020/06). Zonder vergoeding: louter fiscale verrichting buiten boekhouding.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Interestaftrek-overeenkomst met en zonder vergoeding — _cbn_</small>

### 📜 Onbeperkte overdracht naar volgende jaren (art. 194sexies)  
_`regel`_

📖 Niet-aftrekbaar financieringskostensurplus van boekjaar N kan ONBEPERKT in tijd worden overgedragen naar volgende boekjaren — geen verjaring. In een latere periode met EBITDA-ruimte wordt het overgedragen surplus alsnog aftrekbaar (volgens jaar-volgorde, FIFO-principe). Boekhoudkundig: GEEN balans-opname als actieve belastinglatentie (CBN-advies 2020/06) — fictief karakter van de 'vordering op de overheid'. Wel in toelichting jaarrekening vermelden indien materieel.

<small>📚 WIB92 — art. 194sexies — _wettekst_ · CBN-advies 2020/06 — Statutaire jaarrekening — geen actieve belastinglatentie — _cbn_</small>

### ↪️ Uitsluitingen (art. 198/1 §6)  
_`uitzondering`_

📖 EBITDA-regel NIET van toepassing op: (1) financiële ondernemingen (banken, verzekeraars, ICBE's — opgesomd in §6, 1°-13°); (2) 'standalone' vennootschap zonder verbonden ondernemingen, zonder vaste inrichting buiten België, zonder deel uit te maken van groep; (3) langetermijn-publieke-infrastructuur-leningen voor projecten in EU-publiek belang; (4) grandfathered leningen aangegaan vóór 17/6/2016 — uitgefaseerd tot 2024 (geleidelijke uitsluiting); (5) bepaalde patrimoniumvennootschappen onder voorwaarden.

<small>📚 WIB92 — art. 198/1 — _wettekst_</small>

### ⚙️ Verhouding tot thin-cap-regime (art. 198 §1, 11°/1)  
_`mechanisme`_

🔗 Thin-cap (art. 198 §1, 11°/1): rentebetalingen aan verbonden onderneming in laag-belaste jurisdictie (of belastingparadijs) boven 5× (reserves + kapitaal)-ratio worden verworpen. Werkt PARALLEL met EBITDA-regel art. 198/1. Bij cumulatie: meest-beperkende regel telt. Praktisch: voor multinationale groepen met intercompany-leningen geldt vaak thin-cap (regeert intercompany-rente) + EBITDA (regeert totale rente). Beide regimes naast elkaar testen, NIET gecumuleerd verworpen.

<small>📚 WIB92 — art. 198 — _wettekst_ · WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 ATAD thin-cap 30%-EBITDA / 3M€ — basisgeval 📖

_Belgische vastgoedvennootschap met hypothecaire schuld. Fiscaal resultaat (vóór art. 198/1): 4.000.000 EUR. Interestkosten: 5.000.000 EUR. Interestopbrengsten: 200.000 EUR. Afschrijvingen: 3.000.000 EUR. Geen verbonden buitenlandse vennootschap, geen thin-cap-effect. Geen interestaftrek-overeenkomst._

**Berekening:**
- Stap 1 — Financieringskostensurplus = 5.000.000 - 200.000 = 4.800.000 EUR.
- Stap 2 — Fiscale EBITDA = belastbaar resultaat 4.000.000 + financieringskostensurplus 4.800.000 + afschrijvingen 3.000.000 = 11.800.000 EUR.
- Stap 3 — Grensbedrag = MAX(30% × 11.800.000 ; 3.000.000) = MAX(3.540.000 ; 3.000.000) = 3.540.000 EUR.
- Stap 4 — Surplus boven grensbedrag = 4.800.000 - 3.540.000 = 1.260.000 EUR → niet-aftrekbaar (code 1262).
- Stap 5 — Effect op belastbare grondslag: + 1.260.000 EUR → VenB 25% = +315.000 EUR extra belasting.
- Stap 6 — Overdracht: 1.260.000 EUR overdraagbaar naar volgend boekjaar (art. 194sexies). In jaar N+1 met betere EBITDA wordt het alsnog aftrekbaar.
- Stap 7 — Vergelijking: zonder ATAD-regel zou volledige 4.800.000 aftrekbaar geweest zijn → verschil 315.000 EUR cash-impact.

→ **Resultaat**: ATAD-EBITDA-regel veroorzaakt 315.000 EUR extra VenB voor deze vennootschap. Overdraagbaar voor latere recuperatie.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Safe-harbor 3M€ — KMO-vastgoedvennootschap 📖

_Belgische KMO-vastgoedvennootschap. Fiscaal resultaat 500.000 EUR. Interestkosten 2.500.000 EUR. Interestopbrengsten 100.000 EUR. Afschrijvingen 500.000 EUR._

**Berekening:**
- Stap 1 — Financieringskostensurplus = 2.500.000 - 100.000 = 2.400.000 EUR.
- Stap 2 — Fiscale EBITDA = 500.000 + 2.400.000 + 500.000 = 3.400.000 EUR.
- Stap 3 — Grensbedrag = MAX(30% × 3.400.000 ; 3.000.000) = MAX(1.020.000 ; 3.000.000) = 3.000.000 EUR (safe-harbor).
- Stap 4 — Surplus 2.400.000 EUR < grensbedrag 3.000.000 EUR → volledig aftrekbaar.
- Stap 5 — Geen code 1262, geen extra VenB door ATAD-regel.

→ **Resultaat**: Safe-harbor 3 mio beschermt deze KMO. Belangrijke beleidsmaatregel om gewone vastgoedvennootschappen onder controle van bureaucratisch ATAD-regime te houden.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Interestaftrek-overeenkomst tussen groepsleden (CBN 2020/06) 📖

_Groep met vennootschap X (financieringskostensurplus 20.000.000 EUR, fiscale EBITDA 30.000.000 EUR → grensbedrag 9.000.000 → niet-aftrekbaar surplus 11.000.000 EUR) en vennootschap Y (fiscale EBITDA 100.000.000, financieringskostensurplus 10.000.000 → grensbedrag 30.000.000 → niet-benutte aftrekcapaciteit 20.000.000 EUR). Y is bereid 11.000.000 over te dragen aan X._

**Berekening:**
- Stap 1 — Zonder overeenkomst: X verwerpt 11.000.000 EUR (code 1262) → +2.750.000 EUR VenB.
- Stap 2 — X en Y sluiten interestaftrek-overeenkomst vóór 31/12: Y draagt 11.000.000 EUR van zijn niet-benutte aftrekcapaciteit over.
- Stap 3 — Met overeenkomst: X krijgt nieuw grensbedrag 9.000.000 + 11.000.000 = 20.000.000 EUR → financieringskostensurplus 20.000.000 valt nu volledig binnen → geen code 1262.
- Stap 4 — Y's grensbedrag wordt verminderd: 30.000.000 - 11.000.000 = 19.000.000 EUR. Y's eigen financieringskostensurplus 10.000.000 < 19.000.000 → nog steeds vol-aftrekbaar.
- Stap 5 — Optioneel: X betaalt vergoeding aan Y (bv. 25% × 11.000.000 = 2.750.000 EUR — gelijk aan VenB-besparing). Boekhoudkundig: 6701 X / 7501 Y. Fiscale gevolgen volgens normale regels.
- Stap 6 — Zonder vergoeding: louter fiscale verrichting; X verwerkt belastingvermindering bij afsluiting; Y heeft geen boekhoudkundige impact (CBN-advies 2020/06).
- Stap 7 — Formulier 275 CDI bij aangifte voegen — verplicht voor groepsoptimalisatie.

→ **Resultaat**: Groepsoptimalisatie via interestaftrek-overeenkomst: 2.750.000 EUR VenB-besparing voor X — financieel substantieel. Cruciaal: formulier 275 CDI tijdig indienen + economische rationale van overeenkomst documenteren.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Voorbeeld X+Y — _cbn_</small>

## Valkuilen

### ⚠️ Boekhoudkundige EBITDA verwarren met fiscale EBITDA

**Verkeerde assumptie**: Fiscale EBITDA = boekhoudkundige EBITDA (omzet - cost of goods sold - personeelskosten - andere bedrijfskosten + afschrijvingen).

**Kernpunt**: Fiscale EBITDA heeft een ANDERE BEREKENING dan boekhoudkundige EBITDA. Formule: belastbaar resultaat (na DBI/innovatie-aftrek/risicokapitaal, vóór art. 198/1) + financieringskostensurplus + afschrijvingen + waardeverminderingen + niet-aftrekbare elementen. Voor vennootschappen met substantiële DBI-aftrek of innovatie-aftrek wijkt de fiscale EBITDA fors af. Altijd terugrekenen van belastbaar resultaat, NIET van boekhoudkundige cijfer.

<small>📚 WIB92 — art. 198/1 — _wettekst_</small>

### ⚠️ Per-vennootschap-berekening voor groepen

**Verkeerde assumptie**: Elke vennootschap berekent haar eigen 30%-grens.

**Kernpunt**: Voor 'groepen van vennootschappen' (art. 198/1 §6, 14° — definitie strikt) wordt de berekening op groepsniveau gedaan, niet per individuele vennootschap. Een interestaftrek-overeenkomst is een formele manier om binnen-groep-allocatie te wijzigen — maar de TOTALE GRENS van de groep verandert niet. Zonder overeenkomst: de toewijzing volgt de wettelijke standaard-formule per vennootschap met groepscorrectie.

<small>📚 WIB92 — art. 198/1 — _wettekst_</small>

### ⚠️ Vergeten formulier 275 CDI bij interestaftrek-overeenkomst

**Verkeerde assumptie**: Een gewone interestaftrek-overeenkomst tussen groepsleden volstaat — fiscus zal dat accepteren via 'goede trouw'.

**Kernpunt**: Art. 198/1 §4 + Circulaire 2023/C/8: formulier 275 CDI MOET worden gevoegd bij de VenB-aangifte van zowel de overdragende als de ontvangende vennootschap. Zonder formulier: overeenkomst is niet rechtsgeldig fiscaal → overdracht geweigerd → vennootschap X behoudt zijn niet-aftrekbare surplus. Strikte voorwaarde — geen herstel mogelijk na aangiftetermijn.

<small>📚 Circulaire 2023/C/8 — 12/01/2023 — _circulaire_ · aangifte-VenB-2025-verworpen-uitgaven — Code 1262 + 275 CDI — _aangifte_</small>

### ⚠️ Actieve belastinglatentie voor overgedragen surplus boeken

**Verkeerde assumptie**: Niet-aftrekbaar surplus = actieve belastinglatentie → opnemen op de balans.

**Kernpunt**: CBN-advies 2020/06 verbiedt expliciet de opname van actieve belastinglatentie voor overgedragen surplus — het 'fictieve karakter' van de vordering tegen de overheid + voorzichtigheidsbeginsel. Wel: vermelding in toelichting indien materieel. Belangrijk voor jaarrekening-controle.

<small>📚 CBN-advies 2020/06 — Statutaire jaarrekening — geen actieve belastinglatentie — _cbn_</small>

## Accountant-perspectieven

### Multinationale of grote Belgische groep

_De accountant van een groot of multinationale groep met substantiële interestkosten._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijkse EBITDA-test  
_`stap`_

🔗 Bij elke VenB-aangifte: (1) bereken netto-financieringskostensurplus per groep; (2) bereken fiscale EBITDA — let op verschil met boekhoudkundige cijfer; (3) bepaal grensbedrag (max 30% × EBITDA óf 3 mio); (4) bepaal niet-aftrekbaar deel; (5) zoek binnen groep naar onbenutte aftrekcapaciteit → interestaftrek-overeenkomst opstellen vóór 31/12; (6) formulier 275 CDI bij beide aangiftes voegen; (7) tracer overgedragen niet-aftrekbaar surplus voor latere jaren (FIFO). Documentatie: berekeningsblad + ondertekende overeenkomst + 275 CDI.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · WIB92 — art. 194sexies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij leveraged acquisition / vastgoedstructuur  
_`vuistregel`_

🔗 Bij grote schuldgefinancierde transacties (PE-acquisitions, vastgoedstructures, holdings): vooraf ATAD-impact doorrekenen. Vuistregel: hou financieringskostensurplus < 30% van projecterende EBITDA + 3 mio buffer. Indien onmogelijk: groepsstructuur evalueren — kan een onbeperkt-EBITDA-zustervennootschap een interestaftrek-overeenkomst aanbieden? Voor zuiver-vastgoedportfolio: thin-cap eveneens analyseren. Voor multinationale leveraged buyouts: pre-acquisitiedeal-modelling essentieel.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ Thin-cap-regime (5:1 schuld/EV — oudere parallel-regel, niet uitgedoofd) → [[thin-cap-regime]] _(mag-verwijzen)_
- ↪ ATAD-richtlijn algemeen kader (anti-erosie + 5 pijlers) → [[atad-richtlijn]] _(mag-verwijzen)_
- → Belastbare grondslag VenB (cascade) → [[belastbare-grondslag-vennootschapsbelasting]] _(moet-verwijzen)_
- → Verworpen uitgaven (code 1262) → [[verworpen-uitgaven]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]]
- [[atad-richtlijn]] — ATAD-actie 4 (interest limitation rule) — geïmplementeerd in art. 198/1 sinds AJ 2020.
### `vergelijkbaar_met`
- [[thin-cap-regime]]
    - **Gelijkenissen**:
        - Beide beperken renteaftrek op intercompany-leningen
        - Beide gelden naast elkaar (meest-beperkende geldt)
        - Beide gedragen zich als VU (code 1211 thin-cap; code 1262 EBITDA)
    - **Verschillen**:
        - Thin-cap: 5×(reserves+kapitaal)-ratio op intercompany rente aan laag-belaste verbonden onderneming
        - EBITDA: 30%-EBITDA-grens + 3M safe-harbor op TOTALE netto-financieringskosten van de groep
        - Thin-cap = oudere regel, gericht op grensoverschrijdend intercompany; EBITDA = ATAD-implementatie, breder toepassingsgebied
    - ⚠️ **Verwarringsrisico**: Studenten verwarren beide regimes systematisch. Onthoud: thin-cap = intercompany + balansratio; EBITDA = totaal + winstratio.
### `triggert`
- [[verworpen-uitgaven]] — Code 1262 in vak Verworpen uitgaven — niet-aftrekbaar financieringskostensurplus.
