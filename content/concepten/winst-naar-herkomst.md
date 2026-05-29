---
title: "Winst naar herkomst"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.V
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/winst-naar-herkomst.json"
---

_Procedure_ · ook: winst-toerekening VI · profit attribution · verdeling resterend resultaat volgens oorsprong

## Definitie

Winst naar herkomst is de techniek om het totale resultaat van een onderneming met activiteiten in meerdere landen op te splitsen volgens de plaats waar elk deel werd voortgebracht. Art. 7 OESO-modelverdrag legt de basisregel: aan een vaste inrichting (VI) wordt de winst toegerekend die zij zou behalen als zij een afzonderlijke en onafhankelijke onderneming was die dezelfde of soortgelijke activiteiten uitoefent onder dezelfde of soortgelijke omstandigheden (separate-entity-fictie). In de Belgische aangifte VenB wordt het resterend resultaat verdeeld in drie kolommen: Belgisch / niet-bij-verdrag-vrijgesteld / bij-verdrag-vrijgesteld (art. 206/4 WIB92, aangiftecode 1431 PN).

<small>📖 OESO-modelverdrag — art. 7 — _modelverdrag_ · WIB92 — art. 206/4 — _wettekst_ · Aangifte VenB 2025 — uiteenzetting winst — code 1431 PN — _aangifte_</small>

## Substantie

De toerekening bepaalt welk land welk stuk winst mag belasten — en daarmee hoeveel belasting de onderneming over haar wereldwinst betaalt. Hoe meer winst aan een hoge-tarief-VI wordt toegerekend, hoe hoger de totale belastingdruk; hoe meer aan een laag-tarief-VI of vrijgestelde VI, hoe lager. Dit maakt winsttoerekening een centraal twistpunt tussen fisci: elke fiscus heeft een eigen belang in de toerekenings-methodologie. De Authorized OECD Approach (AOA, 2010) standaardiseert dit door een tweestappentest: (1) functional and factual analysis — welke functies, activa en risico's draagt de VI? (2) arm's length-prijzen toepassen op de interne dealings tussen VI en hoofdhuis, alsof het twee onafhankelijke ondernemingen waren.

<small>🔗 OESO-modelverdrag — art. 7 §2 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De rationale is fiscale neutraliteit tussen organisatievormen: een Belgische groep moet voor dezelfde economische realiteit ongeveer dezelfde belasting betalen, of ze nu in het buitenland actief is via (a) een VI (filiaal) of (b) een dochtervennootschap. Bij dochtervennootschap geldt transfer pricing (art. 9 OESO-MV, art. 185 §2 WIB92); bij VI geldt winst-naar-herkomst (art. 7 OESO-MV). De AOA brengt die twee regimes methodologisch gelijk: dezelfde arm's length-principes, dezelfde functional analysis. Resultaat: organisatievorm-keuze is fiscaal neutraal — de winst landt waar de economische substantie zit, niet waar het juridische label staat.

<small>🔗 OESO-modelverdrag — art. 7 + art. 9 — _modelverdrag_ · WIB92 — art. 185 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: OESO-MV art. 7 (post-2010 AOA-versie + pre-AOA voor oudere verdragen); WIB92 art. 206/4 (verdeling resterend resultaat) + art. 185/1 (exit-winst bij overdracht aan vrijgestelde VI) + art. 185 §2 (TP-correctie)

Toepasselijkheid hangt af van het concrete DBV: oudere Belgische verdragen kennen art. 7 nog in pre-AOA-versie (relevante invloed: indirecte verdeelmethodes blijven toegelaten). AOA is geldig waar de 2010-OESO-versie is geïmplementeerd of waar het verdrag bewust de nieuwe terminologie overneemt.

**✅ Voor**
- 📖 Belgische vennootschap met een buitenlandse VI: jaarlijks winst toerekenen per land, in de aangifte VenB verdelen volgens code 1431 PN (drie kolommen).
- 📖 Buitenlandse vennootschap met Belgische inrichting (BNI): toerekening van winst aan de Belgische inrichting volgens art. 7 DBV + interne TP-regels.

**📋 Voorwaarden**
- 📖 Bestaan van een VI is een conditio sine qua non — zonder VI geen toerekening, alle winst blijft in de woonstaat (art. 7 §1 OESO-MV).

**⚠️ Risico**
- 🔗 Onder- of overtoerekening leidt tot dubbele belasting (beide staten claimen) of dubbele vrijstelling (geen van beide belast). Mutual Agreement Procedure (MAP, art. 25 OESO-MV) kan corrigeren, maar duurt jaren. Documentatie van functional analysis bij elke interne dealing is essentieel ter ondersteuning van het transfer-pricing dossier.

## Bouwstenen

### ✴️ Separate-entity-fictie (art. 7 §2 OESO-MV)

De VI wordt bij toerekening behandeld alsof zij een afzonderlijke en onafhankelijke onderneming is, die dezelfde of soortgelijke werkzaamheden uitoefent onder dezelfde of soortgelijke omstandigheden, en die geheel onafhankelijk handelt met de onderneming waarvan zij een VI is. Concrete gevolgen: interne dealings (goederen-overdracht, dienstverlening, intra-bedrijfslening, IP-licenties tussen hoofdhuis en VI) krijgen arm's length-prijzen, alsof het transacties met derden waren. Kosten van leiding en algemene beheer worden aftrekbaar voor zover ze redelijk aan de VI toerekenbaar zijn (art. 7 §3).

<small>📖 OESO-modelverdrag — art. 7 §2 + §3 — _modelverdrag_ · DBV België-Nederland 2001 — art. 7 §2 — _modelverdrag_</small>

### ⚙️ Authorized OECD Approach (AOA) — tweestappentest

AOA (OECD 2010-rapport) structureert de toerekening in twee stappen. Stap 1 — functional and factual analysis: identificeer welke significante people functions (SPF) in de VI worden uitgeoefend; ken op basis daarvan economische eigendom van activa, dragen van risico's en uitvoering van functies toe aan de VI. Stap 2 — arm's length pricing: pas de OECD-Transfer Pricing Guidelines toe op de identified dealings tussen VI en hoofdhuis. AOA past zo dezelfde methodologie toe als bij verbonden ondernemingen — fiscaal-neutraal tussen VI- en dochterstructuur.

<small>🔗 OESO-modelverdrag — art. 7 (2010-versie) — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Indirecte vs directe toerekenings-methode

Twee methodes bestaan. Directe methode (default AOA): bouwt voor de VI een eigen P&L op alsof het een aparte entiteit was, met interne facturen tussen VI en hoofdhuis aan arm's length-prijzen. Indirecte methode (art. 7 §4 oude OESO-MV, nog in pre-2010-verdragen): de totale winst van de onderneming wordt verdeeld via een gebruikelijke verdeelsleutel (omzet, kostenmassa, activa, personeel). De indirecte methode mag enkel als ze in dat land gebruikelijk is en het resultaat in lijn ligt met de §2-beginselen. Sinds AOA wordt directe methode aanbevolen — indirecte enkel waar verdrag pre-2010 is.

<small>📖 OESO-modelverdrag (oude versie) — art. 7 §4 — _modelverdrag_ · DBV België-Nederland 2001 — art. 7 §4 — _modelverdrag_</small>

### 📜 Drie oorsprong-categorieën in aangifte (art. 206/4)

Het totaal resterend resultaat (na art. 206/1-206/3-correcties) wordt verdeeld in drie categorieën: (1) Belgisch resterend resultaat — in België behaald; (2) Niet-bij-verdrag-vrijgesteld — in het buitenland behaald maar niet vrijgesteld krachtens een DBV (bv. bouwwerf < 12 maanden, geen VI, of land zonder DBV); (3) Bij-verdrag-vrijgesteld — buitenlandse VI-winst die door een DBV is vrijgesteld in België. Verliezen worden vóór de splitsing aangerekend volgens een specifieke volgorde (art. 206/4, tweede lid).

<small>📖 WIB92 — art. 206/4 — _wettekst_</small>

### 📜 Verlies-aanrekenings-volgorde (art. 206/4, tweede lid)

Verliezen worden vóór de driedeling aangerekend in volgorde: (a) verliezen geleden in een verdragsland (bij-verdrag-vrijgesteld) — eerst op bij-verdrag-vrijgestelde winst, daarna niet-bij-verdrag, ten slotte Belgische winst; (b) verliezen in een niet-verdragsland — eerst op niet-bij-verdrag-winst, dan Belgische winst; (c) Belgische verliezen — eerst op Belgische winst, dan op niet-bij-verdrag-winst. Voor (a) geldt een onherroepelijke-keuze-vereiste: enkel als de belastingplichtige in een bijlage bij zijn aangifte het land, het bedrag en het belastbare tijdperk vermeldt, mag een verdragsverlies tegen Belgische of niet-bij-verdrag-winst worden aangerekend.

<small>📖 WIB92 — art. 206/4, tweede lid — _wettekst_</small>

### 📜 Exit-winst bij overdracht actief naar vrijgestelde VI (art. 185/1)

Wanneer een Belgische vennootschap een actief overdraagt van haar hoofdhuis naar een buitenlandse VI waarvan de winst in België is vrijgesteld door DBV, wordt het positieve verschil tussen werkelijke waarde en (afgeschreven) aanschaffingswaarde als winst belast in België (art. 185/1 WIB92). Doel: latente meerwaarden niet 'weglopen' naar het vrijgestelde regime zonder ooit in BE te zijn belast. Praktijk: bij verplaatsing van machines, IP-rechten of goodwill naar een vrijgestelde VI moet een exit-tax-berekening worden uitgevoerd.

<small>📖 WIB92 — art. 185/1 — _wettekst_</small>

### ⚙️ Interne dealings VI ↔ hoofdhuis aan arm's length

Onder AOA worden interne dealings (geen 'transacties' want dezelfde rechtspersoon) gewaardeerd alsof het transacties tussen onafhankelijke ondernemingen waren. Typische dealings: levering goederen hoofdhuis → VI; dienstverlening (managementdiensten, IT-support); interne 'lening' (allocatie kapitaal); IP-licentie. Arm's length-prijs bepaald via OECD-Transfer-Pricing-Guidelines-methodes (CUP, resale-price, cost-plus, TNMM, profit-split). Geen aparte facturering nodig — wel documentatie + interne accounting die de dealings traceerbaar maakt.

<small>🔗 OESO-modelverdrag — art. 7 §2 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Geen winst op loutere aankoop door VI (art. 7 §5 oude OESO-MV)

Onder de pre-2010 OESO-MV-versie (art. 7 §5) werd aan een VI geen winst toegerekend op grond van loutere aankoop van goederen of koopwaar voor de onderneming. Deze regel staat in oudere Belgische verdragen (bv. DBV BE-NL 2001 art. 7 §5). De 2010-OESO-MV-versie heeft §5 geschrapt — onder AOA krijgt de aankoopfunctie wél een arm's length-marge als zij significant people functions vereist. Bij gebruik van een DBV altijd nakijken welke versie van art. 7 erin staat.

<small>📖 DBV België-Nederland 2001 — art. 7 §5 — _modelverdrag_</small>

### 📜 Consistentie van methode van jaar tot jaar

De winst-toerekening aan een VI wordt jaar na jaar volgens dezelfde methode bepaald, tenzij er een goede en genoegzame reden bestaat om hiervan af te wijken (art. 7 §6 oude OESO-MV; opgenomen in vele Belgische verdragen). Doel: stabiliteit en voorspelbaarheid, voorkomen dat ondernemingen jaarlijks de methode kiezen die best uitkomt. Wijziging vereist motivering tegenover beide fisci.

<small>📖 DBV België-Nederland 2001 — art. 7 §6 — _modelverdrag_</small>

## Voorbeelden

> [!example]- Aurelia Holding NV met productie-VI in Frankrijk
> _Aurelia Holding NV (BE) heeft naast haar hoofdhuis in Antwerpen een productie-VI in Lyon waar machines staan en 25 werknemers werken. De VI produceert componenten, levert ze intern aan het BE-hoofdhuis dat ze verwerkt en wereldwijd verkoopt. Totaal resultaat groep: 5.000.000 EUR._
>
> 1. Stap 1 — functional analysis VI Lyon: significant people functions = productie-management + kwaliteitscontrole; activa = machines + voorraad grondstoffen; risico's = productiekosten-volatiliteit, kwaliteitsclaims.
> 2. Stap 2 — interne dealing: VI levert componenten aan hoofdhuis. Arm's length-prijs = kostprijs Lyon × (1 + cost-plus-marge 8 %) — getoetst aan vergelijkbare onafhankelijke producenten.
> 3. Stap 3 — VI-resultaat: omzet (interne factuur aan hoofdhuis) − productiekosten − afschrijvingen − allocated overhead = bv. 1.200.000 EUR.
> 4. Stap 4 — BE-aangifte code 1431 PN: 1.200.000 EUR in kolom 'bij-verdrag-vrijgesteld'; 3.800.000 EUR in kolom 'Belgisch'.
> 5. Stap 5 — Belgische belasting alleen op 3.800.000 EUR; 1.200.000 EUR telt mee voor het tariefdeel maar wordt vrijgesteld.
>
> → **Resultaat**: Door correcte AOA-toerekening: France belast 1.200.000 EUR, België belast 3.800.000 EUR. Geen dubbele belasting, geen dubbele vrijstelling.
>
> <small>🔗 DBV België-Frankrijk — art. 7 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- VI lijdt verlies — aanrekening op Belgische winst
> _Zelena Bio NV (BE) heeft een VI in Spanje (DBV-vrijgesteld). In jaar N: BE-winst 800.000 EUR; verlies VI Spanje 200.000 EUR._
>
> **Berekening:**
>
> - Bij-verdrag-vrijgestelde verliezen (a-regel) → eerst tegen vrijgestelde winst (geen), dan niet-bij-verdrag-winst (geen), dan Belgische winst.
> - Spelregel art. 206/4: aanrekening van Spaans verlies op BE-winst MAG, mits onherroepelijke vermelding in bijlage van land + bedrag + belastbaar tijdperk.
> - Indien gekozen: BE-belastbare grondslag = 800.000 − 200.000 = 600.000 EUR.
> - Pas op: in latere jaren wordt Spaanse winst belast in BE tot recapture van het verlies (art. 185 §3 WIB92 ~equivalent — verlies-recapture-regel).
>
> → **Resultaat**: Door bewuste keuze (onherroepelijk) vermindert BE-belastbare grondslag in jaar N met 200.000 EUR, maar geldt recapture in latere winstjaren van Spanje.
>
> <small>🔗 WIB92 — art. 206/4 — _wettekst_</small>

> [!example]- Overdracht IP naar vrijgestelde VI — exit-tax art. 185/1
> _BE-vennootschap draagt een merk (boekwaarde 100.000 EUR, marktwaarde 800.000 EUR) over aan haar Cypriotische VI waarvan de winst onder DBV BE-Cyprus is vrijgesteld._
>
> _Belastbare meerwaarde bij overdracht naar vrijgestelde VI_
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | VI-Cyprus (interne dealing) — fictieve werkelijke waarde | 800.000 |  |
> | Merk (boekwaarde) |  | 100.000 |
> | Meerwaarde (art. 185/1 WIB92 — belastbaar in BE) |  | 700.000 |
>
> De 700.000 EUR latente meerwaarde wordt nu in België belast als VenB-winst (art. 185/1) — voorkomt dat de meerwaarde geruisloos naar het vrijgestelde regime verdwijnt. Cyprus gebruikt vervolgens 800.000 EUR als afschrijvingsbasis.
>
> <small>📖 WIB92 — art. 185/1 — _wettekst_</small>

## Valkuilen

> [!warning]- Geen VI = toch winst toerekenen aan land van werkzaamheid
> **Verkeerde assumptie**: Studenten denken: 'er was activiteit in land X dus we moeten daar winst toerekenen, ook al is er geen VI'.
>
> **Kernpunt**: Art. 7 §1 is duidelijk: alleen bij bestaan van een VI mag het andere land winst belasten. Zonder VI = alle winst in de woonstaat, ook al is er feitelijke buitenlandse activiteit (export, korte werven < 12 maanden, occasionele dienstreizen). De winst-naar-herkomst-procedure veronderstelt steeds een vooraf bevestigde VI-status.
>
> <small>📖 OESO-modelverdrag — art. 7 §1 — _modelverdrag_</small>

> [!warning]- VI-resultaat = boekhoudkundig resultaat van filiaal-administratie
> **Verkeerde assumptie**: Studenten gebruiken kritiekloos het lokale boekhoudresultaat van het buitenlandse filiaal als VI-winst.
>
> **Kernpunt**: Filiaal-boekhouding houdt zelden de AOA-correcties bij (arm's length intra-dealings, allocated overhead, kapitaalvergoeding op de fictieve activa). Voor fiscale toerekening moet je de boekhouding herrekenen met AOA-correcties — vooral interne dealings aan markt-prijs en correcte allocatie van head-office-kosten.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Verlies VI zonder meer aanrekenen op BE-winst
> **Verkeerde assumptie**: Een verlies in een buitenlandse vrijgestelde VI wordt automatisch op BE-winst aangerekend.
>
> **Kernpunt**: Art. 206/4 vereist onherroepelijke keuze + bijlage met land/bedrag/tijdperk. Zonder die keuze wordt het verlies enkel binnen de vrijgestelde-kolom verrekend (= effectief verloren als er geen toekomstige vrijgestelde winst is). De keuze brengt bovendien een recapture-verplichting mee in latere winstjaren.
>
> <small>📖 WIB92 — art. 206/4, laatste lid — _wettekst_</small>

> [!warning]- Pre-2010 art. 7 toepassen volgens AOA-methodologie
> **Verkeerde assumptie**: Studenten passen AOA toe op een verdrag dat nog de oude art. 7-versie bevat.
>
> **Kernpunt**: AOA geldt alleen bij verdragen met de 2010-OESO-MV-versie van art. 7 (of bewuste implementatie). Belgische verdragen pre-2010 (zoals DBV BE-NL 2001) hebben nog de oude formulering: indirecte methode toegelaten, geen winst op loutere aankoop, geen volledige separate-entity-fictie voor financieringskosten. Eerst nakijken welke versie het concrete DBV bevat.
>
> <small>🔗 DBV België-Nederland 2001 — art. 7 — _modelverdrag_</small>

## Accountant-perspectieven

### Belgische vennootschap met buitenlandse VI

_De accountant van een BE-vennootschap die elders een VI heeft — moet jaarlijks de toerekenings-exercise + aangifte-codes correct invullen._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijkse VI-attribution-exercise

Bij elke afsluiting: (1) verzamel VI-boekhouding lokaal; (2) identificeer interne dealings; (3) herwaardeer aan arm's length-prijzen volgens AOA; (4) alloceer head-office-overhead; (5) bepaal VI-resultaat netto; (6) splits totaal in art. 206/4-categorieën; (7) vul aangifte VenB code 1431 PN in (drie kolommen).

<small>🔗 WIB92 — art. 206/4 — _wettekst_ · Aangifte VenB 2025 — code 1431 PN — _aangifte_</small>

##### 📜 TP-dossier voor VI-dealings onderhouden

Houd een dossier bij: (a) functional analysis VI (SPF, activa, risico's); (b) gekozen TP-methode + benchmarking; (c) interne dealings-overzicht; (d) periodieke review bij significante veranderingen. Dit dossier dient zowel voor de Belgische fiscus als voor de buitenlandse fiscus bij MAP-procedure. Bij groepen > 50 mio EUR omzet: documentatie verplicht conform art. 321/4 e.v. WIB92 (Belgisch lokaal en master-dossier).

<small>🔗 WIB92 — art. 321/4 e.v. (TP-documentatieplicht) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij opstart VI: methodes vooraf vastleggen

Bij elke nieuwe VI: leg vooraf vast welke functies, activa en risico's bij de VI horen, hoe interne dealings worden geprijsd, en hoe head-office-kosten worden ge-alloceerd. Documenteer in een policy-document — eens een methode wordt toegepast, geldt de consistentie-eis (art. 7 §6 OESO-MV). Overweeg APA (Advance Pricing Agreement) bij grote groepen met materiële VI's.

<small>🔗 OESO-modelverdrag — art. 7 §6 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Vaste inrichting (basis) → [[vaste-inrichting]] _(moet-verwijzen)_
- → Transfer pricing (analoge methodologie) → [[transfer-pricing]] _(moet-verwijzen)_
- → Buitenlandse winst-en-verlies → [[buitenlandse-winst-en-verlies]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `vereist`
- [[vaste-inrichting]] — Geen VI = geen toerekening; winst-naar-herkomst start pas wanneer VI-status vaststaat.
### `triggert`
- [[buitenlandse-winst-en-verlies]] — Het resultaat van de toerekenings-exercise voedt de drie kolommen in de aangifte (Belgisch / niet-bij-verdrag / bij-verdrag).
- [[vrijstelling-met-progressievoorbehoud]] — De aan de VI toegerekende winst gaat in de aangifte naar de kolom 'bij-verdrag-vrijgesteld' en triggert progressievoorbehoud (art. 23A DBV).
### `vergelijkbaar_met`
- [[transfer-pricing]]
    - **Gelijkenissen**:
        - Beide passen het arm's length-beginsel toe
        - Beide gebruiken OECD-Transfer-Pricing-Guidelines-methodes (CUP, cost-plus, TNMM, profit-split)
        - Beide vereisen functional analysis (functies, activa, risico's)
    - **Verschillen**:
        - Transfer pricing: transacties tussen verbonden ondernemingen (verschillende rechtspersonen) — art. 9 OESO-MV, art. 185 §2 WIB92
        - Winst naar herkomst: 'interne dealings' binnen één rechtspersoon (hoofdhuis ↔ VI) — art. 7 OESO-MV
        - Bij TP zijn er echte facturen; bij VI-attribution is alles intern (geen separate juridische transactie)
    - ⚠️ **Verwarringsrisico**: Studenten denken dat winst-naar-herkomst hetzelfde is als TP. Methodologisch wel parallel, maar juridische basis en mechaniek verschillen — vooral relevant bij correcties en MAP.
### `beinvloed_door`
- [[dubbelbelastingverdrag]] — Het concrete DBV bepaalt welke versie van art. 7 (pre-2010 of post-AOA) van toepassing is, en welke methode (directe/indirecte) toegelaten is.
